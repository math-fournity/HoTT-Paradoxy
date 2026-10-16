#!/usr/bin/env python3
"""Archive and restore R039 with real Git history and an independently rerun research kit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT.parent
FULL = BASE / 'HoTT_silent_steps_rev39_with_git.zip'
KIT = BASE / 'HoTT_silent_steps_R039.zip'
BUNDLE = BASE / 'HoTT_silent_steps_rev39.bundle'
REPORT = BASE / 'HoTT_silent_steps_rev39_delivery_verification.json'
R = '.codex/research/hott/reviews/SILENT-STEPS-001/'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(argv, cwd):
    start = datetime.now(timezone.utc).isoformat()
    proc = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=120,
                          env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1', GIT_OPTIONAL_LOCKS='0'))
    receipt = {'argv': argv, 'cwd': str(cwd), 'started_utc': start,
               'ended_utc': datetime.now(timezone.utc).isoformat(), 'exit_code': proc.returncode,
               'stdout': proc.stdout, 'stderr': proc.stderr}
    if proc.returncode:
        raise RuntimeError(json.dumps(receipt, ensure_ascii=False))
    return receipt


def git(args, cwd=ROOT):
    return run(['git', *args], cwd)


def main():
    for path in (FULL, KIT, BUNDLE, REPORT):
        if path.exists():
            raise FileExistsError(path)
    assert not git(['status', '--porcelain'])['stdout'].strip()
    assert not git(['remote'])['stdout'].strip()
    head = git(['rev-parse', 'HEAD'])['stdout'].strip()
    fsck = git(['fsck', '--full'])
    git(['bundle', 'create', str(BUNDLE), '--all'])
    bundle_verify = git(['bundle', 'verify', str(BUNDLE)])
    manifest = []
    for path in sorted(ROOT.rglob('*')):
        if path.is_symlink():
            raise ValueError('Unexpected symlink: ' + str(path))
        if path.is_file():
            manifest.append({'path': path.relative_to(ROOT).as_posix(), 'bytes': path.stat().st_size,
                             'sha256': sha(path), 'mode': path.stat().st_mode & 0o777})
    with zipfile.ZipFile(FULL, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for item in manifest:
            archive.write(ROOT / item['path'], ROOT.name + '/' + item['path'])
    with zipfile.ZipFile(FULL) as archive:
        assert archive.testzip() is None
        for item in manifest:
            assert hashlib.sha256(archive.read(ROOT.name + '/' + item['path'])).hexdigest() == item['sha256']
        with tempfile.TemporaryDirectory(prefix='r039-restore-', dir=BASE) as temp:
            dest = Path(temp)
            archive.extractall(dest)
            restored = dest / ROOT.name
            for item in manifest:
                path = restored / item['path']
                path.chmod(item['mode'])
                assert sha(path) == item['sha256']
            assert git(['rev-parse', 'HEAD'], restored)['stdout'].strip() == head
            assert not git(['status', '--porcelain'], restored)['stdout'].strip()
            restored_fsck = git(['fsck', '--full'], restored)
            fresh = run([sys.executable, '-B', str(restored / 'scripts/session/r039_verify_v2.py'), '--fresh'], dest)
            assert json.loads(fresh['stdout'])['revision'] == 39
            assert not git(['status', '--porcelain'], restored)['stdout'].strip()
            clone = dest / 'bundle-clone'
            clone_receipt = git(['clone', str(BUNDLE), str(clone)], dest)
            assert git(['rev-parse', 'HEAD'], clone)['stdout'].strip() == head
            assert not git(['status', '--porcelain'], clone)['stdout'].strip()
            assert json.loads((clone / '.codex/research/hott/STATE.json').read_text())['revision'] == 39
    selected = [R + name for name in ('PROOF_NOTE.md', 'CLAIMS.json', 'SOURCES.md', 'PLAN.md')] + [
        'scripts/research/r039_silent_steps.py', 'scripts/tests/test_r039_silent_steps.py',
        'artifacts/r039/RESULTS.json', 'artifacts/r039/TEST_EXECUTION.json',
        'artifacts/r039/MODEL_EXECUTION.json', 'artifacts/r039/RESEARCH_MANIFEST.json',
        'artifacts/r039/REPORT_FINAL.md', 'artifacts/r039/VERIFICATION_V2.json',
        'artifacts/r039/VERIFIER_CORRECTION.json', 'artifacts/r039/sources/FETCH_RECEIPT.json']
    prefix = 'HoTT_silent_steps_R039/'
    readme = '''# R039 内部停顿与完成性

主文：.codex/research/hott/reviews/SILENT-STEPS-001/PROOF_NOTE.md。
执行测试：`python3 -B scripts/tests/test_r039_silent_steps.py`。
31项有限模型测试不是HoTT内核证明；144个确定性有限Delay图是局部穷尽交叉检查。
普通弱互模拟、错误的无限单边跳过关系、保返回结果的Delay关系分别定义。
源码中的preserve_divergence开关仅实现附加状态发散标签过滤的有限检查，不声称实现文献全部分支互模拟条件。
一般证明为纸笔；无原生Lean/Agda/Rocq执行。来源SOURCES中标明web阅读范围，容器下载失败没有伪装为原件存档。
本包不含全部历史或所有manifest引用原件；跨Session恢复应使用with_git完整包。
'''
    with zipfile.ZipFile(KIT, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
        for path in selected:
            archive.write(ROOT / path, prefix + path)
        archive.writestr(prefix + 'README.md', readme)
        archive.writestr(prefix + 'MANIFEST.json', json.dumps({p: sha(ROOT / p) for p in selected}, ensure_ascii=False, indent=2) + '\n')
    with zipfile.ZipFile(KIT) as archive:
        assert archive.testzip() is None
        for path in selected:
            assert hashlib.sha256(archive.read(prefix + path)).hexdigest() == sha(ROOT / path)
        with tempfile.TemporaryDirectory(prefix='r039-kit-', dir=BASE) as temp:
            archive.extractall(temp)
            kitroot = Path(temp) / prefix.rstrip('/')
            kit_test = run([sys.executable, '-B', 'scripts/tests/test_r039_silent_steps.py'], kitroot)
            assert 'Ran 31 tests' in kit_test['stderr'] and '\nOK\n' in kit_test['stderr']
    assert not git(['status', '--porcelain'])['stdout'].strip()
    report = {
        'status': 'PASS_DELIVERY_AND_RESTORE', 'revision': 39, 'research_round': 'R039',
        'workspace': str(ROOT), 'git_head': head,
        'git_commit_count': int(git(['rev-list', '--count', 'HEAD'])['stdout']),
        'clean_worktree': True, 'remote_count': 0, 'all_zip_bytes_verified': True,
        'full_zip': {'path': str(FULL), 'bytes': FULL.stat().st_size, 'sha256': sha(FULL)},
        'research_kit': {'path': str(KIT), 'bytes': KIT.stat().st_size, 'sha256': sha(KIT)},
        'git_bundle': {'path': str(BUNDLE), 'bytes': BUNDLE.stat().st_size, 'sha256': sha(BUNDLE)},
        'fsck': fsck, 'bundle_verify': bundle_verify, 'restored_fsck': restored_fsck,
        'fresh_verifier': fresh, 'bundle_clone': clone_receipt, 'kit_tests': kit_test,
        'manifest': manifest,
        'scope': 'File integrity, Git restoration, finite executable models; NOT native HoTT validation and NOT complete cognition certification.'}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in ('status', 'revision', 'git_head', 'git_commit_count', 'full_zip', 'research_kit', 'git_bundle')}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
