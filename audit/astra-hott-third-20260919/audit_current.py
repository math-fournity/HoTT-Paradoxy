#!/usr/bin/env python3
"""Read-only audit of GLM second response and its exact existing proof runs.

Writes only this audit's own evidence. Does not edit proof sources, receipts,
matrix, governance state or Git. Agda may rebuild its ordinary interface caches.
"""
from pathlib import Path
import datetime, hashlib, importlib.util, json, re, subprocess, sys, time

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
NEW=['20260919-MP-DEDEKIND-OMEGA-'+x for x in ('M1-05','TA-LEM-03','TA-LEM-04')]
CURRENT=['20260919-MP-DEDEKIND-OMEGA-M1-05']
CURRENT+=['20260917-MP-DEDEKIND-OMEGA-'+x for x in ('M2-01','M3-01','M3-UNC-01','BP-01','TA-01')]
CURRENT+=['20260919-MP-DEDEKIND-OMEGA-'+x for x in ('GOLD-03','REAL-LAYER-03','REBOUND-DISARM-01','NECESSITY-LEM-02')]

def sha(b):return hashlib.sha256(b).hexdigest()
def save(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def row(p):
    b=p.read_bytes();return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':sha(b)}
def execute(name,argv,cwd=ROOT):
    d=OUT/'checks'/name;d.mkdir(parents=True,exist_ok=False)
    t=time.monotonic();started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    r=subprocess.run(argv,cwd=cwd,capture_output=True)
    (d/'stdout.txt').write_bytes(r.stdout);(d/'stderr.txt').write_bytes(r.stderr)
    receipt={'argv':argv,'cwd':str(cwd),'exit_code':r.returncode,'started_at':started,
             'duration_seconds':round(time.monotonic()-t,3),'stdout_sha256':sha(r.stdout),'stderr_sha256':sha(r.stderr)}
    save(d/'receipt.json',receipt);return receipt,r

def snapshot():
    paths=[ROOT/'GLM的第二次审计.md',ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md',ROOT/'scripts/audit/verify_formal_proof_run.py']
    paths+=list((ROOT/'GLM的第二次审计').glob('*.md'))
    paths+=list((ROOT/'HoTT/formal/dedekind-omega-missile').glob('*'))
    for n in ('022','023','024','025','027','029','030'):
        paths+=list((ROOT/'Atria的方案/修订片').glob(n+'*.md'))
    for rid in set(NEW+CURRENT):paths+=list((ROOT/'HoTT/verification/runs'/rid).glob('*'))
    paths+=[ROOT/'Astra对击落HoTT工作的第二次审计.md']
    paths+=list((ROOT/'Astra对击落HoTT工作的第二次审计').glob('*.md'))
    return [row(p) for p in sorted(set(paths)) if p.is_file() and p.suffix!='.agdai']

def main():
    head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    before=snapshot();save(OUT/'INPUT-BEFORE.json',{'head':head,'files':before})
    identity=json.loads((ROOT/'audit/astra-hott-first-20260919/FOUR-SET-IDENTITY.json').read_text())
    cognition=[dict(row(ROOT/x['path']),matches_prior=sha((ROOT/x['path']).read_bytes())==x['sha256']) for x in identity]
    save(OUT/'COGNITION-REATTESTATION.json',cognition)
    runs=[]
    for rid in NEW:
        d=ROOT/'HoTT/verification/runs'/rid;run=json.loads((d/'RUN.json').read_text())
        rec,r=execute(rid,run['command_argv'])
        rec.update(run_id=rid,exact_match=r.returncode==run['exit_code'] and r.stdout==(d/'stdout.txt').read_bytes() and r.stderr==(d/'stderr.txt').read_bytes(),
                   original_status=run['status'],original_index_status=run['index_status'])
        manifest=json.loads((d/'source-manifest.json').read_text())
        rec['manifest_files']=[x['path'] for x in manifest['files']]
        rec['source_hash_mismatches']=[x['path'] for x in manifest['files'] if sha((ROOT/x['path']).read_bytes())!=x['sha256']]
        rec['diagnostic']=(r.stdout+r.stderr).decode() if r.returncode else 'KERNEL_ACCEPTED'
        runs.append(rec);save(OUT/'REPLAYS.json',runs);print(rid,r.returncode,rec['exact_match'],flush=True)
    checks=[]
    for rid in CURRENT:
        rec,r=execute(rid+'-verifier',[sys.executable,'-B','scripts/audit/verify_formal_proof_run.py','--run-dir','HoTT/verification/runs/'+rid])
        rec.update(run_id=rid,result=(r.stdout+r.stderr).decode());checks.append(rec)
        print('verifier',rid,r.returncode,flush=True)
    save(OUT/'VERIFIER-RESULTS.json',checks)
    after=snapshot();save(OUT/'INPUT-AFTER.json',{'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'files':after})
    summary={'schema_version':'astra-third-audit/v1','head':head,'new_runs':len(runs),'exact_replays':sum(x['exact_match'] for x in runs),
             'accepted_runs':sum(x['exit_code']==0 for x in runs),'expected_rejections':sum(x['exit_code']==42 and x['exact_match'] for x in runs),
             'current_static_passes':sum(x['exit_code']==0 for x in checks),'current_static_total':len(checks),
             'inputs_unchanged':before==after,'four_set_unchanged':all(x['matches_prior'] for x in cognition),
             'scope':'Three new historical commands, ten representative current receipts; not a global theorem or portable release audit.'}
    save(OUT/'SUMMARY.json',summary);print(json.dumps(summary,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
