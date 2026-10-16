# -*- coding: utf-8 -*-
"""GUI-ASSET-REAUDIT 自建工具的公共部分（SOP 002 §1、§2、§7）。只用标准库。

运行一律使用 `python3 -B -I`。本模块不读取、不引用第一战役的任何文件（I0）。
git 的使用受目标白名单约束：只允许 status、ls-files、rev-parse、hash-object、cat-file。
"""
import datetime
import hashlib
import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.dirname(HERE)                      # audit/GUI-ASSET-REAUDIT
ROOT = os.path.abspath(os.path.join(WORK, '..', '..'))
CORPUS_DIR = 'git-worktree对话录'
CORPUS_RE = re.compile(r'^git-worktree对话录/dev-.*-gui\.md$')
K = 5                                              # SOP 002 §3.1
BLOCK_MAX_LINES = 200                              # SOP 002 §4
BLOCK_MAX_BYTES = 40 * 1024
LONG_LINE_BYTES = 2000                             # SOP 002 §1、003 §9
GIT_ALLOWED = ('status', 'ls-files', 'rev-parse', 'hash-object', 'cat-file')
GENESIS = '0' * 64

LEDGER = os.path.join(WORK, 'ledger2.jsonl')
SEAL = os.path.join(WORK, 'seal-log.jsonl')
MANIFEST = os.path.join(WORK, 'manifest2.json')
BLOCKS = os.path.join(WORK, 'blocks.json')
ALIGN = os.path.join(WORK, 'align2.json')
STATUS = os.path.join(WORK, 'STATUS.md')


class Blocked(Exception):
    """身份、语料或工具条件不满足：按 SOP 写 BLOCKED 并停止（001 §7）。"""


def now_utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def sha256_hex(b):
    return hashlib.sha256(b).hexdigest()


def git(*args):
    """运行白名单内的 git 子命令；其他子命令一律拒绝（目标的硬规则）。"""
    if not args or args[0] not in GIT_ALLOWED:
        raise Blocked('git 子命令不在白名单内：%r' % (args[:1],))
    p = subprocess.run(['git', '-c', 'core.quotepath=off'] + list(args), cwd=ROOT,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout, p.stderr


def corpus_paths():
    """语料清单：用 ls-files 取得，按文件名过滤，tag 为第一个 ' - ' 之前的部分（002 §2）。"""
    rc, out, err = git('ls-files', '--', CORPUS_DIR)
    if rc != 0:
        raise Blocked('ls-files 失败：' + err.decode('utf-8', 'replace'))
    names = [x for x in out.decode('utf-8').split('\n') if x]
    res = []
    for n in names:
        if CORPUS_RE.match(n):
            tag = n.split('/', 1)[1].split(' - ', 1)[0]
            res.append((tag, n))
    tags = [t for t, _ in res]
    if len(res) != 8 or len(set(tags)) != 8:
        raise Blocked('语料数量或 tag 不符：%r' % tags)
    return sorted(res)


def split_lines(data):
    """按 SOP 002 §1 切行：以 LF 切分；末段非空则计为一行，末尾 LF 之后的空串不计。

    返回 [(起始偏移, 不含 LF 的字节, 是否以 LF 结束)]，行号从 1 开始对应列表下标 +1。
    """
    out = []
    pos = 0
    n = len(data)
    while pos < n:
        i = data.find(b'\n', pos)
        if i < 0:
            out.append((pos, data[pos:], False))
            break
        out.append((pos, data[pos:i], True))
        pos = i + 1
    return out


def chunk_bytes(data, lines, s, e):
    """第 s 行至第 e 行（1 基，含端点）的字节切片，含每行的 LF（SOP 002 §1）。"""
    if not (1 <= s <= e <= len(lines)):
        raise ValueError('行区间越界：%d-%d / %d' % (s, e, len(lines)))
    a = lines[s - 1][0]
    b = lines[e][0] if e < len(lines) else len(data)
    return data[a:b]


def read_bytes(path):
    with open(path, 'rb') as f:
        return f.read()


def load_json(path):
    with open(path, 'rb') as f:
        return json.loads(f.read().decode('utf-8'))


def write_json(path, obj):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')
    os.replace(tmp, path)


def load_manifest():
    return load_json(MANIFEST)


def verify_corpus(manifest):
    """语料身份核验：工作树字节必须与 manifest2 的 sha256 与字节数一致，否则 BLOCKED（002 §9）。"""
    for fe in manifest['files']:
        data = read_bytes(os.path.join(ROOT, fe['path']))
        if sha256_hex(data) != fe['sha256'] or len(data) != fe['bytes']:
            raise Blocked('语料身份改变：%s' % fe['tag'])
    return True


def file_by_tag(manifest, tag):
    for fe in manifest['files']:
        if fe['tag'] == tag:
            return fe
    raise Blocked('manifest2 中没有该 tag：%s' % tag)


def load_corpus_lines(manifest, tag):
    """读取某 tag 的字节与切行结果，并核对其身份。"""
    fe = file_by_tag(manifest, tag)
    data = read_bytes(os.path.join(ROOT, fe['path']))
    if sha256_hex(data) != fe['sha256'] or len(data) != fe['bytes']:
        raise Blocked('语料身份改变：%s' % tag)
    return data, split_lines(data)


# ---------- 账本（ledger2.jsonl）：每行带 prev，prev 为上一行原始字节（含换行）的 SHA-256 ----------

def ledger_records(path=LEDGER):
    if not os.path.exists(path):
        return []
    data = read_bytes(path)
    recs = []
    pos = 0
    while pos < len(data):
        i = data.find(b'\n', pos)
        if i < 0:
            raise Blocked('账本末尾缺少换行，账本损坏')
        raw = data[pos:i + 1]
        recs.append((json.loads(raw[:-1].decode('utf-8')), raw))
        pos = i + 1
    return recs


def ledger_append(rec, path=LEDGER):
    recs = ledger_records(path)
    rec = dict(rec)
    rec['prev'] = sha256_hex(recs[-1][1]) if recs else GENESIS
    rec['ts'] = rec.get('ts') or now_utc()
    line = json.dumps(rec, ensure_ascii=False, sort_keys=True, separators=(',', ':')) + '\n'
    with open(path, 'ab') as f:
        f.write(line.encode('utf-8'))
    return rec


def ledger_chain_ok(path=LEDGER):
    """逐行核对 prev 链。返回 (是否完整, 记录数, 首个断点行号或 None)。"""
    recs = ledger_records(path)
    prev = GENESIS
    for i, (rec, raw) in enumerate(recs, start=1):
        if rec.get('prev') != prev:
            return False, len(recs), i
        prev = sha256_hex(raw)
    return True, len(recs), None


# ---------- 封印日志（seal-log.jsonl）：只追加，事件单调 ----------

def seal_append(event, **kw):
    rec = {'event': event, 'ts': now_utc()}
    rec.update(kw)
    with open(SEAL, 'a', encoding='utf-8') as f:
        f.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + '\n')
    return rec


def seal_events():
    if not os.path.exists(SEAL):
        return []
    with open(SEAL, 'r', encoding='utf-8') as f:
        return [json.loads(x) for x in f if x.strip()]


def load_blocks():
    return load_json(BLOCKS)['blocks']
