# AI Context Contract v0.1

**Status:** REVIEW

AI generation is downstream of reviewed project sources.

## Context assembly order

```text
L0 Character Identity
        +
L1 Master Design references/rules
        +
Target Adapter Contract
        +
Task-specific constraints
        ↓
Derived AI Context
        ↓
Proposal / generated output
        ↓
Validation + review
```

## Rules

- Prompts are derived instructions, never canonical identity storage.
- Generated art/model/text may propose changes but cannot silently update L0/L1.
- Do not rely on hidden conversation history for identity-critical facts that should be represented in reviewed project sources.
- An adapter context should include only relevant upstream facts plus its own allowed transformations/validation gates; avoid copying unrelated lore or implementation details.
- Retained AI outputs should record useful provenance when needed for reproducibility/rights review.
- Repeated generated variation does not turn a fact into canon.

## Drift test

If two independent generation sessions receive the same reviewed identity/master contract and target-adapter rules, differences in style/pose/detail may be acceptable, but declared identity invariants must remain stable.

If preserving identity repeatedly requires undocumented prompt additions, the architecture is missing upstream information and should be revised rather than accumulating prompt folklore.
