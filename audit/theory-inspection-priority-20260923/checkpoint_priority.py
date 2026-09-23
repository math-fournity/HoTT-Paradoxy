#!/usr/bin/env python3
"""Canonical checkpoint for the user's theory-inspection-first priority."""
import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
SID='S-PLAN-20260923-ASTRA-THEORY-INSPECTION-FIRST'
BASE=f'.codex/research/hott/sessions/{SID}/'
PLAN='R-HOTT-FOUR-TRACK-PLAN-20260921'
OWNER='HoTT后续研究总体方案/006 - 理论充分检视的首轮范围与验收.md'
TASK='P40-THEORY-INSPECTION-FIRST-001'
CHANGED=['goal.md','goal-3.md','rulings.md','feature-list.md','HoTT后续研究总体方案.md',
 'HoTT后续研究总体方案/002 - 共同任务、术语与优先级原则.md',
 'HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md',
 'HoTT后续研究总体方案/004 - 令牌经济、反漂移与每单元复核.md',
 'HoTT后续研究总体方案/005 - 当前第一步与交接.md',
 'goal-3-工作路径树/001 - 原初目标与当前工作树.md']

def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py')
R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
sys.path.insert(0,str(ROOT/'scripts/audit'))
import projection_edit as E

FOCUS={
 1:('ALIGNED','先弄清HoTT中找什么，理论检视决定后续构造依据'),
 2:('DEEPENED','Schema先行变为源文语义检视，不把目录视作充分'),
 3:('ALIGNED','审清真正前提，再讨论它怎样参与结果'),
 5:('ALIGNED','检视不预判病因，候选后再作最终归因'),
 6:('ALIGNED','全局范围同时保留时间、运动与时序多类问题'),
 9:('DEEPENED','先核理论真实设定，停止以现成模型反定问题'),
 10:('ALIGNED','理论理解服务现实相对见证，非无限资料准备'),
 15:('ALIGNED','强哲学起点保留，充分检视允许反例与安全边界'),
 17:('ALIGNED','先按用户视角检视，再核源文，而非先验否定或赞同'),
 18:('DEEPENED','经济性与普适性选择逐家族分析，不只盯已知三项'),
 21:('ALIGNED','本轮仅调整优先级，无新数学结论与内核重跑'),
 24:('ALIGNED','时间/时序两轴及A/B均进入全景检视'),
 29:('DEEPENED','经济收益与所省条件形成理论检视的问题'),
 30:('DEEPENED','充分检视成为明确首要阶段，接回理论经济学之问'),
 37:('TENSION','快速发现期待保留；本轮没有新悖论，先校正选题依据'),
 38:('DEEPENED','审查作者实际设计选择而非猜测心理'),
 39:('CORRECTED','从有限熟悉候选返回基础与主要理论领域'),
 40:('DEEPENED','知识谱是待检对象，需与固定来源及缺口对应'),
 43:('CORRECTED','三选一优先级撤回，不由已投入路径继续决定'),
 44:('ALIGNED','现实骨架可在理解理论时形成，不要求先有K'),
 45:('DEEPENED','用现实诠释理论，但不把类比加到原规则上'),
 46:('ALIGNED','动作缺口靠源文与交互审查补，不重建平台'),
 47:('ALIGNED','完整原文已重读；广度检视经济性和普适性'),
 48:('DEEPENED','针对性建立在充分理论理解之后，模型敏感性仍必需')}

