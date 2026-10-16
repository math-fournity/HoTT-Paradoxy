#!/usr/bin/env python3
"""Snapshot and full-text reader for R030. Never certifies model understanding."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r030'
def js(x): return json.dumps(x, ensure_ascii=False, indent=2)+'\n'
def runtime():
 p=ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py'
 s=importlib.util.spec_from_file_location('r030_cognition',p);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m

def main():
 a=argparse.ArgumentParser();a.add_argument('action',choices=['init','read','status']);a.add_argument('--page',type=int);x=a.parse_args();OUT.mkdir(exist_ok=True)
 if x.action=='init':
  if (OUT/'BASE_PLAN.json').exists():raise RuntimeError('Already initialized')
  p=runtime().plan(ROOT);(OUT/'BASE_PLAN.json').write_text(js(p))
  base={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in ROOT.rglob('*') if f.is_file() and '.git' not in f.relative_to(ROOT).parts and str(f.relative_to(ROOT))!='artifacts/r030/BASE_PLAN.json'}
  (OUT/'BASELINE.json').write_text(js({'source_zip':'/mnt/data/HoTT_self_reference_rev29_with_git.zip','head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'files':base}))
  pages=[];b=[];n=0
  for d in p['documents']:
   for i,line in enumerate((ROOT/d['path']).read_text().splitlines(keepends=True),1):
    if b and n+len(line)>10000:pages.append(b);b=[];n=0
    if b and b[-1]['path']==d['path'] and b[-1]['end']==i-1:b[-1]['end']=i;b[-1]['text']+=line
    else:b.append({'path':d['path'],'start':i,'end':i,'text':line})
    n+=len(line)
  if b:pages.append(b)
  (OUT/'LOAD_PAGES.json').write_text(js(pages))
  print(js({'revision':p['revision'],'documents':len(p['documents']),'bytes':p['total_bytes'],'pages':len(pages),'snapshot':p['snapshot']}))
 elif x.action=='read':
  p=json.loads((OUT/'BASE_PLAN.json').read_text());pages=json.loads((OUT/'LOAD_PAGES.json').read_text());i=x.page-1
  assert runtime().plan(ROOT)['snapshot']==p['snapshot'],'Changed input snapshot'
  assert 0<=i<len(pages)
  print(f'FULL_TEXT_PAGE {i+1}/{len(pages)}')
  for s in pages[i]:print(f"\n=== {s['path']} L{s['start']}-{s['end']} ===\n"+s['text'],end='')
  dest=OUT/'load_receipts';dest.mkdir(exist_ok=True)
  (dest/f'{i+1:03}.json').write_text(js({'page':i+1,'snapshot':p['snapshot'],'segments':[{k:v for k,v in s.items() if k!='text'} for s in pages[i]],'model_understanding':'NOT_CERTIFIED'}))
 else:
  pages=json.loads((OUT/'LOAD_PAGES.json').read_text());read=sorted(int(f.stem) for f in (OUT/'load_receipts').glob('*.json')) if (OUT/'load_receipts').exists() else []
  print(js({'total_pages':len(pages),'emitted':read,'missing':sorted(set(range(1,len(pages)+1))-set(read))}))
if __name__=='__main__':main()
