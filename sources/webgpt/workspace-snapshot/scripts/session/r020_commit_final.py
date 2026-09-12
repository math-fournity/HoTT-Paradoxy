"""Apply the corrected R020 checkpoint; preserve both rejected dry-run attempts.
New discussion inherits pending-review status instead of upgrading its dependency.
"""
from pathlib import Path
import ast, datetime, hashlib, importlib.util, json, sys
R=Path(__file__).resolve().parents[2];O=R/'artifacts/r020';P='.codex/research/hott/'
SID='S-DISC-20260911-020-GEMINI-DEBATE-FINAL';D=P+'dialogues/GEMINI-001/'
def dump(path,obj):
    if path.exists():raise RuntimeError('Refuse overwrite '+str(path))
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
spec=importlib.util.spec_from_file_location('r020_runtime_final',R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
before=rt.plan(R);assert before['revision']==19
oldstate=json.loads((R/(P+'STATE.json')).read_text())
payload=json.loads((O/'checkpoint-retry1/PAYLOAD.json').read_text())
try:rt.checkpoint(R,before['snapshot'],payload,apply=False)
except rt.CognitionError as e:
    assert str(e)=='DEPENDENCY_REVIEW_REQUIRED: D-GEMINI-001'
    failure={'status':'DRY_RUN_REJECTED_NO_STATE_MUTATION','error':str(e),
             'reason':'New debate depends on a pending-review user-framing record; workflow status must inherit review_required.',
             'resolution':'Keep prior dependencies unchanged; mark the new debate review_required, not certified.',
             'revision':19}
else:raise RuntimeError('Expected dependency gate did not run')
dump(O/'CHECKPOINT_SECOND_ATTEMPT.json',failure)
row=next(x for x in payload['files'] if x['path']==P+'STATE.json')
state=json.loads(row['text']);state['records']['D-GEMINI-001']['status']='review_required'
state['records'][SID]['full_sources'].append('artifacts/r020/CHECKPOINT_SECOND_ATTEMPT.json')
row['text']=json.dumps(state,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
session=next(x for x in payload['files'] if x['path']==P+'sessions/'+SID+'/SESSION.md')
session['text']+='\n第二次dry-run因待复核依赖传播被拒绝。现将新讨论状态明确为review_required，既不升级原用户目标的治理验收，也不把本次评估当数学认证。原依赖条目保持原样。\n'
cp=O/'checkpoint-final';cp.mkdir(exist_ok=False)
for name,obj in [('BASE_PLAN.json',before),('PAYLOAD.json',payload)]:dump(cp/name,obj)
dry=rt.checkpoint(R,before['snapshot'],payload,apply=False);dump(cp/'DRY_RUN.json',dry)
result=rt.checkpoint(R,before['snapshot'],payload,apply=True);dump(cp/'COMMIT.json',result)
after=rt.plan(R);dump(cp/'FRESH_PLAN.json',after)
assert after['revision']==20 and after['latest_session']==SID
required={D+n for n in ('ANALYSIS.md','000_SOURCE.md','005_GEMINI_ORIGINAL.md','TO_GEMINI_001.md','DEBATE_LEDGER.json')}
assert required<={x['path'] for x in after['documents']}
newstate=json.loads((R/(P+'STATE.json')).read_text())
assert all(newstate['records'][k]==v for k,v in oldstate['records'].items())
try:rt.checkpoint(R,before['snapshot'],payload,apply=False)
except rt.CognitionError as e:
    assert str(e)=='STALE_BASE';dump(cp/'STALE_BASE.json',{'status':'REJECTED','error':str(e)})
else:raise AssertionError('Stale snapshot accepted')
index=R/'scripts/README.md'
index.write_text(index.read_text()+'''\n\n## R020 · Gemini意见与首封论辩\n\n- session/r020_restore.py：安全恢复revision19 Git包，不伪造rev24。\n- session/r020_prepare.py：原文及五个角色块逐字切片、固定来源回查。\n- session/r020_finish.py：首次记录准备与15项文件检查；dry-run未通过，错误保留。\n- session/r020_resume_checkpoint.py：保全未提交稿并换用新Session身份；依赖门禁拒绝，错误保留。\n- session/r020_commit_final.py：明确待复核依赖状态后完成事务，原记录与治理器不改。\n- tools/r020_package.py：本地Git与完整/转发ZIP、bundle读回恢复检查。\n\n没有新的数学实验或原生内核证明。所有新增代码先保存再调用；首封信未发送，没有模拟对方回复。\n''')
for name in ('r020_restore.py','r020_prepare.py','r020_finish.py','r020_resume_checkpoint.py','r020_commit_final.py'):
    ast.parse((R/'scripts/session'/name).read_text())
summary={'schema_version':'r020-run-summary/v1','completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'scope':'Scoped opinion assessment and unsent correspondence','initial_dry_run_errors':['SESSION_RECORD_REQUIRED','DEPENDENCY_REVIEW_REQUIRED: D-GEMINI-001'],
         'checkpoint_status':result['status'],'revision':20,'latest_session':SID,
         'next_load_document_count':len(after['documents']),'new_dialogue_routed':True,'stale_base_rejected':True,
         'prior_records_unchanged':True,'prepared_draft_retained':True,
         'file_checks':json.loads((O/'FILE_CHECKS.json').read_text())['passed'],
         'discussion_status':'review_required','peer_contacted':False,'reply_received':False,
         'new_mathematical_experiment':False,'proof_assistant_run':False,
         'full_business_cognition_gate':'NOT_CLAIMED_SCOPED_ATTACHMENT_REVIEW'}
dump(O/'RUN_SUMMARY.json',summary)
print(json.dumps(summary,ensure_ascii=False,indent=2))
