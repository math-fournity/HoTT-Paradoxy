#!/usr/bin/env python3
"""Bounded M4-lite evaluation over a frozen symbolic search engine.

This evaluator is deliberately small.  It compares declared rule selections
under one budget, binds every task to its canonical coordinator search/native
run, and can replay its deterministic semantic payload.  Timing is retained as
descriptive evidence and is excluded from the replay digest.
"""
from __future__ import annotations

import argparse
import copy
import json
import subprocess
import sys
import time
from pathlib import Path

from machine_overview.search import compute_search_semantics
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

PROTOCOL_SCHEMA = "machine-overview-m4-lite-protocol/v1"
FREEZE_SCHEMA = "machine-overview-m4-lite-freeze/v1"
SPEC_SCHEMA = "machine-overview-m4-lite-spec/v1"
RUN_SCHEMA = "machine-overview-m4-lite-run/v1"
ACCEPTED_NATIVE = {
    "NATIVE_CHECKED_CALIBRATION_INSTANCE",
    "NATIVE_CHECKED_EXPLORATION_CANDIDATE",
}


def repo_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], check=True, capture_output=True, text=True,
    )
    return Path(result.stdout.strip()).resolve()


def relative(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise MachineOverviewError(f"PATH_OUTSIDE_REPO:{path}") from exc


def resolve(root: Path, value: str) -> Path:
    path = root / safe_relative(value)
    resolved = path.resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise MachineOverviewError(f"PATH_OUTSIDE_REPO:{value}") from exc
    return resolved


def file_pin(root: Path, value: str) -> dict:
    path = resolve(root, value)
    if not path.is_file() or path.is_symlink():
        raise MachineOverviewError(f"PINNED_FILE_INVALID:{value}")
    return {"path": value, "bytes": path.stat().st_size, "sha256": sha256_file(path)}


def verify_pin(root: Path, pin: dict, label: str) -> Path:
    if not isinstance(pin, dict) or not isinstance(pin.get("path"), str):
        raise MachineOverviewError(f"PIN_INVALID:{label}")
    path = resolve(root, pin["path"])
    if not path.is_file() or path.is_symlink():
        raise MachineOverviewError(f"PIN_MISSING:{label}:{pin['path']}")
    if path.stat().st_size != pin.get("bytes") or sha256_file(path) != pin.get("sha256"):
        raise MachineOverviewError(f"PIN_CHANGED:{label}:{pin['path']}")
    return path


def git_blob(root: Path, commit: str, path: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{commit}:{path}"], cwd=root, capture_output=True,
    )
    if result.returncode != 0:
        raise MachineOverviewError(f"GIT_BLOB_UNAVAILABLE:{commit}:{path}")
    return result.stdout


def freeze_design(root: Path, protocol_path: Path, output_path: Path) -> dict:
    protocol = read_json(protocol_path)
    if protocol.get("schema_version") != PROTOCOL_SCHEMA:
        raise MachineOverviewError("M4_PROTOCOL_SCHEMA_INVALID")
    for value in protocol.get("future_paths", []):
        if resolve(root, value).exists():
            raise MachineOverviewError(f"M4_FUTURE_INPUT_ALREADY_EXISTS:{value}")

    baseline = protocol.get("search_baseline", {})
    commit = baseline.get("commit")
    source_path = baseline.get("path")
    if not isinstance(commit, str) or not isinstance(source_path, str):
        raise MachineOverviewError("M4_SEARCH_BASELINE_INVALID")
    historical = git_blob(root, commit, source_path)
    live = resolve(root, source_path)
    historical_sha = sha256_bytes(historical)
    if historical_sha != baseline.get("sha256"):
        raise MachineOverviewError("M4_SEARCH_BASELINE_DECLARED_HASH_MISMATCH")
    if not live.is_file() or sha256_file(live) != historical_sha:
        raise MachineOverviewError("M4_SEARCH_ENGINE_NOT_AT_FROZEN_BASELINE")

    adapter_sources = [file_pin(root, value) for value in protocol.get("adapter_sources", [])]
    if output_path.exists():
        raise MachineOverviewError(f"M4_FREEZE_ALREADY_EXISTS:{relative(root, output_path)}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    command = [sys.executable, "machine-overview/mo.py", "selftest"]
    completed = subprocess.run(command, cwd=root, capture_output=True, timeout=180)
    stdout_path = output_path.parent / "selftest-stdout.txt"
    stderr_path = output_path.parent / "selftest-stderr.txt"
    write_bytes(stdout_path, completed.stdout)
    write_bytes(stderr_path, completed.stderr)
    if completed.returncode != 0:
        raise MachineOverviewError("M4_FREEZE_SELFTEST_FAILED")

    freeze = {
        "schema_version": FREEZE_SCHEMA,
        "freeze_id": protocol["freeze_id"],
        "created_at_utc": utc_now(),
        "scope": "SEARCH_ENGINE_BYTE_FROZEN / ADAPTERS_FROZEN / DESIGNER_VISIBLE / NOT_BLIND_MODEL_EVAL",
        "protocol": file_pin(root, relative(root, protocol_path)),
        "search_baseline": {
            "commit": commit,
            "path": source_path,
            "sha256": historical_sha,
            "live_match": True,
        },
        "adapter_sources": adapter_sources,
        "future_paths": list(protocol.get("future_paths", [])),
        "future_inputs_absent_at_freeze": True,
        "designer_visibility": protocol.get("designer_visibility"),
        "git": git_state(root),
        "selftest": {
            "command_argv": command,
            "exit_code": completed.returncode,
            "stdout": file_pin(root, relative(root, stdout_path)),
            "stderr": file_pin(root, relative(root, stderr_path)),
        },
        "interpretation_limit": (
            "This freeze tests fixed-engine behavior on later materialized configurations. "
            "The same AI designed the task roles and adapters, so it does not establish novelty, "
            "training-data independence, or general search effectiveness."
        ),
    }
    write_json(output_path, freeze)
    return freeze


def validate_freeze(root: Path, pin: dict) -> dict:
    path = verify_pin(root, pin, "freeze")
    freeze = read_json(path)
    if freeze.get("schema_version") != FREEZE_SCHEMA:
        raise MachineOverviewError("M4_FREEZE_SCHEMA_INVALID")
    verify_pin(root, freeze.get("protocol"), "freeze.protocol")
    for index, source in enumerate(freeze.get("adapter_sources", [])):
        verify_pin(root, source, f"freeze.adapter.{index}")
    baseline = freeze.get("search_baseline", {})
    historical = git_blob(root, baseline.get("commit"), baseline.get("path"))
    if sha256_bytes(historical) != baseline.get("sha256"):
        raise MachineOverviewError("M4_FROZEN_GIT_BLOB_CHANGED")
    live = resolve(root, baseline["path"])
    if sha256_file(live) != baseline["sha256"]:
        raise MachineOverviewError("M4_FROZEN_SEARCH_SOURCE_CHANGED")
    return freeze


def filtered_grammar(grammar: dict, rule_ids: list[str]) -> dict:
    declared = {rule["id"] for rule in grammar.get("rules", [])}
    selected = list(rule_ids)
    if len(selected) != len(set(selected)) or not set(selected).issubset(declared):
        raise MachineOverviewError("M4_MODE_RULE_SELECTION_INVALID")
    result = copy.deepcopy(grammar)
    result["rules"] = [rule for rule in grammar["rules"] if rule["id"] in set(selected)]
    return result


def semantic_stage(grammar: dict, rule_ids: list[str], budget: dict, seed: int) -> tuple[dict, int]:
    selected = filtered_grammar(grammar, rule_ids)
    started = time.monotonic_ns()
    result = compute_search_semantics(selected, budget, seed)
    elapsed = time.monotonic_ns() - started
    first = result["witnesses"][0] if result["witnesses"] else None
    summary = {
        "selected_rules": list(rule_ids),
        "goal_terms_found": result["statistics"]["goal_terms_found"],
        "rule_application_checks": result["statistics"]["rule_application_checks"],
        "complete_within_selected_grammar": result["statistics"]["complete_within_declared_grammar"],
        "truncated": result["statistics"]["truncated"],
        "first_witness": first,
        "order_independent_set_equal": result["order_independence_check"]["order_independent_set_equal"],
        "ablation_removes_goal": result["controls"]["negative"]["expectation_met"],
    }
    return summary, elapsed


def native_classification(verify_run: dict, witness: dict | None) -> dict:
    if witness is None:
        return {"binding": "NO_CANDIDATE", "status": None, "accepted": False}
    if witness.get("ast_sha256") != verify_run.get("candidate_ast_sha256"):
        return {
            "binding": "CANDIDATE_NOT_THE_CANONICAL_NATIVE_WITNESS",
            "status": None,
            "accepted": False,
        }
    return {
        "binding": "BOUND_TO_CANONICAL_NATIVE_RUN",
        "status": verify_run.get("status"),
        "accepted": verify_run.get("status") in ACCEPTED_NATIVE,
    }


def evaluate_mode(task: dict, grammar: dict, verify_run: dict, mode: dict, budget: dict, seed: int) -> dict:
    all_rules = [rule["id"] for rule in grammar["rules"]]
    strategy = mode["strategy"]
    if strategy == "full_typed_enumeration":
        initial_rules = all_rules
    else:
        initial_rules = task["mode_rules"][mode["mode_id"]]["initial_rules"]
    first_stage, first_elapsed = semantic_stage(grammar, initial_rules, budget, seed)
    stages = [{"stage": "initial", **first_stage}]
    elapsed = first_elapsed
    final_stage = first_stage
    feedback_applied = False

    initial_native = native_classification(verify_run, first_stage["first_witness"])
    if strategy == "native_feedback" and first_stage["first_witness"] is not None and not initial_native["accepted"]:
        remove = task["mode_rules"][mode["mode_id"]].get("remove_after_native_rejection", [])
        remaining_rules = [rule for rule in initial_rules if rule not in set(remove)]
        spent = int(first_stage["rule_application_checks"])
        remaining_budget = dict(budget)
        remaining_budget["max_checks"] = max(0, int(budget["max_checks"]) - spent)
        second_stage, second_elapsed = semantic_stage(grammar, remaining_rules, remaining_budget, seed)
        stages.append({
            "stage": "after_native_rejection",
            "removed_rules": list(remove),
            **second_stage,
        })
        elapsed += second_elapsed
        final_stage = second_stage
        feedback_applied = True

    final_native = native_classification(verify_run, final_stage["first_witness"])
    expected = task["expected_native_outcome"]
    if expected == "ACCEPT":
        expectation_met = final_native["accepted"]
    elif expected == "REJECT":
        expectation_met = (
            (final_stage["first_witness"] is None and feedback_applied)
            or (final_native["binding"] == "BOUND_TO_CANONICAL_NATIVE_RUN" and not final_native["accepted"])
        )
    else:
        raise MachineOverviewError(f"M4_EXPECTED_NATIVE_OUTCOME_INVALID:{expected}")
    return {
        "mode_id": mode["mode_id"],
        "strategy": strategy,
        "budget": dict(budget),
        "stages": stages,
        "total_rule_application_checks": sum(int(stage["rule_application_checks"]) for stage in stages),
        "elapsed_nanoseconds_descriptive": elapsed,
        "feedback_applied": feedback_applied,
        "initial_native": initial_native,
        "final_native": final_native,
        "expected_native_outcome": expected,
        "expectation_met": expectation_met,
        "false_promotion": bool(expected == "REJECT" and final_native["accepted"]),
    }


def deterministic_mode(mode: dict) -> dict:
    result = copy.deepcopy(mode)
    result.pop("elapsed_nanoseconds_descriptive", None)
    return result


def compute_evaluation(root: Path, spec_path: Path) -> tuple[dict, dict]:
    spec = read_json(spec_path)
    if spec.get("schema_version") != SPEC_SCHEMA:
        raise MachineOverviewError("M4_SPEC_SCHEMA_INVALID")
    validate_freeze(root, spec.get("freeze"))
    budget = spec.get("budget")
    if not isinstance(budget, dict) or any(int(budget.get(key, -1)) < 0 for key in (
            "max_witnesses", "max_checks", "max_contexts")):
        raise MachineOverviewError("M4_BUDGET_INVALID")
    seed = int(spec.get("seed", 20260913))
    modes = spec.get("modes", [])
    mode_ids = [mode.get("mode_id") for mode in modes]
    if len(mode_ids) != len(set(mode_ids)) or not mode_ids:
        raise MachineOverviewError("M4_MODES_INVALID")

    results = []
    timings = []
    for task in spec.get("tasks", []):
        grammar_path = verify_pin(root, task.get("grammar"), f"task.{task.get('task_id')}.grammar")
        case_path = verify_pin(root, task.get("case"), f"task.{task.get('task_id')}.case")
        search_path = verify_pin(root, task.get("search_run"), f"task.{task.get('task_id')}.search")
        verify_path = verify_pin(root, task.get("verify_run"), f"task.{task.get('task_id')}.verify")
        grammar = read_json(grammar_path)
        case = read_json(case_path)
        search_run = read_json(search_path)
        verify_run = read_json(verify_path)
        if case.get("case_id") != task.get("task_id"):
            raise MachineOverviewError(f"M4_CASE_TASK_ID_MISMATCH:{task.get('task_id')}")
        if search_run.get("case_id") != case.get("case_id") or verify_run.get("case_id") != case.get("case_id"):
            raise MachineOverviewError(f"M4_RUN_CASE_BINDING_MISMATCH:{task.get('task_id')}")
        task_modes = []
        for mode in modes:
            result = evaluate_mode(task, grammar, verify_run, mode, budget, seed)
            timings.append({
                "task_id": task["task_id"],
                "mode_id": mode["mode_id"],
                "elapsed_nanoseconds": result["elapsed_nanoseconds_descriptive"],
            })
            task_modes.append(deterministic_mode(result))

        full = next(item for item in task_modes if item["mode_id"] == "typed_enumeration")
        canonical_first = search_run.get("witnesses", [None])[0] if search_run.get("witnesses") else None
        full_first = full["stages"][0]["first_witness"]
        canonical_match = (
            (canonical_first is None and full_first is None)
            or (canonical_first is not None and full_first is not None
                and canonical_first.get("ast_sha256") == full_first.get("ast_sha256"))
        )
        results.append({
            "task_id": task["task_id"],
            "role": task["role"],
            "expected_native_outcome": task["expected_native_outcome"],
            "canonical_full_search_first_witness_match": canonical_match,
            "canonical_native_status": verify_run.get("status"),
            "modes": task_modes,
        })

    summary_by_mode = []
    for mode_id in mode_ids:
        selected = [next(item for item in task["modes"] if item["mode_id"] == mode_id) for task in results]
        summary_by_mode.append({
            "mode_id": mode_id,
            "tasks": len(selected),
            "expectation_met": sum(bool(item["expectation_met"]) for item in selected),
            "false_promotions": sum(bool(item["false_promotion"]) for item in selected),
            "total_rule_application_checks": sum(int(item["total_rule_application_checks"]) for item in selected),
            "feedback_applications": sum(bool(item["feedback_applied"]) for item in selected),
        })
    deterministic = {
        "evaluation_id": spec["evaluation_id"],
        "budget": dict(budget),
        "seed": seed,
        "task_count": len(results),
        "results": results,
        "summary_by_mode": summary_by_mode,
        "scope_conclusion": (
            "DESCRIPTIVE_M4_LITE_ONLY: same-designer tasks and proposals; no blind-model, novelty, "
            "population-level, or general effectiveness inference"
        ),
    }
    return deterministic, {"timings": timings}


def run_evaluation(root: Path, spec_path: Path, run_id: str, output_path: Path) -> dict:
    deterministic, timing = compute_evaluation(root, spec_path)
    payload = {
        "schema_version": RUN_SCHEMA,
        "run_id": run_id,
        "created_at_utc": utc_now(),
        "evaluator": file_pin(root, "machine-overview/m4_eval.py"),
        "spec": file_pin(root, relative(root, spec_path)),
        "git": git_state(root),
        "deterministic": deterministic,
        "deterministic_sha256": sha256_bytes(json_bytes(deterministic)),
        "descriptive_timing": timing,
    }
    if output_path.exists():
        raise MachineOverviewError(f"M4_RUN_ALREADY_EXISTS:{relative(root, output_path)}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(output_path, payload)
    return payload


def verify_evaluation(root: Path, run_path: Path) -> dict:
    run = read_json(run_path)
    if run.get("schema_version") != RUN_SCHEMA:
        raise MachineOverviewError("M4_RUN_SCHEMA_INVALID")
    verify_pin(root, run.get("evaluator"), "run.evaluator")
    spec_path = verify_pin(root, run.get("spec"), "run.spec")
    deterministic, _ = compute_evaluation(root, spec_path)
    digest = sha256_bytes(json_bytes(deterministic))
    if digest != run.get("deterministic_sha256") or deterministic != run.get("deterministic"):
        raise MachineOverviewError("M4_RUN_REPLAY_MISMATCH")
    return {
        "status": "M4_LITE_REPLAY_VALID",
        "run_id": run.get("run_id"),
        "deterministic_sha256": digest,
        "tasks": deterministic["task_count"],
    }


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    sub = result.add_subparsers(dest="command", required=True)
    freeze = sub.add_parser("freeze")
    freeze.add_argument("--protocol", required=True)
    freeze.add_argument("--out", required=True)
    run = sub.add_parser("run")
    run.add_argument("--spec", required=True)
    run.add_argument("--run-id", required=True)
    run.add_argument("--out", required=True)
    verify = sub.add_parser("verify")
    verify.add_argument("--run", required=True)
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    root = repo_root()
    try:
        if args.command == "freeze":
            output = resolve(root, args.out)
            result = freeze_design(root, resolve(root, args.protocol), output)
            print(json.dumps({"status": "M4_DESIGN_FROZEN", "path": relative(root, output),
                              "freeze_id": result["freeze_id"]}, ensure_ascii=False, indent=2))
        elif args.command == "run":
            output = resolve(root, args.out)
            result = run_evaluation(root, resolve(root, args.spec), args.run_id, output)
            print(json.dumps({"status": "M4_LITE_COMPLETED", "path": relative(root, output),
                              "run_id": result["run_id"],
                              "summary": result["deterministic"]["summary_by_mode"]},
                             ensure_ascii=False, indent=2))
        else:
            print(json.dumps(verify_evaluation(root, resolve(root, args.run)), ensure_ascii=False, indent=2))
    except MachineOverviewError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
