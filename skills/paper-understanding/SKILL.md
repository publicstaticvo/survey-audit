---
name: paper-understanding
description: Extract academic claims and contributions, reconstruct methods and map manuscript structure or internal commitments before verification.
---

## Purpose

Create inspectable targets with the original paper's qualifiers and structure.

## Trigger Conditions

Use when an audit needs a claim inventory, contribution decomposition, method reconstruction, or a structural consistency check.

## Required Inputs

Manuscript version, paper type and scope. Include readable figures and appendices when involved.

## Investigation Guidance

Locate research questions, conclusions and contribution declarations. Break compound statements into individually testable claims while preserving original conditions and links. Connect each contribution to results and claims. Trace procedures from inputs through analysis to outputs, recording unknown steps. For a structural commitment, inspect its intended scope and record what fulfills it or the bounded search for fulfillment. For inconsistent definitions or results, compare matched passages under the same settings. Consult the [legacy mapping](../../taxonomy/legacy-mapping.md) for C1, C4, C5, C7, C8 or C10 artifacts.

## Required Outputs

Return the [Skill result](../../schemas/skill-result.schema.json) and reusable research questions, claims, contributions, method steps and location records as relevant. Use the [shared record format](../../references/shared-records.md) for handoffs.

## Evidence Requirements

Attach original passages and locators. Label reconstructed relationships and state their basis.

## Completion Criteria

Each targeted claim traces to the source and includes its relevant conditions. Each structural check has the matching target scope and outcome.

## Escalation Conditions

Resolve ambiguous version, cross-reference or notation before comparison. Send scientific discrepancies to [scientific verification](../scientific-verification/SKILL.md).

## Limitations

Extraction records what the manuscript asserts. Original graphs, formulas and tables may need visual inspection.
