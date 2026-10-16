#!/usr/bin/env python3
"""Canonical checkpoint for actual slice embeddings; the complete motion task stays open."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-NATIVE-EMBEDDING';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第二十七轮执行报告.md'
NEXT='AST-U03-NATIVE-MOTION-01继续：C311/C312与C313已给原F联合连续、原n/m内点初末态和每片到实际像的同胚（双方连续/双逆，非仅单射）。下一在原[0,1]×[0,1]形式化同源closingD/closingN/closingDen闭参数公式，先证正分母，再证与当前motion内点一致、联合连续/初末态，随后端部在t<1分离、末态相遇/完整纤维及具体空间界。保持原Strong/Weak边界，不静默加LEM或改成静态图/重呈现。完整F、原广义操作、G02错误承诺、四层集成和学术交付仍OPEN。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('DEEPENED','从已核F实际补每片嵌入，完整闭参数和父目标仍保留。'),
2:('ALIGNED','原实数/开区间/plane metric及函数均不改。'),
3:('DEEPENED','四字段连续性和双逆逐项装配，不用单射替拓扑嵌入。'),
5:('ALIGNED','先运行实际正构造再归因，不预设HoTT失败。'),
7:('DEEPENED','四草稿和fresh完整依赖由真实kernel给出，不以AI共识放行。'),
8:('DEEPENED','时间切片逆回到原圆环的实际连续变形函数。'),
9:('DEEPENED','对每个实时间t构造逆，闭时间实例明确。'),
10:('ALIGNED','拓扑嵌入族与实际物理执行仍分开。'),
11:('ALIGNED','证明检查不声称已实际执行全部空间点的运动。'),
12:('DEEPENED','实际像的成员仅mere存在；逆值用公式，资格消去只进命题。'),
13:('DEEPENED','源函数/环境子空间度量/逆律同时固定，不换观测合同。'),
14:('ALIGNED','形式正结果不冒充物理过程已获得。'),
15:('TENSION','当前得到原生正构造而非已闭合理论失配，原目标继续检验。'),
17:('ALIGNED','把原生运行与数学任务作为依据，不由训练印象作裁决。'),
19:('CORRECTED','有限递推的不完成不能替代当前实时间族性质。'),
21:('DEEPENED','四新源码、四草稿和一fresh核、精确source/run/index均留证。'),
22:('ALIGNED','保留两向现实标准和同任务归因，不以辅助定理关闭。'),
23:('DEEPENED','原t及[0,1]限制保留，没有转成有限事件序列。'),
31:('DEEPENED','原生范型接受显式连续逆和图上双逆，不能泛称拒绝此类构造。'),
34:('ALIGNED','未完成闭延拓不称不可延拓，不把无新参数称公理独立。'),
35:('DEEPENED','强验收为原函数到实际像的同胚，仍不穷尽所有现实生成语境。'),
37:('DEEPENED','直接沿原曲线推进拓扑性质，未回算术支线。'),
38:('ALIGNED','无类型拒绝也不作整个HoTT一致性认证。'),
39:('DEEPENED','真实主要缺口已减少，下一同源闭参数是直接后继。'),
40:('ALIGNED','原Lean任务用于对照验收，原生核独立验证。'),
41:('ALIGNED','已完成切片性质与未完成完整redo同时交代。'),
42:('ALIGNED','正构造作为最强反解释保留，不把它改名为缺陷。'),
43:('CORRECTED','从仅连续推进到实际像同胚，避免熟悉的静态证明循环。'),
44:('ALIGNED','实际数学模型有明确现实参照，但不自证物理实施。'),
45:('DEEPENED','原函数和环境度量保留，不能改造拓扑使任意双射自动连续。'),
46:('ALIGNED','现实过程问题驱动显式逆和原像消费者，不推给用户选择。')}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_AND_RELATION_PASS_WITH_SCOPE'
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==200
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();old=state['latest_session'];state['revision']=201;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'ACTUAL_NATIVE_SLICE_HOMEOMORPHISMS_CHECKED','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    manifest=json.loads((ROOT/delivery['primary_run']/'source-manifest.json').read_text())
    sources={x['path']:x['sha256'] for x in manifest['files'] if x['path'].startswith('HoTT/formal/')}
    state['records']['R-ASTRA-NATIVE-EMBEDDING-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / FULL_MOTION_TASK_OPEN','status':'every_actual_slice_homeomorphic_to_its_ambient_metric_image','depends_on':[],'related_records':[SID,'R-ASTRA-NATIVE-MOTION1-20260920'],'full_sources':[REPORT,'audit/astra-native-embedding-20260920/DELIVERY.json'],'source_hashes':sources,'scope':'C313: for every original real t the unchanged motion t is a homeomorphism from the original open interval onto its actual image with the plane subspace metric; explicit continuous inverse and both laws. No full closed-parameter extension/fibers, space bound, ambient-plane process, physical execution or four-stage completion.'}
    state['execution_control'].update(status='ACTIVE_GOAL_NATIVE_SLICES_CHECKED_CLOSED_PARAMETER_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 native real geometry / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-native-embedding-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C311/C312、1.28、revision200与414ebaf已保存
- status: NATIVE_SLICES_HOMEOMORPHIC_TO_ACTUAL_IMAGES / FULL_MOTION_AND_PARENT_OPEN

C313四新源与四草稿均通过；fresh核{delivery['primary_seconds']}秒，16本地/{delivery['import_modules']}图/41pin。formal+关系PASS。反射/turn/bend/stretch/原区间映射反解，实际像沿原plane metric，正反连续与双逆齐全。imageInduction只消去到命题，逆数据来自公式；无新LEM/Lift/SingleOmega/choice参数，不据此称公理最小。旧motion和C311/C312源码不改。

同T3复认：core未变，32managed hash相符；前轮46KC逐条回读，抽查KC24原文；原实际像/连续性库定义已读；query/plan无query_first提升。工具不认证理解。共享Skills沿同一目标执行，当前source和状态重新核验。

策略v1.29提交{commit}；下一：{NEXT}

按PROTOCOL§5保留完整KC legacy原子兼容bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001未关闭；公开报告四片。T01–05原范围保留；T06–10具体逆/像/度量；T11–17新源/核/依赖；T18–21无部署；T22–24精确结果/剩余/索引；T25未改AI治理；T26精确提交。共享C01–C09 NO_CHANGE，C10项目证据UPDATE。无Sub Agent、push/tag/发布。

element_usage：closure当前态/源定义；research实际逆构造/反解释；SOP完整任务不降格；verification核/图/索引；checkpoint原子current truth；dev-notes原文。没有新增通用治理设施。
'''
    core=state['current_core'];audit=f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']}条。

- core_change: NO
- direction_change: SAME_MOTION_CLOSED_PARAMETER_NEXT
- panorama_change: ADD_ACTUAL_NATIVE_SLICE_HOMEOMORPHISMS
- essay_change: NO
- update_decision: 原函数每片拓扑嵌入已核，继续完整闭参数合同
- cross_conflicts: 实际像同胚不等于环境过程/全闭参数/现实实施
- unresolved: 同源闭参数/端部纤维/界、原广义操作与理论承诺

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==core['kc_count']
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名自指/反射/量子化机制未由本切片逆检验，保持原范围。'))
        ev=('四新源、C313主run、第二十七轮；下一原F同源闭参数/纤维/界。若forward不是原motion、度量非原子空间、截断越界或核失败则撤回；若更强过程条件不同则不转用本结论。' if n in TOUCHED else '本轮不提供该主题新证明；精确消费者进入依赖或新直接来源触及时再核。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001简化：嵌入未缩为单射；002时间：逐实t不等于物理执行；003圆环ASK：逆分母有资格、原操作仍有界；004自反：不推元不一致；005表达：实际像度量不改，非全Lean翻译；006知识谱：库image/truncation直接查源码；007助力阻力：原生正结果认账；008现实骨架：闭参数和原操作仍须对齐。

## 已走过的路与即将选择

从同一F的联合连续推进到每片实际像同胚，强于裸单射。候选：同源闭参数/界（直接必要，选择）；复跑静态/算术（无新必要，不选）；全物理总模型（扩大任务，不选）。若闭公式对应失败保存原失败，在同合同修正，不回重呈现。第二十七轮003记八轴、八项反思和开放范围；非候选穷举，不报全HoTT完整性。核/像定义同时作为oracle边界，原Lean作独立框架对照，非跨模型机器翻译。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[delivery['primary_run']],'new_math_claims':['C-313'],'new_kernel_replay':True,'validation':'audit/astra-native-embedding-20260920/DELIVERY.json','parent_objective':'OPEN','full_motion_task':'OPEN'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-201'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 200$','source_state_revision: 201',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-201',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C313在原motion上完成每个实时间切片到其实际plane-metric像的同胚：显式连续逆与双逆，未以单射替代。四草稿+fresh核、formal/关系通过，详DELIVERY。C311/C312原函数不改。完整F仍缺同源闭参数延拓/端部纤维/界；原现实/理论归因仍开放。策略v1.29由'+commit+'保存。下一'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('NATIVE_MOTION_STAGE1_EMBEDDINGS_NEXT','NATIVE_SLICES_CHECKED_CLOSED_PARAMETER_NEXT').replace('`OUT-ASTRA-NATIVE-MOTION-26` |','`OUT-ASTRA-NATIVE-MOTION-26`、`OUT-ASTRA-NATIVE-EMBEDDING-27` |').replace('原生联合连续/原图初末态已核；下一同F每片嵌入及闭参数/界；原操作/归因开放','原F每片实际像同胚已核；下一同源闭参数/纤维/界；原操作/归因开放')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-NATIVE-EMBEDDING-27` | C313原函数每片到实际像的同胚 | `DIR-U-ASTRA-BREAKPOINT` | 原生核/连续显式逆/子空间像 | `FORMAL_CHECKED_WITH_SCOPE / FULL_MOTION_OPEN` | 原motion每个实t拓扑嵌入、双方连续/双逆 | 同源闭参数/端部纤维/空间界、原广义及整体 | `'+REPORT+'`；`audit/astra-native-embedding-20260920/DELIVERY.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户ACTIVE Goal及既有T3研究/集成授权；保存原F每片实际像同胚，继续原完整闭参数义务，不降低父目标。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
