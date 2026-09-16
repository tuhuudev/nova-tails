# NOVA TAILS — Canon & Data Policy v0.1

**Status:** REVIEW

## Purpose

Prevent documentation, structured data, AI prompts, generated assets and implementation code from becoming conflicting sources of truth as the project grows.

## Reviewed baseline vs canon

The repository records both reviewed decisions and explicitly retained hypotheses. `main` is therefore the latest **reviewed baseline**.

Only material with lifecycle status `APPROVED` or `LOCKED` is active canon. `IDEA`, `DRAFT` and `REVIEW` are not canon even when their files are present on `main`.

## Ownership model

```text
APPROVED DECISIONS / BIBLES  explain WHY / constraints
        ↓
CANON DATA                  records concrete WHAT IS TRUE
        ↓
SCHEMAS                     define WHAT IS VALID
        ↓
IMPLEMENTATION              executes reviewed contracts
        ↓
OUTPUTS                     game UI / 2D / 3D / content
```

Prompts consume this chain. They do not sit above it.

## Directory responsibilities

### `docs/`
Human-readable intent, rationale, rules, design constraints and ADRs. Docs may contain explicitly marked non-canonical hypotheses.

Once a canonical entity is represented in `data/`, concrete entity values should be read from data rather than duplicated inconsistently across many docs.

### `data/`
Machine-readable canonical instances, introduced when systems become stable enough to benefit from structured data.

Candidate future structure:

```text
data/
├── characters/
├── skills/
├── equipment/
├── enemies/
├── bosses/
├── factions/
└── world/
```

Do not populate this tree with speculative bulk data during Architecture v0.1.

### `schemas/`
Validation contracts for canonical/structured data. Schemas should be extracted from the first real structured-data slice rather than exhaustively predicted now.

### `prompts/`
Reusable generation instructions built from reviewed canon/context. Prompt templates may specify presentation/generation technique but must not redefine character/world/game facts.

### `assets/`
Intentionally retained binary/source/output assets under asset-storage policy. Stable registry IDs become useful when production-scale assets begin multiplying.

### `src/`, `simulator/`, `tools/`
Executable behavior. If implementation reveals ambiguity in a design rule, surface and reconcile it rather than silently allowing code to become contradictory canon.

## Canonical entity rule

Every production entity should eventually have only the metadata that proves useful, likely including:

- stable ID;
- lifecycle status;
- schema version;
- entity/asset version where useful;
- dependencies/references;
- locked identity fields where appropriate.

Example shape only:

```yaml
id: NT-ORG-FOX-001
name: Momo
status: DRAFT
schema_version: 1
identity:
  origin_domain: Organic
  race: Beastkin
  species: Fox
locked_fields:
  - identity.species
```

This is not yet canonical MOMO data or a final schema.

## Evolution inheritance principle

If evolution remains part of the product, forms should inherit base identity and store meaningful deltas rather than independently duplicating/reinventing the character.

Conceptually:

```text
BASE CHARACTER
  ↓ inherit
FORM-01
FORM-02
FORM-03
```

Exact inheritance representation is deferred until real data exists.

## Change propagation

An approved canonical change should identify affected downstream systems.

Example only:

```text
Character Element changes
├── skills             REVIEW
├── VFX                REVIEW
├── card art           REVIEW
├── evolution          REVIEW
├── equipment synergy  REVIEW
├── base species       unaffected
└── print geometry     possibly unaffected
```

Dependency automation is future tooling. During early phases this is a PR-review responsibility.

## Status rules

- `IDEA`: exploration only; not canon.
- `DRAFT`: represented but unstable; not canon.
- `REVIEW`: candidate ready for explicit review; not canon yet.
- `APPROVED`: active canonical direction/data.
- `LOCKED`: active canon used as a downstream dependency contract; changing it requires impact analysis.
- `DEPRECATED`: retained for history/migration but no longer active canon.

## Versioning

Use versioning pragmatically rather than forcing semantic versioning onto every note.

For assets/entities where version semantics become useful:

- PATCH: correction preserving identity/contract;
- MINOR: compatible detail/addition;
- MAJOR: identity/contract-changing redesign.

Schema versions are independent of asset versions.

## No premature schema complexity

Architecture v0.1 defines policy but intentionally does **not** model every future field.

First schemas should come from working prototype/vertical-slice needs. Likely candidates are Character, Ability/Skill, Enemy/Boss and later Equipment, but even this order may change with prototype findings.

## Conflict resolution

When sources disagree:

1. `LOCKED` reviewed decision/data wins over lower-status material unless explicitly being changed.
2. Newer `APPROVED` ADR can supersede older approved ADR only when the relationship is explicit.
3. Approved structured data wins for concrete entity values once established.
4. Docs explain intent; update them if they contradict approved data.
5. Prompt/generated output never overrides canon.
6. Implementation differences must be surfaced and reconciled, not silently accepted.
