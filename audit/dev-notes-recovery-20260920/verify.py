#!/usr/bin/env python3
"""Read-back of exact recovered blocks, preserved bodies, and one idempotent retry."""
import collections
import json
from pathlib import Path
import repair as m

data = json.loads((m.OUT / 'RECOVERY.json').read_text())
counts, paths, checks = collections.Counter(), {}, []
backup = m.ROOT / 'dev-notes/.dev-notes-skill-stage/recovery-backup-20260920'
for e in data['entries']:
    if e['status'] != 'ARCHIVED':
        continue
    source = backup / e['stage']
    meta = json.loads((source / 'meta.json').read_text())
    raw_prompt = (source / 'prompt.md').read_text()
    raw_answer = (source / 'answer.md').read_text()
    assert m.sha(raw_prompt.encode()) == e['prompt_file_sha256']
    assert m.sha(raw_answer.encode()) == e['answer_file_sha256']
    # Same documented single-terminal-LF handling as the canonical helper.
    prompt = raw_prompt[:-1] if raw_prompt.endswith('\n') else raw_prompt
    answer = raw_answer[:-1] if raw_answer.endswith('\n') else raw_answer
    note = Path(e['receipt']['path'])
    block = m.archive._turn_block(meta['turn_id'], meta['prepared_at'][:10], prompt, answer)
    assert note.read_text().count(block) == 1
    counts[e['session_id']] += 1
    paths[e['session_id']] = str(note.relative_to(m.ROOT))
    checks.append(dict(stage=e['stage'], exact_block_matches=1))

e = next(e for e in data['entries'] if e['status'] == 'ARCHIVED')
stage = m.ROOT / 'dev-notes/.dev-notes-skill-stage' / e['stage']
assert not stage.exists()
note = Path(e['receipt']['path'])
before = m.sha(note.read_bytes())
m.shutil.copytree(backup / e['stage'], stage)
retry = m.archive.commit_stage(stage=stage)
assert retry['status'] == 'DUPLICATE' and retry['stage_removed']
assert before == m.sha(note.read_bytes())

plan = json.loads((m.OUT / 'PLAN.json').read_text())
expected = dict(plan['before'])
for move in plan['moves']:
    expected[move['new']] = expected.pop(move['old'])
notes = m.inventory()
assert all(notes.get(p) == digest for p, digest in expected.items())
seqs = [int(Path(p).name[:4]) for p in notes]
assert len(seqs) == len(set(seqs))
assert m.sha(m.HELPER.read_bytes()) == plan['helper_sha256']
result = dict(status='PASS', recovered_exact_blocks=checks, recovery_counts=dict(counts),
              session_notes=paths, retry=retry, retry_note_unchanged=True,
              note_count=len(notes), original_bodies_preserved=len(expected),
              duplicate_sequences=0, helper_unchanged=True)
m.save('VERIFY.json', result)
print(json.dumps({k:v for k,v in result.items() if k not in ('recovered_exact_blocks','retry')},
                 ensure_ascii=False))
