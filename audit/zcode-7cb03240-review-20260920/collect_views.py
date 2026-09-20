#!/usr/bin/env python3
"""Read-only SQL projections plus the existing canonical model-io reader.

The SQL queries preserve native message/part IDs and sequence. They do not
pretend to reconstruct outgoing requests or replace the canonical raw reader.
No reasoning, system prompts, synthetic control messages, credentials, or DB
writes are selected. Tool payloads stay in private-audit.
"""
from pathlib import Path
import collections
import dataclasses
import hashlib
import importlib.util
import json
import os
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[2]
SID = 'sess_7cb03240-9567-4a2e-9061-b6f0273cd09b'
DB = Path('/Users/aurolafly/.zcode/cli/db/db.sqlite')
RAW = Path('/Users/aurolafly/.zcode/cli/rollout') / ('model-io-' + SID + '.jsonl')
READER = Path('/Users/aurolafly/codex/tools/session_trajectory.py')
OUT = ROOT / 'private-audit/zcode-7cb03240-20260920'

def write(name, text):
    p = OUT / name
    with p.open('x', encoding='utf-8') as f:
        f.write(text)
    p.chmod(0o600)

def sha(b):
    return hashlib.sha256(b).hexdigest()

def main():
    OUT.mkdir(parents=True, exist_ok=True, mode=0o700)
    OUT.chmod(0o700)
    c = sqlite3.connect('file:' + str(DB) + '?mode=ro', uri=True)
    c.row_factory = sqlite3.Row
    c.execute('pragma query_only=ON')
    c.execute('BEGIN')
    meta = dict(c.execute('select id,parent_id,title,directory,time_created,time_updated from session where id=?', (SID,)).fetchone())
    sql = """select m.id message_id,m.sequence message_sequence,m.time_created,
      json_extract(m.data,'$.role') role,json_extract(m.data,'$.finish') finish,
      p.id part_id,p.sequence part_sequence,json_extract(p.data,'$.text') text
      from message m join part p on p.message_id=m.id
      where m.session_id=? and p.session_id=? and json_extract(p.data,'$.type')='text'
      and json_extract(m.data,'$.synthetic') is not 1
      and json_extract(p.data,'$.synthetic') is not 1
      and json_extract(m.data,'$.role') in ('user','assistant')
      order by m.sequence,m.time_created,m.id,p.sequence,p.time_created,p.id"""
    rows = [dict(r) for r in c.execute(sql, (SID,SID))]
    assert all(not r['text'].lstrip().startswith('<system-reminder>') for r in rows)
    tools_sql = """select m.id message_id,m.sequence message_sequence,p.id part_id,
      p.sequence part_sequence,json_extract(p.data,'$.callID') call_id,
      json_extract(p.data,'$.tool') tool,json_extract(p.data,'$.state.status') status,
      json_extract(p.data,'$.state.input') input,json_extract(p.data,'$.state.output') output,
      json_extract(p.data,'$.state.error') error
      from message m join part p on p.message_id=m.id
      where m.session_id=? and p.session_id=? and json_extract(p.data,'$.type')='tool'
      order by m.sequence,m.time_created,m.id,p.sequence,p.time_created,p.id"""
    tool_rows = [dict(r) for r in c.execute(tools_sql, (SID,SID))]
    counts = dict(message_count=c.execute('select count(*) from message where session_id=?',(SID,)).fetchone()[0],
                  part_count=c.execute('select count(*) from part where session_id=?',(SID,)).fetchone()[0])
    c.rollback()
    c.close()
    write('visible-native.json', json.dumps(rows,ensure_ascii=False,indent=1)+'\n')
    write('tool-native.json', json.dumps(tool_rows,ensure_ascii=False,indent=1)+'\n')
    text = ''
    for r in rows:
        text += f"\n## message:{r['message_sequence']} {r['role']} finish={r['finish']} | {r['message_id']} / {r['part_id']}\n\n{r['text']}\n"
    write('visible-native.txt', text)
    spec = importlib.util.spec_from_file_location('canonical_trajectory', READER)
    reader = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = reader
    spec.loader.exec_module(reader)
    raw_before = sha(RAW.read_bytes())
    events = list(reader.iter_zcode_events(RAW))
    selected = [e for e in events if e.kind in ('user_message','assistant_message','tool_call','tool_result','error','usage','model_request')]
    write('canonical-events.json',json.dumps([e.full() for e in selected],ensure_ascii=False,indent=1)+'\n')
    assert sha(RAW.read_bytes()) == raw_before
    native_text = {r['text'] for r in rows}
    comparison = [dict(locator=e.locator,kind=e.kind,exact_in_native=e.text in native_text)
                  for e in events if e.kind=='user_message' or (e.kind=='assistant_message' and e.data.get('finish_reason')=='stop')]
    assert all(x['exact_in_native'] for x in comparison)
    manifest = dict(session=meta, database=str(DB),database_snapshot='SQLite read transaction',
      sql_visible=sql,sql_tools=tools_sql,counts=counts,visible_rows=len(rows),
      visible_counts=dict(collections.Counter((r['role']+':'+str(r['finish'])) for r in rows)),
      tools=len(tool_rows),tool_status_counts=dict(collections.Counter(r['status'] for r in tool_rows)),
      raw=str(RAW),raw_bytes=RAW.stat().st_size,raw_sha256=raw_before,raw_mode=oct(RAW.stat().st_mode&0o777),
      reader=str(READER),reader_sha256=sha(READER.read_bytes()),canonical_event_counts=dict(collections.Counter(e.kind for e in events)),
      tail_native_crosscheck=comparison,private_files={p.name:sha(p.read_bytes()) for p in OUT.iterdir() if p.is_file()},
      boundary='Native stored transcript + tail model requests; no claim of full pre-tail outgoing-request coverage. Reasoning and internal prompts excluded.')
    write('MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:manifest[k] for k in ('session','counts','visible_rows','visible_counts','tools','tool_status_counts','tail_native_crosscheck')},ensure_ascii=False))

if __name__ == '__main__':
    main()
