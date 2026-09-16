# NOVA TAILS — Project State

**Project version:** 0.1.0-dev  
**Phase:** Phase 0 — Repository & Architecture Foundation  
**Updated:** 2026-09-16  
**Source of truth:** this repository

## Status policy

`IDEA → DRAFT → REVIEW → APPROVED → LOCKED`  
Obsolete decisions become `DEPRECATED` rather than being silently erased.

## LOCKED

Nothing is permanently locked yet. The project is deliberately still validating architecture and product assumptions.

## APPROVED DIRECTION

- Build an original multi-species sci-fi/fantasy character universe.
- Shared master character identity should drive game data, 2D art and printable 3D adaptations.
- Printable figures should favor modular, color-separated FDM construction and practical assembly as a current direction, with actual manufacturing rules deferred to physical tests.
- AI is an ideation/production assistant; reviewed repository canon remains authoritative.
- Do not mass-produce characters/assets until a vertical slice validates the systems and asset pipeline.
- Use short-lived, purpose-specific branches and reviewed PRs for significant canonical changes.
- Keep human-readable rationale, machine-readable canon, schemas, prompts and assets as distinct responsibilities.
- Avoid premature Git LFS/schema/automation complexity until real prototype/asset needs exist.

## DRAFT / PRODUCT HYPOTHESES

These are deliberately **not** resolved inside the Phase 0 foundation PR:

- Working project/universe name: **NOVA TAILS**. Name/legal clearance is not complete.
- Character-collection/card-battler as the first interactive product.
- Hero-collector / gacha acquisition concept.
- Five-character team concept.
- Auto/semi-auto combat direction.
- Cultivation-inspired long-term progression.
- Nova Core / The Fracture universe premise.
- Six-origin-domain concept: Organic, Mecha, Spirit, Arcane, Abyss, Celestial.
- Faction architecture.
- Class / role / element taxonomy.
- Evolution forms and branching progression.
- Boss phase + Break mechanics.
- Three-slot equipment direction: Weapon / Armor / Accessory.

These hypotheses will move through dedicated design branches/PRs rather than being silently promoted by architecture documentation.

## EXISTING DESIGN PROOF-OF-CONCEPT

### MOMO — Little Scout

Current concept demonstrates a candidate physical-design direction:

- small stylized fox/scout character;
- approximately three base print colors;
- roughly 10–14 major printable parts target;
- physical seams should correspond to color/material boundaries;
- optional accessories should not make the base figure difficult to manufacture;
- identity should remain consistent between 2D/game/3D adaptations.

MOMO is a proof of concept, not the visual template for the universe and not yet a fully canonical production character.

## MAJOR UNKNOWN / MUST VALIDATE

1. Exact target player and product positioning.
2. Primary platform for the first playable.
3. Core battle interaction model and team size.
4. Progression depth and system overlap.
5. Economy and acquisition model.
6. World conflict and narrative motivation.
7. Character taxonomy complexity.
8. Sustainable 2D → 3D adaptation pipeline.
9. Actual A1 mini connector/tolerance/manufacturing standards from physical tests.
10. IP/name/similarity review process.
11. Whether the game concept is fun without relying on collection/progression rewards.
12. Whether physical printing is core product, extension or later layer.

## CURRENT MILESTONE — Phase 0 Foundation

- [x] Repository initialized
- [x] Project state established
- [x] Branch/PR workflow defined
- [x] Canon/data ownership policy drafted
- [x] Asset storage policy drafted
- [x] PR review template added
- [x] Baseline `.gitignore` added
- [x] Master Architecture v0.1 hardened to separate durable principles from product hypotheses
- [x] Roadmap revised around risk-reduction/prototype gates
- [x] Product Vision removed from Phase 0 PR so it can receive a dedicated review
- [ ] Phase 0 foundation PR reviewed/accepted and merged
- [ ] `main` protection/ruleset configured when repository permissions/workflow allow it

## NEXT MILESTONES

After Phase 0 merge, use separate branches/PRs:

1. `design/product-vision-v0.1`
2. `design/core-loop-v0.1`
3. `design/world-architecture-v0.1`
4. `design/character-taxonomy-v0.1`
5. `design/visual-bible-v0.1`
6. `feature/combat-prototype`

This is a risk-ordering guideline rather than waterfall. A cheap prototype may deliberately move earlier when it can answer a high-risk question faster than more documentation.

## DO NOT DO YET

- Do not generate a 50–100 character roster.
- Do not create hundreds of skills/items.
- Do not write the complete campaign.
- Do not finalize gacha rates or monetization.
- Do not mass-produce STL/3MF assets.
- Do not design exhaustive schemas before the prototype exposes real data needs.
- Do not treat placeholder balance or manufacturing numbers as canon.

## NEXT DECISION

Review the Phase 0 foundation itself. If accepted, merge it into `main`; then start Product Vision on a dedicated branch. The first Product Vision task should identify the highest-risk product assumption and decide whether a low-fidelity prototype/research test should occur before further worldbuilding.
