#!/usr/bin/env python3
"""Minimal v0.1 validator for NOVA TAILS structured asset contracts.

Uses jsonschema when installed. The tool intentionally validates only real JSON
instances; it does not invent registry/version semantics beyond the schemas.
"""
from pathlib import Path
import json
import sys

try:
    from jsonschema import Draft202012Validator
except ImportError:
    print("jsonschema is required: pip install jsonschema", file=sys.stderr)
    raise SystemExit(2)

ROOT = Path(__file__).resolve().parents[1]
CHECKS = [
    (ROOT / "schemas/character-identity.schema.json", ROOT / "data/characters", "*.json"),
    (ROOT / "schemas/adapter-manifest.schema.json", ROOT / "data/adapters", "*.json"),
]

errors = 0
for schema_path, data_dir, pattern in CHECKS:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    for path in sorted(data_dir.glob(pattern)) if data_dir.exists() else []:
        instance = json.loads(path.read_text(encoding="utf-8"))
        found = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
        if found:
            errors += len(found)
            for err in found:
                loc = ".".join(map(str, err.path)) or "<root>"
                print(f"FAIL {path.relative_to(ROOT)}:{loc}: {err.message}")
        else:
            print(f"PASS {path.relative_to(ROOT)}")

raise SystemExit(1 if errors else 0)
