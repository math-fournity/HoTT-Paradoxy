#!/usr/bin/env python3
"""Verify P22's guarded-to-bare source audit."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent;R=O/'P22-GUARDED-CUBICAL-TRANSLATION-AUDIT-REPORT.md';G=ROOT/'HoTT/formal/partiality-race-timeout/GuardErasure.agda';M=ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 t=R.read_text();need=['NO_EXPLICIT_GCTT_TO_BARE_HOTT_FORGETFUL_ROUTE_WITHIN_FIXED_SOURCE','DEFENSE_GUARD_AND_LATER_EXPLICIT','PARK_PENDING_CONCRETE_STANDARD_TRANSLATION_TARGET','NO_NEW_HOTT_DEFECT_CLAIM'];miss=[x for x in need if x not in t];ok=all(x in G.read_text()for x in('collapse-forces-fixed-point','no-fixed-point-of-not','collapse-exists-if-fixed-point')) and '| C-92 |' in M.read_text();d={'schema_version':'p22-guarded-cubical-translation-audit-verification/v1','task_id':'P22-GUARDED-CUBICAL-TO-BARE-HOTT-TRANSLATION-AUDIT-001','status':'PASS_WITH_SCOPE' if not miss and ok else 'FAIL','verdict':'NO_EXPLICIT_GCTT_TO_BARE_HOTT_FORGETFUL_ROUTE_WITHIN_FIXED_SOURCE / DEFENSE_GUARD_AND_LATER_EXPLICIT / PARK_PENDING_CONCRETE_STANDARD_TRANSLATION_TARGET / NO_NEW_HOTT_DEFECT_CLAIM','sources':{str(R.relative_to(ROOT)):h(R),str(G.relative_to(ROOT)):h(G),str(M.relative_to(ROOT)):h(M)},'missing_required_tokens':miss,'local_guard_control_ok':ok};(O/'P22-GUARDED-CUBICAL-TRANSLATION-AUDIT-VERIFICATION.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps(d,ensure_ascii=False,indent=2));raise SystemExit(0 if d['status']=='PASS_WITH_SCOPE' else 1)
if __name__=='__main__':main()
