#!/usr/bin/env python3
"""Finite project-governance copy. Does not copy research state or run a model.

copy preserves every source byte first; adapt-paths changes only path bindings;
seal records reviewed final bytes. All outputs are regular files, never links.
"""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import os
import posixpath
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
RECEIPT = HERE / 'copy-receipt.json'
RAW = HERE / 'pristine'

def digest(b): return hashlib.sha256(b).hexdigest()
def save(obj): RECEIPT.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

def mapping():
    pairs = {'AGENTS.md': 'CLAUDE.md', '最高指示.md': '.claude/cognition/最高指示.md'}
    for area in ['skills', 'tools']:
        for p in sorted((ROOT / '.codex' / area).rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc':
                rel = p.relative_to(ROOT).as_posix()
                pairs[rel] = rel.replace('.codex/', '.claude/', 1)
    for rel in ['AGENTS.md', 'README.md', 'verification/README.md',
                'cognition/LOAD_SET.json', 'cognition/PROTOCOL.md', 'cognition/TASK_ROUTING.md',
                'cognition/CORE_COGNITION.schema.json', 'cognition/SOURCE_MANIFEST.schema.json']:
        pairs['.codex/'+rel] = '.claude/'+rel
    for p in sorted(ROOT.glob('goal*.md')):
        if p.name != 'goal-3-工作路径树.md': pairs[p.name] = '.claude/tasks/'+p.name
    for rel in ['docs/design/detailed/认知水合关系与检查点事务合同.md',
                'docs/quality/数学结论机器证明与证据留存规范.md',
                'docs/quality/长治理文档分片与索引合同.md']:
        pairs[rel] = '.claude/'+rel
    base = '.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS'
    pairs[base+'.md'] = (base+'.md').replace('.codex/', '.claude/', 1)
    for p in sorted((ROOT/base).glob('*.md')):
        rel = p.relative_to(ROOT).as_posix(); pairs[rel] = rel.replace('.codex/', '.claude/', 1)
    for name in ['verify_core_cognition', 'build_core_cognition', 'test_core_cognition',
                 'verify_history_ledgers', 'verify_three_way_cognition', 'verify_governance_shards',
                 'validate_governance_shards', 'logical_document', 'test_goal_task_governance']:
        rel = 'scripts/audit/'+name+'.py'; pairs[rel] = '.claude/'+rel
    return pairs

def transform(rel, dest, text, pairs):
    # Historical sources and schemas keep their identity, not the current host's name.
    if rel.endswith(('strategy-full-verbatim.md', 'strategy-provenance.md', 'references/sources.md',
                     'MANIFEST.json', '.schema.json', 'validate_governance_shards.py')):
        return text
    if rel.endswith('.md'):
        def link(m):
            raw = m.group(1); target = raw.strip('<>')
            if re.match(r'[a-zA-Z][\w+.-]*:', target) or target.startswith('#'): return m.group(0)
            path, sep, anchor = target.partition('#')
            source = posixpath.normpath(posixpath.join(posixpath.dirname(rel), path))
            resolved = pairs.get(source, source)
            new = posixpath.relpath(resolved, posixpath.dirname(dest) or '.')
            new += sep+anchor
            return ']('+('<'+new+'>' if ' ' in new or raw.startswith('<') else new)+')'
        text = re.sub(r'\]\(([^)]+)\)', link, text)
    # Exact known governance paths only. Shared STATE/HEAD/locks/checkpoints remain .codex.
    alternatives = sorted(pairs, key=len, reverse=True)
    pat = re.compile(r'(?<![\w/.-])(?:'+ '|'.join(re.escape(x) for x in alternatives)+r')(?![\w.-])')
    if not rel.endswith('build_core_cognition.py'):
        text = pat.sub(lambda m: pairs[m.group(0)], text)
    if rel.endswith('.py') and rel.startswith('scripts/audit/'):
        text = text.replace('Path(__file__).resolve().parents[2]', 'Path(__file__).resolve().parents[3]')
    if rel == '.codex/tools/cognition_runtime.py':
        text = text.replace("script.parent.parent.name == '.codex'", "script.parent.parent.name == '.claude'")
        text = text.replace("('.codex','skills'", "('.claude','skills'")
    if rel.endswith('scripts/read_cognitive_closure.py'):
        text = text.replace('(".codex", "skills"', '(".claude", "skills"')
    return text

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('action',choices=['copy','adapt-paths','seal','verify'])
    a=ap.parse_args();pairs=mapping()
    if a.action=='copy':
        if RECEIPT.exists():raise RuntimeError('RECEIPT_ALREADY_EXISTS')
        for src,dst in pairs.items():
            p=ROOT/dst
            if p.exists() or p.is_symlink():raise RuntimeError('TARGET_EXISTS '+dst)
            if not (ROOT/src).is_file() or (ROOT/src).is_symlink():raise RuntimeError('INVALID_SOURCE '+src)
        RAW.mkdir(exist_ok=False);rows=[]
        for src,dst in pairs.items():
            b=(ROOT/src).read_bytes();name=digest(src.encode())+'.blob';(RAW/name).write_bytes(b)
            out=ROOT/dst;out.parent.mkdir(parents=True,exist_ok=True)
            with out.open('xb') as f:f.write(b)
            rows.append({'source':src,'target':dst,'source_sha256':digest(b),'source_bytes':len(b),
                         'pristine_blob':name,'copied_sha256':digest(out.read_bytes())})
        save({'schema_version':'claude-project-copy/v1','copied_at':dt.datetime.now(dt.timezone.utc).isoformat(),
              'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
              'scope':'governance files; business data and checkpoints shared, no symlink',
              'phase':'BYTE_IDENTICAL_COPY','files':rows})
    else:
        s=json.loads(RECEIPT.read_text())
        for row in s['files']:
            src=ROOT/row['source'];dst=ROOT/row['target']
            if digest(src.read_bytes())!=row['source_sha256']:raise RuntimeError('SOURCE_CHANGED '+row['source'])
            if dst.is_symlink() or not dst.is_file() or dst.stat().st_ino==src.stat().st_ino:
                raise RuntimeError('NOT_INDEPENDENT_REGULAR_FILE '+row['target'])
        if a.action=='adapt-paths':
            if s['phase']!='BYTE_IDENTICAL_COPY':raise RuntimeError('WRONG_PHASE')
            for row in s['files']:
                dst=ROOT/row['target']
                if digest(dst.read_bytes())!=row['copied_sha256']:raise RuntimeError('TARGET_DRIFT '+row['target'])
            for row in s['files']:
                b=(RAW/row['pristine_blob']).read_bytes()
                body=transform(row['source'],row['target'],b.decode(),pairs).encode()
                (ROOT/row['target']).write_bytes(body)
                row['path_adapted_sha256']=digest(body)
            s['phase']='PATH_ADAPTED_REVIEW_PENDING';save(s)
        elif a.action=='seal':
            for row in s['files']:
                b=(ROOT/row['target']).read_bytes();row['installed_sha256']=digest(b);row['installed_bytes']=len(b)
            s['phase']='INSTALLED_STATIC_REVIEWED';save(s)
        else:
            for row in s['files']:
                if digest((ROOT/row['target']).read_bytes())!=row.get('installed_sha256'):
                    raise RuntimeError('INSTALLED_DRIFT '+row['target'])
    print(json.dumps({'status':'PASS','action':a.action,'files':len(pairs),'receipt':str(RECEIPT)},ensure_ascii=False))

if __name__=='__main__':main()
