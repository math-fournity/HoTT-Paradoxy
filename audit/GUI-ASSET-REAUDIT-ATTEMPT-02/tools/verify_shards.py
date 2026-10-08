# -*- coding: utf-8 -*-
"""分片核对（006 §5）：索引与磁盘一致；每个已提交块的 chunk、notes、classes、assets 哈希按 commit_block 口径重算。

用法：python3 -B -I tools/verify_shards.py
      结果写入 shard-verify.json（每块一行）；全部通过退出码 0，否则 1。
GATE（tools/gate.py）与 CL-BR2 第 7 步、CL-E2 均须运行本工具。
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C  # noqa: E402
import shards  # noqa: E402
import commit_block as CB  # noqa: E402

OUT = os.path.join(C.WORK, 'shard-verify.json')


def index_errors():
    idx = shards.load_index()
    if idx is None:
        raise C.Blocked('尚未切分（无 shards/INDEX.json）')
    errs = []
    for logical, entry in idx['files'].items():
        data = b''
        for p in entry['parts']:
            b = C.read_bytes(os.path.join(C.WORK, p['file']))
            if C.sha256_hex(b) != p['sha256'] or len(b) != p['bytes']:
                errs.append('part 与索引不符：%s' % p['file'])
            data += b
        if C.sha256_hex(data) != entry['sha256'] or len(data) != entry['total_bytes']:
            errs.append('逻辑文件与索引不符：%s' % logical)
    return errs


def committed_raw(data, block):
    """已提交块的 notes 原始字节：该块最后一个未作废节，自标题行起至下一个节标题行前（含行尾换行）。
    RA 的 notes_sha256 在提交时取自文件末尾的节正文（即此原始字节）；此后只在文件末尾追加新节。"""
    lines = shards.split_lines(data)
    hdr = [k for k, ln in enumerate(lines) if ln.startswith(b'## B-')]
    best = None
    for n, k in enumerate(hdr):
        j = hdr[n + 1] if n + 1 < len(hdr) else len(lines)
        if lines[k].decode('utf-8').split(' |', 1)[0][3:] != block:
            continue
        if any(x.startswith('[作废'.encode('utf-8')) for x in lines[k:j]):
            continue
        best = (k, j)
    return None if best is None else b''.join(lines[best[0]:best[1]])


def block_rows():
    manifest = C.load_manifest()
    C.verify_corpus(manifest)
    notes_bytes = shards.read_logical('notes2/dev-01.md')
    _, bad = CB.notes_sections(notes_bytes.decode('utf-8'))
    rows = []
    all_ok = not bad
    for r, _ in C.ledger_records():
        if r.get('type') != 'RA':
            continue
        block, tag = r['block'], r['tag']
        errs = []
        data, lines = C.load_corpus_lines(manifest, tag)
        sl = C.chunk_bytes(data, lines, r['start'], r['end'])
        if C.sha256_hex(sl) != r['chunk_sha256'] or len(sl) != r['bytes']:
            errs.append('chunk_sha256/bytes')
        raw = committed_raw(notes_bytes, block)
        if raw is None or C.sha256_hex(raw) != r['notes_sha256']:
            errs.append('notes_sha256')
        cerr = []
        crow = CB.class_rows(tag, block, cerr)
        crow.sort(key=lambda x: (x['start'], x['end']))
        cls = '\n'.join('%d\t%d\t%s\t%s' % (x['start'], x['end'], x['class'], x['ref']) for x in crow)
        if cerr or C.sha256_hex(cls.encode('utf-8')) != r['classes_sha256']:
            errs.append('classes_sha256')
        arows = [x for x in CB.parse_assets() if x.get('block') == block]
        ast = '\n'.join(json.dumps(x, ensure_ascii=False, sort_keys=True) for x in arows)
        if C.sha256_hex(ast.encode('utf-8')) != r['assets_sha256']:
            errs.append('assets_sha256')
        if [x['ID'] for x in arows] != r.get('assets_ids'):
            errs.append('assets_ids')
        rows.append({'block': block, 'rid': r['rid'], 'ok': not errs, 'errors': errs})
        all_ok = all_ok and not errs
    return all_ok, rows, bad


def main(argv):
    if argv:
        raise C.Blocked('用法：verify_shards.py（无参数）')
    ierr = index_errors()
    all_ok, rows, bad = block_rows()
    result = 'PASS' if (not ierr and all_ok) else 'FAIL'
    write = {'ts': C.now_utc(), 'result': result, 'index_errors': ierr, 'notes_header_errors': bad,
             'blocks': rows}
    C.write_json(OUT, write)
    print('SHARD_VERIFY_%s blocks=%d failed=%d index_errors=%d' % (
        result, len(rows), sum(1 for x in rows if not x['ok']), len(ierr)))
    for x in rows:
        if not x['ok']:
            print('  - %s %s %s' % (x['block'], x['rid'], x['errors']))
    for e in ierr:
        print('  - ' + e)
    sys.exit(0 if result == 'PASS' else 1)


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except C.Blocked as ex:
        print('BLOCKED: %s' % ex)
        sys.exit(2)
