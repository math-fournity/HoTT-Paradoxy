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
from .search import within_grammar_witness, witness_ast_sha256
from .util import (
    MachineOverviewError,
    read_json,
    safe_relative,
    sha256_bytes,
    sha256_file,
    utc_now,
    write_json,
)

SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$")


def validate_identifier(value: str, label: str) -> str:
    if not isinstance(value, str) or not SAFE_ID.match(value) or value in {".", ".."}:
        raise MachineOverviewError(f"UNSAFE_IDENTIFIER:{label}:{value}")
    return value


def _rel(repo_root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError as exc:
        raise MachineOverviewError(f"PATH_OUTSIDE_REPO:{path}") from exc


def resolve_path(repo_root: Path, value: str) -> Path:
    candidate = Path(value)
    return candidate if candidate.is_absolute() else (repo_root / candidate)


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
        raise MachineOverviewError("CASE_SCHEMA_INVALID")
    if revision is not None and int(case.get("revision", -1)) != int(revision):
        raise MachineOverviewError(f"CASE_REVISION_MISMATCH:{path}")
    return case, path


def case_identity_sha256(case: dict) -> str:
    payload = {
        "case_id": case["case_id"],
        "revision": case["revision"],
        "profile_sha256": case["profile"]["sha256"],
        "task_sha256": case["task"]["sha256"],
        "grammar_sha256": case["grammar"]["sha256"],
    }
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
    if task.get("schema_version") != "machine-overview-task/v1":
        raise MachineOverviewError("TASK_SCHEMA_INVALID")
    if grammar.get("schema_version") != "machine-overview-grammar/v1":
        raise MachineOverviewError("GRAMMAR_SCHEMA_INVALID")
    profile_report = inspect_profile(repo_root, profile_path, fast=True)
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

    profile = read_json(profile_path)
    case = {
        "schema_version": "machine-overview-case/v1",
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
        ],
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
            "research_relation": "calibration",
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


def _kernel_artifact_errors(run_id: str, run_dir: Path, run: dict) -> list[str]:
    errors: list[str] = []
    for kernel in run.get("kernel_runs", []):
        label = kernel.get("label", "?")
        kernel_dir = run_dir / "kernel" / str(label)
        for name, key in (("stdout.txt", "stdout"), ("stderr.txt", "stderr")):
            path = kernel_dir / name
            if not path.is_file():
                errors.append(f"KERNEL_ARTIFACT_MISSING:{run_id}:{label}:{name}")
                continue
            data = path.read_bytes()
            if kernel.get(f"{key}_bytes") != len(data) or kernel.get(f"{key}_sha256") != sha256_bytes(data):
                errors.append(f"KERNEL_ARTIFACT_HASH_MISMATCH:{run_id}:{label}:{name}")
        for required in ("command.json", "environment.txt"):
            if not (kernel_dir / required).is_file():
                errors.append(f"KERNEL_ARTIFACT_MISSING:{run_id}:{label}:{required}")
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
    inputs = run.get("inputs", {})
    if inputs.get("case_sha256") != sha256_file(case_file):
        errors.append(f"SEARCH_CASE_HASH_MISMATCH:{run_id}")
    for key in ("task", "grammar"):
        if inputs.get(f"{key}_sha256") != case[key]["sha256"]:
            errors.append(f"SEARCH_INPUT_HASH_MISMATCH:{run_id}:{key}")
    grammar = read_json(repo_root / safe_relative(case["grammar"]["path"]))
    for witness in run.get("witnesses", []):
        if witness.get("ast_sha256") != witness_ast_sha256(witness):
            errors.append(f"WITNESS_AST_HASH_MISMATCH:{run_id}:{witness.get('witness_id')}")
        left = (witness["pair"]["left"]["kind"],) if witness["pair"]["left"]["kind"] == "omega" else (
            "ret", witness["pair"]["left"]["n"], witness["pair"]["left"]["value"])
        right = (witness["pair"]["right"]["kind"],) if witness["pair"]["right"]["kind"] == "omega" else (
            "ret", witness["pair"]["right"]["n"], witness["pair"]["right"]["value"])
        inside, reason = within_grammar_witness(witness["ops"], left, right, grammar)
        if not inside:
            errors.append(f"WITNESS_OUTSIDE_DECLARED_GRAMMAR:{run_id}:{witness.get('witness_id')}:{reason}")
    statistics = run.get("statistics", {})
    if statistics.get("complete_within_declared_grammar") and statistics.get("truncated"):
        errors.append(f"SEARCH_COMPLETENESS_CONTRADICTION:{run_id}")
    if statistics.get("complete_within_declared_grammar") and statistics.get("witness_capture_truncated"):
        errors.append(f"SEARCH_COMPLETENESS_CONTRADICTION:{run_id}:capture")


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
    binding = run.get("source_search_run", {})
    search_run_id = binding.get("run_id")
    if not search_run_id or search_run_id not in runs:
        errors.append(f"VERIFY_UNKNOWN_SEARCH_RUN:{run_id}")
        return
    search_run, search_run_dir = runs[search_run_id]
    if (search_run.get("case_id"), int(search_run.get("case_revision", -1))) != (
            case["case_id"], int(case["revision"])):
        errors.append(f"VERIFY_SEARCH_CASE_MISMATCH:{run_id}")
    if binding.get("sha256") != sha256_file(search_run_dir / "RUN.json"):
        errors.append(f"VERIFY_SEARCH_RUN_HASH_MISMATCH:{run_id}")
    witnesses = {w["witness_id"]: w for w in search_run.get("witnesses", [])}
    witness = witnesses.get(run.get("witness_id"))
    if witness is None:
        errors.append(f"VERIFY_WITNESS_NOT_IN_SEARCH_RUN:{run_id}")
    elif run.get("candidate_ast_sha256") != witness.get("ast_sha256"):
        errors.append(f"VERIFY_CANDIDATE_AST_HASH_MISMATCH:{run_id}")
    if run.get("case_sha256") != sha256_file(case_file):
        errors.append(f"VERIFY_CASE_HASH_MISMATCH:{run_id}")
    if run.get("case_identity_sha256") != case_identity_sha256(case):
        errors.append(f"VERIFY_CASE_IDENTITY_MISMATCH:{run_id}")

    generated = run.get("generated_sources", {})
    for name, row in generated.items():
        path = run_dir / "generated" / name
        if not path.is_file():
            errors.append(f"GENERATED_SOURCE_MISSING:{run_id}:{name}")
        elif sha256_bytes(path.read_bytes()) != row.get("sha256"):
            errors.append(f"GENERATED_SOURCE_MISMATCH:{run_id}:{name}")
    target_path = run_dir / "generated" / "Target.agda"
    if target_path.is_file() and sha256_bytes(target_path.read_bytes()) != run.get("target_text_hash"):
        errors.append(f"TARGET_HASH_MISMATCH:{run_id}")
    ledger_path = repo_root / "machine-overview" / "cases" / case["case_id"] / f"target-freeze-{case['revision']}.json"
    if ledger_path.is_file():
        ledger = read_json(ledger_path)
        entry = ledger.get("entries", {}).get(run.get("candidate_ast_sha256", ""))
        if entry is None:
            errors.append(f"TARGET_FREEZE_ENTRY_MISSING:{run_id}")
        elif entry.get("target_text_hash") != run.get("target_text_hash"):
            errors.append(f"TARGET_FREEZE_MISMATCH:{run_id}")

    errors.extend(_kernel_artifact_errors(run_id, run_dir, run))

    status = run.get("status")
    kernels = {item.get("label"): item for item in run.get("kernel_runs", [])}
    if status in ("NATIVE_CHECKED_CALIBRATION_INSTANCE", "NATIVE_CHECKED_WITH_REPLAY_MISMATCH"):
        for label in ("verify", "controls", "negative-control"):
            if kernels.get(label, {}).get("expectation_met") is not True:
                errors.append(f"VERIFY_STATUS_CONTRADICTION:{run_id}:{label}")
    elif status in ("NATIVE_CHECK_FAILED", "VERIFY_INFRASTRUCTURE_ERROR"):
        if all(item.get("expectation_met") is True for item in kernels.values()):
            errors.append(f"VERIFY_STATUS_CONTRADICTION:{run_id}:no_failure_recorded")
    else:
        errors.append(f"VERIFY_STATUS_UNKNOWN:{run_id}:{status}")


def validate_workspace(repo_root: Path) -> dict:
    root = repo_root / "machine-overview"
    errors: list[str] = []
    cases: dict[tuple[str, int], dict] = {}
    case_paths: dict[tuple[str, int], Path] = {}
    for case_file in sorted((root / "cases").glob("*/case-revision-*.json")):
        case = read_json(case_file)
        key = (case["case_id"], int(case["revision"]))
        cases[key] = case
        case_paths[key] = case_file
        for name in ("profile", "task", "grammar"):
            pinned = case[name]
            path = repo_root / safe_relative(pinned["path"])
            if not path.is_file():
                errors.append(f"CASE_REFERENCE_MISSING:{case_file}:{name}")
            elif sha256_file(path) != pinned["sha256"]:
                errors.append(f"CASE_REFERENCE_HASH_MISMATCH:{case_file}:{name}")
        profile_path = repo_root / safe_relative(case["profile"]["path"])
        if profile_path.is_file():
            profile = read_json(profile_path)
            for source in list(profile.get("sources", [])) + list(profile.get("support_sources", [])):
                path = repo_root / safe_relative(source["path"])
                if not path.is_file():
                    errors.append(f"PROFILE_SOURCE_MISSING:{case_file}:{source['path']}")
                elif source.get("sha256") and sha256_file(path) != source["sha256"]:
                    errors.append(f"PROFILE_SOURCE_HASH_MISMATCH:{case_file}:{source['path']}")

    runs: dict[str, tuple[dict, Path]] = {}
    interrupted_attempts: list[dict] = []
    legacy_runs: list[dict] = []
    for run_dir in sorted(path for path in (root / "runs").glob("*") if path.is_dir() and not path.name.startswith(".")):
        run_file = run_dir / "RUN.json"
        attempt_file = run_dir / "ATTEMPT.json"
        if not run_file.is_file():
            if attempt_file.is_file():
                attempt = read_json(attempt_file)
                status = attempt.get("status")
                if status == "RUNNING":
                    errors.append(f"RUN_ATTEMPT_STILL_RUNNING:{run_dir.name}")
                elif status in ("INTERRUPTED", "FAILED"):
                    interrupted_attempts.append({
                        "run_id": run_dir.name,
                        "status": status,
                        "error": attempt.get("error"),
                        "attempt": attempt.get("attempt"),
                    })
                else:
                    errors.append(f"RUN_ATTEMPT_STATUS_INVALID:{run_dir.name}:{status}")
            else:
                errors.append(f"RUN_DIRECTORY_WITHOUT_RECEIPT:{run_dir.name}")
            continue
        run = read_json(run_file)
        runs[run["run_id"]] = (run, run_dir)
        if (run_dir / "LEGACY.json").is_file():
            marker = read_json(run_dir / "LEGACY.json")
            legacy_runs.append({"run_id": run["run_id"], "kind": run.get("kind"),
                                "reason": marker.get("reason"), "attested_by": marker.get("attested_by")})

    for run_id, (run, run_dir) in runs.items():
        key = (run.get("case_id"), int(run.get("case_revision", -1)))
        if key not in cases:
            errors.append(f"RUN_REFERENCES_UNKNOWN_CASE_REVISION:{run_id}")
            continue
        if (run_dir / "LEGACY.json").is_file():
            _validate_legacy_run(run_id, run, run_dir, cases[key], case_paths[key], errors)
        elif run.get("kind") == "search":
            _validate_search_run(run_id, run, run_dir, cases[key], case_paths[key], repo_root, errors)
        elif run.get("kind") == "verify":
            _validate_verify_run(run_id, run, run_dir, cases[key], case_paths[key], repo_root, runs, errors)
        else:
            errors.append(f"RUN_KIND_UNKNOWN:{run_id}")

    reviews = 0
    for review_file in sorted((root / "reviews").glob("*.json")):
        review = read_json(review_file)
        reviews += 1
        binding = review.get("source_search_run", {})
        search_run_id = binding.get("run_id")
        if not search_run_id or search_run_id not in runs:
            errors.append(f"REVIEW_UNKNOWN_SEARCH_RUN:{review_file.name}")
            continue
        search_run = runs[search_run_id][0]
        witnesses = {w["witness_id"]: w for w in search_run.get("witnesses", [])}
        witness = witnesses.get(review.get("witness_id"))
        if witness is None:
            errors.append(f"REVIEW_WITNESS_NOT_IN_SEARCH_RUN:{review_file.name}")
        elif review.get("candidate_ast_sha256") != witness.get("ast_sha256"):
            errors.append(f"REVIEW_CANDIDATE_AST_HASH_MISMATCH:{review_file.name}")
        if review.get("case_revision") != search_run.get("case_revision"):
            errors.append(f"REVIEW_CASE_REVISION_MISMATCH:{review_file.name}")

    return {
        "schema_version": "machine-overview-validation/v1",
        "cases": len(cases),
        "runs": len(runs),
        "reviews": reviews,
        "interrupted_attempts": interrupted_attempts,
        "legacy_runs": legacy_runs,
        "errors": errors,
        "status": "VALID" if not errors else "INVALID",
    }
