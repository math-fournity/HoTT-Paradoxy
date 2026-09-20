#!/usr/bin/env python3
"""Verify the same-map closed extension run and exact dependency closure."""
from pathlib import Path
import json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
PROOF='MP-ASTRA-NATIVE-COMPLETION-001';run='HoTT/verification/runs/20260920-'+PROOF+'-01';checks=[]
for kind,argv in [('formal',['python3','-B','scripts/audit/verify_formal_proof_run.py','--run-dir',run]),('relation',['python3','-B','scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id',PROOF])]:
 p=subprocess.run(argv,cwd=ROOT,capture_output=True);(OUT/(kind+'.stdout.json')).write_bytes(p.stdout);(OUT/(kind+'.stderr.txt')).write_bytes(p.stderr)
 checks.append({'kind':kind,'argv':argv,'exit':p.returncode});print(kind,p.returncode,flush=True);assert p.returncode==0,p.stdout.decode()[-1800:]+p.stderr.decode()
def nodes(p):return set(re.findall(r'\[label="([^"]+)"\]',p.read_text()))
actual=nodes(ROOT/run/'imports.dot');draft=nodes(OUT/'attempts/002/imports.dot');assert actual==draft
old=nodes(ROOT/'HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-INTERVAL-001-01/imports.dot')
assert actual-old=={'hott-z.NativeCompletion','hott-z.HomogeneousCircle'};assert not old-actual
(OUT/'IMPORT-DELTA.json').write_text(json.dumps({'scope':'Compiler import graph, not minimal proof-term axioms','baseline':len(old),'current':len(actual),'added':sorted(actual-old),'removed':[],'new_external_modules':[]},indent=2)+'\n')
r=json.loads((ROOT/run/'RUN.json').read_text());assert r['exit_code']==0 and '--ignore-interfaces' in r['command_argv']
assert (ROOT/run/'stderr.txt').read_bytes()==b'';assert 'warning:' not in (ROOT/run/'stdout.txt').read_text()
(OUT/'DELIVERY.json').write_text(json.dumps({'status':'FORMAL_CHECKED_AND_RELATION_PASS_WITH_SCOPE','checks':checks,'fresh_kernel_run':run,'extra_kernel_rerun':False,'kernel_seconds':r['duration_seconds'],'source_graph_matches_final_draft':True,'import_modules':len(actual),'claim_ids':['C-291','C-292'],'unproved':['Unconditional weak Lift','Source-preserving Task/Trace/Done and actual rich-structure comparison','Full native process/Task/Trace/Done integration','Complete four-stage redo'],'native_intrinsic_geometry_directly_proved':True,'whole_Lean_interpreter_is_not_a_prerequisite_for_these_native_claims':True},ensure_ascii=False,indent=2)+'\n')
