# Asset Dependency & Versioning v0.1

**Status:** REVIEW

## Dependency graph

```text
Character Identity (L0)
        ↓
Master Design (L1)
        ↓
Adapter Manifest (L2)
        ↓
Deliverables (L3)
```

Each downstream retained object records the upstream revision it consumed.

## Change classes

### Identity-breaking
Changes topology, critical silhouette relationship, signature semantics or another declared invariant. Requires major identity revision and impact review of all adapters.

### Compatible master refinement
Improves geometry/reference/material definition while preserving identity invariants. Requires minor revision and targeted adapter impact review.

### Adaptation-only
Changes medium implementation without changing upstream identity: print split, rig, LOD, composition, export settings. Revises the adapter/deliverable only.

## Staleness rule

If an adapter declares dependency on identity `1.1` and identity moves to `2.0`, that adapter is potentially stale until reviewed. A version mismatch is a review signal, not automatic proof that regeneration is required.

## Provenance

Retained sources should record enough provenance to answer: what upstream version was used, what tool/person produced the retained result, and what validation occurred. Do not store unnecessary personal data.

## Deferred

Automated dependency graphing, checksums, content-addressed storage, registry service and exact SemVer tooling are deferred until the one-character reference proof demonstrates need.
