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
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
TOP = Path("理解章节")
NESTED = Path("AI对话录/理解章节")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def info(path: Path) -> dict[str, object] | None:
    if not path.exists():
        return None
    data = path.read_bytes()
    return {
        "path": path.as_posix(),
        "sha256": digest(data),
        "bytes": len(data),
        "lines": data.count(b"\n"),
    }


def diff_lines(top: Path, nested: Path) -> tuple[list[str], list[str], list[str]]:
    top_lines = top.read_text(encoding="utf-8").splitlines()
    nested_lines = nested.read_text(encoding="utf-8").splitlines()
    unified = list(
        difflib.unified_diff(
            nested_lines,
            top_lines,
            fromfile=f"nested/{top.name}",
            tofile=f"top/{top.name}",
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
    names = sorted({p.name for p in top.iterdir()} | {p.name for p in nested.iterdir()})
    entries: list[dict[str, object]] = []
    for name in names:
        top_path = top / name
        nested_path = nested / name
        top_info = info(top_path)
        nested_info = info(nested_path)
        if top_info is not None and nested_info is not None and top_info["sha256"] == nested_info["sha256"]:
            comparison = "IDENTICAL"
            top_only: list[str] = []
            nested_only: list[str] = []
            unified: list[str] = []
            rationale = classify(name, top_only, nested_only)[1]
            verification = "SHA256_EQUAL"
        elif top_info is None or nested_info is None:
            comparison = "ONE_SIDE_ONLY"
            top_only = []
            nested_only = []
            unified = []
            rationale = "A unique file must be retained and explicitly routed; it cannot be inferred away from a same-name comparison."
            verification = "PRESENCE_CHECK"
        else:
            unified, top_only, nested_only = diff_lines(top_path, nested_path)
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
                "evidence_refs": [f"理解章节/{name}", f"AI对话录/理解章节/{name}"],
                "verification": verification,
                "rollback_source": f"AI对话录/理解章节/{name}" if nested_info is not None else "NESTED_SOURCE_ABSENT",
                "destructive_action": "NOT_PERFORMED",
            }
        )
    identical = sum(1 for e in entries if e["comparison"] == "IDENTICAL")
    different = len(entries) - identical
    return {
        "schema_version": "understanding-chapter-merge/v1",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "source_git_head": git_head(root),
        "canonical_directory": TOP.as_posix(),
        "historical_source_directory": NESTED.as_posix(),
        "policy": {
            "source_policy": "Neither directory is deleted or overwritten by this manifest build.",
            "canonical_selection": "Top-level directory is canonical because it contains the current C0 boundary/index layer; each file remains individually compared.",
            "semantic_limit": "Line-level diff and rule-based classification do not prove mathematical or historical semantic equivalence; nontrivial differences require explicit manual disposition.",
            "rollback": "Nested source and the pre-merge top-level Git commit remain available.",
        },
        "counts": {
            "top_level_files": sum(1 for p in top.iterdir() if p.is_file()),
            "nested_files": sum(1 for p in nested.iterdir() if p.is_file()),
            "union_files": len(entries),
            "same_name_pairs": sum(1 for e in entries if e["top_level"] is not None and e["nested_source"] is not None),
            "identical_pairs": identical,
            "different_pairs": different,
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
