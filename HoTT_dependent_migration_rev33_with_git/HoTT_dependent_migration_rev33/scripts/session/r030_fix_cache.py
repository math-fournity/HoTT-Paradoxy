#!/usr/bin/env python3
"""Fix typed cache aliasing; preserve first-run outputs and source bytes."""
from pathlib import Path
import shutil, json
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'scripts/research/r030_staged_reflection.py'
T=ROOT/'scripts/tests/test_r030_staged_reflection.py'
O=ROOT/'artifacts/r030'
backup=ROOT/'scripts/research/history/r030_initial';backup.mkdir(parents=True,exist_ok=True)
for src in [P,T]:
 dst=backup/src.name
 if dst.exists():raise FileExistsError(dst)
 shutil.copyfile(src,dst)
x=P.read_text();assert x.count('@lru_cache(maxsize=100000)')==2
P.write_text(x.replace('@lru_cache(maxsize=100000)','@lru_cache(maxsize=100000, typed=True)'))
y=T.read_text();assert "'artifacts/r030/RESULTS.json'" in y
T.write_text(y.replace("'artifacts/r030/RESULTS.json'","'artifacts/r030/RESULTS_FIXED.json'"))
(O/'CACHE_CORRECTION.json').write_text(json.dumps({'failure':'lru_cache(typed=False) can reuse natural-number (0,1) entry for Boolean (0,True) before body validation','fix':'typed=True on both caches','original_sources':'scripts/research/history/r030_initial','original_receipts':['artifacts/r030/EXECUTION.json','artifacts/r030/RESULTS.json'],'mathematical_claims_affected':'Does not alter intended natural-number semantics. Runtime input-validation fault; not a HoTT result.'},ensure_ascii=False,indent=2)+'\n')
