#!/usr/bin/env python3
"""Verify correspondence/state, commit locally, and package reproducible history.
This is document/integrity verification, not mathematical or peer review.
"""
from pathlib import Path
from urllib.parse import urlsplit
import ast, datetime, hashlib, json, os, re, subprocess, tempfile, zipfile
R=Path(__file__).resolve().parents[2]
O=R/'artifacts/r022'
D='.codex/research/hott/dialogues/GEMINI-001/'
N=D+'rounds/003/'
BASE='8e6641dd9b229e39875017e6a56732c2b8019af3'
OUTZIP=R.parent/'HoTT_Gemini_reply_rev22_with_git.zip'
BUNDLE=R.parent/'HoTT_Gemini_reply_rev22.bundle'
PACK=R.parent/'Gemini_HoTT_debate_002.zip'
RECEIPT=R.parent/'HoTT_Gemini_reply_rev22_delivery_verification.json'
LOG=[]
CHECKS=[]

def sha(b):return hashlib.sha256(b).hexdigest()
def dump(o):return json.dumps(o,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
def put(p,o):
    if p.exists():raise RuntimeError('Refuse overwrite: '+str(p))
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(o if isinstance(o,str) else dump(o),encoding='utf-8')
def run(args,cwd=R,timeout=90):
    start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    p=subprocess.run(list(map(str,args)),cwd=cwd,capture_output=True,text=True,timeout=timeout,
      env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',GIT_TERMINAL_PROMPT='0'))
    LOG.append({'argv':list(map(str,args)),'cwd':str(cwd),'started_utc':start,
      'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    if p.returncode:raise RuntimeError(str(args)+'\n'+p.stdout+'\n'+p.stderr)
    return p.stdout.strip()
def git(*args,cwd=R):return run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd)
def check(name,cond,detail=None):
    CHECKS.append({'id':name,'status':'PASS' if cond else 'FAIL','detail':detail})
    if not cond:raise AssertionError(name)

def main():
    if any(p.exists() for p in [OUTZIP,BUNDLE,PACK,RECEIPT]):raise RuntimeError('Delivery exists')
    check('inherited_git_head',git('rev-parse','HEAD')==BASE)
    check('no_remote',git('remote')=='')
    md=(R/(D+'TO_GEMINI_002.md')).read_bytes();text=md.decode('utf-8')
    check('letter_utf8_nonempty',len(md)>10000 and '\x00' not in text)
    check('txt_same_bytes',(R/(D+'TO_GEMINI_002.txt')).read_bytes()==md)
    check('math_delimiters',text.count('\\[')==text.count('\\]') and text.count('\\(')==text.count('\\)'))
    check('six_original_topics',all(f'G{i:02d}' in text for i in range(1,7)))
    check('six_new_questions',all(f'H{i:02d}' in text for i in range(1,7)))
    check('standalone_sources',all(f'**[S{i}]' in text for i in range(1,7)))
    ledger=json.loads((R/(D+'DEBATE_LEDGER.json')).read_text())
    outgoing=next(x for x in ledger['outgoing'] if x['id']=='OUT-002')
    check('not_sent_not_received',not outgoing['sent'] and not outgoing['reply_received'] and len(ledger['incoming'])==2)
    check('outgoing_hash',outgoing['sha256']==sha(md))
    check('no_peer_gate',ledger['workflow']['awaiting_peer_to_start_research'] is False)
    summary=json.loads((O/'CHECKPOINT_SUMMARY.json').read_text())
    check('checkpoint_committed',summary['status']=='CHECKPOINT_COMMITTED' and summary['revision']==22)
    check('stale_base_rejected',summary['stale_base_rejected'])
    fresh=json.loads(run([sys_executable(),'-B',R/'scripts/session/r022_plan_check.py']))
    put(O/'FRESH_PLAN_CHECK.json',fresh)
    check('fresh_process_routes_letter',fresh['letter_in_route'] and fresh['revision']==22)
    # Add the two actually used correction/probe scripts to the script index before final commit.
    index=R/'scripts/README.md'
    index.write_text(index.read_text()+
      '\nR022补充工具：`scripts/session/r022_checkpoint_retry.py` 修正被拒载荷的kind与待复核状态，保留失败日志；`r022_plan_check.py` 在新进程只读验证当前路由。\n',encoding='utf-8')
    allow={D+'DEBATE_LEDGER.json',D+'README.md','scripts/README.md','MEMORY.md',
      '.codex/cognition/HEAD.json',*[ '.codex/research/hott/'+x for x in ['STATE.json','FRONTIER.md','LESSONS.md','RESUME.md']]}
    changed=[];violations=[];count=0
    for row in json.loads((O/'RESTORE.json').read_text())['files']:
        rel=row['path']
        if rel.startswith('.git/'):continue
        count+=1;p=R/rel
        if not p.is_file() or sha(p.read_bytes())!=row['sha256']:
            changed.append(rel)
            if rel not in allow:violations.append(rel)
    check('baseline_protection',not violations,{'baseline_files':count,'allowed_changed':changed,'unexpected':violations})
    parsed=[]
    for p in sorted((R/'scripts').rglob('r022_*.py')):
        ast.parse(p.read_text(encoding='utf-8'));parsed.append(str(p.relative_to(R)))
    check('new_scripts_parse',len(parsed)==6,parsed)
    for p in (O.rglob('*.json')):json.loads(p.read_text())
    check('new_json_parse',True)
    broken=[]
    for p in [R/(D+'README.md'),R/(D+'TO_GEMINI_002.md')]:
        for url in re.findall(r'\[[^\]\n]+\]\(([^)\n]+)\)',p.read_text()):
            if urlsplit(url).scheme or url.startswith('#'):continue
            if not (p.parent/url.split('#')[0]).exists():broken.append([str(p),url])
    check('local_links_exist',not broken,broken)
    report='''# R022 第二封完整回信：交付报告

## 交付与来源

已写OUT-002，回应真实收到的IN-002，覆盖G01—G06并提出H01—H06。MD/TXT逐字节一致；信自带问题定义、模型前提、正例、待审构造和一手参考，不需要接收者访问本地目录。

第五节的代码分配/可实现性说明是供反驳的进一步提案，不是新机器证明。旧原文、OUT-001、两轮评估、RP-B01原PLAN/CONSTRUCTION、第五闭包、三问、AGENTS、Skills、Schema、主张矩阵、旧研究与源码均保持原字节。

## 状态

尚未直接发送、没有第三轮来信，没有启动Gemini或其他AI。待用户转发不成为继续研究前提。已用原治理器checkpoint到revision22，最新Session为S-DISC-20260911-022-GEMINI-OUT002；新进程确认信件与最新MEMORY进入动态集合。

本轮没有认证完整第五闭包/动态全集认知加载；任务为有界来信回应与文档交接，未更改全文要求。继承README的旧revision13状态段落没有用于覆盖当前STATE，记录其不同步，不扩展成本轮全仓改造。

## 真实故障与修复

首次准备脚本因文稿未实际落盘而FileNotFoundError，补存全文后重试成功。首次checkpoint dry-run因kind=session_record而LATEST_SESSION_MISSING；与上轮同类错误重复。修正为引擎所需session，并令依赖待核记录的新信件也review_required。旧失败源码、载荷与执行日志保存；未改引擎或伪称一遍成功。

## 验证边界

本轮只验证文件、引用、发送状态、脚本语法、版本/动态路由、原件保护、Git与包回读；不是HoTT内核、数学实验、独立专家或新AI理解验收。机械检查明细见FILE_CHECKS.json，执行范围见READ_SCOPE.json。完整Git提交哈希与打包后检查放在包外delivery_verification，避免自引用。
'''
    put(O/'REPORT.md',report)
    put(O/'FILE_CHECKS.json',{'scope':'FILES_STATE_ONLY_NOT_MATH','passed':len(CHECKS),'checks':CHECKS})
    put(O/'PRECOMMIT_COMMANDS.json',LOG.copy())
    git('add','--all')
    git('commit','-m','docs: reply to Gemini IN-002 and preserve OUT-002 with research questions')
    head=git('rev-parse','HEAD')
    assert git('status','--porcelain')==''
    git('fsck','--full')
    git('bundle','create',BUNDLE,'--all')
    git('bundle','verify',BUNDLE)
    files=[p for p in sorted(R.rglob('*')) if p.is_file()]
    with zipfile.ZipFile(OUTZIP,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files:z.write(p,R.name+'/'+p.relative_to(R).as_posix())
    with zipfile.ZipFile(OUTZIP) as z:
        assert z.testzip() is None
        for p in files:assert z.read(R.name+'/'+p.relative_to(R).as_posix())==p.read_bytes()
    # Small peer packet includes only the discussion context, not the whole governance corpus.
    peer={
      'TO_GEMINI_002.md':D+'TO_GEMINI_002.md','TO_GEMINI_002.txt':D+'TO_GEMINI_002.txt',
      'RELAY_NOTE.txt':N+'RELAY_NOTE.txt','IN-002.md':D+'rounds/002/IN-002.md',
      'TO_GEMINI_001.md':D+'TO_GEMINI_001.md','IN-001.md':D+'005_GEMINI_ORIGINAL.md',
      'R021_ASSESSMENT.md':D+'rounds/002/ASSESSMENT.md','R021_SYNTHESIS.md':D+'rounds/002/SYNTHESIS.md',
      'RP-B01_PLAN.md':'.codex/research/hott/candidates/RP-B01/PLAN.md',
      'RP-B01_CONSTRUCTION.md':'.codex/research/hott/candidates/RP-B01/CONSTRUCTION.md',
      'RESPONSE_MAP.json':N+'RESPONSE_MAP.json','SOURCES.md':N+'SOURCES.md'}
    packet_readme='先读TO_GEMINI_002.md（或同文TXT），优先回答H03/H04/H05。其余为历史与研究上下文，不是独立论文或已完成机器证明。本包尚未直接发送，没有新回信。文档中的项目相对链接仅为原档案来源，完整正文以本包所列文件为准。\n'
    packet_manifest={'scope':'OUT-002 forwarding packet; not a full workspace','files':[]}
    with zipfile.ZipFile(PACK,'w',zipfile.ZIP_DEFLATED) as z:
        z.writestr('README.txt',packet_readme)
        packet_manifest['files'].append({'path':'README.txt','sha256':sha(packet_readme.encode())})
        for name,rel in peer.items():
            data=(R/rel).read_bytes();z.writestr(name,data)
            packet_manifest['files'].append({'path':name,'sha256':sha(data),'bytes':len(data)})
        z.writestr('MANIFEST.json',dump(packet_manifest))
    with zipfile.ZipFile(PACK) as z:
        assert z.testzip() is None
        for row in packet_manifest['files']:assert sha(z.read(row['path']))==row['sha256']
    with tempfile.TemporaryDirectory(prefix='hott-r022-restore-') as temp:
        tmp=Path(temp)
        with zipfile.ZipFile(OUTZIP) as z:z.extractall(tmp)
        extracted=tmp/R.name
        assert git('rev-parse','HEAD',cwd=extracted)==head
        assert git('status','--porcelain',cwd=extracted)==''
        fresh_copy=json.loads(run([sys_executable(),'-B',extracted/'scripts/session/r022_plan_check.py'],cwd=tmp))
        assert fresh_copy['snapshot']==fresh['snapshot']
        clone=tmp/'from-bundle'
        run(['git','-c','core.hooksPath=/dev/null','clone',str(BUNDLE),str(clone)],cwd=tmp)
        assert git('rev-parse','HEAD',cwd=clone)==head
        assert git('status','--porcelain',cwd=clone)==''
    outputs=[]
    for p in [OUTZIP,BUNDLE,PACK]:
        digest=sha(p.read_bytes())
        p.with_name(p.name+'.sha256').write_text(digest+'  '+p.name+'\n')
        outputs.append({'path':str(p),'bytes':p.stat().st_size,'sha256':digest})
    receipt={'status':'VERIFIED_FILES_AND_GIT','root':str(R),'head':head,
      'inherited_head':BASE,'revision':22,'branch':git('branch','--show-current'),
      'working_tree_clean':git('status','--porcelain')=='','git_fsck':'PASS',
      'zip_readback':'ALL_FILES_IDENTICAL','restored_git_clean':True,'bundle_clone_matches':True,
      'relocated_plan_same_snapshot':True,'letter_sha256':sha(md),'letter_bytes':len(md),
      'file_checks':len(CHECKS),'workspace_files_including_git':len(files),
      'outgoing_status':'READY_FOR_USER_RELAY_NOT_SENT','new_peer_reply':False,
      'new_mathematical_kernel_proof':False,'full_business_cognition':'NOT_CLAIMED',
      'outputs':outputs,'commands':LOG,'notes':['No external send','No remote push','Two rejected preliminary runs preserved, then corrected','Known earlier source gaps retained; no silent full-corpus certification']}
    put(RECEIPT,receipt)
    print(dump({'head':head,'revision':22,'letter_bytes':len(md),'checks':len(CHECKS),
      'outputs':outputs,'delivery_verification':str(RECEIPT)}))

def sys_executable():
    import sys
    return sys.executable

if __name__=='__main__':
    try:main()
    except Exception as exc:
        p=R.parent/'HoTT_Gemini_reply_rev22_packaging_failure.json'
        if not p.exists():p.write_text(dump({'error':str(exc),'type':type(exc).__name__,'commands':LOG,'checks':CHECKS}))
        raise
