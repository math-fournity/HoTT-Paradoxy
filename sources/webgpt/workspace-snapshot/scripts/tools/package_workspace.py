#!/usr/bin/env python3
"""Package a clean local repository including .git, create bundle, verify restoration.
Outputs are outside the repository to avoid dirtying the committed snapshot.
No remote is consulted and no working-tree content is deleted or altered.
"""
from pathlib import Path
import argparse, datetime, hashlib, json, os, subprocess, tempfile, zipfile


def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    ap.add_argument('--out-dir',type=Path,required=True)
    ap.add_argument('--name',default='HoTT_workspace_rev16')
    a=ap.parse_args();root=a.root.resolve();out=a.out_dir.resolve();out.mkdir(parents=True,exist_ok=True)
    try:out.relative_to(root)
    except ValueError:pass
    else:raise SystemExit('Outputs must be outside repository')
    if not a.name or any(c not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-' for c in a.name):
        raise SystemExit('Unsafe artifact basename')
    evidence=[]
    def git(args,cwd=root,allow_fail=False):
        p=subprocess.run(['git',*args],cwd=cwd,text=True,capture_output=True,timeout=60,
                         env=dict(os.environ,GIT_TERMINAL_PROMPT='0'))
        evidence.append({'argv':['git',*args],'cwd':str(cwd),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
        if p.returncode and not allow_fail:raise RuntimeError(evidence[-1])
        return p.stdout
    if git(['status','--porcelain=v1']).strip():raise SystemExit('Working tree is not clean')
    if git(['remote']).strip():raise SystemExit('Expected this user-authorized local-only repository to have no remote')
    head=git(['rev-parse','HEAD']).strip();branch=git(['branch','--show-current']).strip()
    git(['fsck','--full'])
    bundle=out/(a.name+'.bundle');archive=out/(a.name+'_with_git.zip')
    report_path=out/(a.name+'_delivery_verification.json')
    for p in (bundle,archive,report_path,Path(str(bundle)+'.sha256'),Path(str(archive)+'.sha256')):
        if p.exists():raise SystemExit('Refusing output overwrite: '+str(p))
    git(['bundle','create',str(bundle),'--all']);git(['bundle','verify',str(bundle)])
    tracked=git(['ls-files','-z']).split('\0');tracked=[p for p in tracked if p]
    paths=[root/p for p in tracked]
    paths += [p for p in (root/'.git').rglob('*') if p.is_file()]
    paths=sorted(set(paths))
    for p in paths:
        if p.is_symlink():raise SystemExit('Package refuses unreviewed symlinks: '+str(p))
        if p.suffix=='.lock':raise SystemExit('Git lock file present: '+str(p))
        if not p.is_file():raise SystemExit('Missing file: '+str(p))
    manifest=[{'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':digest(p)} for p in paths]
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in paths:z.write(p,a.name+'/'+p.relative_to(root).as_posix())
    with zipfile.ZipFile(archive) as z:
        if z.testzip() is not None:raise AssertionError('ZIP CRC failure')
        for row in manifest:
            b=z.read(a.name+'/'+row['path'])
            assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
        with tempfile.TemporaryDirectory(prefix='hott-restore-check-') as td:
            target=Path(td)
            # Every member was created above from safe relative repository paths.
            z.extractall(target)
            restored=target/a.name
            assert git(['rev-parse','HEAD'],restored).strip()==head
            assert not git(['status','--porcelain=v1'],restored).strip()
            git(['fsck','--full'],restored)
    with tempfile.TemporaryDirectory(prefix='hott-bundle-check-') as td:
        target=Path(td)/'clone'
        git(['clone','--no-hardlinks',str(bundle),str(target)])
        assert git(['rev-parse','HEAD'],target).strip()==head
        assert not git(['status','--porcelain=v1'],target).strip()
    assert not git(['status','--porcelain=v1']).strip()
    assert git(['rev-parse','HEAD']).strip()==head
    for p in (bundle,archive):Path(str(p)+'.sha256').write_text(digest(p)+'  '+p.name+'\n')
    report={'schema_version':'hott-workspace-delivery/v1','status':'PASS_RESTORE_AND_GIT_SCOPE',
            'completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'root':str(root),'head':head,'branch':branch,'remote_count':0,
            'commit_count':int(git(['rev-list','--all','--count']).strip()),
            'commits':git(['log','--all','--format=%H %s']).splitlines(),
            'tracked_file_count':len(tracked),'packaged_file_count':len(paths),
            'zip':{'path':str(archive),'bytes':archive.stat().st_size,'sha256':digest(archive)},
            'bundle':{'path':str(bundle),'bytes':bundle.stat().st_size,'sha256':digest(bundle)},
            'checks':['original_worktree_clean','no_remote','git_fsck','bundle_verify','zip_CRC',
                      'all_ZIP_bytes_match','restored_zip_git_clean_and_fsck','clone_bundle_HEAD_and_clean'],
            'files':manifest,'commands':evidence,
            'limits':'Local history starts at supplied rev15 import; no original-host history, mathematics or full-cognition certification.'}
    report_path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('files','commands')},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
