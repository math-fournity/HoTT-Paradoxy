#!/usr/bin/env python3
"""Canonical P41 source-qualification checkpoint, no new proof claims."""
import argparse,hashlib,importlib.util,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
SID='S-RES-20260923-ASTRA-P41-THEORY-IDENTITY';BASE=f'.codex/research/hott/sessions/{SID}/'
RID='R-P41-THEORY-IDENTITY-20260923';TASK='P41-IDENTITY-EQUIVALENCE-PREMISE-QUALIFICATION-001';NEXT='P42-INDUCTION-HIT-TRUNCATION-001'
PARENT='R-HOTT-FOUR-TRACK-PLAN-20260921';SHARD='HoTT理论充分检视/003 - P41同一性、等价与前提资格.md';EVID='audit/p41-theory-identity-20260923/EVIDENCE.json'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as E
def replace_row(doc,path,key,value):
    ls=doc['shards'][path].splitlines(keepends=True);ii=[i for i,l in enumerate(ls) if l.startswith('| `'+key+'` |')];assert len(ii)==1;ls[ii[0]]=value+'\n';doc['shards'][path]=''.join(ls)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    s=json.loads((ROOT/R.STATE).read_text());assert s['revision']==261
    h=json.loads((ROOT/R.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    plan=R.plan(ROOT,profile='governance');assert not plan['review_required'];(HERE/'PLAN.json').write_bytes(R.dump(plan))
    changed={'goal.md','feature-list.md','HoTT后续研究总体方案.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md','goal-3-工作路径树/001 - 原初目标与当前工作树.md'}
    owner=s['records'][PARENT];assert {p for p,v in owner['source_hashes'].items() if (ROOT/p).is_file() and sha(p)!=v}==changed
    for p in changed:owner['source_hashes'][p]=sha(p)
    owner['revalidation']+=' Revision262: P41 Id/equivalence source qualification and next P42; no mathematical claim upgrade.'
    owner['status']='theory_inspection_in_progress';owner['evidence_status']='P41_SOURCE_REVIEWED / P42_NEXT / GOAL_ACTIVE';owner['related_records']=list(dict.fromkeys(owner['related_records']+[RID,NEXT,SID]))
    # A rolling index is a locator, not a verification dependency of completed P40.
    prev=s['records']['R-P40-THEORY-FOUNDATIONS-20260923']
    for p in ['HoTT理论充分检视.md','HoTT理论充分检视/001 - 范围、来源与全局覆盖.md']:prev['source_hashes'].pop(p,None)
    prev['revalidation']='P40 fixed report and EVIDENCE hashes retained. Rolling index/coverage table are navigation, not evidence whose growth invalidates completed source inspection.'
    s['records'][TASK].update(lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE',resolution={'reason':'Id/set and equality-level source review completed; remaining families continue in P42.','evidence':[SHARD,EVID]})
    s['records'][RID]=dict(kind='result',path=SHARD,lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH',depends_on=[],full_sources=[SHARD,EVID],source_hashes={p:sha(p) for p in [SHARD,EVID]},related_records=[TASK])
    s['records'][NEXT]=dict(kind='research_task',path='HoTT理论充分检视.md',lifecycle_status='CURRENT',status='ready',evidence_status='NOT_EXECUTED',depends_on=[],full_sources=[SHARD,'HoTT/theory-schema/DERIVED_STRUCTURES.md'],related_records=[RID])
    s['records']['A-PREMISE-001']['source_qualification']='Historical frozen inventory; C-01 global isProp(Id) withdrawn as a source identification; G-02 needs set condition; A-04/B-03/B-04 scope correction in R-P41-THEORY-IDENTITY-20260923. Original shards and runs unchanged.'
    s['records']['P40-THEORY-INSPECTION-FIRST-001']['evidence_status']='FOUNDATIONS_AND_IDENTITY_SOURCE_REVIEWED / OTHER_FAMILIES_OPEN'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='P41_REFLECTION_COMPLETE',depends_on=[],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']],related_records=[RID,NEXT])
    s['revision']=262;s['latest_session']=SID
    nxt='P42-INDUCTION-HIT-TRUNCATION-001. Inspect base inductive formation/elimination/computation, Nat/W/strict positivity, HIT constructor/endpoint/coherence conditions and general syntax limits, truncation/quotient elimination and existence semantics. Reuse P41 full logic.tex reading and existing native controls; return to induction.tex/hits.tex/hlevels.tex decisive sections. Distinguish construction rules from physical completion. Continue other006 theory families afterwards.'
    s['execution_control'].update(status='THEORY_INSPECTION_P41_COMPLETE_P42_NEXT',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_status_observed='active')
    s['projection']['status']='THEORY_INSPECTION_IN_PROGRESS / P41_IDENTITY / P42_NEXT / GOAL_ACTIVE'
    docs={p:E.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    msg='第006片检视推进到P41：Id/set、isEquiv/ua、η/J与SIP源文资格核对完成。旧C-01全局命题性资格撤回，G-02须isSet，A-04/B-03/B-04解释分层；冻结原件不改。下一P42审归纳/HIT/截断与存在；其他理论领域仍开放，无新数学claim，active goal继续。入口：HoTT理论充分检视003；revision262。'
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];E.replace_in_shard(docs['MEMORY.md'],mp,old,msg)
    E.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：P41源文及十八依赖锚；C01/G02资格纠偏、η/J分层；P42下一；revision262。\n')
    for p,kind in [('方向追踪.md','direction'),('全景视野.md','outcome')]:
        E.replace_in_index(docs[p],'source_state_revision: 261','source_state_revision: 262');E.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-261',f'projection_generation: 20260923-{kind}-262');docs[p]['index_text']=docs[p]['index_text'].replace('THEORY_INSPECTION_P40_REVIEWED_P41_NEXT','THEORY_INSPECTION_P41_REVIEWED_P42_NEXT')
        s['records']['I-DIRECTION-PORTFOLIO-20260912' if kind=='direction' else 'I-OUTCOME-PANORAMA-20260912'].update(projection_generation=f'20260923-{kind}-262',semantic_status='THEORY_INSPECTION_P41_REVIEWED_P42_NEXT',scope='P41 identity source review complete; P42 next; whole theory review ongoing.')
    d='方向追踪/002 - 治理与用户方向.md'
    replace_row(docs['方向追踪.md'],d,'DIR-U-HOTT-FOUR-TRACK','| `DIR-U-HOTT-FOUR-TRACK` | 理论检视P41完成、P42归纳/HIT/截断下一 | active goal、KC2/40/47/48 | `IN_PROGRESS / P42_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P41-THEORY-IDENTITY`、`OUT-P40-THEORY-FOUNDATIONS` | 核形成/消去、正性、HIT一般语法与截断存在，继续广度 | HoTT理论充分检视；revision262 |')
    replace_row(docs['方向追踪.md'],d,'DIR-TOP-PREMISE-INVENTORY','| `DIR-TOP-PREMISE-INVENTORY` | 历史35前提的来源资格持续复审 | KC44–48与P40/P41 | `HISTORICAL_INVENTORY / SOURCE_SCOPE_CORRECTED` | `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P41-THEORY-IDENTITY`、`OUT-MACHINE-OVERVIEW-TARGETING-AUDIT` | C01全局资格撤回/G02限定set/A04和ηJ分层；D01及其他项目按后续原文核对；不重跑旧GEN | PREMISE索引；HoTT理论充分检视003 |')
    E.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-P41-THEORY-IDENTITY` | 同一性／等价源文审查与旧前提资格纠偏 | `DIR-U-HOTT-FOUR-TRACK`、`DIR-TOP-PREMISE-INVENTORY` | Book/官方Agda/15文件及18依赖锚 | `SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH` | C01全局读法无来源资格，G02限定set，η/J/isEquiv/ua/SIP分层 | 不证明新HoTT悖论、全部变体或物理同任务；旧核结果未重放 | {SHARD}；revision262 |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^16\. 理论充分检视继续：.*$','16. 理论充分检视继续：P40/P41源文范围完成，下一P42核归纳/HIT/截断；实数、派生同伦、模型与扩展及全局排序仍开放。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for doc in docs.values():rows+=E.payload_rows(doc,ROOT)
    seen={r['path'] for r in rows}
    for p in R.MUTABLE:
        if p in seen:continue
        t=(ROOT/p).read_text()
        if p==R.STATE:t=R.dump(s).decode()
        elif p.endswith('FRONTIER.md'):t=re.sub(r'^- 第006片active goal已开始。.*$','- '+msg,t,flags=re.M)
        elif p.endswith('RESUME.md'):t=re.sub(r'^第006片active goal已开始。.*$',msg,t,flags=re.M)
        rows.append(dict(path=p,expected_sha256=sha(p),text=t))
    m=json.loads((ROOT/'核心认知.manifest.json').read_text());focus={2:'源内Id而非错误P1作为依据',3:'条件isSet不能省去后归罪理论',5:'识别前提先于最终病因',9:'精确定位规则与相等层',10:'未把纠正AI错误当理论悖论',15:'强哲学起点保留但不自证',17:'用户视角不授权改写HoTT规则',18:'isEquiv/ua确有来源内选择',21:'来源与旧源码未冒充本轮机器证明',29:'经济收益与冗余数据的处理被定位',30:'理论经济检查具体作用于等价',31:'不以一般语义差异否定可表达性',37:'快速发现预期仍与未取得见证有张力',38:'按作者明示设计而非心理推断',39:'基础误读影响旧候选资格',40:'知识谱C01/G02被实质复审',43:'不重复SIP/Bool包装',44:'现实任务仍可提出',45:'源内条件与现实类比分开',47:'完整原文重读且保持经济性检视',48:'先有正确前提才有针对过程'}
    aud=[f'# {SID} 核心认知审计','',f"- identity: {s['current_core']['generation']} / 48 KC",'- core_change: NO','- direction_change: YES; P41源文资格完成、P42下一。','- panorama_change: YES; 仅来源审计与范围纠偏。','- essay_change: NO','- update_decision: checkpoint并更新PREMISE索引，不改冻结原件。','- cross_conflicts: C01/G02全局命题性与Book的set条件冲突已收窄；η/J呈现分开。','- unresolved: 其他理论领域和现实桥开放；writer分片事务兼容缺口不变。','','| KC | 主题 | relation | 立场与理由 | 证据 | 后继及反证条件 |','|---|---|---|---|---|---|']
    for i,u in enumerate(m['units'],1):
        rel='TENSION' if i==37 else 'ALIGNED' if i in focus else 'NOT_TOUCHED';why=focus.get(i,'本wave限定同一性/等价来源资格，未检验此主题数学命题')
        aud.append(f"| `{u['id']}` | {u['semantic_label']} | `{rel}` | {why} | {SHARD} | P42继续下一领域；若精确源文支持旧全局读法或新保真桥出现则重评；未触及项不外推 |")
    aud+=['','## 扩展认知与全波次反思','001理论收益落实isEquiv/ua；002条件不静默删除；003原X和ASK未替换；004理论真实规则回源；005表达边界分层；006知识谱纠错；007不重造Bool例；008现实解释仍待桥；009针对性需要准确前提。',f'完整Goal-3十问/五项价值/六项航向、SOP八项与覆盖回评在{SHARD} §6。CLOSE_WITH_SCOPE后active goal继续P42。','', '## 加载与证据边界','core8与四件套连续上下文及revision261收据复认；完整goal-3/KC47–48重读，截断处补读；logic.tex全文1278行分块读至EOF。显式task源文件已按范围读取并保留读范围。本wave没有新的proof claim或kernel run，原始数学结论不由源文审查提升。完整48KC单文件兼容审计，非嵌套分片事务。']
    ses=f'# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3 research/state\n- load_receipt: revision261连续上下文；PLAN.json={plan["snapshot"]}；goal3与KC47/48完整重读。\n- status: P41_SOURCE_REVIEW_COMPLETE\n- authorization: 用户active goal完成006，本地研究与checkpoint；禁Sub Agent/push/tag。\n- element_usage: core/SOP=航向；Book/Agda=来源；PREMISE=被审对象；旧源码=控制查重；STATE=接续；无新kernel。\n- next: {NEXT}\n\nreflection=no-plan-change；完整反思与影响见{SHARD}。\n'
    bundle={'SESSION.md':ses,'RUNS.json':R.dump(dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],evidence=EVID)).decode(),'CORE_COGNITION_AUDIT.md':'\n'.join(aud)+'\n'}
    rows += [dict(path=BASE+p,expected_sha256=None,text=t) for p,t in bundle.items()]
    pay=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='governance',task_ids=[],authorization='用户active goal执行006，P41源文审查及反思完成，接P42；不push/tag。',files=rows)
    (HERE/'PAYLOAD.json').write_bytes(R.dump(pay));res=R.checkpoint(ROOT,plan['snapshot'],pay,apply=a.apply);(HERE/('APPLY.json' if a.apply else 'DRY-RUN.json')).write_bytes(R.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
