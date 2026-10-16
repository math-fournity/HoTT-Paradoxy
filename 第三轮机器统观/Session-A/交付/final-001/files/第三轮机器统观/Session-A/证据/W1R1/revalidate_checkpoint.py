#!/usr/bin/env python3
"""Apply only the authored method-consumption correction through canonical state."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, re, sys

ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
OWN='第三轮机器统观/Session-A/'
SID='S-RES-20260923-MO3-A-W1R1'
BASE=f'.codex/research/hott/sessions/{SID}/'
TASK='MO3-GOVERNED-A'
REPORT=OWN+'执行记录/004 - 第六稿消费与候选独立性复核.md'
COVER=OWN+'覆盖与关系/003 - 首遍语义裁决与实际验证选择.md'
AUDIT=OWN+'审计/W1R1/CORE_COGNITION_AUDIT.md'
def sha(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    spec=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(spec);spec.loader.exec_module(rt)
    sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as edit
    s=json.loads((ROOT/rt.STATE).read_text());assert s['revision']==270 and SID not in s['records']
    head=json.loads((ROOT/rt.HEAD).read_text());assert all(sha(p)==h for p,h in head['tracked'].items())
    inputs=json.loads((HERE/'method-inputs.json').read_text())
    for x in inputs['rows']: assert sha(x['source'])==sha(x['copy'])==x['sha256'],'method changed during consumption'
    plan=rt.plan(ROOT,profile='research',task_ids=[TASK]);assert set(plan['review_required']) <= {TASK}
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (HERE/'checkpoint-plan.json').write_bytes(rt.dump(plan))
    rev=s['revision']+1
    message=f'MO3 W1完成并已消费最高指示第六稿/Goal5 v1.1/Skill1.1.0。当前候选按自身X_i核验，撤销误加的未声明历史圆环补题；实际引用保真与专门偏差回归仍保留。下一步W2原生C01直接合成/Acc和方法控制；C02覆盖列表、C04路径有序作用及R09组合审查按自身价值继续。W2–W5未完，无新数学claim或seal；revision{rev}。'
    next_action='W2 native C01: construct finite stage graphs, stage-induced edges on SeqColim, Acc qualification and frozen-stage/consumer controls. Continue C02 enumerable cover delivery, C04 path-order process and R09 substitution interfaces for their own Xi; no undeclared historical-circle bridge. All five-scale/multi-mechanism/four-control/native/reality/omission/seal obligations remain.'
    r=s['records'][TASK]
    r.update(status='W1_REVALIDATED_V6_W2_NEXT',evidence_status='METHOD_V6_CONSUMED / W1_SOURCE_PASS_WITH_SCOPE / PROCESS_SPECS_UNPROVED / ROUND_INCOMPLETE',full_sources=['goal-6.md','goal-5.md',REPORT,COVER,AUDIT])
    pins=[x['source'] for x in inputs['rows']]+[REPORT,COVER,AUDIT,OWN+'证据/W1R1/method-inputs.json']
    r['source_hashes'].update({p:sha(p) for p in pins})
    r['revalidation']='Actual full reread of Highest Directive v6, Goal5 v1.1, Goal6, execution Skill1.1.0 and TASK_ROUTING; report004 answers14/re-presentations. Correct Xi/Xh conflation by withdrawing undeclared circle backlog, retain own reality bridges and all parent coverage/controls. Old W0/W1 input hashes remain in historical receipts; no math promotion.'
    r['scope']='MO3 W0/W1 sourced first pass complete with scope and v6 method correction consumed. C01/C02/C04 judged on own Xi; original-circle completion was not claimed. W2-W5 process verification, mechanisms, controls, reality bridges, omissions and final B seal remain.'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='METHOD_REVALIDATION_ONLY_NO_MATH',depends_on=[],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']],related_records=[TASK])
    s['revision']=rev;s['latest_session']=SID
    s['execution_control'].update(current_phase='MO3_W2_NATIVE_THIN_CHAIN',next_minimal_verification=next_action,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_completion_eligible=False)
    s['projection']['status']='MO3_W1_REVALIDATED_V6_W2_NEXT / ROUND_INCOMPLETE / NO_NEW_MATH'
    docs={p:edit.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];edit.replace_in_shard(docs['MEMORY.md'],mp,old,message)
    edit.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：A实际消费第六稿及1.1方法，修正X_i/X_h混同；历史W1收据保留，移除无依据圆环补题。C01仍W2下一；无数学claim。revision{rev}。\n')
    for p,kind,rid in [('方向追踪.md','direction','I-DIRECTION-PORTFOLIO-20260912'),('全景视野.md','outcome','I-OUTCOME-PANORAMA-20260912')]:
        edit.replace_in_index(docs[p],'source_state_revision: 270',f'source_state_revision: {rev}')
        edit.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-270',f'projection_generation: 20260923-{kind}-{rev}')
        docs[p]['index_text']=docs[p]['index_text'].replace('MO3_W1_COMPLETE_W2_NEXT_ROUND_INCOMPLETE','MO3_W1_REVALIDATED_V6_W2_NEXT_ROUND_INCOMPLETE')
        s['records'][rid].update(projection_generation=f'20260923-{kind}-{rev}',semantic_status='MO3_W1_REVALIDATED_V6_W2_NEXT_ROUND_INCOMPLETE',scope='MO3 W1 and v6 method consumption; candidate Xi preserved, undeclared historical bridge removed. W2-W5 remain incomplete.')
    dp='方向追踪/002 - 治理与用户方向.md'
    docs['方向追踪.md']['shards'][dp]=re.sub(r'^\| `DIR-U-MO3-GOVERNED` .*$',f'| `DIR-U-MO3-GOVERNED` | 第三轮八域五尺度与针对性过程 | 用户Goal6、KC2/11/16/44–48 | `ACTIVE / W2_NEXT / V6_REVALIDATED` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MO3-W1-SOURCE-PASS`, `OUT-MO3-V6-REVALIDATION` | C01优先；C02/C04/R09按自身X_i；四控制与父级广度保留 | {REPORT}；revision{rev} |',docs['方向追踪.md']['shards'][dp],flags=re.M)
    edit.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-MO3-V6-REVALIDATION` | 第六稿方法实际消费与候选独立性纠正 | `DIR-U-MO3-GOVERNED` | 新方法全文、14题/呈现、当前owner修正 | `METHOD_CONSUMED / NO_NEW_MATH` | 取消未声明圆环补题；保留各X_i现实桥和多机制义务 | 不认证未来行为或候选成立；W2–W5未完 | {REPORT}；{AUDIT}；revision{rev} |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^17\. MO3-GOVERNED-A.*$','17. MO3-GOVERNED-A：W0/W1有范围完成，v6方法已重新消费；W2–W5未完。C01直接合成/Acc下一，C02覆盖列表、C04路径顺序与R09按各自任务继续。四方法控制、多尺度/多机制、原生/现实桥和最终B封存仍必做；未声明的历史圆环桥不再作为本轮欠账。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for d in docs.values():rows+=edit.payload_rows(d,ROOT)
    seen={x['path'] for x in rows}
    for p in rt.MUTABLE:
        if p in seen:continue
        content=(ROOT/p).read_text()
        if p==rt.STATE:content=rt.dump(s).decode()
        elif p.endswith('FRONTIER.md'):content=re.sub(r'^- MO3-GOVERNED-A.*$','- '+message,content,flags=re.M)
        elif p.endswith('RESUME.md'):content=re.sub(r'^MO3-GOVERNED-A.*$',message,content,flags=re.M)
        rows.append(dict(path=p,expected_sha256=sha(p),text=content))
    a=edit.load(ROOT,AUDIT);legacy=['# '+SID+' 兼容完整审计','- identity: '+s['current_core']['generation']+' / 48 KC']
    legacy += [l for l in a['index_text'].splitlines() if re.match(r'^- (core_change|direction_change|panorama_change|essay_change|update_decision|cross_conflicts|unresolved):',l)]
    legacy += ['语义分片原件：'+AUDIT+'；嵌套writer缺口仍在。']+list(a['shards'].values());audit='\n\n'.join(legacy)+'\n'
    assert rt._audit_v1_kc_rows(audit)==[f'KC-{i:06d}' for i in range(1,49)]
    session=f'# {SID}\n\n- host: codex-desktop\n- model: Astra（用户选择，不认证后端指纹）\n- tier: T3\n- role: RESEARCH_GENERATION / sole canonical integrator\n- load_receipt: {OWN}证据/W1R1/method-inputs.json；最高指示493 EOF，Goal5/6/Skill/route全文，KC47/48重读；STATE268全文+自身269/270已读已核差分，current owner无外来漂移。\n- status: W1_REVALIDATED_V6_W2_NEXT / ROUND_INCOMPLETE\n- report: {REPORT}\n- semantic_audit: {AUDIT}\n- next: {next_action}\n- authorization: 用户Goal6本轮研究checkpoint/精确本地提交；无push/tag/Sub Agent、新Session、core或外部方法正文改动。\n- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；单文件兼容事务内，语义分片事务外。\n\n|element_usage|用途/边界|\n|---|---|\n|新方法全文|真实消费与X_i/X_h纠正，非数学证明|\n|core/四件套|原文未变及逐KC复认|\n|当前owners|撤销误加历史桥，保留父级义务|\n|旧checkpoint|保存at-run而不刷新伪装|\n|原生工具|本单元未运行，资格沿用W0|\n\nreflection=plan-revise(MO3-v6-consumption)。T01/03/04/13/22/24/26更新方法消费与队列；其余T02/05–12/14–21/23/25无产品需求/实现/config/schema/发布/治理合同修改。\n'
    runs=dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],method_inputs=OWN+'证据/W1R1/method-inputs.json',report=REPORT,scope='A consumed method update and corrected task ownership, no new mathematical conclusion.')
    rows += [dict(path=BASE+n,expected_sha256=None,text=t) for n,t in [('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='research',task_ids=[TASK],authorization='用户Goal6授权A研究integrator；按新版Goal6§8实际重读后更新自己的方法pin/队列，保留历史输入，不改core、不push/tag。',files=rows)
    (HERE/'checkpoint-payload.json').write_bytes(rt.dump(payload));result=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (HERE/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(rt.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
