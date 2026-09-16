"""Case revisions, verified input loading and workspace validation.

Every consumer entry point (search, verify, review, explain) resolves the case
through :func:`load_case_inputs`, which re-hashes the referenced profile, task
and grammar files against the frozen case revision and refuses to run on any
mismatch (audit F2).  :func:`validate_workspace` re-derives validity from the
original artifacts instead of trusting status strings (audit F3, F7).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from .profile import inspect_profile
from .search import compute_search_semantics, derive_witness_record, within_grammar_witness, witness_ast_sha256
from .util import (
    MachineOverviewError,
    assert_runner_unchanged,
    json_bytes,
    load_runner_registry_snapshot,
    read_json,
    safe_relative,
    sha256_bytes,
    sha256_file,
    utc_now,
    write_json,
)

SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")

SYMBOLIC_NATIVE_RENDERERS = {
    "l3_interval_observable_v1": "continuous_phase_obstruction",
    "l3_path_coherence_positive_v1": "path_coherence_positive",
    "l3_event_boundary_v1": "explicit_event_boundary",
    "l3_finite_to_exact_candidate_v1": "finite_to_exact_candidate",
    "m3_l2_truncated_limit_v1": "local_to_global_completion_boundary",
    "m3_l4_sip_observation_v1": "identity_observation_boundary",
    "m3_l5_self_guarantee_v1": "self_guarantee_diagonal_boundary",
    "m3_l6_compensation_conflict_v1": "compensation_coherence_conflict",
    "l5_given_proof_check_v1": "given_proof_check_capability",
    "l5_bounded_proof_search_v1": "bounded_proof_search_capability",
    "l5_finite_truth_decision_v1": "finite_truth_decision_capability",
    "l5_lob_self_certification_v1": "lob_self_certification_boundary",
}


def validate_identifier(value: str, label: str) -> str:
    if not isinstance(value, str) or not SAFE_ID.match(value) or value in {".", ".."}:
        raise MachineOverviewError(f"UNSAFE_IDENTIFIER:{label}:{value}")
    return value


def symbolic_renderer_id(grammar: dict) -> str:
    native = grammar.get("native_contract")
    renderer = native.get("renderer") if isinstance(native, dict) else None
    if renderer not in SYMBOLIC_NATIVE_RENDERERS:
        raise MachineOverviewError(f"SYMBOLIC_NATIVE_RENDERER_UNSUPPORTED:{renderer}")
    expected_observation = SYMBOLIC_NATIVE_RENDERERS[renderer]
    if grammar.get("observation_kind") != expected_observation:
        raise MachineOverviewError(
            f"SYMBOLIC_RENDERER_OBSERVATION_MISMATCH:{renderer}:{grammar.get('observation_kind')}"
        )
    return renderer


def _rel(repo_root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError as exc:
        raise MachineOverviewError(f"PATH_OUTSIDE_REPO:{path}") from exc


def resolve_path(repo_root: Path, value: str) -> Path:
    candidate = Path(value)
    candidate = candidate if candidate.is_absolute() else (repo_root / candidate)
    resolved = candidate.resolve()
    try:
        resolved.relative_to(repo_root.resolve())
    except ValueError as exc:
        raise MachineOverviewError(f"PATH_OUTSIDE_REPO:{value}") from exc
    return resolved


def case_files(case_dir: Path) -> list[Path]:
    return sorted(case_dir.glob("case-revision-*.json"),
                  key=lambda item: int(item.stem.rsplit("-", 1)[1]))


def load_case(repo_root: Path, value: str, revision: int | None = None) -> tuple[dict, Path]:
    """Load a case revision; a directory/id without revision selects the newest one."""
    path = resolve_path(repo_root, value)
    if path.is_dir():
        revisions = case_files(path)
        if not revisions:
            raise MachineOverviewError(f"CASE_REVISION_NOT_FOUND:{path}")
        if revision is None:
            path = revisions[-1]
        else:
            candidate = path / f"case-revision-{revision}.json"
            if not candidate.is_file():
                raise MachineOverviewError(f"CASE_REVISION_NOT_FOUND:{candidate}")
            path = candidate
    case = read_json(path)
    if case.get("schema_version") != "machine-overview-case/v1":
        if case.get("schema_version") != "machine-overview-case/v2":
            raise MachineOverviewError("CASE_SCHEMA_INVALID")
    validate_identifier(case.get("case_id"), "case_id")
    if revision is not None and int(case.get("revision", -1)) != int(revision):
        raise MachineOverviewError(f"CASE_REVISION_MISMATCH:{path}")
    return case, path


def case_identity_sha256(case: dict) -> str:
    payload = {
        "case_id": case["case_id"],
        "revision": case["revision"],
        "task_sha256": case["task"]["sha256"],
        "grammar_sha256": case["grammar"]["sha256"],
    }
    # v1 evidence used an identity that did not bind the profile. Keep that
    # historical algorithm readable; every new v2 identity also binds the
    # exact qualified profile bytes.
    if case.get("schema_version") == "machine-overview-case/v2":
        payload["profile_sha256"] = case["profile"]["sha256"]
    return sha256_bytes(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8"))


def load_case_inputs(repo_root: Path, case: dict, *, verify_profile: bool = True) -> dict:
    """Re-hash the frozen inputs; fail closed on any mismatch (audit F2)."""
    inputs: dict = {}
    for key in ("profile", "task", "grammar"):
        pinned = case.get(key)
        if not isinstance(pinned, dict) or not isinstance(pinned.get("sha256"), str):
            raise MachineOverviewError(f"CASE_INPUT_PIN_MISSING:{key}")
        path = repo_root / safe_relative(pinned["path"])
        if not path.is_file():
            raise MachineOverviewError(f"CASE_INPUT_MISSING:{key}:{pinned['path']}")
        data = path.read_bytes()
        digest = sha256_bytes(data)
        if digest != pinned["sha256"]:
            raise MachineOverviewError(f"CASE_INPUT_HASH_MISMATCH:{key}")
        inputs[key] = {"path": pinned["path"], "sha256": digest, "bytes": data, "data": json.loads(data)}
    if verify_profile:
        report = inspect_profile(repo_root, repo_root / case["profile"]["path"], fast=False)
        inputs["profile_report"] = report
        if report["status"] != "PROFILE_QUALIFIED":
            raise MachineOverviewError(f"PROFILE_NOT_QUALIFIED:{report['failures']}")
    return inputs


def validate_task_grammar_contract(task: dict, grammar: dict) -> None:
    """Check cross-document semantics that hashes alone cannot express."""
    if grammar.get("backend") != "symbolic-horn-v1":
        return
    freeze = grammar.get("engine_freeze")
    visibility = task.get("answer_visibility")
    if not isinstance(freeze, dict) or not isinstance(visibility, dict):
        raise MachineOverviewError("SYMBOLIC_HOLDOUT_BINDING_MISSING")
    if (visibility.get("engine_freeze") != freeze.get("path")
            or visibility.get("engine_freeze_sha256") != freeze.get("sha256")):
        raise MachineOverviewError("SYMBOLIC_HOLDOUT_BINDING_MISMATCH")
    if grammar.get("calibration_benchmark") is not None:
        raise MachineOverviewError("SYMBOLIC_HOLDOUT_BENCHMARK_FORBIDDEN")
    observations = task.get("correspondence", {}).get("declared_observation_kinds", [])
    if grammar.get("observation_kind") not in observations:
        raise MachineOverviewError("SYMBOLIC_OBSERVATION_NOT_DECLARED_BY_TASK")
    if task.get("research_relation") == "calibration":
        raise MachineOverviewError("SYMBOLIC_HOLDOUT_CANNOT_BE_CALIBRATION")
    symbolic_renderer_id(grammar)


def create_case(
    repo_root: Path,
    *,
    profile_path: Path,
    task_path: Path,
    grammar_path: Path,
    case_id: str | None = None,
    revision: int = 1,
) -> tuple[dict, Path]:
    task = read_json(task_path)
    grammar = read_json(grammar_path)
    profile = read_json(profile_path)
    if task.get("schema_version") != "machine-overview-task/v1":
        raise MachineOverviewError("TASK_SCHEMA_INVALID")
    if grammar.get("schema_version") != "machine-overview-grammar/v1":
        raise MachineOverviewError("GRAMMAR_SCHEMA_INVALID")
    validate_task_grammar_contract(task, grammar)
    profile_report = inspect_profile(
        repo_root, profile_path, fast=profile.get("schema_version") != "machine-overview-profile/v2",
    )
    if profile_report["status"] != "PROFILE_QUALIFIED":
        raise MachineOverviewError(f"PROFILE_NOT_QUALIFIED:{profile_report['failures']}")

    resolved_id = validate_identifier(case_id or task["task_id"], "case_id")
    case_dir = repo_root / "machine-overview" / "cases" / resolved_id
    case_path = case_dir / f"case-revision-{int(revision)}.json"
    parent_revision = None
    if revision > 1:
        parent_path = case_dir / f"case-revision-{revision - 1}.json"
        if not parent_path.is_file():
            raise MachineOverviewError(f"PARENT_CASE_REVISION_MISSING:{parent_path}")
        parent_revision = revision - 1

    claim_refs: set[str] = set(task.get("claim_refs", []))
    benchmark = grammar.get("calibration_benchmark") or {}
    claim_refs.update(benchmark.get("claim_refs", []))
    for control in task.get("known_positive_controls", []):
        claim_refs.update(control.get("claim_refs", []))

    strict_case = profile.get("schema_version") == "machine-overview-profile/v2"
    engine_freeze = grammar.get("engine_freeze")
    engine_pins = []
    if isinstance(engine_freeze, dict):
        freeze_path = repo_root / safe_relative(engine_freeze.get("path", ""))
        if not freeze_path.is_file() or sha256_file(freeze_path) != engine_freeze.get("sha256"):
            raise MachineOverviewError("ENGINE_FREEZE_PIN_INVALID")
        engine_pins = [{
            "path": engine_freeze["path"], "sha256": engine_freeze["sha256"], "role": "engine_freeze",
        }]
    case = {
        "schema_version": "machine-overview-case/v2" if strict_case else "machine-overview-case/v1",
        "case_id": resolved_id,
        "revision": int(revision),
        "parent_revision": parent_revision,
        "created_at_utc": utc_now(),
        "profile": {"path": _rel(repo_root, profile_path), "sha256": sha256_file(profile_path)},
        "task": {"path": _rel(repo_root, task_path), "sha256": sha256_file(task_path)},
        "grammar": {"path": _rel(repo_root, grammar_path), "sha256": sha256_file(grammar_path)},
        "source_pins": [
            {"path": source["path"], "sha256": source.get("sha256")}
            for source in list(profile.get("sources", [])) + list(profile.get("support_sources", []))
        ] + ([
            {"path": profile["toolchain_ref"], "sha256": profile.get("toolchain_sha256"), "role": "toolchain"},
            {"path": profile["library_registry"], "sha256": profile.get("library_registry_sha256"),
             "role": "library_registry"},
        ] if strict_case else []) + engine_pins,
        "candidate_ast": {
            "status": "PENDING_SEARCH",
            "grammar_id": grammar["grammar_id"],
            "produced_by": None,
        },
        "target_text_hash": None,
        "assumptions": task.get("assumptions", []),
        "obligations": task.get("obligations", []),
        "claim_refs": sorted(claim_refs),
        "state_axes": {
            "formal_legality": "unchecked",
            "mathematical_evidence": "conjecture",
            "task_preservation": "unresolved",
            "reality_correspondence": "model_only",
            "research_relation": task.get("research_relation", "calibration"),
            "execution": "queued",
        },
        "immutability": "content changes require a new revision file; this file is never edited",
    }
    if case_path.exists():
        existing = read_json(case_path)
        comparable = dict(existing)
        comparable.pop("created_at_utc", None)
        probe = dict(case)
        probe.pop("created_at_utc", None)
        if comparable == probe:
            return existing, case_path
        raise MachineOverviewError(f"CASE_ALREADY_EXISTS_WITH_DIFFERENT_CONTENT:{case_path}")
    write_json(case_path, case)
    return case, case_path


def _validate_completed_attempt(run_id: str, run_dir: Path, run: dict, errors: list[str]) -> None:
    attempt_path = run_dir / "ATTEMPT.json"
    if not attempt_path.is_file():
        errors.append(f"RUN_ATTEMPT_MISSING:{run_id}")
        return
    attempt = read_json(attempt_path)
    if attempt.get("schema_version") != "machine-overview-attempt/v2":
        errors.append(f"RUN_ATTEMPT_SCHEMA_INVALID:{run_id}")
    if attempt.get("status") != "COMPLETED" or not attempt.get("ended_at_utc"):
        errors.append(f"RUN_ATTEMPT_NOT_COMPLETED:{run_id}:{attempt.get('status')}")
    for key, expected in (
        ("run_id", run_id),
        ("case_id", run.get("case_id")),
        ("case_revision", run.get("case_revision")),
    ):
        if attempt.get(key) != expected:
            errors.append(f"RUN_ATTEMPT_IDENTITY_MISMATCH:{run_id}:{key}")
    if run.get("kind") == "verify":
        for key in ("witness_id", "candidate_ast_sha256"):
            if attempt.get(key) != run.get(key):
                errors.append(f"RUN_ATTEMPT_IDENTITY_MISMATCH:{run_id}:{key}")
    expected_planned = ["search"] if run.get("kind") == "search" else [
        "verify", "controls", "negative-control",
    ] + (["verify-replay"] if run.get("replay") is not None else [])
    if attempt.get("planned") != expected_planned:
        errors.append(f"RUN_ATTEMPT_PLAN_MISMATCH:{run_id}")
    run_attempt = run.get("attempt") or {}
    if run_attempt.get("attempt") != attempt.get("attempt"):
        errors.append(f"RUN_ATTEMPT_NUMBER_MISMATCH:{run_id}")
    runner = run.get("runner")
    if not isinstance(runner, dict):
        errors.append(f"RUNNER_BINDING_MISSING:{run_id}")
    else:
        try:
            assert_runner_unchanged(run_dir.parents[2], run_dir, runner, require_live_match=False)
        except MachineOverviewError as exc:
            errors.append(f"RUNNER_EVIDENCE_INVALID:{run_id}:{exc}")
        else:
            try:
                snapshot_registry = load_runner_registry_snapshot(run_dir, runner)
            except MachineOverviewError as exc:
                errors.append(f"RUNNER_REGISTRY_INVALID:{run_id}:{exc}")
            else:
                if run.get("coordinator_version") != snapshot_registry.get("coordinator_version"):
                    errors.append(f"RUNNER_COORDINATOR_VERSION_MISMATCH:{run_id}")
                if run.get("registry_id") != snapshot_registry.get("registry_id"):
                    errors.append(f"RUNNER_REGISTRY_ID_MISMATCH:{run_id}")
                manifest = read_json(run_dir / safe_relative(runner["path"]))
                captured_git = manifest.get("git", {})
                run_git = run.get("git", {})
                for key in ("worktree_root", "head", "branch", "git_dir", "git_common_dir"):
                    if run_git.get(key) != captured_git.get(key):
                        errors.append(f"RUNNER_GIT_IDENTITY_MISMATCH:{run_id}:{key}")


def _kernel_artifact_errors(run_id: str, run_dir: Path, run: dict, *, strict: bool = False) -> list[str]:
    errors: list[str] = []
    kernels = run.get("kernel_runs", [])
    if not isinstance(kernels, list):
        return [f"KERNEL_RUNS_INVALID:{run_id}"]
    if strict:
        labels = [item.get("label") for item in kernels]
        expected_labels = ["verify", "controls", "negative-control", "verify-replay"]
        if labels != expected_labels:
            errors.append(f"KERNEL_LABEL_SET_MISMATCH:{run_id}:{labels}")
    for kernel in kernels:
        label = kernel.get("label", "?")
        kernel_dir = run_dir / "kernel" / str(label)
        if strict and kernel_dir.is_dir():
            actual_files = sorted(path.name for path in kernel_dir.iterdir() if path.is_file())
            expected_files = ["command.json", "environment.txt", "stderr.txt", "stdout.txt"]
            if actual_files != expected_files:
                errors.append(f"KERNEL_ARTIFACT_ROSTER_MISMATCH:{run_id}:{label}:{actual_files}")
        artifact_rows = kernel.get("artifacts", {})
        for artifact_key, default_name in (
            ("stdout", "stdout.txt"), ("stderr", "stderr.txt"),
            ("command", "command.json"), ("environment", "environment.txt"),
        ):
            row = artifact_rows.get(artifact_key, {}) if isinstance(artifact_rows, dict) else {}
            name = row.get("path", default_name)
            if strict and name != default_name:
                errors.append(f"KERNEL_ARTIFACT_PATH_MISMATCH:{run_id}:{label}:{artifact_key}:{name}")
                name = default_name
            path = kernel_dir / name
            if not path.is_file():
                errors.append(f"KERNEL_ARTIFACT_MISSING:{run_id}:{label}:{name}")
                continue
            data = path.read_bytes()
            if strict and (row.get("bytes") != len(data) or row.get("sha256") != sha256_bytes(data)):
                errors.append(f"KERNEL_ARTIFACT_HASH_MISMATCH:{run_id}:{label}:{name}")
            if artifact_key in ("stdout", "stderr"):
                if kernel.get(f"{artifact_key}_bytes") != len(data) or kernel.get(
                        f"{artifact_key}_sha256") != sha256_bytes(data):
                    errors.append(f"KERNEL_ARTIFACT_HASH_MISMATCH:{run_id}:{label}:{name}:top-level")
        if strict and (kernel_dir / "command.json").is_file():
            command = read_json(kernel_dir / "command.json")
            expected_command = {
                "command_argv": kernel.get("command_argv"),
                "cwd": kernel.get("cwd"),
                "exit_code": kernel.get("exit_code"),
                "timed_out": kernel.get("timed_out"),
                "timeout_seconds": kernel.get("timeout_seconds"),
            }
            if command != expected_command:
                errors.append(f"KERNEL_COMMAND_RECEIPT_MISMATCH:{run_id}:{label}")
        if strict and (kernel_dir / "environment.txt").is_file():
            expected_environment = (str(kernel.get("environment", "")) + "\n").encode("utf-8")
            if (kernel_dir / "environment.txt").read_bytes() != expected_environment:
                errors.append(f"KERNEL_ENVIRONMENT_CONTENT_MISMATCH:{run_id}:{label}")
        if strict and (kernel_dir / "stdout.txt").is_file() and (kernel_dir / "stderr.txt").is_file():
            from .verify import classify_kernel_result

            derived = classify_kernel_result(
                entry=kernel.get("entry", ""),
                exit_code=kernel.get("exit_code"),
                timed_out=bool(kernel.get("timed_out")),
                expect_success=bool(kernel.get("expect_success")),
                stdout=(kernel_dir / "stdout.txt").read_bytes(),
                stderr=(kernel_dir / "stderr.txt").read_bytes(),
            )
            for key in ("status", "expectation_met", "diagnostic"):
                if kernel.get(key) != derived[key]:
                    errors.append(f"KERNEL_DERIVED_FIELD_MISMATCH:{run_id}:{label}:{key}")
        if kernel.get("status") == "KERNEL_TIMEOUT" and not kernel.get("timed_out"):
            errors.append(f"KERNEL_TIMEOUT_RECORD_INCONSISTENT:{run_id}:{label}")
        expected = kernel.get("expectation_met")
        status = kernel.get("status")
        if expected is True and status not in ("KERNEL_ACCEPTED", "KERNEL_REJECTED_AS_EXPECTED"):
            errors.append(f"KERNEL_EXPECTATION_STATUS_INCONSISTENT:{run_id}:{label}:{status}")
        if expected is False and status in ("KERNEL_ACCEPTED", "KERNEL_REJECTED_AS_EXPECTED"):
            errors.append(f"KERNEL_EXPECTATION_STATUS_INCONSISTENT:{run_id}:{label}:{status}")
    return errors


def _validate_search_run(run_id: str, run: dict, run_dir: Path, case: dict, case_file: Path,
                         repo_root: Path, errors: list[str]) -> None:
    if run.get("schema_version") != "machine-overview-search-run/v2":
        errors.append(f"SEARCH_SCHEMA_INVALID:{run_id}")
    if run_id != run_dir.name or run.get("run_id") != run_id:
        errors.append(f"SEARCH_RUN_DIRECTORY_ID_MISMATCH:{run_id}:{run_dir.name}")
    actual_top = sorted(path.name for path in run_dir.iterdir())
    expected_top = ["ATTEMPT.json", "RUN.json", "runner-manifest.json", "runner-snapshot"]
    if actual_top != expected_top:
        errors.append(f"SEARCH_ARTIFACT_ROSTER_MISMATCH:{run_id}:{actual_top}")
    inputs = run.get("inputs", {})
    if run.get("case_pointer") != case_file.as_posix() or run.get("evidence_refs") != [case_file.as_posix()]:
        errors.append(f"SEARCH_CASE_POINTER_MISMATCH:{run_id}")
    if inputs.get("case_sha256") != sha256_file(case_file):
        errors.append(f"SEARCH_CASE_HASH_MISMATCH:{run_id}")
    if run.get("case_identity_sha256") != case_identity_sha256(case):
        errors.append(f"SEARCH_CASE_IDENTITY_MISMATCH:{run_id}")
    for key in ("profile", "task", "grammar"):
        if inputs.get(f"{key}_sha256") != case[key]["sha256"]:
            errors.append(f"SEARCH_INPUT_HASH_MISMATCH:{run_id}:{key}")
        verified = inputs.get("verified_inputs", {}).get(key, {})
        if verified.get("path") != case[key]["path"] or verified.get("sha256") != case[key]["sha256"]:
            errors.append(f"SEARCH_VERIFIED_INPUT_MISMATCH:{run_id}:{key}")
    if inputs.get("task_path") != case["task"]["path"] or inputs.get("grammar_path") != case["grammar"]["path"]:
        errors.append(f"SEARCH_INPUT_PATH_MISMATCH:{run_id}")
    profile_report = inspect_profile(
        repo_root, repo_root / safe_relative(case["profile"]["path"]), fast=True,
    )
    expected_profile = {
        "profile_id": profile_report.get("profile_id"),
        "profile_status": profile_report.get("status"),
        "toolchain_ref": profile_report.get("toolchain_ref"),
    }
    if run.get("profile") != expected_profile:
        errors.append(f"SEARCH_PROFILE_BINDING_MISMATCH:{run_id}")
    grammar = read_json(repo_root / safe_relative(case["grammar"]["path"]))
    try:
        expected = compute_search_semantics(grammar, run.get("budget", {}), run.get("seed"))
    except MachineOverviewError as exc:
        errors.append(f"SEARCH_RECOMPUTE_FAILED:{run_id}:{exc}")
        expected = None
    if expected is not None:
        for key in (
            "budget", "seed", "statistics", "order_independence_check", "grammar_sensitivity_check",
            "calibration_match", "witnesses", "controls", "exit_reason",
        ):
            if run.get(key) != expected.get(key):
                errors.append(f"SEARCH_RECOMPUTED_FIELD_MISMATCH:{run_id}:{key}")
    witness_ids = [witness.get("witness_id") for witness in run.get("witnesses", [])]
    if len(witness_ids) != len(set(witness_ids)):
        errors.append(f"SEARCH_DUPLICATE_WITNESS_ID:{run_id}")
    for witness in run.get("witnesses", []):
        try:
            derived = derive_witness_record(witness, grammar)
        except MachineOverviewError as exc:
            errors.append(f"WITNESS_SEMANTICS_INVALID:{run_id}:{witness.get('witness_id')}:{exc}")
            continue
        if witness != derived:
            errors.append(f"WITNESS_SEMANTICS_MISMATCH:{run_id}:{witness.get('witness_id')}")
    _validate_completed_attempt(run_id, run_dir, run, errors)


def _validate_legacy_run(run_id: str, run: dict, run_dir: Path, case: dict, case_file: Path,
                         errors: list[str]) -> None:
    """Pre-audit receipts without the binding fields: verify what can still be checked."""
    if run.get("kind") == "search":
        inputs = run.get("inputs", {})
        if inputs.get("case_sha256") != sha256_file(case_file):
            errors.append(f"SEARCH_CASE_HASH_MISMATCH:{run_id}")
        for key in ("task", "grammar"):
            if inputs.get(f"{key}_sha256") != case[key]["sha256"]:
                errors.append(f"SEARCH_INPUT_HASH_MISMATCH:{run_id}:{key}")
    elif run.get("kind") == "verify":
        for name, row in run.get("generated_sources", {}).items():
            path = run_dir / "generated" / name
            if not path.is_file():
                errors.append(f"GENERATED_SOURCE_MISSING:{run_id}:{name}")
            elif sha256_bytes(path.read_bytes()) != row.get("sha256"):
                errors.append(f"GENERATED_SOURCE_MISMATCH:{run_id}:{name}")
        target_path = run_dir / "generated" / "Target.agda"
        if target_path.is_file() and sha256_bytes(target_path.read_bytes()) != run.get("target_text_hash"):
            errors.append(f"TARGET_HASH_MISMATCH:{run_id}")
        errors.extend(_kernel_artifact_errors(run_id, run_dir, run))
    else:
        errors.append(f"RUN_KIND_UNKNOWN:{run_id}")


def _validate_verify_run(run_id: str, run: dict, run_dir: Path, case: dict, case_file: Path,
                         repo_root: Path, runs: dict, errors: list[str]) -> None:
    from .verify import (
        check_proof_hygiene,
        claim_relation_for_case,
        classify_replay,
        derive_verify_status,
        kernel_command,
        render_controls,
        render_falsify,
        render_proof,
        render_target,
        render_verify,
        verify_success_status,
        witness_statement,
    )

    if run.get("schema_version") != "machine-overview-verify-run/v2":
        errors.append(f"VERIFY_SCHEMA_INVALID:{run_id}")
    if run_id != run_dir.name or run.get("run_id") != run_id:
        errors.append(f"VERIFY_RUN_DIRECTORY_ID_MISMATCH:{run_id}:{run_dir.name}")
    actual_top = sorted(path.name for path in run_dir.iterdir())
    expected_top = ["ATTEMPT.json", "RUN.json", "generated", "kernel", "runner-manifest.json", "runner-snapshot"]
    if actual_top != expected_top:
        errors.append(f"VERIFY_ARTIFACT_ROSTER_MISMATCH:{run_id}:{actual_top}")
    binding = run.get("source_search_run", {})
    search_run_id = binding.get("run_id")
    if not search_run_id or search_run_id not in runs:
        errors.append(f"VERIFY_UNKNOWN_SEARCH_RUN:{run_id}")
        return
    search_run, search_run_dir = runs[search_run_id]
    if search_run.get("schema_version") != "machine-overview-search-run/v2":
        errors.append(f"VERIFY_SEARCH_RUN_NOT_STRICT_V2:{run_id}:{search_run_id}")
    if (search_run.get("case_id"), int(search_run.get("case_revision", -1))) != (
            case["case_id"], int(case["revision"])):
        errors.append(f"VERIFY_SEARCH_CASE_MISMATCH:{run_id}")
    if binding.get("sha256") != sha256_file(search_run_dir / "RUN.json"):
        errors.append(f"VERIFY_SEARCH_RUN_HASH_MISMATCH:{run_id}")
    if binding.get("path") != (search_run_dir / "RUN.json").as_posix():
        errors.append(f"VERIFY_SEARCH_RUN_PATH_MISMATCH:{run_id}")
    if binding.get("case_revision") != case["revision"]:
        errors.append(f"VERIFY_SEARCH_BINDING_REVISION_MISMATCH:{run_id}")
    grammar = read_json(repo_root / safe_relative(case["grammar"]["path"]))
    witnesses = {w["witness_id"]: w for w in search_run.get("witnesses", [])}
    witness = witnesses.get(run.get("witness_id"))
    if witness is None:
        errors.append(f"VERIFY_WITNESS_NOT_IN_SEARCH_RUN:{run_id}")
    else:
        if run.get("candidate_ast_sha256") != witness.get("ast_sha256"):
            errors.append(f"VERIFY_CANDIDATE_AST_HASH_MISMATCH:{run_id}")
        try:
            derived_witness = derive_witness_record(witness, grammar)
        except MachineOverviewError as exc:
            errors.append(f"VERIFY_WITNESS_SEMANTICS_INVALID:{run_id}:{exc}")
            derived_witness = None
        if derived_witness is not None and witness != derived_witness:
            errors.append(f"VERIFY_WITNESS_SEMANTICS_MISMATCH:{run_id}")
    if run.get("case_sha256") != sha256_file(case_file):
        errors.append(f"VERIFY_CASE_HASH_MISMATCH:{run_id}")
    if run.get("case_pointer") != case_file.as_posix():
        errors.append(f"VERIFY_CASE_POINTER_MISMATCH:{run_id}")
    if run.get("case_identity_sha256") != case_identity_sha256(case):
        errors.append(f"VERIFY_CASE_IDENTITY_MISMATCH:{run_id}")
    profile_report = inspect_profile(repo_root, repo_root / safe_relative(case["profile"]["path"]), fast=False)
    if profile_report.get("status") != "PROFILE_QUALIFIED":
        errors.append(f"VERIFY_PROFILE_NOT_QUALIFIED:{run_id}")
    toolchain = read_json(repo_root / safe_relative(profile_report["toolchain_ref"]))
    expected_profile = {
        "profile_id": profile_report.get("profile_id"),
        "profile_status": profile_report.get("status"),
        "toolchain_ref": profile_report.get("toolchain_ref"),
    }
    if run.get("profile") != expected_profile:
        errors.append(f"VERIFY_PROFILE_BINDING_MISMATCH:{run_id}")
    toolchain_identity = run.get("toolchain_identity", {})
    expected_toolchain = {
        "agda_binary": toolchain["agda"]["local_binary"],
        "agda_binary_sha256": sha256_file(Path(toolchain["agda"]["local_binary"])),
        "agda_version": toolchain["agda"]["version"],
        "cubical_library_file": toolchain["cubical_library"]["library_file"],
        "cubical_library_file_sha256": sha256_file(Path(toolchain["cubical_library"]["library_file"])),
        "cubical_version": toolchain["cubical_library"]["version"],
        "cubical_tree_sha256": toolchain["cubical_library"]["tree_sha256"],
        "toolchain_config_sha256": profile_report.get("toolchain_sha256"),
        "library_registry": profile_report.get("library_registry"),
        "library_registry_sha256": sha256_file(
            repo_root / safe_relative(profile_report["library_registry"])
        ),
    }
    if toolchain_identity != expected_toolchain:
        errors.append(f"VERIFY_TOOLCHAIN_IDENTITY_MISMATCH:{run_id}")

    expected_include_dirs = list(profile_report.get("native_include_dirs") or [
        "machine-overview/formal", "HoTT/formal/partiality-race-timeout",
    ]) + [f"machine-overview/runs/{run_id}/generated"]
    if run.get("include_dirs") != expected_include_dirs:
        errors.append(f"VERIFY_INCLUDE_DIRS_MISMATCH:{run_id}")

    expected_generated = ("Target.agda", "Proof.agda", "Verify.agda", "Controls.agda", "Falsify.agda")
    generated_dir = run_dir / "generated"
    if generated_dir.is_dir():
        actual_agda_sources = sorted(path.name for path in generated_dir.glob("*.agda"))
        if actual_agda_sources != sorted(expected_generated):
            errors.append(f"GENERATED_SOURCE_ROSTER_MISMATCH:{run_id}:{actual_agda_sources}")
    generated = run.get("generated_sources", {})
    if not isinstance(generated, dict) or set(generated) != set(expected_generated):
        errors.append(f"GENERATED_SOURCE_SET_MISMATCH:{run_id}")
        generated = generated if isinstance(generated, dict) else {}
    for name in expected_generated:
        row = generated.get(name, {})
        path = run_dir / "generated" / name
        if not path.is_file():
            errors.append(f"GENERATED_SOURCE_MISSING:{run_id}:{name}")
        else:
            data = path.read_bytes()
            if sha256_bytes(data) != row.get("sha256") or len(data) != row.get("bytes"):
                errors.append(f"GENERATED_SOURCE_MISMATCH:{run_id}:{name}")
    target_path = run_dir / "generated" / "Target.agda"
    if run.get("proof_origin") not in ("coordinator_template", "external_file"):
        errors.append(f"PROOF_ORIGIN_INVALID:{run_id}:{run.get('proof_origin')}")
    if witness is not None:
        expected_texts = {
            "Target.agda": render_target(case, witness, grammar),
            "Verify.agda": render_verify(witness, grammar),
            "Controls.agda": render_controls(witness, grammar),
            "Falsify.agda": render_falsify(witness, grammar),
        }
        if run.get("proof_origin") == "coordinator_template":
            expected_texts["Proof.agda"] = render_proof(case, witness, grammar)
        for name, text in expected_texts.items():
            path = run_dir / "generated" / name
            if path.is_file() and path.read_bytes() != text.encode("utf-8"):
                errors.append(f"GENERATED_SOURCE_RECOMPUTE_MISMATCH:{run_id}:{name}")
        proof_path = run_dir / "generated" / "Proof.agda"
        if proof_path.is_file():
            try:
                check_proof_hygiene(proof_path.read_text(encoding="utf-8"), run.get("proof_origin", "unknown"))
            except (MachineOverviewError, UnicodeError) as exc:
                errors.append(f"PROOF_HYGIENE_INVALID:{run_id}:{exc}")
        expected_statement = witness_statement(witness, grammar)
        if run.get("statement") != expected_statement:
            errors.append(f"VERIFY_STATEMENT_MISMATCH:{run_id}")
    if target_path.is_file() and sha256_bytes(target_path.read_bytes()) != run.get("target_text_hash"):
        errors.append(f"TARGET_HASH_MISMATCH:{run_id}")
    ledger_path = repo_root / "machine-overview" / "cases" / case["case_id"] / f"target-freeze-{case['revision']}.json"
    if not ledger_path.is_file():
        errors.append(f"TARGET_FREEZE_LEDGER_MISSING:{run_id}")
    else:
        ledger = read_json(ledger_path)
        if ledger.get("schema_version") != "machine-overview-target-freeze/v1" or (
                ledger.get("case_id"), ledger.get("revision")) != (case["case_id"], case["revision"]):
            errors.append(f"TARGET_FREEZE_LEDGER_IDENTITY_MISMATCH:{run_id}")
        entry = ledger.get("entries", {}).get(run.get("candidate_ast_sha256", ""))
        if entry is None:
            errors.append(f"TARGET_FREEZE_ENTRY_MISSING:{run_id}")
        elif entry.get("target_text_hash") != run.get("target_text_hash"):
            errors.append(f"TARGET_FREEZE_MISMATCH:{run_id}")
        expected_freeze = {
            "ledger": ledger_path.relative_to(repo_root).as_posix(),
            "status": "FROZEN" if entry and entry.get("first_verify_run") == run_id else "REUSED",
        }
        if run.get("target_freeze") != expected_freeze:
            errors.append(f"TARGET_FREEZE_RECEIPT_MISMATCH:{run_id}")

    expected_closure_paths = [source["path"] for source in case.get("source_pins", [])] + [
        f"machine-overview/runs/{run_id}/generated/{name}" for name in expected_generated
    ]
    import_closure = run.get("import_closure")
    if not isinstance(import_closure, dict):
        errors.append(f"IMPORT_CLOSURE_MISSING:{run_id}")
    else:
        expected_options = [
            "--ignore-interfaces",
            f"--library-file={toolchain['project_library_registry']}",
            f"-l cubical-{toolchain['cubical_library']['version']}",
        ]
        if import_closure.get("entry") != f"machine-overview/runs/{run_id}/generated/Verify.agda":
            errors.append(f"IMPORT_CLOSURE_ENTRY_MISMATCH:{run_id}")
        if import_closure.get("options") != expected_options:
            errors.append(f"IMPORT_CLOSURE_OPTIONS_MISMATCH:{run_id}")
        rows = import_closure.get("sources", [])
        if [row.get("path") for row in rows] != expected_closure_paths:
            errors.append(f"IMPORT_CLOSURE_SOURCE_SET_MISMATCH:{run_id}")
        for row in rows:
            try:
                path = repo_root / safe_relative(row["path"])
            except (KeyError, MachineOverviewError) as exc:
                errors.append(f"IMPORT_CLOSURE_PATH_INVALID:{run_id}:{exc}")
                continue
            if not path.is_file() or sha256_file(path) != row.get("sha256"):
                errors.append(f"IMPORT_CLOSURE_HASH_MISMATCH:{run_id}:{row.get('path')}")

    errors.extend(_kernel_artifact_errors(run_id, run_dir, run, strict=True))
    kernels = run.get("kernel_runs", [])
    expected_kernel_specs = [
        ("verify", "Verify.agda", True),
        ("controls", "Controls.agda", True),
        ("negative-control", "Falsify.agda", False),
        ("verify-replay", "Verify.agda", True),
    ]
    for kernel, (label, filename, expect_success) in zip(kernels, expected_kernel_specs):
        entry = f"machine-overview/runs/{run_id}/generated/{filename}"
        if (
            kernel.get("label") != label
            or kernel.get("entry") != entry
            or kernel.get("expect_success") is not expect_success
            or kernel.get("cwd") != str(repo_root)
            or kernel.get("timeout_seconds") != run.get("timeout_seconds")
            or kernel.get("command_argv") != kernel_command(repo_root, toolchain, expected_include_dirs, entry)
        ):
            errors.append(f"KERNEL_INVOCATION_MISMATCH:{run_id}:{label}")
    replay = run.get("replay")
    if replay is None:
        errors.append(f"VERIFY_REPLAY_MISSING:{run_id}")
    if replay is not None:
        kernel_map = {item.get("label"): item for item in kernels}
        first = kernel_map.get("verify")
        second = kernel_map.get("verify-replay")
        first_stdout = run_dir / "kernel/verify/stdout.txt"
        second_stdout = run_dir / "kernel/verify-replay/stdout.txt"
        if first and second and first_stdout.is_file() and second_stdout.is_file():
            expected_replay = classify_replay(
                first,
                first_stdout.read_bytes(),
                second,
                second_stdout.read_bytes(),
            )
            expected_replay["exit_codes"] = [first.get("exit_code"), second.get("exit_code")]
            if replay != expected_replay:
                errors.append(f"VERIFY_REPLAY_MISMATCH:{run_id}")
        else:
            errors.append(f"VERIFY_REPLAY_ARTIFACT_MISSING:{run_id}")
    expected_status = derive_verify_status(kernels, replay, verify_success_status(case))
    if run.get("status") != expected_status:
        errors.append(f"VERIFY_STATUS_CONTRADICTION:{run_id}:{run.get('status')}:{expected_status}")
    expected_claim_relation = claim_relation_for_case(case)
    if run.get("claim_relation") != expected_claim_relation:
        errors.append(f"VERIFY_CLAIM_RELATION_MISMATCH:{run_id}")
    _validate_completed_attempt(run_id, run_dir, run, errors)


def validate_workspace(repo_root: Path) -> dict:
    root = repo_root / "machine-overview"
    errors: list[str] = []
    legacy_path = root / "legacy" / "legacy-evidence-v1.json"
    if not legacy_path.is_file():
        legacy = {"cases": {}, "runs": {}, "legacy_markers": {}, "interrupted_attempts": {}, "reviews": {}}
        errors.append("LEGACY_EVIDENCE_MANIFEST_MISSING")
    else:
        legacy = read_json(legacy_path)
        if legacy.get("schema_version") != "machine-overview-legacy-evidence/v1":
            errors.append("LEGACY_EVIDENCE_SCHEMA_INVALID")

    cases: dict[tuple[str, int], dict] = {}
    case_paths: dict[tuple[str, int], Path] = {}
    legacy_cases: list[dict] = []
    for case_file in sorted((root / "cases").glob("*/case-revision-*.json")):
        case = read_json(case_file)
        try:
            validate_identifier(case.get("case_id"), "case_id")
            revision = int(case.get("revision", -1))
        except (MachineOverviewError, TypeError, ValueError) as exc:
            errors.append(f"CASE_IDENTITY_INVALID:{case_file}:{exc}")
            continue
        key = (case["case_id"], revision)
        if key in cases:
            errors.append(f"CASE_IDENTITY_DUPLICATE:{case['case_id']}:{revision}")
        cases[key] = case
        case_paths[key] = case_file
        expected_name = f"case-revision-{revision}.json"
        if case_file.name != expected_name or case_file.parent.name != case["case_id"]:
            errors.append(f"CASE_PATH_IDENTITY_MISMATCH:{case_file}")
        case_digest = sha256_file(case_file)
        if case.get("schema_version") == "machine-overview-case/v1":
            legacy_key = f"{case['case_id']}@{revision}"
            if legacy.get("cases", {}).get(legacy_key) != case_digest:
                errors.append(f"LEGACY_CASE_NOT_ALLOWLISTED:{legacy_key}")
            else:
                legacy_cases.append({"case_id": case["case_id"], "revision": revision,
                                     "sha256": case_digest})
        elif case.get("schema_version") != "machine-overview-case/v2":
            errors.append(f"CASE_SCHEMA_INVALID:{case_file}")
        for name in ("profile", "task", "grammar"):
            pinned = case.get(name, {})
            try:
                path = repo_root / safe_relative(pinned["path"])
            except (KeyError, MachineOverviewError) as exc:
                errors.append(f"CASE_REFERENCE_INVALID:{case_file}:{name}:{exc}")
                continue
            if not path.is_file():
                errors.append(f"CASE_REFERENCE_MISSING:{case_file}:{name}")
            elif sha256_file(path) != pinned.get("sha256"):
                errors.append(f"CASE_REFERENCE_HASH_MISMATCH:{case_file}:{name}")
        if case.get("schema_version") == "machine-overview-case/v2":
            try:
                inputs = load_case_inputs(repo_root, case, verify_profile=True)
            except MachineOverviewError as exc:
                errors.append(f"CASE_STRICT_INPUT_INVALID:{case_file}:{exc}")
            else:
                profile = inputs["profile"]["data"]
                try:
                    validate_task_grammar_contract(inputs["task"]["data"], inputs["grammar"]["data"])
                except MachineOverviewError as exc:
                    errors.append(f"CASE_TASK_GRAMMAR_CONTRACT_INVALID:{case_file}:{exc}")
                expected_pins = [
                    {"path": source["path"], "sha256": source.get("sha256")}
                    for source in list(profile.get("sources", [])) + list(profile.get("support_sources", []))
                ] + [
                    {"path": profile["toolchain_ref"], "sha256": profile.get("toolchain_sha256"),
                     "role": "toolchain"},
                    {"path": profile["library_registry"], "sha256": profile.get("library_registry_sha256"),
                     "role": "library_registry"},
                ]
                engine_freeze = inputs["grammar"]["data"].get("engine_freeze")
                if isinstance(engine_freeze, dict):
                    expected_pins.append({
                        "path": engine_freeze.get("path"), "sha256": engine_freeze.get("sha256"),
                        "role": "engine_freeze",
                    })
                if case.get("source_pins") != expected_pins:
                    errors.append(f"CASE_SOURCE_PIN_SET_MISMATCH:{case_file}")

    runs: dict[str, tuple[dict, Path]] = {}
    interrupted_attempts: list[dict] = []
    legacy_runs: list[dict] = []
    for run_dir in sorted(path for path in (root / "runs").glob("*") if path.is_dir() and not path.name.startswith(".")):
        run_file = run_dir / "RUN.json"
        attempt_file = run_dir / "ATTEMPT.json"
        if not run_file.is_file():
            if not attempt_file.is_file():
                errors.append(f"RUN_DIRECTORY_WITHOUT_RECEIPT:{run_dir.name}")
                continue
            attempt = read_json(attempt_file)
            digest = sha256_file(attempt_file)
            if attempt.get("schema_version") == "machine-overview-attempt/v1":
                if legacy.get("interrupted_attempts", {}).get(run_dir.name) != digest:
                    errors.append(f"LEGACY_INTERRUPTED_ATTEMPT_NOT_ALLOWLISTED:{run_dir.name}")
                    continue
            elif attempt.get("schema_version") == "machine-overview-attempt/v2":
                status = attempt.get("status")
                expected_dir = f"{attempt.get('run_id')}.attempt-{attempt.get('attempt')}-interrupted"
                if status not in ("INTERRUPTED", "FAILED") or not attempt.get("ended_at_utc"):
                    errors.append(f"RUN_ATTEMPT_STATUS_INVALID:{run_dir.name}:{status}")
                    continue
                if run_dir.name != expected_dir and run_dir.name != attempt.get("run_id"):
                    errors.append(f"RUN_ATTEMPT_DIRECTORY_ID_MISMATCH:{run_dir.name}")
            else:
                errors.append(f"RUN_ATTEMPT_SCHEMA_INVALID:{run_dir.name}")
                continue
            interrupted_attempts.append({
                "run_id": run_dir.name, "status": attempt.get("status"), "error": attempt.get("error"),
                "attempt": attempt.get("attempt"), "sha256": digest,
            })
            continue
        run = read_json(run_file)
        run_id = run.get("run_id")
        try:
            validate_identifier(run_id, "run_id")
        except MachineOverviewError as exc:
            errors.append(f"RUN_ID_INVALID:{run_dir.name}:{exc}")
            continue
        if run_id != run_dir.name:
            errors.append(f"RUN_DIRECTORY_ID_MISMATCH:{run_id}:{run_dir.name}")
        if run_id in runs:
            errors.append(f"RUN_ID_DUPLICATE:{run_id}")
        runs[run_id] = (run, run_dir)
        if run.get("schema_version") in ("machine-overview-search-run/v1", "machine-overview-verify-run/v1"):
            run_digest = sha256_file(run_file)
            if legacy.get("runs", {}).get(run_id) != run_digest:
                errors.append(f"LEGACY_RUN_NOT_ALLOWLISTED:{run_id}")
            marker_path = run_dir / "LEGACY.json"
            expected_marker = legacy.get("legacy_markers", {}).get(run_id)
            if marker_path.is_file() and (expected_marker is None or sha256_file(marker_path) != expected_marker):
                errors.append(f"LEGACY_MARKER_NOT_ALLOWLISTED:{run_id}")
            legacy_runs.append({
                "run_id": run_id, "kind": run.get("kind"), "sha256": run_digest,
                "known_gaps": legacy.get("known_gaps", {}).get(run_id)
                or legacy.get("known_gaps", {}).get(
                    "postfix_verify_family" if "POSTFIX" in run_id else "preaudit_verify_family"
                ),
            })
        elif run.get("schema_version") not in ("machine-overview-search-run/v2", "machine-overview-verify-run/v2"):
            errors.append(f"RUN_SCHEMA_INVALID:{run_id}")

    for run_id, (run, run_dir) in runs.items():
        key = (run.get("case_id"), int(run.get("case_revision", -1)))
        if key not in cases:
            errors.append(f"RUN_REFERENCES_UNKNOWN_CASE_REVISION:{run_id}")
            continue
        schema = run.get("schema_version")
        if schema in ("machine-overview-search-run/v1", "machine-overview-verify-run/v1"):
            _validate_legacy_run(run_id, run, run_dir, cases[key], case_paths[key], errors)
        elif run.get("kind") == "search" and schema == "machine-overview-search-run/v2":
            _validate_search_run(run_id, run, run_dir, cases[key], case_paths[key], repo_root, errors)
        elif run.get("kind") == "verify" and schema == "machine-overview-verify-run/v2":
            _validate_verify_run(run_id, run, run_dir, cases[key], case_paths[key], repo_root, runs, errors)
        else:
            errors.append(f"RUN_KIND_SCHEMA_MISMATCH:{run_id}")

    reviews = 0
    legacy_reviews: list[dict] = []
    from .correspondence import derive_correspondence_content

    for review_file in sorted((root / "reviews").glob("*.json")):
        review = read_json(review_file)
        reviews += 1
        review_id = review.get("review_id")
        if review_file.stem != review_id:
            errors.append(f"REVIEW_FILE_ID_MISMATCH:{review_file.name}")
        if review.get("schema_version") == "machine-overview-correspondence-review/v1":
            digest = sha256_file(review_file)
            if legacy.get("reviews", {}).get(review_id) != digest:
                errors.append(f"LEGACY_REVIEW_NOT_ALLOWLISTED:{review_id}")
            else:
                legacy_reviews.append({"review_id": review_id, "sha256": digest})
            continue
        if review.get("schema_version") != "machine-overview-correspondence-review/v2":
            errors.append(f"REVIEW_SCHEMA_INVALID:{review_id}")
            continue
        binding = review.get("source_search_run", {})
        search_run_id = binding.get("run_id")
        if not search_run_id or search_run_id not in runs:
            errors.append(f"REVIEW_UNKNOWN_SEARCH_RUN:{review_file.name}")
            continue
        search_run, search_dir = runs[search_run_id]
        if search_run.get("schema_version") != "machine-overview-search-run/v2":
            errors.append(f"REVIEW_SEARCH_RUN_NOT_STRICT_V2:{review_id}:{search_run_id}")
        if binding.get("sha256") != sha256_file(search_dir / "RUN.json"):
            errors.append(f"REVIEW_SEARCH_HASH_MISMATCH:{review_id}")
        if binding.get("path") != (search_dir / "RUN.json").as_posix():
            errors.append(f"REVIEW_SEARCH_PATH_MISMATCH:{review_id}")
        witnesses = {w["witness_id"]: w for w in search_run.get("witnesses", [])}
        witness = witnesses.get(review.get("witness_id"))
        if witness is None:
            errors.append(f"REVIEW_WITNESS_NOT_IN_SEARCH_RUN:{review_file.name}")
        elif review.get("candidate_ast_sha256") != witness.get("ast_sha256"):
            errors.append(f"REVIEW_CANDIDATE_AST_HASH_MISMATCH:{review_file.name}")
        key = (review.get("case_id"), int(review.get("case_revision", -1)))
        if key not in cases or key != (search_run.get("case_id"), int(search_run.get("case_revision", -1))):
            errors.append(f"REVIEW_CASE_REVISION_MISMATCH:{review_file.name}")
        elif review.get("case_sha256") != sha256_file(case_paths[key]):
            errors.append(f"REVIEW_CASE_HASH_MISMATCH:{review_id}")
        elif review.get("case_pointer") != case_paths[key].as_posix():
            errors.append(f"REVIEW_CASE_PATH_MISMATCH:{review_id}")
        if key in cases and witness is not None:
            case = cases[key]
            try:
                task = read_json(repo_root / safe_relative(case["task"]["path"]))
                grammar = read_json(repo_root / safe_relative(case["grammar"]["path"]))
                profile_report = inspect_profile(
                    repo_root, repo_root / safe_relative(case["profile"]["path"]), fast=True,
                )
                expected_content = derive_correspondence_content(
                    case=case, task=task, witness=witness, profile_report=profile_report,
                    grammar=grammar, search_run=search_run,
                )
                expected_content.pop("derived_witness", None)
            except (KeyError, MachineOverviewError) as exc:
                errors.append(f"REVIEW_RECOMPUTE_FAILED:{review_id}:{exc}")
            else:
                for field, expected in expected_content.items():
                    if review.get(field) != expected:
                        errors.append(f"REVIEW_RECOMPUTED_FIELD_MISMATCH:{review_id}:{field}")
            expected_id = (
                f"RV-{case['case_id']}-r{case['revision']}-{search_run_id}-"
                f"{witness['witness_id']}-{witness['ast_sha256'][:8]}"
            )
            if review_id != expected_id:
                errors.append(f"REVIEW_DETERMINISTIC_ID_MISMATCH:{review_id}:{expected_id}")

    return {
        "schema_version": "machine-overview-validation/v2",
        "cases": len(cases),
        "legacy_cases": legacy_cases,
        "runs": len(runs),
        "reviews": reviews,
        "interrupted_attempts": interrupted_attempts,
        "legacy_runs": legacy_runs,
        "legacy_reviews": legacy_reviews,
        "errors": errors,
        "status": "VALID" if not errors else "INVALID",
    }
