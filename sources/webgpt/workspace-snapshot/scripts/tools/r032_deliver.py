#!/usr/bin/env python3
"""Archive a clean repository incl .git and verify actual ZIP and bundle restores."""
from pathlib import Path
import datetime,hashlib,json,os,subprocess,sys,tempfile,zipfile
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT.parent
ZIP=BASE/'HoTT_restricted_reflection_rev32_with_git.zip'
BUNDLE=BASE/'HoTT_restricted_reflection_rev32.bundle'
REPORT=BASE/'HoTT_restricted_reflection_rev32_delivery_verification.json'
RESEARCH=BASE/'HoTT_restricted_reflection_R032.zip'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(argv,cwd):
    p=subprocess.run(argv,cwd=cwd,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),
                     text=True,capture_output=True,timeout=90)
    result={'argv':argv,'cwd':str(cwd),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    if p.returncode:raise RuntimeError(json.dumps(result,ensure_ascii=False))
    return result
def git(args,cwd=ROOT):return run(['git']+args,cwd)
def main():
    for f in (ZIP,BUNDLE,REPORT,RESEARCH):
        if f.exists():raise FileExistsError(f)
    assert not git(['status','--porcelain'])['stdout'].strip(),'dirty worktree'
    assert not git(['remote'])['stdout'].strip(),'unexpected remote'
    head=git(['rev-parse','HEAD'])['stdout'].strip()
    fsck=git(['fsck','--full'])
    count=int(git(['rev-list','--count','HEAD'])['stdout'])
    git(['bundle','create',str(BUNDLE),'--all']);bundle_check=git(['bundle','verify',str(BUNDLE)])
    files=[]
    for p in sorted(ROOT.rglob('*')):
        if p.is_symlink():raise RuntimeError('unexpected symlink: '+str(p))
        if p.is_file():files.append({'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
    with zipfile.ZipFile(ZIP,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for row in files:z.write(ROOT/row['path'],ROOT.name+'/'+row['path'])
    with zipfile.ZipFile(ZIP) as z:
        assert z.testzip() is None
        for row in files:
            data=z.read(ROOT.name+'/'+row['path'])
            assert len(data)==row['bytes'] and hashlib.sha256(data).hexdigest()==row['sha256']
        with tempfile.TemporaryDirectory(prefix='r032-restore-',dir=BASE) as td:
            dest=Path(td);z.extractall(dest);restored=dest/ROOT.name
            for row in files:
                p=restored/row['path'];p.chmod((ROOT/row['path']).stat().st_mode & 0o777)
                assert sha(p)==row['sha256']
            assert git(['rev-parse','HEAD'],restored)['stdout'].strip()==head
            assert not git(['status','--porcelain'],restored)['stdout'].strip()
            restored_fsck=git(['fsck','--full'],restored)
            fresh=run([sys.executable,'-B',str(restored/'scripts/tools/r032_verify.py'),'--fresh'],dest)
            fresh_json=json.loads(fresh['stdout']);assert fresh_json['revision']==32
            clone=dest/'bundle-clone'
            clone_log=run(['git','clone',str(BUNDLE),str(clone)],dest)
            assert git(['rev-parse','HEAD'],clone)['stdout'].strip()==head
            assert not git(['status','--porcelain'],clone)['stdout'].strip()
    prefixes=('.codex/research/hott/reviews/SELF-REFERENCE-004/',
              'artifacts/r032/','scripts/research/r032_formal/')
    exact={'scripts/research/r032_restricted_reflection.py','scripts/tests/test_r032_restricted_reflection.py',
           'scripts/session/run_logged.py','HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md'}
    selected=[row for row in files if row['path'].startswith(prefixes) or row['path'] in exact]
    with zipfile.ZipFile(RESEARCH,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for row in selected:z.write(ROOT/row['path'],row['path'])
        z.writestr('PACKAGE_SCOPE.md','# R032局部研究资料包\n\n本包不包含完整治理链或Git；完整接续请使用with_git包。一般纸笔证明、Python有限检查、未编译Agda三者分开。\n')
    with zipfile.ZipFile(RESEARCH) as z:assert z.testzip() is None
    assert not git(['status','--porcelain'])['stdout'].strip()
    result={'status':'PASS_DELIVERY_AND_RESTORATION','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'workspace':str(ROOT),'revision':32,'git_head':head,'git_commit_count':count,
       'git_branch':git(['branch','--show-current'])['stdout'].strip(),'remote_count':0,'clean_worktree':True,
       'git_fsck':fsck,'bundle_verify':bundle_check,'zip':{'path':str(ZIP),'bytes':ZIP.stat().st_size,'sha256':sha(ZIP),'files':len(files)},
       'bundle':{'path':str(BUNDLE),'bytes':BUNDLE.stat().st_size,'sha256':sha(BUNDLE)},
       'research_pack':{'path':str(RESEARCH),'bytes':RESEARCH.stat().st_size,'sha256':sha(RESEARCH)},
       'zip_all_bytes_replayed':True,'zip_restored_clean':True,'restored_fsck':restored_fsck,
       'fresh_restored_plan':fresh_json,'bundle_clone_same_head':True,'bundle_clone_clean':True,'clone_log':clone_log,
       'file_manifest':files,'native_kernel':'NOT_RUN','full_business_cognition':'INCOMPLETE',
       'mathematics':'SCOPED_STRUCTURAL_PAPER_PROOFS_AND_FINITE_REPLAY_NOT_FULL_HOTT_CERTIFICATION'}
    REPORT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','revision','git_head','git_commit_count','zip','bundle','research_pack']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
