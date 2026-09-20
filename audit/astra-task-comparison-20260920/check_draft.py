#!/usr/bin/env python3
"""Check a preserved draft using the fixed Cubical v0.9 configuration."""
from pathlib import Path
import argparse,datetime,hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--module',default='Sqrt2TaskComparison');args=ap.parse_args()
source=ROOT/('HoTT/formal/dedekind-omega-missile/'+args.module+'.agda')
attempts=OUT/'attempts';attempts.mkdir(exist_ok=True);dest=attempts/f'{len(list(attempts.iterdir()))+1:03d}';dest.mkdir()
inputs=[source]+[p for p in source.parent.glob('*.agda') if p.name in ['Sqrt2TaskComparison.agda'] and p!=source]
raws={p:p.read_bytes() for p in inputs}
for p,raw in raws.items():(dest/p.name).write_bytes(raw)
argv=json.loads((ROOT/'HoTT/verification/runs/20260919-MP-DEDEKIND-OMEGA-GOLD-03/RUN.json').read_text())['command_argv']
argv=[str(source) if x.endswith('/CutGoldForm.agda') else x for x in argv]
argv=[x for x in argv if x!='--ignore-interfaces' and not x.startswith('--dependency-graph=')];argv.insert(-1,'--dependency-graph='+str(dest/'imports.dot'))
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (dest/'stdout.txt').open('wb') as o,(dest/'stderr.txt').open('wb') as e:
 p=subprocess.Popen(argv,cwd=ROOT,stdout=o,stderr=e);(dest/'PROCESS.json').write_text(json.dumps({'pid':p.pid,'argv':argv,'started':started},indent=2)+'\n');print('ATTEMPT',dest.name,'PID',p.pid,flush=True);code=p.wait()
assert all(p.read_bytes()==raw for p,raw in raws.items())
(dest/'CHECK.json').write_text(json.dumps({'status':'DRAFT_ONLY','exit':code,'argv':argv,'snapshots':[{'name':p.name,'sha256':hashlib.sha256(b).hexdigest()} for p,b in raws.items()],'started':started,'completed':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n')
print('EXIT',code,flush=True);print((dest/'stdout.txt').read_text()[-6500:]);print((dest/'stderr.txt').read_text())
