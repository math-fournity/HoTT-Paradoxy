#!/usr/bin/env python3
"""Register the actual ambient-operation result through the canonical transaction."""
import argparse,hashlib,importlib.util,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-AMBIENT-CIRCLE'
BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第五轮执行报告.md'
RUN='HoTT/verification/runs/20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02'
NEXT='BP-GEO-DEFORMATION-01：固定N与M的初末参数化、F:[0,1]×(0,1)→Plane连续、逐时嵌入与精确末时刻Done，检验较弱曲线弯曲正构造；不要求切片自动扩张为整平面同胚。若成功，限定不可恢复结论只在原操作类；具体公式失败不等于全类不可能。随后GEO-04原生HoTT/Forget保真、真实GOLD连接及U00–U09/G01–G06继续；完整Goal ACTIVE。'
spec=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py')
R=importlib.util.module_from_spec(spec);spec.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','同一实数平面、同一M/N、同一闭包余集观察与明确操作类先行。'),
2:('DEEPENED','区分内在同胚、整平面同胚和逐时嵌入；经典Lean不冒充HoTT规则。'),
5:('ALIGNED','实际正反命题均保留；先验主张不决定证明结果。'),
6:('ALIGNED','有限操作列表不冒充实际时间连续性；后继另给连续时间参数。'),
7:('ALIGNED','内核失败及修复源码均留存，未用AI自述替代验证。'),
10:('ALIGNED','局部环境否定支持研究现实任务差异，不报内部矛盾或理论非现实性已证。'),
12:('DEEPENED','ASK先固定允许操作，不能从不准改变环境的任务偷换到任意曲线变形。'),
13:('ALIGNED','操作输入和终态相等明确，静态同胚没有被当作任何过程自动完成。'),
14:('ALIGNED','C268全称只覆盖有限环境操作类，未获得一切过程的完成判定。'),
15:('TENSION','差异可被经典拓扑明确表达；尚无证据表明此抽象必然误用或理论自毁。'),
17:('ALIGNED','给最强较弱正构造后继，避免因目标预设而偏爱否定结果。'),
21:('DEEPENED','C266–268实际源码、两次正式捕获、当前重放与双校验齐备。'),
22:('ALIGNED','A/B双向研究保留；当前只是限制操作类的不可达定理。'),
31:('DEEPENED','具体非有限实数空间中的环境保持量代替纯参数形态。'),
34:('ALIGNED','数学全称否定、草稿检查失败、未检查的较弱变形严格分开。'),
35:('DEEPENED','用户环境关联差异形成具体模型；到HoTT的完整忠实表达仍未完成。'),
37:('TENSION','原问题有所推进，但未得HoTT缺陷，不能把局部否定改名父目标成功。'),
38:('TENSION','标准拓扑同样区分这些结构，本轮不能证明理论作者忽视了它。'),
39:('DEEPENED','从真实圆、区间、闭包和允许变换这些基础处作判别。'),
41:('ALIGNED','用内核验证及语义审查支持数学工作，而非只增加文件。'),
42:('ALIGNED','公理与编译依赖可信边界保留，工具PASS不替代任务对应。'),
43:('DEEPENED','不重复恒等控制；下一步挑战环境限制的必要性。'),
44:('ALIGNED','同一平面模型是可研究的假想现实，不拒绝现实诠释。'),
45:('DEEPENED','辨明被忘记的是嵌入环境，检验其是否真为原操作必要条件。'),
46:('ALIGNED','实际实现环境与端部关系，并继续研究允许弯曲而非停在口头解释。')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 assert json.loads((OUT/'DELIVERY.json').read_text())['status']=='DUAL_LOCAL_PASS'
 state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==178
 head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text())
 assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
 prior=json.loads((ROOT/'audit/astra-real-geometry-20260919/RESUME-20260920.json').read_text())
 docs=[{'path':x['path'],'prior_sha256':x['current'],'sha256':R.sha((ROOT/x['path']).read_bytes())} for x in prior['documents']]
 assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
 resume={'policy':'PROTOCOL v3 same T3 receipt reattestation; not new full body emission','revision':178,
  'git_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
  'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,
  'known_changes':'Own canonical checkpoint178 and plan c6f406c; 32 HEAD tracked hashes match; unrelated dirty files preserved.',
  'kc_stance_revisited':'All46 rows of S-RES-20260920-ASTRA-REAL-CIRCLE audit reread; new work-specific rows below.',
  'source_samples':['KC-000010','KC-000035','KC-000039','KC-000043','KC-000044','KC-000045','KC-000046'],
  'model_understanding':'NOT_CERTIFIED_BY_TOOL'}
 (OUT/'RESUME.json').write_bytes(R.dump(resume))
 plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert plan['revision']==178
 (OUT/'PLAN-SNAPSHOT.json').write_bytes(R.dump(plan))
 old=state['latest_session'];state['revision']=179;state['latest_session']=SID
 state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL',
  'evidence_status':'C266_C268_LOCAL_FORMAL_AND_RELATION_CHECKS_PASS','status':'complete_with_scope',
  'depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],
  'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
 state['records']['R-ASTRA-AMBIENT-CIRCLE-20260920']={'kind':'result','path':REPORT,
  'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY',
  'status':'complete_with_scope','depends_on':[],'related_records':[SID,'R-ASTRA-REAL-CIRCLE-20260920'],
  'full_sources':[REPORT,'HoTT/formal/astra-real-geometry/AmbientCircle.lean',
   'HoTT/formal/astra-real-geometry/AMBIENT-TOOLCHAIN.json','audit/astra-ambient-geometry-20260920/DELIVERY.json'],
  'scope':'C266–268: intrinsic homeomorphism with distinct closure remainders; no global plane homeomorphism or finite list thereof. Weaker curve deformation, original physical operation class and native HoTT translation open.'}
 state['execution_control'].update(status='ASTRA_AMBIENT_OPERATION_CLASS_CHECKED',last_checkpoint_session=SID,
  checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
 session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端实际路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_GOAL
- load_receipt: audit/astra-ambient-geometry-20260920/RESUME.json；PROTOCOL v3同档复认；32HEAD hash一致、46KC回读、7段原文抽查
- status: C266_C268_FORMAL_CHECKED_WITH_SCOPE / FULL_GOAL_ACTIVE

对象为同一实际实数平面的去点单位圆M与直开线段N。闭包余集分别为单点与两个不同点；仍内在同胚，但不存在整平面同胚扩张或有限串该类操作实现N→M。经典Lean模型不冒充native HoTT；范围不包含一切连续曲线变形。公理仅propext/Classical.choice/Quot.sound，run-02 exit0，双检查PASS。

五个草稿与失败run-01全部保留；原失败源码、runner、toolchain副本逐一匹配旧manifest。-t0仅按实际命令记录，不宣称独立fresh导入重检。相关可信边界在第五轮报告002；未改变公共validator/Skill/Host。具体语义由报告001及claim C266–268拥有。

反思已写报告003八项，计划v1.6提交c6f406c。后继：{NEXT}

未缩减Goal、未重开旧事故、未消费Sub Agent、未push/tag/公开。按PROTOCOL§5使用全46KC legacy单文件兼容bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；未声称分片已原子化。

element_usage：closure恢复scope/owner；研究Skill区分几何/HoTT/现实；SOP要求反思和计划先提交；F011检查精确源码运行索引；checkpoint保存当前范围和后继。T01–05要求不变、T06–10只实例化已计划操作模型、T11–17新增证明和证据、T18–21部署/外部系统不变、T22–24更新状态与失败历史、T25模型/权限不变、T26精确提交。共享治理C01–C09无规则变动，C10项目历史新增，不发布治理版本。
'''
 headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
 audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: WEAKER_CURVE_DEFORMATION_NEXT\n- panorama_change: ADD_C266_C268_AMBIENT\n- essay_change: NO\n- update_decision: 记录具体环境操作类，继续原任务较弱变形。\n- cross_conflicts: 内在同胚与环境同胚否定不是同一命题；不能越类。\n- unresolved: 较弱变形/现实操作/HoTT保真/四层组合。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一动作及反证条件 |\n|---|---|---|---|---|\n'
 for n,(kc,title) in enumerate(headings,1):
  rel,why=TOUCHED.get(n,('NOT_TOUCHED','本轮未研究该具体时间、自指、不可判定性或元理论命题，环境操作定理不作替代。'))
  ev=('C266–268源码/run-02与第五轮001/003；若模型不忠于原操作则撤回对应解释，若hash/核验失败则撤回资格；较弱正构造成功只收窄外推，不否定环境定理。' if n in TOUCHED else '第五轮003未触达范围；出现该主题具名任务或新直接反证再进入。')
  audit+=f'| `{kc}` | {title} | {rel} | {why} | {ev} |\n'
 audit+='''
## 扩展认知逐片复认

001问题/简化：区分内在与环境观察，模型保留来源任务。002前提/时间：环境同胚假设明确；列表顺序未等于连续时间。003圆环/ASK/A-B：闭包关联已有实物；原操作覆盖仍开放。004HoTT/自反：经典Lean辅助，不提升HoTT；自反未触达。005表达/原文/起点：不把新模型改写成用户已经指定的全部现实操作。006知识谱：由实际库closure/image定理和内核获得证据；未作全谱穷尽。007助力/阻力：下一步挑战刚取得否定结果的外推，不固定在熟悉控制。008现实骨架：实际平面操作可作假想现实模型，但较弱弯曲是否保持原任务必须另检。

## 已走过的路

C265只得到内在同胚，本轮加入同一平面和闭包余集，得到有限环境操作不可达。核心未知确实减少，但没有HoTT缺陷。失败未删、公理未藏、工具信任未升级，历史ZCode审查已吸收而不反复重做。

## 即将作出的选择与完备性

后继BP-GEO-DEFORMATION-01固定连续F、逐时嵌入、末时刻精确像及Done，考察较弱曲线弯曲正构造；必要时承认原广泛不可恢复表述不成立。八轴和独立taxonomy详第五轮003。有限列表归纳给该类全称，非枚举/无限搜索完备；未触及所有物理操作、全库使用者、HoTT桥或元理论。core46保持，完整Goal继续，三个尚未闭合层及集成不会因局部负定理被消除。
'''
 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_run':RUN,
  'failed_run':'HoTT/verification/runs/20260920-MP-ASTRA-AMBIENT-CIRCLE-001-01',
  'validation':'audit/astra-ambient-geometry-20260920/DELIVERY.json','claim_ids':['C-266','C-267','C-268'],'parent_goal':'ACTIVE_NOT_COMPLETE'}
 for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-179'
 files=[]
 for rel in list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT)):
  b=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else b.decode()
  if rel in (R.DIRECTION,R.PANORAMA):
   body,n=re.subn(r'(?m)^source_state_revision: 178$','source_state_revision: 179',body);assert n==1
   kind='direction' if rel==R.DIRECTION else 'outcome'
   body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-179',body);assert n==1
  if rel=='MEMORY/001 - 当前执行队列.md':
   start=body.index('用户本线程持续Goal');end=body.index('\n\n',start)
   body=body[:start]+'用户本线程持续Goal ACTIVE；ZCode 7cb审查/计划吸收已完成。第四轮C265为实际实数内在同胚；第五轮C266–268在同一平面中证明闭包余集单点/两个不同点、环境同胚及其有限列表不能实现N→M，Lean实际run-02与双检查PASS。该操作类不等于所有曲线变形；策略v1.6已提交c6f406c。下一最小动作BP-GEO-DEFORMATION-01：连续F、逐时嵌入、精确末时刻Done的较弱正构造。原生HoTT/Forget保真、真实GOLD连接、完整U00–U09/G01–G06仍开放。入口：`'+REPORT+'`。旧SUPPLY/Gödel与全历史修复不自动替代当前动作。'+body[end:]
  if rel=='方向追踪/002 - 治理与用户方向.md':
   lines=body.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]='| `DIR-U-ASTRA-BREAKPOINT` | 完成断点检查并持续推进完整四弹策略 | 用户线程Goal | `ACTIVE_GOAL / AMBIENT_OPERATION_CLASS_CHECKED` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-BREAKPOINT-01`、`OUT-ASTRA-RESTORATION-02`、`OUT-ASTRA-PROOF-WIRING-03`、`OUT-ASTRA-REAL-CIRCLE-04`、`OUT-ASTRA-AMBIENT-CIRCLE-05` | 较弱曲线变形、逐时嵌入与精确Done；环境否定不外推 | `Astra继续尝试/四弹一体完整研究策略/010 - 断点检查接入与总目标执行账本.md` |'
   body='\n'.join(lines)+'\n'
  if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-AMBIENT-CIRCLE-05` | C266–268实际平面内在同胚及有限环境操作不可达 | `DIR-U-ASTRA-BREAKPOINT` | Lean4.34.0/mathlib固定输入、run-02与双校验 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN` | 真实闭包余集、环境保持量与全有限列表归纳 | 较弱曲线变形、全部物理操作、HoTT保真/缺陷 | `'+REPORT+'`；`audit/astra-ambient-geometry-20260920/DELIVERY.json` |\n'
  files.append({'path':rel,'expected_sha256':R.sha(b),'text':body})
 for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research',
  'task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],
  'authorization':'用户持续Goal授权完成实际圆环研究和治理；本次登记已核环境操作类，并检验原任务较弱过程；不宣称父目标完成。','files':files}
 (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload))
 result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
 (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result))
 print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
