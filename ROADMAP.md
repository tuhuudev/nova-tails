# NOVA TAILS — Master Roadmap

**Status:** REVIEW  
**Strategy:** foundation → product hypothesis → playable proof → vertical slice → production.

The roadmap is a sequence of **risk-reduction gates**, not a promise to finish every document before prototyping. If a later prototype invalidates an earlier assumption, return to the relevant decision rather than protecting sunk work.

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

## Phase 1 — Product Vision

Define only what is needed to decide whether the product hypothesis deserves prototyping:
- target player/problem/fantasy;
- primary platform assumption;
- core product pillars;
- first interactive product boundary;
- role of collection/acquisition;
- role of 3D printing;
- business/market assumptions only where they affect design;
- pivot/cancellation criteria.

**Exit gate:** we can explain who the first product is for, what value/fantasy it offers, what we are deliberately not building and which assumptions must be tested.

## Phase 2 — Core Loop

Design the minimum repeated player loop on paper/low-fidelity flow:
- battle/encounter;
- decision/team adjustment;
- reward;
- progression/build;
- next challenge;
- acquisition only if Product Vision still requires it.

**Exit gate:** repeated play has a reason beyond receiving more currency/content.

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
- combat identity;
- element if combat requires it;
- body archetype/signature;
- stable identity/evolution inheritance.

**Exit gate:** approximately six intentionally different test characters can be described without contradictions or redundant taxonomy dimensions.

## Phase 5 — Visual Identity Proof

Define only enough visual system to keep the vertical-slice characters coherent and distinct:
- universe-level visual DNA;
- silhouette/shape principles;
- candidate faction/material language where needed;
- identity-lock rules;
- 2D/3D adaptation principles;
- internal similarity review.

**Exit gate:** multiple character concepts can look different while still feeling related, and one identity can survive 2D/3D adaptation.

## Phase 6 — Combat First Playable

Build the cheapest functional combat proof with placeholder visuals.

Test competing assumptions rather than implementing the full progression/economy stack:
- team size;
- formation/targeting if relevant;
- turn/action model;
- basic/skill/ultimate interaction;
- energy/resource only if needed;
- minimal status/control;
- one simple boss/encounter mechanic.

**GATE A — CORE GAME:** if combat is not understandable and strategically promising without collection/progression rewards, revise Product Vision/Core Loop/Combat before continuing.

## Phase 7 — Mathematical Combat Model

Only after a promising interaction model exists, formalize:
- minimal stats;
- damage/defense curves;
- speed/action economy;
- crit only if it adds useful build space;
- energy/resource economy;
- healing/shields/status/control;
- boss resistance/Break only if prototype supports them.

All numbers remain tunable until simulation/playtest.

## Phase 8 — Structured Game Data & First Schemas

Extract schemas from the working prototype rather than predicting every future field.

Likely first contracts:
1. Character
2. Skill/Ability
3. Enemy/Boss
4. Equipment (when introduced)

**Exit gate:** prototype content can be represented consistently as data and validated automatically.

## Phase 9 — Progression Proof

Test the smallest progression set that creates distinct decisions. Current candidates:
- Level;
- Cultivation/Breakthrough;
- Evolution;
- Skill choices/tree;
- Equipment.

Do not assume all five survive. Merge/remove systems that duplicate stat inflation.

## Phase 10 — Equipment Proof

Introduce equipment only after combat/build decisions exist. Candidate slots are Weapon / Armor / Accessory, but slot count is not a requirement.

**Exit gate:** items create meaningful trade-offs/build changes rather than merely larger numbers.

## Phase 11 — Economy Model

Map every retained resource as source → inventory → sink and model pacing/bottlenecks. Do not add currencies without a distinct job.

## Phase 12 — Acquisition / Gacha Decision

Only after core game/progression exist, decide whether gacha is actually required. If retained, separately research/design rates, pity, duplicate handling, transparency, platform/legal/age-market implications and monetization boundaries before release.

