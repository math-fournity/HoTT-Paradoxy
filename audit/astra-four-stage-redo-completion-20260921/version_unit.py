#!/usr/bin/env python3
"""Stage only the phase-one state transaction and its direct audit evidence."""
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = 'S-COM-20260921-ASTRA-FOUR-STAGE-REDO-COMPLETE'
PLAN_COMMIT = '8b625564ba32ebd8d514166ed5712b915b21abd0'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


existing = set(git('diff', '--cached', '--name-only', '-z').decode().split('\0')) - {''}
if existing:
    assert '--resume-owned-stage' in sys.argv
    allowed = set(json.loads((OUT / 'version-paths.json').read_text())['paths'])
    assert existing <= allowed
assert git('rev-parse', 'HEAD').decode().strip() == PLAN_COMMIT
result = json.loads((ROOT / '.codex/cognition/checkpoints' / SID / 'result.json').read_text())
assert result['status'] == 'CHECKPOINT_COMMITTED' and result['revision'] == 210
paths = set(result['paths'])
for directory in (OUT, ROOT / '.codex/cognition/checkpoints' / SID, ROOT / '.codex/research/hott/sessions' / SID):
    paths.update(path.relative_to(ROOT).as_posix() for path in directory.rglob('*') if path.is_file() and '__pycache__' not in path.parts)
paths.add((OUT / 'version-paths.json').relative_to(ROOT).as_posix())
paths.add((OUT / 'version-whitespace.txt').relative_to(ROOT).as_posix())
(OUT / 'version-paths.json').write_text(json.dumps({'expected_parent': PLAN_COMMIT, 'paths': sorted(paths)}, ensure_ascii=False, indent=2) + '\n')
(OUT / 'version-whitespace.txt').write_text('')
subprocess.run(['git', 'add', '--', *sorted(paths)], cwd=ROOT, check=True)
assert set(git('diff', '--cached', '--name-only', '-z').decode().split('\0')) - {''} <= paths
checked = subprocess.run(['git', 'diff', '--cached', '--check'], cwd=ROOT, capture_output=True)
raw = checked.stdout.decode()
bad = []
for line in raw.splitlines():
    if ': trailing whitespace.' in line or ': new blank line at EOF.' in line:
        path = line.rsplit(':', 2)[0]
        if '/before/' not in path and '/after/' not in path and not path.endswith(('.stdout.txt', '.dot', '.diff')):
            bad.append(line)
assert not bad, bad
(OUT / 'version-whitespace.txt').write_text(raw)
subprocess.run(['git', 'add', '--', str(OUT / 'version-whitespace.txt')], cwd=ROOT, check=True)
print(json.dumps({'selected_paths': len(paths), 'raw_whitespace_lines_preserved': len(raw.splitlines())}, ensure_ascii=False))
if '--commit' in sys.argv:
    subprocess.run([
        'git', 'commit', '--quiet', '--only',
        '-m', 'FOUR-STAGE-REDO-PHASE1-COMPLETE(step-1): 保存范围判词、状态收束与停止裁决; reflection=revised-in ' + PLAN_COMMIT[:7],
        '--', *sorted(paths),
    ], cwd=ROOT, check=True)
