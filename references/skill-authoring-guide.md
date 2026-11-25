# Authoring Skills

Create `skills/<name>/SKILL.md` with YAML `name` and `description`. Name the directory and Skill identically using lowercase words separated by hyphens. Describe the specific invocation context.

Use the sections Purpose, Trigger Conditions, Required Inputs, Investigation Guidance, Required Outputs, Evidence Requirements, Completion Criteria, Escalation Conditions and Limitations. Define applicability and verifiable completion. Provide investigation routes with conditions for choosing among them. Reference the [shared Skill result](../schemas/skill-result.schema.json) and document additional fields the Skill returns. Quote or locate evidence precisely and report uncertainty under the [evidence requirements](../audit-contracts/evidence-requirements.md).

When calling another Skill, provide the proposition, manuscript version, audit scope and relevant IDs. Return inspectable records to the caller. When reusing an earlier result, check version, scope and the evidential role of the returned record.

Run the test suite and exercise the Skill on an authorized input with a consequential decision. Record the actual tools and coverage of the test.
