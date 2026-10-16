"""Validate R023 files, preserve inherited Git, and produce checked deliverables."""
from __future__ import annotations
from pathlib import Path
from datetime import datetime,timezone
import ast,hashlib,json,os,re,subprocess,sys,tempfile,zipfile
from urllib.parse import urlsplit
R=Path(__file__).resolve().parents[2]
O=R/'artifacts/r023';D='.codex/research/hott/dialogues/GEMINI-001/';N=D+'rounds/004/'
BASE='d3ce0ec1b91da8f7c39b1252511f580e04b17db5'
ZIP=R.parent/'HoTT_Gemini_response_rev23_with_git.zip'
BUNDLE=R.parent/'HoTT_Gemini_response_rev23.bundle'
PACK=R.parent/'Gemini_HoTT_debate_003.zip'
RECEIPT=R.parent/'HoTT_Gemini_response_rev23_delivery_verification.json'
LOG=[];CHECKS=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(o):return json.dumps(o,ensure_ascii=False,indent=2)+'\n'
def new(p,o):
    if p.exists():raise FileExistsError(str(p))
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(o if isinstance(o,str) else dump(o),encoding='utf-8')
def run(cmd,cwd=R,timeout=90):
    start=datetime.now(timezone.utc).isoformat()
    p=subprocess.run([str(x) for x in cmd],cwd=cwd,capture_output=True,text=True,timeout=timeout,
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',GIT_TERMINAL_PROMPT='0'))
    LOG.append({'argv':[str(x) for x in cmd],'cwd':str(cwd),'at_utc':start,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    if p.returncode:raise RuntimeError(p.stderr or p.stdout)
    return p.stdout.strip()
def git(*args,cwd=R):return run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd)
def check(name,ok,detail=None):
    CHECKS.append({'id':name,'status':'PASS' if ok else 'FAIL','detail':detail})
    if not ok:raise AssertionError(name)

def main():
    for p in (ZIP,BUNDLE,PACK,RECEIPT):
        if p.exists():raise FileExistsError(str(p))
    check('inherited_head',git('rev-parse','HEAD')==BASE)
    check('no_remote',not git('remote'))
    letter=(R/(D+'TO_GEMINI_003.md')).read_bytes();text=letter.decode()
    check('letter_txt_identical',letter==(R/(D+'TO_GEMINI_003.txt')).read_bytes())
    check('letter_all_topics',all(f'H{i:02}' in text for i in range(1,7)))
    check('letter_new_questions',all(f'J{i:02}' in text for i in range(1,6)))
    check('balanced_math',text.count('\\[')==text.count('\\]') and text.count('\\(')==text.count('\\)'))
    incoming=(R/(N+'IN-003.md')).read_bytes()
    prov=json.loads((R/(N+'PROVENANCE.json')).read_text())
    check('incoming_preserved_hash',prov['body_sha256']==sha(incoming))
    check('incoming_all_sections',all(f'### H{i:02}' in incoming.decode() for i in range(1,7)))
    ledger=json.loads((R/(D+'DEBATE_LEDGER.json')).read_text())
    check('three_real_incoming',len(ledger['incoming'])==3 and ledger['received_rounds']==3)
    last=next(x for x in ledger['outgoing'] if x['id']=='OUT-003')
    check('new_letter_unsent',not last['sent'] and not last['reply_received'])
    prev=next(x for x in ledger['outgoing'] if x['id']=='OUT-002')
    check('old_letter_replied',prev['reply_received'] and prev['reply_id']=='IN-003')
    check('letter_hash',last['sha256']==sha(letter))
    check('peer_not_gate',ledger['workflow']['awaiting_peer_to_start_research'] is False)
    cp=json.loads((O/'CHECKPOINT_SUMMARY.json').read_text())
    check('checkpoint23',cp['status']=='CHECKPOINT_COMMITTED' and cp['revision']==23)
    check('stale_base_rejected',json.loads((O/'checkpoint/STALE_BASE.json').read_text())['error']=='STALE_BASE')
    fresh=json.loads(run([sys.executable,'-B',R/'scripts/session/r023_plan_check.py']))
    check('fresh_route',fresh['required_paths_present'])
    new(O/'FRESH_PLAN.json',fresh)
    allowed={'MEMORY.md','scripts/README.md',D+'README.md',D+'DEBATE_LEDGER.json','.codex/cognition/HEAD.json',
      *['.codex/research/hott/'+x for x in ('STATE.json','FRONTIER.md','LESSONS.md','RESUME.md')]}
    changed=[];violations=[];protected=0
    for row in json.loads((O/'RESTORE.json').read_text())['files']:
        rel=row['path']
        if rel.startswith('.git/'):continue
        protected+=1;p=R/rel
        if not p.is_file() or sha(p.read_bytes())!=row['sha256']:
            changed.append(rel)
            if rel not in allowed:violations.append(rel)
    check('old_assets_protected',not violations,{'existing_non_git_files':protected,'changed':changed,'violations':violations})
    parsed=[]
    for p in sorted((R/'scripts').rglob('r023_*.py')):
        ast.parse(p.read_text());parsed.append(p.relative_to(R).as_posix())
    check('new_scripts_parse',len(parsed)==5,parsed)
    for p in list(O.rglob('*.json'))+list((R/N).glob('*.json')):json.loads(p.read_text())
    check('new_json_parse',True)
    broken=[]
    for rel in (D+'README.md',D+'TO_GEMINI_003.md',N+'ASSESSMENT.md'):
        p=R/rel
        for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',p.read_text()):
            if urlsplit(target).scheme or target.startswith('#'):continue
            if not (p.parent/target.split('#')[0]).exists():broken.append([rel,target])
    check('internal_links',not broken,broken)
    report='''# R023 · IN-003评估与OUT-003交付

## 已完成

完整保存用户转述IN-003及请求包装；H01—H06评估、标准源回查、OUT-003/同文TXT、J01—J05和研究调度意见。实际接收与直接发送分开：IN-003已收到，OUT-002由来信表明用户转发；OUT-003未发送，没有IN-004。

核心评估：模型名称不等于形成已完成；k继承LEM而非新有效算法；计算反射不需AllRealizable；圈双覆盖合法但新悖论未立，ua类型与圈回路不同，标准wind/encode-decode存在，Bool任务只读奇偶。有限字与平方圈为纸笔正向控制，不是新内核验收。

## 真实执行与范围

原治理器checkpoint revision22→23成功，旧快照拒绝，新进程加载包含新来信、评估、回信、MEMORY和Session。完整业务认知/第五闭包动态全集本轮没有认证；没有更改其强制全文政策。本轮为用户要求的有界来源回应，不将文书工作升级为自主业务研究完成。

四次远程源码下载因DNS失败，保留所有错误；通过web读官方网页的证据另记，不伪造下载内容或哈希。无Agda/Lean/Rocq可执行工具，未安装、未运行数学模拟器、没有Fresh或独立专家审查。

## 文件与Git

从提供的revision22包恢复并继承其Git；不改原上传目录或原ZIP。全部旧来信、OUT001/002、Skills、第五闭包、三问、Schema、主张矩阵和历史研究保持原字节。仅当前讨论入口/台账、脚本索引、MEMORY和治理工作状态更新；改前内容由备份/事务/Git保存。
所有新增代码先写scripts再调用。最终包包括完整.git并通过异目录解包与bundle克隆检查；具体HEAD及文件哈希在外部delivery_verification，避免自引用。没有远端或push。

本报告的文件检查不是数学正确性证明。数据细项见FILE_CHECKS.json、SOURCE_REGISTRY.json、READ_SCOPE.json、CHECKPOINT_EXECUTION.json。
'''
    new(O/'REPORT.md',report)
    new(O/'FILE_CHECKS.json',{'scope':'FILES_AND_STATE_NOT_MATHEMATICS','passed':len(CHECKS),'checks':CHECKS})
    new(O/'PRECOMMIT_COMMANDS.json',LOG.copy())
    git('add','--all')
    git('commit','-m','Review Gemini IN-003, test winding claims against sources and draft OUT-003')
    head=git('rev-parse','HEAD');check('clean_after_commit',not git('status','--porcelain'))
    git('fsck','--full')
    git('bundle','create',BUNDLE,'--all');git('bundle','verify',BUNDLE)
    # Freeze non-Git bytes first. A later read of Git can update its index metadata;
    # archive and verify after all current-worktree inspection is finished.
    files=[p for p in sorted(R.rglob('*')) if p.is_file()]
    with zipfile.ZipFile(ZIP,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files:z.write(p,R.name+'/'+p.relative_to(R).as_posix())
    with zipfile.ZipFile(ZIP) as z:
        check('zip_crc',z.testzip() is None)
        check('zip_every_file_same',all(z.read(R.name+'/'+p.relative_to(R).as_posix())==p.read_bytes() for p in files))
    packet={
      'TO_GEMINI_003.md':D+'TO_GEMINI_003.md','TO_GEMINI_003.txt':D+'TO_GEMINI_003.txt',
      'IN-003.md':N+'IN-003.md','ASSESSMENT.md':N+'ASSESSMENT.md','SOURCES.md':N+'SOURCES.md',
      'PROVENANCE.json':N+'PROVENANCE.json','RESPONSE_MAP.json':N+'RESPONSE_MAP.json','RELAY_NOTE.txt':N+'RELAY_NOTE.txt',
      'TO_GEMINI_002.md':D+'TO_GEMINI_002.md','RP-B01_PLAN.md':'.codex/research/hott/candidates/RP-B01/PLAN.md',
      'SOURCE_EXCERPTS.md':'artifacts/r023/SOURCE_EXCERPTS.md'}
    manifest=[]
    with zipfile.ZipFile(PACK,'w',zipfile.ZIP_DEFLATED) as z:
        z.writestr('README.txt','先读TO_GEMINI_003.md，优先回应J01—J04。原文与我方评估分开；仅供用户转发，未直接发送，没有IN-004或机器证明。\n')
        for name,rel in packet.items():
            b=(R/rel).read_bytes();z.writestr(name,b);manifest.append({'path':name,'bytes':len(b),'sha256':sha(b)})
        z.writestr('MANIFEST.json',dump({'files':manifest,'scope':'Discussion packet, not a native proof package'}))
    with zipfile.ZipFile(PACK) as z:
        check('packet_readback',z.testzip() is None and all(sha(z.read(x['path']))==x['sha256'] for x in manifest))
    with tempfile.TemporaryDirectory(prefix='hott-r023-verify-') as temp:
        t=Path(temp)
        with zipfile.ZipFile(ZIP) as z:z.extractall(t)
        restored=t/R.name
        check('restored_head',git('rev-parse','HEAD',cwd=restored)==head)
        check('restored_clean',not git('status','--porcelain',cwd=restored))
        cp2=json.loads(run([sys.executable,'-B',restored/'scripts/session/r023_plan_check.py'],cwd=t))
        check('relocated_snapshot',cp2['snapshot']==fresh['snapshot'])
        clone=t/'bundle-clone';run(['git','-c','core.hooksPath=/dev/null','clone',BUNDLE,clone],cwd=t)
        check('bundle_head',git('rev-parse','HEAD',cwd=clone)==head)
        check('bundle_clean',not git('status','--porcelain',cwd=clone))
    outputs=[]
    for p in (ZIP,BUNDLE,PACK):
        digest=sha(p.read_bytes());new(p.with_name(p.name+'.sha256'),digest+'  '+p.name+'\n')
        outputs.append({'path':str(p),'bytes':p.stat().st_size,'sha256':digest})
    new(RECEIPT,{'status':'VERIFIED_FILES_AND_GIT','root':str(R),'revision':23,'head':head,'inherited_head':BASE,
      'letter_bytes':len(letter),'incoming_bytes':len(incoming),'letter_sha256':sha(letter),'files':len(files),
      'checks':CHECKS,'passed':len(CHECKS),'outputs':outputs,'commands':LOG,
      'native_math_proof':'NOT_RUN','full_business_cognition':'NOT_CLAIMED','incoming':'IN-003_RECEIVED',
      'outgoing':'OUT-003_NOT_SENT','old_assets_protected':True})
    print(dump({'head':head,'revision':23,'checks':len(CHECKS),'outputs':outputs,'receipt':str(RECEIPT)}))

if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=R.parent/'HoTT_Gemini_response_rev23_packaging_failure.json'
        if not failure.exists():failure.write_text(dump({'error':str(exc),'type':type(exc).__name__,'checks':CHECKS,'commands':LOG}))
        raise
