# NOVA TAILS

> Working title. Current product hypothesis: build a distinctive multi-species sci-fi/fantasy universe/IP intended to become original, initially explored through character-centric concepts, with potential game, 2D and modular FDM-printable 3D adaptations. Product Vision still needs to validate audience, differentiation, primary product and output priorities. Originality/IP clearance requires review; it is not guaranteed by AI generation.

## Current phase

**Phase 0 — Repository & Architecture Foundation (v0.1, under review)**

This branch/PR proposes that the repository become the authoritative project record after review/acceptance, with `main` as the latest accepted baseline. Until this Phase 0 PR is accepted/merged, its governance/architecture decisions are proposals.

Chat/AI outputs are proposals until reviewed and intentionally captured through repository workflow.

## Proposed project principles

1. Architecture before mass content production.
2. Validate product/core interaction before building a large content library.
3. If an identity/character is retained across multiple outputs, one master identity should feed those adaptations; Product Vision is not required to retain every output.
4. AI generates proposals; it does not directly define canon.
5. Every important decision is reviewable and traceable.
6. Manufacturing standards must come from real physical tests if printable collectibles remain in scope.
7. Every system layer should create a meaningful decision or serve a clear product purpose.
8. Avoid premature complexity in schemas, IDs, asset registries, storage, branching and content volume.
9. Use research/prototypes/tests to attack high-risk assumptions as soon as they become testable rather than treating the roadmap as waterfall.
10. Treat originality and third-party-rights risk as something to validate, not something AI can guarantee.

## Proposed lifecycle status

- `IDEA` — exploratory.
- `DRAFT` — being designed; not active canon.
- `REVIEW` — ready for explicit review; not active canon yet.
- `APPROVED` — accepted current decision/direction.
- `LOCKED` — dependency contract; changing it requires impact review.
- `DEPRECATED` — retained for history but no longer active.

Concrete entity values become canonical structured data only when the relevant system/entity is approved and represented as such; examples inside an approved architecture document are not automatically canon.

## Foundation files in this PR

- `PROJECT_STATE.md` — current proposal snapshot, unknowns and next gate.
- `ROADMAP.md` — risk-reduction gates from pre-production to production.
- `DECISIONS.md` — proposed architecture/governance decisions plus product hypotheses.
- `CONTRIBUTING.md` — proposed branch, PR, commit and review workflow.
- `docs/MASTER_ARCHITECTURE.md` — durable system-boundary proposal plus clearly marked candidate models.
- `docs/CANON_AND_DATA_POLICY.md` — proposed ownership between docs/data/contracts/code/prompts.
- `docs/ASSET_STORAGE_POLICY.md` — proposed binary/generated/3D storage rules.

Directories such as `data/`, `schemas/`, `simulator/`, `prompts/` and detailed domain folders will be added only when their first real artifacts exist. Serialization/schema technology, stable-ID format and asset-registry naming will be selected from real requirements rather than assumed now.

## Proposed development flow after Phase 0

```text
Product Vision + targeted evidence
          ↓
identify/refine core experience and assumptions
          ↓
AS SOON AS a high-risk assumption is testable
          ↓
cheapest credible prototype/test
          ↓
minimum world / taxonomy / visual work required by retained product
          ↓
representative end-to-end proof
          ↓
scale only after evidence
```

A prototype/test may start during Product Vision itself if that is the fastest credible way to reduce uncertainty.

## Current rule while reviewing Phase 0

Do not expand the universe/content library yet. First accept or revise the foundation; then move into evidence-backed Product Vision and testing rather than silently treating existing game/lore ideas as settled.
