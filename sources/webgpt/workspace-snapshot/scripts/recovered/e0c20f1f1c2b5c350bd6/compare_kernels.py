#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
py=json.load(open(ROOT/'verification/kernel_report.json'))
js=json.load(open(ROOT/'verification/node_crosscheck.json'))
assert py['summary']['overall_ok'] is True
assert js['summary']['overall_ok'] is True
# Compare common semantic conclusions by explicit identifiers rather than counts.
common={
 'factorization': (next(c for c in py['checks'] if c['id']=='K-FIN-001')['passed'], next(c for c in js['checks'] if c['id']=='JS-001')['passed']),
 'refinement': (next(c for c in py['checks'] if c['id']=='K-FIN-002')['passed'], next(c for c in js['checks'] if c['id']=='JS-002')['passed']),
 'natural_orientation': (next(c for c in py['checks'] if c['id']=='K-HOTT-002')['passed'], next(c for c in js['checks'] if c['id']=='JS-003')['passed']),
 'groupoid_core': (next(c for c in py['checks'] if c['id']=='K-HOTT-004')['passed'], next(c for c in js['checks'] if c['id']=='JS-004')['passed']),
 'countermodels': (all(next(c for c in py['checks'] if c['id']==i)['passed'] for i in ['K-Z-PROVENANCE','K-Z-ROLE','K-Z-CONTEXT','K-Z-COST']), next(c for c in js['checks'] if c['id']=='JS-005')['passed']),
 'guard_erasure': (next(c for c in py['checks'] if c['id']=='K-OP-002')['passed'], next(c for c in js['checks'] if c['id']=='JS-006')['passed']),
 'zeno': (next(c for c in py['checks'] if c['id']=='K-LIM-001')['passed'], next(c for c in js['checks'] if c['id']=='JS-007')['passed']),
}
agree=all(a==b==True for a,b in common.values())
out={
 'schema_version':'hott_z.crosscheck_comparison.v1',
 'overall_ok':agree,
 'common_claims':{k:{'python':a,'javascript':b,'agree':a==b} for k,(a,b) in common.items()},
 'python_report_sha256':hashlib.sha256((ROOT/'verification/kernel_report.json').read_bytes()).hexdigest(),
 'javascript_report_sha256':hashlib.sha256((ROOT/'verification/node_crosscheck.json').read_bytes()).hexdigest(),
 'assurance':'independent implementations in Python and JavaScript; finite/executable cross-check, not a mainstream proof assistant'
}
(ROOT/'verification/crosscheck_comparison.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'overall_ok':agree,'claims':len(common)},sort_keys=True))
raise SystemExit(0 if agree else 1)
