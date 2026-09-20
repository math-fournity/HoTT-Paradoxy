#!/usr/bin/env python3
"""Capture v2: compiled dependencies and inert provenance snapshots have distinct roles."""
from pathlib import Path
import argparse, datetime, importlib.util, json, platform, subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
sp = importlib.util.spec_from_file_location('capture', ROOT / 'scripts/audit/capture_agda_proof_run.py')
C = importlib.util.module_from_spec(sp)
sp.loader.exec_module(C)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--case', choices=['SC00', 'SC01', 'SC02', 'SC03', 'SC04', 'SC05'], required=True)
    ap.add_argument('--attempt', default='01')
    args = ap.parse_args()
    primary = args.case == 'SC00'
    proof = 'MP-ASTRA-S1-CONSUMER-001' if primary else 'MP-ASTRA-S1-' + args.case + '-CONTROL'
    run_id = '20260920-' + proof + '-' + args.attempt
    dest = ROOT / 'HoTT/verification/runs' / run_id
    assert not dest.exists()
    source = 'HoTT/formal/astra-s1-consumer-check/' + args.case + '.agda'
    config = 'HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json'
    cfg = json.loads((ROOT / config).read_text())
    a, lib, cache = cfg['agda'], cfg['cubical_library'], cfg['runtime_cache']
    originals = json.loads((ROOT / 'audit/astra-remaining-20260920/SOURCE-INPUTS.json').read_text())
    inputs = [source, config, cfg['project_library_registry'],
              'audit/astra-s1-consumer-20260920/generate_cases.py',
              'audit/astra-s1-consumer-20260920/capture_v2.py',
              'scripts/audit/capture_agda_proof_run.py',
              'audit/astra-remaining-20260920/SOURCE-INPUTS.json']
    # These are inert audit copies, not modules on the compiler import path.
    provenance = [dict(C.file_row(ROOT / r['local_path']), path=r['local_path'])
                  for r in originals['copied_originals']]
    files = [dict(C.file_row(ROOT / p), path=p) for p in inputs]
    pins = [(a['local_binary'], a['binary_bytes'], a['binary_sha256'], 'agda-binary'),
            (a['local_archive'], a['asset_bytes'], a['asset_sha256'], 'agda-release-asset'),
            (lib['local_archive'], lib['asset_bytes'], lib['asset_sha256'], 'cubical-release-asset'),
            (lib['library_file'], lib['library_file_bytes'], lib['library_file_sha256'], 'cubical-library-file')]
    external = []
    for path, bs, hs, label in pins:
        C.expect_file(Path(path), bs, hs, label)
        external.append(C.file_row(Path(path), label=label))
    tree = C.deterministic_tree(Path(lib['local_root']))
    assert tree == {'file_count': lib['tree_file_count'], 'total_bytes': lib['tree_total_bytes'], 'tree_sha256': lib['tree_sha256']}
    external.append(dict(label='cubical-extracted-tree', local_path=lib['local_root'], **tree))
    prim = Path(cache['xdg_data_home']) / 'agda' / a['version'] / 'lib/prim'
    for p in sorted(prim.rglob('*.agda')):
        external.append(C.file_row(p, label='agda-runtime-source:' + p.relative_to(prim).as_posix()))
    graph = OUT / (args.case + '-' + args.attempt + '-imports.dot')
    argv = ['/usr/bin/env', 'XDG_DATA_HOME=' + cache['xdg_data_home'],
            'XDG_CONFIG_HOME=' + cache['xdg_config_home'], 'TMPDIR=' + cache['tmpdir'], a['local_binary'],
            '--ignore-interfaces', '--library-file=' + str(ROOT / cfg['project_library_registry']),
            '-l', 'cubical-0.9', '-i', str(ROOT / 'HoTT/formal/astra-s1-consumer-check'),
            '--dependency-graph=' + str(graph), source]
    version = subprocess.run(argv[:5] + ['--version'], cwd=ROOT, capture_output=True, check=True).stdout.decode().strip()
    started = datetime.datetime.now(datetime.timezone.utc)
    print('RUN ' + run_id, flush=True)
    # This finite observation bound is not a mathematical termination claim.
    timeout = False
    try:
        result = subprocess.run(argv, cwd=ROOT, capture_output=True, timeout=600)
        code, stdout, stderr = result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired as exc:
        timeout = True
        code, stdout, stderr = 124, exc.stdout or b'', exc.stderr or b''
    ended = datetime.datetime.now(datetime.timezone.utc)
    assert all(C.sha((ROOT / f['path']).read_bytes()) == f['sha256'] for f in files)
    assert C.deterministic_tree(Path(lib['local_root'])) == tree
    assert all(C.sha((ROOT / r['path']).read_bytes()) == r['sha256'] for r in provenance)
    assert all(C.file_row(Path(r['local_path']), label=r['label']) == r
               for r in external if r['label'] != 'cubical-extracted-tree')
    manifest = {'schema_version': 'formal-proof-source-manifest/v1', 'proof_id': proof,
                'run_id': run_id, 'files': files, 'external_dependencies': external,
                'noncompiled_provenance_snapshots': provenance}
    env = ('platform=' + platform.platform() + '\nagda=' + version.replace('\n', ' | ') +
           '\ntheory_variant=native Cubical Agda, safe/cubical/guardedness\n' +
           'library_commit=' + lib['tag_commit'] + '\nlibrary_tree_sha256=' + tree['tree_sha256'] +
           '\noriginal_upstream_S1_type_reused=true\ninterfaces_ignored=true\nobservation_seconds=600\n').encode()
    blobs = {'stdout.txt': stdout, 'stderr.txt': stderr, 'environment.txt': env,
             'source-manifest.json': C.json_bytes(manifest)}

    def entry(name):
        return {'path': name, 'bytes': len(blobs[name]), 'sha256': C.sha(blobs[name])}

    run = {'schema_version': 'formal-proof-run/v1', 'run_id': run_id, 'proof_id': proof,
           'claim_ids': ['C-304'] if primary else [], 'proof_assistant': 'Cubical Agda',
           'proof_assistant_version': version, 'theory_variant': 'cubical',
           'command_argv': argv, 'cwd': str(ROOT), 'started_at_utc': started.isoformat(),
           'completed_at_utc': ended.isoformat(), 'duration_seconds': (ended - started).total_seconds(),
           'exit_code': code, 'status': 'OBSERVATION_TIMEOUT' if timeout else 'KERNEL_ACCEPTED_WITH_SCOPE' if code == 0 else 'KERNEL_REJECTED',
           'scope': 'Actual S1 integer-cover consumer chain; ' + args.case +
                    '. Baseline/restoration include family and encoding/winding/intLoop bridges to upstream plus real inverse laws and composition observation. Mutants are only fixed-term causal controls; rejection is not a negative theorem.',
           'non_goals': ['No global HoTT inconsistency/completeness or physical point-removal conclusion.',
                         'No universal failure inferred from one rejected term; no guessed outcome before diagnostic review.'],
           'stdout': entry('stdout.txt'), 'stderr': entry('stderr.txt'), 'environment': entry('environment.txt'),
           'source_manifest': entry('source-manifest.json'),
           'index_status': 'PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE' if primary else 'CONTROL_ONLY_NO_NEW_CLAIM',
           'git_status': 'LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED'}
    dest.mkdir(parents=True)
    for name, data in blobs.items():
        C.exclusive_write(dest / name, data)
    C.exclusive_write(dest / 'RUN.json', C.json_bytes(run))
    if code == 0:
        assert graph.exists()
        C.exclusive_write(dest / 'imports.dot', graph.read_bytes())
    print(json.dumps({'case': args.case, 'run': str(dest.relative_to(ROOT)), 'exit': code,
                      'seconds': run['duration_seconds'], 'external_pins': len(external)}), flush=True)
    if code:
        print(stdout.decode()[-5000:] + stderr.decode(), flush=True)
    raise SystemExit(0 if code in (0, 42) else 1)


if __name__ == '__main__':
    main()
