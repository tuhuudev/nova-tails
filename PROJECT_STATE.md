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

## APPROVED ARCHITECTURE DIRECTION

- Build an original multi-species sci-fi/fantasy character universe.
- When characters span outputs, one reviewed master identity should drive adaptations rather than allowing independent identity drift.
- AI is an ideation/production assistant; reviewed repository state remains authoritative.
- Do not mass-produce characters/assets until a vertical slice validates relevant systems and pipeline assumptions.
- Use short-lived, purpose-specific branches and reviewed PRs for significant changes.
- Keep human-readable rationale, machine-readable canon, schemas, prompts and assets as distinct responsibilities.
- Avoid premature Git LFS/schema/automation complexity until real prototype/asset needs exist.
- Treat the roadmap as risk-driven; use external research and cheap prototypes/tests when they can materially change a decision faster than more documentation.

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
- Role of physical 3D printing in the actual product (core pillar vs extension vs later layer).
- Modular/color-separated/no-AMS-friendly FDM as the preferred physical design direction if the physical layer is retained.

These hypotheses will move through dedicated design branches/PRs rather than being silently promoted by architecture documentation.

## EXISTING DESIGN PROOF-OF-CONCEPT

### MOMO — Little Scout

Current concept demonstrates a candidate physical-design direction: small stylized fox/scout; approximately three base print colors; roughly 10–14 major parts target; physical seams intended to correspond to color/material boundaries; optional accessories intended not to make the base figure difficult to manufacture; identity intended to remain consistent across adaptations.

MOMO is a proof of concept, not the visual template for the universe and not yet a fully canonical production character. Its printability assumptions are not proven until a real model is engineered, sliced, printed and assembled.

## MAJOR UNKNOWN / MUST VALIDATE

1. Exact target player and product positioning.
2. Primary platform for the first playable.
3. Core interaction/battle model and team size if combat is retained.
4. Progression depth and system overlap.
5. Economy and acquisition model.
6. World conflict and narrative motivation.
7. Character taxonomy complexity.
8. Sustainable cross-output adaptation pipeline.
9. Actual target-printer connector/tolerance/manufacturing standards if print is retained.
10. IP/name/similarity review process.
11. Whether the core product is compelling without collection/progression reward scaffolding.
12. Whether physical printing is core product, extension or later layer.
13. Which adjacent products/genres validate or challenge the proposed differentiation.

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
- [x] Physical-collectible direction moved back to REVIEW rather than prematurely treating it as product canon
- [x] Product Vision gate now requires targeted external evidence where it can materially change a decision
- [ ] Phase 0 foundation PR reviewed/accepted and merged
- [ ] `main` protection/ruleset configured when repository permissions/workflow allow it

## NEXT MILESTONES

After Phase 0 merge, use separate branches/PRs:

1. `design/product-vision-v0.1`
2. `design/core-loop-v0.1`
3. `design/world-architecture-v0.1`
4. `design/character-taxonomy-v0.1`
5. `design/visual-bible-v0.1`
6. `feature/combat-prototype` (if combat remains the selected interaction)

This is a risk-ordering guideline rather than waterfall. A cheap prototype may deliberately move earlier when it answers a high-risk question faster than more documentation.

## DO NOT DO YET

- Do not generate a 50–100 character roster.
- Do not create hundreds of skills/items.
- Do not write the complete campaign.
- Do not finalize gacha rates or monetization.
- Do not mass-produce STL/3MF assets.
- Do not design exhaustive schemas before the prototype exposes real data needs.
- Do not treat placeholder balance or manufacturing numbers as canon.

## NEXT DECISION

Review the Phase 0 foundation itself. If accepted, merge it into `main`; then start `design/product-vision-v0.1`. Product Vision should combine focused external research with explicit hypotheses and identify the cheapest credible test for the highest-risk assumption before deep worldbuilding.
