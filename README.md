# NOVA TAILS

> Working title. Current product hypothesis: a distinctive original multi-species sci-fi/fantasy universe/IP, initially explored through character-centric concepts, with potential game, 2D and modular FDM-printable 3D adaptations. Product Vision still needs to validate audience, differentiation, primary product and output priorities. Originality/IP risk requires review; it is not guaranteed by AI generation.

## Current phase

**Phase 0 — Repository & Architecture Foundation (v0.1)**

The repository is the authoritative project record after review. The `main` branch represents the latest reviewed baseline. `APPROVED` marks accepted current decisions/directions; `LOCKED` marks stronger dependency contracts. Draft/review hypotheses may remain visible on `main` without becoming active canon.

Chat/AI outputs are proposals until reviewed and intentionally captured through repository workflow.

## Project principles

1. Architecture before mass content production.
2. Validate product/core interaction before building a large content library.
3. When an identity/character spans outputs, one master identity should feed its adaptations.
4. AI generates proposals; it does not directly define canon.
5. Every important decision is reviewable and traceable.
6. Manufacturing standards must come from real physical tests if printable collectibles remain in scope.
7. Every system layer should create a meaningful decision or serve a clear product purpose.
8. Avoid premature complexity in schemas, storage, branching and content volume.
9. Use research/prototypes/tests to attack high-risk assumptions early rather than treating the roadmap as waterfall.
10. Treat originality and third-party-rights risk as something to validate, not something AI can guarantee.

## Lifecycle status

- `IDEA` — exploratory.
- `DRAFT` — being designed; not active canon.
- `REVIEW` — ready for explicit review; not active canon yet.
- `APPROVED` — accepted current decision/direction.
- `LOCKED` — dependency contract; changing it requires impact review.
- `DEPRECATED` — retained for history but no longer active.

Concrete entity values become canonical data only when the relevant system/entity is approved and represented as such; examples inside an approved architecture document are not automatically canon.

## Repository map

Current foundation files:
- `PROJECT_STATE.md` — current project snapshot, unknowns and next gate.
- `ROADMAP.md` — risk-reduction gates from pre-production to production.
- `DECISIONS.md` — high-impact architecture/design decisions and hypotheses.
- `CONTRIBUTING.md` — branch, PR, commit and review workflow.
- `docs/MASTER_ARCHITECTURE.md` — durable system boundaries plus clearly marked candidate models.
- `docs/CANON_AND_DATA_POLICY.md` — ownership between docs/data/schema/code/prompts.
- `docs/ASSET_STORAGE_POLICY.md` — binary/generated/3D storage rules.

Directories such as `data/`, `schemas/`, `simulator/`, `prompts/` and detailed domain folders will be added when their first real artifacts exist. We intentionally avoid empty architecture theater.

## Development sequence

After Phase 0:

```text
Product Vision + targeted evidence
→ Core Experience / Loop
→ identify highest-risk assumption
→ cheapest credible prototype/test
→ minimum world / taxonomy / visual work needed by retained product
→ structured data / math when behavior is known
→ vertical slice
→ simulation / physical proof only for retained pillars
→ scale only after validation
```

The prototype can move earlier whenever it answers a critical unknown faster than documentation. Each major change should normally use a dedicated short-lived branch and focused PR.

## Current rule

Do not expand the universe because AI makes generation cheap. Expand only after the relevant product/design/game/asset assumptions survive review or testing.
