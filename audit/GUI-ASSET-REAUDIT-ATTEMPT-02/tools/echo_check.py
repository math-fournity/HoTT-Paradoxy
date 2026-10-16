# -*- coding: utf-8 -*-
"""protocol-echo 校验（SOP 005 §4 第 4 步、§5）。

用法：
  python3 -B -I tools/echo_check.py locate
      对 PROTOCOL-ANCHORS2.json 的 8 条锚，在其所指的 SOP 文件中定位匹配行的行号（只输出行号，不输出行文）。
      用于核对锚表与规范文件的对应关系；不替代执行者在上下文中逐字复制（SOP 005 §5）。
  python3 -B -I tools/echo_check.py check echo/<时间戳>.txt
      核对 echo 文件：行数与顺序须与锚表一致，每行 UTF-8 字节（不含换行）的 SHA-256 须与对应锚相等。
      结果追加写入 echo-log2.jsonl；FAIL 时退出码为 1。
"""
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import ROOT, WORK, Blocked, load_json, now_utc, read_bytes, sha256_hex  # noqa: E402
import json  # noqa: E402

ANCHORS = os.path.join(WORK, 'PROTOCOL-ANCHORS2.json')
ECHO_LOG = os.path.join(WORK, 'echo-log2.jsonl')


def anchors():
    return load_json(ANCHORS)['anchors']


def locate():
    out = []
    cache = {}
    for a in anchors():
        f = a['file']
        if f not in cache:
            data = read_bytes(os.path.join(ROOT, f))
            # 行为 LF 切分后的整行（不含 LF），与锚的定义一致
            cache[f] = [ln for ln in data.split(b'\n')]
        hits = [i + 1 for i, ln in enumerate(cache[f]) if hashlib.sha256(ln).hexdigest() == a['sha256']]
        out.append({'id': a['id'], 'file': f, 'lines': hits, 'hit_count': len(hits)})
    res = {'ts': now_utc(), 'mode': 'locate', 'results': out,
           'all_found_once': all(x['hit_count'] == 1 for x in out)}
    print(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True))
    return 0 if res['all_found_once'] else 1


def check(echo_path):
    an = anchors()
    with open(echo_path, 'rb') as f:
        raw = f.read()
    lines = raw.split(b'\n')
    if raw.endswith(b'\n'):
        lines = lines[:-1]
    mismatches = []
    if len(lines) != len(an):
        mismatches.append('行数 %d 与锚数 %d 不符' % (len(lines), len(an)))
    for i, a in enumerate(an):
        if i >= len(lines):
            break
        if hashlib.sha256(lines[i]).hexdigest() != a['sha256']:
            mismatches.append('第 %d 行（锚 %s）哈希不符' % (i + 1, a['id']))
    result = 'OK' if not mismatches else 'FAIL'
    rec = {'ts': now_utc(), 'echo_file': os.path.relpath(echo_path, WORK), 'echo_sha256': sha256_hex(raw),
           'result': result, 'mismatches': mismatches, 'anchor_count': len(an)}
    with open(ECHO_LOG, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + '\n')
    print('ECHO_%s %s' % (result, rec['echo_file']))
    for m in mismatches:
        print('  - ' + m)
    return 0 if result == 'OK' else 1


def main(argv):
    if argv == ['locate']:
        sys.exit(locate())
    if len(argv) == 2 and argv[0] == 'check':
        sys.exit(check(argv[1]))
    raise Blocked('用法：echo_check.py locate | check <echo 文件>')


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Blocked as ex:
        print('BLOCKED: %s' % ex)
        sys.exit(2)
