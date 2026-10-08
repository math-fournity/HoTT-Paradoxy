#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""问答树的机器校验（v3）：标注、分支卡、抽样、审计、综合。

只读 qa/、annotations/、cards/、synthesis/；只写 reports/ 与 audits/（抽样清单）。
阶段（--stage）：
  annotations  每个自有轮恰好一条标注；字段与身份合法；引文与 refs 逐字出现在该轮文档中。
  cards        分支卡章节齐全；终点引用末轮；分叉节点引用分叉轮；每条有效引用。
  sample       生成抽样清单 audits/<单元>.sample.json。须在标注开始之前运行；已有标注的单元拒绝重抽。
  audit        比较标注者与独立审计者在抽样轮上的状态一致率（SOP 006）。
  synthesis    综合文件的引用、论断表、用户原话引文、反例条目与接手指南结构。
  all          annotations 与 cards。
报告：每个单元一份 reports/<阶段>--<单元>.json，并行会话互不覆盖；不带 --unit 的全量运行另写 reports/<阶段>.json 汇总。
退出码：0 = PASS；1 = FAIL；2 = 用法或单元名错误。
"""
import argparse
import collections
import datetime
import hashlib
import json
import math
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]          # audit/GUI-SYNTH-REDO
QA = ROOT / 'qa'
REPORTS = ROOT / 'reports'
AUDITS = ROOT / 'audits'
CARDS = ROOT / 'cards'
SYNTH = ROOT / 'synthesis'
ANN_DEFAULT = ROOT / 'annotations'
STATUS = {'ANSWERED', 'OPEN', 'DEFERRED', 'SUPERSEDED', 'ERROR', 'UNCLEAR', 'NO_CONTENT'}
REQUIRED = ['doc', 'intent', 'ai_action', 'outcome', 'status', 'intent_quote', 'ai_quote', 'refs',
            'reader', 'model']
CARD_SECTIONS = ['## 终点', '## 回溯（终点到分叉）', '## 分叉节点', '## 独有阶段', '## 未决与风险']
REF_RE = re.compile(r'\[(dev-\d{2}|archive-[0-9a-f]{8}|unexported-[0-9a-f]{8})#(\d{4})\]')
GLM_RE = re.compile(r'glm[\s_-]*5\.?3', re.IGNORECASE)
QUOTE_RE = re.compile(r'「([^」\n]+)」')
SAMPLE_RATE = 0.05
SAMPLE_MIN = 2
SAMPLE_SEED = 'gui-qa-tree-audit-v1'
AUDIT_GATE = 0.9
SYNTH_FILES = ['THREADS-MATRIX.md', 'CLAIMS.tsv', 'USER-STATEMENTS.md', 'CONTRADICTIONS.md', 'HANDOFF.md']
CLAIM_STATUS = {'SUPPORTED', 'ASSERTED_ONLY', 'CONTRADICTED', 'SUPERSEDED', 'OPEN'}
HANDOFF_KEYS = ['先读', '跳过', '不能相信', '待用户裁定', '下一步']


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True) + '\n', encoding='utf-8')


def read_jsonl(path):
    return [json.loads(x) for x in path.read_text(encoding='utf-8').split('\n') if x.strip()]


def units():
    """校验单元：分支文件夹（dev-*、archive-*）与每个不可见尾部段（unexported-<前8位>）。"""
    out = {}
    for d in sorted(QA.iterdir()):
        if d.is_dir() and d.name != '_unexported' and (d / '_index.jsonl').exists():
            out[d.name] = d
    tails = QA / '_unexported'
    if tails.is_dir():
        for d in sorted(tails.iterdir()):
            if d.is_dir() and (d / '_index.jsonl').exists():
                out[f'unexported-{d.name[:8]}'] = d
    return out


def folder_of(unit):
    return units().get(unit)


def unit_exists(name):
    return name in units()


def load_index(unit):
    return {r['doc']: r for r in read_jsonl(folder_of(unit) / '_index.jsonl')}


def doc_text(unit, doc):
    return (folder_of(unit) / f'{doc}.md').read_text(encoding='utf-8')


def annotation_files(unit, ann_root):
    """单元的标注文件：<单元>.jsonl 及分部文件 <单元>.<部分>.jsonl。"""
    return sorted(p for p in ann_root.glob('*.jsonl')
                  if p.name == f'{unit}.jsonl' or p.name.startswith(f'{unit}.'))


def fork_of(unit):
    bj = folder_of(unit) / '_branch.json'
    if not bj.exists():
        return None
    fk = json.loads(bj.read_text(encoding='utf-8')).get('fork')
    if not fk:
        return None
    return {'parent_branch': fk.get('parent_branch'), 'parent_doc': fk.get('parent_doc')}


def identity_errors(where, r):
    """reader 与 model 必须非空；model 不得为 GLM-5.3 家族（SOP 006 §4）。"""
    errs = []
    for k in ('reader', 'model'):
        v = r.get(k)
        if not isinstance(v, str) or not v.strip():
            errs.append(f'{where}: {k} 为空')
    m = r.get('model')
    if isinstance(m, str) and GLM_RE.search(m):
        errs.append(f'{where}: model 为 GLM-5.3 家族（SOP 006 §4）')
    return errs


def check_annotations(unit, ann_root, subset=None):
    errs = []
    docs = load_index(unit)
    expected = set(docs) if subset is None else set(docs) & subset
    files = annotation_files(unit, ann_root)
    if not files:
        return [f'{unit}: 缺少 annotations/{unit}.jsonl（或分部文件 {unit}.<部分>.jsonl）'], \
            {'docs': len(docs), 'expected': len(expected), 'annotated': 0}
    rows = []
    for p in files:
        rows += read_jsonl(p)
    seen = collections.Counter(r.get('doc') for r in rows)
    for d, c in seen.items():
        if c > 1:
            errs.append(f'{unit} {d}: 重复标注 {c} 次')
    for d in sorted(expected):
        if d not in seen:
            errs.append(f'{unit} {d}: 缺少标注（覆盖不全）')
    texts = {}
    for i, r in enumerate(rows, 1):
        where = f"{unit} 第 {i} 行 doc={r.get('doc')}"
        miss = [k for k in REQUIRED if k not in r]
        if miss:
            errs.append(f'{where}: 缺字段 {miss}')
            continue
        d = r['doc']
        if d not in docs:
            errs.append(f'{where}: 不是本单元的自有轮')
            continue
        errs += identity_errors(where, r)
        if r['status'] not in STATUS:
            errs.append(f"{where}: status 无效 {r['status']!r}")
        for k, lim in (('intent', 160), ('ai_action', 200), ('outcome', 160)):
            v = r[k]
            if not isinstance(v, str) or not v.strip():
                errs.append(f'{where}: {k} 为空')
            elif len(v) > lim:
                errs.append(f'{where}: {k} 超过 {lim} 字')
        if d not in texts:
            texts[d] = doc_text(unit, d)
        text = texts[d]
        for k in ('intent_quote', 'ai_quote'):
            q = r[k]
            if not isinstance(q, str):
                errs.append(f'{where}: {k} 须为字符串')
            elif q and q not in text:
                errs.append(f'{where}: {k} 不是该轮文档中的逐字子串')
            elif len(q) > 200:
                errs.append(f'{where}: {k} 超过 200 字')
        if not isinstance(r['refs'], list):
            errs.append(f'{where}: refs 须为列表')
        else:
            for ref in r['refs']:
                if not isinstance(ref, str) or ref not in text:
                    errs.append(f'{where}: refs 中的 {ref!r} 不在该轮文档中')
    stats = {'docs': len(docs), 'annotated': len(seen),
             'status_counts': dict(collections.Counter(r.get('status') for r in rows))}
    return errs, stats


def sections_of(text):
    out, sec = {}, None
    for ln in text.split('\n'):
        if ln.startswith('## '):
            sec = ln.strip()
            out[sec] = []
        elif sec is not None:
            out[sec].append(ln)
    return out


def check_card(unit):
    errs = []
    path = CARDS / f'{unit}.md'
    if not path.exists():
        return [f'{unit}: 缺少 cards/{unit}.md'], {}
    secs = sections_of(path.read_text(encoding='utf-8'))
    for s in CARD_SECTIONS:
        if s not in secs:
            errs.append(f'{unit}: 缺少章节 {s}')
    own = load_index(unit)
    last = max(own) if own else None
    for sec, lines in secs.items():
        for ln in lines:
            if not ln.startswith('- '):
                continue
            refs = REF_RE.findall(ln)
            if not refs:
                errs.append(f'{unit} {sec}: 条目没有 [分支#NNNN] 引用：{ln[:50]}')
            for br, dn in refs:
                if br == unit:
                    if dn not in own:
                        errs.append(f'{unit} {sec}: 引用的本分支轮次不存在 {dn}')
                elif unit_exists(br) and dn in load_index(br):
                    continue
                else:
                    errs.append(f'{unit} {sec}: 引用的轮次不存在 [{br}#{dn}]')
    if '## 终点' in secs and last and f'[{unit}#{last}]' not in '\n'.join(secs['## 终点']):
        errs.append(f'{unit} ## 终点: 未引用末轮 [{unit}#{last}]')
    fk = fork_of(unit)
    if '## 分叉节点' in secs and fk:
        ref = f"[{fk['parent_branch']}#{fk['parent_doc']:04d}]"
        if ref not in '\n'.join(secs['## 分叉节点']):
            errs.append(f'{unit} ## 分叉节点: 未引用分叉轮 {ref}')
    return errs, {'last_doc': last}


def check_fork(unit):
    fk = fork_of(unit)
    if not fk:
        return []
    parent, pdoc = fk['parent_branch'], fk['parent_doc']
    if not unit_exists(parent):
        return [f'{unit}: 分叉的父分支不存在 {parent}']
    if f'{pdoc:04d}' not in load_index(parent):
        return [f'{unit}: 分叉节点 {parent}#{pdoc:04d} 不存在']
    return []


def sample_docs(unit):
    """每单元抽取 max(2, ⌈5%·n⌉) 轮（不超过 n）：按 sha256(种子:单元:轮号) 排序取前 k 个，结果可复现。"""
    docs = sorted(load_index(unit))
    n = len(docs)
    k = min(n, max(SAMPLE_MIN, math.ceil(SAMPLE_RATE * n)))
    ranked = sorted(docs, key=lambda d: hashlib.sha256(f'{SAMPLE_SEED}:{unit}:{d}'.encode('utf-8')).hexdigest())
    return sorted(ranked[:k])


def check_audit(unit, ann_root):
    errs = []
    sp = AUDITS / f'{unit}.sample.json'
    apath = AUDITS / f'{unit}.auditor.jsonl'
    if not sp.exists():
        return [f'{unit}: 缺少抽样清单 audits/{unit}.sample.json（先运行 --stage sample）'], {}
    sample = json.loads(sp.read_text(encoding='utf-8'))['docs']
    producer, prod_readers = {}, set()
    for p in annotation_files(unit, ann_root):
        for r in read_jsonl(p):
            producer[r.get('doc')] = r
            prod_readers.add(r.get('reader'))
    auditor = {}
    if apath.exists():
        for r in read_jsonl(apath):
            auditor[r.get('doc')] = r
    texts, agree = {}, 0
    for d in sample:
        if d not in producer:
            errs.append(f'{unit} {d}: 标注者缺少标注')
        if d not in auditor:
            errs.append(f'{unit} {d}: 审计者缺少标注')
            continue
        a = auditor[d]
        errs += identity_errors(f'{unit} {d} 审计者', a)
        if a.get('reader') in prod_readers:
            errs.append(f'{unit} {d}: 审计会话与标注会话相同（SOP 006 §4）')
        if a.get('status') not in STATUS:
            errs.append(f"{unit} {d}: 审计者 status 无效 {a.get('status')!r}")
        if d not in texts:
            texts[d] = doc_text(unit, d)
        for k in ('intent_quote', 'ai_quote'):
            q = a.get(k, '')
            if isinstance(q, str) and q and q not in texts[d]:
                errs.append(f'{unit} {d}: 审计者的 {k} 不是逐字子串')
        if d in producer and producer[d].get('status') == a.get('status'):
            agree += 1
    rate = agree / len(sample) if sample else 0.0
    if sample and rate < AUDIT_GATE:
        errs.append(f'{unit}: 状态一致率 {rate:.2f} 低于 {AUDIT_GATE}，须整体复核（SOP 006 §1）')
    return errs, {'sampled': len(sample), 'agree': agree, 'rate': round(rate, 4)}


def check_synthesis():
    errs, stats = [], {}
    if not SYNTH.exists():
        return ['缺少目录 synthesis/'], stats
    for f in SYNTH_FILES:
        if not (SYNTH / f).exists():
            errs.append(f'缺少 synthesis/{f}')
    known = {u: load_index(u) for u in units()}
    texts = {}

    def text_of(u, dn):
        if (u, dn) not in texts:
            texts[(u, dn)] = doc_text(u, dn)
        return texts[(u, dn)]

    for f in sorted(p for p in SYNTH.iterdir() if p.is_file()):
        for u, dn in REF_RE.findall(f.read_text(encoding='utf-8')):
            if u not in known or dn not in known[u]:
                errs.append(f'{f.name}: 引用的轮次不存在 [{u}#{dn}]')
    us = SYNTH / 'USER-STATEMENTS.md'
    if us.exists():
        n = 0
        for i, line in enumerate(us.read_text(encoding='utf-8').split('\n'), 1):
            quotes = QUOTE_RE.findall(line)
            if not quotes:
                continue
            refs = [(u, dn) for u, dn in REF_RE.findall(line) if u in known and dn in known[u]]
            if not refs:
                errs.append(f'USER-STATEMENTS.md 第 {i} 行：有引文但没有可用的 [分支#NNNN]')
                continue
            for q in quotes:
                n += 1
                if not any(q in text_of(u, dn) for u, dn in refs):
                    errs.append(f'USER-STATEMENTS.md 第 {i} 行：引文不在所引轮中：「{q[:40]}」')
        stats['user_quotes'] = n
    cl = SYNTH / 'CLAIMS.tsv'
    if cl.exists():
        rows = [ln.split('\t') for ln in cl.read_text(encoding='utf-8').split('\n') if ln.strip()]
        if not rows or rows[0][:5] != ['claim_id', 'claim', 'status', 'refs', 'threads']:
            errs.append('CLAIMS.tsv 表头应为 claim_id、claim、status、refs、threads（制表符分隔）')
        ids = set()
        for r in rows[1:]:
            cid = r[0] if r else ''
            if len(r) != 5:
                errs.append(f'CLAIMS.tsv 列数不对：{cid}')
                continue
            if cid in ids:
                errs.append(f'CLAIMS.tsv claim_id 重复：{cid}')
            ids.add(cid)
            if not r[1].strip():
                errs.append(f'{cid}: claim 为空')
            if r[2] not in CLAIM_STATUS:
                errs.append(f'{cid}: status 无效 {r[2]!r}')
            if not REF_RE.search(r[3]):
                errs.append(f'{cid}: 缺少 [分支#NNNN] 证据引用')
        stats['claims'] = len(rows) - 1
    co = SYNTH / 'CONTRADICTIONS.md'
    if co.exists():
        for i, ln in enumerate(co.read_text(encoding='utf-8').split('\n'), 1):
            if ln.startswith('- ') and not REF_RE.search(ln):
                errs.append(f'CONTRADICTIONS.md 第 {i} 行：条目没有 [分支#NNNN] 引用')
    tm = SYNTH / 'THREADS-MATRIX.md'
    if tm.exists() and not REF_RE.search(tm.read_text(encoding='utf-8')):
        errs.append('THREADS-MATRIX.md 没有任何 [分支#NNNN] 引用')
    hf = SYNTH / 'HANDOFF.md'
    if hf.exists():
        hl = hf.read_text(encoding='utf-8').split('\n')
        heads = [ln for ln in hl if ln.startswith('#')]
        for kw in HANDOFF_KEYS:
            if not any(kw in h for h in heads):
                errs.append(f'HANDOFF.md 缺少标题含「{kw}」的一节')
        in_next, cnt = False, 0
        for ln in hl:
            if ln.startswith('#'):
                in_next = '下一步' in ln
            elif in_next and re.match(r'\s*(?:- |\d+[.、)])', ln):
                cnt += 1
        if not 1 <= cnt <= 5:
            errs.append(f'HANDOFF.md「下一步」条目数为 {cnt}，应为 1 至 5 条')
    return errs, stats


def make_report(stage, errs, stats, extra=None):
    body = {'stage': stage, 'status': 'PASS' if not errs else 'FAIL', 'error_count': len(errs),
            'errors': errs[:300], 'stats': stats, 'utc': utc_now()}
    if extra:
        body.update(extra)
    return body


def print_errors(errs, limit=40):
    for m in errs[:limit]:
        print('  -', m)


def run_sample(names, ann_root, force):
    rc = 0
    for u in names:
        if annotation_files(u, ann_root):
            print(f'{u}: 已有标注，拒绝重抽（抽样须在标注开始之前固定）', file=sys.stderr)
            rc = 1
            continue
        sp = AUDITS / f'{u}.sample.json'
        if sp.exists() and not force:
            print(f'{u}: 抽样清单已存在，未覆盖（需要 --force）')
            continue
        docs = sample_docs(u)
        n = len(load_index(u))
        write_json(sp, {'unit': u, 'rule': f'max({SAMPLE_MIN}, ceil({SAMPLE_RATE} * n)) 轮，不超过 n',
                        'seed': SAMPLE_SEED, 'n_docs': n, 'docs': docs, 'generated_utc': utc_now()})
        print(f'{u}: 抽样 {len(docs)} / {n} 轮')
    return rc


def run_audit(names, ann_root, full):
    rc, rows, agree_all, sampled_all = 0, {}, 0, 0
    for u in names:
        errs, stats = check_audit(u, ann_root)
        write_json(REPORTS / f'audit--{u}.json', make_report('audit', errs, stats, {'unit': u}))
        rows[u] = stats
        agree_all += stats.get('agree', 0)
        sampled_all += stats.get('sampled', 0)
        if errs:
            rc = 1
            print(f'audit {u}: FAIL（错误 {len(errs)}）')
            print_errors(errs, 10)
        else:
            print(f'audit {u}: PASS（{stats["agree"]}/{stats["sampled"]}）')
    if full:
        overall = agree_all / sampled_all if sampled_all else 0.0
        gerrs = [] if sampled_all and overall >= AUDIT_GATE else \
            [f'总体状态一致率 {overall:.4f}（{agree_all}/{sampled_all}）低于 {AUDIT_GATE}（C7）']
        write_json(REPORTS / 'audit.json', make_report('audit', gerrs, {'units': rows, 'overall_rate': round(overall, 4),
                                                                      'agree': agree_all, 'sampled': sampled_all}))
        print(f'audit 总体: {"PASS" if not gerrs else "FAIL"}（{agree_all}/{sampled_all} = {overall:.4f}）')
        rc = rc or (1 if gerrs else 0)
    return rc


def main(argv=None):
    ap = argparse.ArgumentParser(description='问答树的标注、分支卡、抽样、审计与综合校验（v3）')
    ap.add_argument('--stage', choices=['annotations', 'cards', 'all', 'sample', 'audit', 'synthesis'],
                    default='all')
    ap.add_argument('--unit', action='append', help='单元名，可重复；省略则为全部单元')
    ap.add_argument('--ann-root', default=str(ANN_DEFAULT))
    ap.add_argument('--docs', default=None, help='覆盖检查的轮号范围，如 0001-0032（分部标注时使用）')
    ap.add_argument('--force', action='store_true', help='sample：覆盖已有的抽样清单（已有标注的单元仍拒绝）')
    a = ap.parse_args(argv)
    known = units()
    names = a.unit or sorted(known)
    bad = [u for u in names if u not in known]
    if bad:
        print(f'未知单元：{", ".join(bad)}', file=sys.stderr)
        return 2
    ann_root = pathlib.Path(a.ann_root)
    if a.stage == 'synthesis':
        errs, stats = check_synthesis()
        write_json(REPORTS / 'synthesis.json', make_report('synthesis', errs, stats))
        print(f"synthesis: {'PASS' if not errs else 'FAIL'}（错误 {len(errs)}）")
        print_errors(errs)
        return 0 if not errs else 1
    if a.stage == 'sample':
        return run_sample(names, ann_root, a.force)
    if a.stage == 'audit':
        return run_audit(names, ann_root, full=a.unit is None)
    subset = None
    if a.docs:
        lo, hi = a.docs.split('-')
        subset = {f'{i:04d}' for i in range(int(lo), int(hi) + 1)}
    stages = ['annotations', 'cards'] if a.stage == 'all' else [a.stage]
    rc = 0
    for st in stages:
        agg, msgs = {}, []
        for u in names:
            if st == 'annotations':
                errs, stats = check_annotations(u, ann_root, subset)
            else:
                if u.startswith('unexported-'):
                    continue
                e1, stats = check_card(u)
                errs = e1 + check_fork(u)
            write_json(REPORTS / f'{st}--{u}.json',
                       make_report(st, errs, stats, {'unit': u, 'subset': a.docs}))
            agg[u] = {'status': 'PASS' if not errs else 'FAIL', 'error_count': len(errs)}
            msgs += errs
        total = len(msgs)
        if a.unit is None and a.docs is None:
            write_json(REPORTS / f'{st}.json', make_report(st, msgs, {'units': agg}))
        print(f"{st}: {'PASS' if total == 0 else 'FAIL'}（单元 {len(agg)}，错误 {total}）")
        print_errors(msgs)
        rc = rc or (1 if total else 0)
    return rc


if __name__ == '__main__':
    sys.exit(main())
