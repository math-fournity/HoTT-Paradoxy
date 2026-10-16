#!/usr/bin/env python3
"""Checkpoint P27 discovery and route the P28 CFTT corpus audit."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = "S-RES-20260921-ASTRA-P27-REFLECTION-CONSUMER-DISCOVERY"
BASE = f".codex/research/hott/sessions/{SID}/"
PLAN = "R-HOTT-FOUR-TRACK-PLAN-20260921"
P26 = "R-P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-20260921"
P27 = "R-P27-REFLECTION-CONSUMER-DISCOVERY-2026-001"
DIR = "audit/p27-reflection-consumer-discovery-20260921"
SOURCES = (
    f"{DIR}/P27-REFLECTION-CONSUMER-DISCOVERY-REPORT.md",
    f"{DIR}/P27-REFLECTION-CONSUMER-SOURCE-FREEZE.json",
    f"{DIR}/verify_p27_reflection_consumer_discovery.py",
    f"{DIR}/P27-REFLECTION-CONSUMER-DISCOVERY-VERIFICATION.json",
)

def h(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()

def runtime():
    spec=importlib.util.spec_from_file_location("runtime",ROOT/".codex/tools/cognition_runtime.py");assert spec and spec.loader
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def editor():
    sys.path.insert(0,str(ROOT/"scripts/audit"));import projection_edit;return projection_edit

def audit(core: dict) -> str:
    rows=re.findall(r"^### (KC-\d+) · .*? · (.+)$",(ROOT/"核心认知.md").read_text(),re.M);assert len(rows)==46
    head=f"# {SID} 核心认知回评\n\n{core['generation']}；46 条。兼容单文件审计仍登记 `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`。\n\n"
    head+="- core_change: NO\n- direction_change: P27 selected CFTT P28; P3/P4 remain parked.\n- panorama_change: local discovery asset promoted to a version-pinned source candidate.\n- essay_change: NO\n- update_decision: P27 closes only discovery and routes a distinct quote/splice consumer audit.\n- cross_conflicts: no actual HoTT defect or global self-validation consumer established.\n- unresolved: P28 source audit and wider reflection-consumer search remain open.\n- writer_compatibility: G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001.\n\n| KC | 主题 | relation | 本单元判断 | 证据、反证条件 |\n|---|---|---|---|---|\n"
    for kc,title in rows:
        rel="DEEPENED" if kc in {"KC-000025","KC-000026","KC-000028","KC-000036","KC-000041","KC-000043","KC-000045","KC-000046"} else "NOT_TOUCHED"
        text="P27以source/consumer而非关键词选择P28。" if rel=="DEEPENED" else "P27未直接检验该用户原文。"
        head+=f"| `{kc}` | {title} | `{rel}` | {text} | P27 report；P28不同源码可反证。 |\n"
    return head+"\n## 波次定位\n\nP27把本地未审的CFTT题录升级为版本固定候选；P28的quote/splice/unstaging操作不同于前面三个syntax分母。\n"

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--apply',action='store_true');args=ap.parse_args();r=runtime();e=editor()
    assert all((ROOT/x).is_file() for x in SOURCES)
    st=json.loads((ROOT/r.STATE).read_text());assert st['revision']==243 and st['latest_session']=='S-RES-20260921-ASTRA-P26-TTASQIIRT-CORPUS'
    hd=json.loads((ROOT/r.HEAD).read_text());assert all(h(ROOT/p)==v for p,v in hd['tracked'].items())
    plan=r.plan(ROOT,profile='research',task_ids=[PLAN]);(OUT/'P27-CHECKPOINT-PLAN.json').write_bytes(r.dump(plan))
    st['revision'] = 244
    st['latest_session'] = SID
    p = st['records'][PLAN]
    p['related_records'] = list(dict.fromkeys(p.get('related_records', []) + [P27, SID]))
    p['status'] = 'four_track_p3_paused_p1_expression_p4_not_triggered_p22_parked_p28_cftt_next'
    p['evidence_status'] = ('P3_PAUSED_SAME_CLASS / P1_MINIMAL_EXPRESSIBILITY_POSITIVE_CONTROL / '
                            'P4_NOT_TRIGGERED_BY_TRANSLATION_GAP_ALONE / P22_GUARDED_BRIDGE_PARKED / '
                            'P27_CFTT_STAGED_CANDIDATE_SELECTED / P28_CFTT_SOURCE_AUDIT_NEXT / GOAL_ACTIVE')
    p['full_sources'] = list(dict.fromkeys(p.get('full_sources', []) + list(SOURCES)))
    p['source_hashes'].update({source: h(ROOT/source) for source in p['full_sources'] if (ROOT/source).is_file()})
    p['revalidation'] = p.get('revalidation', '') + ' Revision244 records P27 CFTT discovery and routes P28 source audit; P26 source scope unchanged.'
    st['records'][P27] = {
        'kind': 'result', 'path': SOURCES[0], 'lifecycle_status': 'CURRENT',
        'evidence_status': 'SUCCESSOR_SELECTED / CFTT_STAGED_QUOTATION_SPLICE_AND_UNSTAGING_CONSUMER_CANDIDATE / LOCAL_DISCOVERY_UNREVIEWED_ASSET_UPGRADED_TO_VERSION_PINNED_CANDIDATE / P28_NOT_STARTED / NO_NEW_HOTT_DEFECT_CLAIM',
        'status': 'complete_with_scope', 'depends_on': [], 'related_records': [PLAN, P26, SID],
        'full_sources': list(SOURCES), 'source_hashes': {source: h(ROOT/source) for source in SOURCES},
        'scope': 'P27 selects an external source candidate only; it does not audit CFTT code or establish a HoTT claim.',
    }
    st['records'][SID] = {
        'kind': 'session', 'path': BASE+'SESSION.md', 'lifecycle_status': 'HISTORICAL',
        'evidence_status': 'P27_DISCOVERY_CHECKPOINTED_WITH_SCOPE', 'status': 'complete_with_scope',
        'depends_on': [], 'related_records': [PLAN, P26, P27],
        'full_sources': [BASE+x for x in ('SESSION.md', 'RUNS.json', 'CORE_COGNITION_AUDIT.md')],
    }
    st['execution_control'].update({
        'status': 'FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_P22_PARKED_P28_CFTT_NEXT',
        'current_phase': 'PHASE_2_P27_CFTT_DISCOVERY_P28_STAGED_QUOTATION_AUDIT_NEXT',
        'second_phase_status': 'P3_PAUSED_P1_POSITIVE_CONTROL_P4_NOT_TRIGGERED_GUARD_PARKED_P28_NEXT',
        'last_checkpoint_session': SID,
        'checkpoint_result': f'.codex/cognition/checkpoints/{SID}/result.json',
        'next_minimal_verification': ('P28-CFTT-STAGED-QUOTATION-SPLICE-UNSTAGING-CORPUS-001. At fixed staged main '
                                      '9c4e2017669086e2f77df5014f1c215a5a7e07a3, inspect the exact Agda code supplement '
                                      'for object/meta stages, quotation, splicing, unstaging, generativity, host reflection and any '
                                      'object proof-predicate/self-soundness claim. Freeze Input/Operation/Observation/Done; do not '
                                      'turn staged code into a HoTT self-validation conclusion.'),
    })
    st['projection']['status'] = ('FOUR_TRACK_P3_PAUSED_P1_EXPRESSIBLE_P4_NOT_TRIGGERED_GUARD_PARKED / '
                                  'P27_CFTT_CANDIDATE_SELECTED / NEXT_P28_CFTT_AUDIT / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM')

    memory=e.load(ROOT, 'MEMORY.md');directions=e.load(ROOT, '方向追踪.md');panorama=e.load(ROOT, '全景视野.md');essay=e.load(ROOT, '扩展认知.md')
    old_queue = ('P26 已确认 TTasQIIRT 的 native QIIRT intrinsic syntax和主入口可检查，但对象proof-predicate/global self-validation未建立；入口还带 UIP、TERMINATING和安全配置边界。下一=P27：在未审公开/本地来源中寻找实际 object proof-predicate/quotation/reflection/self-soundness consumer；P3/P1/P4/Guard继续停放。入口：`audit/p26-ttasqiirt-intrinsic-type-theory-corpus-20260921/P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-REPORT.md`；revision243。')
    new_queue = ('P27 已将本地未审 CFTT 题录升级为版本固定 staged quote/splice/unstaging 候选。下一=P28：固定 staged@`9c4e2017669086e2f77df5014f1c215a5a7e07a3` 审计 Agda code supplement 的对象/元层、quotation/splicing/unstaging与任何proof-predicate/self-soundness；P3/P1/P4/Guard继续停放。入口：`audit/p27-reflection-consumer-discovery-20260921/P27-REFLECTION-CONSUMER-DISCOVERY-REPORT.md`；revision244。')
    e.replace_in_shard(memory, 'MEMORY/001 - 当前执行队列.md', old_queue, new_queue)
    e.append_to_shard(memory, 'MEMORY/003 - 当前验证状态与顺序日志.md', '\nS-RES-20260921-ASTRA-P27-REFLECTION-CONSUMER-DISCOVERY：CFTT DOI资产从DISCOVERY_UNREVIEWED升级为P28版本固定候选；revision244。\n')

    e.replace_in_index(directions, 'source_state_revision: 243', 'source_state_revision: 244')
    e.replace_in_index(directions, 'projection_generation: 20260921-direction-243', 'projection_generation: 20260921-direction-244')
    e.replace_in_index(directions, 'semantic_status: FOUR_TRACK_P26_INTRINSIC_SYNTAX_SCOPED_P27_REFLECTION_CONSUMER_DISCOVERY_NEXT', 'semantic_status: FOUR_TRACK_P27_CFTT_CANDIDATE_P28_AUDIT_NEXT')
    e.replace_in_shard(directions, '方向追踪/002 - 治理与用户方向.md',
        '| `DIR-U-HOTT-FOUR-TRACK` | P26：TTasQIIRT native intrinsic syntax审计 | P25/P26 | `P27_REFLECTION_CONSUMER_DISCOVERY_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN` | 内在syntax正控制，强self-validation仍缺 | P26 report；revision243 |',
        '| `DIR-U-HOTT-FOUR-TRACK` | P27：CFTT反射消费者发现 | P26/P27 | `P28_CFTT_STAGED_AUDIT_NEXT / GOAL_ACTIVE` | `PARADOX_DISCOVERY` | `OUT-HOTT-FOUR-TRACK-PLAN` | 选定quote/splice/unstaging实际consumer | P27 report；revision244 |')
    e.replace_in_shard(directions, '方向追踪/002 - 治理与用户方向.md',
        '| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P26 | `P3_PAUSED / INDEPENDENT_P27_DISCOVERY` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P26 reports；revision243 |',
        '| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX 原圆环 P3 实际消费者分支停放 | P21/P27 | `P3_PAUSED / INDEPENDENT_P28_AUDIT` | `EVIDENCE_DISCIPLINE` | `OUT-ABX-ACTION-INTAKE` | 仅新版本固定实际 K 或强 R 才重开 | P21/P27 reports；revision244 |')

    e.replace_in_index(panorama, 'source_state_revision: 243', 'source_state_revision: 244')
    e.replace_in_index(panorama, 'projection_generation: 20260921-outcome-243', 'projection_generation: 20260921-outcome-244')
    e.replace_in_index(panorama, 'semantic_status: FOUR_TRACK_P26_INTRINSIC_SYNTAX_SCOPED_P27_REFLECTION_CONSUMER_DISCOVERY_NEXT', 'semantic_status: FOUR_TRACK_P27_CFTT_CANDIDATE_P28_AUDIT_NEXT')
    e.replace_in_shard(panorama, '全景视野/003 - 当前机器证明包与原生重放.md',
        '| `OUT-HOTT-FOUR-TRACK-PLAN` | P26 TTasQIIRT native intrinsic syntax审计 | `DIR-U-HOTT-FOUR-TRACK` | P25/P26 | `P26_SCOPED / P27_NEXT` | 内在syntax/NbE不等于object provability/global self-validation | 不证明HoTT缺陷 | P26 report；revision243 |',
        '| `OUT-HOTT-FOUR-TRACK-PLAN` | P27 CFTT反射消费者发现 | `DIR-U-HOTT-FOUR-TRACK` | P26/P27 | `P27_SELECTED / P28_NEXT` | 版本固定quote/splice/unstaging consumer待审 | 不证明HoTT缺陷 | P27 report；revision244 |')
    e.replace_in_shard(panorama, '全景视野/003 - 当前机器证明包与原生重放.md',
        '| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，独立 P26 已完成 | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26 | `P3_PAUSED / P27_DISCOVERY_NEXT` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P26 reports；revision243 |',
        '| `OUT-ABX-ACTION-INTAKE` | ABX P3停放，独立 P27已选 CFTT | `DIR-U-ABX-ORIGINAL-CIRCLE` | P15/P17/P19/P20/P22/P25/P26/P27 | `P3_PAUSED / P28_AUDIT_NEXT` | 避免重复，保留新实际K重开条件 | 不证明原M/N桥 | P21/P27 reports；revision244 |')
    e.append_to_shard(panorama, '全景视野/006 - ERCF-3 与 T3 脉冲及失败台账.md', '\n## P27：CFTT reflection-consumer discovery（revision244）\n\n在本地未审文献资产中发现并版本固定CFTT staged quote/splice/unstaging source candidate；P28审计代码，不将其预判为HoTT自验证。\n')
    e.append_to_shard(panorama, '全景视野/008 - 当前未完成.md', '\n10. `P28-CFTT-STAGED-QUOTATION-SPLICE-UNSTAGING-CORPUS-001`：固定CFTT staged source的quote/splice/unstaging、generativity与对象proof-predicate/self-soundness审计。\n')

    simple={rel:(ROOT/rel).read_text() for rel in r.MUTABLE if rel not in {r.STATE,'MEMORY.md','方向追踪.md','全景视野.md','扩展认知.md'}}
    simple[r.PREFIX+'FRONTIER.md']=simple[r.PREFIX+'FRONTIER.md'].replace('- P26确认 TTasQIIRT@`8db08306287333067b2749f95f8ad3ba7a0e14d1` 的native intrinsic syntax与默认入口接受；它没有object proof-predicate/global self-validation，且有UIP/TERMINATING/安全边界。下一P27在不同2025–2026来源中发现实际反射consumer；不重审停放分支。入口：`audit/p26-ttasqiirt-intrinsic-type-theory-corpus-20260921/P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-REPORT.md`。', '- P27从本地未审CFTT题录与公开source选择staged@`9c4e2017669086e2f77df5014f1c215a5a7e07a3`；P28审计actual quote/splice/unstaging consumer，不预判为HoTT self-validation。入口：`audit/p27-reflection-consumer-discovery-20260921/P27-REFLECTION-CONSUMER-DISCOVERY-REPORT.md`。',1)
    simple[r.PREFIX+'RESUME.md']=simple[r.PREFIX+'RESUME.md'].replace('当前 active goal 在P26后继续：TTasQIIRT@`8db08306287333067b2749f95f8ad3ba7a0e14d1` 的native QIIRT syntax和默认入口已核，但对象proof-predicate/global self-validation未建立，且UIP/TERMINATING/安全配置边界明示。P27对不同2025–2026来源做反射消费者发现；不重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p26-ttasqiirt-intrinsic-type-theory-corpus-20260921/P26-TTASQIIRT-INTRINSIC-TYPE-THEORY-CORPUS-REPORT.md`；revision243。','当前 active goal 在P27后继续：本地未审CFTT题录已以staged@`9c4e2017669086e2f77df5014f1c215a5a7e07a3`版本固定，P28审计其quote/splice/unstaging和actual object/meta boundary；不重审P3/P1最小接口/跨后端/Guard停放分支。入口：`audit/p27-reflection-consumer-discovery-20260921/P27-REFLECTION-CONSUMER-DISCOVERY-REPORT.md`；revision244。',1)
    rows=[]
    for doc in (memory,directions,panorama,essay): rows+=e.payload_rows(doc,ROOT)
    seen={x['path'] for x in rows}
    for rel in r.MUTABLE:
        if rel not in seen: rows.append({'path':rel,'expected_sha256':h(ROOT/rel),'text':r.dump(st).decode() if rel==r.STATE else simple[rel]})
    session=f"# {SID}\n\n- host: codex-desktop\n- model: runtime-model-not-certified-by-tool\n- tier: T3\n- status: `P27_DISCOVERY_CHECKPOINTED_WITH_SCOPE / P28_CFTT_AUDIT_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`\n- load_receipt: research plan snapshot `{plan['snapshot']}`; P27 local and public source reconnaissance.\n- authorization: 用户已授权按 goal-3 持续推进、公开/本地侦察和 checkpoint；不启动 Sub Agent、不 push、不发布。\n"
    runs={'schema_version':'hott-session-runs/v1','session_id':SID,'primary_runs':[{'kind':'P27 discovery verifier','result':'PASS_WITH_SCOPE'},{'kind':'public source pin','result':'staged main 9c4e201 recorded'}],'new_math_claims':[],'new_kernel_replay':False}
    rows += [{'path':BASE+'SESSION.md','expected_sha256':None,'text':session},{'path':BASE+'RUNS.json','expected_sha256':None,'text':r.dump(runs).decode()},{'path':BASE+'CORE_COGNITION_AUDIT.md','expected_sha256':None,'text':audit(st['current_core'])}]
    payload={'schema_version':'cognition-checkpoint/v1','session_id':SID,'load_profile':'research','task_ids':[PLAN],'authorization':'用户已授权按goal-3持续推进、公开/本地侦察和checkpoint；不启动Sub Agent、不push、不发布。','files':rows}
    (OUT/'P27-CHECKPOINT-PAYLOAD.json').write_bytes(r.dump(payload))
    result=r.checkpoint(ROOT,plan['snapshot'],payload,apply=args.apply)
    (OUT/('P27-CHECKPOINT-APPLY.json' if args.apply else 'P27-CHECKPOINT-DRY-RUN.json')).write_bytes(r.dump(result))
    print(json.dumps({key:value for key,value in result.items() if key!='paths'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
