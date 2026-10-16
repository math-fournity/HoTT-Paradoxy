#!/usr/bin/env python3
"""Capture the same-Pell arithmetic comparison alongside the accepted curve theorem."""
from pathlib import Path
import datetime,json,os,platform,subprocess,sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'scripts/audit'))
from capture_lean_proof_run import json_bytes,source_row,exclusive_write,sha
RUN_ID=sys.argv[1] if len(sys.argv)>1 else '20260920-MP-ASTRA-PELL-CURVE-COMPARISON-001-01'
assert RUN_ID.startswith('20260920-MP-ASTRA-PELL-CURVE-COMPARISON-001-') and '/' not in RUN_ID
PROOF='MP-ASTRA-PELL-CURVE-COMPARISON-001'
SOURCE='HoTT/formal/astra-real-geometry/PellCurveComparison.lean'
BASE=Path('/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0')
LEAN=Path('/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean')
OUT=ROOT/'audit/astra-endpoint-closure-20260920/lean-comparison'

def main():
 check=json.loads((OUT/'CHECK.json').read_text())
 assert check['exit']==0 and check['source_sha256']==sha((ROOT/SOURCE).read_bytes()), 'Latest exact-source draft must pass before formal capture'
 run=ROOT/'HoTT/verification/runs'/RUN_ID
 assert not run.exists()
 parent=ROOT/'HoTT/verification/runs/20260920-MP-ASTRA-CURVE-DEFORMATION-001-02/source-manifest.json'
 external=json.loads(parent.read_text())['external_dependencies']
 for row in external:
  p=Path(row['local_path']);b=p.read_bytes()
  assert not p.is_symlink() and len(b)==row['bytes'] and sha(b)==row['sha256'],p
 for name in ['PuncturedCircle','AmbientCircle','DeformationCircle']:
  source=ROOT/'HoTT/formal/astra-real-geometry'/(name+'.lean')
  assert (BASE/'project-build'/(name+'.source.sha256')).read_text()==sha(source.read_bytes())
 p=BASE/'project-build/DeformationCircle.olean';b=p.read_bytes()
 external.append({'label':'local-deformation-circle-import','local_path':str(p),'bytes':len(b),'sha256':sha(b)})
 paths=[SOURCE,*['HoTT/formal/astra-real-geometry/'+n for n in ['PuncturedCircle.lean','AmbientCircle.lean','DeformationCircle.lean','TOOLCHAIN.json','AMBIENT-TOOLCHAIN.json','DEFORMATION-TOOLCHAIN.json','COMPARISON-TOOLCHAIN.json','capture_comparison.py']],'scripts/audit/capture_lean_proof_run.py']
 manifest=json_bytes(dict(schema_version='formal-proof-source-manifest/v1',proof_id=PROOF,run_id=RUN_ID,
  files=[source_row(ROOT,Path(p)) for p in paths],external_dependencies=external,parent_manifest_sha256=sha(parent.read_bytes()),
  policy='Pinned classical Lean/mathlib inputs and three local imports. No independent all-import replay or native HoTT translation claimed.'))
 lp=str(BASE/'project-build')+os.pathsep+(ROOT/'audit/astra-real-geometry-20260919/environment-qualification/LEAN_PATH.txt').read_text().strip()
 argv=['/usr/bin/env','LEAN_PATH='+lp,'TMPDIR='+str(BASE/'tmp'),str(LEAN),'-t','0','-j','4','-M','8192','-R',str(ROOT/'HoTT/formal/astra-real-geometry'),SOURCE]
 start=datetime.datetime.now(datetime.timezone.utc)
 p=subprocess.Popen(argv,cwd=ROOT,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 print(json.dumps({'status':'RUNNING','pid':p.pid}),flush=True)
 stdout,stderr=p.communicate();end=datetime.datetime.now(datetime.timezone.utc)
 version=subprocess.check_output([str(LEAN),'--version'],text=True).strip()
 accepted=p.returncode==0 and b'sorryAx' not in stdout
 environment=('platform='+platform.platform()+'\nlean='+version+'\ntrust_level=0\nthreads=4\nmemory_limit_MB=8192\naxioms=propext, Classical.choice, Quot.sound\n').encode()
 receipt=dict(schema_version='formal-proof-run/v1',run_id=RUN_ID,proof_id=PROOF,claim_ids=['C-274'],proof_assistant='Lean',proof_assistant_version=version,
  theory_variant='Lean integer Pell recurrence plus the established classical real curve theorem; no general cross-kernel translation',
  command_argv=argv,cwd=str(ROOT),started_at_utc=start.isoformat(),completed_at_utc=end.isoformat(),duration_seconds=(end-start).total_seconds(),exit_code=p.returncode,
  status='KERNEL_ACCEPTED_WITH_SCOPE' if accepted else 'KERNEL_REJECTED',
  scope='Same initial pair(1,1) and recurrence(p+2q,p+q) as Agda M1: the integer discriminant is always plus or minus one and never zero. Lean also accepts the conjunction of this universal nonzero result with the existing continuous embedding deformation from N to M.',
  non_goals=['No ambient-homeomorphism extension.','No length, speed, material or universal physical implementation claim.','No native HoTT translation or inconsistency.'],index_status='PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE',git_status='LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED')
 run.mkdir()
 for key,name,data in [('stdout','stdout.txt',stdout),('stderr','stderr.txt',stderr),('environment','environment.txt',environment),('source_manifest','source-manifest.json',manifest)]:
  exclusive_write(run/name,data);receipt[key]={'path':name,'bytes':len(data),'sha256':sha(data)}
 exclusive_write(run/'RUN.json',json_bytes(receipt))
 print(json.dumps({'status':receipt['status'],'exit':p.returncode,'duration':receipt['duration_seconds'],'stdout':stdout.decode(),'stderr':stderr.decode()},ensure_ascii=False),flush=True)

if __name__=='__main__':main()
