"""Exact-statement generation, candidate-proof hygiene and native kernel runs.

Two proof paths are supported:
  * ``coordinator_template``: the trusted coordinator renders a proof from the
    reduced witness using pinned support lemmas (the M1 calibration path);
  * ``external_file``: a candidate process supplies the proof source; the
    coordinator freezes the Target module first and rejects proofs that do not
    inhabit exactly that statement.

Hardening added after the external M1 audit (F2/F3/F7):
  * a verify run is bound to (case revision, search run hash, witness AST hash,
    frozen target hash) and refuses cross-revision evidence;
  * every run writes an ``ATTEMPT.json`` identity first and upgrades it to
    COMPLETED / INTERRUPTED, so infrastructure failures stay visible;
  * kernel runs have an internal timeout with process-group termination;
  * replay classification distinguishes exact byte replay from cache-related
    Agda check-log differences instead of collapsing both into failure;
  * the negative control must show the expected type-error diagnostic for the
    Falsify entry module, not merely a non-zero exit.
"""
from __future__ import annotations

import os
import platform
import re
import signal
import subprocess
import time
from pathlib import Path

from .case import case_identity_sha256, validate_identifier
from .model import (
    agda_bool,
    agda_nat,
    agda_value,
    apply_ops,
    continuation_from_json,
    observation_mode,
    value_from_json,
)
from .search import within_grammar_witness, witness_ast_sha256
from .util import (
    MachineOverviewError,
    git_state,
    json_bytes,
    read_json,
    sha256_bytes,
    sha256_file,
    utc_now,
    write_bytes,
    write_json,
    write_text,
)

OPTIONS = "{-# OPTIONS --safe --cubical --guardedness #-}"

FORBIDDEN_MARKERS = (
    "postulate",
    "primitive ",
    "{!!}",
    "{-# TERMINATING #-}",
    "{-# NON_TERMINATING #-}",
    "--type-in-type",
    "--no-positivity-check",
    "--no-termination-check",
    "--no-universe-check",
    "--allow-unsolved-metas",
    "--allow-incomplete-matches",
)

HEADER_IMPORTS = [
    "open import Cubical.Foundations.Prelude",
    "open import Cubical.Data.Bool.Base using (Bool; true; false)",
    "open import Cubical.Data.Bool.Properties using (true≢false; false≢true)",
    "open import Cubical.Data.Nat.Base using (ℕ; zero; suc)",
    "open import PartialityRaceTimeout",
]

TYPE_ERROR_PATTERN = re.compile(r"error: \[[A-Za-z]+\]")
CHECK_LINE_PATTERN = re.compile(r"^\s*Checking\s+\S+.*\.\s*$")
INFRASTRUCTURE_MARKERS = (
    "io error",
    "cannot read file",
    "cannot find file",
    "interface file",
    "failed to find",
    "environment variable",
)


def check_proof_hygiene(text: str, origin: str) -> None:
    for marker in FORBIDDEN_MARKERS:
        if marker in text:
            raise MachineOverviewError(f"CANDIDATE_FORBIDDEN_DECLARATION:{origin}:{marker}")
    if "module Proof where" not in text:
        raise MachineOverviewError(f"CANDIDATE_MODULE_NAME_INVALID:{origin}")
    if "Target." not in text:
        raise MachineOverviewError(f"CANDIDATE_DOES_NOT_REFERENCE_TARGET:{origin}")


def normalize_agda_log(text: str) -> str:
    kept = [line.rstrip() for line in text.splitlines() if not CHECK_LINE_PATTERN.match(line)]
    while kept and not kept[-1]:
        kept.pop()
    return "\n".join(kept)


def classify_replay(first_receipt: dict, first_stdout: bytes, second_receipt: dict, second_stdout: bytes) -> dict:
    if first_receipt.get("exit_code") != second_receipt.get("exit_code"):
        return {"classification": "EXIT_MISMATCH", "exact": False, "normalized_match": False}
    if first_receipt.get("stderr_sha256") != second_receipt.get("stderr_sha256"):
        return {"classification": "STDERR_MISMATCH", "exact": False, "normalized_match": False}
    if first_receipt.get("stdout_sha256") == second_receipt.get("stdout_sha256"):
        return {"classification": "EXACT_EXIT_STDOUT_STDERR_MATCH", "exact": True, "normalized_match": True}
    if normalize_agda_log(first_stdout.decode("utf-8", "replace")) == normalize_agda_log(second_stdout.decode("utf-8", "replace")):
        return {
            "classification": "EXIT_STDERR_MATCH_WITH_CACHE_LOG_DIFFERENCE",
            "exact": False,
            "normalized_match": True,
            "normalization": "drop Agda 'Checking <Module> (<path>).' lines produced when an interface cache entry is absent",
        }
    return {"classification": "STDOUT_MISMATCH", "exact": False, "normalized_match": False}


