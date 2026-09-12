"""Retain first check report and generate a corrected scope-aware verifier.
Git index refresh is not source mutation. A known missing inherited reference
remains a warning; no placeholder or blanket all-links-pass assertion is made.
"""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[2]; S=R/'scripts/session'; O=R/'artifacts/r021'
p=S/'r021_verify.py';t=p.read_text()
t=t.replace("base=json.loads((O/'BASELINE_FILES.json').read_text())", "all_base=json.loads((O/'BASELINE_FILES.json').read_text())\nbase=[r for r in all_base if not r['path'].startswith('.git/')]")
a="check('V29_local_links',not bad,{'broken':bad,'anchors':'Existence only; external URLs not re-fetched'})"
b="""known={'source':qrel,'target':'sources/aistudio-discussions/README.md'}
known_in_old=known['target'] in old(qrel).decode()
new_broken=[x for x in bad if x!=known]
check('V29_new_local_links',not new_broken,{'new_broken':new_broken,'anchors':'Existence only; external URLs not re-fetched'})
checks.append({'id':'V32_inherited_missing_reference','status':'WARNING' if bad==[known] and known_in_old else ('PASS' if not bad else 'FAIL'),
 'scope':{'missing_inherited':bad,'reference_preexists_in_v4':known_in_old,
 'action':'Preserve historical reference and report missing source; do not invent README or claim complete legacy archive.'}})"""
assert t.count(a)==1;t=t.replace(a,b)
t=t.replace("out=O/'FILE_CHECKS.json'", "out=O/'FILE_CHECKS_FINAL.json'")
t=t.replace("'failed':[x for x in checks if x['status']=='FAIL']", "'failed':[x for x in checks if x['status']=='FAIL'],'warnings':[x for x in checks if x['status']=='WARNING']")
t=t.replace("raise SystemExit(0 if result['passed']==result['total'] else 1)","raise SystemExit(1 if any(x['status']=='FAIL' for x in checks) else 0)")
out=S/'r021_verify_final.py'
if out.exists():raise RuntimeError('Refuse overwrite final verifier')
out.write_text(t)
(O/'VERIFIER_SCOPE_CORRECTION.json').write_text(json.dumps({
 'original_report':'FILE_CHECKS.json','original_failures':['V01_prior_file_scope','.git/index changed during actual git status','V29_local_links: inherited missing sources/aistudio-discussions/README.md'],
 'change':'Exclude .git internals from old source byte immutability; validate Git through git fsck/clean/history. Keep inherited missing reference as explicit WARNING; check new links separately.',
 'no_source_placeholder_created':True,'no_original_failure_removed':True},ensure_ascii=False,indent=2)+'\n')
print(str(out))
