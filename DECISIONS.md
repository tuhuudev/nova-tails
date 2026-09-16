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

## ADR-0001 — Repository is the source of truth

**Status:** APPROVED  
**Date:** 2026-09-16

### Context
The project is being developed through iterative AI-assisted discussion and may eventually contain game systems, lore, structured data, 2D assets and 3D printable assets. Chat history alone is unsuitable as canonical project storage.

### Decision
The Git repository is the authoritative project record. AI/chat outputs remain proposals until reviewed and written into canonical project files.

### Impact
Every significant future session should read the relevant repository state before proposing canonical changes.

### Revisit trigger
Only if project scale requires a dedicated content-management/database system; Git should still retain versioned schemas/code/docs.

---

## ADR-0002 — Architecture before mass content

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Do not create a large roster, skill library, equipment catalog or printable collection before validating architecture and a vertical slice.

### Why
Cheap AI generation can create large amounts of internally inconsistent content and increase sunk cost before core assumptions are proven.

### Validation required
A playable vertical slice and repeatable asset pipeline.

---

## ADR-0003 — Shared master character identity

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Game unit, 2D artwork and 3D printable figure are adaptations of one canonical character identity, not independently redesigned characters.

### Impact
Character specs must explicitly separate locked identity features from output-specific adaptation rules.

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

### Validation required
Core-loop/progression prototype.

---

## ADR-0006 — Physical design philosophy

**Status:** APPROVED DIRECTION / NOT LOCKED  
**Date:** 2026-09-16

### Decision
Physical collectible exploration should prioritize modular FDM manufacturing, strong physical color separation and robust assembly, including workflows that do not require AMS for the base figure.

### Validation required
Physical prints of contrasting character archetypes before locking manufacturing standards. Connector dimensions/tolerances remain unapproved until measured from real prints.

---

## ADR-0007 — Short-lived purpose-specific branches

**Status:** APPROVED  
**Date:** 2026-09-16

### Context
The project will contain interdependent design, code, balance and asset changes. A single long-lived development branch would make review boundaries and canon promotion unclear.

### Decision
Use `main` as reviewed project state and short-lived purpose-specific branches (`design/`, `feature/`, `character/`, `balance/`, `asset/`, `tooling/`, `fix/`, `chore/`). Significant canonical changes go through focused PRs.

### Alternatives considered
- permanent `develop` branch;
- one branch per contributor;
- committing AI changes directly to `main`.

### Why
The current team/project size does not justify GitFlow-style permanent integration branches. Focused branches make review, rollback and dependency reasoning easier.

### Revisit trigger
A larger team/release process demonstrates a concrete need for release/integration branches.

---

## ADR-0008 — Separate canon responsibilities

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Separate responsibilities as follows:

- `docs/` explains intent/rationale;
- `data/` stores machine-readable canonical instances once needed;
- `schemas/` defines validity/contracts;
- `prompts/` derives generation instructions from canon;
- `assets/` stores intentionally retained project assets under storage policy;
- implementation/simulator/tools consume the contracts rather than redefining canon silently.

### Why
This prevents prompt drift, duplicated entity facts and contradictions between documentation, game implementation and asset generation.

### Validation required
The first vertical-slice schemas/data should demonstrate that the split is useful rather than bureaucratic.

---

## ADR-0009 — Do not prematurely enable Git LFS or exhaustive schemas

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Define storage/schema policy now, but delay Git LFS configuration and detailed entity schemas until representative physical assets and prototype data exist.

### Why
Optimizing for hypothetical file sizes/fields creates maintenance cost before actual requirements are known.

### Revisit trigger
- first structured combat data slice for schemas;
- Physical Asset Proof milestone for LFS/storage.

---

## ADR-0010 — Roadmap is risk-driven, not waterfall

**Status:** APPROVED  
**Date:** 2026-09-16

### Decision
Roadmap phases express dependency/risk order, not a requirement to complete large documents sequentially. When a cheap prototype/test can invalidate a risky assumption faster than documentation, prototype earlier and feed evidence back into the relevant decision.

### Why
The project must avoid replacing implementation risk with excessive worldbuilding/design documentation.

### Impact
Product Vision and Core Loop should identify the highest-risk assumptions and select the cheapest credible validation method before expanding content.
