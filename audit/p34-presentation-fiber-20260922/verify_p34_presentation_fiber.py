#!/usr/bin/env python3
"""Verify P34's exact source, kernel receipt, matrix row and registry entry."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
REPORT=HERE/'P34-PRESENTATION-FIBER-REPORT.md';FREEZE=HERE/'P34-PRESENTATION-FIBER-SOURCE-FREEZE.json';RUN=ROOT/'HoTT/verification/runs/20260922-MP-ASTRA-PRESENTATION-FIBER-001-01/RUN.json';MATRIX=ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md';REG=ROOT/'HoTT/verification/PROOF_VERSION_CLOSURE.json';OUT=HERE/'P34-PRESENTATION-FIBER-VERIFICATION.json'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 r=json.loads(RUN.read_text());g=json.loads(REG.read_text());f=json.loads(FREEZE.read_text());text=REPORT.read_text();need=['SAME_BARE_FIBER_HAS_DISTINCT_PRESENTATIONS','noOpenFiberPath','P35','NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM'];miss=[x for x in need if x not in text];bad={p:{'expected':v,'actual':h(ROOT/p)} for p,v in f['sha256'].items() if h(ROOT/p)!=v};entry=next((x for x in g['later_packages'] if x['proof_id']=='MP-ASTRA-PRESENTATION-FIBER-001'),None);ok=r['status']=='KERNEL_ACCEPTED_WITH_SCOPE' and r['exit_code']==0 and '| C-326 |' in MATRIX.read_text() and entry is not None;o={'schema_version':'p34-presentation-fiber-verification/v1','task_id':'P34-P1-ORIGIN-RELATION-DISCOVERY-001','status':'PASS_WITH_SCOPE' if not miss and not bad and ok else 'FAIL','verdict':'FORMAL_CHECKED_WITH_SCOPE / SAME_BARE_FIBER_HAS_DISTINCT_PRESENTATIONS / ENDPOINT_CLOSURE_SEPARATES_PRESENTATIONS / P35_FIBERWISE_TRACE_SPEC_SELECTED / NO_HOTT_DEFECT_OR_ACTUAL_K_CLAIM','report_sha256':h(REPORT),'freeze_sha256':h(FREEZE),'run_sha256':h(RUN),'matrix_sha256':h(MATRIX),'registry_sha256':h(REG),'missing_report_tokens':miss,'source_hash_mismatches':bad,'registered_run_ok':ok,'scope':'Checks the local P1 fiber theorem only; no HoTT defect, K consumer, full origin theory or reality bridge is proved.'};OUT.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n');print(json.dumps(o,ensure_ascii=False,indent=2));raise SystemExit(0 if o['status']=='PASS_WITH_SCOPE' else 1)
if __name__=='__main__':main()
