# SurveyAudit Skills

Version 0.1 helps researchers audit academic papers with traceable evidence. It supports a focused question, such as whether a reported comparison supports a conclusion, and a full-paper audit with an explicit account of remaining uncertainty.

SurveyAudit originally detects reviewer concerns in literature surveys. This framework reuses original detector outputs where the manuscript version and predicate match. It adds three independently extensible layers. The [working taxonomy](taxonomy/underlying-failures.md) describes what can fail. The [Audit Contract](audit-contracts/mandatory-obligations.md) identifies evidence requirements. The [Skill Library](#skill-library) gives agents investigation procedures that they can select and combine.

[Design principles](references/design-principles.md)

## Install and try the example

Obtain this directory and keep its layout. Open it as a workspace in an agent host that can read files and access your manuscript. Use Python 3.10 or newer to validate JSON and render Markdown from the workspace root. Run the commands in your Python environment.

```console
python -m pip install -r requirements.txt
python audit.py validate examples/output/attention-audit.json
python audit.py render examples/output/attention-audit.json --output examples/output/attention-audit.md
python -m unittest discover -s tests -v
```

The report tools use local files and require no API keys. The audit itself uses your agent host and its configured document-reading, search and command tools. For original detector execution, use the existing SurveyAudit backend and its service configuration. [Legacy backend setup and commands](references/legacy-backend.md)

## Audit a paper

With the package directory available to the host, ask:

> Read skills/survey-audit/SKILL.md and use it to audit paper.pdf. Focus on whether the reported comparisons justify the central empirical claims. Write audit.json and audit.md.

Hosts that support skill registration can register the seven Skill directories in place. Preserve access to the adjacent contract, schema and taxonomy files. Reading the entry file as shown above works from a filesystem-enabled host without registration. The entry Skill loads specialist Skills as the evidence warrants and records its choices. It creates a scope-specific contract and gives each obligation an outcome.

For a single investigation, ask:

> Read skills/literature-investigation/SKILL.md. For the claim in Section 4 of paper.pdf, identify the exact source version and locate the evidence establishing what it supports. Return a structured Skill result.

Validate that standalone output with `python audit.py validate RESULT.json --skill-result`.

For the worked example, give your host the [example input](examples/input/attention-audit.md). Its [Markdown report](examples/output/attention-audit.md) and [JSON report](examples/output/attention-audit.json) trace a reported translation comparison and the derivation of a wavelength endpoint. The report distinguishes verified findings, evidence-supported observations requiring confirmation, unresolved questions, and non-applicable obligations. A partial audit records exclusions explicitly.

## Skill Library

| Group | Available in v0.1 | Planned |
| --- | --- | --- |
| [Paper Understanding](skills/paper-understanding/SKILL.md) | Claim extraction, contribution decomposition, method reconstruction and paper structure analysis | Specialized disciplinary extractors |
| [Literature Investigation](skills/literature-investigation/SKILL.md) | Prior work search, citation chasing, reference verification, version tracking and method comparison with host tools | Dedicated source service adapters and automated cross-version passage matching |
| [Scientific Verification](skills/scientific-verification/SKILL.md) | Claim verification, bounded formula checks and transparent recomputation from inspectable data | Dedicated mathematical, dataset and statistical verification protocols |
| [Methodological Analysis](skills/methodological-analysis/SKILL.md) | Design-to-evidence inspection, survey reporting, comparison, synthesis and targeted baseline or ablation inspection | Dedicated benchmark validity, baseline and ablation, and robustness protocols |
| [Critical Reasoning](skills/critical-reasoning/SKILL.md) | Alternative explanation search, counterexample discovery and scope analysis | Domain-specific counterexample suites |
| [Quality Synthesis](skills/quality-synthesis/SKILL.md) | Strength analysis, weakness impact, claim dependencies and qualitative holistic assessment | Cross-disciplinary validation and assessment calibration |

The synthesis evaluates Scholarly Value, Epistemic Credibility and Verifiability, with finding links, repair requirements and conditions for compensation. The judgments apply to the inspected paper and evidence. Taxonomy coverage and assessment reliability across disciplines remain research questions.

## Extend the framework

Add or modify a Skill under `skills/<name>/SKILL.md` using the shared output schema. Compose Skills by selecting targets and sharing the same source, claim and evidence IDs. For additions to failure modes, obligations and domain Skills, see [Contributing](CONTRIBUTING.md) and the [authoring guide](references/skill-authoring-guide.md). Check the [C1–C11 mapping](taxonomy/legacy-mapping.md) before claiming legacy detector equivalence.
