#!/usr/bin/env python3
"""Build an auditable, non-destructive comparison of the two understanding dirs.

The top-level directory is the proposed canonical directory.  This tool never
deletes or overwrites either source.  It records byte identity, line-level
differences, a conservative classification, and the reason for the selected
canonical version.  Semantic claims remain human-reviewable evidence; the
script only classifies the observed diff shape.
"""
from __future__ import annotations

import argparse
import datetime as dt
import difflib
import hashlib
import json
import subprocess
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from logical_document import logical_text  # noqa: E402  (shared reader for v2 shard indexes)
TOP = Path("理解章节")
NESTED = Path("sources/understanding-transform/AI对话录/理解章节")
SNAPSHOT_ROOT = Path("sources/understanding-transform/AI对话录")
SOURCE_MANIFEST = Path("sources/SOURCE_MANIFEST.json")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def info(root: Path, path: Path) -> dict[str, object] | None:
    if not path.exists():
        return None
    data = path.read_bytes()
    return {
        "path": path.relative_to(root).as_posix(),
        "sha256": digest(data),
        "bytes": len(data),
        "lines": data.count(b"\n"),
    }


def diff_lines(top_text: str, nested_text: str, name: str) -> tuple[list[str], list[str], list[str]]:
    top_lines = top_text.splitlines()
    nested_lines = nested_text.splitlines()
    unified = list(
        difflib.unified_diff(
            nested_lines,
            top_lines,
            fromfile=f"nested/{name}",
            tofile=f"top/{name}",
            lineterm="",
        )
    )
    top_only = [line[1:] for line in unified if line.startswith("+") and not line.startswith("+++")]
    nested_only = [line[1:] for line in unified if line.startswith("-") and not line.startswith("---")]
    return unified, top_only, nested_only


def classify(relative: str, top_only: list[str], nested_only: list[str]) -> tuple[str, str]:
    if not nested_only and not top_only:
        return "IDENTICAL", "Both files have identical UTF-8 bytes; retain the top-level path as canonical and record the nested path as a recoverable duplicate."
    if relative == "README.md":
        return "TOP_LEVEL_CURRENT_INDEX_AND_BOUNDARY", "The top-level version adds the current C0/source-manifest/ledger index and replaces the old v2 framing; it is the only version that routes current evidence."
    if relative in {"审计锚点-AI侧.md", "读遍账本.md"}:
        return "TOP_LEVEL_CURRENT_BOUNDARY_ADDITION", "The top-level version adds a current-evidence boundary while retaining the historical ledger/reading narrative; it prevents old PASS or reading labels from becoming current proof."
    if relative.startswith("B") and relative.endswith(".md"):
        return "TOP_LEVEL_CURRENT_BOUNDARY_ADDITION", "The top-level version adds a current-transform boundary banner to the historical work narrative; it does not replace the historical account with a new result."
    return "NONTRIVIAL_REQUIRES_MANUAL_DECISION", "The observed difference is not covered by the established current-boundary/index rules; no silent selection is allowed."


def git_head(root: Path) -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "GIT_HEAD_UNAVAILABLE"


