# -*- coding: utf-8 -*-
"""GATE（006 §4）：每块拍 1 之前运行。通过则在账本写入 GATE 记录（含时间与所依 RS 的编号）。

用法：python3 -B -I tools/gate.py <BLOCK>
检查：账本链完整；存在 RS 收据；本块尚未提交；分片核对与全部已提交块的哈希重算通过（verify_shards）；
      本块没有未作废的草稿节，classes2 与 assets2 中也没有本块的行。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import shards  # noqa: E402
import commit_block as CB  # noqa: E402
import verify_shards as VS  # noqa: E402


def main(argv):
    if len(argv) != 1:
        raise C.Blocked('用法：gate.py <BLOCK>')
    block = argv[0]
    ok, n, bad = C.ledger_chain_ok()
    if not ok:
        raise C.Blocked('账本链断裂（行 %s），GATE 不通过' % bad)
    recs = [r for r, _ in C.ledger_records()]
    rs_idx = [i for i, r in enumerate(recs) if r.get('type') == 'RS']
    if not rs_idx:
        raise C.Blocked('账本中没有 RS 收据，GATE 不通过')
    last_rs = recs[rs_idx[-1]]
    if any(r.get('type') == 'RA' and r.get('block') == block for r in recs):
        raise C.Blocked('%s 已提交，不得再次 GATE' % block)
    info = [b for b in C.load_blocks() if b['block'] == block]
    if not info:
        raise C.Blocked('blocks.json 中没有该块：%s' % block)
    tag = info[0]['tag']
    ierr = VS.index_errors()
    if ierr:
        raise C.Blocked('分片核对失败：%s' % '；'.join(ierr))
    all_ok, rows, bad_hdr = VS.block_rows()
    if not all_ok or bad_hdr:
        raise C.Blocked('已提交块的哈希重算未全部通过（见 shard-verify.json，先运行 verify_shards.py）')
    secs, _ = CB.notes_sections(shards.read_text_logical('notes2/dev-01.md'))
    live = [x for x in secs if x[0] == block and not x[4]]
    if live:
        raise C.Blocked('%s 已有未作废的草稿节，须先按 005 §4 第 9 步作废' % block)
    live_rows = CB.class_rows(tag, block, [])
    live_assets = [x for x in CB.parse_assets() if x.get('block') == block]
    if live_rows or live_assets:
        raise C.Blocked('%s 的 classes2 或 assets2 中已有草稿行，须先移出' % block)
    C.ledger_append({'type': 'GATE', 'block': block, 'tag': tag, 'rs': last_rs['boundary_id'],
                     'rs_ledger_index': rs_idx[-1] + 1,
                     'checks': {'chain_ok': True, 'ledger_records': n, 'shards': 'PASS',
                                'committed_blocks_verified': len(rows), 'live_draft_sections': 0,
                                'live_rows': 0}})
    print('GATE_PASS %s rs=%s ledger_records=%d' % (block, last_rs['boundary_id'], n))


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except C.Blocked as ex:
        print('GATE_BLOCKED: %s' % ex)
        sys.exit(2)
