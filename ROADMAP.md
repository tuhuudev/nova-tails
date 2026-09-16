# NOVA TAILS — Master Roadmap

**Status:** REVIEW  
**Strategy:** foundation → product hypothesis → playable proof → vertical slice → production.

The roadmap is a sequence of **risk-reduction gates**, not a promise to finish every document before prototyping. If evidence invalidates an earlier assumption, return to the relevant decision rather than protecting sunk work.

## Phase 0 — Repository & Architecture Foundation

**Goal:** establish a maintainable source of truth and review discipline without overengineering.

Deliverables:
- repository/project-state baseline;
- status/version/ADR policy;
- short-lived branch + focused PR workflow;
- canon/data ownership policy;
- asset-storage policy;
- baseline ignore/security hygiene;
- master architecture boundary.

**Exit gate:** every important decision has a clear owner/location/status; product hypotheses are visibly separated from durable architecture; future work can be reviewed without relying on chat history.

**Explicit non-goals:** exhaustive folder tree, exhaustive schemas, Git LFS setup, CI/CD platform, large content catalog.

## Phase 1 — Product Vision & Evidence

Define only what is needed to decide whether the product hypothesis deserves prototyping:
- target player/problem/fantasy;
- primary platform assumption;
- core product pillars;
- first interactive product boundary;
- role of collection/acquisition;
- role of 3D printing;
- business/market assumptions only where they affect design;
- pivot/cancellation criteria.

Run targeted external research where it can materially change a decision. Candidate questions:
- adjacent games/products and what player need they serve;
- genre/platform expectations;
- differentiation risk;
- physical-digital collectible precedents if print remains a candidate pillar;
- monetization/platform/legal constraints only if acquisition/gacha becomes likely.

Do not turn this into a giant competitor spreadsheet. Research must end in a decision, hypothesis or test.

**Exit gate:** we can explain who the first product is for, what value/fantasy it offers, what we deliberately are not building, what evidence supports the direction and which assumptions must still be tested.

## Phase 2 — Core Loop

Design the minimum repeated player loop on paper/low-fidelity flow:
- encounter/battle if retained;
- meaningful player decision/team adjustment;
- reward/feedback;
- progression/build if retained;
- next challenge;
- acquisition only if Product Vision still requires it.

**Exit gate:** repeated use/play has a reason beyond receiving more currency/content.

## Phase 3 — Minimum World Architecture

Define only world rules needed to support the first playable/vertical slice:
- premise/conflict;
- player role;
- origin of playable beings/enemies;
- one first-world context;
- enough faction/world logic to make characters and enemies coherent.

Nova Core, The Fracture, six domains and larger cosmology remain replaceable hypotheses until reviewed.

**Exit gate:** the first playable's goals, characters and enemies have coherent narrative reasons to exist. Full campaign/world bible is not required.

## Phase 4 — Minimum Character Taxonomy

Stress-test taxonomy using a small deliberately diverse set rather than designing the whole universe.

Candidate dimensions:
- origin/species identity;
- faction/world identity;
- combat identity if applicable;
- element if interaction requires it;
- body archetype/signature;
- stable identity/evolution inheritance if applicable.

**Exit gate:** approximately six intentionally different test characters can be described without contradictions or redundant taxonomy dimensions.

## Phase 5 — Visual Identity Proof

Define only enough visual system to keep the vertical-slice characters coherent and distinct:
- universe-level visual DNA;
- silhouette/shape principles;
- candidate faction/material language where needed;
- identity-lock rules;
- cross-output adaptation principles;
- internal/external similarity review where appropriate.

**Exit gate:** multiple character concepts can look different while still feeling related, and retained cross-output identity survives adaptation.

## Phase 6 — Interaction / Combat First Playable

Build the cheapest functional proof with placeholder visuals.

If combat remains the core interaction, test competing assumptions rather than implementing the full progression/economy stack:
- team size;
- formation/targeting if relevant;
- turn/action model;
- basic/skill/ultimate vocabulary only if useful;
- energy/resource only if needed;
- minimal status/control;
- one simple encounter/boss mechanic.

**GATE A — CORE PRODUCT:** if the core interaction is not understandable and promising without collection/progression rewards, revise Product Vision/Core Loop before continuing.

## Phase 7 — Mathematical Interaction Model

Only after a promising interaction model exists, formalize the minimum required math: stats, damage/defense/action economy, resources, status/control and encounter resistance mechanics as applicable.

All numbers remain tunable until simulation/playtest.

## Phase 8 — Structured Game Data & First Schemas

