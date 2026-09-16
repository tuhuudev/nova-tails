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

### Revisit trigger
If project scale requires a dedicated content-management/database system; Git should still retain versioned schemas/code/docs and decision history.

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

### Impact
Character specs should eventually separate locked identity features from output-specific adaptation rules.

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
- other low-complexity formats consistent with the IP.

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
A modular, color-separated FDM-printable collectible layer—ideally allowing base figures to be printed without AMS—could be a meaningful differentiator for the IP.

### Why not approved yet
We have design proof-of-concept work, but have not yet decided whether physical printing is a core product pillar, extension or later layer, and manufacturing rules have not been validated on representative physical prototypes.

### Validation required
1. Product Vision decision on the role of physical collectibles.
2. Physical prints of contrasting character archetypes before locking manufacturing standards.
3. Measured connector/tolerance/detail results before canonical manufacturing dimensions.

---

## ADR-0007 — Short-lived purpose-specific branches

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Use `main` as reviewed project baseline and short-lived purpose-specific branches (`design/`, `feature/`, `character/`, `balance/`, `asset/`, `tooling/`, `fix/`, `chore/`). Significant changes to reviewed state go through focused PRs.

### Alternatives considered
- permanent `develop` branch;
- one branch per contributor;
- committing AI changes directly to `main`.

### Why
The current project/team size does not justify GitFlow-style permanent integration branches. Focused branches make review, rollback and dependency reasoning easier.

### Revisit trigger
A larger team/release process demonstrates a concrete need for release/integration branches.

---

## ADR-0008 — Separate canon responsibilities

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Separate responsibilities as follows:
- `docs/` explains intent/rationale and may contain explicitly marked hypotheses;
- `data/` stores machine-readable canonical/structured instances once needed;
- `schemas/` defines validity/contracts;
- `prompts/` derives generation instructions from reviewed canon/context;
- `assets/` stores intentionally retained project assets under storage policy;
- implementation/simulator/tools consume reviewed contracts rather than redefining canon silently.

### Validation required
The first prototype/vertical-slice schemas/data should demonstrate that the split is useful rather than bureaucratic.

---

## ADR-0009 — Do not prematurely enable Git LFS or exhaustive schemas

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Define storage/schema policy now, but delay Git LFS configuration and detailed entity schemas until representative physical assets and prototype data exist.

### Revisit trigger
- first structured product/game-data slice for schemas;
- representative large binary assets for LFS/storage.

---

## ADR-0010 — Roadmap is risk-driven, not waterfall

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Roadmap phases express dependency/risk order, not a requirement to complete large documents sequentially. When targeted external research or a cheap prototype/test can invalidate a risky assumption faster than documentation, use it and feed evidence back into the relevant decision.

### Why
The project must avoid replacing implementation/product risk with excessive worldbuilding/design documentation.

### Impact
Product Vision and Core Loop should identify the highest-risk assumptions and select the cheapest credible validation method before expanding content.
