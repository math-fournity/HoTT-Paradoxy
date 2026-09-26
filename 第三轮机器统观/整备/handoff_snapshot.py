#!/usr/bin/env python3
"""Seal explicitly selected MO3 evidence bytes; no semantic or proof certification.

MANIFEST/SEAL are generated, immutable-by-convention receipts (mo3-handoff/v1),
not a live registry. New delivery => new directory. Never execute bundle content.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import tempfile


SCHEMA = "mo3-handoff/v1"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode()


def safe_relative(value: str) -> str:
    path = PurePosixPath(value)
    if (not value or "\\" in value or "\x00" in value or path.is_absolute()
            or any(p in {"", ".", ".."} for p in value.split("/"))
            or path.parts[0] in {".git", "private-audit"}):
        raise ValueError(f"UNSAFE_PATH:{value}")
    return value


def regular_file(root: Path, relative: str) -> Path:
    path = root / safe_relative(relative)
    at = root
    for component in PurePosixPath(relative).parts:
        at = at / component
        if at.is_symlink():
            raise ValueError(f"SYMLINK_NOT_ALLOWED:{relative}")
    if not path.is_file():
        raise ValueError(f"FILE_MISSING:{relative}")
    return path


def git_identity(root: Path) -> dict:
    def run(*args: str) -> str:
        return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()
    if Path(run("rev-parse", "--show-toplevel")).resolve() != root:
        raise ValueError("NOT_EXACT_GIT_ROOT")
    return {"root": str(root), "head": run("rev-parse", "HEAD"),
            "branch": run("branch", "--show-current")}


def seal(root: Path, paths_file: Path, output: Path) -> dict:
    root = root.resolve()
    output = output.absolute()
    if output.exists() or output.is_symlink():
        raise ValueError("OUTPUT_ALREADY_EXISTS")
    # The caller owns the output directory. Reject symlink parents as well.
    if any(parent.is_symlink() for parent in [output, *output.parents]):
        raise ValueError("OUTPUT_SYMLINK")
    names = [line for line in paths_file.read_text().splitlines()
             if line and not line.startswith("#")]
    if not names or len(names) != len(set(names)):
        raise ValueError("EMPTY_OR_DUPLICATE_PATH_LIST")
    names = sorted(safe_relative(n) for n in names)
    identity = git_identity(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    # Atomic directory publication on the same filesystem; temporary files are ours.
    with tempfile.TemporaryDirectory(prefix=".mo3-seal-", dir=output.parent) as temporary:
        stage = Path(temporary) / "bundle"
        (stage / "files").mkdir(parents=True)
        for name in names:
            source = regular_file(root, name)
            if output == source or output in source.parents:
                raise ValueError("OUTPUT_INCLUDED_IN_INPUT")
            data = source.read_bytes()
            target = stage / "files" / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            rows.append({"path": name, "bytes": len(data), "sha256": digest(data)})
        for row in rows:
            if digest(regular_file(root, row["path"]).read_bytes()) != row["sha256"]:
                raise ValueError(f"SOURCE_CHANGED_DURING_SEAL:{row['path']}")
        if git_identity(root) != identity:
            raise ValueError("GIT_IDENTITY_CHANGED_DURING_SEAL")
        manifest = {"schema_version": SCHEMA, "source_identity": identity,
                    "identity_scope": "exact listed working-file bytes; HEAD is provenance, not a clean-tree claim",
                    "files": rows}
        manifest_bytes = json_bytes(manifest)
        (stage / "MANIFEST.json").write_bytes(manifest_bytes)
        receipt = {"schema_version": SCHEMA, "status": "SEALED_BYTES_ONLY",
                   "manifest_sha256": digest(manifest_bytes), "file_count": len(rows),
                   "subject_commit": identity["head"]}
        (stage / "SEAL.json").write_bytes(json_bytes(receipt))
        if output.exists():
            raise ValueError("OUTPUT_ALREADY_EXISTS")
        os.rename(stage, output)
    return receipt


def verify(bundle: Path, expected_sha: str | None = None, live_root: Path | None = None) -> dict:
    if bundle.is_symlink():
        raise ValueError("BUNDLE_SYMLINK")
    bundle = bundle.absolute()
    if any(parent.is_symlink() for parent in bundle.parents):
        raise ValueError("BUNDLE_PARENT_SYMLINK")
    manifest_bytes = regular_file(bundle, "MANIFEST.json").read_bytes()
    receipt = json.loads(regular_file(bundle, "SEAL.json").read_bytes())
    identity = digest(manifest_bytes)
    if identity != receipt.get("manifest_sha256") or (expected_sha and identity != expected_sha):
        raise ValueError("MANIFEST_HASH_MISMATCH")
    manifest = json.loads(manifest_bytes)
    if (manifest.get("schema_version") != SCHEMA or receipt.get("schema_version") != SCHEMA
            or receipt.get("status") != "SEALED_BYTES_ONLY"):
        raise ValueError("SCHEMA_OR_SEAL_STATUS_MISMATCH")
    rows = manifest["files"]
    names = [safe_relative(row["path"]) for row in rows]
    if not names or len(names) != len(set(names)) or len(names) != receipt.get("file_count"):
        raise ValueError("INVALID_MEMBER_SET")
    if receipt.get("subject_commit") != manifest["source_identity"]["head"]:
        raise ValueError("SUBJECT_COMMIT_MISMATCH")
    for row in rows:
        data = regular_file(bundle, "files/" + row["path"]).read_bytes()
        if len(data) != row["bytes"] or digest(data) != row["sha256"]:
            raise ValueError(f"FILE_HASH_MISMATCH:{row['path']}")
        if live_root and digest(regular_file(live_root.resolve(), row["path"]).read_bytes()) != row["sha256"]:
            raise ValueError(f"LIVE_SOURCE_DRIFT:{row['path']}")
    actual = set()
    for path in bundle.rglob("*"):
        if path.is_symlink():
            raise ValueError("UNLISTED_SYMLINK")
        if path.is_file():
            actual.add(path.relative_to(bundle).as_posix())
    expected = {"MANIFEST.json", "SEAL.json", *("files/" + n for n in names)}
    if actual != expected:
        raise ValueError("UNLISTED_OR_MISSING_FILE")
    return {"status": "VERIFIED_BYTES_ONLY", "manifest_sha256": identity,
            "subject_commit": receipt["subject_commit"], "file_count": len(names),
            "live_checked": live_root is not None,
            "not_certified": ["semantic completeness", "mathematics", "author authenticity", "clean source tree"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    make = commands.add_parser("seal")
    make.add_argument("--root", type=Path, required=True)
    make.add_argument("--paths", type=Path, required=True)
    make.add_argument("--out", type=Path, required=True)
    check = commands.add_parser("verify")
    check.add_argument("--seal", type=Path, required=True)
    check.add_argument("--expected-sha")
    check.add_argument("--live-root", type=Path)
    args = parser.parse_args()
    try:
        result = (seal(args.root, args.paths, args.out) if args.action == "seal"
                  else verify(args.seal, args.expected_sha, args.live_root))
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc)}, ensure_ascii=False))
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
