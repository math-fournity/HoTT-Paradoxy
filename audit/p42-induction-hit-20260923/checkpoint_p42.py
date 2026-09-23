#!/usr/bin/env python3
"""Canonical P42 source-qualification checkpoint, no new proof claims."""
import argparse,hashlib,importlib.util,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
SID='S-RES-20260923-ASTRA-P42-CONSTRUCTION';BASE=f'.codex/research/hott/sessions/{SID}/'
RID='R-P42-THEORY-CONSTRUCTION-20260923';TASK='P42-INDUCTION-HIT-TRUNCATION-001';NEXT='P43-LOGIC-UNIVERSES-REALS-001'
PARENT='R-HOTT-FOUR-TRACK-PLAN-20260921';SHARD='HoTT理论充分检视/004 - P42归纳、HIT、截断与构造资格.md';EVID='audit/p42-induction-hit-20260923/EVIDENCE.json'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as E
def replace_row(doc,path,key,value):
    ls=doc['shards'][path].splitlines(keepends=True);ii=[i for i,l in enumerate(ls) if l.startswith('| `'+key+'` |')];assert len(ii)==1;ls[ii[0]]=value+'\n';doc['shards'][path]=''.join(ls)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    s=json.loads((ROOT/R.STATE).read_text());assert s['revision']==262
    h=json.loads((ROOT/R.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    plan=R.plan(ROOT,profile='governance');assert not plan['review_required'];(HERE/'PLAN.json').write_bytes(R.dump(plan))
    changed={'goal.md','feature-list.md','HoTT后续研究总体方案.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md','goal-3-工作路径树/001 - 原初目标与当前工作树.md'}
    owner=s['records'][PARENT];assert {p for p,v in owner['source_hashes'].items() if (ROOT/p).is_file() and sha(p)!=v}==changed
    for p in changed:owner['source_hashes'][p]=sha(p)
    owner['revalidation']+=' Revision263: P42 construction/elimination source qualification and next P43; no mathematical claim upgrade.'
    owner['status']='theory_inspection_in_progress';owner['evidence_status']='P42_SOURCE_REVIEWED / P43_NEXT / GOAL_ACTIVE';owner['related_records']=list(dict.fromkeys(owner['related_records']+[RID,NEXT,SID]))
    s['records'][TASK].update(lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE',resolution={'reason':'Induction/HIT/truncation source review completed; logic/universes/reals continue in P43.','evidence':[SHARD,EVID]})
    s['records'][RID]=dict(kind='result',path=SHARD,lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH',depends_on=[],full_sources=[SHARD,EVID],source_hashes={p:sha(p) for p in [SHARD,EVID]},related_records=[TASK])
    s['records'][NEXT]=dict(kind='research_task',path='HoTT理论充分检视.md',lifecycle_status='CURRENT',status='ready',evidence_status='NOT_EXECUTED',depends_on=[],full_sources=[SHARD,'HoTT/theory-schema/DERIVED_STRUCTURES.md'],related_records=[RID])
    s['records']['A-PREMISE-001']['source_qualification']+=' P42: A03/A11 total physical process interpretation and E02 lossless interpretation withdrawn as source attribution; E03 retains R-respect/set conditions; E04 h-level is not physical density. Original source/run bytes retained.'
    s['records']['P40-THEORY-INSPECTION-FIRST-001']['evidence_status']='FOUNDATIONS_IDENTITY_CONSTRUCTION_SOURCE_REVIEWED / OTHER_FAMILIES_OPEN'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='P42_REFLECTION_COMPLETE',depends_on=[],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']],related_records=[RID,NEXT])
    s['revision']=263;s['latest_session']=SID
    nxt='P43-LOGIC-UNIVERSES-REALS-001. Inspect exact LEM/choice/resizing/universe assumptions and Dedekind/Cauchy real construction and comparison conditions; reuse logic.tex and existing real proof scopes, do not rerun sqrt2 specification separation. Continue derived homotopy/category, metatheory/models and extensions afterwards.'
    s['execution_control'].update(status='THEORY_INSPECTION_P42_COMPLETE_P43_NEXT',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_status_observed='active')
    s['projection']['status']='THEORY_INSPECTION_IN_PROGRESS / P42_CONSTRUCTION / P43_NEXT / GOAL_ACTIVE'
    docs={p:E.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    msg='第006片检视推进到P42：基本归纳、严格正性、HIT构造资格、截断/商消去及层级源文完成；旧A03/A11/E02/E04强完成/无损/稠密归因收窄，E03补相容责任。下一P43核逻辑/宇宙/实数；其他理论领域仍开放，无新数学claim，active goal继续。入口：HoTT理论充分检视004；revision263。'
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];E.replace_in_shard(docs['MEMORY.md'],mp,old,msg)
    E.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：P42十四文件/五十九依赖锚；构造/消去源文资格收窄；P43下一；revision263。\n')
    for p,kind in [('方向追踪.md','direction'),('全景视野.md','outcome')]:
        E.replace_in_index(docs[p],'source_state_revision: 262','source_state_revision: 263');E.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-262',f'projection_generation: 20260923-{kind}-263');docs[p]['index_text']=docs[p]['index_text'].replace('THEORY_INSPECTION_P41_REVIEWED_P42_NEXT','THEORY_INSPECTION_P42_REVIEWED_P43_NEXT')
        s['records']['I-DIRECTION-PORTFOLIO-20260912' if kind=='direction' else 'I-OUTCOME-PANORAMA-20260912'].update(projection_generation=f'20260923-{kind}-263',semantic_status='THEORY_INSPECTION_P42_REVIEWED_P43_NEXT',scope='P42 construction source review complete; P43 next; whole theory review ongoing.')
    d='方向追踪/002 - 治理与用户方向.md'
    replace_row(docs['方向追踪.md'],d,'DIR-U-HOTT-FOUR-TRACK','| `DIR-U-HOTT-FOUR-TRACK` | 理论检视P42完成、P43逻辑/宇宙/实数下一 | active goal、KC2/40/47/48 | `IN_PROGRESS / P43_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P42-THEORY-CONSTRUCTION`、`OUT-P41-THEORY-IDENTITY` | 核可选假设与实数构造，继续广度 | HoTT理论充分检视；revision263 |')
    replace_row(docs['方向追踪.md'],d,'DIR-TOP-PREMISE-INVENTORY','| `DIR-TOP-PREMISE-INVENTORY` | 历史35前提的来源资格持续复审 | KC44–48与P40–P42 | `HISTORICAL_INVENTORY / SOURCE_SCOPE_CORRECTED` | `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P42-THEORY-CONSTRUCTION`、`OUT-P41-THEORY-IDENTITY` | A03/A11/E02/E04归因收窄，E03补条件；既有Id/set纠偏保留；不重跑旧GEN | PREMISE索引；HoTT理论充分检视003/004 |')
    E.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-P42-THEORY-CONSTRUCTION` | 归纳/HIT/截断构造与消去源文审查 | `DIR-U-HOTT-FOUR-TRACK`、`DIR-TOP-PREMISE-INVENTORY` | Book/三篇HIT来源/14文件及59依赖锚 | `SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH` | 正性、端点与消去责任明确；旧四项非现实归因收窄 | 不证明新HoTT悖论、全schema或物理同任务；旧核结果未重放 | {SHARD}；revision263 |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^16\. 理论充分检视继续：.*$','16. 理论充分检视继续：P40–P42源文范围完成，下一P43核逻辑/宇宙/实数；派生同伦、模型与扩展及全局排序仍开放。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for doc in docs.values():rows+=E.payload_rows(doc,ROOT)
    seen={r['path'] for r in rows}
    for p in R.MUTABLE:
        if p in seen:continue
        t=(ROOT/p).read_text()
        if p==R.STATE:t=R.dump(s).decode()
        elif p.endswith('FRONTIER.md'):t=re.sub(r'^- 第006片检视推进到P41：.*$','- '+msg,t,flags=re.M)
        elif p.endswith('RESUME.md'):t=re.sub(r'^第006片检视推进到P41：.*$',msg,t,flags=re.M)
        rows.append(dict(path=p,expected_sha256=sha(p),text=t))
    m=json.loads((ROOT/'核心认知.manifest.json').read_text());focus={2:'先核理论规则再归因',3:'消去侧条件是明确前提',5:'发现与最终归因分开',9:'形成/构造/消去/计算分层',10:'旧AI误读不当HoTT悖论',14:'持续过程不等于Nat输入',15:'保留哲学起点不自证',18:'HIT计算选择有源内动机',21:'源文和旧源码不冒充新核证明',22:'W良基与物理完成不混同',29:'统一归纳/截断体现具体设计收益',30:'经济性检视落实真实接口',31:'代理模型不等于原生截断',35:'原任务保真桥仍须给出',37:'发现预期与尚无完整见证保持张力',38:'作者明示与解释推断分开',39:'旧四项非现实理由受实质复核',40:'知识谱可被源文纠正',43:'不重跑熟悉Delay族',44:'现实对应仍可构造',45:'域边界与现实解释分开',47:'原文完整重读并核理论省略',48:'靶向规则而非仅加枚举'}
    aud=[f'# {SID} 核心认知审计','',f"- identity: {s['current_core']['generation']} / 48 KC",'- core_change: NO','- direction_change: YES; P42构造源文完成、P43下一。','- panorama_change: YES; 仅来源审计与范围纠偏。','- essay_change: NO','- update_decision: checkpoint并更新PREMISE索引，不改冻结原件。','- cross_conflicts: A03/A11强完成、E02无损、E04稠密归因无源内支持；冻结历史保留。','- unresolved: 其他理论领域和现实桥开放；writer分片事务兼容缺口不变。','','| KC | 主题 | relation | 立场与理由 | 证据 | 后继及反证条件 |','|---|---|---|---|---|---|']
    for i,u in enumerate(m['units'],1):
        rel='TENSION' if i==37 else 'ALIGNED' if i in focus else 'NOT_TOUCHED';why=focus.get(i,'本wave限定归纳/HIT/截断来源资格，未检验此主题数学命题')
        aud.append(f"| `{u['id']}` | {u['semantic_label']} | `{rel}` | {why} | {SHARD} | P43继续下一领域；若精确源文支持旧强完成归因或新保真桥出现则重评；未触及项不外推 |")
    aud+=['','## 扩展认知与全波次反思','001统一构造的收益明确；002构造与消去条件保留；003原X/ASK未替换；004Nat/W/HIT回源；005截断边界分层；006四项旧归因纠正；007不重造Delay例；008现实解释仍待桥；009目标前提选择受源文约束。',f'完整Goal-3十问/五项价值/六项航向、SOP八项与覆盖回评在{SHARD} §7。CLOSE_WITH_SCOPE后active goal继续P43。','', '## 加载与证据边界','core8与四件套按PROTOCOL v3复认revision262收据，HEAD.tracked无hash变化；本审计逐48KC登记立场，抽查KC47/48完整原文并完整重读goal-3。Book/PREMISE按EVIDENCE精确段落读取；P41 logic全文读范围继承不伪称本波重读全文。本wave没有新的proof claim或kernel run，原始数学结论不由源文审查提升。完整48KC单文件兼容审计，非嵌套分片事务。']
    ses=f'# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3 research/state\n- load_receipt: revision262收据复认及HEAD.tracked哈希一致；PLAN.json={plan["snapshot"]}；goal3与KC47/48完整重读。\n- status: P42_SOURCE_REVIEW_COMPLETE\n- authorization: 用户active goal完成006，本地研究与checkpoint；禁Sub Agent/push/tag。\n- element_usage: core/SOP=航向；Book/HIT论文=来源；PREMISE=被审对象；旧源码=控制查重；STATE=接续；无新kernel。\n- next: {NEXT}\n\nreflection=no-plan-change；完整反思与影响见{SHARD}。\n'
    bundle={'SESSION.md':ses,'RUNS.json':R.dump(dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],evidence=EVID)).decode(),'CORE_COGNITION_AUDIT.md':'\n'.join(aud)+'\n'}
    rows += [dict(path=BASE+p,expected_sha256=None,text=t) for p,t in bundle.items()]
    pay=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='governance',task_ids=[],authorization='用户active goal执行006，P42源文审查及反思完成，接P43；不push/tag。',files=rows)
    (HERE/'PAYLOAD.json').write_bytes(R.dump(pay));res=R.checkpoint(ROOT,plan['snapshot'],pay,apply=a.apply);(HERE/('APPLY.json' if a.apply else 'DRY-RUN.json')).write_bytes(R.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