REFLECTION='''## 本次计划修订的完整反思

Goal-3 §3：
1. 新事实是用户明确要求理论检视优先；既有Schema承认105节仅入口、依赖和变体审查未完。
2. 改变P40三选一判词为理论检视先行；数学结论不变。
3. 未更改旧Input/Operation/Done；新增检视模式允许这些尚未定义。
4. 反解释为既有资产可能足够，届时复用；不预设HoTT有错。
5. 本轮无重跑；使用旧Schema与统观审计确定缺口。
6. 理论检视取得第一优先级；局部候选、K扫描后置。
7. 方案与队列闭合即结束本次变更；不增加无关平台。
8. 本波非数学过程实验；固定对象是理论检视范围及其对选题的作用。
9. 新增前提识别的工作次序，无悖论发现增量。
10. 源文语义和关键交互尚未充分核对；先补会改变选择的盲区。

§3.1：最终链连接=准确靶前提；坐标=G0→统观回顾→P40理论检视；价值=降低方便模型支配选题；继续条件=新领域/真实语义缺口；不继续原三选一因范围过窄。裁决SWITCH_BRANCH。

§3.2：后继为P40-THEORY-INSPECTION-FIRST-001，先核C/D/S/E与Book/TC覆盖及已知缺项，再审基础判断/上下文/结构规则。App goal仍为Host报告paused，本轮不自动恢复或启动整个研究阶段。

§3.3：1根目标=同任务现实相对见证；2路径=G0→理论经济统观→PREMISE/GEN缺口→四分支→P39→统观回顾→P40理论检视；3本轮未把代理结果当原X；4撤回熟悉三前提优先；5 P1控制复用、P2/P3待理论检视形成问题、P4无触发；6树与STATE同步，按新源文或已完成覆盖证据重评。

旧SOP八项：分母为理论领域而非新有限文法；由用户原话与KC2/40/47/48锚定；无P3P4判定；负结论不外推；关键交互与扩展保留遗漏入口；原三选一由用户裁定替代；未累积互斥当前方案；反思实际改变next action。

完备性：本轮只定审查范围，未枚举候选、不声称fairness/reduction；复用TC14类与八轴、独立Book目录检查遗漏；source→解释、规则→模型是关键unknown；尚无新Holdout实验或HoTT必要性/现实桥证明。计划不得冒称覆盖已完成。
'''

