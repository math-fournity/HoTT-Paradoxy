#!/usr/bin/env python3
"""Verify P17's bounded Cauchy-reals source audit."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=Path(__file__).resolve().parent
REPORT=OUT/'P17-CUBICAL-HOTT-CAUCHY-REALS-CORPUS-REPORT.md'; FREEZE=OUT/'P17-CUBICAL-HOTT-CAUCHY-REALS-SOURCE-FREEZE.json'; RECEIPT=OUT/'P17-CUBICAL-HOTT-CAUCHY-REALS-CORPUS-VERIFICATION.json'; P16=ROOT/'audit/p16-fourth-successor-discovery-20260921/P16-CUBICAL-CAUCHY-REALS-CANDIDATE-FREEZE.json'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();r=REPORT.read_text();f=json.loads(FREEZE.read_text()); old=json.loads(P16.read_text())
 needed=['NOT_A_P13_CONSUMER_WITHIN_FIXED_P17_SOURCES','DEFENSE_EXPLICIT_APPROXIMATION_RELATION_HII_DATA','TASK_DIFFERENT_FROM_P13_MN_DONE','P18_FIFTH_SUCCESSOR_DISCOVERY_NEXT','K-input','K-output','K-claim','K-forgetting','K-version','IsCauchy','NO_NEW_HOTT_DEFECT_CLAIM']; missing=[x for x in needed if x not in r]
 ident=f['candidate_id']==old['candidate_id'] and f['version']['arxiv']=='2604.24782v1' and len(f['sources']['repository_commit'])==40
 result={'schema_version':'p17-cubical-hott-cauchy-reals-corpus-verification/v1','task_id':'P17-CUBICAL-HOTT-CAUCHY-REALS-CORPUS-001','status':'PASS_WITH_SCOPE' if not missing and ident else 'FAIL','verdict':'NOT_A_P13_CONSUMER_WITHIN_FIXED_P17_SOURCES / DEFENSE_EXPLICIT_APPROXIMATION_RELATION_HII_DATA / TASK_DIFFERENT_FROM_P13_MN_DONE / P18_FIFTH_SUCCESSOR_DISCOVERY_NEXT / NO_NEW_HOTT_DEFECT_CLAIM','scope':'Checks fixed P17 report and source identity. It does not fetch, clone, compile, replay a kernel, prove global absence, or establish a HoTT theorem.','sources':{str(REPORT.relative_to(ROOT)):sha(REPORT),str(FREEZE.relative_to(ROOT)):sha(FREEZE),str(P16.relative_to(ROOT)):sha(P16)},'missing_required_tokens':missing,'source_identity_ok':ident}
 if a.write: RECEIPT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(0 if result['status']=='PASS_WITH_SCOPE' else 1)
if __name__=='__main__':main()
