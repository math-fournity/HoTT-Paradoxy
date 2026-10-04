#!/usr/bin/env python3
"""Restore a frozen workspace-publication manifest into a clean worktree.

The tool refuses a changed source row, a target outside the same repository, or
a target whose HEAD differs from the frozen source HEAD.  It copies only the
manifest-listed regular files and symlinks plus the manifest itself.  It does
not stage, commit, reset, clean, or push; those remain explicit Git actions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path


def git_text(cwd: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=cwd, text=True).strip()


def digest_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_relative(relative: str) -> Path:
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise RuntimeError(f"UNSAFE_MANIFEST_PATH:{relative}")
    return candidate


def validate_source_row(source_root: Path, row: dict[str, object]) -> Path:
    relative = validate_relative(str(row["path"]))
    path = source_root / relative
    info = os.lstat(path)
    kind = row["kind"]
    if kind == "regular":
        if not stat.S_ISREG(info.st_mode):
            raise RuntimeError(f"SOURCE_KIND_CHANGED:{relative}")
        if digest_file(path) != row["sha256"]:
            raise RuntimeError(f"SOURCE_HASH_CHANGED:{relative}")
    elif kind == "symlink":
        if not stat.S_ISLNK(info.st_mode):
            raise RuntimeError(f"SOURCE_KIND_CHANGED:{relative}")
        target = os.readlink(path)
        actual = hashlib.sha256(target.encode("utf-8", "surrogateescape")).hexdigest()
        if actual != row["sha256"]:
            raise RuntimeError(f"SOURCE_LINK_CHANGED:{relative}")
    else:
        raise RuntimeError(f"UNSUPPORTED_SOURCE_KIND:{relative}:{kind}")
    return path


def copy_row(source_root: Path, target_root: Path, row: dict[str, object]) -> None:
    source = validate_source_row(source_root, row)
    relative = validate_relative(str(row["path"]))
    target = target_root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() or target.is_symlink():
        target.unlink()
    if row["kind"] == "regular":
        shutil.copy2(source, target)
    else:
        os.symlink(os.readlink(source), target)


def verify_target_row(target_root: Path, row: dict[str, object]) -> None:
    relative = validate_relative(str(row["path"]))
    target = target_root / relative
    info = os.lstat(target)
    if row["kind"] == "regular":
        if not stat.S_ISREG(info.st_mode) or digest_file(target) != row["sha256"]:
            raise RuntimeError(f"TARGET_HASH_MISMATCH:{relative}")
    else:
        if not stat.S_ISLNK(info.st_mode):
            raise RuntimeError(f"TARGET_KIND_MISMATCH:{relative}")
        actual = hashlib.sha256(os.readlink(target).encode("utf-8", "surrogateescape")).hexdigest()
        if actual != row["sha256"]:
            raise RuntimeError(f"TARGET_LINK_MISMATCH:{relative}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, help="repo-relative frozen manifest path")
    parser.add_argument("--target", required=True, help="absolute clean worktree path")
    args = parser.parse_args()

    source_root = Path(git_text(Path.cwd(), "rev-parse", "--show-toplevel"))
    manifest_relative = validate_relative(args.manifest)
    manifest_path = source_root / manifest_relative
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    if data.get("schema_version") != "workspace-publication-snapshot/v1":
        raise SystemExit("MANIFEST_SCHEMA_UNSUPPORTED")
    if data.get("source_head") != git_text(source_root, "rev-parse", "HEAD"):
        raise SystemExit("SOURCE_HEAD_CHANGED_AFTER_FREEZE")

    target_root = Path(args.target).resolve()
    if not target_root.is_dir():
        raise SystemExit("TARGET_WORKTREE_MISSING")
    if git_text(target_root, "rev-parse", "--git-common-dir") != git_text(source_root, "rev-parse", "--git-common-dir"):
        raise SystemExit("TARGET_NOT_SAME_GIT_REPOSITORY")
    if git_text(target_root, "rev-parse", "HEAD") != data["source_head"]:
        raise SystemExit("TARGET_HEAD_NOT_FROZEN_SOURCE_HEAD")
    if git_text(target_root, "branch", "--show-current") != "dev-03":
        raise SystemExit("TARGET_BRANCH_NOT_DEV03")
    if subprocess.check_output(["git", "status", "--porcelain=v1"], cwd=target_root, text=True).strip():
        raise SystemExit("TARGET_WORKTREE_NOT_CLEAN")

    rows = [*data["tracked_modified"], *data["untracked_nonignored"]]
    for row in rows:
        copy_row(source_root, target_root, row)
    manifest_target = target_root / manifest_relative
    manifest_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(manifest_path, manifest_target)

    for row in rows:
        verify_target_row(target_root, row)
    if digest_file(manifest_target) != digest_file(manifest_path):
        raise RuntimeError("TARGET_MANIFEST_HASH_MISMATCH")

    print(
        json.dumps(
            {
                "status": "RESTORED_AND_HASH_VERIFIED",
                "source_head": data["source_head"],
                "target_branch": "dev-03",
                "tracked_modified": len(data["tracked_modified"]),
                "untracked_nonignored": len(data["untracked_nonignored"]),
                "manifest": str(manifest_relative),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        print(f"RESTORE_FAILED:{error}", file=sys.stderr)
        raise SystemExit(1)
