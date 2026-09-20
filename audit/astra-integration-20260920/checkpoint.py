#!/usr/bin/env python3
"""Canonical record of the same-task audit and the concrete full-motion successor."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-INTEGRATION-AUDIT';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第二十五轮执行报告.md'
NEXT='AST-U03-NATIVE-MOTION-01：按第二十五轮005片，在原生Real/RealPlane/原开区间与闭时间中重构原Lean stretch→bend→turn及同源闭公式的完整时间曲线族。明确处理末态第二坐标符号与当前mRich参数图的对齐，证明全部分母资格、初末态、联合连续、每片嵌入、闭参数内点一致/端部/纤维和所声明空间界。强域与Weak域/所需原则分别登记；不能把静态mCompletion、仅单射/连续或重呈现Run算作全F完成。可分依赖阶段，但完整范围保持，完成后回G01–G06同任务归因；原广义现实操作/错误理论承诺/学术交付仍OPEN。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('DEEPENED','六成功义务与四种实际合同逐项对账，未以局部完成替父目标。'),
2:('DEEPENED','Input/Step/Observation/Done和配置分别固定，原算术和主圆不混。'),
3:('CORRECTED','多张真收据不能跨不同任务拼成矛盾或完整失配。'),
5:('ALIGNED','先核事实再归因，未预设击落成立。'),
7:('ALIGNED','13行来源身份与8包实际核验支撑审计，AI收官措辞不自证。'),
10:('ALIGNED','广义现实目标保持，数学曲线族不冒充物理实施。'),
11:('CORRECTED','证明检查、项求值和对象过程执行分开；原027概括不能替合同。'),
12:('DEEPENED','逐个任务核完成资格，给定源重呈现不能当实际变形。'),
13:('DEEPENED','语义保持缺口定位到Step/Done及理论承诺，不只类型名称。'),
14:('ALIGNED','形式对象/条件输出不当作已完成全部现实过程。'),
15:('TENSION','已审链未提供完整错误理论承诺，强收官判词不能升级。'),
17:('CORRECTED','025/027/030的推断与其限定对账，保留有效披露且纠正越级解释。'),
19:('CORRECTED','单递推/受限操作否定不作所有稠密过程不完成。'),
21:('DEEPENED','8包formal+版本16检查全部通过；没有伪报新kernel replay。'),
22:('ALIGNED','两向现实对照仍须同输入任务，未转成仅内部矛盾目标。'),
31:('ALIGNED','已有模型实物认账，静态末态不代替完整原生时间族。'),
34:('ALIGNED','未定位承诺不等于全理论永无失配；必要性不等于严格新增前提。'),
35:('DEEPENED','原文范围与模型可表达范围逐项区分，不声称全部历史身份已编码。'),
37:('DEEPENED','下一回真实圆完整F，对源参数方向也作显式对齐。'),
38:('ALIGNED','理论风险须有实际误用/承诺，不以正确拒绝当缺陷。'),
39:('DEEPENED','主要连接缺口优先，停止支线反复深化。'),
40:('ALIGNED','原AI方案作为被审证据，来源自身的强判词不取得权威。'),
41:('ALIGNED','报告/收据数不等于完整目标，父范围保留。'),
42:('ALIGNED','正确恢复与明确限制作为反解释认账，不把每种回应都改称命中。'),
43:('CORRECTED','整体审计后选真正缺的原生时间族，避免重呈现/静态图循环。'),
44:('ALIGNED','现实或假想现实可作为模型参考，但本轮没有自证全部物理假设。'),
45:('DEEPENED','具体审省略的源/端部/操作条件是否在同任务被不当丢弃。'),
46:('ALIGNED','原文、真实代码、核与语义解释同时作为判断依据。')}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    verification=json.loads((OUT/'INPUT-VERIFICATION.json').read_text());assert verification['not_passed']==[] and verification['selected_packages']==8
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==198
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    prior=json.loads((ROOT/'audit/astra-book-scope-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
    (OUT/'RESUME.json').write_bytes(R.dump({'policy':'Same-T3 PROTOCOL v3 receipt reattestation, not new full emission','revision':198,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint198; all32 current tracked hashes verified','kc_stance_revisited':'All46 revisited against same-task integration; six direct user texts and five historical plan texts read; original core samples retained','model_understanding':'NOT_CERTIFIED_BY_TOOL','objective':'完成四弹一体的redo','app_goal_status_observed':'active'}))
    plan=R.plan(ROOT,profile='research',task_ids=['R-ASTRA-BOOK-SCOPE-20260920']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    old=state['latest_session'];state['revision']=199;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'SAME_TASK_AUDIT_AND_EIGHT_PACKAGE_REQUALIFICATION','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    source_hashes={}
    for package in verification['results']:
        manifest=json.loads((ROOT/package['run']/'source-manifest.json').read_text())
        for row in manifest['files']:
            if row['path'].startswith('HoTT/formal/') and row['path'].endswith(('.agda','.lean','TOOLCHAIN.json')):source_hashes[row['path']]=row['sha256']
    state['records']['R-ASTRA-INTEGRATION-AUDIT-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'SCOPED_EVIDENCE_QUALIFIED / SAME_TASK_INTEGRATION_OPEN','status':'six_obligations_audited_full_native_motion_next','depends_on':[],'related_records':[SID,'R-ASTRA-BOOK-SCOPE-20260920'],'full_sources':[REPORT,'audit/astra-integration-20260920/INPUT-VERIFICATION.json','audit/astra-integration-20260920/ADDITIONAL-PLAN-SOURCES.json'],'source_hashes':source_hashes,'scope':'Audit of six user texts, five historical plan/closure texts, four distinct task contracts, AST-G01–G06/U00–U09 and eight currently qualified proof packages. No new mathematical claim or kernel replay. Supplied-source reexpression does not certify the actual full time deformation; native full-motion correspondence and broader same-task/theory-claim obligations remain open.'}
    state['execution_control'].update(status='ACTIVE_GOAL_SAME_TASK_AUDITED_NATIVE_MOTION_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 scoped research audit / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-integration-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C309/C310、revision198与eb2c654实际完成
- status: SAME_TASK_INTEGRATION_NOT_YET_ESTABLISHED / PARENT_OPEN

重读六段原文及022/023/025/027/030，原文10冻结行+3补充HEAD一致文件核对；原生任务及Lean完整F/闭扩展全文复读。8包formal/版本16项全PASS，无新kernel replay。原生source/principle图并集1087模块及postulate词法候选留存，仅语法上界、非最小公理集。

G01/G04有决定性对应缺口，G02未找到当前指控的错误承诺，G03/G05不能跨R-REP/R-AMBIENT/R-CURVE/A-SQRT2合同拼接。NativeSourceContract是保持闭图的给定源重呈现；NativeCompletion是静态末态闭延拓，二者均非Lean完整时间F的已证原生翻译。Lean末态y符号与原生paramPoint需要显式对齐。原025/027强叙事与030自身未证边界对账，不伪造元定理。

策略v1.27由{commit}保存。下一动作：{NEXT}

46KC legacy原子兼容bundle按PROTOCOL§5，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；报告六片。T01–05原完整范围和实际合同，T06–10输入/操作/完成与归因，T11–17八包资格和公设边界，T18–21无部署，T22–24旧强判词/当前缺口/后继，T25不改AI治理，T26精确提交。共享C01–C09 NO_CHANGE，C10项目证据UPDATE。无Sub Agent、push/tag/发布。

element_usage：closure/收据复认、research同任务/最强反解释、SOP返回关键缺口、verification八包、canonical事务、dev-notes。没有通用框架扩张。
'''
    audit=f'''# {SID} 核心认知回评

core-cognition-generation-7；46条。

- core_change: NO
- direction_change: NATIVE_FULL_MOTION_NEXT
- panorama_change: ADD_SAME_TASK_INTEGRATION_AUDIT
- essay_change: NO
- update_decision: 六义务审计完成，补实际原生时间曲线族而非重复静态/重呈现
- cross_conflicts: 任务和前提不同不可拼接；原强判词高于其自身证据边界；八包资格不等于整体成功
- unresolved: 完整原生F/广义操作/错误理论承诺、必要元层与整体交付

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名自指/时间/反射构造未新推进，同任务审计不代替其证明。'))
        ev=('第二十五轮001–006、原六用户文本/五AI方案与8包收据；下一完整原生F。若存在已给且同任务的错误承诺/保真桥或本审计漏读关键条件，重评；若新F换模型/Step/Done则不得继承原目标身份。' if n in TOUCHED else '第二十五轮范围；该具名机制实际进入当前依赖或新直接来源出现时重开。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001问题/简化：四种合同分开；002前提/时间：检查/对象执行/数学时间参数分开；003圆环/ASK：原允许操作/端部/source必须保持；004HoTT/自反：旧哥德尔类比不作元证明；005表达/原文：六原文与AI计划身份分开，模型不穷尽原意；006知识谱：025/027/030作为被审对象；007助力/阻力：不把每个反解释都称命中，选择实际未完成F；008现实骨架：数学模型与物理/假想参考之间仍要给明确对应。

## 已走过的路与即将选择

八包当前资格全过，但六义务整体未过；主要缺口是同一任务和错误理论承诺，不由更多收据数量消除。下一原生完整F是具体G04剩余，并会按五种终局如实裁决。八轴：实际对象/等价/过程×跨合同误替×原还原/校准任务×SourceContract/Trace/F/九族×原文/类型/Done×范围验收×既有核收据与源码×三明确配置。有限来源/八包不冒充全库全历史，导入扫描不证明最小公理或一致性。原广义操作与理论归因/学术交付继续OPEN。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[r['run'] for r in verification['results']],'new_math_claims':[],'new_kernel_replay':False,'validation':'audit/astra-integration-20260920/INPUT-VERIFICATION.json','selected_packages':8,'parent_objective':'OPEN'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-199'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 198$','source_state_revision: 199',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-199',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。U07现状审计已核六原文/五AI方案与8包当前资格，区分给定源重呈现、环境Trace、实际曲线族和算术校准；G01/G04及G02错误承诺仍欠整体连接。原生静态闭图/重呈现不代替完整时间F；末态参数方向需核。无新数学claim/核重放。策略v1.27由'+commit+'保存。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('FORMULATIONS_CHECKED_CASE_INTEGRATION_NEXT','SAME_TASK_AUDITED_NATIVE_MOTION_NEXT').replace('`OUT-ASTRA-BOOK-SCOPE-24` |','`OUT-ASTRA-BOOK-SCOPE-24`、`OUT-ASTRA-INTEGRATION-AUDIT-25` |').replace('两组表述已核，跨组桥未证；下一AST-G六义务同任务集成；父范围开放','六义务审计未闭合整体；下一完整原生时间曲线族；原操作/归因开放')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-INTEGRATION-AUDIT-25` | 四层同任务六义务与八包资格审计 | `DIR-U-ASTRA-BREAKPOINT` | 原文/实际源码/已核收据/配置与索引 | `SCOPED_EVIDENCE_QUALIFIED / INTEGRATION_NOT_ESTABLISHED` | 重呈现/环境/曲线/算术合同分开，8包全过；无新定理 | 原生完整F、原广义操作/错误理论承诺/整体交付 | `'+REPORT+'`；`audit/astra-integration-20260920/INPUT-VERIFICATION.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['R-ASTRA-BOOK-SCOPE-20260920'],'authorization':'用户ACTIVE Goal及既有T3审计/集成授权；完整同任务审计后补具体原生F缺口，父标准不降低。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))


if __name__=='__main__':main()
