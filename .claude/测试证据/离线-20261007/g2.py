# 设计会话的离线负对照与正对照（只在 scratchpad 的副本上做；不写测试副本与正式工作树）。
# 用法：python3 -I -B g2.py <新的运行目录>（运行目录不得已存在）
import sys, json, hashlib, shutil, subprocess, importlib.util, pathlib

sys.dont_write_bytecode = True
SCR = pathlib.Path(sys.argv[1])
R = pathlib.Path('/Volumes/D/HoTT-reaudit-testrun')
MAIN = pathlib.Path('/Volumes/D/HoTT_AI_HANDOFF_20260911')
AUDIT = MAIN / '.claude' / '复算收尾审计.py'
VALIDATOR = MAIN / 'scripts' / 'audit' / 'verify_governance_shards.py'
A = 'audit/GUI-ASSET-REAUDIT/'
NEW = 'B-dev-01-0041'


def sha(b):
    return hashlib.sha256(b).hexdigest()


spec = importlib.util.spec_from_file_location('audit_mod', str(AUDIT))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

SCR.mkdir(parents=True, exist_ok=True)
BASE = SCR / 'base'
assert not BASE.exists(), 'base exists; use a new run directory'
BASE.mkdir()
shutil.copytree(R / 'git-worktree对话录', BASE / 'git-worktree对话录')
shutil.copytree(R / 'audit', BASE / 'audit')

# 0041 的 classes、assets 哈希：与审计脚本相同的口径，由执行者的解析函数算出（只用于合成收据）
sys.path.insert(0, str(BASE / A / 'tools'))
import commit_block as cb  # noqa: E402

errs = []
rows = cb.class_rows('dev-01', NEW, errs)
rows.sort(key=lambda x: (x['start'], x['end']))
ct = '\n'.join('%d\t%d\t%s\t%s' % (x['start'], x['end'], x['class'], x['ref']) for x in rows)
at = '\n'.join(json.dumps(x, ensure_ascii=False, sort_keys=True) for x in cb.parse_assets() if x.get('block') == NEW)
CLS, AST = sha(ct.encode('utf-8')), sha(at.encode('utf-8'))
print('0041 class rows:', len(rows), '| errs:', errs[:3], '| assets lines:', 0 if not at else at.count('\n') + 1)


def mk(name):
    d = SCR / name
    assert not d.exists(), d
    shutil.copytree(BASE, d)
    return d


def last_raw(p):
    return [x for x in p.read_bytes().split(b'\n') if x.strip()][-1] + b'\n'


