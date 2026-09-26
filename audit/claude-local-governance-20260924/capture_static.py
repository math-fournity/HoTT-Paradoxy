#!/usr/bin/env python3
"""One-shot, read-only source inspection; writes only a new evidence directory.

No Claude model session, installation, checkpoint, Git mutation or proof run.
The declared reading list records the author's review scope, not model comprehension.
"""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / sys.argv[1]
OUT.mkdir(exist_ok=False)

def save(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def run(argv):
    p = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    return {'argv': argv, 'exit': p.returncode, 'stdout': p.stdout, 'stderr': p.stderr}

def identity(p):
    b = p.read_bytes()
    return {'path': str(p.relative_to(ROOT)), 'bytes': len(b),
            'lines': len(b.splitlines()), 'sha256': hashlib.sha256(b).hexdigest()}

reviewed = [
    'AGENTS.md', '.codex/AGENTS.md', '.codex/cognition/PROTOCOL.md',
    '.codex/cognition/TASK_ROUTING.md', '.codex/cognition/LOAD_SET.json',
    '.codex/skills/SKILL_ROLES.json', '最高指示.md', 'feature-list.md', 'rulings.md',
    'docs/README.md', 'docs/ai/README.md', 'dev-docs/README.md',
    'docs/design/detailed/认知水合关系与检查点事务合同.md',
    'docs/quality/数学结论机器证明与证据留存规范.md',
    'docs/quality/长治理文档分片与索引合同.md',
    'dev-docs/Goal任务项目治理化与全局复用方案-20260923.md',
    '治理框架v5设计方案/003 - 宿主中立化设计：单一真值树与双宿主接入.md',
    '第三轮机器统观/README.md', '第三轮机器统观/续做整备/接续方案.md',
    '第三轮机器统观/整备/Session-A-工作闭包.md',
    '第三轮机器统观/整备/Session-B-工作闭包.md',
    '第三轮机器统观/治理整备/Session-A-goal提示词.txt',
    '第三轮机器统观/治理整备/Session-B-goal提示词.txt',
    '第三轮机器统观/续做整备/Session-C-Goal7启动词.txt',
    '第三轮机器统观/续做整备/Session-D-Goal7审计启动词.txt',
    '.zcode/commands/closure.md', '.zcode/commands/checkpoint-dry.md',
    'README/001 - 当前入口与关键文件.md', 'README/003 - 加载方案与验证入口.md',
    'MEMORY/002 - 当前证据上限与恢复入口.md',
]
reviewed += [str(p.relative_to(ROOT)) for p in sorted(ROOT.glob('goal*.md'))
             if p.name != 'goal-3-工作路径树.md']
reviewed += [str(p.relative_to(ROOT)) for p in sorted((ROOT / '.codex/skills').rglob('*.md'))]
reviewed += [str(p.relative_to(ROOT)) for p in sorted(
    (ROOT / '.codex/research/hott').glob('HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS*.md'))]
reviewed += [str(p.relative_to(ROOT)) for p in sorted(
    (ROOT / '.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS').glob('*.md'))]
reviewed = sorted(set(reviewed))
save('source-inventory.json', {
    'captured_at': dt.datetime.now(dt.timezone.utc).isoformat(),
    'scope': 'physical files fully reviewed for host/path/lifecycle adaptation; not a mathematical audit',
    'reading_assertion': 'AUTHOR_DECLARED_FULL_TEXT_REVIEW_NOT_MACHINE_CERTIFIED',
    'files': [identity(ROOT / p) for p in reviewed],
    'not_full_read': ['四件套数学正文及全部投影', 'STATE全体records', 'MEMORY历史日志',
                      'sources/历史快照', '历史checkpoint/封存副本', '所有proof/run',
                      'v5设计其余历史分片', '全部共享全局治理主库'],
})
save('git.json', {n: run(a) for n, a in {
    'root': ['git', 'rev-parse', '--show-toplevel'],
    'head': ['git', 'rev-parse', 'HEAD'],
    'branch': ['git', 'branch', '--show-current'],
    'common_dir': ['git', 'rev-parse', '--git-common-dir'],
    'status': ['git', '-c', 'core.quotepath=false', 'status', '--short'],
    'index': ['git', '-c', 'core.quotepath=false', 'diff', '--cached', '--name-status'],
    'tags': ['git', 'tag', '--points-at', 'HEAD'],
}.items()})
patterns = re.compile(r'Codex|CODEX|Astra|gpt-|/Users/|/Volumes/|/mnt/|sandbox:|第五闭包|三件套|/goal|create_goal|update_goal|apply_patch|fork_turns')
scan = [ROOT / p for p in reviewed]
scan += list((ROOT / '.codex/skills').rglob('*.py'))
scan += [ROOT / '.codex/tools/cognition_runtime.py']
hits = []
for p in sorted(set(scan)):
    for n, line in enumerate(p.read_text().splitlines(), 1):
        if patterns.search(line):
            hits.append({'path': str(p.relative_to(ROOT)), 'line': n, 'text': line})
save('host-path-hits.json', {'scope_files': len(set(scan)), 'hits': hits})
plans = {}
for profile in ['governance', 'research']:
    r = run(['python3', '-B', '.codex/tools/cognition_runtime.py', 'plan', '--profile', profile])
    save(profile + '-plan-command.json', r)
    if r['exit'] == 0:
        s = json.loads(r['stdout'])
        save(profile + '-plan.json', s)
        plans[profile] = {k: s[k] for k in ['snapshot', 'total_bytes', 'total_lines', 'review_required']}
        plans[profile]['documents'] = len(s['documents'])
        plans[profile]['full_set_bytes'] = sum(d['bytes'] for d in s['documents'] if d['layer'] == 'always_full_documents')
        plans[profile]['query_first_promoted'] = s['hydration_diagnostics']['query_first_promoted']
    else:
        plans[profile] = {'exit': r['exit'], 'stderr': r['stderr']}
save('plan-summary.json', plans)
s = json.loads((ROOT / '.codex/research/hott/STATE.json').read_text())
save('state-hot.json', {k: s[k] for k in ['current_core', 'active', 'latest_session', 'unresolved', 'revision']})
save('claude-version.json', run(['claude', '--version']))
home = Path.home()
settings = json.loads((home / '.claude/settings.json').read_text())
save('claude-safe-config.json', {
    'settings_keys': sorted(settings),
    'permissions': settings.get('permissions'),
    'agents_md': settings.get('pluginConfigs', {}).get('agents-md@builtin'),
    'environment_keys_only': sorted(settings.get('env', {})),
    'personal_skill_names': sorted(p.name for p in (home / '.claude/skills').iterdir()),
    'project_claude_directory_exists': (ROOT / '.claude').exists(),
    'project_claude_md_exists': (ROOT / 'CLAUDE.md').exists(),
})
m = json.loads((ROOT / '.codex/skills/hott-paradox-research/MANIFEST.json').read_text())
base = ROOT / '.codex/skills/hott-paradox-research'
diffs = []
for row in m['files']:
    p = base / row['path']
    actual = identity(p)
    if actual['sha256'] != row['sha256'] or actual['bytes'] != row['bytes']:
        diffs.append({'path': row['path'], 'recorded': row, 'actual': actual})
save('legacy-manifest-check.json', {'declared_version': m['version'], 'entries': len(m['files']), 'mismatches': diffs,
                                 'meaning': 'historical delivery manifest cannot certify current installation'})
print(json.dumps({'out': str(OUT), 'reviewed_files': len(reviewed), 'scanned_files': len(set(scan)),
                  'hits': len(hits), 'plans': plans, 'legacy_manifest_mismatches': len(diffs)}, ensure_ascii=False))
