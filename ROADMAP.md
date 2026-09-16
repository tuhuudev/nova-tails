# NOVA TAILS — Master Roadmap

**Status:** REVIEW  
**Strategy:** foundation → evidence-backed product hypothesis → cheapest useful proof → vertical slice → production.

This is a **risk map, not waterfall**. Product Vision decides which later systems are actually required. A cheap prototype may move ahead of world/taxonomy documentation when it answers a critical unknown faster.

## Phase 0 — Repository & Architecture Foundation

Goal: maintainable reviewed project record without overengineering.

Deliverables: project state, lifecycle/ADR policy, short-lived branch + focused PR workflow, canon/data ownership, asset-storage policy, baseline ignore/security hygiene and architecture boundaries.

**Exit gate:** important decisions have clear location/status; hypotheses are separated from durable architecture; future work can be reviewed without relying on chat history.

**Non-goals:** exhaustive folders/schemas, Git LFS, CI/CD platform, large content catalog.

## Phase 1 — Product Vision & Evidence

Resolve enough to decide what deserves prototyping:
- target audience/player and core fantasy/value;
- primary platform/context;
- primary product format;
- differentiation;
- which outputs are core vs optional/later;
- role of collection/acquisition;
- role of physical printing;
- business/market constraints only where design-relevant;
- pivot/cancellation criteria.

Use targeted external research for adjacent products/genres, expectations, differentiation and relevant platform/physical-digital precedents. Research must end in a decision, hypothesis or test—not a giant competitor spreadsheet.

**Exit gate:** clear target/product/value/boundaries, evidence supporting the direction and explicit high-risk assumptions.

## Phase 2 — Core Loop / Core Experience

Define the minimum repeated experience appropriate to the selected product. For a game hypothesis this may include encounter → decision/build → feedback/reward → progression → next challenge. Acquisition belongs here only if Phase 1 retains it.

**Exit gate:** repeated use/play has value beyond receiving more currency/content.

## Phase 3 — Cheapest High-Risk Prototype

Before large worldbuilding, identify the assumption most likely to invalidate the product and build the cheapest credible test.

Examples:
- low-fidelity interaction/combat prototype;
- clickable UX flow;
- paper/card simulation;
- character desirability/concept test;
- 2D→3D physical proof if physical differentiation is the highest-risk pillar.

**GATE A — CORE PRODUCT:** if the core promise is not understandable/promising without reward scaffolding, revise Phase 1/2.

## Phase 4 — Minimum World Architecture — CONDITIONAL DEPTH

Define only world rules needed by the selected product/prototype: premise/conflict, player/user role, one initial setting and enough world logic for characters/challenges. Nova Core/The Fracture/six domains remain replaceable hypotheses.

Full campaign/cosmology is not required.

## Phase 5 — Minimum Character Taxonomy — CONDITIONAL DEPTH

Stress-test a small diverse set. Candidate dimensions include origin, world identity, interaction/combat identity, visual DNA and stable identity/inheritance. Remove dimensions that do not create useful design/product decisions.

## Phase 6 — Visual Identity Proof

Define enough visual system to make representative characters coherent/distinct and preserve identity across retained outputs. Include similarity review where appropriate.

## Phase 7 — Interaction / Combat Model — IF RETAINED

If the first product is a character battler, prototype team size, targeting/action model, ability/resource vocabulary and one meaningful encounter mechanic with placeholders. Do not implement full progression/economy first.

## Phase 8 — Math + Structured Data — WHEN BEHAVIOR IS KNOWN

Formalize only the stats/formulas/contracts the working prototype needs. Extract first schemas from real behavior rather than predicting every field.

## Phase 9 — Progression Proof — IF RETAINED

Test the smallest set that creates distinct decisions. Current Level/Cultivation/Evolution/Skill/Equipment ideas are candidates, not requirements. Merge/remove duplicate stat-inflation layers.

## Phase 10 — Equipment / Build Layer — IF RETAINED

Introduce only when the core interaction has meaningful build decisions. Weapon/Armor/Accessory is a candidate, not a requirement.

## Phase 11 — Economy — IF RETAINED

Map every resource as source → inventory → sink. No currency without a distinct job.

## Phase 12 — Acquisition / Gacha — IF RETAINED

Decide only after core product/progression exists. If gacha remains likely, separately research rates/pity/duplicates/transparency plus applicable platform/legal/age-market constraints before release. Gacha is not an architecture default.

## Phase 13 — Representative Content Set

Create only enough characters/challenges/world content to teach and demonstrate the retained core systems. Counts are capacity targets, not canon.

## Phase 14 — Capstone Encounter / Experience

Build one representative capstone that combines earlier learned mechanics/ideas and creates decisions rather than only increasing numbers.

## Phase 15 — Vertical Slice

Build one coherent representative slice of the selected product with representative UI, characters/content, core loop and only the progression/assets actually retained.

**GATE B — PRODUCT:** test with users/players before scaling.

## Phase 16 — Simulation / Telemetry — AS NEEDED

Use deterministic simulation when the system is data-driven enough for balance analysis; use telemetry when real users/builds exist. Neither replaces qualitative playtesting.

## Phase 17 — Physical Asset Proof — IF RETAINED

Validate a tiny representative sample through source design/model → print adaptation → slice → print → assembly → review. No tolerance/detail/manufacturing rule becomes locked before physical evidence.

## Phase 18 — Manufacturing Bible — IF RETAINED

Record only proven physical rules after the proof milestone.

## Phase 19 — Asset Registry / Storage Scaling — WHEN NEEDED

Introduce stable asset IDs and Git LFS/external storage only when real asset count/size/history justifies them.

## Phase 20 — AI Pipeline — AFTER STABILITY

Automate stable/repetitive work only:

`Reviewed Canon → Context → Prompt → AI Proposal → Validation → Human Review → Approved Canon/Asset Registry`

Do not automate unstable design decisions merely to generate more content faster.

## Phase 21 — IP / Similarity / Release Gate

Before production-scale release of names/characters/assets: internal comparison, external name/design research, provenance/human review and formal legal review where commercial risk justifies it. This reduces risk; it cannot guarantee zero infringement.

## Production Gate

Scale only if evidence supports the **retained** pillars: understandable/compelling core experience, meaningful decisions, desirable/distinct characters where relevant, sufficient world context, manageable progression/economy where relevant, repeatable asset pipeline, physical viability where retained, and maintainable technical/data architecture.

If a pillar fails, revise or remove it rather than compensating with more content.

## Production

Expand incrementally. Any roster/world/item counts discussed before this gate are hypotheses, not commitments.
