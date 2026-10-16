#!/usr/bin/env python3
"""Bind R034 reads to an immutable plan; record actual emitted text, not understanding."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, subprocess, sys, shutil
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'artifacts/r034'
def dumps(x): return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def rt():
    s=importlib.util.spec_from_file_location('r034_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def sha(b): return hashlib.sha256(b).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['init','page','file','status']);ap.add_argument('--page',type=int);ap.add_argument('--path');ap.add_argument('--start',type=int,default=1);ap.add_argument('--end',type=int);a=ap.parse_args()
    OUT.mkdir(exist_ok=True)
    if a.mode=='init':
        p=rt().plan(ROOT)
        if (OUT/'BASE_PLAN.json').exists():raise FileExistsError('Existing baseline')
        (OUT/'BASE_PLAN.json').write_text(dumps(p)); pages=[]
        for row in p['documents']:
            rel=row['path'];buf='';first=1;end=0
            for num,line in enumerate((ROOT/rel).read_text().splitlines(keepends=True),1):
                if buf and len((buf+line).encode())>15500:
                    pages.append({'path':rel,'start':first,'end':end,'text':buf});buf='';first=num
                buf+=line;end=num
            if buf:pages.append({'path':rel,'start':first,'end':end,'text':buf})
        (OUT/'PAGES.json').write_text(dumps(pages))
        tracks=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0')
        hashes={f:sha((ROOT/f).read_bytes()) for f in tracks if f and (ROOT/f).is_file()}
        (OUT/'BASE_TRACKED_HASHES.json').write_text(dumps(hashes))
        ident={'utc':datetime.now(timezone.utc).isoformat(),'root':str(ROOT),'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).decode().strip(),'status':subprocess.check_output(['git','status','--short'],cwd=ROOT).decode(),'revision':p['revision'],'snapshot':p['snapshot'],'documents':len(p['documents']),'bytes':p['total_bytes'],'pages':len(pages),'tools':{t:shutil.which(t) for t in ['agda','lean','lake','coqc','rocq']},'request':'继续','authorization':'continue sandbox research, save scripts and local Git; no remote mutation','repo_cognitive_closure':'not present at .codex/skills/repo-cognitive-closure/SKILL.md'}
        (OUT/'START.json').write_text(dumps(ident));print(dumps(ident));print(dumps([{k:v for k,v in t.items() if k!='text'}|{'page':i+1} for i,t in enumerate(pages[:18])]))
    elif a.mode=='page':
        p=json.loads((OUT/'BASE_PLAN.json').read_text());pages=json.loads((OUT/'PAGES.json').read_text())
        if rt().plan(ROOT)['snapshot']!=p['snapshot']:raise RuntimeError('Snapshot changed')
        t=pages[a.page-1];text=''.join((ROOT/t['path']).read_text().splitlines(keepends=True)[t['start']-1:t['end']]);assert text==t['text']
        print(f"PAGE {a.page}/{len(pages)} {t['path']} L{t['start']}-{t['end']}\n{text}")
        d=OUT/'read_receipts';d.mkdir(exist_ok=True);(d/f'{a.page:04}.json').write_text(dumps({k:v for k,v in t.items() if k!='text'}|{'sha256':sha(text.encode()),'scope':'emitted only; no semantic certification'}))
    elif a.mode=='file':
        rel=Path(a.path);f=(ROOT/rel).resolve()
        if not f.is_relative_to(ROOT):raise ValueError('Outside root')
        lines=f.read_text().splitlines(keepends=True);end=a.end or len(lines);text=''.join(lines[a.start-1:end]);print(f'{rel} L{a.start}-{end}/{len(lines)}\n{text}')
        d=OUT/'direct_reads';d.mkdir(exist_ok=True);name=sha(str(rel).encode())[:12]+f'-{a.start}-{end}.json';(d/name).write_text(dumps({'path':str(rel),'start':a.start,'end':end,'sha256':sha(text.encode()),'file_sha256':sha(f.read_bytes())}))
    else:
        pages=json.loads((OUT/'PAGES.json').read_text());read=sorted(int(f.stem) for f in (OUT/'read_receipts').glob('*.json'))
        x={'pages_total':len(pages),'pages_emitted':read,'missing_pages':[i for i in range(1,len(pages)+1) if i not in read],'full_cognition':'NOT_CERTIFIED','compaction':'NOT_ASSERTED'}
        (OUT/'READ_STATUS.json').write_text(dumps(x));print(dumps(x))
if __name__=='__main__':main()
