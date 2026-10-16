#!/usr/bin/env python3
"""Capture the concrete ambient-geometry proof with the explicit Lean -t 0 option."""
from pathlib import Path
import datetime,hashlib,json,os,platform,subprocess,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'scripts/audit'))
from capture_lean_proof_run import json_bytes,source_row,exclusive_write,sha

RUN_ID=sys.argv[1] if len(sys.argv)>1 else '20260920-MP-ASTRA-AMBIENT-CIRCLE-001-01'
assert RUN_ID.startswith('20260920-MP-ASTRA-AMBIENT-CIRCLE-001-') and '/' not in RUN_ID
PROOF='MP-ASTRA-AMBIENT-CIRCLE-001'
SOURCE='HoTT/formal/astra-real-geometry/AmbientCircle.lean'
BASE=Path('/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0')
LEAN=Path('/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean')
OUT=ROOT/'audit/astra-ambient-geometry-20260920'

def main():
    run=ROOT/'HoTT/verification/runs'/RUN_ID
    assert not run.exists()
    parent=ROOT/'HoTT/verification/runs/20260920-MP-ASTRA-REAL-CIRCLE-001-02/source-manifest.json'
    external=json.loads(parent.read_text())['external_dependencies']
    for row in external:
        p=Path(row['local_path']);b=p.read_bytes()
        assert not p.is_symlink() and len(b)==row['bytes'] and sha(b)==row['sha256'],p
    prior=ROOT/'HoTT/formal/astra-real-geometry/PuncturedCircle.lean'
    assert (BASE/'project-build/PuncturedCircle.source.sha256').read_text()==sha(prior.read_bytes())
    p=BASE/'project-build/PuncturedCircle.olean';b=p.read_bytes()
    external.append({'label':'local-punctured-circle-import','local_path':str(p),'bytes':len(b),'sha256':sha(b)})
    paths=[SOURCE,'HoTT/formal/astra-real-geometry/PuncturedCircle.lean',
      'HoTT/formal/astra-real-geometry/AMBIENT-TOOLCHAIN.json',
      'HoTT/formal/astra-real-geometry/TOOLCHAIN.json',str(Path(__file__).relative_to(ROOT)),
      'scripts/audit/capture_lean_proof_run.py']
    rows=[source_row(ROOT,Path(p)) for p in paths]
    manifest=json_bytes(dict(schema_version='formal-proof-source-manifest/v1',proof_id=PROOF,run_id=RUN_ID,
      files=rows,external_dependencies=external,parent_manifest_sha256=sha(parent.read_bytes()),
      policy='All selected library/runtime inputs rehashed; local imported source and artifact pinned; Lean invoked with -t 0. No claim of independent lean4checker --fresh replay or full dependency-source rebuild.'))
    lp=str(BASE/'project-build')+os.pathsep+(ROOT/'audit/astra-real-geometry-20260919/environment-qualification/LEAN_PATH.txt').read_text().strip()
    argv=['/usr/bin/env','LEAN_PATH='+lp,'TMPDIR='+str(BASE/'tmp'),str(LEAN),
          '-t','0','-j','4','-M','8192','-R',str(ROOT/'HoTT/formal/astra-real-geometry'),SOURCE]
    start=datetime.datetime.now(datetime.timezone.utc)
    p=subprocess.Popen(argv,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    (OUT/'CAPTURE-PROCESS.json').write_text(json.dumps({'pid':p.pid,'argv':argv,'started':start.isoformat()},indent=2)+'\n')
    print(json.dumps({'status':'RUNNING','pid':p.pid,'trust_level':0}),flush=True)
    stdout,stderr=p.communicate();end=datetime.datetime.now(datetime.timezone.utc)
    version=subprocess.check_output([str(LEAN),'--version'],text=True).strip()
    environment=('platform='+platform.platform()+'\nlean='+version+'\ntrust_level=0\nthreads=4\nmemory_limit_MB=8192\naxioms=propext, Classical.choice, Quot.sound\n').encode()
    accepted=p.returncode==0 and b'sorryAx' not in stdout
    receipt=dict(schema_version='formal-proof-run/v1',run_id=RUN_ID,proof_id=PROOF,claim_ids=['C-266','C-267','C-268'],
      proof_assistant='Lean',proof_assistant_version=version,theory_variant='Lean classical real point-set topology, invoked with -t 0; pinned compiled imports, no independent all-import replay or native HoTT translation',
      command_argv=argv,cwd=str(ROOT),started_at_utc=start.isoformat(),completed_at_utc=end.isoformat(),
      duration_seconds=(end-start).total_seconds(),exit_code=p.returncode,
      status='KERNEL_ACCEPTED_WITH_SCOPE' if accepted else 'KERNEL_REJECTED',
      scope='Concrete embedded punctured unit circle M and straight open segment N in the same Euclidean real plane: closure-minus-set is respectively one point and two distinct points; subspaces intrinsically homeomorphic; no global plane homeomorphism maps either to the other; no finite list of such ambient homeomorphisms reconstructs M from N.',
      non_goals=['No all-physical-process impossibility.','No restriction imposed on alternative cutting/adding/re-embedding constructions.','No HoTT contradiction or faithful native HoTT translation.'],
      index_status='PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE',git_status='LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED')
    run.mkdir()
    for key,name,data in [('stdout','stdout.txt',stdout),('stderr','stderr.txt',stderr),('environment','environment.txt',environment),('source_manifest','source-manifest.json',manifest)]:
        exclusive_write(run/name,data);receipt[key]={'path':name,'bytes':len(data),'sha256':sha(data)}
    exclusive_write(run/'RUN.json',json_bytes(receipt))
    print(json.dumps({'status':receipt['status'],'exit_code':p.returncode,'duration_seconds':receipt['duration_seconds'],'stdout':stdout.decode()[:2200],'stderr':stderr.decode()[:1000]},ensure_ascii=False),flush=True)

if __name__=='__main__':main()
