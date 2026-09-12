"""Validate and commit R025, then create and restore-check portable deliverables."""
from __future__ import annotations
import ast
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r025'
BASE='4c71883e7c2df60f119a8c40dfb7d9a5676deef7'
D='.codex/research/hott/dialogues/GEMINI-001/'
N=D+'rounds/006/'
DELIVERY=ROOT.parent/'HoTT_Gemini_review_rev25_with_git.zip'
BUNDLE=ROOT.parent/'HoTT_Gemini_review_rev25.bundle'
PACKET=ROOT.parent/'Gemini_HoTT_debate_005.zip'
RECEIPT=ROOT.parent/'HoTT_Gemini_review_rev25_delivery_verification.json'
LOG=[];CHECKS=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def serialize(x):return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def put(path,x):
    if path.exists():raise FileExistsError(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(x if isinstance(x,str) else serialize(x),encoding='utf-8')
def command(argv,cwd=ROOT,timeout=90):
    args=[str(a) for a in argv];start=datetime.now(timezone.utc).isoformat()
    p=subprocess.run(args,cwd=cwd,capture_output=True,text=True,timeout=timeout,
        env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',GIT_TERMINAL_PROMPT='0'))
    LOG.append({'argv':args,'cwd':str(cwd),'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),
        'stdout':p.stdout,'stderr':p.stderr,'exit_code':p.returncode})
    if p.returncode:raise RuntimeError(p.stderr or p.stdout)
    return p.stdout.strip()
def git(*args,cwd=ROOT):return command(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],cwd)
def check(name,condition,detail=None):
    CHECKS.append({'id':name,'status':'PASS' if condition else 'FAIL','detail':detail})
    if not condition:raise AssertionError(name)

def main():
    for path in (DELIVERY,BUNDLE,PACKET,RECEIPT):
        if path.exists():raise FileExistsError(path)
    check('inherited_HEAD',git('rev-parse','HEAD')==BASE)
    check('main_branch',git('branch','--show-current')=='main')
    check('no_remote',not git('remote'))
    inc=(ROOT/(N+'IN-005.md')).read_bytes();prov=json.loads((ROOT/(N+'PROVENANCE.json')).read_text())
    check('incoming_identity',sha(inc)==prov['sha256'] and len(inc)==prov['bytes'])
    letter=(ROOT/(D+'TO_GEMINI_005.md')).read_bytes()
    check('letter_md_txt_identical',letter==(ROOT/(D+'TO_GEMINI_005.txt')).read_bytes())
    check('letter_questions',all(x in letter.decode() for x in ['L01','L02','ReachTrap','AllRealizable']))
    ledger=json.loads((ROOT/(D+'DEBATE_LEDGER.json')).read_text())
    check('received_five_real_user_messages',len(ledger['incoming'])==5 and ledger['received_rounds']==5)
    old=next(x for x in ledger['outgoing'] if x['id']=='OUT-004')
    new=next(x for x in ledger['outgoing'] if x['id']=='OUT-005')
    check('old_reply_marked_received',old['reply_received'] and old['reply_id']=='IN-005')
    check('new_not_sent_or_answered',not new['sent'] and not new['reply_received'] and new['sha256']==sha(letter))
    replay=json.loads((OUT/'R024_TEST_REPLAY.json').read_text())
    check('original_31_tests_replayed',replay['exit_code']==0 and 'Ran 31 tests' in replay['stderr'] and replay['stderr'].rstrip().endswith('OK'))
    results=json.loads((OUT/'TARGETED_RESULTS.json').read_text());tests=results['checks']
    check('nine_targeted_groups',results['status']=='PASS_FINITE_SCOPE' and results['check_groups']==9)
    check('8512_block_checks',tests['instruction_and_block_agreement']['cases']==8512)
    check('12_actual_trap_certificates',len(results['certificates'])==12)
    check('six_mutations_detected',tests['mutations_rejected']['count']==6)
    check('new_execution_succeeded',json.loads((OUT/'TARGETED_EXECUTION.json').read_text())['exit_code']==0)
    check('native_not_claimed',results['proof_assistant']=='NOT_RUN')
    summary=json.loads((OUT/'TARGETED_SUMMARY.json').read_text())
    check('raw_results_hash',summary['raw_sha256']==sha((OUT/'TARGETED_RESULTS.json').read_bytes()))
    identities=json.loads((OUT/'EXECUTION_IDENTITY.json').read_text())
    check('executed_code_unchanged',all(sha((ROOT/p).read_bytes())==h for p,h in identities['code_sha256'].items()))
    cp=json.loads((OUT/'CHECKPOINT_SUMMARY.json').read_text())
    check('checkpoint25',cp['revision']==25 and cp['status']=='CHECKPOINT_COMMITTED')
    check('no_full_cognition_upgrade',cp['full_business_cognition']=='NOT_CLAIMED')
    check('stale_write_rejected',json.loads((OUT/'checkpoint/STALE_BASE.json').read_text())['error']=='STALE_BASE')
    fresh=json.loads(command([sys.executable,'-B',ROOT/'scripts/session/r025_plan_check.py']))
    check('fresh_route',fresh['required_paths_present'] and fresh['revision']==25)
    put(OUT/'FRESH_ROUTE.json',fresh)
    allowed={'MEMORY.md','scripts/README.md',D+'README.md',D+'DEBATE_LEDGER.json','.codex/cognition/HEAD.json',
        *['.codex/research/hott/'+p for p in ['STATE.json','FRONTIER.md','LESSONS.md','RESUME.md']]}
    changed=[];violations=[];count=0
    restore=json.loads((OUT/'RESTORE.json').read_text())
    for entry in restore['members']:
        path=entry['path']
        if path.startswith('.git/'):continue
        count+=1;file=ROOT/path
        if not file.is_file() or sha(file.read_bytes())!=entry['sha256']:
            changed.append(path)
            if path not in allowed:violations.append(path)
    check('old_assets_preserved',not violations,{'checked':count,'changed':changed,'violations':violations})
    check('source_archive_unchanged',sha(Path(restore['source']).read_bytes())==restore['source_sha256'])
    for path in ROOT.glob('scripts/**/r025_*.py'):ast.parse(path.read_text(),filename=str(path))
    check('new_scripts_parse',True)
    for path in list(OUT.rglob('*.json'))+list((ROOT/N).glob('*.json')):json.loads(path.read_text())
    check('new_json_parse',True)
    check('no_symlinks',all(not p.is_symlink() for p in ROOT.rglob('*')))
    put(OUT/'REPORT.md','''# R025 · Gemini IN-005评估与OUT-005

本轮接受条件对角证明／EM_H依赖分离，补查D₁的有限到达、返回吸收与全轨迹非返回。T可判定的依据是有限配置与迭代，不是确定性本身。非Bool返回2为工程约定；反射/商接口的下一目标应是具体Rep(f)或局部执行依据，而非预设AllRealizable。

原31测试复现；9组新检查通过，含8512项块对照、153前缀、42尾部、12份trap证书、6项刻意突变识别。原R024源码未改，没有找到编译器反例；没有HoTT内核验证。全称非返回解释来自TECHNICAL_NOTE中的归纳，不由样本量推出。

原文IN-005完整保留；Gemini未提供新执行日志或机器证明。OUT-005未直接发送，无IN-006。依赖外部回复不是研究门槛。

从rev24完整包继承Git。原治理checkpoint24→25成功，新进程及异目录计划包含本轮材料，旧快照被拒绝。完整业务认知集合未全文加载，本轮仅认证有界评估、验证与交接。未改AGENTS、两Skills、第五闭包、三问、Schema、矩阵和旧数学。仅当前工作记忆、动态路由、台账与索引更新。

全部新增代码先scripts保存后执行；原代码与结果保持。完整ZIP包含继承Git，bundle另附。最终HEAD与压缩包验证见外部delivery_verification，不让文件自引用制造假哈希。无远端、无push、无外部AI。
''')
    put(OUT/'FILE_CHECKS.json',{'scope':'FILES_ROUTING_TEST_COUNTS_NOT_MATH_CERTIFICATION','checks':CHECKS.copy()})
    put(OUT/'PRECOMMIT_COMMANDS.json',LOG.copy())
    git('add','--all')
    git('commit','-m','Review Gemini IN-005, audit D1 trace invariants and draft OUT-005')
    head=git('rev-parse','HEAD');check('clean_after_commit',not git('status','--porcelain'))
    git('fsck','--full');git('bundle','create',BUNDLE,'--all');git('bundle','verify',BUNDLE)
    files=[p for p in sorted(ROOT.rglob('*')) if p.is_file()]
    with zipfile.ZipFile(DELIVERY,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
        for file in files:archive.write(file,ROOT.name+'/'+file.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(DELIVERY) as archive:
        check('zip_crc',archive.testzip() is None)
        check('zip_byte_roundtrip',all(archive.read(ROOT.name+'/'+p.relative_to(ROOT).as_posix())==p.read_bytes() for p in files))
    packet={'TO_GEMINI_005.md':D+'TO_GEMINI_005.md','TO_GEMINI_005.txt':D+'TO_GEMINI_005.txt',
        'previous/TO_GEMINI_004.md':D+'TO_GEMINI_004.md'}
    for file in (ROOT/N).iterdir():
        if file.is_file():packet['rounds/006/'+file.name]=N+file.name
    for rel in ['scripts/research/r024_diagonal_machine.py','scripts/tests/test_r024_diagonal_machine.py',
        'scripts/research/r025_diagonal_audit.py','scripts/session/run_logged.py',
        'artifacts/r025/TARGETED_RESULTS.json','artifacts/r025/TARGETED_SUMMARY.json',
        'artifacts/r025/TARGETED_EXECUTION.json','artifacts/r025/R024_TEST_REPLAY.json',
        'artifacts/r025/ENVIRONMENT.json','artifacts/r025/EXECUTION_IDENTITY.json']:
        packet[rel]=rel
    manifest=[]
    with zipfile.ZipFile(PACKET,'w',zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('README.txt','先读TO_GEMINI_005.md，随后看rounds/006/TECHNICAL_NOTE.md。请回应L01或L02的具体缺口，不再仅确认结论。有限测试不是HoTT内核证明。原Python源码可在本包根运行；写结果前需保留原artifacts/r025，避免覆盖既有证据。完整Git工作目录另包。此包未直接发送。\n')
        for name,rel in packet.items():
            b=(ROOT/rel).read_bytes();archive.writestr(name,b);manifest.append({'path':name,'bytes':len(b),'sha256':sha(b)})
        archive.writestr('MANIFEST.json',serialize({'files':manifest,'scope':'review and finite evidence; not native HoTT proof'}))
    with zipfile.ZipFile(PACKET) as archive:
        check('packet_hashes',archive.testzip() is None and all(sha(archive.read(x['path']))==x['sha256'] for x in manifest))
    with tempfile.TemporaryDirectory(prefix='hott-r025-verify-') as temporary:
        target=Path(temporary)
        with zipfile.ZipFile(DELIVERY) as archive:
            archive.extractall(target)
            for member in archive.infolist():
                if not member.is_dir():
                    (target/member.filename).chmod(0o755 if (member.external_attr>>16)&0o111 else 0o644)
        restored=target/ROOT.name
        check('restored_head',git('rev-parse','HEAD',cwd=restored)==head)
        check('restored_clean',not git('status','--porcelain',cwd=restored))
        reload=json.loads(command([sys.executable,'-B',restored/'scripts/session/r025_plan_check.py'],cwd=target))
        check('relocated_same_state',reload['snapshot']==fresh['snapshot'] and reload['required_paths_present'])
        clone=target/'from-bundle';command(['git','-c','core.hooksPath=/dev/null','clone',BUNDLE,clone],cwd=target)
        check('bundle_clone_head',git('rev-parse','HEAD',cwd=clone)==head)
        check('bundle_clone_clean',not git('status','--porcelain',cwd=clone))
    outputs=[]
    for path in (DELIVERY,BUNDLE,PACKET):
        digest=sha(path.read_bytes());put(Path(str(path)+'.sha256'),digest+'  '+path.name+'\n')
        outputs.append({'path':str(path),'bytes':path.stat().st_size,'sha256':digest})
    receipt={'status':'VERIFIED_FILES_AND_GIT','revision':25,'head':head,'inherited_head':BASE,'workspace':str(ROOT),
        'checks':CHECKS,'passed':len(CHECKS),'commands':LOG,'outputs':outputs,'files':len(files),
        'old_tests_replayed':31,'new_check_groups':9,'block_cases':8512,'mutations_detected':6,'trap_certificates':12,
        'full_business_cognition':'NOT_CLAIMED','native_hott_proof':'NOT_RUN','outgoing':'OUT-005_NOT_SENT',
        'original_assets_preserved':True}
    put(RECEIPT,receipt)
    print(serialize({k:receipt[k] for k in ['revision','head','passed','outputs','outgoing']}))
if __name__=='__main__':
    try:main()
    except Exception as exc:
        failure=ROOT.parent/'HoTT_Gemini_review_rev25_packaging_failure.json'
        if not failure.exists():failure.write_text(serialize({'error':str(exc),'type':type(exc).__name__,'checks':CHECKS,'commands':LOG}))
        raise
