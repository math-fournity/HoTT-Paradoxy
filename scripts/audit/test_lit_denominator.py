from __future__ import annotations

import gzip
import hashlib
import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / ".codex/research/hott/LIT-DENOMINATOR-001.md"
SHARDS = INDEX.with_suffix("")
SNAPSHOT = ROOT / "audit/literature/LIT-DENOMINATOR-001/discovery-20260914"


class LiteratureDenominatorTest(unittest.TestCase):
    def test_v2_document_has_all_five_shards(self) -> None:
        index = INDEX.read_text(encoding="utf-8")
        self.assertIn("governance-shard-index:v2", index)
        self.assertIn("全文 = 本索引 + 下方 5 个分片", index)
        self.assertEqual(len(list(SHARDS.glob("*.md"))), 5)
        result = subprocess.run(
            ["python3", "-B", "scripts/audit/verify_governance_shards.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_discovery_manifest_and_raw_payloads_are_bound(self) -> None:
        manifest = json.loads((SNAPSHOT / "MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["query_count"], 18)
        self.assertEqual(manifest["expected_fetches"], 36)
        self.assertEqual(manifest["successful_fetches"], 36)
        self.assertEqual(manifest["failed_fetches"], 0)
        candidate_raw = (SNAPSHOT / manifest["candidate_path"]).read_bytes()
        self.assertEqual(len(candidate_raw), manifest["candidate_bytes"])
        self.assertEqual(hashlib.sha256(candidate_raw).hexdigest(), manifest["candidate_sha256"])
        for row in manifest["fetches"]:
            compressed = (SNAPSHOT / row["raw_path"]).read_bytes()
            self.assertEqual(len(compressed), row["gzip_bytes"])
            self.assertEqual(hashlib.sha256(compressed).hexdigest(), row["gzip_sha256"])
            raw = gzip.decompress(compressed)
            self.assertEqual(len(raw), row["raw_bytes"])
            self.assertEqual(hashlib.sha256(raw).hexdigest(), row["raw_sha256"])

    def test_triage_is_total_non_excluding_and_seed_gaps_are_visible(self) -> None:
        triage = json.loads((SNAPSHOT / "TRIAGE.json").read_text(encoding="utf-8"))
        receipt = json.loads((SNAPSHOT / "TRIAGE-RECEIPT.json").read_text(encoding="utf-8"))
        self.assertEqual(triage["total"], 1941)
        self.assertEqual(
            triage["counts"],
            {
                "ADJACENT_TITLE_SIGNAL": 164,
                "DIRECT_TITLE_SIGNAL": 32,
                "UNCLASSIFIED_TITLE_INSUFFICIENT": 1745,
            },
        )
        self.assertEqual(sum(triage["counts"].values()), triage["total"])
        self.assertEqual(triage["seed_count"], 33)
        self.assertEqual(triage["seed_exact_matches"], 13)
        self.assertEqual(triage["seed_manual_entries"], 20)
        triage_raw = (SNAPSHOT / "TRIAGE.json").read_bytes()
        self.assertEqual(receipt["triage"]["bytes"], len(triage_raw))
        self.assertEqual(receipt["triage"]["sha256"], hashlib.sha256(triage_raw).hexdigest())
        self.assertEqual(receipt["triage"]["total"], triage["total"])
        self.assertEqual(receipt["triage"]["direct_title_signal"], triage["counts"]["DIRECT_TITLE_SIGNAL"])
        self.assertEqual(receipt["triage"]["adjacent_title_signal"], triage["counts"]["ADJACENT_TITLE_SIGNAL"])
        self.assertEqual(receipt["triage"]["unclassified_title_insufficient"], triage["counts"]["UNCLASSIFIED_TITLE_INSUFFICIENT"])
        keys = [row["candidate_key"] for row in triage["candidates"]]
        self.assertEqual(len(keys), len(set(keys)))
        seed_status = {row["seed_id"]: row["status"] for row in triage["seeds"]}
        for seed in (
            "SEED-GODEL-1931",
            "SEED-TURING-1936",
            "SEED-CHURCH-1936",
            "SEED-ROSSER-1936",
            "SEED-DOMINANCES-2017",
            "SEED-AGDA-GODEL",
        ):
            self.assertEqual(seed_status[seed], "REQUIRES_MANUAL_PRIMARY_ENTRY")

    def test_denominator_distinguishes_freeze_from_corpus_completion(self) -> None:
        text = INDEX.read_text(encoding="utf-8") + "\n" + "\n".join(
            path.read_text(encoding="utf-8") for path in sorted(SHARDS.glob("*.md"))
        )
        for literal in (
            "DENOMINATOR_V1_FROZEN",
            "PRIMARY_CORPUS_REVIEW_IN_PROGRESS",
            "COMPREHENSIVE_COVERAGE_NOT_ACHIEVED",
            "1,745",
            "20 个需要手工一手入口",
            "LIT-CLASSICS-001",
            "R2-PROGRAMCODE-001",
            "title-only triage 不执行最终排除",
        ):
            self.assertIn(literal, text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
