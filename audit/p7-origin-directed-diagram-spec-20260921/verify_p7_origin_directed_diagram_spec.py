#!/usr/bin/env python3
"""Verify P7's minimal OriginDirectedDiagram and K-admission specification."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-VERIFICATION.json'
SOURCES = {
    'report': 'audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md',
    'p6': 'audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md',
    'origin': 'ABX行动/003 - 原圆环对象、判据与正反控制.md',
    'curve': 'HoTT/formal/astra-real-geometry/StructuredCurve.lean',
    'diagram': 'HoTT/formal/astra-breakpoint-check/GeometricBoundaryObservation.agda',
    'source_contract': 'HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda',
    'task_integration': 'HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda',
    'plan': 'HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md',
    'next': 'HoTT后续研究总体方案/005 - 当前第一步与交接.md',
}
REQUIRED = (
    'K_HARNESS_ACCEPTED_WITH_SCOPE',
    'P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-001',
    'OriginDirectedDiagram', 'R_ODD', 'U_bare', 'U_static', 'U_full',
    'K-input', 'K-output', 'K-claim', 'K-forgetting', 'K-version',
    'RESTATEMENT_ONLY', 'Done_s', 'NO_NEW_MATHEMATICAL_CLAIM',
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    missing = [rel for rel in SOURCES.values() if not (ROOT / rel).is_file()]
    report = (ROOT / SOURCES['report']).read_text(encoding='utf-8') if not missing else ''
    missing_tokens = [token for token in REQUIRED if token not in report]
    status = 'PASS_WITH_SCOPE' if not missing and not missing_tokens else 'FAIL'
    payload = {
        'schema_version': 'p7-origin-directed-diagram-spec-verification/v1',
        'task_id': 'P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-001',
        'status': status,
        'verdict': 'K_HARNESS_ACCEPTED_WITH_SCOPE / P8_DIRECTED_TYPE_THEORY_IMPLEMENTATION_DISCOVERY_NEXT / NO_NEW_MATHEMATICAL_CLAIM',
        'scope': ('Checks that the P7 report fixes the static, process, observation, forgetting and K-admission fields and maps them to existing local interfaces. '
                  'It does not prove a formal OriginDirectedDiagram construction, actual K, non-representability theorem, or HoTT defect.'),
        'checked_sources': {name: {'path': rel, 'sha256': sha(ROOT / rel)} for name, rel in SOURCES.items() if (ROOT / rel).is_file()},
        'missing_sources': missing,
        'missing_required_report_tokens': missing_tokens,
        'academic_search_decision': 'NOT_RERUN_WITH_REASON: P7 makes no new external factual comparison beyond the P6 sources; repeating the same search would not change its K-admission contract.',
        'not_claimed': ['a new theorem', 'a complete proof-assistant formalization', 'an actual K consumer', 'a HoTT defect'],
    }
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + '\n'
    if args.write:
        OUT.write_text(rendered, encoding='utf-8')
    print(rendered, end='')
    return 0 if status == 'PASS_WITH_SCOPE' else 1


if __name__ == '__main__':
    raise SystemExit(main())
