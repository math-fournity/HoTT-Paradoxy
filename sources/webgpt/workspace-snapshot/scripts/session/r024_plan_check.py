"""Fresh-process read-only verification of current dynamic cognition routing."""
from pathlib import Path
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parents[2]

def main() -> None:
    path = ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py'
    spec = importlib.util.spec_from_file_location('r024_fresh_runtime', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    plan = module.plan(ROOT)
    prefix = '.codex/research/hott/'
    dialogue = prefix+'dialogues/GEMINI-001/'
    required = {
        'MEMORY.md', dialogue+'TO_GEMINI_004.md',
        dialogue+'rounds/005/IN-004.md', dialogue+'rounds/005/ASSESSMENT.md',
        dialogue+'rounds/005/TECHNICAL_NOTE.md',
        prefix+'sessions/S-DISC-20260911-024-GEMINI-IN004/SESSION.md',
        'scripts/research/r024_diagonal_machine.py',
        'scripts/tests/test_r024_diagonal_machine.py',
        'artifacts/r024/COMPILER_SUMMARY.json',
    }
    actual = {item['path'] for item in plan['documents']}
    missing = sorted(required-actual)
    result = {'revision': plan['revision'], 'snapshot': plan['snapshot'],
              'document_count': len(actual), 'required_paths_present': not missing,
              'missing': missing, 'full_text_cognition_certified': False,
              'scope': 'ROUTING_AND_FILE_IDENTITY_ONLY_NOT_SEMANTIC_LOADING'}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if missing or plan['revision'] != 24:
        raise SystemExit(1)

if __name__ == '__main__':
    main()
