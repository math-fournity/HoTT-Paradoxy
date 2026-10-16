#!/usr/bin/env python3
"""Reattest the unchanged core and the applied prior checkpoint before relocation."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text());assert state['revision']==205
head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text());assert all(sha(ROOT/p)==h for p,h in head['tracked'].items())
prior=json.loads((ROOT/'audit/astra-case-integration-20260921/RESUME.json').read_text());assert sha(ROOT/'核心认知.md')==prior['core_sha256']
docs=[dict(path=d['path'],prior_sha256=d['sha256'],sha256=sha(ROOT/d['path'])) for d in prior['documents']]
p=subprocess.run(['python3','-B','.codex/tools/cognition_runtime.py','plan','--profile','research','--task','A-ASTRA-CONTINUING-GOAL-20260919'],cwd=ROOT,capture_output=True)
(OUT/'TASK-PLAN.json').write_bytes(p.stdout);(OUT/'TASK-PLAN.stderr.txt').write_bytes(p.stderr);assert p.returncode==0
plan=json.loads(p.stdout);assert not plan['review_required'] and not plan['hydration_diagnostics']['query_first_promoted']
receipt=dict(policy='Same-T3 PROTOCOL v3 reattestation, not a new full emission',revision=205,core_sha256=prior['core_sha256'],documents=docs,tracked_hashes_match=len(head['tracked']),task='AST-U08-U09-SCOPED-REVIEW-01',previous_goal_turn='PROGRESS: C320 formal source and exact version qualified, primary-source case audit, strategy1.33 and canonical205 committed in9c33e1c',model_understanding='NOT_CERTIFIED_BY_TOOL',hydration_diagnostics=plan['hydration_diagnostics'],scope='Five exact proof entries plus four frozen type-error controls; packaging/replay does not change mathematics or the original six obligations.')
(OUT/'RESUME.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'revision':205,'tracked_match':len(head['tracked']),'documents':len(docs),'query_first_promoted':plan['hydration_diagnostics']['query_first_promoted']}))
