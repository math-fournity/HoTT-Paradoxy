#!/usr/bin/env python3
"""Check the actual ambient geometry module, preserving every attempt."""
from pathlib import Path
import hashlib,json,os,subprocess,datetime
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
BASE=Path('/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0')
BUILD=BASE/'project-build'
BUILD.mkdir(exist_ok=True)
LEAN='/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean'
FORMAL=ROOT/'HoTT/formal/astra-real-geometry'
PATHS=(ROOT/'audit/astra-real-geometry-20260919/environment-qualification/LEAN_PATH.txt').read_text().strip()
env=dict(os.environ,LEAN_PATH=str(BUILD)+os.pathsep+PATHS,TMPDIR=str(BASE/'tmp'))
source=FORMAL/'PuncturedCircle.lean'
stamp=BUILD/'PuncturedCircle.source.sha256'
digest=hashlib.sha256(source.read_bytes()).hexdigest()
if not stamp.exists() or stamp.read_text()!=digest:
 argv=[LEAN,'-R',str(FORMAL),'-o',str(BUILD/'PuncturedCircle.olean'),str(source)]
 r=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True)
 (OUT/'local-build.stdout.txt').write_bytes(r.stdout);(OUT/'local-build.stderr.txt').write_bytes(r.stderr)
 assert r.returncode==0,r.stdout.decode()+r.stderr.decode()
 stamp.write_text(digest)
attempts=OUT/'attempts';attempts.mkdir(exist_ok=True)
attempt=attempts/f'{len(list(attempts.iterdir()))+1:03d}';attempt.mkdir()
source=FORMAL/'AmbientCircle.lean'
(attempt/source.name).write_bytes(source.read_bytes())
argv=[LEAN,'-R',str(FORMAL),str(source)]
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
r=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True)
(attempt/'stdout.txt').write_bytes(r.stdout);(attempt/'stderr.txt').write_bytes(r.stderr)
(attempt/'CHECK.json').write_text(json.dumps({'command':argv,'cwd':str(ROOT),'exit':r.returncode,'started':started,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'status':'DRAFT_ONLY'},indent=2)+'\n')
print('ATTEMPT',attempt.name,'EXIT',r.returncode);print(r.stdout.decode(),r.stderr.decode())
