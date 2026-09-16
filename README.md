# NOVA TAILS

> Working title. Original-IP project exploring a collectible-character game universe, reusable 2D identity and modular FDM-printable 3D collectibles.

## Current phase

**Phase 0 — Repository & Architecture Foundation (v0.1)**

The repository is the source of truth for reviewed project decisions. Chat/AI outputs are proposals until reviewed and promoted through repository workflow.

The exact game/product direction is still being validated. Do not read current gameplay/lore hypotheses as finished canon.

## Project principles

1. Architecture before mass content production.
2. Validate product/core gameplay before building a large roster.
3. One master character identity feeds game, 2D and 3D adaptations.
4. AI generates proposals; it does not directly define canon.
5. Every important decision is reviewable and traceable.
6. 3D standards must ultimately come from real manufacturing tests.
7. Every game system should create a meaningful decision or serve a clear product purpose.
8. Avoid premature complexity in schemas, storage, branching and content volume.

## Canon status

- `IDEA` — exploratory.
- `DRAFT` — being designed.
- `REVIEW` — ready for explicit review.
- `APPROVED` — accepted current direction.
- `LOCKED` — dependency contract; changing it requires impact review.
- `DEPRECATED` — retained for history but no longer current.

## Repository map

Current foundation files:

- `PROJECT_STATE.md` — current project snapshot, unknowns and next gate.
- `ROADMAP.md` — gated pre-production → validation → production roadmap.
- `DECISIONS.md` — high-impact architecture/design decisions.
- `CONTRIBUTING.md` — branch, PR, commit and review workflow.
- `docs/MASTER_ARCHITECTURE.md` — high-level system boundaries/hypotheses.
- `docs/CANON_AND_DATA_POLICY.md` — ownership between docs/data/schema/code/prompts.
- `docs/ASSET_STORAGE_POLICY.md` — binary/generated/3D storage rules.

Directories such as `data/`, `schemas/`, `simulator/`, `prompts/` and detailed domain folders will be added when their first real artifacts exist. We intentionally avoid empty architecture theater.

## Development sequence

After Phase 0 is reviewed and merged:

```text
Product Vision
→ Core Loop
→ World Architecture
→ Character Taxonomy
→ Visual Bible
→ Combat Prototype
→ Mathematical Combat Model
→ Vertical Slice
→ Simulation / Physical Asset Proof
→ Scale only after validation
```

Each major step should normally use a dedicated short-lived branch and focused PR.

## Current rule

Do not expand the universe because AI makes generation cheap. Expand only after the relevant design/game/asset assumptions survive review or testing.
