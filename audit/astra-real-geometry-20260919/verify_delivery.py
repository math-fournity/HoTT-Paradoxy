#!/usr/bin/env python3
"""Dual local checks plus compiler-binding negative controls on isolated copies."""
from pathlib import Path
import copy
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'scripts/audit'))
import verify_proof_version_closure as V

RUN='HoTT/verification/runs/20260920-MP-ASTRA-REAL-CIRCLE-001-02'
PROOF='MP-ASTRA-REAL-CIRCLE-001'
checks=[]
for label,argv in [
 ('formal',['python3','scripts/audit/verify_formal_proof_run.py','--run-dir',RUN,'--rerun']),
 ('relation',['python3','scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id',PROOF]),
 ('regression',['python3','-m','unittest','discover','-s','scripts/audit','-p','test_proof_*py'])]:
 r=subprocess.run(argv,cwd=ROOT,capture_output=True)
 (OUT/(label+'.stdout.txt')).write_bytes(r.stdout);(OUT/(label+'.stderr.txt')).write_bytes(r.stderr)
 checks.append(dict(name=label,argv=argv,exit=r.returncode))
 print(label,r.returncode,flush=True)
 assert r.returncode==0, r.stderr.decode()[:500]

registry=json.loads((ROOT/'HoTT/verification/PROOF_VERSION_CLOSURE.json').read_text())
row=next(p for p in registry['later_packages'] if p['proof_id']==PROOF)
original=json.loads((ROOT/RUN/'RUN.json').read_text())
manifest=json.loads((ROOT/RUN/'source-manifest.json').read_text())
controls=[]
with tempfile.TemporaryDirectory(prefix='lean-binding-',dir='/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/tmp') as temporary:
 fixture=Path(temporary)
 for item in manifest['files']:
  dest=fixture/item['path'];dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/item['path'],dest)
 shutil.copytree(ROOT/RUN,fixture/RUN)
 dest=fixture/'HoTT/CLAIM_EVIDENCE_MATRIX.md';dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md',dest)
 oldroot=V.ROOT;V.ROOT=fixture
 try:
  for case in ['wrong-binary','wrong-assistant','unpinned-binary']:
   receipt=copy.deepcopy(original);mf=copy.deepcopy(manifest)
   binary='/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean'
   if case=='wrong-binary':receipt['command_argv']=[('/usr/bin/true' if x==binary else x) for x in receipt['command_argv']]
   if case=='wrong-assistant':receipt['proof_assistant']='Unrelated'
   if case=='unpinned-binary':mf['external_dependencies']=[x for x in mf['external_dependencies'] if x['local_path']!=binary]
   payload=(json.dumps(mf,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
   (fixture/RUN/'source-manifest.json').write_bytes(payload)
   receipt['source_manifest'].update(bytes=len(payload),sha256=hashlib.sha256(payload).hexdigest())
   (fixture/RUN/'RUN.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
   try:V.check_later_package(fixture/RUN,row,{},V.matrix_identity_lines(dest.read_bytes()))
   except V.ClosureError as error:
    expected='LATER_LEAN_BINARY_NOT_PINNED' if case=='unpinned-binary' else 'LATER_COMMAND_TOOL_MISMATCH'
    assert str(error).startswith(expected),(case,str(error))
    controls.append(dict(case=case,status='REJECTED_AS_EXPECTED',error=str(error)))
   else:raise AssertionError('incorrect acceptance: '+case)
 finally:V.ROOT=oldroot
(OUT/'DELIVERY.json').write_text(json.dumps(dict(status='DUAL_LOCAL_PASS',checks=checks,negative_controls=controls,scope='C-265 only; classical Lean geometry; full goal remains active'),ensure_ascii=False,indent=2)+'\n')
print('DUAL_LOCAL_PASS; 3 compiler-binding negative controls rejected',flush=True)
