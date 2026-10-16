"""Inspect only the state records needed for the current bounded review."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]
s=json.loads((R/'.codex/research/hott/STATE.json').read_text())
l=json.loads((R/'.codex/research/hott/dialogues/GEMINI-001/DEBATE_LEDGER.json').read_text())
print(json.dumps({'state_keys':list(s),'revision':s['revision'],'latest_session':s['latest_session'],
 'records':{k:v for k,v in s['records'].items() if k in ('D-GEMINI-001','D-GEMINI-OUT-003') or 'RP-B01' in k},
 'ledger_keys':list(l),'last_out':l['outgoing'][-1], 'questions':l.get('next_questions')},ensure_ascii=False,indent=2))
