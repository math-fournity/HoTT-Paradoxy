#!/usr/bin/env python3
"""Save a current cognition plan and emit bounded full-text chunks.
Byte coverage is never described as a semantic understanding certificate.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT/'artifacts/r017/cognition'
ENGINE = ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py'

def runtime():
    spec=importlib.util.spec_from_file_location('r017_governance_engine',ENGINE)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=mod
    spec.loader.exec_module(mod)
    return mod

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--init', action='store_true')
    ap.add_argument('--page', type=int)
    ap.add_argument('--status', action='store_true')
    ap.add_argument('--budget',type=int,default=18000)
    a=ap.parse_args()
    rt=runtime()
    OUT.mkdir(parents=True,exist_ok=True)
    if a.init:
        if (OUT/'PLAN.json').exists():raise RuntimeError('Plan exists; no overwriting prior snapshot')
        plan=rt.plan(ROOT)
        pages=[];parts=[];size=0
        for row in plan['documents']:
            lines=(ROOT/row['path']).read_text().splitlines(keepends=True)
            for number,line in enumerate(lines,1):
                count=len(line.encode())
                if size+count+300>a.budget and parts:
                    pages.append(parts);parts=[];size=0
                if parts and parts[-1]['path']==row['path'] and parts[-1]['end_line']==number-1:
                    parts[-1]['text']+=line;parts[-1]['end_line']=number
                else:
                    parts.append({'path':row['path'],'start_line':number,'end_line':number,'text':line});size+=200
                size+=count
        if parts:pages.append(parts)
        (OUT/'PLAN.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
        (OUT/'PAGES.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'snapshot':plan['snapshot'],'revision':plan['revision'],'documents':len(plan['documents']),
                          'total_bytes':plan['total_bytes'],'pages':len(pages),
                          'largest_docs':sorted([{'path':r['path'],'bytes':r['bytes']} for r in plan['documents']],key=lambda r:-r['bytes'])[:10]},ensure_ascii=False,indent=2))
        return
    plan=json.loads((OUT/'PLAN.json').read_text());pages=json.loads((OUT/'PAGES.json').read_text())
    if rt.plan(ROOT)['snapshot']!=plan['snapshot']:raise RuntimeError('Snapshot changed')
    if a.page is not None:
        if not 1<=a.page<=len(pages):raise ValueError('Page out of range')
        print(f'FULL_BODY_PAGE {a.page}/{len(pages)}')
        for p in pages[a.page-1]:
            print(f"\n===== {p['path']} lines {p['start_line']}--{p['end_line']} =====\n{p['text']}",end='')
        receipt={'page':a.page,'snapshot':plan['snapshot'],'pieces':[{k:v for k,v in p.items() if k!='text'}|{'sha256':hashlib.sha256(p['text'].encode()).hexdigest()} for p in pages[a.page-1]],'scope':'stdout emitted; model reception, retention and semantics not certified'}
        (OUT/f'emitted-{a.page:03}.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
    elif a.status:
        read=sorted(int(p.stem.split('-')[1]) for p in OUT.glob('emitted-*.json'))
        print(json.dumps({'emitted_pages':read,'total_pages':len(pages),'missing_pages':[i for i in range(1,len(pages)+1) if i not in read],'model_full_cognition':'NOT_CERTIFIED_BY_TOOL'},ensure_ascii=False))
    else:ap.error('Choose --init, --page or --status')

if __name__=='__main__':main()
