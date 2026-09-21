#!/usr/bin/env python3
"""Verify P28's fixed CFTT source audit."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
REPORT=OUT/'P28-CFTT-STAGED-QUOTATION-SPLICE-UNSTAGING-CORPUS-REPORT.md'
FREEZE=OUT/'P28-CFTT-SOURCE-FREEZE.json'
RESULT=OUT/'P28-CFTT-STAGED-QUOTATION-SPLICE-UNSTAGING-CORPUS-VERIFICATION.json'
EXTERNAL=Path('/tmp/staged-p28-9c4e2017')
def h(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 f=json.loads(FREEZE.read_text());t=REPORT.read_text();need=['ACTUAL_STAGED_QUOTATION_SPLICE_UNSTAGING_CONTRACT_SOURCE_REVIEWED','AGDA_SUPPLEMENT_OBJECT_THEORY_POSTULATED_HOAS','GENERATIVITY_AXIOM_TRUSTME_BOUNDARY','NOT_OBJECT_PROVABILITY_OR_HOTT_SELF_VALIDATION','P29-CLIMBER-OBJECT-PROVABILITY-SOUNDNESS-CORPUS-001','NO_NEW_HOTT_DEFECT_CLAIM'];missing=[x for x in need if x not in t]
 mismatch=[]
 for rel,expected in f['external_files_sha256'].items():
  actual=h(EXTERNAL/rel) if (EXTERNAL/rel).is_file() else None
  if actual!=expected:mismatch.append({'path':rel,'expected':expected,'actual':actual})
 anchors={}
 if not mismatch:
  readme=(EXTERNAL/'icfp24paper/supplement/agda-cftt/README.agda').read_text();obj=(EXTERNAL/'icfp24paper/supplement/agda-cftt/Object.agda').read_text();sop=(EXTERNAL/'icfp24paper/supplement/agda-cftt/SOP.agda').read_text();paper=(EXTERNAL/'icfp24paper/paper.tex').read_text()
  anchors={'hoas_statement':'postulated in a HOAS' in readme,'object_postulate':'postulate' in obj and 'Ty  : Set' in obj,'generativity_trustme':'generative f x y = primTrustMe' in sop,'paper_unstaging':'Unstaging is defined as evaluation' in paper,'paper_agda_postulated':'object theory is embedded as a collection of postulated' in paper}
 pin=f['remote']['commit']=='9c4e2017669086e2f77df5014f1c215a5a7e07a3' and f['p29_candidate']['remote_head_observed']=='6994d29dda860c3a82de207b1f39ea89526f61c9'
 status='PASS_WITH_SCOPE' if not missing and not mismatch and all(anchors.values()) and pin else 'FAIL'
 out={'schema_version':'p28-cftt-staged-verification/v1','task_id':f['task_id'],'status':status,'verdict':f['verdict'],'report_sha256':h(REPORT),'freeze_sha256':h(FREEZE),'missing_report_tokens':missing,'external_source_hash_mismatches':mismatch,'source_anchors':anchors,'pins_ok':pin,'scope':'Checks fixed-source identity and P28 source-level boundaries. It does not run CFTT, prove a HoTT theorem or establish a defect.'}
 RESULT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2));raise SystemExit(0 if status=='PASS_WITH_SCOPE' else 1)
if __name__=='__main__':main()
