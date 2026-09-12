#!/usr/bin/env python3
"""Restore the supplied rev25 snapshot into a fresh writable root; never run archive code."""
from pathlib import Path, PurePosixPath
import hashlib, json, stat, zipfile
ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = Path('/mnt/data/HoTT_Gemini_review_rev25_with_git.zip')
PREFIX = 'HoTT_Gemini_review_rev25/'

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main():
    rows = []
    with zipfile.ZipFile(ARCHIVE) as z:
        for info in z.infolist():
            if not info.filename.startswith(PREFIX):
                raise ValueError(f'Unexpected prefix: {info.filename}')
            rel = PurePosixPath(info.filename[len(PREFIX):])
            if rel.is_absolute() or '..' in rel.parts:
                raise ValueError('Unsafe path')
            mode = info.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError(f'Symlink not allowed: {rel}')
            target = ROOT / rel
            if info.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            data = z.read(info)
            if target.exists():
                raise FileExistsError(target)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            if mode & 0o111:
                target.chmod(0o755)
            rows.append({'path': str(rel), 'bytes': len(data), 'sha256': sha(data)})
    out = ROOT / 'artifacts/r026'
    out.mkdir(parents=True, exist_ok=True)
    receipt = {'archive': str(ARCHIVE), 'archive_sha256': sha(ARCHIVE.read_bytes()),
               'root': str(ROOT), 'restored_files': len(rows), 'files': rows,
               'archive_code_executed': False}
    (out / 'RESTORE.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in receipt.items() if k != 'files'}, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