def diagnose_rejection(entry: str, exit_code: int, stdout_text: str, stderr_text: str) -> str:
    combined = stdout_text + "\n" + stderr_text
    lowered = combined.lower()
    if exit_code == 154 or any(marker in lowered for marker in INFRASTRUCTURE_MARKERS):
        return "INFRASTRUCTURE"
    entry_name = Path(entry).name
    if exit_code == 42 and TYPE_ERROR_PATTERN.search(combined) and entry_name in combined:
        return "EXPECTED_TYPE_REJECTION"
    return "UNEXPECTED"


def _render_context_definitions(ops: list[dict]) -> tuple[list[str], dict[str, str]]:
    lines: list[str] = []
    names: dict[str, str] = {}
    partner_index = 0
    continuation_index = 0
    for op in ops:
        if op["kind"] in ("race_left", "race_right"):
            key = "partner:" + str(op["partner"])
            if key not in names:
                name = f"partner{partner_index}"
                partner_index += 1
                lines += [f"{name} : Delay Bool", f"{name} = {agda_value(value_from_json(op['partner']))}", ""]
                names[key] = name
        elif op["kind"] == "bind":
            key = "continuation:" + str(op["continuation"])
            if key not in names:
                name = f"cur{continuation_index}"
                continuation_index += 1
                continuation = continuation_from_json(op["continuation"])
                lines += [
                    f"{name} : Bool → Delay Bool",
                    f"{name} true = {agda_value(continuation[True])}",
                    f"{name} false = {agda_value(continuation[False])}",
                    "",
                ]
                names[key] = name
    return lines, names


def render_context_expression(ops: list[dict], names: dict[str, str], base: str) -> str:
    expression = base
    for op in ops:
        if op["kind"] == "race_left":
            expression = f"({expression} race {names['partner:' + str(op['partner'])]})"
        elif op["kind"] == "race_right":
            expression = f"({names['partner:' + str(op['partner'])]} race {expression})"
        elif op["kind"] == "bind":
            expression = f"({expression} bind {names['continuation:' + str(op['continuation'])]})"
        elif op["kind"] == "deadline":
            expression = f"(deadline {agda_nat(op['k'])} {expression})"
        else:
            raise MachineOverviewError(f"UNKNOWN_CONTEXT_OP:{op['kind']}")
    return expression


def negative_control_horizon(left: tuple, right: tuple) -> int:
    indices = [value[1] for value in (left, right) if value[0] == "ret"]
    return max(indices) if indices else 0


def render_target(case: dict, witness: dict) -> str:
    left = value_from_json(witness["pair"]["left"])
    right = value_from_json(witness["pair"]["right"])
    ops = witness["ops"]
    mode = observation_mode(ops)
    definition_lines, names = _render_context_definitions(ops)
    observed_type = "Optional Bool" if mode == "deadline" else "Delay Bool"
    lines = [
        OPTIONS,
        "",
        f"-- Generated by machine_overview for case {case['case_id']} / witness {witness['witness_id']}.",
        "-- This module fixes the exact statement the candidate proof must inhabit;",
        "-- its SHA-256 is recorded before any proof source is accepted.",
        "",
        "module Target where",
        "",
        *HEADER_IMPORTS,
        "",
        "p : Delay Bool",
        f"p = {agda_value(left)}",
        "",
        "q : Delay Bool",
        f"q = {agda_value(right)}",
        "",
        *definition_lines,
        f"left : {observed_type}",
        f"left = {render_context_expression(ops, names, 'p')}",
        "",
        f"right : {observed_type}",
        f"right = {render_context_expression(ops, names, 'q')}",
        "",
        "-- Non-separating deadline instance used by the negative control.",
        "control-left : Optional Bool",
        f"control-left = deadline {agda_nat(negative_control_horizon(left, right))} p",
        "",
        "control-right : Optional Bool",
        f"control-right = deadline {agda_nat(negative_control_horizon(left, right))} q",
        "",
    ]
    return "\n".join(lines)


