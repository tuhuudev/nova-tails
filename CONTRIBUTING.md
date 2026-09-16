# Contributing to NOVA TAILS

NOVA TAILS is currently a small, AI-assisted project, but repository discipline should scale without adding enterprise ceremony too early.

## Source-of-truth rule

The repository is the authoritative project record after review. `main` represents the latest **reviewed baseline**, not a claim that every line is locked canon. `DRAFT`/`REVIEW` material may be retained on `main` as visible hypotheses/TODOs.

`APPROVED` means an accepted current decision/direction. Concrete entity facts become canonical when the relevant entity/system is approved and represented as canonical data. `LOCKED` is a stronger dependency contract.

Chat, AI output, sketches and experiments are proposals until intentionally captured and reviewed through repository workflow.

## Branch strategy

Use short-lived branches with one reviewable purpose.

```text
main
├── design/<topic>-vX.Y
├── feature/<topic>
├── character/<id-or-name>
├── balance/<topic>
├── asset/<topic>
├── tooling/<topic>
├── fix/<topic>
└── chore/<topic>
```

Examples: `design/product-vision-v0.1`, `design/core-loop-v0.1`, `feature/combat-prototype`, `character/nt-org-fox-001-momo`, `tooling/canon-validator`.

Do not create permanent `develop`, `ai`, or per-person branches unless the team/workflow later demonstrates a real need.

## Pull requests

Every significant change to reviewed project state should normally use a PR. A PR should solve one coherent problem, state scope/out-of-scope, preserve uncertainty, identify affected areas and validation/evidence, and update `DECISIONS.md` / `PROJECT_STATE.md` when appropriate.

Draft PRs are preferred while a decision is still being explored.

## Lifecycle status

`IDEA → DRAFT → REVIEW → APPROVED → LOCKED`; use `DEPRECATED` for superseded material.

- `IDEA`, `DRAFT`, `REVIEW`: not active canon.
- `APPROVED`: accepted current decision/direction.
- `LOCKED`: downstream dependency contract; changing it requires explicit impact review.
- `DEPRECATED`: no longer active.

Do not lock placeholder balance numbers or untested manufacturing dimensions.

## Commit convention

Prefer Conventional-Commit-style prefixes: `docs:`, `feat:`, `fix:`, `balance:`, `asset:`, `tooling:`, `chore:`, `refactor:`, `test:`.

Keep commits understandable; do not commit unrelated generated files together with a design decision.

## Repository boundaries

```text
docs/       Human-readable rationale, rules, hypotheses and decisions
data/       Machine-readable structured/canonical instances when needed
schemas/    Machine-readable validity/contracts
prototypes/ Disposable or exploratory playable proofs
simulator/  Balance/combat simulation when needed
src/        Production application/game code when introduced
tools/      Validators, generators and project automation
prompts/    AI prompt templates derived from reviewed context
assets/     Intentionally retained binary/source assets under asset policy
```

Do not create empty directory trees merely to look complete. Add a directory when its first real file is needed.

## AI-assisted changes

AI may research, draft, generate and validate proposals, but must read relevant repository state, distinguish approved/locked decisions from hypotheses, preserve locked constraints unless explicitly changed, mark assumptions/placeholders, update affected dependencies and never treat generated imagery/prompts as authoritative identity data.

## Review checklist

Before merge:
- [ ] Scope is coherent and reviewable.
- [ ] No brainstorm is accidentally presented as approved/locked fact.
- [ ] Terminology is consistent with current reviewed architecture.
- [ ] Relevant ADR/decision and project state are updated.
- [ ] Structured data conforms to schemas once schemas exist.
- [ ] Binary/generated files comply with asset policy.
- [ ] No secrets, credentials or local environment files are committed.
- [ ] Validation/test evidence is recorded where applicable.

## Merge policy

Prefer squash merge for focused design/documentation PRs so `main` remains readable. A different method may be used later for code PRs if preserving individual commits becomes valuable.

After merge, delete short-lived branches unless intentionally retained for an active stacked dependency.
