#!/usr/bin/env python3
"""Preserve every local Lean draft check. Not a final F-011 delivery receipt."""
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
source=ROOT/(sys.argv[1] if len(sys.argv)>1 else 'HoTT/formal/astra-real-geometry/PuncturedCircle.lean')
attempts=OUT/'draft-checks'
attempts.mkdir(exist_ok=True)
run=attempts/f'{len(list(attempts.glob("attempt-*")))+1:03d}'
run=attempts/('attempt-'+run.name)
run.mkdir()
data=source.read_bytes()
(run/source.name).write_bytes(data)
lean_path=(OUT/'environment-qualification/LEAN_PATH.txt').read_text().strip()
argv=['/usr/bin/env','LEAN_PATH='+lean_path,
      '/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean',
      str(source.relative_to(ROOT))]
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=subprocess.run(argv,cwd=ROOT,capture_output=True)
(run/'stdout.txt').write_bytes(r.stdout)
(run/'stderr.txt').write_bytes(r.stderr)
(run/'CHECK.json').write_text(json.dumps(dict(argv=argv,cwd=str(ROOT),exit=r.returncode,
  started=started,completed=datetime.datetime.now(datetime.timezone.utc).isoformat(),
  source_sha256=hashlib.sha256(data).hexdigest(),scope='DRAFT_CHECK_NOT_FINAL_DELIVERY'),indent=2)+'\n')
print('ATTEMPT',run.name,'EXIT',r.returncode,flush=True)
print(r.stdout.decode(),r.stderr.decode(),flush=True)
