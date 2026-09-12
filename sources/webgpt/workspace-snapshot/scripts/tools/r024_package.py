"""Validate R024, commit the inherited local Git repository, and verify deliverables.

File/Git checks certify preservation, not HoTT or unbounded mathematical claims.
No remote, push, external agent, dependency installation, or user-host access.
"""
from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import ast
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import zipfile

R = Path(__file__).resolve().parents[2]
O = R/'artifacts/r024'
D = '.codex/research/hott/dialogues/GEMINI-001/'
N = D+'rounds/005/'
BASE = '38d6d706fa7131719ccf94f24abd09b86e00ef17'
ZIP = R.parent/'HoTT_Gemini_review_rev24_with_git.zip'
BUNDLE = R.parent/'HoTT_Gemini_review_rev24.bundle'
PACK = R.parent/'Gemini_HoTT_debate_004.zip'
RECEIPT = R.parent/'HoTT_Gemini_review_rev24_delivery_verification.json'
LOG: list[dict] = []
CHECKS: list[dict] = []

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def dump(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2)+'\n'

def new(path: Path, value: object) -> None:
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value if isinstance(value,str) else dump(value), encoding='utf-8')

def run(argv: list, cwd: Path = R, timeout: int = 90) -> str:
    args = [str(a) for a in argv]
    started = datetime.now(timezone.utc).isoformat()
    proc = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=timeout,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', GIT_TERMINAL_PROMPT='0'))
    LOG.append({'argv':args,'cwd':str(cwd),'started_at_utc':started,
                'finished_at_utc':datetime.now(timezone.utc).isoformat(),
                'exit_code':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr})
    if proc.returncode:
        raise RuntimeError(proc.stderr or proc.stdout or f'Exit {proc.returncode}')
    return proc.stdout.strip()

def git(*args, cwd: Path = R) -> str:
    return run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd)

def check(name: str, condition: bool, detail: object = None) -> None:
    CHECKS.append({'id':name,'status':'PASS' if condition else 'FAIL','detail':detail})
    if not condition:
        raise AssertionError(name)

