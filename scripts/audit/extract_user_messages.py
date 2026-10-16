#!/usr/bin/env python3
"""从三种 AI 对话录中提取全部用户发出的消息，各自输出独立 Markdown。

支持的输入格式：
  1. Codex Desktop rollout JSONL（response_item/message/role=user；剔除环境/指令包装与本地命令注入）
  2. ChatGPT 导出 Markdown（## Prompt: / ## Response: 分节，Prompt 节首行是时间戳）
  3. Gemini 对话 JSON（chunkedPrompt.chunks[]，role=user；driveDocument 附件以占位条目保留）

只读输入；输出 UTF-8 Markdown。逐字保留正文，不改写、不摘要。
用法：python3 extract_user_messages.py [--dir 目录]（默认脚本所在目录）
"""
from pathlib import Path
import argparse, hashlib, json, re

DIR = Path(__file__).resolve().parent

CODEX_FILE = 'rollout-2026-09-09T10-43-44-01a08699-dbe0-7ad2-b1d1-c4fd36321a35_01a0869f-f467-7bc2-81d4-abf91cf20739.jsonl'
CHATGPT_FILE = 'ChatGPT-HoTT - Main-20260911-1222.md'
GEMINI_FILE = 'Gemini - AI 对话录.json'

CODEX_OUT = 'Codex-HoTT-2-用户消息提取-20260911.md'
CHATGPT_OUT = 'ChatGPT-HoTT-Main-用户消息提取-20260911.md'
GEMINI_OUT = 'Gemini-AI对话录-用户消息提取-20260911.md'

# Codex rollout 中 role=user 但并非用户手打的包装/注入：<environment_context>/<user_instructions>/
# <turn_aborted>/<recommended_plugins>/<permissions>/… 统一按"首个 token 是机器标签"识别；另有本地命令注入前缀
MACHINE_TAG_RE = re.compile(r'^\s*<[a-zA-Z_][a-zA-Z0-9_-]*>')
WRAPPER_PREFIXES = ('Caveat:',)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1048576), b''):
            h.update(b)
    return h.hexdigest()


def header(title, source_path, extra):
    size = source_path.stat().st_size
    lines = [
        f'# {title}\n',
        '\n',
        f'- 来源文件：`{source_path.name}`（{size:,} 字节，SHA-256 `{sha256_file(source_path)}`）\n',
        f'- 提取规则：只含用户发出的消息，逐字保留；{extra["rule"]}\n',
        f'- 提取结果：{extra["kept"]} 条用户消息' + (f'；另有 {extra["skipped"]} 条系统包装/注入条目未收录' if extra.get('skipped') else '') + '\n',
        f'- 提取工具：`extract_user_messages.py`（本目录，可复跑核验）；时间：{extra["now"]}\n',
        '\n',
        '---\n',
        '\n',
    ]
    return lines


def emit_message(out, idx, meta, text):
    out.append(f'## [{idx}] {meta}\n')
    out.append('\n')
    body = text if text.endswith('\n') else text + '\n'
    out.append(body)
    out.append('---\n')
    out.append('\n')


def extract_codex(path, out_path, now):
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
            if not text.strip() or text.startswith(WRAPPER_PREFIXES) or MACHINE_TAG_RE.match(text):
                skipped += 1
                continue
            msgs.append((lineno, o.get('timestamp', ''), text.rstrip('\n')))
    out = header('Codex HoTT-2 对话 · 用户消息提取', path,
                 {'rule': 'rollout JSONL 中 response_item/message/role=user；剔除机器标签包装（<environment_context>/<user_instructions>/<recommended_plugins> 等，按 ^<tag> 识别）与 Caveat 本地命令注入',
                  'kept': len(msgs), 'skipped': skipped, 'now': now})
    for i, (lineno, ts, text) in enumerate(msgs, 1):
        emit_message(out, i, f'{ts}（源文件第 {lineno} 行）', text)
    out_path.write_text(''.join(out), encoding='utf-8')
    return len(msgs), skipped


PROMPT_RE = re.compile(r'^## Prompt:\s*$')
RESPONSE_RE = re.compile(r'^## Response:\s*$')
STAMP_RE = re.compile(r'^\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2}:\d{2} [AP]M\s*$')


def extract_chatgpt(path, out_path, now):
    lines = path.read_text(encoding='utf-8', errors='replace').splitlines()
    msgs = []
    i = 0
    while i < len(lines):
        if PROMPT_RE.match(lines[i]):
            j = i + 1
            stamp = ''
            if j < len(lines) and STAMP_RE.match(lines[j].strip()):
                stamp = lines[j].strip()
                j += 1
            while j < len(lines) and lines[j] == '':
                j += 1
            body_start = j
            while j < len(lines) and not (PROMPT_RE.match(lines[j]) or RESPONSE_RE.match(lines[j])):
                j += 1
            body_end = j
            while body_end > body_start and lines[body_end - 1] == '':
                body_end -= 1
            msgs.append((stamp, '\n'.join(lines[body_start:body_end])))
            i = j
        else:
            i += 1
    out = header('ChatGPT HoTT - Main 对话 · 用户消息提取', path,
                 {'rule': 'ChatGPT 导出 Markdown 的 ## Prompt: 分节（首行时间戳单独剥离）；## Response: 分节不收录',
                  'kept': len(msgs), 'now': now})
    for i, (stamp, text) in enumerate(msgs, 1):
        emit_message(out, i, stamp, text)
    out_path.write_text(''.join(out), encoding='utf-8')
    return len(msgs), 0


