#!/usr/bin/env python3
"""Save represented-input and explicit-choice converse results, preserving the parent scope."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260921-ASTRA-MARKOV-REVERSE';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第三十四轮执行报告.md'
NEXT='AST-U07-ASSUMPTION-INTEGRATION-04：将C321–324实际前向/给定界/二元族/显式choice反向接回原四层和G01–G06；逐项区分无条件结果、表示数据条件、逻辑原则条件和实际能力承诺，结合已读Book及新的一手locator研究核自然消费者的输入/观察/Done。充分条件不称必需，条件恢复不称击落；不重复已闭几何/旧控制，也不把一般无选择反向或独立性默认扩大为无边界前置。旧v1审阅包保持冻结，新结果独立可审；若要新版另立源包身份。用户结案标准澄清未回复前不改变原Goal/六义务、不把默认选项当回答；此事不阻塞当前既有授权工作。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('DEEPENED','完成声明反向范围后回四层整体，不永久深化原则支线。'),
2:('DEEPENED','具体界、整列mere存在和逐精度mere存在分别建类型。'),
3:('DEEPENED','原Weak同点恢复由准确合取假设构造，未把部分前提省掉。'),
5:('ALIGNED','正恢复按其范围保存，不将任何结果都改名击落。'),
7:('DEEPENED','实际核/新源/真实诊断与一手文献分层，不由AI断言代真。'),
8:('ALIGNED','原固定圆周/最终图继续使用，没有换点或另造弱目标。'),
9:('ALIGNED','逻辑恢复没有冒充物理运动/时间实现。'),
10:('ALIGNED','现实相对失配仍需实际承诺与同任务，条件等价不是整体失败。'),
11:('DEEPENED','逐精度存在不等于持有整列，核接受也不是无限操作完成。'),
12:('DEEPENED','实际Bool检测定义与apartness的双向正确性可核。'),
13:('DEEPENED','整列截断仅向命题目标消去，合法恢复步骤明确。'),
14:('ALIGNED','类型内指定输出与物理交付分别定级。'),
15:('TENSION','仍无整体击落证明；条件正恢复不支持旧必收费判词。'),
17:('ALIGNED','未先假定choice必要，给出具体用处和不需choice的特定族。'),
19:('ALIGNED','有限每项检测与无限存在由明确Markov假设连接，不偷换。'),
21:('DEEPENED','两新源、四草稿、两修复及fresh439.51911秒正式收据保存。'),
22:('ALIGNED','原双向目标保持，用户结案标准澄清未答不擅自改Goal。'),
23:('ALIGNED','检测条件按n精确定位，无新通用终止证明。'),
31:('DEEPENED','实际界数据/Set族/截断原则在原生系统表达并过核。'),
34:('DEEPENED','非零、命中、apartness与存在的条件层次都明确。'),
35:('ALIGNED','带表示数据输入不是任意裸Dedekind输入，更非全部现实来源。'),
37:('DEEPENED','新反向接原Circle Lift/Weak图并取得指定参数，保同一点。'),
38:('ALIGNED','一手locator研究明示性质/结构区分，不声称作者未意识到。'),
39:('DEEPENED','关闭当前有界方向单元，回主目标实际承诺审计。'),
40:('ALIGNED','新原始文献按已读范围使用，不把搜索二手结果当理论证明。'),
41:('ALIGNED','两个claim完成不自动完成父六义务。'),
42:('ALIGNED','当前AI的条件结果也受不越级纪律，保留强恢复。'),
43:('DEEPENED','不靠反复变更假设或扩大独立性工程延续熟悉路线。'),
44:('ALIGNED','形式数据供给和现实可操作性的对应仍需单独审查。'),
45:('DEEPENED','理论省略何种信息已可定位，但实际错误承诺仍未证。'),
46:('ALIGNED','继续实际证明和审计；结案偏好问题不要求用户代替技术工作。')}
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_AND_RELATION_PASS_WITH_SCOPE'
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==207
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();old=state['latest_session'];state['revision']=208;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'DATA_SENSITIVE_MARKOV_REVERSE_AND_EXPLICIT_COUNTABLE_CHOICE_EQUIVALENCES_CHECKED','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    manifest=json.loads((ROOT/delivery['primary_run']/'source-manifest.json').read_text());sources={f['path']:f['sha256'] for f in manifest['files'] if f['path'].startswith('HoTT/formal/')}
    state['records']['R-ASTRA-MARKOV-REVERSE-20260921']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / DATA_SENSITIVE_AND_CHOICE_CONDITIONAL_CONVERSES','status':'supplied_bounds_binary_subfamily_and_explicit_choice_recovery','depends_on':[],'related_records':[SID,'R-ASTRA-WEAK-COVERAGE-MARKOV-20260921','R-ASTRA-CASE-INTEGRATION-20260921'],'full_sources':[REPORT,'audit/astra-markov-reverse-20260921/DELIVERY.json','audit/astra-markov-reverse-20260921/SOURCE-AUDIT.md'],'source_hashes':sources,'scope':'C323: actual rational-bound Boolean detection iff apartness, Markov with chosen/mere sequence gives nonzero-to-apartness, rational zero/one controls; actual C321 binary-real restricted principle iff Markov without choice. C324: explicit level-ACℕ lzero supplies mere full sequences from pointwise location; under that argument RNZA/original Weak coverage/uniform inverse iff BookMarkov and chosen original Weak output from both hypotheses. No global principle instance, arbitrary-Dedekind unconditional converse, necessity/independence, physical/HoTT false promise or full target claim.'}
    state['execution_control'].update(status='ACTIVE_GOAL_CONDITIONAL_MARKOV_REVERSE_CHECKED_INTEGRATION_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 native conditional converse / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-markov-reverse-20260921/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C321/C322、策略1.35、revision207及eba806f已保存
- status: DATA_SENSITIVE_AND_CHOICE_CONDITIONAL_CONVERSES_CHECKED / PARENT_OPEN

C323/C324两新源MarkovRationalBounds与MarkovCountableChoice。四草稿：001缺有理群is-section导入，002通过；003Set名称歧义，004限定foundation.sets.Set通过；原命题/前提不改。fresh主run{delivery['primary_seconds']}秒、34本地/1108图/41pin，formal关系PASS，图与004字节一致。给定界序列的实际Bool测试iffapart，传入Markov完成恢复，有理零/一控制；二元编码族iffMarkov不需choice。显式level-ACℕ0供给整列mere界，得到任意原Real/原Weak图/逆元的条件等价与指定参数输出。没有原则全局实例、choice必要或无条件任意实数反向。

同T3core/32managed哈希复认，当前46KC逐条回评；实际全文读固定库三个表示/choice模块，其他有理/Set接口按符号读；外部原始Booij/作者ASD索引/Moschovakis各按有限已读范围记录，不称全文/基线独立。closure本轮全文，沿已加载research/verification/governance/SOP，档位未变；工具不认证理解。未修改core。

用户结案标准已通过本线程async问询，未收到回复；原Goal与六义务不改，默认选项不是回答，不作为当前工作阻塞。策略v1.36提交{commit}。下一：{NEXT}

46KC按PROTOCOL§5完整legacy原子兼容bundle，保留G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；报告五片。T01–05原任务/澄清未决；T06–10三层数据/Set族/条件恢复；T11–17源核/失败修复/外部来源限度；T18–21未发布；T22–24有界单元完成/回整体；T25未改AI治理；T26精确提交。共享C01–C09 NO_CHANGE，C10项目证据UPDATE。无Sub Agent、push/tag/外部消息，旧v1包不改。

element_usage：closure具体接口/来源；research强恢复与同任务；SOP回整体；verification真核及条件；checkpoint事务；archive问答。无新通用平台。
'''
    core=state['current_core'];audit=f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']}条。

- core_change: NO
- direction_change: RETURN_FOUR_STAGE_ASSUMPTION_INTEGRATION
- panorama_change: DATA_SENSITIVE_AND_EXPLICIT_CHOICE_MARKOV_REVERSE
- essay_change: NO
- update_decision: 声明反向单元完成，回实际能力承诺与整体范围
- cross_conflicts: 逐精度mere不是整列；充分choice不等于必需；澄清未答不改目标
- unresolved: 无假设一般反向/原则基线、原现实/G02/外部审阅/结案偏好

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==core['kc_count']
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名自指/反射/量子化/理论经济机制未被当前表示数据和条件反向检验，保持原范围。'))
        ev=('两新源/C323–324主run、SOURCE-AUDIT和第三十四轮；下一四层假设/实际承诺审计。若未披露的数据/选择、错Set层、截断越用、换点或核失败则重评；若发现相同任务的真实错误承诺则重开对应归因。' if n in TOUCHED else '无该主题新增数学证据；精确来源/consumer进入当前任务时再核。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001简化：性质/结构/供给分层；002时间：条件程序不冒充物理执行；003圆环ASK：回原Weak点与图；004自反：没有元独立结论；005表达：带数据域和裸域分开；006知识谱：一手文献按已读范围；007助力阻力：不把强恢复改名胜利；008现实骨架：回输入/观察/Done的对应。

## 已走过的路与即将选择

实际界数据检测及Markov恢复已核；二元族无choice等价；Set族可数选择给全Real/原Weak的条件正恢复。下一选父四层假设集成，因G02实际承诺仍决定原目标；不自动追最弱公理/全库独立，也不重复几何/旧运行。Goal澄清未答，既有目标不变。八轴：Dedekind/截断/Markov/Setchoice×数据供给×原Weak任务×有理检测和原最终图×符号/同点输出×条件恢复与等价×原生核/原始文献×固定库。非全候选穷举；零/一实际控制非采样代定理；无选择一般反向及基线地位仍OPEN。

## SOP八项反思

1core46保持且未把数学数据当全部现实；2原Weak反向欠账；3代码核验而非AI裁真；4条件正恢复不扩大失败；5一手locator研究为有限独立对照，不推全理论；6无新core原意；7策略1.36原位提交；8完成当前必要深度后回主链，澄清不停止既有工作。证据为源/run/来源/报告，学术影响未自封。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[delivery['primary_run']],'new_math_claims':['C-323','C-324'],'new_kernel_replay':True,'validation':'audit/astra-markov-reverse-20260921/DELIVERY.json','parent_objective':'OPEN','principle_scope':'DATA_SENSITIVE_AND_CHOICE_CONDITIONAL_NOT_NECESSITY'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260921-'+kind+'-208'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 207$','source_state_revision: 208',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260921-'+kind+'-208',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，六义务不改。第三十四轮C323/C324已核给定有理界序列的实际Bool检测/apartness关系与Markov恢复、有理零/一控制，及C321二元族无choice的Markov等价；显式level-ACℕ0供给整列mere界，给当前全Real/原完整Weak覆盖/逆元的条件等价和同点指定输出。fresh439.51911秒、34本地/1108图/41pin，formal关系PASS；两草稿导入/名称修复保持原命题。不称choice必要、一般无假设反向、独立性或整体失配；旧v1包不改。结案标准async问题未回复，不据默认选项更改Goal。策略v1.36由'+commit+'保存。下一'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('WEAK_MARKOV_FORWARD_CHECKED_CONVERSE_NEXT','CONDITIONAL_MARKOV_REVERSE_CHECKED_INTEGRATION_NEXT').replace('`OUT-ASTRA-WEAK-MARKOV-33` |','`OUT-ASTRA-WEAK-MARKOV-33`、`OUT-ASTRA-MARKOV-REVERSE-34` |').replace('原Weak覆盖经实际二元cut推出Markov已核；下一审反向表示数据，独立性/整体失配未证','给定界/二元族/显式Setchoice反向已核；回四层假设与实际承诺，一般无假设反向/整体目标仍OPEN')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-MARKOV-REVERSE-34` | C323/C324表示数据与可数选择条件反向 | `DIR-U-ASTRA-BREAKPOINT` | 实际有理检测/Set族/合法截断消去/原图恢复 | `FORMAL_CHECKED_WITH_SCOPE / CONDITIONAL_MARKOV_CONVERSES` | 给定界Markov恢复、二元族等价、显式ACℕ0下原Weak等价及指定输出 | 一般无假设反向/必要独立/G02/原现实与父目标 | `'+REPORT+'`；`audit/astra-markov-reverse-20260921/DELIVERY.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户ACTIVE Goal及既有T3研究/集成授权；保存声明反向范围并回四层整体；结案澄清未答不改变原目标。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