def main() -> None:
    for path in (ZIP,BUNDLE,PACK,RECEIPT):
        if path.exists():
            raise FileExistsError(path)
    check('inherited_git_head',git('rev-parse','HEAD') == BASE)
    check('no_remote',not git('remote'))
    check('branch_main',git('branch','--show-current') == 'main')
    incoming=(R/(N+'IN-004.md')).read_bytes()
    provenance=json.loads((R/(N+'PROVENANCE.json')).read_text())
    check('incoming_hash',sha(incoming)==provenance['sha256'])
    check('incoming_size',len(incoming)==provenance['bytes'])
    check('incoming_j01_j05',all(f'### J{i:02}' in incoming.decode() for i in range(1,6)))
    letter=(R/(D+'TO_GEMINI_004.md')).read_bytes()
    check('same_letter_txt',letter==(R/(D+'TO_GEMINI_004.txt')).read_bytes())
    check('letter_k01_k03',all(f'K{i:02}' in letter.decode() for i in range(1,4)))
    check('letter_math_delimiters',letter.count(b'\\[')==letter.count(b'\\]'))
    ledger=json.loads((R/(D+'DEBATE_LEDGER.json')).read_text())
    check('four_actual_incoming',len(ledger['incoming'])==4 and ledger['received_rounds']==4)
    outgoing=next(item for item in ledger['outgoing'] if item['id']=='OUT-004')
    check('letter_recorded_hash',outgoing['sha256']==sha(letter))
    check('not_sent_no_reply',not outgoing['sent'] and not outgoing['reply_received'])
    check('peer_not_prerequisite',ledger['workflow']['awaiting_peer_to_start_research'] is False)
    result=json.loads((O/'COMPILER_RESULTS.json').read_text())
    summary=json.loads((O/'COMPILER_SUMMARY.json').read_text())
    check('program_count_241',result['program_count']==241)
    check('1928_pairs_40_unknown',result['run_pairs']==1928 and result['unknown_pairs']==40 and result['established_pairs']==1888)
    check('raw_result_hash',summary['raw_result_sha256']==sha((O/'COMPILER_RESULTS.json').read_bytes()))
    check('code_hash',result['code_sha256']==sha((R/'scripts/research/r024_diagonal_machine.py').read_bytes()))
    logs=json.loads((O/'TEST_EXECUTION.json').read_text())
    check('31_unit_tests_run',len(logs)==1 and logs[0]['exit_code']==0 and 'Ran 31 tests' in logs[0]['stderr'] and logs[0]['stderr'].rstrip().endswith('OK'))
    check('finite_not_hott_proof',result['proof_by_enumeration'] is False and result['native_hott_proof']=='NOT_RUN' and summary['formal_validation']=='NOT_RUN')
    cp=json.loads((O/'CHECKPOINT_SUMMARY.json').read_text())
    check('checkpoint24',cp['revision']==24 and cp['status']=='CHECKPOINT_COMMITTED')
    check('no_full_cognition_claim',cp['full_business_cognition']=='NOT_CLAIMED')
    check('stale_base_rejected',json.loads((O/'checkpoint/STALE_BASE.json').read_text())['error']=='STALE_BASE')
    fresh=json.loads(run([sys.executable,'-B',R/'scripts/session/r024_plan_check.py']))
    check('fresh_dynamic_route',fresh['required_paths_present'] and fresh['revision']==24)
    new(O/'FRESH_PLAN.json',fresh)
    allowed={'MEMORY.md','scripts/README.md',D+'README.md',D+'DEBATE_LEDGER.json','.codex/cognition/HEAD.json',
             *['.codex/research/hott/'+name for name in ('STATE.json','FRONTIER.md','LESSONS.md','RESUME.md')]}
    changes=[];violations=[];protected=0
    for item in json.loads((O/'RESTORE.json').read_text())['files']:
        path=item['path']
        if path.startswith('.git/'):
            continue
        protected+=1
        f=R/path
        if not f.is_file() or sha(f.read_bytes())!=item['sha256']:
            changes.append(path)
            if path not in allowed:
                violations.append(path)
    check('old_sources_preserved',not violations,{'existing_non_git_files':protected,'changed':changes,'violations':violations})
    parsed=[]
    for path in sorted((R/'scripts').rglob('r024_*.py')):
        ast.parse(path.read_text(),filename=str(path));parsed.append(path.relative_to(R).as_posix())
    check('new_scripts_parse',len(parsed)>=10,parsed)
    failed=R/'scripts/recovered/r024/checkpoint_initial.py'
    try:
        ast.parse(failed.read_text())
    except SyntaxError:
        known_failure=True
    else:
        known_failure=False
    check('failed_initial_source_retained',known_failure and sha(failed.read_bytes())==json.loads((O/'CHECKPOINT_INITIAL_FAILURE.json').read_text())['failed_source_sha256'])
    for path in list(O.rglob('*.json'))+list((R/N).glob('*.json')):
        json.loads(path.read_text(encoding='utf-8'))
    check('new_json_parses',True)
    report='''# R024 · IN-004评估、程序化验证与OUT-004

## 结论和新增证据

本轮吸收Gemini收敛到RP-B01的选择，纠正有限路径字算法与原始transport判断归约的混淆、decode输入不透明性、反射局部拒绝被过度泛化、LEM与条件无代码反证职责混同。IN-004完整可见正文保存，原抬头OUT-002未改；台账据J编号关联OUT-003。

新增明确自然寄存器机、无神谕的字面内联对角编译器及原始日志。31项测试通过；241份代码的1928组运行对照中1888得到结果，40仍UNKNOWN。400份有限字奇偶对照只验证独立算法，不验证原始HoTT归约。TECHNICAL_NOTE给出条件反证与具体编译模拟论证；原生HoTT内化、内核和独立审查均未执行。

Lean正反对照源码已保存，但环境无Lean/Agda/Rocq，官方Lean下载HEAD探测DNS失败；未安装、未伪造编译结果。官方文档的拒绝行为与本轮实际运行严格分开。

## 治理与失败证据

原治理器实际checkpoint23→24，最新Session S-DISC-20260911-024-GEMINI-IN004；244份当前动态来源，新增原文、评估、技术附件、回信和代码均已进入；新进程路由已检查，不等于244份全文语义加载。完整业务认知本轮NOT_CLAIMED；本轮是用户要求的有界评估与针对性检查。

首次checkpoint脚本因payload字典键转录错误在解析时失败，未执行任何保存动作；原失败源码与错误记录均保留。修正后由原治理器提交成功，旧快照再写入实际被拒绝。没有隐去首次失败。

## 文件与Git

从用户提供的rev23完整包恢复并继承Git，不修改原上传目录或原包。第五闭包、三问、AGENTS、Skills、Schema、主张矩阵、原计划、旧信件和旧研究原字节保留。仅当前记忆、状态、讨论台账、讨论入口及脚本索引更新；所有新增源码先保存scripts再执行。

OUT-004未直接发送，无IN-005，不等待外部回复才能继续。包内包含源程序、测试、原结果及技术论证；测试不是HoTT悖论的机器证明。最终HEAD、ZIP与bundle恢复记录保存在外部delivery_verification，避免自引用。无远端、无push、无其他AI。
'''
    new(O/'REPORT.md',report)
    new(O/'FILE_CHECKS.json',{'scope':'FILES_STATE_AND_REPORTED_TEST_COUNTS_NOT_NEW_MATH_PROOF','passed':len(CHECKS),'checks':CHECKS})
    new(O/'PRECOMMIT_COMMANDS.json',LOG.copy())
    git('add','--all')
    git('commit','-m','Review Gemini IN-004, test explicit diagonal compiler and draft OUT-004')
    head=git('rev-parse','HEAD')
    check('clean_worktree_after_commit',not git('status','--porcelain'))
    git('fsck','--full')
    git('bundle','create',BUNDLE,'--all')
    git('bundle','verify',BUNDLE)
    files=[p for p in sorted(R.rglob('*')) if p.is_file()]
    check('no_symlinks_in_export',all(not p.is_symlink() for p in R.rglob('*')))
    with zipfile.ZipFile(ZIP,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for path in files:
            z.write(path,R.name+'/'+path.relative_to(R).as_posix())
    with zipfile.ZipFile(ZIP) as z:
        check('zip_crc',z.testzip() is None)
        check('zip_every_byte_matches',all(z.read(R.name+'/'+p.relative_to(R).as_posix())==p.read_bytes() for p in files))
    packet={'TO_GEMINI_004.md':D+'TO_GEMINI_004.md','TO_GEMINI_004.txt':D+'TO_GEMINI_004.txt',
            'previous/TO_GEMINI_003.md':D+'TO_GEMINI_003.md'}
    for path in sorted((R/N).glob('*')):
        if path.is_file():
            packet['rounds/005/'+path.name]=N+path.name
    for rel in ['scripts/research/r024_diagonal_machine.py','scripts/tests/test_r024_diagonal_machine.py',
                'scripts/session/r024_run_checks.py','scripts/research/r024_lean_controls.lean',
                'scripts/research/r024_lean_negative_control.lean',
                'artifacts/r024/COMPILER_RESULTS.json','artifacts/r024/COMPILER_SUMMARY.json',
                'artifacts/r024/TEST_EXECUTION.json','artifacts/r024/TOOLCHAIN_STATUS.json',
                'artifacts/r024/SOURCE_EXCERPTS.md']:
        packet[rel]=rel
    manifest=[]
    with zipfile.ZipFile(PACK,'w',zipfile.ZIP_DEFLATED) as z:
        z.writestr('README.txt','先读TO_GEMINI_004.md；请优先核K01-K03。31项程序测试与1928组有限对照不是HoTT机器证明。40组UNKNOWN保留。Lean对照未运行。本包未直接发送，不包含模拟回信。源代码先保存后执行；重跑会产生新的运行文件，原结果须保全。完整Git工作目录另包。\n')
        for name,rel in packet.items():
            data=(R/rel).read_bytes();z.writestr(name,data)
            manifest.append({'path':name,'bytes':len(data),'sha256':sha(data)})
        z.writestr('MANIFEST.json',dump({'files':manifest,'scope':'Correspondence and finite program tests, not native proof certification'}))
    with zipfile.ZipFile(PACK) as z:
        check('packet_crc_and_hashes',z.testzip() is None and all(sha(z.read(item['path']))==item['sha256'] for item in manifest))
    with tempfile.TemporaryDirectory(prefix='hott-r024-delivery-') as tmp:
        base=Path(tmp)
        with zipfile.ZipFile(ZIP) as z:
            z.extractall(base)
        restored=base/R.name
        check('restored_head',git('rev-parse','HEAD',cwd=restored)==head)
        check('restored_clean',not git('status','--porcelain',cwd=restored))
        reread=json.loads(run([sys.executable,'-B',restored/'scripts/session/r024_plan_check.py'],cwd=base))
        check('relocated_same_state',reread['snapshot']==fresh['snapshot'] and reread['required_paths_present'])
        clone=base/'bundle-clone'
        run(['git','-c','core.hooksPath=/dev/null','clone',BUNDLE,clone],cwd=base)
        check('bundle_clone_head',git('rev-parse','HEAD',cwd=clone)==head)
        check('bundle_clone_clean',not git('status','--porcelain',cwd=clone))
    outputs=[]
    for path in (ZIP,BUNDLE,PACK):
        digest=sha(path.read_bytes())
        new(path.with_name(path.name+'.sha256'),digest+'  '+path.name+'\n')
        outputs.append({'path':str(path),'bytes':path.stat().st_size,'sha256':digest})
    new(RECEIPT,{'status':'VERIFIED_FILES_AND_GIT','revision':24,'workspace':str(R),'head':head,'inherited_head':BASE,
                'letter_sha256':sha(letter),'letter_bytes':len(letter),'incoming_bytes':len(incoming),'files':len(files),
                'checks':CHECKS,'passed':len(CHECKS),'outputs':outputs,'commands':LOG,
                'unit_tests':31,'finite_comparisons':1928,'unknown_comparisons':40,'native_hott_proof':'NOT_RUN',
                'full_business_cognition':'NOT_CLAIMED','outgoing':'OUT-004_NOT_SENT','original_assets_preserved':True})
    print(dump({'revision':24,'head':head,'checks':len(CHECKS),'outputs':outputs,'receipt':str(RECEIPT)}))

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        failure=R.parent/'HoTT_Gemini_review_rev24_packaging_failure.json'
        if not failure.exists():
            failure.write_text(dump({'error':str(exc),'type':type(exc).__name__,'checks':CHECKS,'commands':LOG}),encoding='utf-8')
        raise
