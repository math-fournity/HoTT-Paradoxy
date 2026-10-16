#!/usr/bin/env python3
"""Replay only the four already-indexed Flash modules; preserve validator outputs."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys

root = Path(__file__).resolve().parents[2]
out = Path(__file__).resolve().parent / 'replays'
out.mkdir(exist_ok=True)
names = ['20260919-MP-G4-RING-ORIGIN-02', '20260919-MP-G4-BREAKPOINT-BRIDGE-03',
         '20260919-MP-G4-NO-BREAKOUT-02', '20260919-MP-G4-CUT-AS-SOURCE-01']
rows=[]
for name in names:
    target = out / name
    target.mkdir()
    argv=[sys.executable,'scripts/audit/verify_formal_proof_run.py','--run-dir',
          'HoTT/verification/runs/'+name,'--rerun']
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    run=subprocess.run(argv,cwd=root,capture_output=True)
    (target/'stdout.json').write_bytes(run.stdout)
    (target/'stderr.txt').write_bytes(run.stderr)
    row=dict(run=name,command=argv,started=started,exit_code=run.returncode,
             completed=datetime.datetime.now(datetime.timezone.utc).isoformat(),
             stdout_sha256=hashlib.sha256(run.stdout).hexdigest(),
             stderr_sha256=hashlib.sha256(run.stderr).hexdigest())
    try: row['verification']=json.loads(run.stdout)
    except ValueError: row['verification']='NON_JSON_OUTPUT'
    rows.append(row)
    (out/'REPLAY.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(row,ensure_ascii=False),flush=True)
