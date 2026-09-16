# NOVA TAILS — Master Asset Architecture v0.1

**Status:** REVIEW  
**Purpose:** Define one authoritative character identity/design source that can feed game, printable, card/2D and content outputs without each lane reinventing the character.

## Strategic direction

NOVA TAILS will test a **Character/IP-first asset system**. The IP asset system is the platform; game, print, card/2D and content are consumers/adapters.

This does not mean every lane must ship, and it does not claim cross-output leverage has been validated. It means that whenever multiple outputs represent the same retained character, they depend on the same reviewed identity/design contract.

## Core rule — one identity, many adaptations

Single source of truth does **not** mean one universal binary file. A game mesh, printable model and illustration have different constraints and may use different geometry/files while preserving the same identity contract.

Architecture layers:

- **L0 — IP Canon:** what the character is.
- **L1 — Master Design:** shared visual/design source.
- **L2 — Adaptations:** medium-specific interpretations.
- **L3 — Deliverables:** exported/published artifacts.

Dependencies flow downward. L2/L3 may propose upstream changes through review, but must never silently redefine L0/L1.

## L0 — IP Canon

Keep compact and semantic:
- stable character ID and lifecycle state;
- identity premise;
- personality anchors;
- body/topology family;
- silhouette invariants;
- signature features and critical asymmetry;
- identity-critical material/palette intent when needed;
- evolution continuity rules when approved;
- approved world/relationship references.

Gameplay stats, STL tolerances, captions and export settings do not belong here.

## L1 — Master Design

Shared design reference:
- canonical proportion/landmark rules;
- approved silhouette and turnaround references;
- signature geometry definition;
- material-zone map and palette tokens;
- master geometry only when useful;
- explicit allowed/forbidden variation notes.

L1 is not automatically a production-ready game mesh or printable mesh.

## L2 — Adaptations

Each adapter consumes L0/L1 and adds medium constraints.

- **Game:** rig, animation, VFX, LOD, collision and gameplay presentation.
- **Print:** part splits, thickness, connectors, stable pose and manufacturability simplification.
- **Card/2D:** pose, camera, composition, expression and VFX.
- **Content:** video/social/story/promotional derivatives using approved identity context.

## L3 — Deliverables

Examples: game bundles, STL/3MF, print profiles, PNG/WebP, card exports and media files. Deliverables are derived outputs, not identity authority.

## Asset property classes

Every retained character distinguishes:

1. **Invariant** — changing it risks changing identity: topology, dominant silhouette relationship, signature geometry, critical asymmetry.
2. **Adaptable** — medium may change within constraints: pose, expression, polygon count, print segmentation, animation exaggeration, lighting.
3. **Derived** — generated/exported from upstream and should not become authority: thumbnails, LODs, STL exports, rendered crops.

## Character package contract

A retained character is addressed by stable ID. Do not create empty character trees before a real retained character exists. Minimum machine-readable fields are defined by `schemas/character-identity.schema.json`.

## Dependency and version model

Every retained master/adaptation should identify:
- character/asset ID;
- source layer;
- lifecycle state;
- revision;
- upstream character/master revision;
- provenance when useful for rights/reproducibility;
- validation state;
- medium constraints.

v0.1 revision semantics:
- identity-breaking semantic change → new major identity revision;
- compatible refinement → minor revision;
- regenerated/export-only change → adaptation/deliverable revision without redefining identity.

Exact automated SemVer/registry technology is deferred until real assets demonstrate the needed granularity.

## Adapter contract

Every adapter declares:
1. upstream character revision;
2. master-design revision when used;
3. invariants it preserves;
4. allowed transformations;
5. validation gates;
6. generated deliverables.

See `docs/ADAPTER_CONTRACTS.md`.

## AI context rule

AI must receive a derived context assembled from reviewed L0/L1 plus the target adapter contract. Prompts and generated outputs are never the source of truth. Proposed identity changes must return upstream for review rather than being silently accepted because an AI output repeated them.

## Repository implementation

Continue existing responsibilities:
- `docs/` — rationale/contracts;
- `data/` — real structured canonical/adaptation instances;
- `schemas/` — machine contracts;
- `assets/` — intentionally retained binaries under asset policy;
- `tools/` — validators/generators when repetition justifies them;
- `prompts/` — derived AI instructions only.

Do not introduce a large empty `canon/master-assets/adaptations` tree. Prove the contract with one reference character first.

## Reference-character proof gate

Use exactly one reference identity and build the smallest useful proof across at least two materially different adapters. Preferred stress test: **2D + print**; a lightweight game representation may be added later if useful.

The architecture passes only if:
- identity remains recognizable across selected outputs;
- signature feature survives adaptation;
- medium constraints do not require hidden identity rewrites;
- upstream revision impact can be traced to adapters;
- a derived output does not become a competing source of truth.

This validates architecture, not market demand.

## Non-goals v0.1

Not decided here: game mechanics/economy, gacha, final lore taxonomy, final DCC formats, Git LFS strategy, exact 3D tolerance/connector standard, final asset-registry technology, or which output lane becomes the first commercial product.
