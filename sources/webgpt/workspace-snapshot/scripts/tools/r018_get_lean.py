"""Bounded, isolated download of an official pinned Lean executable; no global install.
Failure is recorded and never reported as a completed kernel verification.
"""
from pathlib import Path
import hashlib, importlib.util, json, sys, time, urllib.request
R=Path(__file__).resolve().parents[2]
OUT=R/'artifacts/r018';OUT.mkdir(parents=True,exist_ok=True)
URL='https://github.com/leanprover/lean4/releases/download/v4.0.0/lean-4.0.0-linux.tar.zst'
DEST=Path('/mnt/data/lean-audit-tools');DEST.mkdir(exist_ok=True)
record={'url':URL,'version_requested':'v4.0.0','purpose':'Test ordinary Lean Eq, not formalize HoTT internally','global_install':False,'start':time.time()}
try:
    if importlib.util.find_spec('zstandard') is None:
        raise RuntimeError('zstandard module unavailable; no package installation attempted')
    import zstandard, tarfile
    target=DEST/'lean-4.0.0-linux.tar.zst'
    if not target.exists():
        req=urllib.request.Request(URL,headers={'User-Agent':'HoTT-audit/1.0'})
        with urllib.request.urlopen(req,timeout=20) as response, target.open('wb') as f:
            size=0
            while True:
                block=response.read(1024*1024)
                if not block:break
                size+=len(block)
                if size>300*1024*1024:raise RuntimeError('download size limit exceeded')
                f.write(block)
    record['bytes']=target.stat().st_size
    record['sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
    with target.open('rb') as fh, zstandard.ZstdDecompressor().stream_reader(fh) as reader, tarfile.open(fileobj=reader,mode='r|') as tf:
        for member in tf:
            path=Path(member.name)
            if path.is_absolute() or '..' in path.parts:raise RuntimeError('unsafe tool archive path')
            tf.extract(member,path=DEST,filter='data')
    record['executable']=str(DEST/'lean-4.0.0-linux/bin/lean')
    record['status']='AVAILABLE'
except Exception as e:
    record['status']='UNAVAILABLE';record['error']=f'{type(e).__name__}: {e}'
record['end']=time.time()
(OUT/'LEAN_ACCESS.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
