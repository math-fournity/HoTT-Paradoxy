#!/usr/bin/env python3
"""Freeze L5 adapters, sources and role declarations before task matrices."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import l5_consumer_audit
from machine_overview.profile import inspect_profile
from machine_overview.util import (
    MachineOverviewError,
    git_state,
    read_json,
    safe_relative,
    sha256_file,
    utc_now,
    write_bytes,
    write_json,
)

PROTOCOL_SCHEMA = "machine-overview-l5-freeze-protocol/v1"
FREEZE_SCHEMA = "machine-overview-l5-adapter-freeze/v1"


def root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True,
    )
    return Path(result.stdout.strip()).resolve()


def resolve(repo: Path, value: str) -> Path:
    path = (repo / safe_relative(value)).resolve()
    try:
        path.relative_to(repo.resolve())
    except ValueError as exc:
        raise MachineOverviewError(f"PATH_OUTSIDE_REPO:{value}") from exc
    return path


def pin(repo: Path, value: str) -> dict:
    path = resolve(repo, value)
    if not path.is_file() or path.is_symlink():
        raise MachineOverviewError(f"L5_FREEZE_SOURCE_INVALID:{value}")
    return {"path": value, "bytes": path.stat().st_size, "sha256": sha256_file(path)}


def freeze(repo: Path, protocol_path: Path, output_path: Path) -> dict:
    protocol = read_json(protocol_path)
    if protocol.get("schema_version") != PROTOCOL_SCHEMA:
        raise MachineOverviewError("L5_FREEZE_PROTOCOL_INVALID")
    if output_path.exists():
        raise MachineOverviewError("L5_FREEZE_ALREADY_EXISTS")
    existing = [value for value in protocol["future_paths"] if resolve(repo, value).exists()]
    if existing:
        raise MachineOverviewError(f"L5_FUTURE_INPUT_ALREADY_EXISTS:{existing[0]}")
    adapters = [pin(repo, value) for value in protocol["adapter_sources"]]
    scope_path = resolve(repo, protocol["scope"])
    scope = read_json(scope_path)
    artifacts = l5_consumer_audit.validate_scope(repo, scope)
    profile_path = resolve(repo, protocol["profile"])
    profile_report = inspect_profile(repo, profile_path, fast=False)
    if profile_report["status"] != "PROFILE_QUALIFIED":
        raise MachineOverviewError(f"L5_PROFILE_NOT_QUALIFIED:{profile_report['failures']}")

    evidence_dir = output_path.parent
    evidence_dir.mkdir(parents=True, exist_ok=True)
    runs = []
    for label, command in (
        ("selftest", [sys.executable, "machine-overview/mo.py", "selftest"]),
        ("validate", [sys.executable, "machine-overview/mo.py", "validate"]),
    ):
        completed = subprocess.run(command, cwd=repo, capture_output=True, timeout=360)
        stdout_path = evidence_dir / f"pre-{label}-stdout.txt"
        stderr_path = evidence_dir / f"pre-{label}-stderr.txt"
        write_bytes(stdout_path, completed.stdout)
        write_bytes(stderr_path, completed.stderr)
        if completed.returncode != 0:
            raise MachineOverviewError(f"L5_FREEZE_{label.upper()}_FAILED")
        runs.append({
            "label": label,
            "command_argv": command,
            "exit_code": completed.returncode,
            "stdout": pin(repo, stdout_path.relative_to(repo).as_posix()),
            "stderr": pin(repo, stderr_path.relative_to(repo).as_posix()),
        })
    result = {
        "schema_version": FREEZE_SCHEMA,
        "freeze_id": protocol["freeze_id"],
        "created_at_utc": utc_now(),
        "protocol": pin(repo, protocol_path.relative_to(repo).as_posix()),
        "adapter_sources": adapters,
        "profile": pin(repo, profile_path.relative_to(repo).as_posix()),
        "profile_status": profile_report["status"],
        "scope": pin(repo, scope_path.relative_to(repo).as_posix()),
        "source_artifact_count": len(artifacts),
        "future_paths": protocol["future_paths"],
        "future_inputs_absent_at_freeze": True,
        "task_roles_known_before_freeze": protocol["task_roles"],
        "pre_evolution_checks": runs,
        "git": git_state(repo),
        "interpretation": (
            "The same designer fixed four distinct capability roles and native adapters before writing "
            "their TaskSpecs/grammars or the semantic decision matrix. This guards task separation and "
            "source identity; it is not a blind novelty or model-effectiveness evaluation."
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
        print(json.dumps({
            "status": "L5_ADAPTERS_AND_SOURCES_FROZEN",
            "freeze_id": result["freeze_id"],
            "future_paths": len(result["future_paths"]),
            "source_artifacts": result["source_artifact_count"],
        }, ensure_ascii=False, indent=2))
    except (MachineOverviewError, OSError, ValueError, KeyError, subprocess.SubprocessError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

