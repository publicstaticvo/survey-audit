---
name: methodological-analysis
description: Assess whether experimental or survey methods, comparisons, and evidence can support a paper's claims.
---

## Purpose

Identify which conclusions the stated design and analysis can sustain.

## Trigger Conditions

Use for method-evidence alignment, study-selection reporting, missing comparison or missing synthesis.

## Required Inputs

Claim, research question, relevant methods, corpus or data, analysis, comparisons and outputs.

## Investigation Guidance

Connect the claim to the sampled population, measurement, comparator, analysis and outcome. For empirical design, inspect comparison conditions, metric fit, sampling and what an ablation actually isolates. For surveys, inspect selection reporting, explore like-for-like comparisons, and identify where a cross-study synthesis would be justified. Show why each proposed omission matters to a specific claim. Use the [legacy mapping](../../taxonomy/legacy-mapping.md) for C4 and C6–C8 records.

## Required Outputs

Return the [Skill result](../../schemas/skill-result.schema.json) with the design-to-claim chain, relevant assumptions, and affected outcomes.

## Evidence Requirements

Locate methods and results, and record bounded scope and eligibility for any absence. Distinguish reporting limitations from demonstrated design flaws.

## Completion Criteria

Each target has a design-to-evidence judgment or a precise reason it remains unresolved.

## Escalation Conditions

Use [critical reasoning](../critical-reasoning/SKILL.md) if the inference depends on a plausible alternative. Identify additional measurements or materials when conclusions are sensitive to their absence.

## Limitations

Generic design inspection does not establish benchmark validity or robustness across settings. Dedicated protocols are planned.
