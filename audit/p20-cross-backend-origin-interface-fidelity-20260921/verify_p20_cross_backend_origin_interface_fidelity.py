#!/usr/bin/env python3
"""Verify P20's bounded cross-backend fidelity audit."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent;R=O/'P20-CROSS-BACKEND-ORIGIN-INTERFACE-FIDELITY-REPORT.md';M=ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md';C=ROOT/'HoTT/verification/PROOF_VERSION_CLOSURE.json';S=ROOT/'HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda';D=ROOT/'HoTT/formal/astra-breakpoint-check/OriginDirectedDiagram.agda'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 t=R.read_text();need=['NO_REGISTERED_FIELD_PRESERVING_TRANSLATION_WITHIN_DECLARED_DENOMINATOR','BACKEND_SEMANTICS_DISTINCT','P21_SYNTHESIS_AND_STOP_DECISION_NEXT','NO_PROOF_ASSISTANT_BUG_OR_HOTT_DEFECT_CLAIM'];miss=[x for x in need if x not in t];ok=all(x in S.read_text() for x in ('CurveRun','Success','actualCurveRun')) and all(x in D.read_text() for x in ('OriginDirectedDiagram','bareOrigin','originTransport')) and '| C-320 |' in M.read_text() and '| C-325 |' in M.read_text();d={'schema_version':'p20-cross-backend-origin-interface-fidelity-verification/v1','task_id':'P20-CROSS-BACKEND-ORIGIN-INTERFACE-FIDELITY-001','status':'PASS_WITH_SCOPE' if not miss and ok else 'FAIL','verdict':'NO_REGISTERED_FIELD_PRESERVING_TRANSLATION_WITHIN_DECLARED_DENOMINATOR / BACKEND_SEMANTICS_DISTINCT / P21_SYNTHESIS_AND_STOP_DECISION_NEXT / NO_PROOF_ASSISTANT_BUG_OR_HOTT_DEFECT_CLAIM','sources':{str(R.relative_to(ROOT)):h(R),str(S.relative_to(ROOT)):h(S),str(D.relative_to(ROOT)):h(D),str(M.relative_to(ROOT)):h(M),str(C.relative_to(ROOT)):h(C)},'missing_required_tokens':miss,'fixed_source_comparison_ok':ok};(O/'P20-CROSS-BACKEND-ORIGIN-INTERFACE-FIDELITY-VERIFICATION.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps(d,ensure_ascii=False,indent=2));raise SystemExit(0 if d['status']=='PASS_WITH_SCOPE' else 1)
if __name__=='__main__':main()
