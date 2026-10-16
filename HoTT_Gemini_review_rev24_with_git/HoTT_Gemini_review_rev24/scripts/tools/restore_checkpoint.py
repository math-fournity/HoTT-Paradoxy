#!/usr/bin/env python3
"""Restore a fresh workspace from a checkpoint; never overwrite an existing root."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, stat, zipfile

def digest(data): return hashlib.sha256(data).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('archive',type=Path);ap.add_argument('root',type=Path);args=ap.parse_args()
    if args.root.exists(): raise SystemExit('Refusing existing target')
    with zipfile.ZipFile(args.archive) as z:
        rows=[];seen=set()
        for i in z.infolist():
            p=PurePosixPath(i.filename)
            if p.is_absolute() or '..' in p.parts or '\\' in i.filename or stat.S_ISLNK(i.external_attr>>16): raise ValueError(i.filename)
            if i.filename in seen: raise ValueError('Duplicate path')
            seen.add(i.filename)
            if i.is_dir():continue
            data=z.read(i);rows.append((p,data))
        args.root.mkdir(parents=True)
        for p,data in rows:
            target=args.root.joinpath(*p.parts);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
    evidence=args.root/'artifacts/code-recovery';evidence.mkdir(parents=True)
    manifest={'source_archive':str(args.archive),'source_sha256':digest(args.archive.read_bytes()),'files':[
      {'path':str(p),'bytes':len(b),'sha256':digest(b)} for p,b in rows], 'interpretation':'Byte-for-byte latest supplied checkpoint, not original host git history'}
    (evidence/'RESTORE_BASELINE.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'root':str(args.root),'restored_files':len(rows),'archive_sha256':manifest['source_sha256']},indent=2))
if __name__=='__main__':main()
