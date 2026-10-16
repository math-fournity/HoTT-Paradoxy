#!/usr/bin/env python3
"""Restore supplied rev30 bytes to a new worktree without executing archived code."""
from pathlib import Path, PurePosixPath
import zipfile, hashlib, json, stat, datetime
ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT.parent / 'HoTT_self_reflection_rev30_with_git.zip'
PREFIX = 'HoTT_self_reflection_rev30/'

def main():
    entries = []
    with zipfile.ZipFile(ARCHIVE) as z:
        if z.testzip() is not None:
            raise RuntimeError('Archive CRC error')
        for info in z.infolist():
            if not info.filename.startswith(PREFIX):
                raise ValueError('Unexpected archive prefix: ' + info.filename)
            rel = info.filename[len(PREFIX):]
            path = PurePosixPath(rel)
            if not rel or info.is_dir():
                continue
            if path.is_absolute() or '..' in path.parts or '\\' in rel:
                raise ValueError('Unsafe path: ' + rel)
            mode = info.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError('Symlink not restored: ' + rel)
            data = z.read(info)
            target = ROOT / rel
            if target.exists() and target.read_bytes() != data:
                raise ValueError('Refuse overwrite: ' + rel)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            if mode & 0o111:
                target.chmod(0o755)
            entries.append({'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
    art = ROOT / 'artifacts/r031'
    art.mkdir(parents=True, exist_ok=True)
    receipt = {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
               'archive': str(ARCHIVE), 'sha256': hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
               'root': str(ROOT), 'files': entries,
               'action': 'BYTE_RESTORE_ONLY_NO_ARCHIVED_CODE_EXECUTED'}
    (art/'RESTORE.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'root': str(ROOT), 'restored_files':len(entries), 'archive_sha256':receipt['sha256']},indent=2))
if __name__ == '__main__': main()
