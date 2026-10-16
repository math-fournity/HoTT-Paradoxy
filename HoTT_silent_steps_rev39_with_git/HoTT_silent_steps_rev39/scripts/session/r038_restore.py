"""Restore exact R037 archive; preserve its Git history and refuse file replacement."""
from pathlib import Path, PurePosixPath
import hashlib, json, stat, subprocess, zipfile
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[2]
ARCHIVE=Path('/mnt/data/HoTT_transition_abstraction_rev37_with_git.zip')
PREFIX='HoTT_transition_abstraction_rev36/'
EXPECTED='515da9f6143fb5fd545031fa9648a5a002d75c2b'
def sha(b): return hashlib.sha256(b).hexdigest()
def main():
    files={}
    with zipfile.ZipFile(ARCHIVE) as z:
        if z.testzip() is not None: raise ValueError('CRC failure')
        for e in z.infolist():
            if not e.filename.startswith(PREFIX): raise ValueError(e.filename)
            r=e.filename[len(PREFIX):]; p=PurePosixPath(r); mode=e.external_attr>>16
            if not r: continue
            if p.is_absolute() or '..' in p.parts or stat.S_ISLNK(mode): raise ValueError(r)
            target=ROOT.joinpath(*p.parts)
            if e.is_dir(): target.mkdir(parents=True,exist_ok=True); continue
            b=z.read(e); target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=b: raise ValueError('Refuse overwrite '+r)
            target.write_bytes(b)
            if mode&0o111: target.chmod(0o755)
            if '.git' not in p.parts: files[r]=sha(b)
    def git(*a): return subprocess.check_output(['git',*a],cwd=ROOT,text=True).strip()
    assert git('rev-parse','HEAD')==EXPECTED
    out=ROOT/'artifacts/r038';out.mkdir(parents=True,exist_ok=True)
    receipt=dict(source=str(ARCHIVE),source_sha256=sha(ARCHIVE.read_bytes()),root=str(ROOT),head=git('rev-parse','HEAD'),branch=git('branch','--show-current'),remotes=git('remote','-v'),status=git('status','--porcelain'),utc=datetime.now(timezone.utc).isoformat(),baseline_files=files)
    (out/'RESTORE.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='baseline_files'},ensure_ascii=False,indent=2))
    print('restored non-Git files:',len(files))
if __name__=='__main__': main()
