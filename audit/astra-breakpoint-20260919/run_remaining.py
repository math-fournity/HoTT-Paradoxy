#!/usr/bin/env python3
"""Sequentially capture the bounded native type-theory checks. No success inference from exit alone."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = "HoTT/formal/astra-breakpoint-check/"
TOOLCHAIN = "HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json"
CASES = [
    ("COMPUTATION", "ClosedComputation", "257", [], "Closed ua computation and an explicit witness for the opaque contract", 0),
    ("HOLDOUT", "UpstreamLoopHoldout", "258", [], "Library integer winding distinguishes two loops; source holdout, not blind replication", 0),
    ("NEG-BRIDGE", "MissingBridge", "250", [], "Missing middle endpoint in composition: type rejection control", 42),
    ("NEG-OVERLAP", "OverlapMismatch", "254", [], "Incompatible overlap in Partial: type rejection control", 42),
    ("NEG-FACE", "MissingFace", "254", [], "Partial consumer without full face: type rejection control", 42),
    ("NEG-GLUE", "GlueMismatch", "254", [], "Glue base mismatches image under equivalence: type rejection control", 42),
    ("NEG-HIT", "HITMismatch", "254", ["LocalCoherence"], "HIT eliminator fails specified path boundary: type rejection control", 42),
    ("NEG-TRUNC", "TruncRecover", "253", [], "Original Boolean recovery fails propositional truncation coherence", 42),
    ("NEG-QUOT", "QuotRecover", "253", [], "Original representative recovery fails quotient compatibility", 42),
    ("NEG-MIXED", "MixedRecovery", "253", [], "Adding ua transport does not establish universal quotient compatibility", 42),
    ("OPAQUE", "OpaquePath", "257", [], "Explicit postulated path and beta certificate; non-safe axiomatic control", 0),
    ("NEG-OPAQUE-REFL", "OpaqueRefl", "257", ["OpaquePath"], "Postulated beta certificate does not make transport judgmentally reduce in this sample", 42),
]

def main():
    rows = []
    for key, module, claim, imports, scope, expected in CASES:
        run_id = "20260919-MP-ASTRA-" + key + "-01"
        run_dir = ROOT / "HoTT/verification/runs" / run_id
        if run_dir.exists():
            raise SystemExit("EXISTING_RUN_STOP:" + run_id)
        cmd = ["python3", "scripts/audit/capture_agda_proof_run.py", "--run-id", run_id,
               "--proof-id", "MP-ASTRA-" + key + "-001", "--claim-id", "C-" + claim,
               "--source", BASE + module + ".agda", "--toolchain", TOOLCHAIN,
               "--scope", scope, "--non-goal", "No global HoTT inconsistency, completeness, or physical restoration claim"]
        for name in imports:
            cmd += ["--manifest-file", BASE + name + ".agda"]
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        receipt = json.loads((run_dir / "RUN.json").read_text()) if (run_dir / "RUN.json").exists() else {}
        row = {"run_id": run_id, "module": module, "expected_exit": expected,
               "exit_code": receipt.get("exit_code"), "capture_exit": result.returncode,
               "capture_stdout": result.stdout, "capture_stderr": result.stderr,
               "diagnostic_review": "PENDING_DIRECT_REVIEW"}
        rows.append(row)
        print(json.dumps(row, ensure_ascii=False), flush=True)
        if receipt.get("exit_code") not in (0, 42):
            raise SystemExit("UNEXPECTED_CAPTURE_FAILURE")
    (ROOT / "audit/astra-breakpoint-20260919/remaining-runs.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n")

if __name__ == "__main__":
    main()
