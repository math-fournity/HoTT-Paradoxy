#!/usr/bin/env python3
"""Persist the bounded C01 regrouping/control result via the canonical writer."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, re, sys

ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
OWN='第三轮机器统观/Session-A/'
SID='S-RES-20260924-MO3-A-MS04'
BASE=f'.codex/research/hott/sessions/{SID}/'
TASK='MO3-GOVERNED-A'
REPORT=OWN+'执行记录/007 - 真实重组控制与恢复复核.md'
AUDIT=OWN+'审计/MS04/CORE_COGNITION_AUDIT.md'

def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(sp);sp.loader.exec_module(rt)
    sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as edit
    s=json.loads((ROOT/rt.STATE).read_text());assert s['revision']==273 and SID not in s['records']
    h=json.loads((ROOT/rt.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    inp=json.loads((HERE.parent/'MS01/method-inputs/MANIFEST.json').read_text())
    assert all(sha(x['source'])==x['sha256'] for x in inp['rows'])
    checks=json.loads((HERE/'validation-001/RESULT.json').read_text());assert checks['status']=='CHECKED_WITH_SCOPE'
    assert checks['source_drift']==[] and checks['label_mismatches']==[] and all(x['exit']==0 for x in checks['commands'])
    rt.query_record(ROOT,TASK)
    plan=rt.plan(ROOT,profile='research',task_ids=[TASK]);assert set(plan['review_required'])<={TASK} and not plan['hydration_diagnostics']['query_first_promoted']
    (HERE/'checkpoint-plan.json').write_bytes(rt.dump(plan))
    r=s['records'][TASK]
    r.update(status='MS04_REAL_REGROUP_AND_CONTROLS_EXECUTED_C04_NEXT',evidence_status='C01_NATIVE_REUSED / REAL_C01_REGROUPING_AND_BOUNDED_METHOD_CONTROLS / MS02_MS05_REMAINDER / ROUND_INCOMPLETE',full_sources=['goal-6.md','goal-5.md',REPORT,AUDIT])
    pins=[REPORT,AUDIT,OWN+'覆盖与关系/003 - 首遍语义裁决与实际验证选择.md',OWN+'覆盖与关系/004 - 语义单元与联合条件.md',OWN+'方法与偏差复测.md',OWN+'方法与偏差复测/001 - C01真实来源重组与对照.md',OWN+'方法与偏差复测/002 - 联合条件与粒度失真控制.md',OWN+'证据/MS04/validation-001/RESULT.json']
    r['source_hashes'].update({p:sha(p) for p in pins})
    r['revalidation']='Same final v7/Goal1.2 method bytes actually reread after explicit resume. Own coverage003 update reconciled: C01 exact result retained, no runtime feedback inferred. Four real frozen source slices regrouped and compared; ten prompted records reviewed with five specified distortions and normal controls; fixed joint/order fixtures executed and replayed. No new mathematical claim, no blind discovery/future-behavior certification. Remaining higher-level and diverse-process obligations stay open.'
    r['scope']='Full MO3 Goal5 v1.2/Goal6. MS04 executed for real C01 regrouping and named finite method controls. MS02 and MS05 remain incomplete beyond this topic; C04/C02/R09, dedicated bias regression and MS06 final seal still required.'
    rev=s['revision']+1;s['revision']=rev;s['latest_session']=SID
    message=f'MO3已完成C01真实来源重组和指定联合/粒度控制：四源284行、8责任单元、十份覆盖记录4接受6拒绝，均限有提示A自测范围。C327–330证明复用；MS02/MS05其它域与非叶问题、C04/C02/R09、专门偏差回归及MS06未完。下一C04原生运输次序及正常控制。ROUND_INCOMPLETE，无final seal；revision{rev}。'
    nxt='Execute independent C04 native Bouquet/transport-order process after full Highest Directive and KC47/48 reload, including actual shared-family input, reverse-path and constant-family controls. Then C02 finite-index delivery, R09 and all remaining accepted non-leaf questions under MS02/MS05; execute dedicated bias regression before MS06 seal. MS04 only covers the declared real C01 regrouping and finite prompted controls; no more unchanged C01 kernel reruns.'
    s['execution_control'].update(current_phase='MO3_W3_C04_NATIVE_HOLDOUT',status='MO3_ACTIVE_ROUND_INCOMPLETE',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_completion_eligible=False,app_goal_status_observed='active')
    s['projection']['status']='MO3_MS04_EXECUTED_WITH_SCOPE / C04_NEXT / ROUND_INCOMPLETE'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='REAL_SOURCE_REGROUPING_AND_PROMPTED_CONTROLS_NOT_NEW_MATH',depends_on=[],related_records=[TASK,'R-MO3-C01-STAGE-COLIMIT-20260923'],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']])
    docs={p:edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0]
    edit.replace_in_shard(docs['MEMORY.md'],mp,old,message)
    edit.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：真实C01四源职责重组、联合/顺序夹具和十条粒度记录审查实际完成；新增覆盖定位不称新定理。MS04有界完成，MS02/MS05其它问题及偏差回归未完；下一C04，后续C02/R09/封存。revision{rev}。\n')
    for p,kind,rid in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p],'source_state_revision: 273',f'source_state_revision: {rev}')
        edit.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-273',f'projection_generation: 20260924-{kind}-{rev}')
        docs[p]['index_text']=docs[p]['index_text'].replace('MO3_MS01_V12_REVALIDATED_ROUND_INCOMPLETE','MO3_MS04_EXECUTED_WITH_SCOPE_ROUND_INCOMPLETE')
        s['records'][rid].update(projection_generation=f'20260924-{kind}-{rev}',semantic_status='MO3_MS04_EXECUTED_WITH_SCOPE_ROUND_INCOMPLETE',scope='Real C01 regrouping and named prompted controls executed; other domains, native holdout, bias regression and final seal incomplete.')
    dp='方向追踪/002 - 治理与用户方向.md'
    docs['方向追踪.md']['shards'][dp]=re.sub(r'^\| `DIR-U-MO3-GOVERNED` .*$',f'| `DIR-U-MO3-GOVERNED` | 第三轮递归多尺度与针对性过程 | 用户Goal1.2、Goal6-MS01–06、KC2/40/44–48 | `ACTIVE / C04_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-C01-STAGE-COLIMIT`, `OUT-MO3-MS04-CONTROLS` | 原生路径次序、C02/R09及非叶结案/偏差回归 | {REPORT}；revision{rev} |',docs['方向追踪.md']['shards'][dp],flags=re.M)
    edit.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-MO3-MS04-CONTROLS` | C01真实重组与方法控制 | `DIR-U-MO3-GOVERNED` | 四源重建、旧表比较、联合/顺序夹具、十记录审查 | `EXECUTED_WITH_SCOPE / PROMPTED_SELF_REVIEW` | 共同stage、rank及配置责任可单独审查；正常合并/精化未误判 | 无新数学claim，不认证盲发现或所有层次；C04/C02/R09等未完 | {REPORT}；{AUDIT}；revision{rev} |\n')
    pp='全景视野/008 - 当前未完成.md'
    docs['全景视野.md']['shards'][pp]=re.sub(r'^17\. MO3-GOVERNED-A.*$','17. MO3-GOVERNED-A：MS01恢复差分、C01精确原生结果和MS04真实重组/指定粒度控制已完成各自范围；MS02其它域单元、MS05全部非叶结案、C04/C02/R09实际过程、专门偏差回归、MS06最终封存仍未完成。不得用本主题或合成自测替全轮验收。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for d in docs.values():rows+=edit.payload_rows(d,ROOT)
    seen={x['path'] for x in rows}
    for p in rt.MUTABLE:
        if p in seen:continue
        content=(ROOT/p).read_text()
        if p==rt.STATE:content=rt.dump(s).decode()
        elif p.endswith(('FRONTIER.md','RESUME.md')):assert old in content;content=content.replace(old,message,1)
        rows.append(dict(path=p,expected_sha256=sha(p),text=content))
    a=edit.load(ROOT,AUDIT)
    legacy=['# '+SID+' 兼容完整审计','- identity: '+s['current_core']['generation']+' / 48 KC']+[l for l in a['index_text'].splitlines() if re.match(r'^- (core_change|direction_change|panorama_change|essay_change|update_decision|cross_conflicts|unresolved):',l)]+['分片语义原件：'+AUDIT+'；嵌套writer缺口保留。']+list(a['shards'].values())
    audit='\n\n'.join(legacy).rstrip()+'\n';assert rt._audit_v1_kc_rows(audit)==[f'KC-{i:06d}' for i in range(1,49)]
    session=f'# {SID}\n\n- host: codex-desktop\n- model: Astra（用户选择，不认证后端指纹）\n- tier: T3\n- role: RESEARCH_GENERATION / sole canonical integrator\n- load_receipt: {OWN}证据/MS04/recovery-001.json；本次角色/Goal/最高指示全文、逐KC复认及源抽查；STATE268全文与自身269–273差分，273后像无漂移。\n- status: MS04_EXECUTED_WITH_SCOPE / ROUND_INCOMPLETE\n- report: {REPORT}\n- semantic_audit: {AUDIT}\n- next: {nxt}\n- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；完整单文件在事务内，语义分片在独占目录。\n\n|element_usage|实际用途/边界|\n|---|---|\n|原文和方法|恢复并将共同责任用于重组，非永久行为认证|\n|原生结果|C01精确复用，不复跑或升级全registry|\n|真实重组与控制|区分source/语义/软件运行，不认证全层完备|\n|审计与canonical writer|保存当前余项和下一动作，非数学证明|\n\nreflection=no-plan-change；执行59401d8现行计划。T01/04/13/22/24/26更新研究证据/状态；需求、平台、schema、配置和全局治理不改。无Sub Agent、新Session、push/tag、core或历史原件修改。\n'
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],reused_claim_ids=['C-327','C-328','C-329','C-330'],method_evidence=[OWN+'证据/MS04/fixed-controls-result.json',OWN+'证据/MS04/replay-001/RUN.json',OWN+'证据/MS04/granularity-review.json',OWN+'证据/MS04/record-check.json'],validation=OWN+'证据/MS04/validation-001/RESULT.json',scope='Bounded real-source regrouping and prompted method controls; not autonomous discovery or whole-round completion.')
    rows += [dict(path=BASE+n,expected_sha256=None,text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[TASK],authorization='用户恢复MO3研究并确认方法维护完成；沿A唯一integrator与本轮精确写回授权，只保存实际有界成果及未完义务。',files=rows)
    (HERE/'checkpoint-payload.json').write_bytes(rt.dump(payload))
    res=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (HERE/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(rt.dump(res))
    print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
