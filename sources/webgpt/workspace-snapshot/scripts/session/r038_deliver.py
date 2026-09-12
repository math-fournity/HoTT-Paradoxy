#!/usr/bin/env python3
"""Create and independently restore the full Git archive and bounded research kit."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess,sys,tempfile,zipfile
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT.parent
FULL=BASE/'HoTT_path_lifting_rev38_with_git.zip';KIT=BASE/'HoTT_path_lifting_R038.zip'
BUNDLE=BASE/'HoTT_path_lifting_rev38.bundle';REPORT=BASE/'HoTT_path_lifting_rev38_delivery_verification.json'
R='.codex/research/hott/reviews/TRANSITION-ABSTRACTION-002/'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(argv,cwd):
 start=datetime.now(timezone.utc).isoformat()
 p=subprocess.run(argv,cwd=cwd,capture_output=True,text=True,timeout=120,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',GIT_OPTIONAL_LOCKS='0'))
 r={'argv':argv,'cwd':str(cwd),'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
 if p.returncode:raise RuntimeError(json.dumps(r,ensure_ascii=False))
 return r
def git(args,cwd=ROOT):return run(['git',*args],cwd)
def main():
 for p in [FULL,KIT,BUNDLE,REPORT]:
  if p.exists():raise FileExistsError(p)
 assert not git(['status','--porcelain'])['stdout'].strip()
 assert not git(['remote'])['stdout'].strip()
 head=git(['rev-parse','HEAD'])['stdout'].strip();fsck=git(['fsck','--full'])
 git(['bundle','create',str(BUNDLE),'--all']);bv=git(['bundle','verify',str(BUNDLE)])
 manifest=[]
 for p in sorted(ROOT.rglob('*')):
  if p.is_symlink():raise RuntimeError('unexpected symlink '+str(p))
  if p.is_file():manifest.append({'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p),'mode':p.stat().st_mode&0o777})
 with zipfile.ZipFile(FULL,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for row in manifest:z.write(ROOT/row['path'],ROOT.name+'/'+row['path'])
 with zipfile.ZipFile(FULL) as z:
  assert z.testzip() is None
  for row in manifest:assert hashlib.sha256(z.read(ROOT.name+'/'+row['path'])).hexdigest()==row['sha256']
  with tempfile.TemporaryDirectory(prefix='r038-restore-',dir=BASE) as tmp:
   d=Path(tmp);z.extractall(d);restored=d/ROOT.name
   for row in manifest:
    p=restored/row['path'];p.chmod(row['mode']);assert sha(p)==row['sha256']
   assert git(['rev-parse','HEAD'],restored)['stdout'].strip()==head
   assert not git(['status','--porcelain'],restored)['stdout'].strip()
   rfsck=git(['fsck','--full'],restored)
   fresh=run([sys.executable,'-B',str(restored/'scripts/session/r038_verify.py'),'--fresh'],d)
   assert json.loads(fresh['stdout'])['revision']==38
   clone=d/'bundle-clone';clone_receipt=git(['clone',str(BUNDLE),str(clone)],d)
   assert git(['rev-parse','HEAD'],clone)['stdout'].strip()==head
   assert not git(['status','--porcelain'],clone)['stdout'].strip()
   assert json.loads((clone/'.codex/research/hott/STATE.json').read_text())['revision']==38
 selected=[R+x for x in ['PROOF_NOTE.md','CLAIMS.json','SOURCES.md','PLAN.md']]+[
  'scripts/research/r036_transition_abstraction.py','scripts/research/r038_current_lift.py','scripts/tests/test_r038_current_lift.py',
  'artifacts/r038/RESULTS.json','artifacts/r038/TEST_EXECUTION.json','artifacts/r038/MODEL_EXECUTION.json',
  'artifacts/r038/RESEARCH_MANIFEST.json','artifacts/r038/SOURCE_EXCERPTS.md','artifacts/r038/REPORT.md']
 prefix='HoTT_path_lifting_R038/'
 with zipfile.ZipFile(KIT,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in selected:z.write(ROOT/p,prefix+p)
  z.writestr(prefix+'README.md','''# R038 当前态提升研究包\n\n主文：.codex/research/hott/reviews/TRANSITION-ABSTRACTION-002/PROOF_NOTE.md。\n运行：`python3 -B scripts/tests/test_r038_current_lift.py`。\n新结果：`python3 -B scripts/research/r038_current_lift.py --output local-results.json`。\n28项有限测试不是HoTT内核证明；一般定理见纸笔全文。计数器的无穷结论不是从17个样本推出。\n该子包不含完整历史；跨Session应使用with_git完整包。\n''')
  z.writestr(prefix+'MANIFEST.json',json.dumps({p:sha(ROOT/p) for p in selected},ensure_ascii=False,indent=2)+'\n')
 with zipfile.ZipFile(KIT) as z:
  assert z.testzip() is None
  for p in selected:assert hashlib.sha256(z.read(prefix+p)).hexdigest()==sha(ROOT/p)
  with tempfile.TemporaryDirectory(prefix='r038-kit-',dir=BASE) as tmp:
   z.extractall(tmp);kitroot=Path(tmp)/prefix.rstrip('/')
   kt=run([sys.executable,'-B','scripts/tests/test_r038_current_lift.py'],kitroot)
   assert 'Ran 28 tests' in kt['stderr'] and '\nOK\n' in kt['stderr']
 assert not git(['status','--porcelain'])['stdout'].strip()
 report={'status':'PASS_DELIVERY_AND_RESTORE','revision':38,'research_round':'R038','workspace':str(ROOT),'git_head':head,
 'git_commit_count':int(git(['rev-list','--count','HEAD'])['stdout']),'clean_worktree':True,'remote_count':0,
 'all_zip_bytes_verified':True,'full_zip':{'path':str(FULL),'bytes':FULL.stat().st_size,'sha256':sha(FULL)},
 'research_kit':{'path':str(KIT),'bytes':KIT.stat().st_size,'sha256':sha(KIT)},
 'git_bundle':{'path':str(BUNDLE),'bytes':BUNDLE.stat().st_size,'sha256':sha(BUNDLE)},
 'fsck':fsck,'bundle_verify':bv,'restored_fsck':rfsck,'fresh_verifier':fresh,'bundle_clone':clone_receipt,'kit_tests':kt,'manifest':manifest,
 'scope':'File integrity, Git restoration, finite code; no native HoTT or complete cognition certification.'}
 REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ['status','revision','git_head','git_commit_count','full_zip','research_kit','git_bundle']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
