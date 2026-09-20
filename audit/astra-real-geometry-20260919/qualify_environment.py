#!/usr/bin/env python3
"""Build the official, pinned mathlib cache CLI in the owned external cache."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[2]
BASE=Path('/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0')
SOURCE=BASE/'mathlib4-5ed2965256430c3649e86755f9576b54eca72435'
BIN=Path('/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin')
OUT=Path(__file__).resolve().parent/'environment-qualification'
assert Path('/Volumes/D').is_mount()
assert BASE.stat().st_dev==Path('/Volumes/D').stat().st_dev
assert shutil.disk_usage(BASE).free>4*1024**3
OUT.mkdir(exist_ok=True)
for name in ('tmp','compiled-cache','xdg-cache'):(BASE/name).mkdir(exist_ok=True)
lock=SOURCE/'lake-manifest.json'
before=hashlib.sha256(lock.read_bytes()).hexdigest()
env=dict(os.environ)
env.update(PATH=str(BIN)+os.pathsep+env['PATH'],TMPDIR=str(BASE/'tmp'),
           XDG_CACHE_HOME=str(BASE/'xdg-cache'),MATHLIB_CACHE_DIR=str(BASE/'compiled-cache'),
           MATHLIB_NO_CACHE_ON_UPDATE='1',GIT_TERMINAL_PROMPT='0',
           GIT_CONFIG_GLOBAL='/dev/null',GIT_CONFIG_NOSYSTEM='1')
argv=[str(BIN/'lake'),'exe','cache','--help']
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (OUT/'stdout.txt').open('xb') as stdout,(OUT/'stderr.txt').open('xb') as stderr:
    process=subprocess.Popen(argv,cwd=SOURCE,env=env,stdout=stdout,stderr=stderr)
    (OUT/'PROCESS.json').write_text(json.dumps(dict(pid=process.pid,argv=argv,cwd=str(SOURCE),started=started),indent=2)+'\n')
    print(json.dumps(dict(status='RUNNING',pid=process.pid,argv=argv)),flush=True)
    code=process.wait()
deps=[]
for dep in json.loads(lock.read_text())['packages']:
    p=SOURCE/'.lake/packages'/dep['name']
    if (p/'.git').exists():
        actual=subprocess.check_output(['git','-C',str(p),'rev-parse','HEAD'],env=env,text=True).strip()
    else:actual=None
    deps.append(dict(name=dep['name'],expected=dep['rev'],actual=actual,match=actual==dep['rev']))
result=dict(status='PASS' if code==0 and all(d['match'] for d in deps) else 'FAIL',
            exit_code=code,started=started,completed=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            argv=argv,cwd=str(SOURCE),lock_sha256_before=before,
            lock_sha256_after=hashlib.sha256(lock.read_bytes()).hexdigest(),dependencies=deps,
            scope='Source dependency checkout and cache CLI build only; no math theorem replay.')
(OUT/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False),flush=True)
