"""Generator chain for the DM3 fragment (gap-A acceptance unit).

Modeled on ``v2_chain`` but driven by ``v2_dm3`` and the DM3 grammar.  This
module is the ENUMERATOR ONLY: it walks the *declared* DM3 grammar, reduces
witnesses grammar-preservingly, and records out-of-envelope rejections against
every pre-existing delay grammar and the point-set V2 grammar.  Oracle
verdicts come from the native kernel (``v2_dm3_verify``), never from this
module (F-011 tightened by 015 sec 3.4 / 016 sec 2 / 018 sec 3A).
"""
from __future__ import annotations

import json
import random
from itertools import product
from pathlib import Path

from . import v2_dm3 as v2
from .util import MachineOverviewError, sha256_bytes

ENGINE_ROOT = Path("/Volumes/D/HoTT-machine-overview/machine-overview")

REQUIRED_FIELDS = ("grammar_id", "delay_index_max", "dm3_elements", "tower_levels",
                   "context_depth_max")


def load_grammar(path) -> dict:
    text = Path(path).read_text(encoding="utf-8")
    grammar = json.loads(text)
    missing = [f for f in REQUIRED_FIELDS if f not in grammar]
    if missing:
        raise MachineOverviewError(f"DM3_GRAMMAR_MISSING_FIELDS:{missing}")
    if grammar.get("backend") != "v2-dm3":
        raise MachineOverviewError(f"GRAMMAR_BACKEND_NOT_DM3:{grammar.get('backend')}")
    return grammar


# ---------------------------------------------------------------- denominator

def enumerate_atoms(grammar: dict) -> list[tuple]:
    """All declared DM3 ground values (finite denominator): omega plus
    ret(n, b, d, level); 1 + 3*2*3*3 = 55."""
    dm3s = [int(d) for d in grammar["dm3_elements"]]
    levels = [int(l) for l in grammar["tower_levels"]]
    n_max = int(grammar["delay_index_max"])
    atoms: list[tuple] = []
    if grammar.get("include_omega", True):
        atoms.append(v2.omega())
    for n, b, d, level in product(range(n_max + 1), v2.BOOLS, dm3s, levels):
        atoms.append(v2.ret(n, b, d, level))
    return atoms


def single_op_options(grammar: dict) -> list[dict]:
    options: list[dict] = []
    dm3s = [int(d) for d in grammar["dm3_elements"]]
    levels = [int(l) for l in grammar["tower_levels"]]
    for d in dm3s:
        options.append({"kind": "supply", "d": d})
    options.append({"kind": "fill"})
    for level in levels:
        options.append({"kind": "tower", "level": level})
    for pair in grammar.get("between_pairs", []):
        options.append({"kind": "between", "a": int(pair[0]), "b": int(pair[1])})
    return options


def enumerate_contexts(grammar: dict) -> list[list[dict]]:
    """All non-empty well-typed DM3 contexts up to the declared depth.

    The observation mode is fixed by the LAST op (as in the L1 fragment and
    the point-set V2 fragment); terminal ops (fill / tower / between) are not
    extended, which keeps the mode well-defined."""
    depth_max = int(grammar["context_depth_max"])
    terminal = set(v2.TERMINAL_OPS)
    options = single_op_options(grammar)
    frontier: list[list[dict]] = [[]]
    contexts: list[list[dict]] = []
    for _ in range(depth_max):
        nxt: list[list[dict]] = []
        for prefix in frontier:
            for op in options:
                candidate = prefix + [op]
                contexts.append(candidate)
                if op["kind"] not in terminal:
                    nxt.append(candidate)
        frontier = nxt
    return contexts


# ---------------------------------------------------------------- membership

def _value_within(value: tuple, grammar: dict) -> bool:
    if value[0] == "omega":
        return bool(grammar.get("include_omega", True))
    if value[0] != "ret":
        return False
    _, n, _b, d, level = value
    if not 0 <= n <= int(grammar["delay_index_max"]):
        return False
    if int(d) not in [int(x) for x in grammar["dm3_elements"]]:
        return False
    if int(level) not in [int(x) for x in grammar["tower_levels"]]:
        return False
    return True


