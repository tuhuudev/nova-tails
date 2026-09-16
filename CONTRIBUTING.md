# Contributing to NOVA TAILS

NOVA TAILS is currently a small, AI-assisted project, but repository discipline should scale without adding enterprise ceremony too early.

## Source-of-truth rule

`main` represents the latest reviewed canonical project state.

Chat, AI output, sketches and experiments are proposals until reviewed and merged into the repository.

## Branch strategy

Use short-lived branches with one reviewable purpose.

```text
main
├── design/<topic>-vX.Y       # product/game/world/design decisions
├── feature/<topic>           # executable product features/prototypes
├── character/<id-or-name>    # character-specific canonical work
├── balance/<topic>           # balance/simulation changes
├── asset/<topic>             # asset standards/pipeline work
├── tooling/<topic>           # validators/generators/automation
├── fix/<topic>               # corrections
└── chore/<topic>             # repository maintenance
```

Examples:

- `design/product-vision-v0.1`
- `design/core-loop-v0.1`
- `design/world-architecture-v0.1`
- `feature/combat-prototype`
- `character/nt-org-fox-001-momo`
- `tooling/canon-validator`

Do not create permanent `develop`, `ai`, or per-person branches unless the team/workflow later demonstrates a real need.

## Pull requests

Every significant canonical change should use a PR.

A PR should:

1. solve one coherent problem;
2. state what changed;
3. state what remains uncertain;
4. list affected systems/assets;
5. identify validation performed;
6. update `DECISIONS.md` when a high-impact decision changes;
7. update `PROJECT_STATE.md` when project status/next step changes.

Draft PRs are preferred while a decision is still being explored.

## Canon status

Use:

`IDEA → DRAFT → REVIEW → APPROVED → LOCKED`

Use `DEPRECATED` for superseded material.

- `APPROVED` means accepted as current direction.
- `LOCKED` is stronger: downstream work may rely on it and changing it requires explicit impact review.

Do not lock placeholder balance numbers or untested manufacturing dimensions.

## Commit convention

Prefer Conventional-Commit-style prefixes:

- `docs:` documentation/canon prose
- `feat:` executable feature
- `fix:` bug/correction
- `balance:` balance-data change
- `asset:` asset/pipeline change
- `tooling:` tooling/automation
- `chore:` maintenance
- `refactor:` structural code change without behavior intent
- `test:` tests/validation

Keep commits understandable; do not commit unrelated generated files together with a design decision.

## Repository boundaries

```text
docs/       Human-readable rationale, rules and explanation
data/       Machine-readable canonical instances
schemas/    Machine-readable validity/contracts
prototypes/ Disposable or exploratory playable proofs
simulator/  Balance/combat simulation
src/        Production application/game code when introduced
tools/      Validators, generators and project automation
prompts/    AI prompt templates derived from canon
assets/     Approved or working binary/source assets under asset policy
```

The repository should not create empty directory trees merely to look complete. Add a directory when its first real file is needed.

## AI-assisted changes

AI may research, draft, generate and validate proposals, but must:

1. read relevant current canon before proposing changes;
2. preserve `LOCKED` fields unless the change explicitly targets them;
3. mark assumptions/placeholders;
4. avoid silently creating canon;
5. update dependencies when an approved decision changes;
6. never treat generated imagery or prompts as authoritative identity data.

## Review checklist

Before merge:

- [ ] Scope is coherent and reviewable.
- [ ] No brainstorm is accidentally presented as locked fact.
- [ ] Terminology is consistent with current architecture.
- [ ] Relevant ADR/decision entry is updated.
- [ ] Relevant project state is updated.
- [ ] Machine-readable data conforms to schemas once schemas exist.
- [ ] Binary/generated files comply with asset policy.
- [ ] No secrets, credentials or local environment files are committed.
- [ ] Validation/test evidence is recorded where applicable.

## Merge policy

Prefer squash merge for focused design/documentation PRs so `main` remains readable. A different method may be used later for code PRs if preserving individual commits becomes valuable.

After merge, delete short-lived branches unless they are intentionally retained for an active stacked dependency.
