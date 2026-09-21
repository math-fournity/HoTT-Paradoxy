#!/usr/bin/env python3
"""Checkpoint the bounded P2 SIP reuse audit and route P3 selection."""

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
SID = 'S-RES-20260921-ASTRA-P2-KTHEORY-SIP'
BASE = '.codex/research/hott/sessions/' + SID + '/'
PLAN_ID = 'R-HOTT-FOUR-TRACK-PLAN-20260921'
ABX_ID = 'R-ABX-ACTION-20260921'
P1_ID = 'R-P1-RMIN-SPEC-20260921'
P2_ID = 'R-P2-KTHEORY-SIP-20260921'
REPORT = 'audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-REPORT.md'
VERIFY = 'audit/p2-ktheory-sip-20260921/verify_p2_ktheory_sip.py'
RECEIPT = 'audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-VERIFICATION.json'
CHECKPOINT = 'audit/p2-ktheory-sip-20260921/checkpoint_p2_ktheory_sip.py'
P1_REPORT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md'
P1_VERIFY = 'audit/p1-rmin-spec-20260921/verify_p1_rmin_spec.py'
P1_RECEIPT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-VERIFICATION.json'
PLAN_VERIFY = 'audit/four-track-plan-20260921/verify_four_track_plan.py'
PLAN_RECEIPT = 'audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json'
PLAN_INDEX = 'HoTT后续研究总体方案.md'
PLAN_SHARDS = tuple(
    'HoTT后续研究总体方案/' + name
    for name in (
        '001 - 上一轮问答与四分支校正.md',
        '002 - 共同任务、术语与优先级原则.md',
        '003 - 分支顺序、准入与停止条件.md',
        '004 - 令牌经济、反漂移与每单元复核.md',
        '005 - 当前第一步与交接.md',
    )
)
BOOK = 'sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/categories.tex'
SIP_SOURCE = 'HoTT/formal/sip-representation/SIPRepresentation.agda'
SIP_RUN = 'HoTT/verification/runs/20260912-MP-SIP-REPRESENTATION-001-01/RUN.json'
SIP_REPORT = 'audit/sip-representation机器证明实施证据-20260912.md'
RELATIONAL = 'sources/webgpt/workspace-snapshot/.codex/research/hott/sessions/S-ANS-20260910-008-RELATIONAL-SIP/PROOF_NOTE.md'
P2_SOURCES = (
    REPORT, VERIFY, RECEIPT, CHECKPOINT,
    P1_REPORT, P1_VERIFY, P1_RECEIPT,
    BOOK, SIP_SOURCE, SIP_RUN, SIP_REPORT, RELATIONAL,
    PLAN_INDEX, *PLAN_SHARDS, PLAN_VERIFY, PLAN_RECEIPT,
    'goal.md', 'goal-3.md', 'feature-list.md', 'rulings.md',
    'ABX行动.md', 'ABX行动/005 - 状态、停止条件与未来交接.md',
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(body: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, body, count=1)
    assert count == 1, old
    return result


def replace_line(body: str, prefix: str, replacement: str) -> str:
    lines = body.splitlines()
    hits = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    lines[hits[0]] = replacement
    return '\n'.join(lines) + '\n'


def core_audit(core: dict) -> str:
    headings = re.findall(r'^### (KC-\d+) · .*? · (.+)$', (ROOT / '核心认知.md').read_text(), re.M)
    assert len(headings) == core['kc_count'] == 46
    deepened = {1, 2, 3, 5, 10, 14, 19, 21, 22, 31, 34, 35, 37, 41, 42, 43, 44, 45, 46}
    corrected = {15, 38, 39, 40}
    body = f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P2_SIP_REUSE_AUDITED_AND_P3_DENOMINATOR_SELECTION_ROUTED
- panorama_change: BOOK_SIP_EXPLICIT_STRUCTURE_PRESERVATION_AND_HISTORICAL_ASSET_SCOPE_REGISTERED
- essay_change: NO
- update_decision: P2 已关闭；P3 只能先选择一个未覆盖、版本固定的实际消费者分母，不能把 SIP 本身当 consumer
- cross_conflicts: 旧原生 SIP 边界、Book 的一般结构定理、历史关系模型、当前 P1 圆环任务、实际消费者和现实解释具有不同输入与证据等级；名称相同不构成覆盖
- unresolved: 实际版本固定 K_app、同任务失配、完整 OriginTop/物理过程、实现语义差异和独立非现实性判词仍未解决

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
'''
    for number, (kc, title) in enumerate(headings, 1):
        if number in corrected:
            relation = 'CORRECTED'
            judgement = 'P2 以 Book 原文和已有 SIP 正控制排除“结构同一性自动替强完成签字”的读法；不把理论保护机制重新叙述为缺陷。'
            evidence = f'{REPORT}；{RECEIPT}；实际消费者将裸 H/U 提升到 P1 Done_s 才改变此范围。'
        elif number in deepened:
            relation = 'DEEPENED'
            judgement = 'P2 把理论结构保持、现有机器证据和 P1 来源—操作—完成合同逐字段比较，并实施历史资产侦察以避免重复。'
            evidence = f'{REPORT}；{RECEIPT}；P3 版本固定调用链是下一可能改变最终链的证据。'
        else:
            relation = 'NOT_TOUCHED'
            judgement = '本单元只审计 Book §9.8 与先前 SIP 资产的规则级范围，不重新裁决本条独立用户原文。'
            evidence = 'goal.md §2；无新数学定理或现实结论。'
        body += f'| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n'
    body += '''
## 扩展认知逐片复认

001–008：P2 不把“抽象层遗漏的资料”直接定为理论错误。它检验的具体规则恰恰要求结构保持，并将所需观察加入签名作为正控制；因而当前应转向实际使用链，而不是围绕同一规则重复构造。

## 波次定位

- 最终目标连接：P2 检验最终见证链的规则级桥边，排除 Book §9.8 的 SIP 作为裸 H/U→Done_s 桥。
- 全局坐标：P1 已固定共同规格；P2 通过本地资产侦察复用而未重跑既有 SIP 边界；P3 现在获得“选择实际消费者分母”的资格；P4 未触发。
- 实际价值：发现并正确定级了历史 WebGPT/LocalGPT/SIP 资产，避免重做 C-124–C-128 或有限关系模型，同时给 P3 提供明确防御对照。
- 继续检验：继续 SIP 只有在出现具体版本、明确不同的 SIP 规则或实际 K 承诺时才有新分母；没有这种 ingress，更多 toy example 不改变结论。
- 不延续理由：Book 原文、既有 kernel control、历史关系审查与外部 SIP 文献都指向显式结构保持；当前未覆盖链边是实际消费者，不是理论规则。
- 裁决：CLOSE_WITH_SCOPE；SWITCH_BRANCH 到 P3-KAPP-DENOMINATOR-001。

## 停止裁决

P2 结束。P3 的第一动作只是对未覆盖外部实际消费者作资产与学术侦察并冻结分母；找不到合格分母也可形成有界停止，不得自动进入引擎审计或将 SIP 解释为 HoTT 缺陷。
'''
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()

    subprocess.check_call([sys.executable, '-B', P1_VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', PLAN_VERIFY, '--write'], cwd=ROOT)
    for rel in P2_SOURCES:
        assert (ROOT / rel).is_file(), rel

    spec = importlib.util.spec_from_file_location('runtime', ROOT / '.codex/tools/cognition_runtime.py')
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state['revision'] == 220
    assert state['latest_session'] == 'S-RES-20260921-ASTRA-P1-RMIN-SPEC'
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head['tracked'].items())
    plan = runtime.plan(ROOT, profile='research', task_ids=[PLAN_ID])
    assert set(plan['review_required']) <= {PLAN_ID, ABX_ID, P1_ID}
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (OUT / 'P2-KTHEORY-SIP-CHECKPOINT-PLAN.json').write_bytes(runtime.dump(plan))
    for rel in (P1_RECEIPT, RECEIPT, PLAN_RECEIPT):
        assert json.loads((ROOT / rel).read_text())['status'] == 'PASS_WITH_SCOPE'

    prior_latest = state['latest_session']
    state['revision'] = 221
    state['latest_session'] = SID

    p1 = state['records'][P1_ID]
    p1['related_records'] = list(dict.fromkeys(p1['related_records'] + [P2_ID, SID]))
    p1['source_hashes'].update({rel: sha(ROOT / rel) for rel in p1['full_sources']})
    p1['revalidation'] = (
        'Revision221 refreshes P1 source pins after the user-required local-asset reconnaissance rule and records that the '\
        'subsequent P2 SIP denominator closed without a theory bridge. P1 itself remains a scoped common-task qualification.'
    )

    plan_record = state['records'][PLAN_ID]
    plan_record['evidence_status'] = (
        'USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / '
        'P2_SIP_NO_K_WITHIN_SCOPE / P3_KAPP_DENOMINATOR_SELECTION_NEXT / NO_NEW_MATHEMATICAL_CLAIM'
    )
    plan_record['status'] = 'p1_p2_closed_p3_kapp_denominator_selection_next'
    plan_record['full_sources'] = list(dict.fromkeys(plan_record['full_sources'] + list(P2_SOURCES)))
    plan_record['related_records'] = list(dict.fromkeys(plan_record['related_records'] + [P2_ID, SID]))
    plan_record['source_hashes'].update({rel: sha(ROOT / rel) for rel in plan_record['full_sources']})
    plan_record['revalidation'] = (
        'Revision221 executes P2-KTHEORY-SIP-001 with Book §9.8, P1 mapping, academic source check and local-asset '\
        'reconnaissance. Earlier SIP assets are classified rather than repeated; the resulting scoped no-K_theory moves only '\
        'to P3 denominator selection and does not assert a HoTT defect.'
    )
    plan_record['scope'] = (
        'Four-track phase-two plan: P1 fixed restricted R_min; P2 Book §9.8 SIP closes as explicit-structure preservation '\
        'without a H/U→Done_s bridge; P3 now first selects an uncovered version-pinned K_app consumer; P4 remains triggered '\
        'only by an actual semantic/implementation discrepancy. No mathematical defect result is asserted.'
    )

    abx = state['records'][ABX_ID]
    abx['full_sources'] = list(dict.fromkeys(abx['full_sources'] + [REPORT, VERIFY, RECEIPT, PLAN_INDEX, PLAN_RECEIPT]))
    abx['related_records'] = list(dict.fromkeys(abx['related_records'] + [P2_ID, SID]))
    abx_refresh = [
        'ABX行动.md', 'ABX行动/005 - 状态、停止条件与未来交接.md',
        PLAN_INDEX, *PLAN_SHARDS, REPORT, VERIFY, RECEIPT, PLAN_RECEIPT,
        'goal.md', 'goal-3.md', 'feature-list.md', 'rulings.md', P1_RECEIPT,
    ]
    abx['source_hashes'].update({rel: sha(ROOT / rel) for rel in abx_refresh})
    abx['revalidation'] = (
        'Revision221 records the P2 SIP source/reuse audit. The Book and reused native boundary preserve explicit '\
        'structure rather than promote bare H/U to P1 Done_s. ABX is therefore eligible only for P3 selection of a new '\
        'version-pinned actual consumer denominator; no external K_app audit has occurred yet.'
    )
    abx['scope'] = (
        'ABX remains the actual-consumer branch. P1 supplies the restricted shared task; P2 excludes Book §9.8 SIP as '\
        'a theory-level bridge; the next action is only a bounded search for an uncovered version-pinned consumer before '\
        'any K_app claim or same-task mismatch proof.'
    )

    state['records'][P2_ID] = {
        'kind': 'result', 'path': REPORT, 'lifecycle_status': 'CURRENT',
        'evidence_status': (
            'NO_K_THEORY_WITHIN_SIP_DENOMINATOR / BOOK_SOURCE_AND_LOCAL_ASSET_REUSE_AUDITED / '\
            'REUSED_KERNEL_RECEIPT_WITH_SCOPE / ACADEMIC_BOUNDARY_SCAN / NO_NEW_MATHEMATICAL_CLAIM'
        ),
        'status': 'complete_with_scope_p3_kapp_denominator_selection_next', 'depends_on': [],
        'related_records': [P1_ID, PLAN_ID, ABX_ID, prior_latest],
        'full_sources': list(P2_SOURCES),
        'source_hashes': {rel: sha(ROOT / rel) for rel in P2_SOURCES},
        'scope': (
            'P2 maps P1 R_min to the exact Book §9.8 requirements and classifies existing SIP assets. It finds SIP '\
            'requires explicitly preserved structure and does not supply bare H/U→Done_s. It does not prove a general SIP '\
            'theorem, formalize P1 as a standard structure, find K_app, establish a new topology, or prove a HoTT defect.'
        ),
    }
    state['records'][SID] = {
        'kind': 'session', 'path': BASE + 'SESSION.md', 'lifecycle_status': 'HISTORICAL',
        'evidence_status': 'P2_SIP_SOURCE_AND_REUSE_AUDIT_CHECKPOINTED_WITH_SCOPE',
        'status': 'complete_with_scope', 'depends_on': [],
        'related_records': [P2_ID, P1_ID, PLAN_ID, ABX_ID, prior_latest],
        'full_sources': [BASE + name for name in ('SESSION.md', 'RUNS.json', 'CORE_COGNITION_AUDIT.md')],
    }
    state['execution_control'].update(
        portfolio_record=PLAN_ID,
        status='P2_SIP_NO_K_NEXT_P3_KAPP_DENOMINATOR_SELECTION',
        current_phase='PHASE_2_FOUR_TRACK_P3_DENOMINATOR_SELECTION_READY',
        second_phase_status='P1_P2_CLOSED_P3_KAPP_DENOMINATOR_SELECTION_NEXT',
        last_checkpoint_session=SID,
        checkpoint_result='.codex/cognition/checkpoints/' + SID + '/result.json',
        next_minimal_verification=(
            'P3-KAPP-DENOMINATOR-001 only: use goal-3 academic/community and local-asset reconnaissance to select one '\
            'uncovered, version-pinned real library/paper/application consumer with an entry point and possible task-completion '\
            'claim. Do not infer K from a SIP mention, rerun old scans, or start K_engine.'
        ),
    )
    state['projection']['status'] = 'P1_RMIN_ACCEPTED / P2_SIP_NO_K_WITHIN_SCOPE / P3_KAPP_DENOMINATOR_SELECTION_NEXT / NO_NEW_HOTT_DEFECT_CLAIM'

    session = f'''# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 state mutation for a scoped theory-source/reuse result and current-plan update
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: determine whether the exact Structure Identity Principle denominator gives a rule-level bridge from bare H/U to P1 Done_s
- load_receipt: research plan snapshot is saved as `audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-CHECKPOINT-PLAN.json`; P1 closure and current four-piece cognition were used as the task baseline
- status: COMPLETED_WITH_SCOPE / NO_K_THEORY_WITHIN_SIP_DENOMINATOR / P3_DENOMINATOR_SELECTION_NEXT

P2 first performed the user-required local-asset reconnaissance. It found the prior Cubical `SIPRepresentation` proof, historical WebGPT relational-SIP paper/finite work, and machine-overview calibration. Those assets are classified by exact scope; they are neither re-run nor rebranded as current circle-task proof. The frozen Book §9.8 source defines a notion of structure `(P,H)` and requires both forward and inverse structure preservation for structural isomorphism. P1's source, observation, operation and Done fields are therefore only protected if modeled explicitly; the Book does not turn bare carrier equivalence into process completion.

Wave reflection: this closes the rule-level SIP candidate in the final witness chain and prevents a repeat of a mature local proof family. The next potentially informative edge is an actual version-pinned consumer. P3 starts only by selecting a new denominator, and P4 remains untriggered.

| element | use | effect on this unit |
|---|---|---|
| `goal-3.md` §2.1 | used | bound the academic/primary-source check to the SIP statement and its known higher forms |
| `goal-3.md` §2.2 | used | found and classified existing local/WebGPT/machine-overview SIP assets before writing new work |
| Book §9.8 local source | used | establishes the actual `(P,H)`, standardness, and bidirectional-H conditions |
| C-124–C-128 native receipt | reused without replay | supplies a concrete structural positive control, not a current R_min theorem |
| WebGPT relational-SIP note | historical comparison | confirms a related two-way-H analysis but stays REVIEW_REQUIRED and task-distinct |
| actual K_app scan | intentionally unused | P3 is not yet a selected consumer denominator |
| engine audit | intentionally unused | no theory/implementation semantic discrepancy is present |
'''
    runs = {
        'schema_version': 'hott-session-runs/v1', 'session_id': SID,
        'primary_runs': [{
            'kind': 'p2-book-source-local-asset-and-routing-verification',
            'command': f'python3 -B {P1_VERIFY} --write && python3 -B {VERIFY} --write && python3 -B {PLAN_VERIFY} --write',
            'result': 'PASS_WITH_SCOPE; Book §9.8 anchors, P1 mapping, asset classes, prior receipt identity and P3 routing match',
            'mathematics': 'NOT_A_NEW_KERNEL_RUN',
        }],
        'new_math_claims': [], 'new_kernel_replay': False,
        'scope': 'P2 source/reuse audit and routing only; no new theorem, consumer finding or HoTT-defect claim.',
    }

    new_direction = (
        '| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：R_min、K_theory、K_app、K_engine | 用户要求每wave反思、学术调查和本地/历史资产侦察 | `P1_ACCEPTED / P2_SIP_NO_K / P3_DENOMINATOR_SELECTION_NEXT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；`R-P1-RMIN-SPEC-20260921`；`R-P2-KTHEORY-SIP-20260921` | P1/P2关闭；P3先选版本固定消费者；P4按触发 | `HoTT后续研究总体方案.md`；P2 receipt；revision221 receipt |\n'
        '| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P3 实际消费者 `K_app` 分支 | 原圆环 A/B/X H/R/K 整备、P1共同任务、P2 SIP无桥 | `P1_P2_CLOSED / P3_DENOMINATOR_SELECTION_PENDING / NO_DEFECT_VERDICT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P1/P2；C250–324、D1/D2/D3 | 先排除已有资产，冻结一个新消费者分母；不重做no-hit | `ABX行动.md`；总体方案；revision221 receipt |'
    )
    new_panorama = (
        '| `OUT-HOTT-FOUR-TRACK-PLAN` | 第二阶段四分支计划、P1共同规格、P2 SIP规则审计与P3选择路由 | `DIR-U-HOTT-FOUR-TRACK` | P1接口、Book §9.8、既有C124–128、WebGPT关系SIP和公开SIP文献 | `P1_ACCEPTED / P2_NO_K_WITHIN_SIP / P3_SELECTION_NEXT` | SIP只保显式结构；历史资产已分类，不重复 | 不证明一般SIP、P1完全结构化、K、HoTT缺陷或完整物理来源 | `audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-REPORT.md`；revision221 receipt |\n'
        '| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环实际消费者分支 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C250–324、68份run、Flash、D1/D2/D3、Book/社区来源、P1/P2 | `P1_P2_CLOSED / P3_DENOMINATOR_SELECTION_PENDING / NO_ACTUAL_K` | H/R/U与操作合同已有控制；SIP无规则桥 | 不证明新拓扑、外部全库无K或HoTT缺陷 | `ABX行动.md`；总体方案；revision221 receipt |'
    )
    new_memory = (
        '第二阶段四分支中 P1/P2 已结束：P1 的 `R_MIN_ACCEPTED_WITH_SCOPE` 固定共同强任务；P2 的 '\
        '`NO_K_THEORY_WITHIN_SIP_DENOMINATOR` 以 Book §9.8、既有 Cubical SIP 边界和历史资产侦察表明 SIP '\
        '保留显式结构而不提供 H/U→`Done_s`。当前唯一下一单元为 `P3-KAPP-DENOMINATOR-001`：先选择一个 '\
        '未覆盖、版本固定的真实消费者分母。禁止重跑旧SIP/Book/ABX控制或启动引擎审计。入口：`HoTT后续研究总体方案.md`；revision221 checkpoint。'
    )
    new_frontier = '- P1/P2 均已关闭：共同 `R_min` 已固定，Book §9.8 SIP 在其明确结构保持范围内没有 H/U→Done_s 桥，既有 SIP 资产已分类且不重跑。当前只可做 P3-KAPP-DENOMINATOR-001 的版本固定消费者选择；P4仍无触发，入口：`HoTT后续研究总体方案.md`。'
    new_resume = '第二阶段四分支中 P1/P2 已关闭：P1的受限R_min是Input + CurveData + Denotes/Satisfies + O + D；P2以Book §9.8和既有原生SIP边界排除SIP作为裸H/U→Done_s理论桥。新用户SOP要求每wave同时做公开学术检索与本地/历史资产侦察。当前唯一下一项=P3-KAPP-DENOMINATOR-001：挑选未覆盖、版本冻结、有入口的实际消费者；禁止重跑旧SIP、先扫无版本关键词或触发引擎审计。入口：`HoTT后续研究总体方案.md`；revision221 checkpoint。'
    memory_log = '\nS-RES-20260921-ASTRA-P2-KTHEORY-SIP：P2-KTHEORY-SIP-001 完成。Book §9.8的(P,H)标准结构、双向H同构条件及既有Cubical SIPRepresentation C124–128共同表明：SIP只保持显式结构，不把裸H/U升格为P1 Done_s。执行前按新goal-3资产侦察发现并分类旧SIP原生proof=PARTIAL_REUSE、WebGPT关系SIP=HISTORICAL_UNVERIFIED、旧L4校准=只覆盖Bool案例；未重跑。判词NO_K_THEORY_WITHIN_SIP_DENOMINATOR，裁决=CLOSE_WITH_SCOPE并转P3消费者分母选择。P1/P2/总体验证均PASS_WITH_SCOPE；revision221 checkpoint。\n'

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, 'source_state_revision: 220', 'source_state_revision: 221')
            body = replace_once(body, 'projection_generation: 20260921-direction-220', 'projection_generation: 20260921-direction-221')
            body = replace_once(body, 'semantic_status: P1_RMIN_ACCEPTED_P2_SIP_NEXT', 'semantic_status: P1_P2_CLOSED_P3_KAPP_DENOMINATOR_SELECTION_NEXT')
        elif rel == runtime.PANORAMA:
            body = replace_once(body, 'source_state_revision: 220', 'source_state_revision: 221')
            body = replace_once(body, 'projection_generation: 20260921-outcome-220', 'projection_generation: 20260921-outcome-221')
            body = replace_once(body, 'semantic_status: P1_RMIN_ACCEPTED_P2_SIP_NEXT', 'semantic_status: P1_P2_CLOSED_P3_KAPP_DENOMINATOR_SELECTION_NEXT')
        elif rel == '方向追踪/002 - 治理与用户方向.md':
            body = replace_line(body, '| `DIR-U-HOTT-FOUR-TRACK` |', new_direction)
        elif rel == '全景视野/003 - 当前机器证明包与原生重放.md':
            body = replace_line(body, '| `OUT-HOTT-FOUR-TRACK-PLAN` |', new_panorama)
        elif rel == 'MEMORY/001 - 当前执行队列.md':
            body = replace_line(body, '第二阶段四分支中 P1 已结束：', new_memory)
        elif rel == 'MEMORY/003 - 当前验证状态与顺序日志.md':
            body += memory_log
        elif rel == runtime.PREFIX + 'FRONTIER.md':
            body = replace_once(body, '- P1 已以 `R_MIN_ACCEPTED_WITH_SCOPE` 关闭：共同规格是现有 `Input + CurveData + Denotes/Satisfies + O + D`，不是完整 OriginTop。当前只可做 P2-KTHEORY-SIP-001（HoTT Book §9.8 的版本冻结结构同一性分母）；P3 ABX/K_app 和 P4 K_engine 仍按门槛停止，入口：`HoTT后续研究总体方案.md`。', new_frontier)
        elif rel == runtime.PREFIX + 'RESUME.md':
            body = replace_once(body, '第二阶段四分支中 P1 已关闭：受限 `R_min` 是现有 `Input + CurveData + Denotes/Satisfies + O + D`，并非完整现实来源或 HoTT 缺陷。P1学术检查找到结构同一性、cohesive、分层/相对结构的已知邻域，未找到 H/U→Done_s。当前唯一下一项=P2-KTHEORY-SIP-001，固定 HoTT Book §9.8 SIP；禁止重跑已有H/R/K控制、先扫ABX消费者或触发引擎审计。入口：`HoTT后续研究总体方案.md`；revision220 checkpoint。', new_resume)
        files.append({'path': rel, 'expected_sha256': runtime.sha(raw), 'text': body})

    for name, body in (
        ('SESSION.md', session),
        ('RUNS.json', runtime.dump(runs).decode()),
        ('CORE_COGNITION_AUDIT.md', core_audit(state['current_core'])),
    ):
        files.append({'path': BASE + name, 'expected_sha256': None, 'text': body})

    payload = {
        'schema_version': 'cognition-checkpoint/v1', 'session_id': SID,
        'load_profile': 'research', 'task_ids': [PLAN_ID],
        'authorization': '用户要求持续按goal-3执行四分支研究，并新增每wave的公开学术/社区检查和本地/历史资产侦察义务；用户此前授权当前唯一AI更新正确current owners、STATE和canonical checkpoint，且不启动Sub Agent、不push或发布。',
        'files': files,
    }
    (OUT / 'P2-KTHEORY-SIP-checkpoint-payload.json').write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan['snapshot'], payload, apply=args.apply)
    suffix = 'P2-KTHEORY-SIP-checkpoint-apply.json' if args.apply else 'P2-KTHEORY-SIP-checkpoint-dry-run.json'
    (OUT / suffix).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != 'paths'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
