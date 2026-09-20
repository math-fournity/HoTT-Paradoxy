#!/usr/bin/env python3
"""Save the scoped native geometric bundle and return to the four-stage task audit."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-NATIVE-MOTION-BUNDLE';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第三十轮执行报告.md'
NEXT='AST-U07-CASE-INTEGRATION-02：消费C318/C319的256坐标界、同一NativeMotionEvidence记录与固定末态Weak覆盖iff Lift/RNZA，以及C311–317/原R-REP/R-AMBIENT/算术九族。回原六用户文本及022/023/025/027/030逐G01–G06和U00–U09验收：同X/Step/Done、确切理论承诺、目标困难、保真、最强恢复和证据边界。给每候选准确判词及决定性未决；Weak覆盖必要原则与相对整个基线的新公理/独立性不混。声明几何范围已闭合，不重复辅助构造；只有新的原文、机制或实际consumer证据才安排有界successor。U08完整资格/可移植和U09学术交付及原广义现实目标仍保持，不把正模型或记录装配称父目标完成。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('DEEPENED','完成声明几何范围后回四层整体，不停在更多辅助引理。'),
2:('ALIGNED','记录的所有字段绑定同一原函数/域/度量，Weak覆盖另有精确类型。'),
3:('DEEPENED','联合连续/嵌入/图/纤维/界在同一记录中装配，非跨合同拼接。'),
5:('ALIGNED','正模型与条件边界按事实保存，归因不先定。'),
7:('DEEPENED','实际核与精确源/图记录，四次草稿错误保留，不由AI自评判真。'),
8:('DEEPENED','原圆环时间族在固定有限空间界中实现所声明几何性质。'),
9:('DEEPENED','闭时间/参数域精确，空间界不替速度界。'),
10:('ALIGNED','模型几何完成与原现实目标、物理执行分别定级。'),
11:('ALIGNED','核接受证明记录不意味着执行了全部时间/空间过程。'),
12:('DEEPENED','Weak覆盖的mere存在与给定Lift后的选定输出分开，未偷取截断数据。'),
13:('DEEPENED','固定末态图的覆盖iff精确原则，不扩大为任意同胚必需。'),
14:('ALIGNED','界/存在/选定参数不冒充实际物理交付。'),
15:('TENSION','仍未定位目标错误承诺/失配；几何正构造不改名击落。'),
17:('ALIGNED','从原公式证明粗界256，不继承另一包60或预设经典分支必需。'),
19:('CORRECTED','全连续嵌入族/闭端部行为在同域有据，不能由单一逼近失败否定。'),
21:('DEEPENED','四新源、八草稿、fresh主run、矩阵与版本检查留存。'),
22:('ALIGNED','原双向现实目标回G01–G06验收，不被局部成功替代。'),
23:('DEEPENED','所有t∈[0,1]的统一坐标界，不是有限时刻采样。'),
31:('DEEPENED','原生记录承载全部声明几何条款，弱域条件独立可见。'),
34:('ALIGNED','Task iff P不等于P相对整个基线独立或必须新增公理。'),
35:('DEEPENED','原结构和全时间性质明确表达，广义现实操作并未被穷尽。'),
37:('DEEPENED','原圆环几何的真实native缺口按声明范围闭合，下一回主任务。'),
38:('ALIGNED','语法/导入/显式参数修复不归因HoTT理论拒绝。'),
39:('CORRECTED','停止局部几何无止境深化，重新检查原指控的决定性连接。'),
40:('ALIGNED','原Lean/原生前提与所声明粗界比较，非全模型翻译。'),
41:('ALIGNED','声明几何子任务完成不等于完整redo完成。'),
42:('ALIGNED','最强保范围正构造保留，不将必要条件包装成免费假装已证死。'),
43:('CORRECTED','下一从熟悉几何返回同任务/承诺/现实归因，防路径依赖。'),
44:('ALIGNED','数学模型的有限空间图与现实/假想现实对应仍需独立说明。'),
45:('DEEPENED','Weak覆盖具体界限由同点same-map证明，不用名称替观察身份。'),
46:('ALIGNED','真实构造和原文对齐共同决定后继，用户不被要求提供证明。')}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_AND_RELATION_PASS_WITH_SCOPE'
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==203
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();old=state['latest_session'];state['revision']=204;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'NATIVE_GEOMETRIC_BUNDLE_AND_FIXED_WEAK_COVERAGE_CRITERION_CHECKED','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    manifest=json.loads((ROOT/delivery['primary_run']/'source-manifest.json').read_text());sources={x['path']:x['sha256'] for x in manifest['files'] if x['path'].startswith('HoTT/formal/')}
    state['records']['R-ASTRA-NATIVE-MOTION-BUNDLE-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / DECLARED_GEOMETRY_COMPLETE_WEAK_CONDITIONAL','status':'coordinate_bound_256_and_one_motion_evidence_record','depends_on':[],'related_records':[SID,'R-ASTRA-NATIVE-ENDPOINT-FIBERS-20260920','R-ASTRA-WEAK-PRINCIPLE-20260920'],'full_sources':[REPORT,'audit/astra-native-spatial-bound-20260920/DELIVERY.json'],'source_hashes':sources,'scope':'C318/C319: uniform coordinate bound256 on closed square and original open motion; one record on unchanged maps assembles joint continuity, slice image homeomorphisms, interior/n/m diagrams, endpoint time, full fibers and bounds. Fixed final Weak coverage iff Circle Lift and RNZA; given Lift, chosen original parameter. No unconditional Weak coverage, base-independence/LEM necessity, whole-model translation, physical or parent four-stage result.'}
    state['execution_control'].update(status='ACTIVE_GOAL_DECLARED_NATIVE_GEOMETRY_CHECKED_CASE_INTEGRATION_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 native geometry and scoped integration / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-native-spatial-bound-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C316/C317、1.31、revision203与3080159已保存
- status: DECLARED_NATIVE_GEOMETRY_CHECKED_WITH_WEAK_CRITERION / PARENT_OPEN

C318/C319四新源。八草稿：001/003/006/008通过；002括号解析、004缺positive导入、005未显式给Prop motive、007弱覆盖证明的子类型端点隐参数未定，均保留原诊断并在同命题上修复。fresh主run{delivery['primary_seconds']}秒、27本地/{delivery['import_modules']}图/41pin，formal+关系PASS。每坐标≤256；记录12字段绑定原函数，Weak最终覆盖iff Lift/RNZA，给定Lift有chosen参数。没有独立性/LEM必要性或物理结论。

同T3复认：core与32managed哈希一致，前轮46KC逐条复读、KC38–40原文样本；父策略001/008/009/010全文复核成功边界。query/plan无query_first提升。原F/闭延拓/纤维源码不改，工具不认证理解。共享Skills沿当前goal消费，档位未变。

策略v1.32提交{commit}；下一：{NEXT}

46KC按PROTOCOL§5使用legacy原子兼容bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；报告五片。T01–05原目标；T06–10同函数记录/Weak合同；T11–17新源/核/失败/依赖；T18–21无部署；T22–24声明几何闭合与父未决；T25未改AI治理；T26精确提交。共享C01–C09 NO_CHANGE，C10项目证据UPDATE。无Sub Agent、push/tag/发布。

element_usage：closure闭包/父范围回读；research原公式/最强反解释；SOP返回U07；verification源核索引；checkpoint原子状态；dev-notes原文。没有扩张通用平台。
'''
    core=state['current_core'];audit=f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']}条。

- core_change: NO
- direction_change: RETURN_FOUR_STAGE_CASE_INTEGRATION
- panorama_change: ADD_BOUND_AND_NATIVE_MOTION_RECORD_WEAK_CRITERION
- essay_change: NO
- update_decision: 声明几何条款已核，返回原目标决定性连接审计
- cross_conflicts: 条件Weak覆盖不等于无条件；Task iff P不等于基线独立；空间界不等于物理
- unresolved: 原广义任务/G02承诺/同任务失配、完整资格/可移植/学术交付

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==core['kc_count']
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名自指/反射/量子化机制未由本几何界/记录检验，保持原范围。'))
        ev=('四新源、C318/C319主run、第三十轮及原策略001/008/009/010；下一U07。若记录换图/域、界漏输入、Weak必要性越界或核失败则重评；只有新规则/consumer/原文证据才开后继。' if n in TOUCHED else '本轮无该主题新证明；精确consumer进入依赖或新直接来源触及时再核。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001简化：同一记录而非拼不同任务；002时间：坐标界不替速度/物理；003圆环ASK：给定Lift与Weak覆盖范围显式；004自反：不推元不一致；005表达：记录完成不等于广义现实表达穷尽；006知识谱：原生构造与经典源分别核；007助力阻力：停止辅助几何惯性；008现实骨架：返回同X/完成/承诺对齐。

## 已走过的路与即将选择

原公式几何条款和256界进入单一typed记录；固定Weak覆盖↔原则有实际最终图连接。候选：U07同任务/G02/现实审计（直接必要，选）；优化256到60（父需要仅有限空间界，无当前必要）；重复几何/算术（不选）；新机制（仅由新证据触发）。父001六义务缺一不可，防线成功不改名击落。八轴：实数/连续与Prop覆盖×界与整体组装×圆环过程×原F与Weak消费者×全闭域/完成×几何合同/必要原则×native kernel×固定库。非候选穷举，非全模型翻译，公设独立/物理/全目标不由记录自动证明。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[delivery['primary_run']],'new_math_claims':['C-318','C-319'],'new_kernel_replay':True,'validation':'audit/astra-native-spatial-bound-20260920/DELIVERY.json','parent_objective':'OPEN','full_motion_task':'DECLARED_GEOMETRY_COMPLETE_WITH_SCOPE_WEAK_CONDITIONAL'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-204'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 203$','source_state_revision: 204',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-204',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C318/C319已核每坐标≤256与同一NativeMotionEvidence记录，声明原生参数图上的连续/嵌入/闭延拓/初末态/时间/纤维/界齐备；固定末态Weak覆盖iff Lift/RNZA，给定Lift有chosen参数，不称无条件覆盖或基线独立。原源未改，fresh/formal关系见DELIVERY。结束辅助几何单元并回四层同任务审计。策略v1.32由'+commit+'保存。下一'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('NATIVE_FIBERS_CHECKED_SPACE_BOUND_NEXT','DECLARED_NATIVE_GEOMETRY_CHECKED_CASE_INTEGRATION_NEXT').replace('`OUT-ASTRA-NATIVE-ENDPOINT-FIBERS-29` |','`OUT-ASTRA-NATIVE-ENDPOINT-FIBERS-29`、`OUT-ASTRA-NATIVE-MOTION-BUNDLE-30` |').replace('精确相遇时间/完整末态纤维已核；下一统一空间界后回集成；原操作/归因开放','声明几何/256界/同记录已核，Weak覆盖有精确条件；下一四层同任务整体审计')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-NATIVE-MOTION-BUNDLE-30` | C318/C319空间界与同图证据记录及Weak覆盖条件 | `DIR-U-ASTRA-BREAKPOINT` | 原生核/实不等式/同函数record/实际末态覆盖iff | `FORMAL_CHECKED_WITH_SCOPE / DECLARED_GEOMETRY_COMPLETE_WEAK_CONDITIONAL` | 每坐标≤256，声明几何齐备，Weak固定覆盖iff Lift/RNZA | 原G01–G06/理论承诺/现实与学术交付 | `'+REPORT+'`；`audit/astra-native-spatial-bound-20260920/DELIVERY.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户ACTIVE Goal及既有T3研究/集成授权；保存声明原生几何范围及固定Weak条件，返回四层整体，不改变父成功标准。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
