# -*- coding: utf-8 -*-
"""总校验（SOP 002 §7 第 7 条；004 §1；005 §4 第 6 步）。

用法：python3 -B -I tools/check_all.py --chain-only
      链校验：核对 ledger2.jsonl 的 prev 链；按账本哈希确定性抽取 3 个 RA，重算其 chunk_sha256。
      结果写入 check-all-chain.json。全量模式（阶段 B 的 B-01 至 B-14）尚未实现，调用即拒绝。
"""
import hashlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (LEDGER, WORK, Blocked, chunk_bytes, ledger_chain_ok, ledger_records,  # noqa: E402
                    load_blocks, load_corpus_lines, load_manifest, now_utc, read_bytes, sha256_hex,
                    verify_corpus, write_json)


def chain_only():
    ok, n, bad = ledger_chain_ok()
    recs = [r for r, _ in ledger_records() if r.get('type') == 'RA']
    seed = hashlib.sha256(read_bytes(LEDGER) if os.path.exists(LEDGER) else b'').hexdigest()
    picks = []
    if recs:
        idxs = []
        for k in range(0, 3 * 8, 8):
            idxs.append(int(seed[k:k + 8], 16) % len(recs))
        seen = []
        for i in idxs:
            if i not in seen:
                seen.append(i)
        picks = seen
    manifest = load_manifest()
    verify_corpus(manifest)
    blocks = {b['block']: b for b in load_blocks()}
    sampled = []
    all_ok = ok
    for i in picks:
        r = recs[i]
        b = blocks.get(r['block'])
        data, lines = load_corpus_lines(manifest, r['tag'])
        sl = chunk_bytes(data, lines, r['start'], r['end'])
        good = (sha256_hex(sl) == r['chunk_sha256']) and b is not None and b['chunk_sha256'] == r['chunk_sha256']
        all_ok = all_ok and good
        sampled.append({'rid': r['rid'], 'block': r['block'], 'recomputed_ok': good})
    out = {'mode': 'chain-only', 'ts': now_utc(), 'ledger_records': n, 'chain_ok': ok,
           'chain_break_line': bad, 'ra_count': len(recs), 'seed_sha256': seed,
           'sampled': sampled, 'result': 'PASS' if all_ok else 'FAIL'}
    write_json(os.path.join(WORK, 'check-all-chain.json'), out)
    print('CHAIN_%s records=%d ra=%d sampled=%d' % (out['result'], n, len(recs), len(sampled)))
    return 0 if all_ok else 1


def main(argv):
    if argv == ['--chain-only']:
        sys.exit(chain_only())
    raise Blocked('全量模式（B-01 至 B-14）尚未实现；阶段 B 前须先写入并通过自测')


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Blocked as ex:
        print('BLOCKED: %s' % ex)
        sys.exit(2)
