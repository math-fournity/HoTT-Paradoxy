"""Semantics of the declared L2-cofibration fragment (V2 calibration model).

Extends the pinned R041 delay fragment (``machine_overview/model.py``) with a
structural axis, so that omission shapes which the delay fragment cannot carry
can be machine-ified.  See ``Atria的方案/修订片/015`` for the design and the
gate conditions G-a / G-b / G-c.

Ground domain (all finite and decidable):

* computation axis: ``omega`` / ``ret n b face level``
  (``n`` rounds, value ``b``, cofibration ``face``, truncation-tower ``level``)
* cofibration faces: the 16 truth functions over the 4-point boolean cube
  ``{0,1}^2`` (bitmask 0..15).  IMPORTANT FAITHFULNESS CAVEAT (revision 015
  §3.4): this pointwise model validates the *boolean* law ``x && ~x = 0``,
  while the interval ``I`` is a De Morgan algebra in which it fails.  The model
  is therefore SOUND but NOT COMPLETE w.r.t. the interval's face theory.
  This module is the ENUMERATOR ONLY: oracle verdicts must come from the native
  kernel on the real interval ``I``; every separation computed here is an
  enumerator-internal candidate, never a conclusion (F-011).
"""
from __future__ import annotations

from .util import MachineOverviewError

BOOLS = (True, False)

# ---------------------------------------------------------------- faces

#: Number of points of the 4-point boolean cube {0,1}^2.
POINT_COUNT = 4
#: Bitmask over the 4 points; a face is a truth function {0,1}^2 -> Bool.
FACE_COUNT = 16
FACE_ZERO = 0          # constantly false
FACE_ONE = FACE_COUNT - 1  # constantly true
#: Points in declaration order: BOOLS = (True, False) iterates i then j, so
#: index 0 = (i,j) = (T,T), 1 = (T,F), 2 = (F,T), 3 = (F,F).
POINTS = tuple((i, j) for i in BOOLS for j in BOOLS)
#: Face of the first interval variable i (true where i = 1).
FACE_I = sum(1 << k for k, (i, _j) in enumerate(POINTS) if i)
#: Face of the second interval variable j (true where j = 1).
FACE_J = sum(1 << k for k, (_i, j) in enumerate(POINTS) if j)

#: Bounded truncation-tower levels (declared finite denominator).
TOWER_MAX = 2
#: Bounded delay index (mirrors the L1 declaration).
DELAY_INDEX_MAX = 2


def _check_face(face: int) -> int:
    face = int(face)
    if not 0 <= face < FACE_COUNT:
        raise MachineOverviewError(f"FACE_OUT_OF_DECLARED_RANGE:{face}")
    return face


def face_point(face: int, point_index: int) -> bool:
    return bool((_check_face(face) >> int(point_index)) & 1)


def face_min(a: int, b: int) -> int:
    return _check_face(a) & _check_face(b)


def face_max(a: int, b: int) -> int:
    return _check_face(a) | _check_face(b)


def face_neg(a: int) -> int:
    return (~_check_face(a)) & (FACE_COUNT - 1)


def face_between(a: int, b: int) -> bool:
    """Density query (G-a), existence form: is there a face strictly between
    ``a`` and ``b``?

    Read with ``a`` subset ``b``; a strict intermediate exists iff the
    difference carries at least two points.  Value-independent; used to reason
    about whether a declared interval has room (G-a gate), NOT as the
    observation of a value.
    """
    a, b = _check_face(a), _check_face(b)
    diff = b & ~a
    return bin(diff).count("1") >= 2


def face_strictly_between(a: int, f: int, b: int) -> bool:
    """Density query (G-a), positional form: is the face ``f`` strictly inside
    the open interval ``(a, b)`` of the face lattice?

    This is the value-dependent half required by revision 015 §3.2/§3.3: the
    observation must depend on the value's own structural coordinate, otherwise
    ``density_observation`` could never be produced by ``separates``.
    """
    a, f, b = _check_face(a), _check_face(f), _check_face(b)
    below = (a & f) == a          # a subset f
    above = (f & b) == f          # f subset b
    return below and above and f != a and f != b


