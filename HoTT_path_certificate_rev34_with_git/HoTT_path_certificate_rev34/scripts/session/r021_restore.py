"""Restore supplied revision20 archive safely, preserving Git history and input identity."""
from pathlib import Path, PurePosixPath
import datetime, hashlib, json, os, stat, subprocess, zipfile
R = Path(__file__).resolve().parents[2]
Z = Path('/mnt/data/HoTT_Gemini_debate_rev20_with_git.zip')
EXPECTED_HEAD = '3e529cd4ea00124347afa1195aaa3ccc1619b46e'
PREFIX = 'HoTT_Gemini_debate_rev20/'
O = R/'artifacts/r021'

def digest(b): return hashlib.sha256(b).hexdigest()

def git(*args):
    p = subprocess.run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd=R,capture_output=True,text=True,timeout=60)
    if p.returncode: raise RuntimeError(p.stderr)
    return p.stdout.strip()

if (R/'.git').exists(): raise RuntimeError('Refuse repeated restoration')
rows=[]
with zipfile.ZipFile(Z) as z:
    if z.testzip() is not None: raise RuntimeError('ZIP CRC failure')
    seen=set()
    for i in z.infolist():
        if not i.filename.startswith(PREFIX): raise RuntimeError('Wrong archive root')
        name=i.filename[len(PREFIX):]
        if not name or i.is_dir(): continue
        rel=PurePosixPath(name)
        if rel.is_absolute() or any(x in ('','..','.') for x in name.split('/')) or '\\' in name: raise RuntimeError('Unsafe path')
        if name in seen: raise RuntimeError('Duplicate member')
        seen.add(name)
        mode=(i.external_attr>>16)&0xFFFF
        if stat.S_ISLNK(mode): raise RuntimeError('Symlink member rejected')
        target=R.joinpath(*rel.parts)
        if target.exists(): raise RuntimeError('Refuse overwrite '+name)
        b=z.read(i); target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(b)
        if mode&0o111: target.chmod(0o755)
        rows.append({'path':name,'bytes':len(b),'sha256':digest(b)})
assert git('rev-parse','HEAD')==EXPECTED_HEAD
assert git('remote')==''
# The newly authored restoration script is expected to be the only initial untracked content.
tracked=git('diff','--name-only','HEAD')
assert not tracked, tracked
O.mkdir(parents=True,exist_ok=True)
report={'schema_version':'r021-restore/v1','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':str(Z),'source_bytes':Z.stat().st_size,'source_sha256':digest(Z.read_bytes()),'expected_head':EXPECTED_HEAD,'actual_head':git('rev-parse','HEAD'),'branch':git('branch','--show-current'),'files':len(rows),'tracked_changes_after_restore':tracked,'no_remote':True,'path':str(R),'scope':'User-relayed reply assessment and research planning; not a new proof execution'}
(O/'RESTORE.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(O/'BASELINE_FILES.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items()},ensure_ascii=False,indent=2))