def extract_gemini(path, out_path, now):
    data = json.loads(path.read_text(encoding='utf-8'))
    chunks = data.get('chunkedPrompt', {}).get('chunks', [])
    msgs = []
    for c in chunks:
        if c.get('role') != 'user':
            continue
        if 'text' in c and str(c.get('text', '')).strip():
            msgs.append((c.get('createTime', ''), f'text · {c.get("tokenCount", "?")} tokens', str(c['text']).rstrip('\n')))
        elif 'driveDocument' in c:
            doc = c['driveDocument']
            gid = doc.get('id', '?') if isinstance(doc, dict) else str(doc)
            msgs.append((c.get('createTime', ''), f'driveDocument 附件 · id={gid} · {c.get("tokenCount", "?")} tokens（无正文文本，占位保留）',
                         '（该条目为用户附带的 Drive 文档引用，导出 JSON 中不含正文文本。）'))
    out = header('Gemini AI 对话录 · 用户消息提取', path,
                 {'rule': 'chunkedPrompt.chunks[] 中 role=user 的条目；文本逐字保留，driveDocument 附件以占位条目保留；role=model 不收录',
                  'kept': len(msgs), 'now': now})
    for i, (ts, kind, text) in enumerate(msgs, 1):
        emit_message(out, i, f'{ts} · {kind}', text)
    out_path.write_text(''.join(out), encoding='utf-8')
    return len(msgs), 0


def audit(d):
    """通道级计数审计：让任何口径分歧一眼可见（用户数/机器注入/轮次/原始字节）。"""
    import collections
    report = {}
    codex = d / CODEX_FILE
    if codex.exists():
        c = collections.Counter()
        with open(codex, encoding='utf-8', errors='replace') as f:
            for line in f:
                try:
                    o = json.loads(line)
                except json.JSONDecodeError:
                    c['unparseable'] += 1
                    continue
                t = o.get('type'); p = o.get('payload', {})
                c['type:' + str(t)] += 1
                if t == 'response_item' and p.get('type') == 'message' and p.get('role') == 'user':
                    text = ''.join(ch.get('text', '') for ch in p.get('content', []) if isinstance(ch, dict))
                    if not text.strip() or text.startswith('Caveat:'):
                        c['codex_user_machine'] += 1
                    elif MACHINE_TAG_RE.match(text):
                        c['codex_user_machine'] += 1
                    else:
                        c['codex_user_real'] += 1
                if t == 'turn_context':
                    c['codex_turns'] += 1
        raw = codex.read_bytes()
        c['codex_raw_role_user_bytes'] = raw.count(b'"role": "user"') + raw.count(b'"role":"user"')
        report['codex_hott2'] = dict(c)
    md = d / CHATGPT_FILE
    if md.exists():
        text = md.read_text(encoding='utf-8', errors='replace')
        report['chatgpt'] = {
            'prompt_sections': len(PROMPT_RE.findall(text)) if (PROMPT_RE.flags & re.M) else len([l for l in text.splitlines() if PROMPT_RE.match(l)]),
            'response_sections': len([l for l in text.splitlines() if RESPONSE_RE.match(l)]),
            'attachment_only_prompts': text.count('[Attachment:'),
        }
    gj = d / GEMINI_FILE
    if gj.exists():
        try:
            data = json.loads(gj.read_text(encoding='utf-8'))
        except UnicodeDecodeError:
            data = json.loads(gj.read_text(encoding='utf-8-sig'))
        chunks = data.get('chunkedPrompt', {}).get('chunks', [])
        c = collections.Counter(str(ch.get('role')) for ch in chunks)
        c['user_with_text'] = sum(1 for ch in chunks if ch.get('role') == 'user' and str(ch.get('text', '')).strip())
        c['user_drive_document'] = sum(1 for ch in chunks if ch.get('role') == 'user' and 'driveDocument' in ch)
        report['gemini'] = dict(c)
    return report


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dir', type=Path, default=DIR)
    ap.add_argument('--audit', action='store_true', help='只打印各格式通道级计数，不写提取文件')
    a = ap.parse_args()
    d = a.dir.resolve()
    if a.audit:
        print(json.dumps(audit(d), ensure_ascii=False, indent=1))
        return
    import datetime
    now = datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %z')
    results = [
        ('Codex', d / CODEX_FILE, d / CODEX_OUT, extract_codex),
        ('ChatGPT', d / CHATGPT_FILE, d / CHATGPT_OUT, extract_chatgpt),
        ('Gemini', d / GEMINI_FILE, d / GEMINI_OUT, extract_gemini),
    ]
    report = []
    for name, src, dst, fn in results:
        if not src.exists():
            report.append({'source': name, 'status': 'MISSING_INPUT', 'path': str(src)})
            continue
        kept, skipped = fn(src, dst, now)
        report.append({'source': name, 'status': 'OK', 'kept_user_messages': kept,
                       'skipped_wrapper_items': skipped, 'output': dst.name})
        print(f'{name}: {kept} 条用户消息 -> {dst.name}（跳过包装 {skipped} 条）')
    print(json.dumps(report, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
