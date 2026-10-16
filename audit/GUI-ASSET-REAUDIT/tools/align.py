# -*- coding: utf-8 -*-
"""P1 对齐与分块（SOP 002 §3 至 §5）。写 align2.json、align-disagree.jsonl、pointers.json、blocks.json。

本次运行的已登记处置（见 SESSION-REAUDIT.md §4、ledger2 的 NOTE SOP_CONFLICT）：
  - 方法 A（K-gram）按 SOP 002 §3.3 运行，但只作信息性统计（估计重复比例），不用于减少义务行；
    K-gram 索引每个键只保留最近 8 次出现（上限），因此它的覆盖数是下界式的估计。
  - 方法 B（git diff 法）不运行：SOP 002 §3.4 要求 `git diff`，超出目标的 git 白名单。
  - 因方法 B 缺失，SHARED 无法按 SOP 002 §3.1 的交集建立；依目标的"疑则读之、选严"规则，
    SHARED 置为空集，UNIQUE 为全部行。块划分按 SOP 002 §4 的上限在 UNIQUE 上进行。
用法：python3 -B -I tools/align.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (ALIGN, BLOCK_MAX_BYTES, BLOCK_MAX_LINES, BLOCKS, K, WORK,  # noqa: E402
                    Blocked, chunk_bytes, load_manifest, now_utc, read_bytes, verify_corpus,
                    write_json, split_lines, ROOT, seal_append)
import hashlib  # noqa: E402
import json  # noqa: E402

INDEX_CAP = 8
POINTERS = os.path.join(WORK, 'pointers.json')
DISAGREE = os.path.join(WORK, 'align-disagree.jsonl')
RUNS_A = os.path.join(WORK, 'align-runs-A.jsonl')


def digest(line):
    return hashlib.sha256(line).digest()


def method_a(manifest):
    """方法 A（信息性）：K-gram 索引，只与更早的文件比较；返回每文件的覆盖掩码与 run 列表。"""
    index = {}
    results = {}
    runs_out = []
    for tag in manifest['order']:
        fe = next(x for x in manifest['files'] if x['tag'] == tag)
        data = read_bytes(os.path.join(ROOT, fe['path']))
        lines = split_lines(data)
        fps = [digest(x[1]) for x in lines]
        N = len(fps)
        covered = bytearray(N)
        last_end = {}
        nruns = 0
        maxrun = 0
        for i in range(0, N - K + 1):
            key = tuple(fps[i:i + K])
            hits = index.get(key)
            if not hits:
                continue
            for (gtag, gfps, j) in hits:
                diag = (gtag, j - i)
                if last_end.get(diag, -1) > i:
                    continue
                Ng = len(gfps)
                L = K
                while i + L < N and j + L < Ng and fps[i + L] == gfps[j + L]:
                    L += 1
                b = 0
                while i - b - 1 >= 0 and j - b - 1 >= 0 and fps[i - b - 1] == gfps[j - b - 1]:
                    b += 1
                start = i - b
                end = i + L
                for p in range(start, end):
                    covered[p] = 1
                last_end[diag] = end
                nruns += 1
                maxrun = max(maxrun, end - start)
                runs_out.append({'f': tag, 'f_start': start + 1, 'f_end': end, 'g': gtag,
                                 'g_start': j - b + 1, 'length': end - start})
        results[tag] = {'N': N, 'covered': sum(covered), 'runs': nruns, 'max_run': maxrun,
                        'mask': covered}
        # 把本文件加入索引（只供之后的文件比较）
        for i in range(0, N - K + 1):
            key = tuple(fps[i:i + K])
            lst = index.setdefault(key, [])
            lst.append((tag, fps, i))
            if len(lst) > INDEX_CAP:
                del lst[0]
    return results, runs_out


def plan_blocks(lines, data_len):
    """SOP 002 §4：在 UNIQUE 段上按 200 行或 40 KB（先到者）切块。这里 UNIQUE 为全部行。"""
    N = len(lines)

    def off(k):
        return lines[k - 1][0] if k <= N else data_len

    spans = []
    s = 1
    while s <= N:
        e = s
        while e + 1 <= N and (e + 1 - s + 1) <= BLOCK_MAX_LINES and (off(e + 2) - off(s)) <= BLOCK_MAX_BYTES:
            e += 1
        spans.append((s, e))
        s = e + 1
    return spans


def main():
    manifest = load_manifest()
    verify_corpus(manifest)
    results, runs_a = method_a(manifest)
    blocks = []
    per_file = {}
    covered_rows = 0
    for tag in manifest['order']:
        fe = next(x for x in manifest['files'] if x['tag'] == tag)
        data = read_bytes(os.path.join(ROOT, fe['path']))
        lines = split_lines(data)
        N = len(lines)
        spans = plan_blocks(lines, len(data))
        for idx, (s, e) in enumerate(spans, start=1):
            sl = chunk_bytes(data, lines, s, e)
            blocks.append({
                'block': 'B-%s-%04d' % (tag, idx), 'tag': tag, 'start': s, 'end': e,
                'obligation': [[s, e]], 'obligation_count': e - s + 1, 'context_seam': [],
                'bytes': len(sl), 'chunk_sha256': hashlib.sha256(sl).hexdigest(),
                'max_line_bytes': max(len(x[1]) for x in lines[s - 1:e]),
            })
        per_file[tag] = {'N': N, 'shared': 0, 'unique': N, 'blocks': len(spans),
                         'method_A_informational_covered': results[tag]['covered'],
                         'method_A_runs': results[tag]['runs'],
                         'method_A_max_run': results[tag]['max_run']}
        covered_rows += results[tag]['covered']
    T = sum(v['N'] for v in per_file.values())
    sum_shared = sum(v['shared'] for v in per_file.values())
    sum_unique = sum(v['unique'] for v in per_file.values())
    assert sum_shared + sum_unique == T
    # P1 自检：块义务之和等于各文件 UNIQUE 之和；块之间义务不重叠
    obl = sum(b['obligation_count'] for b in blocks)
    if obl != sum_unique:
        raise Blocked('块义务之和 %d 与 UNIQUE 之和 %d 不符' % (obl, sum_unique))
    seen = {}
    for b in blocks:
        for r in range(b['start'], b['end'] + 1):
            key = (b['tag'], r)
            if key in seen:
                raise Blocked('义务行重叠：%s' % (key,))
            seen[key] = b['block']
    if len(seen) != T:
        raise Blocked('块覆盖不全：%d / %d' % (len(seen), T))
    align = {
        'schema': 'gui-asset-reaudit/align2/v1', 'frozen_at': now_utc(),
        'manifest_fingerprint': manifest['fingerprint'], 'T': T,
        'method_A': {'K': K, 'index_cap_per_key': INDEX_CAP, 'scope': 'earlier files only',
                     'use': 'INFORMATIONAL_ONLY', 'covered_total': covered_rows},
        'method_B': {'status': 'NOT_RUN',
                     'reason': 'SOP_CONFLICT：SOP 002 §3.4 要求 git diff，超出目标的 git 白名单；见 SESSION-REAUDIT.md §4'},
        'shared_policy': 'EMPTY_BY_FALLBACK：交集无法建立，依"疑则读之、选严"，全部行为义务行',
        'per_file': per_file,
        'structure_assertions': {'SHARED_union_UNIQUE_eq_T': sum_shared + sum_unique == T,
                                 'sum_N_eq_T': sum(v['N'] for v in per_file.values()) == T,
                                 'block_obligation_sum_eq_unique': obl == sum_unique,
                                 'no_overlap_across_blocks': True},
        'blocks_total': len(blocks),
        'tool': 'tools/align.py',
    }
    write_json(ALIGN, align)
    write_json(BLOCKS, {'schema': 'gui-asset-reaudit/blocks/v1', 'frozen': True,
                        'order': manifest['order'], 'blocks': blocks})
    write_json(POINTERS, {'schema': 'gui-asset-reaudit/pointers/v1', 'pointers': {},
                          'note': 'SHARED 为空（方法 B 未运行，见 SESSION §4），无指针'})
    with open(DISAGREE, 'w', encoding='utf-8') as f:
        f.write('')
    with open(RUNS_A, 'w', encoding='utf-8') as f:
        for r in runs_a:
            f.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n')
    # 重新加载核对计数（002 §5）
    chk = json.load(open(BLOCKS, 'r', encoding='utf-8'))
    if len(chk['blocks']) != len(blocks):
        raise Blocked('blocks.json 回读计数不一致')
    print('ALIGN_OK T=%d blocks=%d method_A_covered(info)=%d unique=%d shared=0' % (
        T, len(blocks), covered_rows, sum_unique))


if __name__ == '__main__':
    try:
        main()
    except Blocked as ex:
        print('BLOCKED: %s' % ex)
        sys.exit(2)
