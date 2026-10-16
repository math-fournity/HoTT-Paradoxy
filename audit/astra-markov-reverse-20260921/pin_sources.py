#!/usr/bin/env python3
"""Pin local principle/representation inputs and record primary external locators."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
cfg=json.loads((ROOT/'HoTT/formal/agda-unimath/no-erasure/TOOLCHAIN.json').read_text());lib=Path(cfg['agda_unimath_library']['local_root'])
local=['HoTT/formal/agda-unimath/hott-z/BinaryWitnessWeights.agda','HoTT/formal/agda-unimath/hott-z/BinaryWitnessReal.agda','HoTT/formal/agda-unimath/hott-z/WeakCoverageMarkov.agda','HoTT/formal/agda-unimath/hott-z/NativeMotionComplete.agda']
external=['real-numbers/arithmetically-located-dedekind-cuts.lagda.md','real-numbers/rational-approximates-of-real-numbers.lagda.md','foundation/axiom-of-countable-choice.lagda.md']
def row(p,scope):
    b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'reading_scope':scope}
rows=[row(ROOT/p,'Existing actual theorem/interface; full source available and pinned') for p in local]+[row(lib/'src'/p,'Full named module read this turn') for p in external]
receipt={'status':'LOCAL_SOURCES_PINNED_EXTERNAL_PRIMARY_SCOPE_RECORDED','head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'library_tree':cfg['agda_unimath_library']['tree_sha256'],'rows':rows,
 'web_sources':[{'url':'https://arxiv.org/html/1805.06781v5','identity':'Booij, arXiv1805.06781v5 (2020-06-21)','read_scope':'abstract and rendered paragraphs through section3.1; not whole paper','role':'Source-reported property/structure distinction, no machine translation or independence certificate'},
 {'url':'https://www.paultaylor.eu/ASD/dedras/index.html','identity':'Bauer and Taylor,2009,doi10.1017/S0960129509007695','read_scope':'author index/abstract only','role':'reference identity, not a HoTT theorem'},
 {'url':'https://www.math.ucla.edu/~joan/kreiselmarkovcorr.pdf','identity':'Moschovakis,2018 corrected draft','read_scope':'visible introduction/section2 excerpt only','role':'distinguish principle/rule/formal-system scope, no HoTT independence claim'}],
 'retrieved_date_utc':'2026-09-21','web_byte_hash':'NOT_CAPTURED; versioned URLs and explicit read ranges only, no local raw-body or full-text reading claim','mathematics':'NOT_CERTIFIED_BY_SOURCE_MANIFEST'}
p=OUT/'SOURCES.json';assert not p.exists();p.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'local_sources':len(rows),'web_primary_locators':3,'status':receipt['status']}))
