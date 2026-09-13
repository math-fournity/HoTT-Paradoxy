"""Regression tests for the seven findings of the external M1 audit (F1-F7)."""
from __future__ import annotations

import copy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

from machine_overview.case import (  # noqa: E402
    _validate_search_run,
    _validate_verify_run,
    case_identity_sha256,
    load_case_inputs,
    validate_identifier,
    validate_workspace,
)
from machine_overview.correspondence import (  # noqa: E402
    derive_correspondence_content,
    mechanism_facts,
    review_correspondence,
)
from machine_overview.model import value_from_json  # noqa: E402
from machine_overview.profile import inspect_profile, qualification_verdict  # noqa: E402
from machine_overview.report import bound_to_search  # noqa: E402
from machine_overview.search import (  # noqa: E402
    compute_search_semantics,
    derive_witness_record,
    run_search,
    within_grammar_witness,
)
from machine_overview.util import MachineOverviewError, find_repo_root, read_json, sha256_file  # noqa: E402
from machine_overview.verify import (  # noqa: E402
    assert_witness_binding,
    classify_replay,
    diagnose_rejection,
    prepare_run_dir,
    render_target,
    run_kernel,
)

REPO = find_repo_root()
MODEL = "HoTT/formal/partiality-race-timeout"


def _git_init(root: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    subprocess.run(["git", "-c", "user.email=a@b", "-c", "user.name=a", "commit", "-q", "--allow-empty", "-m", "init"],
                   cwd=root, check=True)


def _copy_model(root: Path) -> None:
    (root / MODEL).mkdir(parents=True, exist_ok=True)
    for name in ("PartialityRaceTimeout.agda", "TOOLCHAIN.json", "AGDA_LIBRARIES"):
        shutil.copy2(REPO / MODEL / name, root / MODEL / name)


def _copy_system(root: Path) -> None:
    shutil.copytree(
        REPO / "machine-overview", root / "machine-overview",
        ignore=shutil.ignore_patterns("runs", "reviews", "reports", "cases", "__pycache__", ".gitignore", "tests"),
    )
    (root / "machine-overview/cases").mkdir(exist_ok=True)


def _load_search_run(run_id: str) -> dict:
    return read_json(REPO / "machine-overview" / "runs" / run_id / "RUN.json")


def _load_case(revision: int) -> tuple[dict, Path]:
    path = REPO / "machine-overview" / "cases" / "MS-TASK-L1-RACE-COMPLETION-001" / f"case-revision-{revision}.json"
    return read_json(path), path


class F1SourcePinTest(unittest.TestCase):
    def test_source_hash_mismatch_fails_qualification(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-f1-") as tmp:
            root = Path(tmp)
            _copy_model(root)
            with (root / MODEL / "PartialityRaceTimeout.agda").open("a") as handle:
                handle.write("\n-- audit tamper\n")
            (root / "machine-overview/profiles").mkdir(parents=True)
            shutil.copy2(REPO / "machine-overview/profiles/l1-partiality-v0.json",
                         root / "machine-overview/profiles/l1-partiality-v0.json")
            report = inspect_profile(root, root / "machine-overview/profiles/l1-partiality-v0.json", fast=True)
            self.assertEqual(report["status"], "PROFILE_NOT_QUALIFIED")
            self.assertTrue(any("source:" in failure for failure in report["failures"]))

    def test_verdict_includes_source_failures(self) -> None:
        status, failures = qualification_verdict([], [{"path": "x", "status": "FAIL"}])
        self.assertEqual(status, "PROFILE_NOT_QUALIFIED")
        self.assertEqual(failures, ["source:x"])


class F2BindingTest(unittest.TestCase):
    def test_case_input_hash_mismatch_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-f2a-") as tmp:
            root = Path(tmp)
            _git_init(root)
            _copy_model(root)
            _copy_system(root)
            from machine_overview.case import create_case

            case, _ = create_case(
                root,
                profile_path=root / "machine-overview/profiles/l1-partiality-v2.json",
                task_path=root / "machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-002.json",
                grammar_path=root / "machine-overview/grammars/l1-v2.json",
                revision=1,
            )
            grammar_path = root / case["grammar"]["path"]
            modified = read_json(grammar_path)
            modified["context_depth_max"] = 1
            grammar_path.write_text(json.dumps(modified, ensure_ascii=False, indent=2) + "\n")
            with self.assertRaises(MachineOverviewError) as ctx:
                load_case_inputs(root, case, verify_profile=False)
            self.assertEqual(str(ctx.exception), "CASE_INPUT_HASH_MISMATCH:grammar")

    def test_cross_revision_witness_is_rejected(self) -> None:
        case, _ = _load_case(2)
        other_case = dict(case)
        other_case["revision"] = 3
        search = _load_search_run("20260913-SEARCH-L1-002")
        witness = search["witnesses"][0]
        grammar = read_json(REPO / "machine-overview/grammars/l1-v1.json")
        with self.assertRaises(MachineOverviewError) as ctx:
            assert_witness_binding(
                case=other_case,
                search_run=search,
                search_run_path=REPO / "machine-overview/runs/20260913-SEARCH-L1-002/RUN.json",
                witness=witness,
                grammar=grammar,
            )
        self.assertEqual(str(ctx.exception), "WITNESS_FROM_DIFFERENT_CASE_REVISION")

    def test_witness_outside_grammar_is_rejected(self) -> None:
        case, _ = _load_case(2)
        search = _load_search_run("20260913-SEARCH-L1-002")
        witness = next(w for w in search["witnesses"] if w["observation_mode"] == "deadline")
        sparse = read_json(REPO / "machine-overview/grammars/l1-v1.json")
        sparse["deadline_horizons"] = [2]
        with self.assertRaises(MachineOverviewError) as ctx:
            assert_witness_binding(
                case=case,
                search_run=search,
                search_run_path=REPO / "machine-overview/runs/20260913-SEARCH-L1-002/RUN.json",
                witness=witness,
                grammar=sparse,
            )
        self.assertTrue(str(ctx.exception).startswith("WITNESS_OUTSIDE_DECLARED_GRAMMAR"))


class F3ValidationTest(unittest.TestCase):
    def test_missing_kernel_output_is_invalid(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-f3-") as tmp:
            root = Path(tmp)
            (root / MODEL).mkdir(parents=True)
            for name in ("PartialityRaceTimeout.agda", "TOOLCHAIN.json", "AGDA_LIBRARIES"):
                shutil.copy2(REPO / MODEL / name, root / MODEL / name)
            for sub in ("profiles", "tasks", "grammars", "cases", "reviews", "generated-index"):
                shutil.copytree(REPO / "machine-overview" / sub, root / "machine-overview" / sub)
            shutil.copytree(REPO / "machine-overview/runs", root / "machine-overview/runs",
                            ignore=shutil.ignore_patterns("*.agdai"))
            (root / "machine-overview/runs/20260913-VERIFY-L1-DEADLINE-001/kernel/verify/stdout.txt").unlink()
            report = validate_workspace(root)
            self.assertEqual(report["status"], "INVALID")
            self.assertTrue(any("KERNEL_ARTIFACT_MISSING" in error for error in report["errors"]))


class F4CorrespondenceTest(unittest.TestCase):
    def _review(self, witness_id: str, output: Path) -> dict:
        legacy_case, _ = _load_case(2)
        case = copy.deepcopy(legacy_case)
        case["schema_version"] = "machine-overview-case/v2"
        case_path = output.parent / "case.json"
        case_path.write_text(json.dumps(case, ensure_ascii=False, sort_keys=True) + "\n")
        source_search_path = REPO / "machine-overview/runs/20260913-SEARCH-L1-002/RUN.json"
        search = copy.deepcopy(read_json(source_search_path))
        grammar = read_json(REPO / "machine-overview/grammars/l1-v1.json")
        witness = derive_witness_record(
            next(w for w in search["witnesses"] if w["witness_id"] == witness_id), grammar
        )
        search["witnesses"] = [
            witness if row["witness_id"] == witness_id else row for row in search["witnesses"]
        ]
        task = copy.deepcopy(read_json(REPO / "machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-002.json"))
        search["schema_version"] = "machine-overview-search-run/v2"
        search["case_identity_sha256"] = case_identity_sha256(case)
        search.setdefault("inputs", {})["case_sha256"] = sha256_file(case_path)
        search["inputs"]["profile_sha256"] = case["profile"]["sha256"]
        search["inputs"]["task_sha256"] = case["task"]["sha256"]
        search["inputs"]["grammar_sha256"] = case["grammar"]["sha256"]
        search_path = output.parent / "search.json"
        search_path.write_text(json.dumps(search, ensure_ascii=False, sort_keys=True) + "\n")
        return review_correspondence(
            REPO,
            review_id="RV-UNIT",
            case=case,
            case_path=case_path,
            task=task,
            witness=witness,
            profile_report={"profile_id": "L1-PARTIALITY-RACE-DEADLINE-v0", "status": "PROFILE_QUALIFIED",
                            "toolchain_ref": "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"},
            grammar=grammar,
            search_run=search,
            search_run_path=search_path,
            output_path=output,
        )

    def test_value_mismatch_mechanism_has_no_business_continuation(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-f4a-") as tmp:
            review = self._review("WV-0002", Path(tmp) / "review.json")
            self.assertNotIn("business continuation", review["mechanism_summary"])
            self.assertIn("value", review["mechanism_summary"].lower())
            self.assertFalse(review["mechanism_facts"]["has_business_bind"])
            self.assertEqual(review["conclusion"]["task_preservation"], "PRESERVED_AT_MODEL_LEVEL")

    def test_completion_mechanism_mentions_declared_continuation(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-f4b-") as tmp:
            review = self._review("WV-0013", Path(tmp) / "review.json")
            self.assertIn("business continuation", review["mechanism_summary"])
            self.assertTrue(review["mechanism_facts"]["has_business_bind"])
            self.assertEqual(review["mechanism_facts"]["compensation"]["class"], "PRE_KEPT_BY_TASK_DECLARATION")

    def test_mechanism_facts_reject_unclassified_shape(self) -> None:
        search = _load_search_run("20260913-SEARCH-L1-002")
        witness = copy.deepcopy(next(w for w in search["witnesses"] if w["witness_id"] == "WV-0002"))
        witness["separation_kind"] = "unknown_kind"
        facts = mechanism_facts(witness, read_json(REPO / "machine-overview/grammars/l1-v1.json"))
        self.assertEqual(facts["derived_witness"]["separation_kind"], "value_mismatch")
        self.assertNotEqual(facts["compensation"]["class"], "UNRESOLVED")


class F5ReductionGrammarTest(unittest.TestCase):
    def test_sparse_deadline_parameters_are_respected(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-f5-") as tmp:
            root = Path(tmp)
            _git_init(root)
            grammar = read_json(REPO / "machine-overview/grammars/l1-v1.json")
            grammar["deadline_horizons"] = [2]
            case_path = root / "case.json"
            case_path.write_text('{"schema_version": "machine-overview-case/v1"}\n')
            receipt = run_search(
                root, run_id="f5", case_path=case_path,
                case={"case_id": "C", "revision": 1, "grammar": {"path": "x", "sha256": "x"},
                      "task": {"path": "x", "sha256": "x"}, "claim_refs": []},
                grammar=grammar,
                profile_report={"profile_id": "p", "status": "PROFILE_QUALIFIED", "toolchain_ref": "x"},
                registry={"coordinator_version": "test", "registry_id": "test"},
                limits={"max_witnesses": 5000, "max_checks": 1000000},
            )
            for witness in receipt["witnesses"]:
                for op in witness["ops"]:
                    if op["kind"] == "deadline":
                        self.assertIn(op["k"], grammar["deadline_horizons"])
                self.assertEqual(witness["grammar_membership"]["status"], "WITHIN_DECLARED_GRAMMAR")


class F6BudgetCompletenessTest(unittest.TestCase):
    def test_budget_reached_never_claims_completeness(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-f6-") as tmp:
            root = Path(tmp)
            _git_init(root)
            grammar = read_json(REPO / "machine-overview/grammars/l1-v1.json")
            case_path = root / "case.json"
            case_path.write_text('{"schema_version": "machine-overview-case/v1"}\n')
            receipt = run_search(
                root, run_id="f6", case_path=case_path,
                case={"case_id": "C", "revision": 1, "grammar": {"path": "x", "sha256": "x"},
                      "task": {"path": "x", "sha256": "x"}, "claim_refs": []},
                grammar=grammar,
                profile_report={"profile_id": "p", "status": "PROFILE_QUALIFIED", "toolchain_ref": "x"},
                registry={"coordinator_version": "test", "registry_id": "test"},
                limits={"max_witnesses": 5000, "max_checks": 1},
            )
            self.assertEqual(receipt["exit_reason"], "BUDGET_REACHED")
            self.assertTrue(receipt["statistics"]["truncated"])
            self.assertFalse(receipt["statistics"]["complete_within_declared_grammar"])
            self.assertLessEqual(receipt["statistics"]["pair_context_checks"], 1)


class F7RecoveryTest(unittest.TestCase):
    def test_interrupted_attempt_is_rolled_over(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-f7-") as tmp:
            root = Path(tmp)
            run_dir = root / "runs" / "run-x"
            run_dir.mkdir(parents=True)
            (run_dir / "generated").mkdir()
            (run_dir / "ATTEMPT.json").write_text(json.dumps({
                "schema_version": "machine-overview-attempt/v1", "run_id": "run-x", "attempt": 1,
                "status": "INTERRUPTED", "error": "FileExistsError: blocked cache",
            }, ensure_ascii=False) + "\n")
            info = prepare_run_dir(run_dir)
            self.assertEqual(info["attempt"], 2)
            self.assertTrue((root / "runs" / "run-x.attempt-1-interrupted").is_dir())
            self.assertTrue(run_dir.is_dir())

    def test_unregistered_legacy_interruption_is_invalid(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-f7-") as tmp:
            root = Path(tmp)
            run_dir = root / "machine-overview/runs/run-x"
            run_dir.mkdir(parents=True)
            (run_dir / "ATTEMPT.json").write_text(json.dumps({
                "schema_version": "machine-overview-attempt/v1", "run_id": "run-x", "attempt": 1,
                "status": "INTERRUPTED", "error": "FileExistsError: blocked cache",
            }, ensure_ascii=False) + "\n")
            report = validate_workspace(root)
            self.assertEqual(report["status"], "INVALID")
            self.assertTrue(any("LEGACY_INTERRUPTED_ATTEMPT_NOT_ALLOWLISTED" in error for error in report["errors"]))

    def test_unrecorded_partial_directory_is_invalid(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-f7b-") as tmp:
            root = Path(tmp)
            (root / "machine-overview/runs/partial-run/generated").mkdir(parents=True)
            report = validate_workspace(root)
            self.assertEqual(report["status"], "INVALID")
            self.assertTrue(any("RUN_DIRECTORY_WITHOUT_RECEIPT" in error for error in report["errors"]))

    def test_kernel_timeout_is_recorded_and_killed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-f7c-") as tmp:
            root = Path(tmp)
            run_dir = root / "run"
            run_dir.mkdir()
            toolchain = read_json(REPO / MODEL / "TOOLCHAIN.json")
            toolchain["agda"] = dict(toolchain["agda"])
            toolchain["agda"]["local_binary"] = "/usr/bin/yes"
            outcome = run_kernel(root, run_dir, label="timeout-test", toolchain=toolchain,
                                 include_dirs=[], entry="noop.agda", expect_success=True, timeout_seconds=1)
            self.assertEqual(outcome["receipt"]["status"], "KERNEL_TIMEOUT")
            self.assertTrue(outcome["receipt"]["timed_out"])
            self.assertFalse(outcome["receipt"]["expectation_met"])

    def test_replay_classification_distinguishes_cache_logs(self) -> None:
        first = {"exit_code": 0, "stdout_sha256": "a", "stderr_sha256": "s"}
        second = {"exit_code": 0, "stdout_sha256": "b", "stderr_sha256": "s"}
        log_a = "Checking Verify (/x/Verify.agda).\nreal output\n"
        log_b = "Checking Verify (/x/Verify.agda).\n Checking Cubical.X (/y/X.agda).\nreal output\n"
        classification = classify_replay(first, log_a.encode(), second, log_b.encode())
        self.assertEqual(classification["classification"], "EXIT_STDERR_MATCH_WITH_CACHE_LOG_DIFFERENCE")
        self.assertTrue(classification["normalized_match"])

    def test_negative_control_diagnostic_classification(self) -> None:
        expected = "/x/generated/Falsify.agda:17.38-39: error: [UnequalTerms]\nfalse != true of type Bool\n"
        self.assertEqual(diagnose_rejection("x/Falsify.agda", 42, expected, ""), "EXPECTED_TYPE_REJECTION")
        scope_error = "when scope checking MVSupport.⇔-bwd\n"
        self.assertEqual(diagnose_rejection("x/Falsify.agda", 42, scope_error, ""), "UNEXPECTED")
        self.assertEqual(diagnose_rejection("x/Falsify.agda", 154, "some output", ""), "INFRASTRUCTURE")


class StrictV2EvidenceTest(unittest.TestCase):
    """Regression coverage for the second audit's P1/P2 trust-boundary findings."""

    def test_toolchain_and_registry_files_are_content_pinned(self) -> None:
        with tempfile.TemporaryDirectory(prefix="mo-v2-profile-") as tmp:
            root = Path(tmp)
            _copy_model(root)
            _copy_system(root)
            profile = root / "machine-overview/profiles/l1-partiality-v2.json"

            toolchain_path = root / MODEL / "TOOLCHAIN.json"
            toolchain = read_json(toolchain_path)
            toolchain["audit_tamper"] = True
            toolchain_path.write_text(json.dumps(toolchain, ensure_ascii=False, sort_keys=True) + "\n")
            report = inspect_profile(root, profile, fast=True)
            self.assertIn("check:toolchain_file_pin", report["failures"])

            shutil.copy2(REPO / MODEL / "TOOLCHAIN.json", toolchain_path)
            with (root / MODEL / "AGDA_LIBRARIES").open("a", encoding="utf-8") as handle:
                handle.write("# tamper\n")
            report = inspect_profile(root, profile, fast=True)
            self.assertIn("check:library_registry_pin", report["failures"])

    def test_run_identifiers_cannot_escape_the_run_root(self) -> None:
        with self.assertRaises(MachineOverviewError) as ctx:
            validate_identifier("../outside", "run_id")
        self.assertEqual(str(ctx.exception), "UNSAFE_IDENTIFIER:run_id:../outside")

    def test_search_semantic_fields_are_recomputed(self) -> None:
        case, case_path = _load_case(4)
        run_id = "20260913-SEARCH-L1-V2-001"
        run_dir = REPO / "machine-overview/runs" / run_id
        run = copy.deepcopy(read_json(run_dir / "RUN.json"))
        run["statistics"]["pair_context_checks"] += 1
        errors: list[str] = []
        _validate_search_run(run_id, run, run_dir, case, case_path, REPO, errors)
        self.assertTrue(any("SEARCH_RECOMPUTED_FIELD_MISMATCH" in error for error in errors))

    def test_verify_kernel_classification_is_recomputed(self) -> None:
        case, case_path = _load_case(4)
        search_id = "20260913-SEARCH-L1-V2-001"
        search_dir = REPO / "machine-overview/runs" / search_id
        search = read_json(search_dir / "RUN.json")
        run_id = "20260913-VERIFY-L1-V2-DEADLINE-001"
        run_dir = REPO / "machine-overview/runs" / run_id
        run = copy.deepcopy(read_json(run_dir / "RUN.json"))
        run["kernel_runs"][0]["status"] = "KERNEL_REJECTED_UNEXPECTED"
        errors: list[str] = []
        _validate_verify_run(
            run_id, run, run_dir, case, case_path, REPO,
            {search_id: (search, search_dir)}, errors,
        )
        self.assertTrue(any("KERNEL_DERIVED_FIELD_MISMATCH" in error for error in errors))

    def test_attempt_identity_mismatch_is_rejected(self) -> None:
        case, case_path = _load_case(4)
        search_id = "20260913-SEARCH-L1-V2-001"
        search_dir = REPO / "machine-overview/runs" / search_id
        search = read_json(search_dir / "RUN.json")
        run_id = "20260913-VERIFY-L1-V2-VALUE-001"
        source_dir = REPO / "machine-overview/runs" / run_id
        run = read_json(source_dir / "RUN.json")
        with tempfile.TemporaryDirectory(prefix="mo-v2-attempt-") as tmp:
            run_dir = Path(tmp) / "machine-overview/runs" / run_id
            shutil.copytree(source_dir, run_dir)
            attempt = read_json(run_dir / "ATTEMPT.json")
            attempt["witness_id"] = "WV-9999"
            (run_dir / "ATTEMPT.json").write_text(
                json.dumps(attempt, ensure_ascii=False, sort_keys=True) + "\n"
            )
            errors: list[str] = []
            _validate_verify_run(
                run_id, run, run_dir, case, case_path, REPO,
                {search_id: (search, search_dir)}, errors,
            )
        self.assertTrue(any("RUN_ATTEMPT_IDENTITY_MISMATCH" in error for error in errors))

    def test_runner_snapshot_tamper_is_rejected(self) -> None:
        case, case_path = _load_case(4)
        run_id = "20260913-SEARCH-L1-V2-001"
        source_dir = REPO / "machine-overview/runs" / run_id
        run = read_json(source_dir / "RUN.json")
        with tempfile.TemporaryDirectory(prefix="mo-v2-runner-") as tmp:
            run_dir = Path(tmp) / "machine-overview/runs" / run_id
            shutil.copytree(source_dir, run_dir)
            snapshot = run_dir / "runner-snapshot/machine-overview/machine_overview/search.py"
            with snapshot.open("a", encoding="utf-8") as handle:
                handle.write("\n# tamper\n")
            errors: list[str] = []
            _validate_search_run(run_id, run, run_dir, case, case_path, REPO, errors)
        self.assertTrue(any("RUNNER_EVIDENCE_INVALID" in error for error in errors))

    def test_correspondence_rejects_unqualified_profile(self) -> None:
        case, _ = _load_case(4)
        search = _load_search_run("20260913-SEARCH-L1-V2-001")
        grammar = read_json(REPO / "machine-overview/grammars/l1-v2.json")
        task = read_json(REPO / "machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-002.json")
        content = derive_correspondence_content(
            case=case, task=task, witness=search["witnesses"][0],
            profile_report={"profile_id": "p", "status": "PROFILE_NOT_QUALIFIED", "failures": ["x"]},
            grammar=grammar, search_run=search,
        )
        self.assertEqual(content["conclusion"]["task_preservation"], "REVIEW_REQUIRED")
        self.assertEqual(content["review_checks"][0]["status"], "FAIL")

    def test_report_binding_uses_search_id_and_hash(self) -> None:
        search_path = REPO / "machine-overview/runs/20260913-SEARCH-L1-V2-001/RUN.json"
        search = read_json(search_path)
        good = read_json(REPO / "machine-overview/runs/20260913-VERIFY-L1-V2-DEADLINE-001/RUN.json")
        wrong_hash = copy.deepcopy(good)
        wrong_hash["source_search_run"]["sha256"] = "0" * 64
        wrong_id = copy.deepcopy(good)
        wrong_id["source_search_run"]["run_id"] = "other-search"
        self.assertTrue(bound_to_search(good, search, search_path))
        self.assertFalse(bound_to_search(wrong_hash, search, search_path))
        self.assertFalse(bound_to_search(wrong_id, search, search_path))

    def test_strict_target_control_must_belong_to_grammar(self) -> None:
        case, _ = _load_case(4)
        search = _load_search_run("20260913-SEARCH-L1-V2-001")
        witness = next(item for item in search["witnesses"] if item["witness_id"] == "WV-0001")
        grammar = copy.deepcopy(read_json(REPO / "machine-overview/grammars/l1-v2.json"))
        grammar["deadline_horizons"] = [0]
        with self.assertRaises(MachineOverviewError) as ctx:
            render_target(case, witness, grammar)
        self.assertEqual(str(ctx.exception), "NEGATIVE_CONTROL_NOT_AVAILABLE_IN_GRAMMAR")


class SymbolicSearchTest(unittest.TestCase):
    @staticmethod
    def grammar() -> dict:
        return {
            "backend": "symbolic-horn-v1",
            "propositions": ["endpoint_path", "reverse_path", "bottom"],
            "goal": "bottom",
            "observation_kind": "continuous_phase_obstruction",
            "max_proof_depth": 4,
            "mechanism_rules": ["interval_eta", "apart_elim"],
            "ablation": {"remove_rules": ["interval_eta"]},
            "positive_control_goals": ["endpoint_path"],
            "rules": [
                {"id": "interval_eta", "premises": [], "conclusion": "endpoint_path",
                 "term_template": "(λ i → f i)"},
                {"id": "path_sym", "premises": ["endpoint_path"], "conclusion": "reverse_path",
                 "term_template": "sym ({0})"},
                {"id": "path_sym_back", "premises": ["reverse_path"], "conclusion": "endpoint_path",
                 "term_template": "sym ({0})"},
                {"id": "apart_elim", "premises": ["endpoint_path"], "conclusion": "bottom",
                 "term_template": "apart ({0})"},
            ],
        }

    def test_symbolic_search_discovers_minimal_proof_and_ablation_removes_it(self) -> None:
        result = compute_search_semantics(
            self.grammar(), {"max_witnesses": 100, "max_checks": 10000, "max_contexts": 10}, 20260913,
        )
        self.assertTrue(result["statistics"]["complete_within_declared_grammar"])
        self.assertTrue(result["order_independence_check"]["order_independent_set_equal"])
        self.assertFalse(result["grammar_sensitivity_check"]["mutated_contains_goal"])
        first = result["witnesses"][0]
        self.assertEqual(first["proof_term"], "apart ((λ i → f i))")
        self.assertEqual(first["size"], {"nodes": 2, "depth": 2})
        self.assertEqual(derive_witness_record(first, self.grammar()), first)

    def test_symbolic_depth_budget_never_claims_completeness(self) -> None:
        result = compute_search_semantics(
            self.grammar(), {"max_witnesses": 100, "max_checks": 10000, "max_contexts": 1}, 20260913,
        )
        self.assertTrue(result["statistics"]["proof_depth_budget_exhausted"])
        self.assertFalse(result["statistics"]["complete_within_declared_grammar"])
        self.assertEqual(result["exit_reason"], "BUDGET_REACHED")

    def test_l3_profile_controls_are_source_pinned(self) -> None:
        report = inspect_profile(REPO, REPO / "machine-overview/profiles/l3-interval-motion-v1.json", fast=True)
        self.assertEqual(report["status"], "PROFILE_QUALIFIED")
        self.assertEqual(report["sources"][0]["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
