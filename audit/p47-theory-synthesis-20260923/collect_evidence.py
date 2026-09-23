#!/usr/bin/env python3
"""Verify the bounded review's source identities and historical wave receipts, not mathematics."""
import hashlib,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
def h(b):return hashlib.sha256(b).hexdigest()
pins={40:'df5fbcd7f341a6f89291a86d7c2d653bdd36ec7e',41:'e8d5b917883ee41daec002c6aef01213ebf877bf',42:'95886878d0352492b8ed63e372208f66d97d3310',43:'bd43d8468af68d775ea62814238cc6a266bf7f68',44:'29fc16c6cc87db24436ba8a968e6a6b7b7e82b5d',45:'34ad06c695de7f4239dd3e7492a4f1d5687188f9',46:'fbe12679bf7a4e144d1b94f3a3de774d60047816'}
waves=[];errors=[]
for n,pin in pins.items():
 p=next((ROOT/'audit').glob(f'p{n}-*/EVIDENCE.json'));d=json.loads(p.read_text());hashes=d.get('source_hashes',d.get('additional_source_hashes',{})).copy()
 hashes.update({x['path']:x['sha256'] for x in d.get('source_files',[])})
 checks=[]
 for path,expected in hashes.items():
  git=subprocess.run(['git','show',pin+':'+path],cwd=ROOT,capture_output=True)
  actual=h(git.stdout) if git.returncode==0 else None
  current=h((ROOT/path).read_bytes()) if (ROOT/path).is_file() else None
  ok=actual==expected
  # Some historical source assets are deliberately untracked; their present bytes are separate evidence.
  status='PINNED_COMMIT_MATCH' if ok else 'LOCAL_SOURCE_MATCH_NOT_IN_WAVE_COMMIT' if git.returncode and current==expected else 'MISMATCH'
  if status=='MISMATCH':errors.append([n,path,expected,actual,current])
  checks.append(dict(path=path,expected_sha256=expected,status=status,current_matches=current==expected))
 cp=json.loads((p.parent/'APPLY.json').read_text());assert cp['status']=='CHECKPOINT_COMMITTED'
 canonical=json.loads((ROOT/'.codex/cognition/checkpoints'/cp['session_id']/'result.json').read_text())
 assert canonical['status']=='CHECKPOINT_COMMITTED' and canonical['revision']==cp['revision']
 waves.append(dict(wave=n,commit=pin,evidence=str(p.relative_to(ROOT)),evidence_sha256=h(p.read_bytes()),checkpoint=cp,source_checks=checks))
sources=['HoTT后续研究总体方案/006 - 理论充分检视的首轮范围与验收.md','goal-3.md','核心认知.md','.codex/research/hott/PREMISE-001/001 - 分母 V1 冻结（A-G 条目、P1 前提与出处）.md','HoTT/theory-schema/upstream/book-578b85cc/reals.tex','HoTT/theory-schema/upstream/book-578b85cc/hlevels.tex','HoTT/theory-schema/upstream/book-578b85cc/formal.tex','.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/002 - HoTT构造与程序化激发算子全景.md']
reports=sorted((ROOT/'HoTT理论充分检视').glob('*.md'))
expected={f'{c}{i:02d}' for c,k in [('A',11),('B',4),('C',4),('D',5),('E',4),('F',2),('G',5)] for i in range(1,k+1)}
got=re.findall(r'^\| ([A-G]\d\d) \|',reports[8].read_text(),re.M);assert len(got)==35 and set(got)==expected
out=dict(schema_version='bounded-theory-synthesis/v1',baseline=pins[46],waves=waves,source_hashes={p:h((ROOT/p).read_bytes()) for p in sources},report_hashes={str(p.relative_to(ROOT)):h(p.read_bytes()) for p in reports},new_read_ranges={'PREMISE001':'full P1 entries; not all P2/P3P4 historical sentences','reals.tex':[[2180,2458]],'hlevels.tex':[[27,95]],'formal.tex':[[620,644]],'reports001-010':'full'},premise_qualification_count=35,source_errors=errors,
 external_sources=[{'url':'https://cs.ru.nl/~nweide/fsets/finitesets.html','read':'author project page complete; no artifact replay','status':'SOURCE_SCOPE_ONLY'},{'url':'https://arxiv.org/abs/1801.08172v2','read':'metadata and abstract','status':'NEARBY_NOT_SAME_TASK_ABSTRACT_ONLY'},{'url':'https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/tychonoffs-theorem-in-the-framework-of-formal-topologies/EFEF3FFCBF72DA38599C51304EEED36A','read':'publisher page; proof body unavailable','status':'LOCATOR_ONLY'}],
 local_search={'roots':['HoTT/formal','audit','Astra继续尝试','.codex/research/hott/sessions'],'pattern':'finite[-_ ]?subcover|inductive[-_ ]?cover|有限子覆盖|Heine[- _]?Borel','scope':'md/agda/lean/json; excludes PAYLOAD/PLAN/STATE JSON; before P47 report creation','hit':'L3 KEYWORD-INVENTORY deterministic.sources[0].scan.captured_hits.interval[32]: NC-01-HOTT-BOOK, PDF page420; only keyword inventory'},
 new_math_claims=[],new_kernel_runs=[],scope_verdict='FIRST_PASS_COMPLETE_WITH_DECLARED_SCOPE',next_experiment_status='PROPOSED_NOT_EXECUTED',limitations='Counts/hash/receipts do not certify semantic understanding. Scope, exclusions, seven criteria and ranking are report009/010 human-authored judgments; no all-theory safety or paradox proof.')
(HERE/'EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'waves':len(waves),'premise_entries':len(got),'source_errors':errors,'reports':len(reports)},ensure_ascii=False));assert not errors
