#!/usr/bin/env python3
"""Recover the current snapshot and emit bounded, recorded source ranges. No cognition certification."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, shutil, subprocess, sys
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'artifacts/r039'
def dump(x): return json.dumps(x, ensure_ascii=False, indent=2) + '\n'
def sha(b): return hashlib.sha256(b).hexdigest()
def runtime():
    spec = importlib.util.spec_from_file_location('r039_runtime', ROOT / '.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt = importlib.util.module_from_spec(spec); sys.modules[spec.name] = rt; spec.loader.exec_module(rt); return rt
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('mode',choices=['init','read','status']); ap.add_argument('--path'); ap.add_argument('--start',type=int,default=1); ap.add_argument('--end',type=int); a=ap.parse_args()
    OUT.mkdir(parents=True,exist_ok=True)
    if a.mode=='init':
        if (OUT/'BASE_PLAN.json').exists(): raise FileExistsError('Baseline already saved')
        rt=runtime(); plan=rt.plan(ROOT); (OUT/'BASE_PLAN.json').write_text(dump(plan))
        state=(ROOT/'.codex/research/hott/STATE.json').read_bytes(); (OUT/'STATE_BASE.json').write_bytes(state)
        paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0')
        hashes={p:sha((ROOT/p).read_bytes()) for p in paths if p and (ROOT/p).is_file()}; (OUT/'BASE_TRACKED_HASHES.json').write_text(dump(hashes))
        z=ROOT.parent/'HoTT_path_lifting_rev38_with_git.zip'
        report=dict(root=str(ROOT),revision=json.loads(state)['revision'],head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),branch=subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip(),baseline_records=len(json.loads(state)['records']),planned_documents=len(plan['documents']),planned_bytes=plan['total_bytes'],source_zip=str(z),source_sha256=sha(z.read_bytes()),tools={x:shutil.which(x) for x in ['lean','agda','coqc','rocq']},utc=datetime.now(timezone.utc).isoformat(),cognition='NOT_CERTIFIED_FULL_COGNITION',compaction='NOT_ASSERTED')
        (OUT/'START.json').write_text(dump(report)); print(dump(report))
    elif a.mode=='read':
        p=(ROOT/a.path).resolve(); p.relative_to(ROOT)
        lines=p.read_text().splitlines(keepends=True); end=a.end or len(lines); text=''.join(lines[a.start-1:end])
        print(f'FILE {a.path} L{a.start}-{end}/{len(lines)}\n'+text)
        r=OUT/'reads'; r.mkdir(exist_ok=True); (r/(sha(a.path.encode())[:14]+f'-{a.start}-{end}.json')).write_text(dump(dict(path=a.path,start=a.start,end=end,total_lines=len(lines),sha256=sha(p.read_bytes()),emitted_sha256=sha(text.encode()),tool_does_not_certify_model_receipt=True)))
    else:
        report=dict(status='BLOCKED_FULL_COGNITION',basis='Full dynamic corpus not emitted; bounded local continuation only. No fabricated compaction claim.',receipts=[json.loads(p.read_text()) for p in sorted((OUT/'reads').glob('*.json'))],policy_unchanged=True)
        (OUT/'COGNITION_STATUS.json').write_text(dump(report)); print(dump({k:v for k,v in report.items() if k!='receipts'}))
if __name__=='__main__': main()
