---
name: taste-interviewer
description: >-
  Interview the user to learn and set their authentic writing voice and taste. Trigger when the user requests "Taste Interviewer", "set my voice", "learn my voice", "build my voice profile", "calibrate writing style", or "update my writing voice". Conduct an interactive interview one question at a time, and create a reusable RawVoice voice profile. Do not run the interview for normal drafting requests.
license: MIT
compatibility: Prompt-based agent skill for Claude Code, Codex, and other Agent Skills hosts. No API keys needed. Persistent local profile is best-effort and depends on file access.
metadata:
  version: "1.0"
  category: writing-voice-calibration
---

# Taste Interviewer — RawVoice voice calibration

This is a **module of the RawVoice skill**, not another download for ChatGPT or Claude web. The main RawVoice skill reads these interview instructions when the user requests calibration. This Claude ZIP contains no separate local-agent installer or direct-invocation package.

Inspired by Ruben Hassid's published Taste Interviewer method; original implementation and wording. This module is not an official release by Ruben Hassid. Source context: https://www.linkedin.com/posts/ruben-hassid_how-to-make-ai-sound-exactly-like-you-forever-activity-7419982189787951104-f6Ru

## Trigger, workflow and precedence

- **Trigger only on explicit requests** to set, interview, recalibrate or update the user's voice. Normal draft requests use `rawvoice`, not an interview.
- Ask **one main question at a time** and wait for its answer. Probe vague responses and ask for concrete, contrasting examples. Do not invent quotes, beliefs, or examples.
- Read existing voice profiles and supplied writing samples as a **starting hypothesis**, never as a replacement for user answers. In particular, avoid assuming an earlier preference is permanent if the user corrects it.
- Offer two modes only at the start if the user has not chosen: **Deep (100 main questions)** or **Quick (15 main questions)**. A user who invokes "full Taste Interviewer" wants Deep. If the user wants to start instantly, start question one without a bulky form.
- Deep mode must include exactly **100 main questions** across seven categories. Quick mode uses exactly **15 main questions**, intelligently spread across the same categories. Probes and clarifications are not main questions, and should be used sparingly.
- See `references/INTERVIEW_PLAYBOOK.md` for counts, focus areas, and progress handling; see `references/VOICE_PROFILE_TEMPLATE.md` for the exact output sections.

## Questions and evidence

- Focus on beliefs and opinions the person actually holds, writing mechanics, what they reject, tone and humor, structural preferences, nonnegotiable limits, and credibility signals.
- Prefer specific examples: text they wrote and liked, text they wrote and rejected, actual openings and endings, how they edit, and how they change their tone by audience.
- Push back on generic claims such as "professional but natural"; ask what that would look like in a sentence or what would feel wrong.
- Do not pressure disclosure of personal or sensitive information. Allow "skip" or "stop" and maintain a useful partial profile.
- Distinguish **verbatim direct quotes**, **confirmed preferences**, and **AI inferences**. Never present inferred stylistic rules as direct quotes.
- If actual samples are supplied, contrast them with stated preferences and ask about any gap. Preserve samples accurately; do not claim a sample is user-authored unless confirmed.
- Note differences across LinkedIn posts, long articles, industry journalism, presentations, on-camera/stage remarks, and emails.

## Progress / persistence

- Maintain `~/.rawvoice/INTERVIEW_SESSION.md` as the progress ledger **when file-writing tools are available**. Include mode, answered main-question count, per-category counts, every question, every answer, confirmed rules, unresolved issues, and next question. Do not overwrite an existing interview unintentionally; ask whether to continue or start fresh when one exists.
- At the end of a session (including partial), offer a portable Markdown checkpoint if local file persistence is unavailable. Do not claim that an interview automatically follows a user across separate chats without a saved file.
- On completion, or at user's request for a partial profile, generate:
  1. `~/.rawvoice/VOICE_PROFILE.md` — full evidence-grounded profile and interview transcript with explicit labels for unconfirmed inference.
  2. `~/.rawvoice/VOICE_CARD.md` — short always-on rules and format-specific settings for fast reading.
- Create `~/.rawvoice/` if allowed, but do not delete existing files without confirmation. When revising an existing profile, preserve earlier authentic answers; mark changes with dates rather than silently replacing contradictory statements.
- When no direct file access is available (e.g., ordinary chat), deliver the finished `.md` profile as text or a downloadable artifact, and explain that it must be stored or attached for other models to access it.

## Required user handoff after interview

The job is **not complete** when the questions are answered. The user must be able to reuse their voice.

1. Generate **two real Markdown outputs**, `VOICE_PROFILE.md` (full profile) and `VOICE_CARD.md` (concise always-on rules). On file-capable local agents, write them into `~/.rawvoice/`. In chat-only environments, provide downloadable files if the host can create them; otherwise show each file's full contents in separate Markdown code blocks. Do not claim a file was created or saved if it was not.
2. **Tell the user to save and keep these `.md` files private**. Never add profile data or personal interview answers to a public GitHub repository.
3. Explain the next action: for Claude Code/Codex, the installed RawVoice reads `~/.rawvoice/VOICE_CARD.md` and `~/.rawvoice/VOICE_PROFILE.md`; this Claude ZIP includes no local import script; if a separately configured local agent uses those paths, the user can copy their approved files there manually. For ChatGPT **or Claude web**, add the files to a **private Project** and add the persistent instruction prompt supplied in `PROJECT_INSTRUCTIONS.md`. If `.md` uploads are unsupported, provide `.txt` equivalents or paste the content.
4. Ask the user to **test** with a real writing prompt in a fresh conversation **where the files are available**. If needed, refine the profile and resave/reupload it.
5. The words "remember" or "memorize" are **not equivalent** to storing a file. Do not promise guaranteed long-term, cross-chat memory or pretend the profile is accessible when it is not. The Markdown files are the source of truth.

