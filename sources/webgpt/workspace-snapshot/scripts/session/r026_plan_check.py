"""Read-only verification of revision26 routing; not model cognition certification."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('r026_plan_runtime',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
if spec is None or spec.loader is None:
    raise RuntimeError('Runtime loader unavailable')
rt=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=rt
spec.loader.exec_module(rt)
p=rt.plan(ROOT)
base='.codex/research/hott/reviews/EARLY-GEMINI-001/'
required={base+x for x in ['ORIGINAL.md','ASSESSMENT.md','PROOF_NOTE.md','PLAN.md','SOURCES.md']}
required.update({'scripts/research/r026_early_ideas_checks.py','artifacts/r026/CHECK_V1_RESULTS.json',
                '.codex/research/hott/sessions/S-AUD-20260911-026-EARLY-GEMINI/SESSION.md'})
actual={e['path'] for e in p['documents']}
if p['revision']!=26 or not required<=actual:
    raise RuntimeError('Unexpected state or missing source routing')
print(json.dumps({'revision':p['revision'],'latest_session':p['latest_session'],'snapshot':p['snapshot'],
    'required_paths_present':True,'documents':len(actual),'bytes':p['total_bytes'],
    'full_model_cognition':'NOT_CERTIFIED_BY_TOOL','native_kernel':'NOT_RUN'},ensure_ascii=False,indent=2))
