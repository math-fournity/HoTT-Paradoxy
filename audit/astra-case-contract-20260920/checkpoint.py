#!/usr/bin/env python3
"""Canonical transaction for exact supplied-source denotation and the GOLD return."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-CASE-CONTRACT';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第十六轮执行报告.md'
RUN='HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-SOURCE-CONTRACT-001-01'
NEXT='AST-U02-GOLD-CUT-01：资格化旧Cubical配置与CutGoldForm实际L/U，按Book标准命题值切割规格装配dcut及命题性/宇宙层级，再接查询与近似；已有强见证字段应通过合法截断装配命题规格，不改成所有实数必须携带强选择数据。先审计旧注释关于取等价类和Ω/LEM/resizing的解释，不把附加小型化当标准对象存在前提。查询/近似/精确有理根/切割表示分别固定Done，算术支线未有保真归约前不冒充圆环。原圆环广义来源/允许操作、原W无条件Lift、其它断点及四层整体保持OPEN；只在新保任务证据出现时重开已验同形控制。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','六段原文逐项对应，case范围有实际模型证据而非只做状态复述。'),
2:('DEEPENED','输入/源图/输出/完成字段和理论配置实际具名；不隐去给定数据。'),
5:('ALIGNED','保留成功重呈现与普通N错误输出，归因不先验决定。'),
7:('ALIGNED','原始bytes/hash核对与实际内核分开，警告不充当否定证明。'),
10:('ALIGNED','精确源图合同不冒充全部现实过程，原语境未覆盖处明确开放。'),
12:('DEEPENED','Input提供原源与已核等价，Done后输出满足独立Satisfies。'),
13:('DEEPENED','checkedOutput接有限Run与最终图对应；裸载体检查反例实际化。'),
14:('ALIGNED','有限数学证书不冒充物理过程执行或任意数值求解。'),
15:('TENSION','全字段的保图重呈现确有正实例，不能预设抽象必然本例失配。'),
17:('ALIGNED','直接用户原文与旧AI方案分开；022/023自标source=user不作数学认证。'),
19:('ALIGNED','未从非紧性/非完备性推任意过程不可完成。'),
20:('ALIGNED','量子化/最小尺度只记来源假设，无机器物理结论。'),
21:('DEEPENED','14本地源码、正式run、41外部pin及源索引证据真实留存。'),
22:('ALIGNED','两种现实相对方向保留，当前结果限定source-supplied表示任务。'),
31:('DEEPENED','实际范型容纳Input/Denotes/Run与非空原圆实例。'),
34:('ALIGNED','反例只否定bare检查足够，不否定所有可能来源恢复方法。'),
35:('DEEPENED','具名接口已有实际项；物理历史/任意形变不谎称已全部表达。'),
37:('TENSION','用户原圆环的重要区别保留，但当前链未构成HoTT缺陷见证。'),
38:('ALIGNED','本例正确对应和错误输出可区分，不据此声称全库无误用。'),
39:('DEEPENED','基础问题回到同一输入与完成标准，不只讲同胚定义。'),
41:('ALIGNED','局部数学与来源覆盖分别验收，父Goal继续。'),
42:('ALIGNED','不把充分数据变必要收费，也不以旧叙事要求结果迎合。'),
43:('CORRECTED','当前几何/表示合同够用即转实际GOLD，不持续扩准备层。'),
44:('ALIGNED','给定源图是具体数学现实模型，不否定更广假想现实有意义。'),
45:('DEEPENED','原允许变形构成独立holdout，纠正精确图Denotes的外推。'),
46:('DEEPENED','原输入中数据真实列出；用同输入错误输出检验对应而非空来源标签。')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_CHECKED_AND_RELATION_PASS_WITH_SCOPE'
 source_inputs=json.loads((OUT/'SOURCE-INPUTS.json').read_text());assert len(source_inputs['messages'])==6
 state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==189
 head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
 prior=json.loads((ROOT/'audit/astra-rich-task-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
 plan_commit=(OUT/'PLAN-COMMIT.txt').read_text().strip()
 docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
 (OUT/'RESUME.json').write_bytes(R.dump({'policy':'Same-T3 PROTOCOL v3 receipt reattestation; not a new full-emission claim','revision':189,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint189/current plan; all32 tracked hashes match','kc_stance_revisited':'All46 individually revisited against supplied-source case; unchanged core, original samples10/35/39/43–46 and six direct source messages considered','model_understanding':'NOT_CERTIFIED_BY_TOOL','objective':'完成四弹一体的redo','app_goal_status_observed':'active'}))
 plan=R.plan(ROOT,profile='research',task_ids=['R-ASTRA-RICH-TASK-20260920']);assert not plan['review_required'];assert not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
 old=state['latest_session'];state['revision']=190;state['latest_session']=SID
 state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C295_C296_FORMAL_CHECKED_AND_SOURCE_CASE_RECONCILED','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
 state['records']['R-ASTRA-CASE-CONTRACT-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / SOURCE_SUPPLIED_REPRESENTATION_CONTRACT','status':'given_source_case_contract_checked_greater_original_scope_open','depends_on':[],'related_records':[SID,'R-ASTRA-RICH-TASK-20260920'],'full_sources':[REPORT,'HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda','audit/astra-case-contract-20260920/SOURCE-INPUTS.json','audit/astra-case-contract-20260920/DELIVERY.json'],'scope':'C295 explicit supplied-source Input/Denotes/Run and sound output, actual circle/interval instance. C296 same-input bare output false positive. Six direct originals and022/023 source-aligned; exact diagram reexpression not all provenance/deformations/physical restoration. Return to actual GOLD while full parent stays open.'}
 state['execution_control'].update(status='ACTIVE_GOAL_SOURCE_CASE_CONTRACT_CHECKED_GOLD_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
 session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-case-contract-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C293/C294及revision189有实际源核/事务证据
- status: SOURCE_SUPPLIED_CASE_CONTRACT_CHECKED / PARENT_OBJECTIVE_OPEN

六段直接用户原文从既有canonical reader导出逐字/hash/分片范围核对并冻结，022/023另记历史AI方案。用户允许其余部分变形，故不能把整图不变当全部现实同一性；全平面同胚也不是原文已穷尽的操作集合。

C295明确Input给source Rich、targetCarrier、encoding；State/Step/Observation/Denotes/Output/Satisfies/Done/Run具名实现，完整运输给逐参数图保持、有限Run与checkedOutput。actualInput是真实mRich/原区间/C290等价。C296在同一输入下普通N满足载体检查却不满足Denotes/Satisfies，实际输出不是N；精确N目标的旧模型no-go保留。这是足够数据下的保图重呈现，不是所有方法的最小必要数据、全部物理来源或任意复原。

一次fresh正式Agda run约259秒，{delivery['import_modules']}模块，14本地Agda、41外部pin；formal/关系/图对账PASS，无额外kernel rerun。草稿001 exit0伴多余using名字警告，移除后002干净通过。捕获器图命令/复制共用一个graph变量，避免沿用上一轮路径错误。

策略v1.18由{plan_commit}保存。下一动作：{NEXT}

PROTOCOL§5沿用46KC legacy原子bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001继续披露；报告四分片。无Sub Agent、无push/tag/发布。T01–05保持用户原目标并区分模型选择；T06–10给定源合同及输入/输出/Done连接；T11–17原生源核和源快照；T18–21无部署/外部操作；T22–24结果/后继/历史原件保全；T25无AI合同变化；T26精确版本化。C01–C09共享治理方法NO_CHANGE，C10项目证据更新。

element_usage：closure/收据复认恢复；requirements Skill保护原意与模型选择区别；research核同任务/正反例；SOP返回主线；verification核真实源核与来源；canonical writer原子保存；dev-notes归档。无新治理平台。
'''
 audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: GIVEN_SOURCE_CASE_CHECKED_RETURN_GOLD\n- panorama_change: ADD_C295_C296_AND_SOURCE_ALIGNMENT\n- essay_change: NO\n- update_decision: source-supplied重呈现合同完成，原广义来源/物理操作不外推；进入实际GOLD。\n- cross_conflicts: 精确图Denotes比原允许形变更强；充分源数据不等于最小必要收费；只检查载体不够。\n- unresolved: 原广义来源/操作、原W Lift、其它机制/GOLD/四层整体。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、后继及反证条件 |\n|---|---|---|---|---|\n'
 headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
 for n,(kc,title) in enumerate(headings,1):
  rel,why=TOUCHED.get(n,('NOT_TOUCHED','本单元未推进该具名自指/反射/其它时间机制；来源对应不替代它。'))
  ev=('第十六轮001–004、C295/C296源码/run及六原文快照；后继实际GOLD。若换输入/Done、遗漏直接来源、误将精确图当全部历史或源核hash失败则撤回；新同输入反例/较弱充分数据可重评。' if n in TOUCHED else '第十六轮003未触达范围；该具名机制或新直接证据成为当前任务时重开。')
  audit+=f'| `{kc}` | {title} | {rel} | {why} | {ev} |\n'
 audit+='''
## 扩展认知逐片复认

001问题/简化：明确输入与被保持的整图，不用来源标签代替数据。002前提/时间：有限证书/精确重呈现与现实时间分开。003圆环/ASK：六原文的操作/Done范围逐项对照；旧022/023未证强判词保留。004HoTT/自反：实际UA支持保图，未做自反新主张。005表达/原文：原文快照逐字，source合同不伪称全部哲学理论。006知识谱：标准理论和AI解释分开，GOLD旧注释下一审查。007助力/阻力：不以正确运输消灭原问题，也不为预期结论改规格；达到范围即转GOLD。008现实骨架：用户允许变形是独立holdout，限制本Denotes不能涵盖全部现实身份。

## 已走过的路

六原文与两历史方案核对，实际给定源合同正Run与同输入错误输出过核。闭环的是源图重呈现的输入/输出资格；物理来源、所有允许操作或唯一生成方法未被自动证明。没有把先前AmbientStep的有限no-go当旧原句的全称证据。

## 即将作出的选择与完备性

选择GOLD实际L/U标准cut装配、命题性/层级和查询/近似，先核Cubical环境及旧注释；不将算术替换圆环，无保真归约则两实例分计。未选无界扩几何、全物理理论、再次重复裸/Rich分离。原广义任务及其它机制继续OPEN，触发靠新证据/原文/消费者。

八轴与SOP逐项见第十六轮003；六来源覆盖不等于全Session/全理论。Input的全称性由原生项承担，无有限枚举泛化。独立反控制是真实普通N，同任务保图正例非空；原允许变形暴露范围更广的未覆盖轴，已改变判词上限。新同输入方案或较弱数据成功可修正数据必要性判断。
'''
 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[RUN],'claim_ids':['C-295','C-296'],'validation':'audit/astra-case-contract-20260920/DELIVERY.json','source_alignment':'audit/astra-case-contract-20260920/SOURCE-INPUTS.json','extra_kernel_rerun':False,'parent_objective':'OPEN','app_goal_status_observed':'active'}
 for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-190'
 targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
 files=[]
 for rel in targets:
  raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
  if rel in (R.DIRECTION,R.PANORAMA):
   body,n=re.subn(r'(?m)^source_state_revision: 189$','source_state_revision: 190',body);assert n==1
   kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-190',body);assert n==1
  if rel=='MEMORY/001 - 当前执行队列.md':
   start=body.index('用户当前App Goal');end=body.index('\n\n',start)
   body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C295/C296已核给定源数据的Input/Denotes/Run/正确输出和同输入普通N反例；六原文与022/023逐项对照并保全快照。精确图重呈现不能冒充全部物理历史/允许形变，源数据只是本构造充分输入，不是普遍必要收费。策略v1.18由'+plan_commit+'保存。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
  if rel=='方向追踪/002 - 治理与用户方向.md':
   lines=body.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):
     lines[i]=line.replace('NATIVE_RICH_FINITE_TASK_CHECKED_CASE_CONTRACT_OPEN','SOURCE_CASE_CHECKED_GOLD_NEXT_ORIGINAL_SCOPE_OPEN').replace('`OUT-ASTRA-RICH-TASK-15` |','`OUT-ASTRA-RICH-TASK-15`、`OUT-ASTRA-CASE-CONTRACT-16` |').replace('原Input/Denotes/允许操作/Done对照，然后实际GOLD；弱Lift与完整原过程开放','给定源图合同已核；下一实际GOLD标准cut/查询/近似；原广义过程与弱Lift开放')
   body='\n'.join(lines)+'\n'
  if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-CASE-CONTRACT-16` | C295/C296给定源合同、原文对应与错误输出反例 | `DIR-U-ASTRA-BREAKPOINT` | 原生核、实际来源快照与源核关系 | `FORMAL_CHECKED_WITH_SCOPE / SOURCE_SUPPLIED_REPRESENTATION` | Input/Denotes/Run/正确输出；普通N同载体却不忠实；六原文范围辨明 | 全部来源/物理操作、弱Lift、其它机制/GOLD/整体 | `'+REPORT+'`；`audit/astra-case-contract-20260920/DELIVERY.json` |\n'
  files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
 for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['R-ASTRA-RICH-TASK-20260920'],'authorization':'用户ACTIVE Goal及既有T3状态/研究授权；完成给定源case合同并转实际GOLD，完整父范围不变。','files':files}
 (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
 (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
