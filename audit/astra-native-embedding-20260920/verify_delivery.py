#!/usr/bin/env python3
"""Verify actual native slice homeomorphisms onto ambient-metric images."""
from pathlib import Path
import json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
RUN='HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-EMBEDDING-001-01'
checks=[]
for label,args in [('formal',['scripts/audit/verify_formal_proof_run.py','--run-dir',RUN]),('relation',['scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id','MP-ASTRA-NATIVE-EMBEDDING-001'])]:
    p=subprocess.run(['python3','-B',*args],cwd=ROOT,capture_output=True)
    (OUT/(label+'.stdout.json')).write_bytes(p.stdout);(OUT/(label+'.stderr.txt')).write_bytes(p.stderr)
    assert p.returncode==0,p.stdout.decode()+p.stderr.decode();checks.append({'kind':label,'argv':args,'exit':p.returncode})
graph=(ROOT/RUN/'imports.dot').read_bytes();assert graph==(OUT/'attempts/004/imports.dot').read_bytes()
modules=re.findall(rb'label="([^"]+)"',graph)
run=json.loads((ROOT/RUN/'RUN.json').read_text())
receipt={'status':'FORMAL_AND_RELATION_PASS_WITH_SCOPE','claim_ids':['C-313'],'primary_run':RUN,'primary_seconds':run['duration_seconds'],'checks':checks,'compiled_local_modules':16,'import_modules':len(modules),'external_pins':41,'draft_final_graph_exact_match':True,'formal_kernel_runs':1,'draft_checks':4,'theory':'Pinned without-K no-erasure agda-unimath with inherited foundation postulates; not safe Cubical and not a whole-theory consistency certificate.','unproved':['Whole closed-parameter time family, interior agreement, endpoint/fiber classification and uniform spatial bound','Whole Lean/native model translation and original Weak-puncture coverage without a stated principle','Physical/original broad task mismatch and complete four-stage integration'],'parent_goal':'OPEN'}
(OUT/'DELIVERY.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k!='checks'},ensure_ascii=False))
