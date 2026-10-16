#!/usr/bin/env python3
"""Index and validate the three new restoration packages without hiding global failures."""
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/"scripts/audit"))
import verify_formal_proof_run as F
import verify_proof_version_closure as V

def main():
    rows=json.loads((OUT/"restoration-claim-catalogue.json").read_text())["packages"]
    registry=V.load(ROOT/"HoTT/verification/PROOF_VERSION_CLOSURE.json")
    index=V.matrix_identity_lines((ROOT/"HoTT/CLAIM_EVIDENCE_MATRIX.md").read_bytes())
    ids={r["proof_id"] for r in rows}
    selected=[r for r in registry["later_packages"] if r["proof_id"] in ids]
    assert len(selected)==len(ids)
    packages=V.package_map({"packages":[],"later_packages":selected})
    gaps=V.load_gap_allowlist(registry);results=[]
    for row in rows:
        run=ROOT/row["run"]
        for script in ["mark_proof_run_indexed.py","freeze_proof_index_rows.py"]:
            if script.startswith("freeze") and (run/"index-row-manifest.json").exists():continue
            r=subprocess.run(["python3","scripts/audit/"+script,"--run-dir",row["run"]],cwd=ROOT,capture_output=True,text=True)
            assert r.returncode==0,r.stdout+r.stderr
        formal=F.validate(ROOT,Path(row["run"]),False)
        try:
            relation=V.check_later_package(run,packages[row["proof_id"]],gaps,index)
            relation={k:sorted(v) if isinstance(v,set) else v for k,v in relation.items()}
        except V.ClosureError as e:
            relation={"status":"BLOCKED","error":str(e)}
        results.append({"proof_id":row["proof_id"],"formal_run_check":formal,"package_relation":relation})
    global_check=subprocess.run(["python3","scripts/audit/verify_proof_version_closure.py"],cwd=ROOT,capture_output=True,text=True)
    cli=ROOT/"HoTT/verification/runs/20260919-ASTRA-CLI-RESTORATION-01/RUN.json"
    qualification=json.loads(cli.read_text());assert qualification["exit_code"]==0
    assert "--safe" in qualification["command_argv"] and "--cubical" in qualification["command_argv"]
    d={"schema":"astra-restoration-verification/v1","status":"FORMAL_RUN_CHECKS_PASS_GLOBAL_GATE_PARTIAL","packages":results,"cli_qualification":str(cli.relative_to(ROOT)),"global_checker":{"exit_code":global_check.returncode,"stdout":global_check.stdout,"stderr":global_check.stderr},"math_delivery":"NOT_PROMOTED_WHILE_CANONICAL_PACKAGE_OR_GLOBAL_GATE_FAILS","geometry":"ALGEBRAIC_POINT_SET_ONLY; TOPOLOGY_AND_ALLOWED_PROCESS_OPEN"}
    (OUT/"restoration-delivery-verification.json").write_text(json.dumps(d,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"new_packages":len(results),"new_claims":sum(len(V.expand_claim_ids(r["claim_ids"])) for r in rows),"formal_pass":all(x["formal_run_check"]["status"]=="PASS_WITH_SCOPE" for x in results),"global_exit":global_check.returncode},ensure_ascii=False))

if __name__=="__main__":main()
