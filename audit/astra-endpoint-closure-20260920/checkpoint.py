#!/usr/bin/env python3
"""Persist the exact endpoint-extension result using the canonical transaction."""
import argparse,importlib.util,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-ENDPOINT-CLOSURE';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第七轮执行报告.md'
RUN='HoTT/verification/runs/20260920-MP-ASTRA-ENDPOINT-CLOSURE-001-01'
NEXT='BP-GEO-STRUCTURED-CONSUMER-01：使用实际初末边界图建立同一任务Rich/Bare/Forget和消费者，先在Lean几何中检查内在对应的保边界结构提升及重参数化并运输全部结构的正控制；随后复用原生Cubical BoundaryIncidence，对所需有限边界观察给出明确对应/保持证据，不把有限观察冒充整个实数拓扑翻译。保留用户固定端部要求；native HoTT完整保真、真实GOLD、U00–U09/G01–G06仍开放，Goal ACTIVE。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','同一F、相同内点和明确闭方形先固定，精确量词与全部纤维核验。'),
2:('DEEPENED','区分参数标签、环境像、开域嵌入和闭域末态非单射。'),
5:('ALIGNED','先核具体端点行为再归因，不以作者或理论名称决定结论。'),
6:('DEEPENED','闭时间距离连续、末时刻取零已核；无速度/物理完成外推。'),
7:('ALIGNED','六草稿保留，显式子类型修复由核确认，不用自述或图形代替。'),
10:('ALIGNED','不存在本实例所述零距离异像；仍不把该模型当理论普遍现实性认证。'),
12:('DEEPENED','固定端部是需明确保留的额外输入合同，不能被允许端部移动替换。'),
13:('DEEPENED','延拓公式与原F在全部内点一致，避免换模型补端点。'),
14:('ALIGNED','数学闭参数过程的精确完成不自动提供材料/速度能力。'),
15:('TENSION','端点疑问在此连续模型中可一致表达；尚不支持抽象必然逻辑失效。'),
17:('ALIGNED','接受只有边界参数被合并的结果，同时保留原固定边界语境。'),
21:('DEEPENED','C271–274实际核验及双检查；三原Agda包重放与同Pell的Lean合取对照均通过。'),
22:('ALIGNED','A/B研究方向保留；本轮只刻画一个具体过程，不声称全部现实任务解决。'),
31:('DEEPENED','实际几何边界图已就绪，为下一结构消费者提供真实输入。'),
34:('ALIGNED','精确正构造、末态非单射、全部纤维和未知HoTT桥分开。'),
35:('DEEPENED','用户端部与缺点关联被具体实现；原生HoTT全表达仍待对应证明。'),
37:('TENSION','没有得到HoTT缺陷，当前端点模型也未产生预期矛盾。'),
38:('TENSION','不能从用户关注的差异推出理论作者未知或错误；仍需具体使用者证据。'),
39:('DEEPENED','基础处检查零距离/同一点/不同参数，且量化全部内点而非图形猜测。'),
41:('ALIGNED','机器检查帮助精确解释端点，但未将工具成功当研究总目标达成。'),
42:('ALIGNED','经典公理、编译依赖和对应范围透明，保持独立语义审查。'),
43:('DEEPENED','结束局部公式深化，返回实际Rich/Bare消费者及HoTT表达。'),
44:('ALIGNED','用闭参数轨迹把握假想现实，不把缺点无大小当无法建模的理由。'),
45:('DEEPENED','明确当前被保留/忘记的是边界图，随后检验原任务必要性与运输。'),
46:('ALIGNED','实际检查端点关系，下一步由同一模型提供输入，避免另造不相关例子。')}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
 assert json.loads((OUT/'DELIVERY.json').read_text())['status']=='DUAL_LOCAL_PASS'
 assert json.loads((OUT/'lean-comparison/DELIVERY.json').read_text())['status']=='DUAL_LOCAL_PASS'
 assert all(x['exit']==0 for x in json.loads((OUT/'agda-comparison/REPLAY.json').read_text())['results'])
 state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==180
 head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text())
 assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
 prior=json.loads((ROOT/'audit/astra-curve-deformation-20260920/RESUME.json').read_text())
 assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
 docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
 (OUT/'RESUME.json').write_bytes(R.dump({'policy':'Same-context same-T3 continuation; PROTOCOL v3 receipt reattestation, not new full emission','revision':180,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint180/plan v1.8 and breakpoint v1.4; all32 HEAD hashes match; unrelated dirty assets preserved','kc_stance_revisited':'All46 previous rows retained and individually reconsidered below; original samples10/35/39/43–46 retained','model_understanding':'NOT_CERTIFIED_BY_TOOL'}))
 plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert plan['revision']==180
 (OUT/'PLAN-SNAPSHOT.json').write_bytes(R.dump(plan))
 old=state['latest_session'];state['revision']=181;state['latest_session']=SID
 state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C271_C274_LOCAL_DUAL_PASS_AND_AGDA_REPLAY','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+'SESSION.md',BASE+'RUNS.json',BASE+'CORE_COGNITION_AUDIT.md']}
 state['records']['R-ASTRA-ENDPOINT-CLOSURE-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY','status':'complete_with_scope','depends_on':[],'related_records':[SID,'R-ASTRA-CURVE-DEFORMATION-20260920'],'full_sources':[REPORT,'HoTT/formal/astra-real-geometry/EndpointClosure.lean','HoTT/formal/astra-real-geometry/ENDPOINT-TOOLCHAIN.json','audit/astra-endpoint-closure-20260920/DELIVERY.json'],'scope':'C271–273 same-F joint closed-parameter extension and interior agreement; continuous endpoint gap positive before t1 and zero at t1; final full-circle image, exact fibers only identify the endpoint pair. No fixed-boundary recovery or native HoTT translation claim.'}
 state['records']['R-ASTRA-AGDA-LEAN-COMPARISON-20260920']={'kind':'result','path':'Astra继续尝试/断点与证明机制系统检查/第七轮执行报告/004 - Agda与Lean的命题对照.md','lifecycle_status':'CURRENT','evidence_status':'C274_FORMAL_CHECKED_WITH_SCOPE_AND_THREE_AGDA_REPLAYS','status':'complete_with_scope','depends_on':[],'related_records':[SID],'full_sources':['HoTT/formal/astra-real-geometry/PellCurveComparison.lean','audit/astra-endpoint-closure-20260920/lean-comparison/DELIVERY.json','audit/astra-endpoint-closure-20260920/agda-comparison/REPLAY.json'],'scope':'Original Agda M1/M3-UNC/EndpointMaps replays pass; same Pell initial values/recurrence in Lean retain D≠0 and are accepted jointly with curve existence. No general cross-kernel translation or complete original-task restoration claim.'}
 state['execution_control'].update(status='ASTRA_ENDPOINT_EXTENSION_CHECKED',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
 session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_GOAL
- load_receipt: audit/astra-endpoint-closure-20260920/RESUME.json；同上下文同档、core未变、32HEAD hash一致、46KC逐项回评
- status: C271_C274_FORMAL_CHECKED_WITH_SCOPE / FULL_GOAL_ACTIVE

上一轮PROGRESS：C269/C270、实际图示、revision180及版本检查已提交。当前构造同一F的闭参数延拓，核验联合连续、所有内点相同、端点距离初值1/末值0/之前严格正，以及全部末态纤维恰为同一参数或0/1对。不是两个不同平面点距离为零，且开放曲线内点不含pole。此任务没有固定边界条件，不能替代用户固定端部的完整任务。

Lean4.34.0/mathlib固定输入，run-01 exit0，十项公理检查仅标准三公理，双检查PASS。六草稿及其错误保留；父源码不改，无额外公设/内核改动。编译依赖及本机路径可信边界保持，不宣称独立fresh导入重检。报告001/002拥有精确命题与证据。

用户中途质疑“Lean通过与Agda不给通过是否冲突”，已作为当前任务澄清处理：原Agda M1/M3-UNC/EndpointMaps实际重放3/3精确匹配；M1的D为整数Pell判别式而非当前端点距离，M3为平方比较表/有理根规格的非等价。新增C274在Lean复核相同初值/递推的D≠0，并与C269几何存在合取过核。报告004保存原问题及源码/运行对照，补足允许端部移动不等于固定边界任务的范围；没有宣称完整F已经在Agda中重放。该澄清完成后原后继不变，无需另改方案。

反思见第七轮003；完整策略v1.8与断点方案v1.4已在8c2337b提交，修正旧“未执行/接线阻塞”当前文字而保留历史报告。下一动作：{NEXT}

未启动Sub Agent、未push/tag/公开。PROTOCOL§5的完整46KC legacy单文件兼容路径继续使用，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001不伪造关闭。原Goal和ZCode追加要求保持，后者审查已完成。

element_usage：closure恢复当前父任务；研究Skill区分参数/像/物理与HoTT；SOP要求反思和先提交方案；F011实际源码/运行/索引；checkpoint保存后继。T01–05要求不变；T06–10具体端部合同实例化；T11–17证明/运行/失败新增；T18–21部署不变；T22–24状态和历史入口维护；T25Host/模型/权限不变；T26精确提交。C01–C09无共享治理规则变更，C10新增项目历史，无治理发布。
'''
 audit=f'# {SID} 核心认知回评\n\ncore-cognition-generation-7；46条。\n\n- core_change: NO\n- direction_change: ACTUAL_STRUCTURED_CONSUMER_NEXT\n- panorama_change: ADD_C271_C273_ENDPOINTS\n- essay_change: NO\n- update_decision: 接入精确端点纤维并返回原生结构消费者。\n- cross_conflicts: 参数标签不等于环境像，较弱变形不等于固定边界恢复。\n- unresolved: Rich/Bare/Forget、实际HoTT使用、原任务附加条件及四层组合。\n\n| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一动作及反证条件 |\n|---|---|---|---|---|\n'
 headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
 for n,(kc,title) in enumerate(headings,1):
  relation,why=TOUCHED.get(n,('NOT_TOUCHED','本轮未检查该具体逻辑、自指、停机、其它悖论或元理论命题；端点模型不作替代。'))
  evidence=('C271–273源码/run-01及第七轮001/003；若内点一致或类型/hash失败撤回资格；若原任务要求固定端点则另检该合同，不以移动端点恢复越级；未得HoTT缺陷。' if n in TOUCHED else '第七轮003未触达范围；待该主题具名任务或新直接证据出现再进入。')
  audit+=f'| `{kc}` | {title} | {relation} | {why} | {evidence} |\n'
 audit+='''
## 扩展认知逐片复认

001问题/简化：同一F与原M/N保持，区分参数标签/环境像。002前提/时间：闭时间连续距离末值已核，速度与物理未核。003圆环/ASK/A-B：端部关联有实际模型，固定边界作为原条件保留；未证所有任务可完成。004HoTT/自反：Lean几何不替native HoTT；下一步具体消费者，自反未触及。005表达/原文/文章：修订AI当前解释与旧执行状态，不改用户原文或旧收据。006知识谱：实际连续与纤维证明提供证据，不按训练权威判定新颖性。007助力/阻力：结束同一公式的局部深化，转实际结构观察。008现实骨架：边界/环境作为可把握的现实模型，原任务所需约束必须逐项对齐。

## 已走过的路

从内在同胚、环境否定、连续曲线正构造推进到同一F的闭参数全部纤维。核心未知减少，但无HoTT缺陷；六次草稿错误保留，所有主结论有正式run及重放。当前方案中的历史未执行/旧接线失败表述已原位修正。

## 即将作出的选择与完备性

以实际初末边界图进入Rich/Bare/Forget消费者和全结构运输正控制，再核有限边界观察的原生Cubical对应；不得把小观察翻译当完整实数HoTT桥。八轴详第七轮003。全称证明量化任意闭参数及时间，非枚举与开放世界穷尽；独立对照为环境否定/内点嵌入，范围外为固定边界、物理限制与真实库消费者。完整Goal剩余义务保留。
'''
 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_run':RUN,'comparison_run':'HoTT/verification/runs/20260920-MP-ASTRA-PELL-CURVE-COMPARISON-001-01','agda_replays':'audit/astra-endpoint-closure-20260920/agda-comparison/REPLAY.json','drafts':'audit/astra-endpoint-closure-20260920/attempts/001..006','validation':'audit/astra-endpoint-closure-20260920/DELIVERY.json','comparison_validation':'audit/astra-endpoint-closure-20260920/lean-comparison/DELIVERY.json','claim_ids':['C-271','C-272','C-273','C-274'],'parent_goal':'ACTIVE_NOT_COMPLETE'}
 for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-181'
 files=[]
 for rel in list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT)):
  b=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else b.decode()
  if rel in (R.DIRECTION,R.PANORAMA):
   body,n=re.subn(r'(?m)^source_state_revision: 180$','source_state_revision: 181',body);assert n==1
   kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-181',body);assert n==1
  if rel=='MEMORY/001 - 当前执行队列.md':
   start=body.index('用户本线程持续Goal');end=body.index('\n\n',start)
   body=body[:start]+'用户本线程持续Goal ACTIVE；ZCode 7cb吸收已完成。C265–270的实际几何链已核；第七轮C271–273又给同一F闭参数联合连续延拓、内点一致、端点距离初1/末0/此前正及精确末态纤维仅合并0/1。run-01与双检查PASS。完整策略v1.8/断点方案v1.4在8c2337b提交；较弱过程不替代固定边界要求。下一动作BP-GEO-STRUCTURED-CONSUMER-01：实际初末边界图的Rich/Bare/Forget、结构提升/正运输，再核原生Cubical有限观察对应。完整实数HoTT桥、GOLD和U00–U09/G01–G06仍开放。入口：`'+REPORT+'`。旧SUPPLY/Gödel和全历史修复不替代当前动作。'+body[end:]
  if rel=='方向追踪/002 - 治理与用户方向.md':
   lines=body.splitlines()
   for i,line in enumerate(lines):
    if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]='| `DIR-U-ASTRA-BREAKPOINT` | 完成断点检查并持续推进完整四弹策略 | 用户线程Goal | `ACTIVE_GOAL / ENDPOINT_EXTENSION_CHECKED` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `OUT-ASTRA-BREAKPOINT-01`、`OUT-ASTRA-RESTORATION-02`、`OUT-ASTRA-PROOF-WIRING-03`、`OUT-ASTRA-REAL-CIRCLE-04`、`OUT-ASTRA-AMBIENT-CIRCLE-05`、`OUT-ASTRA-CURVE-DEFORMATION-06`、`OUT-ASTRA-ENDPOINT-CLOSURE-07` | 实际结构消费者、全结构运输与原生有限观察；固定端部合同保留 | `Astra继续尝试/四弹一体完整研究策略/010 - 断点检查接入与总目标执行账本.md` |'
   body='\n'.join(lines)+'\n'
  if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-ENDPOINT-CLOSURE-07` | C271–273闭参数端点与纤维，C274同Pell的Lean对照 | `DIR-U-ASTRA-BREAKPOINT` | 两新Lean包双检查、原Agda三包精确重放 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_AND_AGDA_REPLAY` | 内点一致/唯一边界对重合；旧Pell负定理与新曲线存在同获Lean接受 | 固定边界任务/物理条件/完整F的Agda重放/一般跨内核保真或HoTT缺陷 | `'+REPORT+'`；`audit/astra-endpoint-closure-20260920/DELIVERY.json`；`audit/astra-endpoint-closure-20260920/lean-comparison/DELIVERY.json` |\n'
  files.append({'path':rel,'expected_sha256':R.sha(b),'text':body})
 for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户持续Goal授权完成圆环端点研究、计划与治理；登记C271–273并返回实际结构消费者，不改父目标。','files':files}
 (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
 (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
