---
name: survey-audit
description: Audit an academic paper or a requested subset of its claims using evidence-linked investigation and a structured report. Use for full-paper or partial academic audits.
---

## Purpose

Determine which propositions the available evidence supports and how verified strengths and weaknesses affect the paper.

## Trigger Conditions

Use for an evidence-based paper audit, including a targeted review spanning several investigation capabilities.

## Required Inputs

Manuscript and version, requested scope, and any available sources or artifacts. Identify a literature cutoff when judging coverage or priority. Read the [Audit Contract](../../audit-contracts/mandatory-obligations.md) and [evidence requirements](../../audit-contracts/evidence-requirements.md).

## Investigation Guidance

Identify research questions, contributions, central claims and dependencies using [paper understanding](../paper-understanding/SKILL.md). Instantiate the contract with targets and applicability. Keep a shared report draft with stable IDs for claims, evidence and findings. Choose investigations based on what could change the judgment:

- Resolve sources, check versions and trace attribution with [literature investigation](../literature-investigation/SKILL.md).
- Examine claim support, conflicts and checkable calculations with [scientific verification](../scientific-verification/SKILL.md).
- Examine design, methods and synthesis with [methodological analysis](../methodological-analysis/SKILL.md).
- Explore contrary evidence, alternative explanations and scope with [critical reasoning](../critical-reasoning/SKILL.md).
- Assess importance, dependencies and three dimensions with [quality synthesis](../quality-synthesis/SKILL.md).

Invoke by reading the linked Skill and applying it to selected targets. Compose Skills using the [shared record format](../../references/shared-records.md). Reuse existing records after checking version, location, and relevance. Record investigation decisions in order, including which observation triggered follow-up. For SurveyAudit artifacts, apply the [legacy mapping](../../taxonomy/legacy-mapping.md).

If the input is a literature survey and the requested scope matches an original detector, consult [legacy execution](../../references/legacy-backend.md) to inspect a compatible report or invoke the configured original module and its dependencies. Carry the detector predicate, source locations and intermediate artifacts into the reasoning. Evaluate the returned evidence against the current obligation before assigning its outcome.

## Required Outputs

Write JSON conforming to the [report schema](../../schemas/audit-report.schema.json). Include findings, evidence, reasoning, confidence, limitations and suggested next steps. Produce readable Markdown via `python audit.py render REPORT.json --output REPORT.md` from the framework root.

## Evidence Requirements

Ground claims, findings and synthesis in stable source or evidence IDs. Use the [working taxonomy](../../taxonomy/underlying-failures.md) for underlying defects and record presentation separately. Track assessed scope and external searches.

## Completion Criteria

Account for all eight obligations with applicability, targets, reasoning and outcomes. Track material strengths, weaknesses, dependencies and uncertainty within scope. Run `python audit.py validate REPORT.json` from the framework root.

## Escalation Conditions

Prioritize central disputed claims and contradictions. Investigate with qualified primary sources, verified artifact details or an independent route. Report remaining material obstacles as unresolved.

## Limitations

Access and disciplinary expertise constrain claims of verification. The working taxonomy and holistic judgments require empirical validation.
