#!/usr/bin/env python3
"""Record P42 source identity and bounded reading/dependency scope, not proofs."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
BOOK=Path('HoTT/theory-schema/upstream/book-578b85cc')
ranges={'formal.tex':[[764,905]],'induction.tex':[[1,146],[242,447],[566,635],[752,1071]],'hits.tex':[[1,220],[353,429],[1048,1257],[2041,2101]],'hlevels.tex':[[27,118],[447,634]],'logic.tex':[[808,936]]}
paths=[BOOK/p for p in ranges]+[Path('HoTT/formal/ercf-truncation-defense/TruncationDefense.agda'),Path('HoTT/formal/partiality-race-timeout/QuotientMonad.agda')]
old=[]
for p in sorted((ROOT/'.codex/research/hott/PREMISE-001').glob('00[1-7]*.md')):
    paths.append(p.relative_to(ROOT))
    for n,line in enumerate(p.read_text().splitlines(),1):
        if re.search(r'(?:PREMISE-)?(?:A-03|A-11|E-02|E-03|E-04)',line):
            old.append(dict(path=str(p.relative_to(ROOT)),line=n,text=line))
manifest=json.loads((ROOT/'核心认知.manifest.json').read_text())
evidence=dict(schema_version='bounded-theory-source-audit/v1',baseline='e8d5b917883e',book_commit='578b85cc8d586b1677ec4335148adeb443057d24',
    source_hashes={str(p):hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},read_ranges=ranges,
    reused_read_receipt='P41 logic.tex 1-1278; P42 selectively reread unique choice and truncation convention',
    old_dependency_occurrences=old,
    external_sources=[
      dict(url='https://arxiv.org/pdf/1802.01170v2',version='2018-04-30 v2',read='intro; 3.1/3.2 relevant rules; 3.3.4; 3.4/4 boundary paragraphs',claim='selected HIT computation and scoped schema, not a 2026 absence claim'),
      dict(url='https://www.cs.cmu.edu/~rwh/papers/higher/paper.pdf',version='POPL 2019 DOI 10.1145/3290314',read='intro; 4.1 Figures 11/12',claim='indexed CIT schema in distinct cartesian computational theory'),
      dict(url='https://lmcs.episciences.org/6100/pdf',version='LMCS 16(1:10)2020',read='abstract; 2 Figures 1/2 and explanations',claim='HIIT signatures and positivity restriction, not all initial algebras established'),
    ],external_status='SOURCE_REPORTED_NOT_REPLAYED',existing_control_status='SOURCE_INSPECTED_NOT_REPLAYED_THIS_WAVE',new_math_claims=[],new_kernel_runs=[],
    recovery=dict(protocol='v3 receipt reattestation',core_generation=8,unit_count=len(manifest['units']),goal3_and_KC47_48='FULL_REREAD_AFTER_COMPACTION',head_tracked_hash_mismatches=[],not_certified='Hashes do not certify model understanding'),
    verdict='CONSTRUCTION_AND_ELIMINATION_SIDE_CONDITIONS_QUALIFY_OLD_A03_A11_E02_E03_E04')
(HERE/'EVIDENCE.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='SOURCE_IDENTITIES_RECORDED',files=len(paths),dependency_occurrences=len(old),new_kernel_runs=0)))
