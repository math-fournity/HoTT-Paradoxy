# -*- coding: utf-8 -*-
"""工具自测（SOP 002 §7 第 10 条）。用合成样本检验：切行、切片、块划分、方法 A、账本链、notes 解析、git 白名单。

用法：python3 -B -I tools/selftest/run_selftest.py
结果写入 selftest/selftest-result.json。自测使用的临时账本与夹具位于 selftest/_work/，结束后删除。
自测不读取语料、不读取第一战役的任何文件，也不改动真实的 ledger2.jsonl。
"""
import json
import os
import shutil
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
sys.path.insert(0, TOOLS)
import common  # noqa: E402
from common import (Blocked, K, chunk_bytes, ledger_append, ledger_chain_ok, ledger_records,  # noqa: E402
                    sha256_hex, split_lines)
import align  # noqa: E402
import commit_block  # noqa: E402

WORKDIR = os.path.join(HERE, '_work')
RESULT = os.path.join(HERE, 'selftest-result.json')
results = []


def check(name, fn):
    try:
        fn()
        results.append({'test': name, 'result': 'PASS'})
    except Exception as ex:  # noqa: BLE001
        results.append({'test': name, 'result': 'FAIL', 'detail': '%s: %s' % (type(ex).__name__, ex),
                        'trace': traceback.format_exc()[-600:]})


def t_split_lines():
    assert len(split_lines(b'')) == 0
    assert len(split_lines(b'a\n')) == 1
    assert len(split_lines(b'a')) == 1
    l3 = split_lines(b'a\n\nb')
    assert [x[1] for x in l3] == [b'a', b'', b'b'], l3
    assert [x[0] for x in l3] == [0, 2, 3], l3
    assert split_lines(b'\n')[0][1] == b''
    assert split_lines(b'a\n')[0][2] is True and split_lines(b'a')[0][2] is False


def t_chunk_bytes():
    d = b'aa\nbb\ncc\n'
    L = split_lines(d)
    assert chunk_bytes(d, L, 1, 2) == b'aa\nbb\n'
    assert chunk_bytes(d, L, 3, 3) == b'cc\n'
    d2 = b'aa\nbb'
    L2 = split_lines(d2)
    assert chunk_bytes(d2, L2, 2, 2) == b'bb'
    try:
        chunk_bytes(d, L, 2, 4)
        raise AssertionError('越界未拒绝')
    except ValueError:
        pass


def t_plan_blocks_lines():
    d = (b'x' * 9 + b'\n') * 450
    spans = align.plan_blocks(split_lines(d), len(d))
    assert spans == [(1, 200), (201, 400), (401, 450)], spans


def t_plan_blocks_bytes():
    d = (b'y' * 999 + b'\n') * 100
    spans = align.plan_blocks(split_lines(d), len(d))
    assert spans[0] == (1, 40), spans[0]
    assert sum(e - s + 1 for s, e in spans) == 100


def _write_fixture(rel, data):
    p = os.path.join(WORKDIR, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'wb') as f:
        f.write(data)
    return os.path.relpath(p, common.ROOT)


def t_method_a_shared_run():
    f1 = [b'A%d' % i for i in range(1, 13)]
    f2 = [b'N1', b'N2', b'N3'] + f1[1:7] + [b'N4', b'N5', b'N6']
    p1 = _write_fixture('t1.txt', b'\n'.join(f1) + b'\n')
    p2 = _write_fixture('t2.txt', b'\n'.join(f2) + b'\n')
    man = {'order': ['t1', 't2'], 'files': [{'tag': 't1', 'path': p1}, {'tag': 't2', 'path': p2}]}
    res, runs = align.method_a(man)
    assert res['t1']['covered'] == 0
    assert res['t2']['covered'] == 6, res['t2']['covered']
    assert res['t2']['max_run'] == 6, res['t2']['max_run']


def t_method_a_short_run_not_counted():
    f1 = [b'P%d' % i for i in range(1, 9)]
    f2 = [b'Q1', b'P2', b'P3', b'P4', b'P5', b'Q2']  # 共享仅 4 行，少于 K=5
    p1 = _write_fixture('s1.txt', b'\n'.join(f1) + b'\n')
    p2 = _write_fixture('s2.txt', b'\n'.join(f2) + b'\n')
    assert K == 5
    man = {'order': ['s1', 's2'], 'files': [{'tag': 's1', 'path': p1}, {'tag': 's2', 'path': p2}]}
    res, runs = align.method_a(man)
    assert res['s2']['covered'] == 0, res['s2']['covered']


