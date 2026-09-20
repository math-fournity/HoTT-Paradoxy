#!/usr/bin/env python3
"""Verify the exact six-member experiment and preserved causal diagnostics."""
from pathlib import Path
import hashlib, json, re

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
DIAGNOSTICS = {
    'SC01': ('Agda.Builtin.Cubical.Glue.primGlue', 'UNGLUE_INPUT_FAMILY_CHANGED'),
    'SC02': ('correct\nboundary', 'DECODE_SQUARE_BOUNDARY_CHANGED'),
    'SC03': ('predℤ (sucℤ y) != y', 'REMOVED_PROPOSITIONAL_CORRECTION'),
    'SC04': ('when checking that the expression refl has type', 'J_PROOF_NOT_DEFINITIONAL_REFL'),
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    rows = []
    base = (ROOT / 'HoTT/formal/astra-s1-consumer-check/SC00.agda').read_text()
    for n in range(6):
        case = 'SC' + str(n).zfill(2)
        proof = 'MP-ASTRA-S1-CONSUMER-001' if n == 0 else 'MP-ASTRA-S1-' + case + '-CONTROL'
        run_rel = 'HoTT/verification/runs/20260920-' + proof + '-01'
        run_dir = ROOT / run_rel
        run = json.loads((run_dir / 'RUN.json').read_text())
        for key in ['stdout', 'stderr', 'environment', 'source_manifest']:
            data = (run_dir / run[key]['path']).read_bytes()
            assert len(data) == run[key]['bytes'] and sha(data) == run[key]['sha256']
        manifest = json.loads((run_dir / 'source-manifest.json').read_text())
        for row in manifest['files']:
            data = (ROOT / row['path']).read_bytes()
            assert len(data) == row['bytes'] and sha(data) == row['sha256']
        generation = json.loads((OUT / (case + '.json')).read_text())
        actual = (ROOT / generation['source']).read_text()
        common = base.replace('module SC00 where', 'module ' + case + ' where', 1)
        change = generation['mutation']
        if change:
            assert common.count(change[0]) == 1
            common = common.replace(change[0], change[1])
        assert common == actual
        stdout = (run_dir / 'stdout.txt').read_text()
        if n in (0, 5):
            assert run['exit_code'] == 0
            verdict = 'BASELINE_ACCEPTED' if n == 0 else 'EXACT_CORE_RESTORED_IN_INDEPENDENT_SOURCE_ACCEPTED'
            diagnostic = None
        else:
            anchor, verdict = DIAGNOSTICS[case]
            assert run['exit_code'] == 42 and 'error: [UnequalTerms]' in stdout and anchor in stdout
            diagnostic = stdout[stdout.index('/Volumes/D/HoTT_AI_HANDOFF_20260911/HoTT/formal/astra-s1-consumer-check/' + case + '.agda:'):]
        rows.append({'case': case, 'run': run_rel, 'source_sha256': sha(actual.encode()),
                     'exit': run['exit_code'], 'seconds': run['duration_seconds'],
                     'single_declared_change_only': True, 'verdict': verdict,
                     'diagnostic': diagnostic})
    graph = (ROOT / 'HoTT/verification/runs/20260920-MP-ASTRA-S1-CONSUMER-001-01/imports.dot').read_text()
    modules = sorted(re.findall(r'label="([^"]+)"', graph))
    receipt = {'status': 'SIX_DECLARED_CASES_EXACTLY_RECONCILED', 'declared': 6,
               'observed': len(rows), 'remainder': 0, 'accepted': 2, 'fixed_term_type_rejections': 4,
               'cases': rows, 'import_modules': len(modules),
               'source_metadata_gap': 'Initial formal-01 rejected inert .agda provenance snapshots as unqualified local code; original receipts preserved. New v2 primary run must pass formal/relationship checks separately.',
               'scope': 'Finite fixed-term causal experiment, not universal no-go, consistency or complete-library certification.'}
    (OUT / 'CONTROL-VERIFICATION.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'cases'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