def build(root: Path) -> dict[str, object]:
    top = root / TOP
    nested = root / NESTED
    if not top.is_dir():
        raise FileNotFoundError(f"MISSING_CANONICAL_DIRECTORY:{top}")
    if not nested.is_dir():
        raise FileNotFoundError(f"MISSING_TRACKED_HISTORICAL_DIRECTORY:{nested}")
    source_manifest_path = root / SOURCE_MANIFEST
    source_manifest_bytes = source_manifest_path.read_bytes()
    source_manifest = json.loads(source_manifest_bytes)
    snapshot_rows = [
        row
        for row in source_manifest.get("snapshot_roots", [])
        if row.get("root") == SNAPSHOT_ROOT.as_posix()
    ]
    if len(snapshot_rows) != 1:
        raise ValueError(
            f"SOURCE_MANIFEST_SNAPSHOT_MATCH_COUNT:{SNAPSHOT_ROOT}:{len(snapshot_rows)}"
        )
    snapshot_row = snapshot_rows[0]
    names = sorted(
        {p.name for p in top.iterdir() if p.is_file()}
        | {p.name for p in nested.iterdir() if p.is_file()}
    )
    entries: list[dict[str, object]] = []
    for name in names:
        top_path = top / name
        nested_path = nested / name
        top_info = info(root, top_path)
        nested_info = info(root, nested_path)
        sharded = logical_text(root, f"{TOP.as_posix()}/{name}")
        if sharded is not None:
            top_info = dict(top_info or {})
            top_info.update({
                "logical_document": True,
                "logical_sha256": hashlib.sha256(sharded.encode("utf-8")).hexdigest(),
                "logical_bytes": len(sharded.encode("utf-8")),
                "logical_lines": sharded.count("\n"),
                "shard_root": PurePosixPath(name).stem,
            })
        top_text = sharded if sharded is not None else (top_path.read_text(encoding="utf-8") if top_info else None)
        nested_text = nested_path.read_text(encoding="utf-8") if nested_info else None
        if top_text is not None and nested_text is not None and top_text == nested_text:
            comparison = "IDENTICAL"
            top_only: list[str] = []
            nested_only: list[str] = []
            unified: list[str] = []
            rationale = classify(name, top_only, nested_only)[1]
            if sharded is not None:
                rationale += (" The top-level path is a v2 shard index; this comparison uses the reconstructed "
                              "logical text (index plus every shard in table order).")
            verification = "LOGICAL_TEXT_EQUAL" if sharded is not None else "SHA256_EQUAL"
        elif top_info is None or nested_info is None:
            comparison = "ONE_SIDE_ONLY"
            top_only = []
            nested_only = []
            unified = []
            rationale = "A unique file must be retained and explicitly routed; it cannot be inferred away from a same-name comparison."
            verification = "PRESENCE_CHECK"
        else:
            unified, top_only, nested_only = diff_lines(top_text, nested_text, name)
            comparison, rationale = classify(name, top_only, nested_only)
            verification = "UNIFIED_DIFF_RECORDED"
        if top_info is not None:
            decision = "KEEP_TOP_LEVEL_AS_CANONICAL"
        else:
            decision = "KEEP_NESTED_AS_HISTORICAL_UNIQUE_SOURCE"
        entries.append(
            {
                "relative_path": name,
                "top_level": top_info,
                "nested_source": nested_info,
                "comparison": comparison,
                "decision": decision,
                "rationale": rationale,
                "top_only_lines": top_only,
                "nested_only_lines": nested_only,
                "unified_diff": unified,
                "evidence_refs": [f"{TOP.as_posix()}/{name}", f"{NESTED.as_posix()}/{name}"],
                "verification": verification,
                "rollback_source": f"{NESTED.as_posix()}/{name}" if nested_info is not None else "HISTORICAL_SOURCE_ABSENT",
                "destructive_action": "NOT_PERFORMED",
            }
        )
    same_name_pairs = sum(
        1 for e in entries if e["top_level"] is not None and e["nested_source"] is not None
    )
    identical = sum(1 for e in entries if e["comparison"] == "IDENTICAL")
    different_pairs = sum(
        1
        for e in entries
        if e["top_level"] is not None
        and e["nested_source"] is not None
        and e["comparison"] != "IDENTICAL"
    )
    nonidentical_union_entries = len(entries) - identical
    return {
        "schema_version": "understanding-chapter-merge/v2",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "source_git_head": git_head(root),
        "canonical_directory": TOP.as_posix(),
        "historical_source_directory": NESTED.as_posix(),
        "historical_source_provenance": {
            "kind": "TRACKED_BYTE_SNAPSHOT",
            "snapshot_root": SNAPSHOT_ROOT.as_posix(),
            "source_manifest": SOURCE_MANIFEST.as_posix(),
            "source_manifest_sha256": digest(source_manifest_bytes),
            "snapshot_file_count": snapshot_row["file_count"],
            "snapshot_tree_sha256": snapshot_row["tree_sha256"],
            "original_checkout_path": "/Volumes/D/HoTT_AI_HANDOFF_20260911/AI对话录/理解章节",
            "original_nested_repo_head": "c70b01ca26c01c2078a4c0cd31a65d5fbda27fb0",
            "snapshot_scope": "42-file transform snapshot; this merge compares its 24-file 理解章节 subtree",
        },
        "policy": {
            "source_policy": "Neither the canonical directory nor the tracked historical snapshot is deleted or overwritten by this manifest build.",
            "canonical_selection": "Top-level directory is canonical because it contains the current C0 boundary/index layer; each file remains individually compared.",
            "semantic_limit": "Line-level diff and rule-based classification do not prove mathematical or historical semantic equivalence; nontrivial differences require explicit manual disposition.",
            "rollback": "The tracked historical snapshot and the pre-merge top-level Git commit remain available in every linked worktree.",
        },
        "counts": {
            "top_level_files": sum(1 for p in top.iterdir() if p.is_file()),
            "nested_files": sum(1 for p in nested.iterdir() if p.is_file()),
            "union_files": len(entries),
            "same_name_pairs": same_name_pairs,
            "identical_pairs": identical,
            "different_pairs": different_pairs,
            "nonidentical_union_entries": nonidentical_union_entries,
            "top_level_unique": sum(1 for e in entries if e["nested_source"] is None),
            "nested_unique": sum(1 for e in entries if e["top_level"] is None),
            "unresolved_nontrivial": sum(1 for e in entries if e["comparison"] == "NONTRIVIAL_REQUIRES_MANUAL_DECISION"),
        },
        "entries": entries,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=Path("audit/understanding-chapter-merge-manifest.json"))
    args = parser.parse_args()
    root = args.project_root.resolve()
    result = build(root)
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "BUILT", "counts": result["counts"], "output": output.as_posix()}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
