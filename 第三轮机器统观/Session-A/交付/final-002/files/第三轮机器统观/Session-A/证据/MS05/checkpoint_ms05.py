#!/usr/bin/env python3
"""One-shot integration of named non-leaf reviews and finite R05 observations."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,re,sys

ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
OWN='第三轮机器统观/Session-A/';TASK='MO3-GOVERNED-A'
RID='R-MO3-MS05-NONLEAF-20260924';SID='S-RES-20260924-MO3-A-MS05'
BASE=f'.codex/research/hott/sessions/{SID}/'
REPORT=OWN+'执行记录/012 - 非叶问题与反馈关系的独立结案.md'
COVER=OWN+'覆盖与关系/005 - 已接受非叶问题的独立对账.md'
AUDIT=OWN+'审计/MS05/CORE_COGNITION_AUDIT.md'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--apply',action='store_true');args=parser.parse_args()
    spec=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(spec);spec.loader.exec_module(rt)
    sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as edit
    s=json.loads((ROOT/rt.STATE).read_text());assert s['revision']==278 and SID not in s['records'] and RID not in s['records']
    h=json.loads((ROOT/rt.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    methods=json.loads((HERE.parent/'MS01/method-inputs/MANIFEST.json').read_text());assert all(sha(x['source'])==x['sha256'] for x in methods['rows'])
    source=json.loads((HERE/'source/SOURCE-MANIFEST.json').read_text());assert all(sha(x['path'])==x['sha256'] for x in source['sources'])
    run=json.loads((HERE/'feedback-run-002/RUN.json').read_text());obs=json.loads((HERE/'feedback-run-002/result.json').read_text())
    assert run['exit_code']==0 and obs['all_expected'] and run['source_sha256']==sha(OWN+'证据/MS05/run_feedback_scope.py')
    versions=json.loads((HERE/'native-reuse-001/RESULT.json').read_text());assert len(versions['checks'])==4 and all(x['exit']==0 for x in versions['checks'])
    cov=json.loads((HERE/'READING-COVERAGE.json').read_text());assert len(cov['named_nonleaf_ids'])==24 and len(cov['relation_ids'])==13
    rt.query_record(ROOT,TASK);plan=rt.plan(ROOT,profile='research',task_ids=[TASK]);assert set(plan['review_required'])<={TASK} and not plan['hydration_diagnostics']['query_first_promoted']
    (HERE/'checkpoint-plan.json').write_bytes(rt.dump(plan))
    ev=[COVER,REPORT,OWN+'证据/MS05/GENERATION.md',OWN+'证据/MS05/R05-RESULT.md',OWN+'证据/MS05/run_feedback_scope.py',OWN+'证据/MS05/feedback-run-002/RUN.json',OWN+'证据/MS05/feedback-run-002/result.json',OWN+'证据/MS05/native-reuse-001/RESULT.json',OWN+'证据/MS05/READING-COVERAGE.json',OWN+'证据/MS05/source/SOURCE-MANIFEST.json']
    deps=list(s['records'][TASK]['depends_on'])
    s['records'][RID]=dict(kind='result',path=COVER,lifecycle_status='CLOSED',status='NAMED_NONLEAF_REVIEW_COMPLETE_WITH_SCOPE',evidence_status='SEMANTICALLY_REVIEWED / FINITE_R05_EXECUTED / EXISTING_NATIVE_PACKAGES_REVALIDATED / REALITY_MISMATCH_NOT_ESTABLISHED',depends_on=deps,dependency_semantics='verification_staleness',related_records=[TASK],full_sources=ev,source_hashes={p:sha(p) for p in ev},binary_sources=source['sources'],binary_sources_require_explicit_hash_recheck=True,scope='24 accepted domain non-leaf questions, G1-G3, 13 registered relations and seven extension interfaces reviewed with individual limits. Finite R05 controller executed; no native/infinite feedback theorem. SOURCE results and open full metatheory/physical bridges remain qualified; no global coverage/no-paradox claim.')
    task=s['records'][TASK];task['depends_on'].append(RID);task.update(status='MS05_NAMED_SCOPE_COMPLETE_BIAS_NEXT',evidence_status='SCOPED_NATIVE_AND_SOURCE_RESULTS / MS05_NAMED_SCOPE_COMPLETE / BIAS_FINAL_AUDIT_SEAL_REMAIN / ROUND_INCOMPLETE',full_sources=['goal-6.md','goal-5.md',REPORT,AUDIT],scope='Full Goal5 v1.2/Goal6. Named MS02/MS05 non-leaf and relation adjudications now have evidence; mandatory bias regression, final omission/completion/conclusion audit and MS06 seal remain.',revalidation='Full highest503/KC47-48 reload for MS05; original 35 question/relationship source read; finite R05 feedback and fixed extension pages actually inspected. Corrected stale current C04/C02/R09 wording only in owned reports. Core/method inputs unchanged. No new mathematical claim.')
    owned_delta=[REPORT,AUDIT,COVER,OWN+'覆盖与关系/001 - 理论范围与五尺度首遍.md',OWN+'覆盖与关系/002 - 全景重新呈现与过程关系.md',OWN+'覆盖与关系/003 - 首遍语义裁决与实际验证选择.md',OWN+'方法与偏差复测/003 - 有序运输的异机制留出.md']
    for p in owned_delta:task['source_hashes'][p]=sha(p)
    rev=s['revision']+1;s['revision']=rev;s['latest_session']=SID
    message=f'MO3 MS05已逐项对账24领域非叶、G1–G3、13关系/7扩展；R05读取完成再扩图的有限controller已实际运行，源/软件/native/现实边界分列。四个既有native包所选版本检查通过；无新数学claim或合格现实命中。下一专门偏差回归、最终遗漏/结论/完成审计与MS06封存。ROUND_INCOMPLETE；revision{rev}。'
    nxt='Execute the dedicated Goal5 section7(4) bias regression: preserve original circle and help/resistance meaning, mix legitimate refinements and quantitative hypotheses with unsupported substitutions/assertions, include novel-term transfer and later generated paragraph recurrence checks. Then audit all Goal5/6 obligations, conclusion propagation, omission and exact delivery dependency closure before MS06 seal. Do not expand already answered controller or interval examples.'
    s['execution_control'].update(current_phase='MO3_W4_BIAS_REGRESSION',status='MO3_ACTIVE_ROUND_INCOMPLETE',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_completion_eligible=False,app_goal_status_observed='active')
    s['projection']['status']='MO3_MS05_NAMED_SCOPE / BIAS_SEAL_REMAIN / ROUND_INCOMPLETE'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='NONLEAF_SOURCE_SCOPE_AND_FINITE_FEEDBACK',depends_on=[],related_records=[TASK,RID],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']])
    docs={p:edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']};mp='MEMORY/001 - 当前执行队列.md'
    old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0]
    edit.replace_in_shard(docs['MEMORY.md'],mp,old,message)
    edit.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：具名24+3非叶、13关系/7扩展对账及R05有限反馈完成范围；四包所选复核通过，SOURCE与原生等级不混。下一偏差回归/最终审计/MS06；revision{rev}。\n')
    for p,kind,rid in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p],'source_state_revision: 278',f'source_state_revision: {rev}');edit.replace_in_index(docs[p],f'projection_generation: 20260924-{kind}-278',f'projection_generation: 20260924-{kind}-{rev}')
        docs[p]['index_text']=docs[p]['index_text'].replace('MO3_R09_SOURCE_SCOPE_ROUND_INCOMPLETE','MO3_MS05_NAMED_SCOPE_ROUND_INCOMPLETE')
        s['records'][rid].update(projection_generation=f'20260924-{kind}-{rev}',semantic_status='MO3_MS05_NAMED_SCOPE_ROUND_INCOMPLETE',scope='Named non-leaf/relations reviewed; bias/final audit/seal incomplete.')
    dp='方向追踪/002 - 治理与用户方向.md'
    docs['方向追踪.md']['shards'][dp]=re.sub(r'^\| `DIR-U-MO3-GOVERNED` .*$',f'| `DIR-U-MO3-GOVERNED` | 第三轮递归多尺度与针对性过程 | 用户Goal1.2、Goal6-MS01–06、KC2/40/44–48 | `ACTIVE / BIAS_FINAL_AUDIT_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-C01-STAGE-COLIMIT`, `OUT-MO3-MS04-CONTROLS`, `OUT-MO3-C04-BOUQUET-ORDER`, `OUT-MO3-C02-FINITE-COVER`, `OUT-MO3-R13-MARGIN`, `OUT-MO3-R09-SUBSTITUTION`, `OUT-MO3-MS05-NONLEAF` | 专门偏差回归、最终审计与封存 | {REPORT}；revision{rev} |',docs['方向追踪.md']['shards'][dp],flags=re.M)
    edit.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-MO3-MS05-NONLEAF` | 具名非叶/关系独立对账 | `DIR-U-MO3-GOVERNED` | 24+3问题、13关系/7扩展，R05有限实跑及四包复核 | `SOURCE_AND_NATIVE_SCOPED / FINITE_FEEDBACK` | 子项资格与父目标逐项对应，旧current漂移原位修正 | 非全理论/全模型完备；偏差/封存未完 | {COVER}；{REPORT}；revision{rev} |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^17\. MO3-GOVERNED-A.*$','17. MO3-GOVERNED-A：既有native/source单元、MS04及具名MS02/MS05非叶/关系均有范围实物；R05有限反馈另已运行，非无限/native桥。专门偏差回归、最终遗漏/逐结论/完成审计和MS06仍未完；所有更强未证命题继续限制结论。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[r for d in docs.values() for r in edit.payload_rows(d,ROOT)];seen={x['path'] for x in rows}
    for p in rt.MUTABLE:
        if p in seen:continue
        body=(ROOT/p).read_text()
        if p==rt.STATE:body=rt.dump(s).decode()
        elif p.endswith(('FRONTIER.md','RESUME.md')):assert old in body;body=body.replace(old,message,1)
        rows.append(dict(path=p,expected_sha256=sha(p),text=body))
    a=edit.load(ROOT,AUDIT);audit='\n\n'.join(['# '+SID+' 兼容完整审计','- identity: '+s['current_core']['generation']+' / 48 KC']+[l for l in a['index_text'].splitlines() if re.match(r'^- (core_change|direction_change|panorama_change|essay_change|update_decision|cross_conflicts|unresolved):',l)]+['分片语义原件：'+AUDIT+'；嵌套writer缺口保留。']+list(a['shards'].values())).rstrip()+'\n'
    assert rt._audit_v1_kc_rows(audit)==[f'KC-{i:06d}' for i in range(1,49)]
    session=f'''# {SID}

- host: codex-desktop
- model: Astra（用户指定，不认证后端指纹）
- tier: T3
- role: RESEARCH_GENERATION / sole canonical integrator
- thread: 01a0d1bd-c44d-7261-9a37-45bc5fbe87a8
- load_receipt: {OWN}证据/MS05/GENERATION.md与READING-COVERAGE.json；本单元最高指示503/KC47–48全文，旧四件套与STATE268全文及自身269–278差分按PROTOCOL复认，不伪称本单元重读全STATE。
- report: {REPORT}
- semantic_audit: {AUDIT}
- status: MS05_NAMED_SCOPE_COMPLETE / ROUND_INCOMPLETE
- next: {nxt}
- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；PDF需显式hash重核，runtime文本水合不自动追踪二进制。

|element_usage|实际用途与限制|
|---|---|
|最高指示/原意|父层独立提问与有靶反馈过程|
|源码/原典|具体接口来源，不把论文全元理论说成核证|
|反馈软件|有限读完成/扩图/冻结对照，非原生HIT|
|旧native四包|所选版本闭合复核，非新kernel运行|
|全量KC/canonical|48条自审与current状态，不自证B通过|

reflection=no-plan-change。T01/04/13/22/24/26的本轮研究结果/状态更新；core、方法、配置、schema、发布及其余无变化职责不改。无新数学claim、Sub Agent、新Session、push/tag或历史原件重写。
'''
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],software_run=OWN+'证据/MS05/feedback-run-002/RUN.json',prior_software_run=OWN+'证据/MS05/feedback-run-001/RUN.json',native_reuse=OWN+'证据/MS05/native-reuse-001/RESULT.json',source_manifest=OWN+'证据/MS05/source/SOURCE-MANIFEST.json',scope='Named question review and finite controller, not global metatheory or infinite execution.')
    rows += [dict(path=BASE+n,expected_sha256=None,text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[TASK],authorization='用户当前MO3 Goal5/Goal6唯一integrator和精确本地写回授权，继续同轮研究。',files=rows)
    (HERE/'checkpoint-payload.json').write_bytes(rt.dump(payload));res=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (HERE/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(rt.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
