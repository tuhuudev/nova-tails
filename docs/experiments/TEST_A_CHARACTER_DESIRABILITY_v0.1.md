# Test A — Character Desirability and Identity v0.1

**Status:** READY TO RUN — blocked on source-art import and participant recruitment  
**Date:** 2026-09-16  
**Decision owner:** NOVA TAILS product review  
**Primary candidate:** NT-001 / Pyrox

## Decision this test supports

Decide whether the project should retain and further invest in character-led identity work, and whether Pyrox is promising enough to enter a limited 3D-blockout proof **after** the Product Vision review. This test does not approve canon, production art, printing, or an entire product direction.

## Hypotheses and failure signals

| Hypothesis | Pass evidence | Failure signal |
| --- | --- | --- |
| People can distinguish Pyrox from comparable concepts | At least 60% of participants correctly recall or recognize its three candidate signature features after the distractor task | Feedback is mainly generic (for example, “cute”) or recognition is at/below the comparison concepts |
| Pyrox creates enough interest for one more interaction | At least 50% select a 4 or 5 on the five-point “want to see/interact again” item | Fewer than 50% select 4 or 5, with no actionable explanation |
| The presentation is not misleadingly dependent on lore/name | Participants can describe a memorable visual feature before being told the name or setting | Recall depends mainly on the supplied story/name |

These are provisional decision thresholds for a small qualitative test, not statistical proof. Record uncertainty and revise the test before scaling if the sample is too narrow.

## Materials required

- Pyrox selected concept plus its verified production-reference/orthographic materials from `data/assets/NT-001.asset-manifest.json`.
- Two to four comparator concepts shown at similar size, finish and amount of context. Comparators must be candidate/exploratory material, not promoted canon by this test.
- A neutral presentation board: one image per concept, no name, lore, element, rarity, product claim, or “approved” label.
- A private result row per participant using `data/experiments/test-a-character-desirability-template.csv`.

Do not run with screenshots, thumbnail crops, or generated variations that differ materially from the retained source assets. Record the asset ID and SHA-256 used in every response row after import.

## Participants

Recruit 12–20 people outside the active project team. Use a mix that plausibly resembles the intended early audience; do not treat friends already familiar with NOVA TAILS as independent validation. Obtain consent for anonymous design feedback. Do not collect names, contact details, or sensitive personal data in the repository.

## Run procedure

1. Randomize the concept order for each participant; record the order code.
2. Show each concept for 20 seconds with no explanatory text.
3. Remove all boards. Use a two-minute neutral distractor task.
4. Ask unaided recall questions before showing any image again.
5. Show the boards once more in a different randomized order and collect the rating/choice questions.
6. Ask one open-ended “why” question. Do not defend or explain the design while collecting answers.
7. Store only the coded result row. Keep raw images out of the response file.

## Questions

1. “Describe any character you remember. What visual details stand out?”
2. “Which character would you recognize again most easily?”
3. “Which character would you most want to see or interact with again?” (choose one)
4. “For Pyrox, how much would you want to see or interact with it again?” (1 = not at all; 5 = very much)
5. “Which parts of Pyrox do you remember?” (free response; score separately for ears, forehead diamond, split flame-tail)
6. “What is the main reason for your choice?” (free response)

Do not reveal Pyrox's name, element, intended species, lore, or 3D-print plans until all six answers are captured.

## Analysis and decision record

- Count recognition of each signature feature only when the participant names or unambiguously describes it without prompting.
- Calculate Pyrox's feature-recall rate, top-recognition choices, top-return choices, and share of ratings 4–5.
- Summarize recurring reasons and negative feedback; distinguish visual feedback from product-format feedback.
- Record asset IDs/checksums used, participant count, exclusions, deviations, and the decision in a dated review note.

Possible outcomes:

- **Continue:** signals meet the provisional thresholds; review whether a tightly scoped 3D blockout is the next proof.
- **Revise:** one or more signatures are not recalled, but feedback points to a specific visual improvement.
- **Pause/Pivot:** interest and differentiation are both weak or feedback is predominantly generic.

## Guardrails

- Do not change `character.json` or elevate Pyrox's canon status solely from this test.
- Do not start a printable asset catalog or production STL work from a positive result.
- Any 3D blockout permission must be recorded separately in `PROJECT_STATE.md` and cite this test's review note.
