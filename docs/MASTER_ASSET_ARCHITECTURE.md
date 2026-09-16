# NOVA TAILS — Master Asset Architecture v0.1

**Status:** REVIEW  
**Purpose:** Define one authoritative character identity/design source that can be adapted into game, printable, card/2D and content outputs without each lane reinventing the character.

## 1. Strategic direction

NOVA TAILS will test a **Character/IP-first asset system**. The IP asset system is the platform; game, print, card/2D and content are consumers/adapters.

This does **not** mean all output lanes must ship, nor that cross-output leverage has been validated. It means that when two outputs represent the same character, they must depend on the same master identity/design contract.

## 2. Core rule: one identity, many adaptations

Single source of truth does not mean one universal binary file.

A production game mesh, printable model and card illustration have different technical constraints. They may use different geometry and files while preserving the same identity contract.

The architecture separates:

- **L0 — IP Canon:** what the character is;
- **L1 — Master Design:** shared visual/design source;
- **L2 — Adaptations:** medium-specific interpretations;
- **L3 — Deliverables:** exported/published artifacts.

Only reviewed L0/L1 changes may intentionally redefine identity. L2/L3 consumers must not silently redefine it.

## 3. Layer responsibilities

### L0 — IP Canon

Stable semantic identity:
- character ID and lifecycle state;
- identity premise;
- body/topology family;
- silhouette invariants;
- signature feature(s);
- personality anchors;
- palette/material intent where identity-critical;
- evolution continuity rules;
- relationships/world references when approved.

L0 should remain compact. Gameplay stats, STL tolerances and social captions do not belong here.

### L1 — Master Design

Shared design reference used by adaptations:
- canonical proportions and landmark ratios;
- approved silhouette/turnaround references;
- signature geometry definition;
- material-zone map;
- palette tokens;
- master geometry only when it becomes useful;
- design notes explaining what may and may not change.

L1 is not automatically a production-ready game mesh or printable mesh.

### L2 — Adaptations

Each lane consumes L0/L1 and adds medium-specific constraints.

**Game adapter** may add rig, animation, VFX, collision, LOD, stats and skill presentation.

**Print adapter** may split parts, thicken features, add connectors, change unsupported poses and simplify details while preserving identity invariants.

**Card/2D adapter** may add pose, camera, composition and VFX while preserving signature and proportions within approved variation.

**Content adapter** may create video, social images, stories and promotional derivatives from approved identity/design context.

### L3 — Deliverables

Published/exported artifacts such as:
- game bundles/models/textures;
- STL/3MF and print profiles;
- PNG/WebP/card exports;
- video/audio/social deliverables.

Deliverables are reproducible outputs where practical, not authoritative identity sources.

## 4. Dependency direction

```text
IP Canon (L0)
    |
Master Design (L1)
    |
    +----------+----------+----------+
    |          |          |          |
  Game       Print      Card/2D    Content     (L2)
    |          |          |          |
 exports     STL/3MF    images      media       (L3)
```

Dependencies flow downward. An adapter may submit a proposed upstream change, but must not mutate upstream identity implicitly.

## 5. Character package contract

A character package is addressed by a stable ID. A future package may conceptually expose:

```text
character/<id>/
  identity
  visual-contract
  evolution-contract
  references
```

Do not create empty per-character trees before a real retained character exists.

Minimum master identity fields are defined in `schemas/character-identity.schema.json`.

## 6. Identity invariants vs adaptable properties

Every retained character must explicitly distinguish:

**Invariant** — changing it risks creating a different identity.
Examples: topology, dominant silhouette relationship, signature geometry, critical asymmetry.

**Adaptable** — may change by medium within constraints.
Examples: pose, facial expression, polygon count, printable segmentation, animation exaggeration, lighting.

**Derived** — generated from another source and should not be edited as authority.
Examples: thumbnails, game LODs, STL exports, rendered card crops.

This distinction prevents asset drift.

## 7. Provenance and versions

Every retained master/adaptation should eventually record:
- stable asset/character ID;
- source layer;
- lifecycle state;
- version;
- upstream dependency/version;
- creator/tool provenance where useful for rights/reproducibility;
- validation status;
- output-specific constraints.

Versioning rule for v0.1:
- identity-breaking semantic change -> new major identity revision;
- compatible refinement -> minor revision;
- regenerated/export-only artifact -> deliverable revision without redefining identity.

Exact SemVer automation is deferred until real assets prove the required granularity.

## 8. Adapter contract

Every adapter must declare:
1. upstream character identity revision;
2. master-design revision if used;
3. invariants it must preserve;
4. transformations it is allowed to make;
5. output-specific validation gates;
6. generated deliverables.

See `docs/ADAPTER_CONTRACTS.md`.

## 9. Validation gates

A cross-output reference character is successful only if:
- identity remains recognizable across selected outputs;
- signature feature survives adaptation;
- medium constraints do not require hidden identity rewrites;
- a change in master identity can be traced to affected adapters;
- derived output does not become an accidental competing source of truth.

This validates architecture, not market demand.

## 10. Repository implementation policy

Current repo responsibilities remain:
- `docs/` rationale/contracts;
- `data/` canonical structured instances when real retained data exists;
- `schemas/` machine validation contracts;
- `assets/` intentionally retained binary/source/output assets under asset policy;
- `tools/` validation/generation automation when repetition justifies it;
- `prompts/` derived AI instructions only.

Do not introduce a large empty `canon/master-assets/adaptations` tree yet. First prove the contract with one reference character.

## 11. Reference-character proof

Use exactly one reference identity after selecting/revising an experiment character. Build the smallest useful proof across at least two materially different adapters; preferred stress test is **2D + print**, with a lightweight game representation as a third lane only if useful.

The proof should answer:
- what must remain invariant?
- what legitimately changes by medium?
- can dependencies be tracked without duplication?
- does the master contract help AI/human production stay coherent?

Do not scale roster until this proof exposes and resolves architecture weaknesses.

## 12. Explicit non-goals v0.1

Not decided here:
- game mechanics or economy;
- gacha;
- final lore taxonomy;
- final file formats for DCC tools;
- Git LFS strategy;
- exact 3D connector/tolerance standard;
- final asset registry technology;
- final serialization language for every data family;
- which output lane becomes the first commercial product.
