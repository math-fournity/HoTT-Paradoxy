#!/usr/bin/env python3
"""Canonical transaction for intrinsic rich curves and finite ambient tasks."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-RICH-TASK';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第十五轮执行报告.md'
RUN='HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-RICH-TASK-001-02'
NEXT='CASE-RING-CONTRACT-01：逐句对照用户原始圆环表述与022/023，固定实际Input/Denotes、初态、允许操作、观察和Done，核当前原生内在/丰富结构/有限AmbientStep结果分别覆盖哪一义务。保留全字段运输的同模型成功及预选直线N失败，不能互换任务；未指定的物理前提标OPEN，不由非紧性或有限核结果代证。只补当前主X实例所需连接，形成有界判词后进入AST-U02实际GOLD cut/查询/近似，不再扩充一般实分析。其余断点、无条件弱Lift和四层整体保持OPEN。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','实际圆/区间/闭图进入共同结构与有限任务，不停在抽象名称。'),
2:('DEEPENED','裸类型与Rich及操作类各有精确类型；源与核分层。'),
5:('ALIGNED','保留无丰富路径的负结果和全字段运输的同模型成功。'),
7:('ALIGNED','缺import导致的草稿失败保留，补导入后实跑，不作数学拒签。'),
10:('ALIGNED','环境步骤是明示模型，不冒充全部现实复原或其否定。'),
12:('DEEPENED','Step给出真实双向连续变换与交换图，端部不变量由此推出。'),
13:('DEEPENED','有限Trace携带操作见证；裸表示转换不自动提升为环境过程。'),
14:('DEEPENED','Success携带Trace与Done，MereSuccess明确截断；二者不冒充程序或物理完成。'),
15:('TENSION','全字段运输有同任务正成功，不能宣称HoTT必然删除来源。'),
17:('ALIGNED','022/023是被审解释，未经固定Step不把永不可完成当作前提。'),
19:('ALIGNED','有限Trace是操作次数，未据此认证物理时间连续性。'),
20:('ALIGNED','没有假定量子化或最小跳跃；物理对应保持OPEN。'),
21:('DEEPENED','13份本地源码及实际完整核与关系证据留存。'),
22:('ALIGNED','A/B原方向保留，下一闭合同一输入/允许操作/Done。'),
31:('DEEPENED','原生范型接受具体无路径/无Trace与非平凡正控制。'),
34:('ALIGNED','有限环境操作no-go不外推任意过程或弱域不可能。'),
35:('DEEPENED','原生Rich、闭图、观察、Step/Trace/Done已有实际实例，完整原任务仍须对照。'),
37:('TENSION','真实端部结构分离已证，但尚非HoTT现实相对缺陷。'),
38:('CORRECTED','实际univalence连裸载体，完整运输保结构；不能说它自动把直线N当完整M。'),
39:('DEEPENED','基本的端部观察已接实际载体，非共同Plane的恒等控制。'),
41:('ALIGNED','子命题与原Goal分开，正式证据/版本/运行各自核验。'),
42:('ALIGNED','既不抹去区别，也不把正确运输成功改称目标缺陷。'),
43:('CORRECTED','从几何准备返回实例合同；下一完成来源对照后进入GOLD支线。'),
44:('ALIGNED','真实对象与表示图使现实比方可审，但未认证全部物理模型。'),
45:('DEEPENED','把忽略的端部字段与实际遗忘/运输/可达性连接。'),
46:('DEEPENED','完整字段能够保持时保留成功，继续审查原输入究竟给了哪些数据。')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_CHECKED_AND_RELATION_PASS_WITH_SCOPE'
 state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==188
 head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
 plan_commit=(OUT/'PLAN-COMMIT.txt').read_text().strip()
 prior=json.loads((ROOT/'audit/astra-completion-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
 docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
 (OUT/'RESUME.json').write_bytes(R.dump({'policy':'PROTOCOL v3 same-T3 receipt reattestation; not a fresh full-emission claim','revision':188,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint188 and current strategy revision; all32 tracked hashes match','kc_stance_revisited':'All46 individually reconsidered; source samples10/35/39/43–46 reread','model_understanding':'NOT_CERTIFIED_BY_TOOL','app_goal_status_observed':'active','objective':'完成四弹一体的redo'}))
 plan=R.plan(ROOT,profile='research',task_ids=['R-ASTRA-COMPLETION-20260920']);assert not plan['review_required'];assert not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
 old=state['latest_session'];state['revision']=189;state['latest_session']=SID
 state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C293_C294_FORMAL_CHECKED_AND_RELATION_PASS','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
 state['records']['R-ASTRA-RICH-TASK-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / ACTUAL_INTRINSIC_RICH_AND_FINITE_TASK','status':'actual_rich_task_checked_with_scope','depends_on':[],'related_records':[SID,'R-ASTRA-COMPLETION-20260920'],'full_sources':[REPORT,'HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda','HoTT/formal/agda-unimath/hott-z/FiniteTrace.agda','HoTT/formal/agda-unimath/hott-z/NativeCurveTask.agda','HoTT/formal/agda-unimath/hott-z/NativeCurveTaskControls.agda','audit/astra-rich-task-20260920/DELIVERY.json'],'scope':'C293 actual intrinsic Rich/Bare diagrams: univalent bare path, no selected Rich path/lift, full-field transport positive. C294 finite ambient-homeomorphism traces/Done, both no-go directions, swap success, bare trace no universal lift, full-field transport success in the same model. Not all physical operations or complete original Input/Denotes correspondence.'}
 state['execution_control'].update(status='ACTIVE_GOAL_NATIVE_RICH_TASK_CHECKED_CASE_CONTRACT_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
 session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-rich-task-20260920/RESUME.json
- app_goal_status_observed: active
- objective: 完成四弹一体的redo
- previous_goal_turn: PROGRESS；C291/C292及revision188均有实际源核/事务证据
- status: ACTUAL_INTRINSIC_RICH_AND_FINITE_TASK_CHECKED / PARENT_OBJECTIVE_OPEN

C293的Rich以实际内在StrongPuncture/原(0,1)为载体，含参数化、平面实现、连续闭图及内点一致。实际barePath存在，预选mRich/nRich无路径、无任意bare路径的指定结构提升；完整字段运输保留M端部，运输后的区间结构不同于预选直线N。C294的AmbientStep由实际平面同胚与闭图相容给定，不直接假定端部不变量；有限Trace、拼接、Done、Success/MereSuccess及正反实例均原生检查。N↔M无有限该类Trace，坐标交换有非平凡成功；全部字段运输到区间载体也在同一个AmbientStep模型成功。全部物理操作和原Input/Denotes仍开放。

正式01先核前三模块，02纳入更强同模型运输正控制，二者均fresh；primary为02，{delivery['import_modules']}模块、13本地Agda文件，formal/关系检查PASS，meta verifier无额外kernel rerun。草稿001缺empty导入，003缺×导入，修复后通过；缺导入不属HoTT拒签。保留no-erasure配置与库公设，不认证全库一致性。

02的辅助导入图曾误复制01旧图，初次图对账失败；核命令/源码本身正确。保留错误imports.dot，另附真实原命令输出的imports.actual.dot并留GRAPH-RECONCILIATION，实际图与草稿完全相同后才验收。没有改原RUN/源码manifest，也没有为此增加核重跑。

策略v1.17由{plan_commit}保存。下一动作：{NEXT}

PROTOCOL§5沿用全46KC legacy原子bundle，登记G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；用户报告四分片。无Sub Agent、无push/tag/发布。T01–05原完整目标及来源不变；T06–10实际Rich与有限任务模型/对应边界；T11–17原生源码/核/证据；T18–21无部署/外部操作；T22–24状态/后继/历史保全；T25无AI合同改变；T26精确版本化。C01–C09共享治理方法NO_CHANGE，C10项目证据更新。

element_usage：closure和收据复认恢复任务；研究Skill核同任务/正控制；SOP推动回父范围；verification固定源核依赖；canonical writer保原子事务；dev-notes保存公开问答。无新通用设施。
'''
 audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: ORIGINAL_CASE_CONTRACT_THEN_GOLD\n- panorama_change: ADD_C293_C294_RICH_FINITE_TASK\n- essay_change: NO\n- update_decision: 真实丰富结构与有限任务模型已核，返回原输入/操作/Done对应。\n- cross_conflicts: 裸路径与Rich路径、环境Trace是不同类型；完整运输在同模型成功；原W Lift保留。\n- unresolved: 原Input/Denotes与允许操作的完整对应、无条件弱Lift、其它机制/GOLD/四层整体。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一动作及反证条件 |\n|---|---|---|---|---|\n'
 headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
 for n,(kc,title) in enumerate(headings,1):
  rel,why=TOUCHED.get(n,('NOT_TOUCHED','本单元未推进该项具名自指、全局反射或其它时间机制；闭参数数学项不替代它。'))
  ev=('第十五轮001–004、C293/C294源码与run；下一CASE-RING-CONTRACT-01；若闭图并非真实函数、Step被循环定义、正控制未保同任务或核/hash失配则撤回；保原输入的新过程触发重评。' if n in TOUCHED else '第十五轮003未触达范围；该具名机制/任务或新一手证据进入当前队列时重开。')
  audit+=f'| `{kc}` | {title} | {rel} | {why} | {ev} |\n'
 audit+='''
## 扩展认知逐片复认

001问题/简化：裸载体是真实曲线的内在类型，不是环境Plane。002前提/时间：有限操作Trace不等于物理时间运动。003圆环/ASK：真实端部字段进入Rich，Step由环境同胚/交换图给出，不先假定端部不变。004HoTT/自反：实际UA在裸层，完整运输保留结构；反射未推进。005表达/原文：具体结构可表达，完整原语境还需Input/Denotes。006知识谱：022/023关于永不可完成/宣布到达仍是被审解释。007助力/阻力：不以正确运输结果迎合击落，也不以形式正确关闭现实任务；下一回来源合同。008现实骨架：N直线与运输后N载体的数据不同，是否原任务允许替换必须逐项核来源。

## 已走过的路

真实Rich/Bare与C290等价、C291/C292闭图连接；noRichPath和fullTransportPath并存。AmbientStep没有端部同异的假定字段，保持/反射由实际映射推导；有限Trace的否定和非平凡swap、同模型完整运输成功同时实跑。scope是这一操作类，不是全部物理或用户原任务。

## 即将作出的选择与完备性

选择原圆环case合同对照：固定输入/来源/初态/允许操作/观察/Done，把已核内在、丰富结构和Trace放回原句，补当前实例必需的保真连接，形成有界判词后转U02实际GOLD。未选继续一般几何、仅重跑旧no-go、或把物理未知当无限前置。

八轴与八项SOP反思见第十五轮003；全称有限Trace归纳不枚举全部物理操作，不证明HoTT无缺陷。独立控制为真实坐标交换及相同Step/Done模型中的全字段运输成功。新同输入过程/原文或语义桥梁可重评。
'''
 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[RUN],'claim_ids':['C-293','C-294'],'validation':'audit/astra-rich-task-20260920/DELIVERY.json','extra_kernel_rerun':False,'parent_objective':'OPEN','app_goal_status_observed':'active'}
 for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-189'
 targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT))
 baseline=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(baseline.stdout)
 files=[]
 for rel in targets:
  raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
  if rel in (R.DIRECTION,R.PANORAMA):
   body,n=re.subn(r'(?m)^source_state_revision: 188$','source_state_revision: 189',body);assert n==1
   kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-189',body);assert n==1
  if rel=='MEMORY/001 - 当前执行队列.md':
   start=body.index('用户当前App Goal');end=body.index('\n\n',start)
   body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C293/C294接通实际内在载体的Rich/Bare/Forget及有限AmbientStep任务：裸Path与特定Rich无路径、完整运输保结构、N↔M该类有限Trace不成立、非平凡swap及同模型完整运输成功均过核。该操作类不冒充全部现实过程；Input/Denotes与原操作的完整对应尚需闭合。策略v1.17由'+plan_commit+'保存。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
  if rel=='方向追踪/002 - 治理与用户方向.md':
   lines=body.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):
     lines[i]=line.replace('NATIVE_SAME_MAP_COMPLETION_CHECKED_RICH_TASK_OPEN','NATIVE_RICH_FINITE_TASK_CHECKED_CASE_CONTRACT_OPEN').replace('`OUT-ASTRA-COMPLETION-14` |','`OUT-ASTRA-COMPLETION-14`、`OUT-ASTRA-RICH-TASK-15` |').replace('同一内在载体的Rich/Bare/Forget与Task/Trace/Done；弱Lift和原过程仍开放','原Input/Denotes/允许操作/Done对照，然后实际GOLD；弱Lift与完整原过程开放')
   body='\n'.join(lines)+'\n'
  if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-RICH-TASK-15` | C293/C294实际Rich结构与有限环境任务、完整运输正控制 | `DIR-U-ASTRA-BREAKPOINT` | 原生Agda及完整源核依赖/关系检查 | `FORMAL_CHECKED_WITH_SCOPE / INTRINSIC_RICH_AND_FINITE_TASK` | 真实载体和闭图、特定结构分离、全字段运输、有限Trace正反实例 | 原Input/Denotes与操作完整对应、弱Lift、其它机制/GOLD/整体 | `'+REPORT+'`；`audit/astra-rich-task-20260920/DELIVERY.json` |\n'
  files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
 for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['R-ASTRA-COMPLETION-20260920'],'authorization':'用户ACTIVE Goal及既有T3状态/研究授权；实际丰富结构和有限任务已核后返回原case合同，完整范围不变。','files':files}
 (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
 (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
