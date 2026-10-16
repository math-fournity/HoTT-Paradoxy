#!/usr/bin/env python3
"""Capture the native rational quotient proof or one declared incorrect consumer."""
from pathlib import Path
import argparse, datetime, importlib.util, json, platform, subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('capture',ROOT/'scripts/audit/capture_agda_proof_run.py')
C=importlib.util.module_from_spec(sp);sp.loader.exec_module(C)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--module',choices=['QuotientConsumer','RawNumeratorQuotient','RawNumeratorTruncation'],default='QuotientConsumer');ap.add_argument('--cached',action='store_true');args=ap.parse_args()
    primary=args.module=='QuotientConsumer';assert not(primary and args.cached)
    proof='MP-ASTRA-QUOTIENT-CONSUMER-001' if primary else 'MP-ASTRA-'+args.module+'-CONTROL'
    run_id='20260920-'+proof+'-01';dest=ROOT/'HoTT/verification/runs'/run_id;assert not dest.exists()
    base='HoTT/formal/astra-quotient-consumer/';oldbase='HoTT/formal/dedekind-omega-missile/'
    source=base+args.module+'.agda';config=oldbase+'TOOLCHAIN.json';cfg=json.loads((ROOT/config).read_text())
    a,lib,cache=cfg['agda'],cfg['cubical_library'],cfg['runtime_cache']
    inputs=[source]+([] if primary else [base+'QuotientConsumer.agda'])+[oldbase+n+'.agda' for n in ['CutGoldForm','CutInfra','MissileTwoUniversalIrrationality']]+[config,cfg['project_library_registry'],'audit/astra-quotient-20260920/TASKSPEC.md','audit/astra-quotient-20260920/capture.py','scripts/audit/capture_agda_proof_run.py','audit/astra-s1-consumer-20260920/NEXT-SOURCES.json']
    files=[dict(C.file_row(ROOT/p),path=p) for p in inputs]
    pins=[(a['local_binary'],a['binary_bytes'],a['binary_sha256'],'agda-binary'),(a['local_archive'],a['asset_bytes'],a['asset_sha256'],'agda-release-asset'),(lib['local_archive'],lib['asset_bytes'],lib['asset_sha256'],'cubical-release-asset'),(lib['library_file'],lib['library_file_bytes'],lib['library_file_sha256'],'cubical-library-file')]
    external=[]
    for p,bs,hs,label in pins:C.expect_file(Path(p),bs,hs,label);external.append(C.file_row(Path(p),label=label))
    tree=C.deterministic_tree(Path(lib['local_root']));assert tree=={'file_count':lib['tree_file_count'],'total_bytes':lib['tree_total_bytes'],'tree_sha256':lib['tree_sha256']}
    external.append(dict(label='cubical-extracted-tree',local_path=lib['local_root'],**tree))
    prim=Path(cache['xdg_data_home'])/'agda'/a['version']/'lib/prim'
    for p in sorted(prim.rglob('*.agda')):external.append(C.file_row(p,label='agda-runtime-source:'+p.relative_to(prim).as_posix()))
    graph=OUT/(args.module+'-imports.dot')
    argv=['/usr/bin/env','XDG_DATA_HOME='+cache['xdg_data_home'],'XDG_CONFIG_HOME='+cache['xdg_config_home'],'TMPDIR='+cache['tmpdir'],a['local_binary']]
    if not args.cached:argv+=['--ignore-interfaces']
    argv+=['--library-file='+str(ROOT/cfg['project_library_registry']),'-l','cubical-0.9','-i',str(ROOT/base),'-i',str(ROOT/oldbase),'--dependency-graph='+str(graph),source]
    version=subprocess.run(argv[:5]+['--version'],cwd=ROOT,capture_output=True,check=True).stdout.decode().strip()
    started=datetime.datetime.now(datetime.timezone.utc);print('RUN '+run_id,flush=True);timeout=False
    try:
        p=subprocess.run(argv,cwd=ROOT,capture_output=True,timeout=600);code,stdout,stderr=p.returncode,p.stdout,p.stderr
    except subprocess.TimeoutExpired as exc:timeout=True;code,stdout,stderr=124,exc.stdout or b'',exc.stderr or b''
    ended=datetime.datetime.now(datetime.timezone.utc)
    assert all(C.sha((ROOT/f['path']).read_bytes())==f['sha256'] for f in files)
    assert C.deterministic_tree(Path(lib['local_root']))==tree
    assert all(C.file_row(Path(r['local_path']),label=r['label'])==r for r in external if r['label']!='cubical-extracted-tree')
    manifest={'schema_version':'formal-proof-source-manifest/v1','proof_id':proof,'run_id':run_id,'files':files,'external_dependencies':external}
    env=('platform='+platform.platform()+'\nagda='+version.replace('\n',' | ')+'\ntheory_variant=safe/cubical/guardedness\nlibrary_commit='+lib['tag_commit']+'\nlibrary_tree_sha256='+tree['tree_sha256']+'\ninterfaces_ignored='+str(not args.cached)+'\nobservation_seconds=600\noriginal_GOLD_Q_and_sources_unchanged=true\n').encode()
    blobs={'stdout.txt':stdout,'stderr.txt':stderr,'environment.txt':env,'source-manifest.json':C.json_bytes(manifest)}
    def entry(n):return {'path':n,'bytes':len(blobs[n]),'sha256':C.sha(blobs[n])}
    run={'schema_version':'formal-proof-run/v1','run_id':run_id,'proof_id':proof,'claim_ids':['C-305','C-306'] if primary else [],'proof_assistant':'Cubical Agda','proof_assistant_version':version,'theory_variant':'cubical','command_argv':argv,'cwd':str(ROOT),'started_at_utc':started.isoformat(),'completed_at_utc':ended.isoformat(),'duration_seconds':(ended-started).total_seconds(),'exit_code':code,'status':'OBSERVATION_TIMEOUT' if timeout else 'KERNEL_ACCEPTED_WITH_SCOPE' if code==0 else 'KERNEL_REJECTED','scope':'Actual GOLD rational quotient. Primary: arithmetic/GOLD representative invariance, non-propositional set target, mere representative to correct square via explicit constancy and rec→Set, precise impossibility of preserving every original numerator/fraction, and given-source Rich control. Incorrect consumers are fixed-term causal controls only.','non_goals':['No impossibility of choosing some canonical fraction or of computing invariant rational functions.','No physical point-removal or global HoTT inconsistency/completeness conclusion.','Additional chosen-source input is not bare-quotient provenance recovery.'],'stdout':entry('stdout.txt'),'stderr':entry('stderr.txt'),'environment':entry('environment.txt'),'source_manifest':entry('source-manifest.json'),'index_status':'PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE' if primary else 'CONTROL_ONLY_NO_NEW_CLAIM','git_status':'LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED'}
    dest.mkdir(parents=True)
    for n,data in blobs.items():C.exclusive_write(dest/n,data)
    C.exclusive_write(dest/'RUN.json',C.json_bytes(run))
    if code==0:assert graph.exists();C.exclusive_write(dest/'imports.dot',graph.read_bytes())
    print(json.dumps({'run':run_id,'exit':code,'seconds':run['duration_seconds'],'external_pins':len(external),'cached_control':args.cached}),flush=True)
    if code:print(stdout.decode()[-5000:]+stderr.decode(),flush=True)
    raise SystemExit(0 if code in (0,42) else 1)


if __name__=='__main__':main()
