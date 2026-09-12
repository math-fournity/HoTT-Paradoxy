#!/usr/bin/env python3
"""Finish R022 packaging after a correctly detected stale snapshot comparison.
Preserve the first attempt; freeze all document edits before taking a new fingerprint.
This verifies documentation/state and Git, not mathematics, peer response, or cognition.
"""
from pathlib import Path
import ast, datetime, hashlib, importlib.util, json, os, shutil
import subprocess, sys, tempfile, zipfile

R = Path(__file__).resolve().parents[2]
A = R / 'artifacts/r022'
EXT = R.parent
D = '.codex/research/hott/dialogues/GEMINI-001/'
BASE = '8e6641dd9b229e39875017e6a56732c2b8019af3'
FIRST = '595be74d303f5f095f9d6fb5d13cdff0a880a0cb'
LOG = []
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', GIT_TERMINAL_PROMPT='0')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def dump(data):
    return json.dumps(data, ensure_ascii=False, indent=2) + '\n'

def create(path, data):
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(data if isinstance(data, str) else dump(data), encoding='utf-8')

def run(argv, cwd=R, timeout=120):
    args = list(map(str, argv))
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    proc = subprocess.run(args, cwd=cwd, env=ENV, capture_output=True, text=True, timeout=timeout)
    LOG.append(dict(argv=args, cwd=str(cwd), started_utc=start,
                    ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    exit_code=proc.returncode, stdout=proc.stdout, stderr=proc.stderr))
    if proc.returncode:
        raise RuntimeError(f'Command failed {args}: {proc.stderr}')
    return proc.stdout.strip()

def git(*args, cwd=R):
    return run(['git', '-c', 'core.hooksPath=/dev/null', '-c', 'core.fsmonitor=false', *args], cwd)

