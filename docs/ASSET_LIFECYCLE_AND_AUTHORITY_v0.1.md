# NOVA TAILS — Asset Lifecycle & Authority v0.1

Status: PROTOTYPE
Date: 2026-09-16

## Why this exists
NOVA TAILS will produce many AI-assisted and manually authored variants. A visually polished asset must not become authoritative merely because it looks final or contains words such as APPROVED.

## Lifecycle

### EXPLORATION
Disposable or comparative creative work. May contradict other exploration assets.

### CANDIDATE
Selected direction worth evaluating. Must have identity/version/provenance when managed by the production system.

### VALIDATED
Passed a named validation for a defined purpose. Validation is scoped; passing visual recognition does not prove 3D, print, gameplay, or market feasibility.

### APPROVED
Authorized for a named downstream use. Always qualify approval where ambiguity exists, e.g. APPROVED_FOR_3D_BLOCKOUT.

### CANON
Authoritative IP/world/character decision intended to persist across outputs. Canon promotion requires an explicit project decision; generated text cannot self-promote.

## Authority hierarchy
When two assets disagree, use this order unless an explicit decision says otherwise:

1. Explicit project decision / canon record
2. Structured master character/system data
3. Validated production contract
4. Approved authoring master
5. Candidate reference asset
6. Exploration/generation output
7. Presentation text embedded in generated artwork

## Domain-specific approval
Approval is never universal by default.

Examples:
- APPROVED_FOR_3D_BLOCKOUT
- APPROVED_FOR_RUNTIME_EXPORT
- APPROVED_FOR_PRINT_TEST
- APPROVED_FOR_CONTENT

An asset can be approved for blockout while character name, element, lore, scale, or material remains candidate.

## Source-of-truth rule
AI is a producer, not the source of truth.

Generated image/video/3D output must reference upstream structured decisions. If generation invents names, stats, lore, anatomy, topology, abilities, dimensions, or status labels, those inventions remain non-authoritative until explicitly promoted.

## Dependency graph

World/System Rules
-> Character Data
-> Visual DNA
-> Master Design / Production Reference
-> 3D Authoring Master
-> Rig / Animation / Runtime / Print
-> Content / Marketing / Presentation

Downstream assets inherit; they do not silently redefine upstream data.

## Change propagation
When an upstream identity trait changes:
1. record the decision;
2. increment affected data/reference version;
3. mark dependent assets stale or requiring validation;
4. regenerate/re-author only impacted outputs;
5. re-run relevant gates.

## NT-001 current application
Locked prototype identity anchors:
- EAR_SHAPE
- FOREHEAD_MARK
- TAIL_SPLIT

Resolved-for-prototype geometry:
- ears carry identity in physical geometry; glow is optional;
- one physical tail root branches into two persistent physical lobes;
- forehead mark does not depend on glow;
- identity must survive a clay render with FX disabled.

Candidate/non-canon items include character naming, exact element treatment, species/family naming, rarity, final dimensions, lore, abilities, evolution names, and physical production values unless separately approved.

## Scaling rule
Before adding large character volume, demonstrate that this lifecycle survives:
- one full NT-001 vertical slice;
- at least one substantially different character through the same system;
- one upstream change propagating correctly without manual ambiguity.
