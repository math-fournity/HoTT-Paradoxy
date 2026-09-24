#!/usr/bin/env python3
"""Prepare a bounded post-registration wording/pin alignment, never apply it."""
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'.codex/tools'))
sys.path.insert(0,str(ROOT/'scripts/audit'))
import cognition_runtime as cr
import projection_edit as pe
SID='S-RES-20260924-MO3-C-R0-ALIGN'
PREV='S-RES-20260924-MO3-C-R0'
C='第三轮机器统观/Session-C/'
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    s=json.loads((ROOT/cr.STATE).read_text())
    assert s['revision']==284 and s['latest_session']==PREV and SID not in s['records']
    # Current managed files must still equal the actual registration after-images.
    t=json.loads((ROOT/f'.codex/cognition/checkpoints/{PREV}/transaction.json').read_text())
    assert all(sha((ROOT/r['path']).read_bytes())==r['new_sha256'] for r in t['rows'])
    p=cr.plan(ROOT,profile='research',task_ids=['MO3-COVERAGE-C'])
    rows=[]
    for rel in cr.MUTABLE:
        b=(ROOT/rel).read_bytes();text=b.decode()
        if cr.parse_shard_index(b,rel):
            doc=pe.load(ROOT,rel)
            if rel in (cr.DIRECTION,cr.PANORAMA):
                word='direction' if rel==cr.DIRECTION else 'outcome'
                pe.replace_in_index(doc,'source_state_revision: 284','source_state_revision: 285')
                pe.replace_in_index(doc,f'projection_generation: 20260924-{word}-284',f'projection_generation: 20260924-{word}-285')
                pe.replace_in_index(doc,'日期：2026-09-12','日期：2026-09-24')
            if rel=='MEMORY.md':
                pe.append_to_shard(doc,'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：登记284后的C文档状态/来源pin与当前日期路由对齐；无新理论单元、数学或下一方向变化；revision285。\n')
            rows+=pe.payload_rows(doc,ROOT)
        else:
            if rel==cr.PREFIX+'FRONTIER.md':text=text.replace('## 当前状态（2026-09-21）','## 当前状态（2026-09-24）')
            if rel==cr.PREFIX+'RESUME.md':
                text=text.replace('PROTOCOL及Goal6','PROTOCOL及Goal7').replace('## 当前阶段（2026-09-21）','## 当前阶段（2026-09-24）')
            rows.append({'path':rel,'expected_sha256':sha(b),'text':text})
    s['revision']=285;s['latest_session']=SID
    s['execution_control']['last_checkpoint_session']=SID
    s['execution_control']['checkpoint_result']=f'.codex/cognition/checkpoints/{SID}/result.json'
    for rid,word in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:
        s['records'][rid]['projection_generation']=f'20260924-{word}-285'
    rec=s['records']['MO3-COVERAGE-C']
    rec['source_hashes']={f:sha((ROOT/f).read_bytes()) for f in rec['source_hashes']}
    rec['revalidation']='Post-284 wording alignment: scope/audit now refer to actual canonical registration instead of pre-registration absence; proof scopes, parent requirements, source bytes and next action unchanged.'
    sb=cr.PREFIX+'sessions/'+SID+'/'
    s['records'][SID]={'kind':'session','path':sb+'SESSION.md','lifecycle_status':'HISTORICAL','status':'complete_with_scope','evidence_status':'POST_REGISTRATION_WORDING_AND_PIN_ALIGNMENT','depends_on':[],'related_records':['MO3-COVERAGE-C',PREV],'full_sources':[sb+x for x in cr.SESSION_REQUIRED_FILES],'source_hashes':{},'scope':'Correct registration-time absence wording and refresh own pins; no new research result or scope change.'}
    next(r for r in rows if r['path']==cr.STATE)['text']=cr.dump(s).decode()
    oldbase=ROOT/cr.PREFIX/'sessions'/PREV
    audit=(oldbase/'CORE_COGNITION_AUDIT.md').read_text().replace(PREV,SID)
    audit=audit.replace('update_decision: register C and current queue only; no parent completion','update_decision: align post-registration wording and own source pins only; no parent completion')
    audit+='\n本次差分只纠正注册前缺checkpoint的已失效表述、日期及Goal7恢复路由。48条原文立场和数学范围未改变；原始284审计/事务保留。\n'
    session=f'# {SID}\n\n研究对象与父范围仍为Goal7；本单元只对齐注册后的状态措辞及source pins。\n\n- host: codex-desktop\n- model: Astra（用户选择；不认证后端）\n- tier: T3\n- role: RESEARCH_GENERATION / registration alignment\n- load_receipt: 同一R0单元连续性；初次全文与恢复见{C}执行记录001，284全部37后像实际无漂移。\n- parent: PARENT_SCOPE_INCOMPLETE\n- next: 按284既定Book第一章/附录对应推进；新理论单元前重读最高指示。\n\n未新读理论单元/未运行kernel/未改旧证据。已有治理正文足以要求这次纠正，reflection=no-plan-change。完整48KC兼容审计延续同单元实际读取与立场；嵌套分片writer缺口保持。应用只认本SID的canonical result。\n\n|element_usage|用途|\n|---|---|\n|source freshness|发现注册前措辞不再current，原位纠正|\n|canonical writer|刷新实际已核自身pin，不手改STATE|\n|KC/三方|延续本单元48条及范围；不以数据一致自证理解|\n'
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'kernel_runs':[],'evidence':[f'.codex/cognition/checkpoints/{PREV}/result.json',C+'旧成果复用与缺口.md'],'status':'REGISTRATION_ALIGNMENT_ONLY'}
    for name,text in [('SESSION.md',session),('CORE_COGNITION_AUDIT.md',audit),('RUNS.json',cr.dump(runs).decode())]:
        rows.append({'path':sb+name,'expected_sha256':None,'text':text})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['MO3-COVERAGE-C'],'authorization':'Continuation of user-authorized sole Session C canonical current-owner registration; correct only own post-registration wording and pins, preserve all historical evidence.','files':rows}
    out=ROOT/C/'证据/R0/alignment-payload.json'
    with out.open('xb') as f:f.write(cr.dump(payload))
    print(json.dumps({'snapshot':p['snapshot'],'payload':str(out.relative_to(ROOT)),'proposed_revision':285,'state_applied':False},ensure_ascii=False))
if __name__=='__main__':main()
