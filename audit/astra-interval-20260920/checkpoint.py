#!/usr/bin/env python3
"""Canonical state transaction for the original interval bridge and task return."""
from pathlib import Path
import argparse,importlib.util,json,re
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-INTERVAL';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第十三轮执行报告.md'
RUN='HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-INTERVAL-001-01'
NEXT='BP-GEO-NATIVE-COMPLETION-01：针对C290同一开区间到圆的实际逆映射构造闭参数completion，核内点一致、原metric连续及0/1端部像，同时固定N直线completion；端部值须由真实函数导出。随后回AST-U01/U04的Task/Trace/Done、Rich/Bare/Forget和原操作合同，不无限扩充实分析。内在几何已直接原生证明，无需全Lean解释器；具体Lean F/环境/过程若转为HoTT结论仍需native或相称翻译。弱Lift、其它机制、GOLD及四层整体保持OPEN。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','接回原N=(0,1)，并从内在几何返回同任务合同。'),
2:('DEEPENED','原生直接证明与全语言翻译分开；具体过程的保真责任未删。'),
5:('ALIGNED','真实正同胚保留，端部/来源及过程判词继续按证据审查。'),
7:('ALIGNED','层级注解失败保留，实际核通过不靠模式相似性。'),
10:('ALIGNED','标准内在同胚不升级为现实还原完成或HoTT矛盾。'),
12:('DEEPENED','严格区间条件提供逆向正分母；不偷偷包含端点。'),
13:('DEEPENED','两个复合方向恢复原子类型元素，弱域Lift跨复合保持。'),
14:('ALIGNED','连续互逆和Path存在不冒充数值算法或Done-EXACT。'),
15:('TENSION','内在数学正恢复成立，不能继续把这一关系的失败当已证前提。'),
17:('ALIGNED','旧022/023的强判词作为被审来源，不能凭source=user标签认证数学。'),
21:('DEEPENED','七本地模块/41外部pins、一次fresh核及证据关系检查通过。'),
22:('ALIGNED','A/B原目标保留，下一补端部与实际操作合同。'),
31:('DEEPENED','原生范型真实表达并检查原开区间及复合，而非类型参数。'),
34:('ALIGNED','强域成功不外推无条件弱域/任意过程，也不声称后者不可能。'),
35:('DEEPENED','内在圆/原N的原生表达已闭合到精确范围，完整来源过程仍开放。'),
37:('TENSION','未形成原圆环的HoTT缺陷见证；不以同胚成功改名击落。'),
38:('DEEPENED','实际UA作用与真实复合同胚一致，未发现本链错误识别。'),
39:('DEEPENED','从内在等价回到基础的端部观察，继续核真实字段。'),
41:('ALIGNED','实际内核支撑结果，局部资格与整体Goal分开。'),
42:('ALIGNED','未让全Lean解释器成为额外无限前置，也未移走具体保真义务。'),
43:('CORRECTED','纠正002/008旧当前态，停止继续补一般实数基础，回用户结构问题。'),
44:('ALIGNED','实际Circle/Interval对象可把握，仍处理原来源与完成条件。'),
45:('DEEPENED','真实内在链完成后定位尚未对齐的端部/来源/操作字段。'),
46:('ALIGNED','下一动作是同一逆映射的真实completion，端部不填答案标签。')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 assert json.loads((OUT/'DELIVERY.json').read_text())['status']=='FORMAL_CHECKED_AND_RELATION_PASS_WITH_SCOPE'
 state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==186
 head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
 prior=json.loads((ROOT/'audit/astra-continuity-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
 docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
 (OUT/'RESUME.json').write_bytes(R.dump({'policy':'Same-context same-T3 receipt reattestation under PROTOCOL v3; no fresh full emission claim','revision':186,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint186 and plan4d44b0e; all32 tracked hashes match','kc_stance_revisited':'All46 individually reconsidered; original samples10/35/39/43–46 retained in current context','app_goal_status_observed':'active','objective':'完成四弹一体的redo','model_understanding':'NOT_CERTIFIED_BY_TOOL'}))
 plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert not plan['review_required'];assert not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
 old=state['latest_session'];state['revision']=187;state['latest_session']=SID
 state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C289_C290_FORMAL_CHECKED_AND_RELATION_PASS','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
 state['records']['R-ASTRA-INTERVAL-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / ORIGINAL_OPEN_INTERVAL_HOMEOMORPHISM','status':'native_intrinsic_circle_interval_complete_with_scope','depends_on':[],'related_records':[SID,'R-ASTRA-CONTINUITY-20260920'],'full_sources':[REPORT,'HoTT/formal/agda-unimath/hott-z/SignedIntervalHomeomorphism.agda','HoTT/formal/agda-unimath/hott-z/NativeOpenInterval.agda','audit/astra-interval-20260920/DELIVERY.json'],'scope':'C289 Real↔abs-bounded signed interval↔original C281 (0,1), strict membership/both continuous inverses. C290 strong circle composite and original W conditional on Lift/LEM0, native type path action. Direct native intrinsic proof, not full Lean interpretation or original physical/source/endpoint task.'}
 state['execution_control'].update(status='ACTIVE_GOAL_NATIVE_INTRINSIC_INTERVAL_CHECKED_COMPLETION_TASK_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
 session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-interval-20260920/RESUME.json
- app_goal_status_observed: active
- objective: 完成四弹一体的redo
- previous_goal_turn: PROGRESS；C287/C288与revision186有真实证据
- status: NATIVE_INTRINSIC_CIRCLE_INTERVAL_COMPLETE_WITH_SCOPE / PARENT_OBJECTIVE_OPEN

C289用实际t/(1+abs(t))与z/(1-abs(z))、仿射½(1+z)与2u-1，接回C281原OpenRealInterval(0,1)。正分母、严格范围、两方向与原metric连续性均有项。C290与圆同胚实际复合，强域/原W条件分别保留；UA Path作用等于真实复合函数。无条件弱Lift、实际completion与原操作合同未证明。

一次fresh --ignore-interfaces正式运行约243秒，1078模块，较前轮只增两个本地模块；七本地源码及外部pins完整，formal/关系检查PASS，无额外kernel rerun。attempt001未解meta来自signedSubtype缺显式层级/域注解，补subtype lzero Real后002通过，原开区间003通过；未当作数学拒签。

本轮重新读策略002/008及被审历史022/023，修正旧当前态；内在子命题直接native已经满足F011的native-or-faithful-translation选择，不新增全语言解释器前置。具体Lean F/环境/完成若当HoTT结论仍需原生或相称翻译。策略v1.15由4d44b0e保存。下一动作：{NEXT}

PROTOCOL§5沿用46KC legacy原子bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；用户报告四分片。无Sub Agent、无push/tag/发布。T01–05完整原范围保持；T06–10原区间及内在/完整任务边界；T11–17新原生源码/输入/运行证据；T18–21无部署变化；T22–24当前状态纠正/后继/原件保全；T25无AI合同变化；T26精确版本化。C01–C09不修改共享治理方法，C10项目证据更新。

element_usage：closure/收据复认恢复；研究Skill要求同任务与正控制；SOP驱动回父范围；verification固定实际核/依赖/关系；canonical writer写事务；dev-notes归档。无新通用平台或外部AI。
'''
 audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: SAME_MAP_COMPLETION_AND_TASK_RETURN\n- panorama_change: ADD_C289_C290_ORIGINAL_INTERVAL\n- essay_change: NO\n- update_decision: 内在几何已原生核验，回同一映射端部/来源和任务合同。\n- cross_conflicts: 内在同胚不自动保持completion/允许过程；原W Lift不省略；历史强判词不作已证前提。\n- unresolved: 同一原生completion、Task/Trace/Done、弱Lift、其它机制/GOLD/四层整体。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一动作及反证条件 |\n|---|---|---|---|---|\n'
 headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
 for n,(kc,title) in enumerate(headings,1):
  rel,why=TOUCHED.get(n,('NOT_TOUCHED','本轮未推进该项具名时序、自指、全局反射或物理运动结论；内在同胚不替代。'))
  ev=('第十三轮001–004、C289/C290源码/run、原022/023与策略002/008回查；若原N/metric被换或核/hash失败则撤回；下一步同一completion与合同，新保任务证据可重评。' if n in TOUCHED else '第十三轮003未触达范围；该具名任务或新直接证据出现时重新激活。')
  audit+=f'| `{kc}` | {title} | {rel} | {why} | {ev} |\n'
 audit+='''
## 扩展认知逐片复认

001问题/简化：原N同名同字节导入，未换闭区间。002前提/时间：没有把形式同胚说成物理完成。003圆环/ASK：回真实completion及端部，原Step/Done仍需实现。004HoTT/自反：原生Path作用对齐真实函数，自反未触达。005表达/原文：内在模型不再空缺，用户全部原过程仍不自证。006知识谱：旧022/023被审而非直接升级当前真值。007助力/阻力：纠正旧owner并停止继续扩一般实数，回结构与任务；全翻译器不作额外门槛。008现实骨架：实际对象/映射已具备，继续以端部和允许操作对齐。

## 已走过的路

严格界和正分母接原(0,1)，两边返回与连续性原生检查，强域和原W条件完整。审查父表与原来源后，原位纠正过期当前态，未宣称整个策略完成或HoTT矛盾。

## 即将作出的选择与完备性

选择同一逆映射的原生闭参数completion、内点一致、连续与端部值；达到后回Task/Trace/Done/Rich消费者。未选无限一般实数、完整Lean解释器或仅复制旧端点标签。具体Lean过程的原生/翻译责任及原弱域仍开放。八轴和反解释见第十三轮003；全称由源码承担，无有限枚举/全HoTT完备性声称。新真实过程或相容completion证据到来时重评。
'''
 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[RUN],'claim_ids':['C-289','C-290'],'validation':'audit/astra-interval-20260920/DELIVERY.json','extra_kernel_rerun':False,'parent_objective':'OPEN','app_goal_status_observed':'active'}
 for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-187'
 files=[]
 for rel in list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT)):
  raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
  if rel in (R.DIRECTION,R.PANORAMA):
   body,n=re.subn(r'(?m)^source_state_revision: 186$','source_state_revision: 187',body);assert n==1
   kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-187',body);assert n==1
  if rel=='MEMORY/001 - 当前执行队列.md':
   start=body.index('用户当前App Goal');end=body.index('\n\n',start)
   body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C289/C290接通原生实际圆与C281原(0,1)：正分母/严格范围、两向连续互逆、强域及原W条件版本、真实Path作用均过核；不再处于“没有实际原生几何”阶段。正式run和关系PASS，策略v1.15由4d44b0e保存；原操作/来源/Done尚未闭合。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
  if rel=='方向追踪/002 - 治理与用户方向.md':
   lines=body.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):
     lines[i]=line.replace('STRONG_CIRCLE_REAL_HOMEOMORPHISM_CHECKED_INTERVAL_NEXT','NATIVE_INTRINSIC_INTERVAL_CHECKED_COMPLETION_TASK_OPEN').replace('`OUT-ASTRA-CONTINUITY-12` |','`OUT-ASTRA-CONTINUITY-12`、`OUT-ASTRA-INTERVAL-13` |').replace('同一(0,1)开区间；弱Lift和原操作/来源/物理任务仍开放','同一逆映射completion与端部，然后Task/Trace/Done；弱Lift和原过程仍开放')
   body='\n'.join(lines)+'\n'
  if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-INTERVAL-13` | C289/C290原(0,1)实际同胚、圆复合与Path作用 | `DIR-U-ASTRA-BREAKPOINT` | 原生Agda及源码/选项/依赖/关系核验 | `FORMAL_CHECKED_WITH_SCOPE / ORIGINAL_INTERVAL_INTRINSIC_BRIDGE` | 真实原N严格范围/两向连续互逆；强域与原W条件分别保留 | 同一completion、Task/Trace/Done、无条件弱Lift、其它机制/GOLD/四层整体 | `'+REPORT+'`；`audit/astra-interval-20260920/DELIVERY.json` |\n'
  files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
 for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户ACTIVE Goal及既有T3研究/状态维护授权；登记原N内在桥并回端部/任务，不删父范围。','files':files}
 (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
 (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
