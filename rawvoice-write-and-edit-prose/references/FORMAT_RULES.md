# Format rules and pre-publication checklist

| Output | Default structure | Common error to avoid |
|---|---|---|
| LinkedIn post | Opening hook, 2–5 natural paragraphs, optional closing; apply FACTUAL_INTEGRITY.md | Unsourced prevalence or universal tool claims in hooks/closings; fake high-impact rhetoric |
| LinkedIn article | Title, thematic sections, developed paragraphs | Treating a 3,000–5,000-word article like a social post |
| Industry publication article | Headline, opening thesis, evidence and analysis, conclusion; sources as applicable | Industry claims as proven facts without evidence |
| Newsletter | Meaningful subject/title, scene or insight, developed explanation, takeaway | Corporate summary bullets with no story |
| Presentation | One point per slide, clear label, appropriate data and speaking notes | Walls of text or trendy slogans with no content |
| Email | Subject when helpful, direct opening, coherent body, next step | 'I hope this email finds you well' by default |
| Panel / on-camera script | Spoken language, beats and transitions, accurate names and timing | Long sentences that are hard to say aloud |

## Quality gates

1. Meaning and factual claims unchanged unless the user explicitly requested corrections.
2. Facts, people, statistics and dates: sourced or clearly marked as assumptions/illustrations. For LinkedIn/opinion and team/tool explanations, read `FACTUAL_INTEGRITY.md` and repair unsupported hooks, capability claims and takeaways before sharing.
3. Tone authentic to author and audience, not generic AI / corporate marketing language.
4. Layout appropriate to destination; word count followed when specified.
5. Natural cadence and transition, with no forced line breaks.
6. No unwanted zero-width characters, unusual spaces or copy-paste residue in final text.
7. No guarantees of AI-detector results, provenance removal, or invisible watermark removal beyond what tools directly verified.
8. Preserve legitimate Unicode for accented words in different languages, other languages, math, emoji sequences, links and quoted content.

## Optional explicit request

The user can type "RawVoice strict" to request an extra editing pass with suggested changes and an integrity checklist. Normally do not expose the checklist.

## Taste Interviewer integration

- If `~/.rawvoice/VOICE_CARD.md` exists and is readable, consult it for concrete tone, structure, and hard no's. Use the full `~/.rawvoice/VOICE_PROFILE.md` for ambiguous cases or close imitation of sentence rhythm.
- Do not let a provisional/interview-generated voice profile override the user's newest explicit instruction or force a 100-question interview before drafting.
- If the user requests an interview, read the integrated `modules/taste-interviewer/INTERVIEWER.md` module rather than interviewing in the normal drafting workflow.
