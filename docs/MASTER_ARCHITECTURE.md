# NOVA TAILS — Master Architecture v0.1

**Status:** DRAFT  
**Purpose:** Define boundaries and dependencies before detailed content production.

## 1. Product architecture

NOVA TAILS is designed as an original IP whose canonical universe and characters can feed multiple outputs.

```text
                    NOVA TAILS IP
                         |
                    CANON DATA
                         |
          +--------------+--------------+
          |              |              |
        WORLD        CHARACTER       SYSTEMS
          |              |              |
          +--------------+--------------+
                         |
             MASTER CHARACTER DESIGN
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
Defines cosmology, history, worlds, factions, cultures, conflicts, terminology and narrative constraints.

### Character Canon
Defines immutable identity, origin, species, faction, combat identity, signature visual traits and evolution inheritance.

### Game Canon
Defines combat, progression, skills, stats, equipment, enemies, bosses, economy and acquisition.

### Asset Canon
Defines shape language, visual identity, materials, colors, VFX, 2D standards, 3D adaptation and manufacturing constraints.

## 3. Character architecture

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

`Origin Domain` is preferred over `Realm` for biological/metaphysical origin so it does not conflict with Cultivation Rank/Realm terminology.

## 4. Proposed origin domains — DRAFT

- Organic
- Mecha
- Spirit
- Arcane
- Abyss
- Celestial

Species does not determine class. Faction does not determine species. Element should influence mechanics and visual language without becoming a simple recolor system.

## 5. Proposed combat taxonomy — DRAFT

Base classes:

- Warrior
- Guardian
- Ranger
- Mystic
- Support
- Trickster

Roles are separate from classes. Candidate roles include Tank, Bruiser, Burst DPS, Sustained DPS, AoE DPS, Healer, Buffer, Debuffer, Controller, Summoner and Energy/Battery.

Candidate elements:

- Fire
- Water
- Nature
- Lightning/Storm
- Earth
- Frost
- Light
- Void

Element reactions and dual elements are deferred until the base combat model proves they add meaningful decisions.

## 6. Progression boundary — DRAFT

V1 should initially test only five progression dimensions:

1. Level
2. Cultivation Rank
3. Evolution Form / Star
4. Skill Tree
5. Equipment

Artifact, Bond, Rune, Relic and similar layers are deferred unless playtesting demonstrates a real design need.

Progression systems must have distinct jobs. Multiple systems that only provide percentage stat inflation are a design failure.

## 7. Skill architecture — DRAFT

Initial character kit target:

- Basic Attack
- Skill
- Passive
- Ultimate

Machine-readable skill grammar should eventually include:

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

## 8. Equipment architecture — DRAFT

V1 candidate slots:

- Weapon
- Armor
- Accessory

Equipment should create trade-offs/build choices rather than a purely linear item-level ladder.

## 9. Enemy architecture — DRAFT

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
    +-- Raid Boss (future)
    +-- World Boss (future)
```

World enemies should belong to an ecosystem and teach mechanics that the world boss later combines/tests.

## 10. Master character identity

Each canonical character receives a stable ID, e.g.:

```text
NT-ORG-FOX-001
```

Evolution forms inherit the base identity instead of redefining the character.

```text
NT-ORG-FOX-001 / MOMO
+-- FORM-01 Little Scout
+-- FORM-02 Scout
+-- FORM-03 ...
```

Each form should record only deltas: ADD / REMOVE / MODIFY / KEEP-LOCKED.

## 11. Game / 2D / 3D relationship

```text
MASTER CHARACTER IDENTITY
          |
   +------+------+ 
   |      |      |
 GAME    2D     PRINT
```

The adaptations may differ technically while preserving identity.

Examples:

- Card art may use floating energy effects.
- Printable adaptation may convert them to solid/translucent supported geometry.
- Fine cloth can be thickened for FDM.
- Micro color islands can be merged into physical color components.

## 12. AI generation architecture

```text
CANON
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

Before an asset becomes canonical, review:

### Identity
- correct Character ID;
- correct species/faction/class/element;
- locked features preserved;
- recognizable silhouette/signature.

### Visual
- universe/faction shape language;
- intended material/color language;
- sufficiently distinct from internal roster.

### Game
- kit fits role;
- no unbudgeted mechanic overload;
- values are marked placeholder until simulated.

### Print
- color separation;
- robust thickness;
- connector strategy;
- support/orientation feasibility;
- A1 mini build-volume constraint;
- actual tolerance validated physically.

### IP risk
- internal similarity check;
- external name/design similarity research before production;
- retain human design decisions/version history.

## 14. Production principle

Do not expand content simply because AI makes content cheap. Production begins only after a vertical slice validates the core loop, combat, progression and repeatable asset pipeline.
