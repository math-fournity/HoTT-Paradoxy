# -*- coding: utf-8 -*-
"""拍 1 读取记录（SOP 003 §3；006 §4）：只在本块 GATE 之后、拍 1 整读之后运行。

用法：python3 -B -I tools/beat1.py <BLOCK> <start> <end> <returned_end>
写入 reread-state/<BLOCK>.json 的 beat1 字段；已有记录则拒绝覆盖（草稿须先按第 9 步作废）。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402


def main(argv):
    if len(argv) != 4:
        raise C.Blocked('用法：beat1.py <BLOCK> <start> <end> <returned_end>')
    block = argv[0]
    s, e, ret = int(argv[1]), int(argv[2]), int(argv[3])
    info = [b for b in C.load_blocks() if b['block'] == block]
    if not info:
        raise C.Blocked('blocks.json 中没有该块：%s' % block)
    b = info[0]
    if (s, e) != (b['start'], b['end']) or ret != e:
        raise C.Blocked('拍 1 区间须为块区间 %d-%d 且返回末行等于块末行' % (b['start'], b['end']))
    recs = [r for r, _ in C.ledger_records()]
    rs_idx = [i for i, r in enumerate(recs) if r.get('type') == 'RS']
    if not any(r.get('type') == 'GATE' and r.get('block') == block and i > rs_idx[-1]
               for i, r in enumerate(recs)):
        raise C.Blocked('%s 没有本 RS 之后的 GATE 记录，不得开始拍 1' % block)
    path = os.path.join(C.WORK, 'reread-state', block + '.json')
    if os.path.exists(path):
        raise C.Blocked('reread-state 已有记录，不得覆盖：%s' % path)
    os.makedirs(os.path.join(C.WORK, 'reread-state'), exist_ok=True)
    ts = C.now_utc()
    C.write_json(path, {'beat1': {'end': e, 'returned_end': ret, 'start': s,
                                  'tool': 'Read offset=%d limit=200（拍 1）' % s, 'ts': ts},
                        'block': block, 'ts': ts})
    print('BEAT1_RECORDED %s %d-%d' % (block, s, e))


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except C.Blocked as ex:
        print('BLOCKED: %s' % ex)
        sys.exit(2)
