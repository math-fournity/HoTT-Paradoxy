#!/usr/bin/env python3
"""Replay the exact existing arithmetic and restricted-endpoint Agda inputs."""
from pathlib import Path
import concurrent.futures,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent/'agda-comparison'
OUT.mkdir(exist_ok=True)
RUNS=['20260919-MP-DEDEKIND-OMEGA-M1-05','20260917-MP-DEDEKIND-OMEGA-M3-UNC-01','20260919-MP-ASTRA-ENDPOINT-01']
def replay(run):
 argv=['python3','scripts/audit/verify_formal_proof_run.py','--run-dir','HoTT/verification/runs/'+run,'--rerun']
 p=subprocess.run(argv,cwd=ROOT,capture_output=True)
 (OUT/(run+'.stdout.txt')).write_bytes(p.stdout);(OUT/(run+'.stderr.txt')).write_bytes(p.stderr)
 result={'run':run,'argv':argv,'exit':p.returncode}
 print(json.dumps(result),flush=True);return result
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(replay,RUNS))
(OUT/'REPLAY.json').write_text(json.dumps({'scope':'Existing exact Agda inputs, not the Lean curve construction','results':results},indent=2)+'\n')
assert all(x['exit']==0 for x in results)
