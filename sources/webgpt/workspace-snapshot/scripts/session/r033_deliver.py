"""Package committed R033 workspace, verify bytes and real Git restores."""
from pathlib import Path
import datetime,hashlib,json,os,subprocess,sys,tempfile,zipfile
ROOT=Path(__file__).resolve().parents[2];BASE=ROOT.parent
ZIP=BASE/'HoTT_dependent_migration_rev33_with_git.zip'
BUNDLE=BASE/'HoTT_dependent_migration_rev33.bundle'
REPORT=BASE/'HoTT_dependent_migration_rev33_delivery_verification.json'
RESEARCH=BASE/'HoTT_dependent_migration_R033.zip'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(argv,cwd=ROOT):
    p=subprocess.run(argv,cwd=cwd,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),text=True,capture_output=True,timeout=90)
    d={'argv':argv,'cwd':str(cwd),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    if p.returncode:raise RuntimeError(json.dumps(d,ensure_ascii=False))
    return d
def git(args,cwd=ROOT):return run(['git']+args,cwd)
def main():
    for p in [ZIP,BUNDLE,REPORT,RESEARCH]:
        if p.exists():raise FileExistsError(p)
    assert not git(['status','--porcelain'])['stdout'].strip()
    assert not git(['remote'])['stdout'].strip()
    head=git(['rev-parse','HEAD'])['stdout'].strip();fsck=git(['fsck','--full'])
    count=int(git(['rev-list','--count','HEAD'])['stdout'])
    git(['bundle','create',str(BUNDLE),'--all']);bc=git(['bundle','verify',str(BUNDLE)])
    files=[]
    for p in sorted(ROOT.rglob('*')):
        if p.is_symlink():raise RuntimeError('symlink '+str(p))
        if p.is_file():files.append({'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)})
    with zipfile.ZipFile(ZIP,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for row in files:z.write(ROOT/row['path'],ROOT.name+'/'+row['path'])
    with zipfile.ZipFile(ZIP) as z:
        assert z.testzip() is None
        for row in files:
            blob=z.read(ROOT.name+'/'+row['path']);assert len(blob)==row['bytes'] and hashlib.sha256(blob).hexdigest()==row['sha256']
        with tempfile.TemporaryDirectory(prefix='r033-restore-',dir=BASE) as td:
            dest=Path(td);z.extractall(dest);restored=dest/ROOT.name
            for row in files:
                p=restored/row['path'];p.chmod((ROOT/row['path']).stat().st_mode & 0o777)
                assert sha(p)==row['sha256']
            assert git(['rev-parse','HEAD'],restored)['stdout'].strip()==head
            assert not git(['status','--porcelain'],restored)['stdout'].strip()
            restored_fsck=git(['fsck','--full'],restored)
            fresh=run([sys.executable,'-B',str(restored/'scripts/session/r033_verify.py'),'--fresh'],dest)
            fresh_data=json.loads(fresh['stdout']);assert fresh_data['revision']==33
            clone=dest/'bundle-clone';clone_log=run(['git','clone',str(BUNDLE),str(clone)],dest)
            assert git(['rev-parse','HEAD'],clone)['stdout'].strip()==head
            assert not git(['status','--porcelain'],clone)['stdout'].strip()
    prefixes=('.codex/research/hott/reviews/SELF-REFERENCE-005/', 'scripts/research/r033_formal/')
    exact={'scripts/research/r033_dependent_migration.py','scripts/tests/test_r033_dependent_migration.py',
           'artifacts/r033/RESULTS.json','artifacts/r033/TEST_EXECUTION.json','artifacts/r033/CONSTRUCTION_EXECUTION.json',
           'artifacts/r033/REPORT.md','artifacts/r033/VERIFICATION.json','artifacts/r033/NATIVE_PROBE.json'}
    chosen=[r for r in files if r['path'].startswith(prefixes) or r['path'] in exact]
    with zipfile.ZipFile(RESEARCH,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for row in chosen:z.write(ROOT/row['path'],row['path'])
        z.writestr('PACKAGE_SCOPE.md','# R033 局部研究包\n\n含论证、源码、有限检查和准确范围；无完整治理或Git。完整接续使用with_git包。Agda未编译，不是HoTT内核认证。\n')
    with zipfile.ZipFile(RESEARCH) as z:assert z.testzip() is None
    assert not git(['status','--porcelain'])['stdout'].strip()
    result={'status':'PASS_DELIVERY_AND_RESTORATION','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'revision':33,'workspace':str(ROOT),'git_head':head,'git_commit_count':count,
      'branch':git(['branch','--show-current'])['stdout'].strip(),'remote_count':0,'clean_worktree':True,
      'zip':{'path':str(ZIP),'bytes':ZIP.stat().st_size,'sha256':sha(ZIP),'files':len(files)},
      'bundle':{'path':str(BUNDLE),'bytes':BUNDLE.stat().st_size,'sha256':sha(BUNDLE)},
      'research_pack':{'path':str(RESEARCH),'bytes':RESEARCH.stat().st_size,'sha256':sha(RESEARCH)},
      'fsck':fsck,'bundle_check':bc,'restored_fsck':restored_fsck,'fresh_restored_plan':fresh_data,
      'zip_all_bytes_replayed':True,'zip_restore_clean':True,'bundle_clone_same_head':True,'bundle_clone_clean':True,
      'clone_log':clone_log,'file_manifest':files,'native_formal':'NOT_RUN','full_business_cognition':'INCOMPLETE'}
    REPORT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','revision','git_head','git_commit_count','zip','bundle','research_pack']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
