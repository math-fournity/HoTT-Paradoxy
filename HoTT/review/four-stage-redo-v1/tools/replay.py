#!/usr/bin/env python3
"""Recheck the fixed four-stage review cases from a relocated source bundle.

Checks exact input bytes, then executes the pinned Agda compiler with fresh data
and ignored interfaces. It does not certify the mathematical interpretation.
"""
from pathlib import Path,PurePosixPath
from concurrent.futures import ThreadPoolExecutor
import argparse,datetime,hashlib,json,os,platform,re,shutil,subprocess,sys,time

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def within(root,rel):
    q=PurePosixPath(rel)
    if q.is_absolute() or '..' in q.parts or '\\' in rel:raise ValueError('UNSAFE_PATH:'+rel)
    p=root/rel
    if p.is_symlink():raise ValueError('SYMLINK_INPUT:'+rel)
    return p
def verify(root,manifest):
    for row in manifest['files']:
        p=within(root,row['path'])
        if not p.is_file() or p.stat().st_size!=row['bytes'] or digest(p)!=row['sha256']:
            raise ValueError('INPUT_MISMATCH:'+row['path'])
    expected={r['path'] for r in manifest['files']}|{'MANIFEST.json'}
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    if actual!=expected:raise ValueError('UNEXPECTED_BUNDLE_FILES:'+repr(sorted(actual^expected)))
def graph(path):
    raw=path.read_text();nodes=dict(re.findall(r'\b(m\d+)\[label="([^"]+)"\];',raw))
    edges=re.findall(r'\b(m\d+) -> (m\d+);',raw)
    if not nodes:raise ValueError('EMPTY_GRAPH')
    return {'nodes':sorted(nodes.values()),'edges':sorted([nodes[a],nodes[b]] for a,b in edges)}

