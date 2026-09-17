"""Semantics of the DM3-valued V2 fragment (gap-A acceptance unit).

Mirror/enumerator pair: ``formal/V2DM3.agda`` is the SPECIFICATION half
(checked by the Cubical Agda 2.8.0 native kernel); this module is the
ENUMERATOR half and must agree with it item-by-item.  ``tests/test_v2_dm3.py``
checks the three declared witnesses, their same-value controls, the delay-axis
invisibility, the finiteness of the denominator and the algebraic
non-embedding of DM3 into the point-set face lattice.

Gap A (revision 018 sec 3A): the interval-I oracle does not exist -- the
point-set mirror (``formal/V2Cofibration.agda``) defines Face = Point -> Bool,
which carries the boolean law x && ~x = 0 for free, while the interval I is a
De Morgan algebra in which that law FAILS.  The mirror itself proves (sec 10,
via the DM3 counter-model) that the point-set model is sound but not complete
for De Morgan algebras.  This fragment re-interprets the three structural axes
of V2 -- availability (G-b), level (G-c), density (G-a) -- on DM3, the standard
non-boolean De Morgan algebra (the 3-element chain 0 < a < 1 with ~a = a,
hence a && ~a = a != 0).

The question it answers: can the three structural separations be produced in
an algebra where the boolean law FAILS?  The native kernel answers YES for all
three (formal/V2DM3.agda sec 6); in particular the density witness separates
using dm3StrictlyBetween on the chain 0 < a < 1 while boolLawFails
(dm3NonBoolean) holds in the SAME algebra -- the separations do NOT ride on
the boolean law that the point-set model carries for free.

ORACLE SCOPE (015 sec 5 / F-011 / 017 sec 5, tightened for this unit): DM3 is
a non-boolean De Morgan algebra, NOT the real cubical interval I (whose
equality is not decidable, so no Bool-valued separates can be written on it).
This module registers no claim about I.  The upgraded scope is exactly
DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT: the confirmed content is the
NEGATIVE statement that no boolean law is needed, on a specific
kernel-confirmed-non-boolean algebra.
"""
from __future__ import annotations

from itertools import product

from .util import MachineOverviewError

BOOLS = (True, False)

# ---------------------------------------------------------------- DM3

#: DM3, the 3-element chain 0 < a < 1 (mirror sec 10).  Indices follow the
#: declaration order d0, da, d1.
DM3_ELEMENTS = ("d0", "da", "d1")
D0, DA, D1 = 0, 1, 2
DM3_COUNT = len(DM3_ELEMENTS)

#: B3, the bounded truncation-tower lattice (mirror sec 2): b0 <= b1 <= b2.
B3_ELEMENTS = ("b0", "b1", "b2")
B0, B1, B2 = 0, 1, 2
B3_COUNT = len(B3_ELEMENTS)

#: Bounded delay index (mirrors the L1 declaration and the V2 fragment).
DELAY_INDEX_MAX = 2
#: Bounded tower level (B3 has three elements).
TOWER_MAX = 2


def _check_dm3(d: int) -> int:
    d = int(d)
    if not 0 <= d < DM3_COUNT:
        raise MachineOverviewError(f"DM3_OUT_OF_DECLARED_RANGE:{d}")
    return d


def _check_b3(level: int) -> int:
    level = int(level)
    if not 0 <= level < B3_COUNT:
        raise MachineOverviewError(f"LEVEL_OUT_OF_DECLARED_RANGE:{level}")
    return level


def dm3_eq(x: int, y: int) -> bool:
    return _check_dm3(x) == _check_dm3(y)


def dm3_leq(x: int, y: int) -> bool:
    """Chain order 0 < a < 1 (mirror: dm3LeqB)."""
    x, y = _check_dm3(x), _check_dm3(y)
    if x == D0:
        return True
    if x == DA:
        return y != D0
    return y == D1


