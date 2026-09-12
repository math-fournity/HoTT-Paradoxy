#!/usr/bin/env python3
"""Read current route in a fresh process; no full-context certification or writes."""
from pathlib import Path
import importlib.util, json, sys
R=Path(__file__).resolve().parents[2]
S='S-DISC-20260911-022-GEMINI-OUT002'
D='.codex/research/hott/dialogues/GEMINI-001/'
spec=importlib.util.spec_from_file_location('r022_fresh_runtime',R/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
p=rt.plan(R)
paths={r['path'] for r in p['documents']}
assert p['revision']==22 and p['latest_session']==S
assert D+'TO_GEMINI_002.md' in paths and 'MEMORY.md' in paths
ledger=json.loads((R/(D+'DEBATE_LEDGER.json')).read_text())
o=next(x for x in ledger['outgoing'] if x['id']=='OUT-002')
assert not o['sent'] and not o['reply_received']
assert len(ledger['incoming'])==2
print(json.dumps({'status':'PASS_ROUTE_ONLY','root':str(R),'snapshot':p['snapshot'],
  'revision':p['revision'],'latest_session':p['latest_session'],'documents':len(paths),
  'letter_in_route':True,'incoming_count':2,'outgoing_sent':False,'new_peer_reply':False,
  'full_model_reading_or_understanding':'NOT_CERTIFIED'},ensure_ascii=False,indent=2))
