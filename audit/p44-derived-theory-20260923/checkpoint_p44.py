#!/usr/bin/env python3
"""Canonical P44 source-qualification checkpoint, no new proof claims."""
import argparse,hashlib,importlib.util,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
SID='S-RES-20260923-ASTRA-P44-DERIVED';BASE=f'.codex/research/hott/sessions/{SID}/'
RID='R-P44-THEORY-DERIVED-20260923';TASK='P44-DERIVED-HOMOTOPY-CATEGORIES-SETS-001';NEXT='P45-COMPUTATION-METATHEORY-MODELS-001'
PARENT='R-HOTT-FOUR-TRACK-PLAN-20260921';SHARD='HoTT理论充分检视/006 - P44派生同伦、范畴与集合.md';EVID='audit/p44-derived-theory-20260923/EVIDENCE.json'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as E
def replace_row(doc,path,key,value):
    ls=doc['shards'][path].splitlines(keepends=True);ii=[i for i,l in enumerate(ls) if l.startswith('| `'+key+'` |')];assert len(ii)==1;ls[ii[0]]=value+'\n';doc['shards'][path]=''.join(ls)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    s=json.loads((ROOT/R.STATE).read_text());assert s['revision']==264
    h=json.loads((ROOT/R.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
    plan=R.plan(ROOT,profile='governance');assert not plan['review_required'];(HERE/'PLAN.json').write_bytes(R.dump(plan))
    changed={'goal.md','feature-list.md','HoTT后续研究总体方案.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md','goal-3-工作路径树/001 - 原初目标与当前工作树.md'}
    owner=s['records'][PARENT];assert {p for p,v in owner['source_hashes'].items() if (ROOT/p).is_file() and sha(p)!=v}==changed
    for p in changed:owner['source_hashes'][p]=sha(p)
    owner['revalidation']+=' Revision264: P44 derived homotopy/category/set source qualification and next P45; no mathematical claim upgrade.'
    owner['status']='theory_inspection_in_progress';owner['evidence_status']='P44_SOURCE_REVIEWED / P45_NEXT / GOAL_ACTIVE';owner['related_records']=list(dict.fromkeys(owner['related_records']+[RID,NEXT,SID]))
    s['records'][TASK].update(lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE',resolution={'reason':'Derived homotopy/category/set contracts reviewed; computation/metatheory/models continue in P45.','evidence':[SHARD,EVID]})
    s['records'][RID]=dict(kind='result',path=SHARD,lifecycle_status='CLOSED',status='source_review_complete',evidence_status='SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH',depends_on=[],full_sources=[SHARD,EVID],source_hashes={p:sha(p) for p in [SHARD,EVID]},related_records=[TASK])
    s['records'][NEXT]=dict(kind='research_task',path='HoTT理论充分检视.md',lifecycle_status='CURRENT',status='ready',evidence_status='NOT_EXECUTED',depends_on=[],full_sources=[SHARD,'HoTT/theory-schema/SEMANTICS_AND_COHERENCE.md','HoTT/theory-schema/EXTENSIONS_AND_METATHEORY.md'],related_records=[RID])
    s['records']['P40-THEORY-INSPECTION-FIRST-001']['evidence_status']='FOUNDATIONS_AND_DERIVED_USE_SOURCE_REVIEWED / OTHER_FAMILIES_OPEN'
    s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='P44_REFLECTION_COMPLETE',depends_on=[],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']],related_records=[RID,NEXT])
    s['revision']=265;s['latest_session']=SID
    nxt='P45-COMPUTATION-METATHEORY-MODELS-001. Inspect exact calculus assumptions for normalization, canonicity, judgmental equality/checking and proof search; inspect model/coherence/universe/univalence/HIT support in primary sources. Reuse existing R1-R4 and 2LTT evidence without new generic no-go repetitions. Then review related extensions and justified global candidate ranking; goal remains active.'
    s['execution_control'].update(status='THEORY_INSPECTION_P44_COMPLETE_P45_NEXT',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_status_observed='active')
    s['projection']['status']='THEORY_INSPECTION_IN_PROGRESS / P44_DERIVED / P45_NEXT / GOAL_ACTIVE'
    docs={p:E.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
    msg='第006片检视推进到P44：合成同伦/Whitehead/模态、category/Rezk及基数/序数/V的代表性派生合同已核，识别的观察/目标/宇宙条件明确。下一P45审计算/元理论/模型；扩展与全局排序仍开放，无新数学claim，active goal继续。入口：HoTT理论充分检视006；revision265。'
    mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];E.replace_in_shard(docs['MEMORY.md'],mp,old,msg)
    E.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：P44十一文件来源及逻辑/实数能力分析；第四弹/P17复用；P45下一；revision264。\n')
    for p,kind in [('方向追踪.md','direction'),('全景视野.md','outcome')]:
        E.replace_in_index(docs[p],'source_state_revision: 264','source_state_revision: 265');E.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-264',f'projection_generation: 20260923-{kind}-265');docs[p]['index_text']=docs[p]['index_text'].replace('THEORY_INSPECTION_P43_REVIEWED_P44_NEXT','THEORY_INSPECTION_P44_REVIEWED_P45_NEXT')
        s['records']['I-DIRECTION-PORTFOLIO-20260912' if kind=='direction' else 'I-OUTCOME-PANORAMA-20260912'].update(projection_generation=f'20260923-{kind}-265',semantic_status='THEORY_INSPECTION_P44_REVIEWED_P45_NEXT',scope='P44 derived source review complete; P45 next; whole theory review ongoing.')
    d='方向追踪/002 - 治理与用户方向.md'
    replace_row(docs['方向追踪.md'],d,'DIR-U-HOTT-FOUR-TRACK','| `DIR-U-HOTT-FOUR-TRACK` | 理论检视P44完成、P45计算/模型下一 | active goal、KC2/40/47/48 | `IN_PROGRESS / P45_NEXT` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P44-THEORY-DERIVED`、`OUT-P43-THEORY-LOGIC-REALS` | 核演算计算性质与模型假设，随后扩展和排序 | HoTT理论充分检视；revision265 |')
    E.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-P44-THEORY-DERIVED` | 派生同伦/范畴/集合的识别条件 | `DIR-U-HOTT-FOUR-TRACK` | Book/两篇论文/6文件 | `SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_MATH` | 纤维、Whitehead、modal目标、Rezk及V形成消去责任定位 | 非全定理重证、非全模型认证、无新现实桥或核结果 | {SHARD}；revision265 |\n')
    pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^16\. 理论充分检视继续：.*$','16. 理论充分检视继续：P40–P44源文范围完成，下一P45核计算/元理论/模型；扩展与全局排序仍开放。',docs['全景视野.md']['shards'][pp],flags=re.M)
    rows=[]
    for doc in docs.values():rows+=E.payload_rows(doc,ROOT)
    seen={r['path'] for r in rows}
    for p in R.MUTABLE:
        if p in seen:continue
        t=(ROOT/p).read_text()
        if p==R.STATE:t=R.dump(s).decode()
        elif p.endswith('FRONTIER.md'):t=re.sub(r'^- 第006片检视推进到P43：.*$','- '+msg,t,flags=re.M)
        elif p.endswith('RESUME.md'):t=re.sub(r'^第006片检视推进到P43：.*$',msg,t,flags=re.M)
        rows.append(dict(path=p,expected_sha256=sha(p),text=t))
    m=json.loads((ROOT/'核心认知.manifest.json').read_text());focus={2:'基础规则和派生使用都核源',3:'目标类别与层级是显式前提',5:'实际机制与最终归因分开',9:'指出群胚/态射/过程的不同层',10:'有条件识别不冒充缺陷',15:'哲学起点保持可反驳',18:'抽象呈现和减少代表选择有源内收益',21:'本波没有新kernel claim',23:'时序要求不能从路径可逆性直接推出',29:'理论经济定位到Rezk/V',30:'统一普适性按目标类解释',31:'结构可表达不等于所有观察被保留',35:'未声称原圆环被替代后命中',37:'未取得最终见证的张力保留',38:'作者明确设计动机而非猜测',39:'派生规则的实际边界成为研究对象',40:'知识谱由原文与holdout校准',43:'不沿SIP或同义例子反复深化',44:'过程观察仍有资格作为任务要求',45:'需要说明现实强观察如何进入对象',47:'经济/普适性抽象有精确作用点',48:'定位实际识别和目标条件而非无靶枚举'}
    aud=[f'# {SID} 核心认知审计','',f"- identity: {s['current_core']['generation']} / 48 KC",'- core_change: NO','- direction_change: YES; P44派生使用源文完成、P45下一。','- panorama_change: YES; 仅来源审计与范围纠偏。','- essay_change: NO','- update_decision: checkpoint及理论覆盖/树更新；不改冻结源文或旧run。','- cross_conflicts: 无新规则冲突；弱观察、目标类别、宇宙和一般等价不可混同。','- unresolved: 其他理论领域和现实桥开放；writer分片事务兼容缺口不变。','','| KC | 主题 | relation | 立场与理由 | 证据 | 后继及反证条件 |','|---|---|---|---|---|---|']
    for i,u in enumerate(m['units'],1):
        rel='TENSION' if i==37 else 'ALIGNED' if i in focus else 'NOT_TOUCHED';why=focus.get(i,'本wave限定派生同伦/范畴/集合来源资格，未检验此主题数学命题')
        aud.append(f"| `{u['id']}` | {u['semantic_label']} | `{rel}` | {why} | {SHARD} | P45继续下一领域；若精确来源提供无条件强桥或新同任务反例则重评；未触及项不外推 |")
    aud+=['','## 扩展认知与全波次反思','001普适性收益定位；002modal/category/小型条件保留；003原X未替换；004派生数学实际使用回源；005表示/模型/现实分层；006知识谱以来源校准；007不重做SIP；008现实桥仍开放；009精确识别机制服务候选发现。',f'完整Goal-3十问/五项价值/六项航向、SOP八项与覆盖回评在{SHARD} §7。CLOSE_WITH_SCOPE后active goal继续P45。','', '## 加载与证据边界','core8与四件套按PROTOCOL v3复认revision263收据，HEAD.tracked无hash变化；本审计逐48KC登记立场，抽查KC47/48完整原文并完整重读goal-3。Book/PREMISE按EVIDENCE精确段落读取；goal3/KC47–48每波重读；P41 SIP原生控制按既有范围复用。本wave没有新的proof claim或kernel run，原始数学结论不由源文审查提升。完整48KC单文件兼容审计，非嵌套分片事务。']
    ses=f'# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3 research/state\n- load_receipt: revision263收据复认及HEAD.tracked哈希一致；PLAN.json={plan["snapshot"]}；goal3与KC47/48完整重读。\n- status: P44_SOURCE_REVIEW_COMPLETE\n- authorization: 用户active goal完成006，本地研究与checkpoint；禁Sub Agent/push/tag。\n- element_usage: core/SOP=航向；Book/模态/Rezk论文=来源；PREMISE=被审对象；旧源码=控制查重；STATE=接续；无新kernel。\n- next: {NEXT}\n\nreflection=no-plan-change；完整反思与影响见{SHARD}。\n'
    bundle={'SESSION.md':ses,'RUNS.json':R.dump(dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],evidence=EVID)).decode(),'CORE_COGNITION_AUDIT.md':'\n'.join(aud)+'\n'}
    rows += [dict(path=BASE+p,expected_sha256=None,text=t) for p,t in bundle.items()]
    pay=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='governance',task_ids=[],authorization='用户active goal执行006，P44源文审查及反思完成，接P45；不push/tag。',files=rows)
    (HERE/'PAYLOAD.json').write_bytes(R.dump(pay));res=R.checkpoint(ROOT,plan['snapshot'],pay,apply=a.apply);(HERE/('APPLY.json' if a.apply else 'DRY-RUN.json')).write_bytes(R.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
