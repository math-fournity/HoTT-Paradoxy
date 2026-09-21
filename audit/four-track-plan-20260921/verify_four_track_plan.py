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
    for rel in [INDEX, *SHARDS, DIALOGUE, 'goal.md', 'feature-list.md', 'rulings.md', 'ABX行动.md', 'ABX行动/005 - 状态、停止条件与未来交接.md']:
        need(rel)
    marker(INDEX, 'logical_id: HOTT-FOUR-TRACK-PLAN')
    marker(INDEX, 'last_shard: HoTT后续研究总体方案/005 - 当前第一步与交接.md')
    marker(SHARDS[0], '### 用户提问')
    marker(SHARDS[0], '### AI 最终回复')
    marker(SHARDS[1], 'P1：结构规格')
    marker(SHARDS[1], 'P4：实现忠实性')
    marker(SHARDS[2], 'P1：`R_min` 最小规格资格化')
    marker(SHARDS[3], '每个工作单元的最小声明')
    marker(SHARDS[4], '当前第一步')
    marker('goal.md', 'HoTT后续研究总体方案.md')
    marker('feature-list.md', 'F-021')
    marker('rulings.md', '四分支')
    marker('ABX行动.md', 'HoTT后续研究总体方案.md')
    marker('ABX行动/005 - 状态、停止条件与未来交接.md', 'HoTT后续研究总体方案.md')

    receipt = {
        'schema_version': 'four-track-plan-verification/v1',
        'status': 'PASS_WITH_SCOPE',
        'scope': ('Verifies the plan structure, verbatim prior-answer projection, and current routing anchors. '
                  'It does not prove R_min, a K_theory/K_app/K_engine, a new topology, or a HoTT defect.'),
        'files': {rel: sha(need(rel)) for rel in [INDEX, *SHARDS, DIALOGUE]},
        'verdict': 'FOUR_TRACK_PLAN_ROUTED_P1_RMIN_SPEC_FIRST',
    }
    if args.write:
        (ROOT / RECEIPT).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    main()
