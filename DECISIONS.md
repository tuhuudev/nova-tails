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

### Decision
The Git repository is the authoritative project record after review. `main` is the latest reviewed baseline and may intentionally contain explicitly marked draft/review hypotheses. Chat/AI output does not become authoritative merely by being generated.

---

## ADR-0002 — Architecture before mass content

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Do not create a large roster, skill library, equipment catalog or printable collection before validating architecture and a vertical slice/equivalent proof.

### Why
Cheap AI generation can create large amounts of internally inconsistent content and increase sunk cost before core assumptions are proven.

---

## ADR-0003 — Shared master character identity

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
When a character is adapted across outputs, game unit, 2D artwork and 3D printable figure should derive from one canonical character identity rather than becoming independently redesigned identities.

---

## ADR-0004 — First game direction

**Status:** DRAFT / DEFERRED TO PRODUCT VISION  
**Date:** 2026-09-16

### Hypothesis
An accessible character-collection RPG/card-battler may be a suitable first interactive product. Five-character teams and semi-auto/auto combat are hypotheses, not architecture decisions.

### Alternatives to test
- fully manual turn-based;
- smaller 3–4 unit party;
- semi-auto/auto with manual decisions;
- other low-complexity formats consistent with the IP goal.

### Validation required
Dedicated Product Vision review and cheap interaction prototype(s).

---

## ADR-0005 — V1 progression budget

**Status:** DRAFT / DEFERRED TO CORE LOOP  
**Date:** 2026-09-16

### Hypothesis
Level, Cultivation/Breakthrough, Evolution, Skill choices and Equipment are candidate progression dimensions. There is no requirement that all five survive.

### Durable constraint
Each retained progression dimension must create a distinct decision/unlock/job. Systems that merely duplicate percentage stat inflation should be merged, removed or deferred.

---

## ADR-0006 — Physical collectible / FDM direction

**Status:** REVIEW / DEFERRED TO PRODUCT VISION + PHYSICAL PROOF  
**Date:** 2026-09-16

### Hypothesis
A modular, color-separated FDM-printable collectible layer—ideally allowing base figures to be printed without AMS—could be a meaningful differentiator.

### Why not approved yet
We have design proof-of-concept work, but have not decided whether physical printing is a core product pillar, extension or later layer, and manufacturing rules have not been validated on representative physical prototypes.

### Validation required
Product Vision decision plus representative physical prints before locking manufacturing standards.

---

## ADR-0007 — Short-lived purpose-specific branches

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Use `main` as reviewed project baseline and short-lived purpose-specific branches (`design/`, `feature/`, `character/`, `balance/`, `asset/`, `tooling/`, `fix/`, `chore/`). Significant changes to reviewed state go through focused PRs.

### Why
The current project/team size does not justify permanent integration branches. Focused branches make review, rollback and dependency reasoning easier.

---

## ADR-0008 — Separate canon responsibilities

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Separate responsibilities: `docs/` for intent/rationale/hypotheses; `data/` for machine-readable structured/canonical instances when needed; `schemas/` for validity/contracts; `prompts/` for derived generation instructions; `assets/` for intentionally retained project assets; implementation/tools consume reviewed contracts rather than silently redefining canon.

---

## ADR-0009 — Do not prematurely enable Git LFS or exhaustive schemas

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Define storage/schema policy now, but delay Git LFS configuration and detailed entity schemas until representative binary assets and prototype data exist.

---

## ADR-0010 — Roadmap is risk-driven, not waterfall

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Roadmap phases express dependency/risk order, not a requirement to complete large documents sequentially. When targeted external research or a cheap prototype/test can invalidate a risky assumption faster than documentation, use it and feed evidence back into the relevant decision.

### Why
The project must avoid replacing implementation/product risk with excessive worldbuilding/design documentation.

---

## ADR-0011 — Originality is a goal with validation, not a guaranteed property

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
The project aims to build a distinctive original IP, but neither AI generation nor internal design review can guarantee absence of third-party rights. Names and production/release designs require similarity/name research and documented human review; formal legal review can be added where commercial risk justifies it.

### Impact
Do not describe a generated concept as legally cleared merely because it was generated from an original prompt. Preserve provenance and substantive human design decisions.