# ---------------------------------------------------------------- values

def omega() -> tuple:
    return ("omega",)


def ret(n: int, b: bool, face: int, level: int) -> tuple:
    n = int(n)
    if not 0 <= n <= DELAY_INDEX_MAX:
        raise MachineOverviewError(f"DELAY_INDEX_OUT_OF_DECLARED_RANGE:{n}")
    if not 0 <= int(level) <= TOWER_MAX:
        raise MachineOverviewError(f"LEVEL_OUT_OF_DECLARED_RANGE:{level}")
    return ("ret", n, bool(b), _check_face(face), int(level))


def later(value: tuple) -> tuple:
    if value[0] == "omega":
        return omega()
    return ("ret", value[1] + 1, value[2], value[3], value[4])


def bind_value(value: tuple, continuation: dict) -> tuple:
    """``value bind k``; the continuation result supplies face and level."""
    if value[0] == "omega":
        return omega()
    inner = continuation[value[2]]
    if inner[0] == "omega":
        return omega()
    return ("ret", value[1] + inner[1] + 1, inner[2], inner[3], inner[4])


def race_value(left: tuple, right: tuple) -> tuple:
    if left[0] == "omega":
        return right
    if right[0] == "omega":
        return left
    return left if left[1] <= right[1] else right


def conv(value: tuple, b: bool) -> bool:
    return value[0] == "ret" and value[2] == b


def delay_equivalent(left: tuple, right: tuple) -> bool:
    """Result equivalence on the computation axis only.

    Face and level are intentionally invisible here: that is exactly what makes
    the structural separation kinds unavailable in the L1 fragment.
    """
    return all(conv(left, b) == conv(right, b) for b in BOOLS)


# ---------------------------------------------------------------- ops

#: Availability states (G-b): the filler exists vs the filler is in place.
AVAILABILITY = ("absent", "pending", "available")

#: Observation kinds produced by a V2 context.
OBSERVATION_KINDS = ("delay", "optional", "availability", "tower", "density")

#: Separation kinds; the first three coincide with the L1 fragment, the last
#: three are the new structural ones (revision 015 §3.3).
SEPARATION_KINDS = (
    "value_mismatch",
    "completion_divergence",
    "deadline_observation",
    "availability_observation",
    "level_observation",
    "density_observation",
)


def value_to_json(value: tuple) -> dict:
    if value[0] == "omega":
        return {"kind": "omega"}
    return {"kind": "ret", "n": value[1], "value": value[2],
            "face": value[3], "level": value[4]}


def value_from_json(row: dict) -> tuple:
    kind = row.get("kind")
    if kind == "omega":
        return omega()
    if kind == "ret":
        return ret(row["n"], row["value"], row["face"], row["level"])
    raise MachineOverviewError(f"UNKNOWN_VALUE_JSON:{row!r}")


def continuation_from_json(row: dict) -> dict:
    return {True: value_from_json(row["true"]), False: value_from_json(row["false"])}


def continuation_to_json(continuation: dict) -> dict:
    return {"true": value_to_json(continuation[True]),
            "false": value_to_json(continuation[False])}


