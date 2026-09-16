# Contributing to NOVA TAILS

NOVA TAILS is currently a small, AI-assisted project, but repository discipline should scale without adding enterprise ceremony too early.

## Source-of-truth rule

The repository is the authoritative project record after review. `main` represents the latest reviewed baseline, not a claim that every line is locked canon. `DRAFT`/`REVIEW` material may be retained on `main` as visible hypotheses/TODOs.

`APPROVED` means an accepted current decision/direction. Concrete entity facts become canonical when the relevant entity/system is approved and represented as canonical data. `LOCKED` is a stronger dependency contract.

Chat, AI output, sketches and experiments are proposals until intentionally captured and reviewed through repository workflow.

## Branch strategy

Use short-lived branches with one reviewable purpose:

```text
main
├── design/<topic>-vX.Y
├── feature/<topic>
├── character/<slug-or-id-when-defined>
├── balance/<topic>
├── asset/<topic>
├── tooling/<topic>
├── fix/<topic>
└── chore/<topic>
```

Examples such as `design/product-vision-v0.1` or `feature/combat-prototype` illustrate branch syntax; they do not approve the underlying product decision. Do not create permanent `develop`, `ai`, or per-person branches unless the team/workflow later demonstrates a real need.

## Pull requests

Every significant change to reviewed project state should normally use a PR. Keep scope coherent, state out-of-scope and uncertainty, identify affected areas/evidence, and update decisions/project state when appropriate. Draft PRs are preferred while a decision is still being explored.

## Lifecycle status

`IDEA → DRAFT → REVIEW → APPROVED → LOCKED`; use `DEPRECATED` for superseded material. Do not lock placeholder balance numbers or untested manufacturing dimensions.

## Commit convention

Prefer Conventional-Commit-style prefixes: `docs:`, `feat:`, `fix:`, `balance:`, `asset:`, `tooling:`, `chore:`, `refactor:`, `test:`.

Keep commits understandable; do not commit unrelated generated files together with a design decision.

## Repository boundaries

```text
docs/       Human-readable rationale, rules, hypotheses and decisions
data/       Machine-readable structured/canonical instances when needed
schemas/    Validity/contracts when needed
prototypes/ Disposable or exploratory proofs
simulator/  Simulation when needed
src/        Production application/game code when introduced
tools/      Validators, generators and automation
prompts/    AI prompt templates derived from reviewed context
assets/     Intentionally retained binary/source assets under asset policy
```

Exact serialization/schema technology is intentionally undecided until real prototype/tooling requirements exist. Do not create empty directory trees merely to look complete.

## AI-assisted changes

AI may research, draft, generate and validate proposals, but must read relevant repository state, distinguish approved/locked decisions from hypotheses, preserve locked constraints unless explicitly changed, mark assumptions/placeholders, update affected dependencies and never treat generated imagery/prompts as authoritative identity data.

## Review checklist

Before merge:
- [ ] Scope is coherent and reviewable.
- [ ] No brainstorm is accidentally presented as approved/locked fact.
- [ ] Terminology is consistent with current reviewed architecture.
- [ ] Relevant ADR/decision and project state are updated.
- [ ] Structured data conforms to contracts once contracts exist.
- [ ] Binary/generated files comply with asset policy.
- [ ] No secrets, credentials or local environment files are committed.
- [ ] Validation/test evidence is recorded where applicable.

## Merge policy

Prefer squash merge for focused design/documentation PRs so `main` remains readable. A different method may be used later for code PRs if preserving individual commits becomes valuable. Delete short-lived branches after merge unless intentionally retained for an active dependency.
