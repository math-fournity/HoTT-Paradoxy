"""Stage-1 agreement generator for the V2 L2-cofibration fragment.

Design source: ``Atria的方案/修订片/015`` §5 stage 1.  This module is the
BRIDGE half of stage 1: it renders the *entire* declared ground denominator
(289 ground values x 11 declared op-lists = 3179 applyOps evaluations) into a
generated Cubical Agda module ``V2GroundAgreement.agda`` and type-checks it
against the native mirror ``formal/V2Cofibration.agda``.

The mechanical guarantee is a definitional check (NOT a sampling, NOT a
property test): the generated module states

    groundAgreement : checkAll ≡ true
    groundAgreement = refl

where ``checkAll = andL (map checkOne allChecks)`` and ``checkOne`` compares
``obsEqB (proj₁ (applyOps ops inp noSupplied))`` against the EXPECTED Obs
computed by the Python enumerator ``v2_cofibration.apply_ops``.  ``refl`` can
only be discharged by the kernel if EVERY one of the 3179 expected
observations agrees with the native kernel's own evaluation.  A single
disagreement makes the module fail to type-check (that failure IS the
verification).

SCOPE DISCLOSURE (must travel with this run; revision 015 §3.4(i) demands
item-by-item agreement, and this states exactly what is item-by-item):

* ``applyOps`` is checked EXHAUSTIVELY on the full declared denominator
  289 x 11 = 3179 evaluations.  This is exhaustive, not sampled.
* ``separates`` is checked on the 11 DESIGNATED CONTROLS ONLY (3 positive
  controls G-b/G-c/G-a + 5 negative controls + 3 L1-shared-kind reachability
  controls), NOT on the full 289 x 289 pair matrix.  Reason, and it is a
  rendering-budget reason and not a mathematical one: the full matrix would
  require rendering 83521 x 11 ≈ 918k SepResult literals, which is beyond a
  feasible single Agda module.  The designated controls are exactly the ones
  the self-test asserts (tests/test_v2_cofibration.py::SeparationTest), so
  the control set is pinned in two independent places.

FAITHFULNESS CAVEAT (revision 015 §3.4, machine-checked in the mirror's §8-9):
the face lattice is the POINT-SET model (truth functions on the 4-point
boolean cube).  It validates the boolean law f ∧ ¬f = 0 while the interval I
is a De Morgan algebra in which that law FAILS.  The point-set model is SOUND
but NOT COMPLETE.  Consequently this agreement run is an ENGINEERING
acceptance of the enumerator's faithfulness to its declared semantics; it
registers NO mathematical claim (registers_new_claim: false) and no
separation validated here is evidence about the real interval I (F-011).
Oracle verdicts for real-interval questions come only from the native kernel
on I (stage 2).
"""
from __future__ import annotations

import argparse
import io
import sys
from pathlib import Path

from . import v2_cofibration as v2
from . import verify
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

#: The engine worktree (this repo) and the governance handoff repo are both
#: recorded in every agreement receipt so an external auditor can pin the
#: exact source state the agreement was produced from.
ENGINE_ROOT = Path("/Volumes/D/HoTT-machine-overview")
HANDOFF_ROOT = Path("/Volumes/D/HoTT_AI_HANDOFF_20260911")
TOOLCHAIN_JSON = ENGINE_ROOT / "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"
INCLUDE_DIRS = ["machine-overview/formal", "HoTT/formal/partiality-race-timeout"]
DEFAULT_RUN_ID = "20260916-V2-STAGE1-AGREEMENT-001"

#: The 11 designated separation controls.  These MUST stay byte-identical in
#: spirit to tests/test_v2_cofibration.py::SeparationTest; both are consumers
#: of the same v2 semantics, and the expected values below are always
#: recomputed by v2.separates (never hand-written literals).
PARTNER = v2.DECLARED_PARTNER
CONT = v2.DECLARED_CONTINUATION
CONT_DIVERGE = {True: v2.omega(), False: v2.ret(0, False, v2.FACE_J, 0)}


