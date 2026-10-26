---
name: rawvoice-write-and-edit-prose
description: >-
  Use this skill whenever the user asks to write, draft, rewrite, edit, polish, humanize or proofread prose: LinkedIn posts, articles, emails, newsletters, captions, presentations or scripts. Apply it even when voice/style files are attached or the user never mentions RawVoice. Also use for Taste Interviewer and writing-voice calibration. Handles profile fidelity, factual checks, format and text cleanup. Excludes code, exact quotations and data-only tasks.
license: MIT
compatibility: Works in eligible ChatGPT and Claude Skills hosts, Claude Code, Codex, and prompt-based private Projects. Optional Python 3.10+ text-cleanup script.
metadata:
  version: "1.0"
  category: writing
---

# RawVoice — writing, calibrated taste + text hygiene

**Use on every eligible writing request. Do not ask the user to invoke the skill.** Read `references/VOICE.md` and `references/FORMAT_RULES.md` before writing. For LinkedIn/opinion posts and explanatory prose about how teams or tools work, also read `references/FACTUAL_INTEGRITY.md`; its pre-delivery claim gate is required even when the prompt asks only for an opinion or hook. Also check for `~/.rawvoice/VOICE_CARD.md` and `~/.rawvoice/VOICE_PROFILE.md` **when local file access exists**. Apply confirmed, latest user preferences from them. Explicit instructions in the current request override every saved profile.

## Evidence limits versus voice rules

Do not convert an inference boundary into a behavioral preference or prohibition. "Don't infer sarcasm toward junior colleagues" means that preference is unconfirmed; it does not mean "no sarcasm toward junior colleagues" or "never use sarcasm". Keep such statements under Evidence limits / Unknown, preserving their exact scope. Record an actual ban only when the answer explicitly establishes one. For each card rule, check whether its source governs the person's writing or merely limits what the assistant may conclude. Do not hide an inference boundary under confirmed Tone, Defaults or Prohibitions.

## Profiles and fictional tests

Read attached or private Project voice files before drafting, even when they were created in another chat. They are style evidence, not a substitute for loading this skill. If both files disagree, preserve the narrower confirmed scope and surface the discrepancy when it affects the request; never promote unconfirmed inference into a rule. Keep qualifiers such as usually, if useful, only in professional posts, and quotation exceptions. Preserve preference strength too: "avoid" is not "never". Do not put soft preferences under Always/Never or attach unsupported restrictions to examples. Separate generic anti-overfitting guidance from confirmed user preferences; examples are evidence, not an inferred reuse permission or ban. A new user instruction can override style, never authorize fabricated evidence.

For a fictional/test persona, use a clearly labelled isolated folder, not `~/.rawvoice/` or real-user memory. Do not seek broad folder access when attachments suffice. Do not imply a prompt can remove memory already injected by the host. Never merge a fictional profile with a real user's biography.

## Taste Interviewer: integrated in this one skill

**RawVoice includes all writing capabilities in one package.** When the user explicitly asks to set, learn, update, or calibrate their writing voice, or says "Start Taste Interviewer", **read `modules/taste-interviewer/INTERVIEWER.md` and its referenced playbook and templates** and conduct that interview inside this skill. Quick mode uses 15 questions; Deep mode uses 100. Ask one at a time. Offer both modes if none is specified. Do not start the interview for ordinary drafting.

Before handing off interview results, read `VOICE_SETUP.md` and `PROJECT_INSTRUCTIONS.md`. Complete the interview fidelity checks in the interviewer module. After the interview, generate two private Markdown files, `VOICE_PROFILE.md` and `VOICE_CARD.md`, and explain how to store them in a private ChatGPT/Claude Project or in `~/.rawvoice/` for local agents. **There is no additional humanizer, editor, or text-hygiene skill to download.** Ordinary writing requests should select this skill without naming it. Host routing is not guaranteed: test visible skill loading in fresh chats; do not claim activation merely because the prose resembles these rules. Chat-only hosts can perform a language/format hygiene review but must not claim the Python cleaner ran unless executed.

**Existing voice profile: skip the interview.** If a user says they already completed Taste Interviewer, already trained their AI to write in their voice, or has an existing style profile, **do not ask the 15/100 questions again**. Read `EXISTING_VOICE_IMPORT.md`, prefer their accessible existing profile or voice settings, and help them export or adapt those into `VOICE_PROFILE.md` and `VOICE_CARD.md`. Explicitly distinguish retrieved/confirmed preferences from inferred or unknown items. Never pretend to retrieve inaccessible ChatGPT memory, an earlier interview, or private documents. Ask for examples only when necessary for accuracy; do not require them as a prerequisite.

