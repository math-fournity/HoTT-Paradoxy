"""Read-only current-state route probe; not a model-understanding test."""
from pathlib import Path
import importlib.util,json,sys
R=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('r023_plan_probe',R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
p=rt.plan(R)
d='.codex/research/hott/dialogues/GEMINI-001/'
required={d+'rounds/004/IN-003.md',d+'rounds/004/ASSESSMENT.md',d+'TO_GEMINI_003.md','MEMORY.md',
 '.codex/research/hott/sessions/S-DISC-20260911-023-GEMINI-IN003/SESSION.md'}
assert p['revision']==23
assert required<={x['path'] for x in p['documents']}
print(json.dumps({'revision':23,'snapshot':p['snapshot'],'required_paths_present':True,
 'documents':len(p['documents']),'model_context':'NOT_CERTIFIED_BY_TOOL'},ensure_ascii=False))
