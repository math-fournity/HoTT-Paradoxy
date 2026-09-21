#!/usr/bin/env python3
"""Verify P23's ERCF-3 independent-ingress selection."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent;R=O/'P23-INDEPENDENT-INGRESS-DISCOVERY-REPORT.md';S=[ROOT/'HoTT/formal/ercf3-t3/ObjectSyntax.agda',ROOT/'HoTT/formal/ercf3-t3/ProvRepresentability.agda',ROOT/'HoTT/formal/ercf3-t3/DiagonalCore.agda',ROOT/'HoTT/formal/ercf3-t3/RepairedSyntax.agda',ROOT/'理解章节/C4-HoTT自反真理验证回环与理论经济学-20260912.md']
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 t=R.read_text();need=['SUCCESSOR_SELECTED','ERCF3_PROOF_PREDICATE_REPRESENTABILITY_AND_NATURAL_CONSUMER_CANDIDATE','P24_NOT_STARTED','NOT_RERUN_WITH_REASON','NO_NEW_HOTT_DEFECT_CLAIM'];miss=[x for x in need if x not in t];ok=all(p.is_file() for p in S) and 'Prov :' in S[0].read_text();d={'schema_version':'p23-independent-ingress-discovery-verification/v1','task_id':'P23-INDEPENDENT-INGRESS-DISCOVERY-001','status':'PASS_WITH_SCOPE' if not miss and ok else 'FAIL','verdict':'SUCCESSOR_SELECTED / ERCF3_PROOF_PREDICATE_REPRESENTABILITY_AND_NATURAL_CONSUMER_CANDIDATE / P24_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM','sources':{str(R.relative_to(ROOT)):h(R),**{str(p.relative_to(ROOT)):h(p) for p in S}},'missing_required_tokens':miss,'local_ercf3_anchors_ok':ok};(O/'P23-INDEPENDENT-INGRESS-DISCOVERY-VERIFICATION.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps(d,ensure_ascii=False,indent=2));raise SystemExit(0 if d['status']=='PASS_WITH_SCOPE' else 1)
if __name__=='__main__':main()
