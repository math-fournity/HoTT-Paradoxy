#!/usr/bin/env python3
"""Canonical transaction for fixed arithmetic requests and remaining-scope recovery."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-TASK-COMPARISON';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第十九轮执行报告.md'
RUN='HoTT/verification/runs/20260920-MP-ASTRA-SQRT2-TASK-COMPARISON-001-01'
NEXT='BP-REMAINING-CLOSURE-01：按14断点模板与U00–U09核当前实际覆盖，先修本任务相关main证明版本缺口：PointRestoration现存字节已与d059dbf7b543092bce99333843f2bda16a06b327快照匹配，核exact manifest后仅集成对应证明/run及真实依赖，不恢复旧STATE/MEMORY、不混入其它作者改动。随后冻结有界的实际J/依赖运输、非平凡Partial/Glue/HIT或截断/商消费链，做资格消融与合法恢复；不重复同形小控制。九族算术组合不替代全HoTT决策/原广义圆环/弱Lift/必要性及总交付，父Goal继续OPEN。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','原算术规格与当前构造有实际请求/响应/Done，形成有界组合。'),
2:('DEEPENED','Output/Done按请求索引，向上Lift显式，不误作resizing。'),
3:('ALIGNED','多真定理组合不自动形成矛盾或同一任务承诺。'),
5:('ALIGNED','六族正响应与三族空性并存，归因没有预设击落。'),
7:('ALIGNED','三草稿及正式内核通过，样例真假与源规格桥都有项。'),
10:('ALIGNED','固定算术域不冒充全部现实任务和原广义圆环。'),
11:('ALIGNED','没有把分派函数或数学证书当物理时间过程。'),
12:('DEEPENED','可行性与对象真值分层：q=2查询可交付而答案false。'),
13:('DEEPENED','原表/根响应等价桥和错误Done控制，防止任务资格被重命名。'),
14:('ALIGNED','no是空性证书，不是成功见证；生成/给定数据来源明确。'),
15:('TENSION','当前原生组合没有支持自我否定；正确拒绝与正构造均保留。'),
17:('ALIGNED','原注释同一任务断言被当作被审来源，不由内核拒绝自动证成。'),
19:('ALIGNED','仍不从D非零或精确相遇失败推全部近似不可完成。'),
21:('DEEPENED','14本地源/41外部pin/220模块图与完整run、索引关系留存。'),
22:('ALIGNED','现实相对双目标不收窄为内部矛盾；真实使用链义务返回前沿。'),
31:('DEEPENED','实际旧Spec_A/B被原生接口等价连接，没有空壳模型。'),
34:('ALIGNED','九族分派不声称全类型/全程序可判定或任意输出可验证。'),
35:('DEEPENED','算术子任务可明确表达，原广义来源/物理语境仍未穷尽。'),
37:('NOT_TOUCHED','圆环广义操作本轮不推进，算术组合不代替它。'),
38:('CORRECTED','原拒签是已接受否定定理，不是Agda与HoTT不对齐收据。'),
39:('DEEPENED','基础核查区分任务成功、查询真假、原Spec_B缺正号等具体事实。'),
41:('ALIGNED','有界组合完成与完整Goal及整仓版本资格分开。'),
42:('ALIGNED','不以正确恢复消除全部风险，也不以风险名称夸大当前拒绝。'),
43:('CORRECTED','停止扩算术准备，回14模板剩余和相关版本欠账；计划过时状态原位修正。'),
44:('ALIGNED','真实输出与合同可供解释，不能替所有假想现实自证忠实。'),
45:('DEEPENED','响应索引保留必要完成条件，下一查实际自然消费者是否越界。'),
46:('ALIGNED','当前旧源和可重放实物为依据；下一有确切版本缺口和库使用链。')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_CHECKED_AND_RELATION_PASS_WITH_SCOPE'
 state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==192
 head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
 prior=json.loads((ROOT/'audit/astra-approx-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
 plan_commit=(OUT/'PLAN-COMMIT.txt').read_text().strip()
 docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
 (OUT/'RESUME.json').write_bytes(R.dump({'policy':'Same-T3 PROTOCOL v3 receipt reattestation; not a new full-emission claim','revision':192,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint192/current plan; all32 tracked hashes match','kc_stance_revisited':'All46 individually revisited against arithmetic request-comparison unit; core unchanged; original source samples and previous receipt retained','model_understanding':'NOT_CERTIFIED_BY_TOOL','objective':'完成四弹一体的redo','app_goal_status_observed':'active'}))
 plan=R.plan(ROOT,profile='research',task_ids=['R-ASTRA-APPROX-20260920']);assert not plan['review_required'];assert not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
 old=state['latest_session'];state['revision']=193;state['latest_session']=SID
 state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C302_C303_FORMAL_CHECKED_REQUEST_RESPONSE_COMPARISON','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
 state['records']['R-ASTRA-TASK-COMPARISON-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / FIXED_ARITHMETIC_REQUESTS_INTEGRATED','status':'nine_declared_families_checked_remaining_scope_open','depends_on':[],'related_records':[SID,'R-ASTRA-APPROX-20260920'],'full_sources':[REPORT,'HoTT/formal/dedekind-omega-missile/Sqrt2TaskComparison.agda','audit/astra-task-comparison-20260920/DELIVERY.json','audit/astra-task-comparison-20260920/REMAINING-PREFLIGHT.json'],'scope':'C302 nine declared Request families, explicit Output/Done and constructive yes/no dispatcher; feasibility differs from query truth. C303 exact original Spec_A/B equivalences, supplied/generated recovery, scoped original refusal and conditional fourth-layer sufficiency. No universal HoTT solver, necessity or full four-stage result.'}
 manifest=json.loads((ROOT/RUN/'source-manifest.json').read_text())
 state['records']['R-ASTRA-TASK-COMPARISON-20260920']['source_hashes']={f['path']:f['sha256'] for f in manifest['files'] if f['path'].endswith(('.agda','TOOLCHAIN.json'))}
 state['execution_control'].update(status='ACTIVE_GOAL_ARITHMETIC_CASE_INTEGRATED_REMAINING_CLOSURE_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
 session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-task-comparison-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C300/C301与revision192有实际证据
- status: FIXED_ARITHMETIC_REQUESTS_INTEGRATED / PARENT_OPEN

C302固定九族Request，Output/Done/Response向上Lift显式，六族认证响应和三族空性由dispatch给出。表示Done限定真实GOLD并证明输出值canonical，近似响应接真实Trace。q=2查询可行但答案false，Root不可行，不能把返回判定说成所有请求成功。

C303给原Spec_A/B与新响应的精确等价桥，保留旧B无正号并另证正根细化空性；给定/生成下切割响应相同，负三错误旧答案不满足Done。原M3否定定理和响应不等价、无表到根总映射都被接受，不是编译失败。第四层只保留SingleOmega输入下旧充分性；必要性未证。

三草稿均通过，一次fresh正式核约106秒，14本地源/41外部pin/{delivery['import_modules']}模块图，formal/关系/图检查PASS，无额外kernel rerun。源和库未换，主模块显式two-level。系统化断点计划从过时v1.4原位接到实际原生证据，v1.5与完整策略v1.21由{plan_commit}保存。

只读核PointRestoration未入main但与d059恢复快照同字节，当前未修复。下一动作：{NEXT}

PROTOCOL§5沿用46KC legacy原子bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；用户报告四分片。无Sub Agent、无push/tag/发布。T01–05原完整范围与请求资格；T06–10实际接口/原类型桥/条件前提；T11–17原生源核和对账；T18–21无部署改变；T22–24剩余覆盖/版本定位/当前计划纠偏；T25无AI合同变化；T26精确版本化。C01–C09共享方法NO_CHANGE，C10项目证据更新。

element_usage：closure/收据复认、research同任务/反控制、SOP返回剩余范围、verification源核、canonical事务、dev-notes。没有通用求解/审计平台新增。
'''

 audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: ARITHMETIC_REQUESTS_CHECKED_REMAINING_CLOSURE_NEXT\n- panorama_change: ADD_C302_C303_REQUEST_RESPONSE\n- essay_change: NO\n- update_decision: 九族算术组合与原规格桥完成，返回剩余覆盖和相关main版本缺口。\n- cross_conflicts: 可行性不是对象真值；no不是成功见证；旧拒绝不自动成为理论失配；小型化未决。\n- unresolved: 原广义来源/操作、原W Lift、其它机制/GOLD/四层整体。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、后继及反证条件 |\n|---|---|---|---|---|\n'
 headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
 for n,(kc,title) in enumerate(headings,1):
  rel,why=TOUCHED.get(n,('NOT_TOUCHED','本单元未推进该具名自指/反射/其它时间机制；来源对应不替代它。'))
  ev=('第十九轮001–004、C302/C303源码/run及原M1–M4；后继剩余覆盖/版本。若旧类型未保留、真假层次混同、未决缩层被算完成或源核hash变则撤回；实际同任务失配可重评。' if n in TOUCHED else '第十九轮003未触达范围；该具名机制或新直接证据成为当前任务时重开。')
  audit+=f'| `{kc}` | {title} | {rel} | {why} | {ev} |\n'
 audit+='''
## 扩展认知逐片复认

001问题/简化：请求身份及Done显式，不把不同输出仅以同一个数字称谓混同。002前提/时间：分派器的yes/no不是物理执行或所有目标成功。003圆环/ASK：q=2控制分开可完成与命题真值；圆环义务保持。004HoTT/自反：九族可判定不等于全HoTT决策/自验证。005表达/原文：原Spec_A/B等价桥避免偷偷改规格。006知识谱：原注释与实际定理身份分开，实际消费者仍须检查。007助力/阻力：有界算术做到接口后返回剩余覆盖，修正过时当前计划。008现实骨架：类型内正确完成不自证全部现实对应，继续核真实使用链。

## 已走过的路

实际原类型→Response桥、给定/生成响应一致、错误答案Done否定、原拒绝及条件充分性均进同一核包。当前证据没有把HoTT理论承诺定位为那个被否定的任务等价，原“完美击落”推论不成立为当前机器结论。

## 即将作出的选择与完备性

核14模板/U00–09当前覆盖，先按exact snapshot/manifest修本任务相关main版本欠账，随后固定实际J/Partial/Glue/HIT或截断/商链。未选继续同形算术或宣称全理论通过；不复原旧STATE/MEMORY。PointRestoration同字节只是预核，实际修复与验证仍待下一单元。

八轴/反思见第十九轮003。九构造族的模式覆盖与无限参数函数证明是本域证据，不能推到任意HoTT命题。独立对照为原类型等价桥、正根细化、q=2假答案成功与负三错译/恢复；新实际调用或语义要求进入时重评。
'''

 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[RUN],'claim_ids':['C-302','C-303'],'validation':'audit/astra-task-comparison-20260920/DELIVERY.json','extra_kernel_rerun':False,'parent_objective':'OPEN','app_goal_status_observed':'active'}
 for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-193'
 targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
 files=[]
 for rel in targets:
  raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
  if rel in (R.DIRECTION,R.PANORAMA):
   body,n=re.subn(r'(?m)^source_state_revision: 192$','source_state_revision: 193',body);assert n==1
   kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-193',body);assert n==1
  if rel=='MEMORY/001 - 当前执行队列.md':
   start=body.index('用户当前App Goal');end=body.index('\n\n',start)
   body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C302/C303已将原M1/M2/M3与GOLD接为九族Request/Output/Done/Response：六族认证响应、三族空性、原Spec_A/B等价桥、给定/生成恢复与真假层次控制均过核；第四层充分性仍带输入。旧拒签不是Agda/HoTT不对齐证明，未证必要性/全理论/现实失配。系统化断点计划已纠正早期过时状态。策略v1.21由'+plan_commit+'保存。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
  if rel=='方向追踪/002 - 治理与用户方向.md':
   lines=body.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):
     lines[i]=line.replace('BINARY_APPROX_CHECKED_TASK_COMPARISON_NEXT','ARITHMETIC_REQUESTS_CHECKED_REMAINING_CLOSURE_NEXT').replace('`OUT-ASTRA-APPROX-18` |','`OUT-ASTRA-APPROX-18`、`OUT-ASTRA-TASK-COMPARISON-19` |').replace('每个n的真实夹逼/宽度/Trace已核；下一算术任务整合；原广义圆环/弱Lift开放','九族算术合同已核；下一剩余覆盖/相关版本，再实际库消费者；原广义范围开放')
   body='\n'.join(lines)+'\n'
  if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-TASK-COMPARISON-19` | C302/C303固定算术九族与原规格对照 | `DIR-U-ASTRA-BREAKPOINT` | 原生Cubical源核/类型桥/真假与错误控制 | `FORMAL_CHECKED_WITH_SCOPE / FIXED_ARITHMETIC_REQUESTS_INTEGRATED` | 六族响应/三族空性、原Spec桥与恢复、第四层条件保留 | 剩余真实消费者/相关版本、原广义圆环/弱Lift、元层/整体 | `'+REPORT+'`；`audit/astra-task-comparison-20260920/DELIVERY.json` |\n'
  files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
 for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['R-ASTRA-APPROX-20260920'],'authorization':'用户ACTIVE Goal及既有T3状态/研究授权；完成算术九族组合后返回剩余覆盖与相关版本修复，完整父范围不变。','files':files}
 (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
 (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
