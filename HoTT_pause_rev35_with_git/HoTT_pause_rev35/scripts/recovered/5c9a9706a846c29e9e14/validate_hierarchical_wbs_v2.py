from __future__ import annotations

from collections import Counter, defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import zipfile

BASE = Path('/mnt/data')
REGISTRY = BASE / 'HOTT_Z_HIERARCHICAL_WBS_v2.json'
SOURCE_REGISTRY = BASE / 'HOTT_Z_SOURCE_REGISTRY.json'
POINTER = BASE / 'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md'


def duplicates(values: list[str]) -> list[str]:
    return sorted(k for k, v in Counter(values).items() if v > 1)


def topo(nodes: set[str], deps: dict[str, list[str]]) -> tuple[bool, list[str], list[str]]:
    incoming = {n: 0 for n in nodes}
    outgoing: dict[str, list[str]] = defaultdict(list)
    missing: list[str] = []
    for n in nodes:
        for d in deps.get(n, []):
            if d not in nodes:
                missing.append(f'{n}->{d}')
                continue
            incoming[n] += 1
            outgoing[d].append(n)
    q = deque(sorted(n for n, deg in incoming.items() if deg == 0))
    order: list[str] = []
    while q:
        n = q.popleft()
        order.append(n)
        for m in sorted(outgoing[n]):
            incoming[m] -= 1
            if incoming[m] == 0:
                q.append(m)
    cycle = sorted(n for n, deg in incoming.items() if deg > 0)
    return not missing and not cycle and len(order) == len(nodes), order, sorted(set(missing + cycle))


def ids_in_file(path: Path, pattern: str) -> set[str]:
    return set(re.findall(pattern, path.read_text(encoding='utf-8')))


def result(ok: bool, **details):
    return {'ok': bool(ok), **details}


