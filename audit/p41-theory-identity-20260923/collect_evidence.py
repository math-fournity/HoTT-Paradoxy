#!/usr/bin/env python3
"""Identity/equivalence audit source hashes and exact old dependency occurrences."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
book=Path('HoTT/theory-schema/upstream/book-578b85cc')
ranges={'logic.tex':[[1,1278]],'formal.tex':[[235,250],[640,764],[905,968]],
 'basics.tex':[[969,1150],[1465,1501],[1568,1668],[1706,1808],[2165,2252]],
 'equivalences.tex':[[1,38],[148,220],[350,375],[470,520]],'categories.tex':[[1205,1365]]}
paths=[book/f for f in ranges]+[Path('HoTT/theory-schema/CORE_RULES.md'),Path('HoTT/formal/sip-representation/SIPRepresentation.agda'),Path('HoTT/formal/two-level-fibrant-replacement-uip/TwoLevelReplacementUIP.agda')]
old=[]
for p in sorted((ROOT/'.codex/research/hott/PREMISE-001').glob('00[1-7]*.md')):
 paths.append(p.relative_to(ROOT))
 for n,line in enumerate(p.read_text().splitlines(),1):
  if re.search(r'(?:PREMISE-)?C-01|(?:PREMISE-)?G-02',line):old.append(dict(path=str(p.relative_to(ROOT)),line=n,text=line))
out=dict(schema_version='bounded-theory-source-audit/v1',baseline='df5fbcd7',book_commit='578b85cc8d586b1677ec4335148adeb443057d24',
 source_hashes={str(p):hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},read_ranges=ranges,
 old_dependency_occurrences=old,external_source=dict(url='https://agda.readthedocs.io/en/v2.8.0/language/cubical.html#transport',scope='Path J computation and transport',status='SOURCE_REPORTED_NOT_REPLAYED'),
 existing_control_status='SOURCE_INSPECTED_NOT_REPLAYED_THIS_WAVE',new_math_claims=[],new_kernel_runs=[],
 verdict='C01_GLOBAL_SCOPE_NOT_SUPPORTED_BY_BOOK_G02_SET_CONDITION_REQUIRED_ETA_J_VARIANTS_SEPARATED')
(HERE/'EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'SOURCE_IDENTITIES_RECORDED','files':len(paths),'dependency_occurrences':len(old),'new_kernel_runs':0}))
