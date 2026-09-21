#!/usr/bin/env python3
"""Checkpoint P16 source selection and route P17."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, re, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=Path(__file__).resolve().parent
SID='S-RES-20260921-ASTRA-P16-FOURTH-SUCCESSOR-DISCOVERY'; BASE=f'.codex/research/hott/sessions/{SID}/'
PLAN='R-HOTT-FOUR-TRACK-PLAN-20260921'; ABX='R-ABX-ACTION-20260921'; P15='R-P15-PRIETO-CUBIDES-SPHERICAL-MAPS-AGDA-CORPUS-20260921'; P16='R-P16-FOURTH-SUCCESSOR-DISCOVERY-20260921'
REPORT='audit/p16-fourth-successor-discovery-20260921/P16-FOURTH-SUCCESSOR-DISCOVERY-REPORT.md'; FREEZE='audit/p16-fourth-successor-discovery-20260921/P16-CUBICAL-CAUCHY-REALS-CANDIDATE-FREEZE.json'; VERIFY='audit/p16-fourth-successor-discovery-20260921/verify_p16_fourth_successor_discovery.py'; RECEIPT='audit/p16-fourth-successor-discovery-20260921/P16-FOURTH-SUCCESSOR-DISCOVERY-VERIFICATION.json'; SCRIPT='audit/p16-fourth-successor-discovery-20260921/checkpoint_p16_fourth_successor_discovery.py'
SOURCES=(REPORT,FREEZE,VERIFY,RECEIPT,SCRIPT,'goal.md','goal-3.md','feature-list.md','rulings.md','ABX行动.md','HoTT后续研究总体方案.md','HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md','audit/literature/LIT-DENOMINATOR-001/discovery-20260914/DISCOVERY-CANDIDATES.json','audit/literature/LIT-DENOMINATOR-001/discovery-20260914/TRIAGE.json')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def row(t,p,v):
    a=t.splitlines()
    for i,x in enumerate(a):
        if x.startswith(p): a[i]=v; return '\n'.join(a)+'\n'
    raise AssertionError(p)
def audit(core):
    hs=re.findall(r'^### (KC-\d+) · .*? · (.+)$',(ROOT/'核心认知.md').read_text(),re.M); assert len(hs)==core['kc_count']==46
    s=f'# {SID} 核心认知回评\n\n{core["generation"]}；46 条。\n\n- core_change: NO\n- direction_change: P16_CUBICAL_CAUCHY_REALS_CANDIDATE_SELECTED_P17_NEXT\n- panorama_change: REAL_LAYER_ACTUAL_FORMALISATION_CANDIDATE_SELECTED\n- essay_change: NO\n- update_decision: P16 freezes an unreviewed real-layer candidate for P17 rather than treating a title or abstract as a K verdict.\n- cross_conflicts: Cauchy-real construction is not yet task-equivalent to P13 M/N Done.\n- unresolved: P17 source audit, task equivalence, actual K and HoTT-defect conclusion remain open.\n- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.\n\n| KC | 主题 | relation | 本单元判断 | 证据、反证条件 |\n|---|---|---|---|---|\n'
    for n,(k,t) in enumerate(hs,1):
        rel='DEEPENED' if n in {10,15,21,22,35,37,38,39,40,44,45,46} else 'NOT_TOUCHED'
        s+=f'| `{k}` | {t} | {rel} | P16冻结实际Cubical HoTT实数构造候选，未把题名或摘要当作K。 | `{REPORT}`；P17发现真实bare-H-to-Done桥才改变。 |\n'
    return s+'\n## 波次定位\n\nP16为P3实际消费者链选择新的real-layer分母；P17只审固定论文/代码定位，避免重审P15。`SWITCH_BRANCH`。\n'
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--apply',action='store_true'); args=ap.parse_args()
    subprocess.check_call([sys.executable,'-B',VERIFY,'--write'],cwd=ROOT); assert all((ROOT/p).is_file() for p in SOURCES)
    spec=importlib.util.spec_from_file_location('r',ROOT/'.codex/tools/cognition_runtime.py'); r=importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
    st=json.loads((ROOT/r.STATE).read_text()); assert st['revision']==235 and st['latest_session']=='S-RES-20260921-ASTRA-P15-PRIETO-CUBIDES-CORPUS'
    h=json.loads((ROOT/r.HEAD).read_text()); assert all(sha(ROOT/p)==v for p,v in h['tracked'].items())
    plan=r.plan(ROOT,profile='research',task_ids=[PLAN]); (OUT/'P16-CHECKPOINT-PLAN.json').write_bytes(r.dump(plan))
    st['revision']=236; st['latest_session']=SID
    for ident in (PLAN,ABX,P15):
        q=st['records'][ident]; q['related_records']=list(dict.fromkeys(q.get('related_records',[])+[P16,SID])); q['revalidation']=q.get('revalidation','')+' Revision236 records P16 Cauchy-reals candidate selection; prior scope unchanged.'
    p=st['records'][PLAN]; p.update(status='four_track_p16_cubical_cauchy_reals_candidate_selected_p17_next',evidence_status='P16_CUBICAL_CAUCHY_REALS_CANDIDATE_SELECTED / P17_CAUCHY_REALS_CORPUS_NEXT / GOAL_ACTIVE'); p['full_sources']=list(dict.fromkeys(p.get('full_sources',[])+list(SOURCES))); p['source_hashes'].update({x:sha(ROOT/x) for x in p['full_sources'] if (ROOT/x).is_file()})
    a=st['records'][ABX]; a['full_sources']=list(dict.fromkeys(a.get('full_sources',[])+list(SOURCES))); a['source_hashes'].update({x:sha(ROOT/x) for x in a['full_sources'] if (ROOT/x).is_file()}); a['revalidation']='Revision236 selects a distinct real-layer actual formalisation for P17; no K yet.'
    st['records'][P16]={'kind':'result','path':REPORT,'lifecycle_status':'CURRENT','evidence_status':'SUCCESSOR_SELECTED / CUBICAL_HOTT_CAUCHY_REALS_ACTUAL_FORMALISATION_CANDIDATE / P17_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM','status':'complete_with_scope_p17_cauchy_reals_corpus_next','depends_on':[],'related_records':[PLAN,ABX,P15],'full_sources':list(SOURCES),'source_hashes':{x:sha(ROOT/x) for x in SOURCES},'scope':'P16 only selects an unreviewed version-pinned real-layer candidate.'}
    st['records'][SID]={'kind':'session','path':BASE+'SESSION.md','lifecycle_status':'HISTORICAL','evidence_status':'P16_SUCCESSOR_DISCOVERY_CHECKPOINTED_WITH_SCOPE','status':'complete_with_scope','depends_on':[],'related_records':[P16,PLAN,ABX],'full_sources':[BASE+x for x in ('SESSION.md','RUNS.json','CORE_COGNITION_AUDIT.md')]}
    st['execution_control'].update(status='FOUR_TRACK_P16_CUBICAL_CAUCHY_REALS_CANDIDATE_SELECTED_P17_NEXT',current_phase='PHASE_2_P16_COMPLETE_P17_CAUCHY_REALS_CORPUS_NEXT',second_phase_status='P1_TO_P16_COMPLETE_P17_NEXT',last_checkpoint_session=SID,checkpoint_result=f'.codex/cognition/checkpoints/{SID}/result.json',next_minimal_verification='P17-CUBICAL-HOTT-CAUCHY-REALS-CORPUS-001. Read only arXiv 2604.24782v1, direct paper sections and a fixed public code locator if available. Apply P7 to the actual Cauchy-real construction; distinguish explicit approximations/relations/HIT-HII/truncation/choice conditions from bare H_intrinsic and P13 Done. Do not compile, clone or broaden source scope.')
    st['projection']['status']='FOUR_TRACK_P16_CUBICAL_CAUCHY_REALS_CANDIDATE_SELECTED / NEXT_P17_CAUCHY_REALS_CORPUS / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM'
    dr='| `DIR-U-HOTT-FOUR-TRACK` | P16实数层候选与P17语料审计 | 用户要求双重侦察 | `P16_CAUCHY_REALS_CANDIDATE_SELECTED / P17_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | P1–P16 | P17审实际实数构造接口 | P16 report；revision236 |'; ar='| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX P16实数层邻接候选 | H/R/K、P16 | `P17_TASK_EQUIVALENCE_PENDING` | `PARADOX_DISCOVERY` | P16 | 先判任务不同或桥 | P16 report；revision236 |'; pr='| `OUT-HOTT-FOUR-TRACK-PLAN` | P16 Cubical Cauchy-real候选 | `DIR-U-HOTT-FOUR-TRACK` | arXiv v1+LIT未审题录 | `SUCCESSOR_SELECTED / P17_NEXT` | 真实real-layer构造候选 | 不证明K或HoTT缺陷 | P16 report；revision236 |'; ap='| `OUT-ABX-ACTION-INTAKE` | ABX P16实数层候选 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P17卡 | `P17_TASK_EQUIVALENCE_PENDING` | 未审实际语料 | 不证明原M/N桥 | P16 report；revision236 |'
    mem='P16已完成：选择2026 Cubical Agda Cauchy-real formalisation为P17版本冻结候选；本地原仅为未审题录。P17先审实际approximation/relation/HIT-HII/truncation/choice接口与P13任务是否可比；不预设K。入口：`audit/p16-fourth-successor-discovery-20260921/P16-FOURTH-SUCCESSOR-DISCOVERY-REPORT.md`；revision236。'
    front='- P16已完成：Cauchy-reals Cubical Agda实际formalisation成为P17候选。P17只审固定论文/代码定位，先判任务等价与显式条件；不预设K。入口：`audit/p16-fourth-successor-discovery-20260921/P16-FOURTH-SUCCESSOR-DISCOVERY-REPORT.md`。'; res='当前 active goal 在P16后继续：P17=CUBICAL_HOTT_CAUCHY_REALS_CORPUS，审arXiv v1和固定公开代码定位，按P7区分Cauchy real构造接口与P13 bare H/Done；不编译、克隆或扩站。入口：`audit/p16-fourth-successor-discovery-20260921/P16-FOURTH-SUCCESSOR-DISCOVERY-REPORT.md`；revision236。'
    files=[]
    for rel in list(r.MUTABLE)+list(r.mutable_shard_paths(ROOT)):
        raw=(ROOT/rel).read_bytes(); t=raw.decode()
        if rel==r.STATE: t=r.dump(st).decode()
        elif rel==r.DIRECTION: t=t.replace('source_state_revision: 235','source_state_revision: 236',1).replace('projection_generation: 20260921-direction-235','projection_generation: 20260921-direction-236',1).replace('semantic_status: FOUR_TRACK_P15_EXPLICIT_MAP_FACE_WALK_DEFENSE_P16_NEXT','semantic_status: FOUR_TRACK_P16_CUBICAL_CAUCHY_REALS_CANDIDATE_SELECTED_P17_NEXT',1)
        elif rel==r.PANORAMA: t=t.replace('source_state_revision: 235','source_state_revision: 236',1).replace('projection_generation: 20260921-outcome-235','projection_generation: 20260921-outcome-236',1).replace('semantic_status: FOUR_TRACK_P15_EXPLICIT_MAP_FACE_WALK_DEFENSE_P16_NEXT','semantic_status: FOUR_TRACK_P16_CUBICAL_CAUCHY_REALS_CANDIDATE_SELECTED_P17_NEXT',1)
        elif rel=='方向追踪/002 - 治理与用户方向.md': t=row(row(t,'| `DIR-U-HOTT-FOUR-TRACK` |',dr),'| `DIR-U-ABX-ORIGINAL-CIRCLE` |',ar)
        elif rel=='全景视野/003 - 当前机器证明包与原生重放.md': t=row(row(t,'| `OUT-HOTT-FOUR-TRACK-PLAN` |',pr),'| `OUT-ABX-ACTION-INTAKE` |',ap)
        elif rel=='MEMORY/001 - 当前执行队列.md': t=row(t,'P15固定 Prieto-Cubides 页面审计已完成：',mem)
        elif rel=='MEMORY/003 - 当前验证状态与顺序日志.md': t+='\nS-RES-20260921-ASTRA-P16-FOURTH-SUCCESSOR-DISCOVERY：P16选择Cubical Cauchy-real候选，P17审计；revision236。\n'
        elif rel==r.PREFIX+'FRONTIER.md': t=row(t,'- P15已完成：',front)
        elif rel==r.PREFIX+'RESUME.md': t=row(t,'当前 active goal 在P15后继续：',res)
        files.append({'path':rel,'expected_sha256':r.sha(raw),'text':t})
    session=f'# {SID}\n\n- tier: T3 source-selection state mutation\n- status: COMPLETED_WITH_SCOPE / P17_NEXT\n'; runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[{'kind':'P16 public/local candidate selection','result':'PASS_WITH_SCOPE','mathematics':'NO_NEW_KERNEL_RUN'}],'new_math_claims':[],'new_kernel_replay':False}
    for n,t in (('SESSION.md',session),('RUNS.json',r.dump(runs).decode()),('CORE_COGNITION_AUDIT.md',audit(st['current_core']))): files.append({'path':BASE+n,'expected_sha256':None,'text':t})
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':[PLAN],'authorization':'用户已授权按goal-3持续推进、公开/本地侦察和checkpoint；不启动Sub Agent、不push、不发布。','files':files}; (OUT/'P16-checkpoint-payload.json').write_bytes(r.dump(payload)); z=r.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply); (OUT/('P16-checkpoint-apply.json' if args.apply else 'P16-checkpoint-dry-run.json')).write_bytes(r.dump(z)); print(json.dumps({k:v for k,v in z.items() if k!='paths'},ensure_ascii=False))
if __name__=='__main__': main()
