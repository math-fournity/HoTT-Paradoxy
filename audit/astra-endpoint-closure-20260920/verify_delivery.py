#!/usr/bin/env python3
"""Actual command replay plus exact source/run/index relation qualification."""
from pathlib import Path
import json,subprocess
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
RUN='HoTT/verification/runs/20260920-MP-ASTRA-ENDPOINT-CLOSURE-001-01'
checks=[]
for label,argv in [('formal',['python3','scripts/audit/verify_formal_proof_run.py','--run-dir',RUN,'--rerun']),('relation',['python3','scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id','MP-ASTRA-ENDPOINT-CLOSURE-001'])]:
 p=subprocess.run(argv,cwd=ROOT,capture_output=True)
 (OUT/(label+'.stdout.txt')).write_bytes(p.stdout);(OUT/(label+'.stderr.txt')).write_bytes(p.stderr)
 checks.append(dict(name=label,argv=argv,exit=p.returncode));print(label,p.returncode,flush=True)
 assert p.returncode==0,p.stdout.decode()[-1500:]+p.stderr.decode()[-1000:]
(OUT/'DELIVERY.json').write_text(json.dumps(dict(status='DUAL_LOCAL_PASS',checks=checks,scope='C271–273; closed-parameter extension, endpoint gap and exact final fibers; full HoTT goal active'),ensure_ascii=False,indent=2)+'\n')
