# NOVA TAILS — Adapter Contracts v0.1

**Status:** REVIEW

Adapters translate a reviewed character identity/master design into a medium. They are consumers, not independent character authorities.

## Common manifest

Every retained adaptation must record at least:

```text
adapter_id
character_id
character_revision
master_design_revision (when applicable)
adapter_version
lane: game | print | card-2d | content
preserved_invariants[]
allowed_transformations[]
validation{}
deliverables[]
```

The contract is semantic; a permanent serialization format is not mandated yet.

## Game adapter

May change polygon density/LOD, deformation topology, animation exaggeration, VFX, collision and technical helpers.

Must preserve identity-critical silhouette relationships at useful viewing distance, signature semantics, critical asymmetry/orientation and upstream revision traceability.

Validation candidates: gameplay-camera recognition, rig/deformation preservation, LOD readability, and confirmation that gameplay implementation has not silently become canon identity.

## Print adapter

May change part segmentation, thickness, pose for stability/support reduction, connectors/keying, micro-detail and physically separable color boundaries.

Must preserve dominant silhouette, signature geometry, critical asymmetry and proportion relationships unless a documented manufacturing exception is approved.

Validation candidates: manifold/slicer checks, build-volume fit, empirical feature/wall checks, real print/assembly test, recognizable assembled identity. No tolerance value becomes a standard before physical testing.

## Card / 2D adapter

May change pose, camera/composition, expression, lighting, environmental VFX, crop and graphic layout.

Must preserve signature visibility (or document a justified exception), core proportion language, identity-critical material/palette cues, and recognizable identity.

Validation candidates: recognition without nameplate, VFX does not replace signature design, generated variants do not drift into incompatible anatomy.

## Content adapter

May derive short video, social imagery, story snippets, design/print-process material and promotional variants.

Must preserve approved identity facts and visual contract when depicting the character. Content does not create canon by repetition; new lore/design proposals return upstream for review.

## Dependency impact

When an upstream revision changes an invariant, every dependent adapter becomes **potentially stale** until reviewed. Compatible refinements may remain valid when demonstrably unaffected.

Automation is deferred; v0.1 first makes dependency relationships explicit and reviewable.
