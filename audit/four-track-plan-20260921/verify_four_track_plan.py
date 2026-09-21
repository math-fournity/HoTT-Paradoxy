#!/usr/bin/env python3
"""Verify the scoped four-track future-work plan and its routing anchors."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DIALOGUE = 'audit/four-track-plan-20260921/build_four_track_dialogue.py'
P1_VERIFY = 'audit/p1-rmin-spec-20260921/verify_p1_rmin_spec.py'
P1_REPORT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md'
P1_RECEIPT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-VERIFICATION.json'
INDEX = 'HoTT后续研究总体方案.md'
SHARDS = [
    'HoTT后续研究总体方案/001 - 上一轮问答与四分支校正.md',
    'HoTT后续研究总体方案/002 - 共同任务、术语与优先级原则.md',
    'HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md',
    'HoTT后续研究总体方案/004 - 令牌经济、反漂移与每单元复核.md',
    'HoTT后续研究总体方案/005 - 当前第一步与交接.md',
]
RECEIPT = 'audit/four-track-plan-20260921/FOUR-TRACK-PLAN-VERIFICATION.json'


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def need(rel: str) -> Path:
    path = ROOT / rel
    if not path.is_file():
        raise SystemExit(f'missing source: {rel}')
    return path


def marker(rel: str, value: str) -> None:
    if value not in need(rel).read_text(encoding='utf-8'):
        raise SystemExit(f'missing marker {value!r} in {rel}')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()

    subprocess.check_call([sys.executable, '-B', DIALOGUE, '--check'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', P1_VERIFY, '--write'], cwd=ROOT)
    for rel in [INDEX, *SHARDS, DIALOGUE, P1_VERIFY, P1_REPORT, P1_RECEIPT, 'goal.md', 'feature-list.md', 'rulings.md', 'ABX行动.md', 'ABX行动/005 - 状态、停止条件与未来交接.md']:
        need(rel)
    marker(INDEX, 'logical_id: HOTT-FOUR-TRACK-PLAN')
    marker(INDEX, 'last_shard: HoTT后续研究总体方案/005 - 当前第一步与交接.md')
    marker(SHARDS[0], '### 用户提问')
    marker(SHARDS[0], '### AI 最终回复')
    marker(SHARDS[1], 'P1：结构规格')
    marker(SHARDS[1], 'P4：实现忠实性')
    marker(INDEX, 'P1_RMIN_ACCEPTED_WITH_SCOPE')
    marker(SHARDS[2], 'P1：`R_min` 最小规格资格化')
    marker(SHARDS[2], 'P1 已完成的范围结果')
    marker(SHARDS[2], 'P2-KTHEORY-SIP-001')
    marker(SHARDS[3], '每个工作单元的最小声明')
    marker(SHARDS[4], 'P2-KTHEORY-SIP-001')
    marker('goal.md', 'NEXT_P2_KTHEORY_SIP')
    marker('feature-list.md', 'P1_RMIN_ACCEPTED_WITH_SCOPE')
    marker('rulings.md', '四分支')
    marker('ABX行动.md', 'P2 正待审一个新的 HoTT Book §9.8 SIP')
    marker('ABX行动/005 - 状态、停止条件与未来交接.md', 'HoTT后续研究总体方案.md')

    receipt = {
        'schema_version': 'four-track-plan-verification/v1',
        'status': 'PASS_WITH_SCOPE',
        'scope': ('Verifies the plan structure, verbatim prior-answer projection, P1 source/interface receipt, '
                  'and current P2-SIP routing anchors. It does not prove a new R_min theorem, a K_theory/K_app/K_engine, '
                  'a new topology, or a HoTT defect.'),
        'files': {rel: sha(need(rel)) for rel in [INDEX, *SHARDS, DIALOGUE, P1_VERIFY, P1_REPORT, P1_RECEIPT]},
        'verdict': 'FOUR_TRACK_PLAN_P1_CLOSED_P2_SIP_NEXT',
    }
    if args.write:
        (ROOT / RECEIPT).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    main()
