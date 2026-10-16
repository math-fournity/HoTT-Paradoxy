#!/usr/bin/env python3
"""Create full Git delivery and standalone research kit; verify both from new paths."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,os,subprocess,sys,tempfile,zipfile
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT.parent
FULL=BASE/'HoTT_transition_abstraction_rev37_with_git.zip'
KIT=BASE/'HoTT_transition_abstraction_R036.zip'
BUNDLE=BASE/'HoTT_transition_abstraction_rev37.bundle'
REPORT=BASE/'HoTT_transition_abstraction_rev37_delivery_verification.json'
R='.codex/research/hott/reviews/TRANSITION-ABSTRACTION-001/'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(argv,cwd):
 start=datetime.now(timezone.utc).isoformat()
 p=subprocess.run(argv,cwd=cwd,capture_output=True,text=True,timeout=120,
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',GIT_OPTIONAL_LOCKS='0'))
 rec={'argv':argv,'cwd':str(cwd),'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),
      'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
 if p.returncode:raise RuntimeError(json.dumps(rec,ensure_ascii=False))
 return rec
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
  if p.is_symlink():raise RuntimeError('unexpected symlink: '+str(p))
  if p.is_file():manifest.append({'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p),'mode':p.stat().st_mode&0o777})
 with zipfile.ZipFile(FULL,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for row in manifest:z.write(ROOT/row['path'],ROOT.name+'/'+row['path'])
 with zipfile.ZipFile(FULL) as z:
  assert z.testzip() is None
  for row in manifest:
   assert hashlib.sha256(z.read(ROOT.name+'/'+row['path'])).hexdigest()==row['sha256']
  with tempfile.TemporaryDirectory(prefix='r036-full-restore-',dir=BASE) as tmp:
   d=Path(tmp);z.extractall(d);restored=d/ROOT.name
   for row in manifest:
    p=restored/row['path'];p.chmod(row['mode']);assert sha(p)==row['sha256']
   assert git(['rev-parse','HEAD'],restored)['stdout'].strip()==head
   assert not git(['status','--porcelain'],restored)['stdout'].strip()
   rfsck=git(['fsck','--full'],restored)
   fresh=run([sys.executable,'-B',str(restored/'scripts/session/r036_verify.py'),'--fresh'],d)
   fresh_data=json.loads(fresh['stdout']);assert fresh_data['revision']==37
   clone=d/'bundle-clone';clone_receipt=git(['clone',str(BUNDLE),str(clone)],d)
   assert git(['rev-parse','HEAD'],clone)['stdout'].strip()==head
   assert not git(['status','--porcelain'],clone)['stdout'].strip()
   assert json.loads((clone/'.codex/research/hott/STATE.json').read_text())['revision']==37
 # Independent kit preserves package-relative script paths and exact evidence files.
 selected=[R+x for x in ['PROOF_NOTE.md','CLAIMS.json','SOURCES.md','PLAN.md']]+[
 'scripts/research/r036_transition_abstraction.py','scripts/tests/test_r036_transition_abstraction.py',
 'artifacts/r036/RESULTS.json','artifacts/r036/TEST_EXECUTION.json','artifacts/r036/MODEL_EXECUTION.json',
 'artifacts/r036/RESEARCH_MANIFEST.json','artifacts/r036/REPORT.md',
 'HoTT/theory-schema/upstream/book-578b85cc/logic.tex','HoTT/theory-schema/upstream/book-578b85cc/hits.tex']
 prefix='HoTT_transition_abstraction_R036/'
 readme='''# R036 有限状态抽象研究子包

主文：.codex/research/hott/reviews/TRANSITION-ABSTRACTION-001/PROOF_NOTE.md。

复现：在本目录运行 `python3 -B scripts/tests/test_r036_transition_abstraction.py`。
生成新的结果（不要覆盖归档证据）：`python3 -B scripts/research/r036_transition_abstraction.py --output local-results.json`。

28项有限模型测试不是HoTT内核证明；一般命题有纸笔推导；无原创性/物理对应认证。该子包不含完整治理与历史；跨Session恢复应使用HoTT_transition_abstraction_rev37_with_git.zip。最后实质研究R036，revision37只补齐current-owner一致性。
'''
 with zipfile.ZipFile(KIT,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in selected:z.write(ROOT/p,prefix+p)
  z.writestr(prefix+'README.md',readme)
  z.writestr(prefix+'MANIFEST.json',json.dumps({p:sha(ROOT/p) for p in selected},ensure_ascii=False,indent=2)+'\n')
 with zipfile.ZipFile(KIT) as z:
  assert z.testzip() is None
  for p in selected:assert hashlib.sha256(z.read(prefix+p)).hexdigest()==sha(ROOT/p)
  with tempfile.TemporaryDirectory(prefix='r036-kit-restore-',dir=BASE) as tmp:
   z.extractall(tmp);kitroot=Path(tmp)/prefix.rstrip('/')
   kit_tests=run([sys.executable,'-B','scripts/tests/test_r036_transition_abstraction.py'],kitroot)
   assert 'Ran 28 tests' in kit_tests['stderr'] and '\nOK\n' in kit_tests['stderr']
 assert not git(['status','--porcelain'])['stdout'].strip()
 report={'status':'PASS_DELIVERY_AND_RESTORE','revision':37,'research_round':'R036','workspace':str(ROOT),
 'git_head':head,'git_commit_count':int(git(['rev-list','--count','HEAD'])['stdout']),
 'clean_worktree':True,'remote_count':0,'all_zip_bytes_verified':True,
 'full_zip':{'path':str(FULL),'bytes':FULL.stat().st_size,'sha256':sha(FULL)},
 'research_kit':{'path':str(KIT),'bytes':KIT.stat().st_size,'sha256':sha(KIT)},
 'git_bundle':{'path':str(BUNDLE),'bytes':BUNDLE.stat().st_size,'sha256':sha(BUNDLE)},
 'fsck':fsck,'bundle_verify':bv,'restored_fsck':rfsck,'fresh_verifier':fresh,
 'fresh_restore_summary':fresh_data,'bundle_clone':clone_receipt,'kit_tests':kit_tests,
 'manifest':manifest,'scope':'Files/Git/finite model only; no native HoTT or full cognition certification.'}
 REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ['status','revision','research_round','git_head','git_commit_count','full_zip','research_kit','git_bundle']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
