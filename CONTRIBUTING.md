# Contributing to NOVA TAILS

NOVA TAILS is currently a small, AI-assisted project, but repository discipline should scale without adding enterprise ceremony too early.

## Source-of-truth rule

`main` represents the latest **reviewed baseline**, not a claim that every line is locked canon. Only material explicitly marked `APPROVED` or `LOCKED` is canonical. `DRAFT`/`REVIEW` material may be retained on `main` when it is useful to preserve visible hypotheses/TODOs.

Chat, AI output, sketches and experiments are proposals until intentionally captured and reviewed through repository workflow.

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

Every significant change to reviewed project state should normally use a PR.

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

- `IDEA`, `DRAFT`, `REVIEW`: not canonical.
- `APPROVED`: accepted current canon/direction.
- `LOCKED`: downstream work may rely on it; changing it requires explicit impact review.
- `DEPRECATED`: no longer active canon.

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
assets/     Intentionally retained binary/source assets under asset policy
```

The repository should not create empty directory trees merely to look complete. Add a directory when its first real file is needed.

## AI-assisted changes

AI may research, draft, generate and validate proposals, but must:

1. read relevant current repository state before proposing changes;
2. distinguish approved/locked canon from draft hypotheses;
3. preserve `LOCKED` fields unless the change explicitly targets them;
4. mark assumptions/placeholders;
5. avoid silently creating canon;
6. update dependencies when an approved decision changes;
7. never treat generated imagery or prompts as authoritative identity data.

## Review checklist

Before merge:

- [ ] Scope is coherent and reviewable.
- [ ] No brainstorm is accidentally presented as approved/locked fact.
- [ ] Terminology is consistent with current reviewed architecture.
- [ ] Relevant ADR/decision entry is updated.
- [ ] Relevant project state is updated.
- [ ] Machine-readable data conforms to schemas once schemas exist.
- [ ] Binary/generated files comply with asset policy.
- [ ] No secrets, credentials or local environment files are committed.
- [ ] Validation/test evidence is recorded where applicable.

## Merge policy

Prefer squash merge for focused design/documentation PRs so `main` remains readable. A different method may be used later for code PRs if preserving individual commits becomes valuable.

After merge, delete short-lived branches unless they are intentionally retained for an active stacked dependency.