def within_grammar_witness(ops: list[dict], left: tuple, right: tuple,
                           grammar: dict) -> tuple[bool, str | None]:
    """Whether a DM3 candidate lies inside the declared DM3 grammar."""
    if not ops:
        return False, "EMPTY_CONTEXT"
    if len(ops) > int(grammar["context_depth_max"]):
        return False, "CONTEXT_DEPTH"
    dm3s = [int(x) for x in grammar["dm3_elements"]]
    levels = [int(x) for x in grammar["tower_levels"]]
    between = {(int(a), int(b)) for a, b in grammar.get("between_pairs", [])}
    for value, label in ((left, "left"), (right, "right")):
        if not _value_within(value, grammar):
            return False, f"VALUE_OUT_OF_DECLARED_RANGE:{label}"
    for op in ops:
        kind = op.get("kind")
        if kind == "supply":
            if int(op["d"]) not in dm3s:
                return False, "SUPPLY_DM3_ELEMENT"
        elif kind == "fill":
            pass
        elif kind == "tower":
            if int(op["level"]) not in levels:
                return False, "TOWER_LEVEL"
        elif kind == "between":
            if (int(op["a"]), int(op["b"])) not in between:
                return False, "BETWEEN_PAIR"
        else:
            return False, f"UNKNOWN_DM3_OP:{kind}"
    return True, None


# ---------------------------------------------------------------- reduction

def _witness_separates(left: tuple, right: tuple, ops: list[dict],
                       grammar: dict | None) -> bool:
    if left == right or not ops or not v2.delay_equivalent(left, right):
        return False
    if grammar is not None:
        ok, _ = within_grammar_witness(ops, left, right, grammar)
        if not ok:
            return False
    ok, _, _, _ = v2.separates(ops, left, right)
    return ok


def _reduce_index(value: tuple) -> tuple | None:
    if value[0] == "ret" and value[1] > 0:
        return v2.ret(value[1] - 1, value[2], value[3], value[4])
    return None


def reduce_witness(left: tuple, right: tuple, ops: list[dict],
                   grammar: dict | None = None) -> tuple[tuple, tuple, list[dict]]:
    """Greedy size reduction that never leaves the declared DM3 grammar and
    never destroys the separation (mirrors v2_chain.reduce_witness)."""
    ops = [dict(op) for op in ops]
    changed = True
    while changed:
        changed = False
        for index in (0, 1):
            current = left if index == 0 else right
            cand = _reduce_index(current)
            if cand is not None:
                new_left, new_right = (cand, right) if index == 0 else (left, cand)
                if _witness_separates(new_left, new_right, ops, grammar):
                    left, right = new_left, new_right
                    changed = True
        for index, op in enumerate(ops):
            if op["kind"] == "tower" and int(op["level"]) > 0:
                candidate = {**op, "level": int(op["level"]) - 1}
                new_ops = list(ops)
                new_ops[index] = candidate
                if _witness_separates(left, right, new_ops, grammar):
                    ops = new_ops
                    changed = True
        if len(ops) > 1:
            for index in range(len(ops)):
                new_ops = ops[:index] + ops[index + 1:]
                if _witness_separates(left, right, new_ops, grammar):
                    ops = new_ops
                    changed = True
                    break
    return left, right, ops


# ---------------------------------------------------------------- records

def _canonical(left: tuple, right: tuple, ops: list[dict]) -> str:
    return json.dumps({"left": v2.value_to_json(left), "right": v2.value_to_json(right),
                       "ops": ops}, ensure_ascii=False, sort_keys=True)


def _size(left: tuple, right: tuple, ops: list[dict]) -> dict:
    index_sum = 0
    for value in (left, right):
        index_sum += value[1] if value[0] == "ret" else 0
    for op in ops:
        if op["kind"] == "tower":
            index_sum += int(op["level"])
    return {"context_ops": len(ops), "index_sum": index_sum}


def witness_record(left: tuple, right: tuple, ops: list[dict], witness_id: str,
                   grammar: dict | None = None) -> dict:
    separated, observed_left, observed_right, kind = v2.separates(ops, left, right)
    if not separated:
        raise MachineOverviewError("DM3_WITNESS_DOES_NOT_SEPARATE")
    membership = {"status": "WITHIN_DECLARED_GRAMMAR", "reason": None}
    if grammar is not None:
        inside, reason = within_grammar_witness(ops, left, right, grammar)
        membership = {"status": "WITHIN_DECLARED_GRAMMAR" if inside else "OUTSIDE_DECLARED_GRAMMAR",
                      "reason": reason}
    record = {
        "witness_id": witness_id,
        "pair": {"left": v2.value_to_json(left), "right": v2.value_to_json(right)},
        "ops": ops,
        "observation_mode": v2.observation_mode(ops),
        "left_observation": observed_left,
        "right_observation": observed_right,
        "separation_kind": kind,
        "size": _size(left, right, ops),
        "grammar_membership": membership,
    }
    record["ast_sha256"] = sha256_bytes(_canonical(left, right, ops).encode("utf-8"))
    return record


# ---------------------------------------------------------------- L1 erasure

def l1_erase(value: tuple) -> tuple:
    """Erase the structural axis: a DM3 value becomes its L1 delay value."""
    if value[0] == "omega":
        return ("omega",)
    return ("ret", value[1], value[2])