Extract schemas from the working prototype rather than predicting every future field. Candidate first contracts may include Character, Ability, Enemy/Encounter and later Equipment.

**Exit gate:** prototype content can be represented consistently as data and validated automatically.

## Phase 9 — Progression Proof

Test the smallest progression set that creates distinct decisions. Current candidates include Level, Cultivation/Breakthrough, Evolution, Skill choices and Equipment. Do not assume all survive. Merge/remove systems that duplicate stat inflation.

## Phase 10 — Equipment Proof

Introduce equipment only after interaction/build decisions exist. Weapon / Armor / Accessory is a candidate, not a requirement.

**Exit gate:** retained items create meaningful trade-offs/build changes rather than merely larger numbers.

## Phase 11 — Economy Model

Map every retained resource as source → inventory → sink and model pacing/bottlenecks. Do not add currencies without a distinct job.

## Phase 12 — Acquisition / Gacha Decision

Only after core product/progression exist, decide whether gacha is actually required. If retained, separately research/design rates, pity, duplicate handling, transparency, platform/legal/age-market implications and monetization boundaries before release.

Gacha is a product/business decision, not an architectural default.

## Phase 13 — First-World Enemy / Challenge Ecosystem

If combat is retained, create only enough enemies/challenges to teach the first world's mechanics: roughly 6–10 normals and 1–2 elites is a capacity hypothesis, not canon.

## Phase 14 — Boss / Capstone Encounter Proof

Build one capstone encounter that tests mechanics taught earlier. It should create decisions rather than function as an enlarged HP/stat pool.

## Phase 15 — Small Test Roster

Finalize only the roster required for the vertical slice (roughly six is a current capacity hypothesis), covering substantially different identity/play patterns.

Each retained character should have stable identity, product/game purpose, minimal progression if applicable, visual identity spec and adaptation requirements.

## Phase 16 — Vertical Slice

Target, subject to earlier findings:
- 1 coherent world/biome;
- enough content to demonstrate the loop;
- small representative playable roster;
- representative challenges/enemies;
- 1 capstone encounter;
- limited progression/equipment only if retained;
- representative UI;
- representative visual identity;
- representative cross-output adaptation only for product pillars retained in Product Vision.

**GATE B — PRODUCT:** external/internal playtest before scaling.

## Phase 17 — Balance Simulator

When the interaction/combat model is sufficiently deterministic/data-driven, build batch simulation. Simulation complements playtesting; it does not decide whether gameplay feels good.

## Phase 18 — Telemetry

Instrument the playable slice only when there are actual players/builds worth measuring.

## Phase 19 — Physical Asset Proof — CONDITIONAL

Only if Product Vision retains physical collectibles, use a very small sample to validate:

`Master Identity → 2D/reference → source 3D → print adaptation → split → slice → print → assemble → review`

No connector/tolerance/detail rule becomes locked until measured on real prints.

## Phase 20 — 3D Manufacturing Bible — CONDITIONAL

Only after Physical Asset Proof, record proven rules for scale, detail/wall thickness, tolerance, support/orientation, color/part count, connector families, bases and target-printer constraints.

## Phase 21 — Asset Registry

Introduce stable asset IDs/dependencies when real production assets begin multiplying. Do not build a registry system for hypothetical assets.

## Phase 22 — Storage Scaling

Keep text/data/code in normal Git. Re-evaluate Git LFS or external object storage using representative real asset sizes/history.

## Phase 23 — AI Pipeline

Automate only stable/repetitive work:

`Reviewed Canon → Context → Prompt → AI Proposal → Validation → Human Review → Approved Canon/Asset Registry`

Avoid automating unstable design decisions merely to generate more content faster.

## Phase 24 — IP / Similarity Gate

Before production-scale release of names/characters/assets:
- internal silhouette/signature comparison;
- external name/design research;
- documented human review;
- provenance/version history.

This reduces risk; it cannot guarantee zero infringement. Formal legal review can be added where commercial risk justifies it.

## Phase 25 — External Playtest / Production Gate

Observe users/players without coaching and measure comprehension, decisions, failure reasons, character desirability and replay motivation as applicable.

Scale only if evidence supports the retained pillars: coherent core loop, meaningful decisions, desirable/distinct characters, sufficient world context, manageable progression/economy if applicable, repeatable asset pipeline, physically viable print adaptation if retained, and maintainable data/technical architecture.

If a major pillar fails, revise or remove it rather than compensating with more content.

## Production

Expand incrementally and world-by-world. Any roster/content counts discussed before this gate are capacity hypotheses, not commitments.
