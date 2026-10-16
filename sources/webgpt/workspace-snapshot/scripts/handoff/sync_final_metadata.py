#!/usr/bin/env python3
"""Refresh only this handoff's uncommitted framework manifest before checkpoint; old manifests unchanged."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[2];P=R.parent
f=R/'governance/FRAMEWORK_MANIFEST.json';d=json.loads(f.read_text());old={r['path']:r for r in d['files']}
for p in sorted((R/'scripts/handoff').glob('*.py')):
 old[p.relative_to(R).as_posix()]={'path':p.relative_to(R).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
d['files']=[old[k] for k in sorted(old)]
for p in (f,P/'manifests/GOVERNANCE_FRAMEWORK.json'):p.write_text(json.dumps(d,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
print('Current full governance files:',len(d['files']))
