#!/usr/bin/env python3
"""Preserve both auxiliary graphs and attach the actual second-run compiler graph.

The immutable source/run manifests and the mistaken imports.dot remain unchanged.
This is evidence reconciliation, not a new kernel run or retroactive replacement.
"""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
run=ROOT/'HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-RICH-TASK-001-02'
def sha(b):return hashlib.sha256(b).hexdigest()
def nodes(b):return set(re.findall(r'\[label="([^"]+)"\]',b.decode()))
r=json.loads((run/'RUN.json').read_text());assert r['exit_code']==0
arg=[a for a in r['command_argv'] if a.startswith('--dependency-graph=')];assert len(arg)==1
actual=Path(arg[0].split('=',1)[1]);assert actual==OUT/'formal-controls-imports.dot'
assert r['command_argv'][-1]=='HoTT/formal/agda-unimath/hott-z/NativeCurveTaskControls.agda'
assert 'Checking hott-z.NativeCurveTaskControls (' in (run/'stdout.txt').read_text()
wrong=(run/'imports.dot').read_bytes();raw=actual.read_bytes()
first=ROOT/'HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-RICH-TASK-001-01/imports.dot'
assert wrong==first.read_bytes()
assert nodes(raw)-nodes(wrong)=={'hott-z.NativeCurveTaskControls'} and not nodes(wrong)-nodes(raw)
m=json.loads((run/'source-manifest.json').read_text())
for f in m['files']:assert sha((ROOT/f['path']).read_bytes())==f['sha256']
local=[f['path'] for f in m['files'] if f['path'].endswith('.agda')];assert len(local)==13
assert all('hott-z.'+Path(p).stem in nodes(raw) for p in local)
target=run/'imports.actual.dot';assert not target.exists();target.write_bytes(raw)
receipt={'status':'RECONCILED_AUXILIARY_GRAPH_CAPTURE_ERROR','error':'capture_controls.py argv emitted formal-controls-imports.dot but attachment code copied formal-imports.dot from first run','kernel_result_changed':False,'source_and_run_manifest_changed':False,'old_imports_dot_preserved':True,'run_json_sha256':sha((run/'RUN.json').read_bytes()),'source_manifest_sha256':sha((run/'source-manifest.json').read_bytes()),'wrong_attachment':{'path':str((run/'imports.dot').relative_to(ROOT)),'sha256':sha(wrong),'modules':len(nodes(wrong))},'actual_emitted_graph':{'path':str(actual.relative_to(ROOT)),'sha256':sha(raw),'modules':len(nodes(raw))},'new_attachment':{'path':str(target.relative_to(ROOT)),'sha256':sha(raw)},'actual_command_graph_path_matched':True,'all_local_sources_unchanged_and_in_graph':True,'local_source_count':len(local),'no_extra_kernel_run':True}
dest=OUT/'GRAPH-RECONCILIATION.json';assert not dest.exists();dest.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
