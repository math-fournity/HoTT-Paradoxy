#!/usr/bin/env python3
"""Fetch the exact official cache dependency map with <=8 single-connection transfers."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import urllib.request

ROOT=Path(__file__).resolve().parents[2]
BASE=Path('/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0')
SOURCE=BASE/'mathlib4-5ed2965256430c3649e86755f9576b54eca72435'
OUT=Path(__file__).resolve().parent/'cache-download-azure'
MANIFEST=Path(__file__).resolve().parent/'environment-qualification/cache-manifest-v2.stdout.json'
data=json.loads(MANIFEST.read_text())
assert Path('/Volumes/D').is_mount()
assert BASE.stat().st_dev==Path('/Volumes/D').stat().st_dev
assert shutil.disk_usage(BASE).free>4*1024**3
OUT.mkdir()
target=BASE/'compiled-cache'
assert not list(target.glob('*.ltar')) and not list(target.glob('*.aria2'))
entries=sorted(data['entries'],key=lambda x:x['file'])
for e in entries:
    # Upstream Cache.Infra.defaultGetBaseURL(true), the documented official storage endpoint.
    e['url']=e['url'].replace('https://cache.mathlib.org/',
                            'https://lakecache.blob.core.windows.net/')
assert len({e['file'] for e in entries})==len(entries)
for e in entries:
    assert e['url'].startswith('https://lakecache.blob.core.windows.net/mathlib4-master/f/')
    assert '/' not in e['file'] and e['file'].endswith('.ltar')
request=urllib.request.Request(entries[0]['url'],headers={'Range':'bytes=0-0','Accept-Encoding':'identity'})
with urllib.request.urlopen(request,timeout=30) as response:
    preflight=dict(status=response.status,url=response.url,headers=dict(response.headers),
                   probe_bytes=len(response.read(1)))
(OUT/'PREFLIGHT.json').write_text(json.dumps(preflight,indent=2)+'\n')
input_file=BASE/'cache-download-input.txt'
with input_file.open('x') as f:
    for e in entries:f.write(e['url']+'\n  dir='+str(target)+'\n  out='+e['file']+'\n')
args=['/opt/homebrew/bin/aria2c','--no-conf=true','--no-netrc=true',
      '--max-concurrent-downloads=8','--split=1','--max-connection-per-server=1',
      '--piece-length=1M','--min-split-size=1M','--continue=false',
      '--auto-file-renaming=false','--allow-overwrite=false','--file-allocation=none',
      '--max-tries=3','--retry-wait=3','--connect-timeout=20','--timeout=60',
      '--check-certificate=true','--header=Accept-Encoding: identity',
      '--console-log-level=warn','--summary-interval=30',
      '--log='+str(BASE/'cache-download-aria2.log'),
      '--input-file='+str(input_file)]
env=dict(os.environ,TMPDIR=str(BASE/'tmp'))
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (OUT/'stdout.txt').open('xb') as stdout,(OUT/'stderr.txt').open('xb') as stderr:
    p=subprocess.Popen(args,cwd=BASE,env=env,stdout=stdout,stderr=stderr)
    (OUT/'PROCESS.json').write_text(json.dumps(dict(pid=p.pid,argv=args,started=started),indent=2)+'\n')
    print(json.dumps(dict(status='RUNNING',pid=p.pid,files=len(entries))),flush=True)
    code=p.wait()
rows=[]
for e in entries:
    path=target/e['file']
    complete=path.is_file() and not Path(str(path)+'.aria2').exists()
    rows.append(dict(module=e['module'],file=e['file'],complete=complete,
                     bytes=path.stat().st_size if path.exists() else 0,
                     sha256=hashlib.sha256(path.read_bytes()).hexdigest() if complete else None))
receipt=dict(status='DOWNLOADED_NOT_UNPACKED' if code==0 and all(x['complete'] for x in rows) else 'INCOMPLETE',
             exit_code=code,started=started,completed=datetime.datetime.now(datetime.timezone.utc).isoformat(),
             transfer_slots=8,connections_per_file=1,files=rows,
             manifest_sha256=hashlib.sha256(MANIFEST.read_bytes()).hexdigest(),
             trust='Official HTTPS cache with upstream source-derived keys; local SHA256 fixes downloaded bytes, not independent publisher authenticity. No untrusted fork caches or uploads.')
(OUT/'RESULT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],exit_code=code,complete=sum(r['complete'] for r in rows),
                     files=len(rows),bytes=sum(r['bytes'] for r in rows))),flush=True)
