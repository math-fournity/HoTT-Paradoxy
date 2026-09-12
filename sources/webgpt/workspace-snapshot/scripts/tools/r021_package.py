#!/usr/bin/env python3
"""Commit and verify the R021 source-synthesis workspace and portable deliveries.
No remote, peer AI, mathematics experiment or proof assistant is invoked.
"""
from pathlib import Path, PurePosixPath
import ast, datetime, hashlib, json, os, stat, subprocess, tempfile, zipfile

R=Path(__file__).resolve().parents[2]; O=R/'artifacts/r021'; D=R/'.codex/research/hott/dialogues/GEMINI-001'
N=D/'rounds/002'; C=R/'.codex/research/hott/candidates/RP-B01'
BASE='3e529cd4ea00124347afa1195aaa3ccc1619b46e'
SID='S-DISC-20260911-021-GEMINI-SYNTHESIS'
ZIP=R.parent/'HoTT_Gemini_synthesis_rev21_with_git.zip'
BUNDLE=R.parent/'HoTT_Gemini_synthesis_rev21.bundle'
PACK=R.parent/'HoTT_Gemini_two_round_synthesis.zip'
RECEIPT=R.parent/'HoTT_Gemini_synthesis_rev21_delivery_verification.json'
LOG=[]

def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def write_new(p,value):
    if p.exists():raise RuntimeError('Existing output, refuse overwrite '+str(p))
    p.parent.mkdir(parents=True,exist_ok=True)
    if isinstance(value,str):p.write_text(value,encoding='utf-8')
    else:p.write_text(json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
def run(args,cwd=R,timeout=90):
    args=list(map(str,args));start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.run(args,cwd=cwd,text=True,capture_output=True,timeout=timeout,
                     env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
    LOG.append({'argv':args,'cwd':str(cwd),'started_at_utc':start,'exit_code':p.returncode,
                'stdout':p.stdout,'stderr':p.stderr})
    if p.returncode:raise RuntimeError(str(args)+'\n'+p.stdout+'\n'+p.stderr)
    return p.stdout.strip()
def git(*args,cwd=R):
    return run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd)
def main():
    if any(p.exists() for p in [ZIP,BUNDLE,PACK,RECEIPT]):raise RuntimeError('Delivery already exists')
    assert git('rev-parse','HEAD')==BASE
    assert git('remote')==''
    checks=json.loads((O/'FILE_CHECKS_FINAL.json').read_text())
    assert checks['passed']==31 and checks['total']==32
    assert not any(x['status']=='FAIL' for x in checks['checks'])
    summary=json.loads((O/'CHECKPOINT_SUMMARY.json').read_text())
    assert summary['status']=='CHECKPOINT_COMMITTED' and summary['revision']==21
    old_rows=[x for x in json.loads((O/'BASELINE_FILES.json').read_text()) if not x['path'].startswith('.git/')]
    allowed={x['path'] for x in json.loads((O/'INTEGRATION.json').read_text())['changes']}
    allowed|={'MEMORY.md','.codex/cognition/HEAD.json'}
    allowed|={'.codex/research/hott/'+n for n in ['STATE.json','FRONTIER.md','LESSONS.md','RESUME.md']}
    changed=[]
    for row in old_rows:
        p=R/row['path']
        if not p.is_file() or sha(p)!=row['sha256']:changed.append(row['path'])
    assert set(changed)<=allowed,changed
    assert sha(D/'000_SOURCE.md')=='f52053118aa4b3e6a6a6f15c69458037eabffdb8ae8d62f8f45dd6888485b87e'
    assert sha(D/'TO_GEMINI_001.md')=='de5e72847a80ccfd53027f8eed2eeb547d8b7265c05dedd935bc0dad0196b57b'
    for f in (R/'scripts').rglob('r021_*.py'):ast.parse(f.read_text())
    protection={'schema_version':'hott-r021-input-protection/v1','status':'PASS_NON_GIT_BYTE_SCOPE',
        'baseline_git_head':BASE,'base_non_git_files':len(old_rows),
        'unchanged_old_files':len(old_rows)-len(changed),'changed_existing_paths':sorted(changed),
        'fifth_closure_schema_matrix_old_math_old_sources_unchanged':True,
        'governance_runtime_and_full_load_policy_unchanged':True,
        'warning':'Inherited Three Questions reference to sources/aistudio-discussions/README.md is absent in supplied baseline and remains unavailable; no dummy file created.',
        'legacy_manifests':'Old top-level manifests and .codex/SHA256SUMS retained as historical delivery evidence, not reused to certify current tree.'}
    write_new(O/'INPUT_PROTECTION.json',protection)
    report=f'''# R021 · 两轮Gemini综合、研究计划与治理回写

## 实际任务与完成范围

用户已转回IN-002，并说明当前没有Gemini配额。本轮独立综合两次真实意见，不等待、不模拟第三封信，不直接调用外部AI。第一轮意见、OUT-001及原裁决完整保留；新来信按可见用户消息手工转录后精确切片，原错误不修进原文。

原IN-001来源全文25,727字节；IN-002正文{(N/'IN-002.md').stat().st_size}字节。当前用户全文、配额/落盘指令、原文身份记录均在rounds/002。转录不是独立平台原始字节导出或外部模型认证。

## 实质吸收

保留双向目标，分别交付理论选择、局部边界、目标实例。不以完整实例仍开放否定已有局部成果，也不把一般no-go包装为最终悖论。研究可自行构造自然理论解释；库的真实接口审查是互补路径，不是必须先找软件bug。

新来信仍需修正：唯一选择能在真实存在与命题条件下提取数据；transport共轭仅属End族且命题计算不等于归约；χ与对角线要统一二元Code接口及有效通用模型；这段论证不认证绝对一致性；未发现某个越界不能推出所有系统完整隔离。语法出现LEM、noncomputable标签与数学函数不可计算分别判断。

RP-B01已保存PLAN、CONSTRUCTION、CLAIMS：下一动作WP1固定Code模型、有限T及有效h→D_h，再处理分类与Rep的分离及具体规范到执行路径。核心是经典机制，尚无新的原生形式化、数学模拟或独立审查。

## 当前文档与版本

实际更新根AGENTS、Z目标owner、三问v5、业务Skill v1.3.3及其manifest、讨论README/ledger、scripts索引。改前原字节在.codex/history/r021-before及Git中。未另建治理Skill、未改加载策略。

MEMORY、FRONTIER、LESSONS、RESUME、STATE和不可覆盖Session由原checkpoint引擎同步到revision21，最新记录{SID}。新来源、评估与计划实际进入动态全文集合（{summary['dynamic_documents']}份）。旧record没有删除、旧数学状态未升级。

第五闭包、原用户来源、Theory Schema、数学主张矩阵、旧形式化源码、旧sessions、旧实验与治理引擎字节保持。

## 真实检查与错误记录

{checks['passed']}项机械检查通过，1项明确警告：旧三问已有的讨论源README在提供的基线中缺失，本轮没有伪造它。检查包括原文切片、历史保护、版本manifest、新内部链接、动态路由、旧快照拒绝；不是模型理解或数学证明测试。

首次checkpoint dry-run错误将Session标成session_record，管理器要求session，故拒绝LATEST_SESSION_MISSING。STATE未变，失败脚本/载荷/输出保留；改正载荷后原引擎成功提交，STALE_BASE实际拒绝旧快照。

首次文件检查误将git index缓存变化当源码变更，且发现旧断链。修订检查范围：Git用真实history/fsck/clean核查；历史缺件继续警告，不能一律放行。首版失败报告保留。

本輪通过web读取一手条款，但容器下载HTML因DNS失败；保留错误，未声称成功存档全文网页。固定本地书式源码及摘录真实存在。

## 认知和研究边界

这是用户授权的有界来源综合、计划与相关owner维护。完整业务认知gate未通过/未认证，不声称将全部动态历史及第五闭包全文重新载入。没有用文件读取收据、测试数、Git或双方同意补出认知/内核PASS。

没有Lean/Agda/Rocq执行、数学实验、外部AI通信、远端push或已确认新HoTT悖论。已有会话提及的revision24资产不在本谱系，不虚构恢复。

## 阅读入口

- [本轮综合](../../.codex/research/hott/dialogues/GEMINI-001/rounds/002/SYNTHESIS.md)
- [逐项裁决](../../.codex/research/hott/dialogues/GEMINI-001/rounds/002/ASSESSMENT.md)
- [实际回复](../../.codex/research/hott/dialogues/GEMINI-001/rounds/002/IN-002.md)
- [行动方案](../../.codex/research/hott/candidates/RP-B01/PLAN.md)
- [修订后的构造](../../.codex/research/hott/candidates/RP-B01/CONSTRUCTION.md)
- [当前记忆](../../MEMORY.md)
- [文件检查](FILE_CHECKS_FINAL.json)

最终Git HEAD、ZIP逐字节回读、异目录恢复与bundle克隆验证记录在包外delivery_verification.json；不在提交后改工作树以塞入自引用提交哈希。
'''
    write_new(O/'REPORT.md',report)
    git('add','-A')
    git('commit','-m','Integrate two Gemini replies, repair classification contract and persist autonomous HoTT plan')
    head=git('rev-parse','HEAD')
    assert git('status','--porcelain')==''
    git('merge-base','--is-ancestor',BASE,'HEAD')
    git('fsck','--full')
    git('bundle','create',BUNDLE,'--all');git('bundle','verify',BUNDLE)
    # Portable focused source/analysis pack, preserving project-relative paths.
    focus=list(p for p in D.rglob('*') if p.is_file())+list(p for p in C.rglob('*') if p.is_file())
    focus += [O/n for n in ['REPORT.md','SOURCE_EXCERPTS.md','SOURCE_IDENTITIES.json',
                           'FILE_CHECKS_FINAL.json','CHECKPOINT_SUMMARY.json','INPUT_PROTECTION.json']]
    focus += [R/n for n in ['AGENTS.md','MEMORY.md','HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md',
                           '.codex/skills/hott-paradox-research/SKILL.md']]
    focus=sorted(set(focus));focus_rows=[]
    with zipfile.ZipFile(PACK,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in focus:
            name=p.relative_to(R).as_posix();z.write(p,name)
            focus_rows.append({'path':name,'bytes':p.stat().st_size,'sha256':sha(p)})
        z.writestr('R021_FOCUSED_MANIFEST.json',json.dumps({'kind':'source-and-synthesis-subset-not-full-project',
            'revision':21,'reply_received':True,'not_waiting_for_peer':True,
            'native_proof_run':False,'files':focus_rows},ensure_ascii=False,indent=2)+'\n')
    with zipfile.ZipFile(PACK) as z:
        assert z.testzip() is None
        for row in focus_rows:
            b=z.read(row['path']);assert len(b)==row['bytes'] and sha_bytes(b)==row['sha256']
    rows=[]
    with zipfile.ZipFile(ZIP,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(R.rglob('*')):
            if p.is_symlink():raise RuntimeError('Unexpected symlink '+str(p))
            if p.is_file():
                name=p.relative_to(R).as_posix();z.write(p,R.name+'/'+name)
                rows.append({'path':name,'bytes':p.stat().st_size,'sha256':sha(p)})
    with zipfile.ZipFile(ZIP) as z:
        assert z.testzip() is None
        for row in rows:
            b=z.read(R.name+'/'+row['path'])
            assert len(b)==row['bytes'] and sha_bytes(b)==row['sha256']
        with tempfile.TemporaryDirectory(prefix='hott-r021-delivery-') as td:
            dest=Path(td)
            for info in z.infolist():
                parts=PurePosixPath(info.filename)
                assert not parts.is_absolute() and '..' not in parts.parts
                p=dest.joinpath(*parts.parts);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(info))
                mode=stat.S_IMODE(info.external_attr>>16)
                if mode:p.chmod(mode)
            restored=dest/R.name
            assert git('rev-parse','HEAD',cwd=restored)==head
            assert git('status','--porcelain',cwd=restored)==''
            git('fsck','--full',cwd=restored)
            # Actual new process checks current state using a saved project script.
            fresh=json.loads(run([sys.executable,'-B',str(restored/'scripts/session/r021_check_plan.py')],restored))
            assert fresh['revision']==21 and fresh['latest_session']==SID
            assert fresh['required_new_sources_present']
            clone=dest/'bundle-clone'
            run(['git','-c','core.hooksPath=/dev/null','clone',str(BUNDLE),str(clone)],dest)
            assert git('rev-parse','HEAD',cwd=clone)==head and git('status','--porcelain',cwd=clone)==''
    # Git status may refresh index stat data after ZIP creation: compare tracked
    # tree and object integrity, not .git/index cached timestamps.
    assert git('status','--porcelain')=='' and git('remote')==''
    receipt={'schema_version':'hott-r021-delivery/v1','status':'VERIFIED_LOCAL_DELIVERY_WITH_RECORDED_SOURCE_WARNING',
        'completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'workspace':str(R),'revision':21,'latest_session':SID,
        'git':{'head':head,'inherited_head':BASE,'branch':git('branch','--show-current'),
               'commit_count':int(git('rev-list','--count','HEAD')),'clean':True,'fsck':'PASS','remotes':[]},
        'zip':{'path':str(ZIP),'bytes':ZIP.stat().st_size,'sha256':sha(ZIP),'files':len(rows),
               'crc':'PASS','all_member_bytes_verified':True,'restored_git_clean':True},
        'bundle':{'path':str(BUNDLE),'bytes':BUNDLE.stat().st_size,'sha256':sha(BUNDLE),
                  'verify':'PASS','clone_same_head':True},
        'focused_pack':{'path':str(PACK),'bytes':PACK.stat().st_size,'sha256':sha(PACK),
                        'files':len(focus_rows)+1,'readback':'PASS'},
        'fresh_restored_plan':fresh,
        'scope':{'source1_bytes':(D/'000_SOURCE.md').stat().st_size,'source2_bytes':(N/'IN-002.md').stat().st_size,
                 'file_checks_pass':31,'file_checks_warning':1,'new_mathematical_experiments':0,
                 'native_proof_runs':0,'peer_contacted':False,'full_business_cognition':'NOT_CLAIMED',
                 'business_skill_version':'1.3.3','three_questions_version':'v5'},
        'input_protection':protection,'commands':LOG,
        'limits':['One inherited missing reference remains; no source contents fabricated.',
                  'Web tool reads are not container HTML downloads; failed downloads recorded.',
                  'Initial checkpoint payload-kind error and verifier scope failures preserved.',
                  'Original relayed text manually transcribed, not authenticated external model export.',
                  'No absolute theory consistency, originality or new HoTT paradox certified.',
                  'Old manifest snapshots are historical; this external receipt certifies current delivery.']}
    write_new(RECEIPT,receipt)
    for p in [ZIP,BUNDLE,PACK]:write_new(p.with_name(p.name+'.sha256'),sha(p)+'  '+p.name+'\n')
    print(json.dumps({'status':receipt['status'],'head':head,'revision':21,'git_clean':True,
                     'commits':receipt['git']['commit_count'],'zip':receipt['zip'],
                     'focused_pack':receipt['focused_pack'],'bundle':receipt['bundle'],
                     'fresh_restored_plan':fresh},ensure_ascii=False,indent=2))

if __name__=='__main__':
    import sys
    main()
