"""Restore the supplied rev24 archive into a new auditable working tree.
No archive code is executed. Reject path escapes, links and overwrites.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path('/mnt/data/HoTT_Gemini_review_rev24_with_git.zip')
PREFIX = 'HoTT_Gemini_review_rev24/'

def main() -> None:
    rows = []
    with zipfile.ZipFile(SOURCE) as archive:
        seen = set()
        for member in archive.infolist():
            if not member.filename.startswith(PREFIX):
                raise ValueError('Unexpected archive prefix: ' + member.filename)
            name = member.filename[len(PREFIX):]
            if not name or member.is_dir():
                continue
            rel = PurePosixPath(name)
            if rel.is_absolute() or '..' in rel.parts or '\\' in name or name in seen:
                raise ValueError('Unsafe/duplicate path: ' + name)
            seen.add(name)
            mode = member.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError('Symlink rejected: ' + name)
            target = ROOT.joinpath(*rel.parts)
            target.resolve().relative_to(ROOT)
            if target.exists():
                raise FileExistsError(target)
            data = archive.read(member)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            target.chmod(0o755 if mode & 0o111 else 0o644)
            rows.append({'path':name, 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest()})
    out = ROOT / 'artifacts/r025'
    out.mkdir(parents=True, exist_ok=True)
    report = {'schema_version':'r025-restore/v1', 'source':str(SOURCE),
              'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'root':str(ROOT), 'member_count':len(rows), 'members':rows,
              'existing_uploaded_sparse_directory_modified':False}
    (out/'RESTORE.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='members'}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
