#!/usr/bin/env python3
"""Stage and commit only this bounded proof/report/checkpoint unit."""
from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-AMBIENT-CIRCLE'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
assert not git('diff','--cached','--name-only')
result=json.loads((ROOT/'.codex/cognition/checkpoints'/SID/'result.json').read_text())
assert result['status']=='CHECKPOINT_COMMITTED'
paths=set(result['paths'])|{
 'HoTT/formal/astra-real-geometry/AmbientCircle.lean',
 'HoTT/formal/astra-real-geometry/AMBIENT-TOOLCHAIN.json',
 'HoTT/formal/astra-real-geometry/capture_ambient.py',
 'HoTT/CLAIM_EVIDENCE_MATRIX.md','HoTT/verification/PROOF_VERSION_CLOSURE.json',
 'Astra继续尝试/断点与证明机制系统检查/第五轮执行报告.md'}
for directory in [
 'audit/astra-ambient-geometry-20260920',
 '.codex/cognition/checkpoints/'+SID,
 'HoTT/verification/runs/20260920-MP-ASTRA-AMBIENT-CIRCLE-001-01',
 'HoTT/verification/runs/20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02',
 'Astra继续尝试/断点与证明机制系统检查/第五轮执行报告']:
 paths.update(str(p.relative_to(ROOT)) for p in (ROOT/directory).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
paths.add(str((OUT/'version-paths.json').relative_to(ROOT)))
ordered=sorted(paths)
(OUT/'version-paths.json').write_text(json.dumps({'expected_parent':git('rev-parse','HEAD').decode().strip(),'paths':ordered},ensure_ascii=False,indent=2)+'\n')
subprocess.run(['git','add','--',*ordered],cwd=ROOT,check=True)
staged=set(git('diff','--cached','--name-only','-z').decode().split('\0'))-{''}
assert staged<=paths,staged-paths
check=subprocess.run(['git','diff','--cached','--check'],cwd=ROOT,capture_output=True)
raw=check.stdout.decode();(OUT/'version-whitespace.txt').write_text(raw)
bad=[]
for line in raw.splitlines():
 if ': trailing whitespace.' in line or ': new blank line at EOF.' in line:
  path=line.rsplit(':',2)[0]
  # Immutable checkpoint copies/raw original outputs are retained byte for byte.
  if '/before/' not in path and '/after/' not in path and not path.endswith('/stdout.txt'):
   bad.append(line)
assert not bad,bad
extra='audit/astra-ambient-geometry-20260920/version-whitespace.txt'
subprocess.run(['git','add','--',extra],cwd=ROOT,check=True)
assert set(git('diff','--cached','--name-only','-z').decode().split('\0'))-{''} <= paths|{extra}
print(json.dumps({'staged_paths':len(staged),'immutable_whitespace_lines':len(raw.splitlines())},ensure_ascii=False),flush=True)
if '--commit' in sys.argv:
 subprocess.run(['git','commit','--only','-m','BP-GEO-AMBIENT-01(step-1): 实数环境同胚与有限操作C266–268; reflection=revised-in c6f406c','--',*ordered,extra],cwd=ROOT,check=True)
