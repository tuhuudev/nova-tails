# NOVA TAILS — Asset Architecture v0.2

**Status:** PROTOTYPE

## Principle

AI is a producer, not the source of truth. A character is a versioned graph of structured identity, approved design sources, authoring masters and derived outputs.

```text
Character Data + Visual DNA
          │
          ├── Design Source
          └── Production Specification
                    ↓
              Authoring Master
                    ↓
      ┌─────────────┼─────────────┐
    Runtime        Print        Render/Content
```

## Source vs derived

### Source assets
- character/Visual DNA/evolution/skill data
- approved production reference
- editable 2D source where applicable
- editable 3D authoring master
- rig source
- animation source
- VFX source

### Derived assets
- GLB/FBX runtime exports
- optimized textures/LODs
- STL/3MF print exports
- card/social/marketing renders
- thumbnails/previews

Derived assets must point back to their source asset/version. They must not silently become new design masters.

## Character asset domains

```text
assets/characters/NT-001/
├── 00_manifest/
├── 01_reference/
│   ├── concept/
│   ├── orthographic/
│   ├── anatomy/
│   ├── proportions/
│   ├── expressions/
│   ├── poses/
│   ├── materials/
│   └── evolution/
├── 02_2d_master/
├── 03_3d_source/
│   ├── sculpt/
│   ├── retopo/
│   ├── uv/
│   ├── textures/
│   └── master/
├── 04_rig/
├── 05_animation/
├── 06_vfx/
├── 07_runtime/
│   ├── glb/
│   ├── fbx/
│   ├── textures/
│   └── lod/
├── 08_print/
│   ├── master/
│   ├── parts/
│   ├── connectors/
│   ├── stl/
│   ├── 3mf/
│   ├── slicer/
│   └── assembly/
├── 09_game/
├── 10_content/
└── 11_validation/
```

Empty folders do not need to be committed; manifests define expected locations until assets exist.

## Asset lifecycle

`EXPERIMENT → CANDIDATE → APPROVED → DEPRECATED`

`APPROVED` means approved for its declared purpose, not globally canonical for every downstream use.

Example: a concept can be approved as design evidence but still be unsuitable as orthographic modeling reference.

## Asset graph rules

Every managed production asset should have:
- globally unique `assetId` within NOVA TAILS;
- `characterId`;
- type/purpose;
- version;
- lifecycle status;
- source method;
- parent asset IDs;
- validation state;
- declared output path when retained;
- notes/provenance.

## Binary storage

Do not put every AI generation in Git. Retain selected evidence and approved assets according to Asset Storage Policy. As large binary volume grows, evaluate Git LFS or external object storage; manifests and structured metadata remain in normal Git.

## 3D authoring rule

Runtime and print exports are not authoring masters. Keep an editable DCC source (initial target: Blender-compatible authoring master), then derive runtime and print variants.

## Runtime branch

Authoring Master → runtime cleanup/optimization → rig/animation as required → GLB/engine export → validation.

## Print branch

Authoring Master → print-adapted master → part split → connectors → tolerances/calibration → STL/3MF → slicer → physical validation.

A rendered exploded view cannot pass physical feasibility.

## Skill branch

Skill logic and presentation are independent:

```text
Skill Definition
├── Logic
└── Presentation
    ├── animation
    ├── VFX
    ├── SFX
    └── icon/content
```

Balance values can change without rebuilding visual assets; presentation can change without redefining skill logic.

## Validation inheritance

Derived assets do not inherit approval blindly. A source reference approved for 2D identity does not automatically approve a generated 3D model, print mesh or runtime export. Each output has its own gate while retaining lineage to the source.
