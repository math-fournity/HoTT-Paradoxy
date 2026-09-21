#!/usr/bin/env python3
"""Verify P19's registered native Cubical interface control."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
R=OUT/'P19-ORIGIN-DIRECTED-DIAGRAM-KERNELIZATION-REPORT.md';RUN=ROOT/'HoTT/verification/runs/20260921-MP-ASTRA-ORIGIN-DIRECTED-DIAGRAM-001-03/RUN.json';M=ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md';C=ROOT/'HoTT/verification/PROOF_VERSION_CLOSURE.json'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 t=R.read_text();run=json.loads(RUN.read_text());reg=json.loads(C.read_text());need=['MINIMAL_ORIGIN_STRUCTURE_EXPRESSIBLE_WITH_SCOPE','ACTUAL_C320_CROSS_BACKEND_BINDING_NOT_ESTABLISHED','P20_CROSS_BACKEND_ORIGIN_INTERFACE_FIDELITY_NEXT','NO_NEW_HOTT_DEFECT_CLAIM'];miss=[x for x in need if x not in t];pkg=next((x for x in reg['later_packages'] if x['proof_id']=='MP-ASTRA-ORIGIN-DIRECTED-DIAGRAM-001'),None);ok=run['status']=='KERNEL_ACCEPTED_WITH_SCOPE' and run['index_status']=='INDEXED_IN_CLAIM_EVIDENCE_MATRIX' and pkg is not None and '| C-325 |' in M.read_text();d={'schema_version':'p19-origin-directed-diagram-kernelization-verification/v1','task_id':'P19-ORIGIN-DIRECTED-DIAGRAM-KERNELIZATION-001','status':'PASS_WITH_SCOPE' if not miss and ok else 'FAIL','verdict':'MINIMAL_ORIGIN_STRUCTURE_EXPRESSIBLE_WITH_SCOPE / BARE_FORGETFUL_NEGATIVE_CONTROL / FULL_TRANSPORT_POSITIVE_CONTROL / ACTUAL_C320_CROSS_BACKEND_BINDING_NOT_ESTABLISHED / P20_CROSS_BACKEND_ORIGIN_INTERFACE_FIDELITY_NEXT / NO_NEW_HOTT_DEFECT_CLAIM','sources':{str(R.relative_to(ROOT)):h(R),str(RUN.relative_to(ROOT)):h(RUN),str(M.relative_to(ROOT)):h(M),str(C.relative_to(ROOT)):h(C)},'missing_required_tokens':miss,'registered_run_ok':ok};(OUT/'P19-ORIGIN-DIRECTED-DIAGRAM-KERNELIZATION-VERIFICATION.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps(d,ensure_ascii=False,indent=2));raise SystemExit(0 if d['status']=='PASS_WITH_SCOPE' else 1)
if __name__=='__main__':main()
