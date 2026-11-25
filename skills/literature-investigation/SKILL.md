---
name: literature-investigation
description: Search for prior work, chase citations, resolve reference identity and versions, and compare source methods or attribution for a paper audit.
---

## Purpose

Establish the identity, relevance and evidential role of external works.

## Trigger Conditions

Use for ambiguous references, citation support, novelty, attribution, coverage or source retrieval.

## Required Inputs

Proposition or search topic, manuscript version and literature cutoff, bibliography entries or candidate identifiers.

## Investigation Guidance

Resolve DOI or repository IDs and reconcile title, authors, publication status and versions against authoritative records. Search by terms, aliases, and citation neighbors as relevant. Trace attributed statements to source sections. Compare prior work by task, assumptions, method, output and evidence. For potentially missing work, establish date, scope, substantial relevance and existing discussion or attribution. Use graph or abstract signals to prioritize inspection. Follow the [legacy mapping](../../taxonomy/legacy-mapping.md) when reusing C2, C3, C5, C9, C10 or C11 artifacts.

## Required Outputs

Return the [Skill result](../../schemas/skill-result.schema.json) with identity, version, source locations, search traces and relevant comparison records.

## Evidence Requirements

Distinguish authoritative metadata from substantive claim evidence. Identify exact version differences that matter. Record original passages and inclusion decisions.

## Completion Criteria

Account for each selected reference or search target with evidence or a documented unresolved outcome.

## Escalation Conditions

Seek full text for substantive claims and primary records for conflicting identities. Use [scientific verification](../scientific-verification/SKILL.md) when the claim requires inference from the retrieved source.

## Limitations

Search coverage and access vary. Retrieval scores measure discovery signals.
