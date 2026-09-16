# NOVA TAILS

> Working title. Original-IP project exploring a distinctive character universe with potential game, 2D and modular FDM-printable 3D adaptations.

## Current phase

**Phase 0 — Repository & Architecture Foundation (v0.1)**

The repository is the source of truth for project history and reviewed decisions. The `main` branch represents the latest reviewed baseline; only content explicitly marked `APPROVED` or `LOCKED` is canonical. Draft material may still exist on `main` when intentionally retained as a visible hypothesis.

Chat/AI outputs are proposals until reviewed and promoted through repository workflow. The exact first product/game format and the role of physical 3D printing are still being validated.

## Project principles

1. Architecture before mass content production.
2. Validate product/core interaction before building a large roster.
3. When a character spans outputs, one master identity should feed game, 2D and 3D adaptations.
4. AI generates proposals; it does not directly define canon.
5. Every important decision is reviewable and traceable.
6. Manufacturing standards must come from real physical tests if printable collectibles remain in scope.
7. Every game system should create a meaningful decision or serve a clear product purpose.
8. Avoid premature complexity in schemas, storage, branching and content volume.
9. Use prototypes/tests to attack high-risk assumptions early rather than treating the roadmap as waterfall.

## Canon status

- `IDEA` — exploratory.
- `DRAFT` — being designed; not canon.
- `REVIEW` — ready for explicit review; not canon yet.
- `APPROVED` — accepted current canon/direction.
- `LOCKED` — dependency contract; changing it requires impact review.
- `DEPRECATED` — retained for history but no longer active canon.

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

After Phase 0 is reviewed and merged:

```text
Product Vision
→ Core Loop
→ Minimum World Architecture
→ Minimum Character Taxonomy
→ Visual Identity Proof
→ Interaction/Combat Prototype
→ Mathematical/Data Model
→ Vertical Slice
→ Simulation / Physical Asset Proof (if retained)
→ Scale only after validation
```

This is a risk/dependency sequence, not strict waterfall. A cheap prototype may move earlier if it answers a critical unknown faster than more documentation.

Each major step should normally use a dedicated short-lived branch and focused PR.

## Current rule

Do not expand the universe because AI makes generation cheap. Expand only after the relevant product/design/game/asset assumptions survive review or testing.
