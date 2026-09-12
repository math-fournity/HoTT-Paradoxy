"""Record available local tools and current governance state; no installations."""
from __future__ import annotations
from pathlib import Path
import importlib.util
import json
import shutil
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[2]
def main():
    state = json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    tools = {name:shutil.which(name) for name in ['lean','lake','agda','coqc','rocq','z3']}
    packages = {name:bool(importlib.util.find_spec(name)) for name in ['z3','sympy','pytest']}
    outputs = {}
    for args in [['rev-parse','HEAD'],['status','--porcelain'],['remote','-v']]:
        p = subprocess.run(['git','-c','core.hooksPath=/dev/null',*args], cwd=ROOT, capture_output=True,text=True,check=True)
        outputs[' '.join(args)] = p.stdout
    spec = importlib.util.spec_from_file_location('cognition_r025', ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    mod = importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
    plan = mod.plan(ROOT)
    out=ROOT/'artifacts/r025'
    (out/'BASE_PLAN.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n')
    report={'tools':tools, 'packages':packages, 'python':sys.version, 'git':outputs,
        'revision':plan['revision'], 'snapshot':plan['snapshot'], 'document_count':len(plan['documents']),
        'total_bytes':plan['total_bytes'], 'full_business_cognition':'NOT_CERTIFIED; bounded incoming correspondence audit',
        'state_record_ids':list(state['records'])}
    (out/'ENVIRONMENT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
