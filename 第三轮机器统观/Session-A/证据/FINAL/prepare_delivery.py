#!/usr/bin/env python3
"""Bounded input snapshot and exact file-list generator for this MO3 delivery."""
from pathlib import Path
import argparse,ast,datetime,hashlib,importlib.util,json,subprocess
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;OWN=ROOT/'第三轮机器统观/Session-A'
def sh(b):return hashlib.sha256(b).hexdigest()
def put(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def inputs():
    out=HERE/'global-inputs';out.mkdir(exist_ok=False)
    locs=['/Users/aurolafly/.codex/AGENTS.md']+['/Users/aurolafly/.codex/skills/'+s+'/SKILL.md' for s in ['repo-cognitive-closure','repo-cognition-governance','repo-verification-risk']]+['/Users/aurolafly/codex-worktrees/git-ops-prep-3.13.0/docs/governance/'+n for n in ['Git协作集成与恢复行为规范.md','整备工程与交接认知闭包规范.md']]
    rows=[]
    for i,p in enumerate(locs):
        b=Path(p).read_bytes();dest=out/f'{i:02d}-{Path(p).parent.name}-{Path(p).name}.txt';dest.write_bytes(b);rows.append(dict(original=p,snapshot=str(dest.relative_to(ROOT)),sha256=sh(b),bytes=len(b),role='read-only input snapshot, not installed authority'))
    for i,p in enumerate(['docs/workflows/repo-cognitive-closure.md','docs/workflows/repo-cognition-governance.md','docs/workflows/repo-verification-risk.md','docs/governance/AI软件工程项目目录与认知治理规范.md']):
        b=subprocess.check_output(['git','-C','/Users/aurolafly/codex','show','governance-v3.25.0:'+p]);dest=out/f'tag-{i:02d}-{Path(p).name}.txt';dest.write_bytes(b);rows.append(dict(original='git:/Users/aurolafly/codex@governance-v3.25.0:'+p,snapshot=str(dest.relative_to(ROOT)),sha256=sh(b),bytes=len(b)))
    p=Path('/Users/aurolafly/.codex/attachments/b69f6bde-c0bb-4b98-8938-6f17023c7770/goal-objective.md');b=p.read_bytes();(HERE/'ACTIVE-GOAL-OBJECTIVE.txt').write_bytes(b);rows.append(dict(original=str(p),snapshot=str((HERE/'ACTIVE-GOAL-OBJECTIVE.txt').relative_to(ROOT)),sha256=sh(b),bytes=len(b)))
    put(out/'MANIFEST.json',dict(scope='Actually used global methods and actual active Goal body; byte snapshots do not certify reading or authority',rows=rows))
    paths=['AGENTS.md','.codex/skills/hott-local-session-governance/SKILL.md','.codex/cognition/TASK_ROUTING.md','.codex/skills/hott-machine-overview-execution/SKILL.md','goal-5.md','goal-6.md','最高指示.md','核心认知.md','扩展认知.md']+[str(p.relative_to(ROOT)) for p in sorted((ROOT/'扩展认知').glob('*.md'))]
    put(HERE/'RECOVERY.json',dict(schema='mo3-final-recovery/v1',observed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),base_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),state_revision=280,role='RESEARCH_GENERATION/T3',goal='active; Goal5 v1.2 actual objective read',actual_read_scope='See execution014 for full reads, truncation repair and receipt continuity; this file does not certify model comprehension',rows=[dict(path=p,sha256=sh((ROOT/p).read_bytes()),bytes=(ROOT/p).stat().st_size,lines=len((ROOT/p).read_text().splitlines())) for p in paths]))
