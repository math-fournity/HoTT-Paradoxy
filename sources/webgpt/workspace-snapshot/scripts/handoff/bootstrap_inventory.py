#!/usr/bin/env python3
"""Inventory only the currently mounted project materials; restore the R039 baseline safely.
No credential contents, unrelated system files, or external connectors are read.
"""
from __future__ import annotations
import hashlib, json, os, shutil, stat, zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
ROOT = Path('/mnt/data/HoTT_AI_HANDOFF_20260911')
DATA = Path('/mnt/data')
BASE = DATA/'HoTT_silent_steps_rev39_with_git.zip'
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()
def dump(p,x):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
    entries=[]; errors=[]; roots=[]
    for top in sorted(DATA.iterdir()):
        if top == ROOT or top.name.startswith('HoTT_AI_HANDOFF_20260911'): continue
        roots.append(str(top))
        for p in ([top] if not top.is_dir() else sorted(top.rglob('*'))):
            try:
                if p.is_symlink():
                    entries.append({'source':str(p),'relative':p.relative_to(DATA).as_posix(),'kind':'symlink','target':os.readlink(p)})
                elif p.is_file():
                    entries.append({'source':str(p),'relative':p.relative_to(DATA).as_posix(),'kind':'file','size':p.stat().st_size,'sha256':sha(p)})
            except OSError as e: errors.append({'path':str(p),'error':str(e)})
    probes=[]
    for d in ['/.codex','/root/.codex','/home/oai/.codex','/home/oai/share','/tmp','/workspace','/workspaces','/Volumes/D/ALL-Markdown','/Users/aurolafly']:
        p=Path(d); r={'path':d,'exists':p.exists(),'contents_read':False}
        if p.is_dir():
            try:
                r['immediate_names']=sorted(c.name for c in p.iterdir())
                r['scope']='name-only; no credentials or generic runtime content collected'
            except OSError as e: r['error']=str(e)
        probes.append(r)
    dump(ROOT/'manifests/SOURCE_INVENTORY.json',{'schema':'hott.source-inventory.v1','timestamp_utc':datetime.now(timezone.utc).isoformat(),'scope':'current /mnt/data files existing before handoff build; named external path probes only','roots':roots,'entries':entries,'errors':errors,'external_probes':probes,'total_file_bytes':sum(e.get('size',0) for e in entries),'no_claim_about_previous_ephemeral_files':True})
    extracted=[]
    with zipfile.ZipFile(BASE) as z:
        prefix='HoTT_silent_steps_rev39/'
        for info in z.infolist():
            if not info.filename.startswith(prefix): raise ValueError('Unexpected archive root')
            r=PurePosixPath(info.filename[len(prefix):])
            if str(r)=='.': continue
            if r.is_absolute() or '..' in r.parts: raise ValueError('Unsafe archive path')
            if stat.S_ISLNK(info.external_attr>>16): raise ValueError('Symlink baseline needs manual review')
            dest=ROOT/'workspace'/str(r)
            if info.is_dir(): dest.mkdir(parents=True,exist_ok=True); continue
            if dest.exists(): raise FileExistsError(dest)
            dest.parent.mkdir(parents=True,exist_ok=True)
            with z.open(info) as src, dest.open('wb') as out: shutil.copyfileobj(src,out)
            mode=(info.external_attr>>16)&0o777
            if mode: dest.chmod(mode)
            extracted.append({'path':str(r),'size':info.file_size,'sha256':sha(dest)})
    dump(ROOT/'manifests/BASELINE_R039.json',{'archive':str(BASE),'archive_sha256':sha(BASE),'entries':extracted,'files':len(extracted)})
    print(json.dumps({'source_files':len(entries),'bytes':sum(e.get('size',0) for e in entries),'baseline_files':len(extracted),'errors':errors},ensure_ascii=False))
if __name__=='__main__': main()
