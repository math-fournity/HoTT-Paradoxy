#!/usr/bin/env python3
"""Checkpoint P5's successor selection and route the active goal to P6.

The checkpoint records a planning/evidence result only.  It does not create a
mathematical theorem, replay a proof kernel, or certify a HoTT defect.
"""
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
SID = 'S-RES-20260921-ASTRA-P5-SUCCESSOR-DISCOVERY'
BASE = '.codex/research/hott/sessions/' + SID + '/'
PLAN_ID = 'R-HOTT-FOUR-TRACK-PLAN-20260921'
ABX_ID = 'R-ABX-ACTION-20260921'
P1_ID = 'R-P1-RMIN-SPEC-20260921'
P2_ID = 'R-P2-KTHEORY-SIP-20260921'
P3_ID = 'R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921'
P5_ID = 'R-P5-SUCCESSOR-DISCOVERY-20260921'

REPORT = 'audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md'
VERIFY = 'audit/p5-successor-discovery-20260921/verify_p5_successor_discovery.py'
RECEIPT = 'audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-VERIFICATION.json'
CHECKPOINT = 'audit/p5-successor-discovery-20260921/checkpoint_p5_successor_discovery.py'
P1_REPORT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md'
P1_VERIFY = 'audit/p1-rmin-spec-20260921/verify_p1_rmin_spec.py'
P1_RECEIPT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-VERIFICATION.json'
P2_REPORT = 'audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-REPORT.md'
P2_VERIFY = 'audit/p2-ktheory-sip-20260921/verify_p2_ktheory_sip.py'
P2_RECEIPT = 'audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-VERIFICATION.json'
P3_REPORT = 'audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-REPORT.md'
P3_VERIFY = 'audit/p3-unimath-functor-algebras-20260921/verify_p3_unimath_functor_algebras.py'
P3_RECEIPT = 'audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-VERIFICATION.json'
PLAN_VERIFY = 'audit/four-track-plan-20260921/verify_four_track_plan.py'
PLAN_RECEIPT = 'audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json'
PLAN_INDEX = 'HoTT后续研究总体方案.md'
PLAN_SHARDS = tuple(
    'HoTT后续研究总体方案/' + name for name in (
        '001 - 上一轮问答与四分支校正.md',
        '002 - 共同任务、术语与优先级原则.md',
        '003 - 分支顺序、准入与停止条件.md',
        '004 - 令牌经济、反漂移与每单元复核.md',
        '005 - 当前第一步与交接.md',
    )
)
OPEN_OBLIGATIONS = 'audit/abx-action-20260921/H-R-K查找思路整备/005 - 未覆盖义务、禁止重复与重新出发条件.md'
ORIGIN_INTERFACE = 'ABX行动/003 - 原圆环对象、判据与正反控制.md'
SOURCE_CONTRACT = 'HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda'
TASK_INTEGRATION = 'HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda'

