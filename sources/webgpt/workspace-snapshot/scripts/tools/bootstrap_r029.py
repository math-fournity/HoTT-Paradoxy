#!/usr/bin/env python3
"""Restore the supplied rev28 archive without rewriting existing source bytes."""
import hashlib, json, os, stat, zipfile
from pathlib import Path, PurePosixPath
ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = Path('/mnt/data/HoTT_Gemini_review_rev28_with_git.zip')
PREFIX = 'HoTT_Gemini_review_rev28/'
records = []
with zipfile.ZipFile(ARCHIVE) as z:
    for info in z.infolist():
        if not info.filename.startswith(PREFIX):
            raise ValueError(f'Unexpected prefix: {info.filename}')
        rel = PurePosixPath(info.filename[len(PREFIX):])
        if rel.is_absolute() or '..' in rel.parts:
            raise ValueError(f'Unsafe path: {rel}')
        mode = info.external_attr >> 16
        if stat.S_ISLNK(mode):
            raise ValueError(f'Symlink not accepted: {rel}')
        if info.is_dir():
            (ROOT / str(rel)).mkdir(parents=True, exist_ok=True)
            continue
        data = z.read(info)
        target = ROOT / str(rel)
        if target.exists() and target.read_bytes() != data:
            raise FileExistsError(str(target))
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        if mode & 0o111:
            target.chmod(0o755)
        if '.git' not in rel.parts:
            records.append({'path': str(rel), 'sha256': hashlib.sha256(data).hexdigest(), 'bytes':len(data)})
out = ROOT / 'artifacts/r029'
out.mkdir(parents=True, exist_ok=True)
receipt = {'archive':str(ARCHIVE),'archive_sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
           'source_prefix':PREFIX, 'restored_root':str(ROOT), 'files':records}
(out/'BASELINE.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'root':str(ROOT),'files_excluding_git':len(records),'archive_sha256':receipt['archive_sha256']},indent=2))
