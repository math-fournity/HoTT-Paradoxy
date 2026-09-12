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
    if core_manifest.get("core_document_sha256") != sha256(core_path):
        errors.append("CORE_HASH_MISMATCH")
    header = "\n".join(core_path.read_text(encoding="utf-8").splitlines()[:12])
    generation = core_manifest.get("generation")
    if not isinstance(generation, str) or f"generation：`{generation}`" not in header:
        errors.append("CORE_GENERATION_HEADER_MISMATCH")
    source_manifest = read_json(root, "sources/SOURCE_MANIFEST.json")
    explicit = {
        str(row.get("path")): row
        for row in source_manifest.get("explicit_files", [])
        if isinstance(row, dict)
    }
    user_input = "sources/prompts/治理三件套与历史融合要求-用户消息提取-20260912.md"
    if user_input not in explicit:
        errors.append("CORE_USER_INPUT_NOT_IN_SOURCE_MANIFEST")
    elif not (root / user_input).is_file() or explicit[user_input].get("sha256") != sha256(root / user_input):
        errors.append("CORE_USER_INPUT_SOURCE_HASH_MISMATCH")
    if user_input not in core_manifest.get("build_policy", {}).get("user_requirement_inputs", []):
        errors.append("CORE_USER_INPUT_NOT_IN_CORE_BUILD_POLICY")
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
    if fresh.get("status") != "PASS_WITH_SCOPE" or fresh.get("revision") != revision:
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
        "reconciliation_entries": reconciliation["counts"]["total_register_entries"],
        "merge_entries": merge["counts"]["union_files"],
        "fresh_receipt_revision": fresh["revision"],
        "model_context": "NOT_CERTIFIED_BY_TOOL",
        "mathematics": "NOT_CERTIFIED",
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
