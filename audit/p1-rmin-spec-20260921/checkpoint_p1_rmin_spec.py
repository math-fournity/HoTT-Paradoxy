#!/usr/bin/env python3
"""Checkpoint the scoped P1 R_min qualification and P2 SIP routing."""

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
SID = 'S-RES-20260921-ASTRA-P1-RMIN-SPEC'
BASE = '.codex/research/hott/sessions/' + SID + '/'
PLAN_ID = 'R-HOTT-FOUR-TRACK-PLAN-20260921'
ABX_ID = 'R-ABX-ACTION-20260921'
P1_ID = 'R-P1-RMIN-SPEC-20260921'
REPORT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md'
VERIFY = 'audit/p1-rmin-spec-20260921/verify_p1_rmin_spec.py'
RECEIPT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-VERIFICATION.json'
CHECKPOINT = 'audit/p1-rmin-spec-20260921/checkpoint_p1_rmin_spec.py'
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
CODE_SOURCES = (
    'HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda',
    'HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda',
    'HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda',
    'HoTT/formal/agda-unimath/hott-z/NativeCurveTask.agda',
)
RUNS = (
    'HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-SOURCE-CONTRACT-001-01/RUN.json',
    'HoTT/verification/runs/20260921-MP-ASTRA-NATIVE-TASK-INTEGRATION-001-01/RUN.json',
)
P1_SOURCES = (
    REPORT, VERIFY, RECEIPT, CHECKPOINT, *CODE_SOURCES, *RUNS,
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
- direction_change: P1_RMIN_ACCEPTED_WITH_SCOPE_AND_P2_SIP_DENOMINATOR_SELECTED
- panorama_change: P1_SOURCE_INTERFACE_AND_ACADEMIC_BOUNDARY_AUDITED_WITH_SCOPE
- essay_change: NO
- update_decision: P1 已关闭；P2 只能审计 HoTT Book §9.8 的一个版本冻结 SIP 分母，不能先扫 K_app 或重新运行既有控制
- cross_conflicts: 富化规格可表达、结构保持理论、实际消费者承诺、proof-assistant 忠实性和现实解释是不同链边；P1 的接口资格化不能代替任何后续一边
- unresolved: SIP 是否有 H/U→Done_s 桥、版本固定实际 K_app、实现语义差异、完整 OriginTop/物理过程和独立非现实性判词仍未解决

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
'''
    for number, (kc, title) in enumerate(headings, 1):
        if number in corrected:
            relation = 'CORRECTED'
            judgement = 'P1 把来源、闭图、操作和 Done 写成受限共同合同，拒绝把裸空间关系、接口控制或社区类比直接提升为 HoTT 缺陷。'
            evidence = f'{REPORT}；{RECEIPT}；发现明确 K 或同任务桥才改变该范围。'
        elif number in deepened:
            relation = 'DEEPENED'
            judgement = 'P1 固定了后续理论/消费者审计必须共享的强任务 oracle，并按结构保持与 cohesive/stratified 相邻文献标定其边界。'
            evidence = f'{REPORT}；{RECEIPT}；P2 的冻结 SIP 命题和其正反控制决定是否出现理论桥。'
        else:
            relation = 'NOT_TOUCHED'
            judgement = '本单元仅资格化四分支的共同规格和下一理论分母，不重新裁决本条独立用户原文。'
            evidence = 'goal.md §2；没有新数学定理或现实结论。'
        body += f'| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n'
    body += '''
## 扩展认知逐片复认

001–008：本单元只把现有来源—操作—复原代理收束为 `R_min`，并检验这种收束在结构同一性、cohesive 和分层/相对结构的既有语言中的位置。它没有把“已知相邻结构”改写成用户精确过程已经得到理论承诺。

## 波次定位

- 最终目标连接：固定合格见证链中“同一输入、操作、观察与强完成”的共同 oracle；没有这条边，规则桥或消费者都不能被判为同一任务。
- 全局坐标：P1 已完成，P2 的 HoTT Book §9.8 SIP 分母获得启动资格；P3/ABX 仍等待，P4 未触发。
- 实际价值：将散落在 `RichCurve`、`NativeSourceContract` 和 `NativeTaskIntegration` 的现有字段和控制组成可重用合同，且明确本地 kernel receipt 的未版本闭合限制。
- 继续检验：继续 P1 只有在用户给出一个独立、不可由当前 `Input + CurveData + Denotes/Satisfies + O + D` 表达的强 Done 字段时才有资格；否则会重复已审接口。
- 不延续理由：当前 P1 声明范围已达到；进一步构造完整 OriginTop 或物理过程是新的对象理论项目，不会直接减少当前规则桥不确定性。
- 裁决：CLOSE_WITH_SCOPE；SWITCH_BRANCH 到 P2-KTHEORY-SIP-001。

## 停止裁决

P1 结束。下一次只可检查一个冻结版本的 SIP 理论分母；如果它无桥，再进入 P3 的新版本固定实际消费者分母。任何将 P1 本身说成 HoTT 缺陷、完整现实拓扑或公开数学结论的说法都被本审计否定。
'''
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()

    subprocess.check_call([sys.executable, '-B', VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', PLAN_VERIFY, '--write'], cwd=ROOT)
    for rel in P1_SOURCES:
        assert (ROOT / rel).is_file(), rel

    spec = importlib.util.spec_from_file_location('runtime', ROOT / '.codex/tools/cognition_runtime.py')
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state['revision'] == 219
    assert state['latest_session'] == 'S-PLAN-20260921-ASTRA-FOUR-TRACK'
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head['tracked'].items())
    plan = runtime.plan(ROOT, profile='research', task_ids=[PLAN_ID])
    assert set(plan['review_required']) <= {PLAN_ID, ABX_ID}
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (OUT / 'P1-RMIN-SPEC-CHECKPOINT-PLAN.json').write_bytes(runtime.dump(plan))
    assert json.loads((ROOT / RECEIPT).read_text())['status'] == 'PASS_WITH_SCOPE'
    assert json.loads((ROOT / PLAN_RECEIPT).read_text())['status'] == 'PASS_WITH_SCOPE'

    prior_latest = state['latest_session']
    state['revision'] = 220
    state['latest_session'] = SID
    plan_record = state['records'][PLAN_ID]
    plan_record['evidence_status'] = (
        'USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / '
        'P2_SIP_DENOMINATOR_PRE_REGISTERED / NO_NEW_MATHEMATICAL_CLAIM'
    )
    plan_record['status'] = 'p1_rmin_accepted_p2_ktheory_sip_next'
    plan_record['full_sources'] = list(dict.fromkeys(plan_record['full_sources'] + list(P1_SOURCES)))
    plan_record['related_records'] = list(dict.fromkeys(plan_record['related_records'] + [P1_ID, SID]))
    plan_record['source_hashes'].update({rel: sha(ROOT / rel) for rel in plan_record['full_sources']})
    plan_record['revalidation'] = (
        'Revision220 records P1-RMIN-SPEC-001: the existing compound interface is accepted as a scoped common R_min '
        'contract, direct source paths and pre-existing kernel-receipt limits are rechecked, and the P2 SIP denominator '
        'is selected. This updates routing only; it does not find a K or assert a HoTT defect.'
    )
    plan_record['scope'] = (
        'Four-track phase-two plan: P1 closed as a scoped source-operation-restoration interface qualification; P2 now '
        'examines a version-frozen Structure Identity Principle denominator; P3 remains ABX/K_app after P2; P4 remains '
        'triggered by an actual implementation discrepancy. No mathematical defect result is asserted.'
    )

    abx = state['records'][ABX_ID]
    abx['full_sources'] = list(dict.fromkeys(abx['full_sources'] + [REPORT, VERIFY, RECEIPT, PLAN_INDEX, PLAN_RECEIPT]))
    abx['related_records'] = list(dict.fromkeys(abx['related_records'] + [P1_ID, SID]))
    abx_refresh = [
        'ABX行动.md', 'ABX行动/005 - 状态、停止条件与未来交接.md',
        PLAN_INDEX, *PLAN_SHARDS, REPORT, VERIFY, RECEIPT, PLAN_RECEIPT,
        'goal.md', 'goal-3.md', 'feature-list.md', 'rulings.md',
    ]
    abx['source_hashes'].update({rel: sha(ROOT / rel) for rel in abx_refresh})
    abx['revalidation'] = (
        'Revision220 records that P1 accepted the shared R_min contract with scope. ABX remains P3 and cannot reopen '
        'external K_app search until P2 completes the distinct version-frozen SIP theory denominator; previous bounded '
        'no-hit results remain bounded and are not a HoTT-defect verdict.'
    )
    abx['scope'] = (
        'ABX remains the actual-consumer branch. P1 supplies the restricted common Input + CurveData + Denotes/Satisfies + '
        'O + D contract; P2 must still determine whether SIP creates a rule-level bridge before a new K_app denominator is eligible.'
    )

    state['records'][P1_ID] = {
        'kind': 'result', 'path': REPORT, 'lifecycle_status': 'CURRENT',
        'evidence_status': (
            'R_MIN_ACCEPTED_WITH_SCOPE / SOURCE_AND_INTERFACE_AUDIT / '
            'PREEXISTING_KERNEL_RECEIPTS_REUSED_WITH_VERSION_CAVEAT / '
            'ACADEMIC_BOUNDARY_SCAN / NO_NEW_MATHEMATICAL_CLAIM'
        ),
        'status': 'complete_with_scope_p2_ktheory_sip_next', 'depends_on': [],
        'related_records': [PLAN_ID, ABX_ID, prior_latest],
        'full_sources': list(P1_SOURCES),
        'source_hashes': {rel: sha(ROOT / rel) for rel in P1_SOURCES},
        'scope': (
            'P1 accepts a compound, supplied source-operation-observation-Done interface as the restricted common R_min '
            'contract for the circle-puncture task. It neither formalizes complete physical provenance nor proves any new theorem, '
            'K_theory, K_app, implementation anomaly, new topology, or HoTT defect.'
        ),
    }
    state['records'][SID] = {
        'kind': 'session', 'path': BASE + 'SESSION.md', 'lifecycle_status': 'HISTORICAL',
        'evidence_status': 'P1_RMIN_SPECIFICATION_AND_ROUTING_CHECKPOINTED_WITH_SCOPE',
        'status': 'complete_with_scope', 'depends_on': [],
        'related_records': [P1_ID, PLAN_ID, ABX_ID, prior_latest],
        'full_sources': [BASE + name for name in ('SESSION.md', 'RUNS.json', 'CORE_COGNITION_AUDIT.md')],
    }
    state['execution_control'].update(
        portfolio_record=PLAN_ID,
        status='P1_RMIN_ACCEPTED_NEXT_P2_KTHEORY_SIP',
        current_phase='PHASE_2_FOUR_TRACK_P2_READY',
        second_phase_status='P1_RMIN_ACCEPTED_P2_SIP_DENOMINATOR_NEXT',
        last_checkpoint_session=SID,
        checkpoint_result='.codex/cognition/checkpoints/' + SID + '/result.json',
        next_minimal_verification=(
            'P2-KTHEORY-SIP-001 only: freeze the exact HoTT Book §9.8 Structure Identity Principle denominator; map its '
            '(P,H), standard-structure premises and conclusion against P1 R_min, and determine whether it explicitly preserves '
            'structure or actually bridges naked H/U to Done_s. Do not scan K_app, rerun old controls, or start K_engine.'
        ),
    )
    state['projection']['status'] = 'P1_RMIN_ACCEPTED_WITH_SCOPE / P2_KTHEORY_SIP_NEXT / ABX_IS_P3 / NO_NEW_HOTT_DEFECT_CLAIM'

    session = f'''# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 state mutation for a scoped research-specification result and current-plan update
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: qualify the minimal common source-operation-restoration contract before rule-level or consumer-level HoTT research
- load_receipt: research plan snapshot is saved as `audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-CHECKPOINT-PLAN.json`; four-piece current cognition set was already re-established for this T3 work
- status: COMPLETED_WITH_SCOPE / P1_RMIN_ACCEPTED / P2_SIP_NEXT

P1 reads the current `RichCurve`, source-contract and task-integration interfaces rather than constructing a new theorem. It concludes that `RichCurve` alone is insufficient, while the supplied compound `Input + CurveData + Denotes/Satisfies + O + D` is enough to prevent P2 and P3 from silently changing the circle-puncture task. Existing Agda receipts C-295/C-296/C-320 are recorded only within their explicit local-uncommitted and non-physical scope. A bounded public-source scan locates structure identity, cohesive and stratified/relative analogues without identifying the exact R_min task or a bridge to Done_s.

Wave reflection: this closes the common-oracle edge of the final witness chain. Its value is a fixed task contract and a reason to stop P1, not a mathematical or philosophical defeat claim. The next admissible action is the version-frozen P2 SIP denominator; P3/ABX and P4 remain gated.

| element | use | effect on this unit |
|---|---|---|
| `goal-3.md` §2.1/§3.1 | used | required the academic scan and explicit final-goal/wave continuation judgement |
| `RichCurve` / SourceContract / TaskIntegration | used | supplied source, observation, Done and operation controls without inventing fields |
| existing kernel receipts | used with scope | confirmed the cited controls exist; did not establish version closure or a new theorem |
| HoTT Book/cohesive/stratified sources | used as bounded comparison | selected SIP as a new P2 denominator while preserving task differences |
| ABX external K_app scan | intentionally unused | P3 remains gated until P2 ends |
| engine audit | intentionally unused | no semantic/implementation discrepancy exists to trigger P4 |
'''
    runs = {
        'schema_version': 'hott-session-runs/v1', 'session_id': SID,
        'primary_runs': [{
            'kind': 'p1-source-interface-and-routing-verification',
            'command': f'python3 -B {VERIFY} --write && python3 -B {PLAN_VERIFY} --write',
            'result': 'PASS_WITH_SCOPE; current source anchors, receipt limitations, academic-scan labels, dialogue projection and P2 routing match',
            'mathematics': 'NOT_A_NEW_KERNEL_RUN',
        }],
        'new_math_claims': [], 'new_kernel_replay': False,
        'scope': 'P1 specification qualification and routing only; no new theorem or HoTT-defect claim.',
    }

    new_direction = (
        '| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：R_min、K_theory、K_app、K_engine | 用户要求整体规划、令牌经济、每 wave 的最终目标反思与学术/社区既有成果检查 | `P1_RMIN_ACCEPTED_WITH_SCOPE / P2_SIP_NEXT / NO_DEFECT_VERDICT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；`R-P1-RMIN-SPEC-20260921` | P1关闭；P2只审SIP，P3/P4按准入 | `HoTT后续研究总体方案.md`；P1 receipt；revision220 receipt |\n'
        '| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P3 实际消费者 `K_app` 分支 | 原圆环 A/B/X H/R/K 整备与P1共同任务资格化 | `P1_ACCEPTED / P3_PENDING_P2 / NO_DEFECT_VERDICT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P1；C250–324、D1/D2/D3 | P2结束前不扩展K扫描；既有no-hit不重做 | `ABX行动.md`；总体方案；revision220 receipt |'
    )
    new_panorama = (
        '| `OUT-HOTT-FOUR-TRACK-PLAN` | 第二阶段四分支计划、P1共同规格资格化与P2 SIP路由 | `DIR-U-HOTT-FOUR-TRACK` | P1源接口、既有C295/C296/C320收据、公开结构/凝聚/分层比较 | `P1_RMIN_ACCEPTED_WITH_SCOPE / P2_SIP_NEXT` | 共同强任务合同已固定；SIP是新理论分母 | 不证明R_min新定理、K、HoTT缺陷或完整物理来源 | `audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md`；revision220 receipt |\n'
        '| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环实际消费者分支 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C250–324、68份run、Flash、D1/D2/D3、Book/社区来源及P1合同 | `P1_ACCEPTED / P3_PENDING_P2 / NO_ACTUAL_K` | H/R/U与操作合同已有控制；P1固定共同Done；有界K分母无命中 | 不证明新拓扑、外部全库无K或HoTT缺陷 | `ABX行动.md`；总体方案；revision220 receipt |'
    )
    new_memory = (
        '第二阶段四分支中 P1 已结束：`R_MIN_ACCEPTED_WITH_SCOPE`。`RichCurve` 单独不足，但现有 '
        '`Input + CurveData + Denotes/Satisfies + O + D` 已固定圆去点—闭图—复原的受限共同强任务；既有 '
        'C295/C296/C320 仅以本地未版本闭合 receipt 范围重用。当前唯一下一单元为 `P2-KTHEORY-SIP-001`：'
        '冻结 HoTT Book §9.8，检查 SIP 是否显式保结构或错误桥接 H/U 到 `Done_s`。P3 ABX 和 P4 仍不得启动。'
        '入口：`HoTT后续研究总体方案.md`；revision220 checkpoint。'
    )
    new_frontier = '- P1 已以 `R_MIN_ACCEPTED_WITH_SCOPE` 关闭：共同规格是现有 `Input + CurveData + Denotes/Satisfies + O + D`，不是完整 OriginTop。当前只可做 P2-KTHEORY-SIP-001（HoTT Book §9.8 的版本冻结结构同一性分母）；P3 ABX/K_app 和 P4 K_engine 仍按门槛停止，入口：`HoTT后续研究总体方案.md`。'
    new_resume = '第二阶段四分支中 P1 已关闭：受限 `R_min` 是现有 `Input + CurveData + Denotes/Satisfies + O + D`，并非完整现实来源或 HoTT 缺陷。P1学术检查找到结构同一性、cohesive、分层/相对结构的已知邻域，未找到 H/U→Done_s。当前唯一下一项=P2-KTHEORY-SIP-001，固定 HoTT Book §9.8 SIP；禁止重跑已有H/R/K控制、先扫ABX消费者或触发引擎审计。入口：`HoTT后续研究总体方案.md`；revision220 checkpoint。'
    memory_log = '\nS-RES-20260921-ASTRA-P1-RMIN-SPEC：P1-RMIN-SPEC-001 完成，判词 `R_MIN_ACCEPTED_WITH_SCOPE`。RichCurve单独不足；既有Input、CurveData、Denotes/Satisfies、操作合同和Done足以固定当前圆去点—闭图—复原的共同强任务。C295/C296/C320只在两份LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED receipt范围内复用。结构同一性/cohesive/分层相邻理论的有界公开来源检查不产生同一R_min或K。裁决=CLOSE_WITH_SCOPE并转P2-KTHEORY-SIP-001；P3/P4仍gated。P1与总体计划验证均PASS_WITH_SCOPE；revision220 checkpoint。\n'

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, 'source_state_revision: 219', 'source_state_revision: 220')
            body = replace_once(body, 'projection_generation: 20260921-direction-219', 'projection_generation: 20260921-direction-220')
            body = replace_once(body, 'semantic_status: FOUR_TRACK_PLAN_ADOPTED_P1_RMIN_NEXT', 'semantic_status: P1_RMIN_ACCEPTED_P2_SIP_NEXT')
        elif rel == runtime.PANORAMA:
            body = replace_once(body, 'source_state_revision: 219', 'source_state_revision: 220')
            body = replace_once(body, 'projection_generation: 20260921-outcome-219', 'projection_generation: 20260921-outcome-220')
            body = replace_once(body, 'semantic_status: FOUR_TRACK_PLAN_ADOPTED_P1_RMIN_NEXT', 'semantic_status: P1_RMIN_ACCEPTED_P2_SIP_NEXT')
        elif rel == '方向追踪/002 - 治理与用户方向.md':
            body = replace_line(body, '| `DIR-U-HOTT-FOUR-TRACK` |', new_direction)
        elif rel == '全景视野/003 - 当前机器证明包与原生重放.md':
            body = replace_line(body, '| `OUT-HOTT-FOUR-TRACK-PLAN` |', new_panorama)
        elif rel == 'MEMORY/001 - 当前执行队列.md':
            body = replace_line(body, '第二阶段已采用四分支总体计划：', new_memory)
        elif rel == 'MEMORY/003 - 当前验证状态与顺序日志.md':
            body += memory_log
        elif rel == runtime.PREFIX + 'FRONTIER.md':
            body = replace_once(body, '- 第二阶段四分支计划已采用：P1 R_min 规格资格化是唯一下一单元；P2理论桥、P3 ABX消费者和P4引擎审计均须满足各自准入，入口：`HoTT后续研究总体方案.md`。', new_frontier)
        elif rel == runtime.PREFIX + 'RESUME.md':
            body = replace_once(body, '第二阶段不再仅是ABX：总体计划固定 P1 R_min → P2 K_theory → P3 ABX/K_app，P4 K_engine 只由实际差异触发。当前只做P1规格资格化，禁止重跑已有H/R/K控制或先扫外部消费者。入口：`HoTT后续研究总体方案.md`；revision219 checkpoint。', new_resume)
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
        'authorization': '用户要求把每个wave的最终目标价值、全局坐标、继续或停止理由写入goal-3并在当前P1执行；用户此前授权当前唯一AI持续完成四分支第二阶段的有界研究、更新正确current owners、STATE和canonical checkpoint，且不启动Sub Agent、不push或发布。',
        'files': files,
    }
    (OUT / 'P1-RMIN-SPEC-checkpoint-payload.json').write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan['snapshot'], payload, apply=args.apply)
    suffix = 'P1-RMIN-SPEC-checkpoint-apply.json' if args.apply else 'P1-RMIN-SPEC-checkpoint-dry-run.json'
    (OUT / suffix).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != 'paths'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
