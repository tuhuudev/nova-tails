# NT-001 / PYROX — Asset Intake and 3D Handoff v0.1

**Status:** REVIEW / intake pending binary import  
**Date:** 2026-09-16  
**Character record:** `data/characters/NT-001/character.json`  
**Asset manifest:** `data/assets/NT-001.asset-manifest.json`

## Source-of-truth audit

| Concern | Authoritative location | Current state |
| --- | --- | --- |
| Character identity and candidate visual DNA | `data/characters/NT-001/character.json` | Present; `CANDIDATE`, v0.1.0 |
| Retained binary asset inventory | `data/assets/NT-001.asset-manifest.json` | Present; six records, all `MISSING_LOCAL` |
| Binary asset root | `assets/characters/NT-001/` | Prepared; no binaries imported |
| Project/product gate | `PROJECT_STATE.md`, `ROADMAP.md` | Test A / Product Vision remains open |

The reported Library set includes a selected concept, a production reference v1.0, an orthographic candidate, and front/left/back reference. Those binary files were not available in the local clone, so this repository records their expected destinations and provenance without claiming that they have been imported, approved as canon, or checksum-verified.

The existing character JSON identifies the concept path `assets/characters/NT-001/concept/NT-001_concept_v001.png`; that binary is also absent. It is retained in the manifest as the current candidate reference rather than silently replacing it with a differently named file.

## Naming and version rules

- Use `NT001_<ROLE>_v<major>.<minor>.<patch>.<extension>` for newly imported reference assets. Preserve a legacy/source filename only when it is the retained source itself.
- Each asset ID is permanent within the manifest; a filename/version change creates a new record or explicit supersession, not an overwrite.
- Record SHA-256 and import date after local import. A manifest entry with `MISSING_LOCAL` is not a usable production input.
- `character.json` is the identity record. The manifest is the binary index. A render, prompt, or generated variation cannot override either.

## Proposed 3D sequence — blocked until project gate

The Library orthographic was reportedly marked for a 3D blockout, but the repository's current Product Vision gate still prohibits production-scale 3D work. Once that gate explicitly retains the physical/3D pillar, use this minimal sequence:

```text
verified reference import → scale/anatomy review → editable blockout (.blend)
→ silhouette review against candidate DNA → print adaptation/part split
→ slicer profile + physical test → validation record
```

For a future first blockout, capture: Blender version, unit scale, reference file SHA-256, source file path, review date, and a neutral pose/render. Do not commit temporary exports or declare printable dimensions as canonical until a physical validation test exists.

## Intake checklist

- [ ] Obtain the six source binaries from the Library/export.
- [ ] Import each at its manifest destination without overwriting a verified retained asset.
- [ ] Calculate SHA-256 and mark each imported record `PRESENT_UNVERIFIED`.
- [ ] Visually compare the concept, production sheet, and orthographic; document any contradictions with the candidate JSON.
- [ ] Explicitly decide whether Test A/Product Vision permits the NT-001 3D blockout.
- [ ] If permitted, create the source-3D record before making derivative prints/exports.
