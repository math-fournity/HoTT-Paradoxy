"""Four-way native-kernel verification for the gap-A DM3 unit.

Design source: Atria的方案/修订片/018 §3(A) (gap A: the interval-I oracle does
not exist) + 015 §5 + 016 §3 (DENOMINATOR_SINGLE_SOURCE) + 017 §3
(KEY_ADJUDICATION_AUDIT_TRAIL).

For each kernel witness selected by the SEARCH run this module renders four
Cubical Agda modules against the native mirror formal/V2DM3.agda and runs the
native kernel four times:

  verify            sepEqD (separatesD ops p q noSuppliedD) expected == true   (must ACCEPT, exit 0)
  controls          same-value control + delay-axis control                   (must ACCEPT, exit 0)
  negative-control  claim the witness does NOT separate                       (must be REJECTED)
  verify-replay     re-run of verify; exit code + stdout + stderr must match

ORACLE SCOPE (upgraded by this unit, 015 §5 / F-011 / 017 §5): the mirror
formal/V2DM3.agda interprets the V2 structural axes on DM3, the standard
NON-BOOLEAN De Morgan algebra, which the native kernel confirms carries the
failing boolean law a && ~a = a != 0 (boolLawFails = dm3NonBoolean, mirror
sec 10) in the SAME algebra where all three separations hold.  Hence:

    oracle_scope          = DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT
    interval_i_confirmed  = false   (DM3 is a De Morgan algebra, NOT the real
                                    cubical interval I; I's equality is not
                                    decidable, so no Bool-valued separates
                                    exists on it)
    boolean_law_needed    = false   (kernel-confirmed negative fact)

What is confirmed is the NEGATIVE statement that no boolean law is needed;
lifting DM3 to all De Morgan algebras or to I is NOT claimed (F-011).

A fifth kernel unit (VERIFY-GAP-A-DM3-BLI-*) checks the boolean-law
independence itself as an independent module: the density separation holds
AND the boolean law fails, both in the same algebra; plus a negative control
claiming the boolean law holds, which the kernel must reject.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import v2_dm3 as v2
from . import v2_dm3_agreement as A
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
SEARCH_RUN_ID = "SEARCH-GAP-A-DM3-001"

OPTIONS = "{-# OPTIONS --safe --cubical --guardedness #-}"

IMPORTS = [
    "open import Cubical.Foundations.Prelude",
    "open import Cubical.Data.Bool.Base using (Bool; true; false; not; _and_; _or_; if_then_else_)",
    "open import Cubical.Data.Maybe.Base using (Maybe; just; nothing)",
    "open import Cubical.Data.Nat.Base using (ℕ; zero; suc)",
    "open import Cubical.Data.List.Base using (List; []; _∷_)",
    "open import Cubical.Data.Prod.Base using (_×_; _,_; proj₁; proj₂)",
    "open import Cubical.Relation.Nullary.Base using (¬_)",
    "-- the DM3/B3 constructors and the meet/neg operations are imported into",
    "-- V2DM3 from V2Cofibration; Agda does not re-export open-imported names",
    "-- to importers, so the generated modules import them directly.",
    "open import V2Cofibration using (DM3; d0; da; d1; dm3Meet; dm3Neg;",
    "                                          B3; b0; b1; b2;",
    "                                          Avail; absent; pending; available)",
    "open import V2DM3",
]


# ------------------------------------------------------------------ witness

def load_kernel_witnesses(search_run_id: str = SEARCH_RUN_ID):
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
    semantics and assert it against the recorded separation before any kernel
    run.  DENOMINATOR_SINGLE_SOURCE (016 §3)."""
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
            f"DM3_WITNESS_CROSS_CHECK_FAILED:{w['witness_id']}:{checks}")
    return checks


