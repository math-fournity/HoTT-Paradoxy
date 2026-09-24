#!/usr/bin/env python3
"""Verify fixed bytes and copied raw proof receipts with the actual safe CLI."""
from pathlib import Path
import argparse,hashlib,json,os,subprocess
ROOT=Path(__file__).resolve().parents[4]
ap=argparse.ArgumentParser();ap.add_argument('--seal',type=Path,required=True);ap.add_argument('--expected-sha',required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
seal=a.seal.resolve();out=a.output.resolve();assert not out.is_relative_to(seal);out.mkdir(parents=True,exist_ok=False);copy=seal/'files'
assert hashlib.sha256((seal/'MANIFEST.json').read_bytes()).hexdigest()==a.expected_sha
rows=[];env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
commands=[('seal-live',['python3','-B',str(ROOT/'第三轮机器统观/整备/handoff_snapshot.py'),'verify','--seal',str(seal),'--expected-sha',a.expected_sha,'--live-root',str(ROOT)])]
for run in ['20260923-MO3-STAGE-COLIMIT-001-04','20260924-MO3-BOUQUET-ORDER-001-02','20260924-MO3-FINITE-COVER-001-08','20260924-MO3-OPEN-COVER-MARGIN-001-01']:
    commands.append((run,['python3','-B',str(copy/'scripts/audit/verify_formal_proof_run.py'),'--project-root',str(copy),'--run-dir','HoTT/verification/runs/'+run]))
commands.append(('seal-after',['python3','-B',str(ROOT/'第三轮机器统观/整备/handoff_snapshot.py'),'verify','--seal',str(seal),'--expected-sha',a.expected_sha]))
for name,argv in commands:
    r=subprocess.run(argv,cwd=out,env=env,capture_output=True);(out/(name+'.stdout.txt')).write_bytes(r.stdout);(out/(name+'.stderr.txt')).write_bytes(r.stderr);rows.append(dict(name=name,argv=argv,exit=r.returncode))
s=json.loads((seal/'SEAL.json').read_text());result=dict(schema='mo3-copied-delivery-check/v1',status='PASS_WITH_SCOPE' if all(x['exit']==0 for x in rows) else 'FAILED',manifest_sha256=a.expected_sha,subject_commit=s['subject_commit'],file_count=s['file_count'],checks=rows,scope='Byte seal/live/after and four copied raw source/run/index relationships. No kernel rerun, no Git-history copy claim, no B semantic audit; version closure remains the original-repo selected checks.')
(out/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False));raise SystemExit(0 if result['status']=='PASS_WITH_SCOPE' else 1)
