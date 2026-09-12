"""Mechanical/source regression checks for R021; not AI comprehension or math proof."""
from pathlib import Path
import ast, datetime, hashlib, importlib.util, json, re, sys
from urllib.parse import urlsplit, unquote
R=Path(__file__).resolve().parents[2]; O=R/'artifacts/r021'
P='.codex/research/hott/'; D=R/(P+'dialogues/GEMINI-001'); N=D/'rounds/002'
C=R/(P+'candidates/RP-B01'); SID='S-DISC-20260911-021-GEMINI-SYNTHESIS'
checks=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def check(name,condition,detail):
    checks.append({'id':name,'status':'PASS' if condition else 'FAIL','scope':detail})
def read(rel):return (R/rel).read_text()
def old(rel):return (R/'.codex/history/r021-before'/rel).read_bytes()
base=json.loads((O/'BASELINE_FILES.json').read_text())
base_map={r['path']:r for r in base}
integration=json.loads((O/'INTEGRATION.json').read_text())
allowed={x['path'] for x in integration['changes']} | {
 'MEMORY.md',P+'STATE.json',P+'FRONTIER.md',P+'RESUME.md',P+'LESSONS.md','.codex/cognition/HEAD.json'}
changed=[];missing=[]
for name,row in base_map.items():
    f=R/name
    if not f.is_file():missing.append(name)
    elif sha(f.read_bytes())!=row['sha256']:changed.append(name)
check('V01_prior_file_scope',not missing and set(changed)<=allowed,
      {'base_files':len(base),'changed':changed,'missing':missing,'allowed':sorted(allowed)})
check('V02_source1_original',(D/'000_SOURCE.md').read_bytes()==Path('/mnt/data/Pasted markdown(1).md').read_bytes(),
      'Full original uploaded Markdown bytes, not an extracted summary')
msg=(N/'USER_MESSAGE.md').read_text();a=msg.index('````\n')+5;z=msg.index('\n````',a)
check('V03_current_reply_slice',(N/'IN-002.md').read_text()==msg[a:z],
      'Exact visible-transcription slice; not independent platform-byte authentication')
check('V04_user_directive',(N/'USER_DIRECTIVE.txt').read_text()==msg[z+5:],
      'Quota and persistence instruction retained after closing fence')
prov=json.loads((N/'INPUT_PROVENANCE.json').read_text())
check('V05_reply_fingerprint',sha((N/'IN-002.md').read_bytes())==prov['reply_slice']['sha256'],
      {'bytes':(N/'IN-002.md').stat().st_size})
reply=(N/'IN-002.md').read_text()
check('V06_no_silent_correction',all(t in reply for t in ['eval_chi(y, y)','系统绝不会允许','完全自洽']),
      'Original residual errors preserved; correction lives in assessment')
check('V07_outgoing_history',sha((D/'TO_GEMINI_001.md').read_bytes())==
      'de5e72847a80ccfd53027f8eed2eeb547d8b7265c05dedd935bc0dad0196b57b' and
      (D/'TO_GEMINI_001.md').read_bytes()==(D/'TO_GEMINI_001.txt').read_bytes(),
      'Original OUT-001 and text copy byte-identical')
led=json.loads((D/'DEBATE_LEDGER.json').read_text())
check('V08_actual_incoming',led['round']==2 and {x['id'] for x in led['incoming']}=={'IN-001','IN-002'} and
      led['outgoing'][0]['reply_received'], 'Actual received reply recorded; outgoing history not rewritten')
check('V09_no_fictional_send',not led['outgoing'][0]['sent'] and
      not led['workflow']['direct_contact_this_round'] and not led['workflow']['simulated_peer_reply'],
      'No direct peer contact or simulated reply')
check('V10_no_peer_dependency',not led['workflow']['awaiting_peer_to_start_research'] and
      all(not x['further_peer_reply_required'] for x in led['questions']),
      'Plan continues independently of Gemini quota')
check('V11_question_coverage',{x['id'] for x in led['questions']}=={f'G0{i}' for i in range(1,7)} and
      all(x['peer_response']=='IN-002' and x['history'][0]['peer_response']=='NOT_RECEIVED' for x in led['questions']),
      'Six actual per-question state transitions retained')
