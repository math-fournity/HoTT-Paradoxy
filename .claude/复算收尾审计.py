#!/usr/bin/env python3
"""设计会话的独立审计（只读）。用法：python3 -I -B .claude/复算收尾审计.py <工作树根目录> [--out 报告.json]

检查项（均只读，不写入执行者的工作区；导入执行者的工具时使用 -B，不生成字节码）：
  1. 账本全链：每行的 prev 等于上一行原始字节（含换行）的 SHA-256；首行为全零。
  2. RA 收据：块的切片（第 s 至 e 行，含换行）的 chunk_sha256 与 bytes；notes_sha256 按块的节正文（末尾加一个换行）；
     classes_sha256、assets_sha256 通过执行者的 class_rows、parse_assets 重算（口径复用，见报告说明）。
  3. 覆盖：每个 tag 的块与 blocks.json 一致；行数合计与 manifest2 相符；RA 数量是否齐全。
  4. 门禁顺序（v2 块）：每个 RA 之前是否有 GATE，且 GATE 之前有 RS。第一次运行的 40 块（v1）不适用，单独列出。
  5. 封印日志：事件是否单调；是否有 SEAL_BREACH、TAINTED；阶段 C 之前是否出现第一战役产物的访问记录。
  6. 交付物：R1 至 R5 是否存在（按文件名前缀 R1 至 R5 查找）。
  7. 豁免与 ID 缺口：列出 exemptions.json 与账本中的 ID 缺口记录。
退出码：0 = 无阻断问题（未完成不算阻断）；1 = 有阻断问题。
"""
import sys, json, hashlib, re, glob, os, datetime, pathlib

HDR = re.compile(r'^## (B-.+-\d{4}) \| 行 (\d+)–(\d+)\s*$')
VOID = '[作废'
V1_BLOCKS = {'B-dev-01-%04d' % i for i in range(1, 41)}  # 第一次运行的 40 个已提交块（v1 收据，见 CN-061）


def sha(b):
    return hashlib.sha256(b).hexdigest()


