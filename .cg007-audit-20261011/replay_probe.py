#!/usr/bin/env python3
"""Read-only evidence audit. Compile verbatim source copies in this worktree only."""
import hashlib, json, re, shutil, subprocess
from pathlib import Path
ROOT = Path('/Volumes/D/HoTT_AI_HANDOFF_20260911')
HERE = Path(__file__).resolve().parent
SRC = HERE / 'src'
BUILD = HERE / 'build'
SRC.mkdir(parents=True, exist_ok=True)
BUILD.mkdir(parents=True, exist_ok=True)
PKG = ROOT / 'HoTT/formal/claude-cg001/godel-q-zfc-z0-full'
TC = json.loads((PKG / 'LEAN_TOOLCHAIN.json').read_text())
CL = json.loads((PKG / 'MATHLIB_CLOSURE.json').read_text())
PREFIX = Path(TC['prefix'])
for row in TC['pinned_files']:
    data = (PREFIX / row['relative_path']).read_bytes()
    assert len(data) == row['bytes'] and hashlib.sha256(data).hexdigest() == row['sha256'], row
for row in CL['modules']:
    digest = hashlib.sha256()
    base = Path(CL['library_roots'][row['root']]).joinpath(*row['module'].split('.'))
    for suffix in ('.olean', '.olean.private', '.olean.server'):
        path = Path(str(base) + suffix)
        if path.exists():
            digest.update(suffix.encode())
            digest.update(hashlib.sha256(path.read_bytes()).hexdigest().encode())
    assert digest.hexdigest() == row['digest'], row['module']
print('PIN_CHECK: toolchain and', len(CL['modules']), 'compiled dependency module digests match', flush=True)
run_names = [
'20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01',
'20261009-CG001-GODEL-Q-ZFC-Z0-BRIDGE-01',
'20261010-CG001-Z0-LAYER1-TRANSLATE-COMMUTATION-01',
'20261010-CG001-Z0-LAYER1-TRANSLATE-COMMUTATION-NEG-01',
'20261011-CG001-Z0-UNIBRIDGE-01',
'20261011-CG001-Z0-UNIBRIDGE-NEG-01',
'20261011-CG001-Z0-W8-LAYER2-ISEMIFORMULA-IT-01',
'20261011-CG001-Z0-W8-LAYER2-ISEMIFORMULA-IT-NEG-02',
'20261011-CG001-Z0-SHCRAIG-PREDICATE-01',
'20261011-CG001-Z0-SHCRAIG-BRANCHES-01',
'20261011-CG001-Z0-SHCRAIG-NEG-01',
'20261011-CG001-Z0-SHCRAIG-NEGFILLED-01',
'20261011-CG001-Z0-NEGINVOL-01']
sources = []
runs = {}
for name in run_names:
    directory = ROOT / 'HoTT/verification/runs' / name
    meta = json.loads((directory / 'RUN.json').read_text())
    ordered = meta['command_argv'][meta['command_argv'].index('--package') + 2:]
    runs[name] = (directory, meta, ordered)
    for rel in ordered:
        if rel not in sources:
            sources.append(rel)
extras = ['GodelQ/ZFC/ShCraigElimNegLaw.lean', 'GodelQ/ZFC/Z0D3Skeleton.lean', 'GodelQ/ZFC/Z0Blocked.lean']
for rel in sources + extras:
    dest = SRC / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    origin = PKG / rel if rel != 'GodelQ/ZFC/Z0D3Skeleton.lean' else ROOT / 'Z0-D3-攻关包-最小完整版/05-源码/Z0D3Skeleton.lean'
    shutil.copyfile(origin, dest)
    assert dest.read_bytes() == origin.read_bytes()
env = {'PATH': f'{PREFIX}/bin:/usr/bin:/bin', 'LEAN_SYSROOT': str(PREFIX),
       'LEAN_PATH': ':'.join([str(BUILD)] + CL['lean_path']), 'HOME': str(HERE)}
options = [f'-D{k}={v}' for k, v in CL['lean_options'].items()]
profile = '(version 1)(allow default)(deny network*)'
results = {}
for rel in sources + extras:
    out = BUILD / Path(rel).with_suffix('')
    out.parent.mkdir(parents=True, exist_ok=True)
    cached_stdout = HERE / (Path(rel).stem + '.stdout.txt')
    cached_stderr = HERE / (Path(rel).stem + '.stderr.txt')
    if Path(str(out) + '.olean').exists() and cached_stdout.exists() and cached_stderr.exists() and rel in sources:
        results[rel] = (0, cached_stdout.read_bytes().replace(str(SRC).encode() + b'/', b''), cached_stderr.read_bytes().replace(str(SRC).encode() + b'/', b''))
        print('REUSE_THIS_AUDIT_COMPILE', rel, 'EXIT 0', flush=True)
        continue
    cmd = ['/usr/bin/sandbox-exec', '-p', profile, str(PREFIX / 'bin/lean'), *options,
           '-R', str(SRC), '-o', str(out) + '.olean', '-i', str(out) + '.ilean', str(SRC / rel)]
    response = subprocess.run(cmd, cwd=HERE.parent, env=env, capture_output=True, timeout=90)
    # Absolute filename is removed for comparison with original driver's relative argument.
    stdout = response.stdout.replace(str(SRC).encode() + b'/', b'')
    stderr = response.stderr.replace(str(SRC).encode() + b'/', b'')
    results[rel] = (response.returncode, stdout, stderr)
    (HERE / (Path(rel).stem + '.stdout.txt')).write_bytes(response.stdout)
    (HERE / (Path(rel).stem + '.stderr.txt')).write_bytes(response.stderr)
    print('COMPILE', rel, 'EXIT', response.returncode, flush=True)
    if response.returncode:
        print(stdout.decode(errors='replace')[-18000:], stderr.decode(errors='replace'), flush=True)
        if b'sandbox-exec:' in response.stderr:
            raise SystemExit('sandbox unavailable; no bypass attempted')
for name, (directory, meta, ordered) in runs.items():
    observed_out = b''
    observed_err = b''
    observed_rc = 0
    for rel in ordered:
        rc, out, err = results[rel]
        observed_out += f'## lean {rel}\n'.encode() + out
        observed_err += err
        if rc:
            observed_rc = rc
            break
    print('REPLAY', name, 'EXIT_MATCH', observed_rc == meta['exit_code'],
          'STDOUT_MATCH', observed_out == (directory / 'stdout.txt').read_bytes(),
          'STDERR_MATCH', observed_err == (directory / 'stderr.txt').read_bytes(), flush=True)
for rel in extras:
    rc, out, err = results[rel]
    print('EXTRA_PROBE', rel, 'exit', rc, 'sorry_warning', b"uses 'sorry'" in out, flush=True)
print('SCRATCH', HERE)
