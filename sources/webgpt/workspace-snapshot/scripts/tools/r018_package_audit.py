#!/usr/bin/env python3
"""Protect source history; locally commit and package R018 with verified Git restore.
No remote push, shell snippets, global installation or mathematical certification.
All subprocess invocations and errors are retained in an external receipt.
"""
from pathlib import Path
import hashlib
import json
import os
import shutil
import stat
import subprocess
import tempfile
import zipfile

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r018'
DELIVERY=ROOT.parent
ZIP=DELIVERY/'HoTT_json_audit_rev18_with_git.zip'
BUNDLE=DELIVERY/'HoTT_json_audit_rev18.bundle'
RECEIPT=DELIVERY/'HoTT_json_audit_rev18_delivery_verification.json'
LOG=[]
ALLOWED_CHANGED={'.codex/cognition/HEAD.json','.codex/research/hott/STATE.json','.codex/research/hott/FRONTIER.md','.codex/research/hott/LESSONS.md','.codex/research/hott/RESUME.md','MEMORY.md','scripts/README.md'}

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return h.hexdigest()

def run(args,cwd=ROOT,timeout=90):
    p=subprocess.run(args,cwd=cwd,capture_output=True,text=True,timeout=timeout)
    LOG.append({'argv':list(map(str,args)),'cwd':str(cwd),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    if p.returncode:raise RuntimeError(f'Command failed: {args}\n{p.stderr}')
    return p.stdout.strip()

def git(*args,cwd=ROOT):
    return run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd)

def write_json(path,data):
    path.write_text(json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+'\n')

def main():
    for p in (ZIP,BUNDLE,RECEIPT):
        if p.exists():raise RuntimeError(f'Refusing to replace delivery {p}')
    baseline=json.loads((OUT/'RESTORE_BASELINE.json').read_text())
    altered=[];protected=0
    for row in baseline['files']:
        rel=row['path']
        if rel.startswith('.git/'):continue
        p=ROOT/rel
        same=p.is_file() and sha(p)==row['sha256']
        if not same:altered.append(rel)
        elif rel not in ALLOWED_CHANGED:protected+=1
    assert set(altered)<=ALLOWED_CHANGED,altered
    assert sha(Path('/mnt/data/HoTT.json'))==sha(ROOT/'HoTT/sources/external-audits/HoTT.json')=='25eb28f4dbcdf09cf5ebd4eb8722acc97715707b0e21c61015e265b36b182bba'
    assert sha(Path(baseline['zip']))==baseline['sha256']
    state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    assert state['revision']==18
    assert not git('remote')
    input_head=git('rev-parse','HEAD')
    assert input_head=='f38a2cbdee1ef9208f9ed87609a22edc0ed44aa5',input_head
    audit={'schema_version':'hott-r018-protection/v1','status':'PASS_BYTE_SCOPE','protected_prior_non_git_files':protected,'changed_existing_files':altered,'only_authorized_state_and_index_changed':True,
      'source_json_sha256':sha(ROOT/'HoTT/sources/external-audits/HoTT.json'),'original_input_and_original_zip_unchanged':True,'native_lean':'NOT_RUN_UNAVAILABLE','simulator_diagnostic_tests':10,'math_kernel_verified':False,'full_business_cognition_verified':False,
      'old_owners_skills_closure_schema_matrix_and_session_proofs_unchanged':True,'pre_commit_head':input_head}
    write_json(OUT/'INPUT_PROTECTION.json',audit)
    (OUT/'DELIVERY.md').write_text('''# R018 附件审计交付

本轮核查HoTT.json的公开论断与代码，原文完整保存在HoTT/sources/external-audits/HoTT.json；公开投影与逐字源码在artifacts/r018和scripts/recovered/HoTT_json。

主报告REVIEW.md。Python复现及10诊断测试为实际执行；原稿没有Lean执行，新写Lean反证源码也未编译。源头存在性、proof irrelevance和计算语义边界以纸笔推导/一手规则核对，不冒报机器证明。

用户两方向目标的原话已存档并进入动态恢复；哲学owner/Skills未改。五文件checkpoint revision18已提交，旧快照写回拒绝。所有新增程序先落盘scripts再路径运行。

完整ZIP含继承的.git；另提供bundle。Git和字节校验不认证数学或完整认知。最终HEAD在实际Git和包外验证JSON中，不用循环自身hash伪造。
''')
    git('add','-A')
    git('commit','-m','Audit external HoTT dialogue: existence premises, Lean Eq mismatch and simulator scope')
    head=git('rev-parse','HEAD')
    assert git('status','--porcelain')==''
    fsck=git('fsck','--full')
    git('bundle','create',str(BUNDLE),'--all')
    git('bundle','verify',str(BUNDLE))
    file_rows=[]
    with zipfile.ZipFile(ZIP,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_symlink():raise RuntimeError('Refusing symlink '+str(p))
            if p.is_file():
                rel=p.relative_to(ROOT).as_posix()
                z.write(p,ROOT.name+'/'+rel)
                file_rows.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
    with zipfile.ZipFile(ZIP) as z:
        assert z.testzip() is None
        for row in file_rows:
            b=z.read(ROOT.name+'/'+row['path'])
            assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
        with tempfile.TemporaryDirectory(prefix='hott-r018-delivery-') as tmp:
            base=Path(tmp)
            for i in z.infolist():
                p=base/i.filename
                assert p.resolve().is_relative_to(base.resolve())
                p.parent.mkdir(parents=True,exist_ok=True)
                p.write_bytes(z.read(i))
                mode=stat.S_IMODE(i.external_attr>>16)
                if mode:p.chmod(mode)
            restored=base/ROOT.name
            assert git('rev-parse','HEAD',cwd=restored)==head
            assert git('status','--porcelain',cwd=restored)==''
            git('fsck','--full',cwd=restored)
            clone=base/'bundle-clone'
            run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false','clone',str(BUNDLE),str(clone)],cwd=base)
            assert git('rev-parse','HEAD',cwd=clone)==head
            assert git('status','--porcelain',cwd=clone)==''
    count=int(git('rev-list','--count','HEAD'))
    receipt={'schema_version':'hott-r018-delivery/v1','status':'VERIFIED_LOCAL_DELIVERY','root':str(ROOT),'checkpoint_revision':18,
      'branch':git('branch','--show-current'),'head':head,'inherited_head':input_head,'commit_count':count,'remote_count':0,'clean':True,'fsck':'PASS',
      'zip':{'path':str(ZIP),'bytes':ZIP.stat().st_size,'sha256':sha(ZIP),'file_count':len(file_rows),'all_members_read_back':True,'restored_git_clean':True},
      'bundle':{'path':str(BUNDLE),'bytes':BUNDLE.stat().st_size,'sha256':sha(BUNDLE),'verify':'PASS','clone_matches_head':True},
      'protection':audit,'commands':LOG,'limits':['No native Lean compilation','No independent mathematical certification','No claim of complete business cognition loading','External referenced Drive document not embedded or fetched']}
    write_json(RECEIPT,receipt)
    ZIP.with_suffix(ZIP.suffix+'.sha256').write_text(sha(ZIP)+'  '+ZIP.name+'\n')
    print(json.dumps({k:receipt[k] for k in ('status','root','checkpoint_revision','branch','head','commit_count','clean','zip','bundle')},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
