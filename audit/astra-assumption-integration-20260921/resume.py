#!/usr/bin/env python3
"""Reattest current source/state identities for the four-stage assumption integration."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text());assert state['revision']==208
head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(sha(ROOT/p)==h for p,h in head['tracked'].items())
prior=json.loads((ROOT/'audit/astra-markov-reverse-20260921/RESUME.json').read_text());assert sha(ROOT/'核心认知.md')==prior['core_sha256']
docs=[dict(path=d['path'],prior_sha256=d['sha256'],sha256=sha(ROOT/d['path'])) for d in prior['documents']]
p=subprocess.run(['python3','-B','.codex/tools/cognition_runtime.py','plan','--profile','research','--task','A-ASTRA-CONTINUING-GOAL-20260919'],cwd=ROOT,capture_output=True)
(OUT/'TASK-PLAN.json').write_bytes(p.stdout);(OUT/'TASK-PLAN.stderr.txt').write_bytes(p.stderr);assert p.returncode==0
plan=json.loads(p.stdout);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted']
receipt=dict(policy='Same-T3 PROTOCOL v3 reattestation, not a new full emission',revision=208,core_sha256=prior['core_sha256'],documents=docs,tracked_hashes_match=len(head['tracked']),task='AST-U07-ASSUMPTION-INTEGRATION-04',previous_goal_turn='PROGRESS: C323/C324 conditional converse, strategy1.36/canonical208/exact version saved in12199179',model_understanding='NOT_CERTIFIED_BY_TOOL',hydration_diagnostics=plan['hydration_diagnostics'],scope='Reconcile original four stages with C321–324 assumptions and a fixed primary natural consumer. Static source declarations are not relabeled kernel-replayed theorems. Pending goal clarification does not alter the objective.')
(OUT/'RESUME.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'revision':208,'tracked_match':len(head['tracked']),'query_first_promoted':plan['hydration_diagnostics']['query_first_promoted']}))
