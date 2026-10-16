#!/usr/bin/env python3
"""Verify selected local proof evidence and frozen original/source-contract inputs.

This performs provenance/qualification checks only, not new kernel replay.
"""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
LOGS=OUT/'recheck-002';assert not LOGS.exists();LOGS.mkdir()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
selected=['MP-ASTRA-NATIVE-TASK-INTEGRATION-001','MP-ASTRA-NATIVE-SOURCE-CONTRACT-001','MP-ASTRA-SQRT2-TASK-COMPARISON-001','MP-ASTRA-STANDARD-GOLD-CUT-001','MP-ASTRA-NATIVE-MOTION-BUNDLE-001','MP-ASTRA-WEAK-COVERAGE-MARKOV-001','MP-ASTRA-MARKOV-REVERSE-001','MP-ASTRA-S1-CONSUMER-001','MP-ASTRA-QUOTIENT-CONSUMER-001']
registry=json.loads((ROOT/'HoTT/verification/PROOF_VERSION_CLOSURE.json').read_text());results=[]
for proof in selected:
    row=next(r for r in registry['later_packages'] if r['proof_id']==proof);checks=[]
    for label,args in [('formal',['scripts/audit/verify_formal_proof_run.py','--run-dir',row['run']]),('version',['scripts/audit/verify_proof_version_closure.py','--proof-id',proof])]:
        p=subprocess.run(['python3','-B',*args],cwd=ROOT,capture_output=True)
        (LOGS/(proof+'.'+label+'.stdout.json')).write_bytes(p.stdout);(LOGS/(proof+'.'+label+'.stderr.txt')).write_bytes(p.stderr)
        checks.append({'kind':label,'exit':p.returncode,'argv':args});assert p.returncode==0,p.stdout.decode()+p.stderr.decode()
    results.append({'proof_id':proof,'source':row['source'],'run':row['run'],'release_ref':row['release_ref'],'checks':checks})
raw_inputs=json.loads((ROOT/'audit/astra-case-contract-20260920/SOURCE-INPUTS.json').read_text());matched=[]
for group in ('messages','export_manifests','historical_plan_sources'):
    for row in raw_inputs[group]:
        assert sha(ROOT/row['path'])==row['sha256'];matched.append(row['path'])
additional=json.loads((ROOT/'audit/astra-integration-20260920/ADDITIONAL-PLAN-SOURCES.json').read_text())
# The source owner is an existing immutable audit output, not a new registry.
extra_rows=additional['files']
for row in extra_rows:
    path=row.get('path') or row.get('source');assert path and sha(ROOT/path)==row['sha256'];matched.append(path)
assert len(extra_rows)==3
locator=json.loads((OUT/'LOCATOR-SOURCES.json').read_text())
for row in locator['files']:
    p=ROOT/row['path'];raw=p.read_bytes();assert len(raw)==row['bytes'] and sha(p)==row['sha256']
    assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==row['git_blob_oid']
receipt={'status':'SCOPED_EVIDENCE_QUALIFICATION_AND_SOURCE_IDENTITY_PASS','head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'selected_packages':len(selected),'qualification_checks':2*len(selected),'qualification_output_directory':LOGS.relative_to(ROOT).as_posix(),'results':results,'original_source_rows_matched':matched,'locator_snapshot_files_verified':len(locator['files']),'locator_commit':locator['commit'],'new_agda_kernel_replay':False,'coq_kernel_replay':False,'scope':'Selected current source/run/options/index/version plus exact original text and fixed primary source bytes. Does not prove semantic alignment, all-library coverage or Coq theorem validity.'}
(OUT/'INPUT-VERIFICATION.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in receipt.items() if k not in ('results','original_source_rows_matched')},ensure_ascii=False))
