#!/usr/bin/env python3
"""Canonical transaction for actual quotient/truncation consumers and the weak-domain successor."""
from pathlib import Path
import argparse, importlib.util, json, re, subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-QUOTIENT-CONSUMER';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第二十二轮执行报告.md'
RUN='HoTT/verification/runs/20260920-MP-ASTRA-QUOTIENT-CONSUMER-001-01'
NEXT='BP-WEAK-LIFT-PRINCIPLE-01：返回真实Dedekind圆，固定RealNonzeroApartness=∀r:Real,¬(r=0)→apart(r,0)，检验其与原Circle Lift的双向联系；复用已核参数化及显式坐标变换、保持原点/输入，先正向再反向归约。只是候选，不能把LocalStability改名当新成果或声称LEM必要/标准命名原则等价。已有noMissingInverseWitness禁止回到弱点且所有分母逆元不存在的单点反例方向。沿用资格化no-erasure配置；无条件Lift、独立性/反模型、原广义操作、必要元层/整体学术交付继续OPEN；历史Coq关系问题单列。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('DEEPENED','同一真实商的函数值/来源任务分别有完整核证。'),
2:('DEEPENED','原GOLD ℚ、Rep fiber、SquareTask和原来源左逆类型明确。'),
3:('ALIGNED','正平方与原来源否定不是同一命题的P/非P。'),
5:('ALIGNED','正恢复和精确否定都认账，不预设击落。'),
7:('ALIGNED','实际源核、两个错误项及哈希决定判断。'),
10:('ALIGNED','数学来源模型不冒充原广义现实操作。'),
11:('ALIGNED','mere/chosen与checker时间分开，没有物理耗时推论。'),
12:('DEEPENED','rec2关系和rec→Set常值性是实际资格义务。'),
13:('DEEPENED','任务Done区分平方值和每个原代表的分子。'),
14:('ALIGNED','没有从存在某代表跃迁到取得原历史代表。'),
15:('TENSION','当前有精确信息边界，却未找到HoTT作出错误来源承诺。'),
17:('ALIGNED','实际库接口检验纠正粗略的只可返回命题说法。'),
19:('NOT_TOUCHED','未推进全部稠密过程完成性，不由商例子外推。'),
21:('DEEPENED','一fresh主核、两缓存错误项、原记录及160模块图完整。'),
22:('ALIGNED','双向现实目标仍在，不把来源边界自动判成现实失配。'),
31:('DEEPENED','实际非Prop Set值消去有相称数据/正确性实例。'),
34:('DEEPENED','普遍左逆否定已证明；没有否定选某规范代表的不同合同。'),
35:('ALIGNED','真实来源字段可显式表达，但原广义用户语境仍未穷尽。'),
37:('ALIGNED','本例不代替圆环，下一回原点集弱域关键未决。'),
38:('DEEPENED','直接核商与截断的实际消费者是否越级，当前没有命中。'),
39:('DEEPENED','从真实基础商和两实际分数定位边界，不只做标签例子。'),
40:('ALIGNED','库和旧注释分别审查，不把旧强判词作为理论保证。'),
41:('ALIGNED','五项完成不等于完整四弹目标完成。'),
42:('ALIGNED','同任务值恢复成功保留，来源输入增加也准确记载。'),
43:('DEEPENED','实际商链闭合后返回几何弱Lift，不继续同形准备。'),
44:('ALIGNED','来源的数学比方有明确输入，未自证全部现实对应。'),
45:('DEEPENED','量化区分保留值与保留原来源，消费者需要字段已实证。'),
46:('ALIGNED','原对象、实际代码和现实解释边界一起保存。')}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_AND_RELATION_PASS_TWO_CONTROLS_RECONCILED'
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==195
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    prior=json.loads((ROOT/'audit/astra-s1-consumer-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
    (OUT/'RESUME.json').write_bytes(R.dump({'policy':'Same-T3 PROTOCOL v3 receipt reattestation, not new full emission','revision':195,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint195; all32 tracked hashes verified','kc_stance_revisited':'All46 revisited against real rational quotient and provenance tasks; prior samples retained','model_understanding':'NOT_CERTIFIED_BY_TOOL','objective':'完成四弹一体的redo','app_goal_status_observed':'active'}))
    plan=R.plan(ROOT,profile='research',task_ids=['R-ASTRA-S1-CONSUMER-20260920']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    old=state['latest_session'];state['revision']=196;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C305_C306_ACTUAL_QUOTIENT_AND_TRUNCATION_CONSUMER','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    manifest=json.loads((ROOT/RUN/'source-manifest.json').read_text())
    state['records']['R-ASTRA-QUOTIENT-CONSUMER-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / VALUE_AND_ORIGINAL_SOURCE_TASKS_SEPARATED','status':'five_obligations_checked_original_weak_domain_next','depends_on':[],'related_records':[SID,'R-ASTRA-S1-CONSUMER-20260920'],'full_sources':[REPORT,'HoTT/formal/astra-quotient-consumer/QuotientConsumer.agda','audit/astra-quotient-20260920/DELIVERY.json','audit/astra-quotient-20260920/NEXT-SOURCES.json'],'source_hashes':{f['path']:f['sha256'] for f in manifest['files'] if f['path'].endswith(('.agda','TOOLCHAIN.json'))},'scope':'Same GOLD rational quotient. Actual arithmetic/GOLD invariance and rec→Set square recovery with constancy/Done; precise original-numerator/fraction left-inverse and mere-origin contracts refuted; chosen-source Rich distinction. Two fixed incorrect terms rejected. No canonical-representative impossibility, physical mismatch or full four-stage closure.'}
    state['execution_control'].update(status='ACTIVE_GOAL_QUOTIENT_CHAIN_CHECKED_WEAK_PRINCIPLE_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-quotient-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C304/六控制、revision195与523a8f2有实据
- status: ACTUAL_QUOTIENT_CHAIN_CHECKED / PARENT_OPEN

C305在原GOLD ℚ上核实际加乘/L/U保持、Rep fiber的mere代表及显式常值性rec→Set平方；返回真实SquareTask，目标ℚ非Prop。C306原分子/原分数左逆和固定Rep(1)的mere历史输出被精确否定；给定源Rich可观察，不当作从裸商恢复。两错误关系/常值项在正确位置exit42。

fresh主核59.992222秒，4本地模块/160图/41外部pin；两个控制复用同一已核接口缓存（各约2秒），1次草稿另计。主核/关系/原始诊断/hash及草稿正式图一致。未改原GOLD代码或采用旧注释强判词，无新增公设。

策略v1.24由{commit}保存。下一动作：{NEXT}

46KC legacy原子兼容bundle按PROTOCOL§5，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；报告四片。T01–05完整目标与来源合同，T06–10实际quotient/Set消去及否定量词，T11–17源核/缓存控制边界，T18–21无部署，T22–24当前归因/弱域后继，T25无AI合同变化，T26精确提交。共享C01–C09 NO_CHANGE，C10项目证据UPDATE。无Sub Agent、push/tag/发布。

element_usage：closure/收据复认、research正负/实际恢复、SOP返回几何未知、verification源核/反例、canonical事务、dev-notes。无新通用平台。
'''
    audit=f'''# {SID} 核心认知回评

core-cognition-generation-7；46条。

- core_change: NO
- direction_change: ORIGINAL_WEAK_DOMAIN_PRINCIPLE_NEXT
- panorama_change: ADD_C305_C306_QUOTIENT_CONSUMER
- essay_change: NO
- update_decision: 原ℚ商/截断五项完成，回原Circle Lift的原则强度
- cross_conflicts: 不变值恢复不恢复原历史；左逆否定不否定所有代表选择；错误项与数学否定分开
- unresolved: 原广义操作/弱域原则、必要性/元层、整体与历史Coq关系

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名时间/自指/反射问题未推进，商实例不代替它。'))
        ev=('第二十二轮001–004、C305/C306源码/主核/两控制；下一原弱域原则。若换Q、隐去常值性/原q输入、把左逆改成右逆或夸大现实归因，撤回相应结论；真实保任务反例可重评。' if n in TOUCHED else '第二十二轮004未触达；具名机制实际进入当前依赖或用户新原文时重开。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001问题/简化：值与来源任务具体分开；002前提/时间：mere/chosen不混外部耗时；003圆环/ASK：原代表需要哪些信息被明确量化；004HoTT/自反：一般选择/自验证未由此解决；005表达/原文：Rich是来源模型，不冒充全部原语境；006知识谱：实际rec→Set条件检验，不用粗略口号；007助力/阻力：正值恢复和否定历史都认账，转原几何未知；008现实骨架：具体来源解释有输入界限，未自证广义现实。

## 已走过的路与即将选择

五项各有源核或固定项诊断，实际GOLD/有理数链与常值Set消去相连。原始历史合同失败不证明HoTT许诺它；当前不是缺陷命中。下一原Circle Lift与RealNonzeroApartness候选的双向坐标归约，不能只是LocalStability改名。已有noMissingInverseWitness认账，不重复单点无逆元反例。八轴、遗漏/独立对照与停止见第二十二轮004；父目标OPEN。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[RUN],'control_runs':[r['run'] for r in delivery['controls']],'claim_ids':['C-305','C-306'],'validation':'audit/astra-quotient-20260920/DELIVERY.json','formal_kernel_runs':3,'draft_checks':1,'parent_objective':'OPEN'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-196'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 195$','source_state_revision: 196',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-196',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C305/C306已接原GOLD有理商：实际算术/谓词保持、常值rec→Set返回平方及Done、原分子/分数左逆精确否定、给定来源Rich；两个错误消去项准确拒绝。主核160模块/41pin，两个控制缓存边界明确。没有取得HoTT错误来源承诺。策略v1.24由'+commit+'保存。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('S1_CHAIN_QUALIFIED_QUOTIENT_CONSUMER_NEXT','QUOTIENT_CHAIN_CHECKED_WEAK_PRINCIPLE_NEXT').replace('`OUT-ASTRA-S1-CONSUMER-21` |','`OUT-ASTRA-S1-CONSUMER-21`、`OUT-ASTRA-QUOTIENT-CONSUMER-22` |').replace('S1实际六成员已核；下一同GOLD商/截断数据消费；原广义及整体开放','商/截断五项已核；下一原Circle弱域原则归约；原广义及整体开放')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-QUOTIENT-CONSUMER-22` | C305/C306原GOLD商与截断数据链 | `DIR-U-ASTRA-BREAKPOINT` | 原生核/实际源消费者/两错误控制 | `FORMAL_CHECKED_WITH_SCOPE / VALUE_SOURCE_TASKS_SEPARATED` | 不变平方交付与原历史左逆否定、给定来源控制 | 原弱域原则/广义操作、必要元层/整体 | `'+REPORT+'`；`audit/astra-quotient-20260920/DELIVERY.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['R-ASTRA-S1-CONSUMER-20260920'],'authorization':'用户ACTIVE Goal及既有T3研究/集成授权；原商/截断实际五项结束回原几何弱域，完整范围保持。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))


if __name__=='__main__':main()