def render_proof(case: dict, witness: dict) -> str:
    left = value_from_json(witness["pair"]["left"])
    right = value_from_json(witness["pair"]["right"])
    mode = observation_mode(witness["ops"])
    observed_left = value_from_json(witness["left_observation"])
    observed_right = value_from_json(witness["right_observation"])
    lines = [
        OPTIONS,
        "",
        f"-- Coordinator-templated proof for {case['case_id']} / {witness['witness_id']}.",
        "-- The proof only instantiates pinned support lemmas with computable facts.",
        "",
        "module Proof where",
        "",
        *HEADER_IMPORTS,
        "open import Target",
        "open import MVSupport",
        "",
        "equiv : Target.p ≈ Target.q",
    ]
    if left[0] == "omega" and right[0] == "omega":
        lines.append("equiv = MVSupport.≈-same-omega")
    elif left[0] == "ret" and right[0] == "ret" and left[2] == right[2]:
        lines.append(
            f"equiv = MVSupport.≈-same-ret {agda_nat(left[1])} {agda_nat(right[1])} {agda_bool(left[2])}"
        )
    else:
        raise MachineOverviewError("EQUIVALENCE_TEMPLATE_UNSUPPORTED")

    lines += ["", f"gap : {'¬ (Target.left ≡ Target.right)' if mode == 'deadline' else '¬ (Target.left ≈ Target.right)'}"]
    if mode == "deadline":
        if observed_left[0] == "some" and observed_right[0] == "none":
            lines.append(f"gap e = MVSupport.some-neq-none {agda_bool(observed_left[1])} e")
        elif observed_left[0] == "none" and observed_right[0] == "some":
            lines.append(f"gap e = MVSupport.none-neq-some {agda_bool(observed_right[1])} e")
        elif observed_left[0] == "some" and observed_right[0] == "some" and observed_left[1] != observed_right[1]:
            lemma = "true≢false" if observed_left[1] else "false≢true"
            lines.append(
                f"gap e = MVSupport.some-neq-some {agda_bool(observed_left[1])} {agda_bool(observed_right[1])} {lemma} e"
            )
        else:
            raise MachineOverviewError("DEADLINE_GAP_TEMPLATE_UNSUPPORTED")
    else:
        if observed_left[0] == "ret" and observed_right[0] == "ret" and observed_left[2] != observed_right[2]:
            # We exhibit Conv right a (a = left value), which reduces to c ≡ a
            # with c = right value; the lemma must refute c ≡ a.
            lemma = "true≢false" if observed_right[2] else "false≢true"
            lines.append(f"gap h = {lemma} (⇔-fwd (h {agda_bool(observed_left[2])}) refl)")
        elif observed_left[0] == "ret" and observed_right[0] == "omega":
            lines.append(f"gap h = lower (⇔-fwd (h {agda_bool(observed_left[2])}) refl)")
        elif observed_left[0] == "omega" and observed_right[0] == "ret":
            lines.append(f"gap h = lower (⇔-bwd (h {agda_bool(observed_right[2])}) refl)")
        else:
            raise MachineOverviewError("DELAY_GAP_TEMPLATE_UNSUPPORTED")
    lines.append("")
    return "\n".join(lines)


def render_verify(witness: dict) -> str:
    mode = observation_mode(witness["ops"])
    claim = "¬ (Target.left ≡ Target.right)" if mode == "deadline" else "¬ (Target.left ≈ Target.right)"
    lines = [
        OPTIONS,
        "",
        "-- Coordinator-owned entry module: it must only accept a proof that",
        "-- inhabits exactly the frozen Target statement.",
        "",
        "module Verify where",
        "",
        *HEADER_IMPORTS,
        "open import Target",
        "open import Proof",
        "",
        "check-equiv : Target.p ≈ Target.q",
        "check-equiv = Proof.equiv",
        "",
        f"check-gap : {claim}",
        "check-gap = Proof.gap",
        "",
    ]
    return "\n".join(lines)


