#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUI-LINEAGE-KB / build_scope.py — 从冻结输入层推导每线提取范围（只读，不写任何输入）。

为什么存在：workflow 方案 §2 要求「每线 agent 只覆盖本线自有增量」，§4 R1 要求每条发现带
「导出文件行号 与 QA 轮号」双锚。三个输入层各说各的坐标，需要一台机器把它们合成一张表：

  1. `audit/GUI-ASSET-RECOVERY/manifest.json` → `alignment.per_file[tag].unique_ranges`
     是**文本级**唯一区间（与父线导出逐行 diff），不是轮次归属：研究发起人的同一段核心提问
     在 dev-08 与 dev-03 逐字重复时，dev-03 自己那一轮有 24 行落在 SHARED 段里
     （dev-03 12282-12305，src dev-08 13148-13171）。所以轮次归属只认 QA 树
     （`qa/<line>/NNNN.md` 存在即该线自有轮），manifest 只用来定**前缀/自有边界**。
  2. `audit/GUI-SYNTH-REDO/qa/<line>/_index.jsonl` 的 line_from/line_to 与 frontmatter
     的 source_lines 是**源 rollout(jsonl) 坐标**，不是导出行号：dev-08 最后一轮
     byte_to=166,684,447 而导出文件只有 1,637,525 字节。
  3. 裁决#3 的 124 轮口径定义在 raw rollout 上（认知闭包 §8），冻结输入层内不可重算，只引用。

本脚本按**块级有序匹配**把 QA 轮号钉到 GUI 导出行号：按文档顺序取本轮最长的非机械用户行作
needle，在导出的 `## User` 块序列里自上一轮之后找第一个包含该 needle 的块，锚点取该块
`## User` 标题行。机械包裹区（goal 续跑块/环境上下文/页面标记/批注 JSON）整体排除——goal
负载会逐字嵌入用户早先的提问，曾把 dev-03 的轮次锚点整批钉偏。

输出 `wflow-lineage/scope.json`：同一输入必得同一输出。退出码非 0 表示输入层不完整。
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
MANIFEST = os.path.join(ROOT, 'audit', 'GUI-ASSET-RECOVERY', 'manifest.json')
QA = os.path.join(ROOT, 'audit', 'GUI-SYNTH-REDO', 'qa')
GUI = os.path.join(ROOT, 'git-worktree对话录')
TREE = os.path.join(QA, '_tree.json')
OUT = os.path.join(ROOT, 'wflow-lineage', 'scope.json')

LINES = ['dev-08', 'dev-03', 'dev-04', 'dev-02', 'dev-01', 'dev-09', 'dev-06', 'dev-07']

# 裁决 #3（2026-10-07）权威轮数口径的结果；口径定义在 raw rollout 上，冻结输入层内不可重算。
# 来源：认知闭包/GUI-ASSET-RECOVERY-001.md §8 裁决 #3。
ADJUDICATION_124 = {
    'dev-08': 56, 'dev-03': 18, 'dev-04': 11, 'dev-02': 10,
    'dev-01': 10, 'dev-09': 8, 'dev-06': 7, 'dev-07': 4,
}
ADJUDICATION_TOTAL = sum(ADJUDICATION_124.values())

# 裁决 #3 定义「机械前缀」时逐字列出的字符串；用于 needle 候选清洗。
MECH_PREFIXES = (
    '<environment_context>', '<external_codex_apps_open_page>', '<user_instructions>',
    '<system-reminder', '<codex_', '# AGENTS.md instructions', '<INSTRUCTIONS>',
    '<project_context',
)
# 导出中整段属于机械包裹的标签（官方 gui_backtrace.py 的 user_request() 同源判定）。
WRAPPER_TAGS = (
    'codex_internal_context', 'external_codex_apps_open_page', 'environment_context',
    'response-annotations', 'user_instructions',
)
BLOCK_RE = re.compile(r'(?m)^(## User|## Codex|### Files changed in this reply)\s*$')
MIN_NEEDLE = 8
NEEDLE_SHORTENINGS = (None, 40, 30, 20)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def split_blocks(text):
    body = text.split('\n---\n', 1)[1] if text.startswith('---') else text
    out, cur = [], None
    for part in BLOCK_RE.split(body):
        if part in ('## User', '## Codex', '### Files changed in this reply'):
            cur = [part, '']
            out.append(cur)
        elif cur is not None:
            cur[1] += part
    return out