def dm3_meet(x: int, y: int) -> int:
    """Mirror: dm3Meet d0 _ = d0; dm3Meet _ d0 = d0; dm3Meet d1 y = y;
    dm3Meet da da = da; dm3Meet da d1 = da."""
    x, y = _check_dm3(x), _check_dm3(y)
    if x == D0 or y == D0:
        return D0
    if x == D1:
        return y
    # x == DA
    return DA


def dm3_join(x: int, y: int) -> int:
    """Mirror: dm3Join d1 _ = d1; dm3Join _ d1 = d1; dm3Join d0 y = y;
    dm3Join da da = da; dm3Join da d0 = da."""
    x, y = _check_dm3(x), _check_dm3(y)
    if x == D1 or y == D1:
        return D1
    if x == D0:
        return y
    # x == DA
    return DA


def dm3_neg(x: int) -> int:
    """Mirror: dm3Neg d0 = d1; dm3Neg d1 = d0; dm3Neg da = da."""
    x = _check_dm3(x)
    if x == D0:
        return D1
    if x == D1:
        return D0
    return DA


def dm3_non_boolean() -> bool:
    """The boolean law FAILS in DM3: a && ~a = a != 0 (mirror: dm3NonBoolean).

    Returned as a Python-level recomputation of the same negative fact the
    native kernel checks in formal/V2DM3.agda (boolLawFails); it is a
    mechanical finite fact about this specific algebra, not a claim about the
    interval I.
    """
    return dm3_meet(DA, dm3_neg(DA)) != D0


def dm3_strictly_between(a: int, f: int, b: int) -> bool:
    """G-a density, positional form (mirror: dm3StrictlyBetween)."""
    a, f, b = _check_dm3(a), _check_dm3(f), _check_dm3(b)
    return dm3_leq(a, f) and dm3_leq(f, b) and a != f and f != b


def b3_leq(x: int, y: int) -> bool:
    """Bounded tower comparison (mirror: b3LeqB)."""
    x, y = _check_b3(x), _check_b3(y)
    if x == B0:
        return True
    if x == B1:
        return y != B0
    return y == B2


def b3_eq(x: int, y: int) -> bool:
    return _check_b3(x) == _check_b3(y)


# ---------------------------------------------------------------- values

def omega() -> tuple:
    return ("omega",)


def ret(n: int, b: bool, d: int, level: int) -> tuple:
    n = int(n)
    if not 0 <= n <= DELAY_INDEX_MAX:
        raise MachineOverviewError(f"DELAY_INDEX_OUT_OF_DECLARED_RANGE:{n}")
    return ("ret", n, bool(b), _check_dm3(d), _check_b3(level))


def conv(value: tuple, b: bool) -> bool:
    """Delay-axis visibility (mirror: convD): only (n, b) is visible."""
    return value[0] == "ret" and value[2] == b


def delay_equivalent(left: tuple, right: tuple) -> bool:
    """Result equivalence on the computation axis only (mirror: delayEquivD).

    The structural coordinates (dm3, level) are intentionally invisible here:
    that is exactly what makes the three structural separation kinds
    unavailable to every delay (L1) grammar.
    """
    return all(conv(left, b) == conv(right, b) for b in BOOLS)


#: Availability states (G-b), as in the point-set fragment.
AVAILABILITY = ("absent", "pending", "available")

#: Observation modes of a DM3 context (mirror: ModeD).
OBSERVATION_MODES = ("delay", "availability", "tower", "density")

#: Separation kinds produced by the DM3 fragment (mirror: SepKindD).
SEPARATION_KINDS = (
    "availability_observation",
    "level_observation",
    "density_observation",
)


# ---------------------------------------------------------------- supplied

#: SuppliedD = DM3 -> Bool is represented as the set of supplied DM3 elements.
def supplied_at(supplied: frozenset, d: int) -> bool:
    return _check_dm3(d) in supplied


def supply_dm3(supplied: frozenset, d: int) -> frozenset:
    return frozenset(supplied) | {_check_dm3(d)}


# ---------------------------------------------------------------- observations

