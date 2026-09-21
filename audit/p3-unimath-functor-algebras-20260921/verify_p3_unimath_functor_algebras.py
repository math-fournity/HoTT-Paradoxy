#!/usr/bin/env python3
"""Verify the bounded P3 source-freeze and task-contract audit."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORT = 'audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-REPORT.md'
FREEZE = 'audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-SOURCE-FREEZE.json'
RECEIPT = 'audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-VERIFICATION.json'
P1 = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md'
P2 = 'audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-REPORT.md'
ABX_D2 = 'audit/abx-action-20260921/ABX-3-D2-原生直接消费者审计.md'
ABX_D3 = 'audit/abx-action-20260921/ABX-3-D3-HoTT-Book核心规则审计.md'
N5 = 'audit/derived-development-consumer审计-20260912.md'
N42 = 'audit/unimath-e6-scan-and-nosection-replay-20260913.md'
GOAL_SOP = 'goal-3.md'
PLAN = 'HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md'
NEXT = 'HoTT后续研究总体方案/005 - 当前第一步与交接.md'
GOAL = 'goal.md'
FEATURES = 'feature-list.md'
ABX = 'ABX行动.md'


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.is_file():
        raise SystemExit(f'MISSING: {rel}')
    return path.read_text(encoding='utf-8')


def sha(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def require(rel: str, *markers: str) -> None:
    content = read(rel)
    for marker in markers:
        if marker not in content:
            raise SystemExit(f'MISSING_MARKER: {rel}: {marker!r}')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()

    require(
        REPORT,
        'NO_K_WITHIN_UNIMATH_FUNCTOR_ALGEBRAS_DENOMINATOR',
        'NEW_VERSION_PINNED_CONSUMER_DENOMINATOR',
        'functor_alg_mor', 'is_univalent_disp_functor_alg',
        'STOP_BY_DEFAULT', 'CLOSE_WITH_SCOPE',
    )
    require(P1, 'R_MIN_ACCEPTED_WITH_SCOPE')
    require(P2, 'NO_K_THEORY_WITHIN_SIP_DENOMINATOR')
    require(ABX_D2, 'NO_K_WITHIN_D_ABX_2')
    require(ABX_D3, 'NO_H_TOP_OR_U_TO_DONE_STRONG_BRIDGE_WITHIN_BOOK_D_ABX_3')
    require(N5, 'BOUNDED_DEFENSE')
    require(N42, 'SOURCE_INSPECTED_BOUNDED_NEGATIVE')
    require(GOAL_SOP, '## 2.1 学术与社区既有成果检查', '## 2.2 本地与已登记历史资产侦察', '## 3.1 波次坐标、最终价值与继续裁决')
    require(PLAN, 'P3 已完成的范围结果', 'P4 状态')
    require(NEXT, 'P5-SUCCESSOR-DISCOVERY-001', 'P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001', 'active `/goal` 没有完成')
    require(GOAL, 'NEXT_P6_ORIGIN_STRUCTURE_COMPARISON')
    require(FEATURES, 'NEXT_P6_ORIGIN_STRUCTURE_COMPARISON')
    require(ABX, 'P5 已完成四类入口比较')

    freeze = json.loads(read(FREEZE))
    if freeze.get('commit') != 'ab5f5395fbcfda0b7cb9cbc5bfcb88c4ed9ef8ab':
        raise SystemExit('UNIMATH_COMMIT_MISMATCH')
    files = freeze.get('files')
    if not isinstance(files, list) or len(files) != 2:
        raise SystemExit('UNIMATH_FREEZE_FILE_COUNT')
    expected = {
        'UniMath/CategoryTheory/DisplayedCats/SIP.v': 'e0502499e45e82dc6bd5012d85b1590a399894fb617ac880c408e94aa1aa825e',
        'UniMath/CategoryTheory/DisplayedCats/Examples.v': '0c61bbd9dddcb999a0d134093a8150e8f77db953f8abf4e58387c1f5734ac350',
    }
    actual = {row.get('path'): row.get('sha256') for row in files if isinstance(row, dict)}
    if actual != expected:
        raise SystemExit('UNIMATH_FREEZE_HASHES_MISMATCH')
    if any('/ab5f5395fbcfda0b7cb9cbc5bfcb88c4ed9ef8ab/' not in row.get('raw_url', '') for row in files):
        raise SystemExit('UNIMATH_FREEZE_URL_NOT_PINNED')

    receipt = {
        'schema_version': 'p3-unimath-functor-algebras-verification/v1',
        'status': 'PASS_WITH_SCOPE',
        'scope': (
            'Checks the P3 task contract, local-asset classifications, and the immutable remote-source identity record. '\
            'It does not fetch or compile UniMath, verify Rocq kernel acceptance, prove a global absence of K, or prove a HoTT defect.'
        ),
        'verdict': 'NO_K_WITHIN_UNIMATH_FUNCTOR_ALGEBRAS_DENOMINATOR / P3_CLOSE_WITH_SCOPE / P4_NOT_TRIGGERED / P5_COMPLETE_P6_NEXT',
        'files': {rel: sha(rel) for rel in [REPORT, FREEZE, P1, P2, ABX_D2, ABX_D3, N5, N42, GOAL_SOP, PLAN, NEXT, GOAL, FEATURES, ABX]},
        'remote_source_identity': {'repository': freeze['repository'], 'commit': freeze['commit'], 'files': actual},
        'asset_classification': {
            'ABX_D2_D3': 'NEARBY_ONLY',
            'SIPRepresentation': 'PARTIAL_REUSE',
            'N5_N10_N42': 'NEARBY_ONLY',
            'UniMath_functor_algebras': 'NEW_VERSION_PINNED_CONSUMER_DENOMINATOR',
        },
    }
    if args.write:
        (ROOT / RECEIPT).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    main()
