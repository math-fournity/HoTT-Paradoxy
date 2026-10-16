# -*- coding: utf-8 -*-
"""游标与状态（SOP 002 §7 第 6 条；005 §4 第 3 步）。

用法：python3 -B -I tools/cursor.py            打印下一个未提交块
      python3 -B -I tools/cursor.py --refresh  刷新 STATUS.md（由工具生成，不手工编辑）
游标只从 ledger2.jsonl 的 RA 收据与 blocks.json 算出，不凭记忆。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (STATUS, Blocked, GENESIS, ledger_chain_ok, ledger_records,  # noqa: E402
                    load_blocks, load_json, now_utc, seal_events, BLOCKS, MANIFEST)


def phase():
    ph = 'S0/启动（尚无 STAGE 事件）'
    for ev in seal_events():
        if ev.get('event') in ('STAGE_START', 'STAGE_DONE', 'UNSEAL'):
            ph = '%s %s' % (ev['event'], ev.get('stage', ''))
            ph = ph.strip()
    return ph


def next_block():
    done = {r['block'] for r, _ in ledger_records() if r.get('type') == 'RA'}
    for b in load_blocks():
        if b['block'] not in done:
            return b
    return None


def refresh():
    blocks = load_blocks()
    recs = ledger_records()
    ra = [r for r, _ in recs if r.get('type') == 'RA']
    done = {r['block'] for r in ra}
    ok, n, bad = ledger_chain_ok()
    m = load_json(MANIFEST) if os.path.exists(MANIFEST) else {'head': '-', 'files': []}
    per = {}
    for b in blocks:
        t = per.setdefault(b['tag'], {'blocks': 0, 'done_blocks': 0, 'N': 0, 'done_rows': 0})
        t['blocks'] += 1
        t['N'] += b['obligation_count']
        if b['block'] in done:
            t['done_blocks'] += 1
            t['done_rows'] += b['obligation_count']
    nxt = next_block()
    lines = [
        '# STATUS（由 tools/cursor.py --refresh 生成；勿手工编辑）',
        '',
        '- 生成时间（UTC）：%s' % now_utc(),
        '- 语料 HEAD（manifest2）：%s' % m.get('head', '-'),
        '- 当前阶段（seal-log 最后的 STAGE/UNSEAL）：%s' % phase(),
        '- 已提交块：%d / %d' % (len(done), len(blocks)),
        '- 下一块（游标）：%s' % (nxt['block'] if nxt else '无（全部块已提交）'),
        '- 最近 RA：%s' % (ra[-1]['rid'] + ' ' + ra[-1]['block'] if ra else '无'),
        '- 账本：%d 条，prev 链 %s%s' % (n, '完整' if ok else '断裂', '' if ok else '（断点行 %s）' % bad),
        '- 账本首条 prev 应为 %s' % GENESIS,
        '',
        '## 各文件进度',
        '',
        '| tag | 块数 | 已提交块 | 义务行 N | 已提交义务行 |',
        '|---|---:|---:|---:|---:|',
    ]
    for tag in m.get('order', sorted(per)):
        t = per.get(tag, {'blocks': 0, 'done_blocks': 0, 'N': 0, 'done_rows': 0})
        lines.append('| %s | %d | %d | %d | %d |' % (tag, t['blocks'], t['done_blocks'], t['N'], t['done_rows']))
    lines += ['', '（A_DONE 仅在全部块提交且 FILE_DONE2 齐备后才可标注；见 SOP 003 §8。）', '']
    with open(STATUS, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    return nxt


def main(argv):
    if '--refresh' in argv:
        nxt = refresh()
        print('STATUS_REFRESHED next=%s' % (nxt['block'] if nxt else 'NONE'))
        return
    nxt = next_block()
    print(nxt['block'] if nxt else 'NONE')


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Blocked as ex:
        print('BLOCKED: %s' % ex)
        sys.exit(2)
