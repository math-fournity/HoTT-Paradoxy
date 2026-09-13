"""Case revisions: the immutable identity of a task/grammar/profile bundle."""
from __future__ import annotations

from pathlib import Path

from .profile import inspect_profile
from .util import (
    MachineOverviewError,
    read_json,
    safe_relative,
    sha256_file,
    utc_now,
    write_json,
)


def _rel(repo_root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError as exc:
        raise MachineOverviewError(f"PATH_OUTSIDE_REPO:{path}") from exc


def resolve_path(repo_root: Path, value: str) -> Path:
    candidate = Path(value)
    return candidate if candidate.is_absolute() else (repo_root / candidate)


def load_case(repo_root: Path, value: str) -> tuple[dict, Path]:
    path = resolve_path(repo_root, value)
    if path.is_dir():
        revisions = sorted(
            path.glob("case-revision-*.json"),
            key=lambda item: int(item.stem.rsplit("-", 1)[1]),
        )
        if not revisions:
            raise MachineOverviewError(f"CASE_REVISION_NOT_FOUND:{path}")
        path = revisions[-1]
    case = read_json(path)
    if case.get("schema_version") != "machine-overview-case/v1":
        raise MachineOverviewError("CASE_SCHEMA_INVALID")
    return case, path


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

    resolved_id = case_id or task["task_id"]
    case_dir = repo_root / "machine-overview" / "cases" / resolved_id
    case_path = case_dir / f"case-revision-{revision}.json"
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

    case = {
        "schema_version": "machine-overview-case/v1",
        "case_id": resolved_id,
        "revision": revision,
        "parent_revision": parent_revision,
        "created_at_utc": utc_now(),
        "profile": {"path": _rel(repo_root, profile_path), "sha256": sha256_file(profile_path)},
        "task": {"path": _rel(repo_root, task_path), "sha256": sha256_file(task_path)},
        "grammar": {"path": _rel(repo_root, grammar_path), "sha256": sha256_file(grammar_path)},
        "source_pins": [
            {"path": source["path"], "sha256": source.get("sha256")}
            for source in read_json(profile_path).get("sources", [])
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


def validate_workspace(repo_root: Path) -> dict:
    root = repo_root / "machine-overview"
    errors: list[str] = []
    cases: dict[tuple[str, int], dict] = {}
    for case_file in sorted((root / "cases").glob("*/case-revision-*.json")):
        case = read_json(case_file)
        cases[(case["case_id"], int(case["revision"]))] = case
        for key in ("profile", "task", "grammar"):
            pinned = case[key]
            path = repo_root / safe_relative(pinned["path"])
            if not path.is_file():
                errors.append(f"CASE_REFERENCE_MISSING:{case_file}:{key}")
            elif sha256_file(path) != pinned["sha256"]:
                errors.append(f"CASE_REFERENCE_HASH_MISMATCH:{case_file}:{key}")
    runs = 0
    for run_file in sorted((root / "runs").glob("*/RUN.json")):
        run = read_json(run_file)
        runs += 1
        key = (run.get("case_id"), int(run.get("case_revision", -1)))
        if key not in cases:
            errors.append(f"RUN_REFERENCES_UNKNOWN_CASE_REVISION:{run_file}")
            continue
        case = cases[key]
        if run.get("kind") == "search":
            for name, key in (("grammar", "grammar"), ("task", "task")):
                if run["inputs"][f"{name}_sha256"] != case[key]["sha256"]:
                    errors.append(f"RUN_INPUT_HASH_MISMATCH:{run_file}:{name}")
        if run.get("kind") == "verify":
            for name, row in run.get("generated_sources", {}).items():
                path = run_file.parent / "generated" / name
                if not path.is_file() or sha256_file(path) != row["sha256"]:
                    errors.append(f"GENERATED_SOURCE_MISMATCH:{run_file}:{name}")
    return {
        "schema_version": "machine-overview-validation/v1",
        "cases": len(cases),
        "runs": runs,
        "errors": errors,
        "status": "VALID" if not errors else "INVALID",
    }
