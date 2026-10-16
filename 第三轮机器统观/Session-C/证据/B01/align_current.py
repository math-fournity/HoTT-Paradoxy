#!/usr/bin/env python3
"""Prepare one same-unit source-owner consistency transaction, not apply it."""
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'.codex/tools'));sys.path.insert(0,str(ROOT/'scripts/audit'))
import cognition_runtime as cr
import projection_edit as pe
SID='S-RES-20260924-MO3-C-B01-ALIGN';PREV='S-RES-20260924-MO3-C-B01'
def main():
 s=json.loads((ROOT/cr.STATE).read_text());assert s['revision']==287 and s['latest_session']==PREV and SID not in s['records']
 tx=json.loads((ROOT/f'.codex/cognition/checkpoints/{PREV}/transaction.json').read_text())
 assert all(cr.sha((ROOT/r['path']).read_bytes())==r['new_sha256'] for r in tx['rows'])
 p=cr.plan(ROOT,profile='research',task_ids=['MO3-COVERAGE-C']);rows=[]
 for rel in cr.MUTABLE:
  b=(ROOT/rel).read_bytes()
  if cr.parse_shard_index(b,rel):
   d=pe.load(ROOT,rel)
   if rel in (cr.DIRECTION,cr.PANORAMA):
    word='direction' if rel==cr.DIRECTION else 'outcome'
    pe.replace_in_index(d,'source_state_revision: 287','source_state_revision: 288')
    pe.replace_in_index(d,f'projection_generation: 20260924-{word}-287',f'projection_generation: 20260924-{word}-288')
   if rel=='MEMORY.md':pe.append_to_shard(d,'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：范围003的注册前待办与局部覆盖旧摘要改为当前owner路由；B01研究与下一Book2不变，revision288。\n')
   rows+=pe.payload_rows(d,ROOT)
  else:rows.append({'path':rel,'expected_sha256':cr.sha(b),'text':b.decode()})
 s['revision']=288;s['latest_session']=SID;s['execution_control']['last_checkpoint_session']=SID;s['execution_control']['checkpoint_result']=f'.codex/cognition/checkpoints/{SID}/result.json'
 for rid,word in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:s['records'][rid]['projection_generation']=f'20260924-{word}-288'
 r=s['records']['MO3-COVERAGE-C'];r['source_hashes']={f:cr.sha((ROOT/f).read_bytes()) for f in r['source_hashes']};r['revalidation']='Same B01 unit: remove stale pre-registration/current coverage duplication in scope003; source review, mathematics and next action unchanged.'
 sb=cr.PREFIX+'sessions/'+SID+'/'
 s['records'][SID]={'kind':'session','path':sb+'SESSION.md','lifecycle_status':'HISTORICAL','status':'complete_with_scope','evidence_status':'B01_OWNER_CONSISTENCY_ALIGNED','depends_on':[],'related_records':['MO3-COVERAGE-C',PREV],'full_sources':[sb+x for x in cr.SESSION_REQUIRED_FILES],'source_hashes':{},'scope':'Same B01 semantic unit source-owner consistency; no new mathematics or completion.'}
 next(x for x in rows if x['path']==cr.STATE)['text']=cr.dump(s).decode()
 for name in cr.SESSION_REQUIRED_FILES:
  t=(ROOT/cr.PREFIX/'sessions'/PREV/name).read_text().replace(PREV,SID)
  if name=='SESSION.md':t+='\n同一B01单元末审发现范围003还保有R0注册前措辞；已改用条目owner/current STATE定位，并明确本章实审/其余未审。无新理论单元、无新kernel、48KC立场及下一Book2不变。reflection=no-plan-change。\n'
  if name=='RUNS.json':
   d=json.loads(t);d['session_id']=SID;d['status']='B01_OWNER_CONSISTENCY_ONLY';t=cr.dump(d).decode()
  rows.append({'path':sb+name,'expected_sha256':None,'text':t})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['MO3-COVERAGE-C'],'authorization':'User Goal7 sole C integrator; same-unit current owner consistency only.','files':rows}
 out=ROOT/'第三轮机器统观/Session-C/证据/B01/alignment-payload.json'
 with out.open('xb') as f:f.write(cr.dump(payload))
 print(json.dumps({'snapshot':p['snapshot'],'payload':str(out.relative_to(ROOT)),'state_applied':False},ensure_ascii=False))
if __name__=='__main__':main()
