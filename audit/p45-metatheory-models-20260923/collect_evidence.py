#!/usr/bin/env python3
"""P45 source-scope manifest; no new proof or implementation validation."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
paths=['HoTT/theory-schema/upstream/book-578b85cc/formal.tex','HoTT/theory-schema/SEMANTICS_AND_COHERENCE.md','HoTT/theory-schema/EXTENSIONS_AND_METATHEORY.md','.codex/research/hott/PREMISE-001/002 - P2 逐条登记 A-B 构造子与判定.md','.codex/research/hott/PREMISE-001/005 - P3P4 判定与审计链 A-B（AI 执行）.md','HoTT/CLAIM_EVIDENCE_MATRIX.md']
sources=[
 ('https://arxiv.org/pdf/1607.04156v2','intro; Corollaries4.21/4.22; 5.1 scope'),
 ('https://arxiv.org/pdf/2101.11479v2','intro/I.D; Theorem42; Corollaries46/47; atomic context and no-universe scope'),
 ('https://arxiv.org/pdf/1211.2851v5','1.1;1.2.4-1.2.11;3.4.1-3.4.4 scope; initiality qualification'),
 ('https://arxiv.org/pdf/1411.1736v2','intro/main theorem/Def2.1.1; local-universe triple and LF conditions'),
 ('https://arxiv.org/pdf/1705.07088','Def2.1;11.13-11.15 scope;12.9-12.15; intro limitations'),
 ('https://arxiv.org/pdf/1904.07004v2','6.3 scope;11.1-11.3; limitations and AppendixA universe scope'),
 ('https://su.diva-portal.org/smash/get/diva2:1431287/FULLTEXT01.pdf','2020; abstract/introduction;4.3 statement/proof-scope; not entire formalization'),
 ('https://arxiv.org/abs/2603.24923','identity/abstract only; locator, no stronger theorem attributed')]
out=dict(schema_version='bounded-theory-source-audit/v1',baseline='29fc16c6cc87db24436ba8a968e6a6b7b7e82b5d',book_commit='578b85cc8d586b1677ec4335148adeb443057d24',
 source_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},read_ranges={'formal.tex':[[968,1201]],'PREMISE-002':[[141,180]],'PREMISE-005':[[241,277]],'CLAIM_EVIDENCE_MATRIX':'C244-C249 index scope'},
 external_sources=[dict(url=u,read=r,status='SOURCE_REPORTED_NOT_REPLAYED' if 'locator' not in r else 'LOCATOR_ONLY') for u,r in sources],
 existing_R3_status='INDEX_SCOPE_REUSED_NOT_REPLAYED',new_math_claims=[],new_kernel_runs=[],
 verdict='CALCULUS_CONTEXT_MODEL_AND_COMPUTATIONAL_PROPERTIES_QUALIFIED_B01_B02_ATTRIBUTIONS_WITHDRAWN',
 limitations='No complete model construction, entire-paper proof audit, compiler correctness proof or physical bridge; old open statements not promoted to current global absence.')
(HERE/'EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'SOURCE_IDENTITIES_RECORDED','files':len(paths),'new_kernel_runs':0}))
