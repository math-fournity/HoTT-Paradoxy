#!/usr/bin/env python3
"""Compile selected verbatim candidate copies using only existing project tools."""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
ROOT = Path('/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0')
OUT = ROOT / '.cg009-verification'
SRC = OUT / 'src'
BUILD = OUT / 'build'
SRC.mkdir(parents=True, exist_ok=True)
BUILD.mkdir(parents=True, exist_ok=True)
PKG = Path('/Volumes/D/HoTT_AI_HANDOFF_20260911/HoTT/formal/claude-cg001/godel-q-zfc-z0-full')
tc = json.loads((PKG / 'LEAN_TOOLCHAIN.json').read_text())
cl = json.loads((PKG / 'MATHLIB_CLOSURE.json').read_text())
prefix = Path(tc['prefix'])
for r in tc['pinned_files']:
    data = (prefix / r['relative_path']).read_bytes()
    assert len(data) == r['bytes'] and hashlib.sha256(data).hexdigest() == r['sha256']
for r in cl['modules']:
    h = hashlib.sha256()
    base = Path(cl['library_roots'][r['root']]).joinpath(*r['module'].split('.'))
    for suffix in ('.olean', '.olean.private', '.olean.server'):
        p = Path(str(base) + suffix)
        if p.exists():
            h.update(suffix.encode())
            h.update(hashlib.sha256(p.read_bytes()).hexdigest().encode())
    assert h.hexdigest() == r['digest'], r['module']
# Lean resolves a namespace from its first matching root; it does not search
# later roots for each missing child. Copy this session's checked parent modules.
import shutil
parents = ROOT / '.cg007-audit-20261011/build/GodelQ'
for p in parents.rglob('*'):
    if p.is_file():
        dest = BUILD / 'GodelQ' / p.relative_to(parents)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            shutil.copyfile(p, dest)
env = dict(os.environ)
env.update(PATH=f'{prefix}/bin:/usr/bin:/bin', LEAN_SYSROOT=str(prefix), LEAN_PATH=':'.join([str(BUILD)]+cl['lean_path']), HOME=str(OUT))
options = [f'-D{k}={v}' for k,v in cl['lean_options'].items()]
WB = Path('/Users/aurolafly/WorkBuddy/Worktrees/HoTT_AI_HANDOFF_20260911')
rel_pkg = Path('HoTT/formal/claude-cg001/godel-q-zfc-z0-full')
candidates = [
 ('wb-wrong-craig-instance', WB/'dev-bd4295b5'/rel_pkg/'GodelQ/Negative/WithoutCraigBridge.lean', 'GodelQ/Negative/WithoutCraigBridge.lean', []),
 ('wb-conditional-final', WB/'dev-ef7e5239'/rel_pkg/'GodelQ/ZFC/Z0Final.lean', 'GodelQ/ZFC/Z0Final.lean', []),
 ('wb-sigma1-anchor', WB/'dev-ef7e5239'/rel_pkg/'GodelQ/ZFC/ZFCSetSigma1.lean', 'GodelQ/ZFC/ZFCSetSigma1.lean', ['GodelQ.ZFCSetSigma1.zfcProvable_iff_provable','GodelQ.ZFCSetSigma1.zfcProvable_arith_sigma1']),
 ('wb-blocked-repaired-name', WB/'dev-ef7e5239'/rel_pkg/'GodelQ/ZFC/Z0Blocked.lean', 'GodelQ/ZFC/Z0Blocked.lean', ['GodelQ.Z0Blocked.zfcTr_D3_internalize']),
 ('wb-bottom-bridge', WB/'dev-bd4295b5'/rel_pkg/'GodelQ/ZFC/Z0CraigBridge.lean', 'GodelQ/ZFC/Z0CraigBridge.lean', []),
]
results=[]
for key,origin,rel,extra in candidates:
    data=origin.read_bytes()
    copy=SRC/rel
    copy.parent.mkdir(parents=True,exist_ok=True)
    copy.write_bytes(data)
    assert copy.read_bytes()==data
    target=BUILD/Path(rel).with_suffix('')
    target.parent.mkdir(parents=True,exist_ok=True)
    cmd=['/usr/bin/sandbox-exec','-p','(version 1)(allow default)(deny network*)',str(prefix/'bin/lean'),*options,'-R',str(SRC),'-o',str(target)+'.olean',str(copy)]
    record={'key':key,'origin':str(origin),'source_sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'command':cmd,'source_unchanged_at_end':True,'method':'verbatim copy; upstream project build from previous independent audit, same pinned libraries; no canonical receipt'}
    try:
        run=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,timeout=240)
        (OUT/(key+'.stdout.txt')).write_bytes(run.stdout)
        (OUT/(key+'.stderr.txt')).write_bytes(run.stderr)
        record['exit_code']=run.returncode
        record['stdout_file']=str(OUT/(key+'.stdout.txt'))
        record['stderr_file']=str(OUT/(key+'.stderr.txt'))
        if extra and run.returncode==0:
            code='import '+rel.removesuffix('.lean').replace('/','.')+'\n'+'\n'.join('#print axioms '+n for n in extra)+'\n'
            probe=subprocess.run(['/usr/bin/sandbox-exec','-p','(version 1)(allow default)(deny network*)',str(prefix/'bin/lean'),*options,'--stdin'],input=code.encode(),cwd=ROOT,env=env,capture_output=True,timeout=120)
            (OUT/(key+'.axioms.txt')).write_bytes(probe.stdout+probe.stderr)
            record['axiom_probe_exit']=probe.returncode
            record['axiom_probe_stdout']=probe.stdout.decode(errors='replace')
        print(key,'exit',run.returncode,flush=True)
        print(run.stdout.decode(errors='replace')[-4500:],run.stderr.decode(errors='replace'),flush=True)
    except subprocess.TimeoutExpired:
        record['exit_code']='TIMEOUT_240s'
        print(key,'TIMEOUT_240s (cl_prover-heavy candidate; recorded as timeout, not success)',flush=True)
    record['source_unchanged_at_end']=origin.read_bytes()==data
    results.append(record)
summary={'captured_at':datetime.datetime.now().astimezone().isoformat(timespec='seconds'),'pin_verified':True,'compiled_library_digests_checked':len(cl['modules']),'results':results,'scope':'candidate validation only; no upstream proof editing, no publication or official receipt'}
(OUT/'RUN.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
