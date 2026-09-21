#!/usr/bin/env python3
"""Save verified local review delivery without changing any mathematical claim."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260921-ASTRA-SCOPED-REVIEW';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第三十二轮执行报告.md'
NEXT='AST-U05-WEAK-DOMAIN-PRINCIPLE-01：针对原Weak去点域尚未闭合的具体义务，以固定Book实数—二元Markov练习和版本库为来源，先定位精确可复用方向，再尝试在同一原生基线把固定末态Weak覆盖/Lift/RNZA接到二元Markov。固定实际实数、输入、观察/返回、量词和截断层次；只交付过核方向或精确失败/OPEN，不把练习引用当证明，不把原则iff当基线独立/额外公理必需或HoTT失败。先最小有界桥，不做无边界全库独立性工程；若无保任务影响则停止该支回G01/G02。五入口审阅包/独立位置重放已经完成，不重复；原广义现实、实际错误能力承诺、外部同行及父六义务仍保持。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','把当前数学结果交给可复核材料，父六义务未用包数量替代。'),
2:('DEEPENED','两套演算/库及精确选项分开打包和实际运行。'),
5:('ALIGNED','仍按局部结果定级，复现成功不先归因HoTT错误。'),
7:('DEEPENED','脱离旧目录/缓存用实际编译器重放，不由AI记忆自证。'),
10:('ALIGNED','本地运行可复现不等于原现实相对失配。'),
11:('ALIGNED','核检查完成和物理过程完成继续分层。'),
12:('ALIGNED','结果说明把查询false、任务无解和拒绝错误项分开。'),
13:('ALIGNED','给定源/截断输入/合法观察在同行说明中显式保留。'),
14:('ALIGNED','交付的是证明材料，不声称物理能力由文件获得。'),
15:('TENSION','整体击落未成立的判词保留，当前只关闭复现缺口。'),
17:('ALIGNED','固定源hash与原图核验，不通过改假设或换代码取得PASS。'),
21:('DEEPENED','五实际正运行、四原类型控制、两前置完整性控制及原始收据落盘。'),
22:('ALIGNED','原双向现实目标与外部审阅义务都没有由本包取消。'),
31:('ALIGNED','本轮未新增理论表达，只保存原生已核构造及条件。'),
34:('ALIGNED','新后继仅精确原则方向，不把必要关系当已证独立。'),
35:('ALIGNED','Rich/CurveRun和广义创造历史的边界在结果稿中明确。'),
37:('ALIGNED','圆环实际源先于学术叙事，原数学代码不改。'),
38:('ALIGNED','类型控制的具体诊断不提升为作者理论普遍失败。'),
39:('DEEPENED','完成真正不同位置重放，避免只增加旧目录重复编译。'),
40:('ALIGNED','Book固定范围和当前库来源都可取得，未称全知识谱综述。'),
41:('ALIGNED','局部交付完成与父Goal未完成同时记录。'),
42:('ALIGNED','审阅者可从定义/类型反驳当前AI，无需接受历史胜利判词。'),
43:('DEEPENED','下一由原Weak域具体缺口驱动，不再无止境打磨几何/包装。'),
44:('ALIGNED','现实/假想现实仍需保真对应，独立目录不是独立现实证据。'),
45:('ALIGNED','Weak信息条件是具体保真缺口，下一只核相称原则桥。'),
46:('ALIGNED','主动交付可运行输入，未要求用户替代证明工作。')}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    verification=json.loads((OUT/'REPLAY-VERIFICATION.json').read_text());assert verification['status']=='SCOPED_RELOCATION_PASS'
    assert len(verification['cases'])==9 and sum(r['exit_code']==0 for r in verification['cases'])==5
    assert json.loads((OUT/'INTEGRITY-CONTROLS.json').read_text())['status']=='TWO_PRECHECK_CONTROLS_PASS'
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==205
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    plan=R.plan(ROOT,profile='research',task_ids=['A-ASTRA-CONTINUING-GOAL-20260919']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();old=state['latest_session'];state['revision']=206;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'SCOPED_REVIEW_PACKAGE_AND_ACTUAL_RELOCATION_REPLAY_CHECKED','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    manifest=json.loads((ROOT/verification['run']/'bundle-manifest.json').read_text());sources={r['path']:r['sha256'] for r in manifest['source_rows']}
    state['records']['R-ASTRA-SCOPED-REVIEW-20260921']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'EXISTING_PROOFS_REPLAYED_IN_RELOCATED_FRESH_ENVIRONMENT_WITH_SCOPE','status':'five_positive_four_type_controls_and_two_integrity_controls','depends_on':[],'related_records':[SID,'R-ASTRA-CASE-INTEGRATION-20260921'],'full_sources':[REPORT,'HoTT/review/four-stage-redo-v1/README.md','HoTT/review/four-stage-redo-v1/RESULTS.md','HoTT/review/four-stage-redo-v1/REPRODUCE.md','HoTT/review/four-stage-redo-v1/SOURCES.md','audit/astra-review-20260921/REPLAY-VERIFICATION.json'],'source_hashes':sources,'scope':'No new mathematical claim. Fixed local review archive and actual five positive/four frozen negative-control replays from independent paths containing spaces, new runtime data, ignored interfaces. Five named dependency graphs match originals;36primitive source hashes match per case, inputs unchanged. Wrong compiler and missing source fail precheck. Same macOS arm64 machine; no external peer review/publication, OS isolation/global scope or four-stage target certificate.'}
    state['execution_control'].update(status='ACTIVE_GOAL_SCOPED_REVIEW_REPLAYED_WEAK_DOMAIN_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 existing proof replay / local review / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-review-20260921/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C320/原典审计、策略1.33、revision205及9c33e1c已保存
- status: SCOPED_REVIEW_REPLAYED / PARENT_OPEN

五真实入口、四原错误项、两前置完整性控制均在各自判据通过。源包4407文件/53本地证明源/两套固定库/13,966,072字节，编译器另供且hash核验。从实际tar解至含空格目录，由/Volumes/D启动；每case独立work/runtime/库登记，36基础源hash、初始无接口、ignore-interfaces/no-default-libraries，五正具名图一致。所有源字节保持，Observed Checking路径无逸出；不是OS文件访问追踪或沙箱。实际补充run在{verification['run']}，原主run和claim矩阵不改。全9项无超时，2前置错误在调用核前拒绝。

同T3复认：core/32managed hash保持，沿前轮全46KC立场和当前任务重新逐条复认；原典/源类型按既有哈希证据使用，不声称又全文加载整个Book。当前库/参数/原manifest/Git源实际核。closure/governance/verification及执行SOP本轮完整加载，research原skill沿同hash保持；工具不认证理解。当前父六义务复核，下一不把包交付当原目标完成。

策略v1.34提交{commit}；下一：{NEXT}

46KC按PROTOCOL§5 legacy原子兼容bundle；G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；报告四片。T01–05范围及读者入口；T06–10现有命题不变/固定导出；T11–17源码/依赖/运行/完整性；T18–21本地交付未发布；T22–24精确current路由与Weak后继；T25未改AI治理；T26精确提交。共享C01–C09 NO_CHANGE；项目资产路由/证据更新，不新增通用validator或治理策略。无Sub Agent、push/tag/外部消息。

element_usage：closure源身份；research不越题意；SOP反思Weak后继；verification实际重放/图/源；checkpoint原子；archive原文。没有用文件数量或耗时证明数学意义。
'''
    core=state['current_core'];audit=f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']}条。

- core_change: NO
- direction_change: WEAK_DOMAIN_PRINCIPLE_BRIDGE_NEXT
- panorama_change: ADD_ACTUAL_SCOPED_REVIEW_RELOCATION
- essay_change: NO
- update_decision: 本地选定交付已可重放，回原Weak域的具体原则义务
- cross_conflicts: 重定位不是另一机器；固定错误项拒绝不是全称no-go；包完成不等于父目标
- unresolved: 原广义现实/G02/Weak原则基线/外部同行

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==core['kc_count']
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','本单元重放与本地审阅没有检验该具名时间/自指/量子化/理论经济机制；前轮立场保留。'))
        ev=('源包/九实际RUN/REPLAY-VERIFICATION/两完整性控制及第三十二轮；下一原Weak原则桥。若源/选项/图不一致、其他机器失败或原任务归因证据出现则重评；未公开不推专家认可。' if n in TOUCHED else '未新增该机制的数学证据；精确新consumer或原文使其进入当前主任务时再核。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001简化：说明具体类型而非判词；002时间：核耗时非数学运动；003圆环ASK：Strong/Weak及九请求明确；004自反：无新元定理；005表达：未穷尽原来源现实；006知识谱：精确库/Book可取得，非全面综述；007助力阻力：不同目录真核不靠旧PASS；008现实骨架：后继从Weak输入信息缺口出发。

## 已走过的路与即将选择

已交付五真入口/四原错误项的冻结源包和实际新目录重放、两个完整性对照。候选：原Weak/RNZA—Markov具体方向桥（原未决实际相关，选）；更多平台/英文润色/包美化（当前授权验收不需，无新风险暂不做）；重复几何/旧控制（不选）；新G02实际consumer（新来源触发）。原广义现实/G02未改，父Goal保持。分母5+4+2；八轴为原理论构造×原样重定位×数学交接任务×原核消费者×类型接受/诊断/图/字节×有限运行与全称定理区分×实际Agda与完整性脚本×固定macOS/两配置。无候选空间穷举，无跨平台/OS隔离认证。下一必要性桥不能冒充基线独立或击落。

## SOP八项反思

1原46KC分母不变，未以目录隔离替现实骨架；2执行当前U08/U09验收，不自由生成新候选；3脚本只封装/核哈希，数学由原生Agda，解释仍可外审；4零额外失败不是全理论安全；5未观察信封外新数学机制，原Weak原则义务仍可检；6无core新generation；7当前方案已由1.34原位写回；8完成复现后回Weak同任务问题，不停在包装惯性。证据均为本轮包/run/report，不用AI一致票数。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[],'supplemental_replay_runs':[verification['run']],'new_math_claims':[],'new_kernel_replay':True,'validation':'audit/astra-review-20260921/REPLAY-VERIFICATION.json','parent_objective':'OPEN','local_review':'SCOPED_PACKAGE_AND_ACTUAL_RELOCATION_CHECKED'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260921-'+kind+'-206'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 205$','source_state_revision: 206',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260921-'+kind+'-206',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，父六义务不改。第三十二轮完成本地选定审阅包及真实独立位置重放：五正入口exit0/具名图一致，四类型控制预期exit42/诊断匹配，两个输入完整性实例在核运行前拒绝；源字节/36基础源hash保持，含空格目录/新XDG/忽略接口。53本地源/两套库/13,966,072字节包，未外部审稿或公开，不称跨平台/整体击落。原C320及第三十一轮判词保持。策略v1.34由'+commit+'保存。下一'+NEXT+' 入口：`'+REPORT+'`与`HoTT/review/four-stage-redo-v1/README.md`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('SCOPED_CASES_RECLASSIFIED_REVIEW_NEXT','SCOPED_REVIEW_REPLAYED_WEAK_DOMAIN_NEXT').replace('`OUT-ASTRA-CASE-INTEGRATION-31` |','`OUT-ASTRA-CASE-INTEGRATION-31`、`OUT-ASTRA-SCOPED-REVIEW-32` |').replace('同对象双合同C320及原文/原典范围审计已核，整体失配未成立；下一选定范围复现/同行材料','选定本地审阅包5正4控制重定位及2完整性检查完成；整体失配未成立，下一原Weak域原则桥')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-SCOPED-REVIEW-32` | 四弹选定范围本地审阅与实际重定位 | `DIR-U-ASTRA-BREAKPOINT` | 原源/两库/新目录和数据/5正4错误项/2完整性控制 | `SCOPED_RELOCATION_PASS / NO_NEW_MATH_CLAIM` | 五正图一致、错误项按诊断拒绝，源字节和36基础pin保持 | 原Weak/G02/现实、另一机器/外部审稿/父目标 | `'+REPORT+'`；`audit/astra-review-20260921/REPLAY-VERIFICATION.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['A-ASTRA-CONTINUING-GOAL-20260919'],'authorization':'用户ACTIVE Goal及既有T3研究/集成授权；保存选定范围实际复现和本地审阅材料，原父标准不变，下一回原Weak域原则义务。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
