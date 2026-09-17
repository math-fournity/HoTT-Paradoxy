"""GEN-001-V2-1 generator chain over the declared L2-cofibration fragment.

Stage 2 of revision 015 §5: the first family chain (SUPPLY-009 / V2-A,
TASK-FAMILY-V2-EXISTENCE-VERSUS-AVAILABILITY, gate G-b).  This module is the
ENUMERATOR ONLY: it walks the *declared* V2 grammar, reduces candidates
grammar-preservingly and records out-of-envelope rejections against every
pre-existing delay grammar.  Oracle verdicts come from the native kernel
(``v2_verify``), never from this module (F-011 tightened by 015 §3.4 / 016 §2).
"""
from __future__ import annotations

import json
import random
from itertools import product
from pathlib import Path

from . import v2_cofibration as v2
from .util import MachineOverviewError, sha256_bytes, utc_now, write_json

# ---------------------------------------------------------------- grammar

REQUIRED_FIELDS = ("grammar_id", "delay_index_max", "declared_faces", "tower_levels",
                   "context_depth_max", "bind_continuations")


def load_grammar(path) -> dict:
    text = Path(path).read_text(encoding="utf-8")
    grammar = json.loads(text)
    missing = [f for f in REQUIRED_FIELDS if f not in grammar]
    if missing:
        raise MachineOverviewError(f"GRAMMAR_MISSING_FIELDS:{missing}")
    if grammar.get("backend") != "v2-l2-cofibration":
        raise MachineOverviewError(f"GRAMMAR_BACKEND_NOT_V2:{grammar.get('backend')}")
    return grammar


def new_continuation_ids(grammar: dict) -> list[str]:
    return [c["id"] for c in grammar["bind_continuations"]
            if "new" in str(c.get("role", "")).lower()]


# ---------------------------------------------------------------- denominator

def enumerate_atoms(grammar: dict) -> list[tuple]:
    """All declared V2 ground values (finite denominator)."""
    faces = [int(f) for f in grammar["declared_faces"]]
    levels = [int(l) for l in grammar["tower_levels"]]
    n_max = int(grammar["delay_index_max"])
    atoms: list[tuple] = []
    if grammar.get("include_omega", True):
        atoms.append(v2.omega())
    for n, b, face, level in product(range(n_max + 1), v2.BOOLS, faces, levels):
        atoms.append(v2.ret(n, b, face, level))
    return atoms


def _single_op_options(grammar: dict) -> list[dict]:
    options: list[dict] = []
    faces = [int(f) for f in grammar["declared_faces"]]
    levels = [int(l) for l in grammar["tower_levels"]]
    for partner in grammar.get("race_partners", []):
        pv = v2.value_from_json(partner)
        for direction in grammar.get("race_directions", ["race_left", "race_right"]):
            options.append({"kind": direction, "partner": dict(partner)})
    for continuation in grammar["bind_continuations"]:
        options.append({"kind": "bind", "continuation": dict(continuation["map"]),
                        "continuation_id": continuation["id"]})
    for horizon in grammar.get("deadline_horizons", []):
        options.append({"kind": "deadline", "k": int(horizon)})
    for face in faces:
        options.append({"kind": "supply", "face": face})
        options.append({"kind": "fill_of", "face": face})
    if "fill" in [o["kind"] for o in _fill_allowed(grammar)]:
        pass
    for level in levels:
        options.append({"kind": "tower", "level": level})
    for pair in grammar.get("between_pairs", []):
        options.append({"kind": "between", "a": int(pair[0]), "b": int(pair[1])})
    options.append({"kind": "fill"})
    return options


def _fill_allowed(grammar: dict) -> list[dict]:
    return [{"kind": "fill"}]


