"""Validate and render SurveyAudit reports or inspect original detector artifacts."""

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parent
SCHEMA_BASE = "https://survey-audit.invalid/schemas/"
OUTCOME_PRIORITY = ("Contradicted", "Unresolved", "Verified", "Not Applicable")
FINDING_SECTIONS = {
    "verified": "Verified findings",
    "tentative": "Evidence-supported findings requiring confirmation",
    "unresolved": "Unresolved questions",
    "not_applicable": "Non-applicable findings",
}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def validate_schema(document, filename):
    schemas = {
        path.name: read_json(path) | {"$id": SCHEMA_BASE + path.name}
        for path in (ROOT / "schemas").glob("*.schema.json")
    }
    registry = Registry().with_resources(
        (schema["$id"], Resource.from_contents(schema)) for schema in schemas.values()
    )
    schema = schemas[filename]
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(
        schema, registry=registry, format_checker=Draft202012Validator.FORMAT_CHECKER
    ).validate(document)


def index_records(records, label):
    indexed = {record["id"]: record for record in records}
    if len(indexed) != len(records):
        raise ValueError(f"Duplicate {label} ID")
    return indexed


def require_links(ids, index, label):
    missing = set(ids).difference(index)
    if missing:
        raise ValueError(f"{label} refers to unknown IDs: {', '.join(sorted(missing))}")


def validate_report(report):
    validate_schema(report, "audit-report.schema.json")
    evidence = index_records(report["evidence"], "evidence")
    claims = index_records(report["claims"], "claim")
    findings = index_records(report["findings"], "finding")
    contributions = index_records(report["contributions"], "contribution")
    for claim in claims.values():
        require_links(claim["depends_on"], claims, claim["id"])
        if claim["id"] in claim["depends_on"]:
            raise ValueError(f"{claim['id']} depends on itself")
    for record in [*claims.values(), *findings.values(), *contributions.values(), *report["investigation"]]:
        require_links(record["evidence_ids"], evidence, "Evidence link")
    for record in [*findings.values(), *contributions.values()]:
        require_links(record["claim_ids"], claims, record["id"])
    for name, obligation in report["obligations"].items():
        if obligation["applicability"] == "outside_scope" and report["scope"]["mode"] == "full":
            raise ValueError(f"{name} is outside the scope of a full audit")
        if obligation["applicability"] == "applicable":
            outcomes = {target["outcome"] for target in obligation["targets"]}
            expected = next(outcome for outcome in OUTCOME_PRIORITY if outcome in outcomes)
            if obligation["outcome"] != expected or expected == "Not Applicable":
                raise ValueError(f"{name} has inconsistent applicability or target outcomes")
        for target in obligation["targets"]:
            require_links(target["evidence_ids"], evidence, name)
    for dimension in report["assessment"]["dimensions"].values():
        require_links(dimension["finding_ids"], findings, "Dimensional judgment")
    for impact in report["assessment"]["impacts"]:
        require_links([impact["finding_id"], *impact["compensating_finding_ids"]], findings, "Impact")
        require_links(impact["claim_ids"], claims, "Impact")
        require_links(impact["contribution_ids"], contributions, "Impact")
        for identifier in impact["compensating_finding_ids"]:
            if findings[identifier]["kind"] != "strength" or findings[identifier]["status"] != "verified":
                raise ValueError(f"Compensation requires a verified strength: {identifier}")


def labels(values):
    return ", ".join(values) or "None recorded"


def notes(values):
    return " ".join(values) or "None recorded"