def model_dependency(ops: list[dict], separation_kind: str) -> dict:
    """Mechanical classification of which mechanism produced the separation and
    whether that mechanism invokes point-set-only face-lattice laws (015 §5
    mandatory disclosure).  On DM3 NO mechanism invokes the point-set laws,
    because the algebra is not boolean; that is exactly what gap A closes."""
    kinds = {op.get("kind") for op in ops}
    if "between" in kinds or separation_kind == "density_observation":
        cls = "DM3_CHAIN_ORDER"
        invokes = False
        note = (
            "density/between invokes only the chain order of DM3 (dm3StrictlyBetween "
            "on 0 < a < 1), in the SAME algebra where the boolean law fails "
            "(boolLawFails = dm3NonBoolean, mirror sec 10).  The separation does "
            "NOT ride on the boolean law the point-set model carries for free; "
            "gap A is closed at the level of boolean-law independence")
    elif separation_kind == "availability_observation":
        cls = "SUPPLIED_SET_MEMBERSHIP"
        invokes = False
        note = (
            "the availability verdict depends only on decidable membership of the "
            "supplied DM3 set and the fill op, not on any lattice identity; "
            "interpretation-independent, and on DM3 it holds without the boolean law")
    elif separation_kind == "level_observation":
        cls = "BOUNDED_LEVEL_COMPARISON"
        invokes = False
        note = (
            "the tower verdict is a comparison in the bounded lattice {b0,b1,b2}, "
            "finite and decidable; no face-lattice or boolean identity is invoked")
    else:
        raise MachineOverviewError(f"UNKNOWN_DM3_SEPARATION_KIND:{separation_kind}")
    return {"class": cls, "invokes_point_set_only_laws": invokes,
            "boolean_law_needed": False,
            "point_set_law_used_as_conclusion": False, "note": note}


# ------------------------------------------------------------------ rendering

def _header(module_name: str, witness_id: str, extra: list[str]) -> list[str]:
    return [OPTIONS, "",
            "-- GENERATED MODULE for the gap-A DM3 kernel verification",
            f"-- witness {witness_id}; regenerate with",
            "--   python3 -m machine_overview.v2_dm3_verify",
            "-- DENOMINATOR_SINGLE_SOURCE: every expected literal below is",
            "-- computed by machine_overview/v2_dm3.py, the same canonical",
            "-- semantics that produced the SEARCH run.",
            "",
            f"module {module_name} where", "",
            *IMPORTS, "", *extra, ""]


def render_target(w: dict) -> str:
    left = v2.value_from_json(w["pair"]["left"])
    right = v2.value_from_json(w["pair"]["right"])
    lines = _header("Target", w["witness_id"], [
        "p : V2D", f"p = {A.render_value(left)}", "",
        "q : V2D", f"q = {A.render_value(right)}", "",
        "opsList : OpDList", f"opsList = {A.render_op_list(w['ops'])}",
    ])
    return "\n".join(lines) + "\n"


def render_verify(w: dict) -> str:
    left = v2.value_from_json(w["pair"]["left"])
    right = v2.value_from_json(w["pair"]["right"])
    expected = v2.separates(w["ops"], left, right)
    lines = _header("Verify", w["witness_id"], [
        "open import Target", "",
        "kernelVerify : sepEqD (separatesD Target.opsList Target.p Target.q noSuppliedD)",
        f"  {A.render_sep_result(expected)} ≡ true",
        "kernelVerify = refl",
    ])
    return "\n".join(lines) + "\n"


def render_controls(w: dict) -> str:
    left = v2.value_from_json(w["pair"]["left"])
    same = v2.separates(w["ops"], left, left)
    delay = v2.delay_equivalent(left, v2.value_from_json(w["pair"]["right"]))
    lines = _header("Controls", w["witness_id"], [
        "open import Target", "",
        "-- Positive control 1: identical inputs never separate under the same",
        "-- context (the context is deterministic in the supplied set).",
        "sameValueControl : sepEqD (separatesD Target.opsList Target.p Target.p noSuppliedD)",
        f"  {A.render_sep_result(same)} ≡ true",
        "sameValueControl = refl", "",
        "-- Positive control 2: the delay axis (L1 visibility).  The expected",
        "-- value is the canonical semantics' own verdict, whatever it is; the",
        "-- kernel confirms the enumerator and the mirror agree on the axis",
        "-- that the L1 fragment can see.",
        f"delayAxisControl : delayEquivD Target.p Target.q ≡ {A.render_bool(delay)}",
        "delayAxisControl = refl",
    ])
    return "\n".join(lines) + "\n"