def runtime():
    spec = importlib.util.spec_from_file_location('r022_finish_runtime', R / '.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod

def main():
    if git('rev-parse', 'HEAD') != FIRST:
        raise RuntimeError('Unexpected starting HEAD; refuse to package stale baseline')
    rt = runtime()
    old = json.loads((A/'checkpoint-final/AFTER_PLAN.json').read_text())
    current = rt.plan(R)
    before = {d['path']: d['sha256'] for d in old['documents']}
    after = {d['path']: d['sha256'] for d in current['documents']}
    differences = [dict(path=k, before=before.get(k), after=after.get(k))
                   for k in sorted(before.keys() | after.keys()) if before.get(k) != after.get(k)]
    if [d['path'] for d in differences] != ['scripts/README.md']:
        raise RuntimeError('Snapshot discrepancy has an unexpected source: '+dump(differences))
    failure = EXT/'HoTT_Gemini_reply_rev22_packaging_failure.json'
    preserved = A/'PACKAGING_FIRST_FAILURE.json'
    if preserved.exists():
        raise FileExistsError(preserved)
    shutil.copyfile(failure, preserved)
    diagnostic = dict(schema_version='r022-packaging-diagnostic/v1',
                      initial_commit=FIRST, failure='post-package snapshot mismatch',
                      previous_snapshot=old['snapshot'], current_snapshot=current['snapshot'],
                      changed_dynamic_documents=differences,
                      cause='First packaging tool took a route fingerprint, then appended the scripts index before packaging. Byte-identical relocation had a different, correctly newer fingerprint.',
                      remedy='Preserve the failed attempt; finish all file edits first, then compare final frozen source route with relocated package.',
                      mathematical_changes=False, source_letter_changed=False)
    create(A/'PACKAGING_DIAGNOSIS.json', diagnostic)
    idx=R/'scripts/README.md'
    idx.write_text(idx.read_text()+'\nR022交付修复：`scripts/tools/r022_finish_delivery.py` 保留首次快照比较失败，先完成文档修改再冻结并核对源目录／异目录状态；不改数学或治理引擎。\n', encoding='utf-8')
    report=A/'REPORT.md'
    report.write_text(report.read_text()+'''\n## 交付复核中的额外故障\n\n首次打包在成功提交Git、ZIP字节回读和解压恢复后，发现动态快照不匹配。定位为打包工具先生成快照，再追加`scripts/README.md`；二者不是同一个文件状态。实际差异仅该脚本索引，并非ZIP损坏。原失败日志和源码保留，修复工具在全部修改完成后重新固定源状态，再做异目录和bundle恢复核对。最终交付证据仍以包外delivery_verification为准。\n''', encoding='utf-8')
    parsed=[]
    for p in sorted((R/'scripts').rglob('r022_*.py')):
        ast.parse(p.read_text()); parsed.append(p.relative_to(R).as_posix())
    md=(R/(D+'TO_GEMINI_002.md')).read_bytes()
    assert (R/(D+'TO_GEMINI_002.txt')).read_bytes()==md
    assert sha(md)=='8d2234ce189d0dde87d6ee0c342810f651c51d2baf820ce6cd437632f893479c'
    ledger=json.loads((R/(D+'DEBATE_LEDGER.json')).read_text())
    outgoing=next(v for v in ledger['outgoing'] if v['id']=='OUT-002')
    assert not outgoing['sent'] and not outgoing['reply_received'] and len(ledger['incoming'])==2
    allow={D+'DEBATE_LEDGER.json', D+'README.md', 'scripts/README.md', 'MEMORY.md',
           '.codex/cognition/HEAD.json', *['.codex/research/hott/'+s for s in ('STATE.json','FRONTIER.md','LESSONS.md','RESUME.md')]}
    changed=[]; protected=0
    for row in json.loads((A/'RESTORE.json').read_text())['files']:
        if row['path'].startswith('.git/'):
            continue
        protected+=1
        p=R/row['path']
        if not p.is_file() or sha(p.read_bytes())!=row['sha256']:
            changed.append(row['path'])
            assert row['path'] in allow, row['path']
    final_plan=rt.plan(R)
    assert final_plan['revision']==22
    fresh=json.loads(run([sys.executable,'-B',R/'scripts/session/r022_plan_check.py']))
    assert fresh['snapshot']==final_plan['snapshot']
    create(A/'FINAL_FROZEN_PLAN.json',final_plan)
    create(A/'FINAL_FRESH_PLAN_CHECK.json',fresh)
    create(A/'FINAL_FILE_CHECKS.json',dict(status='PASS_FILES_ONLY', scripts_parsed=parsed,
           prior_file_checks=json.loads((A/'FILE_CHECKS.json').read_text())['passed'],
           baseline_non_git_files=protected, allowed_changed=changed,
           letter_sha256=sha(md), new_peer_reply=False, outgoing_sent=False,
           finalized_route_snapshot=final_plan['snapshot']))
    create(A/'FINAL_PRECOMMIT_COMMANDS.json',LOG.copy())
    # Final evidence files do not enter the source route; verify before committing.
    assert rt.plan(R)['snapshot']==final_plan['snapshot']
    git('add','--all')
    git('commit','-m','chore: freeze final R022 route before archive verification')
    head=git('rev-parse','HEAD')
    assert git('status','--porcelain')=='' and git('remote')==''
    git('merge-base','--is-ancestor',BASE,'HEAD')
    git('fsck','--full')
    out=EXT/'HoTT_Gemini_reply_rev22_with_git.zip'
    bundle=EXT/'HoTT_Gemini_reply_rev22.bundle'
    packet=EXT/'Gemini_HoTT_debate_002.zip'
    for path in (out,bundle):
        backup=path.with_name(path.name+'.pre-final')
        if backup.exists():
            raise FileExistsError(backup)
        path.rename(backup)
    git('bundle','create',bundle,'--all')
    git('bundle','verify',bundle)
    files=[p for p in sorted(R.rglob('*')) if p.is_file()]
    assert not any(p.is_symlink() for p in R.rglob('*'))
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files:
            z.write(p,R.name+'/'+p.relative_to(R).as_posix())
    with zipfile.ZipFile(out) as z:
        assert z.testzip() is None
        for p in files:
            assert z.read(R.name+'/'+p.relative_to(R).as_posix())==p.read_bytes()
    with zipfile.ZipFile(packet) as z:
        assert z.testzip() is None
        pm=json.loads(z.read('MANIFEST.json'))
        for row in pm['files']:
            assert sha(z.read(row['path']))==row['sha256']
        assert z.read('TO_GEMINI_002.md')==md
    with tempfile.TemporaryDirectory(prefix='hott-r022-final-') as td:
        tmp=Path(td)
        with zipfile.ZipFile(out) as z:
            for name in z.namelist():
                dest=(tmp/name).resolve();dest.relative_to(tmp.resolve())
            z.extractall(tmp)
        extracted=tmp/R.name
        assert git('rev-parse','HEAD',cwd=extracted)==head
        assert git('status','--porcelain',cwd=extracted)==''
        moved=json.loads(run([sys.executable,'-B',extracted/'scripts/session/r022_plan_check.py'],cwd=tmp))
        assert moved['snapshot']==final_plan['snapshot']
        clone=tmp/'from-bundle'
        run(['git','-c','core.hooksPath=/dev/null','clone',bundle,clone],cwd=tmp)
        assert git('rev-parse','HEAD',cwd=clone)==head
        assert git('status','--porcelain',cwd=clone)==''
        cloned=json.loads(run([sys.executable,'-B',clone/'scripts/session/r022_plan_check.py'],cwd=tmp))
        assert cloned['snapshot']==final_plan['snapshot']
    assert rt.plan(R)['snapshot']==final_plan['snapshot']
    assert git('status','--porcelain')==''
    outputs=[]
    for p in (out,bundle,packet):
        h=sha(p.read_bytes())
        create(p.with_name(p.name+'.sha256'),h+'  '+p.name+'\n')
        outputs.append(dict(path=str(p),bytes=p.stat().st_size,sha256=h))
    result=dict(schema_version='r022-delivery-verification/v1',status='VERIFIED_FILES_AND_GIT',
       root=str(R),revision=22,head=head,source_head=BASE,first_commit=FIRST,
       branch=git('branch','--show-current'),working_tree_clean=True,git_fsck='PASS',
       remote_configured=False,original_non_git_files=protected,allowed_changed=changed,
       zip_readback='ALL_FILES_IDENTICAL',restored_git_clean=True,bundle_clone_matches=True,
       source_route_snapshot=final_plan['snapshot'],relocated_same_snapshot=True,bundle_same_snapshot=True,
       route_documents=len(final_plan['documents']),letter_sha256=sha(md),letter_bytes=len(md),
       outgoing_status='READY_FOR_USER_RELAY_NOT_SENT',new_peer_reply=False,
       file_checks=json.loads((A/'FILE_CHECKS.json').read_text())['passed'],new_scripts_syntax_checks=len(parsed),
       mathematical_kernel_verification='NOT_RUN',full_business_cognition='NOT_CLAIMED',
       failure_diagnosis='Preserved first attempt; mismatch due to script-index edit after early fingerprint, resolved by freeze-before-compare.',
       outputs=outputs,commands=LOG)
    create(EXT/'HoTT_Gemini_reply_rev22_delivery_verification.json',result)
    print(dump({k:result[k] for k in ('status','revision','head','source_route_snapshot','route_documents','letter_bytes','outputs')}))

if __name__=='__main__':
    try:
        main()
    except Exception as exc:
        p=EXT/'HoTT_Gemini_reply_rev22_final_packaging_failure.json'
        if not p.exists():
            p.write_text(dump(dict(type=type(exc).__name__,error=str(exc),commands=LOG)),encoding='utf-8')
        raise
