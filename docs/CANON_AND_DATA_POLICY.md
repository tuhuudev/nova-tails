# NOVA TAILS — Canon & Data Policy v0.1

**Status:** REVIEW

## Purpose

Prevent documentation, structured data, AI prompts, generated assets and implementation code from becoming conflicting sources of truth as the project grows.

## Reviewed baseline vs canon

The repository records both reviewed decisions and explicitly retained hypotheses. `main` is the latest **reviewed baseline**.

Lifecycle semantics:

- `IDEA`, `DRAFT`, `REVIEW`: not active canon.
- `APPROVED`: accepted current decision/direction; downstream design may rely on it, but it may still contain rules rather than concrete entity facts.
- `LOCKED`: stronger dependency contract; changes require explicit impact review.
- `DEPRECATED`: superseded/no longer active.

Concrete entity values become canonical data only when the relevant system/entity is approved and represented as such. An approved architecture principle does not magically make every example underneath it canonical.

## Ownership model

```text
APPROVED / LOCKED DECISIONS   explain WHY / constraints
        ↓
APPROVED CANON DATA           records concrete WHAT IS TRUE
        ↓
SCHEMAS                       define WHAT IS VALID
        ↓
IMPLEMENTATION                executes reviewed contracts
        ↓
OUTPUTS                       UI / 2D / 3D / content
```

Prompts consume this chain. They do not sit above it.

## Directory responsibilities

### `docs/`
Human-readable intent, rationale, rules, design constraints and ADRs. Docs may contain explicitly marked non-canonical hypotheses/examples.

Once a canonical entity is represented in `data/`, concrete entity values should be read from data rather than duplicated inconsistently across many docs.

### `data/`
Machine-readable canonical/approved instances, introduced when systems become stable enough to benefit from structured data. Draft prototype data may also live here later if its status is explicit and tooling benefits from it.

Candidate future structure may include characters, abilities, equipment, enemies/encounters, factions and world data, but no exhaustive tree is approved yet.

### `schemas/`
Validation contracts for structured data. Schemas should be extracted from the first real data slice rather than exhaustively predicted now.

### `prompts/`
Reusable generation instructions built from reviewed canon/context. Prompt templates may specify presentation/generation technique but must not redefine project facts.

### `assets/`
Intentionally retained binary/source/output assets under asset-storage policy. Stable registry IDs become useful when production-scale assets begin multiplying.

### `src/`, `simulator/`, `tools/`
Executable behavior. If implementation reveals ambiguity in a design rule, surface and reconcile it rather than silently allowing code to become contradictory canon.

## Entity identity principle

Production entities should eventually carry only metadata proven useful, likely including stable ID, lifecycle status, schema version, dependencies/references and locked identity fields where appropriate.

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

This is not canonical MOMO data or a final schema.

## Inheritance principle

If forms/evolution remain part of the product, forms should inherit base identity and store meaningful deltas rather than independently duplicating/reinventing the character. Exact representation is deferred until real data exists.

## Change propagation

An approved/locked change should identify affected downstream systems. Dependency automation is future tooling; during early phases this is a PR-review responsibility.

## Versioning

Use versioning pragmatically rather than forcing semantic versioning onto every note.

For assets/entities where version semantics become useful:
- PATCH: correction preserving identity/contract;
- MINOR: compatible detail/addition;
- MAJOR: identity/contract-changing redesign.

Schema versions are independent of asset versions.

## No premature schema complexity

Architecture v0.1 defines policy but intentionally does **not** model every future field. First schemas should come from working prototype/vertical-slice needs.

## Conflict resolution

When sources disagree:

1. `LOCKED` reviewed decision/data wins over lower-status material unless explicitly being changed.
2. A newer `APPROVED` decision can supersede an older one only when the relationship is explicit.
3. Approved structured data wins for concrete entity values once established.
4. Docs explain intent; update them if they contradict approved data.
5. Prompt/generated output never overrides canon.
6. Implementation differences must be surfaced and reconciled, not silently accepted.
