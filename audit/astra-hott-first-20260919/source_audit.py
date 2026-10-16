#!/usr/bin/env python3
"""Record local explicit imports and pragma identities; no semantic parser claim."""
from pathlib import Path
import hashlib, json, re, runpy

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
SRC = ROOT/'HoTT/formal/dedekind-omega-missile'
POSITIVE = runpy.run_path(str(OUT/'replay_audit.py'))['POSITIVE']
modules = {p.stem: p for p in SRC.glob('*.agda')}

def imports(p):
    # This scope contains explicit top-level imports on their own lines.
    return [m for m in re.findall(r'^\s*(?:open\s+)?import\s+([^\s]+)', p.read_text(), re.M)
            if m in modules]

def closure(name):
    found=set()
    def visit(n):
        if n in found: return
        found.add(n)
        for m in imports(modules[n]): visit(m)
    visit(name)
    return sorted(str(modules[n].relative_to(ROOT)) for n in found)

rows=[]
for rid in POSITIVE:
    run_dir=ROOT/'HoTT/verification/runs'/rid
    r=json.loads((run_dir/'RUN.json').read_text())
    manifest=json.loads((run_dir/'source-manifest.json').read_text())
    main=ROOT/r['command_argv'][-1]
    actual=closure(main.stem)
    recorded={f['path'] for f in manifest.get('files',[])}
    code=main.read_text()
    options=re.findall(r'\{-#\s*OPTIONS\s+(.+?)#-\}',code)
    missing=[p for p in actual if p not in recorded]
    stdout=(run_dir/'stdout.txt').read_text()
    rows.append({'run_id':rid,'entrypoint':str(main.relative_to(ROOT)),
                 'pragma_options':options,'pragma_safe':'--safe' in ' '.join(options).split(),
                 'explicit_local_import_closure':actual,'missing_local_source_pins':missing,
                 'missing_modules_in_saved_checker_output':{p:('Checking '+Path(p).stem+' ') in stdout for p in missing},
                 'whole_text_contains_safe':'--safe' in code,
                 'declared_postulates':bool(re.search(r'^postulate\s*$',code,re.M))})
(OUT/'SOURCE-AUDIT.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
for row in rows:
    print(row['run_id'],'safe=',row['pragma_safe'],'missing=',row['missing_local_source_pins'])

