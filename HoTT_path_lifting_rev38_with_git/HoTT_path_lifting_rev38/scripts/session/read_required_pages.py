#!/usr/bin/env python3
"""Display actual full-text pages with bounded output; receipts do not certify cognition."""
from pathlib import Path
import argparse,hashlib,importlib.util,json
ROOT=Path(__file__).resolve().parents[2]
ENGINE=ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py'
spec=importlib.util.spec_from_file_location('cognition',ENGINE);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--init',action='store_true');ap.add_argument('--page',type=int);ap.add_argument('--chars',type=int,default=21000);a=ap.parse_args();out=ROOT/'artifacts/cognition';out.mkdir(exist_ok=True,parents=True)
 if a.init:
  if (out/'PLAN.json').exists():raise SystemExit('Already initialized; retain immutable read plan')
  plan=mod.plan(ROOT);pages=[];buf=[];size=0
  for doc in plan['documents']:
   ls=(ROOT/doc['path']).read_text().splitlines(keepends=True);start=1
   for number,line in enumerate(ls,1):
    if size+len(line)+300>a.chars and buf:
     pages.append(buf);buf=[];size=0
    if buf and buf[-1]['path']==doc['path'] and buf[-1]['end_line']==number-1:
     buf[-1]['end_line']=number;buf[-1]['text']+=line
    else:buf.append({'path':doc['path'],'start_line':number,'end_line':number,'text':line});size+=200
    size+=len(line)
  if buf:pages.append(buf)
  (out/'PLAN.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
  (out/'PAGES.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2)+'\n')
  print(json.dumps({'snapshot':plan['snapshot'],'documents':len(plan['documents']),'bytes':plan['total_bytes'],'lines':plan['total_lines'],'pages':len(pages),'model_context':'NOT_CERTIFIED_BY_TOOL'},ensure_ascii=False))
 elif a.page is not None:
  plan=json.loads((out/'PLAN.json').read_text());assert mod.plan(ROOT)['snapshot']==plan['snapshot'],'Changed snapshot'
  pages=json.loads((out/'PAGES.json').read_text());idx=a.page-1
  if not 0<=idx<len(pages):raise SystemExit('Bad page')
  print(f'FULL_TEXT_PAGE {a.page}/{len(pages)}')
  for x in pages[idx]:print(f"\n===== {x['path']} L{x['start_line']}-{x['end_line']} =====\n"+x['text'],end='')
  rec=out/f'page-{a.page:03d}.json';rec.write_text(json.dumps({'page':a.page,'snapshot':plan['snapshot'],'emitted':[{'path':x['path'],'start_line':x['start_line'],'end_line':x['end_line'],'sha256':hashlib.sha256(x['text'].encode()).hexdigest()} for x in pages[idx]],'model_reception_or_understanding':'NOT_CERTIFIED'},ensure_ascii=False,indent=2)+'\n')
 else:ap.error('choose --init or --page')
if __name__=='__main__':main()
