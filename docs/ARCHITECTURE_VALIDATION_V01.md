# Master Asset Architecture v0.1 — Internal Validation

**Status:** READY FOR REVIEW

## Contract checks

- [x] One-way authority L0 → L1 → L2 → L3 is explicit.
- [x] Single source of truth is semantic/design authority, not one universal binary.
- [x] Invariant vs adaptable vs derived properties are explicit.
- [x] Character Identity has a machine-readable schema.
- [x] Adapter Manifest has a machine-readable schema.
- [x] Game, Print, Card/2D and Content transformation boundaries are documented.
- [x] Upstream revision/staleness semantics are documented.
- [x] AI context is downstream of reviewed sources.
- [x] One reference fixture exists without being promoted to production canon.
- [x] Card/2D and Print manifests declare the same upstream identity.
- [x] Minimal validator + CI workflow are included.

## Deliberately unresolved

- [ ] L1 master-design values: must emerge from a reviewed visual source/proof.
- [ ] Actual Card/2D representative visual.
- [ ] Actual printable geometry/slice/assembly evidence.
- [ ] Physical connector/tolerance values.
- [ ] Market demand / desirability beyond P01 exploratory evidence.

## Gate result

**Architecture definition: PASS FOR PR REVIEW.**

This result means the v0.1 contract is coherent enough to merge and test with real assets. It does not mean the cross-output proof, physical manufacturability, character desirability or commercial product are validated.
