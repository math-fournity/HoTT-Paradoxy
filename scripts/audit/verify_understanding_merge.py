#!/usr/bin/env python3
"""Verify the non-destructive understanding-directory merge receipt."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from logical_document import logical_text  # noqa: E402  (shared reader for v2 shard indexes)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tracked_paths(root: Path) -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "-z"],
        cwd=root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(f"GIT_LS_FILES_FAILED:{result.stderr.strip()}")
    return {item for item in result.stdout.split("\0") if item}


def tree_rows(root: Path) -> tuple[list[dict[str, object]], str]:
    rows: list[dict[str, object]] = []
    for path in sorted(root.rglob("*")):
        if (
            not path.is_file()
            or path.is_symlink()
            or ".git" in path.parts
            or path.name == ".DS_Store"
            or "__pycache__" in path.parts
            or path.suffix == ".agdai"
        ):
            continue
        data = path.read_bytes()
        rows.append(
            {
                "path": path.relative_to(root).as_posix(),
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return rows, digest.hexdigest()


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
    if manifest.get("schema_version") != "understanding-chapter-merge/v2":
        fail(errors, f"MANIFEST_SCHEMA:{manifest.get('schema_version')}")
    try:
        tracked = tracked_paths(root)
    except RuntimeError as exc:
        fail(errors, str(exc))
        tracked = set()
    top = root / manifest["canonical_directory"]
    nested = root / manifest["historical_source_directory"]
    if not top.is_dir():
        fail(errors, f"MISSING_CANONICAL_DIRECTORY:{top}")
    if not nested.is_dir():
        fail(errors, f"MISSING_HISTORICAL_SOURCE_DIRECTORY:{nested}")
    provenance = manifest.get("historical_source_provenance", {})
    source_manifest_rel = provenance.get("source_manifest")
    snapshot_root_rel = provenance.get("snapshot_root")
    if not isinstance(source_manifest_rel, str) or not isinstance(snapshot_root_rel, str):
        fail(errors, "HISTORICAL_SOURCE_PROVENANCE_MISSING")
    else:
        source_manifest_path = root / source_manifest_rel
        snapshot_root = root / snapshot_root_rel
        if source_manifest_rel not in tracked:
            fail(errors, f"SOURCE_MANIFEST_NOT_TRACKED:{source_manifest_rel}")
        if not source_manifest_path.is_file():
            fail(errors, f"SOURCE_MANIFEST_MISSING:{source_manifest_rel}")
        else:
            source_manifest_bytes = source_manifest_path.read_bytes()
            if hashlib.sha256(source_manifest_bytes).hexdigest() != provenance.get(
                "source_manifest_sha256"
            ):
                fail(errors, "SOURCE_MANIFEST_HASH_MISMATCH")
            source_manifest = json.loads(source_manifest_bytes)
            source_rows = [
                row
                for row in source_manifest.get("snapshot_roots", [])
                if row.get("root") == snapshot_root_rel
            ]
            if len(source_rows) != 1:
                fail(errors, f"SOURCE_SNAPSHOT_MATCH_COUNT:{len(source_rows)}")
            elif snapshot_root.is_dir():
                actual_rows, actual_tree_hash = tree_rows(snapshot_root)
                expected = source_rows[0]
                if actual_rows != expected.get("files"):
                    fail(errors, "SOURCE_SNAPSHOT_FILE_ROWS_MISMATCH")
                if actual_tree_hash != expected.get("tree_sha256"):
                    fail(errors, "SOURCE_SNAPSHOT_TREE_HASH_MISMATCH")
                if expected.get("file_count") != provenance.get("snapshot_file_count"):
                    fail(errors, "SOURCE_SNAPSHOT_FILE_COUNT_PROVENANCE_MISMATCH")
                if expected.get("tree_sha256") != provenance.get("snapshot_tree_sha256"):
                    fail(errors, "SOURCE_SNAPSHOT_TREE_PROVENANCE_MISMATCH")
            else:
                fail(errors, f"SOURCE_SNAPSHOT_ROOT_MISSING:{snapshot_root_rel}")
    entries = manifest.get("entries", [])
    names = (
        sorted(
            {p.name for p in top.iterdir() if p.is_file()}
            | {p.name for p in nested.iterdir() if p.is_file()}
        )
        if top.is_dir() and nested.is_dir()
        else []
    )
    if sorted(e.get("relative_path") for e in entries) != names:
        fail(errors, "MANIFEST_UNION_MISMATCH")
    if manifest.get("counts", {}).get("union_files") != len(entries):
        fail(errors, "COUNT_UNION_MISMATCH")
    for entry in entries:
        name = entry["relative_path"]
        tp = top / name
        np = nested / name
        expected_top = entry.get("top_level")
        expected_nested = entry.get("nested_source")
        if expected_top is not None:
            top_rel = tp.relative_to(root).as_posix()
            if expected_top.get("path") != top_rel:
                fail(errors, f"TOP_PATH_IDENTITY_MISMATCH:{name}")
            if top_rel not in tracked:
                fail(errors, f"TOP_FILE_NOT_TRACKED:{name}")
            if not tp.is_file():
                fail(errors, f"TOP_FILE_MISSING:{name}")
            elif sha256(tp) != expected_top.get("sha256"):
                fail(errors, f"TOP_HASH_MISMATCH:{name}")
            if expected_top.get("logical_document"):
                try:
                    rebuilt = logical_text(root, f"理解章节/{name}")
                except (OSError, UnicodeError, ValueError) as exc:
                    fail(errors, f"TOP_LOGICAL_READ_FAILED:{name}:{exc}")
                    rebuilt = None
                if rebuilt is None:
                    fail(errors, f"TOP_LOGICAL_DOCUMENT_MISSING:{name}")
                elif hashlib.sha256(rebuilt.encode("utf-8")).hexdigest() != expected_top.get("logical_sha256"):
                    fail(errors, f"TOP_LOGICAL_HASH_MISMATCH:{name}")
        if expected_nested is not None:
            nested_rel = np.relative_to(root).as_posix()
            if expected_nested.get("path") != nested_rel:
                fail(errors, f"NESTED_PATH_IDENTITY_MISMATCH:{name}")
            if nested_rel not in tracked:
                fail(errors, f"NESTED_SOURCE_NOT_TRACKED:{name}")
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
        "historical_source_tracked": True,
        "historical_source_directory": manifest["historical_source_directory"],
        "semantic_claim": "NO_MATHEMATICAL_EQUIVALENCE_CLAIM",
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
