#!/usr/bin/env python3
"""Freeze six already-exported user originals without rereading native trajectories."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
BASE=ROOT/'Astra继续尝试/断点与证明机制系统检查';DEST=OUT/'source-inputs'
assert not DEST.exists();DEST.mkdir()
def sha(b):return hashlib.sha256(b).hexdigest()
def put(name,raw):
 p=DEST/name;assert not p.exists();p.write_bytes(raw);return {'path':str(p.relative_to(ROOT)),'bytes':len(raw),'sha256':sha(raw)}
selected={1,5,8,11,14,27};rows=[];manifests=[]
for name in ['对话归档清单.json','对话归档增量-002.json']:
 p=BASE/'evidence'/name;raw=p.read_bytes();j=json.loads(raw);manifests.append({'source':str(p.relative_to(ROOT)),**put(name,raw)})
 for m in j['messages']:
  if m['ordinal'] not in selected:continue
  assert m['role']=='user';p=BASE/m['text_file'];raw=p.read_bytes();assert len(raw)==m['utf8_bytes'] and sha(raw)==m['sha256']
  lo,hi=m['shard_byte_range'];assert (BASE/m['shard']).read_bytes()[lo:hi]==raw
  rows.append({'original_export_entry':m,'original_text_path':str(p.relative_to(ROOT)),**put(p.name,raw)})
assert {m['original_export_entry']['ordinal'] for m in rows}==selected
docs=[]
for prefix in ['022','023']:
 ps=list((ROOT/'Atria的方案/修订片').glob(prefix+' - *.md'));assert len(ps)==1;p=ps[0]
 docs.append({'role':'HISTORICAL_AI_AUTHORED_PLAN_NOT_PROVED_MATHEMATICS','source':str(p.relative_to(ROOT)),**put(p.name,p.read_bytes())})
receipt={'status':'SIX_EXACT_ARCHIVED_USER_MESSAGES_AND_TWO_PLAN_SOURCES_FROZEN','method':'Consume existing canonical-reader export entries and raw text; match hash/bytes and shard range. No new native-session traversal or hidden reasoning extraction.','scope':'Only the six selected mathematical user statements, not complete session coverage. Current research prose is interpretation, not user ruling.','messages':rows,'export_manifests':manifests,'historical_plan_sources':docs}
(OUT/'SOURCE-INPUTS.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'messages':len(rows),'plans':len(docs)}))
