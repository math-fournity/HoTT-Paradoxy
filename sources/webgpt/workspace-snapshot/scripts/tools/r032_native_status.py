#!/usr/bin/env python3
"""Bounded local discovery only; no installation or substituted native outputs."""
import datetime,json,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
path=ROOT/'artifacts/r032/NATIVE_STATUS.json'
if path.exists(): raise FileExistsError(path)
found={x:shutil.which(x) for x in ('agda','lean','rocq','coqc')}
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'executables':found,
        'native_check':'NOT_RUN','reason':'No native tool found on PATH' if not any(found.values()) else 'Source has not been compiled in this bounded task',
        'source':'scripts/research/r032_formal/RestrictedReflection.agda',
        'boundary':'No native compilation or full HoTT metatheory is inferred from Python checks.'}
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
