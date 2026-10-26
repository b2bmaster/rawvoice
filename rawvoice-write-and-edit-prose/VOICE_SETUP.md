# RawVoice 1.0 — ChatGPT and Claude setup

Teach it your voice. Keep the profile.
RawVoice uses your reviewed preferences and examples to guide writing. Choose the setup for your platform below. Both routes use the same two personal voice files; they do not sync automatically between platforms.

CHATGPT — PRIVATE PROJECT SETUP
1. Download RAWVOICE_PROJECT_GUIDE.txt from this release.
2. Create a private writing Project in ChatGPT. Add the downloaded guide as a Project source/file.
3. Copy only the marked block in PROJECT_INSTRUCTIONS.txt into that Project's instructions. Keep the Project private and review who can access it.
4. Start Quick mode or import an existing voice using the prompts below.
5. Review, download and add VOICE_PROFILE.md and VOICE_CARD.md to the same Project's sources. If .md files are unsupported in your interface, use .txt copies of the same content.
6. Open a fresh chat inside the Project and ask it to report a few specific preferences from the files. Compare the answer yourself, then make a normal writing request.

This route uses Project files and instructions. It does not require a custom-skill upload option or an API key. Native skill availability, file creation and Python execution vary by host, account and workspace. Do not assume that uploading a guide installs a native skill or runs the optional cleaner.

CLAUDE — INSTALLED SKILL SETUP
1. Download RawVoice_Claude_1.0.zip. Leave it compressed; do not upload the larger publishing kit, public-release ZIP or GitHub's automatic Source code ZIP as a skill.
2. In Claude, enable Code execution and file creation (called Create and edit files in some Settings layouts) if needed. Go to Customize → Skills, choose the add/create upload action, upload the named ZIP, and enable rawvoice-write-and-edit-prose.
3. Create a private writing Project. Copy the marked block in PROJECT_INSTRUCTIONS.txt into Set project instructions and save.
4. Start Quick mode or import an existing voice. Review and add both personal voice files to Project knowledge/Context; do not assume an attachment was automatically saved there.
5. Test an ordinary drafting request in a fresh Project chat. Check actual skill loading if the interface exposes it. Explicitly ask to use RawVoice if automatic selection does not occur.

If your Claude workspace cannot install custom skills, the Project-guide route above is a prompt-based alternative. It does not install the skill. Feature names and permissions may change.

START WITH YOUR EXISTING VOICE
If you already have a profile, attach it privately and say:

Import my existing writing voice. Skip Taste Interviewer. Preserve confirmed preferences and examples, mark unknowns, and generate VOICE_PROFILE.md and VOICE_CARD.md for my review.

The guide includes an existing-voice import section. The assistant can use only material actually available to it; RawVoice cannot open inaccessible memories or chats from another platform.

OR START THE INTERVIEW
Say:

Start Taste Interviewer in Quick mode. Use the RawVoice guide or installed skill. Ask all 15 main questions one at a time. At the end, generate downloadable VOICE_PROFILE.md and VOICE_CARD.md, plus the interview checkpoint and question log. Mark inferences and unknowns clearly.

Deep mode offers 100 main questions. You can skip a question or stop for a partial profile. Quick profiles are provisional. Share writing examples you are comfortable placing in your provider account. If downloadable files are unavailable, request the complete text and save each file yourself.

REVIEW AND REUSE
VOICE_PROFILE.md contains detailed preferences, examples and the transcript. VOICE_CARD.md is the compact companion. Check that usually has not become always, avoid has not become never, and missing information has not become a claim that something does not exist. Correct errors before approving the files.

Save the approved files privately and add them to each Project where you want to use them. To move between ChatGPT and Claude, download the approved versions and upload them to the other platform. A profile guides style; it is not a source of facts. Saying remember this does not replace saving the files or make them available everywhere.

Then make an ordinary request, such as:
Draft a short LinkedIn post from these notes: [your notes]. Preserve the facts and label any invented example.

When preferences change, ask for both profile files to be updated, review the results and replace outdated Project sources. You do not need to repeat the whole interview for every small edit.

YOUR REVIEW MATTERS
AI can still make mistakes. Review profiles and drafts, and verify factual claims before use or publication. Check names, dates, numbers, quotations, conclusions and details added beyond your notes. RawVoice does not guarantee perfect accuracy, exact imitation, permanent memory or detector results.

OPTIONAL TEXT CLEANUP
The included scripts/clean_text.py can check a narrow set of invisible characters and unusual spaces in saved UTF-8 text when a Python-capable environment is available. Project instructions alone do not execute it. The cleaner does not fact-check or detect plagiarism and must not rewrite exact transcript blocks.

PRIVACY AND TROUBLESHOOTING
Keep personal profiles and interview answers out of public repositories and issue reports. For fictional testing, use a separate Project and review the host's memory controls. Uploaded information is handled under your AI provider's settings and terms.
If writing is generic, check that the correct approved profile and card are available. If profiles conflict, replace outdated files. If a tool or file is unavailable, the assistant should disclose that rather than claim it ran or remembered it.

PLATFORM REFERENCES
Guidance checked 26 October 2026; interfaces and workspace access may change.
ChatGPT Projects and shared instructions/files: https://learn.chatgpt.com/docs/projects
Claude skills and ZIP upload: https://support.claude.com/en/articles/12512180-use-skills-in-claude
Claude Projects and knowledge: https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects

TEST SCOPE
The recorded end-to-end tests cover Claude. This copy/setup update does not claim a new ChatGPT or Claude model test. Other local-agent or API installation is outside this guide; the package includes no local installer or import script.
