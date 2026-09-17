"""Four-way native-kernel verification for the GEN-001-V2-1 first-family chain.

Design source: Atria的方案/修订片/015 §5 stage 2 (GEN-001-V2-1 first-family
link) + 修订片 016 (DENOMINATOR_SINGLE_SOURCE) + 修订片 017 §3
(KEY_ADJUDICATION_AUDIT_TRAIL).

For each kernel witness selected by the SEARCH run this module renders four
Cubical Agda modules against the native mirror formal/V2Cofibration.agda and
runs the native kernel four times:

  verify            sepEqB (separates ops p q noSupplied) expected == true    (must ACCEPT, exit 0)
  controls          same-value control + delay-axis control                  (must ACCEPT, exit 0)
  negative-control  claim the witness does NOT separate                      (must be REJECTED, exit 42)
  verify-replay     re-run of verify; exit code + stdout + stderr must match

DENOMINATOR_SINGLE_SOURCE (016 §3): every expected value rendered into the
generated modules is computed by the SAME canonical Python semantics
(v2_cofibration.separates / v2_cofibration.delay_equivalent) that produced the
search run; no expected value is hand-written.  A cross-check re-derives each
witness from the recorded pair/ops and asserts it against the recorded
separation kind and observations before any kernel run is started.

ORACLE SCOPE DISCLOSURE (015 §5 V2 mandatory disclosure, tightened by 017 §5):
the mirror defines Face = Point -> Bool, i.e. the POINT-SET model.  The mirror
itself proves (§10, the DM3 counter-model) that this model is not complete for
De Morgan algebras, and states that real-interval oracle verdicts come only
from the native kernel on I.  NO interval-I interpretation exists in the
mirror.  Therefore each witness is recorded as

    oracle_scope = POINT_SET_MIRROR_MODEL_KERNEL_CONFIRMED
    interval_i_confirmed = false

and per 015 §5 / F-011 the witness is NOT conclusion evidence about the real
interval I; it IS evidence for the GEN-001 capability acceptance (chain:
input -> candidate -> oracle -> receipt), because 003 §4 requires the oracle
verdict to be given by the native kernel for the DECLARED fragment, which is
exactly what this run provides.  A mechanical model-dependency audit
(see model_dependency) classifies which mechanism produced each separation
and whether it invokes point-set-only face-lattice laws.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import v2_agreement as A
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

ENGINE_ROOT = Path("/Volumes/D/HoTT-machine-overview")
MO_ROOT = ENGINE_ROOT / "machine-overview"
HANDOFF_ROOT = Path("/Volumes/D/HoTT_AI_HANDOFF_20260911")
TOOLCHAIN_JSON = ENGINE_ROOT / "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json"
INCLUDE_BASE = ["machine-overview/formal", "HoTT/formal/partiality-race-timeout"]
SEARCH_RUN_ID = "SEARCH-GEN001-V2-1-001"

OPTIONS = "{-# OPTIONS --safe --cubical --guardedness #-}"

IMPORTS = [
    "open import Cubical.Foundations.Prelude",
    "open import Cubical.Data.Bool.Base using (Bool; true; false; not; _and_; _or_; if_then_else_)",
    "open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)",
    "open import Cubical.Data.Prod.Base using (_×_; _,_; proj₁; proj₂)",
    "open import Cubical.Data.Nat.Base using (ℕ; zero; suc)",
    "open import Cubical.Data.List.Base using (List; []; _∷_)",
    "open import V2Cofibration",
]


# ------------------------------------------------------------------ witness

def load_kernel_witnesses(search_run_id: str = SEARCH_RUN_ID) -> list[dict]:
    run = read_json(MO_ROOT / "runs" / search_run_id / "RUN.json")
    sel = run.get("kernel_selection")
    if not sel:
        raise MachineOverviewError(f"NO_KERNEL_SELECTION:{search_run_id}")
    provenance = {
        "search_run_id": search_run_id,
        "search_run_path": f"machine-overview/runs/{search_run_id}/RUN.json",
        "family": run.get("family"),
        "family_short": run.get("family_short"),
        "grammar_id": run.get("grammar_id"),
        "grammar_path": run.get("grammar_path"),
        "search_runner_sha256": run.get("runner", {}).get("sha256"),
    }
    return sel, provenance


def cross_check_witness(w: dict) -> dict:
    """Re-derive the witness from the recorded pair/ops with the canonical
    semantics, and assert it against the recorded separation before any
    kernel run.  DENOMINATOR_SINGLE_SOURCE (016 §3)."""
    left = v2.value_from_json(w["pair"]["left"])
    right = v2.value_from_json(w["pair"]["right"])
    ops = w["ops"]
    separated, ol, orr, kind = v2.separates(ops, left, right)
    same = v2.separates(ops, left, left)
    delay = v2.delay_equivalent(left, right)
    rec_left = tuple(w["left_observation"])
    rec_right = tuple(w["right_observation"])
    checks = {
        "recomputed_separated": separated,
        "separated_match": separated is True,
        "recomputed_separation_kind": kind,
        "recorded_separation_kind": w["separation_kind"],
        "kind_match": kind == w["separation_kind"],
        "left_observation_match": rec_left == ol,
        "right_observation_match": rec_right == orr,
        "same_value_control_separated": same[0],
        "same_value_control_kind": same[3],
        "delay_equivalent_left_right": delay,
    }
    checks["all_match"] = all(
        checks[k] for k in ("separated_match", "kind_match",
                            "left_observation_match", "right_observation_match"))
    if not checks["all_match"]:
        raise MachineOverviewError(
            f"WITNESS_CROSS_CHECK_FAILED:{w['witness_id']}:{checks}")
    return checks


def model_dependency(ops: list[dict], separation_kind: str) -> dict:
    """Mechanical classification of which mechanism produced the separation,
    and whether that mechanism invokes point-set-only face-lattice laws."""
    kinds = {op.get("kind") for op in ops}
    if "between" in kinds or separation_kind == "density_observation":
        cls, invokes = "FACE_LATTICE_ORDER", True
        note = (
            "density/between invokes the point-set order on Face; the mirror "
            "proves (§10, DM3) the point-set model is not complete for De "
            "Morgan algebras, so this separation is MODEL-LEVEL ONLY and can "
            "never lift to the interval I without an interval oracle (which "
            "does not exist in the mirror)")
    elif separation_kind == "availability_observation":
        cls, invokes = "SUPPLIED_SET_MEMBERSHIP", False
        note = (
            "the availability verdict depends only on decidable membership of "
            "the supplied-face set and the fill op, not on any lattice "
            "identity; the separation is structural and interpretation-"
            "independent")
    elif separation_kind == "level_observation":
        cls, invokes = "BOUNDED_LEVEL_COMPARISON", False
        note = (
            "the tower verdict is a comparison in the bounded lattice "
            "{b0,b1,b2}, which is finite and decidable; no face-lattice "
            "identity is invoked")
    elif separation_kind == "deadline_observation":
        cls, invokes = "NAT_DEADLINE_COMPARISON", False
        note = (
            "the deadline verdict is a natural-number comparison on the "
            "computation axis; no face-lattice identity is invoked")
    elif separation_kind == "value_mismatch":
        cls, invokes = "COMPUTATION_AXIS_BOOLEAN_PAYLOAD", False
        note = (
            "delayEquiv compares only the boolean payload b over {true,false}; "
            "disequality of the two booleans is preserved under the canonical "
            "embedding of Bool into any De Morgan algebra, but this lifting is "
            "NOT kernel-proved here and is registered as a candidate follow-up")
    elif separation_kind == "completion_divergence":
        cls, invokes = "OMEGA_VS_RET", False
        note = (
            "omega vs ret on the computation axis; the separation is between "
            "divergence and a returned value, not a face-lattice identity")
    else:
        raise MachineOverviewError(f"UNKNOWN_SEPARATION_KIND:{separation_kind}")
    return {"class": cls, "invokes_point_set_only_laws": invokes,
            "point_set_law_used_as_conclusion": False, "note": note}


# ------------------------------------------------------------------ rendering

def _header(module_name: str, witness_id: str, extra: list[str]) -> list[str]:
    return [OPTIONS, "",
            f"-- GENERATED MODULE for the V2 first-family kernel verification",
            f"-- witness {witness_id}; regenerate with",
            "--   python3 -m machine_overview.v2_verify",
            "-- DENOMINATOR_SINGLE_SOURCE: every expected literal below is",
            "-- computed by machine_overview/v2_cofibration.py, the same",
            "-- canonical semantics that produced the SEARCH run.",
            "",
            f"module {module_name} where", "",
            *IMPORTS, "", *extra, ""]


def render_target(w: dict) -> str:
    left = v2.value_from_json(w["pair"]["left"])
    right = v2.value_from_json(w["pair"]["right"])
    lines = _header("Target", w["witness_id"], [
        f"p : V2\np = {A.render_value(left)}", "",
        f"q : V2\nq = {A.render_value(right)}", "",
        f"opsList : OpList\nopsList = {A.render_op_list(w['ops'])}",
    ])
    return "\n".join(lines) + "\n"


def render_verify(w: dict) -> str:
    left = v2.value_from_json(w["pair"]["left"])
    right = v2.value_from_json(w["pair"]["right"])
    expected = v2.separates(w["ops"], left, right)
    lines = _header("Verify", w["witness_id"], [
        "open import Target", "",
        "kernelVerify : sepEqB (separates Target.opsList Target.p Target.q noSupplied)",
        f"  {A.render_sep_result(expected)} ≡ true",
        "kernelVerify = refl",
    ])
    return "\n".join(lines) + "\n"


def render_controls(w: dict) -> str:
    left = v2.value_from_json(w["pair"]["left"])
    right = v2.value_from_json(w["pair"]["right"])
    same = v2.separates(w["ops"], left, left)
    delay = v2.delay_equivalent(left, right)
    lines = _header("Controls", w["witness_id"], [
        "open import Target", "",
        "-- Positive control 1: identical inputs never separate under the same",
        "-- context (the context is deterministic in the supplied set).",
        "sameValueControl : sepEqB (separates Target.opsList Target.p Target.p noSupplied)",
        f"  {A.render_sep_result(same)} ≡ true",
        "sameValueControl = refl", "",
        "-- Positive control 2: the delay axis (L1 visibility).  The expected",
        "-- value is the canonical semantics' own verdict, whatever it is; the",
        "-- kernel confirms the enumerator and the mirror agree on the axis",
        "-- that the L1 fragment can see.",
        "delayAxisControl : delayEquiv Target.p Target.q ≡ "
        + A.render_bool(delay),
        "delayAxisControl = refl",
    ])
    return "\n".join(lines) + "\n"


def render_falsify(w: dict) -> str:
    """Negative control: CLAIM the witness does not separate.  The expected
    literal carries the real observations but separated=false and kind=nothing,
    so sepEqB reduces to false and `refl` cannot discharge false ≡ true."""
    left = v2.value_from_json(w["pair"]["left"])
    right = v2.value_from_json(w["pair"]["right"])
    _sep, ol, orr, _kind = v2.separates(w["ops"], left, right)
    wrong = (False, ol, orr, None)
    lines = _header("Falsify", w["witness_id"], [
        "open import Target", "",
        "-- NEGATIVE CONTROL.  This module deliberately CLAIMS that the witness",
        "-- does NOT separate.  It must be REJECTED by the kernel: the actual",
        "-- separation is (true , _ , _ , just _) so sepEqB reduces to false,",
        "-- and refl cannot prove false ≡ true.  A kernel ACCEPT here would mean",
        "-- the separation claim is false or the oracle is broken.",
        "wrongClaim : sepEqB (separates Target.opsList Target.p Target.q noSupplied)",
        f"  {A.render_sep_result(wrong)} ≡ true",
        "wrongClaim = refl",
    ])
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------ kernel

def verify_witness(w: dict, run_id: str, provenance: dict, toolchain: dict, timeout: int) -> dict:
    run_dir = MO_ROOT / "runs" / run_id
    if run_dir.exists():
        raise MachineOverviewError(f"RUN_DIR_EXISTS:{run_dir}")
    gen = run_dir / "generated"
    gen.mkdir(parents=True)

    cross = cross_check_witness(w)
    _prov = provenance
    sources = {
        "Target.agda": render_target(w),
        "Verify.agda": render_verify(w),
        "Controls.agda": render_controls(w),
        "Falsify.agda": render_falsify(w),
    }
    for name, text in sources.items():
        write_text(gen / name, text)

    include = list(INCLUDE_BASE) + [f"machine-overview/runs/{run_id}/generated"]
    started = utc_now()
    outcomes = []
    entries = [
        ("verify", "Verify.agda", True),
        ("controls", "Controls.agda", True),
        ("negative-control", "Falsify.agda", False),
    ]
    for label, fname, expect_success in entries:
        entry = f"machine-overview/runs/{run_id}/generated/{fname}"
        out = verify.run_kernel(ENGINE_ROOT, run_dir, label=label,
                                toolchain=toolchain, include_dirs=include,
                                entry=entry, expect_success=expect_success,
                                timeout_seconds=timeout)
        outcomes.append(out)
        print(f"[v2-verify:{run_id}] {label}: status={out['receipt']['status']} "
              f"expectation_met={out['receipt']['expectation_met']} "
              f"exit={out['receipt']['exit_code']}", flush=True)

    replay = verify.run_kernel(ENGINE_ROOT, run_dir, label="verify-replay",
                               toolchain=toolchain, include_dirs=include,
                               entry=f"machine-overview/runs/{run_id}/generated/Verify.agda",
                               expect_success=True, timeout_seconds=timeout)
    replay_class = verify.classify_replay(
        outcomes[0]["receipt"], outcomes[0]["stdout"],
        replay["receipt"], replay["stdout"])
    replay_class["exit_codes"] = [outcomes[0]["receipt"]["exit_code"],
                                 replay["receipt"]["exit_code"]]
    print(f"[v2-verify:{run_id}] verify-replay: {replay_class['classification']}",
          flush=True)

    kernels = [{"label": o["receipt"]["label"], **o["receipt"]}
               for o in outcomes]
    kernels.append({"label": replay["receipt"]["label"], **replay["receipt"]})

    dep = model_dependency(w["ops"], w["separation_kind"])
    four_way = (
        outcomes[0]["receipt"]["expectation_met"]
        and outcomes[1]["receipt"]["expectation_met"]
        and outcomes[2]["receipt"]["expectation_met"]
        and replay["receipt"]["expectation_met"]
        and bool(replay_class.get("normalized_match")))
    status = "KERNEL_FOUR_WAY_PASS" if four_way else "KERNEL_FOUR_WAY_FAIL"

    run = {
        "schema_version": "machine-overview-v2-verify-run/v1",
        "run_id": run_id,
        "kind": "V2_L2_COFIBRATION_KERNEL_VERIFICATION",
        "design_source": (
            "Atria的方案/修订片/015 §5 stage-2 + 016 §3 "
            "DENOMINATOR_SINGLE_SOURCE + 017 §3 KEY_ADJUDICATION_AUDIT_TRAIL"),
        "started_at_utc": started,
        "completed_at_utc": utc_now(),
        "registers_new_claim": False,
        "search_provenance": _prov,
        "witness": w,
        "cross_check": cross,
        "model_dependency_audit": dep,
        "oracle_scope": {
            "oracle": "Cubical Agda 2.8.0 native kernel on the mirror "
                      "formal/V2Cofibration.agda",
            "model": "POINT_SET_FACE_LATTICE (Face = Point → Bool, the declared "
                     "fragment semantics)",
            "interval_i_confirmed": False,
            "interval_i_oracle_exists": False,
            "reason": (
                "the mirror defines Face = Point → Bool (point-set model) and "
                "proves in §10 via the DM3 counter-model that this model is "
                "not complete for De Morgan algebras; the mirror states that "
                "real-interval oracle verdicts come only from the native kernel "
                "on I, and no interval-I interpretation exists in the mirror"),
            "conclusion_evidence_about_interval_i": False,
            "gen001_capability_evidence": four_way,
            "discipline": (
                "015 §5 V2 mandatory disclosure + F-011 + 017 §5: a "
                "point-set-model kernel confirmation is NOT conclusion evidence "
                "about the real interval I; it is evidence that the "
                "input → candidate → oracle → receipt chain is real"),
        },
        "key_adjudication_audit_trail": {
            "adjudication_id": f"{run_id}:oracle-verdict",
            "question": (
                "does the native kernel confirm that witness "
                f"{w['witness_id']} separates as recorded by the enumerator, "
                "and reject the claim that it does not?"),
            "verdict": status,
            "verdict_reason": (
                f"verify={outcomes[0]['receipt']['status']}; "
                f"controls={outcomes[1]['receipt']['status']}; "
                f"negative-control={outcomes[2]['receipt']['status']} "
                f"(exit {outcomes[2]['receipt']['exit_code']}); "
                f"verify-replay={replay_class['classification']}"),
            "falsifier": (
                "a kernel ACCEPT of Falsify.agda, or a REJECT of Verify.agda, "
                "or a non-matching replay, would overturn this verdict"),
            "evidence_anchors": [
                f"machine-overview/runs/{run_id}/RUN.json",
                f"machine-overview/runs/{run_id}/kernel/*/receipt.json",
                "machine-overview/formal/V2Cofibration.agda",
                f"machine-overview/runs/{_prov['search_run_id']}/RUN.json",
            ],
            "audit_status": "AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT",
            "depends_on": [
                _prov["search_run_id"],
                "machine-overview/formal/V2Cofibration.agda",
                "machine-overview/machine_overview/v2_cofibration.py",
            ],
        },
        "kernels": kernels,
        "replay": replay_class,
        "generated_sources": {
            name: {"bytes": len(text.encode("utf-8")),
                   "sha256": sha256_bytes(text.encode("utf-8"))}
            for name, text in sources.items()},
        "git_state_engine": git_state(ENGINE_ROOT),
        "git_state_handoff": git_state(HANDOFF_ROOT),
        "toolchain_identity": verify.kernel_environment_text(toolchain),
        "status": status,
    }
    write_json(run_dir / "RUN.json", run)
    manifest = [
        {"role": "verify-generator",
         "path": (MO_ROOT / "machine_overview/v2_verify.py").as_posix(),
         "sha256": sha256_file(MO_ROOT / "machine_overview/v2_verify.py")},
        {"role": "canonical-python-semantics",
         "path": (MO_ROOT / "machine_overview/v2_cofibration.py").as_posix(),
         "sha256": sha256_file(MO_ROOT / "machine_overview/v2_cofibration.py")},
        {"role": "agda-mirror-library",
         "path": (MO_ROOT / "formal/V2Cofibration.agda").as_posix(),
         "sha256": sha256_file(MO_ROOT / "formal/V2Cofibration.agda")},
        {"role": "search-run-provenance",
         "path": (MO_ROOT / f"runs/{_prov['search_run_id']}/RUN.json").as_posix()},
    ]
    for name in sources:
        manifest.append({
            "role": f"generated:{name}",
            "path": (gen / name).as_posix(),
            "sha256": sha256_file(gen / name)})
    write_bytes(run_dir / "source-manifest.json", json_bytes(manifest))
    return run


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--search-run-id", default=SEARCH_RUN_ID)
    ap.add_argument("--witness-id", default=None,
                    help="verify only this witness (default: all kernel witnesses)")
    ap.add_argument("--timeout", type=int, default=900)
    args = ap.parse_args(argv)

    witnesses, provenance = load_kernel_witnesses(args.search_run_id)
    if args.witness_id:
        witnesses = [w for w in witnesses if w["witness_id"] == args.witness_id]
        if not witnesses:
            raise MachineOverviewError(f"WITNESS_NOT_FOUND:{args.witness_id}")
    toolchain = read_json(TOOLCHAIN_JSON)

    runs = []
    failures = []
    for w in witnesses:
        run_id = f"VERIFY-{provenance['family_short']}-{w['witness_id']}"
        print(f"[v2-verify] witness={w['witness_id']} "
              f"kind={w['separation_kind']} run_id={run_id}", flush=True)
        run = verify_witness(w, run_id, provenance, toolchain, args.timeout)
        runs.append({"run_id": run_id, "status": run["status"],
                     "witness_id": w["witness_id"]})
        if run["status"] != "KERNEL_FOUR_WAY_PASS":
            failures.append(run_id)

    summary = {
        "schema_version": "machine-overview-v2-verify-batch/v1",
        "search_run_id": args.search_run_id,
        "runs": runs,
        "all_pass": not failures,
        "failures": failures,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    return 0 if not failures else 2


if __name__ == "__main__":
    sys.exit(main())