P5_SOURCES = (
    REPORT, VERIFY, RECEIPT, CHECKPOINT,
    P1_REPORT, P1_VERIFY, P1_RECEIPT,
    P2_REPORT, P2_VERIFY, P2_RECEIPT,
    P3_REPORT, P3_VERIFY, P3_RECEIPT,
    PLAN_INDEX, *PLAN_SHARDS, PLAN_VERIFY, PLAN_RECEIPT,
    'goal.md', 'goal-3.md', 'feature-list.md', 'rulings.md',
    'ABX行动.md', 'ABX行动/003 - 原圆环对象、判据与正反控制.md',
    'ABX行动/005 - 状态、停止条件与未来交接.md',
    OPEN_OBLIGATIONS, ORIGIN_INTERFACE, SOURCE_CONTRACT, TASK_INTEGRATION,
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(body: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, body, count=1)
    assert count == 1, old
    return result


def replace_line(body: str, prefix: str, replacement: str) -> str:
    lines = body.splitlines()
    hits = [index for index, line in enumerate(lines) if line.startswith(prefix)]
    # Direction tables retain superseded historical rows with the same stable ID.
    # The first row is the current projection row; later rows remain provenance.
    assert hits, prefix
    lines[hits[0]] = replacement
    return '\n'.join(lines) + '\n'


def core_audit(core: dict) -> str:
    headings = re.findall(r'^### (KC-\d+) · .*? · (.+)$', (ROOT / '核心认知.md').read_text(encoding='utf-8'), re.M)
    assert len(headings) == core['kc_count'] == 46
    deepened = {10, 14, 15, 19, 21, 22, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    corrected = {43}
    body = f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P5_SUCCESSOR_SELECTED_P6_ORIGIN_STRUCTURE_COMPARISON_NEXT
- panorama_change: FIRST_PASS_SCOPE_PRESERVED_AND_OBJECT_THEORY_SUCCESSOR_SELECTED
- essay_change: NO
- update_decision: P5 只关闭首次 successor-discovery 分母；active goal 继续到 P6，不能因旧分母无命中停止
- cross_conflicts: 分层/黏着结构是可能保留额外几何信息的已有对象理论或模型，不能仅因相邻就被写成 K 或 HoTT 缺陷
- unresolved: 完整 OriginTop/R、P6 字段比较、实际 K、同任务失配、理论—实现差异与独立非现实性判词仍开放

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
'''
    for number, (kc, title) in enumerate(headings, 1):
        if number in corrected:
            relation = 'CORRECTED'
            judgment = '将“停止”校正为旧冻结分母的停止，而非 active goal 的停止；P5 立即生成并选择 P6。'
            evidence = f'{REPORT}；{PLAN_INDEX}；P6 的字段比较若显示已有完整结构编码，应转写为防御而非继续声称缺口。'
        elif number in deepened:
            relation = 'DEEPENED'
            judgment = 'P5 把现实对齐需求落到来源—操作—复原字段的对象理论承载问题，并以分层与 cohesive 文献作为反解释控制。'
            evidence = f'{REPORT}；{ORIGIN_INTERFACE}；P6 需要逐字段矩阵，不能由本次候选选择推出数学结论。'
        else:
            relation = 'NOT_TOUCHED'
            judgment = '本单元选择 P6 的对象理论比较，不重新裁决本条独立用户原文。'
            evidence = 'goal.md §2；没有新 kernel 证明、规则桥、实际 K 或现实结论。'
        body += f'| `{kc}` | {title} | {relation} | {judgment} | {evidence} |\n'
    body += '''
## 扩展认知逐片复认

001–008：P5 以“先发现、再归因”的姿态区分了三件事：现有理论已知的结构化防御、尚未完成的对象理论规格、以及尚无证据的 HoTT 缺陷。选择 P6 的价值在于把来源/操作/完成从口号变成可比较字段；它不将现实解释直接伪装成内部矛盾。

## 波次定位

- 最终目标连接：P5 连接最终见证链的 `R_min → 可比较 R_origin` 一边；它尚未触及规则桥、真实消费者失配或内核语义。
- 全局坐标：P1/P2/P3 分别关闭共同规格、SIP 规则和一个外部消费者分母；P4 无触发；P5 生成下一不同分母；P6 成为当前单元。
- 实际价值：防止 `STOP_BY_DEFAULT` 被误读为总目标停止，也防止把 cohesive/stratified 相邻工作误标为 HoTT 缺陷。
- 继续检验：P6 逐字段比较静态对象数据、态射保持、过程/trace 与 Done；其反解释是完整 structured-diagram 编码。
- 不延续理由：旧 SIP/UniMath/ABX 分母的额外搜索不会改变既有有界判词，除非出现新的版本、入口或实际任务承诺。
- 裁决：P5 `CLOSE_WITH_SCOPE`，但 active goal `GOAL_ACTIVE / P6_NEXT`。

## 停止裁决

本 session 不停止 active goal。它只结束 P5 的 discovery 分母，并把 P6 作为下一个可执行的对象理论比较。若 P6 完成，仍按 `goal-3.md` §3.2 产生 successor，除非整体 goal 完成、用户暂停或必要外部状态不可访问。
'''
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()

    for command in (
        [P1_VERIFY, '--write'], [P2_VERIFY, '--write'], [P3_VERIFY, '--write'],
        [VERIFY, '--write'], [PLAN_VERIFY, '--write'],
    ):
        subprocess.check_call([sys.executable, '-B', *command], cwd=ROOT)
    for rel in P5_SOURCES:
        assert (ROOT / rel).is_file(), rel

    spec = importlib.util.spec_from_file_location('runtime', ROOT / '.codex/tools/cognition_runtime.py')
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding='utf-8'))
    assert state['revision'] == 223
    assert state['latest_session'] == 'S-GOV-20260921-ASTRA-P3-SOURCE-PIN-REFRESH'
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding='utf-8'))
    assert all(sha(ROOT / rel) == digest for rel, digest in head['tracked'].items())
    plan = runtime.plan(ROOT, profile='research', task_ids=[PLAN_ID])
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (OUT / 'P5-SUCCESSOR-DISCOVERY-CHECKPOINT-PLAN.json').write_bytes(runtime.dump(plan))
    for rel in (P1_RECEIPT, P2_RECEIPT, P3_RECEIPT, RECEIPT, PLAN_RECEIPT):
        assert json.loads((ROOT / rel).read_text(encoding='utf-8'))['status'] == 'PASS_WITH_SCOPE'

    prior_latest = state['latest_session']
    state['revision'] = 224
    state['latest_session'] = SID

    # Preserve each historical outcome while recording that the active route has advanced.
    for prior_id, prior_label in (
        (P1_ID, 'P1 remains the scoped common R_min qualification.'),
        (P2_ID, 'P2 remains the scoped SIP no-rule-bridge result.'),
        (P3_ID, 'P3 remains the scoped UniMath external-consumer result.'),
    ):
        record = state['records'][prior_id]
        record['related_records'] = list(dict.fromkeys(record['related_records'] + [P5_ID, SID]))
        source_paths = set(record['full_sources']) | set(record.get('source_hashes', {}))
        record['source_hashes'].update({rel: sha(ROOT / rel) for rel in source_paths if (ROOT / rel).is_file()})
        record['revalidation'] = (
            'Revision224 records P5 successor selection after the first four-track pass. ' + prior_label +
            ' It does not gain a HoTT-defect conclusion or reopen its frozen denominator.'
        )

    plan_record = state['records'][PLAN_ID]
    plan_record['evidence_status'] = (
        'USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / '
        'P2_SIP_NO_K_WITHIN_SCOPE / P3_UNIMATH_NO_K_WITHIN_SCOPE / P4_NOT_TRIGGERED / '
        'P5_SUCCESSOR_SELECTED_P6_ORIGIN_STRUCTURE_COMPARISON / GOAL_ACTIVE'
    )
    plan_record['status'] = 'four_track_first_pass_complete_p5_successor_selected_p6_next'
    plan_record['full_sources'] = list(dict.fromkeys(plan_record['full_sources'] + list(P5_SOURCES)))
    plan_record['related_records'] = list(dict.fromkeys(plan_record['related_records'] + [P5_ID, SID]))
    plan_source_paths = set(plan_record['full_sources']) | set(plan_record.get('source_hashes', {}))
    plan_record['source_hashes'].update({rel: sha(ROOT / rel) for rel in plan_source_paths if (ROOT / rel).is_file()})
    plan_record['revalidation'] = (
        'Revision224 preserves P1/P2/P3 scoped negatives and P4_NOT_TRIGGERED, but corrects the old global-stop '
        'reading: P5 compares four ingress classes and selects P6 for a field-level OriginPresentation comparison. '
        'This is a planning/evidence result, not a global no-K or HoTT-defect conclusion.'
    )
    plan_record['scope'] = (
        'First pass remains closed by denominator: P1 restricted R_min; P2 Book SIP no theory bridge; P3 UniMath '
        'functor-algebras no same-task K; P4 not triggered. P5 selects P6 to compare OriginPresentation with marked, '
        'stratified, relative-diagram and cohesive structures. P6 does not itself assert a HoTT defect.'
    )

    abx = state['records'][ABX_ID]
    abx['full_sources'] = list(dict.fromkeys(abx['full_sources'] + list(P5_SOURCES)))
    abx['related_records'] = list(dict.fromkeys(abx['related_records'] + [P5_ID, SID]))
    abx_source_paths = set(abx['full_sources']) | set(abx.get('source_hashes', {}))
    abx['source_hashes'].update({rel: sha(ROOT / rel) for rel in abx_source_paths if (ROOT / rel).is_file()})
    abx['revalidation'] = (
        'Revision224 preserves D_ABX_1/D_ABX_2/D_ABX_3 and the P1/P2/P3 scope. P5 selects an object-theory '
        'comparison for OriginPresentation; no actual K, theory bridge, implementation discrepancy or HoTT defect is claimed.'
    )
    abx['scope'] = (
        'ABX has completed its first consumer/rule pass and P5 successor selection. P6 will compare the current '
        'OriginPresentation with structured mathematical objects before any future K audit. This does not prove no external K, '
        'a new topology, or a HoTT defect.'
    )

    state['records'][P5_ID] = {
        'kind': 'result', 'path': REPORT, 'lifecycle_status': 'CURRENT',
        'evidence_status': (
            'SUCCESSOR_SELECTED_P6_ORIGIN_STRUCTURE_COMPARISON / '
            'ACADEMIC_AND_LOCAL_ASSET_RECONNAISSANCE / NO_NEW_MATHEMATICAL_CLAIM'
        ),
        'status': 'complete_with_scope_p6_origin_structure_comparison_next', 'depends_on': [],
        'related_records': [PLAN_ID, ABX_ID, P1_ID, P2_ID, P3_ID, prior_latest],
        'full_sources': list(P5_SOURCES),
        'source_hashes': {rel: sha(ROOT / rel) for rel in P5_SOURCES},
        'scope': (
            'P5 compares four possible ingress classes and selects an OriginPresentation object-theory comparison. '
            'Its paper/website source review identifies stratified and cohesive work as nearby structures or explicit defenses. '
            'It does not formalize OriginTop/R, prove a theorem, find a K, or establish a HoTT defect.'
        ),
    }
    state['records'][SID] = {
        'kind': 'session', 'path': BASE + 'SESSION.md', 'lifecycle_status': 'HISTORICAL',
        'evidence_status': 'P5_SUCCESSOR_DISCOVERY_CHECKPOINTED_WITH_SCOPE',
        'status': 'complete_with_scope', 'depends_on': [],
        'related_records': [P5_ID, PLAN_ID, ABX_ID, P1_ID, P2_ID, P3_ID, prior_latest],
        'full_sources': [BASE + name for name in ('SESSION.md', 'RUNS.json', 'CORE_COGNITION_AUDIT.md')],
    }
    state['execution_control'].update(
        portfolio_record=PLAN_ID,
        status='FOUR_TRACK_FIRST_PASS_COMPLETE_P5_SUCCESSOR_SELECTED_P6_NEXT',
        current_phase='PHASE_2_P5_SUCCESSOR_SELECTED_P6_ORIGIN_STRUCTURE_COMPARISON_NEXT',
        second_phase_status='P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_P5_SUCCESSOR_SELECTED_P6_NEXT',
        last_checkpoint_session=SID,
        checkpoint_result='.codex/cognition/checkpoints/' + SID + '/result.json',
        next_minimal_verification=(
            'P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001. Freeze OriginPresentation fields and compare marked/pointed, '
            'X→P stratified, relative/cospan-diagram and cohesive structures field by field. Distinguish object data, '
            'morphism preservation, process/trace and Done; retain full structured-transport as a positive control. '
            'P6 closes only its comparison denominator and must generate a successor while the active goal remains active.'
        ),
    )
    state['projection']['status'] = (
        'FOUR_TRACK_FIRST_PASS_COMPLETE / P5_SUCCESSOR_SELECTED / '
        'NEXT_P6_ORIGIN_STRUCTURE_COMPARISON / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM'
    )

    session = f'''# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 state mutation for successor discovery and current-plan routing
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: correct the active-goal control semantics and select one distinct, evidence-bounded successor after P1/P2/P3
- load_receipt: research plan snapshot is saved as `audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-CHECKPOINT-PLAN.json`
- status: COMPLETED_WITH_SCOPE / P5_SUCCESSOR_SELECTED / P6_NEXT / NO_NEW_MATHEMATICAL_CLAIM

The user correctly rejected an interpretation under which a first-pass scoped negative stops the active goal. P5 therefore treats `STOP_BY_DEFAULT` as a ban on repeating an already frozen denominator, performs the required public academic/community and local/historical reconnaissance, and selects P6 rather than waiting for new user prose. The selected P6 compares the current OriginPresentation with established structured-object candidates. It has a strong counter-explanation: a complete natural structured-diagram encoding could show the boundary is already explicitly preserved.

| element | use | effect on this unit |
|---|---|---|
| `goal-3.md` §2.1 | used | checked public stratified and cohesive literature before naming a successor |
| `goal-3.md` §2.2 | used | reused the ABX open-obligation register and P1–P3 rather than recreating a past scan |
| P1/P2/P3 receipts | used | prevented SIP/UniMath re-scan from being mislabeled as progress |
| `OriginPresentation` interface | used | fixed the fields P6 must compare |
| cohesive HoTT source | used as boundary control | indicates an additional-structure model, not an ordinary-HoTT defect |
| P4 engine audit | intentionally not run | no same-rule theory/implementation discrepancy exists in the checked evidence |
| proof assistant kernel | intentionally not run | P5 creates no mathematical proposition requiring a new kernel replay |
'''
    runs = {
        'schema_version': 'hott-session-runs/v1', 'session_id': SID,
        'primary_runs': [{
            'kind': 'p5-source-provenance-plan-and-local-asset-verification',
            'command': f'python3 -B {P1_VERIFY} --write && python3 -B {P2_VERIFY} --write && python3 -B {P3_VERIFY} --write && python3 -B {VERIFY} --write && python3 -B {PLAN_VERIFY} --write',
            'result': 'PASS_WITH_SCOPE; source anchors, old bounded results, P5 candidate card and P6 routing agree',
            'mathematics': 'NOT_A_NEW_KERNEL_RUN',
        }],
        'new_math_claims': [], 'new_kernel_replay': False,
        'scope': 'P5 successor selection and state routing only; no new topological theorem, actual K, or HoTT-defect claim.',
    }

    new_direction = (
        '| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：P5后继选择与P6对象理论比较 | 用户要求 active goal 不因单一分母无命中停止；每wave做学术与本地资产侦察 | `FIRST_PASS_COMPLETE / P5_SUCCESSOR_SELECTED / NEXT_P6_ORIGIN_STRUCTURE_COMPARISON / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1/P2/P3/P5 records | P6 比较 OriginPresentation 的对象、态射、过程与Done承载；完成后生成 successor | `HoTT后续研究总体方案.md`；P5 report；revision224 receipt |'
    )
    new_abx_direction = (
        '| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P5后继选择后的来源—操作—复原对象理论线 | H/R/K整备、P1/P2/P3以及P5四类入口比较 | `NO_ACTUAL_K_IN_TESTED_DENOMINATORS / P5_SUCCESSOR_SELECTED / NEXT_P6_ORIGIN_STRUCTURE_COMPARISON` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P1/P2/P3/P5 | 先确定完整R的结构承载；不能把P6预写为K或HoTT缺陷 | `ABX行动.md`；P5 report；revision224 receipt |'
    )
    new_panorama = '| `OUT-HOTT-FOUR-TRACK-PLAN` | 第二阶段首次pass后的P5 successor选择 | `DIR-U-HOTT-FOUR-TRACK` | P1接口、Book/SIP、UniMath固定外部源码、P5公开与本地比较 | `P5_SUCCESSOR_SELECTED_P6_ORIGIN_STRUCTURE_COMPARISON_NEXT` | P5将停止限定为旧分母；cohesive是已知边界；P6比较OriginPresentation的结构承载 | 不证明完整OriginTop、K、全局无K、HoTT无问题/有缺陷或现实复原结论 | `audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md`；revision224 receipt |'
    new_abx_panorama = '| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环：P5后继对象理论线 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C250–324、D1/D2/D3、P1/P2/P3/P5 | `P5_SUCCESSOR_SELECTED / NEXT_P6_ORIGIN_STRUCTURE_COMPARISON` | 下一项是字段保真比较，不是重扫消费者或宣称缺陷 | 不证明外部全库无K、完整新拓扑学或HoTT缺陷 | `ABX行动.md`；P5 report；revision224 receipt |'
    new_memory = (
        'P5 successor discovery 已完成：P1/P2/P3 的有界结论与 P4 未触发保持；`STOP_BY_DEFAULT` 只停止这些旧分母。公开分层/real-cohesive 文献与本地 H/R/K 资产比较后，选择 `P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001`：逐字段比较 `OriginPresentation` 与标记、分层、相对 diagram/cohesive 结构，固定对象/态射/过程/Done 的承载。P6 不是 HoTT 缺陷结论，完成后仍须生成 successor。入口：`audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md`；revision224 checkpoint。'
    )
    new_frontier = '- P5 successor discovery 已完成：首次 P1/P2/P3 scoped negatives 与 P4_NOT_TRIGGERED 保持，`STOP_BY_DEFAULT` 只禁止重做旧分母。当前 P6 比较 `OriginPresentation` 与带标记、分层、相对 diagram/cohesive 结构，逐字段固定对象、态射、过程和 Done；完整结构编码是强反解释。入口：`audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md`。'
    new_resume = '当前 active goal 在 P5 后继续：P1/P2/P3 各自有界关闭、P4未触发；P5 已选 `P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001`。P6 将 `OriginPresentation` 与标记/分层/相对 diagram/cohesive 结构逐字段比较，区分对象数据、态射保持、过程/trace 与 Done；全字段 transport 是正控制，完整 structured-diagram 编码是反解释。P6 不主张 HoTT 缺陷，结束后仍按goal-3生成 successor。入口：`audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md`；revision224 checkpoint。'
    memory_log = '\nS-RES-20260921-ASTRA-P5-SUCCESSOR-DISCOVERY：用户澄清 active goal 不得被旧分母 STOP_BY_DEFAULT 停止。P5 完成学术/社区与本地/历史资产侦察；分层/real-cohesive 结构为已知边界或防御，未出现新实际K或P4语义差异。选定P6：逐字段比较OriginPresentation与标记、分层、相对diagram/cohesive结构。P5仅关闭discovery分母，Goal保持active；无新数学claim；revision224 checkpoint。\n'

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode('utf-8')
        if rel == runtime.STATE:
            body = runtime.dump(state).decode('utf-8')
        elif rel == runtime.DIRECTION:
            body = replace_once(body, 'source_state_revision: 223', 'source_state_revision: 224')
            body = replace_once(body, 'projection_generation: 20260921-direction-223', 'projection_generation: 20260921-direction-224')
            body = replace_once(body, 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_STOP_BY_DEFAULT', 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_P5_SUCCESSOR_SELECTED_P6_NEXT')
        elif rel == runtime.PANORAMA:
            body = replace_once(body, 'source_state_revision: 223', 'source_state_revision: 224')
            body = replace_once(body, 'projection_generation: 20260921-outcome-223', 'projection_generation: 20260921-outcome-224')
            body = replace_once(body, 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_STOP_BY_DEFAULT', 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_P5_SUCCESSOR_SELECTED_P6_NEXT')
        elif rel == '方向追踪/002 - 治理与用户方向.md':
            body = replace_line(body, '| `DIR-U-HOTT-FOUR-TRACK` |', new_direction)
            body = replace_line(body, '| `DIR-U-ABX-ORIGINAL-CIRCLE` |', new_abx_direction)
        elif rel == '全景视野/003 - 当前机器证明包与原生重放.md':
            body = replace_line(body, '| `OUT-HOTT-FOUR-TRACK-PLAN` |', new_panorama)
            body = replace_line(body, '| `OUT-ABX-ACTION-INTAKE` |', new_abx_panorama)
        elif rel == 'MEMORY/001 - 当前执行队列.md':
            body = replace_line(body, '四分支首次 pass 已完成并 `STOP_BY_DEFAULT`：', new_memory)
        elif rel == 'MEMORY/003 - 当前验证状态与顺序日志.md':
            body += memory_log
        elif rel == runtime.PREFIX + 'FRONTIER.md':
            body = replace_once(body, '- 四分支首次pass已完成并默认停止：P1共同R_min、P2 Book SIP、P3 UniMath实际consumer均未给H/U→P1 Done_s，P4无触发。只接受新版本固定消费者、强R、直接证据失效或可重放理论—实现差异；每次先按goal-3做学术和资产侦察，入口：`HoTT后续研究总体方案.md`。', new_frontier)
        elif rel == runtime.PREFIX + 'RESUME.md':
            body = replace_once(body, '四分支首次pass已完成并STOP_BY_DEFAULT：P1固定受限R_min；P2 Book §9.8 SIP为显式结构保持；P3 UniMath@ab5f5395 functor-algebras实际调用显式结构、输出univalence，不是P1 Done_s；P4未触发。不要用更多关键词/同义库扩张。仅新版本固定consumer、强R、直接失效或可重放理论—实现差异可重开，且先走goal-3学术+资产侦察。入口：`HoTT后续研究总体方案.md`；revision222 checkpoint。', new_resume)
        files.append({'path': rel, 'expected_sha256': runtime.sha(raw), 'text': body})

    for name, body in (
        ('SESSION.md', session),
        ('RUNS.json', runtime.dump(runs).decode('utf-8')),
        ('CORE_COGNITION_AUDIT.md', core_audit(state['current_core'])),
    ):
        files.append({'path': BASE + name, 'expected_sha256': None, 'text': body})

    payload = {
        'schema_version': 'cognition-checkpoint/v1', 'session_id': SID,
        'load_profile': 'research', 'task_ids': [PLAN_ID],
        'authorization': '用户要求 active goal 在每个有界分母之后继续生成并执行 successor，并授权当前唯一AI维护 current owners、STATE与canonical checkpoint；不启动Sub Agent、不push、不发布。',
        'files': files,
    }
    (OUT / 'P5-SUCCESSOR-DISCOVERY-checkpoint-payload.json').write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan['snapshot'], payload, apply=args.apply)
    suffix = 'P5-SUCCESSOR-DISCOVERY-checkpoint-apply.json' if args.apply else 'P5-SUCCESSOR-DISCOVERY-checkpoint-dry-run.json'
    (OUT / suffix).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != 'paths'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
