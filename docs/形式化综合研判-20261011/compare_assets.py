#!/usr/bin/env python3
"""Inventory all formal code in registered worktrees against current dev files."""
import collections
import hashlib
import json
from pathlib import Path
import subprocess
ROOT = Path('/Volumes/D/HoTT_AI_HANDOFF_20260911/.claude/worktrees/elegant-mclaren-767fb0')
CANON = Path('/Volumes/D/HoTT_AI_HANDOFF_20260911')
DEST = ROOT / 'docs/形式化综合研判-20261011'
inventory = json.loads((DEST / 'worktree-inventory.json').read_text())
exts = {'.lean','.agda','.v','.smt2','.mm','.lisp','.acl2'}
canon_files = {str(p.relative_to(CANON)): hashlib.sha256(p.read_bytes()).hexdigest() for p in (CANON/'HoTT/formal').rglob('*') if p.is_file() and p.suffix in exts}
hashes = collections.defaultdict(list)
for path, digest in canon_files.items():
    hashes[digest].append(path)
rows = []
unique = collections.defaultdict(list)
for wt in inventory['worktrees']:
    root = Path(wt['path'])
    if root == ROOT or root == CANON:
        continue
    result = subprocess.run(['git','--no-optional-locks','-C',str(root),'ls-files','-z','--cached','--others','--exclude-standard','--','HoTT/formal'],capture_output=True,timeout=90)
    paths = sorted(set(x.decode() for x in result.stdout.split(b'\0') if x))
    counts = collections.Counter()
    different = []
    for rel in paths:
        p = root / rel
        if p.suffix not in exts or not p.is_file():
            continue
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        if canon_files.get(rel) == digest:
            status = 'same-path-same-content'
        elif digest in hashes:
            status = 'same-content-other-canonical-path'
        else:
            status = 'not-byte-identical-to-canonical-code'
            record = {'worktree':str(root),'path':rel,'sha256':digest,'bytes':p.stat().st_size,'canonical_same_path_exists':rel in canon_files}
            unique[digest].append(record)
            different.append(record)
        counts[status] += 1
    rows.append({'worktree':str(root),'counts':dict(counts),'different_code':different})
report={'captured_at':inventory['captured_at'],'canonical_dev':inventory['canonical_dev'],'scope':'all tracked/untracked nonignored formal code in all registered worktrees; byte-identity is dedup only, not reading or proof verification','worktrees':rows,'unique_digest_count':len(unique),'unique_code_groups':list(unique.values())}
(DEST/'asset-comparison.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
lines=['# 全工位覆盖初筛\n',f"采集时间：{inventory['captured_at']}；canonical dev：`{inventory['canonical_dev'][:8]}`。登记 {inventory['worktree_count']} 个worktree，均存在且初筛无读取错误。\n",'仅初筛，不代表全部原文已读或全部证明已重放。dirty不代表新增成果，clean不代表会话没在工作。\n','| 工位 | dirty | 分支独有提交 | 形式源码相同路径同内容 | 其他路径相同内容 | 待判不同源码 |','|---|---:|---:|---:|---:|---:|']
by_path={r['worktree']:r for r in rows}
for wt in inventory['worktrees']:
    r=by_path.get(wt['path'],{}); c=r.get('counts',{})
    lines.append(f"| `{wt['path']}` | {wt.get('working_count',0)} | {wt.get('unique_commit_count',0)} | {c.get('same-path-same-content',0)} | {c.get('same-content-other-canonical-path',0)} | {c.get('not-byte-identical-to-canonical-code',0)} |")
lines += ['\n详细源身份：`asset-comparison.json`；全部dirty及分支差异：`worktree-inventory.json`。','\n不能把同字节当作已读；仅用于排除重复劳动。同路径不同内容必须读实际版本；尚未有机器证据者不能登记成已证。']
(DEST/'全工位覆盖初筛.md').write_text('\n'.join(lines)+'\n')
for r in rows:
    print(r['worktree'],r['counts'])
print('Unique differing code groups',len(unique))
