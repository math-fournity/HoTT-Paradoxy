"""Typed enumerator, counterexample search and candidate reduction.

The search walks the *declared* grammar only.  It never consults the known
calibration answer while generating candidates; the known result is used after
the fact as an external benchmark (``calibration_match``).
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
from .util import MachineOverviewError, git_state, sha256_file, utc_now, write_json


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
    """All non-empty contexts up to the declared depth (innermost op first)."""
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


def _witness_separates(left: tuple, right: tuple, ops: list[dict]) -> bool:
    if left == right or not ops or not delay_equivalent(left, right):
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
    """Greedy size reduction: shrink indices, then parameters, then drop ops."""
    ops = [dict(op) for op in ops]
    changed = True
    while changed:
        changed = False
        for index in (0, 1):
            current = left if index == 0 else right
            if current[0] == "ret" and current[1] > 0:
                candidate = ret(current[1] - 1, current[2])
                new_left, new_right = (candidate, right) if index == 0 else (left, candidate)
                if _witness_separates(new_left, new_right, ops):
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
                    if _witness_separates(left, right, new_ops):
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
                        if _witness_separates(left, right, new_ops):
                            ops = new_ops
                            changed = True
            elif kind == "deadline" and op["k"] > 0:
                candidate = {**op, "k": op["k"] - 1}
                new_ops = list(ops)
                new_ops[index] = candidate
                if _witness_separates(left, right, new_ops):
                    ops = new_ops
                    changed = True
        if len(ops) > 1:
            for index in range(len(ops)):
                if _is_guarded(ops[index], grammar):
                    continue
                new_ops = ops[:index] + ops[index + 1:]
                if _witness_separates(left, right, new_ops):
                    ops = new_ops
                    changed = True
                    break
    return left, right, ops


def _canonical(left: tuple, right: tuple, ops: list[dict]) -> str:
    payload = {
        "left": value_to_json(left),
        "right": value_to_json(right),
        "ops": ops,
    }
    return json.dumps(payload, ensure_ascii=False, sort_keys=True)


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


def _witness_record(left: tuple, right: tuple, ops: list[dict], witness_id: str) -> dict:
    ok, observed_left, observed_right = separates(ops, left, right)
    if not ok:
        raise MachineOverviewError("WITNESS_DOES_NOT_SEPARATE")
    return {
        "witness_id": witness_id,
        "pair": {"left": value_to_json(left), "right": value_to_json(right)},
        "ops": ops,
        "observation_mode": observation_mode(ops),
        "left_observation": value_to_json(observed_left),
        "right_observation": value_to_json(observed_right),
        "separation_kind": separation_kind(ops, observed_left, observed_right),
        "size": _size(left, right, ops),
    }


def _enumerate_separations(
    grammar: dict,
    *,
    order_seed: int | None,
    max_witnesses: int,
    max_checks: int,
) -> tuple[list[dict], dict]:
    atoms = enumerate_atoms(grammar)
    contexts = enumerate_contexts(grammar)
    if order_seed is not None:
        rng = random.Random(order_seed)
        shuffled_atoms = list(atoms)
        shuffled_contexts = list(contexts)
        rng.shuffle(shuffled_atoms)
        rng.shuffle(shuffled_contexts)
        atoms, contexts = shuffled_atoms, shuffled_contexts

    checks = 0
    truncated = False
    raw: list[dict] = []
    separator_count = 0
    for ops in contexts:
        mode = observation_mode(ops)
        for left in atoms:
            for right in atoms:
                if left == right or not delay_equivalent(left, right):
                    continue
                checks += 1
                if checks > max_checks:
                    truncated = True
                    break
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
            if truncated:
                break
        if truncated:
            break
    statistics = {
        "delay_atoms": len(atoms),
        "contexts": len(contexts),
        "pair_context_checks": checks,
        "separations_seen": separator_count,
        "witnesses_captured": len(raw),
        "complete_within_declared_grammar": separator_count == len(raw),
        "truncated": truncated,
    }
    return raw, statistics


def _reduced_set(raw: list[dict], grammar: dict | None = None) -> dict[str, tuple[tuple, tuple, list[dict]]]:
    reduced: dict[str, tuple[tuple, tuple, list[dict]]] = {}
    for item in raw:
        left, right, ops = reduce_witness(item["left"], item["right"], item["ops"], grammar)
        reduced.setdefault(_canonical(left, right, ops), (left, right, ops))
    return reduced


def _keeping_continuation() -> dict:
    """The completion-preserving consumer: keeps value and convergence."""
    return {
        "true": value_to_json(ret(0, True)),
        "false": value_to_json(ret(0, False)),
    }


def _negative_control_horizon(left: tuple, right: tuple) -> int:
    """A horizon that cannot separate a result-equivalent pair."""
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
) -> dict:
    started = utc_now()
    max_witnesses = int(limits.get("max_witnesses", 200))
    max_checks = int(limits.get("max_checks", 500000))

    raw, statistics = _enumerate_separations(
        grammar, order_seed=None, max_witnesses=max_witnesses, max_checks=max_checks
    )
    reduced = _reduced_set(raw, grammar)
    permuted_raw, permuted_statistics = _enumerate_separations(
        grammar, order_seed=order_seed, max_witnesses=max_witnesses, max_checks=max_checks
    )
    permuted_reduced = _reduced_set(permuted_raw, grammar)
    order_check = {
        "seed": order_seed,
        "order_independent_set_equal": set(permuted_reduced) == set(reduced),
        "statistics_match": permuted_statistics["separations_seen"] == statistics["separations_seen"],
    }

    grammar_disabled = json.loads(json.dumps(grammar))
    grammar_disabled["deadline_horizons"] = []
    mutated_reduced = _reduced_set(
        _enumerate_separations(grammar_disabled, order_seed=None, max_witnesses=max_witnesses, max_checks=max_checks)[0],
        grammar_disabled,
    )
    grammar_sensitivity = {
        "mutation": "remove the deadline operation from the declared grammar",
        "mutated_witness_count": len(mutated_reduced),
        "mutated_contains_deadline_kind": any(
            observation_mode(ops) == "deadline" for _, _, ops in mutated_reduced.values()
        ),
    }

    items = sorted(
        reduced.values(),
        key=lambda item: (_size(item[0], item[1], item[2])["context_ops"], _size(item[0], item[1], item[2])["index_sum"],
                          _canonical(item[0], item[1], item[2])),
    )
    witnesses = [
        _witness_record(left, right, ops, f"WV-{index:04d}")
        for index, (left, right, ops) in enumerate(items, start=1)
    ]

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

    receipt = {
        "schema_version": "machine-overview-search-run/v1",
        "run_id": run_id,
        "kind": "search",
        "case_id": case["case_id"],
        "case_revision": case["revision"],
        "case_pointer": str(case_path),
        "started_at_utc": started,
        "completed_at_utc": utc_now(),
        "coordinator_version": registry["coordinator_version"],
        "registry_id": registry["registry_id"],
        "profile": {
            "profile_id": profile_report["profile_id"],
            "profile_status": profile_report["status"],
            "toolchain_ref": profile_report["toolchain_ref"],
        },
        "inputs": {
            "case_sha256": sha256_file(case_path),
            "grammar_path": case["grammar"]["path"],
            "grammar_sha256": case["grammar"]["sha256"],
            "task_path": case["task"]["path"],
            "task_sha256": case["task"]["sha256"],
        },
        "budget": {"max_witnesses": max_witnesses, "max_checks": max_checks},
        "seed": order_seed,
        "statistics": statistics,
        "order_independence_check": order_check,
        "grammar_sensitivity_check": grammar_sensitivity,
        "calibration_match": _calibration_match(grammar, reduced),
        "witnesses": witnesses,
        "controls": {"positive": positive_control, "negative": negative_control},
        "exit_reason": "BUDGET_REACHED" if statistics["truncated"] else "COMPLETED_WITHIN_BUDGET",
        "evidence_refs": [],
        "git": git_state(repo_root),
    }
    receipt["evidence_refs"] = [case_path.as_posix()]
    if run_dir is not None:
        run_dir.mkdir(parents=True, exist_ok=False)
        write_json(run_dir / "RUN.json", receipt)
    return receipt