check('V12_first_verdicts_immutable',led['claims']==json.loads(old(str((D/'DEBATE_LEDGER.json').relative_to(R))))['claims'],
      'Historical first-round verdicts unchanged; transitions separately recorded')
skill=read('.codex/skills/hott-paradox-research/SKILL.md')
oldskill=old('.codex/skills/hott-paradox-research/SKILL.md').decode()
gate=lambda t:t[t.index('## -1.'):t.index('## 0.')]
check('V13_full_load_policy_unchanged',gate(skill)==gate(oldskill),
      'No change to mandatory cognitive loading section')
check('V14_skill_version','version: "1.3.3"' in skill and '## 14. v1.3.3' in skill,
      'Active business Skill updated, not a proposed package')
check('V15_stale_next_removed','下一步继承revision11的实际问题' not in skill and 'RP-B01' in skill,
      'No permanent next-step reset to old Done task')
manifest=json.loads(read('.codex/skills/hott-paradox-research/MANIFEST.json'))
matched=[]
for row in manifest['files']:
    b=(R/'.codex/skills/hott-paradox-research'/row['path']).read_bytes()
    matched.append(len(b)==row['bytes'] and sha(b)==row['sha256'])
check('V16_current_skill_manifest',manifest['version']=='1.3.3' and all(matched),
      {'entries':len(matched),'scope':'Current skill payload only; legacy delivery manifests are historical'})
qrel='HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md'
check('V17_two_goal_owner_update','v5' in read(qrel) and '双向保留' in read(qrel) and
      '双向目标同时保留' in read('AGENTS.md') and '双向保留' in read('HoTT/Z_LAW_REALITY_RELATIVE_PARADOXES.md'),
      'Question owner, project entry and Z goal aligned without rewriting philosophy original')
check('V18_old_byte_backups',all(sha((R/x['backup']).read_bytes())==x['old_sha256'] for x in integration['changes']),
      'Every human-edited prior file has exact before-image backup')
protected=[p for p in base_map if p.startswith(('认知闭包/','HoTT/theory-schema/',
       'HoTT/formal/','.codex/research/hott/sessions/','.codex/skills/hott-session-governance/')) or
       p=='HoTT/CLAIM_EVIDENCE_MATRIX.md' or p.startswith('scripts/recovered/')]
check('V19_protected_sources',all(p not in changed and p not in missing for p in protected),
      {'files':len(protected),'scope':'Cognitive closure, schema, source rules, old sessions, formal sources, old recovered code'})
new_scripts=sorted((R/'scripts').rglob('r021_*.py'))
syntax=[]
for f in new_scripts:
    try:ast.parse(f.read_text());syntax.append(True)
    except SyntaxError:syntax.append(False)
check('V20_new_code_syntax',all(syntax),{'scripts':[str(p.relative_to(R)) for p in new_scripts],
      'scope':'Syntax only, including preserved failed payload builder'})
newpy=[p for p in R.rglob('*.py') if '.git' not in p.parts and p.relative_to(R).as_posix() not in base_map]
check('V21_scripts_first_locations',all(p.is_relative_to(R/'scripts') for p in newpy),
      'All new executable Python sources located in scripts')
claims=json.loads((C/'CLAIMS.json').read_text())
check('V22_candidate_not_machine_proof',claims['native_formalization']=='NOT_RUN' and
      claims['mathematical_experiments']=='NOT_RUN' and claims['independent_review']=='NOT_RUN',
      'Planning and explanatory derivation do not impersonate native validation')
construction=(C/'CONSTRUCTION.md').read_text();assessment=(N/'ASSESSMENT.md').read_text()
check('V23_contract_boundaries',all(t in construction for t in ['χ:ℕ×ℕ→Bool','Rep(χ)','D_h(y)','模型假设','单价性、HIT']) and
      all(t in assessment for t in ['唯一选择','绝对一致性','noncomputable','Code 可判定相等']),
      'Critical premises and distinctions recorded; keyword presence is not a mathematical proof')
