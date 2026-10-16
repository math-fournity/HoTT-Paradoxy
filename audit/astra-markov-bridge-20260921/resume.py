#!/usr/bin/env python3
"""Same-tier reattestation before the precise Weak-domain principle direction."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text());assert state['revision']==206
head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(sha(ROOT/p)==h for p,h in head['tracked'].items())
prior=json.loads((ROOT/'audit/astra-review-20260921/RESUME.json').read_text());assert sha(ROOT/'核心认知.md')==prior['core_sha256']
docs=[dict(path=d['path'],prior_sha256=d['sha256'],sha256=sha(ROOT/d['path'])) for d in prior['documents']]
p=subprocess.run(['python3','-B','.codex/tools/cognition_runtime.py','plan','--profile','research','--task','A-ASTRA-CONTINUING-GOAL-20260919'],cwd=ROOT,capture_output=True)
(OUT/'TASK-PLAN.json').write_bytes(p.stdout);(OUT/'TASK-PLAN.stderr.txt').write_bytes(p.stderr);assert p.returncode==0
plan=json.loads(p.stdout);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted']
receipt=dict(policy='Same-T3 PROTOCOL v3 reattestation, not a new full emission',revision=206,core_sha256=prior['core_sha256'],documents=docs,tracked_hashes_match=len(head['tracked']),task='AST-U05-WEAK-DOMAIN-PRINCIPLE-01',previous_goal_turn='PROGRESS: five positive/four controlled rejection relocated replays, local source review archive, strategy1.34 and canonical206 committed in3a88f22',model_understanding='NOT_CERTIFIED_BY_TOOL',hydration_diagnostics=plan['hydration_diagnostics'],search={'zvec':'Transport closed','fallback':'exact rg in pinned real/analysis/metric modules and exact source reads'},scope='Construct a real from an arbitrary binary sequence, then prove the precise RNZA-to-BookMarkov direction and compose the existing Weak coverage bridge. No premise of global Markov, LEM, choice or independence is inserted.')
(OUT/'RESUME.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'revision':206,'tracked_match':len(head['tracked']),'query_first_promoted':plan['hydration_diagnostics']['query_first_promoted']}))
