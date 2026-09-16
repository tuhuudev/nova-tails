# NOVA TAILS — Master Roadmap

**Status:** DRAFT  
**Strategy:** architecture → playable proof → vertical slice → production.

## Phase 0 — Repository & Governance

**Goal:** establish source of truth and decision discipline.

Deliverables:
- repository structure;
- `PROJECT_STATE.md`;
- status/version policy;
- decision log;
- roadmap;
- canonical-data conventions.

**Exit gate:** every new canonical decision has a clear home and status.

## Phase 1 — Product Vision

Define:
- target player;
- core fantasy;
- product pillars;
- platform assumption;
- game boundaries;
- role of 3D printing;
- role of AI;
- cancellation/pivot criteria.

**Exit gate:** we can explain what product we are building and explicitly what we are not building.

## Phase 2 — Core Loop

Define and prototype on paper:
- battle loop;
- reward loop;
- team/build loop;
- progression loop;
- acquisition's role;
- short-session and long-term motivations.

**Exit gate:** repeated play has a reason beyond receiving more currency.

## Phase 3 — World Architecture

Define only the world rules needed to support gameplay and character identity:
- cosmology/premise;
- Nova Core and The Fracture (or replacements);
- origin domains/worlds;
- factions and motivations;
- current conflict;
- player role;
- monster/boss origin;
- campaign skeleton.

**Exit gate:** gameplay goals, factions, characters and enemies have coherent narrative reasons to exist.

## Phase 4 — Character Taxonomy

Define:
- Origin Domain → Race → Species;
- Faction / Culture;
- Class / Specialization / Role;
- Element;
- body archetype / signature;
- evolution inheritance;
- stable IDs.

**Exit gate:** six deliberately different test characters can be specified without taxonomy contradictions.

## Phase 5 — Visual Bible

Define:
- universe visual DNA;
- faction DNA;
- shape language;
- material language;
- element VFX language;
- silhouette rules;
- color policy;
- 2D/3D identity preservation;
- internal similarity gate.

**Exit gate:** multiple artists/AI generations can produce different characters that still belong to one universe.

## Phase 6 — Combat First Playable

Build the cheapest functional combat proof. Placeholder visuals only.

Test:
- team size;
- formation/targeting;
- action model;
- Basic / Skill / Passive / Ultimate;
- energy;
- buffs/debuffs;
- control;
- Break;
- boss phases.

**GATE A — FUN / CLARITY:** if the combat is not understandable and strategically promising without gacha/progression rewards, revise before continuing.

## Phase 7 — Mathematical Combat Model

Define:
- primary/secondary stats;
- damage and defense curves;
- crit;
- speed/turn economy;
- energy economy;
- healing/shields;
- status/CC rules;
- boss resistance/Break rules.

All initial numbers remain placeholders until simulation/playtest.

## Phase 8 — Skill Framework

Create machine-readable skill grammar/tags and only enough skills for the vertical slice.

**Exit gate:** skill behavior can be represented consistently in data and evaluated by simulator/game logic.

## Phase 9 — Progression

Test only:
- Level;
- Cultivation Rank;
- Breakthrough;
- Evolution Form;
- Skill Tree.

Remove/merge systems whose only purpose duplicates stat inflation.

## Phase 10 — Equipment

V1 target:
- Weapon;
- Armor;
- Accessory.

Items should produce trade-offs/build choices.

## Phase 11 — Economy

Map every resource as source → inventory → sink.

Model:
- acquisition rate;
- upgrade costs;
- progression pacing;
- bottlenecks;
- free/premium separation if monetization remains in scope.

## Phase 12 — Acquisition / Gacha Decision

Only after core game/progression exist, decide:
- whether gacha is actually needed;
- banners/rates/pity if used;
- duplicate handling;
- guarantees;
- fairness/transparency requirements;
- monetization boundaries.

## Phase 13 — World 01 Enemy Ecosystem

Create only enough enemies to teach the first world's mechanics:
- ~8–10 normal enemies;
- ~2 elites;
- coherent ecological/narrative relationship.

## Phase 14 — Boss Framework

Build one stage/world boss whose phases test mechanics taught in World 01.

Bosses must be encounters, not enlarged HP pools.

## Phase 15 — Six Test Characters

Finalize six characters covering substantially different roles/body archetypes/play patterns.

Each must have:
- canonical identity;
- basic kit;
- progression slice;
- visual spec;
- asset adaptation requirements.

## Phase 16 — Vertical Slice

Target content:
- 1 world;
- ~10 stages;
- 6 playable characters;
- 8–10 normal monsters;
- 2 elites;
- 1 boss;
- ~20–30 skills total;
- ~12–15 equipment items;
- limited progression;
- minimal acquisition flow;
- functional UI.

**GATE B — PRODUCT:** playtest before scaling.

## Phase 17 — Balance Simulator

Build deterministic/data-driven combat engine and batch simulation.

Track:
- win rate;
- DPS;
- damage taken;
- healing;
- CC uptime;
- energy/ultimate frequency;
- turn count;
- boss TTK;
- contribution by character.

## Phase 18 — Telemetry

Instrument prototype/vertical slice with events such as battle start/end, skill use, death, boss phase, stage failure, upgrade, currency source/sink.

## Phase 19 — Physical Asset Proof

Use only 2 characters + 1 boss to validate:

`Master Design → 2D → 3D → print adaptation → split → slice → print → assemble → review`

No manufacturing rule becomes locked until physically tested.

## Phase 20 — 3D Manufacturing Bible

Record proven rules for:
- scale;
- wall/detail thickness;
- peg/socket tolerance;
- overhang/support strategy;
- part/color count;
- orientation;
- connector families;
- base standards;
- A1 mini constraints.

## Phase 21 — Asset Registry

Stable IDs and dependency links for concept, card, portrait, VFX, master model, print model and evolution forms.

## Phase 22 — Storage Scaling

Text/data/code remain normal Git. Add Git LFS/external storage only when binary asset volume requires it.

## Phase 23 — AI Pipeline

Automate only after canon/schema are stable:

`Canon → Context → Prompt → AI Proposal → Validation → Human Review → Canon/Asset Registry`

## Phase 24 — IP / Similarity Gate

Before production-scale release of characters/assets:
- internal silhouette/signature comparison;
- external design/name research;
- documented human review;
- version history.

This reduces risk; it cannot guarantee zero infringement.

## Phase 25 — External Playtest

Observe players without coaching. Measure comprehension, decisions, failure reasons, character desirability and replay motivation.

## Production Gate

Scale only if the vertical slice demonstrates:
- coherent/fun core loop;
- understandable strategic combat;
- meaningful progression;
- desirable/distinct characters;
- coherent world;
- manageable economy;
- repeatable asset pipeline;
- physically viable print adaptation;
- maintainable data/tech architecture.

If major pillars fail, revise rather than compensate with more content.

## Production

Expand incrementally:

`6 → 12 → 24 → 40+ characters`

and world-by-world rather than attempting the complete universe at once.