def fill_of(value: tuple, supplied: frozenset) -> str:
    """Mirror: fillOfD -- decidable membership only, no lattice identity."""
    if value[0] != "ret":
        return "absent"
    return "available" if supplied_at(supplied, value[3]) else "pending"


def tower_of(level: int, value: tuple) -> bool:
    """Mirror: towerOfD -- comparison in the bounded lattice {b0,b1,b2}."""
    if value[0] != "ret":
        return False
    return b3_leq(value[4], level)


def between_of(a: int, value: tuple, b: int) -> bool:
    """Mirror: betweenOfD -- the value's OWN coordinate tested against the
    declared chain interval (value-dependent by design, 015 sec 3.3)."""
    if value[0] != "ret":
        return False
    return dm3_strictly_between(a, value[3], b)


# ---------------------------------------------------------------- ops

def step_op(op: dict, current: tuple, supplied: frozenset,
            result: tuple | None) -> tuple[tuple, frozenset, tuple | None]:
    """One op (mirror: stepOpD).  The value NEVER changes: only the supplied
    set and the pending observation.  The observation is overwritten by later
    ops, and observationModeD takes the LAST op, exactly as in the mirror."""
    kind = op.get("kind")
    if kind == "supply":
        return current, supply_dm3(supplied, op["d"]), result
    if kind == "fill":
        return current, supplied, ("availability", fill_of(current, supplied))
    if kind == "tower":
        return current, supplied, ("tower", tower_of(op["level"], current))
    if kind == "between":
        return current, supplied, ("density", between_of(op["a"], current, op["b"]))
    raise MachineOverviewError(f"UNKNOWN_DM3_CONTEXT_OP:{kind}")


#: Ops that produce (and fix) the observation; extending past one would only
#: overwrite it, so the grammar declares them terminal (as in v2_chain).
TERMINAL_OPS = ("fill", "tower", "between")


def observation_mode(ops: list[dict]) -> str:
    """Mode of the LAST op (mirror: observationModeD); [] is delay."""
    if not ops:
        return "delay"
    kind = ops[-1].get("kind")
    if kind == "fill":
        return "availability"
    if kind == "tower":
        return "tower"
    if kind == "between":
        return "density"
    return "delay"


def apply_ops(ops: list[dict], value: tuple,
              supplied: frozenset = frozenset()) -> tuple[tuple, frozenset]:
    """Mirror: applyOpsD.  Returns (observation, supplied_after) where the
    observation is a full ObsD tuple (``("delay", value)`` when no terminal op
    ran)."""
    current = value
    current_supplied = frozenset(supplied)
    result = None
    for op in ops:
        current, current_supplied, result = step_op(op, current, current_supplied, result)
    if result is None:
        result = ("delay", current)
    return result, current_supplied


def observations_equal(mode: str, left: tuple, right: tuple) -> bool:
    """Mirror: equalForModeD -- the delay mode compares the delay axis only."""
    if mode == "delay":
        return delay_equivalent(left[1], right[1])
    if mode in ("availability", "tower", "density"):
        return left == right
    raise MachineOverviewError(f"UNKNOWN_DM3_OBSERVATION_MODE:{mode}")


def separation_kind(ops: list[dict], observed_left: tuple,
                    observed_right: tuple) -> str:
    """Mirror: separationKindD (mDelayD defaults to kAvailD, as declared)."""
    mode = observation_mode(ops)
    return {
        "availability": "availability_observation",
        "tower": "level_observation",
        "density": "density_observation",
        "delay": "availability_observation",
    }[mode]


def separates(ops: list[dict], left: tuple, right: tuple,
              supplied: frozenset = frozenset()) -> tuple[bool, tuple, tuple, str | None]:
    """Mirror: separatesD -> (separates?, obs_left, obs_right, kind)."""
    if not ops:
        return False, ("delay", left), ("delay", right), None
    (obs_left, _s1) = apply_ops(ops, left, supplied)
    (obs_right, _s2) = apply_ops(ops, right, supplied)
    mode = observation_mode(ops)
    if observations_equal(mode, obs_left, obs_right):
        return False, obs_left, obs_right, None
    return True, obs_left, obs_right, separation_kind(ops, obs_left, obs_right)


