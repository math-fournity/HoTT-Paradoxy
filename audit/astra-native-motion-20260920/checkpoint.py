#!/usr/bin/env python3
"""Publish the bounded native time-family result without closing the complete motion task."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-NATIVE-MOTION1';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第二十六轮执行报告.md'
NEXT='AST-U03-NATIVE-MOTION-01继续：C311/C312已给原生时间族、联合连续和原n/m内点图初末态。下一在同一motion上证明每个时间切片的拓扑嵌入：伸缩的正系数与连续逆、bend坐标图逆、turn正行列式逆及组合。不能仅用HoTT集合单射/is-emb代替拓扑嵌入。随后继续原同源闭参数公式的分母、内点一致、联合连续、端部/完整纤维和空间界；Strong/Weak与所需原则分开。完整F、原广义现实操作、G02错误理论承诺、四层集成和学术交付保持OPEN。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('DEEPENED','对原完整F缺口实际构造并运行，初末态/连续性与嵌入义务分开。'),
2:('ALIGNED','固定原Real/Plane/开区间及no-erasure演算，不用同名模型替换。'),
3:('ALIGNED','把多条件逐项证明，不以连续性代替所有切片嵌入。'),
5:('ALIGNED','正构造过核按范围认账，不预设理论缺陷。'),
7:('DEEPENED','实际241.719743秒fresh核及源码收据，不依AI数学直觉放行。'),
8:('DEEPENED','圆环启发落实到带实时间参数的连续函数，未推物理实现。'),
9:('DEEPENED','时间作为原Real变量明确进入公式和联合度量。'),
10:('ALIGNED','原现实相对问题保留，不由数学同伦自动判物理可行。'),
11:('CORRECTED','内核检查是证明检查，时间族的存在不等于现实执行全过程。'),
12:('DEEPENED','每个逆元先有正分母证据，完整输入和输出接口具名。'),
13:('ALIGNED','给定类型资格与原现实完成标准分开，不把核通过直接称任务完成。'),
14:('ALIGNED','精确登记定义/证明与实际物理交付的区别。'),
15:('TENSION','本轮得到的是合法原生正构造，尚非Z铁律的目标失配见证。'),
17:('ALIGNED','用真实原生源和最强正构造检验预期，不由训练共识裁决。'),
19:('CORRECTED','原连续时间公式可表达且部分性质已核；有限递推不完成不能作普遍否定。'),
21:('DEEPENED','三新源码、四草稿、一次fresh核、精确索引和资格检查留存。'),
22:('ALIGNED','不混两向现实标准，父目标尚需同任务归因。'),
23:('DEEPENED','显式时间t及其闭区间限制可直接定位，不用抽象时序代替。'),
31:('DEEPENED','原生范型接受联合连续及端点等式，不继续声称静态结果等于全F。'),
34:('ALIGNED','未证中间嵌入不作不可能性；没有额外原则参数不作独立性。'),
35:('DEEPENED','补出原模型中的实际时间族，但没有声称已穷尽用户历史/操作语境。'),
37:('DEEPENED','直接围绕原圆/区间写函数及端点证明，不转算术支线。'),
38:('ALIGNED','NotInScope准确归因导入遗漏，不称HoTT逻辑缺陷。'),
39:('DEEPENED','推进主要G04缺口；下一嵌入和闭延拓是真实剩余消费者。'),
40:('ALIGNED','Lean公式作被核对来源，不把其核当原生核或全模型翻译。'),
41:('ALIGNED','本阶段完成与完整redo未完成同时交代。'),
42:('ALIGNED','不把成功正构造改称拒签；保留其对原预期的反解释。'),
43:('CORRECTED','打破静态/重呈现重复，沿已核F继续真正缺的全过程性质。'),
44:('ALIGNED','数学时间模型与现实/假想现实的对应仍明确有限范围。'),
45:('DEEPENED','原n/m图通过逐点等式接入时间族，原Step约束没有被悄悄替换。'),
46:('ALIGNED','以原过程问题选择实际构造，观察与完成条件保持可追问。')}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_AND_RELATION_PASS_WITH_SCOPE'
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==199
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted']
    (OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();old=state['latest_session'];state['revision']=200;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'NATIVE_TIME_FAMILY_CONTINUITY_AND_ENDPOINTS_CHECKED','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    manifest=json.loads((ROOT/delivery['primary_run']/'source-manifest.json').read_text())
    sources={x['path']:x['sha256'] for x in manifest['files'] if x['path'].startswith('HoTT/formal/')}
    state['records']['R-ASTRA-NATIVE-MOTION1-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / FULL_MOTION_TASK_OPEN','status':'joint_continuity_and_original_endpoint_diagrams_checked','depends_on':[],'related_records':[SID,'R-ASTRA-INTEGRATION-AUDIT-20260920'],'full_sources':[REPORT,'audit/astra-native-motion-20260920/DELIVERY.json'],'source_hashes':sources,'scope':'C311/C312: actual native rational time family, positive denominators, joint continuity, closed-time restriction and exact original n/m interior endpoint diagrams with explicit y reflection. Intermediate topological embeddings, full closed-parameter time extension/fibers and spatial bound remain required; no physical or full four-stage result.'}
    state['execution_control'].update(status='ACTIVE_GOAL_NATIVE_MOTION_STAGE1_EMBEDDINGS_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 native real geometry / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-native-motion-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；整体审计、1.27、revision199实际保存
- status: NATIVE_MOTION_STAGE1_CHECKED / FULL_MOTION_AND_PARENT_OPEN

C311/C312实际三新模块。四草稿：三通过，一次NotInScope缺abs导入，修复后过核；fresh忽略接口241.719743秒，12本地/1083图/41pin，formal+关系PASS。原n/m图逐点对接，反射不改参数，固定库原有公设明确。没有新LEM/Lift/SingleOmega参数，也不据此宣称公理最小性。不是全Lean模型翻译。

PROTOCOL v3同档复认：core hash未变；32 managed owner哈希相符；46KC前轮每行全文复读并如下回评；抽查KC41–46原文；前轮199对投影的实际diff已读。research task query/plan无query_first提升，当前父义务与实际原公式复核。工具不认证理解。

策略v1.28已提交{commit}。下一：{NEXT}

46KC使用PROTOCOL§5明确允许的legacy原子bundle；G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001不伪称关闭。公开报告四片。T01–05原范围不变；T06–10原公式/端点接口；T11–17新源/核/依赖/失败；T18–21无部署或外部操作；T22–24阶段结果/剩余与索引；T25未改AI治理；T26精确提交。共享C01–C09 NO_CHANGE，C10项目数学证据UPDATE。

element_usage：closure恢复任务与hash；research实际构造/正反解释；SOP保持父范围；verification源核索引；checkpoint原子写回；dev-notes原文归档。无Sub Agent、push/tag/发布。
'''
    audit=f'''# {SID} 核心认知回评

core-cognition-generation-7；46条。

- core_change: NO
- direction_change: CONTINUE_SAME_MOTION_EMBEDDINGS_NEXT
- panorama_change: ADD_NATIVE_TIME_FAMILY_STAGE1
- essay_change: NO
- update_decision: 记录原生联合连续与初末态，完整父任务不降格
- cross_conflicts: 数学连续族不等于每片嵌入/现实实施；初末态不是全闭方形
- unresolved: 中间嵌入、同源闭参数/纤维/界、原广义操作和理论承诺

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名自指/反射/量子化机制未由本时间函数检验，保持原范围。'))
        ev=('三NativeMotion源码、C311/C312主run、第二十六轮；下一原F嵌入/闭延拓。若参数/公式/度量与原图不符、源或核复现失败则重评；若只得单射不能报拓扑嵌入。' if n in TOUCHED else '本轮不提供该主题新证明；其精确消费者进入当前依赖或新用户原文出现时触及。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001问题/简化：不以省略嵌入收工；002时间/前提：实时间联合函数与物理时间分开；003圆环/ASK：原输入和分母资格明确；004自反：不扩成元不一致；005表达/原文：具体公式对齐不冒充全模型翻译；006知识谱：Lean作为对照源码而非权威裁决；007助力阻力：原生正结果认账，避免静态循环；008现实骨架：实际模型正构造仍需原操作/物理对应。

## 已走过的路与即将选择

已从原静态图推进到真实时间函数，联合连续和端点均核；父完整范围保持。候选：继续同F嵌入/闭延拓（有直接依赖，选定）；回算术/Markov（当前非必要，暂缓）；扩大物理总模型（会换题，不选）。下一不能以仅单射代替嵌入。反证条件是具体逆图/参数域证明失败或源对应出现差异，保存失败后在同合同重新构造，不改为重呈现。

八轴与遗漏、八项反思见第二十六轮003。当前为一个精确有理公式的全称证明，不是候选穷举；未触及全HoTT/任意现实操作。独立框架对照为原Lean源码，非自动保真翻译。物理/所有切片/闭参数/空间界保持OPEN。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[delivery['primary_run']],'new_math_claims':['C-311','C-312'],'new_kernel_replay':True,'validation':'audit/astra-native-motion-20260920/DELIVERY.json','parent_objective':'OPEN','full_motion_task':'OPEN'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-200'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 199$','source_state_revision: 200',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-200',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。原生时间族第一阶段C311/C312已核：联合连续、原n/m内点图初末态与固定反射方向对齐。fresh241.719743秒，12本地/1083图/41pin，formal+关系PASS。完整F尚缺中间拓扑嵌入/全闭参数/纤维/界；不冒充全部HoTT/物理结果。策略v1.28由'+commit+'保存。下一'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('SAME_TASK_AUDITED_NATIVE_MOTION_NEXT','NATIVE_MOTION_STAGE1_EMBEDDINGS_NEXT').replace('`OUT-ASTRA-INTEGRATION-AUDIT-25` |','`OUT-ASTRA-INTEGRATION-AUDIT-25`、`OUT-ASTRA-NATIVE-MOTION-26` |').replace('六义务审计未闭合整体；下一完整原生时间曲线族；原操作/归因开放','原生联合连续/原图初末态已核；下一同F每片嵌入及闭参数/界；原操作/归因开放')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-NATIVE-MOTION-26` | C311/C312原生实际时间族第一阶段 | `DIR-U-ASTRA-BREAKPOINT` | 原生核/正分母/联合度量/原图路径 | `FORMAL_CHECKED_WITH_SCOPE / FULL_MOTION_OPEN` | 联合连续与原n/m初末态、固定y反射对齐 | 同F每片嵌入/闭参数/纤维/界、原广义及整体 | `'+REPORT+'`；`audit/astra-native-motion-20260920/DELIVERY.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户ACTIVE Goal及既有T3研究/集成授权；保存实际原生时间族第一阶段，保留完整父任务与待证义务。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
