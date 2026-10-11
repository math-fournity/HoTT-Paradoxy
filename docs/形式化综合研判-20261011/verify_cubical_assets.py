#!/usr/bin/env python3
"""Replay recovered Cubical assets in private source and library copies."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
ROOT=Path('/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0')
ORIGIN=Path('/Volumes/D/HoTT-machine-overview')
OUT=ROOT/'.cg009-cubical'
SRC=OUT/'src'
LIB=OUT/'cubical'
SRC.mkdir(parents=True,exist_ok=True)
oldrun=ORIGIN/'HoTT/verification/runs/20260914-CUBICAL-GODEL-PROOF-SEARCH-CLASSIFIER-001'
manifest=json.loads((oldrun/'source-manifest.json').read_text())
for r in manifest['files']:
    if r['path'].endswith('.agda'):
        data=(ORIGIN/r['path']).read_bytes()
        assert len(data)==r['bytes'] and hashlib.sha256(data).hexdigest()==r['sha256'],r['path']
        dest=SRC/Path(r['path']).name
        dest.write_bytes(data)
# Additional sources needed by the classifier chain (imports resolve in one flat dir).
extra = [
  ORIGIN/'HoTT/formal/cubical-machine-halting/MachineHalting.agda',
  ORIGIN/'HoTT/formal/cubical-candidate-coverage/CandidateCoverage.agda',
  ORIGIN/'HoTT/formal/partiality-race-timeout/PartialityRaceTimeout.agda',
]
for p in extra:
    if p.exists():
        shutil.copyfile(p, SRC/p.name)
        print('copied', p.name, flush=True)
    else:
        print('MISSING extra', p, flush=True)
agda=Path('/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda')
assert hashlib.sha256(agda.read_bytes()).hexdigest()=='ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e'
# Use the ORIGINAL cubical library (with its _build interface cache) via its own library file,
# exactly as the 2026-09-14 receipts did; do NOT copy the library (cache excluded would force
# full re-typecheck of all 1111 modules).
libs=Path('/Volumes/D/HoTT-machine-overview/HoTT/formal/partiality-race-timeout/AGDA_LIBRARIES')
assert libs.exists()
env=dict(os.environ)
env.update(XDG_DATA_HOME=str(OUT/'xdg-data'),XDG_CONFIG_HOME=str(OUT/'xdg-config'),TMPDIR=str(OUT/'tmp'))
(OUT/'tmp').mkdir(exist_ok=True)
chain=('MiniProofChecker.agda','ProofSerialization.agda','FormulaBitCode.agda','ProofBitCode.agda','NatProofCode.agda','SyntheticIncompleteness.agda','ProofSearchClassifier.agda','MachineHalting.agda','PartialityRaceTimeout.agda','CandidateCoverage.agda')
results=[]
for name in chain:
    if not (SRC/name).exists():
        print('skip (absent)', name, flush=True); continue
    cmd=['/usr/bin/sandbox-exec','-p','(version 1)(allow default)(deny network*)',str(agda),'--ignore-interfaces','--library-file='+str(libs),'-l','cubical-0.9','-i',str(SRC),str(SRC/name)]
    try:
        run=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,timeout=420)
        (OUT/(name+'.stdout.txt')).write_bytes(run.stdout)
        (OUT/(name+'.stderr.txt')).write_bytes(run.stderr)
        result={'file':name,'source_sha256':hashlib.sha256((SRC/name).read_bytes()).hexdigest(),'exit_code':run.returncode,'command':cmd,'stdout':str(OUT/(name+'.stdout.txt')),'stderr':str(OUT/(name+'.stderr.txt'))}
        print(name,'exit',run.returncode,flush=True)
        print(run.stdout.decode(errors='replace')[-1200:],run.stderr.decode(errors='replace')[-800:],flush=True)
    except subprocess.TimeoutExpired:
        result={'file':name,'exit_code':'TIMEOUT_420s'}
        print(name,'TIMEOUT_420s',flush=True)
    results.append(result)
(OUT/'RUN.json').write_text(json.dumps({'captured_at':datetime.datetime.now().astimezone().isoformat(timespec='seconds'),'method':'pinned binary; verbatim project copies; private cubical library copy; all interfaces ignored; external tree full digest not recomputed; not canonical receipt','results':results},ensure_ascii=False,indent=2)+'\n')
