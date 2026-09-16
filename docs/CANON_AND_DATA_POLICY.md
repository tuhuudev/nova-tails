# NOVA TAILS — Canon & Data Policy v0.1

**Status:** REVIEW — proposed until Phase 0 is accepted.

## Purpose

Prevent documentation, structured data, AI prompts, generated assets and implementation code from becoming conflicting sources of truth as the project grows.

## Accepted baseline vs canon

After this policy is accepted, `main` is the latest accepted baseline and may contain explicitly retained hypotheses.

Lifecycle semantics:
- `IDEA`, `DRAFT`, `REVIEW`: not active canon.
- `APPROVED`: accepted current decision/direction; may be a rule rather than a concrete entity fact.
- `LOCKED`: stronger dependency contract; changes require explicit impact review.
- `DEPRECATED`: superseded/no longer active.

Concrete entity values become canonical data only when the relevant system/entity is approved and represented as such. An approved architecture principle does not make every example underneath it canonical.

## Ownership model

```text
APPROVED / LOCKED DECISIONS   explain WHY / constraints
        ↓
APPROVED CANON DATA           records concrete WHAT IS TRUE
        ↓
VALIDATION CONTRACTS          define WHAT IS VALID
        ↓
IMPLEMENTATION                executes accepted contracts
        ↓
OUTPUTS                       UI / 2D / 3D / content
```

Prompts consume this chain. They do not sit above it.

## Directory responsibilities

### `docs/`
Human-readable intent, rationale, rules, design constraints and ADRs. Docs may contain explicitly marked non-canonical hypotheses/examples.

### `data/`
Machine-readable structured/canonical instances, introduced when systems become stable enough to benefit from them. Exact serialization format is intentionally undecided until tooling/prototype needs make the trade-off real.

### `schemas/`
Validation contracts for structured data. Schema technology/format should be selected together with the first real data/tooling slice rather than predicted now.

### `prompts/`
Reusable generation instructions built from accepted canon/context. Prompt templates may specify presentation/generation technique but must not redefine project facts.

### `assets/`
Intentionally retained binary/source/output assets under asset-storage policy. Stable registry IDs become useful when production-scale assets begin multiplying.

### implementation / simulator / tools
Executable behavior. If implementation reveals ambiguity in a design rule, surface and reconcile it rather than silently allowing code to become contradictory canon.

## Identity / entity principle

Production entities should eventually carry only metadata proven useful. Stable-ID format, versioning details and exact data shape are intentionally deferred until Product Vision/taxonomy/prototype work provides real requirements.

If forms/evolution remain part of the product, forms should inherit base identity and store meaningful deltas rather than independently duplicating/reinventing identity. Exact representation is deferred.

## Change propagation

An approved/locked change should identify affected downstream systems. Dependency automation is future tooling; during early phases this is a PR-review responsibility.

## No premature schema complexity

Phase 0 defines policy but intentionally does **not** model future fields or select serialization/schema technology prematurely. First contracts should come from working prototype/representative-slice needs.

## Conflict resolution

When accepted sources disagree:
1. `LOCKED` decision/data wins over lower-status material unless explicitly being changed.
2. A newer `APPROVED` decision can supersede an older one only when the relationship is explicit.
3. Approved structured data wins for concrete entity values once established.
4. Docs explain intent; update them if they contradict approved data.
5. Prompt/generated output never overrides canon.
6. Implementation differences must be surfaced and reconciled, not silently accepted.