def run_case(bundle,manifest,agda,out,case,timeout):
    dest=out/case['id'];dest.mkdir();work=dest/'work';work.mkdir()
    for part in ('sources','vendor'):shutil.copytree(bundle/part,work/part)
    runtime=dest/'runtime';runtime.mkdir();data=runtime/'data';config=runtime/'config';tmp=runtime/'tmp'
    for p in (data,config,tmp):p.mkdir()
    env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','LANG':'en_US.UTF-8',
         'XDG_DATA_HOME':str(data),'XDG_CONFIG_HOME':str(config),'TMPDIR':str(tmp)}
    setup=subprocess.run([str(agda),'--setup'],cwd=work,env=env,capture_output=True)
    (dest/'setup.stdout.txt').write_bytes(setup.stdout);(dest/'setup.stderr.txt').write_bytes(setup.stderr)
    if setup.returncode:raise ValueError('AGDA_SETUP_FAILED:'+case['id'])
    data_result=subprocess.run([str(agda),'--print-agda-data-dir'],cwd=work,env=env,capture_output=True,check=True)
    prim=Path(data_result.stdout.decode().strip())/'lib/prim'
    if not prim.is_relative_to(runtime):raise ValueError('RUNTIME_OUTSIDE_FRESH_ROOT:'+str(prim))
    for row in manifest['agda']['primitive_sources']:
        if digest(prim/row['path'])!=row['sha256']:raise ValueError('BUILTIN_SOURCE_MISMATCH:'+row['path'])
    registry=dest/'libraries';registry.write_text(str(work/case['library_file'])+'\n')
    argv=[str(agda),'--ignore-interfaces','--no-default-libraries','--library-file='+str(registry),'-l',case['library']]
    for inc in case['include_roots']:argv+=['-i',str(work/inc)]
    argv+=['--dependency-graph='+str(dest/'imports.dot'),str(work/case['source'])]
    initial={p.relative_to(work).as_posix():digest(p) for p in work.rglob('*') if p.is_file()}
    if any(p.endswith('.agdai') for p in initial):raise ValueError('PREEXISTING_INTERFACE')
    save(dest/'START.json',{'status':'RUNNING','pid':os.getpid(),'case':case['id'],'argv':argv,'cwd':str(work),'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()})
    print('START '+case['id'],flush=True);start=time.monotonic();expired=False
    with (dest/'stdout.txt').open('wb') as stdout,(dest/'stderr.txt').open('wb') as stderr:
        try:code=subprocess.run(argv,cwd=work,env=env,stdout=stdout,stderr=stderr,timeout=timeout).returncode
        except subprocess.TimeoutExpired:code=124;expired=True
    seconds=time.monotonic()-start
    unchanged=all(digest(work/p)==h for p,h in initial.items())
    raw=(dest/'stdout.txt').read_text(errors='replace')+'\n'+(dest/'stderr.txt').read_text(errors='replace')
    imports=re.findall(r'^\s*Checking ([^\s]+) \((.+)\)\.$',raw,re.M)
    escapes=[p for _,p in imports if not Path(p).is_relative_to(work) and not Path(p).is_relative_to(runtime)]
    expected=case['expected_exit'];diagnostic=not case.get('diagnostic_regex') or bool(re.search(case['diagnostic_regex'],raw))
    same_graph=None
    if expected==0 and code==0:
        same_graph=graph(dest/'imports.dot')==graph(bundle/case['original_graph'])
    passed=code==expected and diagnostic and unchanged and not escapes and bool(imports) and (expected!=0 or same_graph)
    receipt={'schema_version':'astra-scoped-relocation-replay/v1','case_id':case['id'],'proof_id':case['proof_id'],'source_primary_run':case['primary_run'],
      'status':'RELOCATION_REPLAY_PASS_WITH_SCOPE' if passed else 'RELOCATION_REPLAY_FAILED',
      'command_argv':argv,'cwd':str(work),'exit_code':code,'expected_exit':expected,'seconds':seconds,'observation_timeout':expired,
      'input_files_unchanged':unchanged,'interface_cache_initially_empty':True,'ignore_interfaces':True,'fresh_primitive_hashes_matched':len(manifest['agda']['primitive_sources']),
      'observed_checking_lines':len(imports),'observed_path_escapes':escapes,'original_dependency_graph_equal':same_graph,'expected_diagnostic_matched':diagnostic,
      'bundle_manifest_sha256':digest(bundle/'MANIFEST.json'),'compiler_sha256':digest(agda),'replayer_sha256':digest(Path(__file__)),
      'platform':platform.platform(),'artifacts':{p.name:{'bytes':p.stat().st_size,'sha256':digest(p)} for p in sorted(dest.iterdir()) if p.is_file()},
      'scope':'Same machine/macOS arm64 exact compiler and fixed bytes in a distinct fresh directory. No OS access sandbox or network isolation claimed. Imported-source paths observed in compiler output; not an operating-system file-access trace. Negative controls are rejected fixed terms, not negative mathematical theorems.'}
    save(dest/'RUN.json',receipt);print(json.dumps({'case':case['id'],'status':receipt['status'],'exit':code,'seconds':seconds}),flush=True)
    return receipt

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--bundle',type=Path,default=Path(__file__).resolve().parents[1]);ap.add_argument('--agda',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--case',action='append');ap.add_argument('--all',action='store_true');ap.add_argument('--jobs',type=int,choices=(1,2),default=1);ap.add_argument('--timeout',type=int,default=1800);args=ap.parse_args()
    bundle=args.bundle.resolve();agda=args.agda.resolve();out=args.out.resolve();manifest=json.loads((bundle/'MANIFEST.json').read_text())
    verify(bundle,manifest)
    if digest(agda)!=manifest['agda']['binary_sha256']:raise ValueError('COMPILER_HASH_MISMATCH')
    if not args.all and not args.case:raise ValueError('SELECT_CASE_OR_ALL')
    selected=manifest['cases'] if args.all else [c for c in manifest['cases'] if c['id'] in args.case]
    if not args.all and set(args.case)!={c['id'] for c in selected}:raise ValueError('UNKNOWN_CASE')
    if out.exists() or out.is_relative_to(bundle):raise ValueError('OUTPUT_MUST_BE_NEW_AND_OUTSIDE_BUNDLE')
    out.mkdir(parents=True)
    version=subprocess.run([str(agda),'--version'],capture_output=True,check=True).stdout.decode().strip()
    save(out/'ENVIRONMENT.json',{'platform':platform.platform(),'compiler':str(agda),'version':version,'binary_sha256':digest(agda),'bundle':str(bundle),'manifest_sha256':digest(bundle/'MANIFEST.json'),'cases':[c['id'] for c in selected],'jobs':args.jobs,'timeout_per_case':args.timeout})
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futures=[pool.submit(run_case,bundle,manifest,agda,out,c,args.timeout) for c in selected]
        results=[]
        for f in futures:
            try:results.append(f.result())
            except Exception as e:results.append({'status':'RELOCATION_SETUP_OR_VERIFICATION_FAILED','error':str(e)})
    verify(bundle,manifest)
    good=all(r['status']=='RELOCATION_REPLAY_PASS_WITH_SCOPE' for r in results)
    save(out/'RESULT.json',{'status':'SCOPED_RELOCATION_PASS' if good else 'SCOPED_RELOCATION_FAILED','results':results,'new_mathematical_claims':False,'parent_goal':'OPEN'})
    return 0 if good else 1
if __name__=='__main__':sys.exit(main())
