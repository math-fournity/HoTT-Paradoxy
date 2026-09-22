#!/usr/bin/env python3
"""Capture the P34 same-backend presentation-fiber kernel check."""
from __future__ import annotations
import hashlib,json,os,platform,subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
RUN=ROOT/'HoTT/verification/runs/20260922-MP-ASTRA-PRESENTATION-FIBER-001-01'
AGDA=Path('/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda')
LIB=ROOT/'HoTT/formal/agda-unimath/no-erasure/AGDA_LIBRARIES'
SRC=ROOT/'HoTT/formal/agda-unimath/hott-z/PresentationFiber.agda'

def h(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 RUN.mkdir(parents=True,exist_ok=True)
 env=os.environ.copy();env.update({'XDG_DATA_HOME':'/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/xdg-data','XDG_CONFIG_HOME':'/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/xdg-config','TMPDIR':'/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/tmp'})
 cmd=[str(AGDA),f'--library-file={LIB}','-l','agda-unimath-no-erasure','-i',str(ROOT/'HoTT/formal/agda-unimath'),f'--dependency-graph={RUN/"imports.dot"}',str(SRC.relative_to(ROOT))]
 p=subprocess.run(cmd,cwd=ROOT,env=env,text=True,capture_output=True)
 (RUN/'stdout.txt').write_text(p.stdout);(RUN/'stderr.txt').write_text(p.stderr)
 version=subprocess.run([str(AGDA),'--version'],env=env,text=True,capture_output=True).stdout.strip()
 (RUN/'environment.txt').write_text('\n'.join([f'platform={platform.platform()}',f'agda={version}',f'library_file={LIB}',f'theory_variant=Agda without-K HoTT with explicit foundation postulates; local no-erasure derivative',f'command={json.dumps(cmd,ensure_ascii=False)}'])+'\n')
 direct=[SRC,ROOT/'HoTT/formal/agda-unimath/hott-z/NativeRichCurve.agda',ROOT/'HoTT/formal/agda-unimath/hott-z/NativeRealCircleQualification.agda',LIB]
 manifest={'schema_version':'p34-source-manifest/v1','target':str(SRC.relative_to(ROOT)),'direct_sources':{str(x.relative_to(ROOT)):h(x) for x in direct},'dependency_graph':{'path':'imports.dot','sha256':h(RUN/'imports.dot') if (RUN/'imports.dot').is_file() else None},'agda_binary_sha256':h(AGDA),'library_parent_commit':'7b81411d9f60afec359d29ed1e4edf43f4711c8a'}
 (RUN/'source-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
 run={'schema_version':'formal-proof-run/v1','proof_id':'MP-ASTRA-PRESENTATION-FIBER-001','claim_ids':['C-326'],'run_id':'20260922-MP-ASTRA-PRESENTATION-FIBER-001-01','proof_assistant':'Agda (agda-unimath)','proof_assistant_version':version,'theory_variant':'Agda without-K HoTT with explicit foundation postulates; local agda-unimath no-erasure derivative','command_argv':cmd,'cwd':str(ROOT),'exit_code':p.returncode,'status':'KERNEL_ACCEPTED_WITH_SCOPE' if p.returncode==0 else 'KERNEL_REJECTED','stdout':{'path':'stdout.txt','bytes':len(p.stdout.encode()),'sha256':h(RUN/'stdout.txt')},'stderr':{'path':'stderr.txt','bytes':len(p.stderr.encode()),'sha256':h(RUN/'stderr.txt')},'environment':{'path':'environment.txt','sha256':h(RUN/'environment.txt')},'source_manifest':{'path':'source-manifest.json','sha256':h(RUN/'source-manifest.json')},'scope':'PresentationFiber over Bare:RichCurve→Type; transportedRich and nRich lie over OpenRealInterval, are distinguished by endpoint closure, and no fiber path exists. It does not establish a HoTT defect, actual K, full OriginDirectedDiagram, physical provenance, or a general R_origin theorem.','non_goals':['No claim that the presentation fiber is a full original circle/process model.','No actual consumer/K_app or K_theory bridge.','No basic HoTT inconsistency or implementation discrepancy.']}
 (RUN/'RUN.json').write_text(json.dumps(run,ensure_ascii=False,indent=2)+'\n');print(json.dumps(run,ensure_ascii=False,indent=2));raise SystemExit(p.returncode)
if __name__=='__main__':main()
