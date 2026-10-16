#!/usr/bin/env python3
"""Pin the actually consumed principle definitions and named library sections."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
CFG=json.loads((ROOT/'HoTT/formal/agda-unimath/no-erasure/TOOLCHAIN.json').read_text());lib=Path(CFG['agda_unimath_library']['local_root'])
entries=[('HoTT/theory-schema/upstream/book-578b85cc/reals.tex','lines3190–3230 / ex:reals-apart-neq-MP'),('HoTT/formal/agda-unimath/hott-z/MarkovBookForms.agda','full principle translation module'),('HoTT/formal/agda-unimath/hott-z/RealPrincipleBookScope.agda','full zero/pair real principle module'),('HoTT/formal/agda-unimath/hott-z/WeakLiftPrinciple.agda','full zero-real/circle principle bridge'),('HoTT/formal/agda-unimath/hott-z/NativeMotionComplete.agda','existing same-map Weak coverage definitions and iff bridge')]
external=['logic/markovs-principle.lagda.md','logic/markovian-types.lagda.md','elementary-number-theory/unit-fractions-rational-numbers.lagda.md','elementary-number-theory/multiplicative-group-of-positive-rational-numbers.lagda.md','real-numbers/lower-dedekind-real-numbers.lagda.md','real-numbers/real-numbers-from-lower-dedekind-real-numbers.lagda.md']
def row(p,where,reading):
    raw=p.read_bytes();return {'path':where,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'reading_scope':reading}
rows=[row(ROOT/p,p,scope) for p,scope in entries]
rows += [row(lib/'src'/p,str(lib/'src'/p),'full named module; import tree separately frozen by formal run') for p in external]
receipt={'status':'SOURCE_IDENTITY_PINNED_NOT_A_MATH_CERTIFICATE','head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'book_commit':'578b85cc8d586b1677ec4335148adeb443057d24','library_tree':CFG['agda_unimath_library']['tree_sha256'],'rows':rows,'search_scope':'Exact Markov/binary search in real-numbers,real-analysis,metric-spaces after zvec Transport closed; no global absence claim.','not_claimed':'Other exploratory supremum/Cauchy reads were partial and not used as proof dependencies or full-document coverage.'}
p=OUT/'SOURCES.json';assert not p.exists();p.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'sources':len(rows),'status':receipt['status']}))
