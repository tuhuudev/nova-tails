# NOVA TAILS — Adapter Contracts v0.1

**Status:** REVIEW

Adapters translate an approved/reviewed character identity into a medium. They are consumers, not independent character authorities.

## Common adapter manifest

Every retained adaptation should be able to answer:

```yaml
adapter_id: <lane>/<character-id>
character_id: NT-CHAR-001
character_revision: 0.1
master_design_revision: null
adapter_version: 0.1
lane: game | print | card-2d | content
preserved_invariants: []
allowed_transformations: []
validation: {}
deliverables: []
```

This is an illustrative contract; YAML is not yet mandated as the permanent storage format.

## Game adapter

May change:
- polygon density/LOD;
- topology required for deformation;
- animation exaggeration;
- VFX and presentation;
- collision/technical helpers.

Must preserve:
- identity-critical silhouette relationships at gameplay/readable distances where applicable;
- signature feature semantics;
- critical asymmetry/orientation;
- character identity revision traceability.

Validation candidates:
- thumbnail/game-camera recognition;
- rig/deformation does not destroy signature;
- LOD retains critical read;
- no gameplay implementation silently becomes canon identity.

## Print adapter

May change:
- part segmentation;
- wall/feature thickness;
- pose for stability/support reduction;
- connectors and keyed assembly;
- micro-detail simplification;
- color boundaries to physically separable components where appropriate.

Must preserve:
- dominant silhouette;
- signature geometry;
- identity-critical asymmetry;
- proportion relationships unless a documented manufacturing exception exists.

Validation candidates:
- slicer/manifold checks;
- build-volume fit;
- minimum feature/wall checks after empirical calibration;
- real print and assembly test before manufacturing rules are promoted to standards;
- recognizable assembled result.

No tolerance value is canon until physically tested.

## Card / 2D adapter

May change:
- pose;
- camera/lens/composition;
- expression;
- lighting;
- environmental VFX;
- crop and graphic layout.

Must preserve:
- signature geometry visibility or an explicit justified exception;
- core proportion language;
- critical material/palette cues when approved as identity-critical;
- recognizable silhouette in at least one primary presentation asset.

Validation candidates:
- character remains recognizable without nameplate;
- VFX does not replace signature design;
- generated variants do not drift into incompatible anatomy.

## Content adapter

May derive:
- short video;
- social image;
- story snippets;
- design/print process content;
- promotional variations.

Must preserve:
- identity facts from approved context;
- visual contract when depicting the character;
- provenance of generated assets when retained.

Content must not create new canon by repetition. New lore/design proposals return upstream through normal review.

## Dependency impact

When an upstream character/master revision changes an invariant, all dependent adapters are considered **potentially stale** until reviewed.

Compatible upstream refinements may be accepted without regeneration if the adapter is demonstrably unaffected.

Automation for dependency impact is deferred. v0.1 requires the relationship to be explicit and reviewable first.
