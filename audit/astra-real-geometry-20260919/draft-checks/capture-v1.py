#!/usr/bin/env python3
"""Actual Lean check with immutable F-011 artifacts and explicit mathlib/runtime pins.

The existing capture_lean_proof_run.py is prelude-only; this topic runner keeps its
format while pinning the real mathlib dependency closure and recorded LEAN_PATH.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import platform
import subprocess

ROOT=Path(__file__).resolve().parents[3]
BASE=Path('/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0')
MATHLIB=BASE/'mathlib4-5ed2965256430c3649e86755f9576b54eca72435'
LEAN=Path('/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0')
AUDIT=ROOT/'audit/astra-real-geometry-20260919'
SOURCE=Path('HoTT/formal/astra-real-geometry/PuncturedCircle.lean')
RUN_ID='20260920-MP-ASTRA-REAL-CIRCLE-001-01'
PROOF_ID='MP-ASTRA-REAL-CIRCLE-001'
CLAIMS=['C-265']

def sha(b):return hashlib.sha256(b).hexdigest()
def jb(x):return (json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
def write(p,b):
    with p.open('xb') as f:f.write(b);f.flush();os.fsync(f.fileno())

def main():
    run=ROOT/'HoTT/verification/runs'/RUN_ID
    assert not run.exists()
    assert Path('/Volumes/D').is_mount()
    assert BASE.stat().st_dev==Path('/Volumes/D').stat().st_dev
    manifest=json.loads((AUDIT/'environment-qualification/cache-manifest-v2.stdout.json').read_text())
    lean_path=(AUDIT/'environment-qualification/LEAN_PATH.txt').read_text().strip()
    library_roots=[Path(p) for p in lean_path.split(os.pathsep)]
    source_roots=[MATHLIB]+[p for p in (MATHLIB/'.lake/packages').iterdir() if p.is_dir()]
    dependencies=set()
    for entry in manifest['entries']:
        rel=Path(*entry['module'].split('.'))
        sources=[p/rel.with_suffix('.lean') for p in source_roots if (p/rel.with_suffix('.lean')).is_file()]
        oleans=[p/rel.with_suffix('.olean') for p in library_roots if (p/rel.with_suffix('.olean')).is_file()]
        assert len(sources)==1 and len(oleans)==1, (entry['module'],sources,oleans)
        dependencies.update(sources)
        # Imported proof/tactic artifacts; trace/hash/ilean are not execution inputs.
        stem=oleans[0].with_suffix('')
        for suffix in ('.olean','.olean.private','.olean.server','.ir'):
            p=Path(str(stem)+suffix)
            if p.is_file():dependencies.add(p)
    # Pin the compiler, shared runtime, and Lean/Std compiled foundations as a superset.
    dependencies.add(LEAN/'bin/lean')
    for p in (LEAN/'lib/lean').rglob('*'):
        if p.is_file() and p.suffix in ('.olean','.private','.server','.ir','.dylib','.so'):
            dependencies.add(p)
    dependencies.update([MATHLIB/'lakefile.lean',MATHLIB/'lake-manifest.json',MATHLIB/'lean-toolchain'])
    external=[]
    for i,p in enumerate(sorted(dependencies)):
        assert not p.is_symlink(),p
        b=p.read_bytes();external.append(dict(label=f'lean-mathlib-input-{i:05d}',local_path=str(p),bytes=len(b),sha256=sha(b)))
    local_paths=[SOURCE,Path(__file__).relative_to(ROOT),Path('audit/astra-real-geometry-20260919/environment-qualification/cache-manifest-v2.stdout.json')]
    rows=[]
    for p in local_paths:
        b=(ROOT/p).read_bytes();rows.append(dict(path=str(p),bytes=len(b),sha256=sha(b)))
    source_manifest=dict(schema_version='formal-proof-source-manifest/v1',proof_id=PROOF_ID,run_id=RUN_ID,
                         files=rows,external_dependencies=external,
                         trust_boundary='Lean 4.34.0 and official mathlib precompiled dependencies; this run checks the new module, not a full source rebuild of mathlib. All execution artifact bytes pinned.')
    argv=['/usr/bin/env','LEAN_PATH='+lean_path,'TMPDIR='+str(BASE/'tmp'),str(LEAN/'bin/lean'),str(SOURCE)]
    started=datetime.datetime.now(datetime.timezone.utc)
    result=subprocess.run(argv,cwd=ROOT,capture_output=True)
    completed=datetime.datetime.now(datetime.timezone.utc)
    version=subprocess.check_output([str(LEAN/'bin/lean'),'--version'],text=True).strip()
    accepted=result.returncode==0 and b'sorryAx' not in result.stdout
    env=('platform='+platform.platform()+'\nlean_version='+version+'\n'
         'dependency_policy=exact mathlib source-derived cache map, imported source/artifact hashes, Lean/Std runtime superset\n'
         'axioms=propext, Classical.choice, Quot.sound; native HoTT and physical trace not claimed\n').encode()
    sm=jb(source_manifest)
    receipt=dict(schema_version='formal-proof-run/v1',run_id=RUN_ID,proof_id=PROOF_ID,claim_ids=CLAIMS,
      proof_assistant='Lean',proof_assistant_version=version,theory_variant='Lean 4 classical dependent type theory with mathlib real point-set topology; no HoTT translation',
      command_argv=argv,cwd=str(ROOT),started_at_utc=started.isoformat(),completed_at_utc=completed.isoformat(),
      duration_seconds=(completed-started).total_seconds(),exit_code=result.returncode,
      status='KERNEL_ACCEPTED_WITH_SCOPE' if accepted else 'KERNEL_REJECTED',
      scope='For every point p of the unit sphere in EuclideanSpace Real (Fin 2), the complement subtype Punctured p has a Homeomorph to Ioo (0:Real) 1. Includes an explicit pole, surjectivity, inverse roundtrip and both continuity statements. Classical Lean/mathlib only.',
      non_goals=['No physical deformation trace or finite operational restoration asserted.','No ambient-homeomorphism, endpoint-preservation, origin-recovery or HoTT inconsistency result asserted.','No faithful translation into native HoTT proved; no independent rebuild of all imported mathlib proofs.'],
      index_status='PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE',git_status='LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED')
    artifacts={'stdout':result.stdout,'stderr':result.stderr,'environment':env,'source_manifest':sm}
    filenames={'stdout':'stdout.txt','stderr':'stderr.txt','environment':'environment.txt','source_manifest':'source-manifest.json'}
    run.mkdir()
    for key,b in artifacts.items():
        write(run/filenames[key],b);receipt[key]=dict(path=filenames[key],bytes=len(b),sha256=sha(b))
    write(run/'RUN.json',jb(receipt))
    print(json.dumps(dict(status=receipt['status'],run_id=RUN_ID,exit_code=result.returncode,external_inputs=len(external),external_bytes=sum(r['bytes'] for r in external)),ensure_ascii=False),flush=True)

if __name__=='__main__':main()
