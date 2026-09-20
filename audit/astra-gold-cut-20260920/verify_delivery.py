#!/usr/bin/env python3
"""Verify the actual Cubical package and its complete local import closure."""
from pathlib import Path
import json,re,subprocess,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
PROOF='MP-ASTRA-STANDARD-GOLD-CUT-001';run='HoTT/verification/runs/20260920-'+PROOF+'-02';checks=[]
for kind,argv in [('formal',['python3','-B','scripts/audit/verify_formal_proof_run.py','--run-dir',run]),('relation',['python3','-B','scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id',PROOF])]:
 p=subprocess.run(argv,cwd=ROOT,capture_output=True);(OUT/(kind+'.stdout.json')).write_bytes(p.stdout);(OUT/(kind+'.stderr.txt')).write_bytes(p.stderr)
 checks.append({'kind':kind,'argv':argv,'exit':p.returncode});print(kind,p.returncode,flush=True);assert p.returncode==0,p.stdout.decode()[-2200:]+p.stderr.decode()
def nodes(p):return set(re.findall(r'\[label="([^"]+)"\]',p.read_text()))
actual=nodes(ROOT/run/'imports.dot');draft=nodes(OUT/'attempts/004/imports.dot');assert actual==draft
m=json.loads((ROOT/run/'source-manifest.json').read_text());local={Path(f['path']).stem for f in m['files'] if f['path'].endswith('.agda')}
assert local=={x for x in actual if not x.startswith(('Cubical.','Agda.'))};assert len(local)==10
old=nodes(ROOT/'HoTT/verification/runs/20260920-MP-ASTRA-STANDARD-GOLD-CUT-001-01/imports.dot');assert actual-old=={'Sqrt2TableRecovery'} and not old-actual
r=json.loads((ROOT/run/'RUN.json').read_text());assert r['exit_code']==0 and '--ignore-interfaces' in r['command_argv']
assert (ROOT/run/'stderr.txt').read_bytes()==b'';assert 'warning:' not in (ROOT/run/'stdout.txt').read_text()
(OUT/'IMPORT-DELTA.json').write_text(json.dumps({'scope':'Compiler import graph; not minimal axioms','current':len(actual),'pre_recovery_run':len(old),'added':['Sqrt2TableRecovery'],'local_modules':sorted(local),'external_modules_pinned_by_cubical_tree_and_builtins':True},indent=2)+'\n')
pins=[]
for oldrun in ['20260919-MP-DEDEKIND-OMEGA-GOLD-03','20260919-MP-DEDEKIND-OMEGA-REAL-LAYER-04']:
 oldm=json.loads((ROOT/'HoTT/verification/runs'/oldrun/'source-manifest.json').read_text())
 for f in oldm['files']:
  if f['path'].endswith('.agda'):
   assert hashlib.sha256((ROOT/f['path']).read_bytes()).hexdigest()==f['sha256'];pins.append({'source':f['path'],'prior_run':oldrun,'sha256':f['sha256']})
(OUT/'QUALIFICATION.json').write_text(json.dumps({'theory':'Fixed Cubical v0.9 safe/cubical/guardedness; two-level explicit in main/legacy bridge','old_math_sources_unchanged':pins,'environment_identity':'See immutable RUN manifest; binary/archives/library tree checked before and after','book_sources':'Pinned 578b85cc reals.tex85–211 and logic.tex638–675; official same-ref URLs also consulted','old_comments_are_not_proof_claims':True},ensure_ascii=False,indent=2)+'\n')
(OUT/'DELIVERY.json').write_text(json.dumps({'status':'FORMAL_CHECKED_AND_RELATION_PASS_WITH_SCOPE','checks':checks,'fresh_kernel_run':run,'extra_kernel_rerun':False,'kernel_seconds':r['duration_seconds'],'source_graph_matches_final_draft':True,'import_modules':len(actual),'local_source_count':len(local),'claim_ids':['C-297','C-298','C-299'],'unproved':['All-precision approximation','Real-ring x^2=2 and completeness','Same-level smallness or SingleOmega necessity/refutation','Circle/arithmetic faithful reduction and full four-stage redo']},ensure_ascii=False,indent=2)+'\n')
