#!/usr/bin/env python3
"""Preserve actual relocated check outputs in the project evidence root."""
from pathlib import Path
import hashlib,json,shutil
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
RUN='HoTT/verification/runs/20260921-ASTRA-REVIEW-RELOCATION-01'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
e=json.loads((OUT/'EXTRACT.json').read_text());bundle=Path(e['bundle']);src=bundle.parent/'outputs-01'
result=json.loads((src/'RESULT.json').read_text());manifest=json.loads((bundle/'MANIFEST.json').read_text());build=json.loads((OUT/'BUILD.json').read_text())
assert sha(Path(build['archive']))==build['archive_sha256'] and sha(bundle/'MANIFEST.json')==build['manifest_sha256']
assert {x['case_id'] for x in result['results']}=={x['id'] for x in manifest['cases']}
assert result['status']=='SCOPED_RELOCATION_PASS'
dest=ROOT/RUN;assert not dest.exists();dest.mkdir(parents=True)
for name in ['RESULT.json','ENVIRONMENT.json']:shutil.copyfile(src/name,dest/name)
shutil.copyfile(bundle/'MANIFEST.json',dest/'bundle-manifest.json')
for item in result['results']:
    old=src/item['case_id'];new=dest/item['case_id'];new.mkdir()
    actual=json.loads((old/'RUN.json').read_text());assert actual==item
    for name,identity in item['artifacts'].items():assert (old/name).stat().st_size==identity['bytes'] and sha(old/name)==identity['sha256']
    for p in old.iterdir():
        if p.is_file():shutil.copyfile(p,new/p.name)
rows=[{'path':p.relative_to(dest).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(dest.rglob('*')) if p.is_file()]
receipt={'schema_version':'astra-scoped-review-relocation-evidence/v1','run_id':Path(RUN).name,'status':'SCOPED_RELOCATION_PASS','archive':build['archive'],'archive_sha256':build['archive_sha256'],'manifest_sha256':build['manifest_sha256'],'source_baseline':build['source_baseline'],
 'cases':[{'id':r['case_id'],'status':r['status'],'exit_code':r['exit_code'],'seconds':r['seconds'],'original_graph_equal':r['original_dependency_graph_equal'],'observed_path_escapes':r['observed_path_escapes'],'fresh_primitives':r['fresh_primitive_hashes_matched']} for r in result['results']],
 'files':rows,'scope':'Supplemental actual relocation replay of five existing proof entries and four exact type-error controls. No new mathematical claims; original primary runs remain primary. Environment recorded before execution, per-case RUN/outputs copied byte-for-byte. No claim of another machine, external peer review, OS access isolation, full repo qualification or four-stage target completion.'}
save(dest/'RUN.json',receipt);save(OUT/'REPLAY-VERIFICATION.json',{'status':receipt['status'],'run':RUN,'run_sha256':sha(dest/'RUN.json'),'copied_files':len(rows),'cases':receipt['cases'],'archive_sha256':receipt['archive_sha256']});print(json.dumps({'status':receipt['status'],'run':RUN,'files':len(rows),'cases':receipt['cases']},ensure_ascii=False))
