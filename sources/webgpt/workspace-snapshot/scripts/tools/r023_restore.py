"""Restore supplied revision22 into a fresh revision23 worktree, preserving Git bytes."""
from __future__ import annotations
import hashlib, json, stat, zipfile
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = Path('/mnt/data/HoTT_Gemini_reply_rev22_with_git.zip')
PREFIX = 'HoTT_Gemini_reply_rev22'

def main() -> None:
    report = ROOT / 'artifacts/r023/RESTORE.json'
    if report.exists():
        raise FileExistsError('Already restored; refusing a second import')
    rows = []
    with zipfile.ZipFile(ARCHIVE) as archive:
        entries = archive.infolist()
        if sum(i.file_size for i in entries) > 1024**3:
            raise ValueError('Unexpected expansion size')
        seen = set()
        for info in entries:
            parts = PurePosixPath(info.filename).parts
            if not parts or parts[0] != PREFIX or any(x in ('..', '') for x in parts):
                raise ValueError(f'Unsafe member: {info.filename!r}')
            if stat.S_ISLNK(info.external_attr >> 16):
                raise ValueError(f'Symlink member: {info.filename!r}')
            rel = PurePosixPath(*parts[1:])
            if str(rel) == '.' or info.is_dir():
                continue
            if rel in seen:
                raise ValueError(f'Duplicate: {rel}')
            seen.add(rel)
            out = ROOT.joinpath(*rel.parts)
            if out.exists():
                raise FileExistsError(str(out))
            out.parent.mkdir(parents=True, exist_ok=True)
            data = archive.read(info)
            out.write_bytes(data)
            rows.append({'path':rel.as_posix(), 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest()})
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps({'schema_version':'r023-restore/v1', 'at_utc':datetime.now(timezone.utc).isoformat(),
        'archive':str(ARCHIVE), 'archive_sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
        'root':str(ROOT), 'files':rows, 'file_count':len(rows),
        'scope':'Supplied revision22, not original-host full repository'}, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'root':str(ROOT),'restored_files':len(rows),'report':str(report)},ensure_ascii=False))

if __name__ == '__main__':
    main()
