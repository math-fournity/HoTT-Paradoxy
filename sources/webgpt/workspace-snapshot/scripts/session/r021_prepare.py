"""Archive the user-relayed reply without repairing it, and bind review to sources."""
from pathlib import Path
import ast, datetime, hashlib, json, re
R=Path(__file__).resolve().parents[2]
O=R/'artifacts/r021'; D=R/'.codex/research/hott/dialogues/GEMINI-001'
N=D/'rounds/002'

def sha(b):return hashlib.sha256(b).hexdigest()
def put(p,b):
    if p.exists():raise RuntimeError('Refuse overwrite '+str(p))
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
def js(obj):return (json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode()
b=(N/'USER_MESSAGE.md').read_bytes();text=b.decode('utf-8')
a=text.index('````\n')+5;z=text.index('\n````',a)
reply=text[a:z]
# Keep all characters between the original quoted boundaries, including terminal empty lines.
put(N/'IN-002.md',reply.encode())
request=text[z+5:]
put(N/'USER_DIRECTIVE.txt',request.encode())
old=(D/'000_SOURCE.md').read_bytes()
assert old==Path('/mnt/data/Pasted markdown(1).md').read_bytes()
assert 'eval_chi(y, y)' in reply and '系统绝不会允许' in reply and '完全自洽' in reply
headings=re.findall(r'^#### (G0[1-5])',reply,re.M)
assert headings==['G01','G02','G03','G04','G05'] and 'G06 核心构造' in reply
put(N/'INPUT_PROVENANCE.json',js({'schema_version':'hott-relayed-input/v1','dialogue':'GEMINI-001','incoming_id':'IN-002','received_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':'Current user message: manually transcribed visible UTF-8 text, no independent platform raw-byte export','user_message':{'path':str((N/'USER_MESSAGE.md').relative_to(R)),'bytes':len(b),'sha256':sha(b)},'reply_slice':{'start_character':a,'end_character_exclusive':z,'bytes':len(reply.encode()),'sha256':sha(reply.encode())},'original_first_source':{'path':str((D/'000_SOURCE.md').relative_to(R)),'bytes':len(old),'sha256':sha(old),'matches_uploaded_file':True},'no_correction_in_original':True,'direct_peer_contact':False,'peer_identity':'Attributed by user; not API-authenticated','second_reply_contains_machine_execution':False,'quota_statement':'User says no Gemini quota; record as current availability, do not infer recovery date or permanent condition'}))
# Capture exact locally pinned rule passages. No code from inputs is executed.
ranges={
 'HoTT/theory-schema/upstream/book-578b85cc/logic.tex':[(358,418),(797,839)],
 'HoTT/theory-schema/upstream/book-578b85cc/basics.tex':[(1626,1654),(1738,1785)],
 'HoTT/theory-schema/upstream/book-578b85cc/formal.tex':[(978,1015),(1172,1192)]}
parts=['# R021 本地固定规则摘录\n\n这些是已有源码的定点回查，不声称本轮完整重审全书。\n'];identities=[]
for name,sections in ranges.items():
    body=(R/name).read_bytes();lines=body.decode().splitlines()
    identities.append({'path':name,'bytes':len(body),'sha256':sha(body),'read_ranges':sections})
    parts.append('\n## '+name+'\n\nSHA-256: `'+sha(body)+'`\n')
    for lo,hi in sections:
        parts.append('\n```text\n'+'\n'.join(f'{i}: {lines[i-1]}' for i in range(lo,min(hi,len(lines))+1))+'\n```\n')
put(O/'SOURCE_EXCERPTS.md',''.join(parts).encode())
put(O/'SOURCE_IDENTITIES.json',js(identities))
# Record the actual state plan through the existing governed manager, not a new registry.
import importlib.util,sys
spec=importlib.util.spec_from_file_location('r021_cognition_prepare',R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
plan=rt.plan(R);assert plan['revision']==20
put(O/'INITIAL_PLAN.json',rt.dump(plan))
put(O/'READ_SCOPE.json',js({'task':'Scoped two-source assessment and research-plan/governance maintenance','full_business_cognition_gate':'NOT_CLAIMED; new mathematical research/solver not started','read_full':['AGENTS.md','.codex/skills/hott-session-governance/SKILL.md','.codex/skills/hott-paradox-research/SKILL.md','MEMORY.md','.codex/research/hott/FRONTIER.md','.codex/research/hott/RESUME.md','.codex/cognition/PROTOCOL.md',str((D/'TO_GEMINI_001.md').relative_to(R)),str((D/'000_SOURCE.md').relative_to(R)),str((N/'IN-002.md').relative_to(R))],'targeted_prior_sources':'Previous review, Schema entry, Three Questions current explanatory text and pinned rule passages; no claim that all dynamic history or fifth closure was loaded','planned_document_count':len(plan['documents']),'no_dynamic_record_removed_for_context_budget':True}))
print(json.dumps({'reply_bytes':len(reply.encode()),'source1_bytes':len(old),'revision':plan['revision'],'dynamic_documents':len(plan['documents']),'original_reply_not_fixed':True},ensure_ascii=False,indent=2))
