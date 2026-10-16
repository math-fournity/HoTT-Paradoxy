#!/usr/bin/env python3
"""Bounded controls for multiscale research instructions.

Synthetic finite task observations and actual repository loading only. This is
not a general semantic auditor, FCA theorem prover, or an LLM behavior eval.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def dump(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def finite_controls():
    # Synthetic shared-task inputs: every node requests one slot. Budgets belong
    # to whole tasks, not single nodes. IDs/chapters are not the grouping oracle.
    atoms = [{'id': c, 'consumer': g, 'slots': 1} for g, chars in [('shared-2', 'abc'), ('shared-3', 'def')] for c in chars]
    limits = {'shared-2': 2, 'shared-3': 3}
    def groups(records):
        return {g: tuple(sorted(x['id'] for x in records if x['consumer'] == g)) for g in limits}
    by_id = {a['id']: a for a in atoms}
    def observe(ids):
        consumers = {by_id[x]['consumer'] for x in ids}
        if len(consumers) != 1:
            return 'OUT_OF_TASK'
        return 'WITHIN_BUDGET' if sum(by_id[x]['slots'] for x in ids) <= limits[next(iter(consumers))] else 'OVER_BUDGET'
    unit_map = groups(atoms)
    old_schedule = [s for members in unit_map.values() for size in (1, 2) for s in itertools.combinations(members, size)]
    structural_schedule = list(unit_map.values())
    old_observed = [observe(x) for x in old_schedule]
    new_observed = [observe(x) for x in structural_schedule]
    # Source layout changes preserve all stable records; group from semantic key.
    layouts = [atoms, list(reversed(atoms)), atoms[::2] + atoms[1::2]]
    regroup = [groups(xs) for xs in layouts]
    # Explicit order effect in a synthetic state task; normal repeated-order run.
    ops = {'add': lambda x: x + 1, 'double': lambda x: 2 * x}
    def run(order):
        value = 0
        for op in order:
            value = ops[op](value)
        return value
    orders = [('add', 'double'), ('double', 'add')]
    ordered_results = [run(x) for x in orders]
    # Coverage is relative to these independently specified accepted questions.
    expected_questions = {'a', 'b', 'c', 'd', 'e', 'f', 'joint-shared-2', 'joint-shared-3'}
    leaves_only = {x['id'] for x in atoms}
    full = leaves_only | {'joint-shared-2', 'joint-shared-3'}
    return {
        'identity': 'synthetic finite specification; not HoTT evidence or AI discovery',
        'inputs': {'atoms': atoms, 'limits': limits},
        'observations': {
            'old_single_pair_schedule': old_schedule, 'old_outputs': old_observed,
            'structural_schedule': structural_schedule, 'structural_outputs': new_observed,
            'regrouped_layouts': regroup, 'orders': orders, 'ordered_outputs': ordered_results,
            'leaf_only_missing_questions': sorted(expected_questions - leaves_only),
        },
        'checks': {
            'single_pair_controls_all_normal': set(old_observed) == {'WITHIN_BUDGET'},
            'joint_task_difference_visible': new_observed == ['OVER_BUDGET', 'WITHIN_BUDGET'],
            'same_sources_repartition_preserves_declared_groups': all(x == regroup[0] for x in regroup),
            'erase_joint_relationship_loses_both_group_questions': expected_questions - leaves_only == {'joint-shared-2', 'joint-shared-3'},
            'full_declared_question_set_is_accepted': not expected_questions - full,
            'order_preserves_different_observations': ordered_results == [2, 1],
            'unordered_projection_would_merge_distinct_orders': sorted(orders[0]) == sorted(orders[1]) and ordered_results[0] != ordered_results[1],
        },
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    out = args.out.resolve(); out.mkdir(parents=True, exist_ok=False)
    checks, commands = {}, []
    control = finite_controls(); dump(out / 'finite-controls.json', control)
    checks.update(control['checks'])
    paths = (HERE / 'changed-paths.txt').read_text().splitlines()
    archive = HERE / 'before-partial-original.zip'
    with zipfile.ZipFile(archive) as z:
        before_bytes = {p: z.read('files/' + p) for p in paths}
        with tempfile.TemporaryDirectory(prefix='mo3-baseline-replay-') as td:
            z.extractall(td)
            replay=subprocess.run([sys.executable,'-B','第三轮机器统观/整备/handoff_snapshot.py','verify','--seal',str(Path(td).resolve()),'--expected-sha','56e9546968a224ff717b4b513bf4aa99c02e0a4787639f512581f335cc2331fd'],cwd=ROOT,capture_output=True)
            (out/'before-archive-verify.txt').write_bytes(replay.stdout+replay.stderr)
            checks['archived_partial_before_exact_bytes']=replay.returncode==0
    cases = [
        ('goal-route', [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'scripts/audit', '-p', 'test_goal_task_governance.py', '-v']),
        ('shards', [sys.executable, '-B', 'scripts/audit/verify_governance_shards.py']),
        ('invariants', [sys.executable, '-B', 'scripts/audit/verify_v5_invariants.py']),
        ('diff', ['git', 'diff', '--check', '--', *paths]),
    ]
    for role in ('execution', 'audit'):
        cases.append(('skill-' + role, [sys.executable, '-B', '/Users/aurolafly/.codex/skills/.system/skill-creator/scripts/quick_validate.py', str(ROOT/'.codex/skills'/('hott-machine-overview-'+role))]))
    for label, argv in cases:
        run = subprocess.run(argv, cwd=ROOT, capture_output=True, timeout=120)
        (out/(label+'-stdout.txt')).write_bytes(run.stdout); (out/(label+'-stderr.txt')).write_bytes(run.stderr)
        checks[label] = run.returncode == 0
        commands.append({'label': label, 'argv': argv, 'exit': run.returncode})
    current=(ROOT/'最高指示.md').read_text(); before=before_bytes['最高指示.md'].decode()
    quote=lambda s:re.findall(r'~~~text\n(.*?)\n~~~',s,re.S)[:2]
    checks['user_originals_unchanged']=len(quote(before))==2 and quote(before)==quote(current)
    checks['case_independence_retained']=all(x in current for x in ('HOTT_TOPIC_INDEPENDENCE_V1','引用或受到启发不能自动升级成全案翻译义务','不凑第二个'))
    checks['single_file']=not (ROOT/'最高指示').exists()
    q=current.split('### 7.1 必答理解题')[1].split('### 7.2')[0]
    checks['fourteen_questions']=re.findall(r'^(\d+)\. ',q,re.M)==[str(i) for i in range(1,15)]
    checks['audit24']=re.findall(r'^\|D(\d\d) ',current,re.M)==[f'{i:02d}' for i in range(1,25)]
    counts={p:len((ROOT/p).read_text()) for p in paths if p.endswith('提示词.txt')}
    checks['four_prompt_limits']=len(counts)==4 and all(n<=4000 for n in counts.values())
    upstream=[p for p in paths if 'COMPLETENESS/' in p]
    checks['obsolete_signal_only_clause_removed']=all('只对出现信号或文献要求' not in (ROOT/p).read_text() for p in upstream)
    checks['upstream_structural_entry_present']='结构驱动' in (ROOT/upstream[0]).read_text() and '无需先有低层异常' in (ROOT/upstream[1]).read_text()
    spec=importlib.util.spec_from_file_location('cognition',ROOT/'.codex/tools/cognition_runtime.py'); module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    plans={}
    for profile in ('governance','research'):
        plan=module.plan(ROOT,profile=profile);dump(out/(profile+'-plan.json'),plan)
        selected={d['path']:d['sha256'] for d in plan['documents']}
        checks[profile+'_current_directive']=selected.get('最高指示.md')==sha(ROOT/'最高指示.md')
        plans[profile]={'snapshot':plan['snapshot'],'highest':selected.get('最高指示.md'),'review_required':plan.get('review_required'),'promotion':plan['hydration_diagnostics']['query_first_promoted']}
    argv=[sys.executable,'-B','.codex/tools/cognition_runtime.py','plan','--profile','research','--task','MO3-GOVERNED-A']
    r=subprocess.run(argv,cwd=ROOT,capture_output=True,timeout=120)
    (out/'active-plan.json').write_bytes(r.stdout);(out/'active-plan-stderr.txt').write_bytes(r.stderr)
    checks['active_plan_readable']=r.returncode==0
    active=json.loads(r.stdout) if r.returncode==0 else {}
    additional=['dev-docs/第三轮机器统观多尺度覆盖改进工作方案-20260923.md','audit/第三轮机器统观多尺度覆盖再次自审-20260923.md']
    broken=[]
    for rel in paths+additional:
        p=ROOT/rel
        for m in re.finditer(r'\[[^\]]+\]\((?:<([^>]+)>|([^\)]+))\)',p.read_text()):
            target=m.group(1) or m.group(2)
            if '://' in target or target.startswith('#'):continue
            target=re.sub(r':\d+$','',target.split('#')[0])
            if not (p.parent/target).resolve().exists():broken.append({'path':rel,'target':target})
    checks['links_exist']=not broken
    identities=[{'path':p,'sha256':sha(ROOT/p),'before_sha256':hashlib.sha256(before_bytes[p]).hexdigest()} for p in paths]
    checks['all_26_planned_owners_changed']=len(identities)==26 and all(x['sha256']!=x['before_sha256'] for x in identities)
    result={'schema':'mo3-multiscale-evidence/v1','status':'PASS_WITH_SCOPE' if all(checks.values()) else 'FAIL','checks':checks,'commands':commands,'prompt_counts':counts,'plans':plans,'active_review_required':active.get('review_required'),'broken_links':broken,'identities':identities,'limits':['synthetic finite run observations only','not FCA or HoTT theorem proof','not LLM autonomous discovery','no active A/current-state mutation','fresh behavior NOT_RUN']}
    dump(out/'RESULT.json',result)
    print(json.dumps({k:result[k] for k in ('status','checks','prompt_counts','active_review_required','broken_links')},ensure_ascii=False,indent=2))
    return 0 if all(checks.values()) else 1


if __name__=='__main__':raise SystemExit(main())
