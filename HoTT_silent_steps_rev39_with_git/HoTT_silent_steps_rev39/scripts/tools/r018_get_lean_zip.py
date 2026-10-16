"""Isolated official Lean 4.0.0 ZIP fetch; not a global install or current-version claim."""
from pathlib import Path, PurePosixPath
import hashlib, json, stat, time, urllib.request, zipfile
R=Path(__file__).resolve().parents[2];OUT=R/'artifacts/r018'
URL='https://github.com/leanprover/lean4/releases/download/v4.0.0/lean-4.0.0-linux.zip'
D=Path('/mnt/data/lean-audit-tools'); D.mkdir(exist_ok=True)
log={'url':URL,'version_requested':'v4.0.0','global_install':False,'start':time.time()}
try:
    f=D/'lean-4.0.0-linux.zip'
    if not f.exists():
        req=urllib.request.Request(URL,headers={'User-Agent':'HoTT-audit/1.0'})
        with urllib.request.urlopen(req,timeout=20) as response, f.open('wb') as o:
            n=0
            while True:
                b=response.read(1024*1024)
                if not b: break
                n+=len(b)
                if n>400*1024*1024 or time.time()-log['start']>150:raise RuntimeError('Download bound exceeded')
                o.write(b)
    h=hashlib.sha256()
    with f.open('rb') as i:
        for b in iter(lambda:i.read(1024*1024),b''):h.update(b)
    log.update(bytes=f.stat().st_size,sha256=h.hexdigest())
    with zipfile.ZipFile(f) as z:
        for i in z.infolist():
            p=PurePosixPath(i.filename)
            if p.is_absolute() or '..' in p.parts:raise ValueError('Unsafe tool archive path')
            dest=D.joinpath(*p.parts)
            if i.is_dir():dest.mkdir(parents=True,exist_ok=True);continue
            mode=i.external_attr>>16
            if stat.S_ISLNK(mode):
                target=z.read(i).decode(); resolved=(dest.parent/target).resolve()
                resolved.relative_to(D.resolve())
                dest.parent.mkdir(parents=True,exist_ok=True)
                if not dest.exists():dest.symlink_to(target)
                continue
            dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(i))
            if mode&0o111:dest.chmod(0o755)
    log['executable']=str(D/'lean-4.0.0-linux/bin/lean');log['status']='AVAILABLE'
except Exception as e:log['status']='UNAVAILABLE';log['error']=f'{type(e).__name__}: {e}'
log['end']=time.time();(OUT/'LEAN_ACCESS.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n');print(json.dumps(log,ensure_ascii=False,indent=2))
