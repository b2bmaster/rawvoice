# RawVoice — realistic cross-platform acceptance tests

Release numbering: public version 1.0 is the first release. Any 2.x identifiers below refer to internal pre-release development tests.

These are *manual* tests for actual ChatGPT and Claude usage. Automated local unit tests validate packaging and safe text handling; they **do not** prove that an account's Skills UI or project memory works.

## Prepare

1. Install/enable the RawVoice skill ZIP where supported, or paste `PROJECT_INSTRUCTIONS.md` into a private Project when uploads aren't available.
2. If you already have a writing voice, follow `EXISTING_VOICE_IMPORT.md` instead of rerunning Taste Interviewer.
3. Place the approved `VOICE_PROFILE.md` and `VOICE_CARD.md` in the Project's private files/knowledge. Use **the same two files** in both platforms. Keep them out of your public repository.

## Run these three comparisons

- **A — Baseline:** In a new chat without RawVoice's skill/project rules, ask: "Write a 150-word LinkedIn post explaining why powerful AI models need good skills to produce useful work. Avoid inventing personal experiences." Capture the output.
- **B — ChatGPT / RawVoice:** In a new chat inside your RawVoice-enabled private ChatGPT Project, submit the **same prompt without adding 'use RawVoice'**. Capture the output.
- **C — Claude / RawVoice:** Repeat the **identical prompt** inside a RawVoice-enabled private Claude Project using the **same saved voice files**. Capture the output.

## Score each result (0–2 per criterion)

1. **Voice fidelity:** Sounds like the user, not generic promotional copy.
2. **Originality and specificity:** Distinctive and specific without invented experiences.
3. **Facts and meaning:** Preserves the prompt; invented factual assertions reduce the score.
4. **Publishing format:** Correct length, natural layout, appropriate to LinkedIn.
5. **Copy/paste hygiene:** No stray invisible controls, odd spacing, or broken characters. Only count deterministic cleaning as tested if a script was **actually executed**.

Total: 10 points maximum per result. Keep the drafts and scores for comparison. Human review is essential: numbers do not guarantee voice authenticity.

## Check it works in future writing chats

1. Open **another fresh conversation inside the same Project**.
2. Ask: "Draft a polite but direct follow-up email to someone who has not replied for a week." Do not name RawVoice.
3. Ask: "Which rules from the voice files you can access did you apply?" Make sure the assistant cites actual rules, not imaginary ones.
4. Test a long-form article and short presentation notes. Look for the same voice adapted to each format, rather than the same structure copied to all outputs.

## Limits and failure modes

- The interview does not need to be repeated by a user who already has an approved voice profile.
- Skill upload support depends on platform, workspace and settings; an uploaded ZIP is not proof it is active.
- ChatGPT Memory may summarize preferences and cannot be assumed to retain all original 100 interview answers.
- A Claude Project cannot read ChatGPT account Memory: it needs the private exported `.md` files.
- Profile-based writing checks and a **local Python cleaning script** are different features. Test separately.
- Do not claim a guarantee of removing statistical AI watermarks or defeating content detectors.

## Regression gate (2.4.1)

Verify Stop Slop and every duplicate variant OFF after reload before starting cold chats. Test ordinary LinkedIn and email requests without skill names, with and without attached profiles. Record visible skill tool calls, reference reads and script execution. Distinguish automatic routing from explicit invocation and Project-instruction fallback.

Test a partial fictional interview with qualifiers (usually, professional-only, if useful), an ambiguous preference and a deliberate unconfirmed inference. Check exact question/answer transcription including test prefixes, confidence-consistent card compression, provisional labels, and an automatic accurate reuse handoff. Then complete Quick 15/15 if full-flow acceptance is required. Never install fictional files globally.

Challenge unsupported categorical claims such as "software always calculates accurately and on schedule". Expect qualification rather than rhetorical certainty. Re-run the Unicode fixture and preserve accents, emoji ZWJ and inline code. Restore original competitor-skill states and verify after reload.

## Missing-information regression (2.4.3)

In cold Claude chats, with the normal routing preference enabled and Stop Slop verified OFF, test ordinary drafting without naming RawVoice or repeating this rule. Capture visible Skill loading/version and actual output.

1. Missing deadline/name/budget: do not assert no deadline exists, nobody owns the task or zero budget. Omit, accurately limit to what was supplied, or ask only if needed. Do not infer work is blocked or a date cannot be set solely from missing notes.
2. Explicitly confirmed no deadline: preserve that fact; do not downgrade it to unknown.
3. Known deadline: preserve the exact supplied value; do not omit or change it.
4. Approval not mentioned versus explicitly denied: do not conflate the two.

Retain original failed copy as historical evidence. Deliver a separate corrected draft. Re-run the cleaner on saved outputs and restore original competitor-skill states after testing.


## Prerequisite and card-fidelity regression (2.4.4)

In fresh private Claude chats, verify Stop Slop OFF after reload and actual automatic loading of this package.

- Draft from notes asking who owns a definition and recommending definition-before-chart. Notes do not establish unresolved ownership or a proposal blocker. Expect a confirmation question and scoped recommendation; no invented prerequisite in opening, options or closing.
- Contrast with an explicitly supplied process rule: proposal cannot advance until a named approval. Preserve that real prerequisite rather than weakening every dependency.
- Regenerate a fictional card from actual source answers. "Avoid exclamation marks in routine professional updates" stays a scoped soft preference; examples get no unsupported verbatim-reuse ban. Compare full card to original answers, not just the old card; preserve usually, scope and quotation exceptions. Label general assistant guidance separately.
- Correct saved profiles privately without altering the exact transcript. Replace the private Project card, then test a fresh ordinary writing request. Preserve original artifacts as historical evidence.


## First-response LinkedIn factual gate (2.4.5)

With Stop Slop verified OFF after reload, submit ordinary LinkedIn briefs without naming RawVoice in separate fresh private Claude chats. Capture actual skill version and reference reads. Score the first completed response and its delivered file; internal edits before delivery are allowed, user corrective follow-ups are not. Keep failed first responses as failures. If changing the package again, start a new candidate and fresh chat; never count a revision prompt as first-response success.

Use: (1) the original approval-column/decision-owner brief with an illustrative scene; (2) a transfer case about automated reminders and missed handovers; (3) supplied scoped facts including a blank Owner field, a real process prerequisite inside the fictional case, known date and an explicit counterexample where another sheet records an owner. Expect no unsourced prevalence, universal capability denial, invented experience/metrics or scenario-to-world leap. Preserve supplied facts, exceptions and unknowns. Audit hooks and endings as well as body claims.

2.4.6 extension: a blank Owner field is not proof that no other part of the record identifies ownership or that a reader cannot find a name. A current blank is not a forecast that the deadline will arrive with it blank. Preserve these distinctions in the first delivered response, not just its audit.


2.4.7 transcript regression: run a fresh fictional Quick interview with no corrective follow-ups. Capture the actual displayed question block before answering each of all 15 questions. Compare both final profile and ledger questions to those original blocks, and answers to submitted messages. Inspect QUESTIONS_ASKED.jsonl independently. Historical Q5/Q8 sentence-merging failures must fail comparison even when profile and ledger agree. Never score model self-audit as evidence.


2.4.8 regression: from original fictional interview answers, generate a new profile/card in a fresh chat without corrective follow-ups. A "do not infer sarcasm toward junior colleagues" evidence limit must remain unconfirmed, while an explicit process-not-person humor rule remains confirmed. In a second fresh chat test an explicit sarcasm ban, a scoped permission, and an inference-only boundary side by side; preserve their different status and scope. Score delivered files, not self-audits.
