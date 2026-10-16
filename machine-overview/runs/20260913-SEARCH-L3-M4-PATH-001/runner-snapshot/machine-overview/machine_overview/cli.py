"""Command line interface of the machine-overview coordinator."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import __version__
from .case import (
    case_identity_sha256,
    create_case,
    load_case,
    load_case_inputs,
    resolve_path,
    validate_identifier,
    validate_workspace,
)
from .correspondence import review_correspondence
from .index import get as index_get
from .index import load_index, rebuild_index
from .profile import inspect_profile
from .report import bound_to_search, explain_case
from .search import run_search, witness_ast_sha256
from .util import MachineOverviewError, capture_runner_snapshot, find_repo_root, read_json, sha256_file, write_json
from .verify import assert_witness_binding, begin_attempt, finish_attempt, verify_witness


def _machine_root(repo_root: Path) -> Path:
    return repo_root / "machine-overview"


def _registry(repo_root: Path) -> dict:
    return read_json(_machine_root(repo_root) / "registry.json")


def _toolchain(repo_root: Path, profile_report: dict) -> dict:
    return read_json(repo_root / profile_report["toolchain_ref"])


def _print(value: object, as_json: bool) -> None:
    if as_json:
        print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))


def _case_context(repo_root: Path, args: argparse.Namespace, *, verify_profile: bool) -> tuple[dict, Path, dict]:
    case, case_path = load_case(repo_root, args.case, getattr(args, "revision", None))
    inputs = load_case_inputs(repo_root, case, verify_profile=verify_profile)
    return case, case_path, inputs


def _search_context(repo_root: Path, args: argparse.Namespace) -> tuple[dict, Path, dict, dict, Path]:
    validate_identifier(args.search_run, "search_run")
    search_path = _machine_root(repo_root) / "runs" / args.search_run / "RUN.json"
    if not search_path.is_file():
        raise MachineOverviewError(f"SEARCH_RUN_NOT_FOUND:{args.search_run}")
    search_run = read_json(search_path)
    return search_run, search_path


def _witness(search_run: dict, witness_id: str | None) -> dict:
    witnesses = search_run["witnesses"]
    if not witnesses:
        raise MachineOverviewError("SEARCH_RUN_HAS_NO_WITNESS")
    if witness_id is None:
        return witnesses[0]
    validate_identifier(witness_id, "witness_id")
    for item in witnesses:
        if item["witness_id"] == witness_id:
            return item
    raise MachineOverviewError(f"WITNESS_NOT_FOUND:{witness_id}")


def cmd_inspect_profile(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    report = inspect_profile(repo_root, resolve_path(repo_root, args.profile), fast=args.fast)
    _print(report, args.json)
    return 0 if report["status"] == "PROFILE_QUALIFIED" else 1


def cmd_create_case(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    case, path = create_case(
        repo_root,
        profile_path=resolve_path(repo_root, args.profile),
        task_path=resolve_path(repo_root, args.task),
        grammar_path=resolve_path(repo_root, args.grammar),
        case_id=args.case_id,
        revision=args.revision,
    )
    _print({"status": "CASE_READY", "case_id": case["case_id"], "revision": case["revision"],
            "path": str(path), "claim_refs": case["claim_refs"]}, args.json)
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    validate_identifier(args.run_id, "run_id")
    case, case_path, inputs = _case_context(repo_root, args, verify_profile=True)
    grammar = inputs["grammar"]["data"]
    limits = {"max_witnesses": args.max_witnesses, "max_checks": args.max_checks, "max_contexts": args.max_contexts}
    run_dir = _machine_root(repo_root) / "runs" / args.run_id
    _, attempt = begin_attempt(run_dir, run_id=args.run_id, case=case, planned=["search"])
    try:
        runner_binding = capture_runner_snapshot(repo_root, run_dir)
        receipt = run_search(
            repo_root,
            run_id=args.run_id,
            case_path=case_path,
            case=case,
            grammar=grammar,
            profile_report=inputs["profile_report"],
            registry=_registry(repo_root),
            limits=limits,
            order_seed=args.seed,
            run_dir=run_dir,
            case_inputs=inputs,
            runner_binding=runner_binding,
            attempt=attempt,
        )
    except BaseException as exc:  # noqa: BLE001
        finish_attempt(run_dir, attempt, "INTERRUPTED", error=f"{type(exc).__name__}: {exc}")
        raise
    finish_attempt(run_dir, attempt, "COMPLETED")
    rebuild_index(repo_root, _machine_root(repo_root))
    _print({
        "status": receipt["exit_reason"],
        "run_id": receipt["run_id"],
        "case_revision": receipt["case_revision"],
        "witnesses": len(receipt["witnesses"]),
        "complete_within_declared_grammar": receipt["statistics"]["complete_within_declared_grammar"],
        "checks": receipt["statistics"].get(
            "pair_context_checks", receipt["statistics"].get("rule_application_checks")
        ),
        "calibration_match": receipt["calibration_match"].get("status"),
        "first_witness": receipt["witnesses"][0]["witness_id"] if receipt["witnesses"] else None,
    }, args.json)
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    case, case_path, inputs = _case_context(repo_root, args, verify_profile=False)
    search_run, search_path = _search_context(repo_root, args)
    witness = _witness(search_run, args.witness)
    grammar = inputs["grammar"]["data"]
    binding = assert_witness_binding(
        case=case, search_run=search_run, search_run_path=search_path, witness=witness, grammar=grammar,
    )
    profile_report = inspect_profile(repo_root, repo_root / case["profile"]["path"], fast=False)
    if profile_report["status"] != "PROFILE_QUALIFIED":
        raise MachineOverviewError(f"PROFILE_NOT_QUALIFIED:{profile_report['failures']}")
    proof_text = None
    origin = "coordinator_template"
    if args.proof_file:
        proof_text = resolve_path(repo_root, args.proof_file).read_text(encoding="utf-8")
        origin = "external_file"
    receipt = verify_witness(
        repo_root,
        run_id=args.run_id,
        case_path=case_path,
        case=case,
        witness=witness,
        profile_report=profile_report,
        toolchain=_toolchain(repo_root, profile_report),
        registry=_registry(repo_root),
        run_dir=_machine_root(repo_root) / "runs" / args.run_id,
        proof_origin=origin,
        proof_text=proof_text,
        replay=not args.no_replay,
        timeout_seconds=args.timeout_seconds,
        source_search_run=search_run,
        search_run_path=search_path,
        grammar=grammar,
    )
    rebuild_index(repo_root, _machine_root(repo_root))
    _print({
        "status": receipt["status"],
        "run_id": receipt["run_id"],
        "case_revision": receipt["case_revision"],
        "witness": receipt["witness_id"],
        "candidate_ast_sha256": receipt["candidate_ast_sha256"],
        "source_search_run": receipt["source_search_run"]["run_id"] if binding else None,
        "target_text_hash": receipt["target_text_hash"],
        "replay": receipt.get("replay"),
        "kernel": [
            {"label": item["label"], "exit_code": item["exit_code"], "status": item["status"],
             "expectation_met": item["expectation_met"], "diagnostic": item.get("diagnostic")}
            for item in receipt["kernel_runs"]
        ],
    }, args.json)
    return 0 if receipt["status"] in (
        "NATIVE_CHECKED_CALIBRATION_INSTANCE", "NATIVE_CHECKED_EXPLORATION_CANDIDATE",
    ) else 1


def cmd_review_correspondence(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    case, case_path, inputs = _case_context(repo_root, args, verify_profile=False)
    search_run, search_path = _search_context(repo_root, args)
    witness = _witness(search_run, args.witness)
    grammar = inputs["grammar"]["data"]
    assert_witness_binding(case=case, search_run=search_run, search_run_path=search_path, witness=witness, grammar=grammar)
    profile_report = inspect_profile(repo_root, repo_root / case["profile"]["path"], fast=False)
    if profile_report["status"] != "PROFILE_QUALIFIED":
        raise MachineOverviewError(f"PROFILE_NOT_QUALIFIED:{profile_report['failures']}")
    task = inputs["task"]["data"]
    ast = witness_ast_sha256(witness)
    review_id = f"RV-{case['case_id']}-r{case['revision']}-{search_run['run_id']}-{witness['witness_id']}-{ast[:8]}"
    output = _machine_root(repo_root) / "reviews" / f"{review_id}.json"
    review = review_correspondence(
        repo_root,
        review_id=review_id,
        case=case,
        case_path=case_path,
        task=task,
        witness=witness,
        profile_report=profile_report,
        grammar=grammar,
        search_run=search_run,
        search_run_path=search_path,
        output_path=output,
    )
    rebuild_index(repo_root, _machine_root(repo_root))
    _print({"status": "REVIEW_WRITTEN", "review_id": review_id, "path": str(output),
            "conclusion": review["conclusion"]}, args.json)
    return 0


def cmd_explain(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    case, case_path, inputs = _case_context(repo_root, args, verify_profile=False)
    validation = validate_workspace(repo_root)
    if validation["status"] != "VALID":
        raise MachineOverviewError(f"EVIDENCE_VALIDATION_FAILED:{validation['errors'][:5]}")
    runs_root = _machine_root(repo_root) / "runs"
    search_path = runs_root / args.search_run / "RUN.json" if args.search_run else None
    if args.search_run:
        validate_identifier(args.search_run, "search_run")
    if search_path is None or not search_path.is_file():
        search_path = None
        for candidate in reversed(sorted(runs_root.glob("*/RUN.json"))):
            run = read_json(candidate)
            if run.get("kind") == "search" and run.get("case_id") == case["case_id"] and int(run.get("case_revision", -1)) == int(case["revision"]):
                search_path = candidate
                break
        if search_path is None:
            raise MachineOverviewError("NO_SEARCH_RUN_FOR_CASE_REVISION")
    search_run = read_json(search_path)
    if (search_run.get("kind") != "search" or search_run.get("case_id") != case["case_id"]
            or int(search_run.get("case_revision", -1)) != int(case["revision"])):
        raise MachineOverviewError("SEARCH_RUN_DOES_NOT_BELONG_TO_CASE_REVISION")
    verify_runs: list[tuple[dict, Path]] = []
    for candidate in sorted(runs_root.glob("*/RUN.json")):
        run = read_json(candidate)
        if (run.get("kind") == "verify" and run.get("case_id") == case["case_id"]
                and int(run.get("case_revision", -1)) == int(case["revision"])
                and bound_to_search(run, search_run, search_path)):
            verify_runs.append((run, candidate))
    reviews: list[tuple[dict, Path]] = []
    for candidate in sorted((_machine_root(repo_root) / "reviews").glob("*.json")):
        data = read_json(candidate)
        if (data.get("case_id") == case["case_id"]
                and int(data.get("case_revision", -1)) == int(case["revision"])
                and bound_to_search(data, search_run, search_path)):
            reviews.append((data, candidate))
    output = resolve_path(repo_root, args.out) if args.out else (
        _machine_root(repo_root) / "reports" / f"{case['case_id']}-r{case['revision']}-report.md"
    )
    explain_case(
        repo_root,
        case=case,
        case_path=case_path,
        search_run=search_run,
        search_run_path=search_path,
        verify_runs=verify_runs,
        reviews=reviews,
        output_path=output,
    )
    rebuild_index(repo_root, _machine_root(repo_root))
    _print({"status": "REPORT_WRITTEN", "path": str(output), "verify_runs": [item[0]["run_id"] for item in verify_runs]},
           args.json)
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    index = load_index(repo_root, _machine_root(repo_root))
    entries = index["entries"]
    if args.kind:
        entries = [entry for entry in entries if entry["kind"] == args.kind]
    if args.json:
        _print(entries, True)
    else:
        for entry in entries:
            revision = entry.get("revision", entry.get("case_revision", ""))
            print(f"{entry['kind']:<8} {str(entry.get('id')):<50} rev={str(revision):<4} {entry['path']}")
    return 0


def cmd_get(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    entries = index_get(_machine_root(repo_root), args.id, revision=args.revision)
    _print(entries, args.json)
    return 0 if entries else 1


def cmd_query(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    index = load_index(repo_root, _machine_root(repo_root))
    entries = index["entries"]
    if args.kind:
        entries = [entry for entry in entries if entry["kind"] == args.kind]
    lowered = args.text.lower()
    entries = [entry for entry in entries
               if lowered in str(entry.get("id", "")).lower()
               or lowered in entry["path"].lower()
               or lowered in str(entry.get("case_id", "")).lower()]
    _print(entries, args.json)
    return 0


def cmd_rebuild_index(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    index = rebuild_index(repo_root, _machine_root(repo_root))
    _print({"status": "INDEX_REBUILT", "entries": len(index["entries"])}, args.json)
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    repo_root = find_repo_root()
    report = validate_workspace(repo_root)
    _print(report, args.json)
    return 0 if report["status"] == "VALID" else 1


def cmd_selftest(args: argparse.Namespace) -> int:
    import unittest

    repo_root = find_repo_root()
    tests_dir = _machine_root(repo_root) / "tests"
    suite = unittest.defaultTestLoader.discover(str(tests_dir), pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    return 0 if result.wasSuccessful() else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="machine-overview", description=__doc__)
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("inspect-profile", help="qualify a profile's pinned toolchain and sources")
    p.add_argument("--profile", required=True)
    p.add_argument("--fast", action="store_true", help="skip the Cubical source-tree hash")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_inspect_profile)

    p = sub.add_parser("create-case", help="freeze a profile/task/grammar bundle as a case revision")
    p.add_argument("--profile", required=True)
    p.add_argument("--task", required=True)
    p.add_argument("--grammar", required=True)
    p.add_argument("--case-id")
    p.add_argument("--revision", type=int, default=1)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_create_case)

    p = sub.add_parser("search", help="enumerate the declared grammar and reduce candidates")
    p.add_argument("--case", required=True)
    p.add_argument("--revision", type=int)
    p.add_argument("--run-id", required=True)
    p.add_argument("--max-witnesses", type=int, default=20000)
    p.add_argument("--max-checks", type=int, default=5000000)
    p.add_argument("--max-contexts", type=int, default=200000)
    p.add_argument("--seed", type=int, default=20260913)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("verify", help="generate the bound statement and run the native kernel")
    p.add_argument("--case", required=True)
    p.add_argument("--revision", type=int)
    p.add_argument("--search-run", required=True)
    p.add_argument("--witness")
    p.add_argument("--run-id", required=True)
    p.add_argument("--proof-file", help="candidate-supplied proof source (external_file path)")
    p.add_argument("--no-replay", action="store_true")
    p.add_argument("--timeout-seconds", type=int, default=900)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_verify)

    p = sub.add_parser("review-correspondence", help="write the structure-derived correspondence review")
    p.add_argument("--case", required=True)
    p.add_argument("--revision", type=int)
    p.add_argument("--search-run", required=True)
    p.add_argument("--witness")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_review_correspondence)

    p = sub.add_parser("explain", help="render the calibration report from validated receipts")
    p.add_argument("--case", required=True)
    p.add_argument("--revision", type=int)
    p.add_argument("--search-run")
    p.add_argument("--out")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_explain)

    p = sub.add_parser("list", help="list cases, runs, reviews and reports (read-only)")
    p.add_argument("--kind", choices=["case", "search", "verify", "review", "report"])
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("get", help="show indexed artifacts by id (all revisions)")
    p.add_argument("id")
    p.add_argument("--revision", type=int)
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_get)

    p = sub.add_parser("query", help="filter indexed artifacts by text (read-only)")
    p.add_argument("text")
    p.add_argument("--kind", choices=["case", "search", "verify", "review", "report"])
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_query)

    p = sub.add_parser("rebuild-index", help="rebuild the derived query projection")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_rebuild_index)

    p = sub.add_parser("validate", help="re-derive validity from cases, runs and kernel evidence")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_validate)

    p = sub.add_parser("selftest", help="run the coordinator unit and regression tests")
    p.set_defaults(func=cmd_selftest)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except MachineOverviewError as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