def strip_boilerplate(text):
    text = re.sub(r'<external_codex_apps_open_page>.*?</external_codex_apps_open_page>', '', text, flags=re.S)
    text = re.sub(r'<environment_context>.*?</environment_context>', '', text, flags=re.S)
    text = re.sub(r'<codex_internal_context source="goal">.*?(?:</codex_internal_context>|\Z)', '', text, flags=re.S)
    if '<response-annotations>' in text and '## My request:' in text:
        text = text.split('## My request:', 1)[1]
    return text


def clean_lines(text):
    """去机械包裹后的用户正文行（长度 ≥ MIN_NEEDLE，去掉机械前缀行）。"""
    for raw in strip_boilerplate(text).split('\n'):
        s = raw.strip()
        if len(s) >= MIN_NEEDLE and not any(s.startswith(p) for p in MECH_PREFIXES):
            yield s


def _line_of(offsets, pos):
    lo, hi = 0, len(offsets) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if offsets[mid] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return lo


def mechanical_line_mask(text):
    """标记导出行里属于机械包裹区的行。goal 负载会逐字嵌入用户早先的提问，必须排除。"""
    lines = text.split('\n')
    bad = [False] * len(lines)
    offsets, pos = [], 0
    for ln in lines:
        offsets.append(pos)
        pos += len(ln) + 1
    for tag in WRAPPER_TAGS:
        for m in re.finditer(re.escape('<' + tag) + r'.*?' + re.escape('</' + tag + '>'), text, flags=re.S):
            for i in range(_line_of(offsets, m.start()), _line_of(offsets, m.end()) + 1):
                bad[i] = True
        op = len(re.findall(re.escape('<' + tag) + r'[ >]', text))
        cl = len(re.findall(re.escape('</' + tag + '>'), text))
        if op > cl:  # 未闭合的开启标签：遮到文末
            m = list(re.finditer(re.escape('<' + tag) + r'[ >]', text))[-1]
            for i in range(_line_of(offsets, m.start()), len(lines)):
                bad[i] = True
    return bad


def export_user_blocks(lines, mech):
    """导出中的 `## User` 块序列 [(header_line, span_end, text)]，按出现顺序。"""
    return export_blocks(lines, mech, '## User')


def export_blocks(lines, mech, kind):
    """导出中某类块的序列（`## User` 或 `## Codex`），按出现顺序；跳过标题本身在机械区内的块。"""
    out, cur = [], None
    for i, raw in enumerate(lines):
        s = raw.strip()
        if s == kind:
            if cur:
                cur[1] = i  # 上一块到此行为止（0-based 排他）
                out.append(cur)
            cur = [i + 1, None, []]
        elif s in ('## User', '## Codex', '### Files changed in this reply'):
            if cur:
                cur[1] = i
                out.append(cur)
                cur = None
        elif cur is not None:
            cur[2].append(raw)
    if cur:
        cur[1] = len(lines)
        out.append(cur)
    return [(h, e, '\n'.join(t)) for h, e, t in out if not mech[h - 1]]


def prefix_end(alignment_entry):
    """manifest 前缀 SHARED 段的末行：自有内容从这里之后开始（dev-08 无 8 线内父线，返回 1）。"""
    for rng in alignment_entry.get('ranges', []):
        if rng.get('status') == 'SHARED' and rng.get('src') and rng.get('start', 0) <= 2:
            return rng['end']
    return 1


