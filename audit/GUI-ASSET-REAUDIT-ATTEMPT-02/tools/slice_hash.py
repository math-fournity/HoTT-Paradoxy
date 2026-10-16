# -*- coding: utf-8 -*-
"""按 SOP 002 §1 计算任意 (tag, s, e) 的块哈希（chunk_sha256）。

用法：python3 -B -I tools/slice_hash.py <tag> <s> <e>
输出 JSON。各工具通过 chunk_sha256_of() 复用，不另写切片逻辑（002 §7 第 3 条）。
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import Blocked, chunk_bytes, load_corpus_lines, load_manifest, sha256_hex  # noqa: E402


def chunk_sha256_of(manifest, tag, s, e):
    data, lines = load_corpus_lines(manifest, tag)
    sl = chunk_bytes(data, lines, s, e)
    return {'tag': tag, 's': s, 'e': e, 'bytes': len(sl), 'chunk_sha256': sha256_hex(sl),
            'max_line_bytes': max(len(x[1]) for x in lines[s - 1:e]) if e >= s else 0}


def main(argv):
    if len(argv) != 3:
        raise Blocked('用法：slice_hash.py <tag> <s> <e>')
    tag, s, e = argv[0], int(argv[1]), int(argv[2])
    print(json.dumps(chunk_sha256_of(load_manifest(), tag, s, e), ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Blocked as ex:
        print('BLOCKED: %s' % ex)
        sys.exit(2)
