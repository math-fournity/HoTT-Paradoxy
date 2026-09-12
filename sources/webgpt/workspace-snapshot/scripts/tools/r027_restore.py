"""Restore the supplied R026 repository without overwriting old work."""
from pathlib import Path, PurePosixPath
import hashlib, json, os, stat, subprocess, zipfile, datetime
ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT.parent / 'HoTT_early_reassessment_rev26_final_with_git.zip'
RECEIPT = ROOT.parent / 'HoTT_early_reassessment_rev26_final_delivery_verification.json'
def digest(data):
    return hashlib.sha256(data).hexdigest()
def git(*args):
    p = subprocess.run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args], cwd=ROOT, capture_output=True, text=True, timeout=30)
    return {'argv': ['git',*args], 'cwd':str(ROOT),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
def main():
    meta=json.loads(RECEIPT.read_text())
    expected=next(x['sha256'] for x in meta['outputs'] if x['path'].endswith('_with_git.zip'))
    actual=digest(ARCHIVE.read_bytes())
    if actual != expected: raise RuntimeError('Input archive hash mismatch')
    prefix='HoTT_early_reassessment_rev26/'
    baseline=[]; count=0
    with zipfile.ZipFile(ARCHIVE) as z:
        if z.testzip() is not None: raise RuntimeError('Corrupt ZIP')
        seen=set()
        for info in z.infolist():
            if info.is_dir(): continue
            if not info.filename.startswith(prefix): raise RuntimeError('Unexpected prefix')
            rel=PurePosixPath(info.filename[len(prefix):])
            if rel.is_absolute() or '..' in rel.parts or str(rel) in seen: raise RuntimeError('Unsafe/duplicate member')
            seen.add(str(rel))
            if stat.S_ISLNK(info.external_attr >> 16): raise RuntimeError('Symlink rejected')
            dest=ROOT.joinpath(*rel.parts)
            if dest.exists(): raise RuntimeError('Refuse overwrite: '+str(rel))
            blob=z.read(info)
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(blob)
            os.chmod(dest,0o755 if (info.external_attr >> 16) & 0o111 else 0o644)
            count+=1
            if '.git' not in rel.parts: baseline.append({'path':str(rel),'bytes':len(blob),'sha256':digest(blob)})
    out=ROOT/'artifacts/r027'; out.mkdir(parents=True,exist_ok=True)
    checks=[git('rev-parse','HEAD'),git('branch','--show-current'),git('status','--porcelain'),git('remote','-v'),git('fsck','--full')]
    if checks[0]['stdout'].strip()!=meta['head']: raise RuntimeError('HEAD mismatch')
    if any(c['exit_code'] for c in checks): raise RuntimeError('Git check failed')
    result={'schema':'r027-baseline/v1','at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root':str(ROOT),'source':str(ARCHIVE),'source_sha256':actual,'inherited_head':meta['head'],'files_restored':count,'protected_non_git_files':baseline,'git_checks':checks,'scope':'Restoration and preservation only; no full semantic loading certified'}
    (out/'BASELINE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='protected_non_git_files'},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
