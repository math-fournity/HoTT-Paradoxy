#!/usr/bin/env python3
"""Snapshot and print exact source text. Reading receipts are not cognition certification."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, subprocess, sys, shutil
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r038'
def js(x):return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def runtime():
    sp=importlib.util.spec_from_file_location('r038_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(sp);sys.modules[sp.name]=rt;sp.loader.exec_module(rt);return rt
def digest(b):return hashlib.sha256(b).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['init','page','file','status']);ap.add_argument('--page',type=int);ap.add_argument('--path');ap.add_argument('--start',type=int,default=1);ap.add_argument('--end',type=int);a=ap.parse_args();OUT.mkdir(exist_ok=True)
    if a.mode=='init':
        if (OUT/'BASE_PLAN.json').exists():raise FileExistsError('baseline exists')
        rt=runtime();plan=rt.plan(ROOT);(OUT/'BASE_PLAN.json').write_text(js(plan))
        pages=[]
        for doc in plan['documents']:
            lines=(ROOT/doc['path']).read_text().splitlines(keepends=True);chunk='';start=1
            for n,line in enumerate(lines,1):
                if chunk and len((chunk+line).encode())>14000:
                    pages.append(dict(path=doc['path'],start=start,end=n-1));chunk='';start=n
                chunk+=line
            if chunk:pages.append(dict(path=doc['path'],start=start,end=len(lines)))
        (OUT/'PAGES.json').write_text(js(pages))
        tracked=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0')
        hashes={p:digest((ROOT/p).read_bytes()) for p in tracked if p and (ROOT/p).is_file()}
        (OUT/'BASE_TRACKED_HASHES.json').write_text(js(hashes))
        (OUT/'STATE_BASE.json').write_bytes((ROOT/'.codex/research/hott/STATE.json').read_bytes())
        start=dict(root=str(ROOT),head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).decode().strip(),branch=subprocess.check_output(['git','branch','--show-current'],cwd=ROOT).decode().strip(),status=subprocess.check_output(['git','status','--porcelain'],cwd=ROOT).decode(),utc=datetime.now(timezone.utc).isoformat(),documents=len(plan['documents']),total_bytes=plan['total_bytes'],pages=len(pages),tools={x:shutil.which(x) for x in ['lean','agda','coqc','rocq','z3']},source='/mnt/data/HoTT_transition_abstraction_rev37_with_git.zip',source_sha256=digest(Path('/mnt/data/HoTT_transition_abstraction_rev37_with_git.zip').read_bytes()),full_cognition='NOT_CERTIFIED')
        (OUT/'START.json').write_text(js(start));print(js(start));print(js([dict(page=i+1,**p) for i,p in enumerate(pages[:14])]))
    elif a.mode=='page':
        plan=json.loads((OUT/'BASE_PLAN.json').read_text());assert runtime().plan(ROOT)['snapshot']==plan['snapshot']
        pages=json.loads((OUT/'PAGES.json').read_text());p=pages[a.page-1];text=''.join((ROOT/p['path']).read_text().splitlines(keepends=True)[p['start']-1:p['end']]);print(f"PAGE {a.page}/{len(pages)} {p['path']} L{p['start']}-{p['end']}\n{text}")
        d=OUT/'reads';d.mkdir(exist_ok=True);(d/f'{a.page:04d}.json').write_text(js(dict(**p,emitted_sha256=digest(text.encode()),understanding='NOT_CERTIFIED_BY_TOOL')))
    elif a.mode=='file':
        p=(ROOT/a.path).resolve();p.relative_to(ROOT);lines=p.read_text().splitlines(keepends=True);end=a.end or len(lines);text=''.join(lines[a.start-1:end]);print(f'{a.path} L{a.start}-{end}/{len(lines)}\n'+text)
        d=OUT/'direct_reads';d.mkdir(exist_ok=True);(d/(digest(a.path.encode())[:12]+f'-{a.start}-{end}.json')).write_text(js(dict(path=a.path,start=a.start,end=end,file_sha256=digest(p.read_bytes()),emitted_sha256=digest(text.encode()))))
    else:
        pages=json.loads((OUT/'PAGES.json').read_text());read=sorted(int(p.stem) for p in (OUT/'reads').glob('*.json'))
        r=dict(total_pages=len(pages),emitted_pages=read,full_cognition='NOT_CERTIFIED' if len(read)!=len(pages) else 'FULL_EMISSION_ONLY',compaction='NOT_ASSERTED');(OUT/'READ_STATUS.json').write_text(js(r));print(js(r))
if __name__=='__main__':main()
