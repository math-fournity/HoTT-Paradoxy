#!/usr/bin/env python3
"""Record same-tier receipt reattestation and the canonical research task plan."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text())
assert state['revision']==204
assert all(sha(ROOT/p)==h for p,h in head['tracked'].items())
prior=json.loads((ROOT/'audit/astra-native-spatial-bound-20260920/RESUME.json').read_text())
assert sha(ROOT/'核心认知.md')==prior['core_sha256']
docs=[dict(path=d['path'],prior_sha256=d['sha256'],sha256=sha(ROOT/d['path'])) for d in prior['documents']]
p=subprocess.run(['python3','-B','.codex/tools/cognition_runtime.py','plan','--profile','research','--task','A-ASTRA-CONTINUING-GOAL-20260919'],cwd=ROOT,capture_output=True)
(OUT/'TASK-PLAN.json').write_bytes(p.stdout);(OUT/'TASK-PLAN.stderr.txt').write_bytes(p.stderr)
assert p.returncode==0
plan=json.loads(p.stdout)
receipt=dict(policy='Same-T3 PROTOCOL v3 reattestation; no claim of full emission this turn',revision=204,
 core_sha256=prior['core_sha256'],core_unchanged=True,documents=docs,
 known_changes='Own checkpoint204; all current checkpoint-managed hashes match. Existing unrelated dirty retained.',
 kc_stance_revisited='All46 prior audit rows re-read individually; same pair versus same operation/Done, original claims versus exact primary-source commitments, and frozen historical rows versus current interpretation carried into this task; current per-KC review is in the session bundle.',
 task='AST-U07-CASE-INTEGRATION-02',previous_goal_turn='PROGRESS: C318/C319 scoped native geometry bundle and Weak criterion, strategy1.32, checkpoint204',
 model_understanding='NOT_CERTIFIED_BY_TOOL',hydration_diagnostics=plan.get('hydration_diagnostics'))
(OUT/'RESUME.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'revision':204,'tracked':len(head['tracked']),'core_unchanged':True,'changed':[d['path'] for d in docs if d['sha256']!=d['prior_sha256']],'plan_diagnostics':plan.get('hydration_diagnostics')},ensure_ascii=False))
