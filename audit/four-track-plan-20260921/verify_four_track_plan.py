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
P2_VERIFY = 'audit/p2-ktheory-sip-20260921/verify_p2_ktheory_sip.py'
P2_REPORT = 'audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-REPORT.md'
P2_RECEIPT = 'audit/p2-ktheory-sip-20260921/P2-KTHEORY-SIP-VERIFICATION.json'
P3_VERIFY = 'audit/p3-unimath-functor-algebras-20260921/verify_p3_unimath_functor_algebras.py'
P3_REPORT = 'audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-REPORT.md'
P3_FREEZE = 'audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-SOURCE-FREEZE.json'
P3_RECEIPT = 'audit/p3-unimath-functor-algebras-20260921/P3-UNIMATH-FUNCTOR-ALGEBRAS-VERIFICATION.json'
P5_VERIFY = 'audit/p5-successor-discovery-20260921/verify_p5_successor_discovery.py'
P5_REPORT = 'audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-REPORT.md'
P5_RECEIPT = 'audit/p5-successor-discovery-20260921/P5-SUCCESSOR-DISCOVERY-VERIFICATION.json'
P6_VERIFY = 'audit/p6-origin-structure-stratified-20260921/verify_p6_origin_structure_stratified.py'
P6_REPORT = 'audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-REPORT.md'
P6_RECEIPT = 'audit/p6-origin-structure-stratified-20260921/P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-VERIFICATION.json'
P7_VERIFY = 'audit/p7-origin-directed-diagram-spec-20260921/verify_p7_origin_directed_diagram_spec.py'
P7_REPORT = 'audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md'
P7_RECEIPT = 'audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-VERIFICATION.json'
P8_VERIFY = 'audit/p8-directed-type-theory-implementation-discovery-20260921/verify_p8_directed_type_theory_implementation.py'
P8_REPORT = 'audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-REPORT.md'
P8_FREEZE = 'audit/p8-directed-type-theory-implementation-discovery-20260921/P8-RZK-SOURCE-FREEZE.json'
P8_RECEIPT = 'audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-VERIFICATION.json'
P9_VERIFY = 'audit/p9-shott-diruniv-corpus-20260921/verify_p9_shott_diruniv_corpus.py'
P9_REPORT = 'audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-REPORT.md'
P9_FREEZE = 'audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-SOURCE-FREEZE.json'
P9_RECEIPT = 'audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-VERIFICATION.json'
P10_VERIFY = 'audit/p10-second-successor-discovery-20260921/verify_p10_second_successor_discovery.py'
P10_REPORT = 'audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-REPORT.md'
P10_FREEZE = 'audit/p10-second-successor-discovery-20260921/P10-COQHOTT-CANDIDATE-FREEZE.json'
P10_RECEIPT = 'audit/p10-second-successor-discovery-20260921/P10-SECOND-SUCCESSOR-DISCOVERY-VERIFICATION.json'
P11_VERIFY = 'audit/p11-coqhott-circle-coequalizer-corpus-20260921/verify_p11_coqhott_circle_coequalizer.py'
P11_REPORT = 'audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-REPORT.md'
P11_AUDIT = 'audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-SOURCE-AUDIT.json'
P11_RECEIPT = 'audit/p11-coqhott-circle-coequalizer-corpus-20260921/P11-COQHOTT-CIRCLE-COEQUALIZER-VERIFICATION.json'
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
    subprocess.check_call([sys.executable, '-B', P2_VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', P3_VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', P5_VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', P6_VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', P7_VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', P8_VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', P9_VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', P10_VERIFY, '--write'], cwd=ROOT)
    subprocess.check_call([sys.executable, '-B', P11_VERIFY, '--write'], cwd=ROOT)
    for rel in [INDEX, *SHARDS, DIALOGUE, P1_VERIFY, P1_REPORT, P1_RECEIPT, P2_VERIFY, P2_REPORT, P2_RECEIPT, P3_VERIFY, P3_REPORT, P3_FREEZE, P3_RECEIPT, P5_VERIFY, P5_REPORT, P5_RECEIPT, P6_VERIFY, P6_REPORT, P6_RECEIPT, P7_VERIFY, P7_REPORT, P7_RECEIPT, P8_VERIFY, P8_REPORT, P8_FREEZE, P8_RECEIPT, P9_VERIFY, P9_REPORT, P9_FREEZE, P9_RECEIPT, P10_VERIFY, P10_REPORT, P10_FREEZE, P10_RECEIPT, P11_VERIFY, P11_REPORT, P11_AUDIT, P11_RECEIPT, 'goal.md', 'feature-list.md', 'rulings.md', 'ABX行动.md', 'ABX行动/005 - 状态、停止条件与未来交接.md']:
        need(rel)
    marker(INDEX, 'logical_id: HOTT-FOUR-TRACK-PLAN')
    marker(INDEX, 'last_shard: HoTT后续研究总体方案/005 - 当前第一步与交接.md')
    marker(SHARDS[0], '### 用户提问')
    marker(SHARDS[0], '### AI 最终回复')
    marker(SHARDS[1], 'P1：结构规格')
    marker(SHARDS[1], 'P4：实现忠实性')
    marker(INDEX, 'P11_COQHOTT_GLUING_DEFENSE')
    marker(INDEX, 'P12_THIRD_SUCCESSOR_DISCOVERY_NEXT')
    marker(SHARDS[2], 'P1：`R_min` 最小规格资格化')
    marker(SHARDS[2], 'P1 已完成的范围结果')
    marker(SHARDS[2], 'P2-KTHEORY-SIP-001')
    marker(SHARDS[2], 'P2 已完成的范围结果')
    marker(SHARDS[2], 'P3-KAPP-DENOMINATOR-001')
    marker(SHARDS[2], 'P3 已完成的范围结果')
    marker(SHARDS[2], 'P4 状态')
    marker(SHARDS[2], 'P5：`SUCCESSOR_DISCOVERY`')
    marker(SHARDS[2], 'P5 已完成的范围结果')
    marker(SHARDS[2], 'P6：`ORIGIN_STRUCTURE_STRATIFIED_COMPARISON`')
    marker(SHARDS[2], 'P6 已完成的范围结果')
    marker(SHARDS[2], 'P7：`ORIGIN_DIRECTED_DIAGRAM_SPEC`')
    marker(SHARDS[2], 'P7 已完成的范围结果')
    marker(SHARDS[2], 'P8：`DIRECTED_TYPE_THEORY_IMPLEMENTATION_DISCOVERY`')
    marker(SHARDS[2], 'P8 已完成的范围结果')
    marker(SHARDS[2], 'P9：`SHOTT_DIRUNIV_CORPUS_DENOMINATOR`')
    marker(SHARDS[2], 'P9 已完成的范围结果')
    marker(SHARDS[2], 'P10：`SECOND_SUCCESSOR_DISCOVERY`')
    marker(SHARDS[2], 'P10 已完成的范围结果')
    marker(SHARDS[2], 'P11：`COQHOTT_CIRCLE_COEQUALIZER_CORPUS`')
    marker(SHARDS[2], 'P11 已完成的范围结果')
    marker(SHARDS[2], 'P12：`THIRD_SUCCESSOR_DISCOVERY`')
    marker(SHARDS[3], '每个工作单元的最小声明')
    marker(SHARDS[4], 'P5-SUCCESSOR-DISCOVERY-001')
    marker(SHARDS[4], 'P6-ORIGIN-STRUCTURE-STRATIFIED-COMPARISON-001')
    marker(SHARDS[4], 'P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-001')
    marker(SHARDS[4], 'P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-001')
    marker(SHARDS[4], 'P9-SHOTT-DIRUNIV-CORPUS-DENOMINATOR-001')
    marker(SHARDS[4], 'P10-SECOND-SUCCESSOR-DISCOVERY-001')
    marker(SHARDS[4], 'P11-COQHOTT-CIRCLE-COEQUALIZER-CORPUS-001')
    marker(SHARDS[4], 'P12-THIRD-SUCCESSOR-DISCOVERY-001')
    marker('goal.md', 'NEXT_P12_THIRD_SUCCESSOR_DISCOVERY')
    marker('feature-list.md', 'NEXT_P12_THIRD_SUCCESSOR_DISCOVERY')
    marker('rulings.md', '四分支')
    marker('ABX行动.md', 'P5–P7 已给出 R 与 K')
    marker('ABX行动/005 - 状态、停止条件与未来交接.md', 'HoTT后续研究总体方案.md')

    receipt = {
        'schema_version': 'four-track-plan-verification/v1',
        'status': 'PASS_WITH_SCOPE',
        'scope': ('Verifies the plan structure, verbatim prior-answer projection, P1/P2/P3 receipts, '
                  'and the active-goal P5/P6/P7/P8/P9 completion, P10 selection, P11 source-audit, and P12 discovery-routing anchors. It does not prove a new R_min theorem, a K_theory/K_app/K_engine, '
                  'a new topology, or a HoTT defect.'),
        'files': {rel: sha(need(rel)) for rel in [INDEX, *SHARDS, DIALOGUE, P1_VERIFY, P1_REPORT, P1_RECEIPT, P2_VERIFY, P2_REPORT, P2_RECEIPT, P3_VERIFY, P3_REPORT, P3_FREEZE, P3_RECEIPT, P5_VERIFY, P5_REPORT, P5_RECEIPT, P6_VERIFY, P6_REPORT, P6_RECEIPT, P7_VERIFY, P7_REPORT, P7_RECEIPT, P8_VERIFY, P8_REPORT, P8_FREEZE, P8_RECEIPT, P9_VERIFY, P9_REPORT, P9_FREEZE, P9_RECEIPT, P10_VERIFY, P10_REPORT, P10_FREEZE, P10_RECEIPT, P11_VERIFY, P11_REPORT, P11_AUDIT, P11_RECEIPT]},
        'verdict': 'FOUR_TRACK_FIRST_PASS_CLOSED_P5_P6_P7_P8_P9_COMPLETE_P10_SELECTED_P11_GLUING_DEFENSE_P12_THIRD_SUCCESSOR_NEXT',
    }
    if args.write:
        (ROOT / RECEIPT).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    main()
