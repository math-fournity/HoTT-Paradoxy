#!/usr/bin/env python3
"""三份对话录用户发言的逐句拆解账本（审计基建）。

来源：本目录三份用户消息提取文件（含源行号定位）。
分句规则：按 。！？；?! 断句；换行分隔的条目（列表/标题）各自成句；≥2字符才计入。
转述块识别：Gemini 信件（OUT-00x）与网页版中转发的 Gemini 回信正文标记为"转述块"，
  仅拆解用户自己的框架句，转述正文计为独立转述单元（内容覆盖在 A6）。
输出：sentence_ledger.json（每句：ID、来源、轮次、源行、句文本、块类型、锚点占位）。
用法：python3 -B build_sentence_ledger.py [--dir 目录]
"""
from pathlib import Path
import argparse, json, re

DIR = Path(__file__).resolve().parent
OUT = 'sentence_ledger.json'

# --- 分句 ---
SPLIT_RE = re.compile(r'(?<=[。！？；?!])\s*')


def split_sentences(text):
    """按标点断句；按行拆列表/标题；保留原文（去首尾空白）。"""
    units = []
    for raw_line in text.split('\n'):
        line = raw_line.strip()
        if not line:
            continue
        for sent in SPLIT_RE.split(line):
            s = sent.strip()
            if len(s) >= 2:
                units.append(s)
    return units


# --- Codex：从合并38轮文档取每轮用户句 ---
def load_codex(doc_path):
    doc = open(doc_path, encoding='utf-8').read()
    entries = []
    cur_turn = None
    lines = doc.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('# 附录'):
            break
        m = re.match(r'^## 第 (\d+) 轮 · (\S+)', line)
        if m:
            cur_turn = int(m.group(1))
            i += 1
            continue
        m2 = re.match(r'^### 用户（([^，]+)，源 (\d+) 行）', line)
        if m2 and cur_turn:
            ts, src_line = m2.group(1), m2.group(2)
            i += 1
            body = []          # (line_text, platform_flag)
            in_preamble = False
            while i < len(lines):
                ln = lines[i]
                if ln.startswith('### ') or re.match(r'^## 第 \d+ 轮', ln) or ln.startswith('# 附录'):
                    break
                if ln.strip() == '---':
                    i += 1
                    continue
                if ln.startswith('# Response annotations:') or ln.startswith('# Files pasted by the user:'):
                    in_preamble = True
                    body.append((ln, True))
                    i += 1
                    continue
                if ln.startswith('## My request:'):
                    in_preamble = False
                    body.append((ln, True))
                    i += 1
                    continue
                if ln.startswith('<response-annotations>') or ln.startswith('</response-annotations>') or ln.startswith('['):
                    body.append((ln, True))
                    i += 1
                    continue
                body.append((ln, in_preamble))
                i += 1
            text = '\n'.join(t for t, _ in body).strip()
            entries.append({'turn': cur_turn, 'ts': ts, 'src_line': src_line, 'text': text,
                            'platform_flagged': in_preamble,
                            'id_prefix': f'C-T{cur_turn:02d}-L{src_line}'})
            continue
        i += 1
    return entries


# --- ChatGPT md：56 条 Prompt（111 节中的用户节） ---
def load_web(path):
    text = open(path, encoding='utf-8').read()
    entries = []
    idx = 0
    lines = text.split('\n')
    i = 0
    prompt_re = re.compile(r'^## Prompt:\s*$')
    resp_re = re.compile(r'^## Response:\s*$')
    stamp_re = re.compile(r'^\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2}:\d{2} [AP]M\s*$')
    while i < len(lines):
        if resp_re.match(lines[i]):
            j = i + 1
            stamp = ''
            if j < len(lines) and stamp_re.match(lines[j].strip()):
                stamp = lines[j].strip()
                j += 1
            entries.append({'msg': None, 'ts': stamp, 'text': '', 'is_response': True,
                            'id_prefix': f'W-R{len(entries)+1}'})
            i = j
            continue
        if prompt_re.match(lines[i]):
            idx += 1
            j = i + 1
            stamp = ''
            if j < len(lines) and stamp_re.match(lines[j].strip()):
                stamp = lines[j].strip()
                j += 1
            while j < len(lines) and lines[j] == '':
                j += 1
            body = []
            while j < len(lines) and not (prompt_re.match(lines[j]) or resp_re.match(lines[j])):
                body.append(lines[j])
                j += 1
            entries.append({'msg': idx, 'ts': stamp, 'text': '\n'.join(body).strip(),
                            'id_prefix': f'W-{idx:02d}'})
            i = j
        else:
            i += 1
    return entries


# --- Gemini：22 条 user chunk ---
def load_gemini(path):
    data = json.loads(open(path, encoding='utf-8').read())
    chunks = data.get('chunkedPrompt', {}).get('chunks', [])
    entries = []
    n = 0
    for c in chunks:
        if c.get('role') != 'user':
            continue
        n += 1
        if 'text' in c and str(c.get('text', '')).strip():
            entries.append({'msg': n, 'ts': c.get('createTime', ''), 'text': str(c['text']).strip(),
                            'id_prefix': f'G-{n:02d}'})
        else:
            entries.append({'msg': n, 'ts': c.get('createTime', ''), 'text': '',
                            'attachment': True, 'id_prefix': f'G-{n:02d}'})
    return entries


# --- 转述块识别：Gemini 信（OUT-00x 标题）与网页版里内联的 Gemini 回信 ---
RELAY_MARKERS = ('# 致 Gemini', '致 OUT-00', 'Gemini的回复', '这是它的回复', '这是Gemini的回复')


