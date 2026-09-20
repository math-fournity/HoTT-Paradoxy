#!/usr/bin/env python3
"""Capture the actual intrinsic rich-curve and finite ambient-task proofs."""
from pathlib import Path
import datetime,importlib.util,json,platform,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('capture',ROOT/'scripts/audit/capture_agda_unimath_replay_run.py');C=importlib.util.module_from_spec(sp);sp.loader.exec_module(C)
PROOF='MP-ASTRA-NATIVE-RICH-TASK-001';RUN='20260920-'+PROOF+'-01'
dest=ROOT/'HoTT/verification/runs'/RUN;assert not dest.exists()
source='HoTT/formal/agda-unimath/hott-z/NativeCurveTask.agda'
config='HoTT/formal/agda-unimath/no-erasure/TOOLCHAIN.json'
cfg=json.loads((ROOT/config).read_text());a=cfg['agda'];lib=cfg['agda_unimath_library'];cache=cfg['runtime_cache']
inputs=[source]+['HoTT/formal/agda-unimath/hott-z/'+n+'.agda' for n in ['NativeRichCurve','FiniteTrace','NativeCompletion','HomogeneousCircle','NativeOpenInterval','SignedIntervalHomeomorphism','StereographicContinuity','ReciprocalContinuity','NativeStereographic','PunctureApartness','NativeRealCircleQualification']]+[config,cfg['project_library_registry'],'HoTT/formal/agda-unimath/no-erasure/identity-replacement.patch','audit/astra-native-real-20260920/prepare_restricted_library.py','audit/astra-rich-task-20260920/capture.py','scripts/audit/capture_agda_unimath_replay_run.py']
files=[dict(C.file_row(ROOT/p),path=p) for p in inputs]
pins=[(a['local_binary'],a['binary_bytes'],a['binary_sha256'],'agda-binary'),(a['local_archive'],a['asset_bytes'],a['asset_sha256'],'agda-release-asset'),(lib['local_archive'],lib['archive_bytes'],lib['archive_sha256'],'parent-unimath-archive'),(lib['library_file'],lib['library_file_bytes'],lib['library_file_sha256'],'agda-unimath-library-file')]
external=[]
for p,bs,hs,label in pins:C.expect_file(Path(p),bs,hs,label);external.append(C.file_row(Path(p),label=label))
tree=C.deterministic_tree(Path(lib['local_root']));assert tree=={'file_count':lib['tree_file_count'],'total_bytes':lib['tree_total_bytes'],'tree_sha256':lib['tree_sha256']}
external.append(dict(label='agda-unimath-extracted-tree',local_path=lib['local_root'],**tree))
prim=Path(cache['xdg_data_home'])/'agda'/a['version']/'lib/prim'
for p in sorted(prim.rglob('*.agda')):external.append(C.file_row(p,label='agda-runtime-source:'+p.relative_to(prim).as_posix()))
argv=['/usr/bin/env','XDG_DATA_HOME='+cache['xdg_data_home'],'XDG_CONFIG_HOME='+cache['xdg_config_home'],'TMPDIR='+cache['tmpdir'],a['local_binary'],'--ignore-interfaces','--library-file='+str(ROOT/cfg['project_library_registry']),'-l',lib['name'],'-i',str(ROOT/'HoTT/formal/agda-unimath'),'--dependency-graph='+str(OUT/'formal-imports.dot'),source]
version=subprocess.run(argv[:5]+['--version'],cwd=ROOT,capture_output=True,check=True).stdout.decode().strip()
start=datetime.datetime.now(datetime.timezone.utc);print('RUN',RUN,flush=True);p=subprocess.run(argv,cwd=ROOT,capture_output=True);end=datetime.datetime.now(datetime.timezone.utc)
assert all(C.sha((ROOT/f['path']).read_bytes())==f['sha256'] for f in files);assert C.deterministic_tree(Path(lib['local_root']))==tree
assert all(C.file_row(Path(row['local_path']),label=row['label'])==row for row in external if row['label']!='agda-unimath-extracted-tree')
manifest={'schema_version':'formal-proof-source-manifest/v1','proof_id':PROOF,'run_id':RUN,'files':files,'external_dependencies':external}
env=('platform='+platform.platform()+'\nagda='+version.replace('\n',' | ')+'\ntheory_variant='+cfg['theory_variant']+'\nlibrary_parent_commit='+lib['commit_sha']+'\nactual_tree_sha256='+tree['tree_sha256']+'\noriginal_archive_role=parent; two-file derivative pinned separately\nprimitive_sources=individually pinned; interfaces ignored\n').encode()
blobs={'stdout.txt':p.stdout,'stderr.txt':p.stderr,'environment.txt':env,'source-manifest.json':C.json_bytes(manifest)}
def entry(n):return {'path':n,'bytes':len(blobs[n]),'sha256':C.sha(blobs[n])}
run={'schema_version':'formal-proof-run/v1','run_id':RUN,'proof_id':PROOF,'claim_ids':['C-293','C-294'],'proof_assistant':'Agda (agda-unimath)','proof_assistant_version':version,'theory_variant':cfg['theory_variant'],'command_argv':argv,'cwd':str(ROOT),'started_at_utc':start.isoformat(),'completed_at_utc':end.isoformat(),'duration_seconds':(end-start).total_seconds(),'exit_code':p.returncode,'status':'KERNEL_ACCEPTED_WITH_SCOPE' if p.returncode==0 else 'KERNEL_REJECTED','scope':'C293: actual intrinsic StrongPuncture and original interval with parametrization, realization, continuous closed diagram and interior agreement; bare univalent path but no selected Rich path/lift/recovery; full-field transport retains actual boundary. C294: explicit ambient plane homeomorphism steps with commuting closed diagrams, finite traces/composition/Done/success; no finite M-to-N or N-to-M trace in that model; actual nontrivial coordinate-swap success and bare representation trace; no universal lift from bare traces to ambient traces.','non_goals':['Not every physical or user-permitted restoration process; the Step model is explicit and does not identify all curve deformations with ambient homeomorphisms.','Not a HoTT contradiction, unconditional weak Lift, complete Task Input/Denotes contract, GOLD integration or complete four-stage redo.','Transported M structure on the interval differs from the preselected straight N; no claim that univalence discards all data.'],'stdout':entry('stdout.txt'),'stderr':entry('stderr.txt'),'environment':entry('environment.txt'),'source_manifest':entry('source-manifest.json'),'index_status':'PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE','git_status':'LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED'}
dest.mkdir(parents=True)
for n,data in blobs.items():C.exclusive_write(dest/n,data)
C.exclusive_write(dest/'RUN.json',C.json_bytes(run))
if (OUT/'formal-imports.dot').exists():C.exclusive_write(dest/'imports.dot',(OUT/'formal-imports.dot').read_bytes())
print(json.dumps({'run':str(dest.relative_to(ROOT)),'exit':p.returncode,'seconds':run['duration_seconds'],'external_dependencies':len(external)}),flush=True)
if p.returncode:print(p.stdout.decode()[-5000:]+p.stderr.decode());raise SystemExit(1)
