# -*- coding: utf-8 -*-
"""拍 5 预检与提交（SOP 003 §3、§4 至 §6；002 §7 第 4 条）。

用法：
  python3 -B -I tools/commit_block.py <BLOCK> --precheck   只检查，写 precheck/<BLOCK>.json
  python3 -B -I tools/commit_block.py <BLOCK> --commit     预检通过后追加 RA 收据，并刷新 STATUS.md

机械检查的范围（均为对 notes2、classes2、assets2 与块原文的一致性核对，不替代阅读）：
  C1 块身份：chunk_sha256 重算一致；块未曾提交。
  C2 notes2：取该块最后一个未作废的节；节头行号与 blocks.json 一致；无畸形的 "## B-" 节头。
  C3 classes2：该块全部行恰好划分一次（无重叠、无缺口、类别码合法）。
  C4 notes↔classes：每个 notes 条目覆盖的每一行，类别必须与 classes2 一致；每一行都被至少一条 notes 条目覆盖。
  C5 角色标记：原文中精确的 "## User" 行须有 [T] 条目起于该行；"## Codex" 行须有 [C] 或 [P] 条目起于该行。
     其他以 "## " 开头的行须落在某条 notes 条目之内（003 §10）。
  C6 胶囊与 commit 候选：capsule-pattern.json、commit-candidate.json 给出的模式命中的行，须有对应条目。
  C7 反引号标识：块内每个反引号标识须出现在本块 notes 或 assets 中，或在 exemptions.json 中有理由。
  C8 资产：[A] 条目与 assets2 行一一对应（ID 唯一）；名称与引文须为块原文的子串（逐字）。
  C9 复读：reread-state/<BLOCK>.json 含拍 1 与拍 4 的读取记录，返回末行等于块末行，状态 PASS，补记数一致。
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shards import read_text_logical  # noqa: E402
from common import (WORK, Blocked, LEDGER, ledger_append, ledger_records, load_blocks,  # noqa: E402
                    load_corpus_lines, load_manifest, now_utc, sha256_hex, verify_corpus,
                    write_json, load_json)

NOTES_DIR = os.path.join(WORK, 'notes2')
CLASSES_DIR = os.path.join(WORK, 'classes2')
ASSETS = os.path.join(WORK, 'assets2.md')
REREAD_DIR = os.path.join(WORK, 'reread-state')
PRECHECK_DIR = os.path.join(WORK, 'precheck')
EXEMPT = os.path.join(WORK, 'exemptions.json')
CAPSULE = os.path.join(WORK, 'capsule-pattern.json')
CANDIDATE = os.path.join(WORK, 'commit-candidate.json')
CLASS_SET = set('TCPAFGMX')
HDR_RE = re.compile(r'^## (B-.+-\d{4}) \| 行 (\d+)–(\d+)\s*$')
ENT_RE = re.compile(r'^- (?:\[补记·拍4\] )?\[([TCPAFGMX])\] L(\d+)(?:–L(\d+))?')
ASSET_ID_RE = re.compile(r'A2-\d{4}')
TICK_RE = re.compile(r'`([^`\n]{1,300})`')
VOID = '[作废'
USER_MARK = '## User'
CODEX_MARK = '## Codex'


def gate_ok(block):
    recs = [r for r, _ in ledger_records()]
    last_rs = max([i for i, r in enumerate(recs) if r.get('type') == 'RS'] or [-1])
    return any(r.get('type') == 'GATE' and r.get('block') == block and i > last_rs for i, r in enumerate(recs))


def tag_of(block):
    return block[2:-5]


def read_text(path):
    if not os.path.exists(path):
        return ''
    with open(path, 'rb') as f:
        return f.read().decode('utf-8')


def block_info(block):
    for b in load_blocks():
        if b['block'] == block:
            return b
    raise Blocked('blocks.json 中没有该块：%s' % block)


def committed_blocks():
    return {r['block'] for r, _ in ledger_records() if r.get('type') == 'RA'}


def notes_sections(text):
    """notes2 分节。返回 (节列表, 畸形节头列表)。节 = (块ID, s, e, 节正文, 是否作废)。"""
    lines = text.split('\n')
    idx = [i for i, ln in enumerate(lines) if ln.startswith('## B-')]
    secs, bad = [], []
    for k, i in enumerate(idx):
        j = idx[k + 1] if k + 1 < len(idx) else len(lines)
        body = '\n'.join(lines[i:j])
        is_void = any(ln.startswith(VOID) for ln in lines[i:j])
        m = HDR_RE.match(lines[i])
        if m:
            secs.append((m.group(1), int(m.group(2)), int(m.group(3)), body, is_void))
        else:
            bad.append(lines[i])
    return secs, bad


def parse_entries(body):
    ents = []
    for ln in body.split('\n'):
        m = ENT_RE.match(ln)
        if m:
            s = int(m.group(2))
            e = int(m.group(3)) if m.group(3) else s
            ents.append({'class': m.group(1), 's': s, 'e': e, 'addendum': '[补记·拍4]' in ln[:20],
                         'text': ln})
    return ents


def class_rows(tag, block, errs):
    rows = []
    for raw in read_text_logical('classes2/%s.tsv' % tag).split('\n'):
        if not raw or raw.startswith('block_id\t'):
            continue
        cols = raw.split('\t')
        if len(cols) != 5:
            errs.append('classes2 畸形行（列数非 5）：%r' % raw[:80])
            continue
        if cols[0] == block:
            try:
                rows.append({'start': int(cols[1]), 'end': int(cols[2]), 'class': cols[3], 'ref': cols[4]})
            except ValueError:
                errs.append('classes2 行号非整数：%r' % raw[:80])
    return rows


def parse_assets():
    """assets2.md 的表格行：返回 [dict]，列为 ID、位置、名称、类别、定义、状态、引文、块。"""
    rows = []
    for ln in read_text_logical('assets2.md').split('\n'):
        if not ln.startswith('| A2-'):
            continue
        cells = [c.replace('\\|', '|').strip() for c in re.split(r'(?<!\\)\|', ln)[1:-1]]
        if len(cells) != 8:
            rows.append({'bad': ln})
            continue
        rows.append({'ID': cells[0], 'pos': cells[1], 'name': cells[2], 'cat': cells[3],
                     'def': cells[4], 'status': cells[5], 'quote': cells[6], 'block': cells[7]})
    return rows


def precheck(block):
    errs = []
    info = block_info(block)
    tag, s, e = info['tag'], info['start'], info['end']
    if block in committed_blocks():
        errs.append('该块已提交，不得重复提交')
    if not gate_ok(block):
        errs.append('G1 缺少本块在最后一个 RS 之后的 GATE 记录（006 §4；先运行 tools/gate.py）')
    manifest = load_manifest()
    verify_corpus(manifest)
    data, lines = load_corpus_lines(manifest, tag)
    from common import chunk_bytes
    sl = chunk_bytes(data, lines, s, e)
    if sha256_hex(sl) != info['chunk_sha256']:
        errs.append('C1 块哈希与 blocks.json 不符')
    try:
        btxt = [x[1].decode('utf-8') for x in lines[s - 1:e]]
    except UnicodeDecodeError:
        raise Blocked('块原文含非法 UTF-8：%s（应记 ENCODING_ANOMALY）' % block)
    # C2 notes2
    secs, bad = notes_sections(read_text_logical('notes2/%s.md' % tag))
    if bad:
        errs.append('C2 notes2 存在畸形节头 %d 个' % len(bad))
    cand = [x for x in secs if x[0] == block and not x[4]]
    if not cand:
        errs.append('C2 notes2 中没有该块的未作废节')
        body = ''
    else:
        _, hs, he, body, _ = cand[-1]
        if (hs, he) != (s, e):
            errs.append('C2 节头行号 %d–%d 与 blocks.json %d–%d 不符' % (hs, he, s, e))
    ents = parse_entries(body)
    addenda = sum(1 for x in ents if x['addendum'])
    # C3 classes2 划分
    rows = class_rows(tag, block, errs)
    rows.sort(key=lambda r: (r['start'], r['end']))
    expect = s
    cls_of = {}
    for r in rows:
        if r['class'] not in CLASS_SET:
            errs.append('C3 类别码非法：%r' % r['class'])
        if r['start'] > r['end']:
            errs.append('C3 区间倒置：%d–%d' % (r['start'], r['end']))
        if r['start'] < expect:
            errs.append('C3 重叠于行 %d' % r['start'])
        elif r['start'] > expect:
            errs.append('C3 缺口 %d–%d' % (expect, r['start'] - 1))
        for L in range(max(r['start'], s), min(r['end'], e) + 1):
            cls_of.setdefault(L, []).append(r['class'])
        expect = max(expect, r['end'] + 1)
    if expect != e + 1:
        errs.append('C3 覆盖止于行 %d，应为 %d' % (expect - 1, e))
    for L, cl in cls_of.items():
        if len(cl) != 1:
            errs.append('C3 行 %d 被划分 %d 次' % (L, len(cl)))
    # C4 notes ↔ classes 一致，且每行都被条目覆盖
    covered = {}
    for x in ents:
        if x['e'] < x['s'] or x['s'] < s or x['e'] > e:
            errs.append('C4 条目行范围越界或倒置：%s' % x['text'][:60])
            continue
        if x['class'] == 'A':
            continue  # A 为叠加标注，不参与主类划分的一致性核对
        for L in range(x['s'], x['e'] + 1):
            if x['class'] == 'G' and cls_of.get(L) != ['G']:
                continue  # G 亦可作叠加标注：commit 候选出现在其他主类行内时，只记条目，不改划分
            covered.setdefault(L, set()).add(x['class'])
            if cls_of.get(L) and x['class'] not in cls_of[L]:
                errs.append('C4 行 %d：条目类别 %s 与 classes2 %s 不符' % (L, x['class'], cls_of[L]))
    for L in range(s, e + 1):
        if L not in covered:
            errs.append('C4 行 %d 未被 notes 条目覆盖' % L)
    for r in rows:
        if r['class'] == 'A':
            errs.append('C3 classes2 不得使用 A（A 为叠加标注，见 SESSION §8）：%d–%d' % (r['start'], r['end']))
    # C5 角色标记
    n_user = n_codex = n_head = 0
    for L in range(s, e + 1):
        t = btxt[L - s]
        if t == USER_MARK:
            n_user += 1
            if not any(x['s'] == L and x['class'] == 'T' for x in ents):
                errs.append('C5 行 %d 的 ## User 无 [T] 条目起于该行' % L)
        elif t == CODEX_MARK:
            n_codex += 1
            if not any(x['s'] == L and x['class'] in ('C', 'P') for x in ents):
                errs.append('C5 行 %d 的 ## Codex 无 [C]/[P] 条目起于该行' % L)
        elif t.startswith('## '):
            n_head += 1
            if L not in covered:
                errs.append('C5 行 %d 的 ## 正文标题未被条目覆盖' % L)
    # C6 胶囊与 commit 候选
    if os.path.exists(CAPSULE):
        cap = load_json(CAPSULE)
        cre = re.compile(cap['regex'])
        for L in range(s, e + 1):
            if cre.search(btxt[L - s]) and not any(x['s'] <= L <= x['e'] and x['class'] == 'F' for x in ents):
                errs.append('C6 胶囊行 %d 无 [F] 条目' % L)
    ccfg = load_json(CANDIDATE) if os.path.exists(CANDIDATE) else {'min_len': 7, 'max_len': 40, 'require_letter': False}
    cre_c = re.compile(r'(?<![0-9A-Za-z_])([0-9a-fA-F]{%d,%d})(?![0-9A-Za-z_])' % (ccfg['min_len'], ccfg['max_len']))
    n_cand = 0
    for L in range(s, e + 1):
        for m in cre_c.finditer(btxt[L - s]):
            if ccfg.get('require_letter') and not re.search(r'[a-fA-F]', m.group(1)):
                continue
            n_cand += 1
            if not any(x['s'] <= L <= x['e'] and x['class'] == 'G' for x in ents):
                errs.append('C6 行 %d 的 commit 候选 %s 无 [G] 条目' % (L, m.group(1)))
                break
    # C7 反引号标识
    assets_rows = [r for r in parse_assets() if r.get('block') == block]
    notes_blob = body + '\n' + '\n'.join(sorted(json.dumps(r, ensure_ascii=False) for r in assets_rows))
    # 豁免表：{"token": "..."} 精确豁免；{"pattern": "正则", "reason": "..."} 按类别豁免（SESSION §8 登记理由）
    exempt, exempt_pat = set(), []
    if os.path.exists(EXEMPT):
        for x in load_json(EXEMPT):
            if 'token' in x:
                exempt.add(x['token'])
            elif 'pattern' in x:
                exempt_pat.append(re.compile(x['pattern']))
    toks = set()
    for t in btxt:
        for m in TICK_RE.finditer(t):
            toks.add(m.group(1))
    for tok in sorted(toks):
        if tok in notes_blob or tok in exempt or any(p.search(tok) for p in exempt_pat):
            continue
        errs.append('C7 反引号标识未在 notes/assets 中出现且无豁免：%r' % tok[:60])
    # C8 资产
    a_ids_notes = []
    for x in ents:
        if x['class'] == 'A':
            m = ASSET_ID_RE.search(x['text'])
            if not m:
                errs.append('C8 [A] 条目无资产 ID：%s' % x['text'][:60])
            else:
                a_ids_notes.append(m.group(0))
    all_assets = parse_assets()
    ids_seen = {}
    for r in all_assets:
        if 'bad' in r:
            errs.append('C8 assets2 畸形行（列数非 8）：%r' % r['bad'][:60])
            continue
        if r['ID'] in ids_seen:
            errs.append('C8 资产 ID 重复：%s' % r['ID'])
        ids_seen[r['ID']] = r
    blk_ids = [r['ID'] for r in assets_rows]
    for i in a_ids_notes:
        if i not in blk_ids:
            errs.append('C8 [A] 的 %s 不在 assets2 的本块行中' % i)
    for i in blk_ids:
        if i not in a_ids_notes:
            errs.append('C8 assets2 的 %s 无对应 [A] 条目' % i)
    block_text = '\n'.join(btxt)
    for r in assets_rows:
        if r['name'] and r['name'] not in block_text:
            errs.append('C8 %s 名称非块原文子串' % r['ID'])
        if r['quote'] and r['quote'] not in block_text:
            errs.append('C8 %s 引文非块原文子串' % r['ID'])
        if r['quote'] and len(r['quote']) > 200 + 2:
            errs.append('C8 %s 引文超过 200 字符' % r['ID'])
    # C10 notes 中「」内的引文须为块原文子串（003 §4：引文逐字）
    for q in re.findall(r'「([^」\n]*)」', body):
        if q and q not in block_text:
            errs.append('C10 notes 引文非块原文子串：%r' % q[:50])
    # C9 复读
    rr_path = os.path.join(REREAD_DIR, block + '.json')
    if not os.path.exists(rr_path):
        errs.append('C9 缺少 reread-state（拍 1 与拍 4 读取记录）')
        rr = {}
    else:
        rr = load_json(rr_path)
        b1, b4 = rr.get('beat1', {}), rr.get('beat4', {})
        if not (b1.get('start') == s and b1.get('end') == e and b1.get('returned_end') == e):
            errs.append('C9 拍 1 读取记录与块不符')
        if not (b4.get('start') == s and b4.get('end') == e and b4.get('returned_end') == e):
            errs.append('C9 拍 4 复读记录缺失或与块不符')
        if rr.get('status') != 'PASS':
            errs.append('C9 复读状态非 PASS：%r' % rr.get('status'))
        if rr.get('addenda') != addenda:
            errs.append('C9 补记数 %r 与 notes 中 [补记·拍4] 条目数 %d 不符' % (rr.get('addenda'), addenda))
    stats = {'obligations': e - s + 1, 'entries': len(ents), 'addenda': addenda,
             'role_user': n_user, 'role_codex': n_codex, 'head_lines': n_head,
             'commit_candidates': n_cand, 'assets_in_block': len(assets_rows),
             'class_rows': len(rows), 'backtick_tokens': len(toks)}
    return errs, stats, body, rows, assets_rows, rr


def main(argv):
    if len(argv) != 2 or argv[1] not in ('--precheck', '--commit'):
        raise Blocked('用法：commit_block.py <BLOCK> --precheck|--commit')
    block, mode = argv[0], argv[1]
    errs, stats, body, rows, assets_rows, rr = precheck(block)
    os.makedirs(PRECHECK_DIR, exist_ok=True)
    rec = {'block': block, 'ok': not errs, 'errors': errs, 'stats': stats, 'ts': now_utc()}
    write_json(os.path.join(PRECHECK_DIR, block + '.json'), rec)
    if mode == '--precheck':
        print(('PRECHECK_PASS' if not errs else 'PRECHECK_FAIL') + ' %s %s' % (block, json.dumps(stats, ensure_ascii=False)))
        for x in errs[:60]:
            print('  - ' + x)
        if len(errs) > 60:
            print('  ...（另有 %d 条）' % (len(errs) - 60))
        sys.exit(0 if not errs else 1)
    if errs:
        print('COMMIT_REFUSED %s：预检未通过，%d 条错误' % (block, len(errs)))
        sys.exit(1)
    info = block_info(block)
    tag, s, e = info['tag'], info['start'], info['end']
    sec_text = body
    cls_text = '\n'.join('%d\t%d\t%s\t%s' % (r['start'], r['end'], r['class'], r['ref']) for r in rows)
    a_text = '\n'.join(json.dumps(r, ensure_ascii=False, sort_keys=True) for r in assets_rows)
    n_ra = sum(1 for r, _ in ledger_records() if r.get('type') == 'RA')
    rec = {
        'type': 'RA', 'rid': 'RA-%04d' % (n_ra + 1), 'block': block, 'tag': tag, 'start': s, 'end': e,
        'obligations': e - s + 1, 'context_ranges': [], 'bytes': info['bytes'],
        'chunk_sha256': info['chunk_sha256'],
        'tool_reads': [rr['beat1'], rr['beat4']],
        'notes_sha256': sha256_hex(sec_text.encode('utf-8')),
        'classes_sha256': sha256_hex(cls_text.encode('utf-8')),
        'assets_sha256': sha256_hex(a_text.encode('utf-8')),
        'assets_ids': [r['ID'] for r in assets_rows],
        'reread': {'status': rr['status'], 'addenda': rr['addenda']},
        'precheck_stats': stats,
    }
    out = ledger_append(rec)
    import cursor  # noqa: E402
    cursor.refresh()
    print('COMMITTED %s %s prev=%s' % (out['rid'], block, out['prev']))


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Blocked as ex:
        print('BLOCKED: %s' % ex)
        sys.exit(2)
