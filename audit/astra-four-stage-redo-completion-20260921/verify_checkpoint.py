#!/usr/bin/env python3
"""Verify the actual phase-one completion checkpoint, without replaying mathematics."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SID = 'S-COM-20260921-ASTRA-FOUR-STAGE-REDO-COMPLETE'
RESULT = '.codex/cognition/checkpoints/' + SID + '/result.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


result_raw = (ROOT / RESULT).read_bytes()
result = json.loads(result_raw)
assert result['status'] == 'CHECKPOINT_COMMITTED' and result['revision'] == 210
state = json.loads((ROOT / '.codex/research/hott/STATE.json').read_text())
assert state['revision'] == 210 and state['latest_session'] == SID
assert state['execution_control']['status'] == 'FOUR_STAGE_REDO_PHASE_1_COMPLETE_WITH_SCOPE'
assert state['execution_control']['second_phase_status'] == 'NOT_OPENED'
retired = {'A-ASTRA-CONTINUING-GOAL-20260919', 'A-HOTT-MACHINE-OVERVIEW-GOAL-002', 'A-R4-HOTT-NAT-EFFECTIVITY-001', 'A-PREMISE-001'}
assert not retired.intersection(state['active'])
assert (ROOT / 'goal.md').read_text().splitlines()[0] == '# 四弹一体原方案 redo Goal'
head = json.loads((ROOT / '.codex/cognition/HEAD.json').read_text())
assert all(sha(ROOT / path) == digest for path, digest in head['tracked'].items())

three = subprocess.run(['python3', '-B', 'scripts/audit/verify_three_way_cognition.py'], cwd=ROOT, capture_output=True)
(OUT / 'three-way.stdout.txt').write_bytes(three.stdout)
(OUT / 'three-way.stderr.txt').write_bytes(three.stderr)
assert three.returncode == 0, three.stdout.decode() + three.stderr.decode()
shards = subprocess.run(['python3', '-B', 'scripts/audit/verify_governance_shards.py', '--out', str(OUT / 'shards.json')], cwd=ROOT, capture_output=True)
(OUT / 'shards.stdout.txt').write_bytes(shards.stdout)
(OUT / 'shards.stderr.txt').write_bytes(shards.stderr)
assert shards.returncode == 0, shards.stdout.decode() + shards.stderr.decode()

receipt = {
    'status': 'PHASE_1_CHECKPOINT_VERIFIED',
    'canonical_result': RESULT,
    'canonical_result_sha256': sha(ROOT / RESULT),
    'revision': 210,
    'latest_session': SID,
    'tracked_hashes_match': len(head['tracked']),
    'three_way_exit': three.returncode,
    'shard_verifier_exit': shards.returncode,
    'phase_1_verdict': 'ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED / ASSUMPTIONS_AND_TASKS_RECONCILED_WITH_SCOPE',
    'phase_2': 'NOT_OPENED',
    'mathematics_replayed': False,
    'scope': 'State and report delivery verification; no new theorem, kernel run, complete-library result, or global HoTT conclusion.',
}
(OUT / 'POST-CHECKPOINT.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(receipt, ensure_ascii=False))
