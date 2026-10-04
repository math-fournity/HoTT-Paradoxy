#!/usr/bin/env python3
"""Positive and negative tests for mathematical proof delivery governance."""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = Path(__file__).with_name("verify_math_proof_delivery_governance.py")
SPEC = importlib.util.spec_from_file_location("verify_math_proof_delivery_governance", SCRIPT)
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class MathProofDeliveryGovernanceTests(unittest.TestCase):
    def fixture(self) -> tuple[tempfile.TemporaryDirectory, Path]:
        temp = tempfile.TemporaryDirectory(prefix="math-proof-governance-")
        root = Path(temp.name)
        required = (
            set(V.REQUIRED_MARKERS)
            | set(V.ROUTING_MARKERS)
            | {"feature-list.md", "rulings.md", "HoTT/README.md"}
        )
        for rel in required:
            target = root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / rel).read_bytes())
        (root / "HoTT/formal").mkdir(parents=True, exist_ok=True)
        (root / "HoTT/verification/runs").mkdir(parents=True, exist_ok=True)
        return temp, root

    def test_current_project_contract_passes(self) -> None:
        result = V.validate(ROOT)
        self.assertEqual(result["status"], "PASS_WITH_SCOPE")
        self.assertEqual(set(result["required_run_files"]), V.REQUIRED_RUN_FILES)

    def test_missing_skill_marker_fails_closed(self) -> None:
        temp, root = self.fixture()
        try:
            rel = ".codex/skills/hott-paradox-research/SKILL.md"
            path = root / rel
            path.write_text(path.read_text(encoding="utf-8").replace(V.MARKER, "marker-removed"), encoding="utf-8")
            with self.assertRaisesRegex(V.ProofGovernanceError, "MARKER_MISSING"):
                V.validate(root)
        finally:
            temp.cleanup()

    def test_missing_navigation_route_fails_closed(self) -> None:
        temp, root = self.fixture()
        try:
            rel = ".codex/AGENTS.md"
            path = root / rel
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    "根 AGENTS `MATH_PROOF_BEFORE_DELIVERY_V1`",
                    "route-removed",
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(V.ProofGovernanceError, "ROUTING_MARKER_MISSING"):
                V.validate(root)
        finally:
            temp.cleanup()

    def test_missing_local_skill_route_fails_closed(self) -> None:
        temp, root = self.fixture()
        try:
            rel = ".codex/skills/hott-local-session-governance/SKILL.md"
            path = root / rel
            path.write_text(
                path.read_text(encoding="utf-8").replace(
                    ".codex/cognition/PROTOCOL.md",
                    "protocol-route-removed",
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(V.ProofGovernanceError, "ROUTING_MARKER_MISSING"):
                V.validate(root)
        finally:
            temp.cleanup()

    def test_tmp_authoritative_root_fails_closed(self) -> None:
        temp, root = self.fixture()
        try:
            path = root / "HoTT/verification/runs/README.md"
            path.write_text(path.read_text(encoding="utf-8").replace(
                "authoritative_run_root: HoTT/verification/runs",
                "authoritative_run_root: /tmp/proofs",
            ), encoding="utf-8")
            with self.assertRaisesRegex(V.ProofGovernanceError, "ROOT_CONTRACT_INVALID"):
                V.validate(root)
        finally:
            temp.cleanup()

    def test_incomplete_run_file_contract_fails_closed(self) -> None:
        temp, root = self.fixture()
        try:
            path = root / "HoTT/verification/runs/README.md"
            path.write_text(path.read_text(encoding="utf-8").replace(
                "RUN.json,stdout.txt,stderr.txt,environment.txt,source-manifest.json",
                "RUN.json,stdout.txt,environment.txt,source-manifest.json",
            ), encoding="utf-8")
            with self.assertRaisesRegex(V.ProofGovernanceError, "RUN_REQUIRED_FILES_INVALID"):
                V.validate(root)
        finally:
            temp.cleanup()


if __name__ == "__main__":
    unittest.main(verbosity=2)
