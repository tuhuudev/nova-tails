# Reference Character Cross-Output Proof v0.1

**Status:** PLANNED

## Goal

Stress-test the Master Asset Architecture with one identity before scaling the roster.

## Selection rule

Use one reference identity only after its experiment status is explicitly recorded. A reference character is a test fixture, not automatically production canon or flagship.

Given current exploratory evidence, do not automatically choose Scout because of familiarity, and do not automatically choose Spirit/Wild because one participant reacted positively. Selection should maximize architectural stress: a visible signature that must survive materially different media.

## Minimum proof

Create one reviewed identity instance conforming to `schemas/character-identity.schema.json`, then produce:

1. a Card/2D adaptation manifest and representative visual;
2. a Print adaptation manifest and engineering concept;
3. optional lightweight Game adapter only after the first two expose enough architecture requirements.

## Required observations

For each adapter record:
- upstream identity revision;
- preserved invariants;
- transformations made;
- any requested upstream exception/change;
- validation result;
- deliverable provenance.

## Pass gate

PASS only if:
- both outputs still read as the same identity;
- the identity-critical signature survives;
- print constraints can be handled as documented adaptation rather than silent redesign;
- changing one upstream invariant makes affected adapters discoverable;
- neither generated output is treated as a new authority.

## Fail / revise signals

Revise architecture if:
- schema cannot express a real identity without medium-specific pollution;
- adapters duplicate contradictory identity facts;
- a medium repeatedly needs to override invariants;
- version impact cannot be determined;
- AI generation requires large hidden prompt context not represented by reviewed sources.

## Evidence boundary

This proof validates asset architecture only. It does not prove market demand, gameplay fun, commercial viability, originality clearance or manufacturability until those are separately tested.