def enumerate_contexts(grammar: dict) -> list[list[dict]]:
    """All non-empty well-typed V2 contexts up to the declared depth.

    A context's observation mode is fixed by its LAST op (as in the L1
    fragment); ops that terminate the observation (fill / fill_of / tower /
    between / deadline) are not extended, which keeps the mode well-defined.
    """
    depth_max = int(grammar["context_depth_max"])
    terminal = {"deadline", "fill", "fill_of", "tower", "between"}
    options = _single_op_options(grammar)
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
    _, n, _b, face, level = value
    if not 0 <= n <= int(grammar["delay_index_max"]):
        return False
    if int(face) not in [int(f) for f in grammar["declared_faces"]]:
        return False
    if int(level) not in [int(l) for l in grammar["tower_levels"]]:
        return False
    return True


def _continuation_key(cont_map: dict) -> str:
    return json.dumps(cont_map, ensure_ascii=False, sort_keys=True)


def within_grammar_witness(ops: list[dict], left: tuple, right: tuple,
                           grammar: dict) -> tuple[bool, str | None]:
    """Whether a V2 candidate lies inside the declared V2 grammar."""
    if not ops:
        return False, "EMPTY_CONTEXT"
    if len(ops) > int(grammar["context_depth_max"]):
        return False, "CONTEXT_DEPTH"
    faces = [int(f) for f in grammar["declared_faces"]]
    levels = [int(l) for l in grammar["tower_levels"]]
    horizons = {int(k) for k in grammar.get("deadline_horizons", [])}
    partners = {json.dumps(p, ensure_ascii=False, sort_keys=True)
                 for p in grammar.get("race_partners", [])}
    declared_cont = {_continuation_key(c["map"]) for c in grammar["bind_continuations"]}
    between = {(int(a), int(b)) for a, b in grammar.get("between_pairs", [])}
    for value, label in ((left, "left"), (right, "right")):
        if not _value_within(value, grammar):
            return False, f"VALUE_OUT_OF_DECLARED_RANGE:{label}"
    for op in ops:
        kind = op.get("kind")
        if kind in ("race_left", "race_right"):
            if json.dumps(op["partner"], ensure_ascii=False, sort_keys=True) not in partners:
                return False, "RACE_PARTNER"
        elif kind == "bind":
            if _continuation_key(op["continuation"]) not in declared_cont:
                return False, "BIND_CONTINUATION"
        elif kind == "deadline":
            if int(op["k"]) not in horizons:
                return False, "DEADLINE_PARAMETER"
        elif kind == "supply":
            if int(op["face"]) not in faces:
                return False, "SUPPLY_FACE"
        elif kind == "fill":
            pass
        elif kind == "fill_of":
            if int(op["face"]) not in faces:
                return False, "FILL_OF_FACE"
        elif kind == "tower":
            if int(op["level"]) not in levels:
                return False, "TOWER_LEVEL"
        elif kind == "between":
            if (int(op["a"]), int(op["b"])) not in between:
                return False, "BETWEEN_PAIR"
        else:
            return False, f"UNKNOWN_OP:{kind}"
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


def _is_guarded(op: dict, grammar: dict | None) -> bool:
    if not grammar:
        return False
    guard = grammar.get("reduction_guard", {})
    if op["kind"] in guard.get("never_drop_kinds", []):
        return True
    if op["kind"] == "bind":
        for continuation in grammar.get("bind_continuations", []):
            if continuation["id"] in guard.get("never_drop_continuation_ids", []) \
                    and op["continuation"] == continuation["map"]:
                return True
    return False


def _reduce_index(value: tuple) -> tuple | None:
    if value[0] == "ret" and value[1] > 0:
        return v2.ret(value[1] - 1, value[2], value[3], value[4])
    return None


