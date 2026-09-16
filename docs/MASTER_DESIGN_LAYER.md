# Master Design Layer v0.1

**Status:** REVIEW

L1 Master Design bridges semantic identity (L0) and medium adapters (L2). It should contain shared visual information only when that information is genuinely reusable across media.

For the `NT-CHAR-001` reference fixture, L1 should eventually define:
- core-to-orbit proportion ranges;
- orbit segment count/placement constraints only if identity-critical;
- approved silhouette/turnaround reference;
- broken-orbit geometry and negative-space intent;
- material-zone relationship;
- explicit variation envelope.

Do **not** invent these values merely to fill a schema. The current fixture intentionally has `master_design_revision: null` until a reviewed visual source exists.

This is a deliberate architecture test: adapters may initially depend directly on L0, and introduction of L1 must be justified by shared requirements discovered while creating the 2D + print proof.
