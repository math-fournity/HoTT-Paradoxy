#!/usr/bin/env python3
"""Verify P6's field-comparison evidence and local source/run identity.

The verifier checks source identity and report coverage. It does not prove that
any mathematical framework is universally unable or able to encode every
possible origin/operation relation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-VERIFICATION.json'
REPORT = 'audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md'
SOURCES = {
    'p5': 'audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md',
    'origin_interface': 'ABX行动/003 - 原圆环对象、判据与正反控制.md',
    'plan': 'HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md',
    'next': 'HoTT后续研究总体方案/005 - 当前第一步与交接.md',
    'lean': 'HoTT/formal/astra-real-geometry/StructuredCurve.lean',
    'agda_observation': 'HoTT/formal/astra-breakpoint-check/GeometricBoundaryObservation.agda',
    'agda_incidence': 'HoTT/formal/astra-breakpoint-check/BoundaryIncidence.agda',
    'source_contract': 'HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda',
    'task_integration': 'HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda',
    'case_matrix': 'audit/astra-case-integration-20260921/MATRIX-BEFORE.md',
    'lean_run': 'HoTT/verification/runs/20260920-MP-ASTRA-STRUCTURED-CURVE-001-02/RUN.json',
    'lean_manifest': 'HoTT/verification/runs/20260920-MP-ASTRA-STRUCTURED-CURVE-001-02/source-manifest.json',
    'agda_run': 'HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001-01/RUN.json',
    'agda_manifest': 'HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001-01/source-manifest.json',
}
REQUIRED = (
    'PARTIAL_REUSE',
    'COMPOSITE_STRUCTURED_DIRECTED_DIAGRAM_CANDIDATE',
    'P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-001',
    'NO_NEW_HOTT_DEFECT_CLAIM',
    'OriginPresentation',
    'CurvePresentation',
    'RichDiagram',
    'operation-spec',
    'Done_s',
    'https://arxiv.org/abs/1908.01366',
    'https://arxiv.org/abs/1911.04630',
    'https://arxiv.org/abs/math/0111048',
    'https://arxiv.org/abs/1807.10566',
    'https://arxiv.org/abs/1509.07584',
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest_hash(rel_manifest: str, rel_source: str) -> str | None:
    data = json.loads((ROOT / rel_manifest).read_text(encoding='utf-8'))
    for row in data.get('files', []):
        if row.get('path') == rel_source:
            return row.get('sha256')
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    missing = [rel for rel in SOURCES.values() if not (ROOT / rel).is_file()]
    report = (ROOT / REPORT).read_text(encoding='utf-8') if not missing else ''
    missing_tokens = [token for token in REQUIRED if token not in report]
    lean_run = json.loads((ROOT / SOURCES['lean_run']).read_text(encoding='utf-8')) if not missing else {}
    agda_run = json.loads((ROOT / SOURCES['agda_run']).read_text(encoding='utf-8')) if not missing else {}
    comparisons = {
        SOURCES['lean']: manifest_hash(SOURCES['lean_manifest'], SOURCES['lean']),
        SOURCES['agda_observation']: manifest_hash(SOURCES['agda_manifest'], SOURCES['agda_observation']),
        SOURCES['agda_incidence']: manifest_hash(SOURCES['agda_manifest'], SOURCES['agda_incidence']),
    }
    current = {rel: sha(ROOT / rel) for rel in comparisons if (ROOT / rel).is_file()}
    mismatches = {rel: {'manifest': comparisons[rel], 'current': current.get(rel)} for rel in comparisons if comparisons[rel] != current.get(rel)}
    valid_runs = (
        lean_run.get('status') == 'KERNEL_ACCEPTED_WITH_SCOPE' and
        agda_run.get('status') == 'KERNEL_ACCEPTED_WITH_SCOPE'
    )
    status = 'PASS_WITH_SCOPE' if not missing and not missing_tokens and not mismatches and valid_runs else 'FAIL'
    payload = {
        'schema_version': 'p6-origin-structure-stratified-verification/v1',
        'task_id': 'P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001',
        'status': status,
        'verdict': 'PARTIAL_REUSE / COMPOSITE_STRUCTURED_DIRECTED_DIAGRAM_CANDIDATE / P7_NEXT / NO_NEW_HOTT_DEFECT_CLAIM',
        'scope': ('Checks the P6 field-matrix/report anchors and that three reused local formal sources match their saved run manifests. '
                  'It does not prove a universal representation theorem, a non-representability theorem, an actual K, or a HoTT defect.'),
        'checked_sources': {name: {'path': rel, 'sha256': sha(ROOT / rel)} for name, rel in SOURCES.items() if (ROOT / rel).is_file()},
        'reused_run_statuses': {
            'MP-ASTRA-STRUCTURED-CURVE-001': lean_run.get('status'),
            'MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001': agda_run.get('status'),
            'git_closure_boundary': [lean_run.get('git_status'), agda_run.get('git_status')],
        },
        'source_manifest_comparison': {rel: {'manifest_sha256': comparisons[rel], 'current_sha256': current.get(rel)} for rel in comparisons},
        'missing_sources': missing,
        'missing_required_report_tokens': missing_tokens,
        'source_mismatches': mismatches,
        'public_sources_checked': [
            'https://arxiv.org/abs/1908.01366',
            'https://arxiv.org/abs/1811.01119',
            'https://arxiv.org/abs/1911.04630',
            'https://arxiv.org/abs/2101.09363',
            'https://arxiv.org/abs/math/0111048',
            'https://arxiv.org/abs/1807.10566',
            'https://arxiv.org/abs/2407.09146',
            'https://arxiv.org/abs/1509.07584',
        ],
    }
    rendered = json.dumps(payload, ensure_ascii=False, indent=2) + '\n'
    if args.write:
        OUT.write_text(rendered, encoding='utf-8')
    print(rendered, end='')
    return 0 if status == 'PASS_WITH_SCOPE' else 1


if __name__ == '__main__':
    raise SystemExit(main())
