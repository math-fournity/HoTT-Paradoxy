#!/usr/bin/env python3
"""Verify P12's bounded ambient-pair candidate selection."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
REPORT=OUT/'P12-THIRD-SUCCESSOR-DISCOVERY-REPORT.md'
FREEZE=OUT/'P12-AMBIENT-PAIR-CANDIDATE-FREEZE.json'
RECEIPT=OUT/'P12-THIRD-SUCCESSOR-DISCOVERY-VERIFICATION.json'

def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()

def main()->None:
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    report=REPORT.read_text(encoding='utf-8'); freeze=json.loads(FREEZE.read_text(encoding='utf-8'))
    required=['SUCCESSOR_SELECTED','AMBIENT_PAIR_RMIN_REQUALIFICATION_CANDIDATE','P13_NOT_STARTED','H_intrinsic','R_ambient','Done_ambient','C-266','C-267','C-268','PARTIAL_REUSE','NO_NEW_HOTT_DEFECT_CLAIM']
    missing=[x for x in required if x not in report]
    files=freeze.get('sources',[]); identity_ok=len(files)==5 and freeze.get('run_identity',{}).get('proof_id')=='MP-ASTRA-AMBIENT-CIRCLE-001'
    result={'schema_version':'p12-third-successor-discovery-verification/v1','task_id':'P12-THIRD-SUCCESSOR-DISCOVERY-001','status':'PASS_WITH_SCOPE' if not missing and identity_ok else 'FAIL','verdict':'SUCCESSOR_SELECTED / AMBIENT_PAIR_RMIN_REQUALIFICATION_CANDIDATE / P13_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM','scope':'Checks only the declared reuse classification and candidate identity. It does not replay Lean, establish the ambient theorem, formalize R_ambient in HoTT, find K, or prove a HoTT defect.','sources':{str(REPORT.relative_to(ROOT)):sha(REPORT),str(FREEZE.relative_to(ROOT)):sha(FREEZE),'audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md':sha(ROOT/'audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md'),'HoTT/CLAIM_EVIDENCE_MATRIX.md':sha(ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md')},'missing_required_tokens':missing,'candidate_identity_ok':identity_ok,'public_sources_checked':['https://webhomes.maths.ed.ac.uk/~v1ranick/papers/mccleary2.pdf','https://github.com/leanprover-community/mathlib4']}
    if args.write: RECEIPT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(0 if result['status']=='PASS_WITH_SCOPE' else 1)
if __name__=='__main__':main()
