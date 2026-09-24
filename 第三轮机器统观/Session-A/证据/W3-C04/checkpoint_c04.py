#!/usr/bin/env python3
"""Register the exact C04 result and continue the existing MO3 parent queue."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, re, sys
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
OWN='第三轮机器统观/Session-A/';TASK='MO3-GOVERNED-A';RID='R-MO3-C04-BOUQUET-ORDER-20260924'
SID='S-RES-20260924-MO3-A-C04';BASE=f'.codex/research/hott/sessions/{SID}/'
REPORT=OWN+'执行记录/008 - 路径次序留出的生成与核证.md'
PROCESS=OWN+'过程与结果/002 - 双环路运输与状态复原.md'
AUDIT=OWN+'审计/W3-C04/CORE_COGNITION_AUDIT.md'
RUN='HoTT/verification/runs/20260924-MO3-BOUQUET-ORDER-001-02/'
FORMAL='HoTT/formal/mo3/bouquet-order/'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(sp);sp.loader.exec_module(rt)
    sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as edit
    s=json.loads((ROOT/rt.STATE).read_text());assert s['revision']==274 and SID not in s['records'] and RID not in s['records']
    h=json.loads((ROOT/rt.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    methods=json.loads((HERE.parent/'MS01/method-inputs/MANIFEST.json').read_text());assert all(sha(x['source'])==x['sha256'] for x in methods['rows'])
    v=json.loads((HERE/'version-check/RESULT.json').read_text());assert v['subject_commit']=='b2599a4f4a6059d987f754683f2fb30395e75196' and v['checks'][0]['exit']==0
    checks=json.loads((HERE/'validation-001/RESULT.json').read_text());assert all(x['exit']==0 for x in checks['commands'][:2]) and not checks['builtin_drift'] and checks['wrong_order_expected_rejection']
    rt.query_record(ROOT,TASK);plan=rt.plan(ROOT,profile='research',task_ids=[TASK]);assert set(plan['review_required'])<={TASK} and not plan['hydration_diagnostics']['query_first_promoted'];(HERE/'checkpoint-plan.json').write_bytes(rt.dump(plan))
    evidence=[PROCESS,FORMAL+'BouquetOrder.agda',FORMAL+'README.md',FORMAL+'DEPENDENCY-AUDIT.json',RUN+'RUN.json',RUN+'source-manifest.json',RUN+'index-row-manifest.json',OWN+'证据/W3-C04/version-check/RESULT.json']
    s['records'][RID]=dict(kind='result',path=PROCESS,lifecycle_status='CLOSED',status='C04_NATIVE_ORDER_AND_RESTORE_COMPLETE_NOT_QUALIFIED_HOTT_HIT',evidence_status='FORMAL_CHECKED_WITH_SCOPE / SELECTED_PACKAGES_VERSION_CLOSED / IDEAL_TASK_CORRESPONDENCE / REALITY_MISMATCH_NOT_ESTABLISHED',depends_on=[],related_records=[TASK],full_sources=evidence,source_hashes={p:sha(p) for p in evidence},proof_id='MP-MO3-BOUQUET-ORDER-001',claim_ids=['C-331','C-332','C-333','C-334'],subject_commit=v['subject_commit'],scope='Fixed native Bouquet Bool family, two explicit actions, unequal ordered observations, same-family true inverse restoration and constant-family control. No physical circle/instrument, arbitrary family/path classification, HoTT inconsistency or global originality.')
    r=s['records'][TASK];r['depends_on'].append(RID);r['dependency_semantics']='verification_staleness'
    r.update(status='C04_NATIVE_HOLDOUT_COMPLETE_C02_NEXT',evidence_status='C01_AND_C04_EXACT_NATIVE_RESULTS / MS04_EXECUTED / HIGHER_LEVEL_AND_BIAS_REMAINDER / ROUND_INCOMPLETE',full_sources=['goal-6.md','goal-5.md',REPORT,AUDIT])
    pins=[REPORT,AUDIT,OWN+'覆盖与关系/002 - 全景重新呈现与过程关系.md',OWN+'覆盖与关系/003 - 首遍语义裁决与实际验证选择.md',OWN+'覆盖与关系/004 - 语义单元与联合条件.md',OWN+'方法与偏差复测.md']+[OWN+'方法与偏差复测/'+n for n in ['001 - C01真实来源重组与对照.md','002 - 联合条件与粒度失真控制.md','003 - 有序运输的异机制留出.md']]
    r['source_hashes'].update({p:sha(p) for p in pins});r['revalidation']='C04 independently implemented after reloading all503 Highest Directive lines and KC47/48. Native run02 accepted C331-334, two evidence gates and selected Git closure passed. Controls preserve same task and actual inverse order; weaker endpoint-only interpretation is not attributed to core rules. Own coverage/method statuses updated; remaining accepted non-leaf questions, C02/R09, bias regression and seal not closed.'
    r['scope']='Full Goal5 v1.2/Goal6. C01 scoped qualification boundary and C04 native ordered action/ideal calibration normal result complete; real C01 regrouping and bounded method controls done. MS02/MS05 remainder, C02/R09, dedicated bias regression and MS06 still mandatory.'
    rev=s['revision']+1;s['revision']=rev;s['latest_session']=SID
    message=f'MO3 C04已原生核证并在b2599a4f版本闭合C331–334：同族两次序终标记不同，真正逆序恢复与常值族控制成功；该理想校准未构成HoTT失配。C01及MS04保持各自范围。下一C02有限原索引列表交付，再R09、其它非叶结案/偏差回归及MS06。ROUND_INCOMPLETE，无final seal；revision{rev}。'
    nxt='Execute C02 on actual enumerable rational intervals and the original finite-index-list Done: specify and implement exact cover checking/output, connect search to the actual interval task, and include meaningful native/normal controls without an artificial deadline. Then adjudicate R09 and all remaining accepted non-leaf questions (MS02/MS05), perform dedicated bias regression, reconcile full Goal5/6 obligations and seal MS06. Do not repeat C01/C04 without a new consumer or premise.'
    s['execution_control'].update(current_phase='MO3_W3_C02_FINITE_INDEX_DELIVERY',status='MO3_ACTIVE_ROUND_INCOMPLETE',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_completion_eligible=False,app_goal_status_observed='active')
    s['projection']['status']='MO3_C04_NATIVE_COMPLETE_WITH_SCOPE / C02_NEXT / ROUND_INCOMPLETE'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='C04_EXACT_NATIVE_AND_IDEAL_TASK_CHECKED',depends_on=[],related_records=[TASK,RID],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']])
    docs={p:edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']};mp='MEMORY/001 - 当前执行队列.md'
    old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];edit.replace_in_shard(docs['MEMORY.md'],mp,old,message)
    edit.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：C331–334原生同族有序运输/真实逆序/常值控制通过，subject b2599a4f。理想校准正常、无HoTT现实失配；G2只得该范围结果，C02/R09/非叶/偏差/封存继续。revision{rev}。\n')
    for p,kind,rid in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p],'source_state_revision: 274',f'source_state_revision: {rev}');edit.replace_in_index(docs[p],f'projection_generation: 20260924-{kind}-274',f'projection_generation: 20260924-{kind}-{rev}');docs[p]['index_text']=docs[p]['index_text'].replace('MO3_MS04_EXECUTED_WITH_SCOPE_ROUND_INCOMPLETE','MO3_C04_NATIVE_COMPLETE_WITH_SCOPE_ROUND_INCOMPLETE');s['records'][rid].update(projection_generation=f'20260924-{kind}-{rev}',semantic_status='MO3_C04_NATIVE_COMPLETE_WITH_SCOPE_ROUND_INCOMPLETE',scope='C04 exact native order/restoration and ideal-task normal result; C02/R09/non-leaf/bias/seal obligations remain.')
    dp='方向追踪/002 - 治理与用户方向.md';docs['方向追踪.md']['shards'][dp]=re.sub(r'^\| `DIR-U-MO3-GOVERNED` .*$',f'| `DIR-U-MO3-GOVERNED` | 第三轮递归多尺度与针对性过程 | 用户Goal1.2、Goal6-MS01–06、KC2/40/44–48 | `ACTIVE / C02_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-C01-STAGE-COLIMIT`, `OUT-MO3-MS04-CONTROLS`, `OUT-MO3-C04-BOUQUET-ORDER` | C02实际有限索引交付、R09与非叶/偏差回归 | {REPORT}；revision{rev} |',docs['方向追踪.md']['shards'][dp],flags=re.M)
    edit.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-MO3-C04-BOUQUET-ORDER` | 同族有序运输与真实逆序 | `DIR-U-MO3-GOVERNED` | C331–334/source/run02/index及subject b2599a4f | `FORMAL_CHECKED_WITH_SCOPE / IDEAL_TASK_NORMAL` | 端点同一不替完整作用；原生理论保序并完成真实逆向 | 非物理圆环、非HoTT独有/缺陷；其它非叶及C02/R09未结 | {PROCESS}；{REPORT}；revision{rev} |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^17\. MO3-GOVERNED-A.*$','17. MO3-GOVERNED-A：MS01、C01、MS04指定控制和C04原生异机制判别完成各自范围；MS02其它域单元、MS05全部非叶结案、C02有限索引交付、R09、专门偏差回归、MS06最终封存仍未完成。两个实例不抵全域，本轮仍无合格现实相对命中。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for d in docs.values():rows+=edit.payload_rows(d,ROOT)
    seen={x['path'] for x in rows}
    for p in rt.MUTABLE:
        if p in seen:continue
        content=(ROOT/p).read_text()
        if p==rt.STATE:content=rt.dump(s).decode()
        elif p.endswith(('FRONTIER.md','RESUME.md')):assert old in content;content=content.replace(old,message,1)
        rows.append(dict(path=p,expected_sha256=sha(p),text=content))
    a=edit.load(ROOT,AUDIT);legacy=['# '+SID+' 兼容完整审计','- identity: '+s['current_core']['generation']+' / 48 KC']+[l for l in a['index_text'].splitlines() if re.match(r'^- (core_change|direction_change|panorama_change|essay_change|update_decision|cross_conflicts|unresolved):',l)]+['分片语义原件：'+AUDIT+'；嵌套writer缺口保留。']+list(a['shards'].values());audit='\n\n'.join(legacy).rstrip()+'\n';assert rt._audit_v1_kc_rows(audit)==[f'KC-{i:06d}' for i in range(1,49)]
    session=f'# {SID}\n\n- host: codex-desktop\n- model: Astra（用户选择，不认证后端指纹）\n- tier: T3\n- role: RESEARCH_GENERATION / sole canonical integrator\n- load_receipt: {OWN}证据/W3-C04/source-read.json；新单元最高指示503行/KC47–48全文，STATE268全文及自身269–274差分，274 current后像无漂移。\n- status: C04_COMPLETE_WITH_SCOPE / ROUND_INCOMPLETE\n- report: {REPORT}\n- semantic_audit: {AUDIT}\n- subject_commit: {v["subject_commit"]}\n- next: {nxt}\n- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；旧Coq全registry错配非本包依赖。\n\n|element_usage|实际用途/边界|\n|---|---|\n|最高指示及原文|生成当前任务，14题/三呈现，非永久行为证明|\n|原生proof/run/index|精确四claim，真实错误/正常控制，非物理结果|\n|语义单元/现实桥|同族/路径/顺序/观察对应，父G2余项保留|\n|canonical审计|48KC与当前队列；嵌套分片原子缺口不伪修|\n\nreflection=no-plan-change；沿已接受异机制过程后转C02。T01/04/11/13/22/24/26新增证明/证据/状态，需求/全局方法/配置/schema/运维不改，其余组无变更。无Sub Agent、新Session、push/tag、core或历史原件修改。\n'
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=['C-331','C-332','C-333','C-334'],proof_id='MP-MO3-BOUQUET-ORDER-001',native_runs=['20260924-MO3-BOUQUET-ORDER-001-01','20260924-MO3-BOUQUET-ORDER-001-02','20260924-MO3-BOUQUET-ORDER-CONTROL-01'],validation=OWN+'证据/W3-C04/validation-001/RESULT.json',version_check=OWN+'证据/W3-C04/version-check/RESULT.json',scope='Exact native ordered actions and controls; ideal discrete task; no qualified HoTT mismatch.')
    rows += [dict(path=BASE+n,expected_sha256=None,text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[TASK],authorization='沿用户已恢复MO3唯一integrator、研究proof与精确checkpoint授权，保存本包实际结果并继续全部父义务。',files=rows);(HERE/'checkpoint-payload.json').write_bytes(rt.dump(payload));res=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply);(HERE/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(rt.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
