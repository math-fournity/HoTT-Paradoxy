#!/usr/bin/env python3
"""Inventory Agda's own dependency graph; syntactic upper bound, not term pruning."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
library=Path('/Volumes/D/HoTT-toolchain-cache/agda-unimath-7b81411d-astra-no-erasure-v1')
graph=OUT/'attempts/005/imports.dot'
modules=re.findall(r'\[label="([^"]+)"\]',graph.read_text())
assert len(modules)==len(set(modules))
rows=[];markers=[]
for mod in sorted(modules):
 base=ROOT/'HoTT/formal/agda-unimath' if mod.startswith('hott-z.') else library/'src'
 choices=[base/(mod.replace('.','/')+ext) for ext in ['.agda','.lagda.md']]
 found=[p for p in choices if p.is_file()]
 if not found and mod.startswith('Agda.'):
  p=Path('/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/xdg-data/agda/2.8.0-3d04bac/lib/prim')/(mod.replace('.','/')+'.agda');found=[p] if p.is_file() else []
 assert len(found)==1,(mod,found)
 p=found[0];raw=p.read_bytes();row={'module':mod,'path':str(p),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)};rows.append(row)
 active=p.suffix=='.agda'
 for n,line in enumerate(raw.decode().splitlines(),1):
  if p.name.endswith('.lagda.md') and line.strip().startswith('```'):
   active=line.strip()=='```agda';continue
  if not active:continue
  code=line.split('--',1)[0]
  if re.search(r'\b(postulate|primitive)\b|\{!-|\{!!\}|\{\-#\s*(TERMINATING|NON_TERMINATING|NO_POSITIVITY_CHECK|INJECTIVE|REWRITE|COMPILE)',code):
   markers.append({'module':mod,'path':str(p),'line':n,'text':line})
original_runs=[];unparsed=[]
for p in sorted((ROOT/'HoTT/verification/runs').glob('*/source-manifest.json')):
 try:m=json.loads(p.read_text())
 except (ValueError,OSError):continue
 deps=m.get('external_dependencies',[])
 if not isinstance(deps,list) or any(not isinstance(d,dict) for d in deps):
  unparsed.append(str(p.relative_to(ROOT)));continue
 for d in deps:
  if d.get('local_path')=='/Volumes/D/HoTT-toolchain-cache/agda-unimath-7b81411d':
   run=json.loads((p.parent/'RUN.json').read_text());stdout=(p.parent/'stdout.txt').read_text()
   original_runs.append({'run_id':run['run_id'],'proof_id':run['proof_id'],'status':run['status'],'claims':run['claim_ids'],'stdout_records_erasure_module':'Checking reflection.erasing-equality' in stdout,'manifest_sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
result={'status':'SYNTACTIC_IMPORT_CLOSURE_ONLY','not_certified':['Minimal proof-term axiom set','Metatheoretic consistency','All possible unsafe features','Every historical unstructured proof run'],'graph':str(graph.relative_to(ROOT)),'graph_sha256':hashlib.sha256(graph.read_bytes()).hexdigest(),'modules':rows,'marker_lines':markers,'original_tree_registered_runs':original_runs,'other_manifest_shapes_not_interpreted':unparsed}
(OUT/'IMPORT-AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'module_count':len(rows),'markers':markers,'original_tree_registered_runs':original_runs},ensure_ascii=False,indent=2))
