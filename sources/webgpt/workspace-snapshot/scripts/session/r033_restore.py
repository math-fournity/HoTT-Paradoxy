"""Restore the exact revision32 archive into this new working tree; keep receipt."""
from pathlib import Path, PurePosixPath
import hashlib, json, stat, subprocess, zipfile
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT.parent / 'HoTT_restricted_reflection_rev32_with_git.zip'
PREFIX = 'HoTT_restricted_reflection_rev32/'
def main():
    entries = []
    with zipfile.ZipFile(ARCHIVE) as z:
        if sum(i.file_size for i in z.infolist()) > 500_000_000:
            raise ValueError('archive size guard')
        for info in z.infolist():
            if info.is_dir():
                continue
            if not info.filename.startswith(PREFIX):
                raise ValueError(info.filename)
            rel = PurePosixPath(info.filename[len(PREFIX):])
            if rel.is_absolute() or '..' in rel.parts or stat.S_ISLNK(info.external_attr >> 16):
                raise ValueError('unsafe archive entry')
            dest = ROOT.joinpath(*rel.parts)
            if dest.exists():
                raise FileExistsError(dest)
            data = z.read(info)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            dest.chmod(0o755 if (info.external_attr >> 16) & 0o111 else 0o644)
            entries.append({'path': str(rel), 'sha256': hashlib.sha256(data).hexdigest(), 'bytes':len(data)})
    runs = []
    for args in [['git','rev-parse','HEAD'],['git','status','--porcelain=v1'],['git','branch','--show-current'],['git','remote','-v'],['git','fsck','--full']]:
        r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
        runs.append({'argv':args,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
        if r.returncode: raise RuntimeError(r.stderr)
    expected='d06c13832fb315a3d1a441164f8ad9e4d6b85c71'
    if runs[0]['stdout'].strip()!=expected: raise ValueError('wrong Git baseline')
    receipt={'time_utc':datetime.now(timezone.utc).isoformat(),'root':str(ROOT),'archive':str(ARCHIVE),'archive_sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),'baseline_head':expected,'files':entries,'commands':runs}
    out=ROOT/'artifacts/r033/RESTORE.json';out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'baseline_head':expected,'restored_files':len(entries),'bytes':sum(e['bytes'] for e in entries),'receipt':str(out),'commands':runs},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
