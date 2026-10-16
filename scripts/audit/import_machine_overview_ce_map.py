#!/usr/bin/env python3
"""Freeze the machine-overview inputs needed by CE-MAP into the main repo.

The source worktree is read-only input and may be dirty.  The import therefore
copies a declared file set, checks it twice, and records every byte identity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE = Path("/Volumes/D/HoTT-machine-overview")
DEFAULT_DEST = PROJECT_ROOT / "audit/imports/machine-overview-ce-map-20260915"
SCHEMA = "machine-overview-ce-map-import/v1"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def git(source: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(source), *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return proc.stdout.rstrip("\n")


def revision_number(path: Path, prefix: str) -> int:
    stem = path.stem
    if not stem.startswith(prefix):
        return -1
    try:
        return int(stem[len(prefix) :])
    except ValueError:
        return -1


def selected_files(machine_root: Path) -> list[tuple[Path, str]]:
    selected: dict[Path, str] = {}

    def add(paths: Iterable[Path], role: str) -> None:
        for path in paths:
            if path.is_file():
                selected[path.resolve()] = role

    add([machine_root / "registry.json"], "registry")
    add([machine_root / "generated-index/index.json"], "generated_index")
    add((machine_root / "tasks").glob("*.json"), "task_spec")

    cases = machine_root / "cases"
    if cases.is_dir():
        for case_dir in sorted(p for p in cases.iterdir() if p.is_dir()):
            revisions = sorted(
                case_dir.glob("case-revision-*.json"),
                key=lambda p: revision_number(p, "case-revision-"),
            )
            if not revisions:
                continue
            latest = revisions[-1]
            add([latest], "latest_case_revision")
            number = revision_number(latest, "case-revision-")
            add([case_dir / f"target-freeze-{number}.json"], "target_freeze")

    evaluations = machine_root / "evaluations"
    if evaluations.is_dir():
        for eval_dir in sorted(p for p in evaluations.iterdir() if p.is_dir()):
            add(eval_dir.glob("*.json"), "evaluation_manifest")
            add([eval_dir / "REPORT.md", eval_dir / "README.md"], "evaluation_report")
            add(eval_dir.glob("runs/**/RUN.json"), "evaluation_run_manifest")

    add((machine_root / "runs").glob("*/RUN.json"), "coordinator_run_manifest")
    add((machine_root / "reviews").glob("*.json"), "correspondence_review")
    return sorted(selected.items(), key=lambda row: row[0].relative_to(machine_root).as_posix())


def document_identity(path: Path, machine_root: Path, role: str) -> dict[str, Any]:
    data = path.read_bytes()
    rel = path.relative_to(machine_root).as_posix()
    schema = None
    declared_id = None
    if path.suffix == ".json":
        parsed = json.loads(data)
        if isinstance(parsed, dict):
            schema = parsed.get("schema_version")
            # Leaf artifact identity must win over its parent task/case link.
            # RUN/review manifests commonly contain both identifiers.
            for key in (
                "run_id",
                "review_id",
                "evaluation_id",
                "audit_id",
                "task_id",
                "case_id",
                "freeze_id",
            ):
                value = parsed.get(key)
                if isinstance(value, str) and value:
                    declared_id = value
                    break
    return {
        "source_path": f"machine-overview/{rel}",
        "imported_path": f"source/{rel}",
        "role": role,
        "bytes": len(data),
        "sha256": sha256_bytes(data),
        "schema_version": schema,
        "declared_id": declared_id,
    }


def build_catalog(documents: list[dict[str, Any]]) -> dict[str, Any]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in documents:
        grouped[row["role"]].append(
            {
                "source_id": row["declared_id"],
                "path": row["imported_path"],
                "sha256": row["sha256"],
                "schema_version": row["schema_version"],
            }
        )
    evaluations: dict[str, list[str]] = defaultdict(list)
    for row in documents:
        parts = Path(row["source_path"]).parts
        if len(parts) >= 3 and parts[1] == "evaluations":
            evaluations[parts[2]].append(row["imported_path"])
    return {
        "schema_version": "machine-overview-ce-map-catalog/v1",
        "tasks": grouped.get("task_spec", []),
        "cases": grouped.get("latest_case_revision", []),
        "evaluations": [
            {"source_id": key, "paths": sorted(paths)}
            for key, paths in sorted(evaluations.items())
        ],
        "runs": sorted(
            grouped.get("coordinator_run_manifest", [])
            + grouped.get("evaluation_run_manifest", []),
            key=lambda row: row["path"],
        ),
        "reviews": grouped.get("correspondence_review", []),
    }


def validate_import(dest: Path) -> dict[str, Any]:
    manifest_path = dest / "IMPORT.json"
    catalog_path = dest / "CATALOG.json"
    if not manifest_path.is_file() or not catalog_path.is_file():
        raise ValueError("IMPORT_OR_CATALOG_MISSING")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != SCHEMA:
        raise ValueError("IMPORT_SCHEMA_MISMATCH")
    errors: list[str] = []
    for row in manifest.get("documents", []):
        path = dest / row["imported_path"]
        if not path.is_file():
            errors.append(f"MISSING:{row['imported_path']}")
            continue
        data = path.read_bytes()
        if len(data) != row["bytes"]:
            errors.append(f"SIZE:{row['imported_path']}")
        if sha256_bytes(data) != row["sha256"]:
            errors.append(f"HASH:{row['imported_path']}")
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    catalog_hash = sha256_bytes(canonical_json(catalog))
    if catalog_hash != manifest.get("catalog_sha256"):
        errors.append("CATALOG_HASH")
    counts = manifest.get("counts", {})
    if counts.get("documents") != len(manifest.get("documents", [])):
        errors.append("DOCUMENT_COUNT")
    if errors:
        raise ValueError(";".join(errors))
    return {
        "status": "VALID",
        "snapshot_id": manifest["snapshot_id"],
        "documents": counts["documents"],
        "tasks": counts["tasks"],
        "cases": counts["cases"],
        "evaluations": counts["evaluations"],
        "runs": counts["runs"],
        "reviews": counts["reviews"],
        "source_boundary": manifest["source_boundary"],
    }


def capture(source: Path, dest: Path) -> dict[str, Any]:
    machine_root = source / "machine-overview"
    if not machine_root.is_dir():
        raise ValueError(f"MACHINE_OVERVIEW_ROOT_MISSING:{machine_root}")
    files = selected_files(machine_root)
    before = [document_identity(path, machine_root, role) for path, role in files]
    source_status = git(source, "status", "--porcelain=v1", "--untracked-files=all")
    source_meta = {
        "root": str(source),
        "branch": git(source, "branch", "--show-current"),
        "head": git(source, "rev-parse", "HEAD"),
        "common_dir": git(source, "rev-parse", "--git-common-dir"),
        "status_sha256": sha256_bytes(source_status.encode()),
        "status_lines": len(source_status.splitlines()) if source_status else 0,
        "selected_files_are_tracked": sum(
            1
            for path, _ in files
            if subprocess.run(
                ["git", "-C", str(source), "ls-files", "--error-unmatch", str(path.relative_to(source))],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            ).returncode
            == 0
        ),
    }
    if dest.exists():
        raise ValueError(f"IMMUTABLE_DESTINATION_ALREADY_EXISTS:{dest}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="ce-map-import-", dir=dest.parent) as tmp_name:
        tmp = Path(tmp_name)
        for (path, _), row in zip(files, before, strict=True):
            out = tmp / row["imported_path"]
            out.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, out)
        after = [document_identity(path, machine_root, role) for path, role in files]
        if before != after:
            raise ValueError("SOURCE_CHANGED_DURING_CAPTURE")
        catalog = build_catalog(before)
        catalog_bytes = canonical_json(catalog)
        (tmp / "CATALOG.json").write_bytes(catalog_bytes)
        counts = {
            "documents": len(before),
            "bytes": sum(row["bytes"] for row in before),
            "tasks": len(catalog["tasks"]),
            "cases": len(catalog["cases"]),
            "evaluations": len(catalog["evaluations"]),
            "runs": len(catalog["runs"]),
            "reviews": len(catalog["reviews"]),
        }
        identity_material = canonical_json(
            {"documents": before, "source": source_meta, "counts": counts}
        )
        snapshot_id = sha256_bytes(identity_material)
        manifest = {
            "schema_version": SCHEMA,
            "snapshot_id": snapshot_id,
            "source_boundary": "FROZEN_BYTE_SNAPSHOT_OF_DIRTY_EXTERNAL_WORKTREE",
            "source": source_meta,
            "selection_policy": {
                "tasks": "all top-level task JSON",
                "cases": "latest numeric case revision and matching target freeze",
                "evaluations": "all top-level JSON/README/REPORT plus nested RUN.json",
                "runs": "all coordinator top-level RUN.json",
                "reviews": "all correspondence review JSON",
            },
            "counts": counts,
            "catalog_sha256": sha256_bytes(catalog_bytes),
            "documents": before,
            "interpretation_limit": (
                "Byte preservation proves only the imported source identity.  The source worktree "
                "was dirty; this import is not a Git release, a mathematical conclusion, or a claim "
                "that every source file outside the declared selection was captured."
            ),
        }
        (tmp / "IMPORT.json").write_bytes(canonical_json(manifest))
        (tmp / "README.md").write_text(
            "# machine-overview CE-MAP 冻结输入\n\n"
            f"快照 `{snapshot_id}` 从 `{source}` 只读取得。`IMPORT.json` 固定全部文件身份，"
            "`CATALOG.json` 提供 task/case/evaluation/run/review 分母；`source/` 保存被选中的原始字节。\n\n"
            "来源工作树在捕获时含未提交内容，因此本目录只能证明具名字节快照，不证明来源 Git 版本闭合。"
            "CE-MAP 必须保留 UNKNOWN/UNCLASSIFIED，不能从文件存在推导数学结论。\n",
            encoding="utf-8",
        )
        os.replace(tmp, dest)
    return validate_import(dest)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("capture", "validate"))
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--dest", type=Path, default=DEFAULT_DEST)
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "capture":
            if not args.write:
                raise ValueError("CAPTURE_REQUIRES_EXPLICIT_WRITE")
            result = capture(args.source.resolve(), args.dest.resolve())
        else:
            result = validate_import(args.dest.resolve())
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        return 0
    except (OSError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"status": "INVALID", "error": str(exc)}, ensure_ascii=False, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
