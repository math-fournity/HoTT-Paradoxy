#!/usr/bin/env python3
"""Canonical P43 source-qualification checkpoint, no new proof claims."""
import argparse,hashlib,importlib.util,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
SID='S-RES-20260923-ASTRA-P43-LOGIC-REALS';BASE=f'.codex/research/hott/sessions/{SID}/'
RID='R-P43-THEORY-LOGIC-REALS-20260923';TASK='P43-LOGIC-UNIVERSES-REALS-001';NEXT='P44-DERIVED-HOMOTOPY-CATEGORIES-SETS-001'
PARENT='R-HOTT-FOUR-TRACK-PLAN-20260921';SHARD='HoTT理论充分检视/005 - P43逻辑、宇宙与实数能力.md';EVID='audit/p43-logic-reals-20260923/EVIDENCE.json'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as E
def replace_row(doc,path,key,value):
    ls=doc['shards'][path].splitlines(keepends=True);ii=[i for i,l in enumerate(ls) if l.startswith('| `'+key+'` |')];assert len(ii)==1;ls[ii[0]]=value+'\n';doc['shards'][path]=''.join(ls)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    s=json.loads((ROOT/R.STATE).read_text());assert s['revision']==263
    h=json.loads((ROOT/R.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    plan=R.plan(ROOT,profile='governance');assert not plan['review_required'];(HERE/'PLAN.json').write_bytes(R.dump(plan))
    changed={'goal.md','feature-list.md','HoTT后续研究总体方案.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md','goal-3-工作路径树/001 - 原初目标与当前工作树.md'}
    owner=s['records'][PARENT];assert {p for p,v in owner['source_hashes'].items() if (ROOT/p).is_file() and sha(p)!=v}==changed
    for p in changed:owner['source_hashes'][p]=sha(p)
    owner['revalidation']+=' Revision264: P43 logic/universe/reals source qualification and next P44; no mathematical claim upgrade.'
    owner['status']='theory_inspection_in_progress';owner['evidence_status']='P43_SOURCE_REVIEWED / P44_NEXT / GOAL_ACTIVE';owner['related_records']=list(dict.fromkeys(owner['related_records']+[RID,NEXT,SID]))
    s['records'][TASK].update(lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE',resolution={'reason':'Logic/universe/reals review completed; derived homotopy/category/set use continues in P44.','evidence':[SHARD,EVID]})
    s['records'][RID]=dict(kind='result',path=SHARD,lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH',depends_on=[],full_sources=[SHARD,EVID],source_hashes={p:sha(p) for p in [SHARD,EVID]},related_records=[TASK])
    s['records'][NEXT]=dict(kind='research_task',path='HoTT理论充分检视.md',lifecycle_status='CURRENT',status='ready',evidence_status='NOT_EXECUTED',depends_on=[],full_sources=[SHARD,'HoTT/theory-schema/DERIVED_STRUCTURES.md'],related_records=[RID])
    s['records']['A-PREMISE-001']['source_qualification']+=' P43: F2-7 necessity attribution exceeds Book four options; smallness, mathematical completeness, decidability and physical completion separated; original source/run bytes retained.'
    s['records']['P40-THEORY-INSPECTION-FIRST-001']['evidence_status']='FOUNDATIONS_IDENTITY_CONSTRUCTION_LOGIC_REALS_SOURCE_REVIEWED / OTHER_FAMILIES_OPEN'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='P43_REFLECTION_COMPLETE',depends_on=[],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']],related_records=[RID,NEXT])
    s['revision']=264;s['latest_session']=SID
    nxt='P44-DERIVED-HOMOTOPY-CATEGORIES-SETS-001. Inspect synthetic homotopy objects/observations, modalities and Whitehead boundaries, category/SIP/Rezk and cumulative set hierarchy actual dependencies. Reuse P41 SIP and prior native controls; then complete computation/metatheory/models and related extension review plus justified global candidate ranking. No premature goal completion.'
    s['execution_control'].update(status='THEORY_INSPECTION_P43_COMPLETE_P44_NEXT',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_status_observed='active')
    s['projection']['status']='THEORY_INSPECTION_IN_PROGRESS / P43_LOGIC_REALS / P44_NEXT / GOAL_ACTIVE'
    docs={p:E.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    msg='第006片检视推进到P43：LEM/AC/resizing、Ω四路线、Dedekind/Cauchy实数及模数/HIIT/紧致性能力已按声明范围回源；旧F2-7必要性归因收窄，第四弹/P17复用，Schema两处术语纠正。下一P44审派生同伦/范畴/集合；模型、扩展、最终排序仍开放，无新数学claim，active goal继续。入口：HoTT理论充分检视005；revision264。'
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];E.replace_in_shard(docs['MEMORY.md'],mp,old,msg)
    E.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：P43十一文件来源及逻辑/实数能力分析；第四弹/P17复用；P44下一；revision264。\n')
    for p,kind in [('方向追踪.md','direction'),('全景视野.md','outcome')]:
        E.replace_in_index(docs[p],'source_state_revision: 263','source_state_revision: 264');E.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-263',f'projection_generation: 20260923-{kind}-264');docs[p]['index_text']=docs[p]['index_text'].replace('THEORY_INSPECTION_P42_REVIEWED_P43_NEXT','THEORY_INSPECTION_P43_REVIEWED_P44_NEXT')
        s['records']['I-DIRECTION-PORTFOLIO-20260912' if kind=='direction' else 'I-OUTCOME-PANORAMA-20260912'].update(projection_generation=f'20260923-{kind}-264',semantic_status='THEORY_INSPECTION_P43_REVIEWED_P44_NEXT',scope='P43 logic/reals source review complete; P44 next; whole theory review ongoing.')
    d='方向追踪/002 - 治理与用户方向.md'
    replace_row(docs['方向追踪.md'],d,'DIR-U-HOTT-FOUR-TRACK','| `DIR-U-HOTT-FOUR-TRACK` | 理论检视P43完成、P44派生理论下一 | active goal、KC2/40/47/48 | `IN_PROGRESS / P44_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P43-THEORY-LOGIC-REALS`、`OUT-P42-THEORY-CONSTRUCTION` | 核合成同伦/模态/范畴/集合实际使用，继续广度 | HoTT理论充分检视；revision264 |')
    replace_row(docs['方向追踪.md'],d,'DIR-TOP-PREMISE-INVENTORY','| `DIR-TOP-PREMISE-INVENTORY` | 历史前提的来源资格持续复审 | KC44–48与P40–P43 | `HISTORICAL_INVENTORY / SOURCE_SCOPE_CORRECTED` | `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P43-THEORY-LOGIC-REALS`、`OUT-P42-THEORY-CONSTRUCTION` | F2-7须分开Ω/逻辑/实数/有效能力；旧Id与构造纠偏保留，不重跑旧GEN | PREMISE索引；HoTT理论充分检视003–005 |')
    E.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-P43-THEORY-LOGIC-REALS` | 逻辑/宇宙/实数的条件与能力审查 | `DIR-U-HOTT-FOUR-TRACK`、`DIR-TOP-PREMISE-INVENTORY` | Book/TypeTopology/P17复用/11文件 | `SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH` | Ω四路线、modulus与HIIT、紧致性证据分层；旧F2-7归因收窄 | 不证明Necessity真值、实数现实失配或全部现代语义；未重放旧核结果 | {SHARD}；revision264 |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^16\. 理论充分检视继续：.*$','16. 理论充分检视继续：P40–P43源文范围完成，下一P44核派生同伦/范畴/集合；模型与扩展及全局排序仍开放。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for doc in docs.values():rows+=E.payload_rows(doc,ROOT)
    seen={r['path'] for r in rows}
    for p in R.MUTABLE:
        if p in seen:continue
        t=(ROOT/p).read_text()
        if p==R.STATE:t=R.dump(s).decode()
        elif p.endswith('FRONTIER.md'):t=re.sub(r'^- 第006片检视推进到P42：.*$','- '+msg,t,flags=re.M)
        elif p.endswith('RESUME.md'):t=re.sub(r'^第006片检视推进到P42：.*$',msg,t,flags=re.M)
        rows.append(dict(path=p,expected_sha256=sha(p),text=t))
    m=json.loads((ROOT/'核心认知.manifest.json').read_text());focus={2:'沿理论地图补逻辑与分析关键依赖',3:'额外逻辑前提显式保留',5:'不预判非现实根因',9:'宇宙与计算能力分层',10:'来源限界不冒充内部矛盾',14:'极限存在与过程交付分开',15:'保留强哲学起点而不自证',18:'Ω记账与HIIT有具体经济收益',21:'无新kernel结果',22:'已完成数学对象与物理完成分开',29:'额外原则的作用点准确化',30:'不同经济选择不合并成费用',31:'数学构造能表达相容条件',35:'没有从新实数任务推出圆环命中',37:'发现预期与未取得见证仍有张力',38:'作者明确收益不猜心理',39:'旧F2-7基础叙述被源文复核',40:'Schema中的HIIT术语被纠正',43:'P17和第四弹不重做',44:'现实任务可继续设计',45:'需要真实能力桥',47:'原文整段已读并按条件敏感性检视',48:'modulus/located/cover成为精确入口而非无靶枚举'}
    aud=[f'# {SID} 核心认知审计','',f"- identity: {s['current_core']['generation']} / 48 KC",'- core_change: NO','- direction_change: YES; P43逻辑/实数源文完成、P44下一。','- panorama_change: YES; 仅来源审计与范围纠偏。','- essay_change: NO','- update_decision: checkpoint并更新PREMISE索引与Schema两处术语，不改冻结原件。','- cross_conflicts: F2-7的必需Ω/判定完成归因超出源文；Schema HIIT术语已纠正。','- unresolved: 其他理论领域和现实桥开放；writer分片事务兼容缺口不变。','','| KC | 主题 | relation | 立场与理由 | 证据 | 后继及反证条件 |','|---|---|---|---|---|---|']
    for i,u in enumerate(m['units'],1):
        rel='TENSION' if i==37 else 'ALIGNED' if i in focus else 'NOT_TOUCHED';why=focus.get(i,'本wave限定逻辑/宇宙/实数来源资格，未检验此主题数学命题')
        aud.append(f"| `{u['id']}` | {u['semantic_label']} | `{rel}` | {why} | {SHARD} | P44继续下一领域；若精确源文支持旧必要性归因或新保真桥出现则重评；未触及项不外推 |")
    aud+=['','## 扩展认知与全波次反思','001Ω/HIIT收益明确；002modulus/located/cover条件保留；003原X未替换；004逻辑/实数回源；005mere与数据分层；006F2-7和Schema纠正；007P17/第四弹不重做；008现实桥仍开放；009靶前提由能力差别细化。',f'完整Goal-3十问/五项价值/六项航向、SOP八项与覆盖回评在{SHARD} §7。CLOSE_WITH_SCOPE后active goal继续P44。','', '## 加载与证据边界','core8与四件套按PROTOCOL v3复认revision263收据，HEAD.tracked无hash变化；本审计逐48KC登记立场，抽查KC47/48完整原文并完整重读goal-3。Book/PREMISE按EVIDENCE精确段落读取；goal3/KC47–48每波重读；P41 logic与P17来源按既有范围复用。本wave没有新的proof claim或kernel run，原始数学结论不由源文审查提升。完整48KC单文件兼容审计，非嵌套分片事务。']
    ses=f'# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3 research/state\n- load_receipt: revision263收据复认及HEAD.tracked哈希一致；PLAN.json={plan["snapshot"]}；goal3与KC47/48完整重读。\n- status: P43_SOURCE_REVIEW_COMPLETE\n- authorization: 用户active goal完成006，本地研究与checkpoint；禁Sub Agent/push/tag。\n- element_usage: core/SOP=航向；Book/TypeTopology/实数论文=来源；PREMISE=被审对象；旧源码=控制查重；STATE=接续；无新kernel。\n- next: {NEXT}\n\nreflection=no-plan-change；完整反思与影响见{SHARD}。\n'
    bundle={'SESSION.md':ses,'RUNS.json':R.dump(dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],evidence=EVID)).decode(),'CORE_COGNITION_AUDIT.md':'\n'.join(aud)+'\n'}
    rows += [dict(path=BASE+p,expected_sha256=None,text=t) for p,t in bundle.items()]
    pay=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='governance',task_ids=[],authorization='用户active goal执行006，P43源文审查及反思完成，接P44；不push/tag。',files=rows)
    (HERE/'PAYLOAD.json').write_bytes(R.dump(pay));res=R.checkpoint(ROOT,plan['snapshot'],pay,apply=a.apply);(HERE/('APPLY.json' if a.apply else 'DRY-RUN.json')).write_bytes(R.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
