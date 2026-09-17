"""Runner for the GEN-001-V2-1 family chain (SEARCH stage).

Deterministic, order-independent, complete within the declared V2 grammar.
Writes the search receipt (RUN.json) plus the full witness manifest into
``runs/<run_id>/``.  Enumerator only — oracle verdicts come from v2_verify.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import v2_chain as C
from . import search as L1search
from .util import MachineOverviewError, capture_runner_snapshot, sha256_bytes, utc_now, write_json

ENGINE_ROOT = Path("/Volumes/D/HoTT-machine-overview/machine-overview")

DELAY_GRAMMARS = ["l1-v0.json", "l1-v1.json", "l1-v2.json", "l1-witness-recovery-v1.json",
                  "l1-completion-process-v1.json", "l1-divisibility-v1.json", "l1-existence-v1.json"]

# constructors x mechanisms the kernel must cover (selection policy, not a filter)
KERNEL_POLICY = [
    ("availability_observation", None, True),          # family core, L1-invisible
    ("level_observation", "availability_verdict_level_split", False),  # new continuation x new kind
    ("density_observation", None, True),               # G-a, L1-invisible
    ("availability_observation", "availability_verdict_supplied_face_revealed", False),
]


def select_kernel_witnesses(witnesses: list[dict], n: int = 4) -> list[dict]:
    """Pick up to n witnesses covering distinct constructor x mechanism cells,
    preferring minimal size and (where the policy asks) L1 invisibility."""
    from . import v2_cofibration as v2
    chosen: list[dict] = []
    for kind, cont, want_invisible in KERNEL_POLICY:
        pool = [w for w in witnesses if w["separation_kind"] == kind
                and (cont is None or w["bound_continuation"] == cont)]
        if want_invisible:
            inv = [w for w in pool
                   if C.l1_invisible(v2.value_from_json(w["pair"]["left"]),
                                     v2.value_from_json(w["pair"]["right"]))]
            if inv:
                pool = inv
        pool.sort(key=lambda w: (w["size"]["context_ops"], w["size"]["index_sum"]))
        if pool:
            chosen.append(pool[0])
        if len(chosen) >= n:
            break
    if len(chosen) < n:  # top up with any unused minimal witnesses
        used = {w["witness_id"] for w in chosen}
        rest = [w for w in witnesses if w["witness_id"] not in used]
        rest.sort(key=lambda w: (w["size"]["context_ops"], w["size"]["index_sum"]))
        for w in rest:
            chosen.append(w)
            if len(chosen) >= n:
                break
    return chosen[:n]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--grammar", default="grammars/l2-cofibration-a-v1.json")
    ap.add_argument("--max-witnesses", type=int, default=250000)
    ap.add_argument("--max-checks", type=int, default=4000000)
    ap.add_argument("--max-contexts", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=20260913)
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

    existing = {}
    for name in DELAY_GRAMMARS:
        path = ENGINE_ROOT / "grammars" / name
        if path.is_file():
            existing[name] = json.loads(path.read_text(encoding="utf-8"))
    ooe = C.out_of_envelope_check(semantics["witnesses"], existing,
                                  L1search.within_grammar_witness)

    # scoped out-of-envelope (011 discipline): witnesses binding a new declared
    # continuation OR using a V2 structural op; pure race/deadline witnesses are
    # the L1-shared mechanism set and are reported as ingress, not as out-of-envelope
    new_cont = set(C.new_continuation_ids(grammar))
    struct = {"supply", "fill", "fill_of", "tower", "between"}
    scoped_rows, ingress_rows = [], []
    for row, witness in zip(ooe["rows"], semantics["witnesses"]):
        is_scoped = (row["bound_continuation"] in new_cont
                     or any(op["kind"] in struct for op in witness["ops"]))
        (scoped_rows if is_scoped else ingress_rows).append(row)
    scoped = {
        "proof_kind": "mechanical_membership_check",
        "claim": ("Every reduced V2-A witness that binds a new declared V2 continuation "
                  "or uses a V2 structural op lies outside every pre-existing delay "
                  "grammar, with a unique rejection reason"),
        "method": ooe["method"],
        "existing_grammar_count": ooe["existing_grammar_count"],
        "scoped_rows": len(scoped_rows),
        "scoped_rejected_by_all": sum(1 for r in scoped_rows if not r["accepted_by_any"]),
        "scoped_reasons_unique": sum(1 for r in scoped_rows if r["reason_unique"]),
        "scoped_all_rejected": all(not r["accepted_by_any"] for r in scoped_rows),
        "scoped_all_reasons_unique": all(r["reason_unique"] for r in scoped_rows),
        "reason_buckets": {},
        "ingress_rows": len(ingress_rows),
        "ingress_disclosure": ("pure race/deadline witnesses with no structural op and no "
                               "new continuation; their mechanisms (value_mismatch / "
                               "deadline_observation) are L1-reproducible and are shared "
                               "with the five delay families (012 §2.3 ingress)"),
    }
    from collections import Counter
    for row in scoped_rows:
        key = next(iter(row["reasons"].keys()))
        scoped["reason_buckets"][key] = scoped["reason_buckets"].get(key, 0) + 1

    kernel = select_kernel_witnesses(semantics["witnesses"], 4)

    # full witness manifest (compact) + integrity digest
    manifest = [{
        "witness_id": w["witness_id"], "pair": w["pair"], "ops": w["ops"],
        "separation_kind": w["separation_kind"],
        "bound_continuation": w["bound_continuation"],
        "left_observation": w["left_observation"],
        "right_observation": w["right_observation"],
        "observation_mode": w["observation_mode"],
        "size": w["size"], "ast_sha256": w["ast_sha256"],
    } for w in semantics["witnesses"]]
    manifest_bytes = json.dumps(manifest, ensure_ascii=False, sort_keys=True).encode("utf-8")
    (run_dir / "witness-manifest.json").write_bytes(manifest_bytes)

    runner = capture_runner_snapshot(ENGINE_ROOT.parent, run_dir)
    receipt = {
        "schema_version": "machine-overview-v2-search-run/v1",
        "run_id": args.run_id,
        "kind": "V2_L2_COFIBRATION_FAMILY_SEARCH",
        "family": grammar["family"],
        "family_short": grammar["family_short"],
        "grammar_id": grammar["grammar_id"],
        "grammar_path": args.grammar,
        "started_at_utc": None,
        "completed_at_utc": utc_now(),
        "statistics": semantics["statistics"],
        "calibration_match": semantics["calibration_match"],
        "continuation_map_coverage": semantics["continuation_map_coverage"],
        "order_independence_check": order_check,
        "out_of_envelope": scoped,
        "kernel_selection": [{
            "witness_id": w["witness_id"], "separation_kind": w["separation_kind"],
            "bound_continuation": w["bound_continuation"], "pair": w["pair"], "ops": w["ops"],
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
        "scoped_out_of_envelope": f"{scoped['scoped_rejected_by_all']}/{scoped['scoped_rows']}",
        "kernel": [w["witness_id"] for w in kernel],
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