def sep_result_equal(r1: tuple, r2: tuple) -> bool:
    """Mirror: sepEqD."""
    q1, o1, p1, k1 = r1
    q2, o2, p2, k2 = r2
    return q1 == q2 and o1 == o2 and p1 == p2 and k1 == k2


# ---------------------------------------------------------------- denominator

def ground_values() -> list[tuple]:
    """All declared DM3 ground values (the finite denominator):
    1 + 3 * 2 * 3 * 3 = 55 elements (mirror sec 8)."""
    out = [omega()]
    for n, b, d, level in product(range(DELAY_INDEX_MAX + 1), BOOLS,
                                  range(DM3_COUNT), range(B3_COUNT)):
        out.append(ret(n, b, d, level))
    return out


def single_ops() -> list[dict]:
    """The declared single-op denominator (16 ops): 3 supply + 1 fill +
    3 tower + 9 between."""
    ops: list[dict] = []
    for d in range(DM3_COUNT):
        ops.append({"kind": "supply", "d": d})
    ops.append({"kind": "fill"})
    for level in range(B3_COUNT):
        ops.append({"kind": "tower", "level": level})
    for a in range(DM3_COUNT):
        for b in range(DM3_COUNT):
            ops.append({"kind": "between", "a": a, "b": b})
    return ops


def declared_op_lists() -> list[tuple[str, list[dict]]]:
    """The bounded op-list denominator: every single op plus every
    two-op continuation of a supply prefix (the only non-terminal op).
    16 + 3*16 = 64 declared op lists; this is the closed denominator the
    search exhausts, and it contains all three mirror witnesses."""
    out: list[tuple[str, list[dict]]] = []
    for op in single_ops():
        out.append((f"single:{op['kind']}:{len(out)}", [dict(op)]))
    for d in range(DM3_COUNT):
        for op in single_ops():
            out.append((f"supply{d}:{op['kind']}:{len(out)}",
                        [{"kind": "supply", "d": d}, dict(op)]))
    return out


# ---------------------------------------------------------------- witnesses

#: The three structural witnesses declared in formal/V2DM3.agda sec 6, with
#: the expected SepResultD the native kernel checks there by refl.  These are
#: the CALIBRATION BENCHMARK: the enumerator must reproduce them exactly.
WITNESS_A = {
    "witness_id": "WV-A-availability",
    "left": ret(0, True, DA, B0),
    "right": ret(0, True, D1, B0),
    "ops": [{"kind": "supply", "d": DA}, {"kind": "fill"}],
    "expect": (True, ("availability", "available"), ("availability", "pending"),
               "availability_observation"),
}
WITNESS_L = {
    "witness_id": "WV-L-level",
    "left": ret(0, True, DA, B2),
    "right": ret(0, True, DA, B0),
    "ops": [{"kind": "tower", "level": B1}],
    "expect": (True, ("tower", False), ("tower", True), "level_observation"),
}
WITNESS_D = {
    "witness_id": "WV-D-density",
    "left": ret(0, True, DA, B0),
    "right": ret(0, True, D1, B0),
    "ops": [{"kind": "between", "a": D0, "b": D1}],
    "expect": (True, ("density", True), ("density", False), "density_observation"),
}
DECLARED_WITNESSES = (WITNESS_A, WITNESS_L, WITNESS_D)

#: Same-value controls (mirror: sameValueControlA / sameValueControlD): the
#: same context on IDENTICAL inputs must never separate.
SAME_VALUE_CONTROL_A = {
    "witness_id": "CTRL-A-same-value",
    "left": WITNESS_A["left"],
    "right": WITNESS_A["left"],
    "ops": WITNESS_A["ops"],
    "expect": (False, ("availability", "available"), ("availability", "available"), None),
}
SAME_VALUE_CONTROL_D = {
    "witness_id": "CTRL-D-same-value",
    "left": WITNESS_D["left"],
    "right": WITNESS_D["left"],
    "ops": WITNESS_D["ops"],
    "expect": (False, ("density", True), ("density", True), None),
}
SAME_VALUE_CONTROLS = (SAME_VALUE_CONTROL_A, SAME_VALUE_CONTROL_D)


