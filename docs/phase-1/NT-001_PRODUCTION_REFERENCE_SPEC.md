# NT-001 Production Reference Specification v0.1

**Purpose:** create reference assets that can support consistent 3D authoring. Character-bible art is input evidence, not authoritative geometry.

## 1. Cross-view package

Required neutral views:
- front
- left side
- right side
- back
- top
- bottom
- optional 3/4 only as interpretation aid

### Alignment rules
All orthographic production views must:
- represent the same Stage-1 design revision;
- use a neutral standing pose;
- use an orthographic/flat reference presentation, not perspective hero composition;
- share one ground line and declared scale;
- align major landmarks: top of ears, eyes, nose, shoulder, hip, paws, tail root;
- preserve identical marking placement and part count;
- avoid environmental lighting that hides geometry;
- separate elemental glow from physical body geometry.

AI-generated views that violate alignment remain concept references and must not be promoted to production reference.

## 2. Landmark sheet

Record normalized landmarks after the first aligned pack exists:
- overall height excluding optional FX;
- body length nose → rump;
- head width/height/depth;
- ear height/base width/thickness target;
- eye center spacing;
- shoulder/hip height;
- paw footprint;
- tail-root location;
- tail maximum envelope;
- forehead mark center/size.

Do not invent millimeter dimensions from an illustration. Choose final physical scale during 3D/print feasibility and derive measurements consistently.

## 3. Anatomy/detail pack

Required detail references:
- head/muzzle construction;
- eye/eyelid construction;
- ear outer/inner construction;
- forehead mark;
- neck/chest fur masses;
- front paw;
- rear paw;
- back marking;
- tail root and split structure;
- flame-like silhouette layers;
- mouth/teeth/tongue if animation requires them.

## 4. Material specification

Separate physical material regions from rendered effects:

`MAT_FUR_BASE`, `MAT_EMBER_PRIMARY`, `MAT_GOLD_SECONDARY`, `MAT_FLAME_ACCENT`, `MAT_EYE`, plus `FX_FIRE` as non-body presentation unless deliberately modeled.

For each approved material later record:
- base color;
- roughness intent;
- metallic intent (normally non-metal for fur);
- opacity/transmission only when justified;
- print-color mapping separately from render material.

## 5. 3D authoring target

Editable authoring master should support:
- clean body geometry;
- separate eyes/mouth internals as needed;
- UV/material assignment;
- future quadruped rig;
- ear and split-tail deformation;
- facial expression solution (bones and/or morphs);
- named FX anchors;
- derivation of both runtime and print masters.

Suggested scene hierarchy:

```text
NT001_ROOT
├── GEO
│   ├── BODY
│   ├── EYES
│   ├── TEETH
│   ├── TONGUE
│   └── FX_GEO_OPTIONAL
├── RIG
├── MORPHS
├── MATERIALS
└── FX_ANCHORS
    ├── MOUTH
    ├── FOREHEAD
    ├── TAIL_L
    └── TAIL_R
```

## 6. Runtime derivation

Runtime export is derived from the authoring master. Validate:
- scale/orientation;
- normals/tangents;
- material mapping;
- skeleton/root;
- skin weights;
- morphs required by target;
- animation clips;
- texture references;
- visual comparison with approved reference.

Do not optimize away signature features merely to reduce complexity; document any compromise.

## 7. Print derivation

Print master may intentionally differ from runtime geometry while preserving identity.

Review:
- ear thickness;
- paw/leg robustness;
- center of mass;
- tail self-support/attachment;
- thin flame tips;
- seam placement;
- connector geometry;
- material/color part boundaries;
- support/orientation implications.

Tolerance and minimum printable features are calibration outputs, not Character DNA constants.

## 8. Promotion gates

`concept reference` → cross-view review → `production reference candidate` → modeling test → corrections → `approved production reference`.

The reference pack is approved only when a modeler can reconstruct the intended form without resolving major contradictions by guesswork.
