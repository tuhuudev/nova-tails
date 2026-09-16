# NOVA TAILS — Canon & Data Policy v0.1

**Status:** REVIEW

## Purpose

Prevent documentation, game data, AI prompts, generated assets and implementation code from becoming conflicting sources of truth as the project grows.

## Ownership model

```text
DECISIONS / BIBLES          explain WHY
        ↓
CANON DATA                  records WHAT IS TRUE
        ↓
SCHEMAS                     define WHAT IS VALID
        ↓
IMPLEMENTATION              defines executable behavior
        ↓
OUTPUTS                     game UI / 2D / 3D / content
```

Prompts consume this chain. They do not sit above it.

## Directory responsibilities

### `docs/`
Human-readable intent, rationale, rules, design constraints and ADRs.

A prose document may describe a concept before machine-readable data exists. Once a canonical entity is represented in `data/`, the entity's concrete values should be read from data rather than duplicated inconsistently across many docs.

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
Validation contracts for canonical data. Schemas should be introduced together with the first real structured-data slice, not invented in exhaustive detail before we know what the prototype needs.

### `prompts/`
Reusable generation instructions built from canon/context. Prompt templates may specify presentation or generation technique but must not redefine character/world/game facts.

### `assets/`
Binary/source/output assets. Asset files require stable registry IDs once production-scale asset work begins.

### `src/`, `simulator/`, `tools/`
Executable behavior. If code reveals ambiguity in a design rule, resolve the ambiguity in canon/design rather than silently letting implementation become a contradictory specification.

## Canonical entity rule

Every production entity should eventually have:

- stable ID;
- lifecycle status;
- schema version;
- entity version where useful;
- provenance/review state;
- dependencies/references;
- locked identity fields where appropriate.

Example character identity:

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

This is an example contract shape, not yet canonical MOMO data.

## Evolution inheritance

Evolution forms should inherit base identity and store deltas instead of duplicating the complete character.

Conceptually:

```text
BASE CHARACTER
  ↓ inherit
FORM-01
FORM-02
FORM-03
```

Each form can record `ADD`, `REMOVE`, `MODIFY`, and `KEEP_LOCKED` semantics once the schema is designed.

## Change propagation

A canonical change must identify affected downstream systems.

Example:

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

- `IDEA`: exploration only; may live outside canonical data.
- `DRAFT`: represented but unstable.
- `REVIEW`: candidate ready for explicit review.
- `APPROVED`: current canonical direction.
- `LOCKED`: downstream dependency contract; changing it requires impact analysis.
- `DEPRECATED`: retained for history/migration but no longer active.

## Versioning

Use project versioning pragmatically rather than forcing semantic versioning onto every note.

For canonical assets/entities where version matters:

- PATCH: correction that preserves identity/contract;
- MINOR: compatible detail/addition;
- MAJOR: identity/contract-changing redesign.

Schema versions are independent of asset versions.

## No premature schema complexity

Architecture v0.1 should define this policy but should **not** attempt to model every future field.

The first real schemas should be extracted from the vertical-slice needs. Candidate first schemas:

1. Character
2. Skill
3. Enemy/Boss
4. Equipment

Economy/campaign schemas follow only when those systems are actually prototyped.

## Conflict resolution

When two sources disagree:

1. `LOCKED` reviewed decision/data wins over draft material.
2. Newer `APPROVED` ADR supersedes older approved ADR when explicitly marked.
3. Canonical structured data wins for concrete entity values once established.
4. Docs explain intent; update them if they contradict approved data.
5. Prompt/generated output never overrides canon.
6. Implementation differences must be surfaced and reconciled, not silently accepted.
