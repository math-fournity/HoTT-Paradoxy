#!/usr/bin/env python3
"""Verify the bounded P2 SIP source/reuse audit without replaying old proofs."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORT = 'audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-REPORT.md'
RECEIPT = 'audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-VERIFICATION.json'
BOOK = 'sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/categories.tex'
P1 = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md'
SIP_SOURCE = 'HoTT/formal/sip-representation/SIPRepresentation.agda'
SIP_RUN = 'HoTT/verification/runs/20260912-MP-SIP-REPRESENTATION-001-01/RUN.json'
SIP_REPORT = 'audit/sip-representation机器证明实施证据-20260912.md'
RELATIONAL = 'sources/webgpt/workspace-snapshot/.codex/research/hott/sessions/S-ANS-20260910-008-RELATIONAL-SIP/PROOF_NOTE.md'
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
    text = read(rel)
    for marker in markers:
        if marker not in text:
            raise SystemExit(f'MISSING_MARKER: {rel}: {marker!r}')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()

    require(
        REPORT,
        'NO_K_THEORY_WITHIN_SIP_DENOMINATOR',
        'SIP_EXPLICIT_STRUCTURE_PRESERVATION',
        'PARTIAL_REUSE', 'HISTORICAL_UNVERIFIED', 'EXACT_COVERAGE',
        'Input + CurveData + Denotes/Satisfies + O + D',
        'P3', 'CLOSE_WITH_SCOPE',
    )
    require(
        BOOK,
        '\\section{The structure identity principle}',
        'A \\define{notion of structure}',
        'H_{\\alpha\\beta}(f)',
        'standard notion of structure',
        'H_{\\alpha\\beta}(f)$ and $H_{\\beta\\alpha}(\\inv f)',
        'If $X$ is a category and $(P,H)$ is a standard notion of structure',
    )
    require(P1, 'R_MIN_ACCEPTED_WITH_SCOPE', 'Input + CurveData + Denotes/Satisfies + O + D')
    require(SIP_SOURCE, 'C-124-identification', 'C-127-no-recovery', 'C-128-no-identification')
    require(SIP_REPORT, 'SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL')
    require(RELATIONAL, 'PRELIMINARY_PAPER_ARGUMENT / REVIEW_REQUIRED', 'H_{αβ}(f)', 'H_{βα}(f⁻¹)')
    require(GOAL_SOP, '## 2.1 学术与社区既有成果检查', '## 2.2 本地与已登记历史资产侦察')
    require(PLAN, 'P2 已完成的范围结果', 'P3-KAPP-DENOMINATOR-001')
    require(NEXT, 'NO_K_THEORY_WITHIN_SIP_DENOMINATOR', 'P5-SUCCESSOR-DISCOVERY-001', 'P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001', 'P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-001', 'P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-001', 'P9-SHOTT-DIRUNIV-CORPUS-DENOMINATOR-001', 'P10-SECOND-SUCCESSOR-DISCOVERY-001', 'P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-001', 'P12-THIRD-SUCCESSOR-DISCOVERY-001', 'P13-AMBIENT-PAIR-RMIN-REQUALIFICATION-001', 'P14-AMBIENT-OPERATION-K-SUCCESSOR-DISCOVERY-001')
    require(GOAL, 'NEXT_P14_AMBIENT_OPERATION_K_SUCCESSOR_DISCOVERY')
    require(FEATURES, 'NEXT_P14_AMBIENT_OPERATION_K_SUCCESSOR_DISCOVERY')
    require(ABX, 'P5–P7 已给出 R 与 K')

    run = json.loads(read(SIP_RUN))
    if run.get('status') != 'KERNEL_ACCEPTED_WITH_SCOPE':
        raise SystemExit('SIP_RUN_NOT_KERNEL_ACCEPTED_WITH_SCOPE')
    if run.get('proof_id') != 'MP-SIP-REPRESENTATION-001':
        raise SystemExit('SIP_RUN_IDENTITY_MISMATCH')
    if run.get('claim_ids') != ['C-124', 'C-125', 'C-126', 'C-127', 'C-128']:
        raise SystemExit('SIP_RUN_CLAIM_SCOPE_MISMATCH')

    receipt = {
        'schema_version': 'p2-ktheory-sip-verification/v1',
        'status': 'PASS_WITH_SCOPE',
        'scope': (
            'Checks the exact Book §9.8 anchors, P1 contract mapping, local-asset classification, '\
            'and prior SIP kernel-receipt identity. It does not replay the proof, prove the general SIP theorem, '\
            'formalize P1 as a standard structure, locate an actual consumer, or prove a HoTT defect.'
        ),
        'verdict': 'NO_K_THEORY_WITHIN_SIP_DENOMINATOR / P2_CLOSE_WITH_SCOPE / P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_GLUING_DEFENSE_P12_AMBIENT_PAIR_SELECTED_P13_R_AMBIENT_ACCEPTED_P14_NEXT',
        'files': {rel: sha(rel) for rel in [REPORT, BOOK, P1, SIP_SOURCE, SIP_RUN, SIP_REPORT, RELATIONAL, GOAL_SOP, PLAN, NEXT, GOAL, FEATURES, ABX]},
        'reused_kernel_receipt': {
            'proof_id': run['proof_id'], 'claim_ids': run['claim_ids'],
            'status': run['status'], 'git_status': run.get('git_status'),
            'sha256': sha(SIP_RUN),
        },
        'asset_classification': {
            'SIPRepresentation': 'PARTIAL_REUSE',
            'S050_and_implementation_report': 'PARTIAL_REUSE',
            'WebGPT_relational_SIP': 'HISTORICAL_UNVERIFIED',
            'L4_SIP_calibration': 'EXACT_COVERAGE_OF_OLD_BOOL_CASE_ONLY',
        },
    }
    if args.write:
        (ROOT / RECEIPT).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    main()
