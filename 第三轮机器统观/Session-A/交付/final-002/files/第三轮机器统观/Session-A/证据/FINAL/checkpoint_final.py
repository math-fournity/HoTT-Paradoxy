#!/usr/bin/env python3
"""One-shot canonical research conclusion; delivery seal follows the subject commit."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, re, subprocess, sys
ROOT=Path(__file__).resolve().parents[4]; HERE=Path(__file__).resolve().parent
OWN='第三轮机器统观/Session-A/'; TASK='MO3-GOVERNED-A'
SID='S-RES-20260924-MO3-A-FINAL'; RID='R-MO3-FINAL-SYNTHESIS-20260924'
BASE=f'.codex/research/hott/sessions/{SID}/'
REPORT=OWN+'最终报告.md'; EXEC=OWN+'执行记录/014 - 最终语义复核与完成对账.md'; AUDIT=OWN+'审计/FINAL/CORE_COGNITION_AUDIT.md'
ESSAYS={
 '006':'扩展认知/006 - 第三条发现路径：把知识谱当作被考察对象.md',
 '008':'扩展认知/008 - 现实对齐：理论是现实的骨架式模仿.md'}
CHANGED=[OWN+p for p in ['执行记录.md','覆盖与关系.md','覆盖与关系/003 - 首遍语义裁决与实际验证选择.md','覆盖与关系/004 - 语义单元与联合条件.md','覆盖与关系/005 - 已接受非叶问题的独立对账.md','方法与偏差复测/003 - 有序运输的异机制留出.md','结论账本.md']]
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(sp);sp.loader.exec_module(rt)
    sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as edit
    s=json.loads((ROOT/rt.STATE).read_text());h=json.loads((ROOT/rt.HEAD).read_text())
    assert s['revision']==280 and SID not in s['records'] and RID not in s['records']
    assert all(sha(p)==v for p,v in h['tracked'].items())
    assert subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT)==b''
    assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()=='781871d8496ba79e960af31d7f14fdf79c55a7fa'
    methods=json.loads((HERE.parent/'MS01/method-inputs/MANIFEST.json').read_text());assert all(sha(x['source'])==x['sha256'] for x in methods['rows'])
    pattern=r'<!-- original:(KC-\d+):begin -->(.*?)<!-- original:\1:end -->'
    proposed={};originals={}
    for k,p in ESSAYS.items():
        old=(ROOT/p).read_text();before=(HERE/f'ESSAY-{k}-BEFORE.txt').read_text();new=(HERE/f'ESSAY-{k}-PROPOSED.txt').read_text()
        assert old==before and old!=new
        q=re.findall(pattern,old,re.S);assert q==re.findall(pattern,new,re.S);assert q
        proposed[p]=new;originals[p]=[x[0] for x in q]
    rt.query_record(ROOT,TASK);plan=rt.plan(ROOT,profile='research',task_ids=[TASK]);assert set(plan['review_required'])<={TASK,'R-MO3-MS05-NONLEAF-20260924','R-MO3-BIAS-REGRESSION-20260924'} and not plan['hydration_diagnostics']['query_first_promoted']
    (HERE/'checkpoint-plan.json').write_bytes(rt.dump(plan))
    # Only exact, reviewed current report edits may refresh old pins. Frozen runs remain untouched.
    for id,r in s['records'].items():
        for p,v in list(r.get('source_hashes',{}).items()):
            if p in CHANGED and v!=sha(p):
                assert id==TASK or id.startswith('R-MO3-')
                baseline=subprocess.check_output(['git','show','HEAD:'+p],cwd=ROOT)
                assert hashlib.sha256(baseline).hexdigest()==v
                r['source_hashes'][p]=sha(p)
                r['revalidation']='Final source-first review: exact owned editorial status propagation only; original mathematical/source scope and immutable runs unchanged. See execution014.'
    ev=[REPORT,EXEC,AUDIT,OWN+'交付说明.md',OWN+'结论账本.md']+[OWN+'证据/FINAL/'+n for n in ['ESSAY-006-BEFORE.txt','ESSAY-006-PROPOSED.txt','ESSAY-008-BEFORE.txt','ESSAY-008-PROPOSED.txt','RECOVERY.json']]
    hashes={p:sha(p) for p in ev};hashes.update({p:hashlib.sha256(t.encode()).hexdigest() for p,t in proposed.items()})
    deps=list(s['records'][TASK]['depends_on'])
    s['records'][RID]=dict(kind='result',path=REPORT,lifecycle_status='CLOSED',status='RESEARCH_OBLIGATIONS_CLOSED_WITH_SCOPE',evidence_status='FOUR_NATIVE_PACKAGES_AND_NAMED_SOURCE_REVIEW / NO_QUALIFIED_REALITY_HIT / DELIVERY_SEAL_SEPARATE',depends_on=deps,dependency_semantics='verification_staleness',full_sources=ev+list(proposed),source_hashes=hashes,scope='Goal5/6 research obligations reconciled in execution014; no global HoTT completeness or nonexistence theorem. Final byte seal is a later operation with its own immutable receipt; B not performed.')
    task=s['records'][TASK];task.update(lifecycle_status='CLOSED',status='RESEARCH_COMPLETE_SEAL_RECEIPT_REQUIRED',evidence_status='ROUND_COMPLETE_NO_QUALIFIED_HIT_CONDITIONAL_ON_VERIFIED_DELIVERY_SEAL',full_sources=['goal-6.md','goal-5.md',REPORT,EXEC,AUDIT],scope='Research phase closed; host completion requires actual final-001 seal/verify after subject commit. Missing/invalid seal means delivery still incomplete.',revalidation='Final current-role/highest503 full reload; complete core48 and essay9 source-first reread, per-KC review, exact math scope and accepted obligations reconciled. Essay006/008 AI-only corrections preserve quotes. Research completion is not B audit pass.')
    task['resolution']={'evidence':[REPORT,EXEC,AUDIT],'reason':'All accepted research obligations reconciled in execution014 with bounded evidence; research phase closed. Subsequent actual SEAL/verify is separately required for host completion; B remains independent.'}
    task['depends_on']=[RID];task['source_hashes'].update(hashes)
    for p in CHANGED:task['source_hashes'][p]=sha(p)
    rev=s['revision']+1;s['revision']=rev;s['latest_session']=SID
    msg=f'MO3研究义务已按执行014逐项结案，C327–341与source/有限运行各保范围；本轮无合格现实相对命中。006/008解释纠偏保原文。交付末步由第三轮机器统观/Session-A/交付/final-001/SEAL.json及verify拥有：若有效则交用户B独立审计；若缺失/失败则继续封存，不重开旧研究队列。revision{rev}，B未审。'
    nxt='Check final-001 SEAL and verify receipt. If absent or invalid, finish exact subject commit, seal and verify. If valid, hand fixed input to user-arranged B; do not restart research or claim B passed. Only a new material finding or user instruction reopens a research item.'
    s['execution_control'].update(current_phase='MO3_RESEARCH_CLOSED_DELIVERY_SEAL',status='MO3_SEAL_RECEIPT_REQUIRED',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_completion_eligible=False,app_goal_status_observed='active',completion_eligibility_scope='Observed at this pre-seal checkpoint only. Subsequent actual SEAL+verify closes delivery; host Goal status is owned by host tool, no recursive post-seal research checkpoint required.')
    s['execution_control']['second_phase_status']='MO3_RESEARCH_CLOSED / DELIVERY_SEAL_RECEIPT_REQUIRED / OLD_006_FIRST_PASS_HISTORICAL'
    s['projection']['status']='MO3_RESEARCH_CLOSED / NO_QUALIFIED_HIT / SEAL_RECEIPT_REQUIRED'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='FINAL_RESEARCH_RECONCILIATION_AND_AI_EXPOSITION_CORRECTION',depends_on=[],related_records=[TASK,RID],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']])
    docs={p:edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];edit.replace_in_shard(docs['MEMORY.md'],mp,old,msg)
    for p,t in proposed.items():docs['扩展认知.md']['shards'][p]=t
    edit.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：完成研究全项对账及006/008 AI解释纠偏，原文不变；交付末步按独立SEAL/verify事实，B未审；revision{rev}。\n')
    for p,kind,id in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p],'source_state_revision: 280',f'source_state_revision: {rev}');edit.replace_in_index(docs[p],f'projection_generation: 20260924-{kind}-280',f'projection_generation: 20260924-{kind}-{rev}')
        docs[p]['index_text']=docs[p]['index_text'].replace('MO3_BIAS_COMPLETE_ROUND_INCOMPLETE','MO3_RESEARCH_CLOSED_SEAL_RECEIPT_REQUIRED')
        s['records'][id].update(projection_generation=f'20260924-{kind}-{rev}',semantic_status='MO3_RESEARCH_CLOSED_SEAL_RECEIPT_REQUIRED',scope='Research obligations closed with scope; final byte delivery checked through SEAL/verify. No qualified reality hit or B pass.')
    dp='方向追踪/002 - 治理与用户方向.md';docs['方向追踪.md']['shards'][dp]=re.sub(r'^\| `DIR-U-MO3-GOVERNED` .*$',f'| `DIR-U-MO3-GOVERNED` | 第三轮递归多尺度与针对性过程 | 用户Goal1.2、Goal6-MS01–06、KC2/40/44–48 | `RESEARCH_CLOSED / SEAL_RECEIPT_REQUIRED` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-FINAL-SYNTHESIS` | 核实际新seal；有效后交用户B，不自动新开研究 | {REPORT}；revision{rev} |',docs['方向追踪.md']['shards'][dp],flags=re.M)
    edit.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-MO3-FINAL-SYNTHESIS` | 第三轮研究综合及交付条件 | `DIR-U-MO3-GOVERNED` | 四原生包、具名非叶、方法控制及最终源回读 | `RESEARCH_COMPLETE_WITH_SCOPE` | 本轮无合格现实相对命中；精确边界与正常构造 | 不认证全理论或B；交付另核SEAL/verify | {REPORT}；{EXEC}；revision{rev} |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^17\. MO3-GOVERNED-A.*$','17. MO3-GOVERNED-A研究义务按最终报告/执行014结案；交付末步核Session-A/交付/final-001/SEAL.json和verify，缺失则仅继续封存，有效则交用户B。现实合格命中/全理论翻译/扩展元理论/长期行为未知保持；B未审，不因未知自动复活旧队列。',docs['全景视野.md']['shards'][pp],flags=re.M)
    files=[row for d in docs.values() for row in edit.payload_rows(d,ROOT)];seen={x['path'] for x in files}
    for p in rt.MUTABLE:
        if p in seen:continue
        body=(ROOT/p).read_text()
        if p==rt.STATE:body=rt.dump(s).decode()
        elif p.endswith(('FRONTIER.md','RESUME.md')):assert old in body;body=body.replace(old,msg,1)
        files.append(dict(path=p,expected_sha256=sha(p),text=body))
    a=edit.load(ROOT,AUDIT);audit='\n\n'.join(['# '+SID+' 兼容全量审计','- identity: '+s['current_core']['generation']+' / 48 KC']+[l for l in a['index_text'].splitlines() if re.match(r'^- (core_change|direction_change|panorama_change|essay_change|update_decision|cross_conflicts|unresolved):',l)]+['独占语义分片：'+AUDIT+'；兼容writer只原子写首层bundle。']+list(a['shards'].values()))+'\n';assert rt._audit_v1_kc_rows(audit)==[f'KC-{i:06d}' for i in range(1,49)]
    session=f'''# {SID}

- host: codex-desktop
- model: Astra（用户选择；不作后端指纹认证）
- tier: T3
- role: RESEARCH_GENERATION / sole canonical integrator
- thread: 01a0d1bd-c44d-7261-9a37-45bc5fbe87a8
- load_receipt: {OWN}证据/FINAL/RECOVERY.json；最高503/core441/扩展9片本次全文，W0四件套/STATE及自身差分复认，33后像核验。
- report: {REPORT}
- semantic_audit: {AUDIT}
- status: RESEARCH_COMPLETE_WITH_SCOPE / DELIVERY_SEAL_RECEIPT_REQUIRED
- next: {nxt}
- unknowns: 见最终报告§5；B未审，writer分片兼容缺口保留。

|element_usage|本次用途/边界|
|---|---|
|source-first|查006/008残留加码，原文不改|
|proof/run/index|精确复用四包，不增加定理|
|逐层/逐结论|高优先义务真实对账，不以计数自证|
|canonical/seal|研究与后续字节交付分步，不伪造未来收据|

reflection=no-plan-change；影响差分见执行014。无Sub Agent、新Session、push/tag、全局配置或历史改写。
'''
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],selected_existing_proofs=deps[:4],validation_owner=OWN+'证据/FINAL/validation',original_quote_blocks_unchanged=originals,core_sha256=s['current_core']['core_sha256'],delivery_gate='SEAL and verify after subject commit, not yet asserted by this checkpoint')
    files += [dict(path=BASE+n,expected_sha256=None,text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[TASK],authorization='用户MO3本轮研究/必要owner纠偏/canonical写回与精确本地提交授权；不改core原文、历史或全局配置。',files=files)
    (HERE/'checkpoint-payload.json').write_bytes(rt.dump(payload));res=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (HERE/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(rt.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
