# SurveyAudit backend

An existing SurveyAudit checkout and its configured environment supply the original detectors. The release package contains the Agent Skills and audit tools. Legacy source distribution and service setup remain external. The integration was inspected against checkout revision `9c8d3d9c670135336bad49eee374b20aa0d1f211` and the local working files.

The [checkout coverage](../taxonomy/legacy-mapping.md#checkout-coverage) notes identify documented procedures that lack a callable route in the inspected version.

## Reuse an existing report

From the framework root, run `python audit.py legacy path/to/14_final_report.json`. To inspect one route add `--module 07_fact_check`. The command reads the original JSON and keeps all fields of each selected item. With a module filter, counts and severity metadata describe the unfiltered report, so only the selected items are returned. Retain the original file and intermediate artifacts as provenance.

Before reusing a record, establish the manuscript and source versions, run scope, configuration, and the record's category-specific predicate. Inspect `result.json` and the cited module artifacts for the evidence behind report fields such as `checked_scope`, `example`, and `evidence`. The original report places determinate issues in `weaknesses` and unresolved or candidate items in `comments`; reclassify only after checking the original evidence and predicate. Absence of a report row never establishes that an obligation was met. Generate strengths independently.

## Run the original detector

Use the interpreter already configured for the existing backend. Keep the checkout directory named `triage` and run from its parent:

```console
python -m triage.main --help
python -m triage.main --paper path/to/paper.json --query "survey topic" --tool-config path/to/config.yaml --output-dir path/to/new-run --run-modules 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
```

Use a supported parsed paper JSON or LaTeX source. The config is read by the backend's `ToolConfig.from_yaml`. Provide your own endpoints and credentials for the configured agent, external and fallback LLMs, reranker and scholarly or web search. Set GROBID, embedding and proxy endpoints where used. Set the evaluation date and keep source verification enabled. Use the working backend configuration as the reference for field names, paper input shape and required services. Keep it local. Live availability depends on that deployment.

For narrower runs, choose modules from the mapping and include their preprocessing dependencies or use same-paper caches. Module 01 and the classified paper provide shared inputs. Module 07 depends on 06, and 13 consumes 06/07. Modules 08 and 09 use the literature pool when available, with 08 also using prior surveys and entities. Module 14 aggregates selected or cached results. Inspect which modules ran before interpreting a partial report. Module 15 is a separate legacy scoring route and is outside this framework's synthesis.

To rerun only the deterministic structural detector for selection, comparison, synthesis and document-level future work, use the framework's wrapper with the backend interpreter. It reads the original classified input and emits the unchanged module result. The output path must be new. The module uses existing semantic extractions and makes no additional service calls.

```console
python legacy_structure.py path/to/triage path/to/02_classified_paper.json --output structure-result.json
```

See [detector mapping](../taxonomy/legacy-mapping.md) for category definitions and limitations. Compare source-level records for regression testing with the original artifacts from the same case and run configuration.

For the report compatibility regression, set `SURVEYAUDIT_LEGACY_REPORTS` to a directory tree containing original `14_final_report.json` files, then run `python -m unittest discover -s tests -v` from the framework root. This test verifies preservation of all report fields and of each selected module's rows. For the structural detector regression, also set `SURVEYAUDIT_LEGACY_CHECKOUT` to the backend checkout and `SURVEYAUDIT_LEGACY_STRUCTURE_CASE` to a run containing `02_classified_paper.json`. It compares the wrapper's full output against a direct execution of the original module on the same input. Comparing to archived module output also requires the matching backend revision and classified input. The other detector routes require configured services for a fresh run.

The v0.1 integration check covered 581 original reports and 10,772 rows across eight source modules. On human test case 001, the structural wrapper matched direct execution on the current checkout. Its output differs from that case's archived module 12 output. The archive has no verified matching configuration and code revision for a historical equivalence claim.
