#!/usr/bin/env python3
"""Freeze the actually read primary-source ranges for the scoped theory-claim audit."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
BASE='HoTT/theory-schema/upstream/book-578b85cc/'
SPEC={
 'basics.tex':('516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533',[(1,210),(748,805),(1706,1808),(2165,2360)]),
 'logic.tex':('76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2',[(159,255),(353,558),(598,701)]),
 'reals.tex':('f5e4803e17abdb2fbb75a6ebd30022a9587a914711f3ca77dc8fcce50fda39e7',[(1,26),(85,215),(316,365),(3204,3225)]),
 'formal.tex':('e621484e2e457e70536a92367cca452f34df8ecfc9a17a3bdf0e4ee67e5f0cec',[(1073,1207)])}
def sha(b):return hashlib.sha256(b).hexdigest()
dest=OUT/'primary-source-excerpts';dest.mkdir(exist_ok=True)
rows=[]
for name,(expected,ranges) in SPEC.items():
 raw=(ROOT/(BASE+name)).read_bytes();assert sha(raw)==expected;lines=raw.splitlines(keepends=True)
 for first,last in ranges:
  body=b''.join(lines[first-1:last]);target=dest/f'{name[:-4]}-{first:04d}-{last:04d}.tex'
  assert not target.exists();target.write_bytes(body)
  rows.append({'source':BASE+name,'source_sha256':expected,'source_bytes':len(raw),'first_line':first,'last_line':last,'excerpt':target.relative_to(ROOT).as_posix(),'excerpt_sha256':sha(body),'excerpt_bytes':len(body),'upstream':'https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/'+name+'#L'+str(first),'reading_role':'SOURCE_REPORTED_TEXT_NOT_A_NEW_KERNEL_THEOREM'})
receipt={'status':'PINNED_PRIMARY_RANGES_CAPTURED','upstream_commit':'578b85cc8d586b1677ec4335148adeb443057d24','attribution':'The Univalent Foundations Program, Homotopy Type Theory: Univalent Foundations of Mathematics','license':'CC BY-SA 3.0; https://creativecommons.org/licenses/by-sa/3.0/','scope':'Four fixed Book files, twelve actually read ranges; not whole Book or all community consumers. Historical open-problem language is not asserted as current state of the art.','semantic_search_attempt':{'tool':'zvec_grep_search','result':'Transport closed','fallback':'focused native rg plus exact primary-source reads; no index rebuild or deletion'},'rows':rows}
(OUT/'PRIMARY-SOURCES.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'files':len(SPEC),'ranges':len(rows),'status':receipt['status']}))
