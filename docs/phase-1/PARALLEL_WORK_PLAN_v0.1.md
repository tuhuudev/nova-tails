# NOVA TAILS — Pre-Blender Parallel Work Plan v0.1

Status: ACTIVE / PROTOTYPE
Date: 2026-09-16

## Purpose
Continue high-value work while NT-001 waits for an executable Blender environment, without creating downstream rework.

## Track A — 3D Readiness (critical path)

Current gate: NT001_BLOCKOUT_v001.

Before Blender is available:
- Freeze Stage-1 prototype geometry rules at rule level only.
- Maintain Blender input/output contract.
- Do not create additional AI orthographic sheets unless a specific unresolved geometry question requires one.
- Do not canonize physical dimensions, print tolerances, rig topology, UVs, or final materials.

Expected Blender review package:
- NT001_BLOCKOUT_v001.blend
- NT001_BLOCKOUT_v001.glb
- FRONT.png
- BACK.png
- LEFT.png
- RIGHT.png
- TOP.png
- BOTTOM.png
- FRONT_3Q.png
- REAR_3Q.png

## Track B — Product Validation

Run lightweight tests that do not require final 3D.

### P03 — Recognition & Recall
Goal: determine whether NT-001 has memorable identity beyond generic fire-fox familiarity.

Test:
1. Show NT-001 for 8–12 seconds.
2. Hide it.
3. Ask respondent to describe what they remember.
4. Ask them to choose its silhouette among distractors when available.
5. Record which features they mention without prompting.

Primary signals:
- spontaneous mention of ears
- spontaneous mention of forehead diamond
- spontaneous mention of split tail
- confusion with existing creature/IP archetypes
- ability to recognize NT-001 again

Do not treat a single respondent as market validation.

### P04 — Evolution Comprehension
Goal: test the rule before producing final Stage 2/3 assets.

Use rough/candidate evolution explorations only. Ask:
- Which forms look like the same creature family?
- What changed?
- What should never change?
- Which form feels like a natural upgrade rather than a new creature?

### P05 — Combination Interest
Goal: validate the user's pilot signal around combination/upgrading before building a combination engine.

Test concepts, not implementation. Compare:
- evolution only
- combination only
- evolution + combination

Ask what the respondent expects to inherit from each parent and what would make a combination feel random or unfair.

## Track C — System Hardening

Safe work before Blender:
- asset lifecycle and authority rules
- dependency graph
- validation gates
- Blender I/O contract
- review-package convention
- provenance requirements

Defer:
- large automation pipeline
- final Stage 2/3 production
- NT-002 production
- final combination engine
- rig/animation production
- print connector/tolerance values
- game implementation

## Asset Authority

Lifecycle:
EXPLORATION -> CANDIDATE -> VALIDATED -> APPROVED -> CANON

`APPROVED` is domain-specific. Example: APPROVED_FOR_3D_BLOCKOUT does not mean CANON.

Generated artwork never promotes its own labels/status text. Structured project data and explicit project decisions are authoritative.

## Dependency rule

No downstream asset may silently override its upstream source.

Character Data
-> Visual DNA
-> Master Design / Reference
-> 3D Authoring Master
-> Runtime / Print / Content outputs

If downstream work reveals a conflict, create a review decision and update the upstream source intentionally.

## Stop rules

Stop generating additional 2D production sheets unless they resolve a named blocker.
Stop schema expansion unless a real production task exposes a missing contract.
Stop polishing a candidate if the next uncertainty can only be answered by 3D or user validation.

## Current priorities

P0: Prepare/run NT-001 3D blockout when Blender becomes available.
P1: Run P03 recognition/recall with lightweight respondents.
P1: Formalize asset lifecycle/dependency/QA rules.
P2: Explore P04/P05 using low-cost candidate visuals only after P03 protocol is ready.
