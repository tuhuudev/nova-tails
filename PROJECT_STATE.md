# NOVA TAILS — Project State

**Project version:** 0.2.0-dev  
**Phase:** Phase 1 — Product Vision & Evidence  
**Updated:** 2026-09-16  
**Baseline:** Phase 0 accepted via PR #1 / squash commit `f8789431cee5c34b70f029079427436941828883`

## ACCEPTED FOUNDATION

- Repository workflow/canon governance is the accepted baseline.
- Architecture before mass content production.
- Use risk-driven research/prototypes rather than waterfall documentation.
- AI proposes; reviewed repository state is authoritative.
- Separate rationale, canonical structured data, contracts, prompts and retained assets.
- Delay exhaustive schemas/IDs/asset registries/LFS until real requirements exist.
- If multiple adaptations retain the same identity, preserve one master identity.
- Originality/rights must be validated rather than assumed.

## LOCKED

Nothing is permanently locked yet.

## CURRENT PRODUCT VISION — REVIEW

Working strategic hypothesis:

> NOVA TAILS is a character/IP system whose distinctive identities can survive across digital and physical adaptations; the first product should be whichever small experience proves that people care about those identities and want to interact with/collect them.

This is not yet accepted canon.

## PRODUCT OPTIONS UNDER REVIEW

1. Game-first character universe.
2. Character/IP-first collectible ecosystem.
3. Printable-collectible-first.
4. Content-first validation/audience building.

Do not assume these must all survive.

## HIGHEST-RISK ASSUMPTIONS

1. **Character desirability:** strangers can recognize, remember and want more of the identities.
2. **Differentiation:** concept is distinguishable from crowded cute/stylized creature/robot space.
3. **Core interaction:** if game is retained, repeated interaction works without gacha/reward scaffolding.
4. **Physical viability:** if print is retained, unknown original characters are desirable and reliably manufacturable.
5. **Cross-output leverage:** shared identity creates more value than complexity.

## CURRENT EVIDENCE

- 2025 mobile-market examples show active use of hybrid/simple-core + deeper-meta structures; this does not validate a generic NOVA TAILS gacha/card battler.
- MakerWorld has creator commercial-license mechanisms and explicit originality/authorization requirements, making printable originals a plausible but unvalidated distribution/business extension.
- A1 mini real build volume is 180 × 180 × 180 mm; any A1-mini manufacturing standard must ultimately be physically tested.

See `docs/research/PRODUCT_VISION_EVIDENCE_2026-09-16.md`.

## NT-001 / PYROX INTAKE — REVIEW

- A retained candidate record exists at `data/characters/NT-001/character.json` (NT-001 / Pyrox, v0.1.0, `CANDIDATE`).
- The known selected-concept, production-reference, orthographic and per-view asset context is indexed at `data/assets/NT-001.asset-manifest.json`.
- No corresponding binary asset was present in the local clone at intake. The manifest records them as `MISSING_LOCAL`; it does not promote their reported Library status to project canon.
- `docs/production/NT-001_PYROX_INTAKE_AND_3D_HANDOFF.md` defines the safe import target and the conditional 3D handoff.

This intake does **not** override the Product Vision/Test A gate or authorize production-scale 3D work.

## DRAFT / UNVALIDATED

- working name NOVA TAILS;
- card battler / character-collection RPG;
- gacha;
- five-character team;
- auto/semi-auto combat;
- cultivation;
- Nova Core / The Fracture;
- origin/faction/class/role/element counts;
- progression/equipment models;
- 3D printing as core product pillar;
- MOMO as production character.

## FIRST TEST — PROPOSED

**Test A: Character desirability / identity.**

Use 3–5 deliberately diverse character concepts at comparable presentation quality. Test with people outside the project for:
- unaided recall;
- recognizable signature/silhouette;
- perceived distinctiveness;
- preference reason;
- desire to see/interact with one again.

Failure signal: responses are mainly generic “cute/cool” and identities are not remembered/distinguished.

## NEXT DECISION

Review Product Vision v0.1 and decide whether Test A is the correct first risk-reduction experiment. If accepted, create a dedicated experiment branch and define protocol before generating more characters.

## TEST A PREPARATION — READY TO RUN

`docs/experiments/TEST_A_CHARACTER_DESIRABILITY_v0.1.md` and `data/experiments/test-a-character-desirability-template.csv` now provide the protocol and anonymous-result template for the proposed first test. Execution remains blocked until the retained NT-001 source assets are imported and comparable candidate presentation boards are available. Results must be reviewed before changing Pyrox's candidate status or authorizing a 3D blockout.

## DO NOT DO YET

Do not deepen lore, lock combat, build economy/gacha, generate a large roster, or engineer a production STL catalog before the first desirability/differentiation evidence exists.
