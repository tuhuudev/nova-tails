# NOVA TAILS — Project State

**Project version:** 0.1.0-dev  
**Phase:** Phase 0 — Repository & Architecture Foundation  
**Updated:** 2026-09-16  
**Repository role:** authoritative project record after review

## Lifecycle policy

`IDEA → DRAFT → REVIEW → APPROVED → LOCKED`; obsolete decisions become `DEPRECATED`.

`APPROVED` is an accepted current decision/direction. `LOCKED` is a stronger dependency contract. Draft hypotheses may be retained in the reviewed baseline without becoming active canon.

## LOCKED

Nothing is permanently locked yet. This is intentional.

## APPROVED ARCHITECTURE / GOVERNANCE DIRECTION

- When characters span outputs, one reviewed master identity should drive adaptations rather than allowing independent identity drift.
- AI is an ideation/production assistant; the repository is the authoritative project record after review.
- Do not mass-produce characters/assets until a vertical slice/equivalent proof validates relevant systems and pipeline assumptions.
- Use short-lived, purpose-specific branches and reviewed PRs for significant changes.
- Keep human-readable rationale, machine-readable canon, schemas, prompts and assets as distinct responsibilities.
- Avoid premature Git LFS/schema/automation complexity until real prototype/asset needs exist.
- Treat the roadmap as risk-driven; use external research and cheap prototypes/tests when they can materially change a decision faster than more documentation.
- After Product Vision/Core Experience identify the highest-risk assumption, prototype/test it before deep content/worldbuilding.
- Treat originality and third-party-rights risk as something to validate, not something AI can guarantee.

## REVIEW / PRODUCT GOAL

- Distinctive original multi-species sci-fi/fantasy character universe capable of supporting multiple adaptations over time. Product Vision must still validate target audience, differentiation, primary product and output priorities.

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

1. Target player and product positioning.
2. Primary platform.
3. Core interaction/battle model and team size if combat is retained.
4. Progression depth/system overlap.
5. Economy/acquisition model.
6. World conflict/narrative motivation.
7. Character taxonomy complexity.
8. Sustainable cross-output adaptation pipeline.
9. Physical manufacturing standards if print is retained.
10. IP/name/similarity review process and eventual commercial-risk threshold for formal legal review.
11. Whether the core product is compelling without reward scaffolding.
12. Whether physical printing is core, extension or later layer.
13. Which adjacent products/genres validate or challenge differentiation.

## PHASE 0 FOUNDATION CHECK

- [x] Repository/project state baseline
- [x] Branch/PR workflow
- [x] Lifecycle/ADR policy
- [x] Canon/data ownership policy
- [x] Asset storage policy
- [x] PR review template
- [x] Baseline `.gitignore`
- [x] Master Architecture separates durable principles from hypotheses
- [x] Roadmap is risk/evidence/prototype driven rather than waterfall
- [x] Product Vision removed from Phase 0 PR for dedicated review
- [x] Physical-collectible direction returned to REVIEW
- [x] Product Vision gate includes targeted external evidence
- [x] Originality/IP language requires validation rather than implying guarantee
- [x] Early highest-risk prototype/test is now an explicit governance decision
- [x] Internal architecture review completed; no remaining blocking governance/architecture inconsistency identified
- [ ] Owner acceptance / merge of Phase 0 foundation PR
- [ ] `main` protection/ruleset when repository permissions/workflow allow it

## NEXT MILESTONES

After Phase 0 acceptance/merge:
1. `design/product-vision-v0.1` — audience/product/differentiation/output priorities + targeted evidence.
2. `design/core-loop-v0.1` — minimum repeated experience for the selected product.
3. Create a dedicated cheapest-high-risk-prototype branch as soon as the most dangerous assumption is identifiable; it may precede deeper world/taxonomy work.
4. Add minimum world/taxonomy/visual work only to the depth required by the selected product/prototype.

## DO NOT DO YET

Do not mass-generate roster/skills/items/campaign/STL; finalize gacha/monetization; create exhaustive schemas; or lock placeholder balance/manufacturing values.

## NEXT DECISION

Owner accepts or requests changes to the Phase 0 foundation. After merge, Product Vision should combine focused external research with explicit hypotheses and choose the cheapest credible test for the highest-risk product assumption before deep worldbuilding.
