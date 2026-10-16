#!/usr/bin/env python3
"""Build an immutable scoped proof review bundle from exact committed inputs.

MACHINE_MANAGED_CANONICAL export: edit proof/docs owners, then create a new export
directory. Never overwrite an earlier export, receipt or archive.
"""
from pathlib import Path
import argparse,gzip,hashlib,importlib.util,json,shutil,subprocess,tarfile
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
REVIEW=ROOT/'HoTT/review/four-stage-redo-v1'
BASE='9c33e1c32c9649855091d7631ce0ff7a0377d5b1'
SPEC=[('geometry','MP-ASTRA-NATIVE-TASK-INTEGRATION-001'),('source','MP-ASTRA-NATIVE-SOURCE-CONTRACT-001'),('sqrt2','MP-ASTRA-SQRT2-TASK-COMPARISON-001'),('s1','MP-ASTRA-S1-CONSUMER-001'),('quotient','MP-ASTRA-QUOTIENT-CONSUMER-001')]
sp=importlib.util.spec_from_file_location('capture',ROOT/'scripts/audit/capture_agda_unimath_replay_run.py');C=importlib.util.module_from_spec(sp);sp.loader.exec_module(C)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--destination',type=Path,required=True);ap.add_argument('--archive',type=Path,required=True);args=ap.parse_args();dest=args.destination.resolve();archive=args.archive.resolve()
    assert not dest.exists() and not archive.exists();dest.mkdir(parents=True)
    registry=json.loads((ROOT/'HoTT/verification/PROOF_VERSION_CLOSURE.json').read_text());cases=[];source_rows={};provenance=[]
    def put(src,rel,expected=None):
        assert src.is_file() and not src.is_symlink()
        if expected:assert sha(src)==expected,src
        target=dest/rel
        if target.exists():assert target.read_bytes()==src.read_bytes();return
        target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,target)
    for key,proof in SPEC:
        row=next(r for r in registry['later_packages'] if r['proof_id']==proof)
        run=json.loads((ROOT/row['run']/'RUN.json').read_text());man=json.loads((ROOT/row['run']/'source-manifest.json').read_text())
        assert run['exit_code']==0
        argv=run['command_argv'];native='agda-unimath' in row['source']
        inc=['sources/'+argv[i+1].removeprefix(str(ROOT)+'/') for i,x in enumerate(argv) if x=='-i']
        for f in man['files']:
            if f['path'].endswith('.agda'):
                raw=subprocess.check_output(['git','show',row['release_ref']+':'+f['path']],cwd=ROOT)
                assert hashlib.sha256(raw).hexdigest()==f['sha256']
                put(ROOT/f['path'],'sources/'+f['path'],f['sha256']);source_rows[f['path']]=f
        original='origin-primary-runs/'+Path(row['run']).name
        for name in ['RUN.json','stdout.txt','stderr.txt','environment.txt','source-manifest.json','imports.dot','index-row-manifest.json']:
            put(ROOT/row['run']/name,original+'/'+name)
        cases.append({'id':key,'proof_id':proof,'claim_ids':run['claim_ids'],'source':'sources/'+row['source'],'include_roots':inc,'library':'agda-unimath-no-erasure' if native else 'cubical-0.9','library_file':'vendor/unimath/agda-unimath.agda-lib' if native else 'vendor/cubical/cubical.agda-lib','primary_run':row['run'],'source_release_ref':row['release_ref'],'original_graph':original+'/imports.dot','expected_exit':0})
        provenance.append(row)
    # Exact previous causal controls, not newly altered proof terms.
    for i in range(1,5):
        key='SC0'+str(i);runrel='HoTT/verification/runs/20260920-MP-ASTRA-S1-'+key+'-CONTROL-01';run=json.loads((ROOT/runrel/'RUN.json').read_text())
        assert run['exit_code']==42
        path='HoTT/formal/astra-s1-consumer-check/'+key+'.agda';man=json.loads((ROOT/runrel/'source-manifest.json').read_text());f=next(f for f in man['files'] if f['path']==path)
        assert subprocess.check_output(['git','show',BASE+':'+path],cwd=ROOT)==(ROOT/path).read_bytes()
        put(ROOT/path,'sources/'+path,f['sha256']);source_rows[path]=f
        orig='origin-primary-runs/'+Path(runrel).name
        for name in ['RUN.json','stdout.txt','stderr.txt','environment.txt','source-manifest.json']:put(ROOT/runrel/name,orig+'/'+name)
        diagnostics={'SC01':r'(?s)error: \[UnequalTerms\].*primGlue','SC02':r'(?s)error: \[UnequalTerms\].*loop i != base.*boundary','SC03':r'(?s)error: \[UnequalTerms\].*predℤ \(sucℤ y\) != y','SC04':r'(?s)error: \[UnequalTerms\].*decode x \(encode x p\) i != p i'}
        cases.append({'id':key,'proof_id':run['proof_id'],'claim_ids':[],'source':'sources/'+path,'include_roots':['sources/HoTT/formal/astra-s1-consumer-check'],'library':'cubical-0.9','library_file':'vendor/cubical/cubical.agda-lib','primary_run':runrel,'expected_exit':42,'diagnostic_regex':diagnostics[key]})
    cfgN=json.loads((ROOT/'HoTT/formal/agda-unimath/no-erasure/TOOLCHAIN.json').read_text());cfgC=json.loads((ROOT/'HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json').read_text())
    for cfg,field,name in [(cfgN,'agda_unimath_library','unimath'),(cfgC,'cubical_library','cubical')]:
        lib=cfg[field];root=Path(lib['local_root']);tree=C.deterministic_tree(root)
        assert tree=={'file_count':lib['tree_file_count'],'total_bytes':lib['tree_total_bytes'],'tree_sha256':lib['tree_sha256']}
        for p in sorted(root.rglob('*')):
            if p.is_file() and not p.is_symlink() and p.suffix!='.agdai' and p.name!='.DS_Store':put(p,'vendor/'+name+'/'+p.relative_to(root).as_posix())
        assert C.deterministic_tree(dest/'vendor'/name)==tree
    for rel in ['HoTT/formal/agda-unimath/no-erasure/TOOLCHAIN.json','HoTT/formal/agda-unimath/no-erasure/identity-replacement.patch','HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json']:
        put(ROOT/rel,'provenance/'+rel)
    prim=Path(cfgN['runtime_cache']['xdg_data_home'])/'agda'/cfgN['agda']['version']/'lib/prim'
    primitives=[{'path':p.relative_to(prim).as_posix(),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(prim.rglob('*.agda'))]
    for p in sorted(REVIEW.rglob('*')):
        if p.is_file() and p.suffix in ('.md','.py'):put(p,p.relative_to(REVIEW).as_posix())
    primary=ROOT/'audit/astra-case-integration-20260921'
    put(primary/'PRIMARY-SOURCES.json','references/PRIMARY-SOURCES.json')
    for p in sorted((primary/'primary-source-excerpts').iterdir()):put(p,'references/'+p.name)
    rows=[{'path':p.relative_to(dest).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(dest.rglob('*')) if p.is_file()]
    manifest={'schema_version':'astra-scoped-review-bundle/v1','producer':str(Path(__file__).relative_to(ROOT)),'source_baseline':BASE,'cases':cases,'files':rows,'source_rows':list(source_rows.values()),'selected_packages':provenance,'agda':{k:v for k,v in cfgN['agda'].items() if not k.startswith('local_')}|{'primitive_sources':primitives},'scope':'Five accepted proof entries and four exact type-error controls. Libraries pinned including no-erasure derivative; compiler is supplied separately and hash checked. Original receipts retain historical paths and are provenance, not portable commands. No private dialogue, credentials, full repository history or publication included.'}
    save(dest/'MANIFEST.json',manifest)
    archive.parent.mkdir(parents=True,exist_ok=True)
    with archive.open('xb') as f,gzip.GzipFile(fileobj=f,mode='wb',mtime=0) as gz,tarfile.open(fileobj=gz,mode='w|') as tar:
        for p in sorted(dest.rglob('*')):
            if not p.is_file():continue
            info=tar.gettarinfo(str(p),arcname='four-stage-review/'+p.relative_to(dest).as_posix());info.uid=info.gid=0;info.uname=info.gname='';info.mtime=0;info.mode=0o644
            with p.open('rb') as h:tar.addfile(info,h)
    receipt={'status':'BUNDLE_CREATED_NOT_YET_REPLAYED','archive':str(archive),'archive_bytes':archive.stat().st_size,'archive_sha256':sha(archive),'manifest_sha256':sha(dest/'MANIFEST.json'),'file_count':len(rows)+1,'cases':[c['id'] for c in cases],'local_proof_sources':len(source_rows),'producer_sha256':sha(Path(__file__)),'source_baseline':BASE}
    save(OUT/'BUILD.json',receipt);print(json.dumps(receipt,ensure_ascii=False))
if __name__=='__main__':main()
