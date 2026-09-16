# NOVA TAILS — Visual DNA v0.1

**Status:** PROTOTYPE

## Goal

Preserve character recognition across generations and downstream outputs without forcing every image/model to be identical.

## Recognition model

Each creature should define 2–4 signature features with explicit recognition weights and inheritance behavior.

Example shape:

```json
{
  "id": "TAIL_SPLIT",
  "description": "Split flame-shaped tail",
  "recognitionWeight": 0.9,
  "inheritance": "LOCKED"
}
```

Weights are review metadata in v0.1, not automated scores.

## Visual categories

- silhouette
- proportions
- head
- body
- limbs
- tail / rear silhouette feature
- surface and markings
- color roles
- elemental/effect language
- signature features

## Color roles

Store color by design role rather than prose such as “orange and yellow”:

- primary
- secondary
- marking
- accent
- eyes
- element effect

Exact palette values should only become canon after an approved reference asset exists.

## Evolution continuity

Working heuristic:

- preserve recognition-critical silhouette anchors;
- preserve locked markings/features;
- allow size, complexity and effect intensity to evolve;
- introduce optional features only when they strengthen rather than replace identity;
- reject forbidden traits unless the character definition is intentionally revised.

## AI generation rule

Generated images are candidate interpretations of the Visual DNA. They do not redefine Visual DNA automatically.

When a generator introduces a visually attractive but unapproved trait, record/review it before changing structured character data.

## Consistency review

For each candidate output, review:

1. silhouette recognition;
2. locked feature preservation;
3. palette-role continuity;
4. proportion/stage intent;
5. accidental forbidden features;
6. downstream feasibility where relevant (3D separation, animation, printability).

## Promotion

`concept` → review → corrected candidate → consistency test → `approved reference/master`

Only an approved reference should be used as the primary visual source for later evolution/3D work.
