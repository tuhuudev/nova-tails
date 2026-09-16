# Product Strategy Decision 001 — Character/IP-first Asset System

**Status:** REVIEW  
**Date:** 2026-09-16

## Decision

Adopt Character/IP-first as the working architecture direction: build a coherent shared identity/design source before independently expanding game, print, card/2D or content production.

The output lanes are consumers of a shared asset system, not separate sources of character truth.

## Why

The project intends to reuse recognizable identities across materially different media. Allowing each lane to recreate characters independently creates drift, duplicated decisions and inconsistent AI context. A master identity/design contract makes those dependencies explicit while still allowing medium-specific adaptation.

## Important boundary

This is an architecture/production decision, not a market-validation result. It does not prove that users want a game, printable collectible, content product, or even the IP itself. Output-lane investment remains evidence-driven.

## Consequences

- Define L0/L1/L2/L3 authority and adapter contracts now.
- Prove architecture using one reference identity before roster expansion.
- Keep game/print/content-specific implementation downstream.
- Do not force one universal binary asset across all media.
- Build automation only after real repetition/coordination problems appear.

## Revisit when

- the reference-character proof shows the shared contract adds more complexity than coherence;
- a medium cannot preserve identity without repeated upstream exceptions;
- market evidence indicates a narrower product should intentionally optimize around one medium.
