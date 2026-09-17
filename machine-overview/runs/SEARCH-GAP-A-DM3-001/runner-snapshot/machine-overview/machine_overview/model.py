"""Semantics of the pinned R041 delay fragment (L1 calibration model).

The Python model mirrors
``HoTT/formal/partiality-race-timeout/PartialityRaceTimeout.agda`` definition
for definition on ground terms.  It is used by the typed enumerator to propose
candidates; it never replaces the native kernel check.

Delay value:    ("omega",) | ("ret", n, value)
Optional value: ("none",)  | ("some", value)
"""
from __future__ import annotations

from .util import MachineOverviewError

BOOLS = (True, False)


def omega() -> tuple:
    return ("omega",)


def ret(n: int, value: bool) -> tuple:
    return ("ret", int(n), bool(value))


def later(value: tuple) -> tuple:
    if value[0] == "omega":
        return omega()
    return ("ret", value[1] + 1, value[2])


def iter_later(k: int, value: tuple) -> tuple:
    for _ in range(int(k)):
        value = later(value)
    return value


def bind_value(value: tuple, continuation: dict[bool, tuple]) -> tuple:
    """``value bind f`` with a ground continuation ``f : Bool → Delay Bool``."""
    if value[0] == "omega":
        return omega()
    n, a = value[1], bool(value[2])
    inner = continuation[a]
    if inner[0] == "omega":
        return omega()
    return ("ret", n + inner[1] + 1, inner[2])


def race_value(left: tuple, right: tuple) -> tuple:
    if left[0] == "omega":
        return right
    if right[0] == "omega":
        return left
    m, n = left[1], right[1]
    return left if m <= n else right


def deadline_value(k: int, value: tuple) -> tuple:
    if value[0] == "omega":
        return ("none",)
    n, a = value[1], value[2]
    return ("some", a) if n <= int(k) else ("none",)


def conv(value: tuple, b: bool) -> bool:
    return value[0] == "ret" and value[2] == b


def delay_equivalent(left: tuple, right: tuple) -> bool:
    return all(conv(left, b) == conv(right, b) for b in BOOLS)


def optional_equal(left: tuple, right: tuple) -> bool:
    return left == right


def value_to_json(value: tuple) -> dict:
    if value[0] == "omega":
        return {"kind": "omega"}
    if value[0] == "ret":
        return {"kind": "ret", "n": value[1], "value": value[2]}
    if value[0] == "none":
        return {"kind": "none"}
    if value[0] == "some":
        return {"kind": "some", "value": value[1]}
    raise MachineOverviewError(f"UNKNOWN_VALUE:{value!r}")


def value_from_json(row: dict) -> tuple:
    kind = row.get("kind")
    if kind == "omega":
        return omega()
    if kind == "ret":
        return ret(row["n"], row["value"])
    if kind == "none":
        return ("none",)
    if kind == "some":
        return ("some", bool(row["value"]))
    raise MachineOverviewError(f"UNKNOWN_VALUE_JSON:{row!r}")


def continuation_from_json(row: dict) -> dict[bool, tuple]:
    return {
        True: value_from_json(row["true"]),
        False: value_from_json(row["false"]),
    }


def continuation_to_json(continuation: dict[bool, tuple]) -> dict:
    return {
        "true": value_to_json(continuation[True]),
        "false": value_to_json(continuation[False]),
    }


def apply_ops(ops: list[dict], value: tuple) -> tuple:
    """Apply a context (list of operations, innermost first) to a value."""
    current = value
    current_type = "delay"
    for op in ops:
        kind = op.get("kind")
        if kind in ("race_left", "race_right", "bind") and current_type != "delay":
            raise MachineOverviewError(f"TYPED_CONTEXT_VIOLATION:{kind}:after:{current_type}")
        if kind == "deadline" and current_type != "delay":
            raise MachineOverviewError(f"TYPED_CONTEXT_VIOLATION:deadline:after:{current_type}")
        if kind == "race_left":
            current = race_value(current, value_from_json(op["partner"]))
        elif kind == "race_right":
            current = race_value(value_from_json(op["partner"]), current)
        elif kind == "bind":
            current = bind_value(current, continuation_from_json(op["continuation"]))
        elif kind == "deadline":
            current = deadline_value(op["k"], current)
            current_type = "optional"
        else:
            raise MachineOverviewError(f"UNKNOWN_CONTEXT_OP:{kind}")
    return current


def observation_mode(ops: list[dict]) -> str:
    """The declared observation of the whole composed process."""
    if ops and ops[-1].get("kind") == "deadline":
        return "deadline"
    return "delay"


def separates(ops: list[dict], left: tuple, right: tuple) -> tuple[bool, tuple, tuple]:
    """Return (separates?, left_observation, right_observation)."""
    if not ops:
        return False, left, right
    observed_left = apply_ops(ops, left)
    observed_right = apply_ops(ops, right)
    if observation_mode(ops) == "deadline":
        return (not optional_equal(observed_left, observed_right)), observed_left, observed_right
    return (not delay_equivalent(observed_left, observed_right)), observed_left, observed_right


def separation_kind(ops: list[dict], observed_left: tuple, observed_right: tuple) -> str:
    if observation_mode(ops) == "deadline":
        return "deadline_observation"
    if observed_left[0] == "omega" or observed_right[0] == "omega":
        return "completion_divergence"
    return "value_mismatch"


def agda_nat(n: int) -> str:
    n = int(n)
    if n < 0:
        raise MachineOverviewError(f"NEGATIVE_NAT:{n}")
    expression = "zero"
    for _ in range(n):
        expression = f"(suc {expression})"
    return expression


def agda_bool(value: bool) -> str:
    return "true" if value else "false"


def agda_value(value: tuple) -> str:
    if value[0] == "omega":
        return "ω"
    if value[0] == "ret":
        return f"ret {agda_nat(value[1])} {agda_bool(value[2])}"
    raise MachineOverviewError(f"NOT_A_DELAY_VALUE:{value!r}")
