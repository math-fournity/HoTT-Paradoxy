#!/usr/bin/env python3
"""Verify bytes, literal contract locators and report links; not Coq elaboration."""
from pathlib import Path
import hashlib,json,re,urllib.parse
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
REPORT=ROOT/'Astra继续尝试/断点与证明机制系统检查/第三十五轮执行报告.md'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
inputs=json.loads((OUT/'INPUT-VERIFICATION.json').read_text());assert inputs['selected_packages']==9 and inputs['qualification_checks']==18
snapshot=json.loads((OUT/'LOCATOR-SOURCES.json').read_text())
for row in snapshot['files']:assert sha(ROOT/row['path'])==row['sha256']
base=OUT/'upstream-locator/theories'
expected={
 'Analysis/Locator.v':[
 'Definition locator (x : F) := forall q r : Q, q < r -> (\' q < x) + (x < \' r).',
 'Context `{ExcludedMiddle}.','Definition lower_bound :','Lemma tight_bound',
 '(nu : x ≶ 0).','Definition locator_recip : locator (// (x ; nu)).',
 'Lemma locator_times : locator (x * y).','Proof. Abort.',
 'Context {M} {M_ismod : CauchyModulus Q F xs M}.','Context (ls : forall n, locator (xs n)).',
 'Lemma locator_limit {l} : IsLimit _ _ xs l -> locator l.'],
 'Classes/interfaces/canonical_names.v':['Notation "(<>)" := (fun x y => ~x = y)','Infix "≶" := apart','Definition ApartZero','Class Recip A'],
 'Classes/interfaces/abstract_algebra.v':['Class IsField','Class IsDecField'],
 'ExcludedMiddle.v':['Monomorphic Axiom ExcludedMiddle : Type0.','Axiom LEM : forall `{ExcludedMiddle} (P : Type), IsHProp P -> P + ~P.'],
 'BoundedSearch.v':['(P_dec : forall n, Decidable (P n))','(P_inhab : hexists (fun n => P n)).','Definition minimal_n_alt_type']}
locators=[]
for rel,markers in expected.items():
    text=(base/rel).read_text();lines=text.splitlines()
    for marker in markers:
        found=[i for i,line in enumerate(lines,1) if marker in line];assert found,(rel,marker)
        locators.append({'path':(base/rel).relative_to(ROOT).as_posix(),'literal_marker':marker,'lines':found})
links=[]
for p in [REPORT,*sorted(REPORT.with_suffix('').glob('*.md'))]:
    for m in re.finditer(r'\[[^\]]+\]\((?:<([^>]+)>|([^\)]+))\)',p.read_text()):
        target=m.group(1) or m.group(2)
        if target.startswith(('http:','https:','#')):continue
        target=re.sub(r':\d+$','',urllib.parse.unquote(target.split('#')[0]));q=Path(target) if target.startswith('/') else p.parent/target
        assert q.exists(),(p,target);links.append({'source':p.relative_to(ROOT).as_posix(),'target':target})
receipt={'status':'AUDIT_SOURCE_IDENTITY_LOCATORS_AND_LINKS_PASS','proof_qualification_receipt_sha256':sha(OUT/'INPUT-VERIFICATION.json'),'fixed_coq_commit':snapshot['commit'],'source_files_verified':len(snapshot['files']),'literal_locators':locators,'local_report_links_checked':len(links),'coq_compiled':False,'new_mathematical_claims':False,'reading_attestation':{'Locator.v':'Local lines1–429,430–768,769–808 emitted; EOF808. Tool identity is not a comprehension certificate.','fully_read_other_files':['BoundedSearch.v','DProp.v','ExcludedMiddle.v','Classes/interfaces/cauchy.v','LICENSE.txt'],'other_sources':'Relevant declarations only, not all14 full bodies or transitive import closure'},'scope':'Literal declarations and human-scoped contract review, not exported minimal assumptions, Coq validity, runtime computation, all-library absence or a HoTT defect theorem.'}
(OUT/'AUDIT-VERIFICATION.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'sources':len(snapshot['files']),'markers':len(locators),'links':len(links),'coq_compiled':False}))
