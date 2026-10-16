#!/usr/bin/env python3
"""Preserve both principle-translation sources before checking the actual native module."""
from pathlib import Path
import datetime,hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
base='HoTT/formal/agda-unimath/hott-z/';source=base+'RealPrincipleBookScope.agda'
inputs=[source,base+'MarkovBookForms.agda'];raws={p:(ROOT/p).read_bytes() for p in inputs}
attempts=OUT/'attempts';attempts.mkdir(exist_ok=True);dest=attempts/str(len(list(attempts.iterdir()))+1).zfill(3);dest.mkdir()
for p,b in raws.items():(dest/Path(p).name).write_bytes(b)
argv=json.loads((ROOT/'HoTT/verification/runs/20260920-MP-ASTRA-WEAK-LIFT-PRINCIPLE-001-01/RUN.json').read_text())['command_argv']
argv=[source if x.endswith('/WeakLiftConsumer.agda') else x for x in argv]
argv=[x for x in argv if x!='--ignore-interfaces' and not x.startswith('--dependency-graph=')];argv.insert(-1,'--dependency-graph='+str(dest/'imports.dot'))
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (dest/'stdout.txt').open('wb') as o,(dest/'stderr.txt').open('wb') as e:
    p=subprocess.Popen(argv,cwd=ROOT,stdout=o,stderr=e);(dest/'PROCESS.json').write_text(json.dumps({'pid':p.pid,'argv':argv,'started':started},indent=2)+'\n');print('ATTEMPT',dest.name,'PID',p.pid,flush=True);code=p.wait()
assert all((ROOT/p).read_bytes()==b for p,b in raws.items())
(dest/'CHECK.json').write_text(json.dumps({'status':'DRAFT_ONLY','exit':code,'argv':argv,'source_hashes':{p:hashlib.sha256(b).hexdigest() for p,b in raws.items()},'started':started,'completed':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n')
print('EXIT',code,flush=True);print((dest/'stdout.txt').read_text()[-6500:]);print((dest/'stderr.txt').read_text())
