# NOVA TAILS — Master Architecture v0.1

**Status:** REVIEW  
**Purpose:** Define durable boundaries and dependency principles before detailed product/content production. Concrete game/lore taxonomies below remain hypotheses until their dedicated design reviews.

## 1. Durable architecture

NOVA TAILS is being developed as an original IP that may feed multiple outputs. The durable relationship being reviewed in Phase 0 is:

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
            +------------+------------+
            |            |            |
           GAME          2D           3D
            |            |            |
        gameplay       cards       printable
        progression    icons       collectibles
        narrative      promo       STL / 3MF
```

Generated images/models are outputs. They are not the source of truth.

## 2. Canon layers

### Universe Canon
Defines cosmology, history, worlds, factions, cultures, conflicts, terminology and narrative constraints once reviewed.

### Character Canon
Defines immutable identity, origin, species, faction, combat identity, signature visual traits and evolution inheritance once reviewed.

### Game Canon
Defines combat, progression, skills, stats, equipment, enemies, bosses, economy and acquisition once those systems survive design/prototype review.

### Asset Canon
Defines shape language, visual identity, materials, colors, VFX, 2D standards, 3D adaptation and manufacturing constraints. Manufacturing dimensions are not locked until physically tested.

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
+-- Combat
|   +-- Class
|   +-- Specialization
|   +-- Role
|   +-- Element
|   +-- Weapon Family
|
+-- Progression
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
+-- Outputs
    +-- Game
    +-- 2D
    +-- 3D / Print
```

This decomposition is useful as a stress-test model, but individual categories are not canon until Character Taxonomy and gameplay reviews.

`Origin Domain` is currently preferred over `Realm` for biological/metaphysical origin so it does not conflict with possible cultivation terminology. This naming remains reviewable.

## 4. Candidate origin domains — DRAFT

- Organic
- Mecha
- Spirit
- Arcane
- Abyss
- Celestial

Species should not automatically determine class. Faction should not automatically determine species. These independence principles are stronger than the exact candidate lists.

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

These lists must not be mass-populated into characters before Product Vision, Core Loop and combat prototype review. Element reactions and dual elements are deferred until a base combat model demonstrates they add meaningful decisions.

## 6. Candidate progression budget — DRAFT

Initial hypothesis is to test no more than five progression dimensions:

1. Level
2. Cultivation Rank
3. Evolution Form / Star
4. Skill Tree
5. Equipment

Artifact, Bond, Rune, Relic and similar layers are deferred unless playtesting demonstrates a real design need.

Durable principle: progression systems must have distinct jobs. Multiple systems that only provide percentage stat inflation should be merged/removed.

## 7. Candidate skill architecture — DRAFT

Possible initial character kit:

- Basic Attack
- Skill
- Passive
- Ultimate

Machine-readable skill grammar may eventually include:

- trigger;
- target;
- scaling;
- damage/healing type;
- element;
- effects;
- resource interaction;
- cooldown;
- conditions;
- tags.

Detailed skills must wait until combat rules are testable.

## 8. Candidate equipment architecture — DRAFT

Possible V1 slots:

- Weapon
- Armor
- Accessory

Durable principle: equipment should create trade-offs/build choices rather than exist only as a linear item-level ladder.

## 9. Candidate enemy architecture — DRAFT

```text
Enemy
+-- Normal
|   +-- Attacker
|   +-- Defender
|   +-- Support
|   +-- Controller
|   +-- Disruptor
+-- Elite
|   +-- Enhanced
|   +-- Mutated
|   +-- Commander
+-- Boss
    +-- Stage Boss
    +-- Raid Boss (future hypothesis)
    +-- World Boss (future hypothesis)
```

Durable principle: enemies should belong to the world and teach mechanics that later encounters can combine/test rather than functioning only as HP/stat bags.

## 10. Stable identity principle

Each production character should eventually receive a stable ID. Example format only:

```text
NT-ORG-FOX-001
```

Evolution forms should inherit base identity instead of independently redefining the character.

```text
BASE CHARACTER
+-- FORM-01
+-- FORM-02
+-- FORM-03
```

A future schema may record only deltas such as ADD / REMOVE / MODIFY / KEEP-LOCKED. Exact schema is intentionally deferred.

## 11. Game / 2D / 3D relationship

```text
MASTER CHARACTER IDENTITY
          |
   +------+------+ 
   |      |      |
 GAME    2D     PRINT
```

Adaptations may differ technically while preserving reviewed identity.

Examples:

- Card art may use floating energy effects.
- Printable adaptation may convert them to supported solid/translucent geometry.
- Fine cloth can be thickened for FDM.
- Micro color islands can be merged into physical color components.

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
Approved Canon / Asset Registry
```

Prompts are derived artifacts. Prompt text must never silently override canon.

## 13. Validation gates

Before an asset becomes canonical, review the dimensions relevant to that asset.

### Identity
- correct stable identity;
- locked features preserved;
- recognizable silhouette/signature.

### World / Game
- matches reviewed taxonomy/world/game constraints;
- no unbudgeted mechanic overload;
- numeric placeholders remain marked until simulated/playtested.

### Visual
- follows reviewed universe/faction visual language;
- remains sufficiently distinct from internal roster.

### Print
- color/part separation;
- robust geometry;
- connector strategy;
- support/orientation feasibility;
- build-volume constraints;
- physical tolerance validation before locking dimensions.

### IP risk
- internal similarity check;
- external name/design similarity research before production/release;
- retain human design decisions/version history.

This process reduces risk; it does not guarantee absence of third-party rights.

## 14. Production principle

Do not expand content simply because AI makes content cheap. Production begins only after a vertical slice validates the core product/game assumptions and a repeatable asset pipeline.

## Phase 0 review boundary

Phase 0 can approve the **architecture principles** in this document without approving every candidate taxonomy/list. Product Vision, Core Loop, World Architecture, Character Taxonomy, Visual Bible and Combat Prototype should each receive focused follow-up review.
