#!/usr/bin/env python3
"""Repair P5-era source pins after the applied P5 routing checkpoint.

This is evidence hygiene only: it advances the checkpoint revision because
current projection files and receipts changed, but it does not alter P5's
candidate selection or make a mathematical claim.
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
SID = 'S-GOV-20260921-ASTRA-P5-SOURCE-PIN-REFRESH'
BASE = '.codex/research/hott/sessions/' + SID + '/'
PLAN_ID = 'R-HOTT-FOUR-TRACK-PLAN-20260921'
ABX_ID = 'R-ABX-ACTION-20260921'
P1_ID = 'R-P1-RMIN-SPEC-20260921'
P2_ID = 'R-P2-KTHEORY-SIP-20260921'
P3_ID = 'R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921'
P5_ID = 'R-P5-SUCCESSOR-DISCOVERY-20260921'
P5_VERIFY = 'audit/p5-successor-discovery-20260921/verify_p5_successor_discovery.py'
P5_RECEIPT = 'audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-VERIFICATION.json'
PLAN_VERIFY = 'audit/four-track-plan-20260921/verify_four_track_plan.py'
PLAN_RECEIPT = 'audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json'
P1_VERIFY = 'audit/p1-rmin-spec-20260921/verify_p1_rmin_spec.py'
P2_VERIFY = 'audit/p2-ktheory-sip-20260921/verify_p2_ktheory_sip.py'
P3_VERIFY = 'audit/p3-unimath-functor-algebras-20260921/verify_p3_unimath_functor_algebras.py'
CHECKPOINT = 'audit/p5-successor-discovery-20260921/checkpoint_p5_source_pin_refresh.py'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(body: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, body, count=1)
    assert count == 1, old
    return result


def core_audit(core: dict) -> str:
    headings = re.findall(r'^### (KC-\d+) · .*? · (.+)$', (ROOT / '核心认知.md').read_text(encoding='utf-8'), re.M)
    assert len(headings) == core['kc_count'] == 46
    body = f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: NO_SEMANTIC_CHANGE_P5_SOURCE_PIN_FRESHNESS_REPAIRED
- panorama_change: NO_SEMANTIC_CHANGE_P5_SOURCE_PIN_FRESHNESS_REPAIRED
- essay_change: NO
- update_decision: refresh exact file hashes after P5 current-routing edits; retain P6 as the active next verification
- cross_conflicts: source-hash freshness is a provenance condition, not a new object-theory, HoTT, or reality conclusion
- unresolved: P6 field comparison and all prior mathematical/open obligations are unchanged

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
'''
    for kc, title in headings:
        body += f'| `{kc}` | {title} | NOT_TOUCHED | 本单元仅刷新 P5 后的 source hash 与 current projection revision，不重新裁决本条用户原文。 | `.codex/cognition/checkpoints/{SID}/result.json`；新直接研究证据才触及本条。 |\n'
    body += '''
## 扩展认知逐片复认

001–008：未作新的数学或哲学判断。source-pin freshness 只保证未来 AI 能把 P5 的有界候选选择连回正确版本的报告、当前计划与验证收据。

## 波次定位

- 最终目标连接：本单元不推进数学见证链，保证上一 P5→P6 路由可追溯。
- 全局坐标：P5 已完成，P6 仍为 active next；本修复不能把旧分母关闭或 P6 候选解释为目标停止。
- 实际价值：避免当前文件与 STATE 指向不同 hash，防止未来工作在错误证据版本上重复或误判。
- 不延续理由：该修复的唯一产出是 source-pin 一致性；不产生 P6 的对象理论结果。
- 裁决：`NO_SEMANTIC_CHANGE / GOAL_ACTIVE / P6_NEXT`。
'''
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()

    for command in ([P1_VERIFY, '--write'], [P2_VERIFY, '--write'], [P3_VERIFY, '--write'], [P5_VERIFY, '--write'], [PLAN_VERIFY, '--write']):
        subprocess.check_call([sys.executable, '-B', *command], cwd=ROOT)

    spec = importlib.util.spec_from_file_location('runtime', ROOT / '.codex/tools/cognition_runtime.py')
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text(encoding='utf-8'))
    assert state['revision'] == 224
    assert state['latest_session'] == 'S-RES-20260921-ASTRA-P5-SUCCESSOR-DISCOVERY'
    head = json.loads((ROOT / runtime.HEAD).read_text(encoding='utf-8'))
    assert all(sha(ROOT / rel) == digest for rel, digest in head['tracked'].items())
    plan = runtime.plan(ROOT, profile='research', task_ids=[PLAN_ID])
    assert not plan['hydration_diagnostics']['query_first_promoted']
    (OUT / 'P5-SOURCE-PIN-REFRESH-CHECKPOINT-PLAN.json').write_bytes(runtime.dump(plan))

    prior_latest = state['latest_session']
    state['revision'] = 225
    state['latest_session'] = SID

    # Refresh every existing source pin in the active four-track records,
    # including the P5 list whose tuple contained one duplicate locator.
    for record_id in (P1_ID, P2_ID, P3_ID, PLAN_ID, ABX_ID, P5_ID):
        record = state['records'][record_id]
        record['full_sources'] = list(dict.fromkeys(record.get('full_sources', [])))
        source_paths = set(record['full_sources']) | set(record.get('source_hashes', {}))
        record['source_hashes'].update({rel: sha(ROOT / rel) for rel in source_paths if (ROOT / rel).is_file()})
        record['related_records'] = list(dict.fromkeys(record.get('related_records', []) + [SID]))
        record['revalidation'] = record.get('revalidation', '') + (
            ' Revision225 refreshes P5-era source pins after current-routing projection and receipt updates; '
            'the mathematical/task verdict and P6 routing remain unchanged.'
        )

    state['records'][SID] = {
        'kind': 'session', 'path': BASE + 'SESSION.md', 'lifecycle_status': 'HISTORICAL',
        'evidence_status': 'P5_SOURCE_PIN_FRESHNESS_REPAIRED_NO_SEMANTIC_CHANGE',
        'status': 'complete_no_semantic_change', 'depends_on': [],
        'related_records': [P5_ID, PLAN_ID, ABX_ID, P1_ID, P2_ID, P3_ID, prior_latest],
        'full_sources': [BASE + name for name in ('SESSION.md', 'RUNS.json', 'CORE_COGNITION_AUDIT.md')],
    }
    state['execution_control'].update(
        last_checkpoint_session=SID,
        checkpoint_result='.codex/cognition/checkpoints/' + SID + '/result.json',
    )
    state['projection']['status'] += ' / SOURCE_PIN_FRESHNESS_REPAIRED'

    session = f'''# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 source-pin freshness repair only
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: reconcile P5/P6 current-source hashes after the canonical P5 routing checkpoint
- load_receipt: research plan snapshot is saved as `audit/p5-successor-discovery-20260921/P5-SOURCE-PIN-REFRESH-CHECKPOINT-PLAN.json`
- status: COMPLETED / NO_SEMANTIC_OR_MATHEMATICAL_CHANGE / P6_REMAINS_NEXT

The P5 checkpoint correctly selected P6, but the final receipt refresh and a whitespace normalization changed files that are source-pinned by active P1/P2/P3/P5/plan/ABX records. This session recomputes those hashes and removes a duplicate P5 source locator. No source content is reinterpreted, no theory/consumer candidate is added, and P6 remains the active next task.

| element | use | effect on this unit |
|---|---|---|
| P1/P2/P3/P5/plan verifiers | used | regenerate deterministic receipts before pinning them |
| canonical checkpoint | used | advances revision and preserves atomic session provenance |
| public web research | not rerun | no new research question or external fact is asserted |
| proof assistant kernel | not run | source-pin repair creates no mathematical claim |
'''
    runs = {
        'schema_version': 'hott-session-runs/v1', 'session_id': SID,
        'primary_runs': [{
            'kind': 'p5-source-pin-refresh',
            'command': f'python3 -B {P1_VERIFY} --write && python3 -B {P2_VERIFY} --write && python3 -B {P3_VERIFY} --write && python3 -B {P5_VERIFY} --write && python3 -B {PLAN_VERIFY} --write',
            'result': 'PASS_WITH_SCOPE; active source pins refreshed without semantic change',
            'mathematics': 'NOT_A_KERNEL_RUN',
        }],
        'new_math_claims': [], 'new_kernel_replay': False,
        'scope': 'Evidence-binding repair only; P6 remains the next active research unit.',
    }

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode('utf-8')
        if rel == runtime.STATE:
            body = runtime.dump(state).decode('utf-8')
        elif rel == runtime.DIRECTION:
            body = replace_once(body, 'source_state_revision: 224', 'source_state_revision: 225')
            body = replace_once(body, 'projection_generation: 20260921-direction-224', 'projection_generation: 20260921-direction-225')
            body = replace_once(body, 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_P5_SUCCESSOR_SELECTED_P6_NEXT', 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_P5_SUCCESSOR_SELECTED_P6_NEXT_SOURCE_PIN_FRESHNESS_REPAIRED')
        elif rel == runtime.PANORAMA:
            body = replace_once(body, 'source_state_revision: 224', 'source_state_revision: 225')
            body = replace_once(body, 'projection_generation: 20260921-outcome-224', 'projection_generation: 20260921-outcome-225')
            body = replace_once(body, 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_P5_SUCCESSOR_SELECTED_P6_NEXT', 'semantic_status: FOUR_TRACK_FIRST_PASS_COMPLETE_P5_SUCCESSOR_SELECTED_P6_NEXT_SOURCE_PIN_FRESHNESS_REPAIRED')
        elif rel == 'MEMORY/003 - 当前验证状态与顺序日志.md':
            body += '\nS-GOV-20260921-ASTRA-P5-SOURCE-PIN-REFRESH：P5→P6 路由不变；仅刷新 P1/P2/P3/P5/plan/ABX current source hashes，去除 P5 source list 的重复 locator。无新数学 claim；revision225 checkpoint。\n'
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
        'authorization': '用户已授权当前唯一AI维护 active goal 的正确 current state、证据留痕与 canonical checkpoint；本修复不启动Sub Agent、不push、不发布。',
        'files': files,
    }
    (OUT / 'P5-SOURCE-PIN-REFRESH-checkpoint-payload.json').write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan['snapshot'], payload, apply=args.apply)
    suffix = 'P5-SOURCE-PIN-REFRESH-checkpoint-apply.json' if args.apply else 'P5-SOURCE-PIN-REFRESH-checkpoint-dry-run.json'
    (OUT / suffix).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != 'paths'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
