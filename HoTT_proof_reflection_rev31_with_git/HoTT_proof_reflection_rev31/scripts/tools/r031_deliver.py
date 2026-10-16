#!/usr/bin/env python3
"""Archive the clean R031 repository with Git, then actually restore ZIP and bundle."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT.parent
ZIP=BASE/'HoTT_proof_reflection_rev31_with_git.zip'
BUNDLE=BASE/'HoTT_proof_reflection_rev31.bundle'
REPORT=BASE/'HoTT_proof_reflection_rev31_delivery_verification.json'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def execute(argv,cwd):
    p=subprocess.run(argv,cwd=cwd,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),text=True,capture_output=True,timeout=60)
    r={'argv':argv,'cwd':str(cwd),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    if p.returncode:raise RuntimeError(json.dumps(r,ensure_ascii=False))
    return r

def git(args,cwd=ROOT):return execute(['git','-c','core.hooksPath=/dev/null']+args,cwd)

def main():
    for p in (ZIP,BUNDLE,REPORT):
        if p.exists():raise FileExistsError(p)
    status=git(['status','--porcelain'])
    if status['stdout'].strip():raise RuntimeError('worktree is not clean')
    if git(['remote'])['stdout'].strip():raise RuntimeError('unexpected remote')
    head=git(['rev-parse','HEAD'])['stdout'].strip()
    fsck=git(['fsck','--full'])
    commits=int(git(['rev-list','--count','HEAD'])['stdout'])
    git(['bundle','create',str(BUNDLE),'--all'])
    bundle_check=git(['bundle','verify',str(BUNDLE)])
    entries=[]
    for p in sorted(ROOT.rglob('*')):
        if p.is_symlink():raise RuntimeError('symlink not permitted in delivery: '+str(p))
        if p.is_file():entries.append({'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
    with zipfile.ZipFile(ZIP,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for row in entries:z.write(ROOT/row['path'], ROOT.name+'/'+row['path'])
    with zipfile.ZipFile(ZIP) as z:
        assert z.testzip() is None
        for row in entries:
            b=z.read(ROOT.name+'/'+row['path'])
            assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
        with tempfile.TemporaryDirectory(prefix='r031-restore-',dir=BASE) as tmp:
            dest=Path(tmp)
            z.extractall(dest)
            restored=dest/ROOT.name
            for row in entries:
                p=restored/row['path'];original=ROOT/row['path']
                p.chmod(original.stat().st_mode & 0o777)
                assert sha(p)==row['sha256']
            restore_head=git(['rev-parse','HEAD'],restored)
            assert restore_head['stdout'].strip()==head
            restore_status=git(['status','--porcelain'],restored)
            assert not restore_status['stdout'].strip()
            restore_fsck=git(['fsck','--full'],restored)
            fresh=execute([sys.executable,'-B',str(restored/'scripts/tools/r031_verify.py'),'--fresh'],dest)
            fresh_json=json.loads(fresh['stdout']);assert fresh_json['revision']==31
            clone=dest/'bundle-clone'
            clone_receipt=execute(['git','-c','core.hooksPath=/dev/null','clone',str(BUNDLE),str(clone)],dest)
            clone_head=git(['rev-parse','HEAD'],clone)
            assert clone_head['stdout'].strip()==head
            clone_status=git(['status','--porcelain'],clone)
            assert not clone_status['stdout'].strip()
    assert not git(['status','--porcelain'])['stdout'].strip()
    report={'status':'PASS_DELIVERY_AND_RESTORATION','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'workspace':str(ROOT),'revision':31,'git_head':head,'git_commit_count':commits,'git_branch':git(['branch','--show-current'])['stdout'].strip(),
      'remote_count':0,'clean_worktree':True,'git_fsck':fsck,'bundle_verify':bundle_check,
      'zip':{'path':str(ZIP),'bytes':ZIP.stat().st_size,'sha256':sha(ZIP),'files':len(entries)},
      'bundle':{'path':str(BUNDLE),'bytes':BUNDLE.stat().st_size,'sha256':sha(BUNDLE)},
      'zip_replay_all_bytes':True,'restored_head_equal':True,'restored_clean':True,
      'restore_fsck':restore_fsck,'fresh_restored_plan':fresh_json,'bundle_clone_head_equal':True,
      'bundle_clone_clean':True,'clone_command':clone_receipt,
      'file_manifest':entries,
      'mathematical_status':'CONDITIONAL_PAPER_DERIVATION_AND_FINITE_RULE_REPLAY_NOT_FULL_HOTT_KERNEL',
      'full_cognition_status':'INCOMPLETE',
      'limits':'Hashes and Git continuity do not prove mathematical truth or complete model cognition.'}
    REPORT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','revision','git_head','git_commit_count','zip','bundle']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
