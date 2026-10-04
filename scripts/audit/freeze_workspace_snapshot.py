#!/usr/bin/env python3
"""Freeze a content-addressed inventory of the current Git worktree.

The inventory is intended for an auditable publication snapshot.  It records
all tracked modifications and all nonignored untracked files, while recording
but not including ignored runtime/staging artifacts.  It never reads or writes
outside the repository except for the Git executable itself.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def run_git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=root)


def text_git(root: Path, *args: str) -> str:
    return run_git(root, *args).decode("utf-8", "surrogateescape").strip()


def records_from_porcelain(raw: bytes) -> list[tuple[str, str]]:
    """Return `(status, path)` records from porcelain-v1 NUL output.

    Current snapshot lanes do not contain rename/copy entries, but their two
    pathname fields are retained when present so the manifest never silently
    loses a path if one appears between preflight and freeze.
    """
    parts = raw.split(b"\0")
    records: list[tuple[str, str]] = []
    index = 0
    while index < len(parts):
        entry = parts[index]
        index += 1
        if not entry:
            continue
        if len(entry) < 4 or entry[2:3] != b" ":
            raise RuntimeError(f"PORCELAIN_RECORD_INVALID:{entry!r}")
        status = entry[:2].decode("ascii")
        path = entry[3:].decode("utf-8", "surrogateescape")
        records.append((status, path))
        if "R" in status or "C" in status:
            if index >= len(parts) or not parts[index]:
                raise RuntimeError("PORCELAIN_RENAME_OR_COPY_PATH_MISSING")
            secondary = parts[index].decode("utf-8", "surrogateescape")
            index += 1
            records.append((f"{status}:paired", secondary))
    return records


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def file_row(root: Path, status_code: str, relative: str) -> dict[str, object]:
    path = root / relative
    info = os.lstat(path)
    row: dict[str, object] = {
        "path": relative,
        "status": status_code,
        "mode": oct(stat.S_IMODE(info.st_mode)),
    }
    if stat.S_ISREG(info.st_mode):
        row.update({"kind": "regular", "bytes": info.st_size, "sha256": sha256_file(path)})
    elif stat.S_ISLNK(info.st_mode):
        target = os.readlink(path)
        row.update(
            {
                "kind": "symlink",
                "target": target,
                "sha256": hashlib.sha256(target.encode("utf-8", "surrogateescape")).hexdigest(),
            }
        )
    else:
        row.update({"kind": "special"})
    return row


def ignored_reason(path: str) -> str:
    if "/__pycache__/" in f"/{path}" or path.endswith("/__pycache__/"):
        return "GENERATED_PYTHON_BYTECODE"
    if path.startswith("dev-notes/.dev-notes-skill-stage/"):
        return "PRIVATE_PRE_FINAL_ARCHIVE_STAGING"
    return "IGNORED_REQUIRES_EXPLICIT_REVIEW"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="repo-relative JSON output path")
    parser.add_argument("--overwrite", action="store_true", help="replace an earlier manifest for the same snapshot")
    args = parser.parse_args()

    root = Path(text_git(Path.cwd(), "rev-parse", "--show-toplevel"))
    output = (root / args.output).resolve()
    if root not in output.parents:
        raise SystemExit("OUTPUT_OUTSIDE_REPOSITORY")
    if output.exists() and not args.overwrite:
        raise SystemExit(f"REFUSE_OVERWRITE:{output}")

    dirty = records_from_porcelain(
        run_git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all")
    )
    ignored = records_from_porcelain(
        run_git(root, "status", "--porcelain=v1", "-z", "--ignored=matching")
    )

    output_relative = str(output.relative_to(root))
    dirty = [(code, path) for code, path in dirty if path != output_relative]
    tracked_rows = [file_row(root, code, path) for code, path in dirty if code != "??"]
    untracked_rows = [file_row(root, code, path) for code, path in dirty if code == "??"]
    ignored_rows = [
        {"path": path, "status": code, "exclusion_reason": ignored_reason(path)}
        for code, path in ignored
        if code == "!!"
    ]

    manifest = {
        "schema_version": "workspace-publication-snapshot/v1",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "repository_root": str(root),
        "source_branch": text_git(root, "branch", "--show-current"),
        "source_head": text_git(root, "rev-parse", "HEAD"),
        "tracked_modified": tracked_rows,
        "untracked_nonignored": untracked_rows,
        "ignored_excluded": ignored_rows,
        "inclusion_policy": {
            "tracked_modified": "INCLUDE",
            "untracked_nonignored": "INCLUDE",
            "ignored": "EXCLUDE_UNLESS_EXPLICITLY_REVIEWED",
            "manifest_output": "EXCLUDED_FROM_ITS_OWN_PREWRITE_INVENTORY_AND_ADDED_TO_PUBLICATION_COMMIT",
        },
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "FROZEN",
                "output": str(output.relative_to(root)),
                "tracked_modified": len(tracked_rows),
                "untracked_nonignored": len(untracked_rows),
                "ignored_excluded": len(ignored_rows),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"FREEZE_FAILED:{error}", file=sys.stderr)
        raise SystemExit(1)
