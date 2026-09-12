#!/usr/bin/env python3
"""Restore supplied revision 21 safely, retaining its Git history and byte identity."""
from pathlib import Path, PurePosixPath
import hashlib, json, stat, zipfile

ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path('/mnt/data/HoTT_Gemini_synthesis_rev21_with_git.zip')
PREFIX = 'HoTT_Gemini_synthesis_rev21/'
REPORT = ROOT / 'artifacts/r022/RESTORE.json'

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> None:
    if REPORT.exists():
        raise SystemExit('Restore already recorded; refusing to overwrite.')
    rows = []
    with zipfile.ZipFile(SOURCE) as archive:
        for info in archive.infolist():
            if info.is_dir():
                continue
            if not info.filename.startswith(PREFIX):
                raise ValueError(f'Unexpected archive root: {info.filename}')
            rel = PurePosixPath(info.filename[len(PREFIX):])
            if rel.is_absolute() or '..' in rel.parts or '\\' in str(rel):
                raise ValueError(f'Unsafe path: {rel}')
            mode = (info.external_attr >> 16) & 0xffff
            if stat.S_ISLNK(mode):
                raise ValueError(f'Symlink requires explicit review: {rel}')
            target = ROOT.joinpath(*rel.parts)
            target.resolve().relative_to(ROOT)
            data = archive.read(info)
            if target.exists() and target.read_bytes() != data:
                raise ValueError(f'Conflicting existing file: {rel}')
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists():
                target.write_bytes(data)
                target.chmod(0o755 if mode & 0o111 else 0o644)
            if target.read_bytes() != data:
                raise ValueError(f'Readback mismatch: {rel}')
            rows.append({'path': str(rel), 'bytes': len(data), 'sha256': sha(data)})
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps({'source': str(SOURCE), 'source_sha256': sha(SOURCE.read_bytes()),
        'root': str(ROOT), 'status': 'RESTORED_BYTE_VERIFIED', 'files': rows,
        'git_history': 'retained, not reinitialized', 'source_scripts_executed': False},
        ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'root': str(ROOT), 'files_restored': len(rows), 'report': str(REPORT)}, ensure_ascii=False))

if __name__ == '__main__':
    main()
