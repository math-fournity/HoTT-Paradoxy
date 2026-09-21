#!/usr/bin/env python3
"""Save the same-pair task comparison and bounded four-stage evidence audit."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260921-ASTRA-CASE-INTEGRATION';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第三十一轮执行报告.md'
NEXT='AST-U08-U09-SCOPED-REVIEW-01：制作结果式本地同行审阅包，拟选NativeTaskIntegration、NativeSourceContract、Sqrt2TaskComparison、SC00及QuotientConsumer实际入口，按所声明结果依赖确定唯一清单。保留精确假设/原文/Book定位/源run与C320操作合同区别，在不同cwd含空格路径重放核心入口，查绝对路径/缓存/隐式依赖。只认本机固定环境的重定位，不称跨平台/整仓认证。失败保留并修接线不改题；原广义现实/同任务/G02错误承诺/Weak原则基线地位保持OPEN，仅新来源、机制或自然consumer触发数学后继。不发布、不将局部审阅包或候选关闭冒充父六义务完成。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('DEEPENED','回父六义务逐项审，不由局部核PASS定义总成功。'),
2:('DEEPENED','C320固定同对/不同合同，Book具体规则与被归因承诺分开。'),
3:('CORRECTED','同对象不足以连接不同Step/Done；实际拒绝跨合同转换。'),
4:('ALIGNED','反证对象必须是被实际许诺的命题，不能省掉操作前提。'),
5:('ALIGNED','候选先按证据分类，未命中不提前归因也不称全理论安全。'),
6:('ALIGNED','曲线时间/环境步骤与物理过程不同，不能只用稠密性包办。'),
7:('DEEPENED','Book原文、实际类型/核、冻结索引逐源对照，不凭AI多数。'),
8:('DEEPENED','圆环启发导出同一对对象的实际正负操作比较。'),
9:('ALIGNED','时间曲线允许端部移动；不偷称固定环境同胚。'),
10:('ALIGNED','现实相对目标保留，但当前尚未取得同任务失配。'),
11:('CORRECTED','原027把核检查与执行义务相联过强，正文精确降范围。'),
12:('DEEPENED','原ASK平方表/有理根与标准GOLD查询按九请求区分。'),
13:('DEEPENED','提取见证/截断/给定源运输由实际合同审，不把所有存在当Σ。'),
14:('ALIGNED','物理取得能力的越级须定位具体承诺，当前保留缺口。'),
15:('TENSION','Z方向未由四弹证据闭合；保留现实问题而撤回旧成功判词。'),
17:('ALIGNED','原典结构与实数选项直接阅读，新正构造同样受题意审查。'),
18:('ALIGNED','不由抽象表达直接认定时间被非法取消，需任务桥。'),
19:('CORRECTED','指定Pell不归零不等于所有逼近/曲线不能完成。'),
21:('DEEPENED','C320 fresh与13包资格、B1a关系、756旧行字节对账分别记。'),
22:('ALIGNED','两方向分别要求参考侧完成或错误有效交付承诺，不混。'),
23:('DEEPENED','CurveRun连续族与Ambient有限trace具体可定位。'),
24:('ALIGNED','有界元层观察不外推普遍不可停机或规范化失败。'),
27:('ALIGNED','程序/元理论归因要求精确演算，当前未新增这类定理。'),
31:('DEEPENED','HoTT内实际定义并检查两个操作类，不仅作哲学名称比较。'),
34:('ALIGNED','否定任务有项不等于整个理论否定现实；原则iff不等于独立。'),
35:('DEEPENED','Rich表达闭图而未表达所有来源历史，明确未穷尽。'),
37:('DEEPENED','原六用户文本完整复读，几何和算术没有被混成同实例。'),
38:('CORRECTED','查作者实际承诺后不再把“忽略结构”概括为原典事实。'),
39:('CORRECTED','结束已充分的辅助几何，直接比较父目标证据连接。'),
40:('DEEPENED','固定Book四文件十二段提供独立原典分类，非全知识谱认证。'),
41:('ALIGNED','有界审计完成与父Goal未完成同时记录。'),
42:('ALIGNED','旧AI和当前AI的判词都受相同核/归因门禁。'),
43:('CORRECTED','避免重复计算已闭结果，转真实审阅/复现缺口。'),
44:('ALIGNED','现实/假想现实都可研究，数学模型并不自动穷尽其操作。'),
45:('DEEPENED','找应保留的信息及实际消费者，但当前没有证明其被错误许诺。'),
46:('ALIGNED','继续以实际构造/原典主动工作，不要求用户代写桥梁。')}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_AND_RELATION_PASS_WITH_SCOPE'
    inputs=json.loads((OUT/'INPUT-VERIFICATION.json').read_text());assert not inputs['not_passed']
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==204
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();old=state['latest_session'];state['revision']=205;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'SAME_PAIR_OPERATION_CONTRACTS_AND_BOUNDED_FOUR_STAGE_AUDIT_CHECKED','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    manifest=json.loads((ROOT/delivery['primary_run']/'source-manifest.json').read_text());sources={x['path']:x['sha256'] for x in manifest['files'] if x['path'].startswith('HoTT/formal/')}
    state['records']['R-ASTRA-CASE-INTEGRATION-20260921']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / CURRENT_DEFEAT_CLAIM_NOT_ESTABLISHED','status':'same_pair_distinct_operations_and_scoped_case_verdicts','depends_on':[],'related_records':[SID,'R-ASTRA-NATIVE-MOTION-BUNDLE-20260920'],'full_sources':[REPORT,'audit/astra-case-integration-20260921/DELIVERY.json'],'source_hashes':sources,'scope':'C320 actual CurveRun nRich mRich with negative finite ambient Success and no success adapter/equivalence, nontrivial ambient control and Rich distinction. Six user texts/five plans/twelve pinned Book ranges audited; 13 prior packages qualified, not new kernel replay. Historical interpretation clarified with 756 frozen rows preserved. No exact HoTT promise of rejected same task found in checked ranges, no global no-defect theorem; broad reality/G02/principle status and full parent goal open.'}
    state['execution_control'].update(status='ACTIVE_GOAL_SCOPED_CASES_RECLASSIFIED_SCOPED_REVIEW_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 native theorem / source audit / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-case-integration-20260921/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C318/C319、1.32、revision204及a0963cc已保存
- status: SCOPED_CASES_RECLASSIFIED / CURRENT_DEFEAT_CLAIM_NOT_ESTABLISHED / PARENT_OPEN

C320新源NativeTaskIntegration。草稿1通过；fresh主run{delivery['primary_seconds']}秒、31本地/1102图/41pin，formal与关系PASS。同对曲线成功/环境失败，转换不可得；非空环境控制与Rich差别保持。原13包26资格项PASS，未重放13次核；B1a旧run04另做formal和关系检查。旧756表格行逐字/顺序保持，只澄清历史叙事标题/范围并添加C320。

同T3复认：core及32managed hash不变，前轮46KC逐条复读、KC41–46原文样本；当前原六用户文本/五方案与固定Book十二范围全文读取，四固定文件hash固定。query/plan无query_first提升；压缩复认不伪称本轮四件套重新全额输出，工具不认证理解。已加载closure/governance/verification/projectresearch/SOP，档位不变。全文旧STATE的事实沿同hash收据保留，hot/current与新增record实际检查。

策略v1.33提交{commit}。下一：{NEXT}

46KC按PROTOCOL§5完整legacy原子兼容bundle，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；公开报告六片。T01–05原意/同任务；T06–10双合同/结构/归因；T11–17源核/原典/历史行；T18–21本地审阅不发布；T22–24case判词及下一复现；T25未改AI治理；T26精确提交。共享C01–C09 NO_CHANGE，C10项目证据UPDATE。没有新增通用治理组件/validator。无Sub Agent、push/tag/公开。

element_usage：closure复认/原文；research两合同/最强反解释；SOP范围裁决与下一U08/U09；verification新核和旧资格分开；checkpoint原子；dev-notes原文归档。所有必需主张回原类型和实际收据。
'''
    core=state['current_core'];audit=f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']}条。

- core_change: NO
- direction_change: SCOPED_REVIEW_AND_RELOCATION_NEXT
- panorama_change: SAME_PAIR_TASK_COMPARISON_AND_BOUNDED_SOURCE_AUDIT
- essay_change: NO
- update_decision: 当前四弹成功判词未成立，保留精确结果并进入选定范围同行材料
- cross_conflicts: 同对象不同操作不构成P/非P；原典承诺不由旧AI自述替代
- unresolved: 广义现实/同任务/G02/原则基线地位/独立复现与父目标

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==core['kc_count']
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名自指/反射/量子化或理论经济机制未被当前两合同及原典范围检验，保持原状态。'))
        ev=('NativeTaskIntegration/C320主run、原六文本/五方案/PRIMARY-SOURCES、第三十一轮；下一选定范围重放与审阅。若同图失败、合同误录、实际错误承诺/保真桥或新原文出现则重评；不以有界未命中证明全理论安全。' if n in TOUCHED else '当前无该主题新证据；新精确规则/consumer进入依赖或原文使其成为决定性问题时再核。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001简化：裸/结构与任务区分；002时间：核检查/执行/物理不同；003圆环ASK：同对曲线/环境及不同算术请求；004自反：027元层不普遍化；005表达：Rich未穷尽来源现实；006知识谱：十二原典范围且限定负结论；007助力阻力：对旧AI/本AI同样审；008现实骨架：不放弃对应问题但不以未闭合当成功。

## 已走过的路与即将选择

C320给同pair实际正负操作合同，原文/原典回溯指出承诺与完成条件缺口，历史越级判词原位降为历史而旧行不改。候选：选定结果U08/U09真实异地重放和同行材料（直接必要，选）；继续优化几何（无新问题不选）；全库任意搜索或无限公理独立性工程（无当前具体依赖不选）；原文/consumer新机制（保留触发）。六义务不可缺，父Goal仍ACTIVE。八轴与遗漏见报告004：同对象与任务操作变化/原圆环算术/实际运输和Book/输入图与Done/可达覆盖与有效返回/native核与文献/固定库与版本。非全候选穷举，资格数不是数学完备，物理/原则独立/全理论不由C320推出。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[delivery['primary_run']],'new_math_claims':['C-320'],'new_kernel_replay':True,'validation':'audit/astra-case-integration-20260921/DELIVERY.json','existing_package_qualification':'audit/astra-case-integration-20260921/INPUT-VERIFICATION.json','parent_objective':'OPEN','case_audit':'CURRENT_FOUR_STAGE_DEFEAT_CLAIM_NOT_ESTABLISHED'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260921-'+kind+'-205'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 204$','source_state_revision: 205',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260921-'+kind+'-205',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，父六义务不改。第三十一轮C320已核同一nRich/mRich的CurveRun成功与有限Ambient Success失败及转换不可能；六原文/五方案/Book十二范围审计后，当前整体击落判词未成立，各case按范围重分类。13旧包26资格检查PASS，非13新核；旧矩阵756表行字节保持，强叙事原位标历史。原广义现实/同任务/G02/Weak原则地位继续OPEN。策略v1.33由'+commit+'保存。下一'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('DECLARED_NATIVE_GEOMETRY_CHECKED_CASE_INTEGRATION_NEXT','SCOPED_CASES_RECLASSIFIED_REVIEW_NEXT').replace('`OUT-ASTRA-NATIVE-MOTION-BUNDLE-30` |','`OUT-ASTRA-NATIVE-MOTION-BUNDLE-30`、`OUT-ASTRA-CASE-INTEGRATION-31` |').replace('声明几何/256界/同记录已核，Weak覆盖有精确条件；下一四层同任务整体审计','同对象双合同C320及原文/原典范围审计已核，整体失配未成立；下一选定范围复现/同行材料')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-CASE-INTEGRATION-31` | C320同对象双合同与原文原典范围审计 | `DIR-U-ASTRA-BREAKPOINT` | 实际CurveRun/环境否定/源文承诺/既有资格 | `FORMAL_CHECKED_WITH_SCOPE / CURRENT_DEFEAT_CLAIM_NOT_ESTABLISHED` | 同pair曲线成功而环境失败，旧强判词降历史且756表行不改 | 原广义现实/同任务/G02/原则基线与同行交付 | `'+REPORT+'`；`audit/astra-case-integration-20260921/DELIVERY.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户ACTIVE Goal及既有T3研究/集成授权；保存C320及原文原典范围审计，保留父成功标准并转选定范围本地复现/审阅。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))

if __name__=='__main__':main()
