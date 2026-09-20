#!/usr/bin/env python3
"""Canonical transaction for binary-precision approximation and exact-task comparison."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-APPROX';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第十八轮执行报告.md'
RUN='HoTT/verification/runs/20260920-MP-ASTRA-SQRT2-APPROX-001-01'
NEXT='AST-U02-SQRT2-TASK-COMPARISON-01：把原M1/M2/M3及当前GOLD表示、精确查询、按n近似接成明确的请求/响应/Done与算术单例组合包；固定真实输入、输出、算法、空性和恢复，检查尚缺的识别/兑现连接。不能把组合真定理当作HoTT曾许诺被否定的任务等价，也不把Pell整数D当区间宽度。完成后回剩余断点消费者/按实际依赖激活的元层与总验收；原广义圆环、弱Lift、同层小型化/必要性及四层整体保持OPEN，不增加任意实分析前置。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','每个n的真实L/U及宽度证书接到先前标准GOLD，不停在形式名字。'),
2:('DEEPENED','保持原ℚ，原代数证明中点，不换QuoQ适配库接口。'),
3:('DEEPENED','正间隙和有限精度完成在同一输出中并存，合取命题精确。'),
5:('ALIGNED','保留近似成功与精确相遇失败，不预设都失败或都成功。'),
7:('ALIGNED','三草稿及fresh原生核通过；全n由证明承担，闭项只作控制。'),
10:('ALIGNED','当前有限精度合同不是现实物理过程或原圆环全部操作。'),
11:('DEEPENED','RefinementTrace显式n次细化，未把逻辑索引说成物理时间。'),
12:('DEEPENED','输出同时携带成员与所请求宽度，初始错误精度有否定控制。'),
13:('DEEPENED','算法、有限见证与Done关联，同一成功输出非零由依赖Σ记录。'),
14:('DEEPENED','每个n的有限交付已构造，未将其等同一次执行所有精度。'),
15:('TENSION','原生规则给出精度任务正恢复，不能继续以有余距否定该Done。'),
17:('ALIGNED','原M1注释与实际整数D命题区分；数学证明不为宽泛叙事背书。'),
19:('CORRECTED','精确不相遇不推出按精度无法完成；原稠密过程解释需同Done。'),
20:('ALIGNED','没有从该算法证明量子化、最小尺度或物理运动结论。'),
21:('DEEPENED','12本地源码/41外部pin/218模块图与正式run真实保存。'),
22:('ALIGNED','两方向保持，先按真实任务比较，不把改Done成功当原任务成功。'),
31:('DEEPENED','原生范型接实际Bracket、Trace和全部n，不靠空域或参数壳。'),
34:('ALIGNED','有限ExactMeeting空性限本二分，未外推所有现实或理论过程。'),
35:('DEEPENED','算法与精度合同已表达，原广义哲学理论仍未全部形式化。'),
37:('NOT_TOUCHED','原圆环广义来源/操作不因算术本轮有结果而关闭。'),
39:('DEEPENED','基础核查定位D不是宽度、非零不是精度失败。'),
41:('ALIGNED','子包精度结果与全Goal/整仓公开资格分开。'),
42:('ALIGNED','没有迎合击落结论，也没有用理论正结果否认未定现实任务。'),
43:('CORRECTED','达到二进制范围即转算术任务整合，不无限扩实分析。'),
44:('ALIGNED','实际可读的有理输出及两步归约作为数学现实模型。'),
45:('DEEPENED','完成性质按输入n/精确相遇分别定义，防止解释回原任务时越级。'),
46:('ALIGNED','真实L/U、实际输出和错误精度控制落实对应，不只讲一般原理。')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_CHECKED_AND_RELATION_PASS_WITH_SCOPE'
 state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==191
 head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
 prior=json.loads((ROOT/'audit/astra-gold-cut-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
 plan_commit=(OUT/'PLAN-COMMIT.txt').read_text().strip()
 docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
 (OUT/'RESUME.json').write_bytes(R.dump({'policy':'Same-T3 PROTOCOL v3 receipt reattestation; not a new full-emission claim','revision':191,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint191/current plan; all32 tracked hashes match','kc_stance_revisited':'All46 individually revisited against binary-precision unit; core unchanged; original source samples and previous receipt retained','model_understanding':'NOT_CERTIFIED_BY_TOOL','objective':'完成四弹一体的redo','app_goal_status_observed':'active'}))
 plan=R.plan(ROOT,profile='research',task_ids=['R-ASTRA-GOLD-CUT-20260920']);assert not plan['review_required'];assert not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
 old=state['latest_session'];state['revision']=192;state['latest_session']=SID
 state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C300_C301_FORMAL_CHECKED_BINARY_APPROX_AND_PELL','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
 state['records']['R-ASTRA-APPROX-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / BINARY_PRECISION_APPROXIMATION','status':'all_binary_precision_approx_complete_with_scope_task_comparison_next','depends_on':[],'related_records':[SID,'R-ASTRA-GOLD-CUT-20260920'],'full_sources':[REPORT,'HoTT/formal/dedekind-omega-missile/Sqrt2Bisection.agda','HoTT/formal/dedekind-omega-missile/ApproxPellComparison.agda','audit/astra-approx-20260920/DELIVERY.json'],'scope':'C300 actual GOLD Q/L/U bisection, all-n exact dyadic width, nested bounds and n-refinement certificate. C301 same successful output nonzero, no finite exact meeting, initial precision counterexample and original Pell/rational-root coexistence. Not all-epsilon real convergence, CPU/physical time or full four-stage completion.'}
 manifest=json.loads((ROOT/RUN/'source-manifest.json').read_text())
 state['records']['R-ASTRA-APPROX-20260920']['source_hashes']={f['path']:f['sha256'] for f in manifest['files'] if f['path'].endswith(('.agda','TOOLCHAIN.json'))}
 state['execution_control'].update(status='ACTIVE_GOAL_BINARY_APPROX_CHECKED_TASK_COMPARISON_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
 session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-approx-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C297–299与revision191有实际证据
- status: BINARY_PRECISION_REALIZATION_CONSTRUCTED / PARENT_OPEN

C300保持原GOLD Q与L/U，直接证明中点/半宽恒等式；Bracket携成员，refine内缩；∀n输出宽度为递归dyadicWidth、保持初始下界1与上界2的范围，并有恰n次refine的依赖证书。packedBounds接既有goldReal，n=2端点5/4、3/2由refl检查。C301在依赖Σ里记录同一成功输出仍非零，精确相遇为空；初始有效Bracket不满足精度1。旧Pell整数D非零及有理根空性与精度成功同环境成立，不把D与宽度混同。

三个草稿均通过；一次fresh正式核102秒，12本地模块/41外部pin/{delivery['import_modules']}模块图，formal/关系/图检查PASS，无额外kernel rerun。查明库现成QCommRing使用另一QuoQ，所以当前中点使用原Q代数，未改原对象。RefinementTrace计细化调用，不是CPU/物理时间；没有新增任意实数ε共终性、Pell收敛或实数环方程。

策略v1.20由{plan_commit}保存。下一动作：{NEXT}

PROTOCOL§5沿用全46KC legacy原子bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；用户报告四分片。无Sub Agent、无push/tag/发布。T01–05原范围和精度Done；T06–10算法/证书/同一输出与旧任务边界；T11–17原生源码及固定源核；T18–21无部署变化；T22–24新结果/整合后继/旧原件；T25无AI合同变化；T26精确版本化。C01–C09共享治理方法NO_CHANGE，C10项目证据更新。

element_usage：closure/收据复认、research的同任务控制、SOP回主链、verification真实核与源图、canonical原子事务、dev-notes。没有通用平台扩建。
'''

 audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: BINARY_APPROX_CHECKED_ARITHMETIC_TASK_INTEGRATION_NEXT\n- panorama_change: ADD_C300_C301_BINARY_APPROX\n- essay_change: NO\n- update_decision: 按n近似、同一输出非零及旧Pell对照完成，下一算术任务整合。\n- cross_conflicts: 精度Done与精确相遇不同；Pell整数D不是区间宽度；n次细化不是CPU/物理时间。\n- unresolved: 原广义来源/操作、原W Lift、其它机制/GOLD/四层整体。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、后继及反证条件 |\n|---|---|---|---|---|\n'
 headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
 for n,(kc,title) in enumerate(headings,1):
  rel,why=TOUCHED.get(n,('NOT_TOUCHED','本单元未推进该具名自指/反射/其它时间机制；来源对应不替代它。'))
  ev=('第十八轮001–004、C300/C301源码/run和原M1/M2；后继任务整合。若Q/L/U被换、成员或宽度失败、同一输出不耦合、D被混为宽度或hash变则撤回；新同Done反例重评。' if n in TOUCHED else '第十八轮003未触达范围；该具名机制或新直接证据成为当前任务时重开。')
  audit+=f'| `{kc}` | {title} | {rel} | {why} | {ev} |\n'
 audit+='''
## 扩展认知逐片复认

001问题/简化：原Q与谓词保持，未换更方便的QuoQ。002前提/时间：n次细化、证明检查和物理时间分开。003圆环/ASK：给定n的精度Done不同于精确相遇，算术不替圆环。004HoTT/自反：原生核接有限证书，自反未推进。005表达/原文：旧M1已读，D的整数身份不被间隙比喻取代。006知识谱：现成工具不适同载体就用原代数，不为接口改题。007助力/阻力：正负结果同时保留，转任务整合而非继续堆分析。008现实骨架：同一成功输出有余距，现实解释须保同一完成标准。

## 已走过的路

Bracket成员/中点/宽度/嵌套全部有证明，∀n及n次Trace不是有限样例外推。实际n=2归约与精度1错误输出反例互校。旧Pell指标、精确有理根、精确相遇与近似的真值分别保留，未宣称原精确任务被近似完成。

## 即将作出的选择与完备性

下一算术请求/响应/Done整合，连实际旧M1/M2/M3与REP/QUERY/APPROX，查理论许诺和真实输入；不是把三真定理组合成缺陷。随后回剩余断点/元层实际依赖/总验收。原广义圆环、弱Lift、小型化及整体仍OPEN。

八轴和反思见第十八轮003。全部n由原生归纳，单步范围比两步样例更强；有效但精度不足的初始输出是独立控制。任意ε/所有cut算法/Pell收敛/物理成本不在本范围，新同任务证据触发再评。
'''

 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[RUN],'claim_ids':['C-300','C-301'],'validation':'audit/astra-approx-20260920/DELIVERY.json','extra_kernel_rerun':False,'parent_objective':'OPEN','app_goal_status_observed':'active'}
 for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-192'
 targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
 files=[]
 for rel in targets:
  raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
  if rel in (R.DIRECTION,R.PANORAMA):
   body,n=re.subn(r'(?m)^source_state_revision: 191$','source_state_revision: 192',body);assert n==1
   kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-192',body);assert n==1
  if rel=='MEMORY/001 - 当前执行队列.md':
   start=body.index('用户当前App Goal');end=body.index('\n\n',start)
   body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C300/C301已核原GOLD上的全n二分夹逼：成员、嵌套、宽度=(1/2)^n及恰n次细化证书；同一成功输出仍非零，精确相遇为空，旧Pell整数D非零与之相容而非同量。n=2实际归约及错误精度控制通过；不新增任意ε收敛或CPU/物理时间承诺。策略v1.20由'+plan_commit+'保存。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
  if rel=='方向追踪/002 - 治理与用户方向.md':
   lines=body.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):
     lines[i]=line.replace('STANDARD_GOLD_QUERY_CHECKED_APPROX_NEXT','BINARY_APPROX_CHECKED_TASK_COMPARISON_NEXT').replace('`OUT-ASTRA-GOLD-CUT-17` |','`OUT-ASTRA-GOLD-CUT-17`、`OUT-ASTRA-APPROX-18` |').replace('标准GOLD表示/查询已核；下一全精度二分与Pell完成标准对照；原广义圆环/弱Lift开放','每个n的真实夹逼/宽度/Trace已核；下一算术任务整合；原广义圆环/弱Lift开放')
   body='\n'.join(lines)+'\n'
  if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-APPROX-18` | C300/C301全二进制精度夹逼与精确相遇对照 | `DIR-U-ASTRA-BREAKPOINT` | 原生Cubical全称证明/实际归约/源核关系 | `FORMAL_CHECKED_WITH_SCOPE / BINARY_PRECISION_REALIZATION` | 原Q及L/U、宽度与n次Trace；同一输出非零；旧Pell/有理根共存 | 算术任务整合、广义圆环/弱Lift、元层依赖/整体 | `'+REPORT+'`；`audit/astra-approx-20260920/DELIVERY.json` |\n'
  files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
 for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['R-ASTRA-GOLD-CUT-20260920'],'authorization':'用户ACTIVE Goal及既有T3状态/研究授权；完成按n近似及旧精确任务对照后转算术整合，完整父范围不变。','files':files}
 (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
 (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