def designated_controls():
    """The 11 designated separation controls (label, ops, left, right)."""
    partner_json = v2.value_to_json(PARTNER)
    cont_json = v2.continuation_to_json(CONT)
    cont_diverge_json = v2.continuation_to_json(CONT_DIVERGE)
    return [
        # ---- 3 positive controls: delay-equivalent inputs, new axis separates
        ("positive-G-b-availability",
         [{"kind": "supply", "face": v2.FACE_I}, {"kind": "fill"}],
         v2.ret(0, True, v2.FACE_I, 0), v2.ret(0, True, v2.FACE_J, 0)),
        ("positive-G-c-level",
         [{"kind": "tower", "level": 0}],
         v2.ret(0, True, v2.FACE_I, 0), v2.ret(0, True, v2.FACE_I, 1)),
        ("positive-G-a-density",
         [{"kind": "between", "a": v2.FACE_ZERO, "b": v2.FACE_ONE}],
         v2.ret(0, True, v2.FACE_I, 0), v2.ret(0, True, v2.FACE_ONE, 0)),
        # ---- 5 negative controls: no separation must be reported
        ("negative-no-ops",
         [],
         v2.ret(0, True, v2.FACE_I, 0), v2.ret(0, False, v2.FACE_J, 2)),
        ("negative-identical-inputs-delay-context",
         [{"kind": "race_left", "partner": partner_json},
          {"kind": "bind", "continuation": cont_json}],
         v2.ret(1, False, v2.FACE_J, 1), v2.ret(1, False, v2.FACE_J, 1)),
        ("negative-G-b-both-faces-supplied",
         [{"kind": "supply", "face": v2.FACE_I},
          {"kind": "supply", "face": v2.FACE_J},
          {"kind": "fill"}],
         v2.ret(0, True, v2.FACE_I, 0), v2.ret(0, True, v2.FACE_J, 0)),
        ("negative-G-c-equal-levels",
         [{"kind": "tower", "level": 1}],
         v2.ret(0, True, v2.FACE_I, 1), v2.ret(0, True, v2.FACE_J, 1)),
        ("negative-G-a-both-faces-at-bounds",
         [{"kind": "between", "a": v2.FACE_ZERO, "b": v2.FACE_ONE}],
         v2.ret(0, True, v2.FACE_ZERO, 0), v2.ret(0, True, v2.FACE_ONE, 0)),
        # ---- 3 L1-shared-kind reachability controls
        ("l1-shared-value-mismatch",
         [{"kind": "race_left", "partner": partner_json}],
         v2.ret(0, True, v2.FACE_I, 0), v2.ret(0, False, v2.FACE_I, 0)),
        ("l1-shared-completion-divergence",
         [{"kind": "bind", "continuation": cont_diverge_json}],
         v2.ret(0, True, v2.FACE_I, 0), v2.ret(0, False, v2.FACE_I, 0)),
        ("l1-shared-deadline-observation",
         [{"kind": "deadline", "k": 0}],
         v2.ret(0, True, v2.FACE_I, 0), v2.ret(1, True, v2.FACE_I, 0)),
    ]


# ------------------------------------------------------------------ renderers

def render_bool(b: bool) -> str:
    return "true" if b else "false"


def render_nat(n: int) -> str:
    n = int(n)
    if n < 0:
        raise MachineOverviewError(f"NEGATIVE_NAT:{n}")
    if n == 0:
        return "zero"
    return f"suc ({render_nat(n - 1)})"


_B3 = {0: "b0", 1: "b1", 2: "b2"}


def render_b3(level: int) -> str:
    if int(level) not in _B3:
        raise MachineOverviewError(f"LEVEL_OUT_OF_B3:{level}")
    return _B3[int(level)]


def render_face(face: int) -> str:
    bits = [render_bool(v2.face_point(face, k)) for k in range(v2.POINT_COUNT)]
    return "faceFromBits " + " ".join(bits)


