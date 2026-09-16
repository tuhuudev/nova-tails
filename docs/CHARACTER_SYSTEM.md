# NOVA TAILS — Character System v0.1

**Status:** PROTOTYPE

## Purpose

Define the minimum structured identity required for a NOVA TAILS creature to remain consistent across concept art, evolution, future combination mechanics, 3D, game data and content.

## Core model

A character is not an image. It is an identity with stable data and linked assets.

```text
CHARACTER
├── Identity
├── Classification
├── Visual DNA
├── Traits
├── Evolution
├── Asset Manifest
└── Production Metadata
```

## Identity

- `id`: immutable project identifier such as `NT-001`
- `name`: working or canon name
- `version`: semantic design-data version
- `status`: `concept | prototype | validated | production`

Names and presentation can change without changing the character ID.

## Classification

Prototype fields:
- family
- species
- element(s)
- rarity
- evolution stage

Vocabulary remains provisional until validated by Product Vision and real character work.

## Visual DNA

Visual DNA stores recognition-critical design information separately from a render.

Minimum categories:
- silhouette
- proportions
- head/body/limbs/tail anatomy
- surface/pattern language
- color roles
- signature features
- immutable/mutable traits

A character should normally have 2–4 high-value signature features rather than many equally important motifs.

## Trait inheritance

Each evolution-relevant visual trait uses one of four rules:

- `LOCKED` — must remain recognizable
- `EVOLVABLE` — may develop while preserving lineage
- `OPTIONAL` — may appear when justified
- `FORBIDDEN` — must not appear without an explicit canon change

## Evolution heuristic

The working design heuristic is approximately 60% recognizable inherited Visual DNA and 40% development/new complexity. This is not a pixel or mathematical requirement; it is a review heuristic.

Evolution should be expressed as:

```text
PARENT DNA
├── preserved traits
├── enhanced traits
└── approved new traits
        ↓
    CHILD FORM
```

Do not generate a later form as an unrelated prompt with only a shared name.

## Proportion progression

Working direction for a three-stage family:

```text
Stage 1: cute / compact
Stage 2: balanced / agile
Stage 3: powerful / mature
```

This is a prototype convention, not a universal canon rule.

## Asset relationship

Character data is the anchor. Art, 3D, game and content outputs reference the same character ID.

```text
CHARACTER DATA + VISUAL DNA
          ↓
      MASTER DESIGN
          ↓
  ┌───────┼────────┐
  2D      3D      DATA/CONTENT
```

Exploration renders are evidence/candidates, not canon by default. Canon promotion follows `CANON_AND_DATA_POLICY.md` and binary retention follows `ASSET_STORAGE_POLICY.md`.

## Combination compatibility

The schema intentionally leaves room for future combination/inheritance mechanics, but detailed combination rules must not be canonized until evolution consistency is validated with real characters.

## Phase 1 validation target

Use `NT-001` as the first Golden Character candidate:

1. define structured Visual DNA;
2. retain a selected concept candidate;
3. review/correct base design;
4. validate evolution continuity;
5. create approved reference/turnaround assets;
6. only then test 3D/print adaptation.
