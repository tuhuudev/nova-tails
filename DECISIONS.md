# NOVA TAILS — Decision Log

Use this file for high-impact project decisions. Do not silently convert brainstorms into canon.

## ADR template

```text
ADR-XXXX — Title
Status: DRAFT | REVIEW | APPROVED | LOCKED | DEPRECATED
Date: YYYY-MM-DD
Context
Decision
Alternatives considered
Why
Dependencies / impact
Validation required
Revisit trigger
```

---

## ADR-0001 — Repository is the authoritative reviewed project record
**Status:** APPROVED  
**Date:** 2026-09-16

The Git repository is authoritative after review. `main` is the latest reviewed baseline and may intentionally contain explicitly marked draft/review hypotheses. Chat/AI output does not become authoritative merely by being generated.

---

## ADR-0002 — Architecture before mass content
**Status:** APPROVED  
**Date:** 2026-09-16

Do not create a large roster, skill/item catalog, campaign or printable collection before validating architecture and a vertical slice/equivalent proof. Cheap generation is not evidence that generated content is worth producing.

---

## ADR-0003 — Shared master identity across adaptations
**Status:** APPROVED  
**Date:** 2026-09-16

When an identity/character is adapted across outputs, adaptations should derive from one canonical identity rather than becoming independently redesigned identities.

---

## ADR-0004 — First game direction
**Status:** DRAFT / DEFERRED TO PRODUCT VISION  
**Date:** 2026-09-16

Character-collection RPG/card-battler, five-character teams and semi-auto/auto combat are hypotheses. Product Vision + cheap interaction tests decide whether they survive.

---

## ADR-0005 — V1 progression budget
**Status:** DRAFT / DEFERRED TO CORE EXPERIENCE  
**Date:** 2026-09-16

Level, Cultivation/Breakthrough, Evolution, Skill choices and Equipment are candidates only. Each retained progression dimension must create a distinct decision/unlock/job; duplicate stat-inflation layers should be merged/removed.

---

## ADR-0006 — Physical collectible / FDM direction
**Status:** REVIEW / DEFERRED TO PRODUCT VISION + PHYSICAL PROOF  
**Date:** 2026-09-16

A modular, color-separated, no-AMS-friendly FDM layer may differentiate the project. Product Vision must decide its role and representative physical prints must validate manufacturing rules before they are locked.

---

## ADR-0007 — Short-lived purpose-specific branches
**Status:** APPROVED  
**Date:** 2026-09-16

Use `main` as reviewed baseline and short-lived purpose-specific branches (`design/`, `feature/`, `character/`, `balance/`, `asset/`, `tooling/`, `fix/`, `chore/`). Significant changes to reviewed state go through focused PRs. Do not add permanent integration branches without a demonstrated team/release need.

---

## ADR-0008 — Separate canon responsibilities
**Status:** APPROVED  
**Date:** 2026-09-16

Separate responsibilities: `docs/` for intent/rationale/hypotheses; `data/` for machine-readable structured/canonical instances when needed; `schemas/` for validity/contracts when needed; `prompts/` for derived generation instructions; `assets/` for intentionally retained assets; implementation/tools consume reviewed contracts rather than silently redefining canon.

The serialization/schema technology is deliberately undecided until real prototype/tooling requirements exist.

---

## ADR-0009 — Do not prematurely enable Git LFS or exhaustive schemas
**Status:** APPROVED  
**Date:** 2026-09-16

Define storage/data-contract policy now, but delay Git LFS, serialization choice and detailed entity schemas until representative binary assets and prototype data/tooling exist.

---

## ADR-0010 — Roadmap is risk-driven, not waterfall
**Status:** APPROVED  
**Date:** 2026-09-16

Roadmap phases express dependency/risk order. Targeted research or a cheap prototype/test should move earlier whenever it can invalidate a risky assumption faster than documentation. Feed evidence back into decisions instead of protecting sunk work.

---

## ADR-0011 — Originality is a goal with validation, not a guaranteed property
**Status:** APPROVED  
**Date:** 2026-09-16

If the project pursues an original IP, neither AI generation nor internal design review can guarantee absence of third-party rights. Names and production/release designs require similarity/name research and documented human review; formal legal review can be added where commercial risk justifies it.

---

## ADR-0012 — Distinctive original universe/IP as product hypothesis
**Status:** REVIEW / DEFERRED TO PRODUCT VISION  
**Date:** 2026-09-16

Hypothesis: center the project on a distinctive original multi-species sci-fi/fantasy universe/IP, initially explored through character-centric concepts and capable of supporting multiple adaptations over time. Product Vision must validate audience, primary product, differentiation and output priorities using targeted evidence.

---

## ADR-0013 — Prototype the highest-risk product assumption before deep content
**Status:** APPROVED  
**Date:** 2026-09-16

After Product Vision/Core Experience identify the most dangerous assumption, create the cheapest credible prototype/test before investing in deep lore, exhaustive taxonomy or production content. The test type depends on the risk: interaction prototype, paper simulation, clickable flow, concept desirability test or physical proof.

### Why
Architecture is valuable only if it reduces rework. Documentation that delays testing the assumption most likely to kill/change the product becomes a liability.