_AVAIL = {"absent": "absent", "pending": "pending", "available": "available"}


def render_value(value: tuple) -> str:
    if value[0] == "omega":
        return "vω"
    if value[0] == "ret":
        _, n, b, face, level = value
        return f"vret ({render_nat(n)}) ({render_bool(b)}) ({render_face(face)}) ({render_b3(level)})"
    raise MachineOverviewError(f"UNKNOWN_V2_VALUE:{value!r}")


def render_opt(opt: tuple) -> str:
    if opt == ("none",):
        return "none"
    if opt[0] == "some":
        return f"some {render_bool(opt[1])}"
    raise MachineOverviewError(f"UNKNOWN_OPT:{opt!r}")


def render_obs(obs: tuple) -> str:
    kind = obs[0]
    if kind == "delay":
        return f"obsDelay ({render_value(obs[1])})"
    if kind == "optional":
        return f"obsOptional ({render_opt(obs[1])})"
    if kind == "availability":
        state = obs[1]
        if state not in _AVAIL:
            raise MachineOverviewError(f"UNKNOWN_AVAILABILITY:{state!r}")
        return f"obsAvail {_AVAIL[state]}"
    if kind == "tower":
        return f"obsTower {render_bool(obs[1])}"
    if kind == "density":
        return f"obsDensity {render_bool(obs[1])}"
    raise MachineOverviewError(f"UNKNOWN_OBSERVATION:{obs!r}")


def render_continuation(continuation: dict) -> str:
    return (f"λ {{true → {render_value(continuation[True])}; "
            f"false → {render_value(continuation[False])}}}")


def render_op(op: dict) -> str:
    kind = op.get("kind")
    if kind in ("race_left", "race_right"):
        ctor = "opRaceL" if kind == "race_left" else "opRaceR"
        partner = v2.value_from_json(op["partner"])
        return f"{ctor} ({render_value(partner)})"
    if kind == "bind":
        cont = v2.continuation_from_json(op["continuation"])
        return f"opBind ({render_continuation(cont)})"
    if kind == "supply":
        return f"opSupply ({render_face(op['face'])})"
    if kind == "deadline":
        return f"opDeadline ({render_nat(op['k'])})"
    if kind == "fill":
        # The Face argument of opFill is IGNORED by stepOp on both sides
        # (only the supplied set is consulted); rendered as fZERO.  Rendered
        # explicitly as the ignored argument it is, never as a real input.
        return "opFill fZERO"
    if kind == "fill_of":
        return f"opFillOf ({render_face(op['face'])})"
    if kind == "tower":
        return f"opTower {render_b3(op['level'])}"
    if kind == "between":
        return f"opBetween ({render_face(op['a'])}) ({render_face(op['b'])})"
    raise MachineOverviewError(f"UNKNOWN_CONTEXT_OP:{kind}")


def render_op_list(ops: list[dict]) -> str:
    if not ops:
        return "[]"
    return " ∷ ".join(render_op(op) for op in ops) + " ∷ []"


_KIND = {
    "value_mismatch": "kValueMismatch",
    "completion_divergence": "kCompletionDivergence",
    "deadline_observation": "kDeadlineObservation",
    "availability_observation": "kAvailabilityObservation",
    "level_observation": "kLevelObservation",
    "density_observation": "kDensityObservation",
}


def render_sep_kind(kind) -> str:
    if kind is None:
        return "nothing"
    if kind in _KIND:
        return f"just {_KIND[kind]}"
    raise MachineOverviewError(f"UNKNOWN_SEPARATION_KIND:{kind!r}")


def _as_obs(x: tuple) -> tuple:
    """Normalise a separates() observation to an observation tuple.

    ``separates []`` returns the bare INPUT values (no context ran), which on
    the kernel side is ``obsDelay l`` / ``obsDelay r``; a non-empty context
    already returns a full observation tuple.  Both must render to an Obs.
    """
    if x[0] in v2.OBSERVATION_KINDS:
        return x
    if x[0] in ("omega", "ret"):
        return ("delay", x)
    raise MachineOverviewError(f"UNKNOWN_SEP_OBSERVATION:{x!r}")


