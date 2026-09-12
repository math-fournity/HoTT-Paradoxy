#!/usr/bin/env python3
"""Probe available native tools only; do not install or pretend to compile."""
from pathlib import Path
import datetime, hashlib, json, shutil, subprocess
ROOT=Path(__file__).resolve().parents[2]
source=ROOT/'scripts/research/r030_formal/ReflectionBoundary.agda'
r={'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tools':{k:shutil.which(k) for k in ['agda','lean','coqc','rocq']},'source':str(source.relative_to(ROOT)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scope':'Shared intensional type theory fragment only, not full HoTT'}
if r['tools']['agda']:
 cmd=[r['tools']['agda'],'--safe','--without-K',str(source)]
 p=subprocess.run(cmd,cwd=source.parent,text=True,capture_output=True,timeout=35)
 r.update(status='PASS' if p.returncode==0 else 'FAIL',argv=cmd,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
else:r.update(status='NOT_RUN',reason='agda executable not present in this sandbox PATH; no installation attempted')
(ROOT/'artifacts/r030/NATIVE_STATUS.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(r,ensure_ascii=False,indent=2))
