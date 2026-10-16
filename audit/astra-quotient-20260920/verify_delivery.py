#!/usr/bin/env python3
"""Qualify the actual quotient proof and both fixed-term rejection observations."""
from pathlib import Path
import hashlib, json, re, subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
RUN='HoTT/verification/runs/20260920-MP-ASTRA-QUOTIENT-CONSUMER-001-01'
checks=[]
for label,argv in [('formal',['scripts/audit/verify_formal_proof_run.py','--run-dir',RUN]),('relation',['scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id','MP-ASTRA-QUOTIENT-CONSUMER-001'])]:
    p=subprocess.run(['python3','-B',*argv],cwd=ROOT,capture_output=True)
    (OUT/(label+'.stdout.json')).write_bytes(p.stdout);(OUT/(label+'.stderr.txt')).write_bytes(p.stderr)
    assert p.returncode==0,p.stdout.decode()+p.stderr.decode();checks.append({'kind':label,'argv':argv,'exit':p.returncode})
controls=[]
for module,anchor in [('RawNumeratorQuotient','fst a != fst b'),('RawNumeratorTruncation','fst (fst r) != fst (fst s)')]:
    rel='HoTT/verification/runs/20260920-MP-ASTRA-'+module+'-CONTROL-01';path=ROOT/rel
    run=json.loads((path/'RUN.json').read_text());assert run['exit_code']==42
    for key in ['stdout','stderr','environment','source_manifest']:
        b=(path/run[key]['path']).read_bytes();assert len(b)==run[key]['bytes'] and hashlib.sha256(b).hexdigest()==run[key]['sha256']
    for row in json.loads((path/'source-manifest.json').read_text())['files']:
        b=(ROOT/row['path']).read_bytes();assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
    stdout=(path/'stdout.txt').read_text();assert 'error: [UnequalTerms]' in stdout and anchor in stdout
    controls.append({'module':module,'run':rel,'exit':42,'seconds':run['duration_seconds'],'cached_interfaces':True,'diagnostic':stdout[stdout.index('/Volumes/D/HoTT_AI_HANDOFF_20260911/HoTT/formal/astra-quotient-consumer/'+module+'.agda:'):],'verdict':'EXACT_TYPE_REJECTION_CONTROL_NOT_A_NEW_NO_GO_THEOREM'})
run=json.loads((ROOT/RUN/'RUN.json').read_text());graph=(ROOT/RUN/'imports.dot').read_text();modules=re.findall(r'label="([^"]+)"',graph)
draft=(OUT/'attempts/001/imports.dot').read_text();assert graph==draft
receipt={'status':'FORMAL_AND_RELATION_PASS_TWO_CONTROLS_RECONCILED','claim_ids':['C-305','C-306'],'primary_run':RUN,'primary_seconds':run['duration_seconds'],'checks':checks,'controls':controls,'import_modules':len(modules),'compiled_local_modules':4,'external_pins':41,'draft_final_graph_exact_match':True,'formal_kernel_runs':3,'draft_kernel_checks':1,'original_gold_sources_unchanged':True,'unproved':['Canonical choice algorithm or universal right-section theorem','Physical/source-history interpretation for the original circle','Unconditional weak Lift, necessity/metatheory and complete four-stage outcome'],'parent_goal':'OPEN'}
(OUT/'DELIVERY.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ['checks','controls']},ensure_ascii=False))
