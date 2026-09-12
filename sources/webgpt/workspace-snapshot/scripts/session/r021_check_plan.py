"""Read-only current governance plan in a fresh process and relocated directory."""
from pathlib import Path
import importlib.util, json, sys
R=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('r021_freshplan_runtime',R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
p=rt.plan(R);paths={x['path'] for x in p['documents']}
base='.codex/research/hott/'
needed={base+'dialogues/GEMINI-001/rounds/002/'+n for n in ['IN-002.md','ASSESSMENT.md','SYNTHESIS.md']}
needed|={base+'candidates/RP-B01/'+n for n in ['PLAN.md','CONSTRUCTION.md','CLAIMS.json']}
print(json.dumps({'revision':p['revision'],'latest_session':p['latest_session'],
 'document_count':len(p['documents']),'required_new_sources_present':needed<=paths,
 'snapshot':p['snapshot'],'model_context':'NOT_CERTIFIED_BY_FILE_PLAN'},ensure_ascii=False,indent=2))
