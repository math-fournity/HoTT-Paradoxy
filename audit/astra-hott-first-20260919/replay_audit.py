#!/usr/bin/env python3
"""Bounded read-only proof audit; writes only this audit's evidence directory.

Replays existing commands with --ignore-interfaces, preserving their historical
receipts. Does not register new mathematical claims or mutate project state.
"""
from pathlib import Path
import datetime, hashlib, json, subprocess, sys, time

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
POSITIVE = [
    '20260917-MP-DEDEKIND-OMEGA-M1-04',
    '20260917-MP-DEDEKIND-OMEGA-M2-01',
    '20260917-MP-DEDEKIND-OMEGA-M3-01',
    '20260917-MP-DEDEKIND-OMEGA-M3-UNC-01',
    '20260917-MP-DEDEKIND-OMEGA-BP-01',
    '20260918-MP-DEDEKIND-OMEGA-GOLD-02',
    '20260918-MP-DEDEKIND-OMEGA-REAL-LAYER-02',
    '20260917-MP-DEDEKIND-OMEGA-TA-01',
    '20260919-MP-DEDEKIND-OMEGA-REBOUND-DISARM-01',
    '20260919-MP-DEDEKIND-OMEGA-NECESSITY-LEM-01',
]
PROBES = [
    ('UA-control', 'MissileFourTargetA-ProbeControl.agda', 0),
    ('UA-zero', 'MissileFourTargetA-ProbeZero.agda', 42),
    ('UA-one', 'MissileFourTargetA-ProbeSucZero.agda', 42),
    ('AC-zero', 'MissileFourTargetA-ProbeACZero.agda', 42),
    ('AC-one', 'MissileFourTargetA-ProbeACSuc.agda', 42),
    ('LEM-zero', 'MissileFourTargetA-ProbeLEMZero.agda', 42),
    ('LEM-one', 'MissileFourTargetA-ProbeLEMSuc.agda', 42),
]

def sha(b):
    return hashlib.sha256(b).hexdigest()

def snapshot():
    paths = sorted((ROOT / 'HoTT/formal/dedekind-omega-missile').glob('*.agda'))
    paths += [ROOT / 'HoTT/CLAIM_EVIDENCE_MATRIX.md', ROOT / 'scripts/audit/verify_formal_proof_run.py']
    paths += sorted((ROOT / 'HoTT/verification/runs').glob('*DEDEKIND*/RUN.json'))
    return [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
             'sha256': sha(p.read_bytes())} for p in paths]

def execute(label, command):
    dest = OUT / 'replays' / label
    dest.mkdir(parents=True, exist_ok=False)
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    before = time.monotonic()
    r = subprocess.run(command, cwd=ROOT, capture_output=True, check=False)
    (dest / 'stdout.txt').write_bytes(r.stdout)
    (dest / 'stderr.txt').write_bytes(r.stderr)
    row = {'label': label, 'command_argv': command, 'cwd': str(ROOT),
           'started_at': start, 'duration_seconds': round(time.monotonic()-before, 3),
           'exit_code': r.returncode, 'stdout_sha256': sha(r.stdout),
           'stderr_sha256': sha(r.stderr), 'stdout_bytes': len(r.stdout),
           'stderr_bytes': len(r.stderr)}
    (dest / 'receipt.json').write_text(json.dumps(row, ensure_ascii=False, indent=2)+'\n')
    return row, r

def main():
    before = snapshot()
    (OUT/'source-snapshot-before.json').write_text(json.dumps(before, ensure_ascii=False, indent=2)+'\n')
    results = []
    for rid in POSITIVE:
        historical = json.loads((ROOT/'HoTT/verification/runs'/rid/'RUN.json').read_text())
        argv = historical['command_argv']
        if '--ignore-interfaces' not in argv:
            raise RuntimeError('Fresh check flag absent: '+rid)
        row, r = execute(rid, argv)
        old = ROOT/'HoTT/verification/runs'/rid
        row['historical_exact_match'] = (r.returncode == historical['exit_code'] and
            r.stdout == (old/'stdout.txt').read_bytes() and r.stderr == (old/'stderr.txt').read_bytes())
        check, c = execute(rid+'-canonical', [sys.executable, 'scripts/audit/verify_formal_proof_run.py', '--run-dir', str(old.relative_to(ROOT))])
        row['canonical_verification_exit'] = c.returncode
        row['canonical_verification'] = (c.stdout or c.stderr).decode(errors='replace')
        results.append(row)
        (OUT/'RESULTS.json').write_text(json.dumps(results, ensure_ascii=False, indent=2)+'\n')
        print(rid, 'kernel_exit',r.returncode,'exact',row['historical_exact_match'],'canonical',c.returncode, flush=True)
    base = json.loads((ROOT/'HoTT/verification/runs'/POSITIVE[0]/'RUN.json').read_text())['command_argv']
    for label, filename, expected in PROBES:
        command = base[:-1]+['HoTT/formal/dedekind-omega-missile/'+filename]
        row, r = execute(label,command)
        row['expected_exit'] = expected
        row['expectation_met'] = r.returncode == expected
        results.append(row)
        (OUT/'RESULTS.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
        print(label,'exit',r.returncode,'expected',expected,flush=True)
    after = snapshot()
    (OUT/'source-snapshot-after.json').write_text(json.dumps(after,ensure_ascii=False,indent=2)+'\n')
    summary = {'schema_version':'astra-hott-proof-audit/v1','baseline_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
               'source_unchanged':before==after,'positive_runs':len(POSITIVE),'probes':len(PROBES),
               'scope':'Existing proof statements and specific kernel probes only; no theorem of HoTT failure, canonicity or unprovability.',
               'canonical_passes':sum(x.get('canonical_verification_exit')==0 for x in results),
               'positive_kernel_accepts':sum(x['exit_code']==0 for x in results[:len(POSITIVE)]),
               'exact_positive_matches':sum(x.get('historical_exact_match',False) for x in results),
               'probe_expectations_met':sum(x.get('expectation_met',False) for x in results)}
    (OUT/'SUMMARY.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False),flush=True)

if __name__ == '__main__':
    main()