def build_line(tag, manifest_entry, alignment_entry, fork_info, export_text):
    docs = sorted(f for f in os.listdir(os.path.join(QA, tag)) if re.fullmatch(r'\d{4}\.md', f))
    index = {}
    idx_path = os.path.join(QA, tag, '_index.jsonl')
    if os.path.exists(idx_path):
        for ln in open(idx_path, encoding='utf-8'):
            rec = json.loads(ln)
            index[rec['doc']] = rec

    lines = export_text.split('\n')
    mech = mechanical_line_mask(export_text)
    user_blocks = export_user_blocks(lines, mech)
    codex_blocks = export_blocks(lines, mech, '## Codex')
    start_line = prefix_end(alignment_entry) + 1

    rows = []
    prev_header = start_line - 1

    def first_match(needles, blocks):
        for needle in needles:
            for shorten in NEEDLE_SHORTENINGS:
                probe = needle if shorten is None else needle[:shorten]
                if len(probe) < MIN_NEEDLE:
                    continue
                for header, span_end, btext in blocks:
                    if header <= prev_header:
                        continue
                    if probe in btext:
                        return header, span_end, probe
        return None

    for name in docs:
        doc = name[:4]
        blks = split_blocks(open(os.path.join(QA, tag, name), encoding='utf-8').read())
        user_text = '\n'.join(t for k, t in blks if k == '## User')
        codex_text = '\n'.join(t for k, t in blks if k == '## Codex')
        user_needles = sorted(clean_lines(user_text), key=len, reverse=True)
        codex_needles = sorted(clean_lines(codex_text), key=len, reverse=True)

        got, kind = first_match(user_needles, user_blocks), 'user_block'
        if got is None:
            got, kind = first_match(codex_needles, codex_blocks), 'codex_fallback'
        if got is None:
            status = 'export_absent_prose' if (user_needles or codex_needles) \
                else 'no_prose_mechanical_round'
            rows.append({'doc': doc, 'anchor_line': None, 'anchor_status': status,
                         'anchor_block_end': None, 'needle': None})
            continue
        header, span_end, probe = got
        prev_header = header
        rows.append({'doc': doc, 'anchor_line': header, 'anchor_status': kind,
                     'anchor_block_end': span_end + 1 if span_end is not None else None,
                     'needle': probe[:80]})

    # 无 needle 的机械轮不猜行号，只给相邻已锚轮次围出的有界窗口（供 G2 校验用）。
    for i, r in enumerate(rows):
        if r['anchor_line'] is not None:
            continue
        lo = max((rows[j]['anchor_line'] for j in range(i - 1, -1, -1)
                  if rows[j]['anchor_line'] is not None), default=start_line)
        hi = min((rows[j]['anchor_line'] for j in range(i + 1, len(rows))
                  if rows[j]['anchor_line'] is not None), default=manifest_entry['lines'])
        r['anchor_window'] = [lo, hi]

    anchored = [r['anchor_line'] for r in rows if r['anchor_line'] is not None]
    unique_ranges = alignment_entry['unique_ranges']
    unique_parent = next((rng['src'][0] for rng in alignment_entry.get('ranges', [])
                          if rng.get('status') == 'SHARED' and rng.get('src')), None)
    return {
        'export': {'path': os.path.relpath(manifest_entry['path'], ROOT),
                   'lines': manifest_entry['lines'], 'sha256': manifest_entry['sha256']},
        'fork': fork_info,
        'own_docs': len(docs),
        'prefix_end_line': prefix_end(alignment_entry),
        'unique_ranges': unique_ranges,
        'unique_lines': alignment_entry['unique_lines'],
        'unique_relative_to_parent': unique_parent,
        'adjudication_rounds': ADJUDICATION_124[tag],
        'adjudication_citation': '认知闭包/GUI-ASSET-RECOVERY-001.md §8 裁决 #3（2026-10-07）',
        'docs': rows,
        'anchor_summary': {
            'total': len(rows),
            'anchored': len(anchored),
            'mechanical_window': sum(1 for r in rows if r['anchor_status'] == 'no_prose_mechanical_round'),
            'export_absent_prose': sum(1 for r in rows if r['anchor_status'] == 'export_absent_prose'),
            'unresolved_prose_docs': [r['doc'] for r in rows if r['anchor_status'] == 'export_absent_prose'],
        },
        'export_tail': {
            'last_doc_anchored': max((r['doc'] for r in rows if r['anchor_line'] is not None), default=None),
            'last_anchor_line': max(anchored) if anchored else None,
            'export_lines': manifest_entry['lines'],
        },
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--out', default=OUT)
    a = ap.parse_args()

    manifest = json.load(open(MANIFEST, encoding='utf-8'))
    tree = json.load(open(TREE, encoding='utf-8'))
    files = {f['tag']: f for f in manifest['files']}
    alignment = {p['tag']: p for p in manifest['alignment']['per_file']}
    missing = [t for t in LINES if t not in files or t not in alignment]
    if missing:
        print('FATAL: input layers incomplete for %s' % missing, file=sys.stderr)
        return 2

    texts = {t: open(files[t]['path'], encoding='utf-8').read() for t in LINES}
    lines = {}
    for tag in LINES:
        fork = tree['forks'][tag]
        fork = {'parent_branch': fork['parent_branch'], 'parent_doc': fork['parent_doc'],
                'parent_rollout': fork['parent_rollout']}
        lines[tag] = build_line(tag, files[tag], alignment[tag], fork, texts[tag])

    doc = {
        'schema': 'gui-lineage-kb/scope/v1',
        'built_utc': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'built_by': 'wflow-lineage/tools/build_scope.py',
        'inputs': {
            'manifest': {'path': os.path.relpath(MANIFEST, ROOT), 'sha256': sha256_file(MANIFEST),
                         'frozen_at': manifest['frozen_at'], 'head': manifest['head']},
            'qa_tree': {'path': os.path.relpath(TREE, ROOT), 'sha256': sha256_file(TREE)},
            'exports': {t: {'sha256': files[t]['sha256'], 'lines': files[t]['lines'],
                            'hash_verified': sha256_file(files[t]['path']) == files[t]['sha256']}
                        for t in LINES},
        },
        'coordinate_systems': {
            'qa_index_line_range': 'qa/<line>/_index.jsonl 与 NNNN.md frontmatter 的 line_from/line_to 是源 rollout(jsonl) 坐标，不是 GUI 导出行号（dev-08 末轮 byte_to=166,684,447 > 导出 1,637,525 字节）',
            'scope_anchor_line': 'scope.json 的 anchor_line 是本脚本在 GUI 导出内定位的 `## User` 块标题行（1-based），anchor_block_end 是该轮 block 末行',
            'manifest_unique_ranges': '文本级唯一区间（与父线导出逐行 diff）。研究发起人同一段核心提问在 dev-08 与 dev-03 逐字重复时，dev-03 自有轮有 24 行落在 SHARED 段（12282-12305，src dev-08 13148-13171）——它不定轮次归属，只定前缀/自有边界',
            'adjudication_rounds': '裁决#3 口径（raw rollout role=user 记录，剔机械前缀），冻结输入层内不可重算，只引用不推导',
        },
        'caliber': {
            'own_block_docs_total': sum(lines[t]['own_docs'] for t in LINES),
            'block_coordinate_252_note': 'QA 树 NNNN.md 全树 252 个 = 8 线自有 239 个 + archive-01a0fb08 3 个 + archive-01a0fb73 10 个',
            'adjudication_rounds': ADJUDICATION_124,
            'adjudication_total': ADJUDICATION_TOTAL,
        },
        'invisible_tails': [
            {'rollout_id': e['rollout_id'], 'folder': e['folder'],
             'visible_user_turns': e['user_turns_visible'], 'not_visible_user_turns': e['user_turns_not_visible']}
            for e in tree.get('invisible_tails', [])
        ],
        'invisible_turns_total': sum(e['user_turns_not_visible'] for e in tree.get('invisible_tails', [])),
        'lines': lines,
    }

    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    tmp = a.out + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(doc, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    os.replace(tmp, a.out)

    print('scope written: %s' % a.out)
    print('%-8s %5s %8s %8s %10s %s' % ('line', 'docs', 'anchored', 'mech-win', 'absent', 'tail'))
    for tag in LINES:
        s = lines[tag]['anchor_summary']
        tail = lines[tag]['export_tail']
        print('%-8s %5d %8d %8d %10d %s@%s/%s' % (
            tag, s['total'], s['anchored'], s['mechanical_window'], s['export_absent_prose'],
            tail['last_doc_anchored'], tail['last_anchor_line'], tail['export_lines']))
        if s['unresolved_prose_docs']:
            print('         EXPORT_ABSENT   : %s' % s['unresolved_prose_docs'])
    return 0


if __name__ == '__main__':
    sys.exit(main())
