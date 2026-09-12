#!/usr/bin/env python3
"""Restore the supplied revision-16 archive without executing archived code.
Run after saving this file; retain it in the delivered scripts directory.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--archive', type=Path, required=True)
    parser.add_argument('--root', type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    root.mkdir(parents=True, exist_ok=True)
    prefix = 'HoTT_workspace_rev16/'
    rows, targets = [], set()
    with zipfile.ZipFile(args.archive) as archive:
        infos = archive.infolist()
        for info in infos:
            name = info.filename
            if not name.startswith(prefix):
                raise ValueError(f'Unexpected archive root: {name!r}')
            rel = name[len(prefix):]
            if not rel:
                continue
            path = PurePosixPath(rel)
            if path.is_absolute() or '..' in path.parts or '\\' in rel:
                raise ValueError(f'Unsafe name {name!r}')
            if stat.S_ISLNK(info.external_attr >> 16):
                raise ValueError(f'Symlink rejected: {name}')
            dest = root.joinpath(*path.parts)
            dest.resolve().relative_to(root)
            if rel in targets:
                raise ValueError(f'Duplicate path: {rel}')
            targets.add(rel)
            if info.is_dir():
                dest.mkdir(parents=True, exist_ok=True)
                continue
            data = archive.read(info)
            if dest.exists() and dest.read_bytes() != data:
                raise ValueError(f'Refusing different existing content: {dest}')
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists():
                dest.write_bytes(data)
            mode = (info.external_attr >> 16) & 0o777
            if mode:
                dest.chmod(mode & ~0o022)
            rows.append({'path': rel, 'bytes': len(data), 'sha256': sha(data)})
    out = root / 'artifacts/r017/bootstrap'
    out.mkdir(parents=True, exist_ok=True)
    report = {'archive': str(args.archive), 'archive_sha256': sha(args.archive.read_bytes()),
              'workspace': str(root), 'files': rows,
              'note': 'Restored original .git; did not initialize new history or execute archived scripts.'}
    (out / 'restore-manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'root': str(root), 'restored_files': len(rows),
                      'archive_sha256': report['archive_sha256'], 'git_exists': (root/'.git').is_dir()}, indent=2))

if __name__ == '__main__':
    main()
