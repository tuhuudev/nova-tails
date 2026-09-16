# NOVA TAILS — Asset Dependency & Versioning v0.1

**Status:** REVIEW

## Dependency model

An adaptation pins the character revision it was reviewed against.

```text
NT-CHAR-001@0.1
  -> card-2d/NT-CHAR-001@0.1
  -> print/NT-CHAR-001@0.1
```

A future master-design revision may sit between identity and adapters when shared visual source assets exist.

## Change classes

### Compatible refinement
Clarifies or improves a non-invariant without changing identity-critical meaning.

Effect: adapters are reviewed for impact; regeneration is not automatic.

### Identity-impacting change
Changes topology, signature geometry, critical asymmetry or another declared invariant.

Effect: dependent adapters become potentially stale and must be reviewed/rebuilt before claiming compatibility.

### Adapter-only change
Changes medium implementation while preserving pinned upstream invariants.

Effect: increments adapter revision only.

### Deliverable-only change
Re-export/compression/build packaging with no semantic or adapter change.

Effect: deliverable revision only; upstream authority unchanged.

## Why no complex registry yet

A dependency graph with two adapters can be reviewed manually. We should add registry tooling only when repeated real assets make manual tracing error-prone.

## Future automation trigger

Introduce a validator/impact tool when at least one of these becomes true:
- multiple retained characters have multiple adapters;
- upstream changes repeatedly require manual dependency searches;
- CI needs to reject stale/missing adapter references;
- prompts/builds are generated automatically from manifests.

Until then, explicit IDs/revisions in structured manifests are sufficient.
