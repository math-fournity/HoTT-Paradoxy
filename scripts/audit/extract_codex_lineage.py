#!/usr/bin/env python3
"""补齐本地GPT会话谱系的用户消息提取（父线程01a059c1 + 并行会话）。

修复的机器注入通道（不算用户手打）：
  - '<tag>' / '<tag attrs…>'（environment_context、codex_internal_context、recommended_plugins 等）
  - '# AGENTS.md instructions for'（工作区指令注入）
保留的用户侧载荷：
  - '# Files pasted by the user:'（用户粘贴的文件正文）
  - '# Response annotations:'（带引用批注的用户 turn）
用法：python3 -B extract_codex_lineage.py [--dir 目录]
"""
from pathlib import Path
import argparse, datetime, hashlib, json, re

DIR = Path(__file__).resolve().parent
SESS = '/Users/aurolafly/.codex/sessions'
FILES = [
    ('HoTT父线程🌟(01a059c1, 08-31→09-09)', SESS + '/2026/08/31/rollout-2026-08-31T17-37-21-01a059c1-6322-7f90-a2f9-427cae4b590d.jsonl'),
    ('HoTT-2根文件(01a08699 fork基干)', SESS + '/2026/09/09/rollout-2026-09-09T10-37-05-01a08699-dbe0-7ad2-b1d1-c4fd36321a35.jsonl'),
    ('素数线(01a059dd)', SESS + '/2026/08/31/rollout-2026-08-31T18-07-48-01a059dd-458c-74f0-b167-8a2ff16307d7.jsonl'),
    ('素数线worktree(01a05a10)', SESS + '/2026/08/31/rollout-2026-08-31T19-03-46-01a05a10-8378-7cc0-a323-6339e03aa3bd.jsonl'),
    ('归档(01a05ec3)', '/Users/aurolafly/.codex/archived_sessions/rollout-2026-09-01T16-58-11-01a05ec3-e3d8-7423-9bf8-d13af1397555.jsonl'),
]
OUT_PARENT = 'Codex-HoTT父线程-01a059c1-用户消息提取-20260911.md'
OUT_PARALLEL = 'Codex-并行会话-素数与归档-用户消息提取-20260911.md'

TAG = re.compile(r'^\s*<[a-zA-Z_][a-zA-Z0-9_-]*(\s|>)')
MACHINE_PREFIXES = ('# AGENTS.md instructions for', 'Caveat:')


def sha_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1048576), b''):
            h.update(b)
    return h.hexdigest()


def is_machine(text):
    return (not text.strip()) or text.startswith(MACHINE_PREFIXES) or bool(TAG.match(text))


def extract(path):
    msgs, skipped = [], 0
    with open(path, encoding='utf-8', errors='replace') as f:
        for lineno, line in enumerate(f, 1):
            try:
                o = json.loads(line)
            except json.JSONDecodeError:
                continue
            if o.get('type') != 'response_item':
                continue
            p = o.get('payload', {})
            if p.get('type') != 'message' or p.get('role') != 'user':
                continue
            text = ''.join(c.get('text', '') for c in p.get('content', []) if isinstance(c, dict))
            if is_machine(text):
                skipped += 1
                continue
            msgs.append((lineno, o.get('timestamp', ''), text.rstrip('\n')))
    return msgs, skipped


def render(title, groups, out_path, now):
    out = [f'# {title}\n', '\n',
           '- 提取规则：rollout JSONL 的 response_item/message/role=user；剔除机器注入（<tag…> 包装、'
           '# AGENTS.md instructions 工作区指令、Caveat 本地命令输出）；保留用户粘贴文件与引用批注 turn。\n',
           f'- 提取工具：`extract_codex_lineage.py`；时间：{now}\n', '\n']
    total = 0
    for label, path, msgs, skipped in groups:
        out.append(f'## 会话：{label}\n')
        out.append(f'- 文件：`{path}`（{Path(path).stat().st_size:,} 字节，SHA-256 `{sha_file(Path(path))}`）\n')
        out.append(f'- 用户消息 {len(msgs)} 条；机器注入剔除 {skipped} 条\n')
        if not msgs:
            out.append('\n（无用户消息）\n')
        for i, (lineno, ts, text) in enumerate(msgs, 1):
            out.append('\n')
            out.append(f'### [{i}] {ts}（源文件第 {lineno} 行）\n\n')
            body = text if text.endswith('\n') else text + '\n'
            out.append(body)
            out.append('\n---\n')
        total += len(msgs)
    out.append(f'\n合计用户消息：{total} 条\n')
    out_path.write_text(''.join(out), encoding='utf-8')
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', type=Path, default=DIR)
    a = ap.parse_args()
    d = a.dir.resolve()
    now = datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %z')
    parent_groups, parallel_groups = [], []
    for label, path in FILES:
        msgs, skipped = extract(path)
        g = (label, path, msgs, skipped)
        if '01a059c1' in path:
            parent_groups.append(g)
        else:
            parallel_groups.append(g)
        print(f'{label}: 用户消息 {len(msgs)}，机器注入 {skipped}')
    t1 = render('Codex 本地GPT · HoTT 父线程（🌟 HoTT / 01a059c1）用户消息提取', parent_groups, d / OUT_PARENT, now)
    t2 = render('Codex 本地GPT · 并行会话（素数研究线 + 归档）用户消息提取', parallel_groups, d / OUT_PARALLEL, now)
    print(json.dumps({'parent_file': OUT_PARENT, 'parent_messages': t1,
                      'parallel_file': OUT_PARALLEL, 'parallel_messages': t2}, ensure_ascii=False))


if __name__ == '__main__':
    main()
