#!/usr/bin/env python3
"""Verify Goal7 task preparation and real loader graph fixtures.

Does not start C/D, modify STATE, certify natural-language comprehension or
certify research coverage. All writes are owned one-run evidence directories.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    out=a.out.resolve();out.mkdir(parents=True,exist_ok=False)
    checks={};commands=[];state_path=ROOT/'.codex/research/hott/STATE.json';state_before=sha(state_path)
    cases=[
      ('existing-goal-routes',[sys.executable,'-B','-m','unittest','discover','-s','scripts/audit','-p','test_goal_task_governance.py','-v']),
      ('governance-invariants',[sys.executable,'-B','scripts/audit/verify_v5_invariants.py']),
      ('shards',[sys.executable,'-B','scripts/audit/verify_governance_shards.py']),
      ('old-A-seal',[sys.executable,'-B','第三轮机器统观/整备/handoff_snapshot.py','verify','--seal','第三轮机器统观/Session-A/交付/final-002','--expected-sha','e3181cb8111c7a46ca9324cc8f070ad26dd501447d26aad79a87e52e3eb32fdd']),
      ('changed-diff',['git','diff','--check','--','AGENTS.md','.codex/AGENTS.md','.codex/cognition/TASK_ROUTING.md','.codex/skills/hott-local-session-governance/SKILL.md','.codex/skills/hott-machine-overview-execution/SKILL.md','.codex/skills/hott-machine-overview-audit/SKILL.md','README/001 - 当前入口与关键文件.md','feature-list.md','rulings.md','第三轮机器统观/README.md'])]
    for skill in ('hott-local-session-governance','hott-machine-overview-execution','hott-machine-overview-audit'):
        cases.append(('skill-'+skill,[sys.executable,'-B','/Users/aurolafly/.codex/skills/.system/skill-creator/scripts/quick_validate.py',str(ROOT/'.codex/skills'/skill)]))
    for label,argv in cases:
        r=subprocess.run(argv,cwd=ROOT,capture_output=True,timeout=120)
        (out/(label+'-stdout.txt')).write_bytes(r.stdout);(out/(label+'-stderr.txt')).write_bytes(r.stderr)
        checks[label]=r.returncode==0;commands.append({'label':label,'argv':argv,'exit':r.returncode})
    spec=importlib.util.spec_from_file_location('R',ROOT/'.codex/tools/cognition_runtime.py');R=importlib.util.module_from_spec(spec);spec.loader.exec_module(R)
    state=json.loads(state_path.read_text());config=json.loads((ROOT/R.CONFIG).read_text())
    checks['new_tasks_not_registered_or_started']=all(x not in state['records'] for x in ('MO3-COVERAGE-C','MO3-COVERAGE-D'))
    plans={}
    for profile in ('governance','research'):
        p=R.plan(ROOT,profile=profile);dump(out/(profile+'-plan.json'),p)
        paths=[d['path'] for d in p['documents']]
        checks[profile+'_mandatory_inputs']=all(x in paths for x in ('最高指示.md','.codex/cognition/TASK_ROUTING.md')) and [x for x in paths if x in R.FULL_SET]==list(R.FULL_SET)
        plans[profile]={'snapshot':p['snapshot'],'documents':len(paths),'promotion':p['hydration_diagnostics']['query_first_promoted']}
    def get(rel):return R.read_bytes(ROOT,rel)
    def kind(rel):
        p=ROOT/rel;return 'file' if p.is_file() else 'directory' if p.is_dir() else 'missing'
    def ls(rel):return sorted(p.name for p in (ROOT/rel).iterdir() if p.is_file()) if (ROOT/rel).is_dir() else []
    base=R.graph(config,state,get,'research',(),None,kind,ls)
    fixtures={}
    for role,goal,skill in [('C','goal-7.md','execution'),('D','goal-7-audit.md','audit')]:
        sid='MO3-COVERAGE-'+role;s=copy.deepcopy(state)
        sources=[goal,'.codex/skills/hott-machine-overview-'+skill+'/SKILL.md']
        if role=='D':sources.append('goal-7.md')
        s['records'][sid]={'kind':'research_task','path':goal,'status':'FIXTURE_ONLY','lifecycle_status':'ACTIVE_WORK','evidence_status':'FIXTURE_NOT_REAL_EXECUTION','depends_on':[],'related_records':['MO3-GOVERNED-A'],'full_sources':sources,'source_hashes':{goal:sha(ROOT/goal)}}
        g=R.graph(config,s,get,'research',(sid,),None,kind,ls)
        checks[role+'_graph_selects_goal_and_skill']=all(x in g[0] for x in sources)
        checks[role+'_related_A_not_recursively_promoted']=set(g[2])-set(base[2])=={sid}
        s['records'][sid]['source_hashes'][goal]='0'*64
        stale=R.graph(config,s,get,'research',(sid,),None,kind,ls)
        checks[role+'_stale_goal_requires_review']=sid in stale[3]
        fixtures[role]={'identity':'IN_MEMORY_GRAPH_FIXTURE_ONLY','full_sources':sources,'new_selected_records':sorted(set(g[2])-set(base[2])),'stale_expected':sid in stale[3]}
    counts={}
    for role,name in [('C','Session-C-Goal7启动词.txt'),('D','Session-D-Goal7审计启动词.txt')]:
        body=(HERE/name).read_text();counts[role]=len(body)
    checks['new_prompt_limits']=all(n<=4000 for n in counts.values())
    checks['goal_closures_monolithic']=all('governance-shard-index:' not in (ROOT/p).read_text() and not (ROOT/Path(p).stem).is_dir() for p in ('goal-7.md','goal-7-audit.md'))
    baseline=json.loads((HERE/'范围入口基线.json').read_text())
    checks['source_baseline_hashes_match']=all(sha(ROOT/p)==h for p,h in baseline['source_sha256'].items())
    checks['source_baseline_does_not_claim_review']=all(x['status']=='NOT_REVIEWED_BY_PREPARER' for x in baseline['schema_entries']+baseline['book_sections'])
    checks['all_named_schema_ids_unique']=len({x['id'] for x in baseline['schema_entries']})==len(baseline['schema_entries'])
    files=['goal-7.md','goal-7-audit.md','第三轮机器统观/README.md','.codex/cognition/TASK_ROUTING.md','.codex/skills/hott-machine-overview-execution/SKILL.md','.codex/skills/hott-machine-overview-audit/SKILL.md','第三轮机器统观/续做整备/接续方案.md','第三轮机器统观/续做整备/整备验收.md']
    broken=[]
    for rel in files:
        p=ROOT/rel
        for m in re.finditer(r'\[[^\]]+\]\((?:<([^>]+)>|([^\)]+))\)',p.read_text()):
            t=m.group(1) or m.group(2)
            if '://' in t or t.startswith('#'):continue
            t=re.sub(r':\d+$','',t.split('#')[0])
            if not (p.parent/t).resolve().exists():broken.append({'path':rel,'target':t})
    checks['local_links_exist']=not broken
    checks['STATE_bytes_unchanged']=sha(state_path)==state_before
    result={'schema':'goal7-preparation-evidence/v1','status':'PASS_WITH_SCOPE' if all(checks.values()) else 'FAIL','checks':checks,'commands':commands,'prompt_characters':counts,'loader_profiles':plans,'graph_fixtures':fixtures,'source_entry_counts':{'schema':baseline['schema_entry_counts'],'book_sections':baseline['numbered_book_section_count']},'broken_links':broken,'identities':{p:sha(ROOT/p) for p in files},'state_before_sha256':state_before,'state_after_sha256':sha(state_path),'limits':['No C/D session or host Goal started','No actual research or audit results created','Graph fixtures do not prove role understanding or live registration','FRESH_AND_COMPACTION_BEHAVIOR_NOT_VERIFIED','Local preparation not Git version-closed']}
    dump(out/'RESULT.json',result)
    print(json.dumps({k:result[k] for k in ('status','checks','prompt_characters','broken_links')},ensure_ascii=False,indent=2))
    return 0 if all(checks.values()) else 1


if __name__=='__main__':raise SystemExit(main())
