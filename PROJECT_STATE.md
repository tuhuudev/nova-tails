# NOVA TAILS — Project State

**Project version:** 0.1.0-dev  
**Phase:** Phase 0 — Repository & Architecture Foundation  
**Updated:** 2026-09-16  
**Repository role proposed by this PR:** authoritative after review/acceptance; `main` is accepted baseline

## Lifecycle policy — PROPOSED FOR ACCEPTANCE

`IDEA → DRAFT → REVIEW → APPROVED → LOCKED`; obsolete decisions become `DEPRECATED`.

`APPROVED` is an accepted current decision/direction. `LOCKED` is a stronger dependency contract. Draft hypotheses may be retained in the accepted baseline without becoming active canon.

## LOCKED

Nothing is permanently locked yet. This is intentional.

## PHASE 0 ARCHITECTURE / GOVERNANCE — PROPOSED FOR ACCEPTANCE

- If a character/identity is retained across multiple outputs, one reviewed master identity should drive those adaptations rather than allowing independent identity drift; Product Vision is not required to retain multiple outputs.
- AI is an ideation/production assistant; repository changes become authoritative after review/acceptance.
- Do not mass-produce content/assets until a representative end-to-end proof (vertical slice for a game, equivalent proof for another product) validates relevant assumptions.
- Use short-lived, purpose-specific branches and reviewed PRs for significant changes.
- Keep human-readable rationale, machine-readable structured/canonical data, validation contracts, prompts and assets as distinct responsibilities.
- Defer serialization/schema technology, stable-ID format, asset-registry naming and Git LFS until real prototype/tooling/asset requirements exist.
- Treat the roadmap as risk-driven; use external research and cheap prototypes/tests when they can materially change a decision faster than more documentation.
- Once Product Vision/Core Experience expose a highest-risk assumption, prototype/test it before deep content/worldbuilding; this test may move earlier than nominal roadmap phases.
- Treat originality and third-party-rights risk as something to validate, not something AI can guarantee.

## REVIEW / PRODUCT GOAL

- Build a distinctive multi-species sci-fi/fantasy universe/IP intended to become original, initially explored through character-centric concepts and potentially capable of multiple adaptations. Product Vision must validate target audience, differentiation, primary product and output priorities; IP/name/design review must validate originality/rights risk separately.

## DRAFT PRODUCT/DESIGN HYPOTHESES

- working name **NOVA TAILS** (name/legal clearance incomplete);
- character-collection/card-battler as first interactive product;
- gacha/hero acquisition;
- five-character team;
- auto/semi-auto combat;
- cultivation progression;
- Nova Core / The Fracture lore;
- six origin domains/factions/classes/roles/elements;
- evolution/Break/equipment models;
- role of physical 3D printing in the product;
- modular/color-separated/no-AMS-friendly FDM direction if physical collectibles are retained.

These hypotheses require dedicated design/evidence/prototype reviews.

## EXISTING PROOF-OF-CONCEPT

### MOMO — Little Scout

MOMO demonstrates a candidate physical-design direction (small stylized fox/scout, ~3 base colors, ~10–14 major-part target, physical color seams and cross-output identity intent). It is not the universe visual template, not yet a fully canonical production character, and its printability is unproven until engineered/sliced/printed/assembled.

## MAJOR UNKNOWN / MUST VALIDATE

1. Target audience/player and product positioning.
2. Primary platform/context.
3. Primary product format and core experience.
4. Core interaction/battle model and team size if combat is retained.
5. Progression/economy/acquisition if retained.
6. World conflict/narrative motivation to the depth required by product.
7. Character taxonomy complexity.
8. Sustainable cross-output adaptation pipeline if multiple outputs are retained.
9. Physical manufacturing standards if print is retained.
10. IP/name/similarity review process and eventual commercial-risk threshold for formal legal review.
11. Whether the core product is compelling without reward scaffolding.
12. Whether physical printing is core, extension or later layer.
13. Which adjacent products/genres validate or challenge differentiation.

## PHASE 0 FOUNDATION CHECK

- [x] Repository/project state baseline drafted
- [x] Branch/PR workflow drafted
- [x] Lifecycle/ADR policy drafted
- [x] Canon/data ownership policy drafted
- [x] Asset storage policy drafted
- [x] PR review template added
- [x] Baseline `.gitignore` added
- [x] Master Architecture separates durable principles from hypotheses
- [x] Roadmap is risk/evidence/prototype driven rather than waterfall
- [x] Product Vision removed from Phase 0 PR for dedicated review
- [x] Physical-collectible direction returned to REVIEW
- [x] Product Vision gate includes targeted external evidence
- [x] Originality/IP language requires validation rather than implying guarantee
- [x] Early highest-risk prototype/test proposed as governance decision
- [x] Data serialization/schema, stable-ID format and asset-registry naming deliberately deferred until real requirements
- [x] Repository ruleset state checked: no rulesets are currently configured
- [x] Phase 0 foundation prepared for owner/reviewer decision
- [ ] Owner/reviewer accepts Phase 0 and merges
- [ ] Configure `main` protection/ruleset when repository permissions/workflow allow it

## NEXT WORK AFTER ACCEPTANCE — RISK ORDER, NOT WATERFALL

- Start `design/product-vision-v0.1` with targeted evidence around audience/product/differentiation/output priorities.
- Define only enough Core Experience/Loop to expose the major assumptions.
- As soon as the highest-risk assumption is identifiable, create a dedicated prototype/test branch; do not wait for deep world/taxonomy documentation.
- Add minimum world/taxonomy/visual work only to the depth required by the retained product/prototype.

## DO NOT DO YET

Do not mass-generate roster/skills/items/campaign/STL; finalize gacha/monetization; choose exhaustive data/ID/asset naming schemes without requirements; or lock placeholder balance/manufacturing values.

## NEXT DECISION

Owner/reviewer accepts Phase 0 or requests specific changes. After merge, Product Vision should combine focused external research with explicit hypotheses and choose the cheapest credible test for the highest-risk product assumption before deep worldbuilding.
