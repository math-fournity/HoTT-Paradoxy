#!/usr/bin/env python3
"""Record P40 source inspection and the next theory family, using canonical writer."""
import argparse,hashlib,importlib.util,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
SID='S-RES-20260923-ASTRA-P40-THEORY-FOUNDATIONS';BASE=f'.codex/research/hott/sessions/{SID}/'
RID='R-P40-THEORY-FOUNDATIONS-20260923';NEXT='P41-IDENTITY-EQUIVALENCE-PREMISE-QUALIFICATION-001'
PARENT='R-HOTT-FOUR-TRACK-PLAN-20260921';REPORT='HoTT理论充分检视.md'
SHARD='HoTT理论充分检视/002 - P40基础判断、上下文与结构规则.md'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as E

def replace_row(doc,path,key,value):
    lines=doc['shards'][path].splitlines(keepends=True);ix=[i for i,l in enumerate(lines) if l.startswith('| `'+key+'` |')];assert len(ix)==1
    lines[ix[0]]=value+'\n';doc['shards'][path]=''.join(lines)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    s=json.loads((ROOT/R.STATE).read_text());assert s['revision']==260
    h=json.loads((ROOT/R.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    plan=R.plan(ROOT,profile='governance');assert not plan['review_required']
    (HERE/'PLAN.json').write_bytes(R.dump(plan))
    changed={'goal.md','feature-list.md','HoTT后续研究总体方案.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md','HoTT后续研究总体方案/006 - 理论充分检视的首轮范围与验收.md','goal-3-工作路径树/001 - 原初目标与当前工作树.md'}
    owner=s['records'][PARENT];actual={p for p,v in owner['source_hashes'].items() if (ROOT/p).is_file() and sha(p)!=v};assert actual==changed,actual
    for p in changed:owner['source_hashes'][p]=sha(p)
    owner['revalidation']+=' Revision261: P40 primary source review and coverage checks; current progress owners updated, no new math claim.'
    owner['status']='theory_inspection_in_progress';owner['evidence_status']='P40_SOURCE_FOUNDATIONS_REVIEWED / P41_IDENTITY_NEXT / GOAL_ACTIVE'
    owner['related_records']=list(dict.fromkeys(owner['related_records']+[RID,NEXT,SID]))
    s['revision']=261;s['latest_session']=SID
    refs=[REPORT,'HoTT理论充分检视/001 - 范围、来源与全局覆盖.md',SHARD,str((HERE/'EVIDENCE.json').relative_to(ROOT))]
    s['records'][RID]=dict(kind='result',path=SHARD,lifecycle_status='CLOSED',status='source_inspected_with_scope',evidence_status='SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH_CLAIM',depends_on=[],full_sources=refs,source_hashes={p:sha(p) for p in refs},related_records=['P40-THEORY-INSPECTION-FIRST-001'])
    s['records'][NEXT]=dict(kind='research_task',path=REPORT,lifecycle_status='CURRENT',status='ready',evidence_status='NOT_EXECUTED',depends_on=[],full_sources=[SHARD,'.codex/research/hott/PREMISE-001/001 - 分母 V1 冻结（A-G 条目、P1 前提与出处）.md','HoTT/theory-schema/CORE_RULES.md','HoTT/theory-schema/upstream/book-578b85cc/logic.tex'],related_records=[RID])
    s['records']['P40-THEORY-INSPECTION-FIRST-001'].update(status='in_progress',evidence_status='FOUNDATIONS_SOURCE_REVIEWED / REMAINING_FAMILIES_OPEN',related_records=[PARENT,RID,NEXT])
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='P40_SOURCE_REVIEW_WITH_REFLECTION',depends_on=[],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']],related_records=[RID,NEXT])
    nxt='P41-IDENTITY-EQUIVALENCE-PREMISE-QUALIFICATION-001. Audit Id/set, equivalence/ua/funext, judgmental versus propositional eta and structure observations against fixed Book sources. Resolve PREMISE-C-01/G-02 source contradiction and inspect dependencies in P2/P3P4/SUPPLY; preserve frozen originals. Reuse exact native controls where relevant, do not start another delay model. Continue other theory families after this wave; whole006 review remains incomplete.'
    s['execution_control'].update(status='THEORY_INSPECTION_P40_COMPLETE_P41_NEXT',current_phase='PHASE_2_THEORY_INSPECTION',app_goal_status_observed='active',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json')
    s['projection']['status']='THEORY_INSPECTION_IN_PROGRESS / P40_FOUNDATIONS / P41_NEXT / GOAL_ACTIVE'
    docs={p:E.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    msg='第006片active goal已开始。P40核对21来源/105节入口，并完成C01–C04基础源文检视：条件性假设不等于物理同时生产，结构原则不直接给瞬时零成本。PREMISE-C-01/G-02与Book的set限定冲突已定位；下一P41核Id/等价/ua/η及旧依赖。其余理论领域仍开放，未完成总Goal，无新数学claim。结果：HoTT理论充分检视001/002；revision261。'
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];E.replace_in_shard(docs['MEMORY.md'],mp,old,msg)
    E.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：P40来源与基础规则审查完成；C01/G02待P41资格化；active goal继续；revision261。\n')
    for p,kind in [('方向追踪.md','direction'),('全景视野.md','outcome')]:
        E.replace_in_index(docs[p],'source_state_revision: 260','source_state_revision: 261');E.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-260',f'projection_generation: 20260923-{kind}-261')
        docs[p]['index_text']=docs[p]['index_text'].replace('P40_THEORY_INSPECTION_FIRST','THEORY_INSPECTION_P40_REVIEWED_P41_NEXT')
        rr=s['records']['I-DIRECTION-PORTFOLIO-20260912' if kind=='direction' else 'I-OUTCOME-PANORAMA-20260912'];rr.update(projection_generation=f'20260923-{kind}-261',semantic_status='THEORY_INSPECTION_P40_REVIEWED_P41_NEXT',scope='P40 primary source foundations reviewed; P41 next; full review ongoing.')
    replace_row(docs['方向追踪.md'],'方向追踪/002 - 治理与用户方向.md','DIR-U-HOTT-FOUR-TRACK','| `DIR-U-HOTT-FOUR-TRACK` | 理论充分检视：P40基础层完成，P41同一性资格审查 | active goal、KC2/40/47/48 | `IN_PROGRESS / P41_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P40-THEORY-FOUNDATIONS`、`OUT-THEORY-INSPECTION-PRIORITY` | 核C-01/G-02与Id/set、ua及η源内条件，不扩delay模型 | HoTT理论充分检视；revision261 |')
    E.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-P40-THEORY-FOUNDATIONS` | 理论来源核对与C01–C04基础源文检视 | `DIR-U-HOTT-FOUR-TRACK` | 固定Book/Schema/PREMISE及QTT对照 | `SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH` | 21来源/105入口身份通过；基础物理免费解释收窄；Id/set冲突进入P41 | 不证明整个理论检视完成、HoTT缺陷或资源不可表达 | {SHARD}；revision261 |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^16\. `P40-THEORY.*$','16. 理论充分检视继续：P40来源与基础层完成，下一P41审Id/set、等价/ua、η及相关旧前提；其他领域仍按总体方案006推进。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for doc in docs.values():rows+=E.payload_rows(doc,ROOT)
    seen={r['path'] for r in rows}
    for p in R.MUTABLE:
        if p in seen:continue
        t=(ROOT/p).read_text()
        if p==R.STATE:t=R.dump(s).decode()
        elif p.endswith('FRONTIER.md'):t=re.sub(r'^- 用户要求HoTT理论充分检视第一优先。.*$','- '+msg,t,flags=re.M)
        elif p.endswith('RESUME.md'):t=re.sub(r'^用户要求HoTT理论充分检视第一优先。.*$',msg,t,flags=re.M)
        rows.append(dict(path=p,expected_sha256=sha(p),text=t))
    m=json.loads((ROOT/'核心认知.manifest.json').read_text())
    focus={1:'三问的依据回到原规则',2:'Schema与源文分开审',3:'合取前提不是物理资源自动到位',5:'尚无最终归因，先准确识别前提',9:'HoTT设定与解释加强分开',10:'现实相对目标不被类型拒绝替代',11:'上下文有依赖顺序，仍非物理时间',12:'ASK前提与推导资格在原文可定位',15:'哲学起点保留而不自证',18:'经济性解释需与源内规则区分',21:'源文审查不冒充新机器证明',24:'资源时序不吞掉运动时间',29:'经济选择定位到上下文坐标',30:'当前理论经济审视有源内对象',31:'表达限制不由缺时标推断',37:'未找到悖论与快速发现预期保持张力',38:'实际规则先于作者心理推测',39:'回基础发现我们自己的前提误读',40:'知识谱被审，不作真值权威',43:'拒绝继续熟悉delay后端',44:'现实任务可提出但要解释桥',45:'省略与已有条件同时检查',46:'实际源文对齐动作已执行',47:'完整原文重读且用于检视',48:'先核前提真实性才能针对构造'}
    aud=[f'# {SID} 48KC审计','',f"- identity: {s['current_core']['generation']} / 48 KC",'- core_change: NO','- direction_change: YES; P40基础层完成，P41由源文冲突触发。','- panorama_change: YES; 源文结果非数学定理。','- essay_change: NO; 方法应用到源文。','- update_decision: canonical checkpoint；原件保留。','- cross_conflicts: F1解释加强收窄；PREMISE-C-01/G-02待P41。','- unresolved: 总体006尚未完成，现实桥/模型保真/最终见证仍开放。','','| KC | 主题 | relation | 本轮姿态与理由 | 证据 | 后继及反证条件 |','|---|---|---|---|---|---|']
    for i,u in enumerate(m['units'],1):
        rel='TENSION' if i==37 else 'ALIGNED' if i in focus else 'NOT_TOUCHED';why=focus.get(i,'本wave限定基础源文审查，未检验此主题的数学命题')
        aud.append(f"| `{u['id']}` | {u['semantic_label']} | `{rel}` | {why} | {SHARD} | 若原规则/真实解释桥支持旧强读法则重评；P41核同一性，未触及项按后续领域进入 |")
    aud+=['','## 扩展认知逐片回评','001理论简化：不猜作者心理；002前提时间：逻辑可用非物理到位；003ASK：规则前提不能越级；004HoTT：源内规则先审；005表达：不以字段缺失证不可能；006知识谱：识别C01/G02误读；007路径依赖：不扩delay；008现实对齐：桥仍需固定；009针对过程：先有准确靶点。','', '## 全波次反思与选择',f'完整Goal-3十问、五项价值、六项航向、SOP八项和八轴遗漏见{SHARD} §6。裁决CLOSE_WITH_SCOPE，active goal立刻接P41；这不是总体完成。', '', '## 加载与兼容','沿用revision260收据与同连续上下文四件套，重读完整goal-3和KC47/48；research task plan无query-first提升。数学源码未改。writer仍以完整48KC单文件审计兼容；不伪称嵌套分片事务完成。']
    ses=f'# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3 research/state\n- status: P40_SOURCE_REVIEW_COMPLETE_WITH_SCOPE\n- load_receipt: revision260 baseline, PLAN.json snapshot {plan["snapshot"]}; explicit research task hydration inspected.\n- authorization: 用户“开始”及更新active goal要求完成总体方案006；本地研究、证据与checkpoint，禁Sub Agent/push/tag。\n- element_usage: core/goal3=航向；Schema/source=理论实际；旧证据=查重；STATE=接续；proof gate=防源文越级；论文=独立taxonomy。\n- result: {RID}\n- next: {NEXT}\n\n完整反思见{SHARD}。本波无方法变化，reflection=no-plan-change。\n'
    bundle={'SESSION.md':ses,'RUNS.json':R.dump(dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],evidence='audit/p40-theory-inspection-20260923/EVIDENCE.json')).decode(),'CORE_COGNITION_AUDIT.md':'\n'.join(aud)+'\n'}
    rows += [dict(path=BASE+p,expected_sha256=None,text=t) for p,t in bundle.items()]
    pay=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='governance',task_ids=[],authorization='用户active goal执行总体方案006，P40已源文审查并反思，登记下一P41；不push/tag。',files=rows)
    (HERE/'PAYLOAD.json').write_bytes(R.dump(pay));res=R.checkpoint(ROOT,plan['snapshot'],pay,apply=a.apply);(HERE/('APPLY.json' if a.apply else 'DRY-RUN.json')).write_bytes(R.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
