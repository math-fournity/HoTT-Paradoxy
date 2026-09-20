#!/usr/bin/env python3
"""Preserve every curve-deformation draft and check actual Lean inputs."""
from pathlib import Path
import datetime,hashlib,json,os,subprocess
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
BASE=Path('/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0')
BUILD=BASE/'project-build'
LEAN='/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin/lean'
FORMAL=ROOT/'HoTT/formal/astra-real-geometry'
paths=(ROOT/'audit/astra-real-geometry-20260919/environment-qualification/LEAN_PATH.txt').read_text().strip()
env=dict(os.environ,LEAN_PATH=str(BUILD)+os.pathsep+paths,TMPDIR=str(BASE/'tmp'))
for name in ['PuncturedCircle','AmbientCircle']:
 source=FORMAL/(name+'.lean');stamp=BUILD/(name+'.source.sha256')
 digest=hashlib.sha256(source.read_bytes()).hexdigest()
 if not stamp.exists() or stamp.read_text()!=digest:
  argv=[LEAN,'-R',str(FORMAL),'-o',str(BUILD/(name+'.olean')),str(source)]
  p=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True)
  (OUT/(name+'.stdout.txt')).write_bytes(p.stdout);(OUT/(name+'.stderr.txt')).write_bytes(p.stderr)
  assert p.returncode==0,p.stdout.decode()+p.stderr.decode()
  stamp.write_text(digest)
attempts=OUT/'attempts';attempts.mkdir(exist_ok=True)
dest=attempts/f'{len(list(attempts.iterdir()))+1:03d}';dest.mkdir()
source=FORMAL/'DeformationCircle.lean';(dest/source.name).write_bytes(source.read_bytes())
argv=[LEAN,'-R',str(FORMAL),str(source)]
p=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True)
for label,data in [('stdout',p.stdout),('stderr',p.stderr)]: (dest/(label+'.txt')).write_bytes(data)
(dest/'CHECK.json').write_text(json.dumps(dict(status='DRAFT_ONLY',argv=argv,exit=p.returncode,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat()),indent=2)+'\n')
print('ATTEMPT',dest.name,'EXIT',p.returncode);print(p.stdout.decode(),p.stderr.decode())
