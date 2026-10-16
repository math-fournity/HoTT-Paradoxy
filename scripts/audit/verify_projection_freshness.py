#!/usr/bin/env python3
"""Verify current projection/source freshness without mutating the repo."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(root: Path, rel: str) -> dict:
    value = json.loads((root / rel).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON_OBJECT_REQUIRED:{rel}")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.project_root.resolve()
    errors: list[str] = []
    state = read_json(root, ".codex/research/hott/STATE.json")
    revision = state.get("revision")
    if type(revision) is not int:
        errors.append("STATE_REVISION_INVALID")
    for rel, marker in (("方向追踪.md", "integrated-direction-portfolio:v1"), ("全景视野.md", "integrated-outcome-panorama:v1")):
        text = (root / rel).read_text(encoding="utf-8")
        if marker not in text:
            errors.append(f"MARKER_MISSING:{rel}")
        match = re.search(r"(?m)^source_state_revision: (\d+)\s*$", text)
        if not match or int(match.group(1)) != revision:
            errors.append(f"PROJECTION_REVISION_STALE:{rel}")
    core_manifest = read_json(root, "核心认知.manifest.json")
    core_path = root / "核心认知.md"
    if core_manifest.get("schema_version") != "core-cognition/v2":
        errors.append("CORE_SCHEMA_NOT_V2")
    if core_manifest.get("core_document_sha256") != sha256(core_path):
        errors.append("CORE_HASH_MISMATCH")
    header = "\n".join(core_path.read_text(encoding="utf-8").splitlines()[:12])
    generation = core_manifest.get("generation")
    if not isinstance(generation, str) or generation not in header:
        errors.append("CORE_GENERATION_HEADER_MISMATCH")
    required_historical_primary = [
        "sources/prompts/Codex-HoTT-2-用户消息提取-20260911.md",
        "sources/prompts/ChatGPT-HoTT-Main-用户消息提取-20260911.md",
        "sources/prompts/Gemini-AI对话录-用户消息提取-20260911.md",
    ]
    actual_primary = core_manifest.get("build_policy", {}).get("primary_inputs_only")
    if not isinstance(actual_primary, list) or actual_primary[:3] != required_historical_primary:
        errors.append("CORE_HISTORICAL_PRIMARY_INPUT_POLICY_MISMATCH")
    curation_path = root / str(core_manifest.get("curation_authority", ""))
    if not curation_path.is_file() or core_manifest.get("curation_sha256") != sha256(curation_path):
        errors.append("CORE_CURATION_STALE")
    current_core = state.get("current_core", {})
    transition_rel = current_core.get("transition")
    if not isinstance(transition_rel, str):
        errors.append("STATE_CORE_TRANSITION_MISSING")
        transition_rel = "audit/core-cognition-generation-4-transition-20260912.json"
    transition = read_json(root, transition_rel)
    if transition.get("mapping_count") != transition.get("previous", {}).get("unit_count") or transition.get("mapping_remainder") != 0:
        errors.append("CORE_GENERATION_TRANSITION_INCOMPLETE")
    if transition.get("current", {}).get("core_sha256") != sha256(core_path):
        errors.append("CORE_GENERATION_TRANSITION_STALE")
    merge = read_json(root, "audit/understanding-chapter-merge-manifest.json")
    for entry in merge.get("entries", []):
        for key in ("top_level", "nested_source"):
            value = entry.get(key)
            if value is not None:
                path = root / value["path"]
                if not path.is_file() or sha256(path) != value.get("sha256"):
                    errors.append(f"MERGE_SOURCE_STALE:{entry.get('relative_path')}:{key}")
    reconciliation = read_json(root, "audit/cross-source-reconciliation.json")
    for source_class, row in reconciliation.get("source_files", {}).items():
        path = root / row["path"]
        if not path.is_file() or sha256(path) != row.get("sha256"):
            errors.append(f"RECONCILIATION_SOURCE_STALE:{source_class}")
    if reconciliation.get("counts", {}).get("total_register_entries") != 22226:
        errors.append("RECONCILIATION_DENOMINATOR_UNEXPECTED")
    fresh = read_json(root, "audit/fresh-three-way-verification-20260912.json")
    if fresh.get("schema_version") != "fresh-three-way-verification/v2" or fresh.get("status") != "PASS_WITH_SCOPE" or fresh.get("revision") != revision:
        errors.append("FRESH_RECEIPT_STALE_OR_FAILED")
    if fresh.get("model_context") != "NOT_CERTIFIED_BY_TOOL":
        errors.append("MODEL_CONTEXT_BOUNDARY_MISSING")
    if errors:
        print(json.dumps({"status": "FAIL", "errors": errors}, ensure_ascii=False))
        return 1
    print(json.dumps({
        "status": "PASS_WITH_SCOPE",
        "state_revision": revision,
        "core_generation": generation,
        "core_units": core_manifest.get("counts", {}).get("core_units"),
        "reconciliation_entries": reconciliation["counts"]["total_register_entries"],
        "merge_entries": merge["counts"]["union_files"],
        "fresh_receipt_revision": fresh["revision"],
        "model_context": "NOT_CERTIFIED_BY_TOOL",
        "mathematics": "NOT_CERTIFIED",
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
