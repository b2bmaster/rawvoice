# Interview playbook and exact coverage

## Two modes

| Theme | Deep (100 main questions) | Quick (15 main questions) |
|---|---:|---:|
| Beliefs and contrarian takes | 15 | 2 |
| Writing mechanics | 20 | 3 |
| Aesthetic crimes (dislikes) | 15 | 3 |
| Voice and personality | 15 | 2 |
| Structural preferences | 15 | 2 |
| Hard no's / boundaries | 10 | 2 |
| Red flags / credibility | 10 | 1 |
| **Total** | **100** | **15** |

Use one question at a time. The categories are a coverage requirement, not a rigid order. Count a meaningful new main question once; clarifying requests do not count. In Quick mode, the profile must explicitly state it is provisional and based on 15 questions.

## Suggested question angles (vary wording and order)

1. Beliefs: What conventional wisdom in the person's industry do they reject? Which position would they publicly defend, and why?
2. Mechanics: Ask for a real opening, transition, closing, signature phrase and one disliked replacement. Listen for rhythm, syntax, punctuation, paragraph length.
3. Aesthetic crimes: What writing makes them close a tab? Which AI-sounding clichés trigger distrust? Ask for an example and a rewrite.
4. Personality: How do their humor, confidence, anger, and vulnerability shift in a professional post versus a personal story? Where is the boundary?
5. Structure: Contrast short posts, a 3,000-word article, an industry column, a spoken script, an executive email. What must be different?
6. Hard no's: Topics, tones, claims, or practices they refuse to use, and when constraints change by publisher.
7. Red flags: Which signals tell them a writer is bluffing? What evidence or firsthand experience convinces them?

## Main question format

Example for a first question: "What's one popular belief in your industry that you think is wrong? Give me a real example and explain why."

Probe without restarting the count when vague: "When you say 'natural', what exact opening sentence would you keep, and which one would you delete?"

## Progress ledger

Store: mode; date; next question index; category counts; numbered questions with exact user answers; confirmed voice rules; writing sample citations/locations where available; open issues. Before sending each question, freeze its exact string in the append-only QUESTIONS_ASKED.jsonl and display that string in a plain-text fenced block, as specified in INTERVIEWER.md. After each answer, copy the original answer into the ledger and use the already captured question; never regenerate it. Compare final transcript questions to the ask-time records, not just another generated transcript.

If the user pauses the interview, tell them the count completed and how to resume. A later invocation should continue from the ledger when available instead of starting over.

## Output thresholds

On completion, output full evidence-backed profile and short reusable card. Before completion, output a draft profile only if requested or if the session ends. Mark provisional areas, preserve authentic quotes, avoid invented personal positions. Do not silently auto-publish the user's answers elsewhere.
