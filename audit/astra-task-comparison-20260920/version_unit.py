#!/usr/bin/env python3
"""Version the exact arithmetic comparison proof, run and canonical transaction."""
from pathlib import Path
import json, subprocess, sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = 'S-RES-20260920-ASTRA-TASK-COMPARISON'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


assert not git('diff', '--cached', '--name-only')
plan_commit = (OUT / 'PLAN-COMMIT.txt').read_text().strip()
assert git('rev-parse', 'HEAD').decode().strip() == plan_commit
result = json.loads((ROOT / '.codex/cognition/checkpoints' / SID / 'result.json').read_text())
assert result['status'] == 'CHECKPOINT_COMMITTED'
paths = set(result['paths']) | {
    'HoTT/CLAIM_EVIDENCE_MATRIX.md',
    'HoTT/verification/PROOF_VERSION_CLOSURE.json',
    'HoTT/formal/dedekind-omega-missile/Sqrt2TaskComparison.agda',
    'Astra继续尝试/断点与证明机制系统检查/第十九轮执行报告.md',
}
for directory in [
    'audit/astra-task-comparison-20260920',
    '.codex/cognition/checkpoints/' + SID,
    'HoTT/verification/runs/20260920-MP-ASTRA-SQRT2-TASK-COMPARISON-001-01',
    'Astra继续尝试/断点与证明机制系统检查/第十九轮执行报告',
]:
    paths.update(p.relative_to(ROOT).as_posix() for p in (ROOT / directory).rglob('*')
                 if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.agdai')
paths.add((OUT / 'version-paths.json').relative_to(ROOT).as_posix())
ordered = sorted(paths)
(OUT / 'version-paths.json').write_text(json.dumps({
    'expected_parent': plan_commit, 'paths': ordered,
}, ensure_ascii=False, indent=2) + '\n')
subprocess.run(['git', 'add', '--', *ordered], cwd=ROOT, check=True)
assert set(git('diff', '--cached', '--name-only', '-z').decode().split('\0')) - {''} <= paths
check = subprocess.run([
    'git', 'diff', '--cached', '--check', '--', '.',
    ':(exclude)audit/astra-task-comparison-20260920/version-whitespace.txt',
], cwd=ROOT, capture_output=True)
raw = check.stdout.decode()
(OUT / 'version-whitespace.txt').write_text(raw)
bad = []
for line in raw.splitlines():
    if ': trailing whitespace.' in line or ': new blank line at EOF.' in line:
        path = line.rsplit(':', 2)[0]
        if '/before/' not in path and '/after/' not in path and not path.endswith(('/stdout.txt', '.dot')):
            bad.append(line)
assert not bad, bad
extra = (OUT / 'version-whitespace.txt').relative_to(ROOT).as_posix()
subprocess.run(['git', 'add', '--', extra], cwd=ROOT, check=True)
assert set(git('diff', '--cached', '--name-only', '-z').decode().split('\0')) - {''} <= paths | {extra}
print(json.dumps({'selected_paths': len(paths), 'raw_whitespace_lines': len(raw.splitlines())}), flush=True)
if '--commit' in sys.argv:
    subprocess.run([
        'git', 'commit', '--quiet', '--only', '-m',
        'AST-U02-SQRT2-TASK-COMPARISON-01(step-1): 原规格对接与九族算术完成对照C302–303; reflection=revised-in ' + plan_commit[:7],
        '--', *ordered, extra,
    ], cwd=ROOT, check=True)
