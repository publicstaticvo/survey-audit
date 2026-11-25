"""Exercise the published example and, optionally, original SurveyAudit runs."""

import asyncio
import os
import re
import unittest
from collections import Counter
from pathlib import Path
from subprocess import check_output
import sys
from uuid import uuid4
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema import ValidationError
from markdown_it import MarkdownIt

from audit import ROOT, inspect_legacy, read_json, render_report, validate_report, validate_schema


EXAMPLE = ROOT / "examples" / "output" / "attention-audit.json"
EXPECTED_HEADINGS = {
    "Purpose", "Trigger Conditions", "Required Inputs", "Investigation Guidance",
    "Required Outputs", "Evidence Requirements", "Completion Criteria",
    "Escalation Conditions", "Limitations",
}


def local_links(markdown):
    for group in MarkdownIt().parse(markdown):
        for token in group.children or []:
            if token.type == "link_open":
                url = urlsplit(token.attrGet("href"))
                if not url.scheme and url.path:
                    yield unquote(url.path)


class FrameworkTests(unittest.TestCase):
    def test_skill_packages(self):
        skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
        entry = ROOT / "skills" / "survey-audit" / "SKILL.md"
        self.assertIn(entry, skills)
        for path in skills:
            with self.subTest(skill=path.parent.name):
                text = path.read_text(encoding="utf-8")
                self.assertTrue(text.startswith("---\n"))
                frontmatter, delimiter, body = text.removeprefix("---\n").partition("\n---\n")
                self.assertTrue(delimiter)
                metadata = yaml.safe_load(frontmatter)
                self.assertEqual(metadata["name"], path.parent.name)
                self.assertRegex(metadata["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
                self.assertLessEqual(len(metadata["name"]), 64)
                self.assertIn(len(metadata["description"]), range(1, 1025))
                self.assertTrue(EXPECTED_HEADINGS.issubset(re.findall(r"^## (.+)$", body, re.M)))
        linked = {(entry.parent / link).resolve() for link in local_links(entry.read_text(encoding="utf-8"))}
        self.assertTrue(set(skills) - {entry} <= linked)

    def test_public_document_links(self):
        for directory in ("skills", "taxonomy", "audit-contracts", "examples", "references"):
            for path in (ROOT / directory).rglob("*.md"):
                self.assert_document_links(path)
        for path in ROOT.glob("*.md"):
            self.assert_document_links(path)

    def assert_document_links(self, path):
        for link in local_links(path.read_text(encoding="utf-8")):
            with self.subTest(document=path.name, link=link):
                self.assertTrue((path.parent / link).exists())

    def test_example_and_rendering(self):
        report = read_json(EXAMPLE)
        validate_report(report)
        self.assertEqual(render_report(report), EXAMPLE.with_suffix(".md").read_text(encoding="utf-8"))
        self.assertGreater(len({step["skill"] for step in report["investigation"]}), 1)

    def test_standalone_result_from_real_audit(self):
        report = read_json(EXAMPLE)
        result_keys = ("findings", "evidence", "reasoning", "confidence", "limitations", "suggested_next_steps")
        validate_schema({key: report[key] for key in result_keys}, "skill-result.schema.json")

    def test_missing_evidence_is_rejected(self):
        report = read_json(EXAMPLE)
        report["findings"][0]["evidence_ids"] = []
        with self.assertRaises(ValidationError):
            validate_report(report)

    def test_dangling_evidence_is_rejected(self):
        report = read_json(EXAMPLE)
        report["findings"][0]["evidence_ids"] = ["missing"]
        with self.assertRaisesRegex(ValueError, "unknown IDs"):
            validate_report(report)

    def test_unresolved_target_cannot_be_marked_verified(self):
        report = read_json(EXAMPLE)
        report["obligations"]["scope_verification"]["outcome"] = "Verified"
        with self.assertRaisesRegex(ValueError, "inconsistent"):
            validate_report(report)

    def test_published_validation_command(self):
        output = check_output([sys.executable, str(ROOT / "audit.py"), "validate", str(EXAMPLE)], text=True)
        self.assertIn("Valid audit report", output)


class LegacyCompatibilityTests(unittest.TestCase):
    @unittest.skipUnless(os.environ.get("SURVEYAUDIT_LEGACY_REPORTS"), "Set SURVEYAUDIT_LEGACY_REPORTS to existing runs")
    def test_original_reports_preserve_every_field(self):
        root = Path(os.environ["SURVEYAUDIT_LEGACY_REPORTS"])
        paths = sorted(root.rglob("14_final_report.json"))
        self.assertTrue(paths, f"No original reports in {root}")
        rows = Counter()
        for path in paths:
            original = read_json(path)
            self.assertEqual(inspect_legacy(path), original)
            sections = ("weaknesses", "comments")
            modules = {item["source_module"] for section in sections for item in original[section]}
            for module in modules:
                selected = inspect_legacy(path, module)
                for section in sections:
                    self.assertEqual(selected[section], [
                        item for item in original[section] if item["source_module"] == module
                    ])
                    rows[module] += len(selected[section])
        self.assertTrue(rows)
        print(f"Original report compatibility: {len(paths)} reports, {rows.total()} rows, {len(rows)} source modules")

    @unittest.skipUnless(os.environ.get("SURVEYAUDIT_LEGACY_STRUCTURE_CASE"), "Set SURVEYAUDIT_LEGACY_STRUCTURE_CASE to an original run")
    def test_replay_original_structure_detector(self):
        checkout = Path(os.environ["SURVEYAUDIT_LEGACY_CHECKOUT"]).resolve()
        sys.path.insert(0, str(checkout.parent))
        from triage.structure.structure_check import StructureCheck
        from triage.utility.paper_elements import Paper

        case = Path(os.environ["SURVEYAUDIT_LEGACY_STRUCTURE_CASE"])
        classified = case / "02_classified_paper.json"
        paper = Paper.from_skeleton(read_json(classified))
        original = asyncio.run(StructureCheck()(paper))
        work = ROOT / ".runs"
        work.mkdir(exist_ok=True)
        output = work / f"structure-{uuid4()}.json"
        self.addCleanup(output.unlink, missing_ok=True)
        check_output([sys.executable, str(ROOT / "legacy_structure.py"), str(checkout), str(classified), "--output", str(output)])
        self.assertEqual(read_json(output), original)


if __name__ == "__main__":
    unittest.main()