def render_sep_result(sep_tuple: tuple) -> str:
    separated, ol, orr, kind = sep_tuple
    ol, orr = _as_obs(ol), _as_obs(orr)
    return (f"({render_bool(separated)} , {render_obs(ol)} , "
            f"{render_obs(orr)} , {render_sep_kind(kind)})")


# ------------------------------------------------------------------ module

MODULE_HEADER = """{-# OPTIONS --safe --cubical --guardedness #-}

-- GENERATED MODULE.  Do not edit by hand; regenerate with
--   python3 machine-overview/machine_overview/v2_agreement.py
--
-- Stage-1 ground agreement for the V2 L2-cofibration fragment
-- (design source: Atria的方案/修订片/015 §5 stage 1).
--
-- Every entry of the declared denominator is checked DEFINITIONALLY:
--   groundAgreement : checkAll ≡ true     discharged by refl
-- can only pass when the native kernel's own evaluation of applyOps agrees
-- with the Python enumerator's expected observation on ALL @@APPLYOPS@@ of them.
-- A single disagreement is a type error (that error is the verification).
--
-- SCOPE: applyOps is exhaustive over @@GROUND@@ ground values x @@OPLISTS@@
-- declared op-lists.  separates is checked on the @@SEPS@@ DESIGNATED CONTROLS
-- only (see v2_agreement.scope_disclosure): the full pair matrix would need
-- ~918k SepResult literals, beyond a feasible module; the control set is
-- pinned independently by tests/test_v2_cofibration.py::SeparationTest.
--
-- FAITHFULNESS CAVEAT (revision 015 §3.4): the face lattice here is the
-- POINT-SET model, which is SOUND but NOT COMPLETE for the interval I (a De
-- Morgan algebra).  This module registers NO mathematical claim
-- (registers_new_claim: false); no result here is evidence about the real
-- interval I (F-011).

module V2GroundAgreement where

open import Cubical.Foundations.Prelude
open import Cubical.Data.Bool.Base using (Bool; true; false; not; _and_; _or_; if_then_else_)
open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)
open import Cubical.Data.Prod.Base using (_×_; _,_; proj₁; proj₂)
open import Cubical.Data.Nat.Base using (ℕ; zero; suc)
open import Cubical.Data.List.Base using (List; []; _∷_; foldr; map)
open import V2Cofibration

record GroundCheck : Type where
  constructor gc
  field
    ops    : List Op
    inp    : V2
    expect : Obs

checkOne : GroundCheck → Bool
checkOne (gc ops inp exp) = obsEqB (proj₁ (applyOps ops inp noSupplied)) exp

record SepControl : Type where
  constructor sc
  field
    ops    : List Op
    left   : V2
    right  : V2
    expect : SepResult

checkSep : SepControl → Bool
checkSep (sc ops l r exp) = sepEqB (separates ops l r noSupplied) exp
"""


def generate_module(checks, sep_controls) -> str:
    """Render the whole agreement module from computed expected values."""
    header = (MODULE_HEADER
              .replace("@@APPLYOPS@@", str(len(checks)))
              .replace("@@GROUND@@", str(len(v2.ground_values())))
              .replace("@@OPLISTS@@", str(len(v2.declared_op_lists())))
              .replace("@@SEPS@@", str(len(sep_controls))))
    out = [header]
    out.append("\nallChecks : List GroundCheck")
    out.append("allChecks =")
    for ops, value, expected in checks:
        out.append(f"  gc ({render_op_list(ops)}) ({render_value(value)}) ({render_obs(expected)}) ∷")
    out.append("  []")
    out.append("\ncheckAll : Bool")
    out.append("checkAll = andL (map checkOne allChecks)")
    out.append("\ngroundAgreement : checkAll ≡ true")
    out.append("groundAgreement = refl")
    out.append("\nallSepControls : List SepControl")
    out.append("allSepControls =")
    for label, ops, left, right, expected in sep_controls:
        out.append(f"  -- {label}")
        out.append(f"  sc ({render_op_list(ops)}) ({render_value(left)}) "
                   f"({render_value(right)}) ({render_sep_result(expected)}) ∷")
    out.append("  []")
    out.append("\nsepAll : Bool")
    out.append("sepAll = andL (map checkSep allSepControls)")
    out.append("\nsepAgreement : sepAll ≡ true")
    out.append("sepAgreement = refl")
    out.append("")
    return "\n".join(out)


