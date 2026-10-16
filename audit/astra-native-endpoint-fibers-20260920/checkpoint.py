#!/usr/bin/env python3
"""Save exact endpoint meeting time and complete final fibers; retain the spatial bound."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-NATIVE-ENDPOINT-FIBERS';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第二十九轮执行报告.md'
NEXT='AST-U03-NATIVE-MOTION-01继续：C316已核t<1端部分离及闭时间内两端相遇当且仅当t=1；C317完整末态同像关系为u=v或端点对（两种次序），命题性析取，不是实数相等decider。C311–C317原函数/域/连续/嵌入/闭延拓链保持。下一证明同一motion/closedMotion在原闭时间域中的明确统一空间界；可以给相称但准确的粗界，不直接继承Lean的60或把空间界当速度/长度/物理执行。然后回AST-G01–G06四层同任务集成与全范围完成审计。原广义现实操作、G02错误理论承诺、Strong-Weak与学术交付保持原义务。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('DEEPENED','原闭公式的何时相遇与哪些参数同像均实际证明，保留空间界和父目标。'),
2:('ALIGNED','原t/u/closedMotion/mCompletion及基础配置保持。'),
3:('DEEPENED','t<1不同与t=1相同分别固定量词，不能拼矛盾。'),
5:('ALIGNED','正构造与完整分类按证据认账，归因后置。'),
7:('DEEPENED','三草稿与fresh核均实际运行，不以经典直觉替代。'),
8:('DEEPENED','原圆环两个边界参数与全闭域纤维直接进入证明。'),
9:('DEEPENED','闭时间内相遇iff t=1有明确原生类型。'),
10:('ALIGNED','数学时刻/参数分类不冒充物理实施。'),
11:('ALIGNED','证明核检查不是遍历全部时间或全部参数的执行。'),
12:('DEEPENED','分类在Prop析取中，不伪装成任意实数相等决策。'),
13:('DEEPENED','全纤维义务从仅端点见证提升为所有参数双向关系。'),
14:('ALIGNED','逻辑分类与有效输入比较、物理完成分别定级。'),
15:('TENSION','当前仍未形成HoTT错误承诺/现实失配；合法原生正结果保留。'),
17:('ALIGNED','以located order与apartness构造分类，未偷加实数可判定相等。'),
19:('CORRECTED','所有t<1分离与终点相遇相容，不把渐近描述当未完成定理。'),
21:('DEEPENED','两新源码、三草稿、一fresh核与源/索引/版本留证。'),
22:('ALIGNED','原双向现实目标仍需同任务归因。'),
23:('DEEPENED','相遇时刻精确到闭时间参数1，非有限序列替代。'),
31:('DEEPENED','原生范型接受完整端部/纤维关系，不能泛称拒绝该过程。'),
34:('ALIGNED','没有新增LEM参数不证明公理最小；空间界未证不作否定。'),
35:('DEEPENED','保持原模型做全参数分类，不声称穷尽所有现实生成方法。'),
37:('DEEPENED','继续原圆环同源公式，无算术换题。'),
38:('ALIGNED','类型检查全部成功不升级为整个理论一致性。'),
39:('DEEPENED','两个具名缺口关闭，下一空间界为最后的该公式局部义务。'),
40:('ALIGNED','按原Lean纤维形式核对但原生独立证明，非全模型翻译。'),
41:('ALIGNED','本阶段闭合与整体redo未完成并存。'),
42:('ALIGNED','正向反解释不改称缺陷，完整纤维不混成物理判词。'),
43:('CORRECTED','从两端见证推进到完整关系，避免静态或局部重复。'),
44:('ALIGNED','参数边界/实际像/现实角色分开。'),
45:('DEEPENED','观察固定原闭图，开闭域和逻辑析取边界明确。'),
46:('ALIGNED','继续实际核验原过程问题，不把技术决策交回用户。')}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_AND_RELATION_PASS_WITH_SCOPE'
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==202
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();old=state['latest_session'];state['revision']=203;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'NATIVE_ENDPOINT_TIME_AND_COMPLETE_FINAL_FIBERS_CHECKED','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    manifest=json.loads((ROOT/delivery['primary_run']/'source-manifest.json').read_text());sources={x['path']:x['sha256'] for x in manifest['files'] if x['path'].startswith('HoTT/formal/')}
    state['records']['R-ASTRA-NATIVE-ENDPOINT-FIBERS-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / SPACE_BOUND_PENDING','status':'endpoint_meeting_iff_time_one_and_complete_final_fibers','depends_on':[],'related_records':[SID,'R-ASTRA-NATIVE-CLOSED-MOTION-20260920'],'full_sources':[REPORT,'audit/astra-native-endpoint-fibers-20260920/DELIVERY.json'],'source_hashes':sources,'scope':'C316/C317: original endpoint images are unequal for all t<1 and meet iff t=1 on closed time. Full final same-image relation iff equal parameters or opposite endpoints, as propositional disjunction with both implications. No real equality decider or physical implementation; uniform spatial bound and four-stage integration remain open.'}
    state['execution_control'].update(status='ACTIVE_GOAL_NATIVE_FIBERS_CHECKED_SPACE_BOUND_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 native real geometry / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-native-endpoint-fibers-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C314/C315、1.30、revision202与9727d92已保存
- status: EXACT_ENDPOINT_TIME_AND_FULL_FINAL_FIBERS_CHECKED / SPACE_BOUND_AND_PARENT_OPEN

C316/C317两新源码、三草稿均过；fresh核{delivery['primary_seconds']}秒，22本地/{delivery['import_modules']}图/41pin，formal+关系PASS。原closedMotion与mCompletion不改；所有t<1端部不同、闭时间内相遇iff t=1，末态完整同像关系为相等或两个端点。先内点纤维唯一，再严格有序同像迫成端点对，再以abs(u-v)的located分支取得Prop分类。没有新增LEM/Lift/choice参数，也不是实数可判等程序或原库公理最小性/一致性证书。

同T3复认：core未变，32managed hash一致，前轮46KC逐行复读；原内点/端部/基础序和apartness模块已读，当前原文样本沿同任务连续保留，query/plan无query_first提升。工具不认证理解。

策略v1.31提交{commit}；下一：{NEXT}

46KC按PROTOCOL§5走legacy原子兼容bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；公开报告四片。T01–05父范围；T06–10全参数关系/时间iff；T11–17新证明/核/依赖；T18–21无部署；T22–24进展/剩余/索引；T25未改AI治理；T26精确提交。共享C01–C09 NO_CHANGE，C10项目证据UPDATE。无Sub Agent、push/tag/发布。

element_usage：closure复认；research原构造/反解释；SOP全范围；verification源核索引；checkpoint原子状态；dev-notes原文。没有新平台。
'''
    core=state['current_core'];audit=f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']}条。

- core_change: NO
- direction_change: SAME_FORMULA_UNIFORM_SPACE_BOUND_NEXT
- panorama_change: ADD_EXACT_ENDPOINT_TIME_AND_COMPLETE_FIBERS
- essay_change: NO
- update_decision: 时间和完整纤维已核，下一空间界后回整体集成
- cross_conflicts: Prop分类不是相等decider；边界参数相遇不是原开域点合并或物理执行
- unresolved: 统一空间界、原广义操作/错误理论承诺及学术交付

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==core['kc_count']
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名自指/反射/量子化构造不由本纤维分类检验，保留范围。'))
        ev=('NativeEndpointSeparation/NativeCompletionFibers、C316/C317主run、第二十九轮；下一原F空间界。若漏参数情形、将Prop当判定数据、改源或核失败则重评；物理归因必须另对齐。' if n in TOUCHED else '本轮无该主题新证明；精确consumer进入依赖或新直接来源触及时再核。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001简化：全纤维不缩为两个端点；002时间：相遇iff精确t1但不是物理执行；003圆环ASK：域和Prop分类明示；004自反：不外推元不一致；005表达：逻辑分类与可判定相等分开；006知识谱：独立构造性路线不强抄经典by_cases；007助力阻力：不以正结果改称缺陷；008现实骨架：新增边界参数角色保持。

## 已走过的路与即将选择

两个有界义务已核，下一原公式统一空间界（直接必要）；重复静态/算术或扩大为全物理模型无当前必要。空间界不能替速度界，给不同粗界须准确交付。八轴：原实数/图×闭域纤维识别×圆环过程×原端部/同像consumer×全参数/时间×精确iff×native kernel×固定库。非候选枚举，无全理论覆盖。原Lean为独立框架对照而非机器模型翻译。完成空间界后回父G01–G06，不永久打磨本子模块。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[delivery['primary_run']],'new_math_claims':['C-316','C-317'],'new_kernel_replay':True,'validation':'audit/astra-native-endpoint-fibers-20260920/DELIVERY.json','parent_objective':'OPEN','full_motion_task':'SPACE_BOUND_PENDING'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-203'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 202$','source_state_revision: 203',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-203',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C316/C317已核原闭公式的精确相遇时间和末态完整纤维：t<1端部不同，闭时间内相遇iff t=1；末态同像iff u=v或端点对。Prop分类不当实数相等decider。两新源/三草稿/fresh与formal关系核验见DELIVERY；原F/闭延拓源不改。当前公式剩统一空间界，之后回同任务集成。策略v1.31由'+commit+'保存。下一'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('NATIVE_CLOSED_EXTENSION_CHECKED_FIBERS_BOUND_NEXT','NATIVE_FIBERS_CHECKED_SPACE_BOUND_NEXT').replace('`OUT-ASTRA-NATIVE-CLOSED-MOTION-28` |','`OUT-ASTRA-NATIVE-CLOSED-MOTION-28`、`OUT-ASTRA-NATIVE-ENDPOINT-FIBERS-29` |').replace('同源闭公式及全初末图已核；下一端部分离/完整纤维/界；原操作/归因开放','精确相遇时间/完整末态纤维已核；下一统一空间界后回集成；原操作/归因开放')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-NATIVE-ENDPOINT-FIBERS-29` | C316/C317精确端部时间及完整末态纤维 | `DIR-U-ASTRA-BREAKPOINT` | 原生核/逆映射/located order/Prop双向分类 | `FORMAL_CHECKED_WITH_SCOPE / SPACE_BOUND_PENDING` | 端部相遇iff t1，末态同像iff相等或端点对 | 同公式统一空间界、原广义及四层集成 | `'+REPORT+'`；`audit/astra-native-endpoint-fibers-20260920/DELIVERY.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户ACTIVE Goal及既有T3研究/集成授权；保存原端部时间与完整纤维，保留统一空间界及完整父目标。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
