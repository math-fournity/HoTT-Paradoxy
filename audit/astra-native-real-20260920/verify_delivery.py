#!/usr/bin/env python3
"""Check exact receipts and controls, then replay the three positive packages."""
from pathlib import Path
import hashlib,json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
def readrun(name):
 p=ROOT/'HoTT/verification/runs'/('20260920-MP-ASTRA-'+name+'-001-01');r=json.loads((p/'RUN.json').read_text())
 for key in ['stdout','stderr','environment','source_manifest']:
  row=r[key];data=(p/row['path']).read_bytes();assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256']
 return p,r,json.loads((p/'source-manifest.json').read_text())
op,orig,om=readrun('ERASURE-CONFIG');np,neg,nm=readrun('ERASURE-CONTROL')
assert om['files'][0]==nm['files'][0]
assert orig['exit_code']==0 and neg['exit_code']==42
nt=(np/'stdout.txt').read_text();ot=(op/'stdout.txt').read_text()
assert '[UnequalTerms]' in nt and 'p != refl of type Id x x' in nt and 'inv (eraseRetract p)' in nt
assert 'WithoutKFlagPrimEraseEquality' in ot and 'WithoutKFlagPrimEraseEquality' not in nt
source=ROOT/om['files'][0]['path'];assert hashlib.sha256(source.read_bytes()).hexdigest()==om['files'][0]['sha256']
draftnodes=set(re.findall(r'\[label="([^"]+)"\]',(OUT/'attempts/005/imports.dot').read_text()))
realp,real,rm=readrun('NATIVE-REAL')
finalnodes=set(re.findall(r'\[label="([^"]+)"\]',(realp/'imports.dot').read_text()))
assert draftnodes==finalnodes
checks=[]
for label in ['ERASURE-CONFIG','NATIVE-REAL','NOSECTION-RESTRICTED']:
 proof='MP-ASTRA-'+label+'-001';run='HoTT/verification/runs/20260920-'+proof+('-02' if label=='NOSECTION-RESTRICTED' else '-01')
 for kind,argv in [('formal',['python3','-B','scripts/audit/verify_formal_proof_run.py','--run-dir',run,'--rerun']),('relation',['python3','-B','scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id',proof])]:
  p=subprocess.run(argv,cwd=ROOT,capture_output=True)
  (OUT/(label+'-'+kind+'.stdout.txt')).write_bytes(p.stdout);(OUT/(label+'-'+kind+'.stderr.txt')).write_bytes(p.stderr)
  checks.append(dict(proof=proof,kind=kind,argv=argv,exit=p.returncode));print(label,kind,p.returncode,flush=True)
  assert p.returncode==0,p.stdout.decode()[-2000:]+p.stderr.decode()[-2000:]
data={'status':'THREE_PACKAGES_DUAL_LOCAL_PASS_WITH_CONFIGURATION_SCOPE','checks':checks,'negative_control':{'same_source_hash':True,'exit':42,'diagnostic':'UnequalTerms at loopRefl','ordinary_identity_replacement':True},'formal_graph_matches_draft':True,'module_count':len(finalnodes),'scope':'Configuration diagnostic C280; actual Dedekind model C281; existing C05 requalification. Not ordinary HoTT inconsistency or complete redo.'}
(OUT/'DELIVERY.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