# ------------------------------------------------------------------ run

def build_checks():
    """The exhaustive applyOps denominator with Python-computed expectations."""
    ground = v2.ground_values()
    op_lists = v2.declared_op_lists()
    checks = []
    for value in ground:
        for _name, ops in op_lists:
            obs, _supplied = v2.apply_ops(ops, value)
            checks.append((ops, value, obs))
    return checks


def build_sep_controls():
    """The 11 designated controls with Python-computed expectations."""
    out = []
    for label, ops, left, right in designated_controls():
        expected = v2.separates(ops, left, right)
        out.append((label, ops, left, right, expected))
    return out


def source_manifest(generated_path: Path) -> list[dict]:
    here = Path(__file__).resolve()
    mirror = ENGINE_ROOT / "machine-overview/formal/V2Cofibration.agda"
    sem = ENGINE_ROOT / "machine-overview/machine_overview/v2_cofibration.py"
    return [
        {"role": "agreement-generator", "path": here.as_posix(),
         "sha256": sha256_file(here), "bytes": here.stat().st_size},
        {"role": "python-semantics-source", "path": sem.as_posix(),
         "sha256": sha256_file(sem), "bytes": sem.stat().st_size,
         "git_commit": verify_git_head(ENGINE_ROOT)},
        {"role": "agda-mirror-library", "path": mirror.as_posix(),
         "sha256": sha256_file(mirror), "bytes": mirror.stat().st_size,
         "git_commit": verify_git_head(ENGINE_ROOT)},
        {"role": "generated-module", "path": generated_path.as_posix(),
         "sha256": sha256_file(generated_path), "bytes": generated_path.stat().st_size},
    ]


def verify_git_head(root: Path) -> str:
    import subprocess
    return subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        capture_output=True, text=True).stdout.strip()


