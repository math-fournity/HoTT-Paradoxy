#!/usr/bin/env python3
"""Read-only verification of the immutable seal and four copied proof packages."""
from pathlib import Path
import os,json,subprocess,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3];SEAL=HERE.parent/'final-001';COPY=SEAL/'files'
HASH='8f49c74f9db9c2967a3e19ad11749c3d0ed748414f89516080619e2b0fb3d404'
SUBJECT='b4fbad4e6532cebe96cfb2eb9b562938ba9bf240'
assert hashlib.sha256((SEAL/'MANIFEST.json').read_bytes()).hexdigest()==HASH
assert json.loads((SEAL/'SEAL.json').read_text())['subject_commit']==SUBJECT
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1');rows=[]
commands=[('seal-live',['python3','-B',str(ROOT/'第三轮机器统观/整备/handoff_snapshot.py'),'verify','--seal',str(SEAL),'--expected-sha',HASH,'--live-root',str(ROOT)])]
for id in ['MP-MO3-STAGE-COLIMIT-001','MP-MO3-BOUQUET-ORDER-001','MP-MO3-FINITE-COVER-001','MP-MO3-OPEN-COVER-MARGIN-001']:
    commands.append((id,['python3','-B',str(COPY/'scripts/audit/verify_proof_version_closure.py'),'--project-root',str(COPY),'--proof-id',id,'--evidence-only']))
for name,argv in commands:
    proc=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True)
    (HERE/(name+'.stdout.txt')).write_bytes(proc.stdout);(HERE/(name+'.stderr.txt')).write_bytes(proc.stderr)
    rows.append(dict(name=name,argv=argv,exit=proc.returncode))
# Prove that the copied verification did not mutate the sealed input.
argv=['python3','-B',str(ROOT/'第三轮机器统观/整备/handoff_snapshot.py'),'verify','--seal',str(SEAL),'--expected-sha',HASH]
proc=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True);(HERE/'seal-after.stdout.txt').write_bytes(proc.stdout);(HERE/'seal-after.stderr.txt').write_bytes(proc.stderr);rows.append(dict(name='seal-after',argv=argv,exit=proc.returncode))
result=dict(schema='mo3-final-delivery-verification/v1',status='PASS_WITH_SCOPE' if all(x['exit']==0 for x in rows) else 'FAILED',manifest_sha256=HASH,subject_commit=SUBJECT,checks=rows,scope='Exact sealed bytes/live match and copied selected proof evidence relationships; no kernel rerun, no B independent semantic audit, no clean whole-tree claim')
(HERE/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False));raise SystemExit(0 if result['status']=='PASS_WITH_SCOPE' else 1)
