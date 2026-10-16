# -*- coding: utf-8 -*-
"""notes2、classes2、assets2 的分片读写（006 §2、§3、§5）。

逻辑文件名与拼接后的字节内容不变；物理上拆为 part 文件。分片表写入 shards/INDEX.json，
notes2 的分片表同时镜像到 notes2/INDEX.json（006 §2）。

用法：
  python3 -B -I tools/shards.py split                       一次性切分。原文件副本存入 shards/premigration/，
                                                            拼接校验通过后才删除原文件；写 SHARD_MIGRATION 记录。
  python3 -B -I tools/shards.py status                      打印分片表
  python3 -B -I tools/shards.py reindex                     按磁盘现状重建索引（仅在人工修补草稿分片之后使用）
  python3 -B -I tools/shards.py append <逻辑名> <源文件>    只追加（块边界规则见下）

块边界：切分只在块边界换片（notes2 的 "## B-" 行，classes2 的 "B-" 行，assets2 的 "| A2-" 行）；
整块不拆。末片超过 CAP 且新内容以块边界开头时，追加新开一片；否则追加到末片。
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import WORK, Blocked, ledger_append, now_utc, read_bytes, sha256_hex, write_json  # noqa: E402

CAP = 120 * 1024
SHARD_DIR = os.path.join(WORK, 'shards')
INDEX = os.path.join(SHARD_DIR, 'INDEX.json')
PREMIG = os.path.join(SHARD_DIR, 'premigration')
LOGICAL = ['notes2/dev-01.md', 'classes2/dev-01.tsv', 'assets2.md']
BOUNDARY = {'notes2/dev-01.md': b'## B-', 'classes2/dev-01.tsv': b'B-', 'assets2.md': b'| A2-'}


def split_lines(data):
    """按 LF 切行，保留行尾（与 002 §1 的口径一致，不依赖 splitlines 的其它分隔符）。"""
    out, pos = [], 0
    while pos < len(data):
        i = data.find(b'\n', pos)
        end = len(data) if i < 0 else i + 1
        out.append(data[pos:end])
        pos = end
    return out


def part_name(logical, k):
    d, base = os.path.split(logical)
    stem, ext = os.path.splitext(base)
    name = '%s.part-%02d%s' % (stem, k, ext)
    return os.path.join(d, name) if d else name


def load_index():
    if not os.path.exists(INDEX):
        return None
    return json.loads(read_bytes(INDEX).decode('utf-8'))


def block_ids(logical, text):
    """按逻辑文件返回块 ID 序列（用于分片表的首末块记录）。"""
    ids = []
    for ln in text.split('\n'):
        if logical == 'notes2/dev-01.md' and ln.startswith('## B-'):
            ids.append(ln.split(' |', 1)[0][3:])
        elif logical == 'classes2/dev-01.tsv' and ln.startswith('B-'):
            ids.append(ln.split('\t', 1)[0])
        elif logical == 'assets2.md' and ln.startswith('| A2-') and ln.count('|') >= 9:
            ids.append(ln.split('|')[8].strip())
    uniq = []
    for x in ids:
        if x and (not uniq or uniq[-1] != x):
            uniq.append(x)
    return uniq


def entry_for(logical, plist):
    parts, total = [], b''
    for pf in plist:
        b = read_bytes(os.path.join(WORK, pf))
        total += b
        ids = block_ids(logical, b.decode('utf-8'))
        parts.append({'file': pf, 'bytes': len(b), 'sha256': sha256_hex(b), 'lines': b.count(b'\n'),
                      'first_block': ids[0] if ids else None, 'last_block': ids[-1] if ids else None})
    return {'parts': parts, 'total_bytes': len(total), 'sha256': sha256_hex(total)}


def save_index(idx):
    os.makedirs(SHARD_DIR, exist_ok=True)
    for logical in LOGICAL:
        plist = [p['file'] for p in idx['files'][logical]['parts']]
        idx['files'][logical] = entry_for(logical, plist)
    idx['updated'] = now_utc()
    write_json(INDEX, idx)
    notes = dict(idx['files']['notes2/dev-01.md'])
    notes.update({'logical': 'notes2/dev-01.md', 'cap_bytes': CAP})
    write_json(os.path.join(WORK, 'notes2', 'INDEX.json'), notes)


def parts_of(logical):
    idx = load_index()
    if idx is None or logical not in idx['files']:
        return [logical]
    return [p['file'] for p in idx['files'][logical]['parts']]


def read_logical(logical):
    return b''.join(read_bytes(os.path.join(WORK, p)) for p in parts_of(logical))


def read_text_logical(logical):
    return read_logical(logical).decode('utf-8')


def append_logical(logical, data):
    idx = load_index()
    if idx is None or logical not in idx['files']:
        raise Blocked('未切分的逻辑文件不得按分片追加：%s' % logical)
    plist = idx['files'][logical]['parts']
    cur = plist[-1]['file']
    if os.path.getsize(os.path.join(WORK, cur)) >= CAP and data.startswith(BOUNDARY[logical]):
        cur = part_name(logical, len(plist) + 1)
        open(os.path.join(WORK, cur), 'wb').close()
        plist.append({'file': cur})
    with open(os.path.join(WORK, cur), 'ab') as f:
        f.write(data)
    save_index(idx)
    return cur


def split():
    if load_index() is not None:
        raise Blocked('已切分，不得重复切分')
    os.makedirs(PREMIG, exist_ok=True)
    idx = {'schema': 'gui-asset-reaudit/shards/v1', 'cap_bytes': CAP, 'files': {}}
    pre = {}
    for logical in LOGICAL:
        data = read_bytes(os.path.join(WORK, logical))
        pre[logical] = {'bytes': len(data), 'sha256': sha256_hex(data)}
        chunks, cur = [], b''
        for ln in split_lines(data):
            if cur and len(cur) >= CAP and ln.startswith(BOUNDARY[logical]):
                chunks.append(cur)
                cur = b''
            cur += ln
        if cur:
            chunks.append(cur)
        assert b''.join(chunks) == data, logical
        plist = []
        for k, ch in enumerate(chunks, 1):
            pf = part_name(logical, k)
            with open(os.path.join(WORK, pf), 'wb') as f:
                f.write(ch)
            plist.append(pf)
        idx['files'][logical] = {'parts': [{'file': p} for p in plist]}
        with open(os.path.join(PREMIG, logical.replace('/', '__')), 'wb') as f:
            f.write(data)
    save_index(idx)
    for logical in LOGICAL:
        orig = read_bytes(os.path.join(PREMIG, logical.replace('/', '__')))
        assert read_logical(logical) == orig, 'split 拼接与原文件不一致：' + logical
        assert idx['files'][logical]['sha256'] == pre[logical]['sha256'], logical
    for logical in LOGICAL:
        os.remove(os.path.join(WORK, logical))
    parts_txt = '；'.join('%s %d 片 %d 字节' % (lg, len(idx['files'][lg]['parts']), idx['files'][lg]['total_bytes'])
                      for lg in LOGICAL)
    ledger_append({'type': 'NOTE', 'kind': 'SHARD_MIGRATION',
                   'detail': '按 006 §2 切分 notes2、classes2、assets2（每片约 %d KB，只在块边界换片，整块不拆）。切分前：%s。切分后拼接与原文件逐字节相同（sha256 一致），原文件副本存 shards/premigration/，之后删除单文件。分片表：shards/INDEX.json；notes2/INDEX.json。' % (
                       CAP // 1024, '；'.join('%s %d 字节 sha256=%s' % (k, v['bytes'], v['sha256']) for k, v in pre.items())),
                   'ref': 'shards/INDEX.json；shards/premigration/；notes2/INDEX.json'})
    print('SPLIT_DONE ' + parts_txt)


def status():
    idx = load_index()
    if idx is None:
        print('UNSHARDED')
        return
    for logical in LOGICAL:
        e = idx['files'][logical]
        print('%s total=%d sha256=%s' % (logical, e['total_bytes'], e['sha256']))
        for p in e['parts']:
            print('  %s bytes=%d blocks=%s..%s' % (p['file'], p['bytes'], p['first_block'], p['last_block']))


def main(argv):
    if argv == ['split']:
        split()
        return
    if argv == ['status']:
        status()
        return
    if argv == ['reindex']:
        idx = load_index()
        if idx is None:
            raise Blocked('未切分，无可重建的索引')
        save_index(idx)
        print('REINDEXED')
        return
    if len(argv) == 3 and argv[0] == 'append':
        data = read_bytes(argv[2])
        cur = append_logical(argv[1], data)
        print('APPENDED %s bytes=%d part=%s' % (argv[1], len(data), cur))
        return
    raise Blocked('用法：shards.py split | status | append <逻辑名> <源文件>')


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Blocked as ex:
        print('BLOCKED: %s' % ex)
        sys.exit(2)
