#!/usr/bin/env python3
"""Repair source-hash freshness after the P3 first-pass checkpoint."""

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
SID = 'S-GOV-20260921-ASTRA-P3-SOURCE-PIN-REFRESH'
BASE = '.codex/research/hott/sessions/' + SID + '/'
PLAN_ID = 'R-HOTT-FOUR-TRACK-PLAN-20260921'
ABX_ID = 'R-ABX-ACTION-20260921'
P3_ID = 'R-P3-UNIMATH-FUNCTOR-ALGEBRAS-20260921'
P1_VERIFY = 'audit/p1-rmin-spec-20260921/verify_p1_rmin_spec.py'
P2_VERIFY = 'audit/p2-ktheory-sip-20260921/verify_p2_ktheory_sip.py'
P3_VERIFY = 'audit/p3-unimath-functor-algebras-20260921/verify_p3_unimath_functor_algebras.py'
PLAN_VERIFY = 'audit/four-track-plan-20260921/verify_four_track_plan.py'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replace_once(body: str, old: str, new: str) -> str:
    result, count = re.subn(re.escape(old), new, body, count=1)
    assert count == 1, old
    return result


def core_audit(core: dict) -> str:
    headings = re.findall(r'^### (KC-\d+) · .*? · (.+)$', (ROOT / '核心认知.md').read_text(), re.M)
    assert len(headings) == core['kc_count'] == 46
    body = f'''# {SID} 核心认知回评

{core['generation']}；{core['kc_count']} 条。

- core_change: NO
- direction_change: NO_SEMANTIC_CHANGE_SOURCE_PIN_FRESHNESS_REPAIRED
- panorama_change: NO_SEMANTIC_CHANGE_SOURCE_PIN_FRESHNESS_REPAIRED
- essay_change: NO
- update_decision: 修复 P3 后 ABX/plan/P3 record 的 source hash freshness；四分支 first-pass 结论与默认停止不变
- cross_conflicts: 证据哈希失配表示可追溯性需要修复，不是数学结论、外部源码内容或 HoTT 规则发生变化
- unresolved: 仍只有新版本固定consumer、强R、直接证据失效或理论—实现差异可重开；本修复不产生新ingress

| KC | 主题 | relation | 本单元判断 | 证据、停止/反证条件 |
|---|---|---|---|---|
'''
    for kc, title in headings:
        body += f'| `{kc}` | {title} | NOT_TOUCHED | 本单元仅修复 current source-hash 绑定，不重裁该条用户原文或数学方向。 | `.codex/cognition/checkpoints/{SID}/result.json`；新直接研究证据才触及该条。 |\n'
    body += '''
## 扩展认知逐片复认

001–008：未作新的数学或哲学判断。source-pin freshness 是未来 AI 正确读取已有 P1/P2/P3 边界的必要证据卫生，不改变 first-pass 的停止裁决。

## 停止裁决

`FIRST_PASS_STOP_BY_DEFAULT` 保持。该 session 只修复 source hash，不启动任何新 wave。
'''
    return body


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    for script in (P1_VERIFY, P2_VERIFY, P3_VERIFY, PLAN_VERIFY):
        subprocess.check_call([sys.executable, '-B', script, '--write'], cwd=ROOT)

    spec = importlib.util.spec_from_file_location('runtime', ROOT / '.codex/tools/cognition_runtime.py')
    runtime = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(runtime)
    state = json.loads((ROOT / runtime.STATE).read_text())
    assert state['revision'] == 222
    assert state['latest_session'] == 'S-RES-20260921-ASTRA-P3-UNIMATH-FUNCTOR-ALGEBRAS'
    head = json.loads((ROOT / runtime.HEAD).read_text())
    assert all(sha(ROOT / rel) == digest for rel, digest in head['tracked'].items())
    plan = runtime.plan(ROOT, profile='research', task_ids=[PLAN_ID])
    assert set(plan['review_required']) <= {PLAN_ID, ABX_ID, P3_ID}
    (OUT / 'P3-SOURCE-PIN-REFRESH-CHECKPOINT-PLAN.json').write_bytes(runtime.dump(plan))

    prior_latest = state['latest_session']
    state['revision'] = 223
    state['latest_session'] = SID
    for key in (ABX_ID, PLAN_ID, P3_ID):
        record = state['records'][key]
        source_paths = set(record.get('full_sources', [])) | set(record.get('source_hashes', {}))
        record['source_hashes'].update({rel: sha(ROOT / rel) for rel in source_paths if (ROOT / rel).is_file()})
        record['revalidation'] = (
            (str(record.get('revalidation', '')).rstrip() + ' ')
            + 'Revision223 refreshes every existing file source pin after the P3 checkpoint and verifier updates; no mathematical, task, or stop-status conclusion changes.'
        )
    state['records'][SID] = {
        'kind': 'session', 'path': BASE + 'SESSION.md', 'lifecycle_status': 'HISTORICAL',
        'evidence_status': 'SOURCE_PIN_FRESHNESS_REPAIRED_NO_SEMANTIC_CHANGE',
        'status': 'complete', 'depends_on': [],
        'related_records': [P3_ID, PLAN_ID, ABX_ID, prior_latest],
        'full_sources': [BASE + name for name in ('SESSION.md', 'RUNS.json', 'CORE_COGNITION_AUDIT.md')],
    }
    state['execution_control'].update(
        last_checkpoint_session=SID,
        checkpoint_result='.codex/cognition/checkpoints/' + SID + '/result.json',
    )
    state['projection']['status'] = 'FOUR_TRACK_FIRST_PASS_COMPLETE_STOP_BY_DEFAULT / SOURCE_PIN_FRESHNESS_REPAIRED / NO_NEW_HOTT_DEFECT_CLAIM'

    session = f'''# {SID}

- host: Codex desktop local
- model: GPT-6 Astra；服务端路由未由本项目独立认证
- tier: T3 source-hash freshness repair only
- role: CANONICAL_INTEGRATOR_FOR_CURRENT_USER_REQUEST
- objective: repair post-P3 stale source-pin entries without altering the research verdict
- status: COMPLETED / NO_SEMANTIC_OR_MATHEMATICAL_CHANGE

The P3 checkpoint refreshed ABX source hashes from its full-source list but two pre-existing plan-shard hash entries were not in that list. This session recomputes every file-backed source hash in the ABX, four-track plan and P3 records. No source content, task contract, proof, external library assertion, or first-pass stop condition changes.
'''
    runs = {
        'schema_version': 'hott-session-runs/v1', 'session_id': SID,
        'primary_runs': [{
            'kind': 'source-pin-refresh-and-current-receipt-verification',
            'command': f'python3 -B {P1_VERIFY} --write && python3 -B {P2_VERIFY} --write && python3 -B {P3_VERIFY} --write && python3 -B {PLAN_VERIFY} --write',
            'result': 'PASS_WITH_SCOPE; source pins refreshed without semantic change',
            'mathematics': 'NOT_A_KERNEL_RUN',
        }],
        'new_math_claims': [], 'new_kernel_replay': False,
        'scope': 'Evidence binding repair only.',
    }
    log = '\nS-GOV-20260921-ASTRA-P3-SOURCE-PIN-REFRESH：P3 checkpoint 后发现 ABX record 两条既有计划分片 source hash 未随 P3 verifier/plan 更新而刷新。revision223 对ABX、四分支plan和P3 record所有存在文件的source hash重新绑定；无数学、任务、结论或停止状态变化。\n'

    targets = list(runtime.MUTABLE) + list(runtime.mutable_shard_paths(ROOT))
    files = []
    for rel in targets:
        raw = (ROOT / rel).read_bytes()
        body = raw.decode()
        if rel == runtime.STATE:
            body = runtime.dump(state).decode()
        elif rel == runtime.DIRECTION:
            body = replace_once(body, 'source_state_revision: 222', 'source_state_revision: 223')
            body = replace_once(body, 'projection_generation: 20260921-direction-222', 'projection_generation: 20260921-direction-223')
        elif rel == runtime.PANORAMA:
            body = replace_once(body, 'source_state_revision: 222', 'source_state_revision: 223')
            body = replace_once(body, 'projection_generation: 20260921-outcome-222', 'projection_generation: 20260921-outcome-223')
        elif rel == 'MEMORY/003 - 当前验证状态与顺序日志.md':
            body += log
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
        'authorization': '用户授权当前唯一AI持续维护正确治理、状态和证据；本次仅修复P3后发现的source-pin freshness缺口，不启动新数学研究、Sub Agent、push或发布。',
        'files': files,
    }
    (OUT / 'P3-SOURCE-PIN-REFRESH-checkpoint-payload.json').write_bytes(runtime.dump(payload))
    result = runtime.checkpoint(ROOT, plan['snapshot'], payload, apply=args.apply)
    suffix = 'P3-SOURCE-PIN-REFRESH-checkpoint-apply.json' if args.apply else 'P3-SOURCE-PIN-REFRESH-checkpoint-dry-run.json'
    (OUT / suffix).write_bytes(runtime.dump(result))
    print(json.dumps({key: value for key, value in result.items() if key != 'paths'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
