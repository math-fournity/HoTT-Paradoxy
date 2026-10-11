#!/usr/bin/env python3
"""Read-only snapshot of registered worktrees and branch-local changes."""
import datetime
import json
from pathlib import Path
import subprocess

ROOT = Path('/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0')
OUT = ROOT / 'docs/形式化综合研判-20261011/worktree-inventory.json'

def git(*args, cwd=ROOT):
    p = subprocess.run(['git', '--no-optional-locks', '-C', str(cwd), *args], capture_output=True, text=True, timeout=90)
    return p.returncode, p.stdout, p.stderr

code, raw, err = git('worktree', 'list', '--porcelain')
if code:
    raise RuntimeError(err)
rows = []
for block in raw.strip().split('\n\n'):
    fields = dict(line.split(' ', 1) if ' ' in line else (line, True) for line in block.splitlines())
    path = Path(fields['worktree'])
    row = {'path': str(path), 'head': fields.get('HEAD'), 'branch': fields.get('branch'), 'detached': fields.get('detached', False), 'exists': path.is_dir()}
    if not path.is_dir():
        row['error'] = 'registered path missing'
        rows.append(row)
        continue
    try:
        rc, status, stderr = git('status', '--porcelain=v1', '-z', '--untracked-files=all', cwd=path)
        if rc:
            row['status_error'] = stderr
        changes = []
        items = iter(status.split('\0'))
        for item in items:
            if not item:
                continue
            change = {'status': item[:2], 'path': item[3:]}
            if 'R' in item[:2] or 'C' in item[:2]:
                change['old_path'] = next(items, '')
            changes.append(change)
        row['working_changes'] = changes
        row['working_count'] = len(changes)
        rc, base, stderr = git('merge-base', 'dev', 'HEAD', cwd=path)
        row['merge_base_dev'] = base.strip() if not rc else None
        rc, unique, stderr = git('log', '--format=%H%x09%cI%x09%s', 'dev..HEAD', cwd=path)
        row['unique_commits'] = [dict(zip(('sha', 'date', 'subject'), line.split('\t', 2))) for line in unique.splitlines()]
        row['unique_commit_count'] = len(row['unique_commits'])
        if row['merge_base_dev']:
            rc, diff, stderr = git('diff', '--name-status', '-z', row['merge_base_dev'], 'HEAD', cwd=path)
            values = iter(diff.split('\0'))
            committed = []
            for state in values:
                if not state:
                    continue
                first = next(values, '')
                d = {'status': state, 'path': first}
                if state.startswith(('R', 'C')):
                    d['old_path'] = first
                    d['path'] = next(values, '')
                committed.append(d)
            row['branch_changes'] = committed
        evidence = []
        for item in changes:
            p = path / item['path']
            if p.is_file() and (item['path'].startswith(('HoTT/', '.claude/', '.workbuddy-ai/', '形式化追踪/', '外部资料/', 'dev-docs/')) or p.suffix in ('.lean', '.agda', '.v', '.smt2')):
                stat = p.stat()
                evidence.append({'path': item['path'], 'bytes': stat.st_size, 'mtime': datetime.datetime.fromtimestamp(stat.st_mtime).astimezone().isoformat(timespec='seconds')})
        row['relevant_working_files'] = evidence
    except Exception as exc:
        row['error'] = repr(exc)
    rows.append(row)
rc, dev, err = git('rev-parse', 'dev')
result = {'captured_at': datetime.datetime.now().astimezone().isoformat(timespec='seconds'), 'canonical_dev': dev.strip(), 'worktree_count': len(rows), 'scope': 'all registered worktrees; working files plus branch-unique commits and merge-base changes; no content review implied', 'worktrees': rows}
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
for r in rows:
    changed = r.get('working_changes', [])
    formal = [x for x in changed if x['path'].startswith('HoTT/') or x['path'].endswith(('.lean', '.agda', '.smt2'))]
    print(f"{r['path']} | {r.get('branch') or 'detached'} | dirty={len(changed)} formal={len(formal)} unique_commits={r.get('unique_commit_count', '?')} error={r.get('error', '-')}")
print('Inventory:', OUT)
