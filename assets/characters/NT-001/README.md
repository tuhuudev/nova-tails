# NT-001 / PYROX — retained-asset intake

This directory is the local binary root for NT-001. The structured character candidate remains in `data/characters/NT-001/character.json`; the inventory and import state are in `data/assets/NT-001.asset-manifest.json`.

Expected layout:

```text
concept/       Selected concept source
reference/     Production reference sheet and per-view reference
turnaround/    Orthographic source
source-3d/     Editable 3D source once a blockout is permitted
print/         Deliberately retained manufacturing exports and validation evidence
```

No binary file is checked in yet. Import a supplied file only at its manifest path, calculate and record its SHA-256, and retain its review status. Do not replace an existing approved binary with a generated variation.

`source-3d/` and `print/` are intentionally deferred. The current roadmap requires Product Vision/Test A review before the proposed 3D blockout becomes active production work.
