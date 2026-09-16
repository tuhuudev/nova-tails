# NOVA TAILS — AI Context Contract v0.1

**Status:** REVIEW

AI prompts are derived consumers of repository authority. They are never the source of truth.

## Context build order

For a character adaptation, assemble context in this order:

1. character ID + lifecycle + revision;
2. identity premise/personality anchors;
3. visual invariants;
4. signature features and criticality;
5. approved master-design references when available;
6. target adapter contract;
7. adapter-specific allowed transformations;
8. target deliverable requirements.

## Prompt rule

A generated prompt must distinguish:
- **MUST PRESERVE** — upstream invariants;
- **MAY ADAPT** — medium freedoms;
- **MUST NOT INFER AS CANON** — missing lore/stats/material facts;
- **OUTPUT REQUIREMENTS** — current task only.

## Drift control

Generated output is a proposal. Before retention:
- compare against invariant list;
- reject/repair identity drift;
- record which upstream revision was used;
- store only intentionally retained output;
- route any proposed identity change upstream for review.

## Example derived context for NT-CHAR-001

```text
CHARACTER: NT-CHAR-001@0.1 [DRAFT]
PREMISE: floating non-animal identity around a central core and incomplete orbital structure
MUST PRESERVE:
- floating/non-quadruped topology
- meaningful negative space around core
- incomplete asymmetric orbit
- broken-orbit signature is structural
MAY ADAPT:
- pose/orbit rotation
- expression
- detail density
- lighting
- target-medium geometry
DO NOT INVENT AS CANON:
- faction, element, combat role, powers, rarity, final name
```

This context can feed image, modeling, game or content tasks while keeping the same upstream identity.

## Automation trigger

Do not build a complex context-builder service yet. Add a small deterministic tool when repeated manual context assembly becomes error-prone or when a second retained character/adaptation proof begins.
