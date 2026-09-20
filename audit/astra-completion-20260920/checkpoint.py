#!/usr/bin/env python3
"""Canonical transaction for the native same-map closed extension."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-COMPLETION';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第十四轮执行报告.md'
RUN='HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-COMPLETION-001-01'
NEXT='BP-GEO-NATIVE-RICH-TASK-01：用C290实际内在载体及C291/C292同一映射的闭参数延拓建立Rich/Bare/Forget与端部观察；Bare必须是StrongPuncture或原(0,1)，不能退回共同环境Plane。核实际丰富结构能否被该内在等价识别，同时保留全字段运输正控制。按原来源固定Task/Trace/Done和允许操作，区分表示转换、保端部/环境操作及物理过程；不得先定义Allowed排除目标再自证失败。完成最小真实实例后回其它断点、GOLD及四层集成。原W无条件Lift、实际过程和整体目标保持OPEN。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','同一原圆/区间/逆函数的闭参数延拓，直接服务原问题。'),
2:('DEEPENED','实际原生证明延续，内在与丰富结构的语义分层明确。'),
5:('ALIGNED','保留正延拓，不为预期否定而改公式或目标。'),
7:('ALIGNED','草稿及完整依赖实跑，未以LLM判断替代内核。'),
10:('ALIGNED','连续延拓不等于现实复原过程，不据此宣布现实困难或消失。'),
12:('DEEPENED','K正性先提供取逆资格，所有定义域及端点合法性显式。'),
13:('DEEPENED','闭参数项与原开区间函数有全称一致项，未靠同名替换。'),
14:('ALIGNED','有限定义/证明项是形式交付，不自动完成所描述的物理过程。'),
15:('TENSION','内在互逆与闭延拓均有正实例，不能先验把它们称作矛盾。'),
17:('ALIGNED','保留用户问题，旧强解释作为被审对象而非证明前提。'),
19:('ALIGNED','原度量连续性与形式端部值检查不替代实际时间的完成论证。'),
20:('ALIGNED','没有假定现实量子化/最小跳跃或据连续性认证物理。'),
21:('DEEPENED','九本地Agda输入及固定外部依赖，完整核收据/关系/版本核查。'),
22:('ALIGNED','两类现实相对目标仍保留，Task/Trace/Done作为下一连接。'),
31:('DEEPENED','严格范型同时接受内点正控制与闭域非单射的负命题。'),
34:('ALIGNED','本具体闭域非单射不外推任意复原不可能。'),
35:('DEEPENED','真实闭参数与端部字段已表达，完整原过程仍未全部表达。'),
37:('TENSION','有精确端部区别，尚无原圆环HoTT缺陷见证。'),
38:('ALIGNED','是否错误识别要检查实际丰富结构运输，不能从裸同胚直接断言。'),
39:('DEEPENED','回到端部这一基础观察，其值由公式得出而非手填标签。'),
41:('ALIGNED','草稿/正式run/索引分层，父Goal未因局部通过而结束。'),
42:('ALIGNED','既不增全语言翻译前置，也不删掉原操作保真责任。'),
43:('CORRECTED','几何延拓达到当前需要即停止扩充，返回Rich与实际任务。'),
44:('ALIGNED','实际圆和线段的闭参数呈现支持现实解释，但不自证物理事实。'),
45:('DEEPENED','把需要保留的端部差异接到真实对象，下一核遗忘和运输。'),
46:('DEEPENED','从真实公式导出同/异端像，下一回到允许动作和完成标准。')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_CHECKED_AND_RELATION_PASS_WITH_SCOPE'
 state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==187
 head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
 plan_commit=(OUT/'PLAN-COMMIT.txt').read_text().strip()
 prior=json.loads((ROOT/'audit/astra-interval-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
 docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
 (OUT/'RESUME.json').write_bytes(R.dump({'policy':'PROTOCOL v3 same-T3 receipt reattestation; not a fresh full-emission claim','revision':187,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint187 and current strategy revision; all32 tracked hashes match','kc_stance_revisited':'All46 individually reconsidered; source samples10/35/39/43–46 reread','model_understanding':'NOT_CERTIFIED_BY_TOOL','app_goal_status_observed':'active','objective':'完成四弹一体的redo'}))
 plan=R.plan(ROOT,profile='research',task_ids=['R-ASTRA-INTERVAL-20260920']);assert not plan['review_required'];assert not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
 old=state['latest_session'];state['revision']=188;state['latest_session']=SID
 state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C291_C292_FORMAL_CHECKED_AND_RELATION_PASS','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
 state['records']['R-ASTRA-COMPLETION-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / SAME_MAP_CLOSED_EXTENSION','status':'same_map_completion_boundary_checked_with_scope','depends_on':[],'related_records':[SID,'R-ASTRA-INTERVAL-20260920'],'full_sources':[REPORT,'HoTT/formal/agda-unimath/hott-z/HomogeneousCircle.agda','HoTT/formal/agda-unimath/hott-z/NativeCompletion.agda','audit/astra-completion-20260920/DELIVERY.json'],'scope':'C291 positive homogeneous denominator, original-metric continuous closed extension and equality with C290 inverse on every interior point; straight N extension. C292 derived equal M endpoint images, distinct N images, interior injectivity/avoidance and closed noninjectivity. Not physical completion or a universal compactification theorem.'}
 state['execution_control'].update(status='ACTIVE_GOAL_NATIVE_COMPLETION_CHECKED_RICH_TASK_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
 session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-completion-20260920/RESUME.json
- app_goal_status_observed: active
- objective: 完成四弹一体的redo
- status: SAME_MAP_CLOSED_EXTENSION_CHECKED_WITH_SCOPE / PARENT_OBJECTIVE_OPEN

C291固定v=2u−1、d=1−abs(v)、K=v²+d²，证明K>0及齐次圆方程；在原metric下连续。mInterior对全部原(0,1)输入证明等于C290同一逆映射；N直线completion单列。C292两端同像east、N端像不同、内点避开east且单射、闭参数延拓非单射。端部不是假定标签，闭参数延拓也不是物理Trace完成或Cauchy完备化泛性质。

两个草稿检查成功；一次fresh --ignore-interfaces正式run成功，{delivery['import_modules']}模块；九本地Agda及固定外部pins，formal/关系检查PASS，无额外kernel rerun。继承no-erasure库公设，不认证全库一致性；无条件原弱域Lift未证明。

策略v1.16由{plan_commit}保存。下一动作：{NEXT}

PROTOCOL§5沿用全46KC legacy原子bundle，登记G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；用户报告四分片。无Sub Agent、无push/tag/发布。T01–05原完整目标及来源不变；T06–10同映射闭延拓、端部结构及下一任务；T11–17原生源码/核/证据；T18–21无部署/外部操作；T22–24状态/后继/历史保全；T25无AI合同改变；T26精确版本化。C01–C09共享治理方法NO_CHANGE，C10项目证据更新。

element_usage：closure和收据复认恢复任务；研究Skill核同任务/正控制；SOP推动回父范围；verification固定源核依赖；canonical writer保原子事务；dev-notes保存公开问答。无新通用设施。
'''
 audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: RETURN_TO_NATIVE_RICH_AND_TASK\n- panorama_change: ADD_C291_C292_CLOSED_EXTENSION\n- essay_change: NO\n- update_decision: 同一映射延拓完成，返回端部结构和允许操作合同。\n- cross_conflicts: 内点单射与闭域非单射的定义域不同；延拓项不等于物理复原；原弱域Lift保留。\n- unresolved: 原生丰富结构与实际Task/Trace/Done、无条件弱Lift、其它机制/GOLD/四层整体。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一动作及反证条件 |\n|---|---|---|---|---|\n'
 headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
 for n,(kc,title) in enumerate(headings,1):
  rel,why=TOUCHED.get(n,('NOT_TOUCHED','本单元未推进该项具名自指、全局反射或其它时间机制；闭参数数学项不替代它。'))
  ev=('第十四轮001–004、C291/C292源码与run；下一BP-GEO-NATIVE-RICH-TASK-01；若内点非同一函数、端部被手填、metric更换或核/hash失败则撤回；保任务真实反例触发重评。' if n in TOUCHED else '第十四轮003未触达范围；该具名机制/任务或新一手证据进入当前队列时重开。')
  audit+=f'| `{kc}` | {title} | {rel} | {why} | {ev} |\n'
 audit+='''
## 扩展认知逐片复认

001问题/简化：新域明确叫闭参数，未替换原开区间。002前提/时间：延拓连续性与时序或过程完成分开。003圆环/ASK：K正性给取逆资格，端部从真实函数导出。004HoTT/自反：下一比较实际丰富数据，未触达自身反射。005表达/原文：具体对象已表达，完整哲学论证不自证。006知识谱：原022/023仍是被审来源，无新全库/论文覆盖声明。007助力/阻力：当前几何够用就回Rich/Task，不继续堆实分析。008现实骨架：精确M/N端部差别可以成为任务观察；其是否必须保持须回原操作合同，不能由结果倒选规则。

## 已走过的路

九本地模块组成真实原生链；当前两新源码使原逆映射在全部内点与闭延拓一致，端部导出同像，普通N导出异像。未构造“两个不同点零距离”的假设；没有以手填布尔值区分M/N。全局K正性只支持定义资格，不凭有限采样。完整正式核与元数据/关系检查分层。

## 即将作出的选择与完备性

返回AST-U01/U04：以实际内在载体为Bare，带当前真实completion和表示图为Rich，核端部观察及全字段运输正控制，再固定原操作的Task/Trace/Done。没有选无限实分析、全Lean解释器、仅整数端点或先将Allowed定义成不可能到达目标的循环规格。具体物理/来源义务、原W Lift、其它机制与GOLD仍开放。

八轴与八项SOP反思见第十四轮003；本单元为固定公式的全称证明，非候选枚举或开放世界完备性。独立对照为原N直线completion及C290两边逆律，未重跑旧Lean F。out-of-envelope为原来源/操作对哪些结构有保持要求；若用户原输入已有数据或保任务恢复可构造，须保留该正结果。
'''
 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[RUN],'claim_ids':['C-291','C-292'],'validation':'audit/astra-completion-20260920/DELIVERY.json','extra_kernel_rerun':False,'parent_objective':'OPEN','app_goal_status_observed':'active'}
 for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-188'
 targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT))
 baseline=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(baseline.stdout)
 files=[]
 for rel in targets:
  raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
  if rel in (R.DIRECTION,R.PANORAMA):
   body,n=re.subn(r'(?m)^source_state_revision: 187$','source_state_revision: 188',body);assert n==1
   kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-188',body);assert n==1
  if rel=='MEMORY/001 - 当前执行队列.md':
   start=body.index('用户当前App Goal');end=body.index('\n\n',start)
   body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C291/C292已构造并核验C290同一逆映射的闭参数连续延拓：K正性、内点一致、两端同像、N直线端像不同、内点单射/闭域非单射都有实际原生项。正式核/关系PASS；此completion不等于物理过程或Cauchy泛性质。策略v1.16由'+plan_commit+'保存。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
  if rel=='方向追踪/002 - 治理与用户方向.md':
   lines=body.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):
     lines[i]=line.replace('NATIVE_INTRINSIC_INTERVAL_CHECKED_COMPLETION_TASK_OPEN','NATIVE_SAME_MAP_COMPLETION_CHECKED_RICH_TASK_OPEN').replace('`OUT-ASTRA-INTERVAL-13` |','`OUT-ASTRA-INTERVAL-13`、`OUT-ASTRA-COMPLETION-14` |').replace('同一逆映射completion与端部，然后Task/Trace/Done；弱Lift和原过程仍开放','同一内在载体的Rich/Bare/Forget与Task/Trace/Done；弱Lift和原过程仍开放')
   body='\n'.join(lines)+'\n'
  if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-COMPLETION-14` | C291/C292同一逆映射闭参数延拓与真实端部区别 | `DIR-U-ASTRA-BREAKPOINT` | 原生Agda完整依赖核及源码/索引关系 | `FORMAL_CHECKED_WITH_SCOPE / SAME_MAP_CLOSED_EXTENSION` | K正性、内点一致、原metric连续、M两端同像/N异像、内点单射/闭域非单射 | Rich/Task/Trace/Done、原来源操作、无条件弱Lift、其它机制/GOLD/整体 | `'+REPORT+'`；`audit/astra-completion-20260920/DELIVERY.json` |\n'
  files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
 for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['R-ASTRA-INTERVAL-20260920'],'authorization':'用户ACTIVE Goal及既有T3状态/研究授权；同映射completion完成后返回原丰富结构与任务，原完整范围不变。','files':files}
 (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
 (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
