#!/usr/bin/env python3
"""Canonical transaction for actual structure consumers and native boundary observations."""
import argparse,importlib.util,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-STRUCTURED-CONSUMER';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第八轮执行报告.md'
LEAN_RUN='HoTT/verification/runs/20260920-MP-ASTRA-STRUCTURED-CURVE-001-02'
AGDA_RUN='HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001-01'
NEXT='BP-GEO-NATIVE-REAL-QUALIFICATION-01：从固定agda-unimath的real-numbers/dedekind-real-numbers.lagda.md及项目GOLD/CutRealLayer资格化原生实数/点集/拓扑接口、公理与必要函数，构造实际非空圆和指定点，明确当前Lean几何各命题的原生表达/保真义务。C275–279只闭合实际边界观察和原生Σ/ua运输，不能拿有限表、抽象Real参数或HIT S¹名字替代完整模型；原任务来源/固定条件、其它断点机制、GOLD及四层整体仍未完成。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','原任务端部观察→实际结构→原生有限图，结论范围先行。'),
2:('DEEPENED','Lean子空间Bare与原生边界图环境Bare分开，真实结构输入与观察保持明确。'),
5:('ALIGNED','正反控制均真实检查，没有先要求HoTT失败。'),
6:('ALIGNED','复用已有时间模型，本轮不把结构运输冒充新的时间连续性结论。'),
7:('ALIGNED','Lean四草稿及原生显式CLI记录完整；源码和双核结果代替AI自述。'),
10:('ALIGNED','现实相对任务仍开放，当前边界差异不升级为内部矛盾或非现实性。'),
12:('DEEPENED','消费者实际询问端点像重合，恢复只对相同输入/不同输出规格定级。'),
13:('DEEPENED','保持整个completion图的对应与只保开曲线内在同胚分别检查。'),
14:('ALIGNED','原生图可构造不等于完整实数模型或物理能力已经交付。'),
15:('TENSION','保留端部图的原生HoTT能区分实例，当前不支持抽象必然导致错误识别。'),
17:('ALIGNED','完整数据运输正控制与结构非等价同时保留，不以目标偏好筛选。'),
21:('DEEPENED','五claim、Lean和原生Agda两包实际运行及各自双检查通过。'),
22:('ALIGNED','A/B双向目标保持；有限观察的正保持没有代替完整现实任务。'),
31:('DEEPENED','实际几何提供条件输入，原生严格规则接受完整结构的表达与运输。'),
34:('ALIGNED','无结构对应/无共同裸恢复与正运输分别定量词，不称一切恢复不可能。'),
35:('DEEPENED','原生HoTT已表达所选端部图；完整实数几何和用户全部结构仍需表达。'),
37:('TENSION','未找到HoTT缺陷，不能把新的边界定理计作原目标已实现。'),
38:('TENSION','三条实际库接口消费正常，不能据此指控作者忽视端部，亦不外推全库。'),
39:('DEEPENED','从实际边界函数、ΣPathP第二分量及ua的数据运输检查基础处条件。'),
41:('ALIGNED','两内核用于实物核查，形式接口与可复用证明真实接通。'),
42:('ALIGNED','经典公理/native safe/各自Bare及翻译限制公开，不让PASS隐藏换题。'),
43:('DEEPENED','完成局部观察后转真正原生实数模型资格，不继续重复同形端点反例。'),
44:('ALIGNED','以实际环境和边界值理解现实映射，没有否认现实可把握性。'),
45:('DEEPENED','明确字段何时随运输保留、何时被forget删除，归因须回真实任务。'),
46:('ALIGNED','端部关系由实际completion算出而非答案标签，继续完整对象资格。')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 assert json.loads((OUT/'DELIVERY.json').read_text())['status']=='TWO_PACKAGES_DUAL_LOCAL_PASS'
 state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==181
 head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text())
 assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
 prior=json.loads((ROOT/'audit/astra-endpoint-closure-20260920/RESUME.json').read_text())
 assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
 docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
 (OUT/'RESUME.json').write_bytes(R.dump({'policy':'Same-context same-T3 receipt reattestation under PROTOCOL v3; not fresh full emission','revision':181,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint181 plus historical explanation/plan v1.9/v1.10; all32 HEAD tracked hashes match','kc_stance_revisited':'All46 prior positions retained and individually reconsidered below; original samples10/35/39/43–46 retained','app_goal_status_observed':'paused','execution_authority':'Current user message 开始; no tool available to resume the App scheduler','model_understanding':'NOT_CERTIFIED_BY_TOOL'}))
 plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert plan['revision']==181
 (OUT/'PLAN-SNAPSHOT.json').write_bytes(R.dump(plan))
 old=state['latest_session'];state['revision']=182;state['latest_session']=SID
 state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C275_C279_TWO_PACKAGES_DUAL_LOCAL_PASS','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
 state['records']['R-ASTRA-STRUCTURED-CONSUMER-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / ACTUAL_GEOMETRY_AND_NATIVE_SELECTED_OBSERVATION','status':'complete_with_scope','depends_on':[],'related_records':[SID,'R-ASTRA-ENDPOINT-CLOSURE-20260920'],'full_sources':[REPORT,'HoTT/formal/astra-real-geometry/StructuredCurve.lean','HoTT/formal/astra-breakpoint-check/GeometricBoundaryObservation.agda','audit/astra-structured-consumer-20260920/DELIVERY.json'],'scope':'C275–279: actual completed curve structures distinguish endpoints, selected integral observation and coordinate-swap action are exact, native Sigma/ua retain diagram structure. Two Bare interfaces and complete real-geometry translation explicitly remain distinct/open.'}
 state['execution_control'].update(status='USER_STARTED_STRUCTURED_OBSERVATION_CHECKED_APP_GOAL_PAUSED',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
 session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-structured-consumer-20260920/RESUME.json；同档延续、core未变、32HEAD hash一致、46KC回评
- app_goal_status_observed: paused；本轮未调用pause，现有工具无resume接口
- execution_authority: 用户本轮明确“开始”，按此执行；不宣称App自动续行已恢复
- status: C275_C279_FORMAL_CHECKED_WITH_SCOPE / PARENT_OBJECTIVE_OPEN

原重新执行裁决由439499a保存；本轮进入实际结构消费者。Lean CurvePresentation来自同一F的真实interior/completion，bare内在同胚不能提升为保completion/端部对应，观察Coincident不随任意bare同胚运输。环境全运输与开闭参数反向均为正控制；整数坐标嵌入单射，实际n/m边界及坐标交换精确对应。

原生Cubical Agda使用相同整数表，证明无交换边界等价/无RichDiagram路径/无同输入双恢复；ua配套运输和实际坐标交换计算通过。native Bare为边界图环境载体，Lean Bare为开曲线像；有限共同观察不冒充两完整接口或所有实数的翻译。直接核对并实际消费ua、ua-gluePathExt和ΣPathP三接口，不作全库无误用结论。

两包正式运行与原命令重放/本地关系检查通过。Lean标准三公理；Agda真safe/cubical/guardedness源码及显式CLI草稿。Lean四草稿保留，成功前capture-01保留而primary-02；BoundaryIncidence按08beee2快照原字节消费，不改旧run。没有修改公共validator或Host。

反思在第八轮004；方案v1.10已提交25c7800。下一动作：{NEXT}

按PROTOCOL§5使用全46KC legacy审计兼容bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持。无Sub Agent、无automation、无push/tag/发布。T01–05原要求不变；T06–10实例化结构接口；T11–17两核源码/运行/依赖新增；T18–21部署不变；T22–24当前状态/原件/调度事实更新；T25模型与权限不变；T26精确版本化。C01–C09无共享治理规则变化，C10新增项目证据。
'''
 audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: FULL_NATIVE_REAL_QUALIFICATION_NEXT\n- panorama_change: ADD_C275_C279_STRUCTURED_OBSERVATION\n- essay_change: NO\n- update_decision: 接通实际观察与原生结构运输，继续完整模型而非重复控制。\n- cross_conflicts: 两个Bare接口不同；完整现实任务与有限观察不能等同。\n- unresolved: 完整原生实数/拓扑、源历史/固定条件、其它机制和四层集成。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一动作及反证条件 |\n|---|---|---|---|---|\n'
 headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
 for n,(kc,title) in enumerate(headings,1):
  relation,why=TOUCHED.get(n,('NOT_TOUCHED','本轮未检查该具体自指、不可判定性或其它时间/逻辑命题；边界观察结果不替代。'))
  ev=('C275–279两包源码/run与第八轮001/002/004；实际端部值或类型/hash失败撤回；完整原任务有新增必需字段则补模型；不以有限对应升级整个实数HoTT翻译。' if n in TOUCHED else '第八轮004未触达范围；该主题具名任务或新证据出现时再进入。')
  audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
 audit+='''
## 扩展认知逐片复认

001问题/简化：实际边界函数进入结构，不用来源标签冒充模型。002前提/时间：旧时间构造作为输入，当前无新增物理完成声称。003圆环/ASK/A-B：强结构否定与正运输同时交付，完整任务仍需更多条件。004HoTT/自反：原生Σ/ua实际运行，完整实数翻译未认证，自反未触达。005表达/原文/文章：两Bare接口差异明示，原用户问题不被有限观察替换。006知识谱：三个版本化库接口真实消费，未作全库穷尽。007助力/阻力：不把新增拒绝证书自动叫成功，转完整原生模型资格。008现实骨架：真实初末曲线给出了观察值，仍继续把握全对象及必要条件。

## 已走过的路

先前只有一般BoundaryIncidence，本轮实际几何提供n/m与端点性质，整数嵌入反射相等、具体坐标动作交换；原生图和完整ua运输接受。没有HoTT错误识别命中，只有正常结构边界。App Goal仍显示paused，但本轮用户开始指令真实授权执行，未伪称自动调度恢复。

## 即将作出的选择与完备性

选择固定agda-unimath实数入口和GOLD/CutRealLayer资格化完整原生模型及公理，不用抽象参数/Bool/HIT圆充数。八轴/分母/范围外见第八轮004；本轮全称量化相应等价，不是有限采样或开放世界完备。独立控制为环境全运输/参数反向/native坐标交换；两核分别检查，不认证一般互译。完整Goal原范围保留。
'''
 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[LEAN_RUN,AGDA_RUN],'prior_successful_capture':'HoTT/verification/runs/20260920-MP-ASTRA-STRUCTURED-CURVE-001-01','validation':'audit/astra-structured-consumer-20260920/DELIVERY.json','claim_ids':['C-275','C-276','C-277','C-278','C-279'],'parent_objective':'OPEN','app_goal_status_observed':'paused'}
 for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-182'
 files=[]
 for rel in list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT)):
  b=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else b.decode()
  if rel in (R.DIRECTION,R.PANORAMA):
   body,n=re.subn(r'(?m)^source_state_revision: 181$','source_state_revision: 182',body);assert n==1
   kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-182',body);assert n==1
  if rel=='MEMORY/001 - 当前执行队列.md':
   start=body.index('用户本线程持续Goal');end=body.index('\n\n',start)
   body=body[:start]+'用户本线程持续Goal的完整目标未完成；本轮“开始”授权已实际执行，App Goal读取仍paused，工具无resume接口，未宣称自动续行已恢复。C275–279接通实际曲线结构、精确整数边界观察和原生Σ/ua运输，两包双检查PASS；有限观察不冒充完整实数模型，当前无HoTT错误识别命中。策略v1.10由25c7800保存。下一动作BP-GEO-NATIVE-REAL-QUALIFICATION-01：固定agda-unimath实数入口与GOLD/CutRealLayer，核公理、拓扑接口和实际非空点集模型；完整GEO04、其它机制及四层整体仍开放。入口：`'+REPORT+'`。'+body[end:]
  if rel=='方向追踪/002 - 治理与用户方向.md':
   lines=body.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]='| `DIR-U-ASTRA-BREAKPOINT` | 完成断点检查并按原意重执行四层论证 | 用户持续目标及本轮开始指令 | `OPEN_OBJECTIVE / STRUCTURED_OBSERVATION_CHECKED` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-BREAKPOINT-01`、`OUT-ASTRA-RESTORATION-02`、`OUT-ASTRA-PROOF-WIRING-03`、`OUT-ASTRA-REAL-CIRCLE-04`、`OUT-ASTRA-AMBIENT-CIRCLE-05`、`OUT-ASTRA-CURVE-DEFORMATION-06`、`OUT-ASTRA-ENDPOINT-CLOSURE-07`、`OUT-ASTRA-STRUCTURED-CONSUMER-08` | 完整原生实数/拓扑与同任务资格；不以有限观察充数 | `Astra继续尝试/四弹一体完整研究策略/010 - 断点检查接入与总目标执行账本.md` |'
   body='\n'.join(lines)+'\n'
  if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-STRUCTURED-CONSUMER-08` | C275–279实际结构、整数观察与原生ua完整运输 | `DIR-U-ASTRA-BREAKPOINT` | Lean+Cubical Agda两包实际核/原命令重放/关系检查 | `FORMAL_CHECKED_WITH_SCOPE / SELECTED_OBSERVATION_BRIDGE` | 真实端部图不可混同，全结构运输正常；观察及坐标动作精确对应 | 全实数跨内核翻译/全部现实约束/自然误用/HoTT缺陷 | `'+REPORT+'`；`audit/astra-structured-consumer-20260920/DELIVERY.json` |\n'
  files.append({'path':rel,'expected_sha256':R.sha(b),'text':body})
 for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户本轮开始及既有完整研究授权；登记C275–279，区分App paused与当前执行，继续完整原生模型资格，不缩减目标。','files':files}
 (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
 (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
