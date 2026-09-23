#!/usr/bin/env python3
"""Close the declared theory-review pass; keep broader research and proposed work distinct."""
import argparse,hashlib,importlib.util,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
SID='S-RES-20260923-ASTRA-P47-SYNTHESIS';BASE=f'.codex/research/hott/sessions/{SID}/'
RID='R-P47-THEORY-SYNTHESIS-20260923';TASK='P47-THEORY-INSPECTION-SYNTHESIS-001';PARENT='R-HOTT-FOUR-TRACK-PLAN-20260921'
SHARD='HoTT理论充分检视/009 - P47首轮范围验收与旧前提总对账.md';RANK='HoTT理论充分检视/010 - P47候选排序、下一实验与完整反思.md';EVID='audit/p47-theory-synthesis-20260923/EVIDENCE.json'
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
sys.path.insert(0,str(ROOT/'scripts/audit'));import projection_edit as E
def replace_row(doc,path,key,value):
 ls=doc['shards'][path].splitlines(keepends=True);ii=[i for i,l in enumerate(ls) if l.startswith('| `'+key+'` |')];assert len(ii)==1;ls[ii[0]]=value+'\n';doc['shards'][path]=''.join(ls)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
 s=json.loads((ROOT/R.STATE).read_text());assert s['revision']==267
 h=json.loads((ROOT/R.HEAD).read_text());assert all(sha(p)==v for p,v in h['tracked'].items())
 plan=R.plan(ROOT,profile='governance');assert not plan['review_required'];(HERE/'PLAN.json').write_bytes(R.dump(plan))
 changed={'goal.md','feature-list.md','HoTT后续研究总体方案.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md','goal-3-工作路径树/001 - 原初目标与当前工作树.md'}
 owner=s['records'][PARENT];assert {p for p,v in owner['source_hashes'].items() if (ROOT/p).is_file() and sha(p)!=v}==changed
 for p in changed:owner['source_hashes'][p]=sha(p)
 owner.update(status='theory_first_pass_complete_with_scope',evidence_status='P40_P47_DECLARED_REVIEW_COMPLETE / NO_NEW_PARADOX / NEXT_EXPERIMENT_PROPOSED')
 owner['revalidation']+=' Revision268: P47 integrated first-pass acceptance, 35 premise source qualifications, exclusions and ranking. Broader reality-relative witness remains open; no new kernel claim.'
 owner['related_records']=list(dict.fromkeys(owner['related_records']+[RID,SID]))
 for key in [TASK,'P40-THEORY-INSPECTION-FIRST-001']:
  s['records'][key].update(lifecycle_status='CLOSED',status='first_pass_complete_with_declared_scope',evidence_status='SOURCE_INSPECTED_WITH_SCOPE / SYNTHESIS_COMPLETE / NO_NEW_MATH',resolution={'reason':'Overall006 declared fields, semantic criteria, critical interactions, old qualifications, exclusions and candidate ranking completed. Not global safety or a paradox proof.','evidence':[SHARD,RANK,EVID]})
 s['records'][RID]=dict(kind='result',path=SHARD,lifecycle_status='CLOSED',status='first_pass_complete_with_declared_scope',evidence_status='SOURCE_INSPECTED_WITH_SCOPE / NO_NEW_PARADOX_WITNESS',depends_on=[],full_sources=[SHARD,RANK,EVID],source_hashes={p:sha(p) for p in [SHARD,RANK,EVID]},related_records=[TASK,'P40-THEORY-INSPECTION-FIRST-001'])
 s['records']['A-PREMISE-001']['source_qualification']+=' P47: all35 rule locations disposed in report009; A05 presentation, D05 undefined tightness, E01 recursive level and F02 cumulativity/2LTT labels qualified. All old reality judgments remain non-inherited hypotheses, not certified premises.'
 s['records'][SID]=dict(kind='session',path=BASE+'SESSION.md',lifecycle_status='HISTORICAL',status='complete_with_scope',evidence_status='P47_FULL_REFLECTION_AND_FIRST_PASS_ACCEPTANCE',depends_on=[],full_sources=[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']],related_records=[RID])
 s['revision']=268;s['latest_session']=SID
 nxt='No remaining required research in the active overall006 first-pass goal. Deliver reports009/010 and complete that bounded goal. Future recommendation, NOT_EXECUTED: qualify Book11.5 cover evidence to finite original-index delivery, preserving general versus enumerable index domains and existing constructive controls. No automatic P48, no repeated Delay/locator/SIP/Godel scan; broader reality-relative witness remains open.'
 s['execution_control'].update(status='THEORY_FIRST_PASS_COMPLETE_WITH_DECLARED_SCOPE',current_phase='PHASE_2_THEORY_FIRST_PASS_COMPLETE',second_phase_status='FIRST_PASS_COMPLETE / NEXT_TASK_PROPOSED_NOT_EXECUTED',next_minimal_verification=nxt,last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',app_goal_status_observed='active_at_checkpoint',app_goal_completion_eligible=True)
 s['projection']['status']='THEORY_FIRST_PASS_COMPLETE_WITH_SCOPE / P47_SYNTHESIS / NO_NEW_PARADOX_WITNESS'
 docs={p:E.load(ROOT,p) for p in ['MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md']}
 msg='第006片理论首轮已由P40–P47完成声明范围验收：八领域、七项语义义务、四类交互、35条旧前提资格及候选排序见HoTT理论充分检视009–010。发现真实抽象选择，尚无新合格悖论见证；无新kernel claim。下一建议是覆盖证据到有限索引交付的最小任务资格化，未执行；本active goal可完成，更大的现实相对见证目标仍开放。revision268。'
 mp='MEMORY/001 - 当前执行队列.md';old=docs['MEMORY.md']['shards'][mp].split('## 用户当前专题（2026-09-19）\n\n',1)[1].split('\n\n## 既有项目队列',1)[0];E.replace_in_shard(docs['MEMORY.md'],mp,old,msg)
 E.append_to_shard(docs['MEMORY.md'],'MEMORY/003 - 当前验证状态与顺序日志.md',f'\n{SID}：P47综合验收与排序，006首轮完成；七波来源在其提交处哈希复核无差异，35条规则资格逐项记录；后续有限交付建议未执行；revision268。\n')
 for p,kind in [('方向追踪.md','direction'),('全景视野.md','outcome')]:
  E.replace_in_index(docs[p],'source_state_revision: 267','source_state_revision: 268');E.replace_in_index(docs[p],f'projection_generation: 20260923-{kind}-267',f'projection_generation: 20260923-{kind}-268');docs[p]['index_text']=docs[p]['index_text'].replace('THEORY_INSPECTION_P46_REVIEWED_P47_NEXT','THEORY_FIRST_PASS_P47_COMPLETE_WITH_SCOPE')
  s['records']['I-DIRECTION-PORTFOLIO-20260912' if kind=='direction' else 'I-OUTCOME-PANORAMA-20260912'].update(projection_generation=f'20260923-{kind}-268',semantic_status='THEORY_FIRST_PASS_P47_COMPLETE_WITH_SCOPE',scope='Overall006 first pass complete; no new paradox witness; finite-delivery qualification is proposed, not executed.')
 d='方向追踪/002 - 治理与用户方向.md'
 replace_row(docs['方向追踪.md'],d,'DIR-U-HOTT-FOUR-TRACK','| `DIR-U-HOTT-FOUR-TRACK` | 理论首轮范围完成，后继有限交付资格化仅建议 | 用户006目标、KC2/40/47/48 | `FIRST_PASS_COMPLETE / NEXT_EXPERIMENT_PROPOSED` | `THEORY_SCHEMA`, `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P47-THEORY-SYNTHESIS` | 按010最小卡查重与固定输入输出；非自动新队列 | HoTT理论充分检视009–010；revision268 |')
 replace_row(docs['方向追踪.md'],d,'DIR-TOP-PREMISE-INVENTORY','| `DIR-TOP-PREMISE-INVENTORY` | 35条旧前提的来源资格逐项处置 | KC44–48与P40–P47 | `HISTORICAL_INVENTORY / REALITY_JUDGMENTS_NOT_INHERITED` | `THEORY_ECONOMY`, `PARADOX_DISCOVERY` | `OUT-P47-THEORY-SYNTHESIS` | 规则按限定复用，旧9条非现实判定不作事实；冻结原件不改 | PREMISE索引；HoTT理论充分检视009 §4 |')
 E.append_to_shard(docs['全景视野.md'],'全景视野/002 - 治理、门禁与骨架结果.md',f'\n| `OUT-P47-THEORY-SYNTHESIS` | HoTT理论首轮综合验收与排序 | `DIR-U-HOTT-FOUR-TRACK`、`DIR-TOP-PREMISE-INVENTORY` | 八领域七义务/四类交互/旧35条/TC遗漏 | `FIRST_PASS_COMPLETE_WITH_SCOPE / NO_NEW_MATH` | 真实抽象选择与规则条件分层，有限交付为下一资格化建议 | 非全理论安全或新悖论证明；未执行后继 | {SHARD}；{RANK}；revision268 |\n')
 pp='全景视野/008 - 当前未完成.md';docs['全景视野.md']['shards'][pp]=re.sub(r'^16\. 理论充分检视继续：.*$','16. 006理论首轮已完成（P40–P47，报告009–010）；更大现实相对见证仍开放。覆盖证明→有限交付为未执行建议；全部模型/实现/未来变体不在本次结案范围。',docs['全景视野.md']['shards'][pp],flags=re.M)
 rows=[]
 for doc in docs.values():rows+=E.payload_rows(doc,ROOT)
 seen={r['path'] for r in rows}
 for p in R.MUTABLE:
  if p in seen:continue
  t=(ROOT/p).read_text()
  if p==R.STATE:t=R.dump(s).decode()
  elif p.endswith('FRONTIER.md'):t=re.sub(r'^- 第006片检视推进到P46：.*$','- '+msg,t,flags=re.M)
  elif p.endswith('RESUME.md'):t=re.sub(r'^第006片检视推进到P46：.*$',msg,t,flags=re.M)
  rows.append(dict(path=p,expected_sha256=sha(p),text=t))
 focus={1:'找什么/怎么找/凭什么分开；首轮非最终见证',2:'理论地图经八领域源文校准',3:'合取前提固定实际规则及侧条件',4:'未证明任何物理运动前提',5:'先找可检验反差，未预定归因',6:'时间不收窄为tick或密度',7:'以原文修正AI知识谱',8:'芝诺/Russell启发未冒充已证历史解释',9:'时间/可用性精确规则分别定位',10:'现实相对挑战未被内部一致性替代',11:'逻辑依赖与物理时长分开',12:'检查/搜索/程序执行各自限定',13:'工具性通过实际交付接口继续检验',14:'未把理论对象存在当现实能力',15:'必然失配仍是可反驳研究起点',16:'实际V/正性限制已核，未将Russell叙事作定理',17:'避免训练先验替代直接证据',18:'经济收益承认但不预定缺陷',19:'稠密性与过程完成桥尚未建立',20:'物理量子化未在本项目被证明',21:'本阶段未新增机器定理，旧证据只按范围复用',22:'A/B方向均须同任务承诺',23:'P46精确定位clock/crisp/phase限制',24:'时序表示与不可完成判词分开',25:'无新一般自指证明',26:'全域自验证未由内部语法得到',27:'一般计算界限不冒充HoTT独有',28:'不将有限超时当不可停机',29:'经济选择须对任务起实际作用',30:'理论经济与作者明确动机分开记录',31:'单个受限接口不推出全系统不可表达',32:'稠密/离散前提不预定真值',33:'构造过程问题须对准实际形成规则',34:'正负存在均要限定量词与任务',35:'没有新的全理论可表达/不可表达结论',36:'旧R3/2LTT已覆盖，拒绝重复长支',37:'此轮无悖论见证，与用户期待的张力明确保留',38:'作者设计取舍不等承认缺陷',39:'基础清单误读和代理连接是已定位原因，非所有历史失败归因',40:'完整知识谱经源文、交互和holdout校准',43:'否决熟悉Ω/Delay/SIP的路径依赖',44:'现实解释合法而未闭合',45:'有限交付卡保持数学与现实桥不同',46:'选实际过程接口而非纯术语分类',47:'真抽象已定位，非现实性结果未得',48:'下一卡要求前提敏感性和正控制，拒绝蛮举'}
 m=json.loads((ROOT/'核心认知.manifest.json').read_text());aud=[f'# {SID} 核心认知审计','',f"- identity: {s['current_core']['generation']} / 48 KC",'- core_change: NO','- direction_change: YES; 首轮完成、后继仅建议。','- panorama_change: YES; 范围验收而非新数学。','- essay_change: NO','- update_decision: 当前owner及checkpoint；原文/旧run不改。','- cross_conflicts: 旧35条资格见009；物理与形式完成不混同。','- unresolved: 更大现实见证、全模型/实现范围、后继卡资格；均不伪装已完成。','','| KC | 主题 | relation | 立场与理由 | 证据 | 后继及反证条件 |','|---|---|---|---|---|---|']
 for i,u in enumerate(m['units'],1):
  rel='TENSION' if i==37 else 'DEEPENED' if i in [2,30,39,40,47,48] else 'ALIGNED' if i in focus else 'NOT_TOUCHED';why=focus.get(i,'本波未评价AI发展或阻力的一般论断；未来独立AI机制任务才重开')
  aud.append(f"| `{u['id']}` | {u['semantic_label']} | `{rel}` | {why} | {SHARD}；{RANK} | 新侧条件反例、实际强承诺或独立任务推翻对应资格时重评；否则不重复本分母 |")
 aud+=['','## 扩展认知逐片与航向','001：经济收益与源内条件同时保留，若新实例显示条件被删除则重评。','002：按实际形成/消去判据，不以代理名替原生；真实翻译可改变资格。','003：原X保持校准，有限交付尚无回接；取得保任务桥才升级。','004：从语法/派生/模型/扩展建立全景，不宣称全理论穷尽。','005：时间、时序、判断和现实交付分层；新物理模型另审。','006：旧推断越级逐项纠正；旧真实运行未抹除。','007：P1/反射/2LTT/GEN控制复用；新分母才重开。','008：骨架解释作为严肃入口，模型存在不保证现实；反例可改变判断。','009：KC47/48重读，选择T和X_T而非熟悉后端；后继前提不敏感则否决。',f'完整十问、五价值、六航向、SOP八项和八轴见{RANK} §4；已走路径与将作选择明确分开。','', '## 加载与兼容边界','revision267收据复认，HEAD.tracked全部匹配；48KC逐项立场，goal3/KC47–48全读，报告001–010全读，决定性新源文范围见EVIDENCE。无新claim/kernel。G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001仍存在；PROTOCOL单文件完整48KC兼容，不宣称嵌套分片事务修复。']
 ses=f'# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3 research/state\n- load_receipt: revision267复认与HEAD.tracked全匹配；PLAN={plan["snapshot"]}；goal3/KC47–48及报告全文重读。\n- authorization: 用户active goal完成006；本地研究、checkpoint、精确提交；无Sub Agent/push/tag。\n- status: FIRST_PASS_COMPLETE_WITH_DECLARED_SCOPE\n- element_usage: core/SOP=航向与完成条件；源文/旧报告=语义与查重；TC/有限性holdout=遗漏；STATE=完成与建议分开；kernel未用因无新数学claim。\n- next: {nxt}\n- known_gap: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；48KC单文件兼容。\n\nreflection=no-plan-change；006原定最终综合验收已完成。T02/T04/T22/T24/T26更新需求状态/研究报告/索引/记忆/版本；代码测试/配置/数据schema/部署/安全/共享治理框架无变化。数学证明门禁未被来源审查替代。\n'
 bundle={'SESSION.md':ses,'RUNS.json':R.dump(dict(schema_version='hott-session-runs/v1',session_id=SID,new_math_claims=[],new_kernel_runs=[],evidence=EVID,stage_completion='SOURCE_REVIEW_NOT_MATHEMATICAL_WITNESS')).decode(),'CORE_COGNITION_AUDIT.md':'\n'.join(aud)+'\n'}
 rows += [dict(path=BASE+p,expected_sha256=None,text=t) for p,t in bundle.items()]
 pay=dict(schema_version='cognition-checkpoint/v1',session_id=SID,load_profile='governance',task_ids=[],authorization='用户active goal完成006；P47综合验收与完整反思；后继仅建议，不push/tag。',files=rows)
 (HERE/'PAYLOAD.json').write_bytes(R.dump(pay));res=R.checkpoint(ROOT,plan['snapshot'],pay,apply=a.apply);(HERE/('APPLY.json' if a.apply else 'DRY-RUN.json')).write_bytes(R.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
