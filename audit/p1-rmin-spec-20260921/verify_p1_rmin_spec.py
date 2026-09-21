#!/usr/bin/env python3
"""Verify the bounded P1 R_min source-and-interface qualification.

This script checks local anchors and the stated scope.  It neither reruns Agda
nor turns the P1 specification audit into a new mathematical theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-REPORT.md'
RECEIPT = 'audit/p1-rmin-spec-20260921/P1-RMIN-SPEC-VERIFICATION.json'
SOURCES = {
    'rich_curve': 'HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda',
    'source_contract': 'HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda',
    'task_integration': 'HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda',
    'curve_task': 'HoTT/formal/agda-unimath/hott-z/NativeCurveTask.agda',
}
RUNS = {
    'source_contract': 'HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-SOURCE-CONTRACT-001-01/RUN.json',
    'task_integration': 'HoTT/verification/runs/20260921-MP-ASTRA-NATIVE-TASK-INTEGRATION-001-01/RUN.json',
}
PLAN = 'HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md'
NEXT = 'HoTT后续研究总体方案/005 - 当前第一步与交接.md'
GOAL_SOP = 'goal-3.md'


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.is_file():
        raise SystemExit(f'MISSING: {rel}')
    return path.read_text(encoding='utf-8')


def sha(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def require(rel: str, *markers: str) -> None:
    body = read(rel)
    for marker in markers:
        if marker not in body:
            raise SystemExit(f'MISSING_MARKER: {rel}: {marker!r}')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()

    require(
        REPORT,
        'R_MIN_ACCEPTED_WITH_SCOPE',
        'Input + CurveData + Denotes/Satisfies + O + D',
        'Done_w(i,r)',
        'Done_s(i,r)',
        'P2-KTHEORY-SIP-001',
        'KNOWN_ANALOGUE',
        'KNOWN_DEFENSE_OR_BOUNDARY',
        'NEARBY_NOT_SAME_TASK',
        'LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED',
        'CLOSE_WITH_SCOPE',
    )
    if 'HoTT/formal/astra-task-fidelity-20260921/' in read(REPORT):
        raise SystemExit('OBSOLETE_SOURCE_PATH_IN_REPORT')
    require(
        SOURCES['rich_curve'],
        'record CurveData', 'RichCurve :', 'mRich nRich', 'noRichPath',
    )
    require(
        SOURCES['source_contract'],
        'record Input', 'Denotes', 'Satisfies', 'Done', 'plainNNotSatisfied',
        'bareCheckIsInsufficient', 'satisfiesReexpression',
    )
    require(
        SOURCES['task_integration'],
        'record CurveRun', 'samePairDifferentOperations', 'noCurveAmbientEquivalence',
    )
    require(
        SOURCES['curve_task'],
        'record AmbientStep', 'Success', 'noSuccessNtoM', 'bareSuccess',
    )
    require(PLAN, 'P1：`R_min` 最小规格资格化', 'P2：`K_theory` 规则级桥')
    require(NEXT, 'R_MIN_ACCEPTED_WITH_SCOPE', 'NO_K_THEORY_WITHIN_SIP_DENOMINATOR', 'P5-SUCCESSOR-DISCOVERY-001', 'P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001', 'P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-001', 'P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-001', 'P9-SHOTT-DIRUNIV-CORPUS-DENOMINATOR-001')
    require(GOAL_SOP, '## 2.1 学术与社区既有成果检查', '## 3.1 波次坐标、最终价值与继续裁决')

    run_details = {}
    for name, rel in RUNS.items():
        data = json.loads(read(rel))
        if data.get('status') != 'KERNEL_ACCEPTED_WITH_SCOPE':
            raise SystemExit(f'RUN_STATUS_NOT_ACCEPTED_WITH_SCOPE: {rel}')
        if data.get('git_status') != 'LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED':
            raise SystemExit(f'RUN_VERSION_STATUS_CHANGED: {rel}')
        run_details[name] = {
            'path': rel,
            'sha256': sha(rel),
            'claim_ids': data.get('claim_ids'),
            'status': data.get('status'),
            'git_status': data.get('git_status'),
        }

    receipt = {
        'schema_version': 'p1-rmin-spec-verification/v1',
        'status': 'PASS_WITH_SCOPE',
        'scope': (
            'Checks the local source/interface anchors, pre-existing kernel receipt boundary, '\
            'academic-scan labels, and the later P2/P3/P5/P6/P7/P8/P9 active-goal routing update. It does not prove a new theorem, '\
            'an OriginTop theory, a theory-level K, an application K, or a HoTT defect.'
        ),
        'verdict': 'R_MIN_ACCEPTED_WITH_SCOPE / P1_CLOSE_WITH_SCOPE / P5_P6_P7_P8_COMPLETE_P9_NEXT',
        'files': {rel: sha(rel) for rel in [REPORT, *SOURCES.values(), PLAN, NEXT, GOAL_SOP]},
        'preexisting_kernel_receipts': run_details,
        'academic_scan': {
            'HoTT_Book_9_8': 'KNOWN_ANALOGUE_AND_P2_DENOMINATOR',
            'real_cohesive_HoTT': 'KNOWN_DEFENSE_OR_BOUNDARY',
            'stratified_or_relative_structures': 'NEARBY_NOT_SAME_TASK',
            'exact_R_min_identity': 'NO_RESULT_WITHIN_DECLARED_DENOMINATOR',
        },
    }
    if args.write:
        (ROOT / RECEIPT).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    main()
