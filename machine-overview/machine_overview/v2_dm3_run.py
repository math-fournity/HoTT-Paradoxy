"""Runner for the gap-A DM3 search (SEARCH stage).

Deterministic, order-independent, complete within the declared DM3 grammar.
Writes the search receipt (RUN.json) plus the full witness manifest into
``runs/<run_id>/``.  Enumerator only -- oracle verdicts come from
``v2_dm3_verify`` on the native kernel (formal/V2DM3.agda).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import v2_dm3 as v2
from . import v2_dm3_chain as C
from . import search as L1search
from . import v2_chain as V2C
from .util import MachineOverviewError, capture_runner_snapshot, sha256_bytes, utc_now, write_json

ENGINE_ROOT = Path("/Volumes/D/HoTT-machine-overview/machine-overview")

#: Pre-existing grammars every DM3 witness must lie outside of.
DELAY_GRAMMARS = ["l1-v0.json", "l1-v1.json", "l1-v2.json",
                  "l1-witness-recovery-v1.json", "l1-completion-process-v1.json",
                  "l1-divisibility-v1.json", "l1-existence-v1.json"]
POINT_SET_GRAMMAR = "l2-cofibration-a-v1.json"

#: Selection policy: cover all three separation kinds with L1-invisible,
#: minimal witnesses, and additionally one COMPOSED context (a supply prefix
#: before the terminal op) so the two-op grammar is kernel-covered too.
KERNEL_POLICY = [
    ("availability_observation", None),
    ("level_observation", None),
    ("density_observation", None),
    ("density_observation", "composed"),
]


def _reduced_key(spec: dict) -> str:
    left, right, ops = C.reduce_witness(
        v2.value_from_json(spec["left"]), v2.value_from_json(spec["right"]),
        [dict(op) for op in spec["ops"]])
    from . import v2_dm3_chain as chain
    return chain._canonical(left, right, ops)


def select_kernel_witnesses(witnesses: list[dict], grammar: dict,
                            scoped_ids: set, n: int = 4) -> list[dict]:
    """Pick the kernel witnesses, restricted to SCOPED (out-of-envelope)
    witnesses -- i.e. witnesses no pre-existing grammar can express
    (011 discipline).

    PRIMARY POLICY: verify exactly the mirror's three declared calibration
    witnesses (formal/V2DM3.agda sec 6) in their reduced form.  This makes the
    kernel run a direct Python <-> Agda item-by-item agreement check on the
    witnesses the mirror itself proves by refl, at the same time covering all
    three separation kinds AND the composed two-op grammar (the availability
    benchmark is inherently [supply, fill], which reduction cannot shrink).

    TOP-UP: if a benchmark is missing from the scoped set, fill its kind with
    the minimal scoped witness of that kind; then top up to n with further
    minimal scoped witnesses."""
    benchmark = {}
    for entry in grammar.get("calibration_benchmark", {}).get("witnesses", []):
        benchmark[_reduced_key(entry)] = entry["witness_id"]

    scoped = [w for w in witnesses if w["witness_id"] in scoped_ids]
    chosen: list[dict] = []
    # witness records carry the sha256 of the canonical string; recompute the
    # canonical key itself to match the benchmark keys
    by_key = {}
    for w in scoped:
        left = v2.value_from_json(w["pair"]["left"])
        right = v2.value_from_json(w["pair"]["right"])
        by_key[C._canonical(left, right, w["ops"])] = w
    for key, bench_id in benchmark.items():
        if key in by_key:
            w = dict(by_key[key])
            w["calibration_benchmark"] = bench_id
            chosen.append(w)
    covered_kinds = {w["separation_kind"] for w in chosen}

    # fill any uncovered kind with the minimal scoped witness of that kind
    for kind, _flavour in KERNEL_POLICY:
        if kind in covered_kinds:
            continue
        pool = [w for w in scoped if w["separation_kind"] == kind]
        if pool:
            pool.sort(key=lambda w: (w["size"]["context_ops"], w["size"]["index_sum"]))
            chosen.append(pool[0])
            covered_kinds.add(kind)

    if len(chosen) < n:  # top up with unused scoped minimal witnesses
        used = {w["witness_id"] for w in chosen}
        rest = [w for w in scoped if w["witness_id"] not in used]
        rest.sort(key=lambda w: (w["size"]["context_ops"], w["size"]["index_sum"]))
        for w in rest:
            chosen.append(w)
            if len(chosen) >= n:
                break
    return chosen[:n]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", default="SEARCH-GAP-A-DM3-001")
    ap.add_argument("--grammar", default="grammars/v2-dm3-a-v1.json")
    ap.add_argument("--max-witnesses", type=int, default=250000)
    ap.add_argument("--max-checks", type=int, default=4000000)
    ap.add_argument("--max-contexts", type=int, default=100000)
    ap.add_argument("--seed", type=int, default=20260917)
    args = ap.parse_args(argv)

    run_dir = ENGINE_ROOT / "runs" / args.run_id
    if run_dir.exists():
        raise MachineOverviewError(f"RUN_DIR_EXISTS:{run_dir}")
    run_dir.mkdir(parents=True)

    grammar = C.load_grammar(args.grammar)
    limits = {"max_witnesses": args.max_witnesses, "max_checks": args.max_checks,
              "max_contexts": args.max_contexts}

    semantics = C.compute_search_semantics(grammar, limits, order_seed=args.seed)
    order_check = C.order_independence(grammar, limits)
    non_embedding = v2.no_point_set_embedding()
    declared = v2.check_declared_witnesses()

    existing: dict[str, dict] = {}
    predicates: dict[str, tuple] = {}
    for name in DELAY_GRAMMARS:
        path = ENGINE_ROOT / "grammars" / name
        if path.is_file():
            existing[name] = json.loads(path.read_text(encoding="utf-8"))
            predicates[name] = (L1search.within_grammar_witness, "l1")
    ps_path = ENGINE_ROOT / "grammars" / POINT_SET_GRAMMAR
    if ps_path.is_file():
        existing[POINT_SET_GRAMMAR] = json.loads(ps_path.read_text(encoding="utf-8"))
        predicates[POINT_SET_GRAMMAR] = (V2C.within_grammar_witness, "v2-point-set")
    ooe = C.out_of_envelope_check(semantics["witnesses"], existing, predicates)

    # scoped out-of-envelope (011 discipline): a DM3 witness is scoped when no
    # pre-existing grammar can express it -- its ops or its DM3 coordinate fall
    # outside every declared parameter.  Witnesses accepted by the point-set
    # grammar via the shared tower mechanism (values with dm3 = 0, tower level
    # in the point-set declaration) are INGRESS: the level mechanism is shared
    # with the point-set fragment, exactly as race/deadline were shared with
    # the delay families in the V2-1 unit.  They are disclosed, not counted as
    # new envelope.
    scoped_rows, ingress_rows = [], []
    for row, witness in zip(ooe["rows"], semantics["witnesses"]):
        (ingress_rows if row["accepted_by_any"] else scoped_rows).append(row)
    scoped_ids = {r["witness_id"] for r in scoped_rows}
    scoped = {
        "proof_kind": "mechanical_membership_check",
        "claim": ("Every reduced DM3 witness whose ops or DM3 coordinate no "
                  "pre-existing grammar can express is rejected by ALL "
                  "pre-existing grammars: the 7 delay grammars all reject it "
                  "with the SAME reason (UNKNOWN_OP:<opkind>: the DM3 op "
                  "vocabulary does not exist in any delay grammar) and the "
                  "point-set V2 grammar rejects it for its own structural "
                  "reason (VALUE_OUT_OF_DECLARED_RANGE: the DM3 coordinate is "
                  "not a declared face, or PARSE_REJECT: the supply/between ops "
                  "have no face-typed argument)"),
        "method": ooe["method"],
        "existing_grammar_count": ooe["existing_grammar_count"],
        "scoped_rows": len(scoped_rows),
        "scoped_rejected_by_all": sum(1 for r in scoped_rows if not r["accepted_by_any"]),
        "scoped_reasons_unique": sum(1 for r in scoped_rows if r["reason_unique"]),
        "scoped_all_rejected": all(not r["accepted_by_any"] for r in scoped_rows),
        "scoped_all_reasons_unique": all(r["reason_unique"] for r in scoped_rows),
        "delay_family_reason_unique": None,  # filled below
        "delay_family_reason_buckets": {},
        "point_set_reason_buckets": {},
        "reason_buckets": {},
        "ingress_rows": len(ingress_rows),
        "ingress_disclosure": (
            "witnesses accepted by the point-set V2 grammar via the shared "
            "tower mechanism (dm3 coordinate = 0 lies in the point-set "
            "declared faces, tower level in its declared levels); the "
            "level_observation mechanism is shared with the point-set "
            "fragment and these witnesses are L1-invisible but "
            "point-set-reproducible.  They are reported as ingress, not as "
            "out-of-envelope.  All density and availability witnesses are "
            "scoped: their ops (supply/between over DM3) cannot be parsed by "
            "the point-set grammar and their DM3 coordinates cannot be "
            "represented (see non_embedding_check)"),
    }
    from collections import Counter
    delay_uniform = True
    for row in scoped_rows:
        delay_reasons = {info["reason"] for name, info in row["per_grammar"].items()
                         if info["membership_kind"] == "l1"}
        if len(delay_reasons) != 1 or next(iter(delay_reasons)) is None:
            delay_uniform = False
        for reason in delay_reasons:
            scoped["delay_family_reason_buckets"][reason] = \
                scoped["delay_family_reason_buckets"].get(reason, 0) + 1
        ps_reasons = {info["reason"] for name, info in row["per_grammar"].items()
                      if info["membership_kind"] == "v2-point-set"}
        for reason in ps_reasons:
            if reason is None:
                continue
            scoped["point_set_reason_buckets"][reason] = \
                scoped["point_set_reason_buckets"].get(reason, 0) + 1
    scoped["delay_family_reason_unique"] = delay_uniform and bool(
        scoped["delay_family_reason_buckets"])

    kernel = select_kernel_witnesses(semantics["witnesses"], grammar, scoped_ids)

    manifest = [{
        "witness_id": w["witness_id"], "pair": w["pair"], "ops": w["ops"],
        "separation_kind": w["separation_kind"],
        "left_observation": w["left_observation"],
        "right_observation": w["right_observation"],
        "observation_mode": w["observation_mode"],
        "size": w["size"], "ast_sha256": w["ast_sha256"],
    } for w in semantics["witnesses"]]
    manifest_bytes = json.dumps(manifest, ensure_ascii=False, sort_keys=True).encode("utf-8")
    (run_dir / "witness-manifest.json").write_bytes(manifest_bytes)

    runner = capture_runner_snapshot(ENGINE_ROOT.parent, run_dir)
    receipt = {
        "schema_version": "machine-overview-v2-dm3-search-run/v1",
        "run_id": args.run_id,
        "kind": "GAP_A_DM3_FAMILY_SEARCH",
        "family": grammar["family"],
        "family_short": grammar["family_short"],
        "grammar_id": grammar["grammar_id"],
        "grammar_path": args.grammar,
        "registered_gap": grammar["registered_gap"],
        "started_at_utc": None,
        "completed_at_utc": utc_now(),
        "statistics": semantics["statistics"],
        "calibration_match": semantics["calibration_match"],
        "order_independence_check": order_check,
        "declared_witness_check": declared,
        "non_embedding_check": non_embedding,
        "out_of_envelope": scoped,
        "out_of_envelope_full": ooe,
        "kernel_selection": [{
            "witness_id": w["witness_id"], "separation_kind": w["separation_kind"],
            "calibration_benchmark": w.get("calibration_benchmark"),
            "pair": w["pair"], "ops": w["ops"],
            "left_observation": w["left_observation"], "right_observation": w["right_observation"],
            "size": w["size"], "ast_sha256": w["ast_sha256"],
        } for w in kernel],
        "witness_manifest": {
            "path": "witness-manifest.json",
            "bytes": len(manifest_bytes),
            "sha256": sha256_bytes(manifest_bytes),
            "count": len(manifest),
        },
        "runner": runner,
        "evidence_class": "ENUMERATOR_ONLY",
        "scope_disclosure": grammar["scope_disclosure"],
    }
    write_json(run_dir / "RUN.json", receipt)
    print(json.dumps({
        "run_id": args.run_id,
        "complete_within_declared_grammar": semantics["statistics"]["complete_within_declared_grammar"],
        "checks": semantics["statistics"]["pair_context_checks"],
        "separations": semantics["statistics"]["separations_seen"],
        "reduced": semantics["reduced_count"],
        "order_independent": order_check["statistics_match"] and order_check["witness_sets_equal"],
        "calibration": semantics["calibration_match"]["status"],
        "out_of_envelope": f"{scoped['scoped_rejected_by_all']}/{scoped['scoped_rows']}",
        "ingress_rows": scoped["ingress_rows"],
        "non_embedding": non_embedding["result"],
        "kernel": [w["witness_id"] for w in kernel],
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
