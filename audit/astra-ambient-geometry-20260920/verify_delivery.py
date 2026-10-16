#!/usr/bin/env python3
"""Persist bounded formal replay and exact source/run/index relation checks."""
from pathlib import Path
import json,subprocess
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
RUN='HoTT/verification/runs/20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02'
checks=[]
for label,argv in [
 ('formal',['python3','scripts/audit/verify_formal_proof_run.py','--run-dir',RUN,'--rerun']),
 ('relation',['python3','scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id','MP-ASTRA-AMBIENT-CIRCLE-001'])]:
 r=subprocess.run(argv,cwd=ROOT,capture_output=True)
 (OUT/(label+'.stdout.txt')).write_bytes(r.stdout)
 (OUT/(label+'.stderr.txt')).write_bytes(r.stderr)
 checks.append(dict(name=label,argv=argv,exit=r.returncode))
 print(label,r.returncode,flush=True)
 if r.returncode:raise RuntimeError(r.stdout.decode()[-2000:]+r.stderr.decode()[-1000:])
(OUT/'DELIVERY.json').write_text(json.dumps(dict(status='DUAL_LOCAL_PASS',checks=checks,
 scope='C-266..C-268 only, classical Lean geometry; finite ambient-homeomorphism operation class; full goal active'),ensure_ascii=False,indent=2)+'\n')
