#!/usr/bin/env python3
"""Freeze M3 breadth adapters before the four TaskSpec/grammar pairs exist."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from machine_overview.util import (
    MachineOverviewError,
    git_state,
    read_json,
    safe_relative,
    sha256_bytes,
    sha256_file,
    utc_now,
    write_bytes,
    write_json,
)

PROTOCOL_SCHEMA = "machine-overview-m3-breadth-protocol/v1"
FREEZE_SCHEMA = "machine-overview-m3-breadth-freeze/v1"


def root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True,
    )
    return Path(result.stdout.strip()).resolve()


def resolve(repo: Path, value: str) -> Path:
    path = (repo / safe_relative(value)).resolve()
    try:
        path.relative_to(repo)
    except ValueError as exc:
        raise MachineOverviewError(f"PATH_OUTSIDE_REPO:{value}") from exc
    return path


def pin(repo: Path, value: str) -> dict:
    path = resolve(repo, value)
    if not path.is_file() or path.is_symlink():
        raise MachineOverviewError(f"M3_ADAPTER_SOURCE_INVALID:{value}")
    return {"path": value, "bytes": path.stat().st_size, "sha256": sha256_file(path)}


def git_blob(repo: Path, commit: str, path: str) -> bytes:
    result = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=repo, capture_output=True)
    if result.returncode != 0:
        raise MachineOverviewError(f"M3_SEARCH_GIT_BLOB_UNAVAILABLE:{commit}:{path}")
    return result.stdout


def freeze(repo: Path, protocol_path: Path, output_path: Path) -> dict:
    protocol = read_json(protocol_path)
    if protocol.get("schema_version") != PROTOCOL_SCHEMA:
        raise MachineOverviewError("M3_PROTOCOL_SCHEMA_INVALID")
    if output_path.exists():
        raise MachineOverviewError("M3_FREEZE_ALREADY_EXISTS")
    existing = [value for value in protocol.get("future_paths", []) if resolve(repo, value).exists()]
    if existing:
        raise MachineOverviewError(f"M3_FUTURE_INPUT_ALREADY_EXISTS:{existing[0]}")
    baseline = protocol.get("search_baseline", {})
    historical = git_blob(repo, baseline.get("commit"), baseline.get("path"))
    if sha256_bytes(historical) != baseline.get("sha256"):
        raise MachineOverviewError("M3_SEARCH_DECLARED_HASH_MISMATCH")
    if sha256_file(resolve(repo, baseline["path"])) != baseline["sha256"]:
        raise MachineOverviewError("M3_SEARCH_LIVE_HASH_MISMATCH")
    adapters = [pin(repo, value) for value in protocol.get("adapter_sources", [])]

    command = [sys.executable, "machine-overview/mo.py", "selftest"]
    completed = subprocess.run(command, cwd=repo, capture_output=True, timeout=240)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    stdout_path = output_path.parent / "selftest-stdout.txt"
    stderr_path = output_path.parent / "selftest-stderr.txt"
    write_bytes(stdout_path, completed.stdout)
    write_bytes(stderr_path, completed.stderr)
    if completed.returncode != 0:
        raise MachineOverviewError("M3_FREEZE_SELFTEST_FAILED")
    result = {
        "schema_version": FREEZE_SCHEMA,
        "freeze_id": protocol["freeze_id"],
        "created_at_utc": utc_now(),
        "protocol": pin(repo, protocol_path.relative_to(repo).as_posix()),
        "search_baseline": {
            "commit": baseline["commit"],
            "path": baseline["path"],
            "sha256": baseline["sha256"],
            "live_match": True,
        },
        "adapter_sources": adapters,
        "future_paths": list(protocol.get("future_paths", [])),
        "future_inputs_absent_at_freeze": True,
        "task_roles_known_before_freeze": protocol.get("task_roles"),
        "scope": "M3_BREADTH_CONFIGURATION_FREEZE / SAME_DESIGNER / NOT_NOVELTY_OR_EFFECTIVENESS_EVAL",
        "selftest": {
            "command_argv": command,
            "exit_code": completed.returncode,
            "stdout": pin(repo, stdout_path.relative_to(repo).as_posix()),
            "stderr": pin(repo, stderr_path.relative_to(repo).as_posix()),
        },
        "git": git_state(repo),
        "interpretation": (
            "This freeze proves only that the four configuration files were absent after adapters and "
            "controls qualified. The same AI designed their roles; no discovery-independence claim follows."
        ),
    }
    write_json(output_path, result)
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--protocol", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args(argv)
    repo = root()
    try:
        result = freeze(repo, resolve(repo, args.protocol), resolve(repo, args.out))
        print(json.dumps({"status": "M3_BREADTH_ADAPTERS_FROZEN",
                          "freeze_id": result["freeze_id"],
                          "future_paths": len(result["future_paths"])}, indent=2))
    except (MachineOverviewError, OSError, ValueError, KeyError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
