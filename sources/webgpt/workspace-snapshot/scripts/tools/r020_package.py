#!/usr/bin/env python3
"""Protect prior inputs; commit R020 locally; verify full Git delivery and relay pack.
No remote connection, external AI, imported attachment code, or math solver.
"""
from pathlib import Path, PurePosixPath
import ast, datetime, hashlib, json, os, stat, subprocess, tempfile, zipfile
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'artifacts/r020'
BASE_ZIP=Path('/mnt/data/HoTT2_audit_rev19_with_git.zip'); PREFIX='HoTT2_audit_rev19/'
BASE_HEAD='44ba9f3e0527b9e036dd6c9d8ab3e650e89c910a'
ZIP=ROOT.parent/'HoTT_Gemini_debate_rev20_with_git.zip'
BUNDLE=ROOT.parent/'HoTT_Gemini_debate_rev20.bundle'
RECEIPT=ROOT.parent/'HoTT_Gemini_debate_rev20_delivery_verification.json'
RELAY=ROOT.parent/'Gemini_HoTT_debate_001.zip'
D=ROOT/'.codex/research/hott/dialogues/GEMINI-001'
SID='S-DISC-20260911-020-GEMINI-DEBATE-FINAL'
ALLOWED={'MEMORY.md','scripts/README.md','.codex/cognition/HEAD.json','.codex/research/hott/STATE.json','.codex/research/hott/FRONTIER.md','.codex/research/hott/LESSONS.md','.codex/research/hott/RESUME.md'}
LOG=[]
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def write_json(path,value):
    if path.exists():raise RuntimeError('Refuse overwrite '+str(path))
    path.write_text(json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
def run(argv,cwd=ROOT,timeout=90):
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    proc=subprocess.run(list(map(str,argv)),cwd=cwd,text=True,capture_output=True,timeout=timeout)
    LOG.append({'argv':list(map(str,argv)),'cwd':str(cwd),'started_at_utc':started,'exit_code':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr})
    if proc.returncode:raise RuntimeError(str(argv)+'\n'+proc.stderr)
    return proc.stdout.strip()
def git(*args,cwd=ROOT):return run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd)
def main():
    if any(x.exists() for x in (ZIP,BUNDLE,RECEIPT,RELAY)):raise RuntimeError('Existing delivery, refusing overwrite')
    assert git('rev-parse','HEAD')==BASE_HEAD
    assert git('remote')==''
    changed=[];protected=0;base_count=0
    with zipfile.ZipFile(BASE_ZIP) as z:
        for info in z.infolist():
            if info.is_dir():continue
            if not info.filename.startswith(PREFIX):raise RuntimeError('Unexpected base root')
            rel=info.filename[len(PREFIX):]
            if rel.startswith('.git/'):continue
            base_count+=1;p=ROOT/rel;b=z.read(info)
            if not p.is_file() or p.read_bytes()!=b:changed.append(rel)
            elif rel not in ALLOWED:protected+=1
    assert set(changed)<=ALLOWED,changed
    src=D/'000_SOURCE.md';original=Path('/mnt/data/Pasted markdown(1).md')
    assert src.read_bytes()==original.read_bytes()
    assert sha(src)=='f52053118aa4b3e6a6a6f15c69458037eabffdb8ae8d62f8f45dd6888485b87e'
    assert (D/'TO_GEMINI_001.md').read_bytes()==(D/'TO_GEMINI_001.txt').read_bytes()
    ledger=json.loads((D/'DEBATE_LEDGER.json').read_text())
    assert not ledger['outgoing'][0]['sent'] and not ledger['outgoing'][0]['reply_received']
    assert len(ledger['questions'])==6 and all(x['peer_response']=='NOT_RECEIVED' for x in ledger['questions'])
    assert all(x['status']=='PROPOSED_NOT_EXECUTED' for x in ledger['proposed_actions'])
    state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    assert state['revision']==20 and state['latest_session']==SID
    assert state['records']['D-GEMINI-001']['status']=='review_required'
    summary=json.loads((OUT/'RUN_SUMMARY.json').read_text())
    assert summary['stale_base_rejected'] and summary['prior_records_unchanged']
    assert json.loads((OUT/'FILE_CHECKS.json').read_text())['passed']==15
    for f in (ROOT/'scripts/session').glob('r020_*.py'):ast.parse(f.read_text())
    ast.parse(Path(__file__).read_text())
    for f in D.glob('*.json'):json.loads(f.read_text())
    protection={'status':'PASS_BYTE_SCOPE','baseline_zip_sha256':sha(BASE_ZIP),'inherited_head':BASE_HEAD,
                'base_non_git_files':base_count,'protected_old_files_unchanged':protected,
                'changed_existing_paths':changed,'allowed_changes':sorted(ALLOWED),
                'original_input_sha256':sha(src),'canonical_owners_skills_schema_matrix_and_old_research_unchanged':True,
                'limits':'Existing file comparison, not mathematical validation or full cognitive loading.'}
    write_json(OUT/'INPUT_PROTECTION.json',protection)
    (OUT/'DELIVERY.md').write_text('''# R020 · Gemini论辩交付\n\n输入完整保全，五段角色正文逐字切片；有界评估与首封可单独转发的信件。并无本轮Gemini回复、发送动作或机器数学验证。G01—G06保持待对方回答，P01—P03是建议而非成果。\n\n首两次checkpoint dry-run分别被Session登记与依赖复核门禁拒绝，真实错误和准备稿均保留；随后通过新Session身份和正确的待复核状态成功保存revision20，旧快照写回被拒绝。没有修改治理器绕过限制，没有覆盖旧Session。\n\n分析、源文、信件和争议状态已接入动态恢复。原第五闭包、三问、Skills、Schema、主张矩阵与旧研究保持字节不变。只有当前记忆、前沿、接续与脚本索引按授权更新。\n\n源码全部先写scripts再调用。完整ZIP含继承的.git；另有Git bundle和小型转发包。外部delivery_verification.json保存最终HEAD与读回、解压、克隆校验，不在提交后污染工作树。\n\n本包继承提供的revision19而非附件中转述的revision24；没有伪造缺失的后续工作。15项文件检查不等于理解或数学测试。\n''')
    git('add','-A')
    git('commit','-m','Assess relayed Gemini HoTT claims and preserve unsent debate with provenance')
    head=git('rev-parse','HEAD');assert git('status','--porcelain')==''
    git('fsck','--full');git('bundle','create',str(BUNDLE),'--all');git('bundle','verify',str(BUNDLE))
    # Small relay pack: independent letter and all this round's debate documents.
    relay_files=[(p,p.name) for p in sorted(D.iterdir()) if p.is_file()]
    relay_files += [(OUT/n,'evidence/'+n) for n in ('INPUT_MANIFEST.json','SOURCE_EXCERPTS.md','SOURCE_IDENTITIES.json','FILE_CHECKS.json')]
    relay_rows=[]
    with zipfile.ZipFile(RELAY,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p,name in relay_files:
            z.write(p,name);relay_rows.append({'path':name,'bytes':p.stat().st_size,'sha256':sha(p)})
        z.writestr('MANIFEST.json',json.dumps({'kind':'relay_pack','outgoing_status':'DRAFT_READY_NOT_SENT','reply':'NOT_RECEIVED','files':relay_rows},ensure_ascii=False,indent=2)+'\n')
    with zipfile.ZipFile(RELAY) as z:
        assert z.testzip() is None
        for row in relay_rows:
            b=z.read(row['path']);assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
    rows=[]
    with zipfile.ZipFile(ZIP,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_symlink():raise RuntimeError('Unexpected symlink '+str(p))
            if p.is_file():
                rel=p.relative_to(ROOT).as_posix();z.write(p,ROOT.name+'/'+rel)
                rows.append({'path':rel,'bytes':p.stat().st_size,'sha256':sha(p)})
    with zipfile.ZipFile(ZIP) as z:
        assert z.testzip() is None
        for row in rows:
            b=z.read(ROOT.name+'/'+row['path']);assert len(b)==row['bytes'] and hashlib.sha256(b).hexdigest()==row['sha256']
        with tempfile.TemporaryDirectory(prefix='hott-r020-delivery-') as td:
            tmp=Path(td)
            for info in z.infolist():
                rel=PurePosixPath(info.filename)
                assert not rel.is_absolute() and '..' not in rel.parts
                p=tmp.joinpath(*rel.parts);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(info))
                mode=stat.S_IMODE(info.external_attr>>16)
                if mode:p.chmod(mode)
            restored=tmp/ROOT.name
            assert git('rev-parse','HEAD',cwd=restored)==head and git('status','--porcelain',cwd=restored)==''
            git('fsck','--full',cwd=restored)
            clone=tmp/'bundle-clone';run(['git','-c','core.hooksPath=/dev/null','clone',str(BUNDLE),str(clone)],cwd=tmp)
            assert git('rev-parse','HEAD',cwd=clone)==head and git('status','--porcelain',cwd=clone)==''
    receipt={'schema_version':'hott-r020-delivery/v1','status':'VERIFIED_LOCAL_DELIVERY',
             'completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'workspace':str(ROOT),
             'checkpoint_revision':20,'latest_session':SID,
             'git':{'head':head,'inherited_head':BASE_HEAD,'branch':git('branch','--show-current'),'commits':int(git('rev-list','--count','HEAD')),'clean':True,'fsck':'PASS','remotes':[]},
             'zip':{'path':str(ZIP),'bytes':ZIP.stat().st_size,'sha256':sha(ZIP),'files':len(rows),'crc':'PASS','all_members_read_back':True,'restored_git_clean':True},
             'bundle':{'path':str(BUNDLE),'bytes':BUNDLE.stat().st_size,'sha256':sha(BUNDLE),'verified':True,'clone_same_head':True},
             'relay_pack':{'path':str(RELAY),'bytes':RELAY.stat().st_size,'sha256':sha(RELAY),'files':len(relay_rows)+1,'all_members_read_back':True},
             'analysis_scope':{'source_bytes':src.stat().st_size,'speaker_blocks':5,'file_checks':15,'questions':6,'action_proposals':3,'proposals_executed':False,'peer_contacted':False,'new_reply_received':False,'native_proof_assistant_runs':0,'full_business_cognition_gate':'NOT_CLAIMED'},
             'input_protection':protection,'commands':LOG,
             'limits':['Two checkpoint dry-run errors preserved; final transaction succeeded after fixing payload and status, not the governance engine.',
                       'User-relayed model identity not independently certified.',
                       'Quoted rev24 artifacts unavailable in provided revision19 baseline.',
                       'File tests and Git checks certify delivery, not mathematical truth or cognition completeness.']}
    write_json(RECEIPT,receipt)
    for p in (ZIP,BUNDLE,RELAY):p.with_name(p.name+'.sha256').write_text(sha(p)+'  '+p.name+'\n')
    print(json.dumps({'status':receipt['status'],'head':head,'commits':receipt['git']['commits'],'clean':True,'prior_protected_files':protected,'zip':receipt['zip'],'relay_pack':receipt['relay_pack'],'bundle':receipt['bundle']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
