#!/usr/bin/env python3
"""Check the actual delivery-repair checkpoint, without replaying unchanged proofs."""
from pathlib import Path
import hashlib,importlib.util,json,subprocess
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;out=HERE/'validation';out.mkdir(exist_ok=False)
sp=importlib.util.spec_from_file_location('rt',ROOT/'.codex/tools/cognition_runtime.py');rt=importlib.util.module_from_spec(sp);sp.loader.exec_module(rt)
s=json.loads((ROOT/rt.STATE).read_text());h=json.loads((ROOT/rt.HEAD).read_text());rt.query_record(ROOT,'MO3-GOVERNED-A');p=rt.plan(ROOT,profile='research',task_ids=['MO3-GOVERNED-A'])
rows=[]
for name in ['verify_three_way_cognition','verify_governance_shards']:
    argv=['python3','-B','scripts/audit/'+name+'.py'];r=subprocess.run(argv,cwd=ROOT,capture_output=True);(out/(name+'.stdout.txt')).write_bytes(r.stdout);(out/(name+'.stderr.txt')).write_bytes(r.stderr);rows.append(dict(argv=argv,exit=r.returncode))
drift=[f for f,x in h['tracked'].items() if hashlib.sha256((ROOT/f).read_bytes()).hexdigest()!=x]
ok=s['revision']==283 and not drift and not p['review_required'] and not p['hydration_diagnostics']['query_first_promoted'] and all(x['exit']==0 for x in rows)
result=dict(status='PASS_WITH_SCOPE' if ok else 'FAILED',revision=s['revision'],tracked_drift=drift,review_required=p['review_required'],query_first_promoted=p['hydration_diagnostics']['query_first_promoted'],checks=rows,scope='Canonical delivery-interface correction, prior 281/282 native-input checks and diagnostic-003 remain scoped evidence; final002 byte/copy check still required')
(out/'RESULT.json').write_bytes(rt.dump(result));print(json.dumps(result,ensure_ascii=False));raise SystemExit(0 if ok else 1)