SCOPE_DISCLOSURE = {
    "applyops_scope": (
        "EXHAUSTIVE over the full declared denominator: every one of the "
        "289 ground values is evaluated under every one of the 11 declared "
        "op-lists, giving 3179 applyOps checks.  Not sampled."
    ),
    "separates_scope": (
        "DESIGNATED CONTROLS ONLY (11): 3 positive controls (G-b availability, "
        "G-c level, G-a density) + 5 negative controls + 3 L1-shared-kind "
        "reachability controls.  The full 289x289 pair matrix is NOT rendered: "
        "it would need ~918k SepResult literals, beyond a feasible single "
        "Agda module.  This is a rendering-budget boundary, not a mathematical "
        "claim about separates; the control set is pinned independently by "
        "tests/test_v2_cofibration.py::SeparationTest."
    ),
    "faithfulness": (
        "The face lattice is the POINT-SET model (truth functions on the "
        "4-point boolean cube): SOUND but NOT COMPLETE for the interval I, a "
        "De Morgan algebra in which f ∧ ¬f = 0 FAILS (revision 015 §3.4, "
        "machine-checked in V2Cofibration.agda §8-9).  This agreement is an "
        "ENGINEERING acceptance of enumerator faithfulness; it registers no "
        "mathematical claim (registers_new_claim: false) and no result here is "
        "evidence about the real interval I (F-011)."
    ),
}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--run-id", default=DEFAULT_RUN_ID)
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args(argv)

    run_dir = ENGINE_ROOT / "machine-overview/runs" / args.run_id
    if (run_dir / "RUN.json").exists():
        raise MachineOverviewError(f"RUN_DIRECTORY_ALREADY_EXISTS:{run_dir}")
    generated_dir = run_dir / "generated"
    generated_dir.mkdir(parents=True, exist_ok=False)
    entry = generated_dir / "V2GroundAgreement.agda"

    started = utc_now()
    print(f"[v2-agreement] run_id={args.run_id}", flush=True)

    # 1. exhaustive applyOps denominator (Python expectations)
    checks = build_checks()
    expected_total = len(v2.ground_values()) * len(v2.declared_op_lists())
    if len(checks) != expected_total:
        raise MachineOverviewError(
            f"APPLYOPS_COUNT_MISMATCH:got {len(checks)} expected {expected_total}")
    print(f"[v2-agreement] applyOps checks = {len(checks)} (exhaustive)", flush=True)

    # 2. designated separation controls
    sep_controls = build_sep_controls()
    if len(sep_controls) != 11:
        raise MachineOverviewError(f"SEP_CONTROL_COUNT:{len(sep_controls)}")
    for label, _ops, _l, _r, exp in sep_controls:
        print(f"[v2-agreement]   {label}: separated={exp[0]} kind={exp[3]}", flush=True)

    # 3. render + write the generated module
    text = generate_module(checks, sep_controls)
    write_text(entry, text)
    print(f"[v2-agreement] rendered {entry} ({len(text)} bytes)", flush=True)

    # 4. type-check it with the native kernel
    toolchain = read_json(TOOLCHAIN_JSON)
    include_dirs = list(INCLUDE_DIRS) + [f"machine-overview/runs/{args.run_id}/generated"]
    result = verify.run_kernel(
        ENGINE_ROOT, run_dir,
        label="v2-ground-agreement",
        toolchain=toolchain,
        include_dirs=include_dirs,
        entry=entry.as_posix(),
        expect_success=True,
        timeout_seconds=args.timeout,
    )
    receipt = result["receipt"]
    print(f"[v2-agreement] kernel status={receipt['status']} "
          f"expectation_met={receipt['expectation_met']} "
          f"exit_code={receipt['exit_code']}", flush=True)

    # 5. receipt
    manifest = source_manifest(entry)
    run = {
        "schema_version": "machine-overview-v2-stage1-agreement/v1",
        "run_id": args.run_id,
        "kind": "STAGE1_PYTHON_AGDA_GROUND_AGREEMENT",
        "design_source": "Atria的方案/修订片/015 §5 stage-1 (V2 L2-cofibration fragment)",
        "started_at_utc": started,
        "completed_at_utc": utc_now(),
        "registers_new_claim": False,
        "denominator": {
            "ground_values": len(v2.ground_values()),
            "op_lists": len(v2.declared_op_lists()),
            "applyops_checks": len(checks),
            "applyops_exhaustive": True,
            "sep_controls": len(sep_controls),
        },
        "kernel": receipt,
        "scope_disclosure": SCOPE_DISCLOSURE,
        "source_manifest": manifest,
        "git_state_engine": git_state(ENGINE_ROOT),
        "git_state_handoff": git_state(HANDOFF_ROOT),
        "toolchain_identity": verify.kernel_environment_text(toolchain),
        "status": "STAGE1_AGREEMENT_PASS" if receipt["expectation_met"]
                  else "STAGE1_AGREEMENT_FAIL",
    }
    write_json(run_dir / "RUN.json", run)
    write_bytes(run_dir / "source-manifest.json", json_bytes(manifest))
    print(f"[v2-agreement] status={run['status']} -> {run_dir}", flush=True)
    if not receipt["expectation_met"]:
        sys.stderr.write(result["stderr"].decode("utf-8", "replace")[:8000])
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