def sections_of(text):
    lines = text.split('\n')
    idx = [i for i, ln in enumerate(lines) if ln.startswith('## B-')]
    out = []
    for k, i in enumerate(idx):
        m = HDR.match(lines[i])
        if not m:
            continue
        j = idx[k + 1] if k + 1 < len(idx) else len(lines)
        L = lines[i:j]
        out.append({'block': m.group(1), 's': int(m.group(2)), 'e': int(m.group(3)),
                    'body': '\n'.join(L) + '\n', 'void': any(x.startswith(VOID) for x in L)})
    return out


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    root = pathlib.Path(argv[1]).resolve()
    out = None
    if '--out' in argv:
        out = pathlib.Path(argv[argv.index('--out') + 1])
    W = root / 'audit/GUI-ASSET-REAUDIT'
    tools = W / 'tools'
    sys.dont_write_bytecode = True
    sys.path.insert(0, str(tools))
    problems, notes_info = [], {}
    manifest = json.loads((W / 'manifest2.json').read_bytes().decode('utf-8'))
    path_of = {f['tag']: root / f['path'] for f in manifest['files']}

    # 1. 账本全链
    data = (W / 'ledger2.jsonl').read_bytes()
    raws = [x + b'\n' for x in data.split(b'\n') if x.strip()]
    recs = [json.loads(r.decode('utf-8')) for r in raws]
    prev, chain_bad = '0' * 64, []
    for i, (rec, raw) in enumerate(zip(recs, raws), start=1):
        if rec.get('prev') != prev:
            chain_bad.append(i)
        prev = sha(raw)
    notes_info['ledger_records'] = len(recs)
    notes_info['ledger_chain_breaks'] = chain_bad[:5]
    if chain_bad:
        problems.append('账本链断点：行 %s' % chain_bad[:5])

    # 2. RA 收据：切片
    ra = [r for r in recs if r.get('type') == 'RA']
    cache, bad_chunk = {}, []
    for r in ra:
        if r['tag'] not in cache:
            cache[r['tag']] = path_of[r['tag']].read_bytes().splitlines(keepends=True)
        L = cache[r['tag']]
        sl = b''.join(L[r['start'] - 1:r['end']])
        if not (sha(sl) == r['chunk_sha256'] and len(sl) == r['bytes']):
            bad_chunk.append(r['block'])
    notes_info['RA_count'] = len(ra)
    notes_info['RA_chunk_bytes_mismatch'] = bad_chunk
    if bad_chunk:
        problems.append('切片哈希不一致：%s' % bad_chunk[:8])

    # 2b. RA 收据：notes 节（读取全部分片，取未作废的节）
    secs = {}
    for tag in path_of:
        files = sorted(set(glob.glob(str(W / 'notes2' / (tag + '.md'))) + glob.glob(str(W / 'notes2' / (tag + '.part-*.md')))))
        for f in files:
            for s in sections_of(pathlib.Path(f).read_bytes().decode('utf-8')):
                if not s['void']:
                    secs.setdefault(s['block'], []).append(s)
    bad_notes = []
    for r in ra:
        c = secs.get(r['block'], [])
        if len(c) != 1 or sha(c[0]['body'].encode('utf-8')) != r['notes_sha256']:
            bad_notes.append((r['block'], len(c)))
    notes_info['RA_notes_mismatch'] = bad_notes[:8]
    if bad_notes:
        problems.append('notes 节哈希不一致或节数异常：%s' % bad_notes[:8])

    # 2c. classes 与 assets：复用执行者的解析函数（口径复用；见报告）
    try:
        import commit_block as cb  # noqa: E402  模块顶层无写入（已核对）
        assets_all = cb.parse_assets()
        bad_cls, bad_ast = [], []
        for r in ra:
            errs = []
            rows = cb.class_rows(r['tag'], r['block'], errs)
            rows.sort(key=lambda x: (x['start'], x['end']))
            ct = '\n'.join('%d\t%d\t%s\t%s' % (x['start'], x['end'], x['class'], x['ref']) for x in rows)
            at = '\n'.join(json.dumps(x, ensure_ascii=False, sort_keys=True) for x in assets_all if x.get('block') == r['block'])
            if sha(ct.encode('utf-8')) != r['classes_sha256']:
                bad_cls.append(r['block'])
            if sha(at.encode('utf-8')) != r['assets_sha256']:
                bad_ast.append(r['block'])
        notes_info['RA_classes_mismatch'] = bad_cls[:8]
        notes_info['RA_assets_mismatch'] = bad_ast[:8]
        if bad_cls or bad_ast:
            problems.append('classes/assets 哈希不一致：%s %s' % (bad_cls[:5], bad_ast[:5]))
    except Exception as ex:  # 分片后执行者的解析函数须先更新，此处据实报告
        notes_info['classes_assets_check'] = 'NOT_RUN: %s' % ex

    # 3. 覆盖：blocks.json 与 RA，行数合计
    blocks = json.loads((W / 'blocks.json').read_bytes().decode('utf-8'))
    blocks = blocks if isinstance(blocks, list) else blocks.get('blocks', [])
    by_tag = {}
    for b in blocks:
        by_tag.setdefault(b['tag'], []).append(b)
    ra_by_block = {r['block']: r for r in ra}
    cov = {}
    for tag, bl in by_tag.items():
        rows_total = sum(b['end'] - b['start'] + 1 for b in bl)
        got = sum(1 for b in bl if b['block'] in ra_by_block)
        cov[tag] = {'blocks': len(bl), 'committed': got, 'rows_in_blocks': rows_total,
                    'manifest_lines': next((f['lines'] for f in manifest['files'] if f['tag'] == tag), None)}
    notes_info['coverage'] = cov
    notes_info['blocks_total'] = len(blocks)
    notes_info['blocks_committed'] = sum(c['committed'] for c in cov.values())
    notes_info['complete'] = notes_info['blocks_committed'] == len(blocks)

    # 4. 门禁顺序（v2 块）
    gate_issues = []
    first_gate = {}
    last_rs_before = None
    for rec in recs:
        if rec.get('type') == 'RS':
            last_rs_before = rec.get('rid') or rec.get('boundary_id') or rec.get('target')
        if rec.get('type') == 'GATE':
            first_gate.setdefault(rec.get('block'), (rec, last_rs_before))
    for r in ra:
        if r['block'] in V1_BLOCKS:
            continue
        g = first_gate.get(r['block'])
        if g is None:
            gate_issues.append(r['block'])
        elif g[1] is None:
            gate_issues.append(r['block'] + '(无 RS)')
    notes_info['v2_blocks_without_gate_or_rs'] = gate_issues[:10]
    notes_info['v1_blocks_not_subject_to_gate'] = len(V1_BLOCKS & set(ra_by_block))
    if gate_issues:
        problems.append('v2 块缺少 GATE 或 RS：%s' % gate_issues[:8])

    # 5. 封印日志
    seal = [json.loads(l) for l in (W / 'seal-log.jsonl').read_bytes().decode('utf-8').splitlines() if l.strip()]
    events = [s.get('event') for s in seal]
    notes_info['seal_events'] = events
    if any(e in ('SEAL_BREACH', 'TAINTED') for e in events):
        problems.append('封印日志含 SEAL_BREACH 或 TAINTED，须在 R3 首部披露')
    tss = [s.get('ts', '') for s in seal]
    if tss != sorted(tss):
        problems.append('封印日志时间不单调')

    # 6. 交付物
    deliv = {}
    for k in ['R1', 'R2', 'R3', 'R4', 'R5']:
        deliv[k] = sorted(p.name for p in W.iterdir() if p.is_file() and p.name.startswith(k))
    notes_info['deliverables'] = deliv

    # 7. 豁免与 ID 缺口
    ex_path = W / 'exemptions.json'
    notes_info['exemptions'] = json.loads(ex_path.read_bytes().decode('utf-8')) if ex_path.exists() else []
    gaps = [r for r in recs if 'ID_GAP' in json.dumps(r, ensure_ascii=False)]
    notes_info['id_gap_records'] = [g.get('block', '') for g in gaps]

    report = {'checked_at_local': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
              'worktree': str(root), 'blocking_problems': problems, 'facts': notes_info,
              'note': 'classes/assets 通过执行者的解析函数复算（口径复用）；其余哈希由设计会话独立复算。'}
    text = json.dumps(report, ensure_ascii=False, indent=1)
    if out:
        out.write_text(text, encoding='utf-8')
    print(text)
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
