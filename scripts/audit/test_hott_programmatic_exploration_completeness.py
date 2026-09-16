from __future__ import annotations

import re
import subprocess
import unittest
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INDEX = (
    ROOT
    / ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md"
)
SHARDS = INDEX.with_suffix("")
IMPORT = ROOT / "audit/imports/machine-overview-computability-20260914/IMPORT.json"


def logical_text() -> str:
    return INDEX.read_text(encoding="utf-8") + "\n" + "\n".join(
        path.read_text(encoding="utf-8") for path in sorted(SHARDS.glob("*.md"))
    )


class HoTTProgrammaticExplorationCompletenessTest(unittest.TestCase):
    def test_v2_index_and_all_six_shards_are_structurally_valid(self) -> None:
        result = subprocess.run(
            ["python3", "-B", "scripts/audit/verify_governance_shards.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        index = INDEX.read_text(encoding="utf-8")
        self.assertIn("governance-shard-index:v2", index)
        self.assertIn("全文 = 本索引 + 下方 6 个分片", index)
        self.assertEqual(len(list(SHARDS.glob("*.md"))), 6)

    def test_construct_operator_and_direction_denominators_are_explicit(self) -> None:
        text = logical_text()
        for index in range(1, 15):
            self.assertIn(f"`TC-{index:02d}`", text)
            self.assertIn(f"`OP-{index:02d}`", text)
        for family in (
            "A-DelayCollapse",
            "A-ContinuousCarrier",
            "B-MereToChosen",
            "B-ProofToSolver",
            "G-Code",
            "G-HoTTSyntax",
        ):
            self.assertIn(family, text)
        self.assertIn("强制纳入 OP-14 反解释", text)

    def test_generators_oracles_unknown_ingress_and_completion_are_connected(self) -> None:
        text = logical_text()
        for generator in range(1, 7):
            self.assertIn(f"GNR-{generator}", text)
        for ingress in range(1, 8):
            self.assertIn(f"`UI-{ingress:02d}`", text)
        for stage in range(10):
            self.assertRegex(text, rf"`P{stage}`")
        for literal in (
            "dovetailing",
            "task-preserving reduction",
            "natural HoTT use",
            "Independent taxonomy comparison",
            "意外发现的吸收协议",
            "NO_HIT_WITHIN_SCOPE",
            "开放世界意味着每个已完成 pass",
        ):
            self.assertIn(literal, text)

    def test_project_agents_and_skills_require_plan_consumption(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        research = (
            ROOT / ".codex/skills/hott-paradox-research/SKILL.md"
        ).read_text(encoding="utf-8")
        governance = (
            ROOT / ".codex/skills/hott-local-session-governance/SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("HOTT_PARADOX_PROGRAMMATIC_COMPLETENESS_V1", agents)
        self.assertIn(INDEX.name, agents)
        self.assertIn("version: \"1.9.0\"", research)
        self.assertIn("程序化激发与探索包络", research)
        self.assertIn("version: \"3.7.0\"", governance)
        self.assertIn("系统化探索的完备性回评", governance)
        self.assertIn("索引声明的全部 shards", agents)
        self.assertIn("索引声明的全部 shards", research)
        self.assertEqual(
            len(re.findall(r"TheoryConstruct × AbstractionChange", agents)),
            1,
        )

    def test_computability_literature_audit_and_import_are_bound(self) -> None:
        manifest = json.loads(IMPORT.read_text(encoding="utf-8"))
        self.assertEqual(
            manifest["evidence_boundary"],
            "IMPORTED_CANDIDATE_EVIDENCE_NOT_MAIN_MATHEMATICAL_ACCEPTANCE",
        )
        self.assertEqual(len(manifest["files"]), 5)
        for row in manifest["files"]:
            path = ROOT / row["path"]
            raw = path.read_bytes()
            self.assertEqual(len(raw), row["bytes"], row["path"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(), row["sha256"], row["path"])
        source = ROOT / manifest["user_source"]["path"]
        raw = source.read_bytes()
        self.assertEqual(len(raw), manifest["user_source"]["bytes"])
        self.assertEqual(hashlib.sha256(raw).hexdigest(), manifest["user_source"]["sha256"])
        audit = (SHARDS / "006 - 计算合法性主线与学术谱系覆盖审计.md").read_text(encoding="utf-8")
        for literal in (
            "41 个 `LIT-*`",
            "`FULL_TEXT_TO_READ` | 19",
            "Oracle Modalities",
            "Generalized Decidability via Brouwer Trees",
            "The Groupoid-Syntax of Type Theory Is a Set",
            "`R2` | 对全部程序/输入的停机边界",
            "R2_SYNTHETIC_REDUCTION_DUAL_KERNEL_COMPLETE",
            "R2_CONDITIONAL_INTERNAL_NOT_DECIDABLE_MACHINE_REPLAYED",
            "decidable P→enumerable(complement SBTM_HALT)",
            "C-214–C-218",
            "C-219–C-222",
            "C-223–C-226",
            "C-227–C-232",
            "G_HOTT_SYNTAX_FIRST_EXACT_MACHINE_REPLAYED_SLICE",
            "TWO_LEVEL_CONTEXT_UNIFORM_REPLACEMENT_IMPLIES_INNER_UIP_MACHINE_PROVED",
            "LIT-HOTT-COMPUTABILITY-001",
            "NATURAL-CONSUMER-002",
            "LIT_DENOMINATOR_V1_FROZEN",
            "R1_MACHINE_PROVED_IN_MAIN_WITH_F011",
            "MP-CUBICAL-MACHINE-HALTING-001",
        ):
            self.assertIn(literal, audit)


if __name__ == "__main__":
    unittest.main()
