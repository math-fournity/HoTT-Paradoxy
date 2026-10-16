# -*- coding: utf-8 -*-
"""拍 4 复读记录（SOP 003 §3 拍 4；002 §7 第 5 条）。

用法：python3 -B -I tools/reread.py <BLOCK> --status PASS|FAIL --addenda N \
          --second-start S --second-end E --returned-end R

前提：拍 1 的读取记录已写入 reread-state/<BLOCK>.json 的 beat1 字段（由块提交前的 Bash 步骤写入）。
本工具只补写 beat4、status、addenda；返回末行不等于块末行、或状态为 FAIL 时，退出码为 1。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import WORK, Blocked, load_json, now_utc, write_json  # noqa: E402

REREAD_DIR = os.path.join(WORK, 'reread-state')


def main(argv):
    if not argv:
        raise Blocked('用法错误')
    block = argv[0]
    opts = {}
    i = 1
    while i < len(argv):
        k = argv[i]
        if not k.startswith('--') or i + 1 >= len(argv):
            raise Blocked('参数错误：%r' % k)
        opts[k[2:]] = argv[i + 1]
        i += 2
    need = ('status', 'addenda', 'second-start', 'second-end', 'returned-end')
    for k in need:
        if k not in opts:
            raise Blocked('缺少参数 --%s' % k)
    path = os.path.join(REREAD_DIR, block + '.json')
    if not os.path.exists(path):
        raise Blocked('拍 1 读取记录缺失（reread-state/%s.json），不得记复读' % block)
    rr = load_json(path)
    if 'beat1' not in rr:
        raise Blocked('拍 1 读取记录缺失（beat1）')
    s, e = int(opts['second-start']), int(opts['second-end'])
    ret = int(opts['returned-end'])
    status = opts['status']
    if status not in ('PASS', 'FAIL'):
        raise Blocked('status 只能是 PASS 或 FAIL')
    if not (s == rr['beat1']['start'] and e == rr['beat1']['end']):
        status = 'FAIL'
    if ret != e:
        status = 'FAIL'
    rr['beat4'] = {'start': s, 'end': e, 'returned_end': ret, 'ts': now_utc()}
    rr['status'] = status
    rr['addenda'] = int(opts['addenda'])
    rr['ts'] = now_utc()
    os.makedirs(REREAD_DIR, exist_ok=True)
    write_json(path, rr)
    print('REREAD %s status=%s addenda=%d' % (block, status, rr['addenda']))
    sys.exit(0 if status == 'PASS' else 1)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Blocked as ex:
        print('BLOCKED: %s' % ex)
        sys.exit(2)
