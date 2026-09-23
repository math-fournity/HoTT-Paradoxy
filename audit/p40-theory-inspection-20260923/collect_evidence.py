#!/usr/bin/env python3
"""Recompute the frozen source inventory and save a bounded audit receipt."""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
BASE=ROOT/'HoTT/theory-schema'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

text=(BASE/'SOURCES_AND_COVERAGE.md').read_text()
files=re.findall(r'^\| `([^`]+)` \| (\d+) \| `([0-9a-f]{64})`',text,re.M)
rows=[]
for name,n,h in files:
    p=BASE/'upstream/book-578b85cc'/name
    rows.append(dict(path=str(p.relative_to(ROOT)),bytes=len(p.read_bytes()),expected_bytes=int(n),sha256=digest(p),expected_sha256=h))
assert len(rows)==21 and all(r['bytes']==r['expected_bytes'] and r['sha256']==r['expected_sha256'] for r in rows)
sections=re.findall(r'^\| (\d+\.\d+) \| .*?\[([^\]:]+):(\d+)\]',text,re.M)
bad=[sid for sid,name,n in sections if not (BASE/'upstream/book-578b85cc'/name).read_text().splitlines()[int(n)-1].lstrip().startswith('\\section')]
assert len(sections)==105 and not bad
ids={}
for name,prefix in [('CORE_RULES','C'),('DERIVED_STRUCTURES','D'),('SEMANTICS_AND_COHERENCE','S'),('EXTENSIONS_AND_METATHEORY','E')]:
    ids[name]=re.findall(r'^## ('+prefix+r'\d+) ·',(BASE/(name+'.md')).read_text(),re.M)
scope={'formal.tex':[[1,161],[449,800]],'preliminaries.tex':[[1,76]],'logic.tex':[[1,145]]}
decisive=['HoTT/theory-schema/CORE_RULES.md','HoTT/theory-schema/DERIVED_STRUCTURES.md','HoTT/theory-schema/SEMANTICS_AND_COHERENCE.md','HoTT/theory-schema/EXTENSIONS_AND_METATHEORY.md',
 'audit/PREMISE-001-V1信封外遗漏审计-20260916.md',
 '.codex/research/hott/PREMISE-001/001 - 分母 V1 冻结（A-G 条目、P1 前提与出处）.md']
out=dict(schema_version='bounded-theory-source-audit/v1',baseline='f495b8d8',book_commit='578b85cc8d586b1677ec4335148adeb443057d24',
 source_files=rows,source_bytes=sum(r['bytes'] for r in rows),section_count=len(sections),section_line_errors=bad,schema_ids=ids,
 decisive_read_ranges=scope,additional_source_hashes={p:digest(ROOT/p) for p in decisive},
 web_comparison=dict(url='https://bentnib.org/quantitative-type-theory.pdf',doi='10.1145/3209108.3209189',read_scope='Introduction and section2.1',status='SOURCE_REPORTED_NOT_REPLAYED'),
 rejected_web_locator='https://arxiv.org/abs/1712.08055: unrelated physical paper, not used',
 new_math_claims=[],new_kernel_runs=[],scope='Identity/locator checks do not certify semantic coverage; semantic judgments belong to report shard002.')
(HERE/'EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'PASS_WITH_SCOPE','files':len(rows),'sections':len(sections),'source_bytes':out['source_bytes'],'semantic_review_not_certified':True}))
