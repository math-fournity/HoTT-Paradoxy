#!/usr/bin/env python3
"""Current native-case import/marker upper bound; not proof-term axiom minimization."""
from pathlib import Path
import hashlib,importlib.util,json,re
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('scan',ROOT/'scripts/audit/scan_agda_unimath_e6.py');S=importlib.util.module_from_spec(sp);sp.loader.exec_module(S)
library=Path('/Volumes/D/HoTT-toolchain-cache/agda-unimath-7b81411d-astra-no-erasure-v1/src')
prim=Path('/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/xdg-data/agda/2.8.0-3d04bac/lib/prim')
graphs=['HoTT/verification/runs/20260920-MP-ASTRA-NATIVE-SOURCE-CONTRACT-001-01/imports.dot',
        'HoTT/verification/runs/20260920-MP-ASTRA-WEAK-LIFT-PRINCIPLE-001-01/imports.dot']
modules=set();graph_rows=[]
for rel in graphs:
    b=(ROOT/rel).read_bytes();names=re.findall(r'\[label="([^"]+)"\]',b.decode());assert len(names)==len(set(names))
    modules.update(names);graph_rows.append({'path':rel,'sha256':hashlib.sha256(b).hexdigest(),'modules':len(names)})
rows=[];markers=[]
for name in sorted(modules):
    root=ROOT/'HoTT/formal/agda-unimath' if name.startswith('hott-z.') else prim if name.startswith('Agda.') else library
    paths=[root/(name.replace('.','/')+ext) for ext in ['.agda','.lagda.md']]
    paths=[p for p in paths if p.is_file()];assert len(paths)==1,(name,paths)
    p=paths[0];b=p.read_bytes();rows.append({'module':name,'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
    for n,line in S.code_lines(p):
        if re.search(r'\b(postulate|primitive)\b',line.split('--',1)[0]):
            markers.append({'module':name,'path':str(p),'line':n,'text':line.strip()})
receipt={'status':'SYNTACTIC_IMPORT_AND_KEYWORD_UPPER_BOUND','graphs':graph_rows,'module_count':len(rows),
         'modules':rows,'marker_lines':markers,
         'limits':['Code-fence-aware lexical candidates, not a parser-level complete declaration list.',
                   'Imports are not minimized proof-term dependencies; no claim every declaration is used.',
                   'No metatheoretic consistency or non-derivability conclusion.',
                   'Runtime builtin snapshot pins do not mean every builtin was imported.']}
(OUT/'IMPORT-UPPER-BOUND.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'modules':len(rows),'markers':markers},ensure_ascii=False,indent=2))
