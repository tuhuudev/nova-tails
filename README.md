# NOVA TAILS

> Working title. Original-IP project combining a character-collection game universe, 2D assets, and modular FDM-printable 3D collectibles.

## Current phase

**Pre-production — Architecture (v0.1)**

The repository is the single source of truth for project decisions. Chat/AI outputs are proposals until reviewed and promoted into canonical project files.

## Project principles

1. Architecture before mass content production.
2. Prototype core gameplay before building a large roster.
3. One master character identity feeds game, 2D, and 3D outputs.
4. AI generates proposals; it does not directly define canon.
5. Every important decision is versioned and reviewable.
6. 3D assets must respect real FDM manufacturing constraints.
7. Avoid unnecessary systems: every system must create a meaningful player/design decision.

## Canon status

- `IDEA` — exploratory.
- `DRAFT` — being designed.
- `REVIEW` — ready for review.
- `APPROVED` — accepted direction, may still evolve.
- `LOCKED` — canonical constraint; changes require an explicit decision.
- `DEPRECATED` — retained for history but no longer current.

## Repository map

- `PROJECT_STATE.md` — current project snapshot and next step.
- `ROADMAP.md` — stage gates from architecture to production.
- `DECISIONS.md` — architecture/design decision log.
- `docs/MASTER_ARCHITECTURE.md` — high-level system architecture.
- `docs/world/` — universe, lore, factions, locations, campaign.
- `docs/game/` — combat, progression, economy, skills, equipment.
- `docs/design/` — visual and asset design standards.
- `data/` — machine-readable canonical data (YAML/JSON later).
- `schemas/` — validation schemas for canonical data.
- `prompts/` — AI prompt templates derived from canon, never source of truth.
- `simulator/` — future deterministic combat/balance simulator.

## Immediate milestone

Complete Architecture v0.1 in this order:

1. Product Vision
2. Core Loop
3. World Architecture
4. Character Taxonomy
5. Visual Bible
6. Combat Prototype specification

Only after the first playable/vertical-slice assumptions survive review should the project expand into a large roster or large asset library.