def reduce_witness(left: tuple, right: tuple, ops: list[dict],
                   grammar: dict | None = None) -> tuple[tuple, tuple, list[dict]]:
    """Greedy size reduction that never leaves the declared V2 grammar."""
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
            kind = op["kind"]
            if kind in ("race_left", "race_right"):
                partner = v2.value_from_json(op["partner"])
                cand = _reduce_index(partner)
                if cand is not None:
                    candidate = {**op, "partner": v2.value_to_json(cand)}
                    new_ops = list(ops); new_ops[index] = candidate
                    if _witness_separates(left, right, new_ops, grammar):
                        ops = new_ops; changed = True
            elif kind == "bind":
                continuation = v2.continuation_from_json(op["continuation"])
                for key in (True, False):
                    value = continuation[key]
                    cand = _reduce_index(value)
                    if cand is not None:
                        new_cont = dict(continuation); new_cont[key] = cand
                        candidate = {**op, "continuation": v2.continuation_to_json(new_cont)}
                        new_ops = list(ops); new_ops[index] = candidate
                        if _witness_separates(left, right, new_ops, grammar):
                            ops = new_ops; changed = True
            elif kind in ("deadline", "tower"):
                if int(op.get("k", op.get("level", 0))) > 0:
                    key = "k" if "k" in op else "level"
                    candidate = {**op, key: int(op[key]) - 1}
                    new_ops = list(ops); new_ops[index] = candidate
                    if _witness_separates(left, right, new_ops, grammar):
                        ops = new_ops; changed = True
        if len(ops) > 1:
            for index in range(len(ops)):
                if _is_guarded(ops[index], grammar):
                    continue
                new_ops = ops[:index] + ops[index + 1:]
                if _witness_separates(left, right, new_ops, grammar):
                    ops = new_ops; changed = True
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
        if op["kind"] in ("race_left", "race_right"):
            partner = v2.value_from_json(op["partner"])
            index_sum += partner[1] if partner[0] == "ret" else 0
        elif op["kind"] == "bind":
            for key in ("true", "false"):
                value = v2.value_from_json(op["continuation"][key])
                index_sum += value[1] if value[0] == "ret" else 0
        elif op["kind"] in ("deadline", "tower"):
            index_sum += int(op.get("k", op.get("level", 0)))
    return {"context_ops": len(ops), "index_sum": index_sum}


def witness_record(left: tuple, right: tuple, ops: list[dict], witness_id: str,
                   grammar: dict | None = None) -> dict:
    separated, observed_left, observed_right, kind = v2.separates(ops, left, right)
    if not separated:
        raise MachineOverviewError("WITNESS_DOES_NOT_SEPARATE")
    membership = {"status": "WITHIN_DECLARED_GRAMMAR", "reason": None}
    if grammar is not None:
        inside, reason = within_grammar_witness(ops, left, right, grammar)
        membership = {"status": "WITHIN_DECLARED_GRAMMAR" if inside else "OUTSIDE_DECLARED_GRAMMAR",
                      "reason": reason}
    bound_continuation = None
    for continuation in (grammar or {}).get("bind_continuations", []):
        for op in ops:
            if op.get("kind") == "bind" and op["continuation"] == continuation["map"]:
                bound_continuation = continuation["id"]
    record = {
        "witness_id": witness_id,
        "pair": {"left": v2.value_to_json(left), "right": v2.value_to_json(right)},
        "ops": ops,
        "observation_mode": v2.observation_mode(ops),
        "left_observation": observed_left,
        "right_observation": observed_right,
        "separation_kind": kind,
        "bound_continuation": bound_continuation,
        "size": _size(left, right, ops),
        "grammar_membership": membership,
    }
    record["ast_sha256"] = sha256_bytes(_canonical(left, right, ops).encode("utf-8"))
    return record




def _l1_value_json(value: tuple) -> dict:
    """JSON of a V2 value after L1 erasure (delay axis only)."""
    if value[0] == "omega":
        return {"kind": "omega"}
    return {"kind": "ret", "n": value[1], "value": value[2]}


# ---------------------------------------------------------------- L1 erasure

def l1_erase(value: tuple) -> tuple:
    """Erase the structural axis: a V2 value becomes its L1 delay value."""
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
    benchmark = grammar.get("calibration_benchmark")
    if not benchmark:
        return {"status": "NOT_DECLARED"}
    left = v2.value_from_json(benchmark["pair"]["left"])
    right = v2.value_from_json(benchmark["pair"]["right"])
    left, right, ops = reduce_witness(left, right, benchmark["ops"], grammar)
    key = _canonical(left, right, ops)
    return {"status": "PRESENT" if key in reduced else "ABSENT",
            "benchmark_id": benchmark.get("id"),
            "reduced_key": key, "matched_witness": key in reduced}


