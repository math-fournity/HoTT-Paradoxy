#!/usr/bin/env python3
"""Checkpoint the bounded P6 object-theory comparison and P7 routing."""
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
SID = 'S-RES-20260921-ASTRA-P6-ORIGIN-STRUCTURE-STRATIFIED'
BASE = '.codex/research/hott/sessions/' + SID + '/'
PLAN_ID = 'R-HOTT-FOUR-TRACK-PLAN-20260921'
ABX_ID = 'R-ABX-ACTION-20260921'
P1_ID = 'R-P1-RMIN-SPEC-20260921'
P2_ID = 'R-P2-KTHEORY-SIP-20260921'
P3_ID = 'R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921'
P5_ID = 'R-P5-SUCCESSOR-DISCOVERY-20260921'
P6_ID = 'R-P6-ORIGIN-STRUCTURE-STRATIFIED-20260921'

REPORT = 'audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md'
VERIFY = 'audit/p6-origin-structure-stratified-20260921/verify_p6_origin_structure_stratified.py'
RECEIPT = 'audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-VERIFICATION.json'
CHECKPOINT = 'audit/p6-origin-structure-stratified-20260921/checkpoint_p6_origin_structure_stratified.py'
P5_REPORT = 'audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md'
P5_VERIFY = 'audit/p5-successor-discovery-20260921/verify_p5_successor_discovery.py'
P5_RECEIPT = 'audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-VERIFICATION.json'
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
PLAN_SHARDS = tuple('HoTT后续研究总体方案/' + name for name in (
    '001 - 上一轮问答与四分支校正.md',
    '002 - 共同任务、术语与优先级原则.md',
    '003 - 分支顺序、准入与停止条件.md',
    '004 - 令牌经济、反漂移与每单元复核.md',
    '005 - 当前第一步与交接.md',
))
LOCAL_P6 = (
    'ABX行动/003 - 原圆环对象、判据与正反控制.md',
    'HoTT/formal/astra-real-geometry/StructuredCurve.lean',
    'HoTT/formal/astra-breakpoint-check/GeometricBoundaryObservation.agda',
    'HoTT/formal/astra-breakpoint-check/BoundaryIncidence.agda',
    'HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda',
    'HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda',
    'audit/astra-case-integration-20260921/MATRIX-BEFORE.md',
    'HoTT/verification/runs/20260920-MP-ASTRA-STRUCTURED-CURVE-001-02/RUN.json',
    'HoTT/verification/runs/20260920-MP-ASTRA-STRUCTURED-CURVE-001-02/source-manifest.json',
    'HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001-01/RUN.json',
    'HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001-01/source-manifest.json',
)
P6_SOURCES = (
    REPORT, VERIFY, RECEIPT, CHECKPOINT,
    P5_REPORT, P5_VERIFY, P5_RECEIPT,
    P1_REPORT, P1_VERIFY, P1_RECEIPT, P2_REPORT, P2_VERIFY, P2_RECEIPT, P3_REPORT, P3_VERIFY, P3_RECEIPT,
    PLAN_INDEX, *PLAN_SHARDS, PLAN_VERIFY, PLAN_RECEIPT,
    'goal.md', 'goal-3.md', 'feature-list.md', 'rulings.md',
    'ABX行动.md', 'ABX行动/005 - 状态、停止条件与未来交接.md', *LOCAL_P6,
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(body: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, body, count=1)
    assert count == 1, old
    return result


def replace_first_line(body: str, prefix: str, replacement: str) -> str:
    lines = body.splitlines()
    for index, line in enumerate(lines):
        if line.startswith(prefix):
            lines[index] = replacement
            return '\n'.join(lines) + '\n'
    raise AssertionError(prefix)


def core_audit(core: dict) -> str:
    headings = re.findall(r'^### (KC-\d+) · .*? · (.+)$', (ROOT / '核心认知.md').read_text(encoding='utf-8'), re.M)
    assert len(headings) == core['kc_count'] == 46
    deepened = {10, 14, 15, 19, 21, 22, 31, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46}
    body = f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: P6_COMPOSITE_DIAGRAM_CANDIDATE_P7_ORIGIN_DIRECTED_DIAGRAM_SPEC_NEXT
- panorama_change: EXISTING_STRUCTURED_CONTROLS_AND_EXTERNAL_OBJECT_THEORY_COMPARED_WITH_SCOPE
- essay_change: NO
- update_decision: P6 ends only its object-theory comparison; P7 must define a minimal compositional specification without reimplementing geometry
- cross_conflicts: existing rich structures can preserve data when explicitly transported; this is a defense against any claim that ordinary equivalence automatically erases all structure
- unresolved: complete OriginDirectedDiagram, actual K, same-task mismatch, implementation discrepancy and independent non-reality judgement remain open

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
'''
    for number, (kc, title) in enumerate(headings, 1):
        if number in deepened:
            relation = 'DEEPENED'
            judgment = 'P6 把来源、边界、闭合、过程与完成拆为可由结构化/定向组合承载的字段，并保留“完整字段可运输”的正控制。'
            evidence = f'{REPORT}；若完整组合接口只是无新约束的同义并列，P7 必须判 RESTATEMENT_ONLY。'
        else:
            relation = 'NOT_TOUCHED'
            judgment = '本单元只比较原圆环对象理论承载，不重裁本条独立用户原文。'
            evidence = 'goal.md §2；无新 kernel 定理、K 或 HoTT 缺陷结论。'
        body += f'| `{kc}` | {title} | {relation} | {judgment} | {evidence} |\n'
    body += '''
## 扩展认知逐片复认

001–008：P6 没有把“理论能表达某结构”偷换为“理论已经完成用户任务”。相反，它把同一任务拆成显式静态图、定向/时间过程与完成观察；既有框架和本地正控制说明抽象边界可以被认真建模，真正问题仍是有没有实际理论使用把忘却后的裸信息升格为强完成。

## 波次定位

- 最终目标连接：P6 推进 R 端的对象/态射/过程/Done 分解，给未来 K 审计提供同任务规格。
- 全局坐标：P1–P3 的分母关闭保持；P5 选择 P6；P6 完成比较并选择 P7；P4仍未触发。
- 实际价值：发现 C-275–279 与 `CurveRun` 是可复用控制，避免重写几何；发现 directed/cospan/cohesive 文献是反解释而非“未知漏洞”。
- 不延续理由：字段矩阵、正控制、最强反解释和外部比较已固定；更多结构名词不会改变范围。
- 裁决：`PARTIAL_REUSE / COMPOSITE_STRUCTURED_DIRECTED_DIAGRAM_CANDIDATE / P7_NEXT`；不形成 HoTT 缺陷结论。
'''
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    for command in ([P1_VERIFY, '--write'], [P2_VERIFY, '--write'], [P3_VERIFY, '--write'], [P5_VERIFY, '--write'], [VERIFY, '--write'], [PLAN_VERIFY, '--write']):
        subprocess.check_call([sys.executable, '-B', *command], cwd=ROOT)
    for rel in P6_SOURCES:
        assert (ROOT / rel).is_file(), rel

    spec = importlib.util.spec_from_file_location('runtime', ROOT / '.codex/tools/cognition_runtime.py')
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding='utf-8'))
    assert state['revision'] == 225
    assert state['latest_session'] == 'S-GOV-20260921-ASTRA-P5-SOURCE-PIN-REFRESH'
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding='utf-8'))
    assert all(sha(ROOT / rel) == digest for rel, digest in head['tracked'].items())
    plan = runtime.plan(ROOT, profile='research', task_ids=[PLAN_ID])
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (OUT / 'P6-ORIGIN-STRUCTURE-STRATIFIED-CHECKPOINT-PLAN.json').write_bytes(runtime.dump(plan))
    for rel in (P1_RECEIPT, P2_RECEIPT, P3_RECEIPT, P5_RECEIPT, RECEIPT, PLAN_RECEIPT):
        assert json.loads((ROOT / rel).read_text(encoding='utf-8'))['status'] == 'PASS_WITH_SCOPE'

    prior_latest = state['latest_session']
    state['revision'] = 226
    state['latest_session'] = SID
    for record_id, label in ((P1_ID, 'P1 remains the scoped common R_min qualification.'), (P2_ID, 'P2 remains the scoped SIP rule result.'), (P3_ID, 'P3 remains the scoped UniMath consumer result.'), (P5_ID, 'P5 remains the successor-selection result.')):
        record = state['records'][record_id]
        record['related_records'] = list(dict.fromkeys(record.get('related_records', []) + [P6_ID, SID]))
        paths = set(record.get('full_sources', [])) | set(record.get('source_hashes', {}))
        record['source_hashes'].update({rel: sha(ROOT / rel) for rel in paths if (ROOT / rel).is_file()})
        record['revalidation'] = record.get('revalidation', '') + ' Revision226 records P6 object-theory comparison; ' + label + ' No frozen denominator is reopened.'

    plan_record = state['records'][PLAN_ID]
    plan_record['evidence_status'] = ('USER_DIRECTED_PORTFOLIO_PLAN / P1_RMIN_ACCEPTED_WITH_SCOPE / P2_SIP_NO_K_WITHIN_SCOPE / '
        'P3_UNIMATH_NO_K_WITHIN_SCOPE / P4_NOT_TRIGGERED / P5_SUCCESSOR_SELECTED / '
        'P6_COMPOSITE_STRUCTURED_DIRECTED_DIAGRAM_CANDIDATE / P7_ORIGIN_DIRECTED_DIAGRAM_SPEC_NEXT / GOAL_ACTIVE')
    plan_record['status'] = 'four_track_first_pass_p5_p6_complete_p7_origin_directed_diagram_spec_next'
    plan_record['full_sources'] = list(dict.fromkeys(plan_record.get('full_sources', []) + list(P6_SOURCES)))
    plan_record['related_records'] = list(dict.fromkeys(plan_record.get('related_records', []) + [P6_ID, SID]))
    paths = set(plan_record['full_sources']) | set(plan_record.get('source_hashes', {}))
    plan_record['source_hashes'].update({rel: sha(ROOT / rel) for rel in paths if (ROOT / rel).is_file()})
    plan_record['revalidation'] = ('Revision226 completes P6: existing local CurvePresentation/RichDiagram/CurveRun controls and published '
        'marked/stratified/cospan/directed/cohesive structures support a composite explicit object candidate. This is not a HoTT defect or actual K; P7 specifies the minimal consumer-ready interface.')
    plan_record['scope'] = ('P6 checks object-theory field coverage only. It finds partial reusable static and process controls and a composite '
        'structured-directed diagram candidate. No universal representation theorem, no actual K, no HoTT defect and no new topology theorem are claimed.')

    abx = state['records'][ABX_ID]
    abx['full_sources'] = list(dict.fromkeys(abx.get('full_sources', []) + list(P6_SOURCES)))
    abx['related_records'] = list(dict.fromkeys(abx.get('related_records', []) + [P6_ID, SID]))
    paths = set(abx['full_sources']) | set(abx.get('source_hashes', {}))
    abx['source_hashes'].update({rel: sha(ROOT / rel) for rel in paths if (ROOT / rel).is_file()})
    abx['revalidation'] = ('Revision226 completes P6 field comparison: structured local controls and external object theories can express parts of R, '
        'and a composite explicit diagram is the candidate. This is neither a K nor a HoTT-defect verdict.')
    abx['scope'] = ('ABX P6 establishes only a field-level object-theory comparison. P7 will make the minimal OriginDirectedDiagram interface '
        'explicit; actual K and same-task mismatch remain independent obligations.')

    state['records'][P6_ID] = {
        'kind': 'result', 'path': REPORT, 'lifecycle_status': 'CURRENT',
        'evidence_status': 'PARTIAL_REUSE / COMPOSITE_STRUCTURED_DIRECTED_DIAGRAM_CANDIDATE / P7_NEXT / NO_NEW_MATHEMATICAL_CLAIM',
        'status': 'complete_with_scope_p7_origin_directed_diagram_spec_next', 'depends_on': [],
        'related_records': [PLAN_ID, ABX_ID, P5_ID, P1_ID, P2_ID, P3_ID, prior_latest],
        'full_sources': list(dict.fromkeys(P6_SOURCES)),
        'source_hashes': {rel: sha(ROOT / rel) for rel in dict.fromkeys(P6_SOURCES)},
        'scope': ('P6 compares field coverage across local CurvePresentation/RichDiagram/CurveRun assets and public marked, stratified, cospan, directed and cohesive frameworks. It establishes a design candidate only; it does not prove a representation/non-representation theorem, actual K or HoTT defect.'),
    }
    state['records'][SID] = {
        'kind': 'session', 'path': BASE + 'SESSION.md', 'lifecycle_status': 'HISTORICAL',
        'evidence_status': 'P6_OBJECT_THEORY_COMPARISON_CHECKPOINTED_WITH_SCOPE', 'status': 'complete_with_scope', 'depends_on': [],
        'related_records': [P6_ID, P5_ID, PLAN_ID, ABX_ID, P1_ID, P2_ID, P3_ID, prior_latest],
        'full_sources': [BASE + name for name in ('SESSION.md', 'RUNS.json', 'CORE_COGNITION_AUDIT.md')],
    }
    state['execution_control'].update(
        status='FOUR_TRACK_FIRST_PASS_P5_P6_COMPLETE_P7_NEXT',
        current_phase='PHASE_2_P6_COMPOSITE_DIAGRAM_CANDIDATE_P7_SPEC_NEXT',
        second_phase_status='P1_P2_P3_SCOPED_NEGATIVES_P4_NOT_TRIGGERED_P5_P6_COMPLETE_P7_NEXT',
        last_checkpoint_session=SID,
        checkpoint_result='.codex/cognition/checkpoints/' + SID + '/result.json',
        next_minimal_verification=('P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-001. Reuse existing CurvePresentation, RichDiagram, CurveRun and Input/Satisfies to specify only the minimal static diagram, trace, Obs, Done_s, structured morphism and forgetful U. Stop as RESTATEMENT_ONLY if no new consumer-checkable constraint is added; otherwise route the resulting fixed interface to a new actual-K denominator.'),
    )
    state['projection']['status'] = 'FOUR_TRACK_FIRST_PASS / P5_P6_COMPLETE / NEXT_P7_ORIGIN_DIRECTED_DIAGRAM_SPEC / GOAL_ACTIVE / NO_NEW_HOTT_DEFECT_CLAIM'

    session = f'''# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 state mutation for bounded P6 object-theory comparison
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: compare OriginPresentation field coverage without duplicating existing formal controls, then select a minimal P7 specification
- load_receipt: research plan snapshot is saved as `audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-CHECKPOINT-PLAN.json`
- status: COMPLETED_WITH_SCOPE / COMPOSITE_DIAGRAM_CANDIDATE / P7_NEXT / NO_NEW_MATHEMATICAL_CLAIM

P6 conducted the required local and public reconnaissance. The local Lean and Cubical packages already provide exact static/boundary positive and negative controls, whose current source hashes still match saved run manifests. Literature shows that marked, stratified, cospan, directed and cohesive structures are relevant existing theories, not newly invented vocabulary. No single checked static structure automatically supplies every source, trace and completion field. A composite explicit diagram is a design candidate, not an ordinary-HoTT failure.

| element | use | effect on this unit |
|---|---|---|
| `goal-3.md` §2.1 | used | public academic search covers stratified, cospan, directed and cohesive alternatives |
| `goal-3.md` §2.2 | used | detects and reuses C-275–279 and CurveRun instead of rewriting them |
| Lean/Cubical source manifests | used | confirms three current formal sources equal their saved kernel-run source hashes |
| local kernel rerun | intentionally not run | exact old receipts were reused; P6 adds no new theorem |
| P7 anti-restatement control | used | prevents a generic interface document from being treated as research progress without new K-checkable content |
'''
    runs = {
        'schema_version': 'hott-session-runs/v1', 'session_id': SID,
        'primary_runs': [{
            'kind': 'p6-source-manifest-academic-and-object-theory-comparison',
            'command': f'python3 -B {P1_VERIFY} --write && python3 -B {P2_VERIFY} --write && python3 -B {P3_VERIFY} --write && python3 -B {P5_VERIFY} --write && python3 -B {VERIFY} --write && python3 -B {PLAN_VERIFY} --write',
            'result': 'PASS_WITH_SCOPE; P6 matrix, local source/run identities and P7 routing agree',
            'mathematics': 'NOT_A_NEW_KERNEL_RUN',
        }], 'new_math_claims': [], 'new_kernel_replay': False,
        'scope': 'P6 object-theory comparison; no universal theorem, actual K, or HoTT-defect claim.',
    }
    new_direction = '| `DIR-U-HOTT-FOUR-TRACK` | 第二阶段四分支：P6组合对象候选与P7最小规格 | 用户要求活跃goal穿过单分母结束；每wave做学术和本地侦察 | `FIRST_PASS_COMPLETE / P5_P6_COMPLETE / NEXT_P7_ORIGIN_DIRECTED_DIAGRAM_SPEC / GOAL_ACTIVE` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE`, `THEORY_ECONOMY` | `R-HOTT-FOUR-TRACK-PLAN-20260921`；P1/P2/P3/P5/P6 | P7用既有接口收敛OriginDirectedDiagram；无新约束则RESTATEMENT_ONLY | `HoTT后续研究总体方案.md`；P6 report；revision226 receipt |'
    new_abx_direction = '| `DIR-U-ABX-ORIGINAL-CIRCLE` | ABX：P6组合对象候选后的最小来源—过程规格 | H/R/K整备、P1/P2/P3、P5/P6对象理论比较 | `NO_ACTUAL_K_IN_TESTED_DENOMINATORS / P6_COMPOSITE_DIAGRAM_CANDIDATE / NEXT_P7_ORIGIN_DIRECTED_DIAGRAM_SPEC` | `PARADOX_DISCOVERY`, `EVIDENCE_DISCIPLINE` | `R-ABX-ACTION-20260921`；P6 | P7固定可被实际K审计的字段，不将组合对象冒充K | `ABX行动.md`；P6 report；revision226 receipt |'
    new_panorama = '| `OUT-HOTT-FOUR-TRACK-PLAN` | 第二阶段P6对象理论比较完成 | `DIR-U-HOTT-FOUR-TRACK` | C-275–279、CurveRun、分层/cospan/定向/cohesive公开来源 | `P6_COMPOSITE_DIAGRAM_CANDIDATE_P7_NEXT` | 局部结构可显式保存字段；裸同胚不自动补齐；P7收敛最小接口 | 不证明新拓扑、全称表示界限、K或HoTT缺陷 | `audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md`；revision226 receipt |'
    new_abx_panorama = '| `OUT-ABX-ACTION-INTAKE` | ABX 原圆环：P6对象理论比较 | `DIR-U-ABX-ORIGINAL-CIRCLE` | C250–324、P1/P2/P3/P5、C-275–279及对象理论文献 | `P6_COMPOSITE_DIAGRAM_CANDIDATE / NEXT_P7_ORIGIN_DIRECTED_DIAGRAM_SPEC` | P7不是新几何，是可审查R接口；实际K仍缺 | 不证明全库无K、完整新拓扑或HoTT缺陷 | `ABX行动.md`；P6 report；revision226 receipt |'
    new_memory = 'P6 对象理论比较已完成：C-275–279/CurveRun 是现有可复用的局部控制，且当前源码与保存 run manifest 一致。标记、分层、cospan、定向路径/类型论与 cohesive 结构显示 R 可由组合的显式对象表达；裸同胚不会自动补齐其字段。当前 P7 只收敛一个最小 `OriginDirectedDiagram` 规格；如果没有新的可被实际 K 消费的约束，必须判 `RESTATEMENT_ONLY` 并换支。入口：`audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md`；revision226 checkpoint。'
    new_frontier = '- P6 已完成：现有 CurvePresentation/RichDiagram/CurveRun 与标记、分层、cospan、定向/cohesive 文献支持组合的显式R对象，非HoTT缺陷。当前P7仅以既有接口收敛 OriginDirectedDiagram；若无新可消费约束则 RESTATEMENT_ONLY，随后换新的实际K或独立R分母。入口：`audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md`。'
    new_resume = '当前 active goal 在 P6 后继续：P6 发现现有CurvePresentation/RichDiagram/CurveRun与标记、分层、cospan、定向/类型论和cohesive结构可组合承载R；裸同胚不自动补齐字段，完整字段可运输是正控制。P7=ORIGIN-DIRECTED-DIAGRAM-SPEC：只收敛已有接口的静态图、trace、Obs、Done_s、结构态射与U；没有新可被K审计的约束就判RESTATEMENT_ONLY并换支。入口：`audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md`；revision226 checkpoint。'
    memory_log = '\nS-RES-20260921-ASTRA-P6-ORIGIN-STRUCTURE-STRATIFIED：P6完成。C-275–279和CurveRun已是可复用的局部结构/过程控制，源码与保存manifest一致；公开分层、cospan、定向和cohesive理论说明R可由组合对象明确表达。判词=COMPOSITE_STRUCTURED_DIRECTED_DIAGRAM_CANDIDATE，不是HoTT缺陷。P7收敛最小规格，若无新K可消费约束则RESTATEMENT_ONLY；revision226 checkpoint。\n'

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode('utf-8')
        if rel == runtime.STATE: body = runtime.dump(state).decode('utf-8')
        elif rel == runtime.DIRECTION:
            body = replace_once(body, 'source_state_revision: 225', 'source_state_revision: 226')
            body = replace_once(body, 'projection_generation: 20260921-direction-225', 'projection_generation: 20260921-direction-226')
            body = replace_once(body, 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_P5_SUCCESSOR_SELECTED_P6_NEXT_SOURCE_PIN_FRESHNESS_REPAIRED', 'semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_COMPLETE_P7_ORIGIN_DIRECTED_DIAGRAM_NEXT')
        elif rel == runtime.PANORAMA:
            body = replace_once(body, 'source_state_revision: 225', 'source_state_revision: 226')
            body = replace_once(body, 'projection_generation: 20260921-outcome-225', 'projection_generation: 20260921-outcome-226')
            body = replace_once(body, 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_P5_SUCCESSOR_SELECTED_P6_NEXT_SOURCE_PIN_FRESHNESS_REPAIRED', 'semantic_status: FOUR_TRACK_FIRST_PASS_P5_P6_COMPLETE_P7_ORIGIN_DIRECTED_DIAGRAM_NEXT')
        elif rel == '方向追踪/002 - 治理与用户方向.md':
            body = replace_first_line(body, '| `DIR-U-HOTT-FOUR-TRACK` |', new_direction)
            body = replace_first_line(body, '| `DIR-U-ABX-ORIGINAL-CIRCLE` |', new_abx_direction)
        elif rel == '全景视野/003 - 当前机器证明包与原生重放.md':
            body = replace_first_line(body, '| `OUT-HOTT-FOUR-TRACK-PLAN` |', new_panorama)
            body = replace_first_line(body, '| `OUT-ABX-ACTION-INTAKE` |', new_abx_panorama)
        elif rel == 'MEMORY/001 - 当前执行队列.md':
            body = replace_first_line(body, 'P5 successor discovery 已完成：', new_memory)
        elif rel == 'MEMORY/003 - 当前验证状态与顺序日志.md': body += memory_log
        elif rel == runtime.PREFIX + 'FRONTIER.md':
            body = replace_once(body, '- P5 successor discovery 已完成：首次 P1/P2/P3 scoped negatives 与 P4_NOT_TRIGGERED 保持，`STOP_BY_DEFAULT` 只禁止重做旧分母。当前 P6 比较 `OriginPresentation` 与带标记、分层、相对 diagram/cohesive 结构，逐字段固定对象、态射、过程和 Done；完整结构编码是强反解释。入口：`audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md`。', new_frontier)
        elif rel == runtime.PREFIX + 'RESUME.md':
            body = replace_once(body, '当前 active goal 在 P5 后继续：P1/P2/P3 各自有界关闭、P4未触发；P5 已选 `P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001`。P6 将 `OriginPresentation` 与标记/分层/相对 diagram/cohesive 结构逐字段比较，区分对象数据、态射保持、过程/trace 与 Done；全字段 transport 是正控制，完整 structured-diagram 编码是反解释。P6 不主张 HoTT 缺陷，结束后仍按goal-3生成 successor。入口：`audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md`；revision224 checkpoint。', new_resume)
        files.append({'path': rel, 'expected_sha256': runtime.sha(raw), 'text': body})
    for name, body in (('SESSION.md', session), ('RUNS.json', runtime.dump(runs).decode('utf-8')), ('CORE_COGNITION_AUDIT.md', core_audit(state['current_core']))):
        files.append({'path': BASE + name, 'expected_sha256': None, 'text': body})
    payload = {'schema_version': 'cognition-checkpoint/v1', 'session_id': SID, 'load_profile': 'research', 'task_ids': [PLAN_ID],
        'authorization': '用户已授权当前唯一AI按goal-3持续推进、做每wave学术和本地侦察、维护current state和canonical checkpoint；不启动Sub Agent、不push、不发布。', 'files': files}
    (OUT / 'P6-ORIGIN-STRUCTURE-STRATIFIED-checkpoint-payload.json').write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan['snapshot'], payload, apply=args.apply)
    suffix = 'P6-ORIGIN-STRUCTURE-STRATIFIED-checkpoint-apply.json' if args.apply else 'P6-ORIGIN-STRUCTURE-STRATIFIED-checkpoint-dry-run.json'
    (OUT / suffix).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != 'paths'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
