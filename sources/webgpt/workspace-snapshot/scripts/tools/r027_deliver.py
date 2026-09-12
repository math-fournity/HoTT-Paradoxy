"""Commit the local revision27 work and verify full ZIP/bundle restoration.
No remote action. New code and all evidence are retained in the Git workspace.
"""
from pathlib import Path
import datetime, hashlib, json, os, subprocess, sys, tempfile, time, zipfile
ROOT=Path(__file__).resolve().parents[2]; BASE=ROOT.parent
NAME='HoTT_Gemini_review_rev27'; D='.codex/research/hott/dialogues/GEMINI-001/'
O=ROOT/'artifacts/r027'

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1048576),b''):h.update(b)
    return h.hexdigest()

def call(argv,cwd=ROOT,timeout=60):
    t=time.perf_counter();start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.run(argv,cwd=cwd,capture_output=True,text=True,timeout=timeout,
                     env={**os.environ,'GIT_TERMINAL_PROMPT':'0','PYTHONDONTWRITEBYTECODE':'1'})
    rec={'argv':list(map(str,argv)),'cwd':str(cwd),'start_utc':start,
         'duration_seconds':time.perf_counter()-t,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    if p.returncode:
        fail=BASE/(NAME+'_delivery_failure.json')
        fail.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
        raise RuntimeError('Command failed; see '+str(fail))
    return rec

def git(*args,cwd=ROOT):
    return call(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd=cwd)

def main():
    outputs={
      'workspace_zip':BASE/(NAME+'_with_git.zip'),
      'bundle':BASE/(NAME+'.bundle'),
      'letter_packet':BASE/'Gemini_HoTT_debate_006.zip',
      'receipt':BASE/(NAME+'_delivery_verification.json')}
    if any(p.exists() for p in outputs.values()):raise FileExistsError('Do not overwrite delivery outputs')
    verification=call([sys.executable,'-B','scripts/tools/r027_verify.py'])
    (O/'FINAL_VERIFICATION_EXECUTION.json').write_text(json.dumps(verification,ensure_ascii=False,indent=2)+'\n')
    previous=git('rev-parse','HEAD')
    before=git('status','--short')
    if not before['stdout'].strip():raise RuntimeError('No changes to commit')
    git('add','--all')
    commit=git('commit','-m','Audit IN-006, preserve R026 context, and record scoped checks with OUT-006')
    head=git('rev-parse','HEAD')['stdout'].strip()
    clean=git('status','--porcelain=v1')
    if clean['stdout'].strip():raise RuntimeError('Dirty after commit')
    fsck=git('fsck','--full')
    remotes=git('remote')
    if remotes['stdout'].strip():raise RuntimeError('Unexpected remotes')
    history=git('log','-3','--format=%H %s')
    count=int(git('rev-list','--count','HEAD')['stdout'])
    bundle_create=git('bundle','create',str(outputs['bundle']),'--all')
    bundle_check=git('bundle','verify',str(outputs['bundle']))
    files=sorted(p for p in ROOT.rglob('*') if p.is_file())
    if any(p.is_symlink() for p in ROOT.rglob('*')):raise RuntimeError('Unexpected symlink')
    inventory=[{'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p)} for p in files]
    with zipfile.ZipFile(outputs['workspace_zip'],'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files:z.write(p,NAME+'/'+p.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(outputs['workspace_zip']) as z:
        if z.testzip() is not None:raise RuntimeError('ZIP CRC failure')
        for r in inventory:
            b=z.read(NAME+'/'+r['path'])
            if len(b)!=r['bytes'] or hashlib.sha256(b).hexdigest()!=r['sha256']:raise RuntimeError('ZIP member mismatch')
    selected=[D+'TO_GEMINI_006.md',D+'TO_GEMINI_006.txt',D+'TO_GEMINI_005.md']
    selected += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT/D/'rounds/007').glob('*')) if p.is_file()]
    selected += [p.relative_to(ROOT).as_posix() for folder in ['scripts/research/r027_lean','scripts/research/r027_coq','scripts/recovered/Gemini_IN006'] for p in sorted((ROOT/folder).glob('*')) if p.is_file()]
    selected += ['scripts/research/r027_fixedpoint_lemma_audit.py','scripts/tools/r027_run_checks.py',
      'artifacts/r027/FINITE_MODEL_RESULTS.json','artifacts/r027/FINITE_MODEL_RECEIPT.json',
      'artifacts/r027/FINITE_EXECUTION.json','artifacts/r027/NATIVE_RUN.json','artifacts/r027/TOOLCHAIN_PROBE.json',
      'artifacts/r027/REPORT.md','artifacts/r027/VERIFY.json',
      '.codex/research/hott/reviews/EARLY-GEMINI-001/ASSESSMENT.md',
      '.codex/research/hott/reviews/EARLY-GEMINI-001/PLAN.md']
    selected=sorted(set(selected))
    readme=('GEMINI-001 / OUT-006\n\n请先读 .codex/research/hott/dialogues/GEMINI-001/TO_GEMINI_006.md。\n'
      '来信IN-006与我方修改分开。七组有限模型检查已执行；Lean/Coq源码尚未原生编译，切勿冒认通过。\n'
      '本包不是全部仓库；R026评估与计划作为连续性背景保留。完整Git工作目录另行交付。\n'
      '请只就M01实际证明或反例、M02实际版本日志作新增贡献；不需再次道歉或重复赞同。\n'
      '本信尚未直接发送，不表示对方已收到。\n')
    packet_manifest={'scope':'OUT-006 correspondence packet; not native proof or full workspace',
       'files':[{'path':r,'bytes':(ROOT/r).stat().st_size,'sha256':sha(ROOT/r)} for r in selected],
       'generated':['README.txt','MANIFEST.json']}
    with zipfile.ZipFile(outputs['letter_packet'],'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for r in selected:z.write(ROOT/r,r)
        z.writestr('README.txt',readme)
        z.writestr('MANIFEST.json',json.dumps(packet_manifest,ensure_ascii=False,indent=2)+'\n')
    with zipfile.ZipFile(outputs['letter_packet']) as z:
        assert z.testzip() is None
        for r in packet_manifest['files']:
            assert hashlib.sha256(z.read(r['path'])).hexdigest()==r['sha256']
    finalplan=json.loads((O/'FINAL_PLAN.json').read_text())
    with tempfile.TemporaryDirectory(prefix='r027_restore_',dir=BASE) as temp:
        temp=Path(temp)
        with zipfile.ZipFile(outputs['workspace_zip']) as z:z.extractall(temp)
        restored=temp/NAME
        zip_head=git('rev-parse','HEAD',cwd=restored)
        zip_status=git('status','--porcelain=v1',cwd=restored)
        assert zip_head['stdout'].strip()==head and not zip_status['stdout'].strip()
        zip_fsck=git('fsck','--full',cwd=restored)
        fresh=call([sys.executable,'-B',str(restored/'scripts/session/r027_plan_check.py')],cwd=restored)
        assert json.loads(fresh['stdout'])['snapshot']==finalplan['snapshot']
        clone_path=temp/'bundle_clone'
        clone=git('clone',str(outputs['bundle']),str(clone_path),cwd=temp)
        clone_head=git('rev-parse','HEAD',cwd=clone_path)
        clone_status=git('status','--porcelain=v1',cwd=clone_path)
        assert clone_head['stdout'].strip()==head and not clone_status['stdout'].strip()
        clone_fsck=git('fsck','--full',cwd=clone_path)
        clone_plan=call([sys.executable,'-B',str(clone_path/'scripts/session/r027_plan_check.py')],cwd=clone_path)
        assert json.loads(clone_plan['stdout'])['snapshot']==finalplan['snapshot']
    unchanged=git('status','--porcelain=v1')
    assert not unchanged['stdout'].strip()
    report={'schema':'r027-delivery/v1','status':'PASS','root':str(ROOT),'revision':27,'git_head':head,
       'branch':git('branch','--show-current')['stdout'].strip(),'commit_count':count,
       'git_remote_count':0,'history_preserved':True,'git_clean':True,'git_fsck':'PASS',
       'archive_files':len(files),'all_zip_members_identical':True,'relocated_plan_matches':True,
       'bundle_clone_head_matches':True,'bundle_clone_clean':True,
       'finite_checks':'7 groups, 4330 finite labelled models; not general HoTT certification',
       'native_Lean_Rocq_HoTT':'NOT_RUN_TOOL_UNAVAILABLE','full_business_cognition':'NOT_CERTIFIED',
       'peer_reply_status':'OUT-006 PREPARED_NOT_SENT','snapshot':finalplan['snapshot'],
       'original_preservation':json.loads((O/'VERIFY.json').read_text()),
       'outputs':{k:{'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)} for k,p in outputs.items() if k!='receipt'},
       'commands':{'pre_head':previous,'pre_status':before,'commit':commit,'history':history,'fsck':fsck,
          'bundle_create':bundle_create,'bundle_verify':bundle_check,'zip_head':zip_head,'zip_clean':zip_status,
          'zip_fsck':zip_fsck,'zip_plan':fresh,'clone':clone,'clone_head':clone_head,'clone_status':clone_status,
          'clone_fsck':clone_fsck,'clone_plan':clone_plan},
       'file_inventory':inventory,
       'limit':'File and Git verification, finite checks, source audit and paper derivations only. No actual native binary results.'}
    outputs['receipt'].write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    for key,path in outputs.items():
        Path(str(path)+'.sha256').write_text(sha(path)+'  '+path.name+'\n')
    print(json.dumps({'status':'PASS','revision':27,'git_head':head,'commits':count,
       'files_in_zip':len(files),'outputs':report['outputs'],'receipt':str(outputs['receipt'])},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
