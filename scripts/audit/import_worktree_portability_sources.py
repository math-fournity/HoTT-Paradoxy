#!/usr/bin/env python3
"""Import and verify the source bytes needed by linked-worktree governance.

The historical source manifest already pins the ignored transform snapshot.
``import`` copies those exact bytes from the canonical checkout without
overwriting an existing destination.  The ALL-Markdown-root file used by a
current stable record is not copied: the importer verifies its byte-identical
tracked replacement and records the route.  ``verify`` then uses only tracked
project files and the import receipt, so it also works from a fresh linked
worktree that has none of the ignored source repositories.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE_ROOT = Path("/Volumes/D/HoTT_AI_HANDOFF_20260911")
SOURCE_MANIFEST = Path("sources/SOURCE_MANIFEST.json")
STATE = Path(".codex/research/hott/STATE.json")
TRANSFORM_ROOT = Path("sources/understanding-transform/AI对话录")
LEGACY_LOCAL_ARTIFACT = Path(
    "sources/local-gpt/ALL-Markdown-root/HoTT_is_GONE_COMPLETE.md"
)
TRACKED_LOCAL_ARTIFACT = Path("sources/local-gpt/HoTT_is_GONE_COMPLETE.md")
WORKSPACE_SNAPSHOT = Path("sources/webgpt/workspace-snapshot")
RECEIPT = Path("audit/worktree-portability-source-import-20260913.json")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_row(path: Path, relative: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {
        "path": relative.as_posix(),
        "bytes": len(data),
        "sha256": sha256(data),
    }


def git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )


def git_value(root: Path, *args: str) -> str:
    result = git(root, *args)
    if result.returncode != 0:
        raise RuntimeError(
            f"GIT_FAILED:{root}:{' '.join(args)}:{result.stderr.strip()}"
        )
    return result.stdout.strip()


def git_status(root: Path) -> str:
    result = git(root, "status", "--short")
    if result.returncode != 0:
        raise RuntimeError(f"GIT_STATUS_FAILED:{root}:{result.stderr.strip()}")
    return result.stdout.rstrip("\n")


def source_tree(manifest: dict, root_name: str) -> dict:
    rows = [
        row for row in manifest.get("snapshot_roots", []) if row.get("root") == root_name
    ]
    if len(rows) != 1:
        raise RuntimeError(f"SOURCE_TREE_MATCH_COUNT:{root_name}:{len(rows)}")
    return rows[0]


def verify_expected_file(path: Path, expected: dict, label: str) -> None:
    if not path.is_file():
        raise RuntimeError(f"MISSING:{label}:{path}")
    data = path.read_bytes()
    if len(data) != expected["bytes"]:
        raise RuntimeError(
            f"BYTE_COUNT_MISMATCH:{label}:{path}:{len(data)}:{expected['bytes']}"
        )
    digest = sha256(data)
    if digest != expected["sha256"]:
        raise RuntimeError(
            f"HASH_MISMATCH:{label}:{path}:{digest}:{expected['sha256']}"
        )


def ignored_tree_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and ".git" not in path.parts
        and path.name != ".DS_Store"
        and "__pycache__" not in path.parts
        and path.suffix != ".agdai"
    )


def workspace_refs(state: dict) -> list[tuple[str, str]]:
    refs: list[tuple[str, str]] = []
    for record_id, record in state.get("records", {}).items():
        for path in record.get("full_sources", []):
            if isinstance(path, str) and path.startswith("workspace/"):
                refs.append((record_id, path))
    return refs


def import_sources(source_root: Path) -> dict:
    manifest_path = ROOT / SOURCE_MANIFEST
    state_path = ROOT / STATE
    receipt_path = ROOT / RECEIPT
    destination_transform = ROOT / TRANSFORM_ROOT
    if receipt_path.exists():
        raise RuntimeError(f"RECEIPT_ALREADY_EXISTS:{receipt_path}")
    if destination_transform.exists():
        raise RuntimeError(f"DESTINATION_ALREADY_EXISTS:{destination_transform}")

    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    state = json.loads(state_path.read_text(encoding="utf-8"))
    transform = source_tree(manifest, TRANSFORM_ROOT.as_posix())
    local_tree = source_tree(manifest, LEGACY_LOCAL_ARTIFACT.parent.as_posix())
    source_transform = source_root / TRANSFORM_ROOT
    expected_transform = {
        row["path"]: row for row in transform.get("files", [])
    }
    observed_transform = {
        path.relative_to(source_transform).as_posix(): path
        for path in ignored_tree_files(source_transform)
    }
    if set(observed_transform) != set(expected_transform):
        missing = sorted(set(expected_transform) - set(observed_transform))
        extra = sorted(set(observed_transform) - set(expected_transform))
        raise RuntimeError(f"TRANSFORM_TREE_SET_MISMATCH:missing={missing}:extra={extra}")

    copied: list[dict[str, object]] = []
    for relative_text, expected in sorted(expected_transform.items()):
        source = observed_transform[relative_text]
        verify_expected_file(source, expected, "TRANSFORM_SOURCE")
        destination = destination_transform / relative_text
        if destination.exists():
            raise RuntimeError(f"DESTINATION_FILE_ALREADY_EXISTS:{destination}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        verify_expected_file(destination, expected, "TRANSFORM_DESTINATION")
        copied.append(file_row(destination, destination.relative_to(ROOT)))

    local_rows = [
        row
        for row in local_tree.get("files", [])
        if row.get("path") == LEGACY_LOCAL_ARTIFACT.name
    ]
    if len(local_rows) != 1:
        raise RuntimeError(f"LOCAL_ARTIFACT_ROW_COUNT:{len(local_rows)}")
    local_expected = local_rows[0]
    local_source = source_root / LEGACY_LOCAL_ARTIFACT
    verify_expected_file(local_source, local_expected, "LOCAL_SOURCE")
    tracked_local = ROOT / TRACKED_LOCAL_ARTIFACT
    if local_source.read_bytes() != tracked_local.read_bytes():
        raise RuntimeError("LOCAL_ARTIFACT_TRACKED_COPY_DIFFERS")
    local_mapping = {
        "legacy_path": LEGACY_LOCAL_ARTIFACT.as_posix(),
        "tracked_path": TRACKED_LOCAL_ARTIFACT.as_posix(),
        "bytes": local_expected["bytes"],
        "sha256": local_expected["sha256"],
        "relation": "BYTE_IDENTICAL_REPLACEMENT",
    }

    refs = workspace_refs(state)
    unique_workspace = sorted({path for _, path in refs})
    workspace_mappings: list[dict[str, object]] = []
    for original_text in unique_workspace:
        original = Path(original_text)
        source = source_root / original
        tracked = ROOT / WORKSPACE_SNAPSHOT / original.relative_to("workspace")
        if not source.is_file() or not tracked.is_file():
            raise RuntimeError(f"WORKSPACE_MAPPING_MISSING:{original}:{tracked}")
        source_bytes = source.read_bytes()
        tracked_bytes = tracked.read_bytes()
        if source_bytes != tracked_bytes:
            raise RuntimeError(f"WORKSPACE_MAPPING_DIFFERS:{original}:{tracked}")
        workspace_mappings.append(
            {
                "original_path": original.as_posix(),
                "tracked_path": tracked.relative_to(ROOT).as_posix(),
                "bytes": len(tracked_bytes),
                "sha256": sha256(tracked_bytes),
                "records": sorted(record_id for record_id, path in refs if path == original_text),
            }
        )

    dialogue_repo = source_root / "AI对话录"
    workspace_repo = source_root / "workspace"
    dialogue_status = git_status(dialogue_repo)
    workspace_status = git_status(workspace_repo)
    receipt = {
        "schema_version": "worktree-portability-source-import/v1",
        "imported_at_utc": datetime.now(timezone.utc).isoformat(),
        "destination_base_head": git_value(ROOT, "rev-parse", "HEAD"),
        "source_checkout": str(source_root),
        "source_checkout_head": git_value(source_root, "rev-parse", "HEAD"),
        "source_manifest": SOURCE_MANIFEST.as_posix(),
        "source_manifest_sha256": sha256(manifest_bytes),
        "copy_policy": "BYTE_FOR_BYTE_NO_OVERWRITE",
        "dialogues_source_repo": {
            "root": str(dialogue_repo),
            "head": git_value(dialogue_repo, "rev-parse", "HEAD"),
            "status_lines": dialogue_status.splitlines(),
            "clean": not bool(dialogue_status),
        },
        "workspace_source_repo": {
            "root": str(workspace_repo),
            "head": git_value(workspace_repo, "rev-parse", "HEAD"),
            "status_lines": workspace_status.splitlines(),
            "clean": not bool(workspace_status),
        },
        "copied_snapshot": {
            "root": TRANSFORM_ROOT.as_posix(),
            "source_tree_sha256": transform["tree_sha256"],
            "file_count": len(expected_transform),
            "files": copied,
        },
        "local_artifact_mapping": local_mapping,
        "workspace_full_source_references": len(refs),
        "workspace_unique_files": len(unique_workspace),
        "workspace_mappings": workspace_mappings,
        "status": "IMPORTED_AND_BYTE_VERIFIED",
    }
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt_path.write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return receipt


def tracked_set(root: Path) -> set[str]:
    result = git(root, "ls-files", "--cached", "-z")
    if result.returncode != 0:
        raise RuntimeError(f"GIT_LS_FILES_FAILED:{result.stderr.strip()}")
    return {item for item in result.stdout.split("\0") if item}


def verify_import(require_tracked: bool) -> dict[str, object]:
    receipt_path = ROOT / RECEIPT
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if receipt.get("schema_version") != "worktree-portability-source-import/v1":
        raise RuntimeError("RECEIPT_SCHEMA")
    manifest_bytes = (ROOT / SOURCE_MANIFEST).read_bytes()
    if sha256(manifest_bytes) != receipt.get("source_manifest_sha256"):
        raise RuntimeError("SOURCE_MANIFEST_DRIFT")
    rows = list(receipt["copied_snapshot"]["files"])
    for row in rows:
        verify_expected_file(ROOT / row["path"], row, "IMPORTED_FILE")
    for mapping in receipt["workspace_mappings"]:
        verify_expected_file(ROOT / mapping["tracked_path"], mapping, "WORKSPACE_TRACKED_COPY")
    local_mapping = receipt["local_artifact_mapping"]
    verify_expected_file(
        ROOT / local_mapping["tracked_path"], local_mapping, "LOCAL_TRACKED_REPLACEMENT"
    )
    if require_tracked:
        tracked = tracked_set(ROOT)
        required = {row["path"] for row in rows}
        required.update(mapping["tracked_path"] for mapping in receipt["workspace_mappings"])
        required.add(local_mapping["tracked_path"])
        required.add(RECEIPT.as_posix())
        missing = sorted(required - tracked)
        if missing:
            raise RuntimeError(f"IMPORTED_PATHS_NOT_TRACKED:{missing}")
    return {
        "status": "PASS",
        "copied_files": len(rows),
        "workspace_mappings": len(receipt["workspace_mappings"]),
        "workspace_references": receipt["workspace_full_source_references"],
        "require_tracked": require_tracked,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    importer = subparsers.add_parser("import")
    importer.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    verifier = subparsers.add_parser("verify")
    verifier.add_argument("--require-tracked", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "import":
            result = import_sources(args.source_root.resolve())
            summary = {
                "status": result["status"],
                "copied_snapshot_files": result["copied_snapshot"]["file_count"],
                "copied_local_artifacts": 0,
                "local_artifact_mappings": 1,
                "workspace_mappings": result["workspace_unique_files"],
                "workspace_references": result["workspace_full_source_references"],
                "receipt": str(ROOT / RECEIPT),
            }
        else:
            summary = verify_import(args.require_tracked)
    except (OSError, ValueError, KeyError, RuntimeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
