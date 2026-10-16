#!/usr/bin/env python3
"""Capture scoped mechanical evidence for project/global Goal-task integration.

Only this task's output directory is written. No current-state mutation or model run.
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
SHARED = Path("/Users/aurolafly/codex-worktrees/goal-task-governance-20260923")
RUNTIME = Path("/Users/aurolafly/.codex")
MIRROR = Path("/Users/aurolafly/.agents")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    a = parser.parse_args()
    out = a.out.resolve(); out.mkdir(parents=True, exist_ok=False)
    checks = {}; commands = []
    cases = [
        ("goal-route-tests", [sys.executable, "-B", "-m", "unittest", "discover", "-s", "scripts/audit", "-p", "test_goal_task_governance.py", "-v"], ROOT),
        ("v5-invariants", [sys.executable, "-B", "scripts/audit/verify_v5_invariants.py"], ROOT),
        ("three-way-tests", [sys.executable, "-B", "-m", "unittest", "discover", "-s", "scripts/audit", "-p", "test_three_way_cognition.py", "-v"], ROOT),
        ("shards", [sys.executable, "-B", "scripts/audit/verify_governance_shards.py"], ROOT),
        ("shared-guidance", ["bash", str(SHARED / "tools/validate_guidance_completeness.sh"), str(SHARED), str(RUNTIME)], ROOT),
        ("shared-purpose", ["bash", str(SHARED / "tools/validate_cognitive_closure_purpose.sh"), str(SHARED), str(RUNTIME)], ROOT),
        ("old-seal", [sys.executable, "-B", "第三轮机器统观/整备/handoff_snapshot.py", "verify", "--seal", "第三轮机器统观/整备/验证/preparation-seal", "--expected-sha", "091a1d1548c1248602458dd96570857d586f184d92624e6a3825ee95a2b06e1e"], ROOT),
        ("shared-diff", ["git", "diff", "--check"], SHARED),
        ("runtime-diff", ["git", "diff", "--check"], RUNTIME),
        ("project-diff", ["git", "diff", "--check", "--", "AGENTS.md", ".codex/AGENTS.md", ".codex/cognition/LOAD_SET.json", ".codex/cognition/PROTOCOL.md", ".codex/skills", "最高指示.md", "README/001 - 当前入口与关键文件.md", "feature-list.md", "rulings.md", "dev-docs/README.md", "docs/ai/README.md"], ROOT),
    ]
    for label, argv, cwd in cases:
        start = time.monotonic()
        run = subprocess.run(argv, cwd=cwd, capture_output=True, timeout=120)
        (out / (label + '-stdout.txt')).write_bytes(run.stdout)
        (out / (label + '-stderr.txt')).write_bytes(run.stderr)
        checks[label] = run.returncode == 0
        commands.append({"label": label, "argv": argv, "cwd": str(cwd), "exit": run.returncode, "seconds": time.monotonic() - start})
    for name in ("hott-machine-overview-execution", "hott-machine-overview-audit"):
        argv=[sys.executable, "-B", str(RUNTIME / "skills/.system/skill-creator/scripts/quick_validate.py"), str(ROOT / '.codex/skills' / name)]
        run=subprocess.run(argv,capture_output=True)
        (out/(name+'-validation.txt')).write_bytes(run.stdout+run.stderr)
        checks[name] = run.returncode == 0
    mirror_rows=[]
    for name in ('repo-cognitive-closure','repo-cognition-governance'):
        first=RUNTIME/'skills'/name/'SKILL.md';second=MIRROR/'skills'/name/'SKILL.md'
        mirror_rows.append({'name':name,'runtime_sha256':sha(first),'discovery_copy_sha256':sha(second),'identical':first.read_bytes()==second.read_bytes()})
    checks['global_discovery_copy_parity']=all(r['identical'] for r in mirror_rows)
    counts={}
    for role in ('A','B'):
        p=ROOT/f'第三轮机器统观/治理整备/Session-{role}-goal提示词.txt'
        counts[role]={'unicode_codepoints':len(p.read_text()),'utf8_bytes':p.stat().st_size,'sha256':sha(p)}
    checks['prompt_limit']=all(r['unicode_codepoints']<=4000 for r in counts.values())
    paths=[ROOT/'goal-6.md',ROOT/'goal-6-audit.md',ROOT/'第三轮机器统观/README.md',ROOT/'最高指示.md',ROOT/'dev-docs/Goal任务项目治理化与全局复用方案-20260923.md',ROOT/'.codex/skills/hott-machine-overview-execution/SKILL.md',ROOT/'.codex/skills/hott-machine-overview-audit/SKILL.md',SHARED/'docs/design/detailed/Goal任务项目治理化合同.md']
    broken=[];links=0
    for p in paths:
        for m in re.finditer(r'\[[^\]]+\]\((?:<([^>]+)>|([^\)]+))\)',p.read_text()):
            target=m.group(1) or m.group(2)
            if '://' in target or target.startswith('#'):continue
            links+=1
            if not (p.parent/target.split('#')[0]).resolve().exists():broken.append({'file':str(p),'target':target})
    checks['local_links']=not broken
    spec=importlib.util.spec_from_file_location('cognition',ROOT/'.codex/tools/cognition_runtime.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    plans={}
    for profile in ('governance','research'):
        p=mod.plan(ROOT,profile=profile)
        write_json(out/(profile+'-plan.json'),p)
        plans[profile]={'snapshot':p['snapshot'],'documents':len(p['documents']),'full_set_documents':p['full_set_documents'],'promoted':p['hydration_diagnostics']['query_first_promoted'],'mandatory':{x['path']:x['sha256'] for x in p['documents'] if x['path'] in ['最高指示.md','.codex/cognition/TASK_ROUTING.md']}}
    state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    meta={'schema_version':'goal-task-integration-evidence/v1','status':'PASS_WITH_SCOPE' if all(checks.values()) else 'FAIL','checks':checks,'commands':commands,'prompt_counts':counts,'links_checked':links,'broken_links':broken,'mirror_parity':mirror_rows,'plans':plans,'state':{'revision':state['revision'],'latest_session':state['latest_session'],'sha256':sha(ROOT/'.codex/research/hott/STATE.json')},'identities':{str(p):sha(p) for p in paths},'limits':['mechanical and current-session evidence only','fresh/actual compaction behavior NOT_RUN','A/B research NOT_STARTED','no commit/tag/release','project STATE unchanged by this verifier']}
    write_json(out/'RESULT.json',meta)
    print(json.dumps({k:v for k,v in meta.items() if k not in ['commands','identities']},ensure_ascii=False,indent=2))
    return 0 if all(checks.values()) else 1


if __name__=='__main__':raise SystemExit(main())