## Integration with RawVoice

- On every relevant writing task, `rawvoice` uses the newest confirmed `~/.rawvoice/VOICE_CARD.md` and `~/.rawvoice/VOICE_PROFILE.md` **if readable**; otherwise it uses bundled `references/VOICE.md`.
- User's latest explicit instruction outranks the saved profile. The saved profile outranks generic style heuristics. Direct examples and verified facts outrank speculative inferences.
- Do not confuse **writing voice** with voice cloning, pronunciation, or microphone/speech settings; these are out of scope.
- The voice profile is a writing aid, not a guarantee of detector evasion or a perfect reproduction of someone's thought process.

## Capture questions at ask time

Transcript fidelity starts before the answer, not at final profile generation. For every main question:
1. Compose the full question once. Before sending it, append a numbered record with that exact question string to `QUESTIONS_ASKED.jsonl` in the interview folder when file tools are available. Never overwrite an existing question record. Without tools, preserve a numbered verbatim checkpoint in the conversation.
2. Display that same stored string, without rewording, in a fenced plain-text block under the question number/category. The block is the authoritative asked question, including every sentence, punctuation mark and contraction. Keep commentary outside it. Do not ask another version alongside it.
3. After the answer arrives, record its complete text separately. Do not reconstruct the question from the answer, a summary, or the previous ledger. Populate the ledger and full profile by copying the immutable question record and original answer, not by regenerating either.
4. At completion, compare all question entries against the ask-time records and all answer entries against the original messages. Comparing the profile to the ledger alone is insufficient: both can contain the same transcription error. If original evidence is unavailable, mark the affected text unverified; do not label it exact or claim a passed check.

Do not run prose cleanup on verbatim transcript blocks. In particular, do not combine sentences, add conjunctions, change question marks to commas, or normalize contractions. Questions 5 and 8 have previously failed this way; apply this capture rule to every question, regardless of wording or theme. Deliver `QUESTIONS_ASKED.jsonl` with the ledger as the provenance file when file tools are available.

## Evidence limits versus voice rules

Do not convert an inference boundary into a behavioral preference or prohibition. "Don't infer sarcasm toward junior colleagues" means that preference is unconfirmed; it does not mean "no sarcasm toward junior colleagues" or "never use sarcasm". Keep such statements under Evidence limits / Unknown, preserving their exact scope. Record an actual ban only when the answer explicitly establishes one. For each card rule, check whether its source governs the person's writing or merely limits what the assistant may conclude. Do not hide an inference boundary under confirmed Tone, Defaults or Prohibitions.

## Completion fidelity gate

Before delivering either profile:
- Preserve each exact main question and full exact answer in the ledger, including test labels/prefixes and punctuation. If the user requests redaction or condensation, label it explicitly as edited/paraphrased; never call that text verbatim. Keep verbatim text separate from summaries.
- For every derived preference, record source question, scope, exceptions and confidence: confirmed, inferred/unconfirmed, or unknown. A synthesis of examples is inferred unless the answer states the rule. Do not manufacture identity traits.
- Build the card only from confirmed rules with the same qualifiers and exceptions. Put unresolved inferences in an Unconfirmed section; never under Always/Never. Do not turn usually into always, an example into a hard cap, or a professional-only preference into a universal ban. Flag ambiguity rather than choosing the strongest interpretation.
- Preserve modality as well as scope: "avoid", "prefer", "usually", "may" and "never" are different strengths. Put soft preferences under scoped Preferences/Defaults, not Always/Never, even if their wording sounds similar. A heading must not strengthen the rule beneath it. Do not add a "do not reuse verbatim" restriction (or permission to reuse) to tone examples unless the answers explicitly establish it; place general anti-overfitting advice in a clearly labeled assistant-guidance section, not among confirmed user rules. If the profile and card conflict, use the original answer to repair both.
- Compare the card against the full profile before saving. If a change is required, update both consistently. Quick mode must say provisional, including partial Quick interviews.
- Read the root VOICE_SETUP.md and PROJECT_INSTRUCTIONS.md before the handoff. Deliver both actual files and the portable ledger/checkpoint, then explain: attachments work in that chat; private Project sources plus project instructions support future chats inside that Project; local agents can read ~/.rawvoice only for actual approved user profiles. Files must be available; memory promises are not storage.
- For fictional tests, keep the warning on both files, use a separate test folder or test-only Project, adapt project instructions to name the fictional persona rather than "my voice", and never install the persona globally. Mention any host-injected memory limitation honestly. Do not claim Project settings were verified unless inspected.