def main() -> None:
    d = json.loads(REGISTRY.read_text(encoding='utf-8'))
    sreg = json.loads(SOURCE_REGISTRY.read_text(encoding='utf-8'))

    areas = d['areas']
    wps = d['work_packages']
    tms = d['task_modules']
    gates = d['gates']

    area_ids = [x['id'] for x in areas]
    wp_ids = [x['id'] for x in wps]
    tm_ids = [x['id'] for x in tms]
    gate_ids = [x['id'] for x in gates]
    area_set, wp_set, tm_set = set(area_ids), set(wp_ids), set(tm_ids)

    wp_by = {x['id']: x for x in wps}
    tm_by = {x['id']: x for x in tms}

    source_ids = {x['id'] for x in sreg.get('sources', [])}
    claim_ids = ids_in_file(BASE/'CLAIM_LEDGER.md', r'\bZ-\d+\b')
    proof_ids = ids_in_file(BASE/'PROOF_ATTEMPTS.md', r'\bPA-\d+\b')
    result_ids = ids_in_file(BASE/'RESULTS.md', r'\bR-\d+\b')
    literature_ids = ids_in_file(BASE/'LITERATURE_MAP.md', r'\bLIT-\d+\b')

    wp_dep = {x['id']: x.get('dependencies', []) for x in wps}
    tm_dep = {x['id']: x.get('dependencies', []) for x in tms}
    wp_acyclic, wp_order, wp_cycle_or_missing = topo(wp_set, wp_dep)
    tm_acyclic, tm_order, tm_cycle_or_missing = topo(tm_set, tm_dep)

    wp_area_missing = sorted(f"{x['id']}->{x.get('area_id')}" for x in wps if x.get('area_id') not in area_set)
    area_wp_missing = sorted(
        f"{a['id']}->{wid}" for a in areas for wid in a.get('work_packages', []) if wid not in wp_set
    )
    area_wp_mismatch = sorted(
        f"{a['id']}->{wid}" for a in areas for wid in a.get('work_packages', [])
        if wid in wp_by and wp_by[wid].get('area_id') != a['id']
    )

    tm_parent_missing = sorted(f"{x['id']}->{x.get('parent_wp')}" for x in tms if x.get('parent_wp') not in wp_set)
    wp_tm_missing = sorted(f"{w['id']}->{tid}" for w in wps for tid in w.get('task_modules', []) if tid not in tm_set)
    wp_tm_mismatch = sorted(
        f"{w['id']}->{tid}" for w in wps for tid in w.get('task_modules', [])
        if tid in tm_by and tm_by[tid].get('parent_wp') != w['id']
    )
    tm_not_listed_by_parent = sorted(
        f"{t['id']}->{t['parent_wp']}" for t in tms
        if t['id'] not in wp_by[t['parent_wp']].get('task_modules', [])
    )
    every_wp_has_module = sorted(w['id'] for w in wps if not w.get('task_modules'))

    source_ref_missing = []
    claim_ref_missing = []
    proof_ref_missing = []
    result_ref_missing = []
    literature_ref_missing = []
    for kind, items in [('WP', wps), ('TM', tms)]:
        for x in items:
            for ref in x.get('source_refs', []):
                if ref not in source_ids: source_ref_missing.append(f"{kind}:{x['id']}->{ref}")
            for ref in x.get('claim_refs', []):
                if ref not in claim_ids: claim_ref_missing.append(f"{kind}:{x['id']}->{ref}")
            for ref in x.get('proof_refs', []):
                if ref not in proof_ids: proof_ref_missing.append(f"{kind}:{x['id']}->{ref}")
            for ref in x.get('result_refs', []):
                if ref not in result_ids: result_ref_missing.append(f"{kind}:{x['id']}->{ref}")
            for ref in x.get('literature_refs', []):
                if ref not in literature_ids: literature_ref_missing.append(f"{kind}:{x['id']}->{ref}")

    reverse_source_missing = []
    for src in sreg.get('sources', []):
        for wid in src.get('linked_work_packages', []):
            if wid not in wp_set: reverse_source_missing.append(f"{src['id']}->WP:{wid}")
        for tid in src.get('linked_task_modules', []):
            if tid not in tm_set: reverse_source_missing.append(f"{src['id']}->TM:{tid}")

    gate_ref_missing = []
    for g in gates:
        for wid in g.get('requires', []):
            if wid not in wp_set: gate_ref_missing.append(f"{g['id']}:requires->{wid}")
        for target in g.get('unlocks', []):
            if target.startswith('WP-') and target not in wp_set:
                gate_ref_missing.append(f"{g['id']}:unlocks->{target}")

    critical_missing = sorted(x for x in d.get('critical_path', []) if x not in wp_set)

    pointer_name = POINTER.name
    superseded_files = {x.get('file') for x in d.get('superseded_plans', [])}
    pointer_text = POINTER.read_text(encoding='utf-8')
    pointer_json = d.get('canonical_pointer', {})
    pointer_ok = (
        pointer_name not in superseded_files
        and pointer_json.get('file') == pointer_name
        and pointer_json.get('status') == 'ACTIVE_CANONICAL'
        and '当前唯一活动版本' in pointer_text
        and '分层 WBS v2' in pointer_text
    )

    text_files = [
        BASE/'HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md',
        BASE/'CURRENT_RESEARCH_INDEX.md',
        BASE/'HOTT_Z_WBS_CROSSWALK_v2.md',
    ]
    contradictory_pointer_lines = []
    for path in text_files:
        for i, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if pointer_name in line and ('SUPERSEDED_NONCANONICAL' in line or '仅作历史版本' in line):
                contradictory_pointer_lines.append(f'{path.name}:{i}:{line}')

    agents_text = (BASE/'AGENTS.md').read_text(encoding='utf-8')
    agents_section_count = len(re.findall(r'^## 26\b', agents_text, flags=re.M))
    agents_ok = agents_section_count == 1 and 'HOTT_Z_HIERARCHICAL_WBS_v2.json' in agents_text

    old_registry = BASE/'HOTT_Z_WBS_REGISTRY_v1.json'
    old_registry_ok = True
    old_registry_state = None
    if old_registry.exists():
        old = json.loads(old_registry.read_text(encoding='utf-8'))
        old_registry_state = {k: old.get(k) for k in ('canonical', 'status', 'superseded_by')}
        old_registry_ok = (
            old.get('canonical') is False
            and old.get('status') == 'SUPERSEDED_NONCANONICAL'
            and old.get('superseded_by') == REGISTRY.name
        )

    checks = {
        'unique_area_ids': result(not duplicates(area_ids), duplicates=duplicates(area_ids)),
        'unique_wp_ids': result(not duplicates(wp_ids), duplicates=duplicates(wp_ids)),
        'unique_tm_ids': result(not duplicates(tm_ids), duplicates=duplicates(tm_ids)),
        'unique_gate_ids': result(not duplicates(gate_ids), duplicates=duplicates(gate_ids)),
        'wp_area_refs': result(not (wp_area_missing or area_wp_missing or area_wp_mismatch), missing=wp_area_missing+area_wp_missing+area_wp_mismatch),
        'wp_dependency_refs_and_acyclicity': result(wp_acyclic, topological_order=wp_order, issues=wp_cycle_or_missing),
        'tm_parent_and_wp_crossrefs': result(not (tm_parent_missing or wp_tm_missing or wp_tm_mismatch or tm_not_listed_by_parent), missing=tm_parent_missing+wp_tm_missing+wp_tm_mismatch+tm_not_listed_by_parent),
        'tm_dependency_refs_and_acyclicity': result(tm_acyclic, topological_order=tm_order, issues=tm_cycle_or_missing),
        'every_wp_has_module': result(not every_wp_has_module, missing=every_wp_has_module),
        'source_refs': result(not source_ref_missing, missing=sorted(source_ref_missing)),
        'source_reverse_refs': result(not reverse_source_missing, missing=sorted(reverse_source_missing)),
        'claim_refs': result(not claim_ref_missing, missing=sorted(claim_ref_missing)),
        'proof_refs': result(not proof_ref_missing, missing=sorted(proof_ref_missing)),
        'result_refs': result(not result_ref_missing, missing=sorted(result_ref_missing)),
        'literature_refs': result(not literature_ref_missing, missing=sorted(literature_ref_missing)),
        'critical_path_refs': result(not critical_missing, missing=critical_missing),
        'gate_refs': result(not gate_ref_missing, missing=sorted(gate_ref_missing)),
        'canonical_pointer_invariant': result(pointer_ok, superseded=pointer_name in superseded_files, pointer_record=pointer_json),
        'human_text_pointer_consistency': result(not contradictory_pointer_lines, conflicts=contradictory_pointer_lines),
        'agents_single_canonical_section': result(agents_ok, section_26_count=agents_section_count),
        'old_v1_registry_is_noncanonical': result(old_registry_ok, state=old_registry_state),
    }

    counts = {
        'areas': len(areas),
        'work_packages': len(wps),
        'task_modules': len(tms),
        'gates': len(gates),
        'risks': len(d.get('risks', [])),
        'papers': len(d.get('publication_portfolio', [])),
        'sources': len(sreg.get('sources', [])),
    }
    expected_counts = {'areas':14,'work_packages':26,'task_modules':47,'gates':8,'risks':15,'papers':5}
    checks['expected_counts'] = result(all(counts[k] == v for k,v in expected_counts.items()), actual=counts, expected=expected_counts)

    overall = all(v['ok'] for v in checks.values())
    report = {
        'schema_version': 'hott_z_hierarchical_wbs_validation.v2.1',
        'checked_at_utc': datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'),
        'registry': REGISTRY.name,
        'checks': checks,
        'counts': counts,
        'overall_ok': overall,
    }

    out_json = BASE/'verification/hierarchical_wbs_v2_integrity.json'
    out_txt = BASE/'verification/hierarchical_wbs_v2_integrity.txt'
    final_json = BASE/'verification/hierarchical_wbs_v2_final_check.json'
    final_txt = BASE/'verification/hierarchical_wbs_v2_final_check.txt'
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    out_json.write_text(encoded, encoding='utf-8')
    final_json.write_text(encoded, encoding='utf-8')

    lines = [
        f"overall_ok: {str(overall).lower()}",
        *[f"{name}: {str(info['ok']).lower()}" for name, info in checks.items()],
        *[f"{k}: {v}" for k,v in counts.items()],
    ]
    if not overall:
        lines.append('FAILED_CHECK_DETAILS:')
        for name, info in checks.items():
            if not info['ok']:
                lines.append(f'- {name}: {json.dumps(info, ensure_ascii=False)}')
    text = '\n'.join(lines) + '\n'
    out_txt.write_text(text, encoding='utf-8')
    final_txt.write_text(text, encoding='utf-8')

    print(text, end='')
    if not overall:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