def l1_invisible(left: tuple, right: tuple) -> bool:
    """The pair is IDENTICAL after L1 erasure, so no delay grammar (which only
    sees the computation axis) can ever separate it, whatever its context."""
    return l1_erase(left) == l1_erase(right)


# ---------------------------------------------------------------- search

def _enumerate_separations(grammar: dict, *, order_seed, max_witnesses, max_checks,
                           max_contexts) -> tuple[list[dict], dict]:
    atoms = enumerate_atoms(grammar)
    contexts_all = enumerate_contexts(grammar)
    context_budget_exhausted = len(contexts_all) > max_contexts
    contexts = contexts_all[:max_contexts] if context_budget_exhausted else list(contexts_all)
    if order_seed is not None:
        rng = random.Random(order_seed)
        rng.shuffle(atoms)
        rng.shuffle(contexts)
    equivalent_pairs = [(l, r) for l in atoms for r in atoms
                        if l != r and v2.delay_equivalent(l, r)]
    checks_planned = len(contexts_all) * len(equivalent_pairs)

    raw: list[dict] = []
    separator_count = 0
    grammar_violations: list[dict] = []
    checks_executed = 0
    contexts_examined = 0
    checks_budget_exhausted = False
    capture_truncated = False
    kind_histogram: dict[str, int] = {}

    for ops in contexts:
        if checks_executed >= max_checks:
            checks_budget_exhausted = True
            break
        contexts_examined += 1
        for left, right in equivalent_pairs:
            if checks_executed >= max_checks:
                checks_budget_exhausted = True
                break
            checks_executed += 1
            inside, reason = within_grammar_witness(ops, left, right, grammar)
            if not inside:
                grammar_violations.append({"ops": ops, "reason": reason})
                continue
            separated, ol, orr, kind = v2.separates(ops, left, right)
            if separated:
                separator_count += 1
                kind_histogram[kind] = kind_histogram.get(kind, 0) + 1
                if len(raw) < max_witnesses:
                    raw.append({"left": left, "right": right, "ops": [dict(op) for op in ops]})
                else:
                    capture_truncated = True
        if checks_budget_exhausted:
            break

    complete = (not checks_budget_exhausted and not context_budget_exhausted
                and not capture_truncated
                and contexts_examined == len(contexts_all)
                and checks_executed == checks_planned)
    statistics = {
        "v2_atoms": len(atoms),
        "contexts": len(contexts_all),
        "contexts_examined": contexts_examined,
        "equivalent_pairs": len(equivalent_pairs),
        "pair_context_checks": checks_executed,
        "checks_planned": checks_planned,
        "separations_seen": separator_count,
        "separation_kind_histogram": kind_histogram,
        "witnesses_captured": len(raw),
        "witness_capture_truncated": capture_truncated,
        "context_budget_exhausted": context_budget_exhausted,
        "checks_budget_exhausted": checks_budget_exhausted,
        "truncated": checks_budget_exhausted or context_budget_exhausted or capture_truncated,
        "complete_within_declared_grammar": complete,
        "grammar_violations": len(grammar_violations),
    }
    return raw, statistics


def _reduced_set(raw: list[dict], grammar: dict | None = None):
    reduced: dict[str, tuple] = {}
    for item in raw:
        left, right, ops = reduce_witness(item["left"], item["right"], item["ops"], grammar)
        reduced.setdefault(_canonical(left, right, ops), (left, right, ops))
    return reduced


def _calibration_match(grammar: dict, reduced: dict) -> dict:
    """The three mirror-declared witnesses (formal/V2DM3.agda sec 6) must be
    present in the reduced search set: the search must FIND the calibration
    benchmarks, proving the denominator and the canonical semantics cover the
    kernel-checked witnesses."""
    benchmark = grammar.get("calibration_benchmark")
    if not benchmark:
        return {"status": "NOT_DECLARED"}
    rows = []
    for entry in benchmark["witnesses"]:
        left = v2.value_from_json(entry["left"])
        right = v2.value_from_json(entry["right"])
        left, right, ops = reduce_witness(left, right, entry["ops"], grammar)
        key = _canonical(left, right, ops)
        rows.append({"witness_id": entry["witness_id"],
                     "reduced_key": key,
                     "present": key in reduced})
    return {"status": "ALL_PRESENT" if all(r["present"] for r in rows) else "MISSING",
            "rows": rows}


