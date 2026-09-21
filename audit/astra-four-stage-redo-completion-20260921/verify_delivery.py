#!/usr/bin/env python3
"""Check exact committed phase-one completion artifacts without asserting a new theorem."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


version = json.loads((OUT / 'VERSION.json').read_text())
for rel in json.loads((OUT / 'version-paths.json').read_text())['paths']:
    if rel == (OUT / 'DELIVERY.json').relative_to(ROOT).as_posix():
        continue
    assert subprocess.check_output(['git', 'show', version['source_commit'] + ':' + rel], cwd=ROOT) == (ROOT / rel).read_bytes(), rel
post = json.loads((OUT / 'POST-CHECKPOINT.json').read_text())
assert sha(ROOT / post['canonical_result']) == post['canonical_result_sha256']
assert json.loads((ROOT / post['canonical_result']).read_text())['status'] == 'CHECKPOINT_COMMITTED'
assert 'ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED' in (ROOT / 'goal.md').read_text()
assert subprocess.run([
    'git', 'diff', '--quiet', '12199179ab128ad8a4b1ad376f6711fb2ba3011a..' + version['source_commit'],
    '--', 'HoTT/formal', 'HoTT/verification/runs', 'HoTT/CLAIM_EVIDENCE_MATRIX.md', 'HoTT/verification/PROOF_VERSION_CLOSURE.json',
], cwd=ROOT).returncode == 0
delivery = {
    'status': 'FOUR_STAGE_REDO_PHASE_1_DELIVERY_PASS',
    'source_commit': version['source_commit'],
    'plan_commit': version['plan_commit'],
    'committed_paths_byte_checked': len(json.loads((OUT / 'version-paths.json').read_text())['paths']) - 1,
    'canonical_revision': 210,
    'phase_1_verdict': post['phase_1_verdict'],
    'phase_2': post['phase_2'],
    'existing_math_evidence_preserved_without_new_replay': True,
    'math_paths_changed_since_precompletion_baseline': False,
    'scope': 'Completes the current two-stage goal only through the original-four-stage scope verdict. It neither proves HoTT globally sound/unsound nor begins a new candidate study.',
}
(OUT / 'DELIVERY.json').write_text(json.dumps(delivery, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(delivery, ensure_ascii=False))
