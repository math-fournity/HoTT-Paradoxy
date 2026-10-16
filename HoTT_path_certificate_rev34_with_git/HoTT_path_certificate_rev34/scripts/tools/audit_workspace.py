#!/usr/bin/env python3
"""Defined-scope source integrity, syntax, and high-confidence credential check.
Does not execute recovered source and does not claim a comprehensive secret audit.
"""
from pathlib import Path
import argparse, ast, hashlib, json, re, subprocess


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    root=Path(__file__).resolve().parents[2]
    if a.out.exists():raise SystemExit('Output exists')
    m=json.loads((root/'scripts/RECOVERY_MANIFEST.json').read_text())
    errors=[]
    for row in m['unique_payloads']:
        p=root/row['path'];b=p.read_bytes()
        if len(b)!=row['bytes'] or hashlib.sha256(b).hexdigest()!=row['sha256']:errors.append(row['path'])
    assert not errors
    syntax=[]
    for p in (root/'scripts').rglob('*.py'):
        if 'recovered' in p.parts:continue
        ast.parse(p.read_text(),filename=str(p));syntax.append(p.relative_to(root).as_posix())
    # Search strong signals only, never expose a matching credential's content.
    patterns={'private_key_header':re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'),
              'aws_access_key':re.compile(rb'\bAKIA[A-Z0-9]{16}\b'),
              'github_pat':re.compile(rb'\bgh[pousr]_[A-Za-z0-9]{36,255}\b'),
              'explicit_api_secret':re.compile(rb'(?i)(?:api_key|apikey|secret_key)\s*[:=]\s*["\']([A-Za-z0-9_-]{35,})["\']')}
    hits=[];count=0
    for p in root.rglob('*'):
        if not p.is_file() or '.git' in p.relative_to(root).parts:continue
        count+=1;b=p.read_bytes()
        for label,pat in patterns.items():
            if pat.search(b):hits.append({'path':p.relative_to(root).as_posix(),'pattern':label})
    tracked=subprocess.run(['git','ls-tree','-r','--name-only','checkpoint-rev15-import'],cwd=root,capture_output=True,text=True,check=True).stdout.splitlines()
    protected=[];changed=[]
    allowed={'AGENTS.md','MEMORY.md','.codex/research/hott/STATE.json','.codex/research/hott/FRONTIER.md',
             '.codex/research/hott/LESSONS.md','.codex/research/hott/RESUME.md','.codex/cognition/HEAD.json'}
    # Per-file retrieval without changing index or checkout.
    for name in tracked:
        old=subprocess.run(['git','show','checkpoint-rev15-import:'+name],cwd=root,capture_output=True,check=True).stdout
        p=root/name
        same=p.is_file() and p.read_bytes()==old
        if not same:changed.append(name)
        elif name not in allowed:protected.append(name)
    unexpected=[p for p in changed if p not in allowed]
    assert not unexpected,unexpected
    report={'schema_version':'hott-workspace-audit/v1','recovered_payloads':len(m['unique_payloads']),
            'source_occurrences':len(m['source_occurrences']),'recovered_hash_mismatches':errors,
            'new_python_ast_parse_count':len(syntax),'new_python_paths':syntax,
            'credential_pattern_file_count':count,'credential_pattern_hits':hits,
            'credential_scope':'Only listed strong regex signals; not a comprehensive credential or semantic security certification',
            'original_import_files':len(tracked),'protected_unchanged_count':len(protected),
            'changed_import_paths':changed,'unexpected_original_changes':unexpected,
            'status':'PASS_DEFINED_SCOPE' if not hits else 'REVIEW_CREDENTIAL_MATCHES',
            'recovered_code_executed_by_audit':False}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='new_python_paths'},ensure_ascii=False,indent=2))
    if hits:raise SystemExit(2)
if __name__=='__main__':main()
