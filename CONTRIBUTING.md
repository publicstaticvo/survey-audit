# Contributing

- **Failure mode** Describe the failed mechanism, give a bounded example and an adjacent case, and state what evidence would distinguish them. Preserve stable labels or document aliases when renaming or merging categories.
- **Audit obligation** Define purpose, applicability, inputs, evidence, completion, escalation and outcomes. Explain which claims warrant the obligation and how it interacts with existing requirements. Extend the report schema and its validation when the contract changes.
- **Skill** Add a distinct investigation procedure with applicable inputs, real tools or reproducible reasoning, and a public or authorized example. Link the Skill from the orchestrator when it can resolve an identifiable class of audit decisions.
- **Legacy detector** Preserve the original artifact and evidence fields, name the backend revision and verify the original predicate from raw outputs. Record whether the test reuses artifacts or actually executes the detector.

Run `python -m unittest discover -s tests -v` and validate and render affected example reports. See the [authoring guide](references/skill-authoring-guide.md).
