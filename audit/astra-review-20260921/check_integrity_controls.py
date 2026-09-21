#!/usr/bin/env python3
"""Check that incomplete inputs and wrong compiler bytes fail before Agda runs."""
from pathlib import Path
import json,shutil,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
rel=json.loads((OUT/'EXTRACT.json').read_text());bundle=Path(rel['bundle']);agda=Path(rel['compiler']);base=bundle.parent/'integrity controls';assert not base.exists();base.mkdir()
copy=base/'missing source';shutil.copytree(bundle,copy)
target=copy/'sources/HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda';assert target.exists();target.unlink()
specs=[('missing-source',copy,agda,'INPUT_MISMATCH:'),('wrong-compiler',bundle,Path('/usr/bin/true'),'COMPILER_HASH_MISMATCH')]
results=[]
for key,src,tool,diagnostic in specs:
    dest=base/(key+' results');argv=['python3','-B',str(src/'tools/replay.py'),'--agda',str(tool),'--out',str(dest),'--case','geometry']
    p=subprocess.run(argv,cwd='/Volumes/D',capture_output=True)
    (OUT/(key+'.stdout.txt')).write_bytes(p.stdout);(OUT/(key+'.stderr.txt')).write_bytes(p.stderr)
    passed=p.returncode!=0 and diagnostic.encode() in p.stderr and not dest.exists()
    results.append({'case':key,'argv':argv,'exit':p.returncode,'expected_diagnostic':diagnostic,'rejected_before_output_or_Agda':not dest.exists(),'pass':passed})
assert all(r['pass'] for r in results)
(OUT/'INTEGRITY-CONTROLS.json').write_text(json.dumps({'status':'TWO_PRECHECK_CONTROLS_PASS','results':results,'scope':'Missing one frozen proof file and a wrong compiler are rejected before any formal check. This is integrity validation, not a mathematical no-go result.'},ensure_ascii=False,indent=2)+'\n');print(json.dumps({'status':'TWO_PRECHECK_CONTROLS_PASS'}))
