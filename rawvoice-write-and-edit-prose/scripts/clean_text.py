#!/usr/bin/env python3
"""Conservative hygiene for user-authored Latin-script prose and Markdown.

This is not an AI-watermark detector. It strips specific unwanted controls and
normalizes unusual whitespace while preserving code spans, emojis, and most
non-Latin writing. Python 3.10+, stdlib only.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import sys
import unicodedata

# Unwanted invisible artifacts in mostly Latin prose. Do NOT indiscriminately
# remove ZWJ/ZWNJ, variation selectors, bidi controls, or combining accents.
REMOVABLE = {
    "\u200b": "zero-width space",
    "\u2060": "word joiner",
    "\u00ad": "soft hyphen",
    "\ufeff": "byte-order mark / zero-width no-break space",
}
SPACE_NAMES = {
    "\u00a0": "no-break space", "\u1680": "ogham space mark",
    "\u2000": "en quad", "\u2001": "em quad", "\u2002": "en space",
    "\u2003": "em space", "\u2004": "three-per-em space",
    "\u2005": "four-per-em space", "\u2006": "six-per-em space",
    "\u2007": "figure space", "\u2008": "punctuation space",
    "\u2009": "thin space", "\u200a": "hair space",
    "\u202f": "narrow no-break space", "\u205f": "medium mathematical space",
    "\u3000": "ideographic space",
}
# Log rather than remove controls that may be necessary for other languages.
REVIEW = {
    "\u200c": "zero-width non-joiner",
    "\u200d": "zero-width joiner (often required in emoji / scripts)",
    "\u200e": "left-to-right mark", "\u200f": "right-to-left mark",
    "\u202a": "left-to-right embedding", "\u202b": "right-to-left embedding",
    "\u202c": "pop directional formatting", "\u202d": "left-to-right override",
    "\u202e": "right-to-left override",
    "\u2066": "left-to-right isolate", "\u2067": "right-to-left isolate",
    "\u2068": "first strong isolate", "\u2069": "pop directional isolate",
    "\u034f": "combining grapheme joiner",
}


def latin_dominant(text: str) -> bool:
    letters = [c for c in text if unicodedata.category(c).startswith("L")]
    if not letters:
        return True
    latin = sum("LATIN" in unicodedata.name(c, "") for c in letters)
    return latin / len(letters) >= 0.85


def clean_prose(text: str) -> tuple[str, Counter[str], Counter[str]]:
    """Return (clean text, replacement counts, review-only counts)."""
    changes: Counter[str] = Counter()
    review: Counter[str] = Counter()
    safe_to_remove = latin_dominant(text)
    result: list[str] = []
    for char in text:
        if char in REMOVABLE:
            if safe_to_remove:
                changes[REMOVABLE[char]] += 1
                continue
            review[REMOVABLE[char] + " (preserved in non-Latin text)"] += 1
        elif char in SPACE_NAMES:
            if safe_to_remove:
                result.append(" ")
                changes[SPACE_NAMES[char]] += 1
                continue
            review[SPACE_NAMES[char] + " (preserved in non-Latin text)"] += 1
        elif char in REVIEW:
            review[REVIEW[char]] += 1
        result.append(char)
    return "".join(result), changes, review


def clean_text(text: str) -> tuple[str, Counter[str], Counter[str]]:
    """Clean ordinary text; leave fenced code and inline backtick spans untouched."""
    replacements: Counter[str] = Counter()
    review: Counter[str] = Counter()
    if "\r" in text:
        replacements["CRLF/CR line endings"] += text.count("\r")
        text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Protect a file BOM while enabling removal as a UTF-8 artifact.
    if text.startswith("\ufeff"):
        text = text[1:]
        replacements["leading byte-order mark"] += 1

    # Latin dominance is evaluated across document, not line-by-line, to avoid
    # erasing meaningful zero-width separators in languages that use them.
    safe_to_remove = latin_dominant(text)
    output = []
    in_fence = False
    fence_char, fence_width = "", 0
    for line in text.splitlines(keepends=True):
        body = line.rstrip("\n")
        newline = "\n" if line.endswith("\n") else ""
        stripped = body.lstrip(" ")
        if not in_fence and (stripped.startswith("```") or stripped.startswith("~~~")):
            delim = stripped[0]
            run = len(stripped) - len(stripped.lstrip(delim))
            if run >= 3:
                in_fence, fence_char, fence_width = True, delim, run
                output.append(line)
                continue
        elif in_fence and stripped.startswith(fence_char * fence_width):
            output.append(line)
            in_fence = False
            continue

        if in_fence:
            output.append(line)
            continue

        # Preserve single- and multi-backtick inline code. The pieces outside
        # inline code are cleaned; unbalanced opening backticks remain intact.
        pieces = []
        i = 0
        while i < len(body):
            if body[i] == "`":
                j = i
                while j < len(body) and body[j] == "`":
                    j += 1
                ticks = body[i:j]
                end = body.find(ticks, j)
                if end != -1:
                    pieces.append((body[i:end + len(ticks)], False))
                    i = end + len(ticks)
                    continue
            j = body.find("`", i)
            if j < 0:
                j = len(body)
            if j == i:  # unmatched backtick: preserve marker but move on
                j += 1
            pieces.append((body[i:j], True))
            i = j

        processed = []
        for part, is_prose in pieces:
            if not is_prose:
                processed.append(part)
                continue
            if safe_to_remove:
                cleaned, c, r = clean_prose(part)
                replacements.update(c)
                review.update(r)
                processed.append(cleaned)
            else:
                for char in part:
                    if char in REMOVABLE:
                        review[REMOVABLE[char] + " (preserved in non-Latin text)"] += 1
                    elif char in SPACE_NAMES:
                        review[SPACE_NAMES[char] + " (preserved in non-Latin text)"] += 1
                    elif char in REVIEW:
                        review[REVIEW[char]] += 1
                processed.append(part)
        output.append("".join(processed) + newline)

    return "".join(output), replacements, review


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="UTF-8 .txt or .md file")
    parser.add_argument("-o", "--output", type=Path, help="Output file; default stdout")
    parser.add_argument("--report", action="store_true", help="Print changes and review-only chars to stderr")
    parser.add_argument("--check", action="store_true", help="Return exit 1 if a cleanup change is needed; don't write")
    args = parser.parse_args()
    try:
        data = args.input.read_text(encoding="utf-8")
        cleaned, changes, review = clean_text(data)
        if args.report or args.check:
            print(f"Cleanup changes: {sum(changes.values())}", file=sys.stderr)
            for label, count in sorted(changes.items()):
                print(f"  {label}: {count}", file=sys.stderr)
            print(f"Review-only chars: {sum(review.values())}", file=sys.stderr)
            for label, count in sorted(review.items()):
                print(f"  {label}: {count}", file=sys.stderr)
        if args.check:
            return 1 if cleaned != data else 0
        if args.output:
            if args.output.resolve() == args.input.resolve():
                parser.error("Choose a different output file to preserve the original draft")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(cleaned, encoding="utf-8")
        else:
            sys.stdout.write(cleaned)
        return 0
    except (UnicodeError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
