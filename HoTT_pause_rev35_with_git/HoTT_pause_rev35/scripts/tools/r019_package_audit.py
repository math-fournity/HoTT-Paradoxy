#!/usr/bin/env python3
"""Verify source preservation, commit locally and package the complete audit with Git.
No remote operations or imported source updater execution.
"""
from pathlib import Path, PurePosixPath
import hashlib, json, os, stat, subprocess, tempfile, zipfile, datetime
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'artifacts/r019'
BASE_ZIP=Path('/mnt/data/HoTT_json_audit_rev18_with_git.zip'); BASE_PREFIX='HoTT_json_audit_rev18/'
BASE_HEAD='05431a2c37cc82ffaa1ab0b6023bb998d2f9ea3b'
ZIP=ROOT.parent/'HoTT2_audit_rev19_with_git.zip';BUNDLE=ROOT.parent/'HoTT2_audit_rev19.bundle'
RECEIPT=ROOT.parent/'HoTT2_audit_rev19_delivery_verification.json'
ALLOWED={'MEMORY.md','scripts/README.md','.codex/cognition/HEAD.json','.codex/research/hott/STATE.json','.codex/research/hott/FRONTIER.md','.codex/research/hott/LESSONS.md','.codex/research/hott/RESUME.md'}
LOG=[]
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def dump(path,data):path.write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
def run(argv,cwd=ROOT,timeout=90):
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.run(list(map(str,argv)),cwd=cwd,text=True,capture_output=True,timeout=timeout)
    LOG.append({'argv':list(map(str,argv)),'cwd':str(cwd),'started_at_utc':start,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    if p.returncode:raise RuntimeError(str(argv)+'\n'+p.stderr)
    return p.stdout.strip()
def git(*args,cwd=ROOT):return run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd)
def main():
    if any(p.exists() for p in (ZIP,BUNDLE,RECEIPT)):raise RuntimeError('Refuse delivery overwrite')
    assert git('rev-parse','HEAD')==BASE_HEAD
    assert git('remote')==''
    changed=[];protected=0;base_count=0
    with zipfile.ZipFile(BASE_ZIP) as z:
        for i in z.infolist():
            if i.is_dir():continue
            assert i.filename.startswith(BASE_PREFIX)
            rel=i.filename[len(BASE_PREFIX):]
            if rel.startswith('.git/'):continue
            base_count+=1;p=ROOT/rel;b=z.read(i)
            if not p.is_file() or p.read_bytes()!=b:changed.append(rel)
            elif rel not in ALLOWED:protected+=1
    assert set(changed)<=ALLOWED,changed
    raw=ROOT/'HoTT/sources/external-audits/HoTT-2(1).json'
    assert sha(raw)==sha(Path('/mnt/data/HoTT-2(1).json'))=='c2da542fdcc7b7a691242d991c21f7778c5c0ecda7e9a26cb2ab598dbab5ed27'
    assert json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())['revision']==19
    assert json.loads((OUT/'DIAGNOSTIC_TESTS.json').read_text())['passed']==32
    assert len(json.loads((OUT/'ATTACHMENT_AUDIT.json').read_text())['attachments'])==2
    rep=json.loads((OUT/'REPLAYS.json').read_text());assert len(rep)==3 and all(x['stdout_identical'] and x['exit_code']==0 for x in rep)
    assert json.loads((OUT/'GOVERNANCE_FAULT_PROBE.json').read_text())['success_claim_printed_despite_failure']
    # Machine-readable archive/index integrity, not a mathematical correctness assertion.
    for row in json.loads((OUT/'CODE_INDEX.json').read_text()):
        p=ROOT/row['path'];assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes']
    protect={'status':'PASS_BYTE_SCOPE','inherited_head':BASE_HEAD,'baseline_zip':str(BASE_ZIP),'baseline_zip_sha256':sha(BASE_ZIP),'base_non_git_file_count':base_count,'unchanged_protected_files':protected,'changed_existing_paths':changed,'allowed_changed_paths':sorted(ALLOWED),'original_input_sha256':sha(raw),'old_owners_skills_closure_schema_matrix_code_and_session_records_unchanged':True,'scope':'Exact byte comparison to supplied revision18 package except explicit dynamic memory/index. No native proof or full business cognition certification.'}
    dump(OUT/'INPUT_PROTECTION.json',protect)
    (OUT/'DELIVERY.md').write_text('''# R019 审计交付

完整核验HoTT-2(1).json（源界面名HoTT-2.json）全部公开内容、代码、运行输出和两个Python附件；17次Python执行不是17项数学实验。报告REVIEW.md，分项裁决CLAIMS.json，完整边界COVERAGE.md。

三版原示意器均已复现、exit0、stdout相同，32项诊断为软件审计；另有受控Git失败探针、两附件解码。没有执行原文件里的治理改写、没有Lean内核运行。否定的是超出证据的证明声明，保留用户双向问题与窄公理化计算现象。

当前工作根HoTT2_audit_rev19，继承rev18 Git main历史。checkpoint revision19真实保存，旧快照写回拒绝；原研究结论、用户原文和Skills未改。本包包含.git，另有bundle；压缩包外验证JSON记录最终HEAD、字节和恢复结果。

scripts/recovered/HoTT2_json包含会写绝对路径的外部脚本，仅作原始证据，勿批量运行。当前审计所有新代码已先存scripts再调用。源JSONthought/signatures只保全，既不当数学证明，也不取代当前模型自己的推演。
''')
    git('add','-A');git('commit','-m','Audit HoTT-2 additions: replay simulators, reject invalid checks, preserve governance evidence')
    head=git('rev-parse','HEAD');assert not git('status','--porcelain')
    git('fsck','--full');git('bundle','create',str(BUNDLE),'--all');git('bundle','verify',str(BUNDLE))
    rows=[]
    with zipfile.ZipFile(ZIP,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_symlink():raise RuntimeError('Unexpected symlink '+str(p))
            if p.is_file():
                rel=p.relative_to(ROOT).as_posix();z.write(p,ROOT.name+'/'+rel)
                rows.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
    with zipfile.ZipFile(ZIP) as z:
        assert z.testzip() is None
        for row in rows:
            b=z.read(ROOT.name+'/'+row['path']);assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
        with tempfile.TemporaryDirectory(prefix='hott-r019-restore-') as td:
            tmp=Path(td)
            for info in z.infolist():
                rel=PurePosixPath(info.filename)
                assert not rel.is_absolute() and '..' not in rel.parts
                p=tmp.joinpath(*rel.parts);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(info))
                mode=stat.S_IMODE(info.external_attr>>16)
                if mode:p.chmod(mode)
            restored=tmp/ROOT.name
            assert git('rev-parse','HEAD',cwd=restored)==head
            assert git('status','--porcelain',cwd=restored)==''
            git('fsck','--full',cwd=restored)
            clone=tmp/'from-bundle';run(['git','-c','core.hooksPath=/dev/null','clone',str(BUNDLE),str(clone)],cwd=tmp)
            assert git('rev-parse','HEAD',cwd=clone)==head and not git('status','--porcelain',cwd=clone)
    receipt={'schema_version':'hott-r019-delivery/v1','status':'VERIFIED_LOCAL_DELIVERY','completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'workspace':str(ROOT),'checkpoint_revision':19,'latest_session':'S-AUD-20260910-019-HOTT2-JSON','git':{'head':head,'inherited_head':BASE_HEAD,'branch':git('branch','--show-current'),'commits':int(git('rev-list','--count','HEAD')),'clean':True,'fsck':'PASS','remotes':[]},'zip':{'path':str(ZIP),'bytes':ZIP.stat().st_size,'sha256':sha(ZIP),'file_count':len(rows),'crc':'PASS','all_members_read_back':True,'restored_git_clean':True},'bundle':{'path':str(BUNDLE),'bytes':BUNDLE.stat().st_size,'sha256':sha(BUNDLE),'verify':'PASS','clone_same_head':True},'audit':{'source_chunks':73,'unchanged_prefix_chunks':16,'new_chunks':57,'python_execution_records':17,'native_lean_runs':0,'actual_original_simulator_replays':3,'diagnostic_tests':32,'decoded_python_attachments':2,'controlled_git_fault_probe':True,'math_kernel_verification':False,'full_business_cognition_gate':False},'input_protection':protect,'commands':LOG,'limits':['No source Lean compilation or HoTT formal proof','No proof of historical source commit outcome; only missing evidence and tested unchecked-success behavior','Only scoped source audit, not independent Fresh Session business cognition test','External Drive document body is absent; two embedded Python attachments were present and decoded']}
    dump(RECEIPT,receipt)
    ZIP.with_suffix(ZIP.suffix+'.sha256').write_text(sha(ZIP)+'  '+ZIP.name+'\n')
    print(json.dumps({'status':receipt['status'],'head':head,'commits':receipt['git']['commits'],'clean':True,'protected_prior_files':protected,'changed_existing_paths':changed,'zip':receipt['zip'],'bundle':receipt['bundle']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
