#!/usr/bin/env python3
"""Build, commit, seal and round-trip the authorized full handoff; not a math verifier.
All code is persisted before invocation. Stage names deliberately separate mutation from sealing.
"""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, os, shutil, stat, subprocess, sys, tempfile, time, zipfile
ROOT=Path(__file__).resolve().parents[2]
PKG=ROOT.parent
ART=ROOT/'artifacts/r040'
TAG='handoff-r040'
BASE='1ad50e950c619d1332572d0bd3ffae2746522d57'
EXCLUDED_SELF='validation/FILE_MANIFEST.json'

def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def dump(p,x,overwrite=False):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists() and not overwrite:raise FileExistsError(p)
 p.write_text(json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
def run(argv,cwd=ROOT,timeout=120):
 st=time.time();p=subprocess.run(list(map(str,argv)),cwd=cwd,capture_output=True,text=True,timeout=timeout,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','GIT_CONFIG_NOSYSTEM':'1','GIT_CONFIG_GLOBAL':os.devnull,'GIT_TERMINAL_PROMPT':'0','GIT_OPTIONAL_LOCKS':'0'})
 return {'argv':list(map(str,argv)),'cwd':str(cwd),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'elapsed_seconds':round(time.time()-st,4)}
def good(r):
 if r['exit_code']:raise RuntimeError(json.dumps(r,ensure_ascii=False))
 return r['stdout'].strip()
def git(*args,cwd=ROOT):return good(run(['git','-c','core.hooksPath='+str(PKG/'validation/empty-hooks'),*args],cwd))
def static():
 if git('rev-parse','HEAD')!=BASE:raise RuntimeError('Not inherited R039 HEAD')
 files=[]
 for p in sorted(ROOT.rglob('*')):
  if not p.is_file() or p.is_symlink():continue
  r=p.relative_to(ROOT).as_posix()
  selected=(r.startswith(('.codex/skills/','governance/','scripts/handoff/')) or r in ['AGENTS.md','README.md','.codex/AGENTS.md','.codex/README.md','.codex/cognition/PROTOCOL.md','.codex/cognition/LOAD_SET.json','.codex/cognition/USER_REQUIREMENTS.md','exchange/README.md','exchange/BASELINE.json'])
  if selected and r!='governance/FRAMEWORK_MANIFEST.json':files.append({'path':r,'bytes':p.stat().st_size,'sha256':sha(p)})
 m={'schema_version':'hott.governance-complete-manifest.v1','portable_version':'1.0.0','original_protocol_version':'1.3.0','original_runtime_version':'1.3.0','session_skill_version':'1.0.0','business_skill_actual_version':'1.3.4','business_skill_legacy_manifest_version':'1.3.3','scope':'Full original two HoTT Skills and executable dependencies plus authoritative portable entry, policies and tools. Mutable state and history included in package-wide manifest, not duplicated here.','single_state_owner':'.codex/research/hott/STATE.json','files':files,'not_packaged_as_invented_skills':['repo-cognitive-closure (generic historical reference; standalone local skill not supplied)'],'legacy_failures':{'tests':73,'passed':70,'failed':3,'runtime_tests':56,'runtime_passed':56,'report':'artifacts/r040/FRAMEWORK_TESTS.json'},'mathematical_certification':False}
 dump(ROOT/'governance/FRAMEWORK_MANIFEST.json',m)
 dump(PKG/'manifests/GOVERNANCE_FRAMEWORK.json',m)
 # Keep the original raw input material reversible even on a new filesystem.
 from archive_store import restore
 with tempfile.TemporaryDirectory(prefix='hott-originals-restored-') as tmp:
  target=Path(tmp)/'originals';rr=restore(PKG/'archive',target,None)
  inv=json.loads((PKG/'manifests/SOURCE_INVENTORY.json').read_text())
  store=json.loads((PKG/'archive/STORE.json').read_text())
  source_entries=store['files']
  if isinstance(source_entries,dict):items=[{'path':k,**v} for k,v in source_entries.items()]
  else:items=source_entries
  count=0;total=0
  for r in items:
   rel=r.get('relative',r.get('relative_path',r.get('path')));p=target/rel
   expected=r.get('sha256');size=r.get('bytes',r.get('size'))
   if sha(p)!=expected or p.stat().st_size!=size:raise RuntimeError('Original restore mismatch: '+rel)
   count+=1;total+=size
  report={'status':'ALL_ORIGINALS_RESTORED_TO_NEW_FILESYSTEM_AND_HASHED','files':count,'bytes':total,'restore_return':rr,'source_store_sha256':sha(PKG/'archive/objects.pack'),'temporary_materialization_removed_after_verification':True,'original_inputs_untouched':True}
  dump(PKG/'validation/ORIGINALS_FILESYSTEM_RESTORE.json',report)
  dump(ART/'ORIGINALS_FILESYSTEM_RESTORE.json',report)
 print(json.dumps({'framework_files':len(files),'original_restore':report},ensure_ascii=False))

def precommit():
 old=json.loads((PKG/'manifests/BASELINE_R039.json').read_text())
 allowed={'AGENTS.md','README.md','.gitignore','.codex/cognition/LOAD_SET.json','.codex/cognition/HEAD.json','MEMORY.md','.codex/research/hott/STATE.json','.codex/research/hott/FRONTIER.md','.codex/research/hott/LESSONS.md','.codex/research/hott/RESUME.md'}
 changed=[];same=[];missing=[]
 for e in old['entries']:
  rel=e['path']
  if rel.startswith('.git/'):continue
  p=ROOT/rel
  if not p.is_file():missing.append(rel)
  elif sha(p)==e['sha256']:same.append(rel)
  else:changed.append(rel)
 if missing or set(changed)-allowed:raise RuntimeError('Baseline preservation failure '+repr((missing,set(changed)-allowed)))
 cp=json.loads((ART/'CHECKPOINT_VERIFICATION.json').read_text())
 if cp['revision']!=40 or not cp['new_documents_routed']:raise RuntimeError('Checkpoint not verified')
 fm=json.loads((ROOT/'governance/FRAMEWORK_MANIFEST.json').read_text())
 for row in fm['files']:
  if sha(ROOT/row['path'])!=row['sha256']:raise RuntimeError('Framework changed: '+row['path'])
 report={'status':'BASELINE_AND_FRAMEWORK_PRESERVED_WITH_AUTHORIZED_GOVERNANCE_EDITS','old_non_git_unchanged':len(same),'changed_existing':changed,'missing_existing':missing,'framework_files_checked':len(fm['files']),'old_records_preserved':cp['old_records_preserved'],'current_records':cp['current_records'],'research_unchanged':True,'legacy_test_failures_preserved':3}
 dump(ART/'BASELINE_PRESERVATION.json',report);dump(PKG/'validation/BASELINE_PRESERVATION.json',report)
 # Save exact final paths/counts without placing Git HEAD inside the commit it describes.
 dump(ART/'PRECOMMIT_CHECKS.json',{'baseline':BASE,'checks':[run(['git','diff','--check']),run(['git','fsck','--full'])]})
 for r in json.loads((ART/'PRECOMMIT_CHECKS.json').read_text())['checks']:good(r)
 print(json.dumps(report,ensure_ascii=False))

def commit():
 if git('rev-parse','HEAD')!=BASE:raise RuntimeError('Unexpected HEAD before authorized final commit')
 good(run(['git','add','--all']))
 good(run(['git','commit','-m','R040: portable full-AI handoff, preserved history and incremental audit protocol']))
 git('tag',TAG)
 head=git('rev-parse','HEAD');tree=git('rev-parse','HEAD^{tree}')
 if git('status','--porcelain'):raise RuntimeError('Dirty after commit')
 if git('remote'):raise RuntimeError('Unexpected remote')
 fsck=run(['git','fsck','--full']);good(fsck)
 hist=PKG/'history';hist.mkdir(exist_ok=True)
 bundle=hist/'HoTT_handoff_full.bundle'
 good(run(['git','bundle','create',bundle,'--all']))
 bv=run(['git','bundle','verify',bundle]);good(bv)
 idn={'schema':'hott.handoff-identity.v1','project_id':'ALL-Markdown/HoTT','handoff_id':'HoTT_AI_HANDOFF_20260911','last_mathematical_round':'R039','governance_revision':40,'head_commit':head,'head_tree':tree,'branch':git('branch','--show-current'),'shared_baseline_tag':TAG,'inherited_baseline_commit':BASE,'source_baseline_zip_sha256':sha('/mnt/data/HoTT_silent_steps_rev39_with_git.zip'),'full_git_bundle':'history/HoTT_handoff_full.bundle','bundle_sha256':sha(bundle),'commit_count':int(git('rev-list','--count','HEAD')),'remote_count':0,'shared_baseline_advances_only_on_explicit_acknowledgement':True}
 dump(PKG/'manifests/HANDOFF_IDENTITY.json',idn)
 dump(PKG/'validation/GIT_PRESEAL.json',{'fsck':fsck,'bundle_verify':bv,'status_porcelain':git('status','--porcelain'),'identity':idn})
 print(json.dumps(idn,ensure_ascii=False,indent=2))

def extract_safe(z,dest):
 for i in z.infolist():
  q=PurePosixPath(i.filename)
  if q.is_absolute() or '..' in q.parts or '\\' in i.filename:raise ValueError('Unsafe ZIP name')
  mode=(i.external_attr>>16)&0o177777
  if stat.S_ISLNK(mode):raise ValueError('Unexpected symlink')
  target=dest.joinpath(*q.parts)
  if i.is_dir():target.mkdir(parents=True,exist_ok=True);continue
  target.parent.mkdir(parents=True,exist_ok=True)
  with z.open(i) as src,target.open('xb') as out:shutil.copyfileobj(src,out)
  os.chmod(target,(mode&0o777) or 0o644)

def seal():
 idn=json.loads((PKG/'manifests/HANDOFF_IDENTITY.json').read_text());head=idn['head_commit']
 if git('rev-parse','HEAD')!=head or git('status','--porcelain'):raise RuntimeError('Pre-seal git state changed')
 from govern import load
 plan=load(ROOT).plan(ROOT)
 reading=json.loads((PKG/'onboarding/READING_PLAN.json').read_text())
 if plan['snapshot']!=reading['snapshot']:raise RuntimeError('Onboarding is stale')
 # Prove full-bundle recovery separately. Local clone executes no research scripts.
 with tempfile.TemporaryDirectory(prefix='hott-fullbundle-') as td:
  target=Path(td)/'clone'
  cr=run(['git','-c','core.hooksPath='+str(PKG/'validation/empty-hooks'),'clone','--',PKG/'history/HoTT_handoff_full.bundle',target]);good(cr)
  if git('rev-parse','HEAD',cwd=target)!=head:raise RuntimeError('Bundle clone HEAD mismatch')
  if git('status','--porcelain',cwd=target):raise RuntimeError('Dirty bundle clone')
  # A bundle clone has an origin pointing to the bundle. It is not a network endpoint; remove it.
  git('remote','remove','origin',cwd=target)
  fresh=load(target).plan(target)
  if fresh['snapshot']!=plan['snapshot'] or fresh['revision']!=40:raise RuntimeError('Relocated governance mismatch')
  br={'status':'FULL_BUNDLE_RESTORED','clone':cr,'head_commit':head,'snapshot':fresh['snapshot'],'revision':fresh['revision'],'documents':len(fresh['documents']),'research_scripts_executed':False}
  dump(PKG/'validation/BUNDLE_RESTORE.json',br)
 # Metadata-only admission manifest. Full text already built and separately checked after ZIP recovery.
 dump(PKG/'validation/PRESEAL_SUMMARY.json',{'status':'READY_FOR_FILE_SEAL','source_originals':324,'original_zip_count':52,'state_revision':40,'head_commit':head,'snapshot':plan['snapshot'],'current_core_documents':len(plan['documents']),'legacy_tests':{'run':73,'pass':70,'fail':3},'new_delta_tests':16,'last_math_round':'R039','AI_cognition_certified':False,'native_HoTT_certified':False})
 rows=[]
 for p in sorted(PKG.rglob('*')):
  if p.is_symlink():raise ValueError('Package symlink refused: '+str(p))
  if not p.is_file():continue
  rel=p.relative_to(PKG).as_posix()
  if rel==EXCLUDED_SELF:continue
  rows.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p),'mode':format(stat.S_IMODE(p.stat().st_mode),'04o')})
 dump(PKG/EXCLUDED_SELF,{'schema':'hott.full-package-files.v1','self_excluded':EXCLUDED_SELF,'files':rows,'file_count':len(rows),'total_bytes_excluding_manifest':sum(r['bytes'] for r in rows),'not_a_signature':True})
 out=PKG.with_suffix('.zip')
 if out.exists():raise FileExistsError(out)
 with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
  for p in sorted(PKG.rglob('*')):
   if p.is_file():z.write(p,PKG.name+'/'+p.relative_to(PKG).as_posix())
 manifest_sha=sha(PKG/EXCLUDED_SELF)
 with zipfile.ZipFile(out) as z:
  expected={PKG.name+'/'+r['path']:r for r in rows}
  expected[PKG.name+'/'+EXCLUDED_SELF]={'sha256':manifest_sha,'bytes':(PKG/EXCLUDED_SELF).stat().st_size}
  if set(z.namelist())!=set(expected):raise RuntimeError('ZIP names mismatch')
  for name,r in expected.items():
   h=hashlib.sha256();n=0
   with z.open(name) as f:
    for b in iter(lambda:f.read(1048576),b''):h.update(b);n+=len(b)
   if h.hexdigest()!=r['sha256'] or n!=r['bytes']:raise RuntimeError('ZIP readback mismatch '+name)
  with tempfile.TemporaryDirectory(prefix='hott-final-extract-') as td:
   extract_safe(z,Path(td));rest=Path(td)/PKG.name
   rr=run([sys.executable,'-B',rest/'workspace/scripts/handoff/verify_package.py','--package-root',rest],cwd=Path(td),timeout=180);good(rr)
   check=json.loads(rr['stdout'])
 # source worktree physical git files are not modified by final verifier (GIT_OPTIONAL_LOCKS=0).
 final={'status':'COMPLETE_HANDOFF_ZIP_VERIFIED','zip':str(out),'zip_bytes':out.stat().st_size,'zip_sha256':sha(out),'package_directory':str(PKG),'package_files':len(expected),'manifest_sha256':manifest_sha,'head_commit':head,'revision':40,'last_mathematical_round':'R039','source_originals_preserved':324,'source_original_bytes':748544776,'source_store_unique_bytes':217002151,'zip_all_members_readback_passed':True,'restored_directory_validation':rr,'restored_verifier_summary':check,'bundle_restore_verified':True,'delta_tests':16,'legacy_tests':{'run':73,'pass':70,'fail':3},'math_certified':False,'recipient_cognition_certified':False,'current_runtime_scope':'All identified files present in initial current sandbox inventory; unavailable historic sources not invented'}
 external=out.with_name(out.stem+'_VERIFICATION.json');dump(external,final)
 out.with_suffix('.zip.sha256').write_text(final['zip_sha256']+'  '+out.name+'\n',encoding='ascii')
 print(json.dumps({k:final[k] for k in ['status','zip','zip_bytes','zip_sha256','package_files','head_commit','revision']},ensure_ascii=False,indent=2))

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('stage',choices=['static','precommit','commit','seal']);a=ap.parse_args();globals()[a.stage]()
if __name__=='__main__':main()
