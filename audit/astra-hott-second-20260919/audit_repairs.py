#!/usr/bin/env python3
"""Audit GLM's exact proof repairs; only write derived evidence in this directory.

Existing mathematical commands retain their recorded arguments. No historical
receipt, source theorem, canonical state, or Git index is edited. Agda may rebuild
its normal interface cache. This is an audit runner, not a new theorem registry.
"""
from pathlib import Path
import datetime, hashlib, json, re, subprocess, sys, time

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
NEW = ['20260919-MP-DEDEKIND-OMEGA-' + s for s in
       ('REAL-LAYER-03', 'NECESSITY-LEM-02', 'GOLD-03')]
OLD = ['20260917-MP-DEDEKIND-OMEGA-' + s for s in
       ('M1-04', 'M2-01', 'M3-01', 'M3-UNC-01', 'BP-01', 'TA-01')]
OLD += ['20260918-MP-DEDEKIND-OMEGA-GOLD-02',
        '20260918-MP-DEDEKIND-OMEGA-REAL-LAYER-02',
        '20260919-MP-DEDEKIND-OMEGA-REBOUND-DISARM-01',
        '20260919-MP-DEDEKIND-OMEGA-NECESSITY-LEM-01']

def sha(b): return hashlib.sha256(b).hexdigest()
def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')
def file_row(p):
    b=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)), 'bytes':len(b), 'sha256':sha(b)}
def snapshot():
    paths=set((ROOT/'GLM的审计报告').glob('*.md'))
    paths.add(ROOT/'GLM的审计报告.md')
    paths.update((ROOT/'HoTT/formal/dedekind-omega-missile').glob('*'))
    paths.update(ROOT/p for p in ['HoTT/CLAIM_EVIDENCE_MATRIX.md',
                                 'scripts/audit/verify_formal_proof_run.py'])
    for rid in NEW+OLD:
        paths.update((ROOT/'HoTT/verification/runs'/rid).glob('*'))
    return [file_row(p) for p in sorted(paths) if p.is_file() and p.suffix!='.agdai']
def execute(label, argv, cwd=ROOT):
    d=OUT/'checks'/label
    d.mkdir(parents=True, exist_ok=False)
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    t=time.monotonic()
    r=subprocess.run(argv,cwd=cwd,capture_output=True,check=False)
    (d/'stdout.txt').write_bytes(r.stdout)
    (d/'stderr.txt').write_bytes(r.stderr)
    row={'label':label,'argv':argv,'cwd':str(cwd),'started_at':started,
         'duration_seconds':round(time.monotonic()-t,3),'exit_code':r.returncode,
         'stdout_sha256':sha(r.stdout),'stderr_sha256':sha(r.stderr)}
    save(d/'receipt.json',row)
    return row,r

def main():
    base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    before=snapshot(); save(OUT/'INPUT-BEFORE.json',{'head':base,'files':before})
    identity=json.loads((ROOT/'audit/astra-hott-first-20260919/FOUR-SET-IDENTITY.json').read_text())
    cognition=[dict(file_row(ROOT/r['path']), matches_previous=sha((ROOT/r['path']).read_bytes())==r['sha256']) for r in identity]
    save(OUT/'COGNITION-REATTESTATION.json',cognition)
    rows=[]
    src=ROOT/'HoTT/formal/dedekind-omega-missile'
    modules={p.stem:p for p in src.glob('*.agda')}
    for rid in NEW:
        d=ROOT/'HoTT/verification/runs'/rid
        run=json.loads((d/'RUN.json').read_text())
        manifest=json.loads((d/'source-manifest.json').read_text())
        row,r=execute(rid,run['command_argv'])
        row['exact_match']=r.returncode==run['exit_code'] and r.stdout==(d/'stdout.txt').read_bytes() and r.stderr==(d/'stderr.txt').read_bytes()
        visited=set()
        def visit(name):
            if name in visited:return
            visited.add(name)
            for imp in re.findall(r'^\s*(?:open\s+)?import\s+(\S+)',modules[name].read_text(),re.M):
                if imp in modules:visit(imp)
        visit(Path(run['command_argv'][-1]).stem)
        closure=sorted(str(modules[n].relative_to(ROOT)) for n in visited)
        row['explicit_local_import_closure']=closure
        row['missing_local_pins']=sorted(set(closure)-{f['path'] for f in manifest['files']})
        row['external_dependency_labels']=[f['label'] for f in manifest.get('external_dependencies',[])]
        rows.append(row); save(OUT/'REPLAYS.json',rows)
        print(rid,'exit',r.returncode,'exact',row['exact_match'],'missing',row['missing_local_pins'],flush=True)
    validation=[]
    for rid in NEW+OLD:
        row,r=execute(rid+'-verifier',[sys.executable,'scripts/audit/verify_formal_proof_run.py','--run-dir','HoTT/verification/runs/'+rid])
        row['result']=(r.stdout+r.stderr).decode(errors='replace')
        validation.append(row)
        print('verifier',rid,r.returncode,flush=True)
    save(OUT/'VERIFIER-RESULTS.json',validation)
    after=snapshot();save(OUT/'INPUT-AFTER.json',{'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'files':after})
    summary={'schema_version':'astra-hott-second-audit/v1','baseline_head':base,
             'reviewed_inputs_unchanged':before==after,'new_exact_replays':sum(r['exact_match'] for r in rows),
             'new_runs':len(rows),'all_new_local_closures_pinned':all(not r['missing_local_pins'] for r in rows),
             'new_verifier_passes':sum(r['exit_code']==0 for r in validation[:3]),
             'old_verifier_passes':sum(r['exit_code']==0 for r in validation[3:]),
             'old_verifier_total':len(OLD),'four_set_hashes_unchanged':all(r['matches_previous'] for r in cognition),
             'scope':'Three repaired existing proof entries; ten old static receipts. No new theorem, no universal verifier certification.'}
    save(OUT/'SUMMARY.json',summary);print(json.dumps(summary,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
