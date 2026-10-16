#!/usr/bin/env python3
"""A concrete closed reflection instance for an ALREADY PROVABLE formula."""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import sys

src = Path(__file__).with_name('r031_proof_reflection.py')
spec = importlib.util.spec_from_file_location('r031_primitives', src)
m = importlib.util.module_from_spec(spec); sys.modules[spec.name] = m; spec.loader.exec_module(m)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    if a.out.exists():raise FileExistsError(a.out)
    p=m.atom('P'); truth=m.imp(p,p)
    b=m.Builder()
    hbox=b.add('hyp',formula=m.box(truth))
    hp=b.add('hyp',formula=p)
    ident=b.add('intro',hypothesis=hp,body=hp)
    b.add('intro',hypothesis=hbox,body=ident)
    cert=b.finish(m.imp(m.box(truth),truth))
    checked=m.replay(cert,{})
    assert checked['closed_theorem_parameters']==[]
    out={'schema_version':'r031-positive-reflection/v1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'checker_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'certificate':cert,'replay':checked,
         'scope':'This one provable reflection instance does not certify uniform self-soundness.'}
    a.out.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'accepted':checked['accepted'],'conclusion':checked['conclusion'],
                      'parameters':checked['closed_theorem_parameters'],'nodes':checked['nodes_checked']}))

if __name__=='__main__':main()