def render_falsify(w: dict) -> str:
    """Negative control: CLAIM the witness does not separate."""
    left = v2.value_from_json(w["pair"]["left"])
    right = v2.value_from_json(w["pair"]["right"])
    _sep, ol, orr, _kind = v2.separates(w["ops"], left, right)
    wrong = (False, ol, orr, None)
    lines = _header("Falsify", w["witness_id"], [
        "open import Target", "",
        "-- NEGATIVE CONTROL.  This module deliberately CLAIMS that the witness",
        "-- does NOT separate.  It must be REJECTED by the kernel: the actual",
        "-- separation is (true , _ , _ , just _) so sepEqD reduces to false,",
        "-- and refl cannot prove false ≡ true.  A kernel ACCEPT here would mean",
        "-- the separation claim is false or the oracle is broken.",
        "wrongClaim : sepEqD (separatesD Target.opsList Target.p Target.q noSuppliedD)",
        f"  {A.render_sep_result(wrong)} ≡ true",
        "wrongClaim = refl",
    ])
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------ boolean law

def render_bli_verify() -> str:
    """The boolean-law-independence module: the density separation holds AND
    the boolean law fails, in the SAME algebra.  Both conjuncts are the
    mirror's own machine-checked theorems (witnessD / boolLawFails); this
    independent module re-states the conjunction for the external auditor."""
    lines = _header("BLIVerify", "BOOL_LAW_INDEPENDENCE", [
        "-- BOOLEAN-LAW INDEPENDENCE (gap A core).  The density separation",
        "-- (separatesD opsD pD qD noSuppliedD) holds, and the boolean law",
        "-- FAILS in the same algebra (dm3Meet da (dm3Neg da) = da != d0).",
        "-- Both are the mirror's own theorems; the conjunction is the content",
        "-- of the gap-A oracle upgrade: NO BOOLEAN LAW IS NEEDED.",
        "bliDensity : sepEqD (separatesD opsD pD qD noSuppliedD)",
        "  (true , obsDensityD true , obsDensityD false , just kDensityD) ≡ true",
        "bliDensity = witnessD", "",
        "bliNonBoolean : ¬ (dm3Meet da (dm3Neg da) ≡ d0)",
        "bliNonBoolean = boolLawFails", "",
        "bliConjunction : BoolLawIndependence",
        "bliConjunction = boolLawIndependence",
    ])
    return "\n".join(lines) + "\n"


def render_bli_falsify() -> str:
    """Negative control: CLAIM the boolean law HOLDS in DM3.  dm3Meet da
    (dm3Neg da) reduces to da, so the claim is da ≡ d0 and refl cannot
    discharge it; the kernel must reject."""
    lines = _header("BLIFalsify", "BOOL_LAW_INDEPENDENCE", [
        "-- NEGATIVE CONTROL.  This module deliberately CLAIMS that the boolean",
        "-- law HOLDS in DM3, i.e. that a && ~a = 0.  It must be REJECTED by the",
        "-- kernel: dm3Meet da (dm3Neg da) reduces to da, so the goal is",
        "-- da ≡ d0, which refl cannot prove.  A kernel ACCEPT here would mean",
        "-- DM3 is boolean and the gap-A upgrade is void.",
        "wrongClaim : dm3Meet da (dm3Neg da) ≡ d0",
        "wrongClaim = refl",
    ])
    return "\n".join(lines) + "\n"


