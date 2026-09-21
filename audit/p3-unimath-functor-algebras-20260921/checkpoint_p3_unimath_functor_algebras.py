#!/usr/bin/env python3
"""Checkpoint the bounded P3 UniMath consumer audit and first-pass stop."""

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
SID = 'S-RES-20260921-ASTRA-P3-UNIMATH-FUNCTOR-ALGEBRAS'
BASE = '.codex/research/hott/sessions/' + SID + '/'
PLAN_ID = 'R-HOTT-FOUR-TRACK-PLAN-20260921'
ABX_ID = 'R-ABX-ACTION-20260921'
P1_ID = 'R-P1-RMIN-SPEC-20260921'
P2_ID = 'R-P2-KTHEORY-SIP-20260921'
P3_ID = 'R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921'
REPORT = 'audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-REPORT.md'
FREEZE = 'audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-SOURCE-FREEZE.json'
VERIFY = 'audit/p3-unimath-functor-algebras-20260921/verify_p3_unimath_functor_algebras.py'
RECEIPT = 'audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-VERIFICATION.json'
CHECKPOINT = 'audit/p3-unimath-functor-algebras-20260921/checkpoint_p3_unimath_functor_algebras.py'
P1_REPORT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md'
P1_VERIFY = 'audit/p1-rmin-spec-20260921/verify_p1_rmin_spec.py'
P1_RECEIPT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-VERIFICATION.json'
P2_REPORT = 'audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-REPORT.md'
P2_VERIFY = 'audit/p2-ktheory-sip-20260921/verify_p2_ktheory_sip.py'
P2_RECEIPT = 'audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-VERIFICATION.json'
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
ABX_D2 = 'audit/abx-action-20260921/ABX-3-D2-原生直接消费者审计.md'
ABX_D3 = 'audit/abx-action-20260921/ABX-3-D3-HoTT-Book核心规则审计.md'
N5 = 'audit/derived-development-consumer审计-20260912.md'
N42 = 'audit/unimath-e6-scan-and-nosection-replay-20260913.md'
P3_SOURCES = (
    REPORT, FREEZE, VERIFY, RECEIPT, CHECKPOINT,
    P1_REPORT, P1_VERIFY, P1_RECEIPT, P2_REPORT, P2_VERIFY, P2_RECEIPT,
    ABX_D2, ABX_D3, N5, N42,
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
- direction_change: P3_UNIMATH_ACTUAL_CONSUMER_DENOMINATOR_CLOSED_AND_FIRST_PASS_STOPPED
- panorama_change: VERSION_PINNED_EXTERNAL_SIP_CONSUMER_AUDITED_WITH_SCOPE
- essay_change: NO
- update_decision: P1/P2/P3 first pass 已结束；P4 未触发。没有新的版本固定消费者、强R、证据失效或实现差异时默认停止
- cross_conflicts: 外部库实际使用 SIP、Book 理论、P1 圆环任务和现实过程完成是不同层次；实际库调用不能因含 SIP 自动成为同任务 K
- unresolved: 其它版本固定 K_app、完整 OriginTop/物理过程、同任务失配、实现语义差异和独立非现实性判词仍为未来有条件问题

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
'''
    for number, (kc, title) in enumerate(headings, 1):
        if number in corrected:
            relation = 'CORRECTED'
            judgement = 'P3 对真实 UniMath 调用进行版本固定审计，确认它把结构保持作为前提而不是把等价/forgetful结果当作圆环强完成。'
            evidence = f'{REPORT}；{RECEIPT}；新调用链满足同一P1 Input/Operation/Done 才可改变范围。'
        elif number in deepened:
            relation = 'DEEPENED'
            judgement = 'P3 将现实对齐的消费者义务落到外部源码版本、入口、结构条件与输出类型，并按资产侦察避免重做已有 local/Book 工作。'
            evidence = f'{REPORT}；{FREEZE}；新版本固定consumer或强R才可重开。'
        else:
            relation = 'NOT_TOUCHED'
            judgement = '本单元只审计一个版本固定的外部 SIP 调用，不重新裁决本条独立用户原文。'
            evidence = 'goal.md §2；无新数学定理或现实结论。'
        body += f'| `{kc}` | {title} | {relation} | {judgement} | {evidence} |\n'
    body += '''
## 扩展认知逐片复认

001–008：P3 把“现实缺口”严格保持为同任务、同操作、同观察、同完成的消费者义务。外部库显式结构化并证明范畴 univalence 是有价值的负向实例，但不等于圆环任务被理论完成或被否定。

## 波次定位

- 最终目标连接：P3 检验最终见证链的实际消费者边，使用版本固定 UniMath 源码而非理论标题。
- 全局坐标：P1固定共同强任务，P2关闭SIP规则桥，P3关闭第一个外部实际consumer分母；P4没有触发事实。
- 实际价值：把可能的外部K收窄为明确源码条件；防止未来AI把真实SIP使用本身误当作用户圆环强完成的证据。
- 继续检验：同一分母已无新增操作、观察或完成条件可查；继续必须换成一个新、版本固定、可能承担P1 Done_s的调用链。
- 不延续理由：当前计划只要求一个新的实际消费者分母；本分母已出现明确结构保持和任务不等，更多同义扫描不会改变判词。
- 裁决：CLOSE_WITH_SCOPE；P4_NOT_TRIGGERED；FIRST_PASS_STOP_BY_DEFAULT。

## 停止裁决

四分支 first pass 已完成，默认停止。只有新版本固定消费者、更强可判定R、直接证据失效或可重放理论—实现差异能重开；否则不得扩大为无边界全库扫描或“HoTT无问题/有问题”的总判词。
'''
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()

    subprocess.check_call([sys.executable, '-B', P1_VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', P2_VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', PLAN_VERIFY, '--write'], cwd=ROOT)
    for rel in P3_SOURCES:
        assert (ROOT / rel).is_file(), rel

    spec = importlib.util.spec_from_file_location('runtime', ROOT / '.codex/tools/cognition_runtime.py')
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state['revision'] == 221
    assert state['latest_session'] == 'S-RES-20260921-ASTRA-P2-KTHEORY-SIP'
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head['tracked'].items())
    plan = runtime.plan(ROOT, profile='research', task_ids=[PLAN_ID])
    assert set(plan['review_required']) <= {PLAN_ID, ABX_ID, P1_ID, P2_ID}
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (OUT / 'P3-UNIMATH-FUNCTOR-ALGEBRAS-CHECKPOINT-PLAN.json').write_bytes(runtime.dump(plan))
    for rel in (P1_RECEIPT, P2_RECEIPT, RECEIPT, PLAN_RECEIPT):
        assert json.loads((ROOT / rel).read_text())['status'] == 'PASS_WITH_SCOPE'

    prior_latest = state['latest_session']
    state['revision'] = 222
    state['latest_session'] = SID
    for prior_id, note in (
        (P1_ID, 'Revision222 refreshes P1 source pins after the completed P2/P3 routing updates; P1 remains the scoped common R_min qualification.'),
        (P2_ID, 'Revision222 refreshes P2 source pins after the completed P3 external-consumer audit; P2 remains the scoped SIP no-bridge result.'),
    ):
        record = state['records'][prior_id]
        record['related_records'] = list(dict.fromkeys(record['related_records'] + [P3_ID, SID]))
        record['source_hashes'].update({rel: sha(ROOT / rel) for rel in record['full_sources']})
        record['revalidation'] = note

    plan_record = state['records'][PLAN_ID]
    plan_record['evidence_status'] = (
        'USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / '\
        'P2_SIP_NO_K_WITHIN_SCOPE / P3_UNIMATH_NO_K_WITHIN_SCOPE / P4_NOT_TRIGGERED / FIRST_PASS_STOP_BY_DEFAULT'
    )
    plan_record['status'] = 'four_track_first_pass_complete_stop_by_default'
    plan_record['full_sources'] = list(dict.fromkeys(plan_record['full_sources'] + list(P3_SOURCES)))
    plan_record['related_records'] = list(dict.fromkeys(plan_record['related_records'] + [P3_ID, SID]))
    plan_record['source_hashes'].update({rel: sha(ROOT / rel) for rel in plan_record['full_sources']})
    plan_record['revalidation'] = (
        'Revision222 completes the first P3 version-pinned external consumer denominator: UniMath functor algebras uses '\
        'explicit SIP structure conditions to prove univalence and has no P1 strong-task bridge. The first four-track pass '\
        'therefore stops by default; this is not a global no-K or HoTT-defect conclusion.'
    )
    plan_record['scope'] = (
        'First four-track pass complete: P1 restricted R_min; P2 Book SIP no theory bridge; P3 UniMath functor-algebras '\
        'external consumer no same-task K; P4 not triggered. Reopen only for a new version-pinned consumer, stronger R, '\
        'direct evidence invalidation, or reproducible theory/implementation semantic discrepancy.'
    )

    abx = state['records'][ABX_ID]
    abx['full_sources'] = list(dict.fromkeys(abx['full_sources'] + [REPORT, FREEZE, VERIFY, RECEIPT, PLAN_INDEX, PLAN_RECEIPT]))
    abx['related_records'] = list(dict.fromkeys(abx['related_records'] + [P3_ID, SID]))
    abx_source_paths = set(abx['full_sources']) | set(abx.get('source_hashes', {}))
    abx['source_hashes'].update({rel: sha(ROOT / rel) for rel in abx_source_paths if (ROOT / rel).is_file()})
    abx['revalidation'] = (
        'Revision222 closes the first P3 denominator: the version-pinned UniMath functor-algebras use of SIP consumes '\
        'explicit structure compatibility and returns univalence, not P1 Done_s. Along with P1/P2, this completes the '\
        'first pass; ABX is STOP_BY_DEFAULT until an admissible new ingress appears.'
    )
    abx['scope'] = (
        'ABX has completed its first four-track pass: common R_min is scoped, SIP has no rule bridge, and one external '\
        'actual SIP consumer is a task-distinct structural defense. This does not prove that no external K exists; new '\
        'work needs a version-pinned consumer, stronger R, direct evidence failure, or implementation discrepancy.'
    )

    state['records'][P3_ID] = {
        'kind': 'result', 'path': REPORT, 'lifecycle_status': 'CURRENT',
        'evidence_status': (
            'NO_K_WITHIN_UNIMATH_FUNCTOR_ALGEBRAS_DENOMINATOR / VERSION_PINNED_REMOTE_SOURCE_INSPECTED / '\
            'LOCAL_ASSET_AND_ACADEMIC_RECONNAISSANCE / P4_NOT_TRIGGERED / NO_NEW_MATHEMATICAL_CLAIM'
        ),
        'status': 'complete_with_scope_first_pass_stop_by_default', 'depends_on': [],
        'related_records': [P1_ID, P2_ID, PLAN_ID, ABX_ID, prior_latest],
        'full_sources': list(P3_SOURCES),
        'source_hashes': {rel: sha(ROOT / rel) for rel in P3_SOURCES},
        'scope': (
            'P3 audits one immutable UniMath external SIP consumer. It identifies explicit functor-algebra structure '\
            'compatibility and an is_univalent output, not a bare H/U input or the P1 circle process Done_s. It does not '\
            'fetch/compile UniMath in this project, prove global no-K, or prove a HoTT defect.'
        ),
    }
    state['records'][SID] = {
        'kind': 'session', 'path': BASE + 'SESSION.md', 'lifecycle_status': 'HISTORICAL',
        'evidence_status': 'P3_UNIMATH_EXTERNAL_CONSUMER_AUDIT_CHECKPOINTED_WITH_SCOPE',
        'status': 'complete_with_scope', 'depends_on': [],
        'related_records': [P3_ID, P2_ID, P1_ID, PLAN_ID, ABX_ID, prior_latest],
        'full_sources': [BASE + name for name in ('SESSION.md', 'RUNS.json', 'CORE_COGNITION_AUDIT.md')],
    }
    state['execution_control'].update(
        portfolio_record=PLAN_ID,
        status='FOUR_TRACK_FIRST_PASS_COMPLETE_STOP_BY_DEFAULT',
        current_phase='PHASE_2_FOUR_TRACK_FIRST_PASS_COMPLETE',
        second_phase_status='P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_STOP_BY_DEFAULT',
        last_checkpoint_session=SID,
        checkpoint_result='.codex/cognition/checkpoints/' + SID + '/result.json',
        next_minimal_verification=(
            'STOP_BY_DEFAULT. Reopen only for a version-pinned external consumer whose actual input/output can plausibly '\
            'bridge H/U to the same P1 Done_s; a user/independent-source stronger R_min; direct evidence invalidation; '\
            'or reproducible theory/implementation semantic discrepancy. Run goal-3 academic and local-asset reconnaissance first.'
        ),
    )
    state['projection']['status'] = 'FOUR_TRACK_FIRST_PASS_COMPLETE_STOP_BY_DEFAULT / P1_P2_P3_SCOPED_NEGATIVES / P4_NOT_TRIGGERED / NO_NEW_HOTT_DEFECT_CLAIM'

    session = f'''# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 state mutation for a version-pinned external-source consumer audit and stop decision
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: audit one real external SIP consumer against P1's same-task source-operation-observation-Done contract
- load_receipt: research plan snapshot is saved as `audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-CHECKPOINT-PLAN.json`; remote source identity is pinned in `P3-UNIMATH-FUNCTOR-ALGEBRAS-SOURCE-FREEZE.json`
- status: COMPLETED_WITH_SCOPE / NO_K_WITHIN_UNIMATH_FUNCTOR_ALGEBRAS_DENOMINATOR / FIRST_PASS_STOP_BY_DEFAULT

P3 performs both required reconnaissance layers. Local historical audits show that the chosen UniMath Rocq denominator is distinct from ABX local consumers, Book rules, old Bool SIP proof, agda-unimath and toolchain scans. Public UniMath source is fixed at commit `ab5f5395…`: `Examples.v` explicitly builds functor-algebra compatibility and calls the SIP helper from `SIP.v` to prove a displayed-category univalence property. It does not accept bare carrier information or assert the P1 circle process's Done_s.

Wave reflection: P3 closes the actual-consumer edge for this first external denominator, and with P1/P2 completes the planned first pass. Continuing the same denominator would duplicate the fixed invocation and its task mismatch. P4 has no trigger. Further work now requires new evidence rather than more scanning.

| element | use | effect on this unit |
|---|---|---|
| `goal-3.md` §2.1 | used | selected official UniMath docs and version-pinned public source rather than a generic SIP discussion |
| `goal-3.md` §2.2 | used | distinguished local ABX/N5/N42/SIP assets from the new external Rocq consumer |
| `git ls-remote` + immutable raw URLs | used | fixed repository commit and file hashes without modifying the external library |
| UniMath SIP/Examples invocation | used | establishes actual explicit-structure consumer behavior at the selected source lines |
| Rocq compilation | intentionally not run | this is a source audit, not a local replay/certification of external library code |
| P4 engine audit | intentionally not run | no theory-versus-implementation discrepancy was observed |
'''
    runs = {
        'schema_version': 'hott-session-runs/v1', 'session_id': SID,
        'primary_runs': [{
            'kind': 'p3-source-freeze-local-asset-and-routing-verification',
            'command': f'python3 -B {P1_VERIFY} --write && python3 -B {P2_VERIFY} --write && python3 -B {VERIFY} --write && python3 -B {PLAN_VERIFY} --write',
            'result': 'PASS_WITH_SCOPE; local-asset categories, remote immutable identifiers, task-contract boundary and first-pass stop routing match',
            'mathematics': 'NOT_A_NEW_KERNEL_RUN',
        }],
        'new_math_claims': [], 'new_kernel_replay': False,
        'scope': 'P3 external source audit and routing only; no external compilation, theorem or HoTT-defect claim.',
    }

    new_direction = (
        '| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支首次有界pass | 用户要求每wave反思、学术调查与本地/历史资产侦察 | `P1_P2_P3_SCOPED_NEGATIVES / P4_NOT_TRIGGERED / STOP_BY_DEFAULT` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1/P2/P3 records | 首次pass结束；仅合格新ingress重开 | `HoTT后续研究总体方案.md`；P3 receipt；revision222 receipt |\n'
        '| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：原圆环实际消费者 `K_app` 分支 | H/R/K整备、P1/P2与UniMath P3外部调用审计 | `FIRST_PASS_STOP_BY_DEFAULT / NO_ACTUAL_K_IN_TESTED_DENOMINATORS` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P1/P2/P3 | 新版本固定consumer、强R、直接失效或实现差异才重开 | `ABX行动.md`；总体方案；revision222 receipt |'
    )
    new_panorama = (
        '| `OUT-HOTT-FOUR-TRACK-PLAN` | 第二阶段四分支首次pass：P1规格、P2规则、P3外部消费者与P4触发判定 | `DIR-U-HOTT-FOUR-TRACK` | P1接口、Book/SIP、UniMath固定外部源码、历史资产/公开文献 | `FIRST_PASS_COMPLETE_STOP_BY_DEFAULT` | P1固定强任务；P2/P3各一分母无桥；P4无触发 | 不证明全局无K、HoTT无问题/有缺陷或完整物理来源 | `audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-REPORT.md`；revision222 receipt |\n'
        '| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环实际消费者首个外部 P3 分母 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C250–324、D1/D2/D3、P1/P2、UniMath functor-algebras | `FIRST_PASS_STOP_BY_DEFAULT / NO_ACTUAL_K_IN_TESTED_DENOMINATORS` | UniMath调用显式保结构、输出univalence，不同于P1 Done | 不证明外部全库无K或HoTT缺陷 | `ABX行动.md`；P3 report；revision222 receipt |'
    )
    new_memory = (
        '四分支首次 pass 已完成并 `STOP_BY_DEFAULT`：P1 固定受限 `R_min`；P2 在 Book §9.8 SIP 中无 '\
        'H/U→`Done_s` 规则桥；P3 审计版本固定 UniMath functor-algebras 的实际 SIP 调用，发现其显式保结构并仅证明 '\
        'univalence，不是圆环强完成；P4未触发。后续仅在新版本固定consumer、强R、直接证据失效或理论—实现可重放差异时启动，且先执行goal-3双重侦察。入口：`HoTT后续研究总体方案.md`；revision222 checkpoint。'
    )
    new_frontier = '- 四分支首次pass已完成并默认停止：P1共同R_min、P2 Book SIP、P3 UniMath实际consumer均未给H/U→P1 Done_s，P4无触发。只接受新版本固定消费者、强R、直接证据失效或可重放理论—实现差异；每次先按goal-3做学术和资产侦察，入口：`HoTT后续研究总体方案.md`。'
    new_resume = '四分支首次pass已完成并STOP_BY_DEFAULT：P1固定受限R_min；P2 Book §9.8 SIP为显式结构保持；P3 UniMath@ab5f5395 functor-algebras实际调用显式结构、输出univalence，不是P1 Done_s；P4未触发。不要用更多关键词/同义库扩张。仅新版本固定consumer、强R、直接失效或可重放理论—实现差异可重开，且先走goal-3学术+资产侦察。入口：`HoTT后续研究总体方案.md`；revision222 checkpoint。'
    memory_log = '\nS-RES-20260921-ASTRA-P3-UNIMATH-FUNCTOR-ALGEBRAS：P3第一个外部版本固定消费者分母完成。UniMath@ab5f5395的Examples.v functor_algebras明确构造functor_alg_mor并调用SIP helper，输出is_univalent_disp；没有bare H/U或P1圆环Done_s。判词NO_K_WITHIN_UNIMATH_FUNCTOR_ALGEBRAS_DENOMINATOR。P1/P2/P3首次pass完成、P4_NOT_TRIGGERED、STOP_BY_DEFAULT。新入场仅限版本固定consumer、强R、直接证据失效或可重放理论—实现差异；先做goal-3双重侦察。验证PASS_WITH_SCOPE；revision222 checkpoint。\n'

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, 'source_state_revision: 221', 'source_state_revision: 222')
            body = replace_once(body, 'projection_generation: 20260921-direction-221', 'projection_generation: 20260921-direction-222')
            body = replace_once(body, 'semantic_status: P1_P2_CLOSED_P3_KAPP_DENOMINATOR_SELECTION_NEXT', 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_STOP_BY_DEFAULT')
        elif rel == runtime.PANORAMA:
            body = replace_once(body, 'source_state_revision: 221', 'source_state_revision: 222')
            body = replace_once(body, 'projection_generation: 20260921-outcome-221', 'projection_generation: 20260921-outcome-222')
            body = replace_once(body, 'semantic_status: P1_P2_CLOSED_P3_KAPP_DENOMINATOR_SELECTION_NEXT', 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_STOP_BY_DEFAULT')
        elif rel == '方向追踪/002 - 治理与用户方向.md':
            body = replace_line(body, '| `DIR-U-HOTT-FOUR-TRACK` |', new_direction)
        elif rel == '全景视野/003 - 当前机器证明包与原生重放.md':
            body = replace_line(body, '| `OUT-HOTT-FOUR-TRACK-PLAN` |', new_panorama)
        elif rel == 'MEMORY/001 - 当前执行队列.md':
            body = replace_line(body, '第二阶段四分支中 P1/P2 已结束：', new_memory)
        elif rel == 'MEMORY/003 - 当前验证状态与顺序日志.md':
            body += memory_log
        elif rel == runtime.PREFIX + 'FRONTIER.md':
            body = replace_once(body, '- P1/P2 均已关闭：共同 `R_min` 已固定，Book §9.8 SIP 在其明确结构保持范围内没有 H/U→Done_s 桥，既有 SIP 资产已分类且不重跑。当前只可做 P3-KAPP-DENOMINATOR-001 的版本固定消费者选择；P4仍无触发，入口：`HoTT后续研究总体方案.md`。', new_frontier)
        elif rel == runtime.PREFIX + 'RESUME.md':
            body = replace_once(body, '第二阶段四分支中 P1/P2 已关闭：P1的受限R_min是Input + CurveData + Denotes/Satisfies + O + D；P2以Book §9.8和既有原生SIP边界排除SIP作为裸H/U→Done_s理论桥。新用户SOP要求每wave同时做公开学术检索与本地/历史资产侦察。当前唯一下一项=P3-KAPP-DENOMINATOR-001：挑选未覆盖、版本冻结、有入口的实际消费者；禁止重跑旧SIP、先扫无版本关键词或触发引擎审计。入口：`HoTT后续研究总体方案.md`；revision221 checkpoint。', new_resume)
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
        'authorization': '用户要求按goal-3对每wave实施学术/社区与本地/历史资产侦察、持续反思并交付有效成果；用户此前授权当前唯一AI更新正确current owners、STATE和canonical checkpoint，且不启动Sub Agent、不push或发布。',
        'files': files,
    }
    (OUT / 'P3-UNIMATH-FUNCTOR-ALGEBRAS-checkpoint-payload.json').write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan['snapshot'], payload, apply=args.apply)
    suffix = 'P3-UNIMATH-FUNCTOR-ALGEBRAS-checkpoint-apply.json' if args.apply else 'P3-UNIMATH-FUNCTOR-ALGEBRAS-checkpoint-dry-run.json'
    (OUT / suffix).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != 'paths'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
