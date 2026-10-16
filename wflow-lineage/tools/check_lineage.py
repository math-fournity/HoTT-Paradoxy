#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUI-LINEAGE-KB / check_lineage.py — 按 §5 门禁 G1/G2/G4/G5/G6/G8 机械校验 lineage 产物（只读）。

与 wflow-lineage/scope.json（由 build_scope.py 从冻结输入层生成）配套：G1 轮覆盖、G2 双锚与
枚举合法性、G4 D3 资产在 CROSS-FEED 的机验覆盖、G5 carried 落点的 git 可解析性、G6 KB-INDEX
相对链接解析、G8 ledger 无未结 CONFLICT/UNKNOWN。G3（判词逐字回原文）另有 --seed 抽样预检，
供 Master 在派审计 agent 之前自查；N10 审计 agent 仍须用**自己的新鲜种子**独立复跑，本脚本的
结果不替代 G3。

机验与语义的分界（AUDIT.md 必须照此写）：
  G4_mech  只证明 619 个 A-ID 都在 CROSS-FEED.md 出现过——「出现过」不等于「有归宿＋一句理由」，
           语义部分由 N10 逐条核。
  G5_mech  只证明 carried 行的 artifact_ref 路径可在工作树或所引 git ref 解析；不证明那个落点
           真的承载了该判词，语义部分由 N10 核。

判定口径（与方案 §4 一致）：
  R1 双锚  DISCOVERIES.tsv 每行 round 或 export_line 至少其一可定位。
  G2       round 必须是 scope.json 里该线的自有轮；export_line 必须落在该轮的锚点区间内
           （codex_fallback 锚的是回答块，窗口为该块起至下一轮锚点前）；无锚机械轮用
           anchor_window；export_absent 轮不校验行号位置但登记。
  口径覆盖  G1 的分母是 QA 树自有轮数（块坐标，mechanical 轮也计——它们仍是该线自有内容），
           同时并列裁决#3 轮数供口径核对；两者不互换。