def apply_ops(ops: list[dict], value: tuple, supplied: frozenset = frozenset()):
    """Apply a V2 context to a ground value.

    Returns ``(result, supplied_after)`` where ``result`` is either a V2 value
    (delay-axis observation) or an observation tuple:

    * ``("optional", optional_value)`` for a deadline context
    * ``("availability", availability_state)`` for a fill context
    * ``("tower", visible_bool)`` for a tower context
    * ``("density", between_bool)`` for a between context
    """
    current = value
    current_supplied = frozenset(supplied)
    result = None
    for op in ops:
        kind = op.get("kind")
        if kind == "race_left":
            current = race_value(current, value_from_json(op["partner"]))
        elif kind == "race_right":
            current = race_value(value_from_json(op["partner"]), current)
        elif kind == "bind":
            current = bind_value(current, continuation_from_json(op["continuation"]))
        elif kind == "supply":
            current_supplied = current_supplied | {_check_face(op["face"])}
        elif kind == "deadline":
            if current[0] == "omega":
                result = ("optional", ("none",))
            else:
                result = ("optional", ("some", current[2]) if current[1] <= int(op["k"]) else ("none",))
        elif kind == "fill":
            result = ("availability", _fill_of(current, current_supplied))
        elif kind == "fill_of":
            result = ("availability", "available" if _check_face(op["face"]) in current_supplied else "pending")
        elif kind == "tower":
            if current[0] == "omega":
                result = ("tower", False)
            else:
                result = ("tower", current[4] <= int(op["level"]))
        elif kind == "between":
            # G-a density observation.  VALUE-DEPENDENT by design (revision
            # 015 §3.3): the value's own face is the tested position; the two
            # declared faces are the interval bounds.  A value-independent
            # reading could never separate two inputs and would make
            # ``density_observation`` unreachable.
            if current[0] != "ret":
                result = ("density", False)
            else:
                result = ("density", face_strictly_between(op["a"], current[3], op["b"]))
        else:
            raise MachineOverviewError(f"UNKNOWN_CONTEXT_OP:{kind}")
    if result is None:
        return ("delay", current), current_supplied
    return result, current_supplied


def _fill_of(value: tuple, supplied: frozenset) -> str:
    if value[0] != "ret":
        return "absent"
    return "available" if value[3] in supplied else "pending"


def observation_mode(ops: list[dict]) -> str:
    if not ops:
        return "delay"
    last = ops[-1].get("kind")
    if last == "deadline":
        return "optional"
    if last in ("fill", "fill_of"):
        return "availability"
    if last == "tower":
        return "tower"
    if last == "between":
        return "density"
    return "delay"


def _observations_equal(mode: str, left, right) -> bool:
    if mode == "delay":
        return delay_equivalent(left, right)
    if mode == "optional":
        return left == right
    if mode in ("availability", "tower", "density"):
        return left == right
    raise MachineOverviewError(f"UNKNOWN_OBSERVATION_MODE:{mode}")


def _payload(observed: tuple) -> tuple:
    """Strip the ``("delay", value)`` wrapper an :func:`apply_ops` result may
    carry, so equality / classification always sees the value or the declared
    observation payload itself."""
    return observed[1] if observed[0] == "delay" else observed


def separates(ops: list[dict], left: tuple, right: tuple, supplied: frozenset = frozenset()):
    """Return ``(separates?, left_observation, right_observation, kind)``.

    The comparison always uses the payload of the observation: for a delay-mode
    context that is the resulting V2 *value* (not its ``("delay", _)`` wrapper,
    which would make ``conv`` fail on every input and every pair look equal).
    """
    if not ops:
        return False, left, right, None
    (obs_left, _s1) = apply_ops(ops, left, supplied)
    (obs_right, _s2) = apply_ops(ops, right, supplied)
    mode = observation_mode(ops)
    payload_left = _payload(obs_left)
    payload_right = _payload(obs_right)
    if mode == "delay":
        equal = delay_equivalent(payload_left, payload_right)
    else:
        equal = payload_left == payload_right
    if equal:
        return False, obs_left, obs_right, None
    return True, obs_left, obs_right, separation_kind(ops, obs_left, obs_right)


def separation_kind(ops: list[dict], observed_left, observed_right) -> str:
    mode = observation_mode(ops)
    if mode == "optional":
        return "deadline_observation"
    if mode == "availability":
        return "availability_observation"
    if mode == "tower":
        return "level_observation"
    if mode == "density":
        return "density_observation"
    left = _payload(observed_left)
    right = _payload(observed_right)
    if left[0] == "omega" or right[0] == "omega":
        return "completion_divergence"
    return "value_mismatch"
