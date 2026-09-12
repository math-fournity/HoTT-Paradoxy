"""Repair record-kind mismatch in saved payload, without changing the governance engine."""
from pathlib import Path
import copy, hashlib, importlib.util, json, sys, traceback
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r035/checkpoint'
P='.codex/research/hott/'
SID='S-PAUSE-20260911-035-COMPUTATION-BOUNDARY'
S=P+'sessions/'+SID+'/'
def dump(obj):return json.dumps(obj,ensure_ascii=False,indent=2)+'\n'
def save(name,obj):
    f=OUT/name
    if f.exists():raise FileExistsError(f)
    f.write_text(dump(obj),encoding='utf-8')
def main():
    spec=importlib.util.spec_from_file_location('r035_apply_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    base=json.loads((OUT/'BASE.json').read_text());old=json.loads((OUT/'STATE_BASE.json').read_text())
    payload=json.loads((OUT/'PAYLOAD.json').read_text())
    try:rt.checkpoint(ROOT,base['snapshot'],payload,apply=False)
    except rt.CognitionError as exc:
        if str(exc)!='LATEST_SESSION_MISSING':raise
        save('FIRST_FAILURE_REPLAY.json',{'error':str(exc),'traceback':traceback.format_exc(),
             'scope':'Reproduced dry-run rejection of original saved payload; first tool call exited 1.',
             'reason':'latest record kind must be session, not pause_checkpoint','writes':False})
    else:raise RuntimeError('Expected original payload to fail')
    corrected=copy.deepcopy(payload)
    for row in corrected['files']:
        if row['path']==P+'STATE.json':
            state=json.loads(row['text']);state['records'][SID]['kind']='session';state['records'][SID]['session_type']='user_pause'
            row['text']=dump(state)
        elif row['path']==S+'SESSION.md':
            row['text']+='\n## 保存过程的失败与修正\n首次dry-run因最新记录kind写成pause_checkpoint而被原运行器拒绝，LATEST_SESSION_MISSING；未写入状态。保留原脚本与载荷，第二脚本仅修正为session并另加session_type，不修改治理器。\n'
    save('PAYLOAD_CORRECTED.json',corrected)
    save('DRY.json',rt.checkpoint(ROOT,base['snapshot'],corrected,apply=False))
    result=rt.checkpoint(ROOT,base['snapshot'],corrected,apply=True);save('COMMIT.json',result)
    after=rt.plan(ROOT);save('AFTER.json',after)
    state=json.loads((ROOT/(P+'STATE.json')).read_text())
    assert all(state['records'][k]==v for k,v in old['records'].items())
    assert state['active']==old['active']
    assert state['unresolved']==old['unresolved']
    assert state['execution_control']['status']=='PAUSED_BY_USER'
    routes={row['path'] for row in after['documents']}
    required=set(state['records'][SID]['full_sources']+[S+'SESSION.md','MEMORY.md',P+'reviews/SELF-REFERENCE-006/PROOF_NOTE.md',P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md'])
    assert required<=routes, required-routes
    try:rt.checkpoint(ROOT,base['snapshot'],corrected,apply=False)
    except rt.CognitionError as exc:
        if str(exc)!='STALE_BASE':raise
        save('STALE.json',{'status':'REJECTED','error':str(exc),'writes':False})
    else:raise RuntimeError('Stale payload accepted')
    summary={'status':result['status'],'revision':35,'execution_status':'PAUSED_BY_USER',
       'previous_records_unchanged':len(old['records']),'records':len(state['records']),
       'active_and_unresolved_preserved':True,'required_sources_routed':True,
       'planned_documents':len(after['documents']),'planned_bytes':after['total_bytes'],
       'stale_write_rejected':True,'business_cognition':'NOT_CERTIFIED_BOUNDED_PAUSE',
       'mathematical_experiments':0,'native_formal_runs':0,'first_failure_preserved':True}
    save('SUMMARY.json',summary);print(dump(summary))
if __name__=='__main__':main()
