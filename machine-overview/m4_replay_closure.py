#!/usr/bin/env python3
"""Close M4-lite replay over snapshots before live coordinator evolution.

The original design freeze intentionally required its adapter sources to remain
byte-identical at their live paths.  This tool snapshots those already-checked
bytes and creates a v2 replay spec whose validation uses the snapshots.  The
symbolic search source remains pinned live and to its exact Git blob.
"""
from __future__ import annotations

import argparse
import copy
import json
import subprocess
import sys
from pathlib import Path

import m4_eval
from machine_overview.util import (
    MachineOverviewError,
    git_state,
    json_bytes,
    read_json,
    safe_relative,
    sha256_bytes,
    sha256_file,
    utc_now,
    write_bytes,
    write_json,
)

CLOSURE_SCHEMA = "machine-overview-m4-replay-closure/v2"
RUN_SCHEMA = "machine-overview-m4-replay-run/v2"


def repo_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True,
    )
    return Path(result.stdout.strip()).resolve()


def resolve(root: Path, value: str) -> Path:
    path = root / safe_relative(value)
    resolved = path.resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise MachineOverviewError(f"PATH_OUTSIDE_REPO:{value}") from exc
    return resolved


def relative(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise MachineOverviewError(f"PATH_OUTSIDE_REPO:{path}") from exc


def pin(root: Path, path: Path | str) -> dict:
    resolved = resolve(root, path) if isinstance(path, str) else path.resolve()
    if not resolved.is_file() or resolved.is_symlink():
        raise MachineOverviewError(f"PIN_FILE_INVALID:{resolved}")
    return {
        "path": relative(root, resolved),
        "bytes": resolved.stat().st_size,
        "sha256": sha256_file(resolved),
    }


def verify_pin(root: Path, row: dict, label: str) -> Path:
    if not isinstance(row, dict) or not isinstance(row.get("path"), str):
        raise MachineOverviewError(f"PIN_INVALID:{label}")
    path = resolve(root, row["path"])
    if (not path.is_file() or path.is_symlink() or path.stat().st_size != row.get("bytes")
            or sha256_file(path) != row.get("sha256")):
        raise MachineOverviewError(f"PIN_CHANGED:{label}:{row.get('path')}")
    return path


def git_blob(root: Path, commit: str, path: str) -> bytes:
    result = subprocess.run(["git", "show", f"{commit}:{path}"], cwd=root, capture_output=True)
    if result.returncode != 0:
        raise MachineOverviewError(f"GIT_BLOB_UNAVAILABLE:{commit}:{path}")
    return result.stdout


def create_closure(
    root: Path, *, freeze_path: Path, spec_path: Path, original_run_path: Path,
    output_dir: Path, replay_spec_path: Path,
) -> dict:
    if output_dir.exists() or replay_spec_path.exists():
        raise MachineOverviewError("M4_REPLAY_CLOSURE_OUTPUT_ALREADY_EXISTS")
    original_verify = m4_eval.verify_evaluation(root, original_run_path)
    freeze = read_json(freeze_path)
    if freeze.get("schema_version") != m4_eval.FREEZE_SCHEMA:
        raise MachineOverviewError("M4_ORIGINAL_FREEZE_SCHEMA_INVALID")

    output_dir.mkdir(parents=True, exist_ok=False)
    snapshots = []
    source_rows = list(freeze.get("adapter_sources", []))
    source_rows.append({
        "path": freeze["search_baseline"]["path"],
        "bytes": resolve(root, freeze["search_baseline"]["path"]).stat().st_size,
        "sha256": freeze["search_baseline"]["sha256"],
    })
    seen = set()
    for index, row in enumerate(source_rows):
        source = verify_pin(root, row, f"original_source.{index}")
        if row["path"] in seen:
            continue
        seen.add(row["path"])
        snapshot = output_dir / "snapshot" / safe_relative(row["path"])
        write_bytes(snapshot, source.read_bytes())
        snapshots.append({
            "original": dict(row),
            "snapshot": pin(root, snapshot),
        })

    baseline = freeze["search_baseline"]
    if sha256_bytes(git_blob(root, baseline["commit"], baseline["path"])) != baseline["sha256"]:
        raise MachineOverviewError("M4_SEARCH_GIT_BLOB_MISMATCH")
    closure_path = output_dir / "REPLAY-CLOSURE.json"
    closure = {
        "schema_version": CLOSURE_SCHEMA,
        "closure_id": "M4-LITE-L3-REPLAY-CLOSURE-V2",
        "created_at_utc": utc_now(),
        "purpose": "Preserve the accepted M4 adapter/search bytes before later M3 renderer evolution.",
        "original_design_freeze": pin(root, freeze_path),
        "original_spec": pin(root, spec_path),
        "original_run": pin(root, original_run_path),
        "original_run_verification": original_verify,
        "snapshots": snapshots,
        "search_baseline": dict(baseline),
        "live_dependency_after_closure": (
            "Only machine-overview/machine_overview/search.py must remain at the frozen hash because "
            "the v2 evaluator executes that pure function. Adapter validation uses snapshot bytes."
        ),
        "interpretation": (
            "This is evidence-preserving replay closure, not a second task-design freeze and not new "
            "effectiveness evidence. It inherits the original same-designer limitations."
        ),
        "git": git_state(root),
    }
    write_json(closure_path, closure)

    replay_spec = copy.deepcopy(read_json(spec_path))
    replay_spec["freeze"] = pin(root, closure_path)
    replay_spec["replay_closure_origin"] = {
        "original_spec": pin(root, spec_path),
        "meaning": "semantic task/mode content unchanged; only the freeze validator is redirected to snapshots",
    }
    write_json(replay_spec_path, replay_spec)
    return {"closure": closure_path, "spec": replay_spec_path, "snapshots": len(snapshots)}


def validate_closure(root: Path, closure_pin: dict) -> dict:
    closure_path = verify_pin(root, closure_pin, "replay_closure")
    closure = read_json(closure_path)
    if closure.get("schema_version") != CLOSURE_SCHEMA:
        raise MachineOverviewError("M4_REPLAY_CLOSURE_SCHEMA_INVALID")
    freeze_path = verify_pin(root, closure.get("original_design_freeze"), "original_design_freeze")
    freeze = read_json(freeze_path)
    expected = {row["path"]: row for row in freeze.get("adapter_sources", [])}
    expected[freeze["search_baseline"]["path"]] = {
        "path": freeze["search_baseline"]["path"],
        "sha256": freeze["search_baseline"]["sha256"],
    }
    seen = set()
    for index, item in enumerate(closure.get("snapshots", [])):
        original = item.get("original", {})
        snapshot = verify_pin(root, item.get("snapshot"), f"snapshot.{index}")
        if original.get("path") not in expected:
            raise MachineOverviewError(f"M4_REPLAY_SNAPSHOT_UNEXPECTED:{original.get('path')}")
        if original.get("sha256") != expected[original["path"]].get("sha256"):
            raise MachineOverviewError(f"M4_REPLAY_ORIGINAL_HASH_MISMATCH:{original['path']}")
        if sha256_file(snapshot) != original.get("sha256"):
            raise MachineOverviewError(f"M4_REPLAY_SNAPSHOT_HASH_MISMATCH:{original['path']}")
        seen.add(original["path"])
    if seen != set(expected):
        raise MachineOverviewError("M4_REPLAY_SNAPSHOT_ROSTER_MISMATCH")

    baseline = closure["search_baseline"]
    live_search = resolve(root, baseline["path"])
    if sha256_file(live_search) != baseline["sha256"]:
        raise MachineOverviewError("M4_REPLAY_LIVE_SEARCH_CHANGED")
    if sha256_bytes(git_blob(root, baseline["commit"], baseline["path"])) != baseline["sha256"]:
        raise MachineOverviewError("M4_REPLAY_SEARCH_GIT_BLOB_CHANGED")
    return closure


def compute_with_closure(root: Path, spec_path: Path) -> tuple[dict, dict]:
    original = m4_eval.validate_freeze
    m4_eval.validate_freeze = lambda current_root, closure_pin: validate_closure(current_root, closure_pin)
    try:
        return m4_eval.compute_evaluation(root, spec_path)
    finally:
        m4_eval.validate_freeze = original


def run_replay(root: Path, *, spec_path: Path, run_id: str, output_path: Path) -> dict:
    if output_path.exists():
        raise MachineOverviewError("M4_REPLAY_RUN_ALREADY_EXISTS")
    deterministic, timing = compute_with_closure(root, spec_path)
    payload = {
        "schema_version": RUN_SCHEMA,
        "run_id": run_id,
        "created_at_utc": utc_now(),
        "evaluator": pin(root, Path(__file__).resolve()),
        "base_evaluator": pin(root, "machine-overview/m4_eval.py"),
        "spec": pin(root, spec_path),
        "deterministic": deterministic,
        "deterministic_sha256": sha256_bytes(json_bytes(deterministic)),
        "descriptive_timing": timing,
        "git": git_state(root),
        "status": "M4_LITE_REPLAY_CLOSED_OVER_ADAPTER_SNAPSHOTS",
    }
    output_path.parent.mkdir(parents=True, exist_ok=False)
    write_json(output_path, payload)
    return payload


def verify_replay(root: Path, run_path: Path) -> dict:
    run = read_json(run_path)
    if run.get("schema_version") != RUN_SCHEMA:
        raise MachineOverviewError("M4_REPLAY_RUN_SCHEMA_INVALID")
    verify_pin(root, run.get("evaluator"), "run.evaluator")
    verify_pin(root, run.get("base_evaluator"), "run.base_evaluator")
    spec_path = verify_pin(root, run.get("spec"), "run.spec")
    deterministic, _ = compute_with_closure(root, spec_path)
    digest = sha256_bytes(json_bytes(deterministic))
    if deterministic != run.get("deterministic") or digest != run.get("deterministic_sha256"):
        raise MachineOverviewError("M4_REPLAY_V2_MISMATCH")
    return {
        "status": "M4_LITE_REPLAY_V2_VALID",
        "run_id": run["run_id"],
        "tasks": deterministic["task_count"],
        "deterministic_sha256": digest,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create")
    create.add_argument("--freeze", required=True)
    create.add_argument("--spec", required=True)
    create.add_argument("--original-run", required=True)
    create.add_argument("--out-dir", required=True)
    create.add_argument("--replay-spec", required=True)
    run = sub.add_parser("run")
    run.add_argument("--spec", required=True)
    run.add_argument("--run-id", required=True)
    run.add_argument("--out", required=True)
    verify = sub.add_parser("verify")
    verify.add_argument("--run", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = repo_root()
    try:
        if args.command == "create":
            result = create_closure(
                root,
                freeze_path=resolve(root, args.freeze),
                spec_path=resolve(root, args.spec),
                original_run_path=resolve(root, args.original_run),
                output_dir=resolve(root, args.out_dir),
                replay_spec_path=resolve(root, args.replay_spec),
            )
            print(json.dumps({"status": "M4_REPLAY_CLOSURE_CREATED",
                              "closure": relative(root, result["closure"]),
                              "spec": relative(root, result["spec"]),
                              "snapshots": result["snapshots"]}, indent=2))
        elif args.command == "run":
            result = run_replay(root, spec_path=resolve(root, args.spec), run_id=args.run_id,
                                output_path=resolve(root, args.out))
            print(json.dumps({"status": result["status"], "run_id": result["run_id"],
                              "deterministic_sha256": result["deterministic_sha256"]}, indent=2))
        else:
            print(json.dumps(verify_replay(root, resolve(root, args.run)), indent=2))
    except (MachineOverviewError, OSError, ValueError, KeyError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