def append(p, rec):
    data = p.read_bytes()
    if not data.endswith(b'\n'):
        data += b'\n'
    rec = dict(rec, prev=sha(last_raw(p)))
    p.write_bytes(data + json.dumps(rec, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8') + b'\n')


def ra_record(d):
    man = json.loads((d / A / 'manifest2.json').read_bytes().decode('utf-8'))
    rel = [f['path'] for f in man['files'] if f['tag'] == 'dev-01'][0]
    bl = json.loads((d / A / 'blocks.json').read_bytes().decode('utf-8'))
    bl = bl if isinstance(bl, list) else bl.get('blocks', [])
    b = [x for x in bl if x['block'] == NEW][0]
    L = (d / rel).read_bytes().splitlines(keepends=True)
    sl = b''.join(L[b['start'] - 1:b['end']])
    text = (d / A / 'notes2' / 'dev-01.md').read_bytes().decode('utf-8')
    secs = [s for s in mod.sections_of(text) if s['block'] == NEW and not s['void']]
    assert len(secs) == 1, len(secs)
    return {'type': 'RA', 'tag': 'dev-01', 'block': NEW, 'start': b['start'], 'end': b['end'],
            'chunk_sha256': sha(sl), 'bytes': len(sl), 'notes_sha256': sha(secs[0]['body'].encode('utf-8')),
            'classes_sha256': CLS, 'assets_sha256': AST, 'rid': 'RA-TEST-0041'}


def run_audit(d):
    rep = d / 'report.json'
    p = subprocess.run(['python3', '-I', '-B', str(AUDIT), str(d), '--out', str(rep)], capture_output=True, text=True)
    r = json.loads(rep.read_text(encoding='utf-8'))
    f = r['facts']
    keys = ['RA_count', 'blocks_committed', 'complete', 'ledger_chain_breaks', 'RA_notes_mismatch',
            'RA_classes_mismatch', 'RA_assets_mismatch', 'v2_blocks_without_gate_or_rs', 'seal_events']
    out = {'exit': p.returncode, 'blocking_problems': r['blocking_problems']}
    out.update({k: f.get(k) for k in keys})
    return out


res = {}

d = mk('g2-m0'); res['M0 正对照（未改动）'] = run_audit(d)

d = mk('g2-m1'); p = d / A / 'notes2' / 'dev-01.md'
lines = p.read_bytes().decode('utf-8').split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('## B-dev-01-0005 |')]
assert len(idx) == 1, idx
lines.insert(idx[0] + 1, '负对照：注入的一行')
p.write_bytes('\n'.join(lines).encode('utf-8'))
res['M1 改 notes 一行（块 0005）'] = run_audit(d)

d = mk('g2-m2'); p = d / A / 'ledger2.jsonl'
L = p.read_bytes().split(b'\n')
k = [i for i, x in enumerate(L) if x.strip()][9]
o = json.loads(L[k]); o['mut'] = 'x'
L[k] = json.dumps(o, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
p.write_bytes(b'\n'.join(L))
res['M2 改账本第 10 行'] = run_audit(d)

d = mk('g2-m3'); p = d / A / 'seal-log.jsonl'
data = p.read_bytes()
if not data.endswith(b'\n'):
    data += b'\n'
p.write_bytes(data + json.dumps({'event': 'SEAL_BREACH', 'ts': '2026-10-08T01:00:00Z', 'note': '负对照'}, ensure_ascii=False).encode('utf-8') + b'\n')
res['M3 封印日志追加 SEAL_BREACH'] = run_audit(d)

d = mk('g2-m4'); append(d / A / 'ledger2.jsonl', ra_record(d))
res['M4 v2 收据（0041）无 GATE、无 RS'] = run_audit(d)

d = mk('g2-m5'); lg = d / A / 'ledger2.jsonl'
append(lg, {'type': 'RS', 'rid': 'RS-TEST-0041', 'block': NEW})
append(lg, {'type': 'GATE', 'block': NEW, 'rid': 'GATE-TEST-0041', 'rs': 'RS-TEST-0041'})
append(lg, ra_record(d))
res['M5 对照：先 RS，再 GATE，再 RA（0041）'] = run_audit(d)

d = mk('g2-m6'); p = d / A / 'ledger2.jsonl'
L = p.read_bytes().split(b'\n')
nz = [i for i, x in enumerate(L) if x.strip()]
last = json.loads(L[nz[-1]])
assert last['type'] == 'RA' and last['block'] == 'B-dev-01-0040', last
p.write_bytes(b'\n'.join(x for i, x in enumerate(L) if x.strip() and i != nz[-1]) + b'\n')
res['M6 删除末尾的 RA（0040）'] = run_audit(d)

d = mk('g2-m7'); p = d / A / 'ledger2.jsonl'
L = p.read_bytes().split(b'\n')
hit = [i for i, x in enumerate(L) if x.strip() and json.loads(x).get('type') == 'RA' and json.loads(x).get('block') == 'B-dev-01-0020']
assert len(hit) == 1, hit
p.write_bytes(b'\n'.join(x for i, x in enumerate(L) if x.strip() and i != hit[0]) + b'\n')
res['M7 删除中间的 RA（0020）'] = run_audit(d)

print(json.dumps(res, ensure_ascii=False, indent=1))


# ---- J：治理校验器的正负对照（副本） ----
def validator(root, out):
    p = subprocess.run(['python3', '-B', str(VALIDATOR), '--project-root', str(root), '--out', str(out)], capture_output=True, text=True)
    txt = out.read_text(encoding='utf-8') if out.exists() else p.stdout + p.stderr
    return p.returncode, txt


def jroot(name):
    d = SCR / name
    (d / 'dev-docs').mkdir(parents=True)
    shutil.copy2(R / 'dev-docs' / 'GUI导出全量复算重读审计SOP.md', d / 'dev-docs')
    shutil.copytree(R / 'dev-docs' / 'GUI导出全量复算重读审计SOP', d / 'dev-docs' / 'GUI导出全量复算重读审计SOP')
    return d


j0 = jroot('j0')
code, txt = validator(j0, SCR / 'j0.json')
print('J0 正对照 exit', code, '\n', txt[:700])

j1 = jroot('j1')
ix = j1 / 'dev-docs' / 'GUI导出全量复算重读审计SOP.md'
ls0 = ix.read_bytes().decode('utf-8').split('\n')
ls1 = [l for l in ls0 if not l.startswith('last_shard:')]
assert len(ls1) == len(ls0) - 1
ix.write_bytes('\n'.join(ls1).encode('utf-8'))
code, txt = validator(j1, SCR / 'j1.json')
print('J1 删除 last_shard exit', code, '\n', txt[:400])

j2 = jroot('j2')
(j2 / 'dev-docs' / 'GUI导出全量复算重读审计SOP' / '003 - 全量重读五拍循环与双账本.md').unlink()
code, txt = validator(j2, SCR / 'j2.json')
print('J2 缺少 003 分片 exit', code, '\n', txt[:400])

print('副本账本与测试副本一致（未被改动）:', sha((BASE / A / 'ledger2.jsonl').read_bytes()) == sha((R / A / 'ledger2.jsonl').read_bytes()))