def check_declared_witnesses() -> dict:
    """Recompute every declared witness and same-value control with the
    canonical semantics and assert agreement with the mirror's expectations."""
    rows = []
    for spec in DECLARED_WITNESSES + SAME_VALUE_CONTROLS:
        got = separates(spec["ops"], spec["left"], spec["right"])
        rows.append({
            "witness_id": spec["witness_id"],
            "matches_mirror": sep_result_equal(got, spec["expect"]),
            "computed": got,
            "expected": spec["expect"],
        })
        if not rows[-1]["matches_mirror"]:
            raise MachineOverviewError(f"DM3_WITNESS_MISMATCH:{rows[-1]}")
    invisible = {spec["witness_id"]: delay_equivalent(spec["left"], spec["right"])
                 for spec in DECLARED_WITNESSES}
    return {"all_match": True, "rows": rows, "delay_invisible": invisible}


# ---------------------------------------------------------------- non-embedding

def no_point_set_embedding() -> dict:
    """Exhaustive finite check: NO function f: DM3 -> Faces (the 16-point
    boolean face lattice of the point-set mirror) preserves meet and negation.

    Finite domain (3 elements into 16, 16**3 = 4096 candidate functions),
    complete enumeration, fixed proposition; therefore this is a valid
    machine-checked NEGATIVE statement about the two DECLARED finite
    structures.  It shows the DM3 fragment is not a relabelling of a
    point-set sub-fragment: the algebra in which the density separation is
    computed cannot be represented inside the point-set model at all.
    Scope: the point-set model only (an enumerator-internal finite structure);
    it says nothing about the real interval I (F-011)."""
    from . import v2_cofibration as ps
    face_count = ps.FACE_COUNT
    total = 0
    preserving = 0
    counterexamples = []
    for f0 in range(face_count):
        for fa in range(face_count):
            for f1 in range(face_count):
                total += 1
                f = {D0: f0, DA: fa, D1: f1}
                ok = True
                for x in range(DM3_COUNT):
                    for y in range(DM3_COUNT):
                        if ps.face_min(f[x], f[y]) != f[dm3_meet(x, y)]:
                            ok = False
                for x in range(DM3_COUNT):
                    if ps.face_neg(f[x]) != f[dm3_neg(x)]:
                        ok = False
                if ok:
                    preserving += 1
                    if len(counterexamples) < 4:
                        counterexamples.append({k: v for k, v in f.items()})
    claim = "NO meet-and-negation-preserving embedding of DM3 into the point-set boolean face lattice exists"
    return {
        "proof_kind": "model_exhaustive_negative_check",
        "claim": claim,
        "domain": {
            "dm3": "3-element non-boolean De Morgan algebra (mirror sec 10)",
            "faces": f"16 truth functions over the 4-point boolean cube (point-set mirror)",
            "candidate_functions": total,
            "functions_preserving_meet_and_neg": preserving,
        },
        "result": preserving == 0,
        "counterexamples_found": counterexamples,
        "scope": ("the two declared finite structures only; NOT a claim about the "
                  "real interval I (F-011 / 015 sec 5)"),
        "registers_new_claim": False,
    }


# ---------------------------------------------------------------- json

def value_to_json(value: tuple) -> dict:
    if value[0] == "omega":
        return {"kind": "omega"}
    return {"kind": "ret", "n": value[1], "value": value[2],
            "dm3": value[3], "level": value[4]}


def value_from_json(row: dict) -> tuple:
    kind = row.get("kind")
    if kind == "omega":
        return omega()
    if kind == "ret":
        return ret(row["n"], row["value"], row["dm3"], row["level"])
    raise MachineOverviewError(f"UNKNOWN_DM3_VALUE_JSON:{row!r}")
