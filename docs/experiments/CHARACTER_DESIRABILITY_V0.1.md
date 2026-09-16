# NOVA TAILS — Character Desirability Experiment v0.1

**Status:** REVIEW / EXPERIMENT  
**Date:** 2026-09-16  
**Purpose:** Test whether unknown NOVA TAILS character identities are distinguishable, memorable and desirable before investing in a large roster, deep lore, combat systems or production 3D assets.

## 1. Decision this experiment informs

Primary question:

> Do people who have no project context perceive individual NOVA TAILS characters as distinct identities worth seeing/interacting with again, rather than as interchangeable cute/stylized creature concepts?

This experiment does **not** validate a game, gacha, monetization, lore, STL demand or market size.

## 2. Why this test comes first

The current product hypothesis is identity-first. If the identities themselves are weak, adding progression, rarity, lore, VFX or physical manufacturing can hide the problem without solving it.

External design research supports treating form/silhouette and stable signature features as important recognition variables; color is useful but should not be the only identity carrier. The experiment therefore separates silhouette/identity recall from polished-render preference.

## 3. Hypotheses

### H-A — Distinguishability
Participants can tell the concepts apart without names/lore.

### H-B — Recall
After a distraction/delay, participants can recall meaningful identity features of multiple concepts.

### H-C — Specific preference
Preference is explained by character-specific traits (shape, signature feature, attitude, implied role/story), not only generic adjectives such as “cute” or “cool.”

### H-D — Continued-interest signal
At least some concepts cause participants to voluntarily choose one they want to see/interact with again.

## 4. Test set

Use **4 concepts** for v0.1. Four is enough to expose collisions while keeping participant burden low.

Concepts must deliberately span different identity axes rather than being four fox/robot recolors:

- **A — Agile Scout:** small/light silhouette, strong directional feature, curious/kinetic attitude. MOMO may be used only as a candidate, not canon.
- **B — Heavy Guardian:** broad/grounded silhouette, protective mass/signature structure, calm/steady attitude.
- **C — Arcane/Spirit:** non-mechanical or strongly non-scout construction, floating/ritual or unusual body logic, mysterious/supportive attitude.
- **D — Wild/Abyssal:** asymmetric/predatory silhouette, one major disruptive signature feature, dangerous/controlled attitude.

Species, faction and final names remain intentionally uncommitted. The purpose is to test identity space, not taxonomy.

## 5. Controlled presentation rules

To reduce confounds:

1. comparable rendering quality and framing;
2. neutral/simple background;
3. similar apparent image size;
4. no name, rarity, stats, class, lore paragraph or franchise logo during first exposure;
5. no elaborate VFX that hides silhouette;
6. each concept gets one primary signature feature and at most 2–3 secondary motifs;
7. color palettes must differ, but the concept must still read when converted to silhouette/grayscale;
8. do not tell participants which concept is “main character.”

## 6. Test procedure

### Stage 1 — First exposure
Show all four full-color concepts in randomized order for a short fixed exposure. Ask only for immediate impression in the participant's own words.

Record:
- first adjective/idea;
- what they think each character does/is;
- immediate favorite, if any;
- reason.

### Stage 2 — Silhouette recognition
Show randomized black silhouettes without color/details.

Ask participant to match each silhouette to the previously seen concept or describe it.

Record:
- correct/incorrect match;
- feature used to recognize it;
- confusion pairs.

### Stage 3 — Distraction + unaided recall
After a short unrelated distraction, remove the concepts.

Ask:
- “Which characters do you remember?”
- “What do you remember about each?”

Do not provide names or prompts initially.

Record identity features recalled, not merely number of colors remembered.

### Stage 4 — Preference / continued interest
Show concepts again and ask:
- Which one would you choose to see a short story/animation about?
- Which one would you choose to play/interact with if there were a small experience?
- Which one, if any, would you want as a physical desk figure?
- Why?

These are directional signals only; they are not purchase-intent proof.

### Stage 5 — Similarity probe
Ask whether any concept reminds them strongly of an existing character/franchise and why. Record exact references for later similarity research; participant association is a warning signal, not legal clearance.

## 7. Participant strategy

### Pilot
5 participants outside the project to detect broken questions/presentation bias.

### v0.1 directional sample
Target **15–25 participants** after pilot, with a mix of:
- stylized-character/game fans;
- people without strong game/collectible involvement;
- optionally a small maker/3D-print subgroup.

This is exploratory concept testing, not statistically representative market research. Do not present percentages from this sample as population-level truth.

## 8. Metrics

Track per concept and overall:

- `silhouette_match_rate`
- `unaided_recall_rate`
- `signature_feature_recall_rate`
- `generic_reason_rate` (preference explained only by generic adjectives)
- `continued_interest_rate`
- `confusion_pair_count`
- `strong_external_similarity_mentions`

Also retain qualitative quotes/reasons because a small directional sample can hide important design failure modes.

## 9. Decision rubric

No single metric automatically passes the project. Use the following as **experiment thresholds**, not universal industry benchmarks:

### Strong signal
- most concepts are distinguishable in silhouette;
- at least 2–3 concepts produce recurring specific feature recall;
- preference reasons repeatedly cite identity-specific traits;
- continued-interest choices are not concentrated only on “prettiest render” effects;
- no concept produces a dominant problematic external-character association.

### Weak signal / iterate
- participants mostly describe all concepts as generic cute/cool animals/robots;
- recall is primarily color rather than form/signature;
- silhouettes are repeatedly confused;
- preferences cannot be explained beyond rendering polish/color;
- strong similarity associations repeatedly point to the same existing property.

## 10. Bias controls

- Randomize presentation order.
- Do not reveal project creator preference.
- Do not explain lore before recall.
- Keep render quality comparable.
- Record negative/neutral reactions, not only favorites.
- Do not change concepts halfway through a participant batch; version the test set instead.
- Separate creator/team participants from external participants.

## 11. Artifact requirements before testing

For each of four concepts:
- one clean full-color concept image;
- one silhouette derived from exactly that design;
- one short internal identity note (not shown initially): body archetype, shape language, signature feature, attitude, intended contrast against the other three;
- version label.

No production STL, detailed skill kit, final taxonomy, evolution tree or lore chapter is required.

## 12. Result record

Create after pilot:

`docs/experiments/results/CHARACTER_DESIRABILITY_V0.1_RESULTS.md`

It should include participant composition, artifact versions, raw directional metrics, qualitative observations, confusion matrix, similarity mentions, limitations and a decision: `ITERATE IDENTITY`, `PROCEED TO NEXT RISK`, or `INCONCLUSIVE / RETEST`.

## 13. Next action

Design the four **identity briefs first**, review them for intentional contrast, then generate/render concepts. Do not generate concepts first and reverse-engineer identity briefs afterward.
