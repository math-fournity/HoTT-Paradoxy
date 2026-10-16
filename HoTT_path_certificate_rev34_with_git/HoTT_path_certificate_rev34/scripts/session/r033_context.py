"""Plan immutable inputs and emit full required core text; never certify cognition."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, shutil, subprocess, sys, urllib.request
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'artifacts/r033'
CORE=['认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md','HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md']
def js(x):return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def runtime():
    s=importlib.util.spec_from_file_location('r033_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m);return m

def main():
    a=argparse.ArgumentParser();a.add_argument('mode',choices=['init','read','status','probe']);a.add_argument('--first',type=int);a.add_argument('--last',type=int);x=a.parse_args()
    OUT.mkdir(parents=True,exist_ok=True)
    if x.mode=='init':
        p=runtime().plan(ROOT)
        dest=OUT/'BASE_PLAN.json'
        if dest.exists():raise FileExistsError(dest)
        dest.write_text(js(p));pages=[]
        for rel in CORE:
            start=1;buf='';end=0
            for n,l in enumerate((ROOT/rel).read_text().splitlines(keepends=True),1):
                if buf and len((buf+l).encode())>18000:
                    pages.append({'path':rel,'start':start,'end':end,'text':buf});start=n;buf=''
                buf+=l;end=n
            if buf:pages.append({'path':rel,'start':start,'end':end,'text':buf})
        (OUT/'CORE_PAGES.json').write_text(js(pages))
        print(js({'revision':p['revision'],'documents':len(p['documents']),'bytes':p['total_bytes'],'core_pages':len(pages),'snapshot':p['snapshot']}))
    elif x.mode=='read':
        pages=json.loads((OUT/'CORE_PAGES.json').read_text());records=OUT/'read_receipts';records.mkdir(exist_ok=True)
        for i in range(x.first,x.last+1):
            p=pages[i-1];actual=''.join((ROOT/p['path']).read_text().splitlines(keepends=True)[p['start']-1:p['end']])
            assert actual==p['text']
            print(f"FULL TEXT PAGE {i}/{len(pages)} {p['path']} L{p['start']}-{p['end']}\n{actual}")
            (records/f'{i:03}.json').write_text(js({k:v for k,v in p.items() if k!='text'}|{'sha256':hashlib.sha256(actual.encode()).hexdigest(),'model_understanding':'NOT_CERTIFIED'}))
    elif x.mode=='probe':
        r={'time_utc':datetime.now(timezone.utc).isoformat(),'tools':{t:shutil.which(t) for t in ['agda','lean','lake','coqc','rocq','ghc','apt-get','curl']},'commands':[]}
        for cmd in [['curl','-I','--max-time','8','https://github.com/agda/agda/releases'],['apt-cache','policy','agda-bin']]:
            try:
                v=subprocess.run(cmd,capture_output=True,text=True,timeout=12);r['commands'].append({'argv':cmd,'code':v.returncode,'stdout':v.stdout,'stderr':v.stderr})
            except Exception as e:r['commands'].append({'argv':cmd,'error':repr(e)})
        (OUT/'NATIVE_PROBE.json').write_text(js(r));print(js(r))
    else:
        pages=json.loads((OUT/'CORE_PAGES.json').read_text());read=sorted(p.stem for p in (OUT/'read_receipts').glob('*.json'))
        print(js({'pages':len(pages),'emitted':read,'full_dynamic_cognition':'NOT_CERTIFIED','compaction':'NOT_ASSERTED'}))
if __name__=='__main__':main()
