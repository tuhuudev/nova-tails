# NT-001 Blockout Projection Review v001

**Status:** CANDIDATE / projection review completed  
**Source model:** `assets/characters/NT-001/03_3d_source/master/NT001_BLOCKOUT_v001.blend`  
**Source reference:** `NT001-PRODREF-001`, SHA-256 `032a0abb8d580e8850d147ffff45ac0ba0b1ab5827ff79e658e5d51c71ecaccd`  
**Blender:** 5.1.2

## Scope

This is a primary-and-secondary-form reconciliation model. It does not approve a
sculpt, runtime mesh, print adaptation, real-world dimensions, or the candidate
character as canon.

## Required renders

All required renders are retained in `assets/characters/NT-001/11_validation/blockout/v001/renders/`:

- FRONT, LEFT, RIGHT, BACK, TOP and BOTTOM orthographic;
- 3/4 FRONT and 3/4 REAR clay.

## Projection findings

| Contract item | Result | Finding |
| --- | --- | --- |
| Bilateral body | PASS | Matched limb, eye and ear volumes use the same shared scene. |
| `EAR_SHAPE` | PASS FOR BLOCKOUT | Two large physical triangular ear volumes remain visible without material or FX. Flame/fur edge detail remains out of scope. |
| `FOREHEAD_MARK` | PASS FOR BLOCKOUT | Centered diamond guide reads in the front projection and is not emissive. |
| `TAIL_SPLIT` | PASS FOR BLOCKOUT | One root separates into two persistent, tapered physical lobes; the top and rear views make both lobes explicit. |
| Head / muzzle depth | PASS FOR BLOCKOUT | Short muzzle, large head and compact body reconcile across front and side views. |
| Paw contact | PASS FOR BLOCKOUT | Enlarged four-paw footprint reaches the ground plane. No print claim is made. |
| Wings / prohibited additions | PASS | None are present. |

## Non-blocking holds

- Ear internal flame layering and surface fur are deferred to sculpt/reference refinement.
- Back markings, exact palette, final figure scale, production topology and print part split remain unresolved by design.
- The generated reference pack remains candidate evidence, not authoritative orthography.

## Decision

`NT001-3D-BLOCKOUT-001` remains **CANDIDATE**. It has satisfied the required
render/object contract and has no unresolved identity-critical geometry conflict
at blockout detail. Promotion to `APPROVED_FOR_SCULPT` requires an explicit
project review decision; this document does not make that promotion.