def render_report(report):
    paper = report["paper"]
    scope = report["scope"]
    lines = [
        f"# {paper['title']}", "",
        f"{paper['version']} · {paper['source']}", "",
        f"**Scope ({scope['mode']})** {scope['description']}", "",
        f"**Literature cutoff** {scope['literature_cutoff'] or 'Unspecified'}", "",
        f"**Conclusion** {report['assessment']['conclusion']}", "",
        f"**Reasoning and confidence ({report['confidence']})** {report['reasoning']}", "",
        f"**Limitations** {notes(report['limitations'])}", "",
        f"**Suggested next steps** {notes(report['suggested_next_steps'])}", "",
        "## Research questions, claims and contributions", "",
    ]
    lines.extend(f"- {question}" for question in report["research_questions"])
    for claim in report["claims"]:
        lines.append(f"- **{claim['id']}** {claim['statement']} Evidence {labels(claim['evidence_ids'])}. Dependencies {labels(claim['depends_on'])}.")
    for item in report["contributions"]:
        lines.append(f"- **{item['id']}** {item['statement']} Claims {labels(item['claim_ids'])}. Evidence {labels(item['evidence_ids'])}.")
    for status, title in FINDING_SECTIONS.items():
        lines.extend(["", f"## {title}", ""])
        items = [item for item in report["findings"] if item["status"] == status]
        if not items:
            lines.append("None recorded.")
        for item in items:
            lines.extend([
                f"### {item['id']} · {item['kind'].title()}", "",
                item["statement"], "", item["reasoning"], "",
                f"**Evidence** {labels(item['evidence_ids'])} · **Claims** {labels(item['claim_ids'])} · **Confidence** {item['confidence']}", "",
            ])
            if item.get("failure_categories"):
                lines.extend([f"**Underlying failures** {labels(item['failure_categories'])}", ""])
            for field in ("reviewer_concern", "legacy_categories", "presentation"):
                if field in item:
                    value = item[field]
                    lines.extend([f"**{field.replace('_', ' ').title()}** {labels(value) if isinstance(value, list) else value}", ""])
            if item["limitations"]:
                lines.extend([f"**Limitations** {notes(item['limitations'])}", ""])
            if item["suggested_next_steps"]:
                lines.extend([f"**Suggested next steps** {notes(item['suggested_next_steps'])}", ""])
    lines.extend(["", "## Audit obligations", ""])
    for name, obligation in report["obligations"].items():
        title = name.replace("_", " ").title()
        lines.append(f"- **{title} · {obligation['outcome']}** ({obligation['applicability']}) {obligation['reasoning']}")
        for target in obligation["targets"]:
            lines.append(f"  - {target['target']} · {target['outcome']}. {target['reasoning']} Evidence {labels(target['evidence_ids'])}.")
    lines.extend(["", "## Quality assessment", ""])
    for name, item in report["assessment"]["dimensions"].items():
        title = name.replace("_", " ").title()
        lines.append(f"- **{title}** {item['judgment']} Findings {labels(item['finding_ids'])}. **Uncertainty** {item['uncertainty']}")
    for impact in report["assessment"]["impacts"]:
        critical = "Critical" if impact["critical"] else "Noncritical"
        lines.extend([
            "", f"### Impact of {impact['finding_id']} · {critical}", "",
            f"{impact['importance']} Claims {labels(impact['claim_ids'])}. Contributions {labels(impact['contribution_ids'])}.", "",
            f"**Repair** {impact['repair']}", "",
            f"**Compensation** {impact['compensation']} Related strengths {labels(impact['compensating_finding_ids'])}.",
        ])
    lines.extend(["", "## Investigation trace", ""])
    for item in report["investigation"]:
        lines.append(f"1. **{item['skill']}** {item['decision']} Evidence {labels(item['evidence_ids'])}.")
    lines.extend(["", "## Evidence", ""])
    for item in report["evidence"]:
        lines.extend([
            f"### {item['id']} · {item['kind'].replace('_', ' ').title()}", "",
            f"{item['source']} · {item['version']} · {item['locator']}", "",
            item["content"], "", f"**Role** {item['role']}", "",
        ])
        for field in ("criterion", "coverage", "query", "date", "filters"):
            if field in item:
                lines.extend([f"**{field.title()}** {item[field]}", ""])
    return "\n".join(lines).rstrip() + "\n"


def inspect_legacy(path, module=None):
    report = read_json(path)
    for section in ("weaknesses", "comments"):
        items = report[section]
        if not isinstance(items, list) or any(not isinstance(item, dict) for item in items):
            raise ValueError(f"Expected original report rows in {section}")
    if module is None:
        return report
    return {
        section: [item for item in report[section] if item.get("source_module") == module]
        for section in ("weaknesses", "comments")
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate")
    validate.add_argument("report", type=Path)
    validate.add_argument("--skill-result", action="store_true")
    render = commands.add_parser("render")
    render.add_argument("report", type=Path)
    render.add_argument("--output", type=Path, required=True)
    legacy = commands.add_parser("legacy")
    legacy.add_argument("report", type=Path)
    legacy.add_argument("--module")
    args = parser.parse_args()
    if args.command == "legacy":
        print(json.dumps(inspect_legacy(args.report, args.module), indent=2, ensure_ascii=True))
        return
    report = read_json(args.report)
    if args.command == "validate" and args.skill_result:
        validate_schema(report, "skill-result.schema.json")
        evidence = index_records(report["evidence"], "evidence")
        for finding in index_records(report["findings"], "finding").values():
            require_links(finding["evidence_ids"], evidence, finding["id"])
    else:
        validate_report(report)
    if args.command == "render":
        args.output.write_text(render_report(report), encoding="utf-8", newline="\n")
    else:
        print(f"Valid audit report: {args.report}")


if __name__ == "__main__":
    main()
