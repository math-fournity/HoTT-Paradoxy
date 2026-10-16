#!/usr/bin/env python3
"""Canonical transaction for the same-map native metric homeomorphism."""
from pathlib import Path
import argparse,importlib.util,json,re
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-CONTINUITY';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第十二轮执行报告.md'
RUN='HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-CONTINUITY-001-01'
NEXT='BP-GEO-NATIVE-INTERVAL-01：构造Real与C281同一OpenRealInterval(0,1)的实际互逆连续映射，核严格区间归属、逆向分母、两复合律和原metric连续性，再与C288同胚复合。保留原W域Lift条件，不换成闭区间或双向一致连续；无条件弱Lift、完整Lean翻译、原固定端部/来源/运动、GOLD及其它断点与四层集成仍开放。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','同一映射/原度量的连续性直接闭合既有几何义务。'),
2:('DEEPENED','pointwise模数、uniform合同、类型Path及metric数据相等严格分开。'),
5:('ALIGNED','以真实局部估计和消费者合成检查，不预认HoTT失败。'),
7:('ALIGNED','取逆证明与同胚实际过核，API拼写错误只作实现失败。'),
10:('ALIGNED','同胚不自动变成原物理运动或非现实性结论。'),
12:('DEEPENED','局部逆元大小和输入邻域的资格由r下界显式控制。'),
13:('DEEPENED','保持原函数/metric，未另造拉回度量使结果平凡通过。'),
14:('ALIGNED','每点截断模数存在不冒充全局数值选择器或物理实施能力。'),
15:('TENSION','正常构造和连续组合不是抽象必然出错的证明。'),
17:('ALIGNED','保留真实正向同胚与原弱域条件，不因目标偏好删除。'),
21:('DEEPENED','五本地模块与41外部pins、一次fresh正式核及索引关系检查。'),
22:('ALIGNED','A/B原目标继续保留，当前完成的是数学空间任务。'),
31:('DEEPENED','原生范型接受完整局部估计/度量同胚，未以名字替代实物。'),
34:('ALIGNED','强域存在性不外推弱域无条件或所有操作都可完成。'),
35:('DEEPENED','实际几何原生表达已从类型等价进入原度量下的双向连续。'),
37:('TENSION','原圆环缺陷尚未成立，固定端部和来源/过程条件继续开放。'),
38:('DEEPENED','库原点态连续定义被真实消费，未发现此链错误许诺。'),
39:('DEEPENED','从取逆的实际误差和截断消去检查基础条件。'),
41:('ALIGNED','AI构造的估计由核验证，source/run依赖均保全。'),
42:('ALIGNED','连续存在证明不被说成任意实数算法交付；作用域完整。'),
43:('DEEPENED','局部模数解决后回同一映射，再回原开区间而非重复控制。'),
44:('ALIGNED','原metric的邻域、误差和圆点用于把握理论对象。'),
45:('DEEPENED','强/弱域与原任务条件持续对齐，新增假设不隐去。'),
46:('ALIGNED','由具体取逆/映射操作触发证明，下一动作回实际(0,1)接口。')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 assert json.loads((OUT/'DELIVERY.json').read_text())['status']=='FORMAL_CHECKED_AND_RELATION_PASS_WITH_SCOPE'
 state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==185
 head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
 prior=json.loads((ROOT/'audit/astra-stereographic-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
 docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
 (OUT/'RESUME.json').write_bytes(R.dump({'policy':'Same-context same-T3 receipt reattestation under PROTOCOL v3; no fresh full emission claim','revision':185,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint185 and plan b891d2c; all32 tracked hashes match','kc_stance_revisited':'All46 individually reconsidered; original samples10/35/39/43–46 retained in current context','app_goal_status_observed':'active','objective':'完成四弹一体的redo','model_understanding':'NOT_CERTIFIED_BY_TOOL'}))
 plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert not plan['review_required'];assert not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
 old=state['latest_session'];state['revision']=186;state['latest_session']=SID
 state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C287_C288_FORMAL_CHECKED_AND_RELATION_PASS','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
 state['records']['R-ASTRA-CONTINUITY-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / SAME_METRIC_SAME_MAP_HOMEOMORPHISM','status':'strong_circle_real_homeomorphism_complete_with_scope','depends_on':[],'related_records':[SID,'R-ASTRA-STEREOGRAPHIC-20260920'],'full_sources':[REPORT,'HoTT/formal/agda-unimath/hott-z/ReciprocalContinuity.agda','HoTT/formal/agda-unimath/hott-z/StereographicContinuity.agda','audit/astra-continuity-20260920/DELIVERY.json'],'scope':'C287 actual reciprocal has local rational modulus on apart-nonzero real subspace. C288 same C285 maps and original C281 metrics form six-field pointwise homeomorphism StrongPuncture↔Real; original weak domain conditional on Lift/LEM0. No uniform-homeomorphism, global numerical modulus selection, interval bridge, physical process or complete redo.'}
 state['execution_control'].update(status='ACTIVE_GOAL_NATIVE_METRIC_HOMEOMORPHISM_CHECKED_INTERVAL_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
 session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-continuity-20260920/RESUME.json
- app_goal_status_observed: active
- objective: 完成四弹一体的redo
- previous_goal_turn: PROGRESS；C285/C286与revision185有真实证据
- status: STRONG_CIRCLE_REAL_HOMEOMORPHISM_WITH_SCOPE / PARENT_OBJECTIVE_OPEN

C287在实际非零实数子空间构造有理局部模数：中心2r≤abs(x)、附近abs(y)≥r、逆元上界及逆元距离公式给误差预算。正有理下界只消去到连续性命题，未新增/传入选择或LEM，不提取全局数值选择器。C288使用同一C285函数与C281原metric，组合加法/乘法/取负/子空间和取逆连续性，与原两复合律组成六字段PointwiseHomeomorphism。原W域继续有Lift/LEM条件版本。

一次fresh --ignore-interfaces正式运行约246秒，1076模块；相对前轮只增两个本地模块。五本地Agda文件全部pin，源码/选项/依赖/关系核验PASS，无额外kernel rerun。attempt002的NotInScope仅为API名字错误；名字和隐式参数调用修正后003通过，不作为数学拒签。继承库公设与no-erasure边界未变。

策略v1.14由b891d2c保存。下一动作：{NEXT}

按PROTOCOL§5沿用46KC legacy原子bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；用户研究报告四分片。无Sub Agent、无push/tag/发布。T01–05完整原范围不变；T06–10同metric/同映射连续合同与模数；T11–17新证明、输入和运行证据；T18–21无部署变化；T22–24结果/后继/原件保全；T25无AI系统改变；T26精确版本化。C01–C09无共享治理框架修改，C10新增项目证据。

element_usage：closure/收据复认用于恢复；研究Skill用于同任务及截断/选择边界；SOP用于方案提交；verification用于实际核与关系；canonical writer用于事务；dev-notes用于最终对话。未新建通用平台或外部AI。
'''
 audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: SAME_OPEN_INTERVAL_NEXT\n- panorama_change: ADD_C287_C288_METRIC_HOMEOMORPHISM\n- essay_change: NO\n- update_decision: 同映射连续性闭合到Real后回原(0,1)接口。\n- cross_conflicts: 模数截断存在不是全局算法；pointwise不是uniform；同胚不是metric数据/物理过程相等。\n- unresolved: 开区间、弱Lift、全翻译、原固定端部/来源/过程与四层整体。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一动作及反证条件 |\n|---|---|---|---|---|\n'
 headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
 for n,(kc,title) in enumerate(headings,1):
  rel,why=TOUCHED.get(n,('NOT_TOUCHED','本轮未推进该项具名自指、时序、全局反射或物理运动命题；局部连续性不替代。'))
  ev=('第十二轮001–004及C287/C288源码/run；若原metric/函数被换、邻域前提错误或核/hash失败则撤回；新弱Lift/过程证据进入时重评；下一步实际开区间。' if n in TOUCHED else '第十二轮003未触达范围；该具名任务或新直接证据出现时再激活。')
  audit+=f'| `{kc}` | {title} | {rel} | {why} | {ev} |\n'
 audit+='''
## 扩展认知逐片复认

001问题/简化：同一函数和原度量保持，未改题造连续。002前提/时间：未证明物理时间过程。003圆环/ASK：取逆局部前提真实控制误差，W域未替换。004HoTT/自反：度量证明在原生配置中完成，自反未触达。005表达/原文：同胚到Real不等于全部原开区间/过程，未宣布目标完成。006知识谱：使用真实连续接口并核pointwise/uniform边界。007助力/阻力：局部估计解决后回到两函数和原N接口，避免停在一般引理。008现实骨架：实际邻域与误差帮助对齐，仍保留来源/端部任务。

## 已走过的路

由具体模数和全部邻域输入推逆元误差，合法处理截断存在；组合旧函数而未换度量，六字段同胚全部有项。只把API拼写失败作为实现证据，未制造HoTT拒签叙事。

## 即将作出的选择与完备性

选择Real↔同一(0,1)开区间的实际连续互逆；不选择闭区间仿射替代、不要求更强uniform-homeo、不继续堆同形连续例子。八轴/量词/覆盖与反解释见第十二轮003。无有限枚举或全HoTT完备性声称；弱域Lift和物理任务继续开放，反例/新保任务构造出现时重评。
'''
 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[RUN],'claim_ids':['C-287','C-288'],'validation':'audit/astra-continuity-20260920/DELIVERY.json','extra_kernel_rerun':False,'parent_objective':'OPEN','app_goal_status_observed':'active'}
 for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-186'
 files=[]
 for rel in list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT)):
  raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
  if rel in (R.DIRECTION,R.PANORAMA):
   body,n=re.subn(r'(?m)^source_state_revision: 185$','source_state_revision: 186',body);assert n==1
   kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-186',body);assert n==1
  if rel=='MEMORY/001 - 当前执行队列.md':
   start=body.index('用户当前App Goal');end=body.index('\n\n',start)
   body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保留。C287证明apart非零Dedekind取逆的实际有理局部模数；C288把C285同一两映射在C281原metric下接成双向连续互逆，强域↔Real六字段同胚过核。原W域仍有Lift/LEM条件，未声称uniform-homeo、等距、全局数值模数选择或物理完成。正式run与证据关系PASS，策略v1.14由b891d2c保存。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
  if rel=='方向追踪/002 - 治理与用户方向.md':
   lines=body.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):
     lines[i]=line.replace('ACTUAL_POINTSET_EQUIVALENCE_CHECKED_CONTINUITY_OPEN','STRONG_CIRCLE_REAL_HOMEOMORPHISM_CHECKED_INTERVAL_NEXT').replace('`OUT-ASTRA-STEREOGRAPHIC-11` |','`OUT-ASTRA-STEREOGRAPHIC-11`、`OUT-ASTRA-CONTINUITY-12` |').replace('同映射连续性/同胚/区间；弱域Lift及原任务仍开放','同一(0,1)开区间；弱Lift和原操作/来源/物理任务仍开放')
   body='\n'.join(lines)+'\n'
  if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-CONTINUITY-12` | C287/C288实际局部模数与原metric双向连续同胚 | `DIR-U-ASTRA-BREAKPOINT` | 原生正式Agda及源码/选项/依赖/关系检查 | `FORMAL_CHECKED_WITH_SCOPE / SAME_METRIC_SAME_MAP_HOMEOMORPHISM` | 强域↔Real同胚；原W域Lift条件；截断模数边界明确 | 开区间、无条件弱Lift、全翻译、原物理过程及四层整体 | `'+REPORT+'`；`audit/astra-continuity-20260920/DELIVERY.json` |\n'
  files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
 for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户ACTIVE Goal及既有T3研究/状态维护授权；登记真实同映射同胚并回同一开区间，保持整个redo。','files':files}
 (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
 (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
