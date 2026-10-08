#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUI 导出综合重读（v3）的确定性工具。

只读语料 git-worktree对话录/dev-*-gui.md。输出只写入 audit/GUI-SYNTH-REDO/ 下的约定位置。
不联网，不调用子代理。结果只由文件内容决定，可重复运行。

子命令：
  segment                                   切分语料，生成 index/（语料变化时重跑）
  status [--tag T]                          查看进度与下一批
  batch --tag T (--id B | --next)           打印一批的行号范围、交换清单与读取参数
  add --tag T --batch B --events F --reader R --model M
                                            校验事件草稿；通过后写入 events/、receipts/、progress/
  verify --tag T --stage events|cards|final|audit [--min-recall X]
  verify --stage synthesis                  跨线综合文件的校验（需 8 条线 final 通过）
  sample --tag T [--rate 0.05] [--seed S]   生成审计抽样清单（audits/T.sample.json）
"""
import argparse
import collections
import datetime
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = pathlib.Path(os.environ.get('GSR_ROOT', HERE.parent))
REPO = HERE.parents[2]
CORPUS = pathlib.Path(os.environ.get('GSR_CORPUS', REPO / 'git-worktree对话录'))

TAGS = ['dev-01', 'dev-02', 'dev-03', 'dev-04', 'dev-06', 'dev-07', 'dev-08', 'dev-09']
MAX_BATCH_LINES = 900
MAX_BATCH_BYTES = 65000
MAX_TEXT = 160
MAX_NONE = 60
MAX_TOPIC = 24
MAX_EVENTS_PER_EX = 6
MAX_EVIDENCE_PER_EX = 80
USER_KINDS = {'USER_STATEMENT', 'USER_CORRECTION', 'USER_DECISION', 'USER_QUESTION'}
AI_KINDS = {'AI_POSITION', 'AI_RESULT', 'AI_ACTION', 'OPEN', 'EVIDENCE'}
KINDS = USER_KINDS | AI_KINDS | {'NONE'}
SYNTH_FILES = ['THREADS-MATRIX.md', 'CLAIMS.tsv', 'USER-STATEMENTS.md', 'CONTRADICTIONS.md', 'HANDOFF.md']
CLAIM_STATUS = {'SUPPORTED', 'ASSERTED_ONLY', 'CONTRADICTED', 'SUPERSEDED', 'OPEN'}
CARD_SECTIONS = ['## 起点', '## 主线', '## 用户的纠正与裁定', '## 主张与结果', '## 证据指针',
                 '## 开放问题', '## 结束状态', '## 与其他线的接点']
CARD_REF_SECTIONS = {'## 主线', '## 用户的纠正与裁定', '## 主张与结果', '## 证据指针', '## 开放问题'}
CARD_CROSS_SECTION = '## 与其他线的接点'
FENCE_RE = re.compile(r'^(\s{0,3})(`{3,}|~{3,})(.*)$')
HEX_RE = re.compile(r'(?<![0-9A-Za-z_])[0-9a-f]{7,40}(?![0-9A-Za-z_])')
TICK_RE = re.compile(r'`([^`\n]{3,200})`')
URL_RE = re.compile(r'https?://[^\s<>"\'`)\]]+')
PATH_EXT_RE = re.compile(r'\.(md|py|json|jsonl|tsv|txt|lean|agda|tex|csv|yaml|yml|toml|sh|zsh|log)$')
ID_RE = re.compile(r'\b(dev-0[1-9]):(V\d{6}|R\d{6}|E\d{4})\b')


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def die(msg, code=1):
    print(msg, file=sys.stderr)
    sys.exit(code)


def rj(path):
    return json.loads(path.read_text(encoding='utf-8'))


def wj(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True) + '\n', encoding='utf-8')


def read_jsonl(path):
    if not path.exists():
        return []
    out = []
    for ln in path.read_text(encoding='utf-8').split('\n'):
        if ln.strip():
            out.append(json.loads(ln))
    return out


def append_jsonl(path, recs):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as fh:
        for r in recs:
            fh.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n')


def write_jsonl(path, recs):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n' for r in recs),
                    encoding='utf-8')


def rel_or_name(p):
    try:
        return p.relative_to(REPO).as_posix()
    except ValueError:
        return p.name


def corpus_path(tag):
    hits = sorted(CORPUS.glob(f'{tag} - *-gui.md'))
    if len(hits) != 1:
        die(f'语料文件不唯一或缺失：{tag}（命中 {len(hits)} 个）')
    return hits[0]


class Corpus:
    """语料的行视图。行号从 1 开始；每行不含换行符；chunk_bytes 还原原始字节（含换行）。"""

    def __init__(self, tag):
        self.tag = tag
        self.path = corpus_path(tag)
        self.data = self.path.read_bytes()
        self.ends_nl = self.data.endswith(b'\n')
        parts = self.data.split(b'\n')
        self.lines = parts[:-1] if self.ends_nl else parts
        self.n = len(self.lines)
        self.text = [ln.decode('utf-8') for ln in self.lines]

    def chunk_bytes(self, a, b):
        out = b'\n'.join(self.lines[a - 1:b])
        if b < self.n or self.ends_nl:
            out += b'\n'
        return out


def git_check(c):
    data = c.data
    blob = hashlib.sha1(b'blob %d\x00' % len(data) + data).hexdigest()
    head = None
    try:
        rel = c.path.relative_to(REPO).as_posix()
        out = subprocess.run(['git', '-C', str(REPO), 'ls-tree', 'HEAD', '--', rel],
                             capture_output=True, text=True, timeout=60).stdout.split()
        if len(out) >= 3:
            head = out[2]
    except (ValueError, OSError, subprocess.SubprocessError):
        head = None
    return {'blob_sha1': blob, 'head_blob_sha1': head, 'matches_head': (head == blob) if head else None}


def candidates(c, a, b):
    """机器抽取的证据候选：十六进制串（7–40 位）、反引号中的路径、URL。每个交换内去重。"""
    seen, out = set(), []
    for i in range(a, b + 1):
        t = c.text[i - 1]
        found = []
        for m in HEX_RE.finditer(t):
            found.append(('HEX', m.group(0)))
        for m in TICK_RE.finditer(t):
            v = m.group(1).strip()
            if '/' in v or PATH_EXT_RE.search(v):
                found.append(('PATH', v))
        for m in URL_RE.finditer(t):
            found.append(('URL', m.group(0).rstrip('.,;:，。；、')))
        for kind, v in found:
            if (kind, v) in seen:
                continue
            seen.add((kind, v))
            out.append({'kind': kind, 'value': v, 'line': i})
    overflow = max(0, len(out) - MAX_EVIDENCE_PER_EX)
    return out[:MAX_EVIDENCE_PER_EX], overflow


def segment_corpus(c):
    fence = None
    user_at, codex_at, other = [], [], []
    raw_user = 0
    for i, t in enumerate(c.text, start=1):
        s = t.rstrip()
        if s == '## User':
            raw_user += 1
        m = FENCE_RE.match(t)
        if m:
            mk = m.group(2)
            if fence is None:
                fence = (mk[0], len(mk))
            elif mk[0] == fence[0] and len(mk) >= fence[1] and m.group(3).strip() == '':
                fence = None
            continue
        if fence is not None:
            continue
        if s == '## User':
            user_at.append(i)
        elif s == '## Codex':
            codex_at.append(i)
        elif s.startswith('## ') and len(other) < 50:
            other.append([i, s[:60]])
    n = c.n
    spans = []
    first = user_at[0] if user_at else n + 1
    if first > 1:
        spans.append(('E0000', 1, first - 1, False))
    for k, s0 in enumerate(user_at):
        e0 = user_at[k + 1] - 1 if k + 1 < len(user_at) else n
        spans.append(('E%04d' % (k + 1), s0, e0, True))
    prev, contiguous = 0, True
    for _, a, b, _u in spans:
        if a != prev + 1 or b < a:
            contiguous = False
        prev = b
    contiguous = contiguous and prev == n
    concat = b''.join(c.chunk_bytes(a, b) for _, a, b, _u in spans)
    partition_ok = contiguous and sha256(concat) == sha256(c.data)

    ex_recs, ev_recs, evid = [], [], 0
    for exid, a, b, is_user in spans:
        cid = f'{c.tag}:{exid}'
        cands, overflow = candidates(c, a, b)
        head = ''
        for ln in range(a + 1 if is_user else a, b + 1):
            if c.text[ln - 1].strip():
                head = c.text[ln - 1].strip()[:100]
                break
        cstarts = [x for x in codex_at if a <= x <= b]
        cbytes = c.chunk_bytes(a, b)
        ex_recs.append({'exid': cid, 'kind': 'USER_EXCHANGE' if is_user else 'PREAMBLE',
                        'line_start': a, 'line_end': b, 'lines': b - a + 1, 'bytes': len(cbytes),
                        'sha256': sha256(cbytes), 'user_head': head, 'codex_msgs': len(cstarts),
                        'codex_starts': cstarts[:200], 'evidence_count': len(cands),
                        'evidence_overflow': overflow})
        for cd in cands:
            evid += 1
            ev_recs.append({'id': f'{c.tag}:R{evid:06d}', 'ex': cid, 'kind': cd['kind'],
                            'value': cd['value'], 'line': cd['line']})

    bat_recs, cur = [], None
    for r in ex_recs:
        if cur is None or cur['lines'] + r['lines'] > MAX_BATCH_LINES or cur['bytes'] + r['bytes'] > MAX_BATCH_BYTES:
            if cur is not None:
                bat_recs.append(cur)
            cur = {'batch': f'{c.tag}:B{len(bat_recs) + 1:03d}', 'exes': [], 'line_from': r['line_start'],
                   'line_to': r['line_end'], 'lines': 0, 'bytes': 0}
        cur['exes'].append(r['exid'])
        cur['line_to'] = r['line_end']
        cur['lines'] += r['lines']
        cur['bytes'] += r['bytes']
    if cur is not None:
        bat_recs.append(cur)
    for bt in bat_recs:
        bt['sha256'] = sha256(c.chunk_bytes(bt['line_from'], bt['line_to']))
        bt['oversize'] = bt['lines'] > MAX_BATCH_LINES

    gc = git_check(c)
    meta = {'tag': c.tag, 'file': rel_or_name(c.path), 'sha256': sha256(c.data), 'bytes': len(c.data),
            'lines': c.n, 'ends_with_newline': c.ends_nl, 'partition_ok': partition_ok,
            'exchanges': len(ex_recs), 'user_exchanges': sum(1 for r in ex_recs if r['kind'] == 'USER_EXCHANGE'),
            'codex_messages': len(codex_at), 'user_headers_in_fences_skipped': raw_user - len(user_at),
            'other_h2_sample': other[:20], 'batches': len(bat_recs),
            'oversize_batches': sum(1 for b in bat_recs if b['oversize']), 'evidence': len(ev_recs),
            'git': gc, 'git_matches_head': gc['matches_head'], 'generated_utc': utc_now()}
    return ex_recs, bat_recs, ev_recs, meta


def cmd_segment(_a):
    out = ROOT / 'index'
    report = {'generated_utc': utc_now(), 'corpus': rel_or_name(CORPUS), 'tags': {}}
    ok = True
    for tag in TAGS:
        c = Corpus(tag)
        ex_recs, bat_recs, ev_recs, meta = segment_corpus(c)
        write_jsonl(out / f'{tag}.exchanges.jsonl', ex_recs)
        write_jsonl(out / f'{tag}.batches.jsonl', bat_recs)
        write_jsonl(out / f'{tag}.evidence.jsonl', ev_recs)
        wj(out / f'{tag}.manifest.json', meta)
        ok = ok and meta['partition_ok']
        report['tags'][tag] = {k: meta[k] for k in ('lines', 'bytes', 'exchanges', 'user_exchanges',
                                                     'codex_messages', 'batches', 'evidence',
                                                     'partition_ok', 'git_matches_head')}
        print(f"{tag}: 行 {meta['lines']}  交换 {meta['exchanges']}（用户轮 {meta['user_exchanges']}）  "
              f"Codex 消息 {meta['codex_messages']}  批 {meta['batches']}  证据候选 {meta['evidence']}  "
              f"划分 {'OK' if meta['partition_ok'] else 'FAIL'}  与 HEAD 一致 {meta['git_matches_head']}")
    report['all_partition_ok'] = ok
    wj(out / 'SEGMENT_REPORT.json', report)
    return 0 if ok else 1


def load_index(tag):
    d = ROOT / 'index'
    paths = [d / f'{tag}.exchanges.jsonl', d / f'{tag}.batches.jsonl',
             d / f'{tag}.evidence.jsonl', d / f'{tag}.manifest.json']
    if not all(p.exists() for p in paths):
        die(f'缺少索引：{tag}。请先运行 gsr.py segment')
    return read_jsonl(paths[0]), read_jsonl(paths[1]), read_jsonl(paths[2]), rj(paths[3])


def receipts_of(tag):
    return read_jsonl(ROOT / 'receipts' / f'{tag}.jsonl')


def events_of(tag):
    return read_jsonl(ROOT / 'events' / f'{tag}.jsonl')


def done_batches(tag):
    return {r['batch'] for r in receipts_of(tag)}


def next_batch(tag, bats):
    done = done_batches(tag)
    for b in bats:
        if b['batch'] not in done:
            return b
    return None


def print_batch_hint(tag, bt):
    print(f"  批次 {bt['batch']}：行 {bt['line_from']}–{bt['line_to']}（{bt['lines']} 行，{bt['bytes']} 字节，"
          f"{len(bt['exes'])} 个交换）")
    print(f'  读取：Read(file_path="{corpus_path(tag)}", offset={bt["line_from"]}, limit={bt["lines"]})')
    print(f'  事件草稿：audit/GUI-SYNTH-REDO/scratch/{bt["batch"].replace(":", "-")}.jsonl')


def update_progress(tag):
    ex, bats, _ev, _m = load_index(tag)
    rec = receipts_of(tag)
    evs = events_of(tag)
    done = {r['batch'] for r in rec}
    covered = {e for b in bats if b['batch'] in done for e in b['exes']}
    p = ROOT / 'progress' / f'{tag}.json'
    prev = rj(p) if p.exists() else {}
    state = {'tag': tag, 'status': prev.get('status', 'IN_PROGRESS'), 'batches_total': len(bats),
             'batches_done': len(done), 'exchanges_total': len(ex), 'exchanges_covered': len(covered),
             'events': len(evs), 'readers': sorted({r.get('reader', '') for r in rec}),
             'models': sorted({r.get('model', '') for r in rec}),
             'last_batch': rec[-1]['batch'] if rec else None, 'updated_utc': utc_now()}
    if state['status'] == 'DONE' and len(done) < len(bats):
        state['status'] = 'IN_PROGRESS'
    wj(p, state)


def set_status(tag, status):
    p = ROOT / 'progress' / f'{tag}.json'
    st = rj(p) if p.exists() else {'tag': tag}
    st['status'] = status
    st['updated_utc'] = utc_now()
    wj(p, st)


def cmd_status(a):
    tags = [a.tag] if a.tag else TAGS
    for tag in tags:
        if not (ROOT / 'index' / f'{tag}.batches.jsonl').exists():
            print(f'{tag}: 未切分（先运行 segment）')
            continue
        ex, bats, _ev, meta = load_index(tag)
        done = done_batches(tag)
        covered = {e for b in bats if b['batch'] in done for e in b['exes']}
        pj = ROOT / 'progress' / f'{tag}.json'
        state = rj(pj)['status'] if pj.exists() else 'NOT_STARTED'
        print(f"{tag}  状态 {state}  批次 {len(done)}/{len(bats)}  交换 {len(covered)}/{len(ex)}  "
              f"事件 {len(events_of(tag))}  划分 {'OK' if meta['partition_ok'] else 'FAIL'}")
        nb = next_batch(tag, bats)
        if nb is None:
            print(f'  全部批次已完成：下一步写 cards/{tag}.md，然后 verify --stage final')
        else:
            print_batch_hint(tag, nb)
    return 0


def cmd_batch(a):
    ex, bats, _ev, _m = load_index(a.tag)
    if a.next:
        bt = next_batch(a.tag, bats)
        if bt is None:
            print('没有未完成的批次')
            return 0
    else:
        bt = next((b for b in bats if b['batch'] == a.id), None)
        if bt is None:
            die(f'没有批次 {a.id}')
    ex_by = {e['exid']: e for e in ex}
    print_batch_hint(a.tag, bt)
    for eid in bt['exes']:
        e = ex_by[eid]
        print(f"  {eid} 行 {e['line_start']}–{e['line_end']}  Codex {e['codex_msgs']}  "
              f"候选 {e['evidence_count']}  首行：{e['user_head'][:70]}")
    return 0


def cmd_add(a):
    tag, bid = a.tag, a.batch
    ex, bats, ev_idx, _m = load_index(tag)
    bt = next((b for b in bats if b['batch'] == bid), None)
    if bt is None:
        die(f'没有批次 {bid}')
    if bid in done_batches(tag):
        die(f'批次 {bid} 已完成，不能重复写入')
    c = Corpus(tag)
    if sha256(c.chunk_bytes(bt['line_from'], bt['line_to'])) != bt['sha256']:
        die('语料与索引不一致：批次哈希不符（语料可能已改动），停止', 2)
    ex_by = {e['exid']: e for e in ex}
    cand = collections.defaultdict(set)
    for e in ev_idx:
        cand[e['ex']].add(e['value'])
    raw = read_jsonl(pathlib.Path(a.events))
    errs, per = [], collections.defaultdict(list)
    for i, r in enumerate(raw, start=1):
        exid = str(r.get('ex', ''))
        if ':' not in exid:
            exid = f'{tag}:{exid}'
        r['ex'] = exid
        where = f'第 {i} 条（{exid}）'
        if exid not in bt['exes']:
            errs.append(f'{where}：不属于本批次')
            continue
        e = ex_by[exid]
        line, kind, text = r.get('line'), r.get('kind'), r.get('text')
        quote, refs, topic = r.get('quote', False), r.get('refs', []) or [], r.get('topic', '') or ''
        if not isinstance(line, int) or not (e['line_start'] <= line <= e['line_end']):
            errs.append(f'{where}：line 不在该交换的行范围内')
        if kind not in KINDS:
            errs.append(f'{where}：kind 无效：{kind!r}')
        if not isinstance(text, str) or not text.strip():
            errs.append(f'{where}：text 为空')
        if not isinstance(quote, bool):
            errs.append(f'{where}：quote 须为 true 或 false')
        if not isinstance(refs, list) or not all(isinstance(x, str) for x in refs):
            errs.append(f'{where}：refs 须为字符串列表')
        if not isinstance(topic, str) or len(topic) > MAX_TOPIC:
            errs.append(f'{where}：topic 超过 {MAX_TOPIC} 字')
        if kind == 'NONE':
            if not (isinstance(text, str) and text.startswith('NONE:') and len(text) <= MAX_NONE):
                errs.append(f'{where}：NONE 的 text 须以 "NONE:" 开头并写明理由（不超过 60 字）')
            if quote is True:
                errs.append(f'{where}：NONE 不得 quote=true')
        else:
            if isinstance(text, str) and len(text) > MAX_TEXT:
                errs.append(f'{where}：text 超过 {MAX_TEXT} 字')
            if kind in USER_KINDS and quote is not True:
                errs.append(f'{where}：用户轮的事件必须 quote=true（逐字引用原行）')
            if quote is True and isinstance(line, int) and 1 <= line <= c.n and isinstance(text, str):
                if text not in c.text[line - 1]:
                    errs.append(f'{where}：quote 不是第 {line} 行的逐字子串')
            for rv in refs:
                if rv not in cand[exid]:
                    errs.append(f'{where}：refs {rv!r} 不在本交换的证据候选中')
        per[exid].append(r)
    for eid in bt['exes']:
        rs = per.get(eid, [])
        if not rs:
            errs.append(f'{eid}：没有事件，也没有 NONE 记录')
        elif any(x.get('kind') == 'NONE' for x in rs) and len(rs) > 1:
            errs.append(f'{eid}：NONE 必须是该交换的唯一记录')
        elif len(rs) > MAX_EVENTS_PER_EX:
            errs.append(f'{eid}：事件数 {len(rs)} 超过上限 {MAX_EVENTS_PER_EX}')
    if errs:
        for m in errs[:60]:
            print('ERROR', m)
        print(f'未写入：{len(errs)} 处错误。修正 {a.events} 后重新运行 add。')
        return 1
    existing = events_of(tag)
    nxt = 1 + max([int(x['id'].split(':V')[1]) for x in existing if ':V' in x.get('id', '')] or [0])
    out = []
    for eid in bt['exes']:
        for r in per.get(eid, []):
            out.append({'id': f'{tag}:V{nxt:06d}', 'ex': eid, 'batch': bid, 'kind': r['kind'],
                        'line': r['line'], 'text': r['text'], 'quote': bool(r.get('quote', False)),
                        'topic': r.get('topic', '') or '', 'refs': r.get('refs', []) or [],
                        'reader': a.reader, 'model': a.model, 'utc': utc_now()})
            nxt += 1
    append_jsonl(ROOT / 'events' / f'{tag}.jsonl', out)
    append_jsonl(ROOT / 'receipts' / f'{tag}.jsonl',
                 [{'batch': bid, 'exes': bt['exes'], 'line_from': bt['line_from'], 'line_to': bt['line_to'],
                   'lines': bt['lines'], 'sha256': bt['sha256'], 'events': len(out),
                   'reader': a.reader, 'model': a.model, 'utc': utc_now()}])
    update_progress(tag)
    print(f'已写入 {bid}：交换 {len(bt["exes"])}，事件 {len(out)}。')
    return 0


def check_events(tag):
    ex, bats, ev_idx, _m = load_index(tag)
    c = Corpus(tag)
    ex_by = {e['exid']: e for e in ex}
    bat_by = {b['batch']: b for b in bats}
    errs, done_ex, done_b = [], set(), set()
    for r in receipts_of(tag):
        b = bat_by.get(r['batch'])
        if b is None:
            errs.append(f"收据 {r['batch']} 不在索引中")
            continue
        if sha256(c.chunk_bytes(b['line_from'], b['line_to'])) != r['sha256']:
            errs.append(f"{r['batch']}：语料哈希与收据不符")
        done_b.add(r['batch'])
        done_ex.update(b['exes'])
    cand = collections.defaultdict(set)
    for e in ev_idx:
        cand[e['ex']].add(e['value'])
    per, seen = collections.defaultdict(list), set()
    evs = events_of(tag)
    for x in evs:
        xid = x.get('id')
        if xid in seen:
            errs.append(f'事件编号重复：{xid}')
        seen.add(xid)
        exid = x.get('ex')
        if exid not in ex_by:
            errs.append(f'{xid}：未知交换 {exid}')
            continue
        e = ex_by[exid]
        if x.get('batch') not in done_b:
            errs.append(f"{xid}：所属批次 {x.get('batch')} 没有收据")
        line, kind = x.get('line'), x.get('kind')
        if not isinstance(line, int) or not (e['line_start'] <= line <= e['line_end']):
            errs.append(f'{xid}：line 越出交换范围')
        if kind not in KINDS:
            errs.append(f'{xid}：kind 无效')
        if kind in USER_KINDS and x.get('quote') is not True:
            errs.append(f'{xid}：用户轮事件必须逐字引用')
        if x.get('quote') is True and isinstance(line, int) and 1 <= line <= c.n:
            if x.get('text', '') not in c.text[line - 1]:
                errs.append(f'{xid}：quote 不是第 {line} 行的逐字子串')
        for rv in x.get('refs', []) or []:
            if rv not in cand[exid]:
                errs.append(f'{xid}：refs {rv!r} 不在候选中')
        per[exid].append(x)
    for eid in sorted(done_ex):
        rs = per.get(eid, [])
        if not rs:
            errs.append(f'{eid}：已完成批次中没有事件也没有 NONE')
            continue
        if len(rs) > MAX_EVENTS_PER_EX:
            errs.append(f'{eid}：事件数超过上限')
        if ex_by[eid]['kind'] == 'USER_EXCHANGE':
            if not any(x['kind'] in USER_KINDS or x['kind'] == 'NONE' for x in rs):
                errs.append(f'{eid}：用户轮既无 USER_* 事件也无 NONE（用户的话没有被记录或说明）')
    user_ex = [eid for eid in done_ex if ex_by[eid]['kind'] == 'USER_EXCHANGE']
    stats = {'batches_done': len(done_b), 'batches_total': len(bats),
             'exchanges_covered': len(done_ex), 'exchanges_total': len(ex),
             'user_exchanges_covered': len(user_ex),
             'events_by_kind': dict(collections.Counter(x.get('kind') for x in evs))}
    return errs, stats


def check_card(tag):
    p = ROOT / 'cards' / f'{tag}.md'
    if not p.exists():
        return [f'缺少线索卡 cards/{tag}.md'], {}
    data = p.read_bytes()
    text = data.decode('utf-8')
    errs = []
    if len(data) > 40000:
        errs.append('线索卡超过 40000 字节')
    cache = {}

    def known(tg, token):
        if tg not in cache:
            cache[tg] = {x['id'] for x in events_of(tg)} if (ROOT / 'events' / f'{tg}.jsonl').exists() else set()
        return token in cache[tg]

    ev_path = ROOT / 'index' / f'{tag}.evidence.jsonl'
    evid_ids = {x['id'] for x in read_jsonl(ev_path)} if ev_path.exists() else set()
    present, counts, sec = set(), collections.Counter(), None
    for ln in text.split('\n'):
        if ln.startswith('## '):
            sec = ln.strip()
            present.add(sec)
            continue
        if sec is None or not ln.startswith('- '):
            continue
        refs = [m.group(0) for m in ID_RE.finditer(ln)]
        counts[sec] += 1
        if sec in CARD_REF_SECTIONS and not refs:
            errs.append(f'{sec} 中的条目没有事件编号：{ln[:50]}')
        for rv in refs:
            tg = rv.split(':')[0]
            if sec != CARD_CROSS_SECTION and tg != tag:
                errs.append(f'{sec} 中引用了其他线的编号：{rv}')
            if ':V' in rv and not known(tg, rv):
                errs.append(f'未知事件编号：{rv}')
            if ':R' in rv and tg == tag and rv not in evid_ids:
                errs.append(f'未知证据编号：{rv}')
    for s in CARD_SECTIONS:
        if s not in present:
            errs.append(f'缺少章节：{s}')
    return errs, {'bytes': len(data), 'bullets_by_section': dict(counts)}


def check_synthesis():
    errs = []
    d = ROOT / 'synthesis'
    for f in SYNTH_FILES:
        if not (d / f).exists():
            errs.append(f'缺少 synthesis/{f}')
    for tag in TAGS:
        p = ROOT / 'reports' / f'{tag}.final.json'
        if not p.exists() or rj(p).get('status') != 'PASS':
            errs.append(f'{tag} 尚未通过 final 校验')
    ev = {tg: {x['id'] for x in events_of(tg)} for tg in TAGS}
    rv = {}
    for tg in TAGS:
        p = ROOT / 'index' / f'{tg}.evidence.jsonl'
        rv[tg] = {x['id'] for x in read_jsonl(p)} if p.exists() else set()
    if d.exists():
        for f in sorted(d.iterdir()):
            if not f.is_file():
                continue
            for m in ID_RE.finditer(f.read_text(encoding='utf-8')):
                tok, tg = m.group(0), m.group(1)
                if ':V' in tok and tok not in ev.get(tg, set()):
                    errs.append(f'{f.name}：未知事件编号 {tok}')
                if ':R' in tok and tok not in rv.get(tg, set()):
                    errs.append(f'{f.name}：未知证据编号 {tok}')
    cl = d / 'CLAIMS.tsv'
    if cl.exists():
        rows = [ln.split('\t') for ln in cl.read_text(encoding='utf-8').split('\n') if ln.strip()]
        if not rows or rows[0][:5] != ['claim_id', 'claim', 'status', 'refs', 'threads']:
            errs.append('CLAIMS.tsv 表头应为 claim_id、claim、status、refs、threads（制表符分隔）')
        for r in rows[1:]:
            if len(r) != 5:
                errs.append(f'CLAIMS.tsv 列数不对：{r[0] if r else ""}')
                continue
            if r[2] not in CLAIM_STATUS:
                errs.append(f'{r[0]}：status 无效 {r[2]!r}')
            if not ID_RE.search(r[3]):
                errs.append(f'{r[0]}：缺少证据编号')
    stats = {'files': sorted(p.name for p in d.iterdir()) if d.exists() else []}
    return errs, stats


def report_out(path, label, errs, stats):
    status = 'PASS' if not errs else 'FAIL'
    wj(path, {'label': label, 'status': status, 'error_count': len(errs), 'errors': errs[:300],
              'stats': stats, 'utc': utc_now()})
    print(f'{label}: {status}（错误 {len(errs)}）')
    for m in errs[:30]:
        print('  -', m)
    return 0 if status == 'PASS' else 1


def cmd_verify_audit(tag, min_recall):
    sp, ap = ROOT / 'audits' / f'{tag}.sample.json', ROOT / 'audits' / f'{tag}.auditor.jsonl'
    if not sp.exists() or not ap.exists():
        die(f'缺少 {sp.name} 或 {ap.name}')
    sample = set(rj(sp)['exes'])
    have = collections.defaultdict(set)
    for x in events_of(tag):
        have[x['ex']].add(x.get('line'))
    errs, misses, total, covered = [], [], 0, 0
    for r in read_jsonl(ap):
        exid = str(r.get('ex', ''))
        if ':' not in exid:
            exid = f'{tag}:{exid}'
        line = r.get('line')
        if exid not in sample:
            errs.append(f'{exid} 不在抽样清单中')
            continue
        if not isinstance(line, int):
            errs.append(f'{exid}：line 不是整数')
            continue
        total += 1
        if line in have.get(exid, set()):
            covered += 1
        else:
            misses.append(f'{exid} 第 {line} 行')
    recall = (covered / total) if total else 0.0
    if total == 0:
        errs.append('审计者清单为空')
    elif recall < min_recall:
        errs.append(f'召回率 {recall:.3f} 低于门槛 {min_recall}')
    stats = {'auditor_points': total, 'covered': covered, 'recall': round(recall, 4),
             'min_recall': min_recall, 'sampled_exchanges': len(sample), 'misses': misses[:100]}
    return report_out(ROOT / 'reports' / f'{tag}.audit.json', f'{tag} audit', errs, stats)


def cmd_verify(a):
    if a.stage == 'synthesis':
        errs, stats = check_synthesis()
        return report_out(ROOT / 'reports' / 'synthesis.json', 'synthesis', errs, stats)
    if not a.tag:
        die('该阶段需要 --tag')
    tag = a.tag
    if a.stage == 'events':
        errs, stats = check_events(tag)
        return report_out(ROOT / 'reports' / f'{tag}.events.json', f'{tag} events', errs, stats)
    if a.stage == 'cards':
        errs, stats = check_card(tag)
        return report_out(ROOT / 'reports' / f'{tag}.cards.json', f'{tag} cards', errs, stats)
    if a.stage == 'audit':
        return cmd_verify_audit(tag, a.min_recall)
    # final
    errs, stats = check_events(tag)
    ex, bats, _e, _m = load_index(tag)
    if len(done_batches(tag)) != len(bats):
        errs.append(f'未完成的批次：{len(bats) - len(done_batches(tag))} 个')
    cerrs, cstats = check_card(tag)
    errs += cerrs
    stats['card'] = cstats
    status = 'PASS' if not errs else 'FAIL'
    wj(ROOT / 'reports' / f'{tag}.final.json',
       {'tag': tag, 'stage': 'final', 'status': status, 'error_count': len(errs), 'errors': errs[:300],
        'stats': stats, 'utc': utc_now()})
    if status == 'PASS':
        set_status(tag, 'DONE')
    print(f'{tag} final: {status}（错误 {len(errs)}）')
    for m in errs[:30]:
        print('  -', m)
    return 0 if status == 'PASS' else 1


def cmd_sample(a):
    ex, _b, _e, _m = load_index(a.tag)
    picked = []
    for e in ex:
        h = int(sha256(f'{a.seed}:{e["exid"]}')[:12], 16) / float(16 ** 12)
        if h < a.rate:
            picked.append(e['exid'])
    if not picked and ex:
        picked = [ex[len(ex) // 2]['exid']]
    wj(ROOT / 'audits' / f'{a.tag}.sample.json',
       {'tag': a.tag, 'rate': a.rate, 'seed': a.seed, 'exes': picked, 'n_exchanges': len(ex),
        'generated_utc': utc_now()})
    print(f'{a.tag}: 抽样 {len(picked)} / {len(ex)} 个交换（种子 {a.seed}）')
    return 0


def cmd_batch_dispatch(a):
    return cmd_batch(a)


def main(argv=None):
    ap = argparse.ArgumentParser(description='GUI 综合重读（v3）工具')
    sub = ap.add_subparsers(dest='cmd', required=True)
    sub.add_parser('segment')
    p = sub.add_parser('status')
    p.add_argument('--tag', choices=TAGS)
    p = sub.add_parser('batch')
    p.add_argument('--tag', required=True, choices=TAGS)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--id')
    g.add_argument('--next', action='store_true')
    p = sub.add_parser('add')
    p.add_argument('--tag', required=True, choices=TAGS)
    p.add_argument('--batch', required=True)
    p.add_argument('--events', required=True)
    p.add_argument('--reader', required=True)
    p.add_argument('--model', required=True)
    p = sub.add_parser('verify')
    p.add_argument('--tag', choices=TAGS)
    p.add_argument('--stage', required=True, choices=['events', 'cards', 'final', 'audit', 'synthesis'])
    p.add_argument('--min-recall', type=float, default=0.95)
    p = sub.add_parser('sample')
    p.add_argument('--tag', required=True, choices=TAGS)
    p.add_argument('--rate', type=float, default=0.05)
    p.add_argument('--seed', default='gsr-audit-v1')
    a = ap.parse_args(argv)
    table = {'segment': cmd_segment, 'status': cmd_status, 'batch': cmd_batch_dispatch,
             'add': cmd_add, 'verify': cmd_verify, 'sample': cmd_sample}
    return table[a.cmd](a)


if __name__ == '__main__':
    sys.exit(main())
