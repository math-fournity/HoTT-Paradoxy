#!/usr/bin/env python3
"""Apply the bounded bias review and corrected AI exposition atomically."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,re,sys
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
OWN='第三轮机器统观/Session-A/';TASK='MO3-GOVERNED-A';RID='R-MO3-BIAS-REGRESSION-20260924';SID='S-RES-20260924-MO3-A-BIAS';BASE=f'.codex/research/hott/sessions/{SID}/'
REPORT=OWN+'执行记录/013 - 偏差回归与解释层纠偏.md';METHOD=OWN+'方法与偏差复测/004 - 原意保持与量化表达的混合回归.md';AUDIT=OWN+'审计/BIAS/CORE_COGNITION_AUDIT.md';ESSAY='扩展认知/007 - AI数学的两件事：助力、阻力与符号翻转.md'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    spec=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(spec);spec.loader.exec_module(rt);sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as edit
    s=json.loads((ROOT/rt.STATE).read_text());assert s['revision']==279 and SID not in s['records'] and RID not in s['records'];h=json.loads((ROOT/rt.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    methods=json.loads((HERE.parent/'MS01/method-inputs/MANIFEST.json').read_text());assert all(sha(x['source'])==x['sha256'] for x in methods['rows'])
    inputs=json.loads((HERE/'INPUT-MANIFEST.json').read_text());assert inputs['before_responses'] and not inputs['blind'];assert all(sha(x['path'])==x['sha256'] for x in inputs['rows'])
    score=json.loads((HERE/'scoring-run-001/score.json').read_text());assert score['case_count']==18 and score['label_agreement']==18 and not score['malformed_records']
    run=json.loads((HERE/'scoring-run-001/RUN.json').read_text());assert run['exit_code']==0 and run['responses_sha256']==sha(OWN+'证据/BIAS/RESPONSES.json') and run['script_sha256']==sha(OWN+'证据/BIAS/score_records.py')
    assert sha(ESSAY)==sha(OWN+'证据/BIAS/inputs/ESSAY-007-BEFORE.md')
    proposed=(HERE/'ESSAY-007-PROPOSED.txt').read_text();pattern=r'<!-- original:(KC-\d+):begin -->(.*?)<!-- original:\1:end -->';assert re.findall(pattern,(ROOT/ESSAY).read_text(),re.S)==re.findall(pattern,proposed,re.S)
    rt.query_record(ROOT,TASK);plan=rt.plan(ROOT,profile='research',task_ids=[TASK]);assert set(plan['review_required'])<={TASK} and not plan['hydration_diagnostics']['query_first_promoted'];(HERE/'checkpoint-plan.json').write_bytes(rt.dump(plan))
    ev=[REPORT,METHOD,AUDIT]+[OWN+'证据/BIAS/'+n for n in ['PROTOCOL.md','INPUT-MANIFEST.json','CASES.json','ORACLE.json','RESPONSES.json','SEMANTIC-REVIEW.md','LATE-INPUT.md','LATE-INPUT-FREEZE.json','LATE-RESPONSE.md','scoring-run-001/RUN.json','scoring-run-001/score.json','ESSAY-007-PROPOSED.txt']]
    hashes={p:sha(p) for p in ev};hashes[ESSAY]=hashlib.sha256(proposed.encode()).hexdigest()
    s['records'][RID]=dict(kind='result',path=METHOD,lifecycle_status='CLOSED',status='PROMPTED_BIAS_REGRESSION_COMPLETE_WITH_SCOPE',evidence_status='EIGHTEEN_MIXED_RECORDS_AND_LATE_TRANSFER / SAME_A_NOT_BLIND / EXPOSITION_CORRECTED / FUTURE_BEHAVIOR_NOT_CERTIFIED',depends_on=['R-MO3-MS05-NONLEAF-20260924'],dependency_semantics='verification_staleness',related_records=[TASK],full_sources=ev+[ESSAY],source_hashes=hashes,scope='Known circle/origin substitution and help/resistance quantification errors mixed with legitimate refinements/hypotheses, new terms and later self-generated paragraphs. Same A designed/responded/reviewed; score checks labels, not independent semantics. Three user quote blocks unchanged; no new mathematical claim.')
    task=s['records'][TASK];task['depends_on'].append(RID);task.update(status='BIAS_COMPLETE_FINAL_AUDIT_AND_SEAL_NEXT',evidence_status='SCOPED_RESEARCH_AND_FOUR_METHOD_CONTROLS / FINAL_AUDIT_SEAL_REMAIN / ROUND_INCOMPLETE',full_sources=['goal-6.md','goal-5.md',REPORT,AUDIT],scope='Full Goal5/Goal6: scoped research, named non-leaf/relations and four method-control families have evidence. Final conclusion/omission/completion audit and MS06 seal still required.',revalidation='Full highest503 and primary circle/KC41-43/47-48 actually re-read for bias unit. Frozen mixed cases and subsequent paragraphs evaluated with explicit same-A limits. Corrected only unsupported AI exposition in essay007; original user quote blocks/core/methods unchanged. Known owned method/report pins refreshed.')
    for p in [REPORT,METHOD,AUDIT,OWN+'方法与偏差复测.md']:task['source_hashes'][p]=sha(p)
    task['source_hashes'][ESSAY]=hashes[ESSAY]
    rev=s['revision']+1;s['revision']=rev;s['latest_session']=SID
    message=f'MO3专门偏差回归已执行18份混合表达与后续新词/旧摘要检查；同A有提示自测，不认证未来能力。扩展007已限定AI新增量化/机械免偏差解释，三原文块与core不变。研究及具名非叶/关系和四类方法控制均有范围实物；下一最终逐结论/遗漏/完成审计和MS06 seal。ROUND_INCOMPLETE；revision{rev}。'
    nxt='Perform final source-first conclusion and omission audit, reconcile every Goal5/Goal6 obligation and current report, then build the exact delivery dependency path list including complete logical shards, method versions, source/proof/run/index/checkpoint assets. Commit only owned scope, seal a new generation and verify it for independent B. Do not mark the host Goal complete until the actual full deliverable passes; no claim of B audit pass.'
    s['execution_control'].update(current_phase='MO3_W5_FINAL_AUDIT_AND_SEAL',status='MO3_ACTIVE_ROUND_INCOMPLETE',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_completion_eligible=False,app_goal_status_observed='active');s['projection']['status']='MO3_BIAS_COMPLETE / FINAL_AUDIT_SEAL_REMAIN / ROUND_INCOMPLETE'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='PROMPTED_MIXED_BIAS_REVIEW_AND_EXPOSITION_CORRECTION',depends_on=[],related_records=[TASK,RID],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']])
    docs={p:edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']};mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];edit.replace_in_shard(docs['MEMORY.md'],mp,old,message)
    docs['扩展认知.md']['shards'][ESSAY]=proposed
    edit.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：18混合表达/后续文本偏差回归及007AI解释纠偏完成范围，原文不改；非独立/盲/永久能力认证。下一最终审计与MS06；revision{rev}。\n')
    for p,kind,rid in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p],'source_state_revision: 279',f'source_state_revision: {rev}');edit.replace_in_index(docs[p],f'projection_generation: 20260924-{kind}-279',f'projection_generation: 20260924-{kind}-{rev}');docs[p]['index_text']=docs[p]['index_text'].replace('MO3_MS05_NAMED_SCOPE_ROUND_INCOMPLETE','MO3_BIAS_COMPLETE_ROUND_INCOMPLETE');s['records'][rid].update(projection_generation=f'20260924-{kind}-{rev}',semantic_status='MO3_BIAS_COMPLETE_ROUND_INCOMPLETE',scope='Prompted mixed bias review and bounded source correction; final audit/seal incomplete.')
    dp='方向追踪/002 - 治理与用户方向.md';docs['方向追踪.md']['shards'][dp]=re.sub(r'^\| `DIR-U-MO3-GOVERNED` .*$',f'| `DIR-U-MO3-GOVERNED` | 第三轮递归多尺度与针对性过程 | 用户Goal1.2、Goal6-MS01–06、KC2/40/44–48 | `ACTIVE / FINAL_AUDIT_SEAL_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-C01-STAGE-COLIMIT`, `OUT-MO3-MS04-CONTROLS`, `OUT-MO3-C04-BOUQUET-ORDER`, `OUT-MO3-C02-FINITE-COVER`, `OUT-MO3-R13-MARGIN`, `OUT-MO3-R09-SUBSTITUTION`, `OUT-MO3-MS05-NONLEAF`, `OUT-MO3-BIAS-REGRESSION` | 最终逐结论/遗漏/完成审计及封存 | {REPORT}；revision{rev} |',docs['方向追踪.md']['shards'][dp],flags=re.M)
    edit.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-MO3-BIAS-REGRESSION` | 原意/量化混合回归与解释层修正 | `DIR-U-MO3-GOVERNED` | 18固定表达、后续文本及原文块对账 | `PROMPTED_SELF_REVIEW_WITH_SCOPE` | 正常精化/假说与替换/加码分别处置，007正文纠偏 | 不认证未来能力/独立B/全轮完成 | {METHOD}；{REPORT}；revision{rev} |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^17\. MO3-GOVERNED-A.*$','17. MO3-GOVERNED-A：研究/具名非叶与四类方法控制已有范围实物，偏差回归及007解释层修正已执行；最终逐结论/遗漏/完成审计、精确依赖清单和MS06 seal仍未完成。B独立审计未执行，开放世界及各源/native/现实边界保持。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[row for d in docs.values() for row in edit.payload_rows(d,ROOT)];seen={x['path'] for x in rows}
    for p in rt.MUTABLE:
        if p in seen:continue
        body=(ROOT/p).read_text()
        if p==rt.STATE:body=rt.dump(s).decode()
        elif p.endswith(('FRONTIER.md','RESUME.md')):assert old in body;body=body.replace(old,message,1)
        rows.append(dict(path=p,expected_sha256=sha(p),text=body))
    a=edit.load(ROOT,AUDIT);audit='\n\n'.join(['# '+SID+' 兼容完整审计','- identity: '+s['current_core']['generation']+' / 48 KC']+[l for l in a['index_text'].splitlines() if re.match(r'^- (core_change|direction_change|panorama_change|essay_change|update_decision|cross_conflicts|unresolved):',l)]+['分片语义原件：'+AUDIT+'；嵌套writer边界保留。']+list(a['shards'].values())).rstrip()+'\n';assert rt._audit_v1_kc_rows(audit)==[f'KC-{i:06d}' for i in range(1,49)]
    session=f'''# {SID}

- host: codex-desktop
- model: Astra（用户指定；不认证后端指纹）
- tier: T3
- role: RESEARCH_GENERATION / sole canonical integrator / method qualification
- thread: 01a0d1bd-c44d-7261-9a37-45bc5fbe87a8
- load_receipt: {OWN}证据/BIAS/PROTOCOL.md和INPUT-MANIFEST.json；最高指示503、本次相关用户全文/007全文；四件套/STATE原完整加载及自身至279差分按PROTOCOL复认，279后像无漂移。
- report: {REPORT}
- semantic_audit: {AUDIT}
- status: BIAS_COMPLETE_WITH_SCOPE / ROUND_INCOMPLETE
- next: {nxt}
- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；原生/来源/现实及旧registry余项保持。

|element_usage|实际用途与边界|
|---|---|
|用户原文/最高指示|保原问并限制AI加强，不先辩倒研究方向|
|冻结题/正常控制|18题混合，评分仅计录入/标签|
|后续生成|常规核验后换词产物，非永久能力认证|
|canonical/48KC|应用AI解释纠偏，原文块不改|

reflection=no-plan-change。T04/13/22/24/26更新研究控制/解释/状态；核心原文、Goal/Skill/全局配置/方法验收及其余无变化职责不改。无新数学claim、Sub Agent、新Session、push/tag或历史改写。
'''
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],scoring_run=OWN+'证据/BIAS/scoring-run-001/RUN.json',scope='Frozen record/label agreement; semantic review is same-A and bounded.',input_manifest=OWN+'证据/BIAS/INPUT-MANIFEST.json',exposition_owner=ESSAY,user_quote_blocks_unchanged=['KC-000041','KC-000042','KC-000043'])
    rows += [dict(path=BASE+n,expected_sha256=None,text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[TASK],authorization='用户本轮MO3唯一integrator、研究/必要owner纠偏与canonical写回授权；不改core原文或全局配置。',files=rows);(HERE/'checkpoint-payload.json').write_bytes(rt.dump(payload));res=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply);(HERE/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(rt.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
