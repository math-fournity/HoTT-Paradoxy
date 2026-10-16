"""Record availability and an explicit bounded official-toolchain fetch attempt."""
from pathlib import Path
import hashlib, json, shutil, subprocess, urllib.request
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r024'
rows=[]
for name in ('lean','lake','agda','coqc','rocq'):
    exe=shutil.which(name)
    row={'name':name,'path':exe}
    if exe:
        p=subprocess.run([exe,'--version'],text=True,capture_output=True,timeout=10)
        row.update(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
    rows.append(row)
url='https://github.com/leanprover/lean4/releases/download/v4.19.0/lean-4.19.0-linux.tar.zst'
try:
    req=urllib.request.Request(url,method='HEAD',headers={'User-Agent':'HoTT-R024-audit'})
    with urllib.request.urlopen(req,timeout=10) as response:
        attempt={'url':url,'method':'HEAD','status':response.status,'headers':dict(response.headers),'downloaded':False}
except Exception as exc:
    attempt={'url':url,'method':'HEAD','error':repr(exc),'downloaded':False}
result={'utc':datetime.now(timezone.utc).isoformat(),'executables':rows,'official_toolchain_probe':attempt,
        'toolchain_installed':False,'native_math_proof':'NOT_RUN'}
(OUT/'TOOLCHAIN_STATUS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
