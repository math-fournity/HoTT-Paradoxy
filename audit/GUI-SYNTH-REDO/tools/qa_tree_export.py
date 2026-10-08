#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUI 结构化问答树导出（v3）。

以 Codex rollout 为源，复用 GUI 导出器的谱系（build_lineage）、切点（双条件 cutoff）与可见事件
（collect_events）逻辑，只读调用，不修改导出器或任何 ~/.codex 文件。

输出（默认 audit/GUI-SYNTH-REDO/qa/）：
  <branch>/NNNN.md        一轮问答：`## User` + 其后的 `## Codex` 与改动胶囊（与 GUI 渲染口径一致）
  <branch>/_index.jsonl   每轮的源定位：rollout、行号、字节区间、源字节 SHA-256
  <branch>/_branch.json   分支元数据：线程、自有文档数、父分支与分叉节点（fork）
  _tree.json              分支树、分叉节点、不可见尾部（未被任何导出引用的轮次）
  _manifest.json          规范导出器哈希、各导出的谱系与切点、计数

分支与自有：每轮归属于它所在的 rollout 所属线程（owner thread）。子分支只继承父段的前缀，
前缀轮次只存在于拥有它的分支文件夹中；分叉节点 = 子分支第一条自有轮之前的那一轮。
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
import pathlib
import shutil
import sys

REPO = pathlib.Path(__file__).resolve().parents[3]
DEFAULT_OUT = REPO / 'audit' / 'GUI-SYNTH-REDO' / 'qa'
DEFAULT_CANON = pathlib.Path(
    '/Users/aurolafly/codex-worktrees/pdag-isolated-runner-route/tools/trajectory_gui_ref_export.py')