def split_relay(text):
    """把消息切成 (用户框架句列表, 转述块列表)。转述块=```代码围栏内或明确信件正文。"""
    own, relays = [], []
    in_fence = False
    fence_buf = []
    for line in text.split('\n'):
        if line.strip().startswith('```') and len(line.strip()) >= 3:
            if in_fence:
                relays.append('\n'.join(fence_buf))
                fence_buf = []
            in_fence = not in_fence
            continue
        if in_fence:
            fence_buf.append(line)
            continue
        own.append(line)
    own_text = '\n'.join(own)
    for s in split_sentences(own_text):
        own.append if False else None
    return split_sentences(own_text), relays


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', type=Path, default=DIR)
    a = ap.parse_args()
    d = a.dir.resolve()
    codex = load_codex(d / 'Codex-HoTT-2-完整38轮-用户与AI-20260911.md')
    web = load_web(d / 'ChatGPT-HoTT - Main-20260911-1222.md')
    gem = load_gemini(d / 'Gemini - AI 对话录.json')
    ledger = []
    stats = {'codex_msgs': 0, 'web_msgs': 0, 'gemini_msgs': 0,
             'own_sentences': 0, 'relay_blocks': 0, 'attachments': 0}
    for e in codex:
        stats['codex_msgs'] += 1
        plat_text, user_text = '', e['text']
        if '# Response annotations:' in e['text'] or '# Files pasted by the user:' in e['text']:
            lines2 = e['text'].split('\n')
            plat_lines, user_lines2, in_p = [], [], False
            for ln in lines2:
                if ln.startswith('# Response annotations:') or ln.startswith('# Files pasted by the user:'):
                    in_p = True
                    plat_lines.append(ln)
                    continue
                if ln.startswith('## My request:'):
                    in_p = False
                    plat_lines.append(ln)
                    continue
                (plat_lines if in_p else user_lines2).append(ln)
            plat_text, user_text = '\n'.join(plat_lines), '\n'.join(user_lines2)
        for k, s in enumerate(split_sentences(plat_text), 1):
            ledger.append({'id': f"{e['id_prefix']}-P{k:02d}", 'src': 'codex', 'turn': e['turn'],
                           'ts': e['ts'], 'block': 'platform', 'text': s, 'anchor': ''})
        sents, relays = split_relay(user_text)
        for k, s in enumerate(sents, 1):
            ledger.append({'id': f"{e['id_prefix']}-S{k:02d}", 'src': 'codex', 'turn': e['turn'],
                           'ts': e['ts'], 'block': 'own', 'text': s, 'anchor': ''})
            stats['own_sentences'] += 1
        for k, r in enumerate(relays, 1):
            ledger.append({'id': f"{e['id_prefix']}-R{k}", 'src': 'codex', 'turn': e['turn'],
                           'ts': e['ts'], 'block': 'relay', 'text': r[:120] + ('…' if len(r) > 120 else ''),
                           'relay_len': len(r), 'anchor': ''})
            stats['relay_blocks'] += 1
    sec = 0
    for e in web:
        sec += 1
        if e.get('is_response'):
            ledger.append({'id': f'W-SEC{sec:03d}-AI', 'src': 'web', 'turn': sec,
                           'ts': e['ts'], 'block': 'ai_response', 'text': '（AI 回复节：无用户发言，计为遍历单元）', 'anchor': 'A6/A9'})
            continue
        stats['web_msgs'] += 1
        if '[Attachment:' in e['text'] and len(e['text']) < 80:
            ledger.append({'id': f"{e['id_prefix']}-ATT", 'src': 'web', 'turn': sec,
                           'ts': e['ts'], 'block': 'attachment', 'text': e['text'], 'anchor': ''})
            stats['attachments'] += 1
            continue
        if e['id_prefix'] == 'W-51':
            sents, relays = split_sentences(e['text']), []
        else:
            sents, relays = split_relay(e['text'])
        for k, s in enumerate(sents, 1):
            ledger.append({'id': f"{e['id_prefix']}-S{k:02d}", 'src': 'web', 'turn': sec,
                           'ts': e['ts'], 'block': 'own', 'text': s, 'anchor': ''})
            stats['own_sentences'] += 1
        for k, r in enumerate(relays, 1):
            ledger.append({'id': f"{e['id_prefix']}-R{k}", 'src': 'web', 'turn': sec,
                           'ts': e['ts'], 'block': 'relay', 'text': r[:120] + ('…' if len(r) > 120 else ''),
                           'relay_len': len(r), 'anchor': ''})
            stats['relay_blocks'] += 1
    for e in gem:
        stats['gemini_msgs'] += 1
        if e.get('attachment'):
            ledger.append({'id': f"{e['id_prefix']}-ATT", 'src': 'gemini', 'turn': e['msg'],
                           'ts': e['ts'], 'block': 'attachment', 'text': '（Drive 文档附件，无正文文本）', 'anchor': ''})
            stats['attachments'] += 1
            continue
        sents, relays = split_relay(e['text'])
        for k, s in enumerate(sents, 1):
            ledger.append({'id': f"{e['id_prefix']}-S{k:02d}", 'src': 'gemini', 'turn': e['msg'],
                           'ts': e['ts'], 'block': 'own', 'text': s, 'anchor': ''})
            stats['own_sentences'] += 1
        for k, r in enumerate(relays, 1):
            ledger.append({'id': f"{e['id_prefix']}-R{k}", 'src': 'gemini', 'turn': e['msg'],
                           'ts': e['ts'], 'block': 'relay', 'text': r[:120] + ('…' if len(r) > 120 else ''),
                           'relay_len': len(r), 'anchor': ''})
            stats['relay_blocks'] += 1
    json.dump({'stats': stats, 'entries': ledger}, open(d / OUT, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False))


if __name__ == '__main__':
    main()