def row(doc,path,id,new):
    lines=doc['shards'][path].splitlines(keepends=True)
    idx=[i for i,l in enumerate(lines) if l.startswith('| `'+id+'` |')];assert len(idx)==1
    lines[idx[0]]=new+'\n';doc['shards'][path]=''.join(lines)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    s=json.loads((ROOT/R.STATE).read_text());assert s['revision']==259
    h=json.loads((ROOT/R.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    plan=R.plan(ROOT,profile='governance');assert not plan['review_required']
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (HERE/'PLAN.json').write_bytes(R.dump(plan))
    parent=s['records'][PLAN]
    changed={p for p,v in parent['source_hashes'].items() if (ROOT/p).is_file() and sha(p)!=v}
    assert changed==set(CHANGED),changed
    for p in CHANGED+[OWNER]:parent['source_hashes'][p]=sha(p)
    parent['full_sources']=list(dict.fromkeys(parent['full_sources']+[OWNER]))
    parent['revalidation']+=' Revision260: user prioritizes sufficient theory inspection; current plan sources reviewed, previous three-premise selection superseded. No mathematical state upgrade.'
    parent['status']='theory_inspection_first';parent['evidence_status']='PRIORITY_ADOPTED / THEORY_REVIEW_PLANNED_NOT_COMPLETED'
    parent['related_records']=list(dict.fromkeys(parent['related_records']+[SID,TASK]))
    s['revision']=260;s['latest_session']=SID
    s['records'][TASK]=dict(kind='research_plan',path=OWNER,lifecycle_status='CURRENT',status='planned',evidence_status='DOCUMENTED_NOT_EXECUTED',depends_on=[],full_sources=[OWNER,'HoTT/THEORY_SCHEMA.md','HoTT/theory-schema/SOURCES_AND_COVERAGE.md'],related_records=[PLAN])
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='PLAN_AND_QUEUE_UPDATED_NO_NEW_MATH',depends_on=[],full_sources=[BASE+x for x in ('SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md')],related_records=[TASK,PLAN])
    nxt='P40-THEORY-INSPECTION-FIRST-001. First inspect HoTT theory broadly using existing Schema C/D/S/E, fixed Book chapters, PREMISE-001 and TC01-14. Reconcile source coverage with actual semantic review, audit economy/universality choices and key rule interactions, and resolve source-to-interpretation gaps before choosing targeted processes. First qualify the coverage/missing-rule map, then examine the registered C01-C03 context/structural-rule gap. Reuse exact existing controls; no duplicate delay enumeration, arbitrary three-premise shortlist, unrelated consumer scan or new platform. See overall plan shard006. Theory review is not yet complete; App goal remains observed paused.'
    s['execution_control'].update(status='P40_THEORY_INSPECTION_FIRST',current_phase='PHASE_2_THEORY_INSPECTION_BEFORE_CANDIDATES',second_phase_status='THEORY_REVIEW_FIRST_P1P2P3_FOLLOW_REVIEW_P4_TRIGGERED_ONLY',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json')
    s['projection']['status']='THEORY_INSPECTION_FIRST / CORE8_UNCHANGED / NO_NEW_MATH'
    docs={p:E.load(ROOT,p) for p in ('MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md')}
    msg='用户要求HoTT理论充分检视第一优先。P40改为THEORY-INSPECTION-FIRST：先核Schema/Book/PREMISE/TC的语义覆盖与关键交互，再选靶前提和针对过程；旧三选一后置。首步复核已有范围和缺项，随后审基础判断/上下文/结构规则。core8/48与KC47/48原文常驻要求不变；本轮仅方案/队列更新，尚未完成充分检视，无新数学claim。入口：总体方案006；revision260。App goal实测paused未操作恢复。'
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0]
    E.replace_in_shard(docs['MEMORY.md'],mp,old,msg)
    E.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：理论充分检视优先裁定落盘；P40三选一替代，core8不变；revision260。\n')
    for p,kind in [('方向追踪.md','direction'),('全景视野.md','outcome')]:
        E.replace_in_index(docs[p],'source_state_revision: 259','source_state_revision: 260')
        E.replace_in_index(docs[p],f'projection_generation: 20260922-{kind}-259',f'projection_generation: 20260923-{kind}-260')
        docs[p]['index_text']=docs[p]['index_text'].replace('CORE8_MACHINE_OVERVIEW_AUDIT_P40_PENDING','P40_THEORY_INSPECTION_FIRST')
        rec=s['records']['I-DIRECTION-PORTFOLIO-20260912' if kind=='direction' else 'I-OUTCOME-PANORAMA-20260912'];rec.update(projection_generation=f'20260923-{kind}-260',semantic_status='P40_THEORY_INSPECTION_FIRST',scope='Theory inspection before candidate selection; not yet substantively completed.')
    row(docs['方向追踪.md'],'方向追踪/002 - 治理与用户方向.md','DIR-U-HOTT-FOUR-TRACK','| `DIR-U-HOTT-FOUR-TRACK` | 理论充分检视先于候选选择与四分支验证 | 用户本轮裁定、KC2/40/47/48 | `P40_THEORY_INSPECTION_FIRST / PLANNED_NOT_COMPLETED` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-MACHINE-OVERVIEW-TARGETING-AUDIT`、`OUT-THEORY-INSPECTION-PRIORITY` | 先核Schema/Book/PREMISE/TC语义与交互覆盖，再处理基础判断/上下文/结构规则缺口 | 总体方案006；revision260 |')
    out='全景视野/002 - 治理、门禁与骨架结果.md'
    E.append_to_shard(docs['全景视野.md'],out,f'\n| `OUT-THEORY-INSPECTION-PRIORITY` | 理论充分检视第一优先的范围、顺序与验收 | `DIR-U-HOTT-FOUR-TRACK` | 用户裁定、已有Schema及统观回顾 | `DOCUMENTED_PLAN / NO_NEW_MATH_CLAIM` | 区分检视与验证模式，复用旧地图并核语义缺口 | 不证明充分检视已完成、HoTT缺陷或全局无问题 | {OWNER}；revision260 |\n')
    pp='全景视野/008 - 当前未完成.md';text=docs['全景视野.md']['shards'][pp]
    text=re.sub(r'^16\. `P40-PREMISE-TARGETED.*$', '16. `P40-THEORY-INSPECTION-FIRST-001`：先完成总体方案006声明的理论广度与关键语义检视，再排序靶前提；旧三选一不再是当前队列。',text,flags=re.M)
    text=text.replace('下一P40先核源内靶点与敏感过程，不重复旧枚举。','P40先做理论充分检视，靶点与敏感过程随后选择，不重复旧枚举。')
    docs['全景视野.md']['shards'][pp]=text
    rows=[]
    for doc in docs.values():rows+=E.payload_rows(doc,ROOT)
    seen={r['path'] for r in rows}
    for p in R.MUTABLE:
        if p in seen:continue
        text=(ROOT/p).read_text()
        if p==R.STATE:text=R.dump(s).decode()
        elif p.endswith('FRONTIER.md'):text=re.sub(r'^- 机器统观目标忠实性回顾完成：.*$','- '+msg,text,flags=re.M)
        elif p.endswith('RESUME.md'):text=re.sub(r'^机器统观目标忠实性回顾完成：.*$',msg,text,flags=re.M)
        rows.append(dict(path=p,expected_sha256=sha(p),text=text))
    manifest=json.loads((ROOT/'核心认知.manifest.json').read_text())
    audit=[f'# {SID} 核心认知回评','',f"- identity: {s['current_core']['generation']} / 48 KC",
      '- core_change: NO; 本轮是优先级裁定，原文进rulings。','- direction_change: YES; 理论充分检视取代三选一。',
      '- panorama_change: YES; 只记录方案与队列变化。','- essay_change: NO; KC47/48完整原文与阐释已存在。',
      '- update_decision: canonical checkpoint，旧研究结果不升降级。','- cross_conflicts: 旧三选一入口已原位收敛；全景旧结果保留历史。',
      '- unresolved: 理论检视待执行；模型保真/现实桥/最终见证开放；writer分片事务缺口不变。','',
      '| KC | 主题 | relation | 判断与理由 | 证据 | 下一动作与反证条件 |','|---|---|---|---|---|---|']
    for i,u in enumerate(manifest['units'],1):
        rel,why=FOCUS.get(i,('NOT_TOUCHED','本轮只改理论检视优先级，未执行本主题数学研究；原要求不变'))
        audit.append(f"| `{u['id']}` | {u['semantic_label']} | `{rel}` | {why} | 总体方案006、rulings、goal-3 | P40检视真实规则与交互；已有充分源文/保真证据则复用；具体新义务才重开未触及项 |")
    audit+=['','## 扩展认知回评','',
      '001理论简化/002前提与时间：经济选择需先被准确理解；003圆环ASK：保留原X而不以它限制全理论；004HoTT自反：Schema及关键依赖先审，不自动重开反射；005表达范围：检视不要求先有反例；006知识谱：主要理论域广度先行；007路径依赖：撤回熟悉三前提首选；008现实对齐：解释不能加强原规则；009针对过程：在理解源内前提后生效。各片未增加数学结论。','',REFLECTION]
    session=f'# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3 plan/state mutation\n- load_receipt: revision259 canonical receipt/HEAD全匹配，core8与四件套在本连续上下文保持；本轮完整重读goal-3与KC47/48并核Schema/source coverage/current owners；PLAN.json={plan["snapshot"]}。\n- status: PRIORITY_CHANGE_COMPLETE / THEORY_REVIEW_PENDING\n- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001，48KC单文件兼容bundle。\n- element_usage: core=研究意识；Schema=范围；四件套/STATE=持续路由；proof gate=防新结论越级；无新kernel/外部调用；语义检索transport closed后用rg与精确入口。\n\n影响：需求/研究方案/当前队列和历史处置变化；core、数学代码、工具链、全局AGENTS/Skills/权限/部署不变。不新建平台；仅一个现有总体方案分片。全反思见CORE_COGNITION_AUDIT。\n'
    bundle={'SESSION.md':session,'RUNS.json':R.dump(dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],kind='priority-plan-mutation')).decode(),'CORE_COGNITION_AUDIT.md':'\n'.join(audit)+'\n'}
    rows += [dict(path=BASE+p,expected_sha256=None,text=v) for p,v in bundle.items()]
    payload=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='governance',task_ids=[],authorization='用户要求理论充分检视第一优先，授权相关方案与当前队列修改；不恢复App goal、不push/tag、不启动子代理。',files=rows)
    (HERE/'PAYLOAD.json').write_bytes(R.dump(payload));res=R.checkpoint(ROOT,plan['snapshot'],payload,apply=a.apply)
    (HERE/('APPLY.json' if a.apply else 'DRY-RUN.json')).write_bytes(R.dump(res))
    print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
