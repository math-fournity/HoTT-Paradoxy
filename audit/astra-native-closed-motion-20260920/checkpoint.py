#!/usr/bin/env python3
"""Save the exact native closed extension, retaining fiber/separation/bound obligations."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-NATIVE-CLOSED-MOTION';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第二十八轮执行报告.md'
NEXT='AST-U03-NATIVE-MOTION-01继续：C314/C315已给同源closedMotion的全实时间/闭参数正分母、联合连续、与原F全部内点一致、完整n/m初末态和末态端点合并/闭域非单射，内点单射保留。下一在同一公式证明t<1端部图分离，再做末态完整纤维分类与明确空间界；若定义距离须对齐所用度量/观察，不以仅两端相遇代替完整纤维，也不把旧Lean的60界直接当原生结果。优先保持当前构造前提，任何额外原则/Strong-Weak边界显式登记。完成后返回同任务集成；原广义操作、G02错误承诺与学术交付保持OPEN。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('DEEPENED','推进原同源闭公式，不把静态延拓替全过程。'),
2:('ALIGNED','原Real/Plane/开闭参数和原F保持，前提不偷换。'),
3:('DEEPENED','正分母、连续、内点一致和初末态分别核验。'),
5:('ALIGNED','按核证据接纳正构造，不预设理论矛盾。'),
7:('DEEPENED','草稿与fresh核实际留证，导入错误不冒充数学失败。'),
8:('DEEPENED','原圆环两端及内点过程进入同源公式。'),
9:('DEEPENED','时间与参数联合变化有原生连续证明，不只静态末态。'),
10:('ALIGNED','数学延拓与物理实现保持区分。'),
11:('ALIGNED','核检查不代表执行了所有实点运动。'),
12:('DEEPENED','closedK的正性先于逆元，未假装分母为零时也可算。'),
13:('DEEPENED','闭域增点与原开域分别命名，内点保真有全称等式。'),
14:('ALIGNED','形式延拓不写成物理已完成。'),
15:('TENSION','当前仍为合法原生正构造，未得到目标理论失配。'),
17:('ALIGNED','原Lean按t=1分情形没有被当作必需公理；原生给构造性证明。'),
19:('CORRECTED','连续时间延拓不能被有限Pell递推的性质替换。'),
21:('DEEPENED','四新源、五草稿、一fresh核及精确索引/版本留存。'),
22:('ALIGNED','两个现实方向仍需同任务归因。'),
23:('DEEPENED','全实时间和闭方形限制明示，不以事件序列代替。'),
31:('DEEPENED','原生检查接受同源闭过程，不能泛称HoTT只接受静态图。'),
34:('ALIGNED','剩余端部分离/完整纤维/界未证，不称不可能。'),
35:('DEEPENED','端部观察进入全过程；广义来源/物理语境未穷尽。'),
37:('DEEPENED','工作继续原圆环公式，无算术换题。'),
38:('ALIGNED','NotInScope明确归因缺导入，非合法HoTT命题被拒。'),
39:('DEEPENED','闭公式一致性缺口已推进，下一端部/纤维/界直接必要。'),
40:('ALIGNED','对照原Lean公式并独立证明，不拿经典分支方式当唯一途径。'),
41:('ALIGNED','阶段成果与完整redo开放同时保存。'),
42:('ALIGNED','正构造认账，不能将闭域非单射重新命名为内点矛盾。'),
43:('CORRECTED','延续原F全过程，避免静态同胚/重呈现惯性。'),
44:('ALIGNED','模型可理解为几何过程但不自证物理。'),
45:('DEEPENED','原u同源内点图与新增边界参数的不同职责明确。'),
46:('ALIGNED','原过程问题驱动具体核验，不推给用户决定技术路线。')}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_AND_RELATION_PASS_WITH_SCOPE'
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==201
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();old=state['latest_session'];state['revision']=202;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'NATIVE_CLOSED_EXTENSION_CONTINUITY_AND_DIAGRAMS_CHECKED','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    manifest=json.loads((ROOT/delivery['primary_run']/'source-manifest.json').read_text());sources={x['path']:x['sha256'] for x in manifest['files'] if x['path'].startswith('HoTT/formal/')}
    state['records']['R-ASTRA-NATIVE-CLOSED-MOTION-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / FULL_MOTION_TASK_OPEN','status':'same_closed_extension_and_full_initial_final_diagrams_checked','depends_on':[],'related_records':[SID,'R-ASTRA-NATIVE-EMBEDDING-20260920'],'full_sources':[REPORT,'audit/astra-native-closed-motion-20260920/DELIVERY.json'],'source_hashes':sources,'scope':'C314/C315: same native rational closed-parameter extension has positive denominator for all real t, joint continuity, exact agreement with original motion at every open parameter, complete initial n/final m diagrams, final endpoint collision and closed-domain noninjectivity, retained interior injectivity. Endpoint separation before1, exact full fibers and space bound still required; no physical/four-stage completion.'}
    state['execution_control'].update(status='ACTIVE_GOAL_NATIVE_CLOSED_EXTENSION_CHECKED_FIBERS_BOUND_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 native real geometry / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-native-closed-motion-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C313、v1.29、revision201与31c453a已保存
- status: NATIVE_CLOSED_EXTENSION_CHECKED / FULL_MOTION_AND_PARENT_OPEN

C314/C315四新源、五草稿（001缺非严格不等式导入NotInScope；002–005通过）。fresh核{delivery['primary_seconds']}秒，20本地/{delivery['import_modules']}图/41pin，formal+关系PASS。全实时间/闭参数分母正性、联合连续、原F内点一致、原n/m全闭图初末态；最终两边界像相同但原内点保持单射，域不同无矛盾。

正性用严格序/apartness cotransitivity，没有决定t=1的新LEM/Lift/choice参数；原库公设和no-erasure配置保持，不称最小公理/一致性。原F和C313源不改。PROTOCOL同档复认，32managed hash相符，前轮46KC逐条读回、KC12–15抽查，原EndpointClosure公式与相关native源码已读；query/plan无query_first提升，工具不认证理解。

策略v1.30提交{commit}。下一：{NEXT}

46KC按PROTOCOL§5走legacy原子兼容bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；报告四片。T01–05原范围；T06–10公式/域/内点合同；T11–17新证明/核/失败/依赖；T18–21无部署；T22–24阶段结果/未决/索引；T25未改AI治理；T26精确提交。共享C01–C09 NO_CHANGE，C10项目证据UPDATE。无Sub Agent、push/tag/发布。

element_usage：closure复认；research具体正构造与最强反解释；SOP保父范围；verification核/源/索引；checkpoint原子状态；dev-notes原文。无新治理平台。
'''
    core=state['current_core'];audit=f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']}条。

- core_change: NO
- direction_change: SAME_CLOSED_FORMULA_SEPARATION_FIBERS_BOUND_NEXT
- panorama_change: ADD_NATIVE_CLOSED_EXTENSION
- essay_change: NO
- update_decision: 同源闭公式已核，继续剩余端部/纤维/界
- cross_conflicts: 闭域非单射与开域单射域不同，不能作矛盾；数学延拓不等于物理操作
- unresolved: t<1端部分离/完整纤维/空间界、原广义及理论承诺

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==core['kc_count']
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名自指/反射/量子化机制未由本闭公式检验，保持范围。'))
        ev=('四NativeClosedMotion源、C314/C315主run、第二十八轮；下一同源端部/纤维/界。若内点公式不一致、域或前提被换、核或版本失败则重评；未证全纤维不称只合并两端。' if n in TOUCHED else '本轮无该主题新证明；精确消费者进入依赖或新直接来源触及再核。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001简化：闭公式与F有全内点等式；002时间：全实t不冒充物理；003圆环ASK：正分母资格和端部观察显式；004自反：不外推元不一致；005表达：开闭参数分别命名；006知识谱：经典by_cases路线不是唯一原生路线；007助力阻力：继续全过程而非静态重复；008现实骨架：新增边界参数不是原去点圆中的点。

## 已走过的路与即将选择

同源闭公式正性/连续/内点和全初末图均核。下一同公式的t<1端部分离、完整纤维和空间界（直接必要）；静态/算术重复无新价值，不选；完整物理总模型不是当前前置。分母/域/度量出现新差异时重评，不能默换。八轴：原实数/连续函数×同源闭参数扩展×圆环过程×原F/端部观察×联合时间参数×连续及一致/图身份×native kernel×固定库；无候选穷举，不报全HoTT完整。独立对照为原Lean，不是跨模型机器翻译。下一三项未证与原归因开放。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[delivery['primary_run']],'new_math_claims':['C-314','C-315'],'new_kernel_replay':True,'validation':'audit/astra-native-closed-motion-20260920/DELIVERY.json','parent_objective':'OPEN','full_motion_task':'OPEN'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-202'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 201$','source_state_revision: 202',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-202',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C314/C315同源closedMotion已核：全实时间/闭参数正分母、联合连续、原F内点一致、全n/m初末图、末态端点合并及闭域非单射/内点单射。原F/C313源不改；fresh及formal/关系见DELIVERY。完整F仍缺t<1端部分离/完整纤维/空间界；原广义/理论归因开放。策略v1.30由'+commit+'保存。下一'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('NATIVE_SLICES_CHECKED_CLOSED_PARAMETER_NEXT','NATIVE_CLOSED_EXTENSION_CHECKED_FIBERS_BOUND_NEXT').replace('`OUT-ASTRA-NATIVE-EMBEDDING-27` |','`OUT-ASTRA-NATIVE-EMBEDDING-27`、`OUT-ASTRA-NATIVE-CLOSED-MOTION-28` |').replace('原F每片实际像同胚已核；下一同源闭参数/纤维/界；原操作/归因开放','同源闭公式及全初末图已核；下一端部分离/完整纤维/界；原操作/归因开放')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-NATIVE-CLOSED-MOTION-28` | C314/C315原F同源闭参数延拓 | `DIR-U-ASTRA-BREAKPOINT` | 原生核/构造性正分母/联合连续/内点一致 | `FORMAL_CHECKED_WITH_SCOPE / FULL_MOTION_OPEN` | 全n/m初末图、端点合并/闭域非单射与内点单射 | t<1端部分离/完整纤维/空间界、原广义及整体 | `'+REPORT+'`；`audit/astra-native-closed-motion-20260920/DELIVERY.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户ACTIVE Goal及既有T3研究/集成授权；保存原F同源闭延拓，保留未决端部/纤维/界与完整父目标。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
