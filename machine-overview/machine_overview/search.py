"""Typed enumerator, counterexample search and grammar-preserving reduction.

The search walks the *declared* grammar only.  It never consults the known
calibration answer while generating candidates; the known result is used after
the fact as an external benchmark (``calibration_match``).

Reduction is grammar-preserving (audit F5): every shrink must remain an element
of the declared grammar — declared deadline parameters, declared continuation
maps, declared index bounds and the declared context depth.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

from .model import (
    apply_ops,
    continuation_to_json,
    delay_equivalent,
    observation_mode,
    optional_equal,
    ret,
    separation_kind,
    separates,
    value_from_json,
    value_to_json,
)
from .util import MachineOverviewError, git_state, sha256_bytes, sha256_file, utc_now, write_json


def witness_ast_sha256(witness: dict) -> str:
    payload = {"pair": witness["pair"], "ops": witness["ops"]}
    return sha256_bytes(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode("utf-8"))


def _value_within(value: tuple, *, index_max: int, include_omega: bool) -> bool:
    if value[0] == "omega":
        return include_omega
    if value[0] != "ret":
        return False
    return 0 <= value[1] <= index_max


def within_grammar_witness(ops: list[dict], left: tuple, right: tuple, grammar: dict) -> tuple[bool, str | None]:
    """Whether a candidate is an element of the declared grammar."""
    index_max = int(grammar["delay_index_max"])
    partner_max = int(grammar.get("race_partner_index_max", index_max))
    include_omega = bool(grammar.get("include_omega", True))
    depth_max = int(grammar["context_depth_max"])
    if not ops:
        return False, "EMPTY_CONTEXT"
    if len(ops) > depth_max:
        return False, "CONTEXT_DEPTH"
    for value, label in ((left, "left"), (right, "right")):
        if not _value_within(value, index_max=index_max, include_omega=include_omega):
            return False, f"DELAY_INDEX:{label}"
    declared_continuations = {
        json.dumps(continuation["map"], ensure_ascii=False, sort_keys=True)
        for continuation in grammar.get("bind_continuations", [])
    }
    horizons = {int(k) for k in grammar.get("deadline_horizons", [])}
    for op in ops:
        kind = op.get("kind")
        if kind in ("race_left", "race_right"):
            partner = value_from_json(op["partner"])
            if not _value_within(partner, index_max=partner_max, include_omega=include_omega):
                return False, "RACE_PARTNER_INDEX"
        elif kind == "bind":
            key = json.dumps(op["continuation"], ensure_ascii=False, sort_keys=True)
            if key not in declared_continuations:
                return False, "BIND_CONTINUATION"
        elif kind == "deadline":
            if int(op["k"]) not in horizons:
                return False, "DEADLINE_PARAMETER"
        else:
            return False, f"UNKNOWN_OP:{kind}"
    return True, None


def enumerate_atoms(grammar: dict) -> list[tuple]:
    atoms: list[tuple] = []
    if grammar.get("include_omega", True):
        atoms.append(("omega",))
    for n in range(int(grammar["delay_index_max"]) + 1):
        for value in (True, False):
            atoms.append(ret(n, value))
    return atoms


def _single_op_options(grammar: dict) -> list[dict]:
    options: list[dict] = []
    partner_bound = int(grammar.get("race_partner_index_max", grammar["delay_index_max"]))
    partners = [("omega",)] if grammar.get("include_omega", True) else []
    for n in range(partner_bound + 1):
        for value in (True, False):
            partners.append(ret(n, value))
    for partner in partners:
        options.append({"kind": "race_left", "partner": value_to_json(partner)})
        options.append({"kind": "race_right", "partner": value_to_json(partner)})
    for continuation in grammar["bind_continuations"]:
        options.append({"kind": "bind", "continuation": dict(continuation["map"])})
    for horizon in grammar["deadline_horizons"]:
        options.append({"kind": "deadline", "k": int(horizon)})
    return options


def enumerate_contexts(grammar: dict) -> list[list[dict]]:
    """All non-empty well-typed contexts up to the declared depth."""
    depth_max = int(grammar["context_depth_max"])
    frontier: list[list[dict]] = [[]]
    contexts: list[list[dict]] = []
    for _ in range(depth_max):
        next_frontier: list[list[dict]] = []
        for prefix in frontier:
            for op in _single_op_options(grammar):
                candidate = prefix + [op]
                contexts.append(candidate)
                if op["kind"] != "deadline":
                    next_frontier.append(candidate)
        frontier = next_frontier
    return contexts


def _witness_separates(left: tuple, right: tuple, ops: list[dict], grammar: dict | None) -> bool:
    if left == right or not ops or not delay_equivalent(left, right):
        return False
    if grammar is not None:
        ok, _ = within_grammar_witness(ops, left, right, grammar)
        if not ok:
            return False
    ok, _, _ = separates(ops, left, right)
    return ok


def _is_guarded(op: dict, grammar: dict | None) -> bool:
    if not grammar:
        return False
    guard = grammar.get("reduction_guard", {})
    if op["kind"] in guard.get("never_drop_kinds", []):
        return True
    if op["kind"] == "bind":
        for continuation in grammar.get("bind_continuations", []):
            if continuation["id"] in guard.get("never_drop_continuation_ids", []) and op["continuation"] == continuation["map"]:
                return True
    return False


def reduce_witness(left: tuple, right: tuple, ops: list[dict], grammar: dict | None = None) -> tuple[tuple, tuple, list[dict]]:
    """Greedy size reduction that never leaves the declared grammar."""
    ops = [dict(op) for op in ops]
    changed = True
    while changed:
        changed = False
        for index in (0, 1):
            current = left if index == 0 else right
            if current[0] == "ret" and current[1] > 0:
                candidate = ret(current[1] - 1, current[2])
                new_left, new_right = (candidate, right) if index == 0 else (left, candidate)
                if _witness_separates(new_left, new_right, ops, grammar):
                    left, right = new_left, new_right
                    changed = True
        for index, op in enumerate(ops):
            kind = op["kind"]
            if kind in ("race_left", "race_right"):
                partner = value_from_json(op["partner"])
                if partner[0] == "ret" and partner[1] > 0:
                    candidate = {**op, "partner": value_to_json(ret(partner[1] - 1, partner[2]))}
                    new_ops = list(ops)
                    new_ops[index] = candidate
                    if _witness_separates(left, right, new_ops, grammar):
                        ops = new_ops
                        changed = True
            elif kind == "bind":
                continuation = {
                    True: value_from_json(op["continuation"]["true"]),
                    False: value_from_json(op["continuation"]["false"]),
                }
                for key in ("true", "false"):
                    value = continuation[key == "true"]
                    if value[0] == "ret" and value[1] > 0:
                        new_continuation = dict(continuation)
                        new_continuation[key == "true"] = ret(value[1] - 1, value[2])
                        candidate = {**op, "continuation": continuation_to_json(new_continuation)}
                        new_ops = list(ops)
                        new_ops[index] = candidate
                        if _witness_separates(left, right, new_ops, grammar):
                            ops = new_ops
                            changed = True
            elif kind == "deadline" and op["k"] > 0:
                candidate = {**op, "k": op["k"] - 1}
                new_ops = list(ops)
                new_ops[index] = candidate
                if _witness_separates(left, right, new_ops, grammar):
                    ops = new_ops
                    changed = True
        if len(ops) > 1:
            for index in range(len(ops)):
                if _is_guarded(ops[index], grammar):
                    continue
                new_ops = ops[:index] + ops[index + 1:]
                if _witness_separates(left, right, new_ops, grammar):
                    ops = new_ops
                    changed = True
                    break
    return left, right, ops


def _canonical(left: tuple, right: tuple, ops: list[dict]) -> str:
    return json.dumps({"left": value_to_json(left), "right": value_to_json(right), "ops": ops},
                      ensure_ascii=False, sort_keys=True)


def _size(left: tuple, right: tuple, ops: list[dict]) -> dict:
    index_sum = 0
    for value in (left, right):
        if value[0] == "ret":
            index_sum += value[1]
    for op in ops:
        if op["kind"] in ("race_left", "race_right"):
            partner = value_from_json(op["partner"])
            index_sum += partner[1] if partner[0] == "ret" else 0
        elif op["kind"] == "bind":
            for key in ("true", "false"):
                value = value_from_json(op["continuation"][key])
                index_sum += value[1] if value[0] == "ret" else 0
        elif op["kind"] == "deadline":
            index_sum += op["k"]
    return {"context_ops": len(ops), "index_sum": index_sum}


def _witness_record(left: tuple, right: tuple, ops: list[dict], witness_id: str, grammar: dict | None = None) -> dict:
    ok, observed_left, observed_right = separates(ops, left, right)
    if not ok:
        raise MachineOverviewError("WITNESS_DOES_NOT_SEPARATE")
    membership = {"status": "WITHIN_DECLARED_GRAMMAR", "reason": None}
    if grammar is not None:
        inside, reason = within_grammar_witness(ops, left, right, grammar)
        membership = {"status": "WITHIN_DECLARED_GRAMMAR" if inside else "OUTSIDE_DECLARED_GRAMMAR", "reason": reason}
    record = {
        "witness_id": witness_id,
        "pair": {"left": value_to_json(left), "right": value_to_json(right)},
        "ops": ops,
        "observation_mode": observation_mode(ops),
        "left_observation": value_to_json(observed_left),
        "right_observation": value_to_json(observed_right),
        "separation_kind": separation_kind(ops, observed_left, observed_right),
        "size": _size(left, right, ops),
        "grammar_membership": membership,
    }
    record["ast_sha256"] = witness_ast_sha256(record)
    return record


def _enumerate_separations(
    grammar: dict,
    *,
    order_seed: int | None,
    max_witnesses: int,
    max_checks: int,
    max_contexts: int,
) -> tuple[list[dict], dict]:
    atoms = enumerate_atoms(grammar)
    contexts_all = enumerate_contexts(grammar)
    context_budget_exhausted = len(contexts_all) > max_contexts
    contexts = contexts_all[:max_contexts] if context_budget_exhausted else list(contexts_all)
    if order_seed is not None:
        rng = random.Random(order_seed)
        rng.shuffle(atoms)
        rng.shuffle(contexts)

    equivalent_pairs = [
        (left, right)
        for left in atoms
        for right in atoms
        if left != right and delay_equivalent(left, right)
    ]
    checks_planned = len(contexts_all) * len(equivalent_pairs)

    raw: list[dict] = []
    separator_count = 0
    grammar_violations: list[dict] = []
    checks_executed = 0
    contexts_examined = 0
    checks_budget_exhausted = False
    capture_truncated = False

    for ops in contexts:
        if checks_executed >= max_checks:
            checks_budget_exhausted = True
            break
        contexts_examined += 1
        mode = observation_mode(ops)
        for left, right in equivalent_pairs:
            if checks_executed >= max_checks:
                checks_budget_exhausted = True
                break
            checks_executed += 1
            inside, reason = within_grammar_witness(ops, left, right, grammar)
            if not inside:
                grammar_violations.append({"ops": ops, "reason": reason})
                continue
            observed_left = apply_ops(ops, left)
            observed_right = apply_ops(ops, right)
            if mode == "deadline":
                separated = not optional_equal(observed_left, observed_right)
            else:
                separated = not delay_equivalent(observed_left, observed_right)
            if separated:
                separator_count += 1
                if len(raw) < max_witnesses:
                    raw.append({"left": left, "right": right, "ops": [dict(op) for op in ops]})
                else:
                    capture_truncated = True
        if checks_budget_exhausted:
            break

    complete = (
        not checks_budget_exhausted
        and not context_budget_exhausted
        and not capture_truncated
        and contexts_examined == len(contexts_all)
        and checks_executed == checks_planned
    )
    statistics = {
        "delay_atoms": len(atoms),
        "contexts": len(contexts_all),
        "contexts_examined": contexts_examined,
        "pair_context_checks": checks_executed,
        "checks_planned": checks_planned,
        "separations_seen": separator_count,
        "witnesses_captured": len(raw),
        "witness_capture_truncated": capture_truncated,
        "context_budget_exhausted": context_budget_exhausted,
        "checks_budget_exhausted": checks_budget_exhausted,
        "truncated": checks_budget_exhausted or context_budget_exhausted or capture_truncated,
        "complete_within_declared_grammar": complete,
        "grammar_violations": len(grammar_violations),
    }
    return raw, statistics


def _reduced_set(raw: list[dict], grammar: dict | None = None) -> dict[str, tuple[tuple, tuple, list[dict]]]:
    reduced: dict[str, tuple[tuple, tuple, list[dict]]] = {}
    for item in raw:
        left, right, ops = reduce_witness(item["left"], item["right"], item["ops"], grammar)
        reduced.setdefault(_canonical(left, right, ops), (left, right, ops))
    return reduced


def _keeping_continuation() -> dict:
    return {
        "true": value_to_json(ret(0, True)),
        "false": value_to_json(ret(0, False)),
    }


def _negative_control_horizon(left: tuple, right: tuple) -> int:
    indices = [value[1] for value in (left, right) if value[0] == "ret"]
    return max(indices) if indices else 0


def _calibration_match(grammar: dict, reduced: dict) -> dict:
    benchmark = grammar.get("calibration_benchmark")
    if not benchmark:
        return {"status": "NOT_DECLARED"}
    left = value_from_json(benchmark["pair"]["left"])
    right = value_from_json(benchmark["pair"]["right"])
    left, right, ops = reduce_witness(left, right, benchmark["ops"], grammar)
    key = _canonical(left, right, ops)
    return {
        "status": "PRESENT" if key in reduced else "ABSENT",
        "benchmark_id": benchmark.get("id"),
        "claim_refs": benchmark.get("claim_refs", []),
        "reduced_key": key,
        "matched_witness": key in reduced,
    }


def run_search(
    repo_root: Path,
    *,
    run_id: str,
    case_path: Path,
    case: dict,
    grammar: dict,
    profile_report: dict,
    registry: dict,
    limits: dict,
    order_seed: int | None = 20260913,
    run_dir: Path | None = None,
    case_inputs: dict | None = None,
) -> dict:
    started = utc_now()
    max_witnesses = int(limits.get("max_witnesses", 20000))
    max_checks = int(limits.get("max_checks", 5000000))
    max_contexts = int(limits.get("max_contexts", 200000))

    if case_inputs is not None:
        for key in ("grammar", "task"):
            if case_inputs[key]["sha256"] != case[key]["sha256"]:
                raise MachineOverviewError(f"SEARCH_INPUT_HASH_MISMATCH:{key}")

    raw, statistics = _enumerate_separations(
        grammar, order_seed=None, max_witnesses=max_witnesses, max_checks=max_checks, max_contexts=max_contexts
    )
    reduced = _reduced_set(raw, grammar)
    permuted_raw, permuted_statistics = _enumerate_separations(
        grammar, order_seed=order_seed, max_witnesses=max_witnesses, max_checks=max_checks, max_contexts=max_contexts
    )
    permuted_reduced = _reduced_set(permuted_raw, grammar)
    order_check = {
        "seed": order_seed,
        "order_independent_set_equal": set(permuted_reduced) == set(reduced),
        "statistics_match": permuted_statistics["separations_seen"] == statistics["separations_seen"],
    }

    grammar_disabled = json.loads(json.dumps(grammar))
    grammar_disabled["deadline_horizons"] = []
    mutated_statistics = _enumerate_separations(
        grammar_disabled, order_seed=None, max_witnesses=max_witnesses, max_checks=max_checks, max_contexts=max_contexts
    )[1]
    mutated_reduced = _reduced_set(
        _enumerate_separations(
            grammar_disabled, order_seed=None, max_witnesses=max_witnesses, max_checks=max_checks,
            max_contexts=max_contexts,
        )[0],
        grammar_disabled,
    )
    grammar_sensitivity = {
        "mutation": "remove the deadline operation from the declared grammar",
        "mutated_witness_count": len(mutated_reduced),
        "mutated_contains_deadline_kind": any(observation_mode(ops) == "deadline" for _, _, ops in mutated_reduced.values()),
        "mutated_statistics": mutated_statistics,
    }

    items = sorted(
        reduced.values(),
        key=lambda item: (_size(item[0], item[1], item[2])["context_ops"],
                          _size(item[0], item[1], item[2])["index_sum"],
                          _canonical(item[0], item[1], item[2])),
    )
    witnesses = [
        _witness_record(left, right, ops, f"WV-{index:04d}", grammar)
        for index, (left, right, ops) in enumerate(items, start=1)
    ]
    if any(w["grammar_membership"]["status"] != "WITHIN_DECLARED_GRAMMAR" for w in witnesses):
        raise MachineOverviewError("REDUCTION_LEFT_DECLARED_GRAMMAR")

    preserving = {"kind": "bind", "continuation": _keeping_continuation()}
    if items:
        control_left, control_right = items[0][0], items[0][1]
    else:
        control_left, control_right = ("omega",), ("omega",)
    preserved_ok, preserved_left, preserved_right = separates([preserving], control_left, control_right)
    positive_control = {
        "control": "bind_preserves_result_equivalence",
        "pair": {"left": value_to_json(control_left), "right": value_to_json(control_right)},
        "context": preserving,
        "preserved": not preserved_ok,
        "left_observation": value_to_json(preserved_left),
        "right_observation": value_to_json(preserved_right),
        "claim_ref": "C-71",
    }
    deadline_op = {"kind": "deadline", "k": _negative_control_horizon(control_left, control_right)}
    ok, observed_left, observed_right = separates([deadline_op], control_left, control_right)
    negative_control = {
        "control": "declared_deadline_does_not_separate_this_pair",
        "pair": {"left": value_to_json(control_left), "right": value_to_json(control_right)},
        "context": deadline_op,
        "separated": ok,
        "left_observation": value_to_json(observed_left),
        "right_observation": value_to_json(observed_right),
        "expected": "NOT_SEPARATED",
        "expectation_met": not ok,
    }

    inputs = {
        "case_sha256": sha256_file(case_path),
        "task_sha256": case["task"]["sha256"],
        "task_path": case["task"]["path"],
        "grammar_sha256": case["grammar"]["sha256"],
        "grammar_path": case["grammar"]["path"],
    }
    if case_inputs is not None:
        inputs["profile_sha256"] = case["profile"]["sha256"]
        inputs["verified_inputs"] = {
            key: {"path": case_inputs[key]["path"], "sha256": case_inputs[key]["sha256"]}
            for key in ("profile", "task", "grammar")
        }
    case_identity_sha256 = sha256_bytes(json.dumps({
        "case_id": case["case_id"], "revision": case["revision"],
        "task_sha256": case["task"]["sha256"], "grammar_sha256": case["grammar"]["sha256"],
    }, ensure_ascii=False, sort_keys=True).encode("utf-8"))

    exit_reason = (
        "COMPLETED_WITHIN_BUDGET" if statistics["complete_within_declared_grammar"]
        else "BUDGET_REACHED" if statistics["checks_budget_exhausted"] or statistics["context_budget_exhausted"]
        else "WITNESS_CAPTURE_LIMITED"
    )
    receipt = {
        "schema_version": "machine-overview-search-run/v1",
        "run_id": run_id,
        "kind": "search",
        "case_id": case["case_id"],
        "case_revision": case["revision"],
        "case_pointer": str(case_path),
        "case_identity_sha256": case_identity_sha256,
        "started_at_utc": started,
        "completed_at_utc": utc_now(),
        "coordinator_version": registry["coordinator_version"],
        "registry_id": registry["registry_id"],
        "profile": {
            "profile_id": profile_report["profile_id"],
            "profile_status": profile_report["status"],
            "toolchain_ref": profile_report["toolchain_ref"],
        },
        "inputs": inputs,
        "budget": {"max_witnesses": max_witnesses, "max_checks": max_checks, "max_contexts": max_contexts},
        "seed": order_seed,
        "statistics": statistics,
        "order_independence_check": order_check,
        "grammar_sensitivity_check": grammar_sensitivity,
        "calibration_match": _calibration_match(grammar, reduced),
        "witnesses": witnesses,
        "controls": {"positive": positive_control, "negative": negative_control},
        "exit_reason": exit_reason,
        "evidence_refs": [case_path.as_posix()],
        "git": git_state(repo_root),
    }
    if run_dir is not None:
        # The caller (CLI) owns run-directory exclusivity via begin_attempt;
        # an interrupted same-id attempt has already been rolled over there.
        run_dir.mkdir(parents=True, exist_ok=True)
        write_json(run_dir / "RUN.json", receipt)
    return receipt
