#!/usr/bin/env python3
"""Verify P29's fixed-source and external run evidence."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent;REPORT=OUT/'P29-CLIMBER-OBJECT-PROVABILITY-SOUNDNESS-CORPUS-REPORT.md';FREEZE=OUT/'P29-CLIMBER-SOURCE-FREEZE.json';RUN=OUT/'runs/20260921-P29-CLIMBER-BUILD-SMOKE-01/RUN.json';RESULT=OUT/'P29-CLIMBER-OBJECT-PROVABILITY-SOUNDNESS-CORPUS-VERIFICATION.json';EXT=Path('/tmp/climber-p29-6994d29d')
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 f=json.loads(FREEZE.read_text());t=REPORT.read_text();need=['OBJECT_PROVABILITY_AND_ONE_RUNG_REFLECTION_CONFIRMED','METALANGUAGE_SOUNDNESS_AND_LEVEL_STRATIFICATION_EXPLICIT','NOT_HOTT_AND_NOT_SAME_THEORY_GLOBAL_SELF_VALIDATION','P30_HOTT_REFLECTION_OBLIGATION_CROSSWALK_SELECTED','NO_NEW_HOTT_DEFECT_CLAIM'];missing=[x for x in need if x not in t];mis=[]
 for rel,exp in f['external_files_sha256'].items():
  actual=h(EXT/rel) if (EXT/rel).is_file() else None
  if actual!=exp:mis.append({'path':rel,'expected':exp,'actual':actual})
 anchors={}
 if not mis:
  obj=(EXT/'Climber/Object.lean').read_text();climb=(EXT/'Climber/Climb.lean').read_text();refl=(EXT/'Climber/Reflection.lean').read_text()
  anchors={'object_prov':'| prov (φ : Formula)' in obj,'prov_interpreted_in_lean':'| .prov φ  => Derivable₀ φ' in obj,'sound_extension':'sound  : ∀ (φ : Formula)' in climb,'climb_sound':'theorem climb_sound' in climb,'rfn_schema':'def rfn0Schema' in refl,'rung_con':'theorem T₁_rfn_derives_con' in refl,'base_noncon':'theorem con_not_derivable_in_T₀' in refl}
 run=json.loads(RUN.read_text());runok=run.get('external_commit')=='6994d29dda860c3a82de207b1f39ea89526f61c9' and run.get('status')=='BUILD_AND_SMOKE_ACCEPTED_WITH_SCOPE' and run.get('build',{}).get('exit_code')==0 and run.get('smoke',{}).get('exit_code')==0
 status='PASS_WITH_SCOPE' if not missing and not mis and all(anchors.values()) and runok else 'FAIL';out={'schema_version':'p29-climber-verification/v1','task_id':f['task_id'],'status':status,'verdict':f['verdict'],'report_sha256':h(REPORT),'freeze_sha256':h(FREEZE),'missing_report_tokens':missing,'external_source_hash_mismatches':mis,'source_anchors':anchors,'run_ok':runok,'scope':'Checks P29 fixed source and saved external build/smoke. It does not prove a HoTT result or universal reflection theorem.'};RESULT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2));raise SystemExit(0 if status=='PASS_WITH_SCOPE' else 1)
if __name__=='__main__':main()
