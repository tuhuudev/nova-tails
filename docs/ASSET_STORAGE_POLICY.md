# NOVA TAILS — Asset Storage Policy v0.1

**Status:** REVIEW

## Goal

Keep Git useful as the project grows from text/design files into source art, renders, 3D models and printable packages.

## Current policy

During Architecture and early prototype phases:

- keep docs, structured data, schemas and code in normal Git;
- avoid committing disposable AI generations and local exports;
- commit only binary assets that are intentionally part of project history/review;
- do not enable Git LFS merely because the project may need it later.

## Asset classes

### Canon/source assets
Examples: approved master artwork, source 3D model, production texture/source file.

These may eventually use Git LFS or external object storage when size/history justifies it.

### Derived assets
Examples: thumbnails, renders, game-ready exports, STL/3MF generated from a source model.

Prefer reproducible generation where practical. Do not version every temporary export.

### Exploration assets
AI generations, discarded concepts, slicer previews and temporary test renders should not automatically enter Git history.

Important exploration/reference outputs may be retained selectively with a clear purpose.

## Future asset registry

Production assets should receive stable IDs and dependency links, for example:

```text
CHR-NT-ORG-FOX-001
CARD-NT-ORG-FOX-001-F01-001
PORTRAIT-NT-ORG-FOX-001-001
MODEL-NT-ORG-FOX-001-MASTER-001
PRINT-NT-ORG-FOX-001-F01-001
VFX-WIND-001
```

Exact naming will be reviewed before production asset scale-up.

## Git LFS gate

Introduce Git LFS only after we have representative real files and can answer:

- which extensions are large;
- average/maximum sizes;
- how often source binaries change;
- who needs to clone them;
- whether GitHub LFS quota/cost is acceptable;
- whether external object storage would be better for generated outputs.

Likely future LFS candidates may include large source 3D/art files, but no extension is automatically approved today.

## Physical-print artifacts

For a printable character, distinguish:

```text
MASTER DESIGN
→ SOURCE 3D MODEL
→ PRINT ADAPTATION
→ PARTS
→ STL/3MF EXPORT
→ SLICER PROFILE / TEST
→ PHYSICAL VALIDATION RESULT
```

A generated STL is not proof of manufacturability. Print constraints become canonical only after documented physical validation.

## Do not commit

- local caches;
- editor/IDE state;
- OS metadata;
- temporary render directories;
- slicer caches;
- credentials/API keys;
- large unreviewed generation batches;
- duplicate exports such as `final_final_v2`.

## Scaling trigger

Revisit this policy at the Physical Asset Proof milestone, before multiple characters begin producing large binary histories.
