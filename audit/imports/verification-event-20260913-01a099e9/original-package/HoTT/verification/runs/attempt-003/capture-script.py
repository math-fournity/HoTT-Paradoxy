#!/usr/bin/env python3
"""Capture one non-overwriting native Agda run in this isolated package."""
import argparse
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BINARY = Path('/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda')
EXPECTED_BINARY = 'ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('run_id')
    ap.add_argument('--negative', action='store_true')
    ap.add_argument('--module', default=None)
    args = ap.parse_args()
    if not args.run_id.replace('-', '').replace('_', '').isalnum():
        raise SystemExit('unsafe run ID')
    assert digest(BINARY) == EXPECTED_BINARY, 'Agda binary hash mismatch'
    run = ROOT / 'HoTT/verification/runs' / args.run_id
    run.mkdir(exist_ok=False)
    (run / 'source').mkdir()
    shutil.copy2(Path(__file__), run / 'capture-script.py')
    builtin_interfaces = [
        {'path': p.relative_to(ROOT).as_posix(), 'sha256': digest(p)}
        for p in sorted((ROOT / 'vendor/agda-data').rglob('*.agdai'))
    ]
    dump(run / 'builtin-interface-inputs.json', builtin_interfaces)
    sources = []
    for p in sorted((ROOT / 'HoTT/formal').glob('*.agda')):
        shutil.copy2(p, run / 'source' / p.name)
        sources.append({'path': p.relative_to(ROOT).as_posix(), 'sha256': digest(p), 'bytes': p.stat().st_size})
    dependencies = []
    for p in sorted((ROOT / 'vendor/agda-data').rglob('*')):
        if p.is_file() and p.suffix != '.agdai' and p.name != '.DS_Store':
            dependencies.append({'path': p.relative_to(ROOT).as_posix(), 'sha256': digest(p), 'bytes': p.stat().st_size})
    dump(run / 'source-manifest.json', {'sources': sources, 'dependencies': dependencies, 'binary': {'path': str(BINARY), 'sha256': digest(BINARY)}})
    env = os.environ.copy()
    selected = {'XDG_DATA_HOME': str(ROOT / 'vendor/agda-data'),
                'XDG_CONFIG_HOME': str(ROOT / 'build/config'),
                'TMPDIR': str(ROOT / 'build/tmp')}
    env.update(selected)
    version = subprocess.run([str(BINARY), '--version'], capture_output=True, text=True, env=env, check=True).stdout
    cwd = ROOT / 'HoTT/formal'
    target = args.module or ('BadCast.agda' if args.negative else 'VerificationEvent.agda')
    assert target in [p.name for p in cwd.glob('*.agda')], 'module must be a local source'
    command = [str(BINARY), '--no-libraries', '--safe', '--cubical', '--ignore-interfaces', '-i', str(cwd), target]
    start = datetime.now(timezone.utc).isoformat()
    try:
        result = subprocess.run(command, cwd=cwd, env=env, capture_output=True, timeout=60)
        code, stdout, stderr = result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired as error:
        code, stdout, stderr = 124, error.stdout or b'', error.stderr or b''
        stderr += b'\nCAPTURE_TIMEOUT_60_SECONDS\n'
    (run / 'stdout.txt').write_bytes(stdout)
    (run / 'stderr.txt').write_bytes(stderr)
    (run / 'environment.txt').write_text(platform.platform() + '\nPython ' + sys.version + '\n' + version + json.dumps(selected, indent=2) + '\n')
    stable = all(digest(ROOT / entry['path']) == entry['sha256'] for entry in sources + dependencies)
    receipt = {'schema_version': 'isolated-agda-run/v1', 'run_id': args.run_id,
               'started_at': start, 'finished_at': datetime.now(timezone.utc).isoformat(),
               'command': command, 'cwd': str(cwd), 'agda_version': version.strip(),
               'exit_code': code, 'negative_control': args.negative,
               'source_and_dependency_hashes_stable': stable,
               'capture_script_sha256': digest(run / 'capture-script.py'),
               'builtin_interface_inputs_sha256': digest(run / 'builtin-interface-inputs.json'),
               'stdout_sha256': digest(run / 'stdout.txt'), 'stderr_sha256': digest(run / 'stderr.txt'),
               'scope': 'Finite three-stage registration model, native Cubical Path and propositional truncation; no universal HoTT self-verifier or physical-time claim',
               'shared_repository_writes': False}
    index = ROOT / 'HoTT/CLAIM_EVIDENCE_MATRIX.md'
    if index.exists():
        shutil.copy2(index, run / 'claim-index.md')
        receipt['claim_index_sha256'] = digest(index)
    dump(run / 'RUN.json', receipt)
    print(json.dumps({'run': str(run), 'exit_code': code, 'hashes_stable': stable}, ensure_ascii=False))
    if stdout:
        print(stdout.decode(errors='replace')[-5000:])
    if stderr:
        print(stderr.decode(errors='replace')[-2000:], file=sys.stderr)
    if not stable:
        return 2
    return 0 if ((code != 0 and code != 124) if args.negative else code == 0) else 1

if __name__ == '__main__':
    raise SystemExit(main())
