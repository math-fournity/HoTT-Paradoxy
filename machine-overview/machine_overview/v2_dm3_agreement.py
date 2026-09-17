"""Agda rendering for the DM3 fragment (gap-A acceptance unit).

Renders the canonical Python semantics (``v2_dm3``) into Cubical Agda terms
against the native mirror ``formal/V2DM3.agda``.  DENOMINATOR_SINGLE_SOURCE
(016 sec 3): every literal rendered here is computed by ``v2_dm3``, the same
module that produced the search run; no expected value is hand-written.
"""
from __future__ import annotations

from . import v2_dm3 as v2
from .util import MachineOverviewError

_DM3 = {0: "d0", 1: "da", 2: "d1"}
_B3 = {0: "b0", 1: "b1", 2: "b2"}


def render_bool(b: bool) -> str:
    return "true" if b else "false"


def render_nat(n: int) -> str:
    n = int(n)
    if n < 0:
        raise MachineOverviewError(f"NEGATIVE_NAT:{n}")
    if n == 0:
        return "zero"
    return f"suc ({render_nat(n - 1)})"


def render_dm3(d: int) -> str:
    if int(d) not in _DM3:
        raise MachineOverviewError(f"DM3_OUT_OF_RENDER_RANGE:{d}")
    return _DM3[int(d)]


def render_b3(level: int) -> str:
    if int(level) not in _B3:
        raise MachineOverviewError(f"LEVEL_OUT_OF_B3:{level}")
    return _B3[int(level)]


_AVAIL = {"absent": "absent", "pending": "pending", "available": "available"}


def render_value(value: tuple) -> str:
    if value[0] == "omega":
        return "vωd"
    if value[0] == "ret":
        _, n, b, d, level = value
        return (f"vretd ({render_nat(n)}) ({render_bool(b)}) "
                f"({render_dm3(d)}) ({render_b3(level)})")
    raise MachineOverviewError(f"UNKNOWN_DM3_VALUE:{value!r}")


def render_obs(obs: tuple) -> str:
    kind = obs[0]
    if kind == "delay":
        return f"obsDelayD ({render_value(obs[1])})"
    if kind == "availability":
        state = obs[1]
        if state not in _AVAIL:
            raise MachineOverviewError(f"UNKNOWN_AVAILABILITY:{state!r}")
        return f"obsAvailD {_AVAIL[state]}"
    if kind == "tower":
        return f"obsTowerD {render_bool(obs[1])}"
    if kind == "density":
        return f"obsDensityD {render_bool(obs[1])}"
    raise MachineOverviewError(f"UNKNOWN_DM3_OBSERVATION:{obs!r}")


def render_op(op: dict) -> str:
    kind = op.get("kind")
    if kind == "supply":
        return f"opSupplyD {render_dm3(op['d'])}"
    if kind == "fill":
        return "opFillD"
    if kind == "tower":
        return f"opTowerD {render_b3(op['level'])}"
    if kind == "between":
        return f"opBetweenD {render_dm3(op['a'])} {render_dm3(op['b'])}"
    raise MachineOverviewError(f"UNKNOWN_DM3_CONTEXT_OP:{kind}")


def render_op_list(ops: list[dict]) -> str:
    if not ops:
        return "[]"
    return " ∷ ".join(render_op(op) for op in ops) + " ∷ []"


_KIND = {
    "availability_observation": "kAvailD",
    "level_observation": "kLevelD",
    "density_observation": "kDensityD",
}


def render_sep_kind(kind) -> str:
    if kind is None:
        return "nothing"
    if kind in _KIND:
        return f"just {_KIND[kind]}"
    raise MachineOverviewError(f"UNKNOWN_DM3_SEPARATION_KIND:{kind!r}")


def _as_obs(x: tuple) -> tuple:
    """Normalise a separates() result element to a full observation tuple.

    ``separates []`` returns the bare INPUT values (no context ran), which on
    the kernel side is ``obsDelayD l`` / ``obsDelayD r``; a non-empty context
    already returns a full observation tuple."""
    if x[0] in v2.OBSERVATION_MODES:
        return x
    if x[0] in ("omega", "ret"):
        return ("delay", x)
    raise MachineOverviewError(f"UNKNOWN_DM3_SEP_OBSERVATION:{x!r}")


def render_sep_result(sep_tuple: tuple) -> str:
    separated, ol, orr, kind = sep_tuple
    ol, orr = _as_obs(ol), _as_obs(orr)
    return (f"({render_bool(separated)} , {render_obs(ol)} , "
            f"{render_obs(orr)} , {render_sep_kind(kind)})")
