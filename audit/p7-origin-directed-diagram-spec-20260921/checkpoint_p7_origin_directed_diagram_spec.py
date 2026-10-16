#!/usr/bin/env python3
"""Checkpoint P7's K-admission contract and route the active goal to P8."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = 'S-RES-20260921-ASTRA-P7-ORIGIN-DIRECTED-DIAGRAM-SPEC'
BASE = '.codex/research/hott/sessions/' + SID + '/'
PLAN_ID='R-HOTT-FOUR-TRACK-PLAN-20260921'; ABX_ID='R-ABX-ACTION-20260921'
P1_ID='R-P1-RMIN-SPEC-20260921'; P2_ID='R-P2-KTHEORY-SIP-20260921'; P3_ID='R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921'; P5_ID='R-P5-SUCCESSOR-DISCOVERY-20260921'; P6_ID='R-P6-ORIGIN-STRUCTURE-STRATIFIED-20260921'; P7_ID='R-P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-20260921'
REPORT='audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md'
VERIFY='audit/p7-origin-directed-diagram-spec-20260921/verify_p7_origin_directed_diagram_spec.py'
RECEIPT='audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-VERIFICATION.json'
CHECKPOINT='audit/p7-origin-directed-diagram-spec-20260921/checkpoint_p7_origin_directed_diagram_spec.py'
P1V='audit/p1-rmin-spec-20260921/verify_p1_rmin_spec.py'; P1R='audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md'; P1J='audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-VERIFICATION.json'
P2V='audit/p2-ktheory-sip-20260921/verify_p2_ktheory_sip.py'; P2R='audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-REPORT.md'; P2J='audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-VERIFICATION.json'
P3V='audit/p3-unimath-functor-algebras-20260921/verify_p3_unimath_functor_algebras.py'; P3R='audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-REPORT.md'; P3J='audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-VERIFICATION.json'
P5V='audit/p5-successor-discovery-20260921/verify_p5_successor_discovery.py'; P5R='audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md'; P5J='audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-VERIFICATION.json'
P6V='audit/p6-origin-structure-stratified-20260921/verify_p6_origin_structure_stratified.py'; P6R='audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md'; P6J='audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-VERIFICATION.json'
PV='audit/four-track-plan-20260921/verify_four_track_plan.py'; PJ='audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json'
PLAN='HoTT后续研究总体方案.md'
SHARDS=tuple('HoTT后续研究总体方案/'+x for x in ('001 - 上一轮问答与四分支校正.md','002 - 共同任务、术语与优先级原则.md','003 - 分支顺序、准入与停止条件.md','004 - 令牌经济、反漂移与每单元复核.md','005 - 当前第一步与交接.md'))
INTERFACES=('ABX行动/003 - 原圆环对象、判据与正反控制.md','HoTT/formal/astra-real-geometry/StructuredCurve.lean','HoTT/formal/astra-breakpoint-check/GeometricBoundaryObservation.agda','HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda','HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda')
P7_SOURCES=(REPORT,VERIFY,RECEIPT,CHECKPOINT,P6R,P6V,P6J,P5R,P5V,P5J,P1R,P1V,P1J,P2R,P2V,P2J,P3R,P3V,P3J,PLAN,*SHARDS,PV,PJ,'goal.md','goal-3.md','feature-list.md','rulings.md','ABX行动.md','ABX行动/005 - 状态、停止条件与未来交接.md',*INTERFACES)

def sha(p: Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def repl(body:str,old:str,new:str)->str:
    out,n=re.subn(re.escape(old),new,body,count=1);assert n==1,old;return out
def row(body:str,prefix:str,value:str)->str:
    xs=body.splitlines()
    for i,x in enumerate(xs):
        if x.startswith(prefix):xs[i]=value;return '\n'.join(xs)+'\n'
    raise AssertionError(prefix)

def audit(core:dict)->str:
    hs=re.findall(r'^### (KC-\d+) · .*? · (.+)$',(ROOT/'核心认知.md').read_text(encoding='utf-8'),re.M);assert len(hs)==core['kc_count']==46
    touched={10,14,15,19,21,22,35,37,38,39,40,41,42,43,44,45,46}
    s=f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P7_K_HARNESS_ACCEPTED_P8_DIRECTED_IMPLEMENTATION_DISCOVERY_NEXT
- panorama_change: ORIGIN_DIRECTED_DIAGRAM_ADMISSION_CONTRACT_WITH_SCOPE
- essay_change: NO
- update_decision: P7 ends the specification/admission denominator and selects a new implementation-discovery denominator P8
- cross_conflicts: a precise K gate separates an explicit structure-preserving consumer from a genuine bare-input task upgrade
- unresolved: actual K, same-task mismatch, ordinary-HoTT relevance, theory/implementation divergence and philosophical non-reality all remain open

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
'''
    for i,(k,t) in enumerate(hs,1):
        if i in touched:
            rel='DEEPENED'; j='P7 将来源、过程、观察和完成固定为可否证的 K 准入条件，禁止事后把额外现实条件塞给候选。';e=f'{REPORT}；P8若没有真实输入/输出/Done承诺，必须拒绝K资格。'
        else:
            rel='NOT_TOUCHED';j='本单元仅收敛原圆环 K admission harness，不重新裁决本条独立用户原文。';e='goal.md §2；无新数学定理或HoTT缺陷结论。'
        s+=f'| `{k}` | {t} | {rel} | {j} | {e} |\n'
    return s+'''\n## 扩展认知逐片复认\n\n001–008：P7 的目的不是把现实解释塞入理论内部，而是在理论/库的真实输入输出上先固定同任务契约。被完整字段约束的调用是防御；只有未持有这些字段却声称强完成的调用才是候选。\n\n## 波次定位\n\n- 最终目标连接：P7 把 R 端接到 K 的实际消费者准入边。\n- 全局坐标：P6完成对象承载比较；P7完成K admission harness；P8开始新的版本固定实现 discovery。\n- 实际价值：未来候选不能只因“talks about paths/direction”入场，必须满足五个输入输出条件。\n- 不延续理由：P7规格已固定；再增字段而无消费者不会改变准入。\n- 裁决：`K_HARNESS_ACCEPTED_WITH_SCOPE / P8_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`。\n'''

def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');a=ap.parse_args()
    for x in (P1V,P2V,P3V,P5V,P6V,VERIFY,PV):subprocess.check_call([sys.executable,'-B',x,'--write'],cwd=ROOT)
    for x in P7_SOURCES:assert (ROOT/x).is_file(),x
    spec=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(spec);assert spec.loader;spec.loader.exec_module(rt)
    st=json.loads((ROOT/rt.STATE).read_text(encoding='utf-8'));assert st['revision']==226;assert st['latest_session']== 'S-RES-20260921-ASTRA-P6-ORIGIN-STRUCTURE-STRATIFIED'
    head=json.loads((ROOT/rt.HEAD).read_text());assert all(sha(ROOT/r)==h for r,h in head['tracked'].items())
    plan=rt.plan(ROOT,profile='research',task_ids=[PLAN_ID]);assert not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-CHECKPOINT-PLAN.json').write_bytes(rt.dump(plan))
    for x in (P1J,P2J,P3J,P5J,P6J,RECEIPT,PJ):assert json.loads((ROOT/x).read_text())['status']=='PASS_WITH_SCOPE'
    prior=st['latest_session'];st['revision']=227;st['latest_session']=SID
    for ident,label in ((P1_ID,'P1 remains scoped R_min.'),(P2_ID,'P2 remains scoped SIP result.'),(P3_ID,'P3 remains scoped UniMath result.'),(P5_ID,'P5 remains successor selection.'),(P6_ID,'P6 remains composite-object comparison.')):
        r=st['records'][ident];r['related_records']=list(dict.fromkeys(r.get('related_records',[])+[P7_ID,SID]));paths=set(r.get('full_sources',[]))|set(r.get('source_hashes',{}));r['source_hashes'].update({x:sha(ROOT/x) for x in paths if (ROOT/x).is_file()});r['revalidation']=r.get('revalidation','')+' Revision227 records P7 K-admission harness; '+label
    pr=st['records'][PLAN_ID];pr['evidence_status']='USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / P2_SIP_NO_K_WITHIN_SCOPE / P3_UNIMATH_NO_K_WITHIN_SCOPE / P4_NOT_TRIGGERED / P5_SUCCESSOR_SELECTED / P6_COMPOSITE_DIAGRAM_CANDIDATE / P7_K_HARNESS_ACCEPTED / P8_DIRECTED_IMPLEMENTATION_DISCOVERY_NEXT / GOAL_ACTIVE';pr['status']='four_track_first_pass_p5_p6_p7_complete_p8_directed_implementation_discovery_next';pr['full_sources']=list(dict.fromkeys(pr.get('full_sources',[])+list(P7_SOURCES)));pr['related_records']=list(dict.fromkeys(pr.get('related_records',[])+[P7_ID,SID]));paths=set(pr['full_sources'])|set(pr.get('source_hashes',{}));pr['source_hashes'].update({x:sha(ROOT/x) for x in paths if (ROOT/x).is_file()});pr['revalidation']='Revision227 completes P7: OriginDirectedDiagram and five K admission checks are fixed. P8 is a fresh, version-pinned directed/simplicial implementation discovery; no actual K or HoTT defect is claimed.';pr['scope']='P7 is a specification/admission result, not a formal theorem. It ensures future K auditing distinguishes bare input from explicit structured input and selects P8 for a new external implementation denominator.'
    abx=st['records'][ABX_ID];abx['full_sources']=list(dict.fromkeys(abx.get('full_sources',[])+list(P7_SOURCES)));abx['related_records']=list(dict.fromkeys(abx.get('related_records',[])+[P7_ID,SID]));paths=set(abx['full_sources'])|set(abx.get('source_hashes',{}));abx['source_hashes'].update({x:sha(ROOT/x) for x in paths if (ROOT/x).is_file()});abx['revalidation']='Revision227 completes P7 K harness and selects P8 fresh directed/simplicial implementation discovery. No K, mismatch or HoTT defect has been found.';abx['scope']='ABX has a fixed K admission harness; P8 now seeks one version-pinned actual directed/simplicial implementation or consumer to which it can be applied.'
    st['records'][P7_ID]={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'K_HARNESS_ACCEPTED_WITH_SCOPE / P8_DIRECTED_TYPE_THEORY_IMPLEMENTATION_DISCOVERY_NEXT / NO_NEW_MATHEMATICAL_CLAIM','status':'complete_with_scope_p8_directed_implementation_discovery_next','depends_on':[],'related_records':[PLAN_ID,ABX_ID,P6_ID,P5_ID,P1_ID,P2_ID,P3_ID,prior],'full_sources':list(dict.fromkeys(P7_SOURCES)),'source_hashes':{x:sha(ROOT/x) for x in dict.fromkeys(P7_SOURCES)},'scope':'P7 fixes a minimal static/process/observation/forgetting contract and five K admission checks. It does not formalize the interface in a kernel, find K, prove a mismatch or prove a HoTT defect.'}
    st['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'P7_K_ADMISSION_HARNESS_CHECKPOINTED_WITH_SCOPE','status':'complete_with_scope','depends_on':[],'related_records':[P7_ID,P6_ID,PLAN_ID,ABX_ID,prior],'full_sources':[BASE+x for x in ('SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md')]}
    st['execution_control'].update(status='FOUR_TRACK_FIRST_PASS_P5_P6_P7_COMPLETE_P8_NEXT',current_phase='PHASE_2_P7_K_HARNESS_ACCEPTED_P8_DIRECTED_IMPLEMENTATION_DISCOVERY_NEXT',second_phase_status='P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_P5_P6_P7_COMPLETE_P8_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification='P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-001. Search public implementation and community sources plus local/historical assets; freeze one real version/entry/call chain; evaluate P7 K-input/K-output/K-claim/K-forgetting/K-version. A directed-type paper or explicit structured input is not K.')
    st['projection']['status']='FOUR_TRACK_FIRST_PASS / P5_P6_P7_COMPLETE / NEXT_P8_DIRECTED_IMPLEMENTATION_DISCOVERY / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM'
    session=f'''# {SID}\n\n- host: Codex desktop local\n- model: GPT-6 Astra；服务端路由未由本项目独立认证\n- tier: T3 state mutation for P7 K-admission specification\n- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST\n- objective: freeze a minimal OriginDirectedDiagram and reject non-consumer candidates before P8\n- load_receipt: `audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-CHECKPOINT-PLAN.json`\n- status: COMPLETED_WITH_SCOPE / K_HARNESS_ACCEPTED / P8_NEXT / NO_NEW_MATHEMATICAL_CLAIM\n\nP7 did not make a new geometric object or rerun existing kernels. It maps existing local structures to a pre-registered consumer admission test: a real K must have a version, bare input, output, same Done claim and demonstrated forgetting. P8 is therefore a new implementation-discovery denominator rather than an inference from paper titles.\n\n| element | use | effect on this unit |\n|---|---|---|\n| P6 field matrix | used | supplies exact fields and anti-restatement control |\n| local formal controls | used | maps each K condition to a positive or negative control |\n| public search | not rerun | P7 introduced no new factual theory comparison beyond P6 |\n| proof kernel | not run | P7 produces no new mathematical theorem |\n'''
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[{'kind':'p7-k-admission-spec-and-routing-verification','command':f'python3 -B {P1V} --write && python3 -B {P2V} --write && python3 -B {P3V} --write && python3 -B {P5V} --write && python3 -B {P6V} --write && python3 -B {VERIFY} --write && python3 -B {PV} --write','result':'PASS_WITH_SCOPE; P7 K admission fields and P8 routing agree','mathematics':'NOT_A_NEW_KERNEL_RUN'}],'new_math_claims':[],'new_kernel_replay':False,'scope':'P7 specification/admission result only.'}
    drow='| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：P7 K admission harness 与P8实现discovery | 用户要求活跃goal跨分母推进并每wave做有界侦察 | `FIRST_PASS_COMPLETE / P5_P6_P7_COMPLETE / NEXT_P8_DIRECTED_IMPLEMENTATION_DISCOVERY / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1–P7 | P8固定实际实现/调用链，逐项跑五条件 | `HoTT后续研究总体方案.md`；P7 report；revision227 receipt |'
    arow='| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P7 K admission harness 后的P8实现discovery | H/R/K整备、P1–P7 | `NO_ACTUAL_K_IN_TESTED_DENOMINATORS / P7_K_HARNESS_ACCEPTED / NEXT_P8_DIRECTED_IMPLEMENTATION_DISCOVERY` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P7 | 只审计版本固定实际输入/输出；论文名不是K | `ABX行动.md`；P7 report；revision227 receipt |'
    prow='| `OUT-HOTT-FOUR-TRACK-PLAN` | 第二阶段P7 K admission harness 完成 | `DIR-U-HOTT-FOUR-TRACK` | P6结构矩阵、CurvePresentation/RichDiagram/CurveRun、P7合同 | `P7_K_HARNESS_ACCEPTED_P8_NEXT` | 未来K须同时有bare输入、输出、Done承诺、forgetting和版本证据 | 不证明K、失配、新拓扑或HoTT缺陷 | `audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md`；revision227 receipt |'
    aprow='| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环：P7 K admission harness | `DIR-U-ABX-ORIGINAL-CIRCLE` | P1–P7及现有局部控制 | `P7_K_HARNESS_ACCEPTED / NEXT_P8_DIRECTED_IMPLEMENTATION_DISCOVERY` | P8以五项条件选择真实实现分母 | 不证明全库无K、K或HoTT缺陷 | `ABX行动.md`；P7 report；revision227 receipt |'
    mem='P7 K admission harness 已完成：`OriginDirectedDiagram` 固定静态图、过程、Obs/Done与三层forgetful；未来K必须有输入、输出、同任务Done、忘却和版本五项直接证据。当前P8选择一个版本固定directed/simplicial type-theory实际实现/消费者分母；论文名或显式结构输入不是K。入口：`audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md`；revision227 checkpoint。'
    frontier='- P7 K harness 已完成：未来候选必须通过 K-input/K-output/K-claim/K-forgetting/K-version。当前P8在公开directed/simplicial type-theory实现或消费者中选择一个版本固定分母；显式结构输入或论文标题只构成防御/线索。入口：`audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md`。'
    resume='当前 active goal 在P7后继续：P7以OriginDirectedDiagram和五项K admission条件把R接到真实消费者审计。P8=DIRECTED_TYPE_THEORY_IMPLEMENTATION_DISCOVERY：先做公开/本地资产侦察，固定一个实际版本/入口/调用链，再逐项检验bare输入、输出、Done承诺、forgetting与版本；没有五项直接证据不是K。入口：`audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md`；revision227 checkpoint。'
    log='\nS-RES-20260921-ASTRA-P7-ORIGIN-DIRECTED-DIAGRAM-SPEC：P7完成。OriginDirectedDiagram与K-input/K-output/K-claim/K-forgetting/K-version冻结；这是K准入合同，不是K或数学定理。P8开始新的directed/simplicial实现discovery分母，必须先做公开与本地侦察；revision227 checkpoint。\n'
    files=[]
    for rel in list(rt.MUTABLE)+list(rt.mutable_shard_paths(ROOT)):
        raw=(ROOT/rel).read_bytes();body=raw.decode('utf-8')
        if rel==rt.STATE:body=rt.dump(st).decode('utf-8')
        elif rel==rt.DIRECTION:
            body=repl(body,'source_state_revision: 226','source_state_revision: 227');body=repl(body,'projection_generation: 20260921-direction-226','projection_generation: 20260921-direction-227');body=repl(body,'semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_COMPLETE_P7_ORIGIN_DIRECTED_DIAGRAM_NEXT','semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_COMPLETE_P8_DIRECTED_IMPLEMENTATION_DISCOVERY_NEXT')
        elif rel==rt.PANORAMA:
            body=repl(body,'source_state_revision: 226','source_state_revision: 227');body=repl(body,'projection_generation: 20260921-outcome-226','projection_generation: 20260921-outcome-227');body=repl(body,'semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_COMPLETE_P7_ORIGIN_DIRECTED_DIAGRAM_NEXT','semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_COMPLETE_P8_DIRECTED_IMPLEMENTATION_DISCOVERY_NEXT')
        elif rel=='方向追踪/002 - 治理与用户方向.md':body=row(row(body,'| `DIR-U-HOTT-FOUR-TRACK` |',drow),'| `DIR-U-ABX-ORIGINAL-CIRCLE` |',arow)
        elif rel=='全景视野/003 - 当前机器证明包与原生重放.md':body=row(row(body,'| `OUT-HOTT-FOUR-TRACK-PLAN` |',prow),'| `OUT-ABX-ACTION-INTAKE` |',aprow)
        elif rel=='MEMORY/001 - 当前执行队列.md':body=row(body,'P6 对象理论比较已完成：',mem)
        elif rel=='MEMORY/003 - 当前验证状态与顺序日志.md':body+=log
        elif rel==rt.PREFIX+'FRONTIER.md':body=repl(body,'- P6 已完成：现有 CurvePresentation/RichDiagram/CurveRun 与标记、分层、cospan、定向/cohesive 文献支持组合的显式R对象，非HoTT缺陷。当前P7仅以既有接口收敛 OriginDirectedDiagram；若无新可消费约束则 RESTATEMENT_ONLY，随后换新的实际K或独立R分母。入口：`audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md`。',frontier)
        elif rel==rt.PREFIX+'RESUME.md':body=repl(body,'当前 active goal 在 P6 后继续：P6 发现现有CurvePresentation/RichDiagram/CurveRun与标记、分层、cospan、定向/类型论和cohesive结构可组合承载R；裸同胚不自动补齐字段，完整字段可运输是正控制。P7=ORIGIN-DIRECTED-DIAGRAM-SPEC：只收敛已有接口的静态图、trace、Obs、Done_s、结构态射与U；没有新可被K审计的约束就判RESTATEMENT_ONLY并换支。入口：`audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md`；revision226 checkpoint。',resume)
        files.append({'path':rel,'expected_sha256':rt.sha(raw),'text':body})
    for n,b in (('SESSION.md',session),('RUNS.json',rt.dump(runs).decode('utf-8')),('CORE_COGNITION_AUDIT.md',audit(st['current_core']))):files.append({'path':BASE+n,'expected_sha256':None,'text':b})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':[PLAN_ID],'authorization':'用户已授权当前唯一AI按goal-3持续推进、更新current state与canonical checkpoint；不启动Sub Agent、不push、不发布。','files':files};(OUT/'P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-checkpoint-payload.json').write_bytes(rt.dump(payload));res=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=a.apply);(OUT/('P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-checkpoint-apply.json' if a.apply else 'P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-checkpoint-dry-run.json')).write_bytes(rt.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