# Fresh manager plan: do not execute input code or archived tests.
spec=importlib.util.spec_from_file_location('r021_verify_runtime',R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
plan=rt.plan(R);docs={x['path'] for x in plan['documents']}
need={str(p.relative_to(R)) for p in [N/'IN-002.md',N/'ASSESSMENT.md',N/'SYNTHESIS.md',C/'PLAN.md',C/'CONSTRUCTION.md',C/'CLAIMS.json']}
check('V24_current_dynamic_route',plan['revision']==21 and plan['latest_session']==SID and need<=docs,
      {'documents':len(plan['documents']),'required_new_paths':sorted(need)})
state=json.loads(read(P+'STATE.json'));oldstate=json.loads(old(P+'STATE.json'))
check('V25_history_record_preservation',set(oldstate['records'])<=set(state['records']) and
      all(state['records'][k]['path']==v['path'] and state['records'][k]['kind']==v['kind'] for k,v in oldstate['records'].items()),
      'Old record identities never removed or retargeted')
check('V26_metadata_update_scope',all(state['records'][k]==v for k,v in oldstate['records'].items()
      if k not in {'D-GEMINI-001','U-DUAL-DIRECTION-JSON-001'}),
      'Only two justified metadata records changed; no old mathematical status upgrades')
check('V27_prior_dry_run_failure',json.loads((O/'checkpoint/FAILURE.json').read_text())['error']=='LATEST_SESSION_MISSING' and
      json.loads((O/'checkpoint/BASE_PLAN.json').read_text())['revision']==20,
      'Rejected bad session-kind payload preserved; runtime unmodified')
check('V28_checkpoint_and_stale',json.loads((O/'checkpoint-final/COMMIT.json').read_text())['status']=='CHECKPOINT_COMMITTED' and
      json.loads((O/'checkpoint-final/STALE_BASE.json').read_text())['error']=='STALE_BASE',
      'Actual final transaction succeeded and old snapshot refused')
scan=[D/'README.md',N/'SOURCES.md',N/'SYNTHESIS.md',N/'ASSESSMENT.md',C/'PLAN.md',C/'CONSTRUCTION.md',R/qrel]
bad=[]
for f in scan:
    for target in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)',f.read_text()):
        u=urlsplit(target)
        if u.scheme or target.startswith('#'):continue
        dest=f.parent/unquote(u.path)
        if not dest.exists():bad.append({'source':str(f.relative_to(R)),'target':target})
check('V29_local_links',not bad,{'broken':bad,'anchors':'Existence only; external URLs not re-fetched'})
web=json.loads((O/'web/MANIFEST.json').read_text())
check('V30_download_failures_disclosed',all(x['status']=='FAILED' and x['error'] for x in web['sources']) and
      'DNS' in (N/'SOURCES.md').read_text(),
      'Web reading and failed container snapshots distinguished')
check('V31_scope_not_fabricated',json.loads((O/'READ_SCOPE.json').read_text())['full_business_cognition_gate'].startswith('NOT_CLAIMED') and
      '没有通过' in read('MEMORY.md'),
      'No full dynamic-cognition or kernel claim')
result={'schema_version':'hott-r021-file-checks/v1','scope':'Mechanical file/source/state regression, not mathematical or AI semantic certification',
 'passed':sum(x['status']=='PASS' for x in checks),'total':len(checks),'checks':checks,
 'changed_existing_paths':sorted(changed),'protected_unchanged_files':len(base)-len(changed),
 'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'native_math_runs':0,'peer_contacted':False,'full_cognition':'NOT_CLAIMED'}
out=O/'FILE_CHECKS.json'
if out.exists():raise RuntimeError('Existing check report; preserve it and use a new run identifier')
out.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
print(json.dumps({'passed':result['passed'],'total':result['total'],'failed':[x for x in checks if x['status']=='FAIL'],
                  'protected_unchanged_files':result['protected_unchanged_files']},ensure_ascii=False,indent=2))
raise SystemExit(0 if result['passed']==result['total'] else 1)