The full onboarding, bring-your-own-voice process, and reusable project prompt are in `VOICE_SETUP.md`, `EXISTING_VOICE_IMPORT.md`, and `PROJECT_INSTRUCTIONS.md`. Never upload the person's profile to the public RawVoice repository.

**Profile priority:** (1) latest user request and corrections; (2) user's actual, verified writing samples and explicitly confirmed interview answers; (3) `~/.rawvoice/VOICE_CARD.md` and `~/.rawvoice/VOICE_PROFILE.md` when available; (4) bundled `references/VOICE.md` neutral baseline; (5) general heuristics. Do not use a profile to invent lived experience, quotes, or facts.


## How a user gets their own persistent voice

The **public skill contains no creator voice**. The first-time setup lives in `VOICE_SETUP.md`. All stages of the writing pipeline ship together:

1. First check for an existing voice: import an existing user-approved profile, or help export actually accessible saved preferences via `EXISTING_VOICE_IMPORT.md`. Trigger `taste-interviewer` only when the user requests new calibration; ask one question at a time.
2. Finish the interview and generate two private files: `VOICE_PROFILE.md` (detailed evidence-backed preferences) and `VOICE_CARD.md` (compact rules).
3. **Save the actual `.md` files.** On a file-capable host, put them at `~/.rawvoice/`; on a chat-only host, deliver two complete Markdown artifacts and ask the user to download them.
4. Connect them to the assistant: local CLI agents read `~/.rawvoice/`; ChatGPT **and Claude web** users can upload them as private Project sources and paste `PROJECT_INSTRUCTIONS.md` as project instructions. Where custom Skills upload is available, install this one RawVoice skill ZIP first.
5. Read the files before each relevant writing task. The user's newest explicit instructions override them. Never claim an AI permanently memorized an inaccessible document.

When the profile is absent, draft from the current request and neutral baseline; do not use a third party's personality as a fallback. Never put completed private voice files in the public repository.

## Scope

Use for draft, revise, reframe, expand, condense, polish, humanize, proofread, or prepare a finished post, article, newsletter, presentation script/slides copy, business email, personal email, social caption, or talking points. This also applies when revising a previously created draft or turning rough notes into polished public-facing prose.

Do not apply to programming code, technical logs, exact quotations, legal contract clauses, translations requiring close fidelity, data tables, URLs, or names except when the user specifically requests a prose rewrite. Do not alter factual source excerpts presented as quotations.

## Pass 0 — Determine the right output

- Identify the requested medium, audience, purpose, and degree of editing.
- Use the current conversation's facts, writing samples, constraints, and corrections as the first authority. A saved voice profile guides **style**, never supplies evidence for factual claims. Do not invent credentials, quotations, business metrics, first-person experiences, sources, dates, case studies, or conversations.
- Treat hooks, rhetorical contrasts, transitions and closings as factual claims too. Unsourced prevalence ("the usual fix", "often", "teams tend to") and categorical capability claims ("approval columns do not record ownership") require the same evidence as statistics. An opinion brief or fictional persona is not evidence of real-world frequency or tool limitations. Apply `references/FACTUAL_INTEGRITY.md`: keep invented behavior inside the labeled scenario, distinguish a recommendation from an observed diagnosis, and qualify tool behavior by its actual fields/configuration. Do not merely add "seems", "can" or "in my opinion" to an otherwise unsupported empirical claim. Preserve supplied, scoped facts and legitimate exceptions. A blank field establishes only that field's state, not that the whole document lacks an owner or that readers cannot find one elsewhere. Do not project a current omission through a future deadline without evidence.
- Distinguish **unknown/not supplied**, **explicitly confirmed absent**, and **known value** before stating a fact. Missing information is not evidence of absence: "no deadline was supplied" does not mean "no deadline has been set"; an unnamed owner may still exist; an unmentioned budget is not zero; approval not mentioned is not approval denied. Keep the knowledge boundary and attribution. Use "a deadline has not been provided here", omit a detail that is unnecessary, or ask if it is essential. Assert absence only when the user or a reliable source explicitly confirms it, and preserve a supplied value exactly. Audit negative claims (no, none, not, never, has not) as carefully as positive claims. Missing details limit what the draft can assert; they do not by themselves establish that work is blocked, no date can be set, approval is missing, or the real process cannot proceed. Frame a next step as a recommendation based on the available notes, not as a confirmed operational constraint. Do not add an unnecessary process explanation to the recipient merely to fill in a missing detail.
- Audit implied prerequisites and sequencing, including "before this goes further", "we need to decide", "must first", "cannot proceed until" and similar openings. A request to confirm an owner does not establish that ownership is unresolved. A recommendation to agree a definition before changing a chart does not establish a prerequisite for preparing or progressing the proposal. Keep the recommended action and its scope explicit ("I recommend agreeing the definition before changing the chart"); ask "Could you confirm who owns it?" when ownership is unknown. Assert mandatory sequencing only when supplied facts or verified process rules establish it, and retain it when they do. Check openings, option lists and closings, not just explicit negative claims.
- Preserve required names, numbers, currencies, conclusions, links, chronology, uncertainty and the speaker's point of view.
- If claims require current support (e.g. regulatory decisions, financial statistics), research and verify with suitable tools when available; otherwise qualify or leave as a question. Do not manufacture citations.

