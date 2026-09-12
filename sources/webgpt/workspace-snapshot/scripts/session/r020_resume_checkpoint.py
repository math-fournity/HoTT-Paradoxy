"""Recover the failed R020 registration using a NEW immutable session identity.
The prepared session is kept intact. This script is saved before invocation.
No mathematics, peer contact, or full business-cognition claim is performed.
"""
from pathlib import Path
import ast, copy, datetime, hashlib, importlib.util, json, sys
R=Path(__file__).resolve().parents[2]
O=R/'artifacts/r020'; P='.codex/research/hott/'
OLD='S-DISC-20260911-020-GEMINI-DEBATE'
SID=OLD+'-FINAL'
D=P+'dialogues/GEMINI-001/'
def sha(b): return hashlib.sha256(b).hexdigest()
def write_new(path,value):
    p=R/path; b=value if isinstance(value,bytes) else (json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
    if p.exists(): raise RuntimeError('Refuse overwrite '+str(p))
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
spec=importlib.util.spec_from_file_location('r020_runtime_retry',R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
before=rt.plan(R)
if before['revision']!=19: raise RuntimeError('Checkpoint unexpectedly advanced')
original_state=json.loads((R/(P+'STATE.json')).read_text())
prepared_path=P+'sessions/'+OLD+'/SESSION.md'
prepared=(R/prepared_path).read_bytes()
payload=json.loads((O/'checkpoint/PAYLOAD.json').read_text())
if payload['session_id']!=OLD: raise RuntimeError('Unexpected prepared payload')
# Reproduce the original dry-run rejection without any writes, then preserve it.
try:
    rt.checkpoint(R,before['snapshot'],payload,apply=False)
except rt.CognitionError as e:
    if str(e)!='SESSION_RECORD_REQUIRED': raise
    failure={'status':'DRY_RUN_REJECTED_NO_STATE_MUTATION','error':str(e),'original_session_id':OLD,
             'reason':'Prepared session file existed on disk but was not included as a new session in checkpoint changes.',
             'recovery':'Preserve prepared draft, use a new final session identity and include its text in the transaction.',
             'prepared_session_sha256':sha(prepared),'revision_before_retry':before['revision']}
else: raise RuntimeError('Expected failure not reproduced')
write_new('artifacts/r020/CHECKPOINT_FIRST_ATTEMPT.json',failure)
payload['session_id']=SID
for row in payload['files']:
    row['text']=row['text'].replace(OLD,SID)
state_row=next(x for x in payload['files'] if x['path']==P+'STATE.json')
state=json.loads(state_row['text'])
state['records'][SID]['full_sources']=[P+'sessions/'+OLD+'/REQUEST.md',prepared_path,'artifacts/r020/CHECKPOINT_FIRST_ATTEMPT.json']
state['records'][SID]['scope']='Final transaction for scoped review; earlier prepared uncommitted session kept as a draft with failure evidence.'
state_row['text']=json.dumps(state,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
final_session=prepared.decode().replace(OLD,SID)+'''\n## 实际登记重试\n\n首次dry-run因SESSION_RECORD_REQUIRED被拒绝，STATE未更新。先前准备的Session文件保留原字节，不冒充已提交历史。为遵守Session不可覆盖规则，使用新的-FINAL身份，将本正文作为新文件通过事务写入。没有修改治理器、绕过校验或删除旧记录。\n'''
payload['files'].append({'path':P+'sessions/'+SID+'/SESSION.md','expected_sha256':None,'text':final_session})
# Source base hashes remain current because the first attempt never applied.
cp=O/'checkpoint-retry1';cp.mkdir(exist_ok=False)
for name,obj in [('BASE_PLAN.json',before),('PAYLOAD.json',payload)]:
    (cp/name).write_bytes(rt.dump(obj))
(cp/'DRY_RUN.json').write_bytes(rt.dump(rt.checkpoint(R,before['snapshot'],payload,apply=False)))
result=rt.checkpoint(R,before['snapshot'],payload,apply=True)
(cp/'COMMIT.json').write_bytes(rt.dump(result))
after=rt.plan(R);(cp/'FRESH_PLAN.json').write_bytes(rt.dump(after))
if after['revision']!=20 or after['latest_session']!=SID:raise AssertionError('Bad final state')
paths={x['path'] for x in after['documents']}
required={D+'ANALYSIS.md',D+'TO_GEMINI_001.md',D+'000_SOURCE.md',D+'005_GEMINI_ORIGINAL.md',D+'DEBATE_LEDGER.json',P+'sessions/'+SID+'/SESSION.md'}
assert required<=paths
updated=json.loads((R/(P+'STATE.json')).read_text())
assert all(updated['records'][k]==v for k,v in original_state['records'].items())
assert (R/prepared_path).read_bytes()==prepared
try: rt.checkpoint(R,before['snapshot'],payload,apply=False)
except rt.CognitionError as e:
    assert str(e)=='STALE_BASE';(cp/'STALE_BASE.json').write_bytes(rt.dump({'status':'REJECTED','error':str(e)}))
else:raise AssertionError('Stale base accepted')
index=R/'scripts/README.md'
index.write_text(index.read_text()+'''\n\n## R020 · Gemini意见评估与可转发论辩\n\n- session/r020_restore.py：安全恢复提供的revision19 Git包。\n- session/r020_prepare.py：源文逐字保全及五段角色切片、固定规则回查。\n- session/r020_finish.py：首次文件检查与登记准备；dry-run被拒绝，保留源码与错误记录。\n- session/r020_resume_checkpoint.py：保全准备稿，用新Session身份完成受控checkpoint并检查旧快照拒绝。\n- tools/r020_package.py：字节保护、本地Git提交、完整ZIP、论辩子包与bundle恢复校验。\n\n本轮没有新增数学试算或原生证明助手运行。所有新代码均先保存再调用；发送和回信状态不模拟。\n''')
for name in ('r020_restore.py','r020_prepare.py','r020_finish.py','r020_resume_checkpoint.py'):
    ast.parse((R/'scripts/session'/name).read_text())
summary={'schema_version':'r020-run-summary/v1','completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'scope':'Scoped source assessment and user-relay draft, not a mathematical experiment',
         'first_checkpoint_attempt':failure,'checkpoint_status':result['status'],'revision':20,'latest_session':SID,
         'next_load_document_count':len(after['documents']),'new_dialogue_routed':True,
         'stale_base_rejected':True,'prior_records_unchanged':True,'prepared_draft_preserved':True,
         'file_checks':json.loads((O/'FILE_CHECKS.json').read_text())['passed'],
         'peer_contacted':False,'reply_received':False,'new_math_machine_proof':False,
         'full_business_cognition_gate':'NOT_CLAIMED_SCOPED_ATTACHMENT_REVIEW'}
write_new('artifacts/r020/RUN_SUMMARY.json',summary)
print(json.dumps(summary,ensure_ascii=False,indent=2))
