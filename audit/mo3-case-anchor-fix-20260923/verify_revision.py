#!/usr/bin/env python3
"""Check the changed HoTT research instructions, without editing A or STATE.

Generated files are one-run evidence, not canonical research state. Text checks
test explicit contracts only; semantic review and fresh behavior are separate.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    paths = HERE.joinpath('changed-paths.txt').read_text().splitlines()
    before = HERE / 'before/files'
    checks, commands = {}, []
    state_path = ROOT / '.codex/research/hott/STATE.json'
    state_before = sha(state_path)
    cases = [
        ('goal-route-tests', [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'scripts/audit', '-p', 'test_goal_task_governance.py', '-v']),
        ('v5-invariants', [sys.executable, '-B', 'scripts/audit/verify_v5_invariants.py']),
        ('shards', [sys.executable, '-B', 'scripts/audit/verify_governance_shards.py']),
        ('before-seal', [sys.executable, '-B', '第三轮机器统观/整备/handoff_snapshot.py', 'verify', '--seal', str(HERE / 'before'), '--expected-sha', 'c6f552d481578b34f80f24ebce910df5260657c6bd4cb9fe417d841497dae5d2']),
        ('historical-seal', [sys.executable, '-B', '第三轮机器统观/整备/handoff_snapshot.py', 'verify', '--seal', '第三轮机器统观/整备/验证/preparation-seal', '--expected-sha', '091a1d1548c1248602458dd96570857d586f184d92624e6a3825ee95a2b06e1e']),
        ('changed-diff', ['git', 'diff', '--check', '--', *paths]),
    ]
    for role in ('execution', 'audit'):
        cases.append(('skill-' + role, [sys.executable, '-B', '/Users/aurolafly/.codex/skills/.system/skill-creator/scripts/quick_validate.py', str(ROOT / '.codex/skills' / ('hott-machine-overview-' + role))]))
    for label, argv in cases:
        start = time.monotonic()
        run = subprocess.run(argv, cwd=ROOT, capture_output=True, timeout=120)
        (out / (label + '-stdout.txt')).write_bytes(run.stdout)
        (out / (label + '-stderr.txt')).write_bytes(run.stderr)
        checks[label] = run.returncode == 0
        commands.append({'label': label, 'argv': argv, 'exit': run.returncode, 'seconds': time.monotonic() - start})

    current = (ROOT / '最高指示.md').read_text()
    old = (before / '最高指示.md').read_text()
    originals = lambda s: re.findall(r'~~~text\n(.*?)\n~~~', s, re.S)[:2]
    checks['two_user_originals_byte_identical'] = len(originals(old)) == 2 and originals(old) == originals(current)
    original_circle = lambda s: next(x for x in s.splitlines() if x.startswith('> 我再给你看一个抽象导致悖论的例子'))
    checks['circle_original_preserved'] = original_circle(old) == original_circle(current)
    questions = current.split('### 7.1 必答理解题\n', 1)[1].split('### 7.2 ', 1)[0]
    checks['fourteen_questions_retained'] = re.findall(r'^(\d+)\. ', questions, re.M) == [str(i) for i in range(1, 15)]
    checks['three_representations_retained'] = all('**' + x + '次：' in current for x in ('第一', '第二', '第三'))
    checks['twenty_four_audit_dimensions_retained'] = re.findall(r'^\|D(\d\d) ', current, re.M) == [f'{i:02d}' for i in range(1, 25)]
    checks['monolithic_directive_retained'] = not (ROOT / '最高指示').exists() and 'governance-shard-index:' not in current
    checks['independent_task_contract_present'] = all(x in current for x in ('HOTT_TOPIC_INDEPENDENCE_V1', '**X_i**', '**X_h**', '**X_ring**', '无需先找到一个历史悖论作为祖先'))
    checks['unconditional_circle_question_removed'] = '11. 用户圆环原文中' not in current and '仅当实际引用、类比或声称回答历史X_h时' in questions
    checks['forced_historical_pair_removed'] = '每次选**表面相异的两例**' not in current and '历史六例中哪两例' not in questions
    checks['inspiration_does_not_require_full_case_translation'] = '引用或受到启发不能自动升级成全案翻译义务' in current
    third = current.split('**第三次：', 1)[1].split('\n\n', 1)[0]
    checks['third_representation_does_not_force_second_candidate'] = '不凑第二个' in third and '再生成一个候选' not in third
    goal5 = (ROOT / 'goal-5.md').read_text()
    checks['fixed_topic_holdout_removed'] = '不以存在/交付为中心的留出主题' not in goal5 and '不预先固定成' in goal5
    checks['scope_and_proof_requirements_retained'] = all(x in goal5 for x in ('S1', 'S2', 'S3', 'S4', 'S5', 'TheoryConstruct × AbstractionChange', '结构驱动', '本轮整体须实际尝试机制不同的过程', '数学结论交付规范', '原生 HoTT/Path/HIT/univalence'))
    counts = {}
    for folder in ('整备', '治理整备'):
        for role in ('A', 'B'):
            path = f'第三轮机器统观/{folder}/Session-{role}-goal提示词.txt'
            text = (ROOT / path).read_text()
            counts[path] = {'unicode_codepoints': len(text), 'sha256': sha(ROOT / path)}
    checks['all_four_prompts_under_4000'] = all(x['unicode_codepoints'] <= 4000 for x in counts.values())

    broken, link_count = [], 0
    for rel in paths:
        p = ROOT / rel
        for match in re.finditer(r'\[[^\]]+\]\((?:<([^>]+)>|([^\)]+))\)', p.read_text()):
            target = match.group(1) or match.group(2)
            if '://' in target or target.startswith('#'):
                continue
            link_count += 1
            target = re.sub(r':\d+$', '', target.split('#')[0])
            if not (p.parent / target).resolve().exists():
                broken.append({'file': rel, 'target': target})
    checks['changed_file_links_exist'] = not broken

    spec = importlib.util.spec_from_file_location('cognition', ROOT / '.codex/tools/cognition_runtime.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    plans = {}
    for profile in ('governance', 'research'):
        plan = module.plan(ROOT, profile=profile)
        dump(out / (profile + '-plan.json'), plan)
        selected = {d['path']: d['sha256'] for d in plan['documents'] if d['path'] in ('最高指示.md', '.codex/cognition/TASK_ROUTING.md')}
        plans[profile] = {'snapshot': plan['snapshot'], 'selected': selected, 'promotion': plan['hydration_diagnostics']['query_first_promoted']}
        checks[profile + '_loads_current_directive'] = selected.get('最高指示.md') == sha(ROOT / '最高指示.md') and selected.get('.codex/cognition/TASK_ROUTING.md') == sha(ROOT / '.codex/cognition/TASK_ROUTING.md')
    argv = [sys.executable, '-B', '.codex/tools/cognition_runtime.py', 'plan', '--profile', 'research', '--task', 'MO3-GOVERNED-A']
    run = subprocess.run(argv, cwd=ROOT, capture_output=True, timeout=120)
    (out / 'active-task-plan.json').write_bytes(run.stdout)
    (out / 'active-task-plan-stderr.txt').write_bytes(run.stderr)
    checks['active_task_plan_readable'] = run.returncode == 0
    active_plan = json.loads(run.stdout) if run.returncode == 0 else {}
    # Stale pins are evidence for mandatory rereading, not a failing source seal.
    stale = {k: v for k, v in active_plan.items() if 'review' in k or 'stale' in k}
    state = json.loads(state_path.read_text())
    rows = []
    for path in paths:
        rows.append({'path': path, 'before_sha256': sha(before / path), 'after_sha256': sha(ROOT / path), 'changed': (before / path).read_bytes() != (ROOT / path).read_bytes()})
    checks['all_planned_paths_changed'] = all(x['changed'] for x in rows)
    result = {
        'schema_version': 'mo3-case-anchor-fix-evidence/v1',
        'status': 'PASS_WITH_SCOPE' if all(checks.values()) else 'FAIL',
        'checks': checks, 'commands': commands, 'prompt_counts': counts,
        'links_checked': link_count, 'broken_links': broken, 'plans': plans,
        'active_task_review_fields': stale,
        'state_observation': {'revision': state['revision'], 'before_sha256': state_before, 'after_sha256': sha(state_path), 'writer': 'verifier does not write STATE; concurrent A may change it'},
        'paths': rows,
        'limits': ['text checks and real loader behavior only', 'manual semantic audit is separately recorded', 'fresh LLM behavior NOT_RUN', 'active A consumption NOT_CERTIFIED', 'no mathematics or A result audited'],
    }
    dump(out / 'RESULT.json', result)
    print(json.dumps({'status': result['status'], 'checks': checks, 'prompt_counts': counts, 'active_task_review_fields': stale}, ensure_ascii=False, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
