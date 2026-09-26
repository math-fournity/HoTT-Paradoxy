#!/usr/bin/env python3
"""Mechanical integration tests for the real local Goal6 loading route.

These checks do not classify natural-language tasks or certify AI behavior.
"""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("mo3_cognition", ROOT / ".codex/tools/cognition_runtime.py")
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


class GoalRouteTests(unittest.TestCase):
    def test_both_profiles_include_highest_and_route_without_changing_four_set(self):
        for profile in ("governance", "research"):
            plan = R.plan(ROOT, profile=profile)
            paths = [d["path"] for d in plan["documents"]]
            self.assertIn("最高指示.md", paths)
            self.assertIn(".codex/cognition/TASK_ROUTING.md", paths)
            self.assertEqual([p for p in paths if p in R.FULL_SET], list(R.FULL_SET))
            self.assertEqual(plan["hydration_diagnostics"]["query_first_promoted"], [])

    def test_highest_read_to_eof_has_exact_bytes_but_no_understanding_certificate(self):
        plan = R.plan(ROOT)
        part = R.read_chunk(ROOT, plan["snapshot"], "最高指示.md", 1, 262144)
        self.assertIsNone(part["next_start_line"])
        self.assertEqual(part["text"].encode(), (ROOT / "最高指示.md").read_bytes())
        self.assertEqual(part["model_context"], "NOT_CERTIFIED_BY_TOOL")

    def test_stale_snapshot_cannot_read_as_current(self):
        with self.assertRaisesRegex(R.CognitionError, "STALE_SNAPSHOT"):
            R.read_chunk(ROOT, "0" * 64, "最高指示.md")

    def test_missing_mandatory_highest_fails_plan(self):
        original = R.read_bytes
        def missing(root, relative):
            if relative == "最高指示.md":
                raise R.CognitionError("MISSING_REQUIRED_HIGHEST")
            return original(root, relative)
        with patch.object(R, "read_bytes", side_effect=missing):
            with self.assertRaisesRegex(R.CognitionError, "MISSING_REQUIRED_HIGHEST"):
                R.plan(ROOT)

    def test_added_role_identity_is_validated_by_existing_runtime(self):
        roles = json.loads((ROOT / R.ROLES).read_text())
        self.assertEqual(roles["roles"]["machine_overview_execution"]["name"], "hott-machine-overview-execution")
        self.assertEqual(roles["roles"]["machine_overview_audit"]["name"], "hott-machine-overview-audit")
        bad = copy.deepcopy(roles)
        bad["roles"]["machine_overview_audit"]["name"] = "wrong-auditor"
        def get(relative):
            return json.dumps(bad).encode() if relative == R.ROLES else (ROOT / relative).read_bytes()
        with self.assertRaisesRegex(R.CognitionError, "SKILL_ROLE_EXTRA_FRONTMATTER_MISMATCH"):
            R.validate_roles(get)

    def test_missing_role_source_is_rejected(self):
        def get(relative):
            if relative == ".codex/skills/hott-machine-overview-audit/SKILL.md":
                raise R.CognitionError("MISSING_AUDIT_SKILL")
            return (ROOT / relative).read_bytes()
        with self.assertRaisesRegex(R.CognitionError, "MISSING_AUDIT_SKILL"):
            R.validate_roles(get)

    def test_prompts_bounded_and_closures_monolithic(self):
        for role in ("A", "B"):
            body = (ROOT / f"第三轮机器统观/治理整备/Session-{role}-goal提示词.txt").read_text()
            self.assertGreater(len(body), 100)
            self.assertLessEqual(len(body), 4000)
        for name in ("goal-6.md", "goal-6-audit.md"):
            body = (ROOT / name).read_text()
            self.assertNotIn("governance-shard-index:", body)
            self.assertFalse((ROOT / Path(name).stem).is_dir())


if __name__ == "__main__":
    unittest.main()
