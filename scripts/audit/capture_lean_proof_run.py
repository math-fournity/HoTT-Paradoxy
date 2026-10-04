#!/usr/bin/env python3
"""Run one Lean proof source and persist an immutable F-011 proof receipt."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[2]
RUN_ROOT = Path("HoTT/verification/runs")


class CaptureError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def safe_relative(value: str) -> Path:
    if not value or "\\" in value or "\x00" in value:
        raise CaptureError(f"UNSAFE_RELATIVE_PATH:{value}")
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise CaptureError(f"UNSAFE_RELATIVE_PATH:{value}")
    return Path(*path.parts)


def source_row(root: Path, relative: Path) -> dict[str, object]:
    path = root / relative
    if not path.is_file() or path.is_symlink():
        raise CaptureError(f"SOURCE_MISSING_OR_SYMLINK:{relative.as_posix()}")
    data = path.read_bytes()
    return {"path": relative.as_posix(), "bytes": len(data), "sha256": sha(data)}


def pinned_file_row(path: Path, label: str) -> dict[str, object]:
    if not path.is_file() or path.is_symlink():
        raise CaptureError(f"PINNED_FILE_MISSING_OR_SYMLINK:{label}:{path}")
    data = path.read_bytes()
    return {
        "label": label,
        "local_path": str(path),
        "bytes": len(data),
        "sha256": sha(data),
    }


def require_project_git_root(root: Path) -> None:
    """Accept both a primary checkout and a linked Git worktree.

    A primary checkout normally stores a `.git` directory, whereas a linked
    worktree stores a `.git` file pointing at the shared Git directory.  The
    receipt still has to be rooted at the checkout itself, so verify that Git
    resolves this exact directory as its top level rather than merely checking
    the on-disk shape of `.git`.
    """
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit("PROJECT_GIT_ROOT_REQUIRED")
    try:
        actual = Path(result.stdout.decode("utf-8", "strict").strip()).resolve()
    except (UnicodeError, OSError):
        raise SystemExit("PROJECT_GIT_ROOT_REQUIRED")
    if actual != root:
        raise SystemExit("PROJECT_GIT_ROOT_REQUIRED")


def exclusive_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--proof-id", required=True)
    parser.add_argument("--claim-id", action="append", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--manifest-file", action="append", default=[])
    parser.add_argument("--scope", required=True)
    parser.add_argument("--non-goal", action="append", default=[])
    parser.add_argument("--lean")
    parser.add_argument(
        "--toolchain",
        help=(
            "optional project-relative lean-proof-toolchain/v1 metadata; when "
            "present, capture verifies and pins lean.root/bin/lean as an "
            "external dependency"
        ),
    )
    args = parser.parse_args()

    root = args.project_root.resolve()
    require_project_git_root(root)
    if not args.run_id or "/" in args.run_id or not all(c.isalnum() or c in "._-" for c in args.run_id):
        raise SystemExit("RUN_ID_INVALID")
    run_relative = RUN_ROOT / args.run_id
    run_dir = root / run_relative
    if run_dir.exists():
        raise SystemExit("RUN_DIRECTORY_ALREADY_EXISTS")

    source = safe_relative(args.source)
    manifest_paths = [source]
    toolchain_relative: Path | None = None
    if args.toolchain:
        toolchain_relative = safe_relative(args.toolchain)
        if toolchain_relative not in manifest_paths:
            manifest_paths.append(toolchain_relative)
    for value in args.manifest_file:
        path = safe_relative(value)
        if path not in manifest_paths:
            manifest_paths.append(path)
    rows = [source_row(root, path) for path in manifest_paths]

    external_dependencies: list[dict[str, object]] = []
    toolchain = None
    if toolchain_relative is not None:
        try:
            toolchain = json.loads((root / toolchain_relative).read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            raise SystemExit("LEAN_TOOLCHAIN_INVALID") from exc
        lean_spec = toolchain.get("lean") if isinstance(toolchain, dict) else None
        lean_root = lean_spec.get("root") if isinstance(lean_spec, dict) else None
        if (
            not isinstance(toolchain, dict)
            or toolchain.get("schema_version") != "lean-proof-toolchain/v1"
            or not isinstance(lean_root, str)
            or not Path(lean_root).is_absolute()
        ):
            raise SystemExit("LEAN_TOOLCHAIN_INVALID")
        lean_path = (Path(lean_root) / "bin" / "lean").resolve()
        if args.lean and Path(args.lean).resolve() != lean_path:
            raise SystemExit("LEAN_TOOLCHAIN_BINARY_MISMATCH")
        binary = pinned_file_row(lean_path, "lean-binary")
        expected_bytes = lean_spec.get("binary_bytes")
        expected_sha = lean_spec.get("binary_sha256")
        if binary["bytes"] != expected_bytes or binary["sha256"] != expected_sha:
            raise SystemExit("LEAN_TOOLCHAIN_BINARY_HASH_MISMATCH")
        external_dependencies.append(binary)
    else:
        lean = args.lean or shutil.which("lean")
        if not lean:
            raise SystemExit("LEAN_EXECUTABLE_NOT_FOUND")
        lean_path = Path(lean).resolve()
    version = subprocess.run([str(lean_path), "--version"], cwd=root, capture_output=True, check=False)
    if version.returncode != 0:
        raise SystemExit("LEAN_VERSION_COMMAND_FAILED")
    version_line = version.stdout.decode("utf-8", "replace").strip()
    if toolchain is not None:
        expected_version = toolchain["lean"].get("version_line")
        if not isinstance(expected_version, str) or expected_version != version_line:
            raise SystemExit("LEAN_TOOLCHAIN_VERSION_MISMATCH")

    command = [str(lean_path), source.as_posix()]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(command, cwd=root, capture_output=True, check=False)
    completed = dt.datetime.now(dt.timezone.utc)

    source_manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": args.proof_id,
        "run_id": args.run_id,
        "files": rows,
        "external_dependencies": external_dependencies,
    }
    source_manifest_data = json_bytes(source_manifest)
    environment = "\n".join([
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={platform.python_version()}",
        f"lean_executable={lean_path}",
        "lean_version=" + version_line,
        "dependency_policy=Lean prelude only; exact source hashes and any requested pinned lean binary are in source-manifest.json",
        "secret_policy=no credentials or full environment dump retained",
        "",
    ]).encode("utf-8")
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": args.run_id,
        "proof_id": args.proof_id,
        "claim_ids": args.claim_id,
        "proof_assistant": "Lean",
        "proof_assistant_version": version.stdout.decode("utf-8", "replace").strip(),
        "command_argv": command,
        "cwd": str(root),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if result.returncode == 0 else "KERNEL_REJECTED",
        "scope": args.scope,
        "non_goals": args.non_goal,
        "stdout": {"path": "stdout.txt", "bytes": len(result.stdout), "sha256": sha(result.stdout)},
        "stderr": {"path": "stderr.txt", "bytes": len(result.stderr), "sha256": sha(result.stderr)},
        "environment": {"path": "environment.txt", "bytes": len(environment), "sha256": sha(environment)},
        "source_manifest": {"path": "source-manifest.json", "bytes": len(source_manifest_data), "sha256": sha(source_manifest_data)},
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }

    run_dir.mkdir(parents=True, exist_ok=False)
    try:
        exclusive_write(run_dir / "stdout.txt", result.stdout)
        exclusive_write(run_dir / "stderr.txt", result.stderr)
        exclusive_write(run_dir / "environment.txt", environment)
        exclusive_write(run_dir / "source-manifest.json", source_manifest_data)
        exclusive_write(run_dir / "RUN.json", json_bytes(run))
    except BaseException:
        print(f"PARTIAL_RUN_DIRECTORY_RETAINED:{run_relative.as_posix()}", file=sys.stderr)
        raise

    print(json.dumps({
        "status": run["status"],
        "run_path": run_relative.as_posix(),
        "exit_code": result.returncode,
        "stdout_bytes": len(result.stdout),
        "stderr_bytes": len(result.stderr),
        "source_files": len(rows),
        "index_status": run["index_status"],
    }, ensure_ascii=False))
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
