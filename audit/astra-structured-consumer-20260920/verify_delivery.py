#!/usr/bin/env python3
"""Replay and qualify each exact structured-consumer proof package."""
from pathlib import Path
import json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
packages=[('LEAN','MP-ASTRA-STRUCTURED-CURVE-001','20260920-MP-ASTRA-STRUCTURED-CURVE-001-02'),('AGDA','MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001','20260920-MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001-01')]
checks=[]
for label,proof,run in packages:
 for kind,argv in [('formal',['python3','scripts/audit/verify_formal_proof_run.py','--run-dir','HoTT/verification/runs/'+run,'--rerun']),('relation',['python3','scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id',proof])]:
  p=subprocess.run(argv,cwd=ROOT,capture_output=True)
  (OUT/(label+'-'+kind+'.stdout.txt')).write_bytes(p.stdout);(OUT/(label+'-'+kind+'.stderr.txt')).write_bytes(p.stderr)
  checks.append(dict(package=proof,kind=kind,argv=argv,exit=p.returncode));print(label,kind,p.returncode,flush=True)
  assert p.returncode==0,p.stdout.decode()[-2000:]+p.stderr.decode()[-1000:]
(OUT/'DELIVERY.json').write_text(json.dumps({'status':'TWO_PACKAGES_DUAL_LOCAL_PASS','checks':checks,'scope':'C275–279, actual Lean boundary observation and native Agda diagram separately checked; no full real-geometry cross-kernel translation'},ensure_ascii=False,indent=2)+'\n')