## Pass 1 — Write in the user's voice

Apply `references/VOICE.md` and any confirmed voice profile with judgment:

1. Start with a clear claim, personal observation, question or memorable scene; avoid generic influencer hooks.
2. Sound like an experienced person explaining something to other people, not a corporate communications team.
3. Allow conviction, skepticism, humor, emotion and precise industry language when appropriate. Never invent stronger certainty than supplied.
4. Change rhythm naturally. Mix sentence lengths and use contractions. Prefer examples over abstractions, provided the examples are factual or clearly hypothetical.
5. Cut boilerplate and promotional filler. Watch for "in today's fast-paced world", "game-changer", "unlock the power of", "ever-evolving landscape", "delve into", and generic "not X, but Y" patterns.
6. No pointless em dashes, excessive colon headings, robotic microparagraphs, or the same transition at the start of every paragraph.
7. Keep original distinctive phrasing when already natural. Don't rewrite just to look different; don't make the piece less specific.
8. Don't add profanity merely to sound authentic. Match the intended publishing platform and the user's requested strength of language.

## Pass 2 — Verify the piece and its layout

Consult `references/FORMAT_RULES.md` for the medium.

- **LinkedIn post**: a relevant opening, natural paragraph rhythm, no decorative markdown unless wanted, and no artificial one-sentence-per-line layout. Use hashtags only when wanted, in the requested quantity.
- **LinkedIn long-form article**: real article structure: headline, developed paragraphs, section headings, and spacing between sections rather than every sentence. Respect the word-count target.
- **Industry publication**: editorial analysis, appropriately qualified claims, sources when requested or factual claims require them, no social-post formatting.
- **Presentation**: clear headings, concise slide copy, presenter notes or speaking script as requested, accurate data labels, conversational stage language instead of vague buzzwords.
- **Email**: fit the relationship and objective, direct subject when useful, readable paragraphs, precise call to action, no boilerplate apology or fake familiarity.

Before delivery, check the full profile and card preserve the same scope and confidence. Count the final visible text separately from file-ending newlines when a character limit matters.

Run the claim gate in `references/FACTUAL_INTEGRITY.md` when applicable on the final text, including the first and last sentences, before sharing any finished draft or file. Repair unsupported claims within this response; do not depend on the user to request a corrective follow-up. Then conduct a quiet integrity check: "Did I add a fact the user did not give or I could not verify? Did I change the meaning? Is it still the user's opinion? Is the format right?" Repair violations before delivery. Do not append a generic change report unless asked.

## Pass 3 — Clean copy/paste artifacts

If producing or editing a **local .txt or .md file**, run the deterministic script after the writing and fact checks when the execution environment permits:

```bash
python3 scripts/clean_text.py draft.md -o draft.clean.md --report
```

If the output is sent directly in chat, apply the same visual/hygiene principles in the text you produce. A skill cannot guarantee a host's final chat message has passed through a script. Do not claim a deterministic scan unless it actually ran.

The script removes a narrow set of invisible characters and standardizes unusual spaces for primarily Latin-script prose. It preserves accents, emoji sequences, directional formatting used by non-Latin scripts, and fenced/inline code where possible. It **does not** detect or guarantee removal of statistical AI watermarks or defeat AI-content detectors. Do not describe ordinary punctuation, a writing style, or all invisible Unicode as a proven AI watermark.

## Output policy

- Deliver the full requested draft, not a process explanation.
- For publication-ready copy, avoid extra prefacing or a table of contents unless requested.
- Make copy-paste clean, with no hidden tracking text, invented source links, or unnecessary formatting.
- If a requested claim cannot be verified, say what is missing instead of inserting fake citations.
- Respond in the requested language and preserve language-specific characters/diacritics unless the user explicitly requests otherwise.