def render_controls(witness: dict) -> str:
    mode = observation_mode(witness["ops"])
    claim = "¬ (Target.left ≡ Target.right)" if mode == "deadline" else "¬ (Target.left ≈ Target.right)"
    lines = [
        OPTIONS,
        "",
        "-- Positive controls: a completion-preserving consumer does not separate",
        "-- the same result-equivalent pair, while the declared consumer does.",
        "",
        "module Controls where",
        "",
        *HEADER_IMPORTS,
        "open import Target",
        "open import Proof",
        "",
        "keeping : Bool → Delay Bool",
        "keeping _ = ret zero true",
        "",
        "preserved : (Target.p bind keeping) ≈ (Target.q bind keeping)",
        "preserved = bind-cong Target.p Target.q keeping keeping Proof.equiv (λ a → ≈-refl (keeping a))",
        "",
        f"not-preserved : {claim}",
        "not-preserved = Proof.gap",
        "",
    ]
    return "\n".join(lines)


def render_falsify(witness: dict) -> str:
    return "\n".join([
        OPTIONS,
        "",
        "-- Negative control: this instance does NOT separate the pair, so the",
        "-- kernel must reject the following claim with a type error in this module.",
        "",
        "module Falsify where",
        "",
        *HEADER_IMPORTS,
        "open import Target",
        "open import MVSupport",
        "",
        "bad : ¬ (Target.control-left ≡ Target.control-right)",
        "bad e = MVSupport.some-neq-none true e",
        "",
    ])


def _kernel_environment(toolchain: dict) -> dict[str, str]:
    cache = toolchain["runtime_cache"]
    env = dict(os.environ)
    for key in ("xdg_data_home", "xdg_config_home", "tmpdir"):
        path = Path(cache[key])
        path.mkdir(parents=True, exist_ok=True)
        if path.is_symlink():
            raise MachineOverviewError(f"RUNTIME_CACHE_SYMLINK:{key}")
    env["XDG_DATA_HOME"] = cache["xdg_data_home"]
    env["XDG_CONFIG_HOME"] = cache["xdg_config_home"]
    env["TMPDIR"] = cache["tmpdir"]
    return env


def kernel_command(repo_root: Path, toolchain: dict, include_dirs: list[str], entry: str) -> list[str]:
    agda = toolchain["agda"]
    cubical = toolchain["cubical_library"]
    library_registry = toolchain["project_library_registry"]
    command = [
        agda["local_binary"],
        "--ignore-interfaces",
        f"--library-file={repo_root / library_registry}",
        "-l",
        f"cubical-{cubical['version']}",
    ]
    for include in include_dirs:
        command += ["-i", include]
    command.append(entry)
    return command


