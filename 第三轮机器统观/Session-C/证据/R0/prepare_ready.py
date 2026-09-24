#!/usr/bin/env python3
"""Finalize R0 document freshness through the canonical writer only."""
from pathlib import Path
import json,sys,hashlib
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'.codex/tools'));sys.path.insert(0,str(ROOT/'scripts/audit'))
import cognition_runtime as cr
import projection_edit as pe
SID='S-RES-20260924-MO3-C-R0-READY';PREV='S-RES-20260924-MO3-C-R0-ALIGN'
def main():
 s=json.loads((ROOT/cr.STATE).read_text());assert s['revision']==285 and s['latest_session']==PREV
 cp=ROOT/f'.codex/cognition/checkpoints/{PREV}'
 t=json.loads((cp/'transaction.json').read_text())
 assert all(cr.sha((ROOT/r['path']).read_bytes())==r['new_sha256'] for r in t['rows'])
 p=cr.plan(ROOT,profile='research',task_ids=['MO3-COVERAGE-C']);rows=[]
 for rel in cr.MUTABLE:
  b=(ROOT/rel).read_bytes()
  if cr.parse_shard_index(b,rel):
   d=pe.load(ROOT,rel)
   if rel in (cr.DIRECTION,cr.PANORAMA):
    word='direction' if rel==cr.DIRECTION else 'outcome'
    pe.replace_in_index(d,'source_state_revision: 285','source_state_revision: 286')
    pe.replace_in_index(d,f'projection_generation: 20260924-{word}-285',f'projection_generation: 20260924-{word}-286')
   if rel=='MEMORY.md':pe.append_to_shard(d,'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：R0各C入口的注册前残句与复用状态已统一；source pins刷新，数学/范围/next不变，revision286。\n')
   rows+=pe.payload_rows(d,ROOT)
  else:rows.append({'path':rel,'expected_sha256':cr.sha(b),'text':b.decode()})
 s['revision']=286;s['latest_session']=SID
 s['execution_control']['last_checkpoint_session']=SID;s['execution_control']['checkpoint_result']=f'.codex/cognition/checkpoints/{SID}/result.json'
 for rid,word in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:s['records'][rid]['projection_generation']=f'20260924-{word}-286'
 r=s['records']['MO3-COVERAGE-C'];r['source_hashes']={f:cr.sha((ROOT/f).read_bytes()) for f in r['source_hashes']}
 r['revalidation']='Final R0 current-text consistency: distinguish historical W-source-only step from later four-package exact reuse; remove pre-registration absence wording. No proof/source/goal/next-action change.'
 sb=cr.PREFIX+'sessions/'+SID+'/'
 s['records'][SID]={'kind':'session','path':sb+'SESSION.md','lifecycle_status':'HISTORICAL','status':'complete_with_scope','evidence_status':'R0_CURRENT_TEXT_FRESHNESS_ALIGNED','depends_on':[],'related_records':['MO3-COVERAGE-C',PREV],'full_sources':[sb+x for x in cr.SESSION_REQUIRED_FILES],'source_hashes':{},'scope':'R0 wording and input-pin consistency only; parent scope incomplete.'}
 next(x for x in rows if x['path']==cr.STATE)['text']=cr.dump(s).decode()
 old=ROOT/cr.PREFIX/'sessions'/PREV
 for name in cr.SESSION_REQUIRED_FILES:
  text=(old/name).read_text().replace(PREV,SID)
  if name=='SESSION.md':text+='\nR0最终一致性复核：过程索引、父范围剩余和W历史查重段不再把注册前状态当当前；只刷新实际修改的C来源pin。下一仍为Book第1章/附录广度首遍；无需重复全registry或旧kernel。\n'
  if name=='RUNS.json':
   d=json.loads(text);d['session_id']=SID;d['status']='R0_WORDING_FRESHNESS_ONLY';text=cr.dump(d).decode()
  rows.append({'path':sb+name,'expected_sha256':None,'text':text})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['MO3-COVERAGE-C'],'authorization':'User Goal7 sole-integrator authorization; finalize only current text and actual source pins, no scope/proof change.','files':rows}
 out=ROOT/'第三轮机器统观/Session-C/证据/R0/ready-payload.json'
 with out.open('xb') as f:f.write(cr.dump(payload))
 print(json.dumps({'snapshot':p['snapshot'],'payload':str(out.relative_to(ROOT)),'state_applied':False},ensure_ascii=False))
if __name__=='__main__':main()
