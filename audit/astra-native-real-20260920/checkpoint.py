#!/usr/bin/env python3
"""One authorized canonical transaction for native real/configuration qualification."""
from pathlib import Path
import argparse,importlib.util,json,re
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-NATIVE-REAL';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第九轮执行报告.md'
NEXT='BP-GEO-NATIVE-PUNCTURE-APARTNESS-01：在已核实际Dedekind圆中固定逻辑删点¬(p=east)与正分离删点，核立体投影取逆需要的分母证据，构造可证明的映射及正控制；不要把经典Lean的反证法、强apartness输入或额外逻辑原则默默代入原任务。随后推进实际映射/连续性；完整GEO04、GOLD打包、其它断点机制、四层集成与学术交付仍未完成。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','共同圆环任务保持，环境诊断只作为真实模型的必要输入资格。'),
2:('CORRECTED','原without-K配置额外导入路径擦除规则；确切理论配置不能只写HoTT。'),
5:('DEEPENED','真实出现empty诊断后立即按原语/消融/原公理拆分归因。'),
7:('ALIGNED','实际源码与四类原始运行可查，不从AI或警告语气推断数学结论。'),
10:('ALIGNED','扩展实现配置中的empty不是用户现实相对目标完成。'),
12:('DEEPENED','模型后继检查逻辑删点是否提供取逆实际所需证据，不预先偷换输入。'),
13:('DEEPENED','正分离与否定不等的定义分开，保真义务先于强制接线。'),
14:('ALIGNED','圆/去点圆/区间的项并不提供实际运动或物理完成能力。'),
15:('TENSION','额外原语失配不能被提升为抽象必然错误；原Z方向保留待证。'),
17:('ALIGNED','不因库权威掩盖实际警告，也不因目标期待把配置矛盾改名为HoTT矛盾。'),
21:('DEEPENED','三个正包原命令复验与关系检查，负控制精确拒绝；原语源/二进制/库树固定。'),
22:('ALIGNED','A/B原目标保持，单个环境问题不替代共同任务的完成反差。'),
31:('DEEPENED','从抽象实数参数推进实际Dedekind点集与非空实例，严格字段仍保留。'),
34:('ALIGNED','no-section只作统一选择命题；不存在项的解释不扩大到所有选择行为。'),
35:('DEEPENED','实际实数圆和区间进入without-K模型，完整用户理论表达仍开放。'),
37:('TENSION','原圆环总体论证尚未闭合，不能以新环境发现宣布全部redo完成。'),
38:('DEEPENED','检查库真实原语及consumer，旧C05在消融后保留是必要反解释。'),
39:('DEEPENED','在基础等式归约处定位精确问题，但保留它是实现扩展这一事实。'),
40:('ALIGNED','版本化源码与官方文档对照知识先验；不以已知性否定本项目新证据缺口。'),
41:('ALIGNED','AI产生候选项并由实际核/控制检查，运行实物而非数量承担结论。'),
42:('CORRECTED','检查器接受不自动等于目标演算正确；显式条件进入索引和旧包资格。'),
43:('DEEPENED','消融闭合后回原生实数删点任务，不无限扩大为全库证明器审计。'),
44:('ALIGNED','具体实数坐标模型用于把握圆环，未以现实不可理解拒绝研究。'),
45:('DEEPENED','实际real/metric输入接口与Lean经典假设分别对齐，继续必要前提检查。'),
46:('ALIGNED','从实际几何构造与操作前提出发，后继是取逆资格而非纯名词控制。')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='THREE_PACKAGES_DUAL_LOCAL_PASS_WITH_CONFIGURATION_SCOPE'
 state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==182
 head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
 prior=json.loads((ROOT/'audit/astra-structured-consumer-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
 docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
 (OUT/'RESUME.json').write_bytes(R.dump({'policy':'PROTOCOL v3 same-T3 receipt reattestation, not fresh full emission','revision':182,'core_unchanged':True,'core_sha256':prior['core_sha256'],'documents':docs,'known_changes':'Own checkpoint182 and plan a1d935f; 32 HEAD tracked hashes match','kc_stance_revisited':'All46 individually reconsidered; original samples10/35/39/43–46 emitted again','app_goal_status_observed':'active','objective':'完成四弹一体的redo','model_understanding':'NOT_CERTIFIED_BY_TOOL'}))
 plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert plan['revision']==182
 (OUT/'PLAN-SNAPSHOT.json').write_bytes(R.dump(plan))
 old=state['latest_session'];state['revision']=183;state['latest_session']=SID
 state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'THREE_PACKAGES_DUAL_LOCAL_PASS_WITH_CONFIGURATION_SCOPE','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
 state['records']['R-ASTRA-NATIVE-REAL-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / ACTUAL_DEDEKIND_MODEL / EXTRA_REDUCTION_DIAGNOSTIC','status':'complete_with_scope','depends_on':[],'related_records':[SID,'R-ASTRA-STRUCTURED-CONSUMER-20260920'],'full_sources':[REPORT,'HoTT/formal/agda-unimath/hott-z/NativeRealCircleQualification.agda','HoTT/formal/agda-unimath/hott-z/ErasureConfigurationDiagnostic.agda','audit/astra-native-real-20260920/DELIVERY.json'],'scope':'C280 diagnostic concerns extra primEraseEquality reduction, not ordinary HoTT. C281 actual nonempty Dedekind pointsets. C282 requalifies unchanged C05 source after identity replacement. No full geometry translation or global soundness claim.'}
 state['records']['G-ASTRA-UNIMATH-CONFIG-20260920']={'kind':'issue','path':REPORT,'lifecycle_status':'HISTORICAL','evidence_status':'SELECTED_CONSUMERS_REQUALIFIED_WITH_SCOPE','status':'closed_with_scope','depends_on':[],'related_records':['R-ASTRA-NATIVE-REAL-20260920'],'full_sources':[REPORT,'audit/astra-native-real-20260920/DERIVATION.json','audit/astra-native-real-20260920/IMPORT-AUDIT.json'],'closure_reason':'Original tree preserved, extra reduction isolated; selected old source and actual model pass restricted configuration. No claim that all historical consumers or all library axioms were audited.','reopen_if':'New actual consumer needs the erasing reduction, relevant source changes, or new evidence invalidates restricted qualification.'}
 state['records']['A-ASTRA-CONTINUING-GOAL-20260919']['scope']='Current App objective 完成四弹一体的redo; retain complete accepted breakpoint/four-stage/ZCode-absorption/governance scope in strategy010. Partial model qualification is not parent completion.'
 state['execution_control'].update(status='ACTIVE_GOAL_NATIVE_REAL_MODEL_QUALIFIED_WITH_SCOPE',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
 session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-native-real-20260920/RESUME.json
- app_goal_status_observed: active
- objective: 完成四弹一体的redo
- status: THREE_PACKAGES_DUAL_LOCAL_PASS_WITH_CONFIGURATION_SCOPE / PARENT_OBJECTIVE_OPEN

本轮在原生实际实数资格化过程中发现上游primEraseEquality与without-K配置风险。额外原语与univalence使显式empty诊断过核；普通恒等函数替代后的同源码在loopRefl精确拒绝。官方Agda文档已说明该兼容性问题，不称新发现HoTT矛盾。原库不改、隔离副本两文件差分，实际Dedekind实数圆/去点圆/区间和旧NoCanonicalPoint同源码均经正式忽略interfaces运行与原命令复验。库仍有univalence/funext/HIT/truncation/replacement等公设；895模块图是导入上界而非最小公理集合。

C280/C281及C282重资格化均有run/source/index；C282不是新发现定理。最初复用C05导致registry重复claim失败，-01和失败输出保留，以新身份C282/new run-02修复；不改公共validator。负控制不按正包索引。原始草稿两次非数学失败保留。

策略v1.11已由a1d935f提交。{NEXT}

PROTOCOL§5全46KC legacy bundle兼容路径；G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持，未伪称原子分片审计。无Sub Agent、无push/tag/发布。T01–05完整用户范围保留；T06–10模型/配置边界明确；T11–17证明输入及验证新增；T18–21无部署变化；T22–24旧资格与当前动作更新；T25无Host/模型合同变更；T26精确版本化。C01–C09未修改共享治理方法；C10保存项目证据与已知边界。

element_usage：closure/runtime用于恢复和事务；研究Skill用于原生构造与反解释；verification用于同源码消融与重放；归档用于完整答复；图/语法扫描仅作证据导航；未启动外部AI或新平台。
'''
 audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: NATIVE_PUNCTURE_APARTNESS_NEXT\n- panorama_change: ADD_NATIVE_MODEL_AND_CONFIGURATION_QUALIFICATION\n- essay_change: NO\n- update_decision: 在真实实数模型继续同任务前提检查。\n- cross_conflicts: 不一致扩展配置不冒充普通HoTT；高宇宙实数不冒充SingleOmega；逻辑删点不冒充正分离。\n- unresolved: 完整几何翻译、实际过程、原约束、GOLD打包、其它机制和四层集成。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一动作及反证条件 |\n|---|---|---|---|---|\n'
 headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
 for n,(kc,title) in enumerate(headings,1):
  rel,why=TOUCHED.get(n,('NOT_TOUCHED','本轮未检查该具名时序/自指/运动/全局反射命题；配置诊断不替代。'))
  ev=('第九轮001–004及C280–282源码/run、同源码负控制；若原语差异不再解释拒绝、模型hash/核检查失败或原任务条件被替换则撤回；下一项检验实际删点/取逆前提。' if n in TOUCHED else '第九轮003未触达范围；该具名构造/现实任务或新直接证据进入时重新激活。')
  audit+=f'| `{kc}` | {title} | {rel} | {why} | {ev} |\n'
 audit+='''
## 扩展认知逐片复认

001问题/简化：实际模型入口替代抽象参数；未缩用户目标。002时间/前提：没有新物理连续性结果。003圆环/ASK：删点与分母条件明确，下一实际构造保持任务。004HoTT/自反：额外归约与标准规则分开，自反未触达。005表达/原文：原实数点集非空不等于完整论证。006知识谱：上游公开原语与官方说明真实对照，既不迷信也不夸大新颖性。007助力/阻力：原PASS资格复核与旧定理正控制同时保留。008现实骨架：实坐标/度量使具体圆可把握，下一步沿操作输入检查。

## 已走过的路

从真实Dedekind模型加载触发配置警告，给出最小诊断并同源码消融；回放旧定理且实际构造非空圆/区间。保存失败、原树和输入身份。没有将empty诊断计为HoTT击落，没有将原语替换包装成整个库的一致性证明。

## 即将作出的选择与完备性

选择逻辑删点与apartness/取逆资格；未选择全库重审或重新堆叠有限整数端点例子。八轴、反解释、独立版本化来源与停止条件见第九轮003。895模块是导入分母，不是候选搜索分母；没有无限公平搜索或全理论否定。新自然消费者/源变动可重开配置事件。当前实数模型与GOLD属于不同Agda演算和rational实现，需真实保真接口。
'''
 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':['HoTT/verification/runs/20260920-MP-ASTRA-ERASURE-CONFIG-001-01','HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-REAL-001-01','HoTT/verification/runs/20260920-MP-ASTRA-NOSECTION-RESTRICTED-001-02'],'negative_control':'HoTT/verification/runs/20260920-MP-ASTRA-ERASURE-CONTROL-001-01','superseded_index_attempt':'HoTT/verification/runs/20260920-MP-ASTRA-NOSECTION-RESTRICTED-001-01','validation':'audit/astra-native-real-20260920/DELIVERY.json','claim_ids':['C-280','C-281','C-282'],'parent_objective':'OPEN','app_goal_status_observed':'active'}
 for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-183'
 files=[]
 for rel in list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT)):
  raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
  if rel in (R.DIRECTION,R.PANORAMA):
   body,n=re.subn(r'(?m)^source_state_revision: 182$','source_state_revision: 183',body);assert n==1
   kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-183',body);assert n==1
  if rel=='MEMORY/001 - 当前执行队列.md':
   start=body.index('用户本线程持续Goal');end=body.index('\n\n',start)
   body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”；完整原范围保留。C280定位额外primEraseEquality归约配置：原配置接受empty，普通恒等替换的同源码精确拒绝；不是普通HoTT矛盾。隔离no-erasure变体中C281实际Dedekind圆/去点圆/区间非空模型与C282旧C05同源码复核均通过，三包复验/关系检查及控制留证；不认证整库一致性。策略v1.11由a1d935f保存。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
  if rel=='方向追踪/002 - 治理与用户方向.md':
   lines=body.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]='| `DIR-U-ASTRA-BREAKPOINT` | 完成断点检查并按原意重执行四层论证 | 用户ACTIVE Goal：完成四弹一体的redo | `OPEN_OBJECTIVE / NATIVE_REAL_MODEL_QUALIFIED_WITH_SCOPE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-BREAKPOINT-01`、`OUT-ASTRA-RESTORATION-02`、`OUT-ASTRA-PROOF-WIRING-03`、`OUT-ASTRA-REAL-CIRCLE-04`、`OUT-ASTRA-AMBIENT-CIRCLE-05`、`OUT-ASTRA-CURVE-DEFORMATION-06`、`OUT-ASTRA-ENDPOINT-CLOSURE-07`、`OUT-ASTRA-STRUCTURED-CONSUMER-08`、`OUT-ASTRA-NATIVE-REAL-09` | 逻辑删点/正分离/取逆前提；完整几何及原任务尚开放 | `Astra继续尝试/四弹一体完整研究策略/010 - 断点检查接入与总目标执行账本.md` |'
   body='\n'.join(lines)+'\n'
  if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-NATIVE-REAL-09` | C280配置诊断、C281实际Dedekind模型、C282旧证明重资格化 | `DIR-U-ASTRA-BREAKPOINT` | 三包实际Agda/复验/关系检查与同源码负控制 | `FORMAL_CHECKED_WITH_SCOPE / EXTRA_REDUCTION_ISOLATED` | 原语额外归约不是标准HoTT；模型非空、旧定理消融后仍检查通过 | 全库一致性、原生同胚/F/Lean翻译、原任务及四层整体 | `'+REPORT+'`；`audit/astra-native-real-20260920/DELIVERY.json` |\n'
  files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
 for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户ACTIVE Goal完成四弹一体的redo；既有研究与当前状态维护授权；只推进本单元实际资格，不缩父范围。','files':files}
 (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
 (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
