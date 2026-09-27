#!/usr/bin/env python3
"""Verify every Cloud-Opus run (2026-09-27) and write 11-收据核验结果.json.

For each HoTT/verification/runs/20260927-COPUS-* directory, calls
verify_copus_run.validate(run, rerun=<flag>, expect_rejected=<RUN.expected_outcome == REJECT>)
and records the result or the failure.  With --rerun every command_argv is executed
again and exit code, stdout and stderr must be byte-identical to the receipt.

Usage:
  python3 -B Cloud-Opus审计并补完GLM/tools/verify_all_runs.py [--rerun] [--out <path>]
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNS = Path("HoTT/verification/runs")
DEFAULT_OUT = ROOT / "Cloud-Opus审计并补完GLM/11-收据核验结果.json"


def load_single():
    path = Path(__file__).resolve().parent / "verify_copus_run.py"
    spec = importlib.util.spec_from_file_location("verify_copus_run", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module, path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rerun", action="store_true")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    a = ap.parse_args()
    single, single_path = load_single()
    rows = []
    started = dt.datetime.now(dt.timezone.utc)
    for run_dir in sorted((ROOT / RUNS).glob("20260927-COPUS-*")):
        relative = run_dir.relative_to(ROOT)
        expected = json.loads((run_dir / "RUN.json").read_text(encoding="utf-8")).get("expected_outcome")
        t0 = time.monotonic()
        try:
            result = single.validate(relative, a.rerun, expected == "REJECT")
        except Exception as exc:  # recorded, never hidden
            result = {"status": "FAIL", "run_id": run_dir.name, "error": f"{type(exc).__name__}: {exc}"}
        result["expected_outcome"] = expected
        result["verify_seconds"] = round(time.monotonic() - t0, 3)
        rows.append(result)
        print(f"{run_dir.name}\t{result['status']}\t{result.get('replay', '-')}", flush=True)
    ok = {"PASS_WITH_SCOPE", "NEGATIVE_CONTROL_REJECTED_AS_EXPECTED"}
    summary = {
        "schema_version": "copus-run-verification/v1",
        "generated_at_utc": started.isoformat(timespec="seconds"),
        "completed_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "verifier": "Cloud-Opus审计并补完GLM/tools/verify_copus_run.py",
        "verifier_sha256": single.load_canonical().sha(single_path.read_bytes()),
        "rerun": a.rerun,
        "run_count": len(rows),
        "pass_count": sum(1 for r in rows if r["status"] == "PASS_WITH_SCOPE"),
        "negative_rejected_count": sum(1 for r in rows if r["status"] == "NEGATIVE_CONTROL_REJECTED_AS_EXPECTED"),
        "fail_count": sum(1 for r in rows if r["status"] not in ok),
        "exact_replay_count": sum(1 for r in rows if r.get("replay") == "EXACT_EXIT_STDOUT_STDERR_MATCH"),
        "index_meaning": "GOAL_LOCAL_INDEX_PLUS_MATRIX_PRESENCE: one row per identity in 证据索引.md and presence in HoTT/CLAIM_EVIDENCE_MATRIX.md; not the canonical INDEXED_IN_CLAIM_EVIDENCE_MATRIX / PROOF_VERSION_CLOSURE status (integrator-owned).",
        "runs": rows,
    }
    Path(a.out).write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: summary[k] for k in ("run_count", "pass_count", "negative_rejected_count", "fail_count", "exact_replay_count")}))
    return 0 if summary["fail_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