def _continuation_map_coverage(grammar: dict) -> dict:
    """Map-uniqueness for the declared V2 continuations (014 §2.1, recomputed
    for the V2 map space).  Two levels: V2 maps must be mutually distinct; and
    their L1 erasures must not collide with any pre-existing grammar's declared
    continuation maps."""
    conts = grammar["bind_continuations"]
    v2_keys = [_continuation_key(c["map"]) for c in conts]
    distinct_v2 = len(set(v2_keys)) == len(v2_keys)
    erased = {}
    for c in conts:
        erased[c["id"]] = {k: _l1_value_json(v2.value_from_json(v))
                           for k, v in c["map"].items()}
    return {"continuation_count": len(conts),
            "v2_maps_mutually_distinct": distinct_v2,
            "erased_maps": erased}


def out_of_envelope_check(witnesses: list[dict], existing_grammars: dict,
                          l1_within_grammar) -> dict:
    """Mechanical membership check of every witness against every pre-existing
    delay grammar using the L1 membership predicate (011 §2).  Records the
    rejection reason per grammar and whether the reason is unique."""
    rows = []
    for witness in witnesses:
        per_grammar: dict[str, dict] = {}
        reasons: dict[str, int] = {}
        for name, grammar in existing_grammars.items():
            left = v2.value_from_json(witness["pair"]["left"])
            right = v2.value_from_json(witness["pair"]["right"])
            ops = [dict(op) for op in witness["ops"]]
            try:
                inside, reason = l1_within_grammar(ops, left, right, grammar)
            except Exception as exc:  # L1 parser rejects V2 shapes outright
                inside, reason = False, f"L1_PARSE_REJECT:{type(exc).__name__}"
            per_grammar[name] = {"inside": inside, "reason": reason}
            reasons[reason] = reasons.get(reason, 0) + 1
        rows.append({
            "witness_id": witness["witness_id"],
            "separation_kind": witness["separation_kind"],
            "bound_continuation": witness.get("bound_continuation"),
            "l1_invisible": l1_invisible(v2.value_from_json(witness["pair"]["left"]),
                                         v2.value_from_json(witness["pair"]["right"])),
            "per_grammar": per_grammar,
            "reasons": reasons,
            "reason_unique": len(reasons) == 1,
            "accepted_by_any": any(r["inside"] for r in per_grammar.values()),
        })
    unique_all = all(r["reason_unique"] for r in rows)
    rejected_all = not any(r["accepted_by_any"] for r in rows)
    return {
        "proof_kind": "mechanical_membership_check",
        "claim": ("Every reduced witness of the V2-A family lies outside every "
                  "pre-existing delay grammar, with a unique rejection reason"),
        "method": "machine_overview.search.within_grammar_witness (L1 predicate) evaluated "
                  "for each witness against each pre-existing delay grammar; V2 values are "
                  "erased to their delay axis and V2 continuations to their delay maps by "
                  "the L1 reader, which is exactly the claim being tested",
        "existing_grammar_count": len(existing_grammars),
        "rows": rows,
        "unique_reason_count": sum(1 for r in rows if r["reason_unique"]),
        "rejected_by_all_count": sum(1 for r in rows if not r["accepted_by_any"]),
        "all_reasons_unique": unique_all,
        "all_rejected": rejected_all,
    }


def compute_search_semantics(grammar: dict, limits: dict,
                             order_seed: int | None = 20260913) -> dict:
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
        "continuation_map_coverage": _continuation_map_coverage(grammar),
        "witnesses": witnesses,
        "reduced_count": len(witnesses),
        "order_seed": order_seed,
    }


def order_independence(grammar: dict, limits: dict) -> dict:
    """Re-run with a different seed: statistics must match and the reduced
    witness set must be equal (order-independent completeness)."""
    a = compute_search_semantics(grammar, limits, order_seed=20260913)
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
