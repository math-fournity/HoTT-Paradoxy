"""Create full paused workspace archive and Git bundle; independently restore both."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, subprocess, sys, tempfile, zipfile
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT.parent
ZIP=BASE/'HoTT_pause_rev35_with_git.zip'
BUNDLE=BASE/'HoTT_pause_rev35.bundle'
REPORT=BASE/'HoTT_pause_rev35_delivery_verification.json'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(argv,cwd):
    started=datetime.now(timezone.utc).isoformat()
    p=subprocess.run(argv,cwd=cwd,text=True,capture_output=True,timeout=120,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
    rec={'argv':argv,'cwd':str(cwd),'started_utc':started,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    if p.returncode:raise RuntimeError(json.dumps(rec,ensure_ascii=False))
    return rec
def git(args,cwd=ROOT):return run(['git',*args],cwd)
def main():
    for p in [ZIP,BUNDLE,REPORT]:
        if p.exists():raise FileExistsError(p)
    assert not git(['status','--porcelain'])['stdout'].strip()
    assert not git(['remote'])['stdout'].strip()
    head=git(['rev-parse','HEAD'])['stdout'].strip()
    fsck=git(['fsck','--full']);git(['bundle','create',str(BUNDLE),'--all']);bv=git(['bundle','verify',str(BUNDLE)])
    manifest=[]
    for f in sorted(ROOT.rglob('*')):
        if f.is_symlink():raise RuntimeError('Unexpected symlink: '+str(f))
        if f.is_file():manifest.append({'path':str(f.relative_to(ROOT)),'sha256':sha(f),'bytes':f.stat().st_size,'mode':f.stat().st_mode & 0o777})
    with zipfile.ZipFile(ZIP,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for row in manifest:z.write(ROOT/row['path'],ROOT.name+'/'+row['path'])
    with zipfile.ZipFile(ZIP) as z:
        assert z.testzip() is None
        for row in manifest:
            raw=z.read(ROOT.name+'/'+row['path']);assert hashlib.sha256(raw).hexdigest()==row['sha256']
        with tempfile.TemporaryDirectory(prefix='r035-restore-',dir=BASE) as temp:
            dest=Path(temp);z.extractall(dest);restored=dest/ROOT.name
            for row in manifest:
                f=restored/row['path'];f.chmod(row['mode']);assert sha(f)==row['sha256']
            assert git(['rev-parse','HEAD'],restored)['stdout'].strip()==head
            assert not git(['status','--porcelain'],restored)['stdout'].strip()
            rfsck=git(['fsck','--full'],restored)
            fresh=run([sys.executable,'-B',str(restored/'scripts/session/r035_verify.py'),'--fresh'],dest)
            fresh_data=json.loads(fresh['stdout']);assert fresh_data['pause_status']=='PAUSED_BY_USER'
            clone=dest/'bundle-clone';cl=run(['git','clone',str(BUNDLE),str(clone)],dest)
            assert git(['rev-parse','HEAD'],clone)['stdout'].strip()==head
            assert not git(['status','--porcelain'],clone)['stdout'].strip()
            assert json.loads((clone/'.codex/research/hott/STATE.json').read_text())['execution_control']['status']=='PAUSED_BY_USER'
    assert not git(['status','--porcelain'])['stdout'].strip()
    result={'status':'PASS_PAUSED_DELIVERY_AND_RESTORE','utc':datetime.now(timezone.utc).isoformat(),
      'workspace':str(ROOT),'revision':35,'pause_status':'PAUSED_BY_USER','git_head':head,
      'git_commit_count':int(git(['rev-list','--count','HEAD'])['stdout']),
      'clean_worktree':True,'remote_count':0,
      'zip':{'path':str(ZIP),'bytes':ZIP.stat().st_size,'sha256':sha(ZIP),'files':len(manifest)},
      'bundle':{'path':str(BUNDLE),'bytes':BUNDLE.stat().st_size,'sha256':sha(BUNDLE)},
      'fsck':fsck,'bundle_verify':bv,'restored_fsck':rfsck,'fresh_verifier':fresh,
      'fresh_restore_summary':fresh_data,'clone_receipt':cl,'all_zip_bytes_verified':True,
      'bundle_clone_same_head_and_paused':True,'manifest':manifest,
      'mathematical_experiments':0,'native_formal_runs':0,'model_understanding':'NOT_CERTIFIED'}
    REPORT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k in ['status','revision','pause_status','git_head','git_commit_count','zip','bundle']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
