#!/usr/bin/env python3
"""Verify P16's bounded real-layer actual-formalisation selection."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
REPORT = OUT / 'P16-FOURTH-SUCCESSOR-DISCOVERY-REPORT.md'
FREEZE = OUT / 'P16-CUBICAL-CAUCHY-REALS-CANDIDATE-FREEZE.json'
RECEIPT = OUT / 'P16-FOURTH-SUCCESSOR-DISCOVERY-VERIFICATION.json'
LOCAL = ROOT / 'audit/literature/LIT-DENOMINATOR-001/discovery-20260914/DISCOVERY-CANDIDATES.json'
def sha(p: Path) -> str: return hashlib.sha256(p.read_bytes()).hexdigest()
def main() -> None:
    a=argparse.ArgumentParser(); a.add_argument('--write',action='store_true'); args=a.parse_args()
    report=REPORT.read_text(encoding='utf-8'); freeze=json.loads(FREEZE.read_text(encoding='utf-8') )
    needed=['SUCCESSOR_SELECTED','CUBICAL_HOTT_CAUCHY_REALS_ACTUAL_FORMALISATION_CANDIDATE','P17_NOT_STARTED','P17-CUBICAL-HOTT-CAUCHY-REALS-CORPUS-001','K-input','K-output','K-claim','K-forgetting','K-version','NO_NEW_HOTT_DEFECT_CLAIM']
    missing=[x for x in needed if x not in report]
    identity=freeze['candidate_id']=='P17-CUBICAL-HOTT-CAUCHY-REALS-CORPUS-001' and freeze['published_source']['arxiv_url']=='https://arxiv.org/abs/2604.24782' and freeze['published_source']['arxiv_version']=='v1'
    local_ok='Formalizing the Real Numbers in Homotopy Type Theory with Cubical Agda' in LOCAL.read_text(encoding='utf-8')
    result={'schema_version':'p16-fourth-successor-discovery-verification/v1','task_id':'P16-FOURTH-SUCCESSOR-DISCOVERY-001','status':'PASS_WITH_SCOPE' if not missing and identity and local_ok else 'FAIL','verdict':'SUCCESSOR_SELECTED / CUBICAL_HOTT_CAUCHY_REALS_ACTUAL_FORMALISATION_CANDIDATE / P17_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM','scope':'Checks P16 source identity, prior local unreviewed status, and P17 card fields. It does not read full paper/code, replay Agda, find K, or prove a HoTT defect.','sources':{str(REPORT.relative_to(ROOT)):sha(REPORT),str(FREEZE.relative_to(ROOT)):sha(FREEZE),str(LOCAL.relative_to(ROOT)):sha(LOCAL)},'missing_required_tokens':missing,'source_identity_ok':identity,'local_predecessor_ok':local_ok}
    if args.write: RECEIPT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2)); raise SystemExit(0 if result['status']=='PASS_WITH_SCOPE' else 1)
if __name__=='__main__': main()
