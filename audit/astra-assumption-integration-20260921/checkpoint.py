#!/usr/bin/env python3
"""Save source-contract reconciliation without relabeling it a new kernel theorem."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-AUD-20260921-ASTRA-ASSUMPTION-INTEGRATION';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第三十五轮执行报告.md'
NEXT='当前原四弹范围判词与证据保存完成后不默认扩张：原强结论未建立，精确局部结果保留；新版审阅包、一般反向/最弱原则/独立性和其他消费者为可选研究。后继仅由会改变当前结论的具体同任务承诺、反例机制、证据失效、实际审阅需求或用户新任务触发。已有v1及C321–324独立source/run/report可检查，不重复旧核或资格检查来制造进展。原广义现实与六义务未完成，不将本次审计当击落或App Goal完成；Coq仅source-contract级。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('DEEPENED','回原五方案和六义务，识别还缺同任务与真实承诺。'),
2:('DEEPENED','各合同输入/观察/完成/前提分栏，静态Coq与已核Agda不同等级。'),
3:('CORRECTED','同源判据不能替同任务合取前提，C321–324未补原算术识别。'),
5:('ALIGNED','新自然消费者没有被强行归因为错误；范围内未命中不等于全局无缺陷。'),
7:('DEEPENED','原文/代码/commit/blob/本地核资格交叉，不凭AI一致或语气。'),
8:('ALIGNED','原圆环/源/操作意图保留，现模型未冒充全现实。'),
9:('ALIGNED','modulus/limit输入与实际物理时间继续分开。'),
10:('ALIGNED','当前现实相对失配未成立，不转成内部一致性证明。'),
11:('DEEPENED','检查/归约/存在/数据/物理执行分开审理。'),
12:('DEEPENED','自然消费者实际所需locator/apartness/modulus可定位。'),
13:('DEEPENED','有条件的合法见证恢复不等于从所有截断一般取值。'),
14:('ALIGNED','有效交付承诺要有具体来源，不能由对象定义自证。'),
15:('TENSION','原强胜利判词仍缺证据，保留Z研究方向而不强行认证。'),
17:('ALIGNED','实际source区分<>和≶，不凭符号习惯误读。'),
19:('CORRECTED','022/025的普遍过程否定仍受当前正构造和不同Done限制。'),
21:('DEEPENED','九包十八资格、14源身份、初次汇总失败/修复完整保留。'),
22:('ALIGNED','原双向目标保持，未答结案问题不改目标。'),
31:('ALIGNED','HoTT能表达若干Rich/Task条件的实物已存在，但非全表达性证明。'),
34:('ALIGNED','充分条件、原则必要后果和不可证性不混用。'),
35:('DEEPENED','当前模型与用户全部来源/历史/现实同一性之间仍有独立义务。'),
37:('ALIGNED','六条圆环原文重新全文读，不用新算术成功覆盖原问题。'),
38:('CORRECTED','所查自然消费者明示条件，不能概括作者未意识到结构差别。'),
39:('DEEPENED','停止无意义旧编译重复，补真实声明来源和下一交接缺口。'),
40:('DEEPENED','新增精确2020源码与论文合同对照，历史版本不当2026全库状态。'),
41:('ALIGNED','本轮审计完成不等于原目标证明完成。'),
42:('ALIGNED','旧AI和当前AI都按精确命题审，强恢复真实保留。'),
43:('CORRECTED','不让费用标签使任何结果自动命中，不沿元理论无限扩张。'),
44:('ALIGNED','理论骨架与现实对应仍要明确Task，未把源码当物理证据。'),
45:('DEEPENED','实际消费者的观察/输入前提成为归因证据，非抽象臆测。'),
46:('ALIGNED','主动查原始实现并落索引，未要求用户代证明。')}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    inputs=json.loads((OUT/'INPUT-VERIFICATION.json').read_text());assert inputs['status']=='SCOPED_EVIDENCE_QUALIFICATION_AND_SOURCE_IDENTITY_PASS'
    audit_check=json.loads((OUT/'AUDIT-VERIFICATION.json').read_text());assert audit_check['status']=='AUDIT_SOURCE_IDENTITY_LOCATORS_AND_LINKS_PASS'
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==208
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();old=state['latest_session'];state['revision']=209;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'SCOPED_ORIGINAL_ARGUMENT_AND_PRIMARY_CONSUMER_CONTRACT_AUDIT','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    snapshot=json.loads((OUT/'LOCATOR-SOURCES.json').read_text());sources={r['path']:r['sha256'] for r in snapshot['files']}
    for row in inputs['results']:
        man=json.loads((ROOT/row['run']/'source-manifest.json').read_text())
        sources.update({f['path']:f['sha256'] for f in man['files'] if f['path'].startswith('HoTT/formal/')})
    state['records']['R-ASTRA-ASSUMPTION-INTEGRATION-20260921']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'SOURCE_CONTRACT_AUDITED_NOT_COQ_REPLAY / ORIGINAL_TARGET_NOT_ESTABLISHED','status':'original_four_stages_reconciled_with_explicit_assumptions_and_primary_source_contracts','depends_on':[],'related_records':[SID,'R-ASTRA-MARKOV-REVERSE-20260921','R-ASTRA-CASE-INTEGRATION-20260921'],'full_sources':[REPORT,'audit/astra-assumption-integration-20260921/INPUT-VERIFICATION.json','audit/astra-assumption-integration-20260921/AUDIT-VERIFICATION.json'],'source_hashes':sources,'scope':'Six original user statements/five historical plans re-read and reconciled with C321–324 and existing geometry/arithmetic. Nine selected packages18qualification checks, no new kernel run/claim. Fourteen primary Coq source files at478aeef5 pinned; visible locator/apartness/modulus/LEM contexts and partial formalization distinguished. No exported-minimal-assumptions/full-library/Coq-validity certificate, no global absence, physical or four-stage target theorem.'}
    state['execution_control'].update(status='SCOPED_REDO_VERDICT_SAVED_NO_DEFAULT_EXPANSION',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 scoped source audit / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-assumption-integration-20260921/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: paused (fresh get_goal at recovery)
- current_user_instruction: 开始；本轮继续已授权工作，不伪称工具已将App Goal恢复为active
- previous_goal_turn: PROGRESS；C323/C324、策略1.36、revision208及12199179已保存
- status: SOURCE_CONTRACTS_RECONCILED_WITH_SCOPE / PARENT_OPEN

本轮无新数学claim和新kernel replay。九包十八formal/version资格PASS；六原文/五计划全文复读核hash。固定作者Coq branch locators commit478aeef5（2020-06-11）14文件共127054字节，Git blob/SHA256核验，BSD许可保留；Locator.v本地1–808全文、BoundedSearch/DProp/ExcludedMiddle/cauchy及决定性notation/field上下文读。可见locator/apartness/modulus/LEM条件明确；<>不同于≶，实数Recip用ApartZero；乘法locator在该文件Abort。未编译Coq、未PrintAssumptions/全import闭包或当2026全部版本。源声明不冒充定理。

首次验证汇总将旧JSON容器误读为sources/rows（实际files），在9包子检查成功后汇总失败；原脚本/诊断/根日志保留，改正确字段后recheck-002全通过，无数学源/收据改动。当前数学矩阵/registry没有修改。原强结论仍缺同任务/G02/G04，不由条件恢复填平。

同T3core与32managed哈希复认、46KC逐项回评，closure本轮完整加载，沿既有research/governance/verification/SOP；新的外部来源按可见范围和确切版本，非全论文重读。恢复时52文档hash与先前收据一致，抽读KC1/2和37–41原文，并逐项复认下表；工具不认证理解。历史014批注只作原文不执行。用户“开始”后追问最近redo是否过度设计，本轮确认v1.37将可选新版包无新必要性地提升为默认后继，已以v1.38收束。结案澄清未回复，原研究目的/六义务不改，但未答不授权无限扩张。策略v1.38提交{commit}。下一：{NEXT}

46KC按PROTOCOL§5 legacy原子兼容bundle，保留G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；报告六片。T01–05原意/任务；T06–10声明输入/等级；T11–17源身份/资格/失败修复；T18–21无外部发布；T22–24旧强判词限度/新版材料；T25未改AI治理；T26精确提交。共享C01–C09 NO_CHANGE，C10项目来源证据UPDATE。无Sub Agent、push/tag/外部消息或上游修改。

element_usage：closure源文和版本；research最强反解释/实际承诺；SOP回整体交付；verification资格非新核；checkpoint原子；archive完整问答。
'''
    core=state['current_core'];audit=f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']}条。

- core_change: NO
- direction_change: SCOPED_REDO_VERDICT_NO_DEFAULT_EXPANSION
- panorama_change: PRIMARY_CONSUMER_CONTRACT_AND_ORIGINAL_FOUR_STAGE_RECONCILIATION
- essay_change: NO
- update_decision: 选定声明不支持旧无条件归因；保精确定理，交付现有报告，取消新版包默认后继
- cross_conflicts: 两内部判据不等于同任务；Source/Kernel分级；未答澄清不改Goal
- unresolved: 原广义现实/G02/G04、一般反向/独立性、Coq重放/全历史与外部审阅

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==core['kc_count']
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名自指/量子化/理论经济机制未被当前来源合同审计检验，保持既有范围。'))
        ev=('原六文本/五计划、14固定源、9包18资格及第三十五轮；交付范围判词，不默认扩张。若找到同任务无条件实际承诺、被漏前提或新源/核冲突则重评；静态代码不算Coq过核，不外推全理论无风险。' if n in TOUCHED else '本轮无该机制新证据；具体原文/consumer进入依赖时再核。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001简化：任务信息不可交换；002时间：源码检查不等于执行物理；003圆环ASK：原X与算术分类分开；004自反：元全称不由局部观察推出；005表达：Rich不穷尽原意；006知识谱：实际消费者胜过猜测；007助力阻力：承认原强推论失去资格；008现实骨架：继续固定同任务与观察。

## 已走过的路与即将选择

新固定Coq来源明确其数据/关系/条件输入，并有部分形式化边界；原四层证据再次按精确命题对账。用户质疑过度设计后复核：第34轮只将新版包列为条件事项，v1.37无具体新增复现或审阅需要便升级为默认下一步，确属局部过度安排。现在仅完成已有报告和必要保存，原强论证不成立于已审范围；不以未证明必要性强行恢复旧判词，也不默认穷尽所有模型。八轴为原TheoryConstruct×假设/表示变化×四层任务×固定自然消费者×Input/Done/声明×已核/条件/未证×源文/现有核资格×固定Agda与2020Coq源码。非全库/无限候选覆盖；旧包资格PASS不等于Coq实跑或物理证据。

## SOP八项反思

1core46保持；2来自当前U07归因缺口；3静态源码明确非新核结论；4范围内未见不扩大全域否定；5自然消费者/Abort状态纳入而非忽略；6未改core原意；7策略1.38原位提交；8用户过度设计质疑促使取消无必要新版包，原策略重做与新发现分别验收。用户结案问题待答，研究目的未完成；fresh工具返回App Goal paused，本轮用户“开始”授权继续工作，不把工作恢复等同工具状态变更。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[],'new_math_claims':[],'new_kernel_replay':False,'existing_proof_qualification':'audit/astra-assumption-integration-20260921/INPUT-VERIFICATION.json','source_contract_verification':'audit/astra-assumption-integration-20260921/AUDIT-VERIFICATION.json','parent_objective':'OPEN','coq_replay':False}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260921-'+kind+'-209'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 208$','source_state_revision: 209',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260921-'+kind+'-209',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal原文为“完成四弹一体的redo”，六义务不改。恢复时工具状态paused；用户“开始”后追问最近redo是否过度设计，本轮按该指令继续并收束默认扩张，不伪称App已active。第三十五轮将C321–324接回原六用户文本/五方案，九包十八资格项通过，无新math claim/kernel replay。新增Coq作者branch commit478aeef5（2020-06-11）14源Git blob/SHA256快照；可见locator/apartness/modulus/LEM上下文明确，<>与≶不同，Recip用ApartZero，乘法locator此处Abort。未运行Coq或认证全库依赖/最小导出假设，不当2026全库现状。原四弹同任务/G02/G04归因未成立；完整物理/一般反向/独立性继续OPEN。首次汇总字段名读取错误已保留并修复，数学源不改。原v1.37无新必要性便把可选新版包变成默认后继，现以v1.38撤回该安排；结案澄清未回复不授权无限延长redo。策略v1.38由'+commit+'保存。下一'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('CONDITIONAL_MARKOV_REVERSE_CHECKED_INTEGRATION_NEXT','SCOPED_REDO_VERDICT_NO_DEFAULT_EXPANSION').replace('`OUT-ASTRA-MARKOV-REVERSE-34` |','`OUT-ASTRA-MARKOV-REVERSE-34`、`OUT-ASTRA-ASSUMPTION-INTEGRATION-35` |').replace('给定界/二元族/显式Setchoice反向已核；回四层假设与实际承诺，一般无假设反向/整体目标仍OPEN','原四层假设与固定自然消费者已对账；未获同任务错误承诺，交付范围判词并取消新版包默认后继')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-ASSUMPTION-INTEGRATION-35` | 原四层与固定Coq自然消费者合同审计 | `DIR-U-ASTRA-BREAKPOINT` | 六原文/五方案/9包18资格/14固定源码 | `SOURCE_CONTRACT_AUDITED_NOT_COQ_REPLAY / TARGET_NOT_ESTABLISHED` | 明示locator/apartness/modulus/LEM及部分形式化；条件不能冒充免费承诺 | 原G01/G02/G04/现实/外审与父目标 | `'+REPORT+'`；`audit/astra-assumption-integration-20260921/INPUT-VERIFICATION.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户“开始”和后续过度设计质疑、既有T3审计/集成授权；保存原四层和实际消费者对账，取消新版包默认后继，不修改研究目的或上游。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
