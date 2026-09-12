"""Read-only current-route check; not a certificate of model comprehension."""
from pathlib import Path
import importlib.util
import json
import sys
ROOT=Path(__file__).resolve().parents[2]
def main():
    spec=importlib.util.spec_from_file_location('r025_plan_runtime', ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    plan=rt.plan(ROOT)
    d='.codex/research/hott/dialogues/GEMINI-001/'
    required={d+'TO_GEMINI_005.md',d+'rounds/006/IN-005.md',d+'rounds/006/ASSESSMENT.md',d+'rounds/006/TECHNICAL_NOTE.md',
        'MEMORY.md','scripts/research/r025_diagonal_audit.py','artifacts/r025/TARGETED_SUMMARY.json',
        '.codex/research/hott/sessions/S-DISC-20260911-025-GEMINI-IN005/SESSION.md'}
    missing=sorted(required-{item['path'] for item in plan['documents']})
    result={'revision':plan['revision'],'snapshot':plan['snapshot'],'document_count':len(plan['documents']),
        'required_paths_present':not missing,'missing':missing,'full_text_cognition_certified':False}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    if missing or plan['revision']!=25:raise SystemExit(1)
if __name__=='__main__':main()
