# RawVoice — Use an existing writing voice (skip Taste Interviewer)

Already completed an interview, trained ChatGPT through previous conversations, or saved your writing style elsewhere? **Do not repeat the interview.** RawVoice can import the preferences you already have.

This is a **bring-your-own-voice** route, not an automatic account-memory extractor. A skill cannot simply open all of your ChatGPT memories, past conversations, private files, or Claude preferences. The AI must use information that is **actually accessible in the current session**; the user reviews the result and saves their own private files.

## Route A — You have an existing `.md`, text, or document profile

1. Give that profile to the AI or attach it inside a private project.
2. Say: **"RawVoice: import my existing voice. Skip Taste Interviewer. Read the attached profile, preserve my confirmed style, and generate `VOICE_PROFILE.md` plus a concise `VOICE_CARD.md`. Flag anything ambiguous rather than inventing it."**
3. Review the two generated files and correct errors. Keep original examples when they belong to you; do not paste private employer/customer details into public documents.
4. Download both Markdown files. For this Claude release, add them to private Claude Project knowledge. This ZIP contains no local import script. A separately configured local agent may use manually copied approved files, but that setup is outside this Claude guide.
5. Start a **new chat in that Project** and test a writing request without mentioning the skill.

## Route B — You already taught ChatGPT or Claude your voice, but have no export file

1. In the assistant/conversation where your prior preferences are accessible, paste the following prompt:

> **RawVoice — export existing voice; no interview.** Use only my writing preferences, corrections and examples that you can genuinely access in this conversation or through available memory or project knowledge. Do not claim to access the original interview or earlier chats unless you can retrieve them. Draft two separate Markdown files: `VOICE_PROFILE.md` (detailed) and `VOICE_CARD.md` (concise actionable rules). Separate *confirmed explicit preferences* from *inferences based on examples*. Include preferred tone, structure, opening style, humor, vocabulary, formatting, common dislikes, and format-specific rules only where evidence exists. Never add invented personal details or copy another person's style. If any important information is missing, mark it unknown instead of interviewing me again. Show a summary for my review before export.

2. Review and correct the draft profile. **Memory often contains a summary, not every answer to a past 100-question interview.** If you want exact coverage of those answers, you must supply the saved answers or original profile yourself.
3. Ask the assistant to provide/download **both** `.md` files. If files cannot be created, paste the Markdown into two plain-text files with those names.
4. Upload these files to **private** project knowledge in ChatGPT/Claude (or import locally). Do **not** put them in a public GitHub repository.
5. In the Project instructions, use the supplied `PROJECT_INSTRUCTIONS.md`. For supported skill uploads, enable RawVoice as well. Start a new chat **inside the Project**; unrelated chats may not have the profile.

## Route C — You have writing samples but no reliable preference summary

Share 2–5 pieces you actually wrote, ideally across multiple formats, plus a few examples of what you dislike. Ask RawVoice to **infer** a provisional `VOICE_PROFILE.md` and `VOICE_CARD.md`, clearly label inferred rules, and have you approve them. There is no requirement to run 15 or 100 new questions.

## Required private files

- `VOICE_PROFILE.md`: detailed confirmed preferences, cited examples **from the user's own provided text where available**, inferred/unknown items clearly marked, and context-specific rules.
- `VOICE_CARD.md`: brief, explicit rules the AI should apply to every eligible writing request; include exceptions for formats when necessary.

**Priority:** Latest user instruction > verified, user-approved voice rules and samples > existing private profile > neutral skill defaults. A voice profile is not a source for factual claims.

## Test the import

Use `TESTING_GUIDE.md`. Compare the same request with and without RawVoice, then repeat in a fresh Project conversation. Ask the AI which **specific available profile rules** it applied. Do not count unsupported claims about memory or an unexecuted text-cleaning script as passing results.
