#!/usr/bin/env python3
"""Rerun only the read-and-reviewed pure R015 experiment; never overwrite history."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, sys

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    root=Path(__file__).resolve().parents[2]
    src=root/'.codex/research/hott/sessions/S-ANS-20260910-015-QUOTIENT-DESCENT/FINITE_CHECKS.py'
    previous=src.with_name('FINITE_RESULTS.json')
    if a.out.exists():raise SystemExit('Refusing overwrite')
    before=hashlib.sha256(src.read_bytes()).hexdigest()
    if before!='ecbdcd2f4c4d9e34c02b0f2880ed11a145a2add3ac743a3082e8bd8d132ac6a6':
        raise SystemExit('R015 source differs from reviewed original')
    spec=importlib.util.spec_from_file_location('reviewed_r015',src)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    now=module.run();old=json.loads(previous.read_text())
    # Original result can also contain execution metadata outside the run() fields.
    matches={k:old.get(k)==v for k,v in now.items()}
    if not all(matches.values()):raise AssertionError({'mismatching_fields':matches})
    assert hashlib.sha256(src.read_bytes()).hexdigest()==before
    report={'schema_version':'hott-replay-r015/v1','status':'REPRODUCED_FINITE_RESULTS',
            'source_path':str(src.relative_to(root)),'source_sha256':before,
            'old_result_sha256':hashlib.sha256(previous.read_bytes()).hexdigest(),
            'exact_run_fields_match':matches,'result':now,
            'scope':'Seven finite-word checks; NOT an independent proof or HoTT kernel replay'}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'groups':now['group_count'],'all_run_fields_match':all(matches.values())}))
if __name__=='__main__':main()
