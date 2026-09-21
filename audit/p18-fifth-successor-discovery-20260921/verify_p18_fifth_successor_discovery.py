#!/usr/bin/env python3
"""Verify P18's anti-drift branch switch."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent;R=OUT/'P18-FIFTH-SUCCESSOR-DISCOVERY-REPORT.md';O=OUT/'P18-FIFTH-SUCCESSOR-DISCOVERY-VERIFICATION.json';P6=ROOT/'audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md';P7=ROOT/'audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md'
def sh(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');x=a.parse_args();t=R.read_text();need=['P3_CONTINUATION_REJECTED_AS_SAME_CLASS','SWITCH_TO_P1_OBJECT_THEORY','ORIGIN_DIRECTED_DIAGRAM_KERNELIZATION_CANDIDATE','P19_NOT_STARTED','RESTATEMENT_ONLY','NO_NEW_HOTT_DEFECT_CLAIM'];miss=[z for z in need if z not in t];ok='OriginDirectedDiagram' in P7.read_text() and 'CurvePresentation' in P6.read_text();d={'schema_version':'p18-fifth-successor-discovery-verification/v1','task_id':'P18-FIFTH-SUCCESSOR-DISCOVERY-001','status':'PASS_WITH_SCOPE' if not miss and ok else 'FAIL','verdict':'P3_CONTINUATION_REJECTED_AS_SAME_CLASS / SWITCH_TO_P1_OBJECT_THEORY / ORIGIN_DIRECTED_DIAGRAM_KERNELIZATION_CANDIDATE / P19_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM','scope':'Checks the P18 branch switch and P6/P7 local predecessor anchors. It does not formalize an object theory, prove a representation theorem, find K, or prove a HoTT defect.','sources':{str(R.relative_to(ROOT)):sh(R),str(P6.relative_to(ROOT)):sh(P6),str(P7.relative_to(ROOT)):sh(P7)},'missing_required_tokens':miss,'local_predecessors_ok':ok}
 if x.write:O.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(d,ensure_ascii=False,indent=2));raise SystemExit(0 if d['status']=='PASS_WITH_SCOPE' else 1)
if __name__=='__main__':main()
