---
name: quality-synthesis
description: Synthesize evidence-backed strengths, weaknesses and claim dependencies into dimensional academic judgments.
---

## Purpose

Assess Scholarly Value, Epistemic Credibility and Verifiability based on the investigated claims.

## Trigger Conditions

Use when a full or partial audit requires interpretation of the importance and interaction of findings.

## Required Inputs

Audit scope, claims, contributions, their dependencies, findings, obligation outcomes, and source access limitations.

## Investigation Guidance

Identify positive results with evidence. Link each material weakness to the claims and contributions it affects. Explain severity and whether repair requires rewriting, reanalysis, new evidence or a change to the main claim. A strength can compensate when it supports the same claim through independent grounds or preserves a separable contribution. Explain which dependency is covered, and identify critical defects that leave the intended claim without sufficient independent support. Assess value by the contribution to knowledge or practice, credibility by how the inference follows from evidence, and verifiability by whether readers can inspect the source and trace the analysis.

## Required Outputs

Return the [Skill result](../../schemas/skill-result.schema.json) plus three dimensional judgments, a scoped conclusion, impact and repair records, demonstrated compensation relationships and unresolved dependencies. The [report schema](../../schemas/audit-report.schema.json) defines the combined form.

## Evidence Requirements

Reference finding IDs and evidence-backed claim dependencies. Support each strength substantively. Carry uncertainty into every affected judgment.

## Completion Criteria

Every material strength and weakness has a justified effect or a reason its effect remains unclear. All three dimensions have a bounded judgment. Use qualitative judgments without an aggregate numeric score.

## Escalation Conditions

Reopen investigation when a central judgment depends on an uncertain source, assumption or strength.

## Limitations

Dimension judgments are reasoned assessments under the audit scope. Cross-disciplinary validity and empirically calibrated ratings are planned.
