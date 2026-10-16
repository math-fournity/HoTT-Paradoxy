#!/usr/bin/env python3
"""Version C323/C324, source/run evidence and only this canonical transaction."""
from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
SID='S-RES-20260921-ASTRA-MARKOV-REVERSE'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
existing=set(git('diff','--cached','--name-only','-z').decode().split('\0'))-{''}
if existing:
    assert '--resume-owned-stage' in sys.argv
    assert existing<=set(json.loads((OUT/'version-paths.json').read_text())['paths'])
plan_commit=(OUT/'PLAN-COMMIT.txt').read_text().strip();assert git('rev-parse','HEAD').decode().strip()==plan_commit
result=json.loads((ROOT/'.codex/cognition/checkpoints'/SID/'result.json').read_text());assert result['status']=='CHECKPOINT_COMMITTED'
paths=set(result['paths'])|{'HoTT/CLAIM_EVIDENCE_MATRIX.md','HoTT/verification/PROOF_VERSION_CLOSURE.json','Astra继续尝试/断点与证明机制系统检查/第三十四轮执行报告.md'}
paths.update('HoTT/formal/agda-unimath/hott-z/'+name+'.agda' for name in ('MarkovRationalBounds','MarkovCountableChoice'))
for directory in ['audit/astra-markov-reverse-20260921','.codex/cognition/checkpoints/'+SID,'Astra继续尝试/断点与证明机制系统检查/第三十四轮执行报告','HoTT/verification/runs/20260921-MP-ASTRA-MARKOV-REVERSE-001-01']:
    paths.update(p.relative_to(ROOT).as_posix() for p in (ROOT/directory).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.agdai')
paths.add((OUT/'version-paths.json').relative_to(ROOT).as_posix());ordered=sorted(paths)
(OUT/'version-paths.json').write_text(json.dumps({'expected_parent':plan_commit,'paths':ordered},ensure_ascii=False,indent=2)+'\n')
subprocess.run(['git','add','--',*ordered],cwd=ROOT,check=True)
assert set(git('diff','--cached','--name-only','-z').decode().split('\0'))-{''}<=paths
p=subprocess.run(['git','diff','--cached','--check','--','.',':(exclude)audit/astra-markov-reverse-20260921/version-whitespace.txt'],cwd=ROOT,capture_output=True)
raw=p.stdout.decode();(OUT/'version-whitespace.txt').write_text(raw);bad=[]
for line in raw.splitlines():
    if ': trailing whitespace.' in line or ': new blank line at EOF.' in line:
        path=line.rsplit(':',2)[0]
        if '/before/' not in path and '/after/' not in path and not path.endswith(('/stdout.txt','.dot','.diff')):bad.append(line)
assert not bad,bad
extra=(OUT/'version-whitespace.txt').relative_to(ROOT).as_posix();subprocess.run(['git','add','--',extra],cwd=ROOT,check=True)
assert set(git('diff','--cached','--name-only','-z').decode().split('\0'))-{''}<=paths|{extra}
print(json.dumps({'selected_paths':len(paths),'raw_whitespace_lines':len(raw.splitlines())}),flush=True)
if '--commit' in sys.argv:
    subprocess.run(['git','commit','--quiet','--only','-m','AST-U05-MARKOV-REVERSE-01(step-1): C323–324实际界数据和显式可数选择反向; reflection=revised-in '+plan_commit[:7],'--',*ordered,extra],cwd=ROOT,check=True)
