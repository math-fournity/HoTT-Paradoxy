#!/usr/bin/env python3
"""P46 source identity manifest; source-scope audit, no new kernel certification."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
paths=['HoTT/theory-schema/EXTENSIONS_AND_METATHEORY.md','HoTT/formal/partiality-race-timeout/GuardErasure.agda','HoTT/formal/partiality-race-timeout/CostFactorization.agda','audit/p33-2ltt-v5-self-metatheory-boundary-audit-20260922/P33-2LTT-V5-SELF-METATHEORY-BOUNDARY-AUDIT-REPORT.md','HoTT/CLAIM_EVIDENCE_MATRIX.md']
sources=[
 ('https://arxiv.org/pdf/1611.02108v1','sections 3,4.1-4.3,6;7 theorem/UA scope; interval,face,comp,Glue side conditions'),
 ('https://agda.readthedocs.io/en/v2.8.0/language/cubical.html','interval,IUniv,transp,Partial overlap,hcomp missing side,Glue; official contract only'),
 ('https://arxiv.org/pdf/1606.05223v2','intro and sections2.2-2.4; semantics introduction; no clock quantification in this version'),
 ('https://arxiv.org/pdf/2102.01969v3','Figures1/2;3.1 forcing ticks;Def4.1/Thm4.3;5.2 boundary and induction under clocks'),
 ('https://arxiv.org/pdf/1509.07584v3','section2 crisp/ordinary/substitution;sections7-8 topology vs identity and R-flat'),
 ('https://arxiv.org/pdf/1705.07442v5','section2.2 shape/extension and substitution;Def5.3 Segal;Def10.6 Rezk'),
 ('https://arxiv.org/pdf/2107.04663v2','sections2.2-2.5 cost monoid,step laws and extensional phase'),
 ('https://bentnib.org/quantitative-type-theory.pdf','Atkey LICS2018 DOI10.1145/3209108.3209189; variable/conversion/Pi rules and substitution lemma; earlier scheme limitation'),
 ('https://arxiv.org/pdf/2503.05790v2','Joshua Chen;intro1.1-1.4;Def4.2.1 and5.0.8; assumptions and coherence data'),
 ('https://arxiv.org/pdf/2311.18781v2','intro;2.4 boxed context display and telescope decalage'),
 ('https://arxiv.org/pdf/2407.09146v2','sections3.1.2-3.1.4 lattice interval,modal/global tininess,simplicial monad and axioms'),
 ('https://arxiv.org/pdf/2605.00812v2','Def1.1-1.4 and Thm1.5-1.6 conditions; categorical vs standard UA'),
 ('https://arxiv.org/pdf/1712.01800v1','intro and Kan/pretype/exact-equality scope; behavioral judgments not decidable')]
out=dict(schema_version='bounded-theory-source-audit/v1',baseline='34ad06c695de7f4239dd3e7492a4f1d5687188f9',source_hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},read_ranges={'GuardErasure.agda':'full','CostFactorization.agda':[[1,110]],'P33 report':'full','CLAIM_EVIDENCE_MATRIX':'C92-99 and C227-232 scope; no replay'},external_sources=[dict(url=u,read=r,status='SOURCE_REPORTED_NOT_REPLAYED') for u,r in sources],existing_evidence='P6 object-framework comparison, P33 2LTT, P42 CHM, old breakpoint and C92-99 controls reused with their original scopes',new_math_claims=[],new_kernel_runs=[],verdict='EXTENSION_RULES_AND_RESTRICTIONS_QUALIFIED',limitations='E03/E05/CATT deeper metatheory excluded with reasons in report008; no all-extension compatibility, physical interpretation, whole implementation or native translation certification.')
(HERE/'EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'SOURCE_IDENTITIES_RECORDED','files':len(paths),'new_kernel_runs':0}))
