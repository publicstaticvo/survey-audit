# Shared audit records

The [Skill result schema](../schemas/skill-result.schema.json) defines the shared claim, contribution, finding and evidence records. Copy the same records into the report and standalone results. Assign an ID once, preserve it across calls, and merge evidence only after checking its version, locator and role.

- **Claim** Use `id`, `statement`, `evidence_ids` and `depends_on`. Preserve population, metric, date and other qualifiers within the statement. `depends_on` lists claim IDs.
- **Contribution** Use `id`, `statement`, `claim_ids` and `evidence_ids`.
- **Target-specific observation** Use `reasoning` to explain the check and connect related evidence through `evidence_ids`. Use a finding for a strength, weakness or question the next Skill must act on. Use a search trace for retrieval details and an artifact for a calculation or reconstructed method.
- **Additional records** Add Skill-specific fields when they benefit the caller. For reusable claims and contributions, use top-level `claims` and `contributions` arrays with the shared record shape.
