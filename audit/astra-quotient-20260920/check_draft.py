#!/usr/bin/env python3
"""Preserve each rational quotient consumer draft before a native check."""
from pathlib import Path
import datetime, hashlib, json, subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
source='HoTT/formal/astra-quotient-consumer/QuotientConsumer.agda'
inputs=[source]+['HoTT/formal/dedekind-omega-missile/'+n+'.agda' for n in ['CutGoldForm','CutInfra','MissileTwoUniversalIrrationality']]
attempts=OUT/'attempts';attempts.mkdir(exist_ok=True);dest=attempts/str(len(list(attempts.iterdir()))+1).zfill(3);dest.mkdir()
raws={p:(ROOT/p).read_bytes() for p in inputs}
for p,b in raws.items():(dest/Path(p).name).write_bytes(b)
cfg=json.loads((ROOT/'HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json').read_text());cache=cfg['runtime_cache']
argv=['/usr/bin/env','XDG_DATA_HOME='+cache['xdg_data_home'],'XDG_CONFIG_HOME='+cache['xdg_config_home'],'TMPDIR='+cache['tmpdir'],cfg['agda']['local_binary'],'--library-file='+str(ROOT/cfg['project_library_registry']),'-l','cubical-0.9','-i',str(ROOT/'HoTT/formal/astra-quotient-consumer'),'-i',str(ROOT/'HoTT/formal/dedekind-omega-missile'),'--dependency-graph='+str(dest/'imports.dot'),source]
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (dest/'stdout.txt').open('wb') as o,(dest/'stderr.txt').open('wb') as e:
    p=subprocess.Popen(argv,cwd=ROOT,stdout=o,stderr=e);(dest/'PROCESS.json').write_text(json.dumps({'pid':p.pid,'argv':argv,'started':started},indent=2)+'\n');print('ATTEMPT',dest.name,'PID',p.pid,flush=True);code=p.wait()
assert all((ROOT/p).read_bytes()==b for p,b in raws.items())
(dest/'CHECK.json').write_text(json.dumps({'status':'DRAFT_ONLY','exit':code,'argv':argv,'snapshots':[{'path':p,'sha256':hashlib.sha256(b).hexdigest()} for p,b in raws.items()],'started':started,'completed':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n')
print('EXIT',code,flush=True);print((dest/'stdout.txt').read_text()[-6500:]);print((dest/'stderr.txt').read_text())
