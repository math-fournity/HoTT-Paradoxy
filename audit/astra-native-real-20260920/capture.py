#!/usr/bin/env python3
"""Capture this dependency qualification with explicit primitive/runtime pins.

Reuse the project's formal-proof-run/v1 serialization and checks. A successful
diagnostic run certifies acceptance in the declared extended configuration only.
"""
from pathlib import Path
import argparse,datetime,importlib.util,json,platform,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('capture',ROOT/'scripts/audit/capture_agda_unimath_replay_run.py')
C=importlib.util.module_from_spec(sp);sp.loader.exec_module(C)
ap=argparse.ArgumentParser();ap.add_argument('--module',required=True);ap.add_argument('--run-id',required=True);ap.add_argument('--proof-id',required=True);ap.add_argument('--claim-id',required=True);ap.add_argument('--variant',choices=['original','restricted'],required=True);ap.add_argument('--expected-exit',type=int,default=0);args=ap.parse_args()
relative='HoTT/verification/runs/'+args.run_id;dest=ROOT/relative
assert not dest.exists()
config='HoTT/formal/agda-unimath/'+('UNIMATH_TOOLCHAIN.json' if args.variant=='original' else 'no-erasure/TOOLCHAIN.json')
cfg=json.loads((ROOT/config).read_text());a=cfg['agda'];lib=cfg['agda_unimath_library'];cache=cfg['runtime_cache']
source='HoTT/formal/agda-unimath/hott-z/'+args.module+'.agda'
inputs=[source,config,cfg['project_library_registry'],'audit/astra-native-real-20260920/capture.py','scripts/audit/capture_agda_unimath_replay_run.py']
if args.variant=='restricted':inputs+=['HoTT/formal/agda-unimath/no-erasure/identity-replacement.patch','audit/astra-native-real-20260920/prepare_restricted_library.py']
files=[]
for p in inputs:files.append(dict(C.file_row(ROOT/p),path=p))
for path,bs,hs,label in [(a['local_binary'],a['binary_bytes'],a['binary_sha256'],'agda-binary'),(a['local_archive'],a['asset_bytes'],a['asset_sha256'],'agda-release-asset'),(lib['local_archive'],lib['archive_bytes'],lib['archive_sha256'],'parent-unimath-archive'),(lib['library_file'],lib['library_file_bytes'],lib['library_file_sha256'],'agda-unimath-library-file')]:C.expect_file(Path(path),bs,hs,label)
tree=C.deterministic_tree(Path(lib['local_root']))
assert tree=={'file_count':lib['tree_file_count'],'total_bytes':lib['tree_total_bytes'],'tree_sha256':lib['tree_sha256']}
external=[C.file_row(Path(p),label=l) for p,l in [(a['local_binary'],'agda-binary'),(a['local_archive'],'agda-release-asset'),(lib['local_archive'],'parent-unimath-archive'),(lib['library_file'],'agda-unimath-library-file')]]
external.append(dict(label='agda-unimath-extracted-tree',local_path=lib['local_root'],**tree))
prim=Path(cache['xdg_data_home'])/'agda'/a['version']/'lib/prim'
for p in sorted(prim.rglob('*.agda')):external.append(C.file_row(p,label='agda-runtime-source:'+p.relative_to(prim).as_posix()))
command=['/usr/bin/env','XDG_DATA_HOME='+cache['xdg_data_home'],'XDG_CONFIG_HOME='+cache['xdg_config_home'],'TMPDIR='+cache['tmpdir'],a['local_binary'],'--ignore-interfaces','--library-file='+str(ROOT/cfg['project_library_registry']),'-l',lib['name'],'-i',str(ROOT/'HoTT/formal/agda-unimath'),'--dependency-graph='+str(OUT/(args.run_id+'.dot')),source]
version=subprocess.run(command[:5]+['--version'],cwd=ROOT,capture_output=True,check=True).stdout.decode()
start=datetime.datetime.now(datetime.timezone.utc)
print('RUN',args.run_id,flush=True)
p=subprocess.run(command,cwd=ROOT,capture_output=True)
end=datetime.datetime.now(datetime.timezone.utc)
assert all(C.sha((ROOT/f['path']).read_bytes())==f['sha256'] for f in files)
assert C.deterministic_tree(Path(lib['local_root']))==tree
assert all(C.file_row(Path(row['local_path']),label=row['label'])==row for row in external if row['label']!='agda-unimath-extracted-tree')
theory=('Agda without-K + agda-unimath univalence + primEraseEquality EXTRA reduction: configuration diagnostic, NOT ordinary HoTT' if args.variant=='original' else cfg['theory_variant'])
scope={'ErasureConfigurationDiagnostic':'Exact source derives universal loopRefl and configurationEmpty using the extra primEraseEquality reduction and imported library univalence. This is a diagnostic of this extended configuration, not HoTT alone.','NativeRealCircleQualification':'Actual ℝ lzero Dedekind real plane, product metric, equation-defined unit circle, east/north and north≠east, punctured nonempty metric subspace, and inhabited strict open interval. No circle/interval homeomorphism or Lean-to-HoTT translation is asserted.','NoCanonicalPoint':'Same historical derived NoCanonicalPoint source replayed against the local identity-preserving derivative; inherited foundation postulates remain. This removes the observed erasure rule for this check, not every possible source of inconsistency.'}[args.module]
manifest={'schema_version':'formal-proof-source-manifest/v1','proof_id':args.proof_id,'run_id':args.run_id,'files':files,'external_dependencies':external}
mb=C.json_bytes(manifest)
environment=('platform='+platform.platform()+'\nagda='+version.replace('\n',' | ')+'\ntheory_variant='+theory+'\nlibrary_parent_commit='+lib['commit_sha']+'\nactual_tree_sha256='+tree['tree_sha256']+'\nvariant='+args.variant+'\nupstream_archive_role=parent; actual derivative defined by exact patch when restricted\nprimitive_sources=pinned individually; no interfaces trusted (--ignore-interfaces)\n').encode()
blobs={'stdout.txt':p.stdout,'stderr.txt':p.stderr,'environment.txt':environment,'source-manifest.json':mb}
def entry(name):return {'path':name,'bytes':len(blobs[name]),'sha256':C.sha(blobs[name])}
run={'schema_version':'formal-proof-run/v1','run_id':args.run_id,'proof_id':args.proof_id,'claim_ids':[args.claim_id],'proof_assistant':'Agda (agda-unimath)','proof_assistant_version':version.strip(),'theory_variant':theory,'command_argv':command,'cwd':str(ROOT),'started_at_utc':start.isoformat(),'completed_at_utc':end.isoformat(),'duration_seconds':(end-start).total_seconds(),'exit_code':p.returncode,'status':'KERNEL_ACCEPTED_WITH_SCOPE' if p.returncode==0 else 'KERNEL_REJECTED','scope':scope,'non_goals':['No ordinary HoTT inconsistency claim.','No global soundness certification of Agda, all library postulates, or the derivative.','No complete four-stage redo, physical realization, or general faithful translation claim.'],'stdout':entry('stdout.txt'),'stderr':entry('stderr.txt'),'environment':entry('environment.txt'),'source_manifest':entry('source-manifest.json'),'index_status':'PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE','git_status':'LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED','expected_exit_for_control':args.expected_exit}
dest.mkdir(parents=True)
for name,raw in blobs.items():C.exclusive_write(dest/name,raw)
C.exclusive_write(dest/'RUN.json',C.json_bytes(run))
graph=OUT/(args.run_id+'.dot')
if graph.exists():C.exclusive_write(dest/'imports.dot',graph.read_bytes())
print(json.dumps({'run':relative,'exit':p.returncode,'expected':args.expected_exit,'seconds':run['duration_seconds'],'external_count':len(external)}),flush=True)
if p.returncode!=args.expected_exit:print(p.stdout.decode()[-6000:]+p.stderr.decode());raise SystemExit(1)