# ------------------------------------------------------------------ kernel

def _oracle_scope(four_way: bool, dep: dict) -> dict:
    return {
        "oracle": "Cubical Agda 2.8.0 native kernel on the mirror formal/V2DM3.agda",
        "model": "DM3 (the 3-element chain 0 < a < 1, the standard NON-BOOLEAN De "
                 "Morgan algebra; mirror sec 10)",
        "oracle_scope": "DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT",
        "interval_i_confirmed": False,
        "interval_i_oracle_exists": False,
        "boolean_law_needed": False,
        "boolean_law_confirmed_unnecessary": True,
        "reason": (
            "DM3 is a non-boolean De Morgan algebra in which the native kernel "
            "confirms a && ~a = a != 0 (boolLawFails = dm3NonBoolean, mirror sec "
            "10), and in the SAME algebra all three structural separations "
            "(availability / level / density) are kernel-accepted.  DM3 is NOT "
            "the real cubical interval I: I's equality is not decidable, so no "
            "Bool-valued separates exists on it, which is exactly why the "
            "interval-I oracle gap was registered (018 §3A).  What this unit "
            "confirms is the NEGATIVE statement that no boolean law is needed, "
            "on a specific kernel-confirmed-non-boolean algebra; lifting DM3 to "
            "all De Morgan algebras or to I is NOT claimed"),
        "conclusion_evidence_about_interval_i": False,
        "gen001_capability_evidence": four_way,
        "gap_a_status": "DM3_LAYER_CONFIRMED_INTERVAL_I_LAYER_STILL_OPEN",
        "discipline": (
            "015 §5 V2 mandatory disclosure + F-011 + 017 §5 + 018 §3A: this is "
            "NOT conclusion evidence about the real interval I; it IS evidence "
            "that the input -> candidate -> oracle -> receipt chain is real, and "
            "that the structural separations do not depend on the boolean law"),
        "mechanism_class": dep["class"],
        "invokes_point_set_only_laws": dep["invokes_point_set_only_laws"],
    }


