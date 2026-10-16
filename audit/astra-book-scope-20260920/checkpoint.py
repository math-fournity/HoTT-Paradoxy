#!/usr/bin/env python3
"""Canonical update for two exact principle translations and return to case integration."""
from pathlib import Path
import argparse,importlib.util,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-BOOK-SCOPE';BASE='.codex/research/hott/sessions/'+SID+'/'
REPORT='Astra继续尝试/断点与证明机制系统检查/第二十四轮执行报告.md'
RUN='HoTT/verification/runs/20260920-MP-ASTRA-REAL-PRINCIPLE-SCOPE-001-01'
NEXT='AST-U07-INTEGRATION-AUDIT-01：按第二十四轮003片及原AST-G01–G06/U00–U09，绑定原文→同X输入/操作/观察/Done→实际源码/核→保任务恢复→理论归因。主圆与算术校准无保真归约不互替；重点核NativeSourceContract的给定源重呈现与真实几何形变是否同任务，原Rich/Bare/Step/Done、经典Lean完整F与直接原生/条件弱域各自范围。依真实缺口选择剩余具体证明/学术交付，不以小包通过替全目标，也不无限展开所有Markov理论。缺现实操作定义保留具体分歧，未有完整失配则Goal OPEN；原未决原则与历史Coq关系问题保留。'
sp=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(sp);sp.loader.exec_module(R)
TOUCHED={
1:('ALIGNED','两组翻译完成后返回同一X的完整六义务审计。'),
2:('DEEPENED','实数零点/全点对与二进制两个公式分别有精确类型。'),
3:('DEEPENED','两个分别成立的↔没有自动给出跨组桥。'),
5:('ALIGNED','不因新翻译过核预设四弹成功。'),
7:('ALIGNED','真实核/源码及来源定位决定状态，不依AI相似性判断。'),
10:('ALIGNED','原广义现实任务未被公式规范化替换。'),
11:('ALIGNED','mere存在没有被改写成现实时间搜索保证。'),
12:('DEEPENED','输出资格保留命题性存在及假设原则输入。'),
13:('ALIGNED','真假反转保留全部输入和结论形式，不偷换chosen见证。'),
14:('ALIGNED','翻译函数不意味着无条件取得任一原则。'),
15:('TENSION','当前未建立错误理论承诺或自我否定，原目标仍需实证。'),
17:('ALIGNED','原典已讨论的区别不被包装成盲点；来源陈述未越级。'),
19:('NOT_TOUCHED','未研究一般稠密过程完成性，不能由逻辑表述推它。'),
21:('DEEPENED','6本地模块/1079图/41pin，230秒fresh核与关系检查留存。'),
22:('ALIGNED','两向现实目标保持；同一任务的实际连接回到下一主项。'),
31:('DEEPENED','原模型差运算、实际Markov定义被直接消费。'),
34:('ALIGNED','未证实数/二进制桥不被说成不存在，独立性未推断。'),
35:('ALIGNED','本模型对应式不冒充原典所有实数/宇宙的整体解释。'),
37:('ALIGNED','下一回原圆同任务集成，不让逻辑支线替原几何。'),
38:('ALIGNED','对理论缺陷的归因仍须具体原承诺，不能只凭差别存在。'),
39:('ALIGNED','基础公式清楚后检查主要职责连接，不继续仅磨局部。'),
40:('DEEPENED','Book/库/本模型各自有来源和作用域，名称不能代替桥。'),
41:('ALIGNED','两新claim不等于完整研究目标，范围不缩水。'),
42:('ALIGNED','合法恢复和公开前提的反解释保留。'),
43:('CORRECTED','有界原典核对结束，返回六义务整体，避免Markov支线无限扩张。'),
44:('ALIGNED','重呈现与物理形变的解释差异明确留给主任务核对。'),
45:('DEEPENED','检验原Input/Step/Done是否真保持同一现实任务，不能拿给定源恒等图替形变。'),
46:('ALIGNED','实际源核/原文/消费者共同作为下一集成依据。')}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_AND_RELATION_PASS_WITH_SCOPE'
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==197
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    prior=json.loads((ROOT/'audit/astra-weak-principle-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
    (OUT/'RESUME.json').write_bytes(R.dump({'policy':'Same-T3 PROTOCOL v3 receipt reattestation, not new full emission','revision':197,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint197; all32 current tracked hashes verified','kc_stance_revisited':'All46 revisited against formula translation and full-case return; prior original source samples retained','model_understanding':'NOT_CERTIFIED_BY_TOOL','objective':'完成四弹一体的redo','app_goal_status_observed':'active'}))
    plan=R.plan(ROOT,profile='research',task_ids=['R-ASTRA-WEAK-PRINCIPLE-20260920']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    old=state['latest_session'];state['revision']=198;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C309_C310_EXACT_PRINCIPLE_FORMULATION_TRANSLATIONS','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    manifest=json.loads((ROOT/RUN/'source-manifest.json').read_text())
    state['records']['R-ASTRA-BOOK-SCOPE-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / TWO_TRANSLATIONS_BRIDGE_OPEN','status':'source_scope_unit_complete_case_integration_audit_next','depends_on':[],'related_records':[SID,'R-ASTRA-WEAK-PRINCIPLE-20260920'],'full_sources':[REPORT,'HoTT/formal/agda-unimath/hott-z/RealPrincipleBookScope.agda','HoTT/formal/agda-unimath/hott-z/MarkovBookForms.agda','audit/astra-book-scope-20260920/DELIVERY.json','audit/astra-book-scope-20260920/INTEGRATION-PREFLIGHT.json'],'source_hashes':{f['path']:f['sha256'] for f in manifest['files'] if f['path'].endswith(('.agda','TOOLCHAIN.json'))},'scope':'C309 real zero/pair apartness formula translation on original Real0 and Circle Lift/inverse linkage. C310 exact Book/library binary Markov translation with truncated existence. No cross-group real/binary bridge, unconditional principle or full Book interpretation. Return to full same-task integration audit.'}
    state['execution_control'].update(status='ACTIVE_GOAL_FORMULATIONS_CHECKED_CASE_INTEGRATION_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-book-scope-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；C307/C308、revision197与5d069b5实际完成
- status: TWO_FORMULATION_TRANSLATIONS_CHECKED / PARENT_OPEN

C309原ℝ₀上的零点/全点对以差运算互推，并接原Lift/统一逆元；C310以bool反转和命题性存在消去对接Book/库Markov。两组没有跨接，未提供原则实例、chosen见证、时限或独立性。

1草稿+1fresh完整核通过，230.513688秒、6本地模块/1079图/41pin，formal/关系/图PASS。原典Dedekind/Cauchy/choice/宇宙和本模型分层，文献桥保持SOURCE_REPORTED_NOT_REPLAYED，不新增公设。复读NativeSourceContract确认给定源重呈现不自动等于实际形状变化，当前owner旧待核Input描述已原位修正。

策略v1.26由{commit}保存。下一动作：{NEXT}

46KC legacy原子兼容bundle按PROTOCOL§5，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；报告四片。T01–05完整同X目标，T06–10准确公式/语义域，T11–17原生源核/模型前提，T18–21无部署，T22–24范围/原典/回整体，T25无AI合同变化，T26精确提交。共享C01–C09 NO_CHANGE，C10项目证据UPDATE。无Sub Agent、push/tag/发布。

element_usage：closure/收据复认、research精确翻译、SOP返回整体主链、verification源核、canonical事务、dev-notes。没有新通用框架。
'''
    audit=f'''# {SID} 核心认知回评

core-cognition-generation-7；46条。

- core_change: NO
- direction_change: FULL_SAME_TASK_INTEGRATION_AUDIT_NEXT
- panorama_change: ADD_C309_C310_FORMULATION_SCOPE
- essay_change: NO
- update_decision: 有界原典核对结束，回AST-G01–G06完整连接审计
- cross_conflicts: 两个独立↔不组成跨组桥；mere存在不变chosen；给定源重呈现不等于实际形变
- unresolved: 实数/二进制桥、原广义操作/保真、整体交付和历史Coq关系

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名时间/自指/反射问题未推进，公式翻译不代替它。'))
        ev=('第二十四轮001–004、C309/C310及原典/INTEGRATION-PREFLIGHT；下一六义务。若偷换实数/存在、拼接缺桥、把重呈现算实际形变或缩小父范围，撤回重评；新同任务反例可改变判断。' if n in TOUCHED else '第二十四轮003未触达；具名机制实际进入当前依赖或新原文要求时重开。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001问题/简化：公式相似不代替类型连接；002前提/时间：mere输出与运行时限分开；003圆环/ASK：下一核实际原操作/Done；004HoTT/自反：没有从表述互推得到总自验证；005表达/原文：给定源实例不穷尽原意；006知识谱：源/模型/选择各自核；007助力/阻力：有界翻译完成就回主链，停止支线惯性；008现实骨架：下一对现实指称和数学任务的逐项连接做审查。

## 已走过的路与即将选择

两组翻译有源核，缺实数编码/模型桥准确保留。原典意识到边界，不替原击落判词背书。下一以AST-G01–G06逐项审实际主圆输入/过程/观察/完成，对经典Lean F、原生重呈现、条件弱域和算术支线分类后选真正剩余。八轴/遗漏/停止见第二十四轮003；不是缩范围完成Goal。
'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[RUN],'claim_ids':['C-309','C-310'],'validation':'audit/astra-book-scope-20260920/DELIVERY.json','formal_kernel_runs':1,'draft_checks':1,'parent_objective':'OPEN'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-198'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 197$','source_state_revision: 198',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-198',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C309/C310已核两组翻译：原ℝ₀零点/全点对及二进制Book/库Markov，前者接原Lift/逆元，后者保mere存在；两组跨接仍未证。fresh核6本地/1079图/41pin，原典/选择/宇宙分别定级。策略v1.26由'+commit+'保存。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('WEAK_PRINCIPLE_CHARACTERIZED_BOOK_SCOPE_NEXT','FORMULATIONS_CHECKED_CASE_INTEGRATION_NEXT').replace('`OUT-ASTRA-WEAK-PRINCIPLE-23` |','`OUT-ASTRA-WEAK-PRINCIPLE-23`、`OUT-ASTRA-BOOK-SCOPE-24` |').replace('原弱Lift原则已刻画；下一原典/Markov准确范围；原广义及整体开放','两组表述已核，跨组桥未证；下一AST-G六义务同任务集成；父范围开放')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-BOOK-SCOPE-24` | C309/C310实数与二进制表述分别翻译 | `DIR-U-ASTRA-BREAKPOINT` | 精确类型/原生核/原典范围核对 | `FORMAL_CHECKED_WITH_SCOPE / TWO_TRANSLATIONS_BRIDGE_OPEN` | 零点/全点对、Book/库Markov各自↔，未跨组推断 | 原同任务集成/现实操作、必要后继/整体 | `'+REPORT+'`；`audit/astra-book-scope-20260920/DELIVERY.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['R-ASTRA-WEAK-PRINCIPLE-20260920'],'authorization':'用户ACTIVE Goal及既有T3研究/集成授权；原典准确表述核对完成后返回完整同任务集成，原目标不缩小。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))


if __name__=='__main__':main()
