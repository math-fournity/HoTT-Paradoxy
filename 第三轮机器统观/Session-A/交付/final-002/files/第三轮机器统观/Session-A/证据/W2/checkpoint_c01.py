#!/usr/bin/env python3
"""Preserve C01 evidence; do not claim unread moving method inputs revalidated."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, re, sys
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
OWN='第三轮机器统观/Session-A/'
SID='S-RES-20260923-MO3-A-C01'
BASE=f'.codex/research/hott/sessions/{SID}/'
TASK='MO3-GOVERNED-A'
RESULT='R-MO3-C01-STAGE-COLIMIT-20260923'
REPORT=OWN+'过程与结果/001 - 阶段合成与递归资格.md'
AUDIT=OWN+'审计/W2-C01/CORE_COGNITION_AUDIT.md'
EXEC=OWN+'执行记录/005 - C01原生结果与C04接续.md'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(sp);sp.loader.exec_module(rt)
    sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as edit
    s=json.loads((ROOT/rt.STATE).read_text());assert s['revision']==271 and SID not in s['records'] and RESULT not in s['records']
    h=json.loads((ROOT/rt.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    plan=rt.plan(ROOT,profile='research',task_ids=[TASK]);assert set(plan['review_required']) <= {TASK} and not plan['hydration_diagnostics']['query_first_promoted']
    (HERE/'c01-checkpoint-plan.json').write_bytes(rt.dump(plan))
    version=json.loads((HERE/'version-check/RESULT.json').read_text());assert version['status']=='SELECTED_PACKAGES_VERSION_CLOSED'
    proof='HoTT/formal/mo3/stage-colimit/'
    run='HoTT/verification/runs/20260923-MO3-STAGE-COLIMIT-001-04/'
    pins=[REPORT,proof+'StageColimit.agda',proof+'README.md',run+'RUN.json',run+'source-manifest.json',run+'index-row-manifest.json',OWN+'证据/W2/version-check/RESULT.json']
    s['records'][RESULT]=dict(kind='result',path=REPORT,lifecycle_status='CLOSED',status='C01_SCOPED_BOUNDARY_COMPLETE_NOT_QUALIFIED_HOTT_HIT',evidence_status='FORMAL_CHECKED_WITH_SCOPE / SELECTED_PACKAGES_VERSION_CLOSED / REALITY_MISMATCH_NOT_ESTABLISHED',depends_on=[],related_records=[TASK],full_sources=pins,source_hashes={p:sha(p) for p in pins},claim_ids=['C-327','C-328','C-329','C-330'],proof_id='MP-MO3-STAGE-COLIMIT-001',subject_commit=version['head'],scope='Exact Stage/StageStep/fsuc and native stage-induced SeqColim relation plus frozen-stage control. No arbitrary colimit theorem, physical nontermination, HoTT preservation promise, original-circle solution or global completeness.')
    r=s['records'][TASK]
    r.update(status='W2_C01_EVIDENCE_COMPLETE_METHOD_INPUT_PENDING',evidence_status='REVIEW_REQUIRED',depends_on=[RESULT],dependency_semantics='verification_staleness',full_sources=['goal-6.md','goal-5.md',EXEC,AUDIT])
    r['related_records']=list(dict.fromkeys(r.get('related_records',[])+[RESULT]))
    r['source_hashes'].update({p:sha(p) for p in [EXEC,AUDIT]})
    r['revalidation']='C01 source/kernel/index/version evidence is fixed at f02b61f and recorded separately. Parent method pins intentionally remain stale: after actual read of 493-line6ba input, Highest Directive changed to503-linea6cb. That input is not fully consumed; user final-version clarification is pending. No false method revalidation, no Goal pause/completion.'
    rev=s['revision']+1;s['revision']=rev;s['latest_session']=SID
    message=f'MO3 C01已完成精确原生薄链：C327–330在f02b61f上selected版本闭合，研究判词为有正控制的资格边界、未建立HoTT现实相对命中。方法输入在493行版消费后又变503行，parent为REVIEW_REQUIRED，待定稿信号及完整恢复；C04尚未执行。C02/R09、四控制和W2–W5未完，无final seal。revision{rev}。'
    next_action='Resolve authoritative final method input and fully reload/re-present it; keep stale pins until actual consumption. Then implement C04 native Bouquet/UA/path-order consumer and execute W2 method controls, followed by C02 and R09. C01 math boundary is preserved at f02b61f; do not repeat same-stage mechanism or treat it as a HoTT reality mismatch.'
    s['execution_control'].update(current_phase='MO3_W2_METHOD_INPUT_REVALIDATION',status='MO3_ACTIVE_SOURCE_REVALIDATION_PENDING',next_minimal_verification=next_action,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_completion_eligible=False,app_goal_status_observed='active')
    s['projection']['status']='MO3_C01_SCOPED_MATH_COMPLETE / METHOD_REVIEW_REQUIRED / ROUND_INCOMPLETE'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='C01_SCOPED_MATH_WITH_SOURCE_REVALIDATION_PENDING',depends_on=[],related_records=[TASK,RESULT],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']])
    docs={p:edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];edit.replace_in_shard(docs['MEMORY.md'],mp,old,message)
    edit.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：C327–330原生source/run/index与本包Git闭合；C01未获现实相对命中。方法再次更新，parent REVIEW_REQUIRED，不刷新未读pin。C04/四控制等仍未完；revision{rev}。\n')
    for p,kind,rid in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p],'source_state_revision: 271',f'source_state_revision: {rev}');edit.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-271',f'projection_generation: 20260923-{kind}-{rev}')
        docs[p]['index_text']=docs[p]['index_text'].replace('MO3_W1_REVALIDATED_V6_W2_NEXT_ROUND_INCOMPLETE','MO3_C01_COMPLETE_METHOD_REVIEW_REQUIRED_ROUND_INCOMPLETE')
        s['records'][rid].update(projection_generation=f'20260923-{kind}-{rev}',semantic_status='MO3_C01_COMPLETE_METHOD_REVIEW_REQUIRED_ROUND_INCOMPLETE',scope='C01 scoped native mathematical result; whole round incomplete and method inputs awaiting current consumption.')
    dp='方向追踪/002 - 治理与用户方向.md';docs['方向追踪.md']['shards'][dp]=re.sub(r'^\| `DIR-U-MO3-GOVERNED` .*$',f'| `DIR-U-MO3-GOVERNED` | 第三轮八域五尺度与针对性过程 | 用户Goal6、KC2/11/16/44–48 | `ACTIVE / METHOD_REVIEW_REQUIRED` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-C01-STAGE-COLIMIT` | 先闭合最新方法输入，再C04/四控制；C02/R09继续 | {EXEC}；revision{rev} |',docs['方向追踪.md']['shards'][dp],flags=re.M)
    edit.append_to_shard(docs['全景视野.md'],'全景视野/003 - 当前机器证明包与原生重放.md',f'\n| `OUT-MO3-C01-STAGE-COLIMIT` | 阶段合成与Acc资格 | `DIR-U-MO3-GOVERNED` | 原生SeqColim/Acc/PT，C327–330，正式run04 | `FORMAL_CHECKED_WITH_SCOPE / SELECTED_VERSION_CLOSED` | 有限阶段良基/保边；指定合成链非Acc；恒定族正控制 | 不证明物理不可完成、HoTT保Acc承诺或现实相对命中 | {REPORT}；{run}；f02b61f；revision{rev} |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^17\. MO3-GOVERNED-A.*$','17. MO3-GOVERNED-A：C01原生数学薄链已完成，尚非现实相对命中；当前方法再次变更，parent REVIEW_REQUIRED。定稿输入与实际重读闭合后继续C04/四控制、C02/R09及W2–W5。没有final seal或B审计；无声明的历史圆环桥不作附加欠账。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for d in docs.values():rows+=edit.payload_rows(d,ROOT)
    seen={x['path'] for x in rows}
    for p in rt.MUTABLE:
        if p in seen:continue
        content=(ROOT/p).read_text()
        if p==rt.STATE:content=rt.dump(s).decode()
        elif p.endswith(('FRONTIER.md','RESUME.md')):assert old in content;content=content.replace(old,message,1)
        rows.append(dict(path=p,expected_sha256=sha(p),text=content))
    a=edit.load(ROOT,AUDIT);legacy=['# '+SID+' 兼容完整审计','- identity: '+s['current_core']['generation']+' / 48 KC']+[l for l in a['index_text'].splitlines() if re.match(r'^- (core_change|direction_change|panorama_change|essay_change|update_decision|cross_conflicts|unresolved):',l)]+['语义原件：'+AUDIT+'；嵌套writer缺口仍在。']+list(a['shards'].values());audit='\n\n'.join(legacy)+'\n';assert rt._audit_v1_kc_rows(audit)==[f'KC-{i:06d}' for i in range(1,49)]
    session=f'# {SID}\n\n- host: codex-desktop\n- model: Astra（用户选择，不认证后端指纹）\n- tier: T3\n- role: RESEARCH_GENERATION / sole canonical integrator\n- load_receipt: W0完整STATE268及自身269–271已读事务差分；current owners无漂移。最高指示493行6ba全文/Skill6fb全文与KC44–48/扩展008消费见{EXEC}；后到503行a6cb尚未读，parent保REVIEW_REQUIRED。\n- status: C01_SCOPED_MATH_COMPLETE / ROUND_INCOMPLETE\n- report: {REPORT}\n- semantic_audit: {AUDIT}\n- next: {next_action}\n- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001，完整单文件在事务内、语义分片事务外。\n\n|element_usage|实际用途/边界|\n|---|---|\n|core/方法|生成与任务保真，最新未读pin不伪刷|\n|原生工具|C327–330及控制，实际数学范围|\n|F011|两项证据/selected版本通过，全局旧错配披露|\n|审计/STATE|保存结果、失败、后继与真实stale|\n\nreflection=no-plan-change，C01以有正控制边界收尾并返回广度。T01/03/04/11/13/22/24/26为数学source/run/索引/当前态变更；其余T02/05–10/12/14–21/23/25无产品/配置/schema/部署/治理合同修改。无Sub Agent、新Session、push/tag/发布或core更改。\n'
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=['C-327','C-328','C-329','C-330'],proof_id='MP-MO3-STAGE-COLIMIT-001',primary_run=run,control_run='HoTT/verification/runs/20260923-MO3-STAGE-COLIMIT-CONTROL-01',subject_commit=version['head'],semantic_audit=AUDIT,source_revalidation_pending=True,scope='C01 exact mathematical boundary and scoped controls; no qualified HoTT reality mismatch or round completion.')
    rows += [dict(path=BASE+n,expected_sha256=None,text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[TASK],authorization='用户Goal6授权A精确研究checkpoint与本地提交；只保存C01自身结果及真实方法stale，不刷新未消费输入、不改历史/core、不push/tag。',files=rows)
    (HERE/'c01-checkpoint-payload.json').write_bytes(rt.dump(payload));res=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply);(HERE/('c01-checkpoint-apply.json' if args.apply else 'c01-checkpoint-dry-run.json')).write_bytes(rt.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
