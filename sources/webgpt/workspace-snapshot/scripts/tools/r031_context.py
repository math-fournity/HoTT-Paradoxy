#!/usr/bin/env python3
"""Plan all governed inputs, print bounded full-text pages, never certify understanding."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, sys
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'artifacts/r031'
CLOSURE='认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md'
QUESTIONS='HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md'
def rt():
 p=ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py'
 s=importlib.util.spec_from_file_location('r031_cognition',p);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m
def main():
 a=argparse.ArgumentParser();a.add_argument('action',choices=['init','read','status']);a.add_argument('--page',type=int,default=1);x=a.parse_args()
 if x.action=='init':
  plan=rt().plan(ROOT);(OUT/'BASE_PLAN.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
  pages=[]
  for rel in [CLOSURE,QUESTIONS]:
   lines=(ROOT/rel).read_text().splitlines(keepends=True); buf='';start=1;end=0
   for n,line in enumerate(lines,1):
    if buf and len((buf+line).encode())>20000:
     pages.append({'path':rel,'start':start,'end':end,'text':buf});buf='';start=n
    buf+=line;end=n
   if buf:pages.append({'path':rel,'start':start,'end':end,'text':buf})
  (OUT/'CORE_PAGES.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2)+'\n')
  print(json.dumps({'revision':plan['revision'],'all_documents':len(plan['documents']),'all_bytes':plan['total_bytes'],'core_pages':len(pages),'snapshot':plan['snapshot']},ensure_ascii=False,indent=2))
 elif x.action=='read':
  ps=json.loads((OUT/'CORE_PAGES.json').read_text());p=ps[x.page-1]
  print(f"PAGE {x.page}/{len(ps)} FULL TEXT {p['path']} L{p['start']}-{p['end']}\n"+p['text'])
  r=OUT/'read_receipts';r.mkdir(exist_ok=True);(r/f'{x.page:03}.json').write_text(json.dumps({k:v for k,v in p.items() if k!='text'},ensure_ascii=False)+'\n')
 else:
  ps=json.loads((OUT/'CORE_PAGES.json').read_text());seen=sorted(int(p.stem) for p in (OUT/'read_receipts').glob('*.json'))
  print(json.dumps({'core_pages':len(ps),'emitted':seen,'all_dynamic_full_text_loaded':False,'note':'Disk traversal and previous receipts are not context loading.'},indent=2))
if __name__=='__main__':main()
