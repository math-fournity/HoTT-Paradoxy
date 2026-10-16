#!/usr/bin/env python3
"""Record actual v1.2 consumption and bounded reuse decisions through canonical state."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, re, sys
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
OWN='第三轮机器统观/Session-A/'
SID='S-RES-20260923-MO3-A-MS01'
BASE=f'.codex/research/hott/sessions/{SID}/'
TASK='MO3-GOVERNED-A'
C01='R-MO3-C01-STAGE-COLIMIT-20260923'
REPORT=OWN+'执行记录/006 - Goal1.2差分复核与复用裁决.md'
AUDIT=OWN+'审计/MS01/CORE_COGNITION_AUDIT.md'
PROCESS=OWN+'过程与结果/001 - 阶段合成与递归资格.md'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(sp);sp.loader.exec_module(rt)
    sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as edit
    s=json.loads((ROOT/rt.STATE).read_text());assert s['revision']==272 and SID not in s['records']
    h=json.loads((ROOT/rt.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    inp=json.loads((HERE/'method-inputs/MANIFEST.json').read_text())
    for x in inp['rows']:assert sha(x['source'])==sha(x['copy'])==x['sha256'],'method changed during review'
    checks=json.loads((HERE/'reuse-check.json').read_text());assert all(c['exit']==0 for c in checks['checks'].values()) and not checks['checkpoint_drift'] and not checks['builtin_drift']
    plan=rt.plan(ROOT,profile='research',task_ids=[TASK]);assert set(plan['review_required']) <= {TASK,C01} and not plan['hydration_diagnostics']['query_first_promoted']
    (HERE/'checkpoint-plan.json').write_bytes(rt.dump(plan))
    s['records'][C01]['source_hashes'][PROCESS]=sha(PROCESS)
    s['records'][C01]['revalidation']='Current formal-run and selected Git version checks passed at unchanged f02 source/inputs. Process report now states already-completed controls accurately; no theorem, code, native rule or run changed. C01 only closes its exact family, not all high-level questions.'
    r=s['records'][TASK]
    r.update(status='MS01_V12_REVALIDATED_MS02_MS04_NEXT',evidence_status='V7_AND_GOAL1_2_ACTUALLY_CONSUMED / C01_REUSED_WITH_SCOPE / COVERAGE_DELTA_OPEN / ROUND_INCOMPLETE',full_sources=['goal-6.md','goal-5.md',REPORT,AUDIT])
    pins=[x['source'] for x in inp['rows']]+[REPORT,AUDIT,OWN+'证据/MS01/method-inputs/MANIFEST.json']
    r['source_hashes'].update({p:sha(p) for p in pins})
    r['revalidation']='User resumed with Goal5 v1.2 objective. Fully read Highest Directive v7(503 lines), Goal5/6, role/common/router, improvement plan/self-audit and all six planning shards. Report006 has explicit MS01-MS06 delta and14/re-presentations. Reuse unchanged C01 proof; expand W1 semantic units/relations and redo coverage adjudication, not theorem proofs. Unexecuted controls remain mandatory; maintainer tests do not substitute for A.'
    r['scope']='Full MO3 Goal5 v1.2/Goal6 MS01-MS06. W0 source intake and W1 sourced questions retained with coverage delta; C01 exact native boundary reused. Recursive semantic organisation, real regrouping/granularity controls, all accepted non-leaf adjudications, remaining processes and final seal still required.'
    rev=s['revision']+1;s['revision']=rev;s['latest_session']=SID
    message=f'MO3恢复active，Goal5 v1.2/最高指示第七稿及完整方法链已实际消费。MS01差分裁决：C01 C327–330原样复用；W1来源/问题保留，递归语义组织和本层结案补审；方法控制仍待做。下一步MS02/MS04真实单元重组与粒度控制，再C04/C02/R09及余项。ROUND_INCOMPLETE，无final seal；revision{rev}。'
    nxt='MS02/MS04: enrich existing W1 owners with recursive/overlapping units, exact members and joint/order/shared-background conditions; independently regroup fixed real C01 sources and compare with prior organisation, including middle-layer/joint/order/unknown/calculus negative controls and complete positive control. Then execute C04 native path-order process, C02 delivery and R09; individually adjudicate all accepted higher-level questions under MS05 before MS06 seal. Do not rerun unchanged C01 proof or count maintainer fixtures as A research.'
    s['execution_control'].update(current_phase='MO3_V12_SEMANTIC_REORGANISATION',status='MO3_ACTIVE_ROUND_INCOMPLETE',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_completion_eligible=False,app_goal_status_observed='active')
    s['projection']['status']='MO3_MS01_V12_REVALIDATED / MS02_MS04_NEXT / ROUND_INCOMPLETE'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='MS01_REUSE_AND_COVERAGE_DELTA_REVIEW_ONLY',depends_on=[],related_records=[TASK,C01],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']])
    docs={p:edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];edit.replace_in_shard(docs['MEMORY.md'],mp,old,message)
    edit.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：用户新版Goal已恢复；MS01实际消费与差分复核，C01证明不重做，W1层次/关系评价补审；R05未由静态C01实现明确。MS02/MS04下一，MS02–06/W2–W5仍未完。revision{rev}。\n')
    for p,kind,rid in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p],'source_state_revision: 272',f'source_state_revision: {rev}');edit.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-272',f'projection_generation: 20260923-{kind}-{rev}')
        docs[p]['index_text']=docs[p]['index_text'].replace('MO3_C01_COMPLETE_METHOD_REVIEW_REQUIRED_ROUND_INCOMPLETE','MO3_MS01_V12_REVALIDATED_ROUND_INCOMPLETE')
        s['records'][rid].update(projection_generation=f'20260923-{kind}-{rev}',semantic_status='MO3_MS01_V12_REVALIDATED_ROUND_INCOMPLETE',scope='Actual v1.2 method consumption and MS01 delta; C01 reused, MS02-MS06 and whole round not complete.')
    dp='方向追踪/002 - 治理与用户方向.md';docs['方向追踪.md']['shards'][dp]=re.sub(r'^\| `DIR-U-MO3-GOVERNED` .*$',f'| `DIR-U-MO3-GOVERNED` | 第三轮递归多尺度与针对性过程 | 用户Goal1.2、Goal6-MS01–06、KC2/40/44–48 | `ACTIVE / MS02_MS04_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-C01-STAGE-COLIMIT`, `OUT-MO3-MS01-REUSE` | 真实语义重组/粒度控制后继续C04/C02/R09；不重跑不变C01 | {REPORT}；revision{rev} |',docs['方向追踪.md']['shards'][dp],flags=re.M)
    edit.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-MO3-MS01-REUSE` | Goal1.2恢复与复用差分 | `DIR-U-MO3-GOVERNED` | 当前方法全文、C01证据复核、272后像与差分 | `MS01_COMPLETE_WITH_SCOPE / COVERAGE_DELTA_OPEN` | C01正确实物保留，W1组织/高层结案补审，未做控制继续 | 不替MS02–06，不认证全理论或未来行为；R05不作已验证反馈 | {REPORT}；{AUDIT}；revision{rev} |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^17\. MO3-GOVERNED-A.*$','17. MO3-GOVERNED-A：第七稿/Goal1.2已实际消费，MS01差分完成；C01精确证明复用。MS02语义单元与MS04真实重组/粒度控制下一；C04/C02/R09、MS05全部已接受中高层结案、MS06最终封存仍未完成。一个C01不抵高层全覆盖，维护者脚本不抵A研究。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for d in docs.values():rows+=edit.payload_rows(d,ROOT)
    seen={x['path'] for x in rows}
    for p in rt.MUTABLE:
        if p in seen:continue
        content=(ROOT/p).read_text()
        if p==rt.STATE:content=rt.dump(s).decode()
        elif p.endswith(('FRONTIER.md','RESUME.md')):assert old in content;content=content.replace(old,message,1)
        rows.append(dict(path=p,expected_sha256=sha(p),text=content))
    a=edit.load(ROOT,AUDIT);legacy=['# '+SID+' 兼容完整审计','- identity: '+s['current_core']['generation']+' / 48 KC']+[l for l in a['index_text'].splitlines() if re.match(r'^- (core_change|direction_change|panorama_change|essay_change|update_decision|cross_conflicts|unresolved):',l)]+['分片语义原件：'+AUDIT+'；嵌套writer缺口仍在。']+list(a['shards'].values());audit='\n\n'.join(legacy)+'\n';assert rt._audit_v1_kc_rows(audit)==[f'KC-{i:06d}' for i in range(1,49)]
    session=f'# {SID}\n\n- host: codex-desktop\n- model: Astra（用户选择，不认证后端指纹）\n- tier: T3\n- role: RESEARCH_GENERATION / sole canonical integrator\n- load_receipt: {OWN}证据/MS01/method-inputs/MANIFEST.json；STATE268全文及自身269–272已读事务差分，272的37后像无漂移；core48身份不变。\n- status: MS01_COMPLETE_WITH_SCOPE / ROUND_INCOMPLETE\n- report: {REPORT}\n- semantic_audit: {AUDIT}\n- next: {nxt}\n- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001，完整单文件在事务内，语义分片在独占目录。\n\n|element_usage|实际用途/边界|\n|---|---|\n|新方法全文/原文|角色和研究消费，14题/三呈现；非能力自动认证|\n|proof验证|C01精确复用，非全registry通过|\n|W1/覆盖|定位真实层次/关系缺口，不抹历史|\n|审计/STATE|唯一当前队列及真实未完项|\n\nreflection=plan-revise(MO3-v1.2-delta)。影响T01/02/03/04/13/22/24/26；代码/工具链/schema/部署/全局治理不改。既有用户授权继续有效；无Sub Agent、新Session、push/tag/发布或core修改。\n'
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],reused_claim_ids=['C-327','C-328','C-329','C-330'],reuse_check=OWN+'证据/MS01/reuse-check.json',report=REPORT,semantic_audit=AUDIT,scope='New method actually consumed; prior proof unchanged; coverage delta and pending controls explicit.')
    rows += [dict(path=BASE+n,expected_sha256=None,text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[TASK],authorization='用户恢复Goal并提供1.2新内容；沿既有A研究integrator授权，更新实际消费与差分，不改方法维护者原件/旧收据/core，不push/tag。',files=rows)
    (HERE/'checkpoint-payload.json').write_bytes(rt.dump(payload));res=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply);(HERE/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(rt.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
