# RawVoice 1.0

Writing guidance shaped around your voice.

RawVoice is an independent Claude skill that helps turn your writing preferences and examples into a reusable voice profile. Start with the optional Taste Interviewer, or import a profile you already use.

**AI can still make mistakes. Review the output and verify factual claims before use or publication.**

## Download and install

[Download RawVoice_Claude_1.0.zip](RawVoice_Claude_1.0.zip?raw=true)

Upload that ZIP in Claude's **Customize → Skills**, then enable **rawvoice-write-and-edit-prose**. Do not upload GitHub's automatic Source code ZIP or the entire repository as a Claude skill.

See the [setup guide](SETUP_GUIDE.txt) for current installation steps, account/workspace considerations and troubleshooting.

## Make it your voice

1. Create a private writing Project and add the supplied [Project instructions](PROJECT_INSTRUCTIONS.txt).
2. Start Taste Interviewer in **Quick mode (15 main questions, one at a time)**, or import an existing voice profile. Deep mode offers 100 questions; the documented observed end-to-end test covers Quick mode.
3. Review the generated `VOICE_PROFILE.md` and `VOICE_CARD.md`. Correct errors before treating the files as approved preferences.
4. Add both approved files to that Project's knowledge. Start a fresh chat in the same Project and test an ordinary writing request.

Saving and making the files available supports reuse. This is not a promise of permanent memory across unrelated chats. Automatic skill selection also depends on the host and your setup.

## Included

- Interview and existing-profile import workflows.
- Voice-aware drafting and editing guidance for posts, articles, emails and other prose.
- Format guidance and an optional Python text-cleanup script.
- Setup instructions, a clearly labeled fictional walkthrough and a feedback template.

The skill source is in [rawvoice-write-and-edit-prose](rawvoice-write-and-edit-prose/). It contains no completed personal profile.

## Read before use

- [Limitations and user review](LIMITATIONS.txt)
- [Fictional workflow demonstration](FICTIONAL_DEMO.txt)
- [Release notes and test scope](RELEASE_NOTES.txt)
- [Feedback template](FEEDBACK.txt)

Keep your profile files and interview answers private. Use short redacted or fictional examples when reporting a problem.

**1.0 is the first public release version.** Earlier 2.x identifiers in development notes are internal pre-release labels. The release-preparation changes have packaging validation; no new full Claude model test is claimed after those changes. Known factual/source-fidelity failures remain documented in the limitations.

## License and attribution

[MIT license](LICENSE), retained as supplied. The interviewer source credits inspiration from Ruben Hassid's Taste Interviewer method and states that it is not his official release. RawVoice is not an official Anthropic product.