def verify_witness(w: dict, run_id: str, provenance: dict, toolchain: dict,
                   timeout: int) -> dict:
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
        print(f"[dm3-verify:{run_id}] {label}: status={out['receipt']['status']} "
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
    print(f"[dm3-verify:{run_id}] verify-replay: {replay_class['classification']}",
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
        "schema_version": "machine-overview-v2-dm3-verify-run/v1",
        "run_id": run_id,
        "kind": "GAP_A_DM3_KERNEL_VERIFICATION",
        "design_source": (
            "Atria的方案/修订片/018 §3(A) gap A + 015 §5 + 016 §3 "
            "DENOMINATOR_SINGLE_SOURCE + 017 §3 KEY_ADJUDICATION_AUDIT_TRAIL"),
        "started_at_utc": started,
        "completed_at_utc": utc_now(),
        "registers_new_claim": False,
        "registered_negative_fact": (
            "the boolean law x&&~x=0 is NOT needed for any of the three "
            "structural V2 separations; machine-confirmed by the native kernel "
            "on the non-boolean De Morgan algebra DM3 (scope: that algebra)"),
        "search_provenance": _prov,
        "witness": w,
        "cross_check": cross,
        "model_dependency_audit": dep,
        "oracle_scope": _oracle_scope(four_way, dep),
        "key_adjudication_audit_trail": {
            "adjudication_id": f"{run_id}:oracle-verdict",
            "question": (
                "does the native kernel confirm that DM3 witness "
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
                "machine-overview/formal/V2DM3.agda",
                f"machine-overview/runs/{_prov['search_run_id']}/RUN.json",
            ],
            "audit_status": "AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT",
            "depends_on": [
                _prov["search_run_id"],
                "machine-overview/formal/V2DM3.agda",
                "machine-overview/machine_overview/v2_dm3.py",
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
         "path": (MO_ROOT / "machine_overview/v2_dm3_verify.py").as_posix(),
         "sha256": sha256_file(MO_ROOT / "machine_overview/v2_dm3_verify.py")},
        {"role": "renderer",
         "path": (MO_ROOT / "machine_overview/v2_dm3_agreement.py").as_posix(),
         "sha256": sha256_file(MO_ROOT / "machine_overview/v2_dm3_agreement.py")},
        {"role": "canonical-python-semantics",
         "path": (MO_ROOT / "machine_overview/v2_dm3.py").as_posix(),
         "sha256": sha256_file(MO_ROOT / "machine_overview/v2_dm3.py")},
        {"role": "agda-mirror-library",
         "path": (MO_ROOT / "formal/V2DM3.agda").as_posix(),
         "sha256": sha256_file(MO_ROOT / "formal/V2DM3.agda")},
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


def verify_bool_law_independence(run_id: str, search_run_id: str,
                                 toolchain: dict, timeout: int) -> dict:
    """The fifth kernel unit: boolean-law independence as an independent
    module, with its own negative control.  Renders against the mirror
    directly (no search witness needed: the mirror declares pD/qD/opsD)."""
    run_dir = MO_ROOT / "runs" / run_id
    if run_dir.exists():
        raise MachineOverviewError(f"RUN_DIR_EXISTS:{run_dir}")
    gen = run_dir / "generated"
    gen.mkdir(parents=True)

    sources = {
        "BLIVerify.agda": render_bli_verify(),
        "BLIFalsify.agda": render_bli_falsify(),
    }
    for name, text in sources.items():
        write_text(gen / name, text)

    include = list(INCLUDE_BASE) + [f"machine-overview/runs/{run_id}/generated"]
    started = utc_now()
    outcomes = []
    entries = [("bli-verify", "BLIVerify.agda", True),
               ("bli-negative-control", "BLIFalsify.agda", False)]
    for label, fname, expect_success in entries:
        entry = f"machine-overview/runs/{run_id}/generated/{fname}"
        out = verify.run_kernel(ENGINE_ROOT, run_dir, label=label,
                                toolchain=toolchain, include_dirs=include,
                                entry=entry, expect_success=expect_success,
                                timeout_seconds=timeout)
        outcomes.append(out)
        print(f"[dm3-verify:{run_id}] {label}: status={out['receipt']['status']} "
              f"expectation_met={out['receipt']['expectation_met']} "
              f"exit={out['receipt']['exit_code']}", flush=True)

    replay = verify.run_kernel(ENGINE_ROOT, run_dir, label="bli-verify-replay",
                               toolchain=toolchain, include_dirs=include,
                               entry=f"machine-overview/runs/{run_id}/generated/BLIVerify.agda",
                               expect_success=True, timeout_seconds=timeout)
    replay_class = verify.classify_replay(
        outcomes[0]["receipt"], outcomes[0]["stdout"],
        replay["receipt"], replay["stdout"])
    replay_class["exit_codes"] = [outcomes[0]["receipt"]["exit_code"],
                                 replay["receipt"]["exit_code"]]
    print(f"[dm3-verify:{run_id}] bli-verify-replay: {replay_class['classification']}",
          flush=True)

    kernels = [{"label": o["receipt"]["label"], **o["receipt"]}
               for o in outcomes]
    kernels.append({"label": replay["receipt"]["label"], **replay["receipt"]})

    passed = (
        outcomes[0]["receipt"]["expectation_met"]
        and outcomes[1]["receipt"]["expectation_met"]
        and replay["receipt"]["expectation_met"]
        and bool(replay_class.get("normalized_match")))
    status = "KERNEL_BLI_PASS" if passed else "KERNEL_BLI_FAIL"

    run = {
        "schema_version": "machine-overview-v2-dm3-bli-run/v1",
        "run_id": run_id,
        "kind": "GAP_A_DM3_BOOLEAN_LAW_INDEPENDENCE",
        "design_source": "Atria的方案/修订片/018 §3(A) gap A core fact",
        "started_at_utc": started,
        "completed_at_utc": utc_now(),
        "registers_new_claim": False,
        "registered_negative_fact": (
            "the boolean law x && ~x = 0 is not needed: the density separation "
            "holds in DM3 while dm3Meet da (dm3Neg da) = da != d0, both "
            "kernel-checked in the same algebra"),
        "question": (
            "can the V2 structural separations be produced in a De Morgan "
            "algebra where the boolean law FAILS?"),
        "answer": "YES for availability / level / density (kernel-confirmed)",
        "search_run_id": search_run_id,
        "oracle_scope": {
            "oracle": "Cubical Agda 2.8.0 native kernel on formal/V2DM3.agda",
            "model": "DM3 (non-boolean De Morgan algebra)",
            "oracle_scope": "DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT",
            "interval_i_confirmed": False,
            "boolean_law_needed": False,
            "scope_of_negative_fact": (
                "the algebra DM3 as defined in mirror sec 10; NOT a claim about "
                "the real interval I (F-011)"),
        },
        "key_adjudication_audit_trail": {
            "adjudication_id": f"{run_id}:boolean-law-independence",
            "question": (
                "does the native kernel simultaneously accept the density "
                "separation and the failure of the boolean law in DM3, and "
                "reject the claim that the boolean law holds?"),
            "verdict": status,
            "verdict_reason": (
                f"bli-verify={outcomes[0]['receipt']['status']}; "
                f"bli-negative-control={outcomes[1]['receipt']['status']} "
                f"(exit {outcomes[1]['receipt']['exit_code']}); "
                f"bli-verify-replay={replay_class['classification']}"),
            "falsifier": (
                "a kernel ACCEPT of BLIFalsify.agda (i.e. a proof of "
                "dm3Meet da (dm3Neg da) ≡ d0) would overturn this verdict"),
            "evidence_anchors": [
                f"machine-overview/runs/{run_id}/RUN.json",
                f"machine-overview/runs/{run_id}/kernel/*/receipt.json",
                "machine-overview/formal/V2DM3.agda",
            ],
            "audit_status": "AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT",
            "depends_on": [
                "machine-overview/formal/V2DM3.agda",
                search_run_id,
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
         "path": (MO_ROOT / "machine_overview/v2_dm3_verify.py").as_posix(),
         "sha256": sha256_file(MO_ROOT / "machine_overview/v2_dm3_verify.py")},
        {"role": "agda-mirror-library",
         "path": (MO_ROOT / "formal/V2DM3.agda").as_posix(),
         "sha256": sha256_file(MO_ROOT / "formal/V2DM3.agda")},
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
    ap.add_argument("--bli-run-id", default=None,
                    help="also run the boolean-law-independence unit under this run id")
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
        print(f"[dm3-verify] witness={w['witness_id']} "
              f"kind={w['separation_kind']} run_id={run_id}", flush=True)
        run = verify_witness(w, run_id, provenance, toolchain, args.timeout)
        runs.append({"run_id": run_id, "status": run["status"],
                     "witness_id": w["witness_id"]})
        if run["status"] != "KERNEL_FOUR_WAY_PASS":
            failures.append(run_id)

    if args.bli_run_id:
        bli = verify_bool_law_independence(args.bli_run_id, args.search_run_id,
                                           toolchain, args.timeout)
        runs.append({"run_id": args.bli_run_id, "status": bli["status"],
                     "witness_id": "BOOL_LAW_INDEPENDENCE"})
        if bli["status"] != "KERNEL_BLI_PASS":
            failures.append(args.bli_run_id)

    summary = {
        "schema_version": "machine-overview-v2-dm3-verify-batch/v1",
        "search_run_id": args.search_run_id,
        "runs": runs,
        "all_pass": not failures,
        "failures": failures,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=1))
    return 0 if not failures else 2


if __name__ == "__main__":
    sys.exit(main())
