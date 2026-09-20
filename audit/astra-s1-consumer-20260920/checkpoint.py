#!/usr/bin/env python3
"""Canonical state update for the actual S1 consumer proof and six exact controls."""
from pathlib import Path
import argparse, importlib.util, json, re, subprocess
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = 'S-RES-20260920-ASTRA-S1-CONSUMER'
BASE = '.codex/research/hott/sessions/' + SID + '/'
REPORT = 'Astra继续尝试/断点与证明机制系统检查/第二十一轮执行报告.md'
RUN = 'HoTT/verification/runs/20260920-MP-ASTRA-S1-CONSUMER-001-02'
NEXT = 'BP-QUOTIENT-CONSUMER-01：按第二十一轮004片五项，固定同GOLD的Cubical.Data.Rationals.Base.ℚ、代表关系与实际rec2加乘/平方；检验原始分子观察是否尊重关系，以代表fiber和[]surjective的mere见证实际消费rec→Set及常值性，核正确值/Done、错误关系或常值证据和合法恢复。新增命题先精确量词/假设并原生过核；不换QuoQ，不把额外给原代表当裸商类历史恢复。原广义圆环/弱Lift、必要性与元层实际依赖、完整组合和学术交付保持；全registry历史Coq关系问题单列。'
sp = importlib.util.spec_from_file_location('runtime', ROOT / '.codex/tools/cognition_runtime.py')
R = importlib.util.module_from_spec(sp)
sp.loader.exec_module(R)
TOUCHED = {
1:('DEEPENED','实际源→编码解码→依赖逆律→消费者全链已核。'),
2:('DEEPENED','原S¹与ℤ不换，本地族/函数有明确上游Path/PathP对应。'),
3:('ALIGNED','四次拒绝不能合取成理论缺陷。'),
5:('ALIGNED','按真实结果归因：原链/恢复有效，当前候选没有失配。'),
7:('ALIGNED','核及diff决定结果，模型自评不作证。'),
10:('ALIGNED','模型绕行信息恢复不冒充全部现实任务。'),
11:('ALIGNED','库路径和实际checker耗时分开。'),
12:('DEEPENED','Glue输入、方块边界、路径纠正、J项资格分别有诊断。'),
13:('DEEPENED','删条件前后同签名与实际consumer固定；SC01改家族明确另分因果层。'),
14:('ALIGNED','原交付能力越级目标仍开放，不因本链正常边界算命中。'),
15:('TENSION','本域没有支持理论自我否定的证据，保留原范围。'),
17:('ALIGNED','库代码被作为待检对象，未以权威代替原生证明。'),
19:('NOT_TOUCHED','本轮不研究全部逼近/稠密完成，不由源码检查外推。'),
21:('DEEPENED','七次核、六成员、146模块和出处分类失败/修复均留存。'),
22:('ALIGNED','现实相对两向目标不被缩成四个非法项。'),
31:('DEEPENED','实际依赖J与原类型消费者，没有空参数包装。'),
34:('ALIGNED','指定项失败不是对应命题普遍不可能，恢复已给正证。'),
35:('ALIGNED','原广义来源/操作不由S¹语法自动表示完全。'),
37:('ALIGNED','HIT圆不替点集去点；原实数模型和未决保留。'),
38:('DEEPENED','直查实际基础链中局部数据有没有被遗漏。'),
39:('DEEPENED','具体基础规则链得到可审诊断，不以简单测试数量代替探索。'),
40:('ALIGNED','下一rec→Set由实际知识源定位，其未运行边界明确。'),
41:('ALIGNED','当前pass完成与四弹整体完成不同。'),
42:('ALIGNED','原数据恢复有效必须认账，不据四拒绝保住指控。'),
43:('DEEPENED','本域有结果后转另一实际商/截断规则链，不重复改名。'),
44:('ALIGNED','绕行解释是模型内任务，没有自证物理对应。'),
45:('DEEPENED','局部结构进入真实后续项的方式已具体化，下一核表示历史与函数值。'),
46:('ALIGNED','原类型、原数据、实际核与语义边界同时保留。')}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args()
    delivery=json.loads((OUT/'DELIVERY.json').read_text());assert delivery['status']=='FORMAL_AND_RELATION_PASS_SIX_CONTROLS_RECONCILED'
    state=json.loads((ROOT/R.STATE).read_text());assert state['revision']==194
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(R.sha((ROOT/p).read_bytes())==h for p,h in head['tracked'].items())
    prior=json.loads((ROOT/'audit/astra-remaining-20260920/RESUME.json').read_text());assert R.sha((ROOT/'核心认知.md').read_bytes())==prior['core_sha256']
    commit=(OUT/'PLAN-COMMIT.txt').read_text().strip()
    docs=[{'path':d['path'],'prior_sha256':d['sha256'],'sha256':R.sha((ROOT/d['path']).read_bytes())} for d in prior['documents']]
    (OUT/'RESUME.json').write_bytes(R.dump({'policy':'Same-T3 PROTOCOL v3 receipt reattestation, not new full emission','revision':194,'core_sha256':prior['core_sha256'],'core_unchanged':True,'documents':docs,'known_changes':'Own checkpoint194; current32 tracked hashes verified','kc_stance_revisited':'All46 revisited against actual S1 chain; prior source samples retained','model_understanding':'NOT_CERTIFIED_BY_TOOL','objective':'完成四弹一体的redo','app_goal_status_observed':'active'}))
    plan=R.plan(ROOT,profile='research',task_ids=['R-ASTRA-REMAINING-CLOSURE-20260920']);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'CHECKPOINT-PLAN.json').write_bytes(R.dump(plan))
    old=state['latest_session'];state['revision']=195;state['latest_session']=SID
    state['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'C304_NATIVE_S1_CHAIN_AND_SIX_CONTROLS','status':'complete_with_scope','depends_on':[],'related_records':[old,'A-ASTRA-CONTINUING-GOAL-20260919'],'full_sources':[BASE+n for n in ['SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md']]}
    manifest=json.loads((ROOT/RUN/'source-manifest.json').read_text())
    state['records']['R-ASTRA-S1-CONSUMER-20260920']={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'FORMAL_CHECKED_WITH_SCOPE / SIX_DECLARED_CASES_RECONCILED','status':'actual_s1_chain_qualified_quotient_consumer_next','depends_on':[],'related_records':[SID,'R-ASTRA-REMAINING-CLOSURE-20260920'],'full_sources':[REPORT,'HoTT/formal/astra-s1-consumer-check/SC00.agda','audit/astra-s1-consumer-20260920/DELIVERY.json','audit/astra-s1-consumer-20260920/CONTROL-VERIFICATION.json'],'source_hashes':{f['path']:f['sha256'] for f in manifest['files'] if f['path'].endswith(('.agda','TOOLCHAIN.json'))},'scope':'Original upstream S1 and integers; extracted real helix/decode/J chain with explicit upstream function bridges, inverse laws and composition observation. Six cases reconciled, two accept and four fixed-term type rejections. Primary02 separates inert provenance copies after initial qualification error; original source/run preserved. No physical deletion/global consistency/whole objective conclusion.'}
    state['execution_control'].update(status='ACTIVE_GOAL_S1_CHAIN_QUALIFIED_QUOTIENT_CONSUMER_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification=NEXT)
    session=f'''# {SID}

- host: Codex desktop local
- model: GPT-6-based Codex；不认证服务端路由
- tier: T3 research / canonical checkpoint
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- load_receipt: audit/astra-s1-consumer-20260920/RESUME.json
- objective: 完成四弹一体的redo
- app_goal_status_observed: active
- previous_goal_turn: PROGRESS；14包97资产与revision194实际完成
- status: ACTUAL_S1_CHAIN_QUALIFIED / PARENT_OPEN

C304使用原S¹/ℤ，逐字提取实际helix至winding-hom，新增上游族/编码/函数对应及真实往返、组合consumer。六成员两接受四类型拒绝；SC01输入族、SC02方块边界、SC03纠正Path、SC04 J/refl分别定位，没有新增数学不可能性。

主run02 fresh31.673237秒、146模块、41外部pin；实际本地编译源1，出处副本4单列。初次01核过但formal把出处副本当本地代码而拒；capture_v2独立分类后源码未改重新执行，初次原件和失败保持；两个SC00图逐字相同。总七次核运行不是七个候选。formal/关系及六成员diff对账PASS。

策略v1.23由{commit}保存。下一动作：{NEXT}

46KC兼容legacy bundle按PROTOCOL§5，G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001保持；报告四分片。T01–05原范围与实际任务，T06–10依赖链和上游桥，T11–17源码/核及出处分类修复，T18–21无部署，T22–24候选关闭/后继与原失败，T25无AI治理变化，T26精确提交。共享C01–C09 NO_CHANGE，C10项目证据UPDATE。无Sub Agent、push/tag/发布。

element_usage：closure/收据复认、research实际正反/恢复、SOP返回不同规则族、verification精确源核、canonical事务、dev-notes。未改共享validator，不另建平台。
'''
    audit=f'''# {SID} 核心认知回评

core-cognition-generation-7；46条。

- core_change: NO
- direction_change: QUOTIENT_TRUNCATION_CONSUMER_NEXT
- panorama_change: ADD_C304_S1_CHAIN
- essay_change: NO
- update_decision: 当前实际S1链六成员结束，进入原ℚ商/截断数据消费者
- cross_conflicts: 正确拒绝不计缺陷；原类型/上游对应不替现实桥；出处文件与编译源分类分开
- unresolved: 原广义任务/弱Lift、其它消费者、必要性/元层、整体与历史Coq关系

| KC | 主题 | relation | 工作姿态及实际理由 | 证据、下一选择与反证条件 |
|---|---|---|---|---|
'''
    headings=re.findall(r'^### (KC-\d+) · .*? · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M);assert len(headings)==46
    for n,(kc,title) in enumerate(headings,1):
        relation,why=TOUCHED.get(n,('NOT_TOUCHED','该具名自指/时间/反射问题未推进，本域不代替它。'))
        ev=('第二十一轮001–004、C304源/run及六控制；下一同GOLD商/截断。若上游对应不成立、条件被合法省去但目标仍完整、run/hash不一致或本域被外推则撤回重评。' if n in TOUCHED else '第二十一轮004未触达；具名机制实际成为当前依赖或用户新原文要求时重开。')
        audit+=f'| `{kc}` | {title} | {relation} | {why} | {ev} |\n'
    audit+='''
## 扩展认知逐片复认

001问题/简化：原任务/类型与限定代码分母明确；002前提/时间：参数和checker耗时不混；003圆环/ASK：具体面条件传递被直接核查；004HoTT/自反：J消去不是一般自我验证；005表达/原文：HIT不替实际去点；006知识谱：上游函数有Path/PathP桥，不因库身份免审；007助力/阻力：四正确拒绝可关闭候选，转新真实链；008现实骨架：模型绕行解释保持边界，原广义任务继续。

## 已走过的路与即将选择

SC00及SC05有效、四修改诊断准确，主记录分类失败已留证修复，不能把当前正常防线说成击落。下一rec→Set/实际有理商定位不同规则族，考察函数值与原代表观察，不重复旧Bool商。八轴、独立对照、六成员余数0、七次运行区别及停止条件见第二十一轮004；不是全库/全理论完备性。
'''
    controls=json.loads((OUT/'CONTROL-RUNS.json').read_text())
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[RUN],'control_runs':[x['run'] for x in controls],'historical_initial_run':'HoTT/verification/runs/20260920-MP-ASTRA-S1-CONSUMER-001-01','claim_ids':['C-304'],'validation':'audit/astra-s1-consumer-20260920/DELIVERY.json','total_kernel_runs':7,'parent_objective':'OPEN'}
    for rec,kind in [('I-DIRECTION-PORTFOLIO-20260912','direction'),('I-OUTCOME-PANORAMA-20260912','outcome')]:state['records'][rec]['projection_generation']='20260920-'+kind+'-195'
    targets=list(R.MUTABLE)+list(R.mutable_shard_paths(ROOT));b=subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',*targets],cwd=ROOT,capture_output=True,check=True);(OUT/'current-owner-baseline.txt').write_bytes(b.stdout)
    files=[]
    for rel in targets:
        raw=(ROOT/rel).read_bytes();body=R.dump(state).decode() if rel==R.STATE else raw.decode()
        if rel in (R.DIRECTION,R.PANORAMA):
            body,n=re.subn(r'(?m)^source_state_revision: 194$','source_state_revision: 195',body);assert n==1
            kind='direction' if rel==R.DIRECTION else 'outcome';body,n=re.subn(r'(?m)^projection_generation: .+$','projection_generation: 20260920-'+kind+'-195',body);assert n==1
        if rel=='MEMORY/001 - 当前执行队列.md':
            start=body.index('用户当前App Goal');end=body.index('\n\n',start)
            body=body[:start]+'用户当前App Goal为ACTIVE：“完成四弹一体的redo”，完整范围保持。C304实际S1整数覆盖链与上游对应已过核，SC00–05两接受四准确类型拒绝，未构成理论失配。主run02区分真实编译源与出处副本，原01及分类失败保留；146模块/41外部pin。策略v1.23由'+commit+'保存。下一动作'+NEXT+' 入口：`'+REPORT+'`。'+body[end:]
        if rel=='方向追踪/002 - 治理与用户方向.md':
            lines=body.splitlines()
            for i,line in enumerate(lines):
                if line.startswith('| `DIR-U-ASTRA-BREAKPOINT` |'):lines[i]=line.replace('BREAKPOINT_VERSIONS_CLOSED_S1_CONSUMER_NEXT','S1_CHAIN_QUALIFIED_QUOTIENT_CONSUMER_NEXT').replace('`OUT-ASTRA-REMAINING-CLOSURE-20` |','`OUT-ASTRA-REMAINING-CLOSURE-20`、`OUT-ASTRA-S1-CONSUMER-21` |').replace('14旧包版本已修；下一实际S1依赖消费链六成员；原广义及其它机制开放','S1实际六成员已核；下一同GOLD商/截断数据消费；原广义及整体开放')
            body='\n'.join(lines)+'\n'
        if rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=body.rstrip()+'\n| `OUT-ASTRA-S1-CONSUMER-21` | C304实际S1依赖消费链及六控制 | `DIR-U-ASTRA-BREAKPOINT` | 原生核/上游对应/准确诊断及合法恢复 | `FORMAL_CHECKED_WITH_SCOPE / SIX_CASES_RECONCILED` | 原链与恢复接受，四指定修改被拒；原记录分类修复留证 | 商/截断实际使用、原广义任务/弱Lift、必要性/整体 | `'+REPORT+'`；`audit/astra-s1-consumer-20260920/DELIVERY.json` |\n'
        files.append({'path':rel,'expected_sha256':R.sha(raw),'text':body})
    for name,body in [('SESSION.md',session),('RUNS.json',R.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit)]:files.append({'path':BASE+name,'expected_sha256':None,'text':body})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':['R-ASTRA-REMAINING-CLOSURE-20260920'],'authorization':'用户ACTIVE Goal及既有T3研究/集成授权；实际S1六成员结束转真实商/截断，完整父范围保持。','files':files}
    (OUT/'checkpoint-payload.json').write_bytes(R.dump(payload));result=R.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('checkpoint-apply.json' if args.apply else 'checkpoint-dry-run.json')).write_bytes(R.dump(result));print(json.dumps({k:v for k,v in result.items() if k!='paths'},ensure_ascii=False))


if __name__=='__main__':main()