# (分支标签, GUI 标题)。标题与语料 README 的“GUI 标题（必须精确匹配）”表一致。
EXPORTS = [
    ('dev-08', '🌟 08 - 哥德尔'),
    ('dev-01', '🌟 01 - ZFC-1'),
    ('dev-02', '02 - ZFC-1'),
    ('dev-03', '03 - ZFC-1'),
    ('dev-04', '04 - ZFC-1'),
    ('dev-06', '🌟 06 - ZFC-1'),
    ('dev-07', '🌟 07 - ZFC-2 ω 的完成性'),
    ('dev-09', '🌟 09 - 哥德尔'),
]
GENERATOR = 'qa_tree_export/v1'


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def sha256_file(path):
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def load_canon(path):
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('gui_export_canon', str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules['gui_export_canon'] = mod
    spec.loader.exec_module(mod)
    return mod


def die(msg, code=1):
    print(msg, file=sys.stderr)
    sys.exit(code)


def build_docs(mod, events):
    """把一个导出的可见事件序列切成轮：每个 user_message 开一轮；无用户轮前的助手消息单独成轮。"""
    docs, cur = [], None
    for ev, seg, recs, _cut in events:
        if ev.kind == 'user_message':
            line = mod.source_line_from_locator(str(ev.locator), seg.path)
            if line is None:
                die(f'USER_LINE_UNRESOLVED:{seg.path}')
            cur = {'user': ev, 'seg': seg, 'recs': recs, 'line': line, 'items': []}
            docs.append(cur)
        elif ev.kind in ('assistant_message', 'file_change'):
            if cur is None:
                cur = {'user': None, 'seg': seg, 'recs': recs, 'line': None, 'items': []}
                docs.append(cur)
            cur['items'].append((ev, seg, recs))
    for d in docs:
        if d['line'] is None:
            first = d['items'][0] if d['items'] else None
            d['line'] = mod.source_line_from_locator(str(first[0].locator), first[1].path) if first else 0
        d['key'] = f"{d['seg'].path}#{d['line']}"
    return docs


def doc_records(mod, doc):
    """返回本轮涉及的源记录（轮次用户消息与所有可见条目的记录），用于字节区间与哈希。"""
    rows = []
    items = ([(doc['user'], doc['seg'], doc['recs'])] if doc['user'] is not None else []) + \
            [(ev, seg, recs) for ev, seg, recs in doc['items']]
    for ev, seg, recs in items:
        ln = mod.source_line_from_locator(str(ev.locator), seg.path)
        rec = recs.get(ln) if ln is not None else None
        if rec is None:
            die(f'SOURCE_RECORD_MISSING:{seg.path}:{ln}')
        rows.append((ln, rec))
    return rows


def check_consistent(a, b):
    """同一轮在不同导出中出现时，可见条目必须一致（较短者是较长者的前缀）。"""
    ka = [(ev.kind, str(ev.locator)) for ev, _s, _r in a['items']]
    kb = [(ev.kind, str(ev.locator)) for ev, _s, _r in b['items']]
    n = min(len(ka), len(kb))
    return ka[:n] == kb[:n]


def render_doc(mod, label, number, doc, span, capsules):
    head = ['---',
            f'branch: {label}',
            f'doc: {number:04d}',
            f"owner_thread: {doc['seg'].thread_id}",
            f"owner_rollout: {doc['seg'].rollout_id}",
            f"source_lines: {span['line_from']}-{span['line_to']}",
            f"source_bytes: {span['byte_from']}-{span['byte_to']}",
            f"source_sha256: {span['sha256']}",
            '---']
    parts = ['\n'.join(head)]
    if doc['user'] is not None:
        parts.append('## User\n\n' + (doc['user'].text or ''))
    turn_ids = []
    for ev, seg, _recs in doc['items']:
        if ev.kind == 'assistant_message':
            parts.append('## Codex\n\n' + (ev.text or ''))
            if ev.turn_id and ev.turn_id not in turn_ids:
                turn_ids.append(ev.turn_id)
    for tid in turn_ids:
        changes = capsules.get((doc['seg'].path, tid))
        if changes:
            parts.append(mod.render_gui_file_change_capsule(changes))
    return '\n\n'.join(parts) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description='GUI 结构化问答树导出（v3）')
    ap.add_argument('--out', default=str(DEFAULT_OUT))
    ap.add_argument('--canonical', default=str(DEFAULT_CANON))
    ap.add_argument('--force', action='store_true', help='覆盖已有输出目录（只删除本脚本生成的目录）')
    a = ap.parse_args(argv)
    out = pathlib.Path(a.out)
    canon_path = pathlib.Path(a.canonical)
    if not canon_path.is_file():
        die(f'CANONICAL_EXPORTER_MISSING:{canon_path}')
    if out.exists() and any(out.iterdir()):
        if not a.force:
            die(f'输出目录非空：{out}（加 --force 覆盖）')
        shutil.rmtree(out)
    mod = load_canon(canon_path)
    latest = mod.load_session_index(mod.DEFAULT_SESSION_INDEX) if mod.DEFAULT_SESSION_INDEX.is_file() else {}
    inv = mod.scan_rollout_segments(mod.DEFAULT_SESSIONS_ROOT, mod.DEFAULT_ARCHIVED_SESSIONS_ROOT)
    reader = mod.load_shared_trajectory_reader()

    # 1. 每个导出：谱系、可见事件、轮次序列
    exports, warnings = {}, []
    for tag, title in EXPORTS:
        te = mod.resolve_gui_title(title, latest, mod.DEFAULT_STATE_DB, mod.DEFAULT_SESSION_INDEX.resolve())
        sel, sw = mod.select_current_rollout(te, inv)
        if sel is None:
            die(f'TARGET_NOT_FOUND:{tag}')
        lin, lw = mod.build_lineage(sel, inv)
        events, ew = mod.collect_events(lin, reader)
        capsules = mod.gui_file_changes_by_turn(events)
        docs = build_docs(mod, events)
        exports[tag] = {'thread': te.thread_id, 'selected': sel, 'lineage': lin, 'events': events,
                        'capsules': capsules, 'docs': docs, 'warnings': list(sw) + list(lw) + list(ew)}
        if exports[tag]['warnings']:
            warnings.extend(f'{tag}:{w}' for w in exports[tag]['warnings'])

    # 2. 全局轮表：同一源轮只保留一份（取可见条目最多的那次出现），并检查前缀一致
    registry, order_in = {}, {}
    for tag, ex in exports.items():
        order_in[tag] = []
        for d in ex['docs']:
            if d['key'] not in registry:
                registry[d['key']] = d
            else:
                cur = registry[d['key']]
                if len(d['items']) > len(cur['items']):
                    if not check_consistent(cur, d):
                        die(f"DOC_CONFLICT:{d['key']}")
                    registry[d['key']] = d
                elif not check_consistent(d, cur):
                    die(f"DOC_CONFLICT:{d['key']}")
            order_in[tag].append(d['key'])

    # 3. 线程 -> 分支标签；归档根（不直接导出）由 dev-08 谱系派生
    thread_label = {ex['thread']: tag for tag, ex in exports.items()}
    dev08 = exports['dev-08']
    seen_dev08 = False
    for sl in dev08['lineage']:
        if sl.thread_id == exports['dev-08']['thread']:
            seen_dev08 = True
            continue
        if not seen_dev08 and sl.thread_id not in thread_label:
            thread_label[sl.thread_id] = f"archive-{sl.thread_id[:8]}"
    own_export = {}
    for tag in exports:
        own_export[tag] = tag
    for lbl in set(thread_label.values()):
        if lbl.startswith('archive-'):
            own_export[lbl] = 'dev-08'

    # 4. 每个轮的归属分支；自有轮按其自有导出中的位置排序
    owner_label = {}
    for key, d in registry.items():
        tid = d['seg'].thread_id
        if tid not in thread_label:
            die(f'UNMAPPED_THREAD:{tid}')
        owner_label[key] = thread_label[tid]
    pos = {tag: {k: i for i, k in enumerate(dict.fromkeys(keys))} for tag, keys in order_in.items()}
    own_keys = {}
    for key, lbl in owner_label.items():
        own_keys.setdefault(lbl, []).append(key)
    labels = sorted(own_keys, key=lambda l: (not l.startswith('archive-'), l))
    tree = {'labels': {}, 'parents': {}, 'forks': {}}
    numbering = {}
    for lbl in labels:
        ex_tag = own_export[lbl]
        if key_missing := [k for k in own_keys[lbl] if k not in pos[ex_tag]]:
            die(f'OWN_DOC_NOT_IN_OWN_EXPORT:{lbl}:{key_missing[0]}')
        ordered = sorted(own_keys[lbl], key=lambda k: pos[ex_tag][k])
        idx = [pos[ex_tag][k] for k in ordered]
        contiguous = idx == list(range(idx[0], idx[0] + len(idx))) if idx else True
        numbering[lbl] = {k: i + 1 for i, k in enumerate(ordered)}
        tree['labels'][lbl] = {'own_export': ex_tag, 'own_docs': len(ordered), 'contiguous': contiguous,
                               'thread_id': next((t for t, l in thread_label.items() if l == lbl), None),
                               'keys': ordered}

    # 5. 分叉节点：自有段第一轮之前的那一轮（必须属于其他分支）
    for lbl in labels:
        info = tree['labels'][lbl]
        ex_tag = info['own_export']
        first_pos = pos[ex_tag][info['keys'][0]]
        if first_pos == 0:
            tree['parents'][lbl] = None
            continue
        fork_key = order_in[ex_tag][first_pos - 1]
        parent = owner_label[fork_key]
        if parent == lbl:
            die(f'FORK_NODE_OWNED_BY_SELF:{lbl}')
        seg_path = registry[fork_key]['seg'].path
        cutoff = None
        for sl in exports[ex_tag]['lineage']:
            if sl.segments and sl.segments[0].path == seg_path and sl.cutoff is not None:
                cutoff = {'end_byte_offset': sl.cutoff.end_byte_offset,
                          'end_ordinal_exclusive': sl.cutoff.end_ordinal_exclusive}
        tree['parents'][lbl] = parent
        tree['forks'][lbl] = {'parent_branch': parent, 'parent_doc': numbering[parent][fork_key],
                              'parent_rollout': registry[fork_key]['seg'].rollout_id,
                              'cutoff': cutoff}

    # 6. 写出
    out.mkdir(parents=True, exist_ok=True)
    file_cache = {}
    def raw_bytes(path):
        k = str(path)
        if k not in file_cache:
            file_cache[k] = path.read_bytes()
        return file_cache[k]
    total_docs = 0
    for lbl in labels:
        info = tree['labels'][lbl]
        ex_tag = info['own_export']
        folder = out / lbl
        folder.mkdir(parents=True, exist_ok=True)
        index_lines = []
        for key in info['keys']:
            d = registry[key]
            n = numbering[lbl][key]
            rows = doc_records(mod, d)
            byte_from = min(r.byte_start for _l, r in rows)
            byte_to = max(r.byte_end for _l, r in rows)
            line_from = min(l for l, _r in rows)
            line_to = max(l for l, _r in rows)
            digest = hashlib.sha256(raw_bytes(d['seg'].path)[byte_from:byte_to]).hexdigest()
            span = {'line_from': line_from, 'line_to': line_to, 'byte_from': byte_from,
                    'byte_to': byte_to, 'sha256': digest}
            text = render_doc(mod, lbl, n, d, span, exports[ex_tag]['capsules'])
            (folder / f'{n:04d}.md').write_text(text, encoding='utf-8')
            index_lines.append({'doc': f'{n:04d}', 'owner_rollout': d['seg'].rollout_id,
                                'owner_thread': d['seg'].thread_id, 'source_file': d['seg'].path.name,
                                'line_from': line_from, 'line_to': line_to, 'byte_from': byte_from,
                                'byte_to': byte_to, 'sha256': digest,
                                'user_turn': d['user'] is not None, 'items': len(d['items'])})
            total_docs += 1
        with (folder / '_index.jsonl').open('w', encoding='utf-8') as fh:
            for row in index_lines:
                fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + '\n')
        branch = {'branch': lbl, 'thread_id': info['thread_id'], 'own_export': ex_tag,
                  'own_docs': info['own_docs'], 'contiguous_in_own_export': info['contiguous'],
                  'parent': tree['parents'].get(lbl), 'fork': tree['forks'].get(lbl)}
        (folder / '_branch.json').write_text(json.dumps(branch, ensure_ascii=False, indent=1, sort_keys=True) + '\n',
                                             encoding='utf-8')

    # 7. 不可见尾部：某段文件中未被任何导出引用的用户轮（不据内容判断，只计数与时间范围）
    visible_by_path = {}
    for key, d in registry.items():
        visible_by_path[str(d['seg'].path)] = visible_by_path.get(str(d['seg'].path), 0) + 1
    segs = {}
    for tag, ex in exports.items():
        for sl in ex['lineage']:
            for sg in sl.segments:
                segs[str(sg.path)] = sg
    tails = []
    for path_s, sg in sorted(segs.items()):
        file_users = [ev for ev in reader.iter_codex_events(sg.path) if ev.kind == 'user_message']
        visible = visible_by_path.get(path_s, 0)
        if len(file_users) > visible:
            ts = sorted(str(getattr(ev, 'timestamp', '') or '') for ev in file_users)
            recs_map = mod.source_records_by_line(sg)
            all_events = [(ev, sg, recs_map, None) for ev in reader.iter_codex_events(sg.path)]
            tail_docs = [d for d in build_docs(mod, all_events) if d['key'] not in registry]
            tail_caps = mod.gui_file_changes_by_turn(all_events)
            folder = out / '_unexported' / sg.rollout_id
            folder.mkdir(parents=True, exist_ok=True)
            rows = []
            for n, d in enumerate(tail_docs, start=1):
                rr = doc_records(mod, d)
                bf = min(r.byte_start for _l, r in rr)
                bt = max(r.byte_end for _l, r in rr)
                lf = min(l for l, _r in rr)
                lt = max(l for l, _r in rr)
                dg = hashlib.sha256(raw_bytes(sg.path)[bf:bt]).hexdigest()
                span = {'line_from': lf, 'line_to': lt, 'byte_from': bf, 'byte_to': bt, 'sha256': dg}
                (folder / f'{n:04d}.md').write_text(
                    render_doc(mod, '_unexported/' + sg.rollout_id, n, d, span, tail_caps), encoding='utf-8')
                rows.append({'doc': f'{n:04d}', 'owner_rollout': sg.rollout_id, 'owner_thread': sg.thread_id,
                             'source_file': sg.path.name, 'line_from': lf, 'line_to': lt,
                             'byte_from': bf, 'byte_to': bt, 'sha256': dg,
                             'user_turn': d['user'] is not None, 'items': len(d['items'])})
            with (folder / '_index.jsonl').open('w', encoding='utf-8') as fh:
                for row in rows:
                    fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + '\n')
            tails.append({'rollout_id': sg.rollout_id, 'thread_id': sg.thread_id,
                          'source_file': sg.path.name, 'user_turns_in_file': len(file_users),
                          'user_turns_visible': visible,
                          'user_turns_not_visible': len(file_users) - visible,
                          'exported_turns': len(tail_docs), 'folder': f'_unexported/{sg.rollout_id}',
                          'first_timestamp': ts[0] if ts else None, 'last_timestamp': ts[-1] if ts else None})
    tree_out = {'generated_utc': utc_now(), 'labels': {l: {k: v for k, v in tree['labels'][l].items() if k != 'keys'}
                                                       for l in labels},
                'parents': tree['parents'], 'forks': tree['forks'], 'invisible_tails': tails,
                'warnings': warnings}
    (out / '_tree.json').write_text(json.dumps(tree_out, ensure_ascii=False, indent=1, sort_keys=True) + '\n',
                                    encoding='utf-8')

    # 8. 清单：规范导出器哈希、各导出谱系与切点、源文件哈希
    manifest = {'generator': GENERATOR, 'generated_utc': utc_now(),
                'canonical': {'path': str(canon_path), 'sha256': sha256_file(canon_path)},
                'exports': {}, 'totals': {'branches': len(labels), 'own_docs': total_docs,
                                          'unique_visible_turns': len(registry)},
                'raw_rollouts': []}
    for tag, ex in exports.items():
        manifest['exports'][tag] = {
            'thread_id': ex['thread'], 'selected_rollout': ex['selected'].rollout_id,
            'lineage': [{'thread_id': sl.thread_id, 'rollout_id': sl.segments[0].rollout_id,
                         'cutoff': ({'end_byte_offset': sl.cutoff.end_byte_offset,
                                     'end_ordinal_exclusive': sl.cutoff.end_ordinal_exclusive}
                                    if sl.cutoff else None)} for sl in ex['lineage']],
            'warnings': ex['warnings']}
    for path_s, sg in sorted(segs.items()):
        manifest['raw_rollouts'].append({'rollout_id': sg.rollout_id, 'source_file': sg.path.name,
                                         'bytes': sg.path.stat().st_size, 'sha256': sg.sha256 or sha256_file(sg.path)})
    (out / '_manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=1, sort_keys=True) + '\n',
                                        encoding='utf-8')
    print(f'分支 {len(labels)} 个；自有轮 {total_docs} 个（唯一可见轮 {len(registry)}）；'
          f'不可见尾部段 {len(tails)} 个；警告 {len(warnings)} 条。输出：{out}')
    return 0 if not warnings else 0


if __name__ == '__main__':
    sys.exit(main())
