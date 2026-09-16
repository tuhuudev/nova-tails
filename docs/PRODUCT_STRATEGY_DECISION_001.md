# Product Strategy Decision 001 — IP-first Asset Platform

**Status:** REVIEW  
**Date:** 2026-09-16

## Decision under review

Prefer an architecture in which the **character/IP asset system is the shared platform** and game, printable collectibles, card/2D and content are downstream consumers.

The immediate investment is therefore the master identity/design architecture and a one-character cross-output proof, rather than choosing and fully building one output lane first.

## Rationale

- reduces the risk of independent character drift across media;
- preserves the option to test different products from one identity base;
- aligns with the existing Product Vision hypothesis that character identity may be the reusable core;
- makes AI generation more controllable because prompts can derive from explicit invariants;
- allows output-specific technical optimization without pretending one binary asset fits every medium.

## Important qualification

This is an architecture/product-development direction, not evidence that a multi-output ecosystem has market demand.

Output lanes still need behavioral validation. A lane that does not create value may be dropped even if its adapter is technically possible.

## Consequences

Do now:
- define master identity/design contracts;
- define adapters/dependencies;
- stress-test with one DRAFT reference character;
- keep validation evidence separate from architecture confidence.

Do not do now:
- generate a large roster;
- build full game systems;
- mass-produce STLs;
- automate a complex asset registry;
- assume all four lanes must launch.
