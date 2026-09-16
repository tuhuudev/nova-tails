# Schema Validation Expectation

CI runs `python tools/validate_asset_contracts.py` when schemas/structured asset data change.

Expected v0.1 fixtures:
- `data/characters/NT-CHAR-001.reference.json` → character identity schema PASS;
- `data/adapters/NT-CHAR-001.card-2d.reference.json` → adapter manifest schema PASS;
- `data/adapters/NT-CHAR-001.print.reference.json` → adapter manifest schema PASS.

CI success verifies structural contract conformance only, not semantic quality or production readiness.
