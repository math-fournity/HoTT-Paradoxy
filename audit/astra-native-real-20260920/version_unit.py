#!/usr/bin/env python3
"""Version only this proof/configuration/report/canonical-checkpoint unit."""
from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260920-ASTRA-NATIVE-REAL'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
existing=set(git('diff','--cached','--name-only','-z').decode().split('\0'))-{''}
if existing:
 prior=json.loads((OUT/'version-paths.json').read_text())
 assert existing<=set(prior['paths']), 'Preserve any foreign index entry'
result=json.loads((ROOT/'.codex/cognition/checkpoints'/SID/'result.json').read_text());assert result['status']=='CHECKPOINT_COMMITTED'
paths=set(result['paths'])|{'HoTT/formal/agda-unimath/hott-z/ErasureConfigurationDiagnostic.agda','HoTT/formal/agda-unimath/hott-z/NativeRealCircleQualification.agda','HoTT/CLAIM_EVIDENCE_MATRIX.md','HoTT/verification/PROOF_VERSION_CLOSURE.json','Astra继续尝试/断点与证明机制系统检查/第九轮执行报告.md'}
dirs=['audit/astra-native-real-20260920','HoTT/formal/agda-unimath/no-erasure','.codex/cognition/checkpoints/'+SID,'Astra继续尝试/断点与证明机制系统检查/第九轮执行报告']
dirs+=['HoTT/verification/runs/20260920-MP-ASTRA-'+x for x in ['ERASURE-CONFIG-001-01','ERASURE-CONTROL-001-01','NATIVE-REAL-001-01','NOSECTION-RESTRICTED-001-01','NOSECTION-RESTRICTED-001-02']]
for d in dirs:
 paths.update(p.relative_to(ROOT).as_posix() for p in (ROOT/d).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.agdai')
paths.add((OUT/'version-paths.json').relative_to(ROOT).as_posix())
ordered=sorted(paths)
(OUT/'version-paths.json').write_text(json.dumps({'expected_parent':git('rev-parse','HEAD').decode().strip(),'paths':ordered},ensure_ascii=False,indent=2)+'\n')
subprocess.run(['git','add','--',*ordered],cwd=ROOT,check=True)
staged=set(git('diff','--cached','--name-only','-z').decode().split('\0'))-{''};assert staged<=paths
p=subprocess.run(['git','diff','--cached','--check','--','.',':(exclude)audit/astra-native-real-20260920/version-whitespace.txt'],cwd=ROOT,capture_output=True)
raw=p.stdout.decode();(OUT/'version-whitespace.txt').write_text(raw)
bad=[]
for line in raw.splitlines():
 if ': trailing whitespace.' in line or ': new blank line at EOF.' in line:
  path=line.rsplit(':',2)[0]
  # Raw version output in immutable environment receipts has a terminal " | ".
  # Preserve its captured bytes/hash; it is not editable report whitespace.
  immutable_env=path.startswith('HoTT/verification/runs/') and path.endswith('/environment.txt')
  if '/before/' not in path and '/after/' not in path and not immutable_env and not path.endswith(('/stdout.txt','.dot','.patch')):bad.append(line)
assert not bad,bad
extra=(OUT/'version-whitespace.txt').relative_to(ROOT).as_posix()
subprocess.run(['git','add','--',extra],cwd=ROOT,check=True)
assert set(git('diff','--cached','--name-only','-z').decode().split('\0'))-{''}<=paths|{extra}
print(json.dumps({'selected_paths':len(ordered),'staged_paths':len(staged),'preserved_raw_whitespace_lines':len(raw.splitlines())}),flush=True)
if '--commit' in sys.argv:
 subprocess.run(['git','commit','--quiet','--only','-m','BP-GEO-NATIVE-REAL-QUALIFICATION-01(step-1): 额外归约消融与实际实数模型C280–282; reflection=revised-in a1d935f','--',*ordered,extra],cwd=ROOT,check=True)
