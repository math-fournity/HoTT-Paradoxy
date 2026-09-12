"""Read-only fresh-process continuity check. Resolves the root from this script."""
from pathlib import Path
import importlib.util, json, sys
ROOT=Path(__file__).resolve().parents[2]
def main():
    s=importlib.util.spec_from_file_location('r027_plan_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(s);sys.modules[s.name]=rt;s.loader.exec_module(rt)
    plan=rt.plan(ROOT)
    paths={x['path'] for x in plan['documents']}
    required={
      '.codex/research/hott/reviews/EARLY-GEMINI-001/ASSESSMENT.md',
      '.codex/research/hott/reviews/EARLY-GEMINI-001/PLAN.md',
      'artifacts/r026/CHECK_V1_RESULTS.json',
      '.codex/research/hott/dialogues/GEMINI-001/TO_GEMINI_005.md',
      '.codex/research/hott/dialogues/GEMINI-001/TO_GEMINI_006.md',
      '.codex/research/hott/dialogues/GEMINI-001/rounds/007/IN-006.md',
      'artifacts/r027/FINITE_MODEL_RESULTS.json','artifacts/r027/NATIVE_RUN.json'}
    if plan['revision']!=27 or not required <= paths: raise RuntimeError('Continuity check failed')
    print(json.dumps({'status':'PASS_READ_ONLY','revision':plan['revision'],
      'latest_session':plan['latest_session'],'snapshot':plan['snapshot'],
      'documents':len(paths),'required_preserved':sorted(required),
      'full_model_understanding':'NOT_CERTIFIED','root':str(ROOT)},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
