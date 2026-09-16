# NOVA TAILS — Asset Storage Policy v0.1

**Status:** REVIEW

## Goal

Keep Git useful if the project grows from text/design files into source art, renders, game exports, 3D models or printable packages. The policy does not assume every asset class will remain in the final product.

## Current policy

During Architecture and early prototype phases:
- keep docs, structured data, contracts and code in normal Git;
- avoid committing disposable AI generations and local exports;
- commit only binary assets intentionally needed for project history/review;
- do not enable Git LFS merely because the project may need it later.

## Asset classes

### Canon/source assets
Examples may include approved master artwork, production source files or source 3D models if those outputs are retained. Large source assets may eventually use Git LFS or external object storage when representative size/history justifies it.

### Derived assets
Examples may include thumbnails, renders, game-ready exports or STL/3MF generated from a source model. Prefer reproducible generation where practical; do not version every temporary export.

### Exploration assets
AI generations, discarded concepts, previews and temporary test renders should not automatically enter Git history. Retain selected references only when they serve an explicit review/provenance purpose.

## Future asset registry

Introduce stable asset IDs/dependency links only when real production assets begin multiplying. ID/naming format must be designed from actual retained output types and lookup/migration needs rather than hypothetical catalogs.

## Git LFS gate

Introduce Git LFS only after representative real files exist and we can answer which extensions are actually large, typical/max size, change frequency, clone needs, quota/cost and whether external object storage is better for derived outputs. No file extension is automatically approved for LFS today.

## Physical-print artifacts — conditional

If Product Vision retains printable collectibles, distinguish source from derived/manufacturing evidence:

```text
MASTER IDENTITY/DESIGN
→ SOURCE 3D MODEL
→ PRINT ADAPTATION
→ PARTS
→ STL/3MF EXPORT
→ SLICER PROFILE / TEST
→ PHYSICAL VALIDATION RESULT
```

A generated STL is not proof of manufacturability. Print constraints become canonical only after documented physical validation.

## Do not commit

- local caches/editor/OS metadata;
- temporary render/export/slicer caches;
- credentials/API keys;
- large unreviewed generation batches;
- meaningless duplicate exports such as `final_final_v2`.

## Scaling trigger

Revisit this policy when representative large binary assets exist—particularly before production-scale art/3D work. If an output pillar is dropped from Product Vision, remove its storage complexity rather than preserving it for hypothetical future use.