只读：不写任何文件，不改 ledger。退出码 0 = 全部通过，1 = 有 FAIL，2 = 输入/用法错误。
"""
import argparse
import json
import os
import random
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SCOPE = os.path.join(ROOT, 'wflow-lineage', 'scope.json')
LINEAGE = os.path.join(ROOT, 'wflow-lineage', 'lineage')  # 默认值，可被 --lineage 覆盖
LEDGER = os.path.join(ROOT, 'wflow-lineage', 'ledger.jsonl')
GUI = os.path.join(ROOT, 'git-worktree对话录')

COLUMNS = ['id', 'line', 'layer', 'round', 'export_line', 'type', 'claim',
           'verdict_token', 'artifact_ref', 'status', 'propagated_to', 'notes']
TYPES = {'判定', '发现', '来源', '控制', '拒绝', '方法', '概念', '治理'}
STATUSES = {'carried', 'parked', 'superseded', 'cold', 'open'}
# 该行没有判词可引时的显式标记（等同 MISSING）：G3 不得把它当成“必须逐字找到的判词”而误报。
NO_TOKEN = {'', 'MISSING', '(none)', '(空)', '无', 'none', 'NONE', '-', '—'}
# 该行不绑定具体轮次时的显式标记：只要 export_line 可定位，R1 即满足。
NO_ROUND = {'', '-', '—', '(none)', 'NONE', '无'}


def fail(msg):
    print('  FAIL  %s' % msg)


def pass_(msg):
    print('  pass  %s' % msg)


def gate(title):
    print('\n== %s ==' % title)


def load_tsv(path):
    rows = []
    with open(path, encoding='utf-8') as fh:
        for lineno, raw in enumerate(fh, 1):
            line = raw.rstrip('\n')
            if not line.strip():
                continue
            rows.append((lineno, line.split('\t')))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--scope', default=SCOPE)
    ap.add_argument('--lineage', default=LINEAGE)
    ap.add_argument('--ledger', default=LEDGER)
    ap.add_argument('--json', action='store_true', help='机读输出：门禁结论与逐线缺口')
    ap.add_argument('--seed', default='gui-lineage-audit-v1')
    ap.add_argument('--sample', type=int, default=30)
    a = ap.parse_args()
    lineage_root = os.path.abspath(a.lineage)

    if not os.path.exists(a.scope):
        print('FATAL: scope.json missing — run tools/build_scope.py first', file=sys.stderr)
        return 2
    scope = json.load(open(a.scope, encoding='utf-8'))
    exports = {}
    for tag, s in scope['lines'].items():
        path = os.path.join(ROOT, s['export']['path'])
        exports[tag] = open(path, encoding='utf-8').read().split('\n') if os.path.exists(path) else None

    results = {}
    line_state = {}
    for tag in ['dev-08', 'dev-03', 'dev-04', 'dev-02', 'dev-01', 'dev-09', 'dev-06', 'dev-07']:
        line_state[tag] = {'thread': False, 'tsv': False, 'covered': [], 'missing': [],
                           'anchor_failures': 0, 'enum_failures': 0, 'column_failures': 0,
                           'g3_full_failures': 0}

    # ---------------- G1 覆盖 ----------------
    gate('G1 覆盖（8 线 THREAD.md/DISCOVERIES.tsv 齐备；自有轮覆盖）')
    g1_fail = 0
    for tag in ['dev-08', 'dev-03', 'dev-04', 'dev-02', 'dev-01', 'dev-09', 'dev-06', 'dev-07']:
        s = scope['lines'][tag]
        thread = os.path.join(lineage_root, tag, 'THREAD.md')
        tsv = os.path.join(lineage_root, tag, 'DISCOVERIES.tsv')
        line_state[tag]['thread'] = os.path.exists(thread)
        line_state[tag]['tsv'] = os.path.exists(tsv)
        if not os.path.exists(thread):
            fail('%s: THREAD.md missing' % tag)
            g1_fail += 1
            continue
        if not os.path.exists(tsv):
            fail('%s: DISCOVERIES.tsv missing' % tag)
            g1_fail += 1
            continue
        own = {d['doc'] for d in s['docs']}
        covered = set()
        for _, cols in load_tsv(tsv):
            if len(cols) > 3 and re.fullmatch(r'\d{4}', cols[3].strip()):
                covered.add(cols[3].strip())
        line_state[tag]['covered'] = sorted(covered & own)
        missing = sorted(own - covered)
        cov = len(covered & own)
        note = 'block 坐标 %d/%d；裁决#3 轮数 %d' % (cov, len(own), s['adjudication_rounds'])
        line_state[tag]['missing'] = missing
        if len(own) == 0:
            fail('%s: scope 无自有轮（输入层异常）' % tag)
            g1_fail += 1
        elif cov < len(own):
            fail('%s: 未覆盖 %d 轮 %s（%s）' % (tag, len(missing), missing[:12], note))
            g1_fail += 1
        else:
            pass_('%s: %s' % (tag, note))
    results['G1'] = g1_fail == 0

    # ---------------- G2 双锚与枚举 ----------------
    gate('G2 双锚（round/export_line 可定位；行号落在该轮区间内；枚举合法）')
    g2_fail = 0
    total_rows = 0
    for tag in ['dev-08', 'dev-03', 'dev-04', 'dev-02', 'dev-01', 'dev-09', 'dev-06', 'dev-07']:
        s = scope['lines'][tag]
        tsv = os.path.join(lineage_root, tag, 'DISCOVERIES.tsv')
        if not os.path.exists(tsv):
            continue
        docs = {d['doc']: d for d in s['docs']}
        total_lines = s['export']['lines']
        bad_anchor, bad_enum, bad_cols = [], [], []
        line_state[tag]['anchor_failures'] = 0
        line_state[tag]['enum_failures'] = 0
        line_state[tag]['column_failures'] = 0
        for lineno, cols in load_tsv(tsv):
            total_rows += 1
            if len(cols) != len(COLUMNS):
                bad_cols.append((lineno, len(cols)))
                line_state[tag]['column_failures'] += 1
                continue
            row = dict(zip(COLUMNS, [c.strip() for c in cols]))
            rnd = row['round']
            eline = row['export_line']
            no_round = rnd in NO_ROUND
            if not rnd and not eline:
                bad_anchor.append((lineno, 'round 与 export_line 均空'))
                continue
            if rnd and not no_round and rnd not in docs:
                bad_anchor.append((lineno, 'round %s 不是 %s 自有轮' % (rnd, tag)))
                continue
            if eline:
                if not re.fullmatch(r'\d+', eline):
                    bad_anchor.append((lineno, 'export_line 非数字: %r' % eline))
                    continue
                n = int(eline)
                if n < 1 or n > total_lines:
                    bad_anchor.append((lineno, 'export_line %d 越界 (1..%d)' % (n, total_lines)))
                    continue
                if rnd and not no_round:
                    d = docs[rnd]
                    if d['anchor_line'] is not None:
                        lo = d['anchor_line']
                        hi = d.get('anchor_block_end') or lo
                        nxt = next((x['anchor_line'] for x in s['docs']
                                    if x['anchor_line'] and x['anchor_line'] > lo), total_lines + 1)
                        hi = max(hi, nxt - 1)
                        if not (lo <= n <= hi):
                            bad_anchor.append((lineno, 'round %s 行号 %d 不在轮区间 %d..%d'
                                               % (rnd, n, lo, hi)))
                    elif d.get('anchor_window'):
                        lo, hi = d['anchor_window']
                        if not (lo <= n <= hi):
                            bad_anchor.append((lineno, 'round %s 行号 %d 不在机械轮窗口 %d..%d'
                                               % (rnd, n, lo, hi)))
                    else:
                        bad_anchor.append((lineno, 'round %s 为 export_absent 轮，行号不可核'
                                           % rnd))
            if row['type'] and row['type'] not in TYPES:
                bad_enum.append((lineno, 'type=%r' % row['type']))
                line_state[tag]['enum_failures'] += 1
            if row['status'] and row['status'] not in STATUSES:
                bad_enum.append((lineno, 'status=%r' % row['status']))
                line_state[tag]['enum_failures'] += 1
        line_state[tag]['anchor_failures'] = len(bad_anchor)
        if bad_cols:
            fail('%s: %d 行列数不等于 %d（%s）' % (tag, len(bad_cols), len(COLUMNS), bad_cols[:3]))
            g2_fail += 1
        if bad_anchor:
            fail('%s: %d 行锚点不合格（%s）' % (tag, len(bad_anchor), bad_anchor[:3]))
            g2_fail += 1
        if bad_enum:
            fail('%s: %d 行枚举非法（%s）' % (tag, len(bad_enum), bad_enum[:3]))
            g2_fail += 1
        if not (bad_cols or bad_anchor or bad_enum):
            pass_('%s: 全部行双锚/枚举合法' % tag)
    results['G2'] = g2_fail == 0

    # ---------------- G3 全量逐字（机验，强于抽样） ----------------
    gate('G3_full 判词逐字全量（每个非 MISSING 判词必须在语料中逐字出现）')
    qa_root = os.path.join(ROOT, 'audit', 'GUI-SYNTH-REDO', 'qa')
    extra_corpora = {}
    for name in ('assets-ledger.md', 'D3-资产登记v2-20261007.md'):
        p = os.path.join(ROOT, 'audit', 'GUI-ASSET-RECOVERY', name)
        extra_corpora[name] = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    qa_cache = {}
    full_bad, full_total, full_missing = [], 0, 0
    g3_by_line = {}
    for tag in ['dev-08', 'dev-03', 'dev-04', 'dev-02', 'dev-01', 'dev-09', 'dev-06', 'dev-07']:
        tsv = os.path.join(lineage_root, tag, 'DISCOVERIES.tsv')
        if not os.path.exists(tsv):
            continue
        for lineno, cols in load_tsv(tsv):
            if len(cols) != len(COLUMNS):
                continue
            row = dict(zip(COLUMNS, [c.strip() for c in cols]))
            tok, rnd = row['verdict_token'], row['round']
            if tok in NO_TOKEN:
                full_missing += 1
                continue
            full_total += 1
            g3_by_line.setdefault(tag, 0)
            text = exports.get(tag)
            if text is not None and any(tok in l for l in text):
                continue
            key = (tag, rnd)
            if key not in qa_cache:
                p = os.path.join(qa_root, tag, '%s.md' % rnd)
                qa_cache[key] = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
            if tok in qa_cache[key]:
                continue
            if any(tok in t for t in extra_corpora.values()):
                continue
            full_bad.append((tag, lineno, rnd, tok))
            g3_by_line[tag] = g3_by_line.get(tag, 0) + 1
            if tag in line_state:
                line_state[tag]['g3_full_failures'] = g3_by_line[tag]
    if full_bad:
        fail('%d/%d 个判词在导出原文、该轮 QA 文档与 D3/资产账本中都找不到逐字匹配（%s）'
             % (len(full_bad), full_total, full_bad[:5]))
        results['G3_full'] = False
    else:
        pass_('%d 个非 MISSING 判词全部逐字命中语料（另有 %d 行标 MISSING，其合理性由 N10 核）'
              % (full_total, full_missing))
        results['G3_full'] = True

    # ---------------- G3 抽样预检（master-side，不替代 N10） ----------------
    gate('G3 判词逐字预检（Master 自查；N10 必须用新鲜种子独立复跑）')
    g3_fail = 0
    rng = random.Random(a.seed)
    pool = []
    for tag in ['dev-08', 'dev-03', 'dev-04', 'dev-02', 'dev-01', 'dev-09', 'dev-06', 'dev-07']:
        tsv = os.path.join(lineage_root, tag, 'DISCOVERIES.tsv')
        if not os.path.exists(tsv):
            continue
        for lineno, cols in load_tsv(tsv):
            if len(cols) != len(COLUMNS):
                continue
            row = dict(zip(COLUMNS, [c.strip() for c in cols]))
            tok = row['verdict_token']
            if tok and tok not in NO_TOKEN:
                pool.append((tag, lineno, tok))
    if not pool:
        pass_('无可抽样的判词行（产物为空或全部 MISSING）')
    else:
        sample = pool if len(pool) <= a.sample else rng.sample(pool, a.sample)
        bad = []
        for tag, lineno, tok in sample:
            text = exports.get(tag)
            if text is None or not any(tok in l for l in text):
                bad.append((tag, lineno, tok))
        if bad:
            fail('%d/%d 个判词在导出原文中找不到逐字匹配（%s）'
                 % (len(bad), len(sample), bad[:3]))
            g3_fail += 1
        else:
            pass_('抽样 %d/%d 个判词逐字命中导出原文（seed=%s）' % (len(sample), len(pool), a.seed))
    results['G3_pre'] = g3_fail == 0

    # ---------------- G4 D3 资产归宿（机验） ----------------
    gate('G4 D3 资产归宿（机验：619 个 A-ID 全部在 CROSS-FEED.md 出现）')
    d3 = os.path.join(ROOT, 'audit', 'GUI-ASSET-RECOVERY', 'D3-资产登记v2-20261007.md')
    cross = os.path.join(lineage_root, 'CROSS-FEED.md')
    if not os.path.exists(cross):
        fail('CROSS-FEED.md 尚未生成（N9 之后才可验）')
        results['G4_mech'] = False
    elif not os.path.exists(d3):
        fail('D3 登记文件缺失：%s' % d3)
        results['G4_mech'] = False
    else:
        ids = sorted(set(re.findall(r'A-0\d{3}', open(d3, encoding='utf-8').read())))
        text = open(cross, encoding='utf-8').read()
        missing = [i for i in ids if i not in text]
        if missing:
            fail('D3 %d 条资产中 %d 条未在 CROSS-FEED.md 出现（%s）'
                 % (len(ids), len(missing), missing[:10]))
            results['G4_mech'] = False
        else:
            pass_('D3 %d 条资产全部出现（语义归宿＋理由由 N10 逐条核）' % len(ids))
            results['G4_mech'] = True

    # ---------------- G5 carried 落点 git 可解析（机验） ----------------
    gate('G5 carried 落点可解析（机验：artifact_ref 的 path 在工作树或所引 ref 可解析）')
    carried, unresolved = [], []
    for tag in ['dev-08', 'dev-03', 'dev-04', 'dev-02', 'dev-01', 'dev-09', 'dev-06', 'dev-07']:
        tsv = os.path.join(lineage_root, tag, 'DISCOVERIES.tsv')
        if not os.path.exists(tsv):
            continue
        for lineno, cols in load_tsv(tsv):
            if len(cols) != len(COLUMNS):
                continue
            row = dict(zip(COLUMNS, [c.strip() for c in cols]))
            if row['status'] != 'carried' or not row['artifact_ref']:
                continue
            m = re.match(r'^(.+?)@(.+)$', row['artifact_ref'])
            if not m:
                continue
            path, ref = m.group(1), m.group(2)
            carried.append((tag, lineno, path, ref))
            if os.path.exists(os.path.join(ROOT, path)):
                continue
            try:
                r = subprocess.run(['git', 'cat-file', '-e', '%s:%s' % (ref, path)],
                                   cwd=ROOT, capture_output=True, timeout=30)
                if r.returncode != 0:
                    unresolved.append((tag, lineno, '%s@%s' % (path, ref)))
            except Exception:
                unresolved.append((tag, lineno, '%s@%s（git 查询失败）' % (path, ref)))
    if not carried:
        pass_('无 carried 行可验（产物为空或全部未标 carried）')
        results['G5_mech'] = True
    elif unresolved:
        fail('%d/%d 个 carried 落点不可解析（%s）——按 §5 G5 应降级 parked 并登记'
             % (len(unresolved), len(carried), unresolved[:5]))
        results['G5_mech'] = False
    else:
        pass_('%d 个 carried 落点全部可解析（落点是否真承载该判词由 N10 核）' % len(carried))
        results['G5_mech'] = True

    # ---------------- G6 链接 ----------------
    gate('G6 KB-INDEX 相对链接解析')
    kb = os.path.join(lineage_root, 'KB-INDEX.md')
    if not os.path.exists(kb):
        pass_('KB-INDEX.md 尚未生成（N9 之后才可验）')
        results['G6'] = True
    else:
        bad = []
        links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', open(kb, encoding='utf-8').read())
        for link in links:
            if re.match(r'^[a-z]+:', link) or link.startswith('#'):
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(kb), link.split('#')[0]))
            if not os.path.exists(target):
                bad.append(link)
        if bad:
            fail('%d 个相对链接解析失败（%s）' % (len(bad), bad[:5]))
            results['G6'] = False
        else:
            pass_('全部 %d 个相对链接解析成功' % len(links))
            results['G6'] = True

    # ---------------- G8 ledger ----------------
    gate('G8 ledger 无未结 OPEN 的 CONFLICT/UNKNOWN')
    ledger_path = os.path.abspath(a.ledger)
    if not os.path.exists(ledger_path):
        pass_('ledger.jsonl 不存在')
        results['G8'] = True
    else:
        data = json.load(open(ledger_path, encoding='utf-8'))
        entries = data.get('entries', [])
        # append-only 纪律：一条 OPEN 登记若被后续 CLOSED 条目以 supersedes 指名取代，即视为已结。
        superseded = set()
        for e in entries:
            if e.get('state') == 'CLOSED' and e.get('supersedes'):
                superseded.add(e['supersedes'].replace(' UNKNOWN', '').replace(' CONFLICT', '').strip())
        open_items = [e for e in entries
                      if e.get('state') == 'OPEN' and e.get('kind') in ('CONFLICT', 'UNKNOWN')
                      and e.get('node') not in superseded]
        if open_items:
            fail('%d 条未结 CONFLICT/UNKNOWN（%s）' % (len(open_items), open_items[:2]))
            results['G8'] = False
        else:
            live_open = [e for e in entries
                         if e.get('state') == 'OPEN' and e.get('node') not in superseded]
            sup = len(superseded)
            pass_('ledger %d 条记录，无未结 CONFLICT/UNKNOWN%s%s'
                  % (len(entries),
                     '（%d 条 OPEN 登记已被 supersedes 裁定收口）' % sup if sup else '',
                     '（另有 %d 条非 CONFLICT/UNKNOWN 的 OPEN 登记）' % len(live_open)
                     if live_open else ''))
            results['G8'] = True

    # ---------------- 汇总 ----------------
    print('\n== 汇总 ==')
    for k, v in results.items():
        print('%-8s %s' % (k, 'PASS' if v else 'FAIL'))
    hard = [k for k, v in results.items() if not v and k != 'G3_pre']
    code = 1 if hard else 0
    if a.json:
        gaps = [{'line': t, 'missing_rounds': st['missing'],
                 'anchor_failures': st['anchor_failures'], 'enum_failures': st['enum_failures'],
                 'column_failures': st['column_failures'], 'g3_full_failures': st['g3_full_failures'],
                 'thread_missing': not st['thread'], 'tsv_missing': not st['tsv'],
                 'covered': len(st['covered']), 'own_rounds': scope['lines'][t]['own_docs']}
                for t, st in line_state.items()
                if st['missing'] or st['anchor_failures'] or st['enum_failures']
                or st['column_failures'] or st['g3_full_failures']
                or not st['thread'] or not st['tsv']]
        print(json.dumps({'exit_code': code,
                          'gates': {k: v for k, v in results.items()},
                          'gaps': gaps,
                          'total_rows': total_rows}, ensure_ascii=False))
    return code


if __name__ == '__main__':
    sys.exit(main())
