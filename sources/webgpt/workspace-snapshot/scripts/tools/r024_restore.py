"""Restore the supplied rev23 repository without executing archived scripts/hooks."""
from pathlib import Path, PurePosixPath
import hashlib, json, stat, subprocess, zipfile

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT.parent / 'HoTT_Gemini_response_rev23_with_git.zip'
PREFIX = 'HoTT_Gemini_response_rev23'

def main():
    target = ROOT / 'artifacts/r024'
    target.mkdir(parents=True, exist_ok=True)
    files = []
    with zipfile.ZipFile(ARCHIVE) as z:
        for info in z.infolist():
            p = PurePosixPath(info.filename)
            if p.is_absolute() or '..' in p.parts or not p.parts or p.parts[0] != PREFIX:
                raise ValueError(f'Unsafe archive member: {info.filename}')
            if stat.S_ISLNK(info.external_attr >> 16):
                raise ValueError('Symlink member refused')
            rel = Path(*p.parts[1:])
            if not rel.parts: continue
            dest = ROOT / rel
            if info.is_dir():
                dest.mkdir(parents=True, exist_ok=True); continue
            b = z.read(info)
            if dest.exists() and dest.read_bytes() != b:
                raise FileExistsError(str(dest))
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(b)
            files.append({'path':rel.as_posix(), 'bytes':len(b), 'sha256':hashlib.sha256(b).hexdigest()})
    records = []
    for args in [('rev-parse','HEAD'),('status','--porcelain'),('branch','--show-current'),('remote','-v')]:
        argv = ['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args]
        p = subprocess.run(argv,cwd=ROOT,capture_output=True,text=True,timeout=30)
        records.append({'argv':argv,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
        if p.returncode: raise RuntimeError(records[-1])
    assert records[0]['stdout'].strip() == '38d6d706fa7131719ccf94f24abd09b86e00ef17'
    assert not records[3]['stdout'].strip()
    result = {'archive':str(ARCHIVE),'archive_sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
              'root':str(ROOT),'files':files,'git':records,'archive_code_executed':False}
    (target/'RESTORE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'root':str(ROOT),'files':len(files),'head':records[0]['stdout'].strip(),'status':records[1]['stdout']},ensure_ascii=False))
if __name__=='__main__': main()
