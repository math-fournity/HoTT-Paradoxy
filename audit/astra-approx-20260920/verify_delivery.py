#!/usr/bin/env python3
"""Verify the native binary-precision proof and original Pell comparison."""
from pathlib import Path
import json,re,subprocess,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
PROOF='MP-ASTRA-SQRT2-APPROX-001';run='HoTT/verification/runs/20260920-'+PROOF+'-01';checks=[]
for kind,argv in [('formal',['python3','-B','scripts/audit/verify_formal_proof_run.py','--run-dir',run]),('relation',['python3','-B','scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id',PROOF])]:
 p=subprocess.run(argv,cwd=ROOT,capture_output=True);(OUT/(kind+'.stdout.json')).write_bytes(p.stdout);(OUT/(kind+'.stderr.txt')).write_bytes(p.stderr)
 checks.append({'kind':kind,'argv':argv,'exit':p.returncode});print(kind,p.returncode,flush=True);assert p.returncode==0,p.stdout.decode()[-2200:]+p.stderr.decode()
def nodes(p):return set(re.findall(r'\[label="([^"]+)"\]',p.read_text()))
actual=nodes(ROOT/run/'imports.dot');draft=nodes(OUT/'attempts/003/imports.dot');assert actual==draft
m=json.loads((ROOT/run/'source-manifest.json').read_text());local={Path(f['path']).stem for f in m['files'] if f['path'].endswith('.agda')}
assert local=={x for x in actual if not x.startswith(('Cubical.','Agda.'))};assert len(local)==12
old=nodes(ROOT/'HoTT/verification/runs/20260920-MP-ASTRA-STANDARD-GOLD-CUT-001-02/imports.dot')
(OUT/'IMPORT-DELTA.json').write_text(json.dumps({'scope':'Compiler import graph, not minimal axioms','current':len(actual),'prior_gold':len(old),'added':sorted(actual-old),'removed':sorted(old-actual),'local_modules':sorted(local),'all_external_modules_pinned_by_library_tree_and_builtins':True},indent=2)+'\n')
r=json.loads((ROOT/run/'RUN.json').read_text());assert r['exit_code']==0 and '--ignore-interfaces' in r['command_argv']
assert (ROOT/run/'stderr.txt').read_bytes()==b'';assert 'warning:' not in (ROOT/run/'stdout.txt').read_text()
(OUT/'DELIVERY.json').write_text(json.dumps({'status':'FORMAL_CHECKED_AND_RELATION_PASS_WITH_SCOPE','checks':checks,'fresh_kernel_run':run,'extra_kernel_rerun':False,'kernel_seconds':r['duration_seconds'],'source_graph_matches_final_draft':True,'import_modules':len(actual),'local_source_count':len(local),'claim_ids':['C-300','C-301'],'initial_endpoints':['1','2'],'precision_width':'d(0)=1, d(suc n)=d(n)*(1/2)','trace_counts':'refine calls, not CPU or physical time','unproved':['Arbitrary-real-epsilon cofinality or complete real convergence','Pell convergence/optimality or equality of Pell D and interval width','Real-ring square-root equation and same-level smallness','Circle/arithmetic faithful reduction and full four-stage redo']},ensure_ascii=False,indent=2)+'\n')
