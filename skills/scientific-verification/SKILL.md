---
name: scientific-verification
description: Verify a bounded scientific claim against traceable sources, proof steps, or inspectable data and calculations.
---

## Purpose

Determine which specified claims are supported, contradicted, or unresolved.

## Trigger Conditions

Use for central or disputed scientific claims, apparent contradictions, or targeted evidence and calculation checks.

## Required Inputs

Exact claim, qualifiers, dependencies and relevant manuscript and external evidence.

## Investigation Guidance

Formulate a testable proposition. Compare like definitions, units, cases and measurement conditions. Trace supportive and contradictory passages independently. For a formal claim, inspect assumptions and each decisive derivation or attempt a counterexample. For a quantitative claim, recompute the specified statistic when sufficient data and the formula are available, recording inputs and arithmetic. For evidence absence, limit the conclusion to the searched unit and criteria. Read the [legacy mapping](../../taxonomy/legacy-mapping.md) for C1, C2, C3 and C6.

## Required Outputs

Return the [Skill result](../../schemas/skill-result.schema.json) with claim links and, when performed, inspectable derivations or calculation traces.

## Evidence Requirements

Ground each decision in original passages, artifacts or derivations. Record relevant counterevidence and same-setting checks.

## Completion Criteria

Each target has an outcome, an evidence chain, and any unresolved link described.

## Escalation Conditions

Use [literature investigation](../literature-investigation/SKILL.md) for source ambiguity, or [critical reasoning](../critical-reasoning/SKILL.md) for competing explanations or counterexamples.

## Limitations

Specialist mathematical and statistical verification, independent dataset authentication and experiment reproduction remain outside the generic procedure.
