# NT-001 Production Reference QA v0.1

**Input:** Stage-1 Production Reference Pack candidate generated during Phase 1.
**Result:** CONDITIONAL FAIL for direct 3D authoring; PASS as design/production-planning reference.

## Decision summary

The sheet establishes a coherent Stage-1 direction and useful landmark/material language, but it is still a single AI-generated composite. Individual views are not authoritative orthographic projections and contain enough view-to-view interpretation that a modeler would still have to guess geometry.

## Component review

| Component | Result | Decision |
|---|---|---|
| Overall Stage-1 silhouette | PASS | Preserve compact quadruped + oversized ears + dominant rear tail mass. |
| EAR_SHAPE identity | PASS WITH CHANGE | Flame-like silhouette must be physical ear/fur geometry; emissive glow is optional FX. Exact inner/outer boundary must be normalized. |
| FOREHEAD_MARK | PASS | Keep centered diamond as surface identity. It must remain readable without emissive FX. |
| TAIL_SPLIT | PASS WITH CHANGE | Adopt one physical root that separates into two persistent flame-shaped lobes. This resolves prior ambiguity; exact root transition still needs aligned views. |
| Head/muzzle | PASS WITH CHANGE | Preserve short cute muzzle; normalize head depth and cheek volume between front/side. |
| Eyes | PASS | Amber/gold identity direction retained; exact eye geometry belongs to anatomy sheet. |
| Paws/legs | PASS WITH CHANGE | Maintain enlarged paws but avoid view-dependent paw size. Geometry must support later print robustness. |
| Back marking | HOLD | Not a signature feature. Keep candidate until it proves useful in back/3D readability. |
| Fire/glow | PASS WITH CHANGE | Treat as presentation/VFX layer, not required physical anatomy. |
| Palette | PASS AS CANDIDATE | Role separation is useful; exact color values require later visual approval. |
| Dimensions shown in sheet | REFERENCE ONLY | Normalized ratios are guidance, not measured truth. No real-world mm dimensions are canon. |
| Six-view orthographic claim | FAIL | Views are visually useful but cannot be treated as mathematically reconciled orthographic geometry. |

## Geometry decisions resolved by this review

### TAIL_TOPOLOGY
**Resolved for prototype:** one physical tail root → two persistent physical lobes/branches. Both lobes must exist with FX disabled. Tail identity is not merely an internal painted notch.

### EAR_PHYSICAL_BOUNDARY
**Resolved at rule level:** outer ear and inner flame-like shapes are physical/fur geometry. Glow/fire emission is optional presentation FX. Exact production contour remains to be reconciled in the dedicated orthographic pack.

### BACK_MARKING
Still unresolved/non-blocking. Do not promote to locked Visual DNA.

### FIGURE_SCALE
Still intentionally deferred until 3D blockout.

## Cross-view failures to prevent

Dedicated production views must correct these AI-composite risks:
1. ear width/depth changing between front, side and back;
2. tail lobe count/spacing changing by camera angle;
3. tail root being hidden or reinterpreted;
4. head depth and muzzle length drifting;
5. paw size/spacing changing between front and side;
6. markings moving relative to anatomy;
7. fur spikes being mistaken for hard geometric landmarks;
8. perspective distortion being presented as orthographic information.

## Promotion gate

The next pack must be generated/authored as **six individual neutral modeling references**, then reconciled against one normalized landmark contract. They remain CANDIDATE until cross-view QA passes.

Only after that pass may the project label the pack:

`APPROVED FOR 3D BLOCKOUT`

This approval does not imply CANON character status.
