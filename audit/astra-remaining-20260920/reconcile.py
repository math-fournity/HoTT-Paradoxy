#!/usr/bin/env python3
"""Read-only provenance and qualification of the original breakpoint proof packages."""
from pathlib import Path
import hashlib, json, subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SNAPSHOT = 'd059dbf7b543092bce99333843f2bda16a06b327'


def git(*args, check=True):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, check=check)


def main():
    registry = json.loads((ROOT / 'HoTT/verification/PROOF_VERSION_CLOSURE.json').read_text())
    selected = [p for p in registry['later_packages']
                if p['source'].startswith('HoTT/formal/astra-breakpoint-check/')
                and p.get('release_ref') == 'LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED']
    assert len(selected) == 14
    paths = set()
    checks = []
    for p in selected:
        run = ROOT / p['run']
        manifest = json.loads((run / 'source-manifest.json').read_text())
        paths.update(r['path'] for r in manifest['files'])
        paths.update(q.relative_to(ROOT).as_posix() for q in run.rglob('*')
                     if q.is_file() and '__pycache__' not in q.parts and q.suffix != '.agdai')
        argv = ['python3', '-B', 'scripts/audit/verify_formal_proof_run.py', '--run-dir', p['run']]
        result = subprocess.run(argv, cwd=ROOT, capture_output=True)
        (OUT / (p['proof_id'] + '.formal.stdout.json')).write_bytes(result.stdout)
        (OUT / (p['proof_id'] + '.formal.stderr.txt')).write_bytes(result.stderr)
        checks.append({'proof_id': p['proof_id'], 'claims': p['claim_ids'], 'run': p['run'],
                       'argv': argv, 'exit': result.returncode})
        assert result.returncode == 0, (p['proof_id'], result.stdout.decode(), result.stderr.decode())
    rows = []
    for path in sorted(paths):
        data = (ROOT / path).read_bytes()
        old = git('show', SNAPSHOT + ':' + path, check=False)
        head = git('show', 'HEAD:' + path, check=False)
        rows.append({'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                     'snapshot_present': old.returncode == 0,
                     'same_as_snapshot': old.returncode == 0 and old.stdout == data,
                     'head_present': head.returncode == 0,
                     'same_as_head': head.returncode == 0 and head.stdout == data})
    argv = ['python3', '-B', 'scripts/audit/verify_proof_version_closure.py', '--evidence-only']
    for p in selected:
        argv += ['--proof-id', p['proof_id']]
    result = subprocess.run(argv, cwd=ROOT, capture_output=True)
    (OUT / 'selected-evidence.stdout.json').write_bytes(result.stdout)
    (OUT / 'selected-evidence.stderr.txt').write_bytes(result.stderr)
    assert result.returncode == 0, result.stdout.decode()
    receipt = {'status': 'READ_ONLY_QUALIFIED_PROVENANCE_REVIEW_REQUIRED',
               'expected_target': git('rev-parse', 'HEAD').stdout.decode().strip(),
               'snapshot': SNAPSHOT, 'selected': selected, 'checks': checks,
               'files': rows, 'evidence_exit': result.returncode,
               'kernel_replayed': False, 'mathematics': 'NO_NEW_THEOREM_FROM_VERSION_RECONCILIATION'}
    (OUT / 'RECONCILIATION.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'packages': len(selected), 'files': len(rows),
                      'not_same_as_snapshot': [r for r in rows if not r['same_as_snapshot']],
                      'not_same_as_head': [r['path'] for r in rows if not r['same_as_head']]}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