def t_ledger_chain():
    p = os.path.join(WORKDIR, 'test-ledger.jsonl')
    if os.path.exists(p):
        os.remove(p)
    for i in range(3):
        ledger_append({'type': 'TEST', 'i': i}, path=p)
    ok, n, bad = ledger_chain_ok(p)
    assert ok and n == 3, (ok, n, bad)
    # 篡改中间一行：链必须断裂
    with open(p, 'rb') as f:
        lines = f.read().split(b'\n')
    lines[1] = lines[1].replace(b'"i":1', b'"i":9')
    with open(p, 'wb') as f:
        f.write(b'\n'.join(lines))
    ok2, n2, bad2 = ledger_chain_ok(p)
    # 第 2 行被改后，第 3 行记录的 prev（指向原第 2 行）不再匹配，断点应在第 3 行
    assert not ok2 and bad2 == 3, (ok2, bad2)


def t_notes_sections_and_entries():
    txt = '\n'.join([
        '## B-dev-01-0001 | 行 1–5',
        '- [T] L1–L3: 「首行」 | 轮长=3',
        '- [C] L4: 「决定」',
        '- [A] L5: A2-0001 | 「名」',
        '[作废·块未提交]',
        '',
        '## B-dev-01-0001 | 行 1–5',
        '- [T] L1–L3: 「首行」 | 轮长=3',
        '- [C] L4–L5: 「决定」',
        '- [补记·拍4] [G] L5: abc1234',
        '',
        '## B-dev-01-0002 | 行 6–9',
        '- [M] L6–L9: 机械',
    ])
    secs, bad = commit_block.notes_sections(txt)
    assert not bad
    cand = [x for x in secs if x[0] == 'B-dev-01-0001' and not x[4]]
    assert len(cand) == 1, cand
    ents = commit_block.parse_entries(cand[0][3])
    assert [e['class'] for e in ents] == ['T', 'C', 'G'], ents
    assert ents[2]['addendum'] is True and ents[1]['e'] == 5


def t_git_whitelist():
    for sub in ('diff', 'log', 'show', 'blame', 'reflog'):
        try:
            common.git(sub)
            raise AssertionError('白名单未拒绝 git %s' % sub)
        except Blocked:
            pass
    rc, out, _ = common.git('rev-parse', 'HEAD')
    assert rc == 0 and len(out.strip()) == 40


def t_corpus_tags():
    pairs = common.corpus_paths()
    assert len(pairs) == 8 and len({t for t, _ in pairs}) == 8, pairs


def t_echo_check_fail_path():
    import echo_check
    p = os.path.join(WORKDIR, 'echo-short.txt')
    with open(p, 'wb') as f:
        f.write(b'x1\nx2\n')
    saved = echo_check.ECHO_LOG
    echo_check.ECHO_LOG = os.path.join(WORKDIR, 'echo-log-test.jsonl')
    try:
        rc = echo_check.check(p)
    finally:
        echo_check.ECHO_LOG = saved
    assert rc == 1
    rec = json.loads(open(os.path.join(WORKDIR, 'echo-log-test.jsonl'), encoding='utf-8').readline())
    assert rec['result'] == 'FAIL' and any('行数' in m for m in rec['mismatches']), rec


def main():
    if os.path.exists(WORKDIR):
        shutil.rmtree(WORKDIR)
    os.makedirs(WORKDIR)
    try:
        for name, fn in [('split_lines', t_split_lines), ('chunk_bytes', t_chunk_bytes),
                         ('plan_blocks_lines_limit', t_plan_blocks_lines),
                         ('plan_blocks_bytes_limit', t_plan_blocks_bytes),
                         ('method_A_shared_run_counted', t_method_a_shared_run),
                         ('method_A_short_run_not_counted', t_method_a_short_run_not_counted),
                         ('ledger_chain_detects_tamper', t_ledger_chain),
                         ('notes_sections_entries', t_notes_sections_and_entries),
                         ('git_whitelist_refuses_others', t_git_whitelist),
                         ('corpus_tags_eight', t_corpus_tags),
                         ('echo_check_fail_path', t_echo_check_fail_path)]:
            check(name, fn)
    finally:
        shutil.rmtree(WORKDIR, ignore_errors=True)
    overall = 'PASS' if all(r['result'] == 'PASS' for r in results) else 'FAIL'
    out = {'ts': common.now_utc(), 'overall': overall, 'tests': results, 'tool_files': sorted(
        x for x in os.listdir(TOOLS) if x.endswith('.py'))}
    with open(RESULT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')
    print('SELFTEST_%s %d/%d' % (overall, sum(1 for r in results if r['result'] == 'PASS'), len(results)))
    for r in results:
        if r['result'] != 'PASS':
            print('  FAIL %s: %s' % (r['test'], r.get('detail')))
    sys.exit(0 if overall == 'PASS' else 1)


if __name__ == '__main__':
    main()
