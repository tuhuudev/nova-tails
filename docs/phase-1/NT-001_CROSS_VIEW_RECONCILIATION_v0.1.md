# NT-001 Cross-view Reconciliation v0.1

**Input:** generated Stage-1 orthographic reference sheet and six extracted candidate panels.
**Status:** FAIL FOR AUTHORITATIVE ORTHOGRAPHY / PASS FOR 3D BLOCKOUT INPUT WITH CONSTRAINTS.

## Why

The pack is substantially clearer than the earlier Character Bible and resolves the intended one-root/two-lobe tail structure. However, the six panels originate from one AI-generated composite rather than projections of one shared 3D volume. They therefore cannot be treated as measured orthographic truth.

## Reconciliation matrix

| Area | Front↔Back | Left↔Right | Side↔Top/Bottom | Result |
|---|---|---|---|---|
| Ear identity | recognizable | recognizable | depth not authoritative | BLOCKOUT OK |
| Head width/depth | broadly coherent | minor interpretation risk | depth must be solved in blockout | BLOCKOUT OK |
| Muzzle | front identity clear | side length approximate | n/a | BLOCKOUT OK |
| Torso | compact identity clear | length approximate | width/depth approximate | BLOCKOUT OK |
| Legs/paws | readable | proportions vary slightly | footprint not measured | BLOCKOUT OK |
| Tail root | rear intent clearer | partially obscured in side | top/bottom are interpretive | NEED 3D SOLVE |
| Two tail lobes | clear in rear/top/bottom | silhouette overlaps in side | coherent as concept | BLOCKOUT OK |
| Forehead mark | clear | location readable | visible from top conceptually | BLOCKOUT OK |
| Back marking | inconsistent authority | n/a | candidate only | HOLD |

## Authoritative rules for blockout

When a generated view conflicts with another view, use this priority:

1. `production-reference.v0.1.json` geometry contract (currently version 0.2.0 internally);
2. locked Visual DNA (`EAR_SHAPE`, `FOREHEAD_MARK`, `TAIL_SPLIT`);
3. front view for frontal identity and width relationships;
4. side views for body/head depth and body length;
5. back view for tail root and two-lobe relationship;
6. top/bottom only as secondary envelope references;
7. decorative fur spikes/markings are non-authoritative unless separately locked.

## Blockout constraints

The first 3D blockout must be deliberately simple:
- no detailed fur sculpt;
- no emissive/fire FX;
- no texture-dependent identity;
- no detailed claws/teeth;
- no production topology requirement yet;
- one physical tail root splitting into two physical lobes;
- large triangular physical ears;
- centered forehead diamond may be represented as a simple surface marker;
- bilateral body symmetry unless a reviewed exception is introduced.

## Blockout QA renders required

Render the same blockout with orthographic cameras:
- FRONT
- LEFT
- RIGHT
- BACK
- TOP
- BOTTOM
- 3/4 FRONT clay
- 3/4 REAR clay

Then compare those projections back to the reference pack. Unlike AI-generated views, these eight renders will all come from one geometry and become the first genuinely reconciled cross-view evidence.

## Decision

Do **not** promote the AI reference pack itself to authoritative orthography.

Proceed to `3D BLOCKOUT v0.1` because remaining inconsistencies are exactly the class of ambiguity a shared 3D volume is intended to resolve. Promote a later reference/model pair only after blockout projection review.