def listing():
    reasons={}
    def add(p,why):
        p=Path(p)
        if p.is_absolute():
            try:p=p.relative_to(ROOT)
            except ValueError:return
        if '..' in p.parts or '.git' in p.parts or 'private-audit' in p.parts or 'dev-notes' in p.parts:return
        q=ROOT/p
        if not q.is_file() or q.is_symlink() or q.suffix in ('.pyc','.agdai') or '__pycache__' in p.parts:return
        s=p.as_posix()
        delivery='第三轮机器统观/Session-A/交付/'
        historical=(s.startswith(delivery+'final-001-verification/') or s in [delivery+'final-001/SEAL.json',delivery+'final-001/MANIFEST.json'])
        if (s.startswith(delivery) and not historical) or s.endswith('执行异常-旧暂停复活-20260924.md'):return
        reasons.setdefault(s,set()).add(why)
    def tree(p,why):
        for q in (ROOT/p).rglob('*'):add(q,why)
    tree('第三轮机器统观/Session-A','A reports, controls, failures and generated evidence')
    for p in ['HoTT/formal/mo3','HoTT/theory-schema','.codex/skills/hott-paradox-research','.codex/skills/hott-paradox-search-sop','.codex/skills/hott-local-session-governance','.codex/skills/hott-machine-overview-execution','.codex/skills/hott-machine-overview-audit']:
        tree(p,'actual method or theory/proof source closure')
    for q in (ROOT/'HoTT/verification/runs').glob('*MO3*'):tree(q,'all MO3 accepted/intermediate/failed formal runs')
    for parent in ['.codex/cognition/checkpoints','.codex/research/hott/sessions']:
        for q in (ROOT/parent).glob('*MO3-A-*'):tree(q,'canonical MO3 transaction and full session bundle')
    w=json.loads((OWN/'证据/W0/loading-progress-003.json').read_text())
    for r in w['full_read_paths_asserted_by_assistant']:add(r['path'],'actual W0 required reading chain')
    for p in ['AGENTS.md','.codex/AGENTS.md','README.md','MEMORY.md','feature-list.md','rulings.md','docs/README.md','.codex/cognition/LOAD_SET.json','.codex/cognition/PROTOCOL.md','.codex/cognition/TASK_ROUTING.md','.codex/skills/SKILL_ROLES.json','.codex/cognition/HEAD.json','.codex/research/hott/STATE.json','核心认知.md','核心认知.manifest.json','方向追踪.md','全景视野.md','扩展认知.md','最高指示.md','goal-5.md','goal-6.md','goal-5-audit.md','goal-6-audit.md','HoTT/CLAIM_EVIDENCE_MATRIX.md','HoTT/verification/PROOF_VERSION_CLOSURE.json','HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json','HoTT/formal/dedekind-omega-missile/AGDA_LIBRARIES','第三轮机器统观/整备/Session-A-工作闭包.md','第三轮机器统观/整备/Session-B-工作闭包.md','第三轮机器统观/整备/handoff_snapshot.py','第三轮机器统观/治理整备/Session-A-goal提示词.txt','第三轮机器统观/治理整备/Session-B-goal提示词.txt','HoTT/sources/user-originals/Z铁律-抽象-圆环-时间维度-用户原始论述-20260901.md','HoTT/sources/user-originals/Better-Best悖论-原文.md']:
        if not (ROOT/p).is_file():raise FileNotFoundError(p)
        add(p,'required method, exact claim/source/state or B interface')
    state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text());visited=set()
    def strings(x,why):
        if isinstance(x,str):
            if len(x)<1000:
                try:add(x,why)
                except OSError:pass
        elif isinstance(x,list):
            for v in x:strings(v,why)
        elif isinstance(x,dict):
            for k,v in x.items():strings(k,why);strings(v,why)
    def record(id):
        if id in visited:return
        visited.add(id);r=state['records'][id];strings(r,'selected record '+id)
        for d in r.get('depends_on',[]):record(d)
    record('MO3-GOVERNED-A');strings(state['current_core'],'current core identity and source curation')
    for p in ['核心认知.manifest.json',state['current_core']['curation']]:strings(json.loads((ROOT/p).read_text()),'hash-pinned user primary source')
    # Each run manifest fixes the local transitive proof input paths, including controls.
    for q in (ROOT/'HoTT/verification/runs').glob('*MO3*/source-manifest.json'):
        for r in json.loads(q.read_text()).get('files',[]):add(r['path'],'formal run local input dependency')
    # Actual validation tool closure: recursively add resolvable local Python imports.
    scripts=['.codex/tools/cognition_runtime.py']+['scripts/audit/'+n+'.py' for n in ['capture_agda_proof_run','verify_formal_proof_run','verify_proof_version_closure','freeze_proof_index_rows','mark_proof_run_indexed','verify_core_cognition','build_core_cognition','verify_three_way_cognition','verify_governance_shards','validate_governance_shards','projection_edit']]
    todo=list(scripts);seen=set()
    while todo:
        p=todo.pop()
        if p in seen:continue
        seen.add(p);add(p,'actual canonical verification/runtime tool and local imports')
        for node in ast.walk(ast.parse((ROOT/p).read_text())):
            modules=([node.module] if isinstance(node,ast.ImportFrom) and node.module else [a.name for a in node.names] if isinstance(node,ast.Import) else [])
            for m in modules:
                for parent in [Path(p).parent,Path('scripts/audit'),Path('.codex/tools')]:
                    f=parent/(m.replace('.','/')+'.py')
                    if (ROOT/f).is_file():todo.append(str(f))
    # Expand every selected logical index through its exact shard table.
    sp=importlib.util.spec_from_file_location('projection_edit',ROOT/'scripts/audit/projection_edit.py');e=importlib.util.module_from_spec(sp);sp.loader.exec_module(e)
    done=set()
    while True:
        pending=[p for p in reasons if p.endswith('.md') and p not in done]
        if not pending:break
        for p in pending:
            done.add(p);text=(ROOT/p).read_text()
            if re_index(text):
                doc=e.load(ROOT,p)
                for f in doc['shards']:add(f,'complete logical document '+p)
    # Scope report/list include themselves without self-hashing.
    listpath=OWN/'交付路径清单.txt';scope=HERE/'delivery-scope.json'
    reasons.setdefault(str(listpath.relative_to(ROOT)),set()).add('precise list itself, no self hash')
    reasons.setdefault(str(scope.relative_to(ROOT)),set()).add('dependency selection explanation, no self hash')
    put(scope,dict(schema='mo3-delivery-scope/v1',selected_records=sorted(visited),files=[dict(path=p,reasons=sorted(v)) for p,v in sorted(reasons.items())],excluded=['private trajectories/dev-notes/unrelated dirty/historical nested repos','compiled interfaces/cache','delivery generation itself','obsolete control incident owner'],scope='Named dependency closure; byte enumeration is not a semantic completeness proof'))
    listpath.write_text('\n'.join(sorted(reasons))+'\n')
    print(json.dumps(dict(paths=len(reasons),bytes=sum((ROOT/p).stat().st_size for p in reasons),list=str(listpath.relative_to(ROOT))),ensure_ascii=False))
def re_index(text):return 'governance-shard-index:v1' in text[:1000] or 'governance-shard-index:v2' in text[:1000]
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['inputs','list']);args=ap.parse_args();inputs() if args.mode=='inputs' else listing()
