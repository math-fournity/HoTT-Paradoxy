#!/usr/bin/env python3
"""Checkpoint bounded Rzk P8 audit and route the active goal to P9."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, re, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260921-ASTRA-P8-RZK-DIRECTED-IMPLEMENTATION';BASE='.codex/research/hott/sessions/'+SID+'/'
PLAN_ID='R-HOTT-FOUR-TRACK-PLAN-20260921';ABX_ID='R-ABX-ACTION-20260921'
IDS=('R-P1-RMIN-SPEC-20260921','R-P2-KTHEORY-SIP-20260921','R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921','R-P5-SUCCESSOR-DISCOVERY-20260921','R-P6-ORIGIN-STRUCTURE-STRATIFIED-20260921','R-P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-20260921')
P8_ID='R-P8-RZK-DIRECTED-IMPLEMENTATION-20260921'
REPORT='audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-REPORT.md';FREEZE='audit/p8-directed-type-theory-implementation-discovery-20260921/P8-RZK-SOURCE-FREEZE.json';VERIFY='audit/p8-directed-type-theory-implementation-discovery-20260921/verify_p8_directed_type_theory_implementation.py';RECEIPT='audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-VERIFICATION.json';CHECKPOINT='audit/p8-directed-type-theory-implementation-discovery-20260921/checkpoint_p8_rzk_discovery.py'
PV='audit/four-track-plan-20260921/verify_four_track_plan.py';PJ='audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json'
VPATHS=('audit/p1-rmin-spec-20260921/verify_p1_rmin_spec.py','audit/p2-ktheory-sip-20260921/verify_p2_ktheory_sip.py','audit/p3-unimath-functor-algebras-20260921/verify_p3_unimath_functor_algebras.py','audit/p5-successor-discovery-20260921/verify_p5_successor_discovery.py','audit/p6-origin-structure-stratified-20260921/verify_p6_origin_structure_stratified.py','audit/p7-origin-directed-diagram-spec-20260921/verify_p7_origin_directed_diagram_spec.py',VERIFY,PV)
RPATHS=('audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md','audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-VERIFICATION.json','audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-REPORT.md','audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-VERIFICATION.json','audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-REPORT.md','audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-VERIFICATION.json','audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md','audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-VERIFICATION.json','audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md','audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-VERIFICATION.json','audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md','audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-VERIFICATION.json')
PLAN='HoTT后续研究总体方案.md';SHARDS=tuple('HoTT后续研究总体方案/'+x for x in ('001 - 上一轮问答与四分支校正.md','002 - 共同任务、术语与优先级原则.md','003 - 分支顺序、准入与停止条件.md','004 - 令牌经济、反漂移与每单元复核.md','005 - 当前第一步与交接.md'))
P8_SOURCES=(REPORT,FREEZE,VERIFY,RECEIPT,CHECKPOINT,*VPATHS,*RPATHS,PLAN,*SHARDS,PJ,'goal.md','goal-3.md','feature-list.md','rulings.md','ABX行动.md','ABX行动/005 - 状态、停止条件与未来交接.md','audit/literature/LIT-DENOMINATOR-001/discovery-20260914/DISCOVERY-CANDIDATES.json')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def repl(b,o,n):
 x,c=re.subn(re.escape(o),n,b,count=1);assert c==1,o;return x
def row(b,pre,val):
 xs=b.splitlines()
 for i,x in enumerate(xs):
  if x.startswith(pre):xs[i]=val;return '\n'.join(xs)+'\n'
 raise AssertionError(pre)
def core_audit(core):
 hs=re.findall(r'^### (KC-\d+) · .*? · (.+)$',(ROOT/'核心认知.md').read_text(encoding='utf-8'),re.M);assert len(hs)==core['kc_count']==46
 s=f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P8_RZK_DEFENSE_P9_SHOTT_DIRUNIV_NEXT
- panorama_change: VERSION_PINNED_DIRECTED_IMPLEMENTATION_NOT_A_CONSUMER
- essay_change: NO
- update_decision: Rzk explicit direction is a defense; P9 uses a distinct related corpus denominator
- cross_conflicts: directed primitives show explicit input preservation, not a free upgrade from bare topological equivalence
- unresolved: sHoTT corpus, actual K, same-task mismatch, basic HoTT relevance and implementation semantics remain open

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
'''
 for i,(k,t) in enumerate(hs,1):
  if i in {10,14,15,19,21,22,35,37,38,39,40,41,42,43,44,45,46}:r='DEEPENED';j='P8 把 P7 五项 K 条件应用到实际定向实现，发现方向作为显式输入而非裸同胚的隐藏产物。';e=f'{REPORT}；P9若给出裸输入与Done承诺才改变该判断。'
  else:r='NOT_TOUCHED';j='本单元只审计固定 Rzk 输入/输出入口。';e='goal.md §2；无新数学定理或HoTT缺陷结论。'
  s+=f'| `{k}` | {t} | {r} | {j} | {e} |\n'
 return s+'\n## 扩展认知逐片复认\n\n001–008：P8 的正控制是一个实际实现显式表达方向；这缩小而非扩大指控。P9 必须保持相同纪律。\n\n## 波次定位\n\n- 最终目标连接：P8 检验 K 的实际实现边。\n- 全局坐标：P5–P7固定规格与准入；P8关闭Rzk分母为防御；P9选关联但不同的diruniv corpus。\n- 裁决：`NOT_A_CONSUMER / DEFENSE_PRESERVES_DIRECTIONAL_INPUT / P9_NEXT`。\n'
def main():
 a=argparse.ArgumentParser();a.add_argument('--apply',action='store_true');args=a.parse_args()
 for x in VPATHS:subprocess.check_call([sys.executable,'-B',x,'--write'],cwd=ROOT)
 for x in P8_SOURCES:assert (ROOT/x).is_file(),x
 spec=importlib.util.spec_from_file_location('runtime',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(spec);assert spec.loader;spec.loader.exec_module(rt)
 st=json.loads((ROOT/rt.STATE).read_text());assert st['revision']==227;assert st['latest_session']=='S-RES-20260921-ASTRA-P7-ORIGIN-DIRECTED-DIAGRAM-SPEC'
 h=json.loads((ROOT/rt.HEAD).read_text());assert all(sha(ROOT/x)==z for x,z in h['tracked'].items());plan=rt.plan(ROOT,profile='research',task_ids=[PLAN_ID]);assert not plan['hydration_diagnostics']['query_first_promoted'];(OUT/'P8-RZK-CHECKPOINT-PLAN.json').write_bytes(rt.dump(plan))
 for x in (*RPATHS,PJ,RECEIPT):
  if x.endswith('.json'):assert json.loads((ROOT/x).read_text())['status']=='PASS_WITH_SCOPE'
 prior=st['latest_session'];st['revision']=228;st['latest_session']=SID
 for ident in (*IDS,PLAN_ID,ABX_ID):
  r=st['records'][ident];r['related_records']=list(dict.fromkeys(r.get('related_records',[])+[P8_ID,SID]));paths=set(r.get('full_sources',[]))|set(r.get('source_hashes',{}));r['source_hashes'].update({x:sha(ROOT/x) for x in paths if (ROOT/x).is_file()});r['revalidation']=r.get('revalidation','')+' Revision228 records Rzk P8 bounded defense; prior scope unchanged.'
 pr=st['records'][PLAN_ID];pr['evidence_status']='USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / P2_SIP_NO_K_WITHIN_SCOPE / P3_UNIMATH_NO_K_WITHIN_SCOPE / P4_NOT_TRIGGERED / P5_SUCCESSOR_SELECTED / P6_COMPOSITE_DIAGRAM_CANDIDATE / P7_K_HARNESS_ACCEPTED / P8_RZK_DEFENSE / P9_SHOTT_DIRUNIV_CORPUS_NEXT / GOAL_ACTIVE';pr['status']='four_track_first_pass_p5_p6_p7_p8_complete_p9_shott_diruniv_next';pr['full_sources']=list(dict.fromkeys(pr.get('full_sources',[])+list(P8_SOURCES)));pr['related_records']=list(dict.fromkeys(pr.get('related_records',[])+[P8_ID,SID]));paths=set(pr['full_sources'])|set(pr.get('source_hashes',{}));pr['source_hashes'].update({x:sha(ROOT/x) for x in paths if (ROOT/x).is_file()});pr['revalidation']='Revision228 completes Rzk P8: explicit directed source/target/order/shape is a defense, no OriginDirectedDiagram U_bare to Done_s call exists within fixed six-file scope. P9 selects distinct sHoTT diruniv corpus.';pr['scope']='P8 is a version-pinned Rzk source audit restricted to six files. It does not audit all Rzk, build Rzk, prove its metatheory, find K, or prove a HoTT defect.'
 abx=st['records'][ABX_ID];abx['full_sources']=list(dict.fromkeys(abx.get('full_sources',[])+list(P8_SOURCES)));paths=set(abx['full_sources'])|set(abx.get('source_hashes',{}));abx['source_hashes'].update({x:sha(ROOT/x) for x in paths if (ROOT/x).is_file()});abx['revalidation']='Revision228 Rzk P8 is an explicit-direction defense, not K. P9 is a distinct sHoTT diruniv corpus audit.';abx['scope']='P8 found no K in the frozen Rzk six-file implementation scope; P9 separately audits sHoTT diruniv formalisation corpus.'
 st['records'][P8_ID]={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'NOT_A_CONSUMER / DEFENSE_PRESERVES_DIRECTIONAL_INPUT / P9_SHOTT_DIRUNIV_CORPUS_DENOMINATOR_NEXT / NO_NEW_MATHEMATICAL_CLAIM','status':'complete_with_scope_p9_shott_diruniv_next','depends_on':[],'related_records':[PLAN_ID,ABX_ID,*IDS,prior],'full_sources':list(dict.fromkeys(P8_SOURCES)),'source_hashes':{x:sha(ROOT/x) for x in dict.fromkeys(P8_SOURCES)},'scope':'P8 freezes Rzk commit 01b081e and six selected docs/tests. It identifies explicit directed input and no P7 K output/claim within that scope. It is not a whole-repo audit, compiler replay, K or HoTT defect.'}
 st['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'P8_RZK_DIRECTED_IMPLEMENTATION_AUDIT_CHECKPOINTED_WITH_SCOPE','status':'complete_with_scope','depends_on':[],'related_records':[P8_ID,PLAN_ID,ABX_ID,prior],'full_sources':[BASE+x for x in ('SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md')]}
 st['execution_control'].update(status='FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_COMPLETE_P9_NEXT',current_phase='PHASE_2_P8_RZK_DEFENSE_P9_SHOTT_DIRUNIV_NEXT',second_phase_status='P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_P5_P6_P7_P8_COMPLETE_P9_NEXT',last_checkpoint_session=SID,checkpoint_result='.codex/cognition/checkpoints/'+SID+'/result.json',next_minimal_verification='P9-SHOTT-DIRUNIV-CORPUS-DENOMINATOR-001. Freeze LIshy2/sHoTT diruniv branch/commit, actual Rzk entry/imports and modal/postulate/formalisation layers; evaluate P7 five K conditions. Explicit structure or a directed-univalence theorem is not K.')
 st['projection']['status']='FOUR_TRACK_FIRST_PASS / P5_P6_P7_P8_COMPLETE / NEXT_P9_SHOTT_DIRUNIV_CORPUS / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM'
 session=f'''# {SID}\n\n- host: Codex desktop local\n- model: GPT-6 Astra；服务端路由未由本项目独立认证\n- tier: T3 state mutation for version-pinned Rzk source audit\n- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST\n- objective: apply P7 K-admission harness to a real directed proof-assistant implementation\n- load_receipt: `audit/p8-directed-type-theory-implementation-discovery-20260921/P8-RZK-CHECKPOINT-PLAN.json`\n- status: COMPLETED_WITH_SCOPE / NOT_A_CONSUMER / DEFENSE_PRESERVES_DIRECTIONAL_INPUT / P9_NEXT\n\nRzk@01b081e is a real source-pinned directed/simplicial implementation. Its selected docs make direction/source/target/order/shape explicit and do not give a P7 bare-input-to-Done_s commitment. P9 is selected from the distinct sHoTT diruniv corpus named by Rzk itself.\n\n| element | use | effect on this unit |\n|---|---|---|\n| P7 admission harness | used | rules out a title-only or primitive-only K claim |\n| git ls-remote + detached clone | used | fixed source identity and selected source bytes |\n| local historical search | used | records Riehl–Shulman/Rzk prior awareness without treating it as completed audit |\n| Rzk compiler | not run | source audit does not certify external build/runtime |\n'''
 runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[{'kind':'p8-source-freeze-and-k-admission-verification','command':'git ls-remote https://github.com/rzk-lang/rzk.git HEAD; git clone --depth=1 rzk; selected-source hash/lexical checks; local P1–P8 verifiers','result':'PASS_WITH_SCOPE; Rzk frozen six-file scope is explicit-direction defense, not K','mathematics':'NOT_A_NEW_KERNEL_RUN'}],'new_math_claims':[],'new_kernel_replay':False,'scope':'P8 version-pinned external source audit only.'}
 drow='| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：P8 Rzk防御与P9 sHoTT语料 | 用户要求每wave做外部与本地侦察 | `FIRST_PASS_COMPLETE / P5_P6_P7_P8_COMPLETE / NEXT_P9_SHOTT_DIRUNIV_CORPUS / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1–P8 | P9固定sHoTT diruniv代码/依赖并跑五条件 | `HoTT后续研究总体方案.md`；P8 report；revision228 receipt |'
 arow='| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P8 Rzk防御后的P9 sHoTT语料 | H/R/K、P1–P8 | `NO_ACTUAL_K_IN_TESTED_DENOMINATORS / P8_RZK_DEFENSE / NEXT_P9_SHOTT_DIRUNIV` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P8 | 分离modal/postulate/formalisation与实际K | `ABX行动.md`；P8 report；revision228 receipt |'
 prow='| `OUT-HOTT-FOUR-TRACK-PLAN` | P8 Rzk有向实现审计 | `DIR-U-HOTT-FOUR-TRACK` | Rzk@01b081e README、directed interval/cube/data/tests | `NOT_A_CONSUMER / DEFENSE_PRESERVES_DIRECTIONAL_INPUT / P9_NEXT` | 定向source/target/order显式输入；无固定原圆环Done承诺 | 不证明Rzk全库、K或HoTT缺陷 | `audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-REPORT.md`；revision228 receipt |'
 aprow='| `OUT-ABX-ACTION-INTAKE` | ABX P8 Rzk实际实现分母 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P7五项判别、Rzk@01b081e六文件 | `NOT_A_CONSUMER / P9_SHOTT_DIRUNIV_NEXT` | 显式结构防御；Rzk指向sHoTT为不同语料分母 | 不证明全库无K、K或HoTT缺陷 | `ABX行动.md`；P8 report；revision228 receipt |'
 mem='P8 Rzk 实现审计已完成：Rzk@01b081e的固定六文件显式给出directed interval source/target/order/shape，未给原圆环U_bare→Done_s，判为NOT_A_CONSUMER/DEFENSE。当前P9冻结Rzk所指sHoTT diruniv语料，须分开modal/postulate/formalisation与实际K。入口：`audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-REPORT.md`；revision228 checkpoint。'
 frontier='- P8 Rzk@01b081e 已完成：显式direction/source/target/shape是防御，无原圆环Done承诺。当前P9固定sHoTT diruniv corpus，分离modal/postulate/formalisation与实际K，并逐项跑P7五条件。入口：`audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-REPORT.md`。'
 resume='当前 active goal 在P8后继续：Rzk@01b081e固定六文件是显式有向输入防御，非K。P9=SHOTT_DIRUNIV_CORPUS_DENOMINATOR：冻结LIshy2/sHoTT diruniv branch/commit/entry/imports，分离modal/postulate/formalisation，然后以P7五项条件检查实际K。入口：`audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-REPORT.md`；revision228 checkpoint。'
 log='\nS-RES-20260921-ASTRA-P8-RZK-DIRECTED-IMPLEMENTATION：P8完成。Rzk@01b081e六文件显式提供有向source/target/order/shape，无原圆环U_bare→Done_s，判NOT_A_CONSUMER/DEFENSE。P9审计sHoTT diruniv关联语料，须固定branch/commit/entry并分离modal/postulate/formalisation；revision228 checkpoint。\n'
 files=[]
 for rel in list(rt.MUTABLE)+list(rt.mutable_shard_paths(ROOT)):
  raw=(ROOT/rel).read_bytes();b=raw.decode()
  if rel==rt.STATE:b=rt.dump(st).decode()
  elif rel==rt.DIRECTION:b=repl(repl(repl(b,'source_state_revision: 227','source_state_revision: 228'),'projection_generation: 20260921-direction-227','projection_generation: 20260921-direction-228'),'semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_COMPLETE_P8_DIRECTED_IMPLEMENTATION_DISCOVERY_NEXT','semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_COMPLETE_P9_SHOTT_DIRUNIV_NEXT')
  elif rel==rt.PANORAMA:b=repl(repl(repl(b,'source_state_revision: 227','source_state_revision: 228'),'projection_generation: 20260921-outcome-227','projection_generation: 20260921-outcome-228'),'semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_COMPLETE_P8_DIRECTED_IMPLEMENTATION_DISCOVERY_NEXT','semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_P7_P8_COMPLETE_P9_SHOTT_DIRUNIV_NEXT')
  elif rel=='方向追踪/002 - 治理与用户方向.md':b=row(row(b,'| `DIR-U-HOTT-FOUR-TRACK` |',drow),'| `DIR-U-ABX-ORIGINAL-CIRCLE` |',arow)
  elif rel=='全景视野/003 - 当前机器证明包与原生重放.md':b=row(row(b,'| `OUT-HOTT-FOUR-TRACK-PLAN` |',prow),'| `OUT-ABX-ACTION-INTAKE` |',aprow)
  elif rel=='MEMORY/001 - 当前执行队列.md':b=row(b,'P7 K admission harness 已完成：',mem)
  elif rel=='MEMORY/003 - 当前验证状态与顺序日志.md':b+=log
  elif rel==rt.PREFIX+'FRONTIER.md':b=repl(b,'- P7 K harness 已完成：未来候选必须通过 K-input/K-output/K-claim/K-forgetting/K-version。当前P8在公开directed/simplicial type-theory实现或消费者中选择一个版本固定分母；显式结构输入或论文标题只构成防御/线索。入口：`audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md`。',frontier)
  elif rel==rt.PREFIX+'RESUME.md':b=repl(b,'当前 active goal 在P7后继续：P7以OriginDirectedDiagram和五项K admission条件把R接到真实消费者审计。P8=DIRECTED_TYPE_THEORY_IMPLEMENTATION_DISCOVERY：先做公开/本地资产侦察，固定一个实际版本/入口/调用链，再逐项检验bare输入、输出、Done承诺、forgetting与版本；没有五项直接证据不是K。入口：`audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md`；revision227 checkpoint。',resume)
  files.append({'path':rel,'expected_sha256':rt.sha(raw),'text':b})
 for n,b in (('SESSION.md',session),('RUNS.json',rt.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',core_audit(st['current_core']))):files.append({'path':BASE+n,'expected_sha256':None,'text':b})
 payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':[PLAN_ID],'authorization':'用户已授权当前唯一AI按goal-3持续推进、做外部/本地侦察、维护current state与canonical checkpoint；不启动Sub Agent、不push、不发布。','files':files};(OUT/'P8-RZK-checkpoint-payload.json').write_bytes(rt.dump(payload));res=rt.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply);(OUT/('P8-RZK-checkpoint-apply.json' if args.apply else 'P8-RZK-checkpoint-dry-run.json')).write_bytes(rt.dump(res));print(json.dumps({k:v for k,v in res.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__':main()
