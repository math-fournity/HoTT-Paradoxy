#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
from typing import Any, Callable, Iterable

ROOT = Path('/mnt/data')
SOURCE_FILES = [
    'HoTT批判-结构等价但意义不等价(1).md',
    'HoTT批判-最终判决书本体论论证(1).md',
    'HoTT批判-三大阿喀琉斯之踵(1).md',
    'HoTT攻击-后继函数量子纠缠攻击(1).md',
    'HoTT攻击-哥德尔式几何攻击.md',
    'HoTT攻击-康托尔式对角线攻击.md',
    'HoTT悖论-表达性坍缩悖论(1).md',
    'HoTT悖论-自指类型循环悖论(1).md',
    'Z铁律论证HoTT缺乏时间维度-完整提取(2).md',
    'HoTT理论bug探讨文件索引.md',
    '数理征服者：用穿越时空的逻辑凝视粉碎HOTT理论幻觉.md',
]
COMPARISON_FILES = [
    'Z铁律论证HoTT缺乏时间维度-完整提取.md',
    '【✅】Finally HOTT is GONE and GONE with the Wind.md',
    '【✅】Finally HOTT is GONE and GONE with the Wind(2).md',
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def line_count(path: Path) -> int:
    data = path.read_bytes()
    if not data:
        return 0
    return data.count(b'\n') + (0 if data.endswith(b'\n') else 1)


def all_functions(domain: tuple[str, ...], codomain: tuple[str, ...]) -> Iterable[dict[str, str]]:
    for values in itertools.product(codomain, repeat=len(domain)):
        yield dict(zip(domain, values, strict=True))


def has_factorization(
    observations: list[dict[str, str]],
    abstract_key: str,
    target_key: str,
) -> bool:
    abstract_values = tuple(sorted({x[abstract_key] for x in observations}))
    target_values = tuple(sorted({x[target_key] for x in observations}))
    for decoder in all_functions(abstract_values, target_values):
        if all(decoder[x[abstract_key]] == x[target_key] for x in observations):
            return True
    return False


def model_checks() -> dict[str, Any]:
    semantic_roles = [
        {'bare_structure': 'Nat-chain', 'role': 'Arithmetic'},
        {'bare_structure': 'Nat-chain', 'role': 'ListIndex'},
    ]
    ambiguous_surface = [
        {'surface': 'bank', 'intended_spec': 'FinancialInstitution'},
        {'surface': 'bank', 'intended_spec': 'RiverEdge'},
    ]
    resource_traces = [
        {'extensional_function': 'identity', 'cost': '1'},
        {'extensional_function': 'identity', 'cost': '101'},
    ]

    def neg(x: int) -> int:
        return 1 - x

    fixed_points = [x for x in (0, 1) if neg(x) == x]
    trajectory = [0]
    for _ in range(9):
        trajectory.append(neg(trajectory[-1]))
    recurrence_holds = all(trajectory[n + 1] == neg(trajectory[n]) for n in range(len(trajectory) - 1))

    checks = {
        'semantic_role_factors_through_bare_structure': has_factorization(
            semantic_roles, 'bare_structure', 'role'
        ),
        'intended_spec_factors_through_surface_string': has_factorization(
            ambiguous_surface, 'surface', 'intended_spec'
        ),
        'operational_cost_factors_through_extensional_function': has_factorization(
            resource_traces, 'extensional_function', 'cost'
        ),
        'boolean_negation_fixed_points': fixed_points,
        'guarded_boolean_trajectory': trajectory,
        'guarded_recurrence_holds': recurrence_holds,
    }

    assert checks['semantic_role_factors_through_bare_structure'] is False
    assert checks['intended_spec_factors_through_surface_string'] is False
    assert checks['operational_cost_factors_through_extensional_function'] is False
    assert checks['boolean_negation_fixed_points'] == []
    assert checks['guarded_recurrence_holds'] is True
    return checks


def main() -> None:
    records: list[dict[str, Any]] = []
    for name in SOURCE_FILES + COMPARISON_FILES:
        path = ROOT / name
        if not path.exists():
            raise FileNotFoundError(path)
        records.append({
            'name': name,
            'bytes': path.stat().st_size,
            'lines': line_count(path),
            'sha256': sha256(path),
            'kind': 'new_source' if name in SOURCE_FILES else 'comparison',
        })

    groups: dict[str, list[str]] = {}
    for rec in records:
        groups.setdefault(rec['sha256'], []).append(rec['name'])
    duplicate_groups = [names for names in groups.values() if len(names) > 1]

    result = {
        'schema_version': 'hott_z_round3_source_inventory.v1',
        'source_count': len(SOURCE_FILES),
        'records': records,
        'exact_duplicate_groups': duplicate_groups,
        'finite_model_checks': model_checks(),
        'disclaimer': (
            'Finite enumeration checks only. They validate the displayed finite countermodels and source hashes; '
            'they are not proof-assistant verification of general HoTT theorems.'
        ),
    }

    json_path = ROOT / 'verification' / 'round3_source_inventory_and_model_check.json'
    txt_path = ROOT / 'verification' / 'round3_source_inventory_and_model_check.txt'
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    lines = [
        'HOTT–Z round 3 source inventory and finite model checks',
        '=' * 64,
        f"new source files: {result['source_count']}",
        '',
        'Exact duplicate groups:',
    ]
    for group in duplicate_groups:
        lines.append('  - ' + ' == '.join(group))
    lines.extend([
        '',
        'Finite countermodel checks:',
        f"  semantic role factors through bare structure: {result['finite_model_checks']['semantic_role_factors_through_bare_structure']}",
        f"  intended specification factors through surface string: {result['finite_model_checks']['intended_spec_factors_through_surface_string']}",
        f"  operational cost factors through extensional function: {result['finite_model_checks']['operational_cost_factors_through_extensional_function']}",
        f"  fixed points of Boolean negation: {result['finite_model_checks']['boolean_negation_fixed_points']}",
        f"  guarded trajectory: {result['finite_model_checks']['guarded_boolean_trajectory']}",
        f"  guarded recurrence holds: {result['finite_model_checks']['guarded_recurrence_holds']}",
        '',
        result['disclaimer'],
    ])
    txt_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json_path)
    print(txt_path)


if __name__ == '__main__':
    main()
