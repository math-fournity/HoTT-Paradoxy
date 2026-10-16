#!/usr/bin/env python3
"""Capture build and smoke evidence for the fixed external Climber checkout."""
from __future__ import annotations
import hashlib,json,subprocess,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent/'runs/20260921-P29-CLIMBER-BUILD-SMOKE-01';EXT=Path('/tmp/climber-p29-6994d29d');LAKE=Path('/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.30.0/bin/lake')
FILES=['README.md','Climber/Object.lean','Climber/Climb.lean','Climber/Reflection.lean','Climber/Counter.lean','Climber/Demo.lean','Climber/Elab.lean','Smoke.lean']
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(label,args):
 t=time.monotonic();p=subprocess.run(args,cwd=EXT,text=True,capture_output=True,check=False);d=time.monotonic()-t;o=OUT/f'{label}-stdout.txt';e=OUT/f'{label}-stderr.txt';o.write_text(p.stdout);e.write_text(p.stderr);return {'argv':args,'exit_code':p.returncode,'duration_seconds':d,'stdout':{'path':o.name,'sha256':h(o),'bytes':o.stat().st_size},'stderr':{'path':e.name,'sha256':h(e),'bytes':e.stat().st_size}}
def main():
 assert LAKE.is_file() and (EXT/'.git').exists();commit=subprocess.run(['git','-C',str(EXT),'rev-parse','HEAD'],text=True,capture_output=True,check=True).stdout.strip();assert commit=='6994d29dda860c3a82de207b1f39ea89526f61c9';
 if OUT.exists():raise RuntimeError(f'exists:{OUT}')
 OUT.mkdir(parents=True);build=run('lake-build',[str(LAKE),'build']);smoke=run('lake-smoke',[str(LAKE),'exe','smoke']);mf=OUT/'source-manifest.json';mf.write_text(json.dumps({'external_commit':commit,'files':{x:h(EXT/x) for x in FILES}},indent=2)+'\n');env=OUT/'environment.txt';env.write_text(f'lake={subprocess.run([str(LAKE),"--version"],text=True,capture_output=True,check=True).stdout}commit={commit}\n')
 out={'schema_version':'p29-climber-build-smoke-run/v1','run_id':'20260921-P29-CLIMBER-BUILD-SMOKE-01','external_commit':commit,'build':build,'smoke':smoke,'source_manifest':{'path':mf.name,'sha256':h(mf)},'environment':{'path':env.name,'sha256':h(env)},'status':'BUILD_AND_SMOKE_ACCEPTED_WITH_SCOPE' if build['exit_code']==0 and smoke['exit_code']==0 else 'UNEXPECTED_RUN_RESULT','scope':'External Lean build and smoke only; no Bedrock cascade, HoTT theorem, global self-validation or defect claim.'};(OUT/'RUN.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2));raise SystemExit(0 if out['status']=='BUILD_AND_SMOKE_ACCEPTED_WITH_SCOPE' else 1)
if __name__=='__main__':main()
