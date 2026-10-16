#!/usr/bin/env python3
"""Verify exact represented-real and conditional all-Dedekind converse scope."""
from pathlib import Path
import json,re,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
RUN='HoTT/verification/runs/20260921-MP-ASTRA-MARKOV-REVERSE-001-01'
checks=[]
for label,args in [('formal',['scripts/audit/verify_formal_proof_run.py','--run-dir',RUN]),('relation',['scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id','MP-ASTRA-MARKOV-REVERSE-001'])]:
    p=subprocess.run(['python3','-B',*args],cwd=ROOT,capture_output=True)
    (OUT/(label+'.stdout.json')).write_bytes(p.stdout);(OUT/(label+'.stderr.txt')).write_bytes(p.stderr)
    assert p.returncode==0,p.stdout.decode()+p.stderr.decode();checks.append({'kind':label,'argv':args,'exit':p.returncode})
graph=(ROOT/RUN/'imports.dot').read_bytes();assert graph==(OUT/'attempts/004/imports.dot').read_bytes()
modules=re.findall(rb'label="([^"]+)"',graph);local=[m for m in modules if m.startswith(b'hott-z.')];assert len(local)==34
run=json.loads((ROOT/RUN/'RUN.json').read_text())
receipt={'status':'FORMAL_AND_RELATION_PASS_WITH_SCOPE','claim_ids':['C-323','C-324'],'primary_run':RUN,'primary_seconds':run['duration_seconds'],'checks':checks,'compiled_local_modules':len(local),'import_modules':len(modules),'external_pins':41,'draft_final_graph_exact_match':True,'formal_kernel_runs':1,'draft_checks':4,'draft_rejections':2,
 'draft_repairs':['001 missing is-section-diff-ℚ import; added additive-group module without changing statement','003 Set name ambiguity; qualified foundation.sets.Set without changing the family'],
 'theory':'Pinned without-K no-erasure agda-unimath with inherited foundation postulates. BookMarkov and level-ACℕ lzero are explicit arguments, not supplied global postulates.',
 'unproved':['Unconditional Markov-to-RNZA on all arbitrary Dedekind reals; extra data/choice is not silently removed.','Necessity/independence of countable choice or Markov; baseline unprovability and necessity of LEM/resizing.','Physical execution, unconditional full Weak recovery, false HoTT promise and completed four-stage objective.'],'parent_goal':'OPEN'}
(OUT/'DELIVERY.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in receipt.items() if k!='checks'},ensure_ascii=False))
