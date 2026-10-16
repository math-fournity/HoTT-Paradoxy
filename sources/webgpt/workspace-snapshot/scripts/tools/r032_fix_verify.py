#!/usr/bin/env python3
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'scripts/tools/r032_verify.py'
old=p.read_text()
b=ROOT/'scripts/tools/r032_verify.failed_initial.py'
if b.exists():raise FileExistsError(b)
b.write_text(old)
old=old.replace("expected={'MEMORY.md'","expected={'.codex/cognition/HEAD.json','MEMORY.md'")
needle="    assert state['revision']==32 and state['latest_session']==SID\n"
replacement=needle+"    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text())\n    assert head['revision']==32 and head['latest_session']==SID\n    for rel,digest in head['tracked'].items():assert sha(ROOT/rel)==digest,rel\n"
assert needle in old
p.write_text(old.replace(needle,replacement))
(ROOT/'artifacts/r032/VERIFY_FIX.json').write_text(json.dumps({
 'failure':'First verifier expected seven old file changes, omitting HEAD.json written by the unchanged transaction manager.',
 'correction':'Include HEAD.json only after checking revision/session and every tracked file digest.',
 'source_preserved':'scripts/tools/r032_verify.failed_initial.py',
 'failure_replay':'artifacts/r032/VERIFY_INITIAL_EXECUTION.json'},ensure_ascii=False,indent=2)+'\n')
