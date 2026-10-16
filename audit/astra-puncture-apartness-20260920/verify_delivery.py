#!/usr/bin/env python3
"""Verify this completed fresh kernel run without claiming a second kernel replay."""
from pathlib import Path
import json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
PROOF='MP-ASTRA-PUNCTURE-APARTNESS-001';run='HoTT/verification/runs/20260920-'+PROOF+'-01'
checks=[]
for kind,argv in [('formal',['python3','-B','scripts/audit/verify_formal_proof_run.py','--run-dir',run]),('relation',['python3','-B','scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id',PROOF])]:
 p=subprocess.run(argv,cwd=ROOT,capture_output=True)
 (OUT/(kind+'.stdout.json')).write_bytes(p.stdout);(OUT/(kind+'.stderr.txt')).write_bytes(p.stderr)
 checks.append({'kind':kind,'argv':argv,'exit':p.returncode});print(kind,p.returncode,flush=True)
 assert p.returncode==0,p.stdout.decode()[-1800:]+p.stderr.decode()
def nodes(p):return set(re.findall(r'\[label="([^"]+)"\]',p.read_text()))
actual=nodes(ROOT/run/'imports.dot');draft=nodes(OUT/'attempts/003/imports.dot');assert actual==draft
baseline=nodes(ROOT/'HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-REAL-001-01/imports.dot')
extra=sorted(actual-baseline);markers=[]
lib=Path('/Volumes/D/HoTT-toolchain-cache/agda-unimath-7b81411d-astra-no-erasure-v1/src')
for mod in extra:
 for suffix in ['.agda','.lagda.md']:
  p=lib/(mod.replace('.','/')+suffix)
  if p.exists():
   for n,line in enumerate(p.read_text().splitlines(),1):
    if re.search(r'^\s*(postulate|primitive)\b|NO_POSITIVITY|NON_TERMINATING|TERMINATING|type-in-type|allow-unsolved',line):markers.append({'module':mod,'line':n,'text':line})
(OUT/'IMPORT-DELTA.json').write_text(json.dumps({'scope':'Compiler import graph and bounded lexical scan, not minimal proof-term axioms or whole soundness proof','total':len(actual),'baseline':len(baseline),'new_modules':extra,'new_lexical_markers':markers},ensure_ascii=False,indent=2)+'\n')
r=json.loads((ROOT/run/'RUN.json').read_text());assert r['exit_code']==0 and '--ignore-interfaces' in r['command_argv']
assert (ROOT/run/'stderr.txt').read_bytes()==b''
assert 'warning:' not in (ROOT/run/'stdout.txt').read_text()
(OUT/'DELIVERY.json').write_text(json.dumps({'status':'FORMAL_CHECKED_AND_RELATION_PASS_WITH_SCOPE','checks':checks,'fresh_kernel_run':run,'extra_kernel_rerun':False,'kernel_seconds':r['duration_seconds'],'source_graph_matches_final_draft':True,'import_modules':len(actual),'new_lexical_markers':markers,'claim_ids':['C-283','C-284'],'unproved':['Unconditional LocalStability/Lift','Its negation or independence','Necessity of global LEM','Full homeomorphism or physical process']},ensure_ascii=False,indent=2)+'\n')
