# NOVA TAILS — Master Architecture v0.1

**Status:** REVIEW  
**Purpose:** Define durable boundaries and dependency principles before detailed product/content production. Concrete game/lore taxonomies and output priorities below remain hypotheses until dedicated reviews.

## 1. Durable architecture

NOVA TAILS is being developed as an original IP that can support multiple adaptations if Product Vision retains them. The durable relationship being reviewed in Phase 0 is:

```text
                    NOVA TAILS IP
                         |
                    REVIEWED CANON
                         |
          +--------------+--------------+
          |              |              |
        WORLD        CHARACTER       SYSTEMS
          |              |              |
          +--------------+--------------+
                         |
             MASTER CHARACTER IDENTITY
                         |
              ADAPTATIONS (optional)
             /          |          \
           GAME         2D          3D
```

No adaptation lane is automatically required to be a launch product. Product Vision decides priorities. Generated images/models are outputs, not the source of truth.

## 2. Canon layers

### Universe Canon
Defines cosmology, history, worlds, factions, cultures, conflicts, terminology and narrative constraints once reviewed.

### Character Canon
Defines immutable identity, origin, signature visual traits and other retained character constraints once reviewed.

### Game Canon — if/when a game is retained
Defines combat/interaction, progression, skills, stats, equipment, enemies, bosses, economy and acquisition once those systems survive design/prototype review.

### Asset Canon
Defines reviewed visual identity and output adaptation standards. Manufacturing constraints become canonical only if physical collectibles remain in scope and are physically tested.

## 3. Candidate character architecture — PRODUCT/DESIGN HYPOTHESIS

```text
CHARACTER
|
+-- Origin
|   +-- Origin Domain
|   +-- Race
|   +-- Species
|   +-- Variant / Trait
|
+-- World Identity
|   +-- Faction
|   +-- Culture
|
+-- Combat (if retained)
|   +-- Class
|   +-- Specialization
|   +-- Role
|   +-- Element
|   +-- Weapon Family
|
+-- Progression (if retained)
|   +-- Level
|   +-- Cultivation Rank
|   +-- Evolution Form
|   +-- Skill Tree
|   +-- Equipment
|
+-- Visual DNA
|   +-- Body Archetype
|   +-- Shape Language
|   +-- Signature Feature
|   +-- Material Language
|   +-- Locked Identity Features
|
+-- Adaptations
    +-- Game
    +-- 2D
    +-- 3D / Print
```

This decomposition is a stress-test model, not approved taxonomy. Individual categories must justify the decisions they enable.

## 4. Candidate origin domains — DRAFT

- Organic
- Mecha
- Spirit
- Arcane
- Abyss
- Celestial

If retained, species should not automatically determine combat class and faction should not automatically determine species. These independence principles are stronger than the exact candidate lists.

## 5. Candidate combat taxonomy — DRAFT

Possible base classes:

- Warrior
- Guardian
- Ranger
- Mystic
- Support
- Trickster

Possible roles include Tank, Bruiser, Burst DPS, Sustained DPS, AoE DPS, Healer, Buffer, Debuffer, Controller, Summoner and Energy/Battery.

Possible elements:

- Fire
- Water
- Nature
- Lightning/Storm
- Earth
- Frost
- Light
- Void

These lists must not be mass-populated before Product Vision, Core Loop and interaction/combat prototype review. Element reactions and dual elements are deferred until a base model demonstrates they add meaningful decisions.

## 6. Candidate progression budget — DRAFT

Current brainstorming includes Level, Cultivation/Breakthrough, Evolution, Skill choices/tree and Equipment. There is no requirement that all survive.

Durable principle: retained progression systems must have distinct jobs. Multiple systems that only provide percentage stat inflation should be merged/removed.

## 7. Candidate ability architecture — DRAFT

If the game direction requires character combat kits, a possible starting vocabulary is Basic Attack / Skill / Passive / Ultimate.

A future machine-readable ability grammar may include trigger, target, scaling, type, element, effects, resource interaction, cooldown, conditions and tags. Exact grammar must be extracted from the prototype rather than invented exhaustively now.

## 8. Candidate equipment architecture — DRAFT

Weapon / Armor / Accessory is a candidate model only.

Durable principle: if equipment exists, it should create trade-offs/build choices rather than exist only as a linear item-level ladder.

## 9. Candidate enemy architecture — DRAFT

Normal / Elite / Boss and subtypes are candidate encounter taxonomy only.

Durable principle: if the game uses enemies, they should teach/test mechanics and belong coherently to the world rather than functioning only as HP/stat bags.

## 10. Stable identity principle

Each production character should eventually receive a stable ID once the character taxonomy/registry needs it. Example format only:

```text
NT-ORG-FOX-001
```

If evolution/forms remain part of the product, forms should inherit base identity instead of independently redefining the character. Exact schema is intentionally deferred.

## 11. Cross-output identity principle

```text
MASTER CHARACTER IDENTITY
          |
    optional adaptations
     /       |       \
   GAME     2D      PRINT
```

Adaptations may differ technically while preserving reviewed identity.

Examples if print is retained:
- card/concept art may use floating energy effects;
- print adaptation may convert them to supported geometry;
- fine cloth may be thickened for FDM;
- micro color regions may be merged into physical components.

These are adaptation examples, not manufacturing specifications.

## 12. AI generation architecture

```text
REVIEWED CANON
  ↓
Context Builder
  ↓
Prompt Template
  ↓
AI Proposal
  ↓
Validation
  ↓
Human Review
  ↓
Approved Canon / Asset Registry (when applicable)
```

Prompts are derived artifacts. Prompt text must never silently override canon.

## 13. Validation gates

Use only gates relevant to the artifact/system being reviewed.

### Identity
- correct stable identity when IDs exist;
- locked features preserved;
- recognizable signature/silhouette where visual identity applies.

### World / Game
- matches reviewed constraints;
- no unbudgeted mechanic overload;
- numeric placeholders remain marked until tested.

### Visual
- follows reviewed universe/faction language once defined;
- remains sufficiently distinct from internal roster.

### Print — only if retained
- part/color separation;
- robust geometry;
- connector strategy;
- support/orientation/build-volume feasibility;
- physical tolerance validation before locking dimensions.

### IP risk
- internal similarity check;
- external name/design similarity research before production/release;
- retain human design decisions/version history.

This process reduces risk; it does not guarantee absence of third-party rights.

## 14. Production principle

Do not expand content simply because AI makes content cheap. Production begins only after a vertical slice or equivalent proof validates the retained product assumptions and required pipelines.

## Phase 0 review boundary

Phase 0 can approve the **architecture/governance principles** in this document without approving candidate game, world, taxonomy or physical-product decisions. Product Vision, Core Loop, Minimum World Architecture, Character Taxonomy, Visual Identity and Interaction/Combat Prototype should receive focused follow-up review as applicable.
