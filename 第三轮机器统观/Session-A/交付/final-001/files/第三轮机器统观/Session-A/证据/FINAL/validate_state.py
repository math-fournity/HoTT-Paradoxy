#!/usr/bin/env python3
"""Validate the final wording checkpoint, reusing unchanged native evidence checks."""
from pathlib import Path
import hashlib,importlib.util,json,subprocess
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
out=HERE/'wording-validation';out.mkdir(exist_ok=False)
sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(sp);sp.loader.exec_module(rt)
s=json.loads((ROOT/rt.STATE).read_text());h=json.loads((ROOT/rt.HEAD).read_text());v=json.loads((HERE/'validation/RESULT.json').read_text())
sha=lambda p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
rt.query_record(ROOT,'MO3-GOVERNED-A');p=rt.plan(ROOT,profile='research',task_ids=['MO3-GOVERNED-A'])
checks=[]
for name in ['verify_three_way_cognition','verify_governance_shards']:
    cmd=['python3','-B','scripts/audit/'+name+'.py'];r=subprocess.run(cmd,cwd=ROOT,capture_output=True);(out/(name+'.stdout.txt')).write_bytes(r.stdout);(out/(name+'.stderr.txt')).write_bytes(r.stderr);checks.append(dict(argv=cmd,exit=r.returncode))
drift=[f for f,x in h['tracked'].items() if sha(f)!=x];native=[]
for r in v['primary_runs']:
    m=json.loads((ROOT/'HoTT/verification/runs'/r['run']/'source-manifest.json').read_text());native += [x['path'] for x in m['files'] if sha(x['path'])!=x['sha256']]
receipt=json.loads((ROOT/'.codex/cognition/checkpoints/S-RES-20260924-MO3-A-FINAL-WORDING/result.json').read_text())
ok=s['revision']==282 and receipt['status']=='CHECKPOINT_COMMITTED' and v['status']=='PASS_WITH_SCOPE' and not drift and not native and not p['review_required'] and not p['hydration_diagnostics']['query_first_promoted'] and all(x['exit']==0 for x in checks) and sha(s['current_core']['path'])==v['core_sha256']
result=dict(status='PASS_WITH_SCOPE' if ok else 'FAILED',revision=s['revision'],canonical_receipt='.codex/cognition/checkpoints/S-RES-20260924-MO3-A-FINAL-WORDING/result.json',checks=checks,tracked_drift=drift,unchanged_native_input_drift=native,review_required=p['review_required'],query_first_promoted=p['hydration_diagnostics']['query_first_promoted'],reused_validation=dict(path='第三轮机器统观/Session-A/证据/FINAL/validation/RESULT.json',sha256=sha('第三轮机器统观/Session-A/证据/FINAL/validation/RESULT.json')),scope='Wording/state only; unchanged native packages reuse the actual four-package validation, no additional kernel replay')
(out/'RESULT.json').write_bytes(rt.dump(result));print(json.dumps(result,ensure_ascii=False));raise SystemExit(0 if ok else 1)
