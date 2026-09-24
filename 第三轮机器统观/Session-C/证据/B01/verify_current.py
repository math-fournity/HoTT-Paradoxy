#!/usr/bin/env python3
"""Record actual B01 transaction/structure checks without changing owners."""
from pathlib import Path
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'.codex/tools'))
import cognition_runtime as cr
SID='S-RES-20260924-MO3-C-B01-ALIGN'
def main():
 cp=ROOT/f'.codex/cognition/checkpoints/{SID}'
 result=json.loads((cp/'result.json').read_text());tx=json.loads((cp/'transaction.json').read_text())
 assert result['status']=='CHECKPOINT_COMMITTED'
 mismatches=[r['path'] for r in tx['rows'] if cr.sha((ROOT/r['path']).read_bytes())!=r['new_sha256']]
 s=json.loads((ROOT/cr.STATE).read_text());assert s['revision']==288 and s['latest_session']==SID
 q=cr.query(ROOT,'MO3-COVERAGE-C') if hasattr(cr,'query') else None
 p=cr.plan(ROOT,profile='research',task_ids=['MO3-COVERAGE-C'])
 checks=[]
 for cmd in [['python3','-B','scripts/audit/verify_three_way_cognition.py'],['python3','-B','scripts/audit/verify_governance_shards.py']]:
  r=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True)
  checks.append({'argv':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 data={'status':'POST_CHECKPOINT_MATCH' if not mismatches else 'MISMATCH','canonical_result':str((cp/'result.json').relative_to(ROOT)),'canonical_result_sha256':cr.sha((cp/'result.json').read_bytes()),'revision':s['revision'],'after_paths':len(tx['rows']),'after_mismatches':mismatches,'plan_snapshot':p['snapshot'],'review_required':p['review_required'],'query_first_promoted':p['hydration_diagnostics']['query_first_promoted'],'core_sha256':cr.sha((ROOT/'核心认知.md').read_bytes()),'checks':checks,'parent_coverage':'PARENT_SCOPE_INCOMPLETE','kernel_replayed':False}
 out=ROOT/'第三轮机器统观/Session-C/证据/B01/POST-288.json'
 with out.open('xb') as f:f.write(cr.dump(data))
 print(json.dumps({k:v for k,v in data.items() if k!='checks'},ensure_ascii=False))
 for c in checks:
  try:
   d=json.loads(c['stdout']);summary={k:d[k] for k in ['status','index_count','errors','reader_banner_issues','direction_count','outcome_count'] if k in d}
  except json.JSONDecodeError:summary=c['stdout'][-1500:]
  print(json.dumps({'command':c['argv'][-1],'exit_code':c['exit_code'],'summary':summary},ensure_ascii=False))
 assert not mismatches and not p['review_required'] and not p['hydration_diagnostics']['query_first_promoted']
 assert all(c['exit_code']==0 for c in checks)
if __name__=='__main__':main()
