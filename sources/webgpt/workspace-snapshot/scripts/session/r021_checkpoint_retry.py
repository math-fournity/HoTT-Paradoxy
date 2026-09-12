"""Retry only the rejected R021 payload; preserve original script and failure.
The existing manager requires latest-session.kind == 'session', not 'session_record'.
"""
from pathlib import Path
import importlib.util, json, sys, hashlib, datetime
R=Path(__file__).resolve().parents[2]; O=R/'artifacts/r021'; CP=O/'checkpoint-final'
P='.codex/research/hott/'; SID='S-DISC-20260911-021-GEMINI-SYNTHESIS'
def put(p,o):
    if p.exists():raise RuntimeError('Refuse overwrite '+str(p))
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
spec=importlib.util.spec_from_file_location('r021_retry_runtime',R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
before=rt.plan(R);assert before['revision']==20
old=json.loads((R/(P+'STATE.json')).read_text())
payload=json.loads((O/'checkpoint/PAYLOAD.json').read_text())
state_row=next(x for x in payload['files'] if x['path']==P+'STATE.json')
state=json.loads(state_row['text'])
assert state['records'][SID]['kind']=='session_record'
state['records'][SID]['kind']='session'
state['records'][SID]['full_sources'].append('artifacts/r021/checkpoint/FAILURE.json')
state_row['text']=json.dumps(state,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
row=next(x for x in payload['files'] if x['path']==P+'sessions/'+SID+'/SESSION.md')
row['text']+='\n## 实际登记纠错\n\n首个dry-run因LATEST_SESSION_MISSING被拒绝：新Session错误标为session_record，现改为运行器要求的session。首次没有写回STATE，也未产生Session文件。原失败脚本与PAYLOAD/FAILURE保留；不修改引擎或绕过门禁。\n'
put(CP/'BASE_PLAN.json',before);put(CP/'PAYLOAD.json',payload)
try:
    put(CP/'DRY_RUN.json',rt.checkpoint(R,before['snapshot'],payload,apply=False))
    result=rt.checkpoint(R,before['snapshot'],payload,apply=True)
    put(CP/'COMMIT.json',result)
except Exception as exc:
    put(CP/'FAILURE.json',{'type':type(exc).__name__,'error':str(exc)})
    raise
plan=rt.plan(R);put(CP/'FRESH_PLAN.json',plan)
assert plan['revision']==21 and plan['latest_session']==SID
paths={x['path'] for x in plan['documents']}
needed={P+'dialogues/GEMINI-001/rounds/002/'+n for n in
        ['IN-002.md','USER_MESSAGE.md','ASSESSMENT.md','SYNTHESIS.md','SOURCES.md']}
needed|={P+'candidates/RP-B01/'+n for n in ['PLAN.md','CONSTRUCTION.md','CLAIMS.json']}
needed.add(P+'sessions/'+SID+'/SESSION.md')
assert needed<=paths
new=json.loads((R/(P+'STATE.json')).read_text())
allowed={'D-GEMINI-001','U-DUAL-DIRECTION-JSON-001'}
assert set(old['records'])<=set(new['records'])
assert all(new['records'][k]==v for k,v in old['records'].items() if k not in allowed)
try:rt.checkpoint(R,before['snapshot'],payload,apply=False)
except rt.CognitionError as exc:
    assert str(exc)=='STALE_BASE';put(CP/'STALE_BASE.json',{'status':'REJECTED','error':str(exc)})
else:raise AssertionError('Stale payload accepted')
summary={'status':result['status'],'revision':21,'latest_session':SID,
 'dynamic_documents':len(plan['documents']),'new_sources_and_plan_routed':True,
 'prior_records_removed':False,'prior_record_metadata_updated':sorted(allowed),
 'stale_base_rejected':True,'first_dry_run_rejected':'LATEST_SESSION_MISSING',
 'business_gate':'NOT_CLAIMED','new_math_machine_run':False,
 'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
put(O/'CHECKPOINT_SUMMARY.json',summary)
print(json.dumps(summary,ensure_ascii=False,indent=2))
