#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'artifacts/r040';OUT.mkdir(parents=True,exist_ok=True)
cmd=[sys.executable,'-B','scripts/handoff/test_delta_tool.py'];start=datetime.now(timezone.utc).isoformat()
p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
receipt={'argv':cmd,'cwd':str(ROOT),'started_at_utc':start,'finished_at_utc':datetime.now(timezone.utc).isoformat(),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'source_sha256':{str(q.relative_to(ROOT)):hashlib.sha256(q.read_bytes()).hexdigest() for q in [ROOT/'scripts/handoff/delta_tool.py',ROOT/'scripts/handoff/test_delta_tool.py']},'scope':'Synthetic packaging, hash, Git and isolated reconstruction tests; NOT mathematical or AI cognitive verification'}
out=OUT/'DELTA_TEST_EXECUTION.json'
if out.exists():raise FileExistsError(out)
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(p.stdout+p.stderr);raise SystemExit(p.returncode)
