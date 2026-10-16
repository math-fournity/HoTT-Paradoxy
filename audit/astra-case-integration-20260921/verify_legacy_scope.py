#!/usr/bin/env python3
"""Qualify the unchanged legacy B1a entry after editorial history classification."""
from pathlib import Path
import json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
checks=[]
for label,args in [('formal',['scripts/audit/verify_formal_proof_run.py','--run-dir','HoTT/verification/runs/20260919-MP-DEDEKIND-OMEGA-REAL-LAYER-04']),('relation',['scripts/audit/verify_proof_version_closure.py','--evidence-only','--proof-id','MP-DEDEKIND-OMEGA-REAL-LAYER'])]:
 p=subprocess.run(['python3','-B',*args],cwd=ROOT,capture_output=True)
 (OUT/('legacy-real-layer.'+label+'.stdout.json')).write_bytes(p.stdout);(OUT/('legacy-real-layer.'+label+'.stderr.txt')).write_bytes(p.stderr)
 assert p.returncode==0,p.stdout.decode()+p.stderr.decode();checks.append({'argv':args,'exit':p.returncode})
(OUT/'LEGACY-REAL-LAYER-QUALIFICATION.json').write_text(json.dumps({'status':'UNCHANGED_B1A_EVIDENCE_RELATION_PASS','checks':checks,'scope':'Conditional SingleOmega sufficiency only; frozen legacy row remains byte-identical. Historical charging interpretations are not certified.'},ensure_ascii=False,indent=2)+'\n')
print('UNCHANGED_B1A_EVIDENCE_RELATION_PASS')
