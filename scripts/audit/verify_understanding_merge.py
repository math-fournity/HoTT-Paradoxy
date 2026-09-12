#!/usr/bin/env python3
"""Verify the non-destructive understanding-directory merge receipt."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--manifest", type=Path, default=Path("audit/understanding-chapter-merge-manifest.json"))
    args = parser.parse_args()
    root = args.project_root.resolve()
    manifest = json.loads((root / args.manifest).read_text(encoding="utf-8"))
    errors: list[str] = []
    top = root / manifest["canonical_directory"]
    nested = root / manifest["historical_source_directory"]
    if not top.is_dir():
        fail(errors, f"MISSING_CANONICAL_DIRECTORY:{top}")
    if not nested.is_dir():
        fail(errors, f"MISSING_HISTORICAL_SOURCE_DIRECTORY:{nested}")
    entries = manifest.get("entries", [])
    names = sorted({p.name for p in top.iterdir()} | {p.name for p in nested.iterdir()}) if top.is_dir() and nested.is_dir() else []
    if sorted(e.get("relative_path") for e in entries) != names:
        fail(errors, "MANIFEST_UNION_MISMATCH")
    if manifest.get("counts", {}).get("union_files") != len(entries):
        fail(errors, "COUNT_UNION_MISMATCH")
    for entry in entries:
        name = entry["relative_path"]
        tp = root / "理解章节" / name
        np = root / "AI对话录/理解章节" / name
        expected_top = entry.get("top_level")
        expected_nested = entry.get("nested_source")
        if expected_top is not None:
            if not tp.is_file():
                fail(errors, f"TOP_FILE_MISSING:{name}")
            elif sha256(tp) != expected_top.get("sha256"):
                fail(errors, f"TOP_HASH_MISMATCH:{name}")
        if expected_nested is not None:
            if not np.is_file():
                fail(errors, f"NESTED_SOURCE_MISSING:{name}")
            elif sha256(np) != expected_nested.get("sha256"):
                fail(errors, f"NESTED_HASH_MISMATCH:{name}")
        if entry.get("comparison") == "NONTRIVIAL_REQUIRES_MANUAL_DECISION":
            fail(errors, f"UNRESOLVED_NONTRIVIAL:{name}")
        if entry.get("decision") == "KEEP_TOP_LEVEL_AS_CANONICAL" and expected_top is None:
            fail(errors, f"DECISION_WITHOUT_TOP:{name}")
        if entry.get("destructive_action") != "NOT_PERFORMED":
            fail(errors, f"DESTRUCTIVE_ACTION_NOT_PROVEN_SAFE:{name}")
    expected_counts = {
        "same_name_pairs": sum(
            1 for entry in entries if entry.get("top_level") is not None and entry.get("nested_source") is not None
        ),
        "identical_pairs": sum(1 for entry in entries if entry.get("comparison") == "IDENTICAL"),
        "different_pairs": sum(
            1
            for entry in entries
            if entry.get("top_level") is not None
            and entry.get("nested_source") is not None
            and entry.get("comparison") != "IDENTICAL"
        ),
        "nonidentical_union_entries": sum(1 for entry in entries if entry.get("comparison") != "IDENTICAL"),
        "top_level_unique": sum(1 for entry in entries if entry.get("nested_source") is None),
        "nested_unique": sum(1 for entry in entries if entry.get("top_level") is None),
    }
    for key, expected in expected_counts.items():
        if manifest.get("counts", {}).get(key) != expected:
            fail(errors, f"COUNT_{key.upper()}_MISMATCH:{manifest.get('counts', {}).get(key)}:{expected}")
    if errors:
        print(json.dumps({"status": "FAIL", "errors": errors}, ensure_ascii=False))
        return 1
    print(json.dumps({
        "status": "PASS",
        "union_files": len(entries),
        "same_name_pairs": manifest["counts"]["same_name_pairs"],
        "identical_pairs": manifest["counts"]["identical_pairs"],
        "different_pairs": manifest["counts"]["different_pairs"],
        "nonidentical_union_entries": manifest["counts"]["nonidentical_union_entries"],
        "canonical": manifest["canonical_directory"],
        "historical_source_retained": True,
        "semantic_claim": "NO_MATHEMATICAL_EQUIVALENCE_CLAIM",
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
