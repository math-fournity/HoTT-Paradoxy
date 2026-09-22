#!/usr/bin/env python3
"""Verify P33 coverage assets and preserve the no-new-theorem boundary."""
from __future__ import annotations
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
REPORT=HERE/'P33-2LTT-V5-SELF-METATHEORY-BOUNDARY-AUDIT-REPORT.md'; FREEZE=HERE/'P33-2LTT-V5-SOURCE-FREEZE.json'; OUT=HERE/'P33-2LTT-V5-SELF-METATHEORY-BOUNDARY-AUDIT-VERIFICATION.json'
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 f=json.loads(FREEZE.read_text()); missing=[x for x in ('P2_GATE_NOT_PASSED','P34','EXACT_COVERAGE','NO_NEW_HOTT_DEFECT_CLAIM') if x not in REPORT.read_text()]; bad={p:{'expected':v,'actual':h(ROOT/p)} for p,v in f['local_source_sha256'].items() if h(ROOT/p)!=v}; o={'schema_version':'p33-2ltt-v5-verification/v1','task_id':'P33-2LTT-V5-SELF-METATHEORY-BOUNDARY-AUDIT-2026-001','status':'PASS_WITH_SCOPE' if not missing and not bad else 'FAIL','verdict':f['verdict'],'report_sha256':h(REPORT),'freeze_sha256':h(FREEZE),'missing_report_tokens':missing,'local_source_hash_mismatches':bad,'scope':'Checks exact local coverage and current primary-source locator; proves no new 2LTT, HoTT, consumer, or reality-task theorem.'}; OUT.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n'); print(json.dumps(o,ensure_ascii=False,indent=2));
 if o['status']!='PASS_WITH_SCOPE': raise SystemExit(1)
if __name__=='__main__': main()
