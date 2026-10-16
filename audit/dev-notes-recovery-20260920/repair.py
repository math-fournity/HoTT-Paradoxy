#!/usr/bin/env python3
"""Bounded repair of this repo's committed duplicate note names; no helper policy changes.

Use plan, then apply, then recover. Original note bodies stay byte-identical.
Generated JSON files are operation receipts, not a new registry.
"""
import argparse
import collections
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
HELPER = Path('/Users/aurolafly/.codex/skills/dev-notes-archive/scripts/archive_turn.py')
spec = importlib.util.spec_from_file_location('archive_turn', HELPER)
archive = importlib.util.module_from_spec(spec)
spec.loader.exec_module(archive)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def save(name, obj):
    archive._atomic_json(OUT / name, obj)

def inventory():
    return {str(p.relative_to(ROOT)): sha(p.read_bytes())
            for p in archive._note_files(ROOT / 'dev-notes')}

def plan():
    baseline = inventory()
    groups = collections.defaultdict(list)
    for rel in baseline:
        groups[int(Path(rel).name[:4])].append(rel)
    number = max(groups)
    moves = []
    for seq, paths in sorted(groups.items()):
        if len(paths) < 2:
            continue
        origins = []
        for rel in paths:
            assert git('show', 'HEAD:' + rel) == (ROOT / rel).read_bytes(), rel
            history = git('log', '--diff-filter=A', '--format=%ct %H', '--', rel).decode().splitlines()
            assert history, rel
            origins.append((history[-1], rel))
        for origin, rel in sorted(origins)[1:]:
            number += 1
            target = 'dev-notes/' + f'{number:04d}' + Path(rel).name[4:]
            assert not (ROOT / target).exists()
            moves.append(dict(old=rel, new=target, sha256=baseline[rel], first_add=origin))
    try:
        archive._next_note_path(ROOT / 'dev-notes', '2026-09-20', 'probe')
        observed = 'ACCEPTED'
    except archive.ArchiveError as exc:
        observed = exc.code
    result = dict(head=git('rev-parse', 'HEAD').decode().strip(), before=baseline,
                  helper_sha256=sha(HELPER.read_bytes()), moves=moves,
                  duplicate_groups=sum(len(v) > 1 for v in groups.values()),
                  allocator_before=observed)
    save('PLAN.json', result)
    paths = [m['old'] for m in moves]
    baseline_run = subprocess.run(['/Users/aurolafly/codex/tools/check_file_baseline.sh',
                                   *paths], cwd=ROOT, capture_output=True, text=True)
    assert baseline_run.returncode == 0, baseline_run.stderr
    save('BASELINE.json', dict(exit_code=baseline_run.returncode, stdout=baseline_run.stdout,
                               stderr=baseline_run.stderr))
    print(json.dumps(dict(status='PLANNED', notes=len(baseline), moves=len(moves),
                          allocator_before=observed)))

def apply():
    p = json.loads((OUT / 'PLAN.json').read_text())
    home = archive._resolved_code_home(None)
    with archive._project_lock(home, ROOT):
        assert sha(HELPER.read_bytes()) == p['helper_sha256']
        assert git('rev-parse', 'HEAD').decode().strip() == p['head']
        expected = dict(p['before'])
        for m in p['moves']:
            expected[m['new']] = expected.pop(m['old'])
        if inventory() == expected:
            print(json.dumps(dict(status='ALREADY_APPLIED')))
            return
        assert inventory() == p['before'], 'note inventory changed; replan before mutation'
        done = []
        try:
            for m in p['moves']:
                assert not (ROOT / m['new']).exists()
                assert git('show', p['head'] + ':' + m['old']) == (ROOT / m['old']).read_bytes()
            save('JOURNAL.json', dict(status='PREPARED', moves=p['moves']))
            for m in p['moves']:
                (ROOT / m['old']).rename(ROOT / m['new'])
                done.append(m)
            assert inventory() == expected, 'byte/content reconciliation failed'
            next_path = archive._next_note_path(ROOT / 'dev-notes', '2026-09-20', 'probe')
            save('RENAME.json', dict(status='RENAMED_VERIFIED', note_count=len(expected),
                                    moved=len(done), unchanged_body_hashes=True,
                                    next_sequence=int(next_path.name[:4]), moves=done))
            save('JOURNAL.json', dict(status='COMPLETED', moves=done))
        except BaseException:
            for m in reversed(done):
                assert not (ROOT / m['old']).exists()
                (ROOT / m['new']).rename(ROOT / m['old'])
            assert inventory() == p['before']
            save('JOURNAL.json', dict(status='ROLLED_BACK', moves=done))
            raise
    print(json.dumps(dict(status='RENAMED_VERIFIED', moved=len(done), preserved=len(expected))))

def recover():
    stage_root = ROOT / 'dev-notes' / archive.STAGE_ROOT_NAME
    backup = stage_root / 'recovery-backup-20260920'
    archive._ensure_private_dir(backup)
    entries = []
    paths = list(stage_root.glob('stage-*/meta.json'))
    paths.sort(key=lambda p: json.loads(p.read_text())['prepared_at'])
    for meta_path in paths:
        stage = meta_path.parent
        meta = json.loads(meta_path.read_text())
        prompt = (stage / 'prompt.md').read_text()
        answer = (stage / 'answer.md').read_text()
        row = dict(stage=stage.name, session_id=meta['session_id'], turn_id=meta['turn_id'],
                   prepared_at=meta['prepared_at'], prompt_file_sha256=sha(prompt.encode()),
                   answer_file_sha256=sha(answer.encode()))
        dest = backup / stage.name
        if not dest.exists():
            shutil.copytree(stage, dest)
        for f in ('meta.json', 'prompt.md', 'answer.md'):
            assert (stage / f).read_bytes() == (dest / f).read_bytes()
        if '__REPLACE_WITH_' in prompt + answer:
            row.update(status='PRESERVED_INCOMPLETE', reason='Original user prompt missing; not invented.')
        elif '<codex_internal_context' in prompt:
            row.update(status='PRESERVED_EXCLUDED', reason='Internal control context is not user-visible input.')
        else:
            receipt = archive.commit_stage(stage=stage)
            assert receipt['status'] in ('ARCHIVED', 'DUPLICATE') and receipt['stage_removed']
            row.update(status=receipt['status'], receipt=receipt)
        entries.append(row)
        save('RECOVERY.json', dict(status='IN_PROGRESS', entries=entries,
                                  evidence='Original pre-final staged texts, not Host-delivery certification.'))
    save('RECOVERY.json', dict(status='RECOVERY_PASS_WITH_DECLARED_EXCLUSIONS', entries=entries,
                              evidence='Original pre-final staged texts, not Host-delivery certification.'))
    print(json.dumps(dict(status='RECOVERY_PASS_WITH_DECLARED_EXCLUSIONS',
                          counts=dict(collections.Counter(e['status'] for e in entries)))))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['plan', 'apply', 'recover'])
    args = parser.parse_args()
    {'plan': plan, 'apply': apply, 'recover': recover}[args.action]()