def out_of_envelope_check(witnesses: list[dict], existing_grammars: dict,
                          membership_predicates: dict) -> dict:
    """Mechanical membership check of every witness against every pre-existing
    grammar.  ``membership_predicates`` maps grammar name -> (predicate, kind)
    where kind is ``l1`` (delay reader) or ``v2-point-set``.  Records the
    rejection reason per grammar and whether the reason is unique."""
    rows = []
    for witness in witnesses:
        per_grammar: dict[str, dict] = {}
        reasons: dict[str, int] = {}
        for name, grammar in existing_grammars.items():
            predicate, kind = membership_predicates[name]
            left = v2.value_from_json(witness["pair"]["left"])
            right = v2.value_from_json(witness["pair"]["right"])
            ops = [dict(op) for op in witness["ops"]]
            if kind == "l1":
                # delay readers see the erasure of the DM3 value
                left, right = l1_erase(left), l1_erase(right)
            try:
                inside, reason = predicate(ops, left, right, grammar)
            except Exception as exc:
                inside, reason = False, f"PARSE_REJECT:{type(exc).__name__}"
            per_grammar[name] = {"inside": inside, "reason": reason,
                                 "membership_kind": kind}
            # reasons keys must be strings for JSON serialization; an accepted
            # grammar contributes the literal key "ACCEPTED" (the witness is
            # mechanically inside that grammar: a shared mechanism, ingress)
            reason_key = reason if reason is not None else "ACCEPTED"
            reasons[reason_key] = reasons.get(reason_key, 0) + 1
        rows.append({
            "witness_id": witness["witness_id"],
            "separation_kind": witness["separation_kind"],
            "l1_invisible": l1_invisible(v2.value_from_json(witness["pair"]["left"]),
                                         v2.value_from_json(witness["pair"]["right"])),
            "per_grammar": per_grammar,
            "reasons": reasons,
            "reason_unique": len(reasons) == 1,
            "accepted_by_any": any(r["inside"] for r in per_grammar.values()),
        })
    return {
        "proof_kind": "mechanical_membership_check",
        "claim": ("Every reduced DM3 witness lies outside every pre-existing delay "
                  "grammar and outside the point-set V2 grammar, with rejection "
                  "reasons recorded per grammar"),
        "method": ("machine_overview.search.within_grammar_witness (L1 predicate, values "
                   "erased to their delay axis) for the delay grammars; "
                   "machine_overview.v2_chain.within_grammar_witness (point-set predicate) "
                   "for the V2 point-set grammar, which cannot parse DM3 ops or represent "
                   "the DM3 algebra (see no_point_set_embedding)"),
        "existing_grammar_count": len(existing_grammars),
        "rows": rows,
        "unique_reason_count": sum(1 for r in rows if r["reason_unique"]),
        "rejected_by_all_count": sum(1 for r in rows if not r["accepted_by_any"]),
        "all_reasons_unique": all(r["reason_unique"] for r in rows),
        "all_rejected": not any(r["accepted_by_any"] for r in rows),
    }


def compute_search_semantics(grammar: dict, limits: dict,
                             order_seed: int | None = 20260917) -> dict:
    max_witnesses = int(limits.get("max_witnesses", 20000))
    max_checks = int(limits.get("max_checks", 5000000))
    max_contexts = int(limits.get("max_contexts", 200000))
    if min(max_witnesses, max_checks, max_contexts) < 0:
        raise MachineOverviewError("SEARCH_BUDGET_NEGATIVE")
    raw, statistics = _enumerate_separations(
        grammar, order_seed=order_seed, max_witnesses=max_witnesses,
        max_checks=max_checks, max_contexts=max_contexts)
    reduced = _reduced_set(raw, grammar)
    witnesses = []
    for index, (left, right, ops) in enumerate(sorted(reduced.values(),
                                                     key=lambda t: _size(t[0], t[1], t[2])["index_sum"]),
                                               start=1):
        witnesses.append(witness_record(left, right, ops, f"WV-{index:04d}", grammar))
    return {
        "statistics": statistics,
        "calibration_match": _calibration_match(grammar, reduced),
        "witnesses": witnesses,
        "reduced_count": len(witnesses),
        "order_seed": order_seed,
    }


def order_independence(grammar: dict, limits: dict) -> dict:
    """Re-run with a different seed: statistics must match and the reduced
    witness set must be equal (order-independent completeness)."""
    a = compute_search_semantics(grammar, limits, order_seed=20260917)
    b = compute_search_semantics(grammar, limits, order_seed=777)
    keys_a = {w["ast_sha256"] for w in a["witnesses"]}
    keys_b = {w["ast_sha256"] for w in b["witnesses"]}
    stats_match = (a["statistics"]["pair_context_checks"] == b["statistics"]["pair_context_checks"]
                   and a["statistics"]["separations_seen"] == b["statistics"]["separations_seen"])
    return {
        "statistics_match": stats_match,
        "witness_sets_equal": keys_a == keys_b,
        "counts": [len(keys_a), len(keys_b)],
        "separations": [a["statistics"]["separations_seen"], b["statistics"]["separations_seen"]],
    }
