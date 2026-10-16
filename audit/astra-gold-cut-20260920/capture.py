#!/usr/bin/env python3
"""Fresh native Cubical check of standard cut packing and exact GOLD queries."""
from pathlib import Path
import datetime,importlib.util,json,platform,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('C',ROOT/'scripts/audit/capture_agda_proof_run.py');C=importlib.util.module_from_spec(sp);sp.loader.exec_module(C)
PROOF='MP-ASTRA-STANDARD-GOLD-CUT-001';RUN='20260920-'+PROOF+'-01'
dest=ROOT/'HoTT/verification/runs'/RUN;assert not dest.exists()
base='HoTT/formal/dedekind-omega-missile/'
source=base+'Sqrt2CutQueries.agda';config=base+'TOOLCHAIN.json'
cfg=json.loads((ROOT/config).read_text());a=cfg['agda'];lib=cfg['cubical_library'];cache=cfg['runtime_cache']
inputs=[base+n+'.agda' for n in ['Sqrt2CutQueries','Sqrt2CutBridge','StandardDedekind','CutRealLayer','CutGoldForm','CutInfra','MissileTwoUniversalIrrationality','MissileThreeUnconditional','MissileThreeVerdictCollision']]+[config,cfg['project_library_registry'],'HoTT/theory-schema/upstream/book-578b85cc/reals.tex','HoTT/theory-schema/upstream/book-578b85cc/logic.tex','audit/astra-gold-cut-20260920/capture.py','scripts/audit/capture_agda_proof_run.py']
files=[dict(C.file_row(ROOT/p),path=p) for p in inputs]
pins=[(a['local_binary'],a['binary_bytes'],a['binary_sha256'],'agda-binary'),(a['local_archive'],a['asset_bytes'],a['asset_sha256'],'agda-release-asset'),(lib['local_archive'],lib['asset_bytes'],lib['asset_sha256'],'cubical-release-asset'),(lib['library_file'],lib['library_file_bytes'],lib['library_file_sha256'],'cubical-library-file')]
external=[]
for p,bs,hs,label in pins:C.expect_file(Path(p),bs,hs,label);external.append(C.file_row(Path(p),label=label))
tree=C.deterministic_tree(Path(lib['local_root']));assert tree=={'file_count':lib['tree_file_count'],'total_bytes':lib['tree_total_bytes'],'tree_sha256':lib['tree_sha256']}
external.append(dict(label='cubical-extracted-tree',local_path=lib['local_root'],**tree))
prim=Path(cache['xdg_data_home'])/'agda'/a['version']/'lib/prim'
for p in sorted(prim.rglob('*.agda')):external.append(C.file_row(p,label='agda-runtime-source:'+p.relative_to(prim).as_posix()))
graph=OUT/'formal-imports.dot'
argv=['/usr/bin/env','XDG_DATA_HOME='+cache['xdg_data_home'],'XDG_CONFIG_HOME='+cache['xdg_config_home'],'TMPDIR='+cache['tmpdir'],a['local_binary'],'--ignore-interfaces','--library-file='+str(ROOT/cfg['project_library_registry']),'-l','cubical-0.9','-i',str(ROOT/base),'--dependency-graph='+str(graph),source]
version=subprocess.run(argv[:5]+['--version'],cwd=ROOT,capture_output=True,check=True).stdout.decode().strip()
start=datetime.datetime.now(datetime.timezone.utc);print('RUN',RUN,flush=True);p=subprocess.run(argv,cwd=ROOT,capture_output=True);end=datetime.datetime.now(datetime.timezone.utc)
assert all(C.sha((ROOT/f['path']).read_bytes())==f['sha256'] for f in files);assert C.deterministic_tree(Path(lib['local_root']))==tree
assert all(C.file_row(Path(row['local_path']),label=row['label'])==row for row in external if row['label']!='cubical-extracted-tree')
manifest={'schema_version':'formal-proof-source-manifest/v1','proof_id':PROOF,'run_id':RUN,'files':files,'external_dependencies':external}
env=('platform='+platform.platform()+'\nagda='+version.replace('\n',' | ')+'\ntheory_variant=Cubical Agda, safe/cubical/guardedness; main and legacy bridge explicitly two-level\nlibrary_commit='+lib['tag_commit']+'\nlibrary_tree_sha256='+tree['tree_sha256']+'\nno_added_LEM_resizing_or_SingleOmega_inputs\nruntime_builtin_sources=individually pinned; interfaces ignored\n').encode()
blobs={'stdout.txt':p.stdout,'stderr.txt':p.stderr,'environment.txt':env,'source-manifest.json':C.json_bytes(manifest)}
def entry(n):return {'path':n,'bytes':len(blobs[n]),'sha256':C.sha(blobs[n])}
run={'schema_version':'formal-proof-run/v1','run_id':RUN,'proof_id':PROOF,'claim_ids':['C-297','C-298','C-299'],'proof_assistant':'Cubical Agda','proof_assistant_version':version,'theory_variant':'cubical','command_argv':argv,'cwd':str(ROOT),'started_at_utc':start.isoformat(),'completed_at_utc':end.isoformat(),'duration_seconds':(end-start).total_seconds(),'exit_code':p.returncode,'status':'KERNEL_ACCEPTED_WITH_SCOPE' if p.returncode==0 else 'KERNEL_REJECTED','scope':'Standard truncated Dedekind predicate at arbitrary level, proposition/set proofs, explicit equivalence to literal Book identity roundedness and corrected legacy dcut. Unchanged GOLD L/U packed as actual standard and legacy real-carrier elements at Type1 without LEM/resizing/SingleOmega inputs. Exact L/U decisions for all rationals; q=-3 computes true for lower-cut query but false for the actual old M3 square table. Untruncated located output at(1,2) is not a proposition; exact rational-root output remains empty.','non_goals':['No real-ring x^2=2 equation or completeness theorem is added; actual predicates and carrier membership are proved.','No same-level small-real representation, SingleOmega necessity/refutation, global resizing result, all-cut computability or physical process claim.','No all-precision approximation proof in this unit, no circle-to-arithmetic faithful reduction, full four-stage closure or HoTT contradiction.'],'stdout':entry('stdout.txt'),'stderr':entry('stderr.txt'),'environment':entry('environment.txt'),'source_manifest':entry('source-manifest.json'),'index_status':'PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE','git_status':'LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED'}
dest.mkdir(parents=True)
for n,data in blobs.items():C.exclusive_write(dest/n,data)
C.exclusive_write(dest/'RUN.json',C.json_bytes(run))
if p.returncode==0:
 assert graph.exists() and b'Sqrt2CutQueries' in graph.read_bytes();C.exclusive_write(dest/'imports.dot',graph.read_bytes())
print(json.dumps({'run':str(dest.relative_to(ROOT)),'exit':p.returncode,'seconds':run['duration_seconds'],'external_dependencies':len(external)}),flush=True)
if p.returncode:print(p.stdout.decode()[-5000:]+p.stderr.decode());raise SystemExit(1)
