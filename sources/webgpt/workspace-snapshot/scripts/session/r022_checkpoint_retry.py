#!/usr/bin/env python3
"""Repair the rejected payload's metadata only; keep original script and failure log."""
from pathlib import Path
import importlib.util, json, sys
R=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
D=P+'dialogues/GEMINI-001/'
SID='S-DISC-20260911-022-GEMINI-OUT002'
O=R/'artifacts/r022'
CP=O/'checkpoint-final'

def dump(o):return json.dumps(o,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
def put(p,o):
    if p.exists():raise RuntimeError('Refuse overwrite '+str(p))
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(dump(o),encoding='utf-8')

def main():
    spec=importlib.util.spec_from_file_location('r022_retry_runtime',R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    before=rt.plan(R)
    assert before['revision']==21
    original=json.loads((R/(P+'STATE.json')).read_text())
    payload=json.loads((O/'checkpoint/PAYLOAD.json').read_text())
    row=next(x for x in payload['files'] if x['path']==P+'STATE.json')
    state=json.loads(row['text'])
    assert state['records'][SID]['kind']=='session_record'
    state['records'][SID]['kind']='session'
    state['records']['D-GEMINI-OUT-002']['status']='review_required'
    state['records']['D-GEMINI-OUT-002']['workflow_status']='READY_FOR_USER_RELAY'
    state['records'][SID]['full_sources'].extend(['artifacts/r022/CHECKPOINT_EXECUTION.json','artifacts/r022/PREPARE_EXECUTION.json'])
    row['text']=dump(state)
    session=next(x for x in payload['files'] if x['path']==P+'sessions/'+SID+'/SESSION.md')
    session['text']+='\n## 登记元数据纠正\n\n第一次dry-run因session_record不等于治理器要求的session而拒绝，未写入工作状态。修正此字段，并把依赖待复核记录的新信件状态设为review_required；其待转发状态另保存在workflow_status。原失败源码、载荷及错误日志保留，引擎未改。\n'
    lessons=next(x for x in payload['files'] if x['path']==P+'LESSONS.md')
    lessons['text']+='\n- 当前治理器要求latest记录kind为session，且继承待复核依赖的记录也须标review_required；信件发送状态另设字段。R021已发生过同类错误，本轮再次重复，保存为需避免的工程教训，不称首次无误成功。\n'
    put(CP/'BASE_PLAN.json',before);put(CP/'PAYLOAD.json',payload)
    put(CP/'DRY_RUN.json',rt.checkpoint(R,before['snapshot'],payload,apply=False))
    result=rt.checkpoint(R,before['snapshot'],payload,apply=True)
    put(CP/'COMMIT.json',result)
    after=rt.plan(R);put(CP/'AFTER_PLAN.json',after)
    must={D+'TO_GEMINI_002.md',D+'rounds/003/USER_REQUEST.md',D+'rounds/003/RESPONSE_MAP.json',D+'rounds/003/SOURCES.md',P+'sessions/'+SID+'/SESSION.md','MEMORY.md'}
    assert must <= {x['path'] for x in after['documents']}
    assert after['revision']==22
    try:rt.checkpoint(R,before['snapshot'],payload,apply=False)
    except rt.CognitionError as exc:
        assert str(exc)=='STALE_BASE';put(CP/'STALE_BASE.json',{'status':'REJECTED','error':str(exc)})
    else:raise RuntimeError('Stale base accepted')
    actual=json.loads((R/(P+'STATE.json')).read_text())
    assert all(actual['records'][k]==v for k,v in original['records'].items() if k!='D-GEMINI-001')
    summary={'status':result['status'],'revision':22,'latest_session':SID,
        'new_letter_in_load_set':True,'dynamic_documents':len(after['documents']),
        'old_record_identities_preserved':True,'stale_base_rejected':True,
        'direct_send':False,'peer_reply_received':False,'full_business_cognition':'NOT_CLAIMED',
        'prior_rejected_dry_run':'LATEST_SESSION_MISSING',
        'metadata_repairs':['latest kind=session','new dependent outgoing record status=review_required']}
    put(O/'CHECKPOINT_SUMMARY.json',summary)
    print(dump(summary))
if __name__=='__main__':main()
