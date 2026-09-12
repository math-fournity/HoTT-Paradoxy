"""Restore the supplied revision27 without altering it; preserve a byte baseline."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, stat, zipfile, subprocess, datetime

def sha(b): return hashlib.sha256(b).hexdigest()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('archive', type=Path); args=ap.parse_args()
    root=Path(__file__).resolve().parents[2]
    prefix='HoTT_Gemini_review_rev27/'
    baseline=[]
    with zipfile.ZipFile(args.archive) as z:
        members=z.infolist()
        if sum(x.file_size for x in members)>500_000_000: raise ValueError('Unexpected archive size')
        seen=set()
        for i in members:
            if not i.filename.startswith(prefix): raise ValueError('Unexpected prefix '+i.filename)
            rel=i.filename[len(prefix):]
            if not rel or i.is_dir(): continue
            p=PurePosixPath(rel)
            if p.is_absolute() or '..' in p.parts or '\\' in rel: raise ValueError('Unsafe path')
            if stat.S_ISLNK(i.external_attr>>16): raise ValueError('Symlink rejected')
            if rel in seen: raise ValueError('Duplicate path')
            seen.add(rel)
            target=root/rel
            if target.exists(): raise FileExistsError(target)
            b=z.read(i); target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(b)
            if not rel.startswith('.git/'):
                baseline.append({'path':rel,'bytes':len(b),'sha256':sha(b)})
    def git(*a):
        p=subprocess.run(['git','-c','core.hooksPath=/dev/null','-C',str(root),*a],capture_output=True,text=True,timeout=30)
        if p.returncode: raise RuntimeError(p.stderr)
        return p.stdout.strip()
    out=root/'artifacts/r028';out.mkdir(parents=True,exist_ok=True)
    receipt={'input':str(args.archive),'archive_sha256':sha(args.archive.read_bytes()),
             'restored_root':str(root),'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
             'git_head':git('rev-parse','HEAD'),'git_branch':git('branch','--show-current'),
             'remotes':git('remote','-v'),'initial_status':git('status','--porcelain=v1'),
             'files':baseline,'scope':'all supplied project files excluding .git; new bootstrap excluded'}
    (out/'RESTORE_BASELINE.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='files'},ensure_ascii=False,indent=2))
    print('Preserved project-file baseline:',len(baseline))
if __name__=='__main__': main()