def run_kernel(
    repo_root: Path,
    run_dir: Path,
    *,
    label: str,
    toolchain: dict,
    include_dirs: list[str],
    entry: str,
    expect_success: bool,
    timeout_seconds: int = 900,
) -> dict:
    """Run one kernel process with timeout and process-group termination.

    Returns ``{"receipt": {...}, "stdout": bytes, "stderr": bytes}``.
    """
    target_dir = run_dir / "kernel" / label
    command = kernel_command(repo_root, toolchain, include_dirs, entry)
    environment = _kernel_environment(toolchain)
    environment_text = "\n".join([
        f"platform={platform.platform()}",
        f"python={platform.python_version()}",
        f"agda_binary={toolchain['agda']['local_binary']}",
        f"agda_binary_sha256={sha256_file(Path(toolchain['agda']['local_binary']))}",
        "dependency_policy=pinned Agda release asset, pinned Cubical release tree, no network",
        "",
    ])
    started = utc_now()
    started_monotonic = time.monotonic()
    process = subprocess.Popen(
        command, cwd=repo_root, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env=environment, start_new_session=True,
    )
    timed_out = False
    try:
        stdout, stderr = process.communicate(timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        timed_out = True
        stdout, stderr = b"", b""
        for sig in (signal.SIGTERM, signal.SIGKILL):
            try:
                os.killpg(process.pid, sig)
            except ProcessLookupError:
                break
            try:
                stdout, stderr = process.communicate(timeout=10)
                break
            except subprocess.TimeoutExpired:
                stdout, stderr = b"", b""
        else:
            stdout, stderr = b"", b""
    duration = time.monotonic() - started_monotonic
    completed = utc_now()
    stdout_text = stdout.decode("utf-8", "replace")
    stderr_text = stderr.decode("utf-8", "replace")

    if timed_out:
        status = "KERNEL_TIMEOUT"
        expectation_met = False
    elif expect_success:
        if process.returncode == 0:
            status, expectation_met = "KERNEL_ACCEPTED", True
        elif diagnose_rejection(entry, process.returncode or 0, stdout_text, stderr_text) == "INFRASTRUCTURE":
            status, expectation_met = "KERNEL_INFRASTRUCTURE_ERROR", False
        else:
            status, expectation_met = "KERNEL_REJECTED_UNEXPECTED", False
    else:
        diagnosis = diagnose_rejection(entry, process.returncode or 0, stdout_text, stderr_text)
        if process.returncode == 0:
            status, expectation_met = "KERNEL_ACCEPTED_UNEXPECTED", False
        elif diagnosis == "EXPECTED_TYPE_REJECTION":
            status, expectation_met = "KERNEL_REJECTED_AS_EXPECTED", True
        elif diagnosis == "INFRASTRUCTURE":
            status, expectation_met = "KERNEL_INFRASTRUCTURE_ERROR", False
        else:
            status, expectation_met = "KERNEL_REJECTED_WITH_UNEXPECTED_DIAGNOSTIC", False

    artifacts = {
        "stdout": {"path": "stdout.txt", "bytes": len(stdout), "sha256": sha256_bytes(stdout)},
        "stderr": {"path": "stderr.txt", "bytes": len(stderr), "sha256": sha256_bytes(stderr)},
        "environment": {"path": "environment.txt", "bytes": len(environment_text.encode()),
                        "sha256": sha256_bytes(environment_text.encode())},
        "command": {"path": "command.json"},
    }
    receipt = {
        "label": label,
        "command_argv": command,
        "cwd": str(repo_root),
        "entry": entry,
        "expect_success": expect_success,
        "exit_code": process.returncode,
        "timed_out": timed_out,
        "timeout_seconds": timeout_seconds,
        "duration_seconds": duration,
        "stdout_bytes": len(stdout),
        "stdout_sha256": sha256_bytes(stdout),
        "stderr_bytes": len(stderr),
        "stderr_sha256": sha256_bytes(stderr),
        "started_at_utc": started,
        "completed_at_utc": completed,
        "status": status,
        "expectation_met": expectation_met,
        "diagnostic": diagnose_rejection(entry, process.returncode or 0, stdout_text, stderr_text),
        "environment": environment_text,
        "artifacts": artifacts,
    }
    write_bytes(target_dir / "stdout.txt", stdout)
    write_bytes(target_dir / "stderr.txt", stderr)
    write_text(target_dir / "environment.txt", receipt["environment"] + "\n")
    write_json(target_dir / "command.json", {
        "command_argv": command,
        "cwd": str(repo_root),
        "exit_code": process.returncode,
        "timed_out": timed_out,
        "timeout_seconds": timeout_seconds,
    })
    return {"receipt": receipt, "stdout": stdout, "stderr": stderr}


def prepare_run_dir(run_dir: Path) -> dict:
    """Create an exclusive run directory or roll over a recorded interruption."""
    if run_dir.exists():
        if (run_dir / "RUN.json").is_file():
            raise MachineOverviewError(f"RUN_DIRECTORY_ALREADY_EXISTS:{run_dir.name}")
        attempt_file = run_dir / "ATTEMPT.json"
        if not attempt_file.is_file():
            raise MachineOverviewError(f"RUN_DIRECTORY_INCOMPLETE_UNRECORDED:{run_dir.name}")
        attempt = read_json(attempt_file)
        if attempt.get("status") not in ("INTERRUPTED", "FAILED"):
            raise MachineOverviewError(f"RUN_ATTEMPT_ACTIVE:{run_dir.name}:{attempt.get('status')}")
        index = 1
        while True:
            rolled = run_dir.parent / f"{run_dir.name}.attempt-{index}-interrupted"
            if not rolled.exists():
                break
            index += 1
        os.rename(run_dir, rolled)
        run_dir.mkdir(parents=True, exist_ok=False)
        return {"rolled_over_from": rolled.as_posix(), "attempt": index + 1}
    run_dir.mkdir(parents=True, exist_ok=False)
    return {"rolled_over_from": None, "attempt": 1}


def begin_attempt(run_dir: Path, *, run_id: str, case: dict, planned: list[str] | tuple[str, ...],
                  witness_id: str | None = None, candidate_ast_sha256: str | None = None) -> tuple[dict, dict]:
    """Create the run directory and persist its attempt identity before any work."""
    info = prepare_run_dir(run_dir)
    attempt = {
        "schema_version": "machine-overview-attempt/v1",
        "run_id": run_id,
        "attempt": info["attempt"],
        "status": "RUNNING",
        "started_at_utc": utc_now(),
        "case_id": case.get("case_id"),
        "case_revision": case.get("revision"),
        "witness_id": witness_id,
        "candidate_ast_sha256": candidate_ast_sha256,
        "planned": list(planned),
        "rolled_over_from": info["rolled_over_from"],
    }
    write_json(run_dir / "ATTEMPT.json", attempt)
    return info, attempt


def finish_attempt(run_dir: Path, attempt: dict, status: str, *, error: str | None = None) -> None:
    attempt["status"] = status
    attempt["ended_at_utc"] = utc_now()
    if error is not None:
        attempt["error"] = error
    write_json(run_dir / "ATTEMPT.json", attempt)


def assert_witness_binding(
    *,
    case: dict,
    search_run: dict,
    search_run_path: Path,
    witness: dict,
    grammar: dict,
) -> dict:
    """Refuse evidence that does not belong to this case revision (audit F2)."""
    if search_run.get("case_id") != case["case_id"]:
        raise MachineOverviewError("WITNESS_FROM_DIFFERENT_CASE")
    if int(search_run.get("case_revision", -1)) != int(case["revision"]):
        raise MachineOverviewError("WITNESS_FROM_DIFFERENT_CASE_REVISION")
    inputs = search_run.get("inputs", {})
    if inputs.get("grammar_sha256") != case["grammar"]["sha256"]:
        raise MachineOverviewError("SEARCH_RUN_INPUT_MISMATCH:grammar")
    if inputs.get("task_sha256") != case["task"]["sha256"]:
        raise MachineOverviewError("SEARCH_RUN_INPUT_MISMATCH:task")
    recorded = {w["witness_id"]: w for w in search_run.get("witnesses", [])}
    if witness["witness_id"] not in recorded:
        raise MachineOverviewError("WITNESS_NOT_IN_SEARCH_RUN")
    recorded_witness = recorded[witness["witness_id"]]
    if recorded_witness.get("ast_sha256") and recorded_witness["ast_sha256"] != witness_ast_sha256(witness):
        raise MachineOverviewError("WITNESS_AST_MISMATCH")
    left = value_from_json(witness["pair"]["left"])
    right = value_from_json(witness["pair"]["right"])
    inside, reason = within_grammar_witness(witness["ops"], left, right, grammar)
    if not inside:
        raise MachineOverviewError(f"WITNESS_OUTSIDE_DECLARED_GRAMMAR:{reason}")
    return {
        "run_id": search_run["run_id"],
        "path": search_run_path.as_posix(),
        "sha256": sha256_file(search_run_path),
        "case_revision": int(search_run["case_revision"]),
    }


def _freeze_target(repo_root: Path, case: dict, witness_ast_sha256_value: str, target_sha: str, run_id: str) -> dict:
    ledger_dir = repo_root / "machine-overview" / "cases" / case["case_id"]
    ledger_path = ledger_dir / f"target-freeze-{case['revision']}.json"
    if ledger_path.is_file():
        ledger = read_json(ledger_path)
    else:
        ledger = {
            "schema_version": "machine-overview-target-freeze/v1",
            "case_id": case["case_id"],
            "revision": case["revision"],
            "entries": {},
        }
    entries = ledger.setdefault("entries", {})
    entry = entries.get(witness_ast_sha256_value)
    if entry is not None:
        if entry.get("target_text_hash") != target_sha:
            raise MachineOverviewError("TARGET_CHANGED")
        status = "REUSED"
    else:
        entries[witness_ast_sha256_value] = {
            "target_text_hash": target_sha,
            "frozen_at_utc": utc_now(),
            "first_verify_run": run_id,
        }
        status = "FROZEN"
    write_json(ledger_path, ledger)
    return {"ledger": ledger_path.relative_to(repo_root).as_posix(), "status": status}


def verify_witness(
    repo_root: Path,
    *,
    run_id: str,
    case_path: Path,
    case: dict,
    witness: dict,
    profile_report: dict,
    toolchain: dict,
    registry: dict,
    run_dir: Path,
    proof_origin: str = "coordinator_template",
    proof_text: str | None = None,
    replay: bool = True,
    timeout_seconds: int = 900,
    source_search_run: dict | None = None,
    search_run_path: Path | None = None,
    grammar: dict | None = None,
) -> dict:
    started = utc_now()
    validate_identifier(run_id, "run_id")

    binding = None
    if source_search_run is not None:
        if search_run_path is None or grammar is None:
            raise MachineOverviewError("SEARCH_BINDING_INCOMPLETE")
        binding = assert_witness_binding(
            case=case, search_run=source_search_run, search_run_path=search_run_path,
            witness=witness, grammar=grammar,
        )

    # All rejection paths below run before any side effect: a rejected candidate
    # must not consume a run id or leave a partial receipt behind.
    target_text = render_target(case, witness)
    target_bytes = target_text.encode("utf-8")
    target_sha = sha256_bytes(target_bytes)
    if case.get("target_text_hash") and case["target_text_hash"] != target_sha:
        raise MachineOverviewError("TARGET_CHANGED")

    if proof_text is None:
        proof_text = render_proof(case, witness)
    check_proof_hygiene(proof_text, proof_origin)

    attempt_info, attempt = begin_attempt(
        run_dir,
        run_id=run_id,
        case=case,
        witness_id=witness["witness_id"],
        candidate_ast_sha256=witness_ast_sha256(witness),
        planned=["verify", "controls", "negative-control"] + (["verify-replay"] if replay else []),
    )
    try:
        freeze = _freeze_target(repo_root, case, attempt["candidate_ast_sha256"], target_sha, run_id)
        generated = run_dir / "generated"
        generated.mkdir()
        write_bytes(generated / "Target.agda", target_bytes)
        write_bytes(generated / "Proof.agda", proof_text.encode("utf-8"))
        write_bytes(generated / "Verify.agda", render_verify(witness).encode("utf-8"))
        write_bytes(generated / "Controls.agda", render_controls(witness).encode("utf-8"))
        write_bytes(generated / "Falsify.agda", render_falsify(witness).encode("utf-8"))

        include_dirs = [
            "machine-overview/formal",
            "HoTT/formal/partiality-race-timeout",
            f"machine-overview/runs/{run_id}/generated",
        ]
        outcomes = [
            run_kernel(repo_root, run_dir, label="verify", toolchain=toolchain, include_dirs=include_dirs,
                       entry=f"machine-overview/runs/{run_id}/generated/Verify.agda", expect_success=True,
                       timeout_seconds=timeout_seconds),
            run_kernel(repo_root, run_dir, label="controls", toolchain=toolchain, include_dirs=include_dirs,
                       entry=f"machine-overview/runs/{run_id}/generated/Controls.agda", expect_success=True,
                       timeout_seconds=timeout_seconds),
            run_kernel(repo_root, run_dir, label="negative-control", toolchain=toolchain, include_dirs=include_dirs,
                       entry=f"machine-overview/runs/{run_id}/generated/Falsify.agda", expect_success=False,
                       timeout_seconds=timeout_seconds),
        ]
        replay_classification = None
        if replay:
            replay_outcome = run_kernel(
                repo_root, run_dir, label="verify-replay", toolchain=toolchain, include_dirs=include_dirs,
                entry=f"machine-overview/runs/{run_id}/generated/Verify.agda", expect_success=True,
                timeout_seconds=timeout_seconds,
            )
            replay_classification = classify_replay(
                outcomes[0]["receipt"], outcomes[0]["stdout"], replay_outcome["receipt"], replay_outcome["stdout"]
            )
            replay_classification["exit_codes"] = [outcomes[0]["receipt"]["exit_code"], replay_outcome["receipt"]["exit_code"]]
            outcomes.append(replay_outcome)

        kernels = [outcome["receipt"] for outcome in outcomes]
        infrastructure = [k for k in kernels if k["status"] in ("KERNEL_TIMEOUT", "KERNEL_INFRASTRUCTURE_ERROR")]
        failures = [k for k in kernels if k["expectation_met"] is not True]
        base_met = all(k["expectation_met"] for k in kernels[:3])
        if infrastructure:
            status = "VERIFY_INFRASTRUCTURE_ERROR"
        elif failures or not base_met:
            status = "NATIVE_CHECK_FAILED"
        elif replay_classification and not replay_classification["normalized_match"]:
            status = "NATIVE_CHECKED_WITH_REPLAY_MISMATCH"
        else:
            status = "NATIVE_CHECKED_CALIBRATION_INSTANCE"

        source_closure = [
            {"path": "HoTT/formal/partiality-race-timeout/PartialityRaceTimeout.agda",
             "sha256": sha256_file(repo_root / "HoTT/formal/partiality-race-timeout/PartialityRaceTimeout.agda")},
            {"path": "machine-overview/formal/MVSupport.agda",
             "sha256": sha256_file(repo_root / "machine-overview/formal/MVSupport.agda")},
        ] + [
            {"path": f"machine-overview/runs/{run_id}/generated/{name}",
             "sha256": sha256_file(generated / name)}
            for name in ("Target.agda", "Proof.agda", "Verify.agda", "Controls.agda", "Falsify.agda")
        ]
        receipt = {
            "schema_version": "machine-overview-verify-run/v1",
            "run_id": run_id,
            "kind": "verify",
            "case_id": case["case_id"],
            "case_revision": case["revision"],
            "case_pointer": str(case_path),
            "case_sha256": sha256_file(case_path),
            "case_identity_sha256": case_identity_sha256(case),
            "witness_id": witness["witness_id"],
            "candidate_ast_sha256": attempt["candidate_ast_sha256"],
            "source_search_run": binding,
            "started_at_utc": started,
            "completed_at_utc": utc_now(),
            "coordinator_version": registry["coordinator_version"],
            "profile": {
                "profile_id": profile_report["profile_id"],
                "profile_status": profile_report["status"],
                "toolchain_ref": profile_report["toolchain_ref"],
            },
            "proof_origin": proof_origin,
            "attempt": attempt_info,
            "timeout_seconds": timeout_seconds,
            "toolchain_identity": {
                "agda_binary": toolchain["agda"]["local_binary"],
                "agda_binary_sha256": sha256_file(Path(toolchain["agda"]["local_binary"])),
                "agda_version": toolchain["agda"]["version"],
                "cubical_library_file": toolchain["cubical_library"]["library_file"],
                "cubical_library_file_sha256": sha256_file(Path(toolchain["cubical_library"]["library_file"])),
                "cubical_version": toolchain["cubical_library"]["version"],
                "cubical_tree_sha256": toolchain["cubical_library"]["tree_sha256"],
            },
            "include_dirs": include_dirs,
            "import_closure": {
                "entry": f"machine-overview/runs/{run_id}/generated/Verify.agda",
                "options": ["--ignore-interfaces", f"--library-file={toolchain['project_library_registry']}",
                            f"-l cubical-{toolchain['cubical_library']['version']}"],
                "sources": source_closure,
            },
            "generated_sources": {
                name: {"sha256": sha256_file(generated / name), "bytes": (generated / name).stat().st_size}
                for name in ("Target.agda", "Proof.agda", "Verify.agda", "Controls.agda", "Falsify.agda")
            },
            "target_text_hash": target_sha,
            "target_freeze": freeze,
            "statement": {
                "pair": witness["pair"],
                "ops": witness["ops"],
                "observation_mode": witness["observation_mode"],
                "left_observation": witness["left_observation"],
                "right_observation": witness["right_observation"],
                "separation_kind": witness["separation_kind"],
            },
            "kernel_runs": kernels,
            "replay": replay_classification,
            "status": status,
            "claim_relation": {
                "kind": "calibration_instance_of_known_mechanism",
                "related_claims": case.get("claim_refs", []),
                "registers_new_claim": False,
                "note": "Exploration receipts stay under machine-overview/runs; "
                        "they do not enter HoTT/CLAIM_EVIDENCE_MATRIX.md.",
            },
            "git": git_state(repo_root),
        }
        write_json(run_dir / "RUN.json", receipt)
        finish_attempt(run_dir, attempt, "COMPLETED")
        return receipt
    except BaseException as exc:  # noqa: BLE001 - record every interruption
        finish_attempt(run_dir, attempt, "INTERRUPTED", error=f"{type(exc).__name__}: {exc}")
        raise
