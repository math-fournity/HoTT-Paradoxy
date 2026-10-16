#!/usr/bin/env python3
"""Check actual agda-unimath real geometry; preserve every draft and raw output."""
from pathlib import Path
import argparse,datetime,hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--module',default='NativeRealCircleQualification');ap.add_argument('--registry');ap.add_argument('--library',default='agda-unimath');args=ap.parse_args()
source=ROOT/('HoTT/formal/agda-unimath/hott-z/'+args.module+'.agda')
attempts=OUT/'attempts';attempts.mkdir(exist_ok=True)
dest=attempts/f'{len(list(attempts.iterdir()))+1:03d}';dest.mkdir()
(dest/source.name).write_bytes(source.read_bytes())
argv=json.loads((ROOT/'HoTT/verification/runs/20260913-MP-UNIMATH-NOSECTION-REPLAY-02/RUN.json').read_text())['command_argv']
argv=[str(source) if x.endswith('/NoCanonicalPoint.agda') else x for x in argv]
if args.registry:
 argv=[('--library-file='+str(ROOT/args.registry)) if x.startswith('--library-file=') else (args.library if x=='agda-unimath' else x) for x in argv]
# Drafts may reuse standard interfaces; final delivery will perform a clean --ignore-interfaces run.
argv.remove('--ignore-interfaces')
argv.insert(-1,'--dependency-graph='+str(dest/'imports.dot'))
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (dest/'stdout.txt').open('wb') as stdout,(dest/'stderr.txt').open('wb') as stderr:
 p=subprocess.Popen(argv,cwd=ROOT,stdout=stdout,stderr=stderr)
 (dest/'PROCESS.json').write_text(json.dumps({'pid':p.pid,'argv':argv,'started':started},indent=2)+'\n')
 print('ATTEMPT',dest.name,'PID',p.pid,flush=True)
 code=p.wait()
(dest/'CHECK.json').write_text(json.dumps({'status':'DRAFT_ONLY','exit':code,'argv':argv,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'started':started,'completed':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2)+'\n')
print('EXIT',code,flush=True)
print((dest/'stdout.txt').read_text()[-6000:]);print((dest/'stderr.txt').read_text())