Gacha is a product/business decision, not an architectural default.

## Phase 13 — World 01 Enemy Ecosystem

Create only enough enemies to teach the first world's mechanics:
- roughly 6–10 normal enemies;
- roughly 1–2 elites;
- coherent ecological/narrative relationship.

Exact counts are production targets, not canon.

## Phase 14 — Boss Encounter Proof

Build one boss whose encounter tests mechanics taught earlier. Boss should create decisions rather than function as an enlarged HP pool.

## Phase 15 — Six Test Characters

Finalize only the small roster required for the vertical slice, covering substantially different roles/body archetypes/play patterns.

Each retained character should have:
- stable identity;
- gameplay purpose;
- minimal progression slice;
- visual identity spec;
- asset adaptation requirements.

## Phase 16 — Vertical Slice

Target, subject to earlier prototype findings:
- 1 coherent world/biome;
- enough stages to demonstrate the loop (not necessarily exactly 10);
- ~6 playable characters;
- small enemy ecosystem;
- 1–2 elites;
- 1 boss;
- limited equipment/progression;
- functional representative UI;
- representative 2D identity;
- at least one 3D adaptation candidate.

**GATE B — PRODUCT:** external/internal playtest before scaling.

## Phase 17 — Balance Simulator

When combat is sufficiently deterministic/data-driven, build batch simulation.

Candidate metrics:
- win rate;
- DPS/contribution;
- damage taken;
- healing/support contribution;
- CC uptime;
- resource/ultimate frequency;
- turn/time-to-complete;
- boss TTK.

Simulation complements playtesting; it does not decide whether gameplay feels good.

## Phase 18 — Telemetry

Instrument the playable slice only when there are actual players/builds worth measuring. Candidate events include battle start/end, skill use, death, boss phase, failure, upgrade and resource source/sink.

## Phase 19 — Physical Asset Proof

Use a very small sample (for example two contrasting characters plus one larger encounter/collectible) to validate:

`Master Identity → 2D → source 3D → print adaptation → split → slice → print → assemble → review`

No connector/tolerance/detail rule becomes locked until measured on real prints.

## Phase 20 — 3D Manufacturing Bible

Record proven rules for scale, detail/wall thickness, tolerance, support/orientation, color/part count, connector families, bases and target-printer constraints.

## Phase 21 — Asset Registry

Introduce stable asset IDs/dependencies when real production assets begin multiplying. Do not build a registry system for hypothetical assets.

## Phase 22 — Storage Scaling

Keep text/data/code in normal Git. Re-evaluate Git LFS or external object storage using representative real asset sizes/history.

## Phase 23 — AI Pipeline

Automate only stable/repetitive work:

`Reviewed Canon → Context → Prompt → AI Proposal → Validation → Human Review → Canon/Asset Registry`

Avoid automating unstable design decisions merely to generate more content faster.

## Phase 24 — IP / Similarity Gate

Before production-scale release of names/characters/assets:
- internal silhouette/signature comparison;
- external name/design research;
- documented human review;
- provenance/version history.

This reduces risk; it cannot guarantee zero infringement. Formal legal review can be added where commercial risk justifies it.

## Phase 25 — External Playtest / Production Gate

Observe players without coaching and measure comprehension, decisions, failure reasons, character desirability and replay motivation.

Scale only if evidence supports:
- coherent/enjoyable core loop;
- understandable strategic decisions;
- meaningful progression;
- desirable/distinct characters;
- coherent enough world context;
- manageable economy if applicable;
- repeatable asset pipeline;
- physically viable print adaptation if retained as a pillar;
- maintainable data/technical architecture.

If a major pillar fails, revise or remove it rather than compensating with more content.

## Production

Expand incrementally and world-by-world. Numbers such as `6 → 12 → 24 → 40+ characters` are capacity examples, not commitments.
