#!/usr/bin/env python3
"""Canonical P45 source-qualification checkpoint, no new proof claims."""
import argparse,hashlib,importlib.util,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
SID='S-RES-20260923-ASTRA-P45-METATHEORY';BASE=f'.codex/research/hott/sessions/{SID}/'
RID='R-P45-THEORY-METATHEORY-20260923';TASK='P45-COMPUTATION-METATHEORY-MODELS-001';NEXT='P46-CUBICAL-AND-EXTENSION-BOUNDARIES-001'
PARENT='R-HOTT-FOUR-TRACK-PLAN-20260921';SHARD='HoTT理论充分检视/007 - P45计算、元理论与模型保证.md';EVID='audit/p45-metatheory-models-20260923/EVIDENCE.json'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as E
def replace_row(doc,path,key,value):
    ls=doc['shards'][path].splitlines(keepends=True);ii=[i for i,l in enumerate(ls) if l.startswith('| `'+key+'` |')];assert len(ii)==1;ls[ii[0]]=value+'\n';doc['shards'][path]=''.join(ls)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    s=json.loads((ROOT/R.STATE).read_text());assert s['revision']==265
    h=json.loads((ROOT/R.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    plan=R.plan(ROOT,profile='governance');assert not plan['review_required'];(HERE/'PLAN.json').write_bytes(R.dump(plan))
    changed={'goal.md','feature-list.md','HoTT后续研究总体方案.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md','goal-3-工作路径树/001 - 原初目标与当前工作树.md'}
    owner=s['records'][PARENT];assert {p for p,v in owner['source_hashes'].items() if (ROOT/p).is_file() and sha(p)!=v}==changed
    for p in changed:owner['source_hashes'][p]=sha(p)
    owner['revalidation']+=' Revision264: P45 computational and model guarantee source qualification and next P46; no mathematical claim upgrade.'
    owner['status']='theory_inspection_in_progress';owner['evidence_status']='P45_SOURCE_REVIEWED / P46_NEXT / GOAL_ACTIVE';owner['related_records']=list(dict.fromkeys(owner['related_records']+[RID,NEXT,SID]))
    s['records'][TASK].update(lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE',resolution={'reason':'Computation/metatheory/model scopes reviewed; concrete Cubical and extensions continue in P46.','evidence':[SHARD,EVID]})
    s['records'][RID]=dict(kind='result',path=SHARD,lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH',depends_on=[],full_sources=[SHARD,EVID],source_hashes={p:sha(p) for p in [SHARD,EVID]},related_records=[TASK])
    s['records'][NEXT]=dict(kind='research_task',path='HoTT理论充分检视.md',lifecycle_status='CURRENT',status='ready',evidence_status='NOT_EXECUTED',depends_on=[],full_sources=[SHARD,'HoTT/theory-schema/SEMANTICS_AND_COHERENCE.md','HoTT/theory-schema/EXTENSIONS_AND_METATHEORY.md'],related_records=[RID])
    s['records']['A-PREMISE-001']['source_qualification']+=' P45: B01 decidability does not source an all-system inability to express observation; B02 symbolic beta is not a physical zero-time guarantee; exact calculus scopes retained.'
    s['records']['P40-THEORY-INSPECTION-FIRST-001']['evidence_status']='FOUNDATIONS_DERIVED_AND_METATHEORY_SOURCE_REVIEWED / OTHER_FAMILIES_OPEN'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='P45_REFLECTION_COMPLETE',depends_on=[],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']],related_records=[RID,NEXT])
    s['revision']=266;s['latest_session']=SID
    nxt='P46-CUBICAL-AND-EXTENSION-BOUNDARIES-001. Inspect precise interval/face/composition/Glue rules and relevant guarded/clocked/directed/cohesive/2LTT/cost/internal-model/categorical-univalence extension contracts. Reuse existing native controls and prior source audits; no general reflection reruns. Then finish declared-scope cross-family audit and justified candidate ranking required by overall006; goal remains active.'
    s['execution_control'].update(status='THEORY_INSPECTION_P45_COMPLETE_P46_NEXT',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_status_observed='active')
    s['projection']['status']='THEORY_INSPECTION_IN_PROGRESS / P45_METATHEORY / P46_NEXT / GOAL_ACTIVE'
    docs={p:E.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    msg='第006片检视推进到P45：Book/cubical计算性质、模型/相干性/initiality保证已按精确来源范围分层；B01全系统不可表达与B02物理瞬时归因撤回。下一P46核Cubical具体规则和相关扩展；之后整体验收与排序。无新数学claim，active goal继续。入口：HoTT理论充分检视007；revision266。'
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];E.replace_in_shard(docs['MEMORY.md'],mp,old,msg)
    E.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：P45十一文件来源及逻辑/实数能力分析；第四弹/P17复用；P46下一；revision264。\n')
    for p,kind in [('方向追踪.md','direction'),('全景视野.md','outcome')]:
        E.replace_in_index(docs[p],'source_state_revision: 265','source_state_revision: 266');E.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-265',f'projection_generation: 20260923-{kind}-266');docs[p]['index_text']=docs[p]['index_text'].replace('THEORY_INSPECTION_P44_REVIEWED_P45_NEXT','THEORY_INSPECTION_P45_REVIEWED_P46_NEXT')
        s['records']['I-DIRECTION-PORTFOLIO-20260912' if kind=='direction' else 'I-OUTCOME-PANORAMA-20260912'].update(projection_generation=f'20260923-{kind}-266',semantic_status='THEORY_INSPECTION_P45_REVIEWED_P46_NEXT',scope='P45 metatheory source review complete; P46 next; whole theory review ongoing.')
    d='方向追踪/002 - 治理与用户方向.md'
    replace_row(docs['方向追踪.md'],d,'DIR-U-HOTT-FOUR-TRACK','| `DIR-U-HOTT-FOUR-TRACK` | 理论检视P45完成、P46Cubical/扩展下一 | active goal、KC2/40/47/48 | `IN_PROGRESS / P46_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P45-THEORY-METATHEORY`、`OUT-P44-THEORY-DERIVED` | 核具体扩展规则与条件，再整体排序 | HoTT理论充分检视；revision266 |')
    replace_row(docs['方向追踪.md'],d,'DIR-TOP-PREMISE-INVENTORY','| `DIR-TOP-PREMISE-INVENTORY` | 历史前提的来源资格持续复审 | KC44–48与P40–P45 | `HISTORICAL_INVENTORY / SOURCE_SCOPE_CORRECTED` | `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P45-THEORY-METATHEORY`、`OUT-P43-THEORY-LOGIC-REALS` | B01不能由判定界限推不可表达，B02非瞬时物理承诺；其余旧纠偏保持，不重跑GEN | PREMISE索引；HoTT理论充分检视003–007 |')
    E.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-P45-THEORY-METATHEORY` | 计算/语义/初始性保证范围核对 | `DIR-U-HOTT-FOUR-TRACK`、`DIR-TOP-PREMISE-INVENTORY` | Book/元理论论文/6本地文件 | `SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH` | 检查/归约/搜索、模型/语法分层；B01/B02归因纠正 | 不证明全HoTT一致性或实现正确性；无新核结果和现实桥 | {SHARD}；revision266 |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^16\. 理论充分检视继续：.*$','16. 理论充分检视继续：P40–P45源文范围完成，下一P46核Cubical/相关扩展；整体验收与全局排序仍开放。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for doc in docs.values():rows+=E.payload_rows(doc,ROOT)
    seen={r['path'] for r in rows}
    for p in R.MUTABLE:
        if p in seen:continue
        t=(ROOT/p).read_text()
        if p==R.STATE:t=R.dump(s).decode()
        elif p.endswith('FRONTIER.md'):t=re.sub(r'^- 第006片检视推进到P44：.*$','- '+msg,t,flags=re.M)
        elif p.endswith('RESUME.md'):t=re.sub(r'^第006片检视推进到P44：.*$',msg,t,flags=re.M)
        rows.append(dict(path=p,expected_sha256=sha(p),text=t))
    m=json.loads((ROOT/'核心认知.manifest.json').read_text());focus={2:'理论地图补元理论范围',3:'模型与计算定理前提明确',5:'具体反差先于归因',9:'计算与物理时间分开',10:'模型限界不是内部矛盾',12:'检查与搜索资格区分',15:'强哲学起点仍可反驳',18:'语法接口与模型简化有实际收益',21:'无新kernel数学结果',24:'内部证明与元层解释分开',25:'正规化不等于任意程序停机',26:'核验与全域真理不混同',27:'一般计算界限不冒充HoTT独有',28:'未重开无具体对象桥的反射线',29:'理论经济性需连具体任务',30:'元理论相干性方法回源',31:'判定界限不等于不可表达',35:'未把一般元理论当原X命中',36:'已有R3不等于HoTT R4',37:'最终见证未得的张力保留',38:'来源范围取代心理推断',39:'基础B01/B02归因被复核',40:'知识谱须受直接来源修正',43:'不重复一般R3或2LTT',44:'现实解释仍是合法研究问题',45:'模型不是物理桥',47:'经济收益及省略条件准确化',48:'靶前提须为所选演算实际规则'}
    aud=[f'# {SID} 核心认知审计','',f"- identity: {s['current_core']['generation']} / 48 KC",'- core_change: NO','- direction_change: YES; P45计算/模型源文完成、P46下一。','- panorama_change: YES; 仅来源审计与范围纠偏。','- essay_change: NO','- update_decision: checkpoint及理论覆盖/树/PREMISE资格更新；不改冻结源文或旧run。','- cross_conflicts: 旧B01不可表达与B02瞬时归因无规则支持；元定理演算范围不得外推。','- unresolved: 其他理论领域和现实桥开放；writer分片事务兼容缺口不变。','','| KC | 主题 | relation | 立场与理由 | 证据 | 后继及反证条件 |','|---|---|---|---|---|---|']
    for i,u in enumerate(m['units'],1):
        rel='TENSION' if i==37 else 'ALIGNED' if i in focus else 'NOT_TOUCHED';why=focus.get(i,'本wave限定计算/元理论/模型来源资格，未检验此主题数学命题')
        aud.append(f"| `{u['id']}` | {u['semantic_label']} | `{rel}` | {why} | {SHARD} | P46继续下一领域；若精确来源提供无条件强桥或新同任务反例则重评；未触及项不外推 |")
    aud+=['','## 扩展认知与全波次反思','001模型/计算接口收益；002精确元定理条件；003原X不替换；004实际calculus回源；005检查/搜索/语义分层；006旧B01/B02修正；007不重做R3/2LTT；008模型非现实桥；009靶前提真实才有针对性。',f'完整Goal-3十问/五项价值/六项航向、SOP八项与覆盖回评在{SHARD} §7。CLOSE_WITH_SCOPE后active goal继续P46。','', '## 加载与证据边界','core8与四件套按PROTOCOL v3复认revision263收据，HEAD.tracked无hash变化；本审计逐48KC登记立场，抽查KC47/48完整原文并完整重读goal-3。Book/PREMISE按EVIDENCE精确段落读取；goal3/KC47–48每波重读；既有R3矩阵与P41/P44结构合同按范围复用。本wave没有新的proof claim或kernel run，原始数学结论不由源文审查提升。完整48KC单文件兼容审计，非嵌套分片事务。']
    ses=f'# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3 research/state\n- load_receipt: revision263收据复认及HEAD.tracked哈希一致；PLAN.json={plan["snapshot"]}；goal3与KC47/48完整重读。\n- status: P45_SOURCE_REVIEW_COMPLETE\n- authorization: 用户active goal完成006，本地研究与checkpoint；禁Sub Agent/push/tag。\n- element_usage: core/SOP=航向；Book/计算与模型论文=来源；PREMISE=被审对象；旧源码=控制查重；STATE=接续；无新kernel。\n- next: {NEXT}\n\nreflection=no-plan-change；完整反思与影响见{SHARD}。\n'
    bundle={'SESSION.md':ses,'RUNS.json':R.dump(dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],evidence=EVID)).decode(),'CORE_COGNITION_AUDIT.md':'\n'.join(aud)+'\n'}
    rows += [dict(path=BASE+p,expected_sha256=None,text=t) for p,t in bundle.items()]
    pay=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='governance',task_ids=[],authorization='用户active goal执行006，P45源文审查及反思完成，接P46；不push/tag。',files=rows)
    (HERE/'PAYLOAD.json').write_bytes(R.dump(pay));res=R.checkpoint(ROOT,plan['snapshot'],pay,apply=a.apply);(HERE/('APPLY.json' if a.apply else 'DRY-RUN.json')).write_bytes(R.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
