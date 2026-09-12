#!/usr/bin/env python3
"""Read current artifacts by named paths; record emitted text, not understanding."""
from pathlib import Path
import argparse, json, hashlib, importlib.util, sys, zipfile, datetime, subprocess
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r032'
CORE=['认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md','HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md']
def sha(b): return hashlib.sha256(b).hexdigest()
def rt():
    p=ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py'
    spec=importlib.util.spec_from_file_location('r032_runtime',p)
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m

def main():
    p=argparse.ArgumentParser();p.add_argument('action',choices=['init','read','status']);p.add_argument('--page',type=int);a=p.parse_args()
    OUT.mkdir(exist_ok=True,parents=True)
    if a.action=='init':
        if (OUT/'BASE_PLAN.json').exists(): raise RuntimeError('Already initialized')
        plan=rt().plan(ROOT)
        (OUT/'BASE_PLAN.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
        manifest={}
        zpath=ROOT.parent/'HoTT_proof_reflection_rev31_with_git.zip'
        with zipfile.ZipFile(zpath) as z:
            if z.testzip(): raise RuntimeError('CRC failure')
            for ent in z.infolist():
                if ent.is_dir(): continue
                rel=ent.filename.split('/',1)[1];data=z.read(ent)
                if rel != '.git/index' and (ROOT/rel).read_bytes()!=data: raise RuntimeError('Restoration mismatch: '+rel)
                if not rel.startswith('.git/'): manifest[rel]=sha(data)
        restore={'archive':str(zpath),'archive_sha256':sha(zpath.read_bytes()),'files':manifest,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()}
        (OUT/'RESTORE.json').write_text(json.dumps(restore,ensure_ascii=False,indent=2)+'\n')
        pages=[]
        for rel in CORE:
            start=1;buf='';end=0
            for n,line in enumerate((ROOT/rel).read_text().splitlines(keepends=True),1):
                if buf and len((buf+line).encode())>18000:
                    pages.append({'path':rel,'start':start,'end':end,'text':buf});buf='';start=n
                buf+=line;end=n
            if buf: pages.append({'path':rel,'start':start,'end':end,'text':buf})
        (OUT/'CORE_PAGES.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'revision':plan['revision'],'snapshot':plan['snapshot'],'documents':len(plan['documents']),'bytes':plan['total_bytes'],'core_pages':len(pages),'restored_files':len(manifest)},ensure_ascii=False,indent=2))
    elif a.action=='read':
        ps=json.loads((OUT/'CORE_PAGES.json').read_text());page=ps[a.page-1]
        print(f"FULL TEXT PAGE {a.page}/{len(ps)} {page['path']} L{page['start']}-{page['end']}\n{page['text']}")
        r=OUT/'read_receipts';r.mkdir(exist_ok=True)
        (r/f'{a.page:03}.json').write_text(json.dumps({'path':page['path'],'start':page['start'],'end':page['end'],'sha256':sha(page['text'].encode()),'emitted_only':True},ensure_ascii=False)+'\n')
    else:
        print(json.dumps({'pages_emitted':sorted(p.name for p in (OUT/'read_receipts').glob('*.json')),'full_dynamic_loaded':False,'scope':'Full core emission alone does not certify complete skill admission.'},indent=2))
if __name__=='__main__': main()
