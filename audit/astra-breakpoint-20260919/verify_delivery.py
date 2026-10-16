#!/usr/bin/env python3
"""Verify this exact proof family with the existing canonical validators.

The global Git/version validator is also run and its failure remains visible.
Scoped relationship checking is explicitly not a substitute for its global PASS.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts/audit"))
import verify_formal_proof_run as F
import verify_proof_version_closure as V

def main():
    catalogue = json.loads((OUT / "claim-catalogue.json").read_text())["claims"]
    registry = V.load(ROOT / "HoTT/verification/PROOF_VERSION_CLOSURE.json")
    wanted = {c["proof_id"] for c in catalogue}
    all_rows = registry["packages"] + registry["later_packages"]
    selected = [x for x in all_rows if x["proof_id"] in wanted]
    assert len(selected) == len(wanted)
    packages = V.package_map({"packages": [], "later_packages": selected})
    try:
        V.package_map(registry)
        global_registry_error = None
    except V.ClosureError as exc:
        global_registry_error = str(exc)
    matrix = V.matrix_identity_lines((ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md").read_bytes())
    gaps = V.load_gap_allowlist(registry)
    results = []
    for c in catalogue:
        for script in ("mark_proof_run_indexed.py", "freeze_proof_index_rows.py"):
            if script.startswith("freeze") and (ROOT / c["run"] / "index-row-manifest.json").exists():
                continue
            r = subprocess.run(["python3", "scripts/audit/" + script, "--run-dir", c["run"]], cwd=ROOT, capture_output=True, text=True)
            if r.returncode:
                raise RuntimeError(r.stdout + r.stderr)
        formal = F.validate(ROOT, Path(c["run"]), rerun=False)
        try:
            relation = V.check_later_package(ROOT / c["run"], packages[c["proof_id"]], gaps, matrix)
            relation = {k:sorted(v) if isinstance(v,set) else v for k,v in relation.items()}
        except V.ClosureError as exc:
            relation = {"status":"BLOCKED", "error":str(exc)}
        results.append({"claim": c["claim_id"], "formal": formal, "canonical_package_relation": relation})
    negatives = []
    for run in sorted((ROOT / "HoTT/verification/runs").glob("20260919-MP-ASTRA-NEG-*-01")):
        receipt = json.loads((run / "RUN.json").read_text())
        stdout = (run / "stdout.txt").read_bytes()
        assert receipt["exit_code"] == 42 and b"error: [UnequalTerms]" in stdout
        assert hashlib.sha256(stdout).hexdigest() == receipt["stdout"]["sha256"]
        negatives.append({"run":run.name, "status":"EXPECTED_TYPE_REJECTION_DIAGNOSTIC_CHECKED",
                          "diagnostic":stdout.decode().split("error: [UnequalTerms]",1)[1].strip()})
    global_check = subprocess.run(["python3", "scripts/audit/verify_proof_version_closure.py"], cwd=ROOT, capture_output=True, text=True)
    global_result = {"exit_code": global_check.returncode, "stdout": global_check.stdout, "stderr":global_check.stderr}
    (OUT / "global-version-closure.json").write_text(json.dumps(global_result, ensure_ascii=False, indent=2) + "\n")
    result = {"schema":"astra-delivery-check/v1", "scope":"Eleven newly indexed local packages; no global certification",
              "status":"FORMAL_RUN_VALIDATION_PASS_PACKAGE_AND_GLOBAL_GATE_PARTIAL", "packages":results,
              "negative_controls":negatives,"global_version_closure":global_result,
              "global_registry_error":global_registry_error,
              "git":"LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED"}
    (OUT / "delivery-verification.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"new_packages":len(results),"negative_controls":len(negatives),"global":global_result}, ensure_ascii=False))

if __name__ == "__main__":
    main()
