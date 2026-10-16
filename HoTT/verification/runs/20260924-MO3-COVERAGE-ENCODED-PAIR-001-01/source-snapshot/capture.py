#!/usr/bin/env python3
"""Capture this without-K fragment honestly; the shared Cubical capturer
hardcodes Path/HIT environment text and is not suitable for this experiment.
No existing run or toolchain configuration is changed.
"""
from pathlib import Path
import datetime as dt, hashlib, json, os, platform, shutil, subprocess, sys, tempfile
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
PROOF='MP-MO3-COVERAGE-ENCODED-PAIR-001'
def sha(b):return hashlib.sha256(b).hexdigest()
def dump(x):return (json.dumps(x,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
def row(p):
 b=p.read_bytes();return {'bytes':len(b),'sha256':sha(b)}
def main():
 run_id,source_name=sys.argv[1:]
 assert run_id.startswith('20260924-MO3-COVERAGE-ENCODED-PAIR-') and '/' not in run_id
 assert source_name in ('EncodedPair.agda','WrongJudgmental.agda')
 run_dir=ROOT/'HoTT/verification/runs'/run_id;assert not run_dir.exists()
 original=json.loads((ROOT/'HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json').read_text())
 agda=original['agda'];binary=Path(agda['local_binary'])
 assert row(binary)=={'bytes':agda['binary_bytes'],'sha256':agda['binary_sha256']}
 old_data=Path(original['runtime_cache']['xdg_data_home'])/'agda'/agda['version']
 cache=Path(tempfile.mkdtemp(prefix='mo3-coverage-encoded-pair-'))
 data=cache/'data'/'agda'/agda['version']
 shutil.copytree(old_data,data,ignore=shutil.ignore_patterns('*.agdai'))
 (cache/'config').mkdir();(cache/'tmp').mkdir()
 command=['/usr/bin/env',f'XDG_DATA_HOME={cache / "data"}',f'XDG_CONFIG_HOME={cache / "config"}',f'TMPDIR={cache / "tmp"}',str(binary),'--no-libraries','--ignore-interfaces','-i',str(HERE),str((HERE/source_name).relative_to(ROOT))]
 version=subprocess.run(command[:5]+['--version'],cwd=ROOT,capture_output=True,check=True)
 probe=subprocess.run(command[:5]+['--print-agda-dir'],cwd=ROOT,capture_output=True,check=True)
 assert Path(probe.stdout.decode().strip())==data
 local=[HERE/source_name,HERE/'EncodedPair.agda',Path(__file__)]
 local=list(dict.fromkeys(local))
 files=[{'path':str(p.relative_to(ROOT)),**row(p)} for p in local]
 external=[{'label':'agda-binary','local_path':str(binary),**row(binary)}]
 external += [{'label':'agda-builtin:'+str(p.relative_to(data)),'local_path':str(p),**row(p)} for p in sorted(data.rglob('*.agda'))]
 started=dt.datetime.now(dt.timezone.utc)
 result=subprocess.run(command,cwd=ROOT,capture_output=True)
 ended=dt.datetime.now(dt.timezone.utc)
 assert all(row(ROOT/r['path'])=={k:r[k] for k in ('bytes','sha256')} for r in files)
 manifest={'schema_version':'formal-proof-source-manifest/v1','proof_id':PROOF,'run_id':run_id,'files':files,'external_dependencies':external}
 env=('platform='+platform.platform()+'\n'+version.stdout.decode()+'\ntheory_variant=Agda 2.8.0 without-K exact-split safe; native intensional identity; explicit function-extensionality and identity-law parameters; no Cubical Path or univalence claimed\n'+'builtin_data='+str(data)+'\ncache_policy=fresh copied data, fresh XDG config/temp, no global configuration writes\n').encode()
 contents={'stdout.txt':result.stdout,'stderr.txt':result.stderr,'environment.txt':env,'source-manifest.json':dump(manifest)}
 run={'schema_version':'formal-proof-run/v1','run_id':run_id,'proof_id':PROOF,'claim_ids':['C-342','C-343'],'proof_assistant':'Agda','proof_assistant_version':agda['version'],'theory_variant':'Agda without-K exact-split safe intensional identity fragment, explicit extensionality/identity-law hypotheses','command_argv':command,'cwd':str(ROOT),'started_at_utc':started.isoformat(),'completed_at_utc':ended.isoformat(),'duration_seconds':(ended-started).total_seconds(),'exit_code':result.returncode,'status':'KERNEL_ACCEPTED_WITH_SCOPE' if result.returncode==0 else 'KERNEL_REJECTED','scope':'Conditional dependent beta for the specified Bool→Nat pair encoding; primitive-pair and projection controls. WrongJudgmental is an expected rejection, not a theorem of general non-reducibility.','non_goals':['No full Book-to-Agda translation','No univalence, Cubical Path, HIT or physical claim','No general impossibility, divergence or global HoTT paradox','No proof that the explicit extensionality assumptions have a model'],'index_status':'PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE','git_status':'LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED'}
 for k,n in [('stdout','stdout.txt'),('stderr','stderr.txt'),('environment','environment.txt'),('source_manifest','source-manifest.json')]:run[k]={'path':n,'bytes':len(contents[n]),'sha256':sha(contents[n])}
 run_dir.mkdir(parents=True,exist_ok=False)
 for name,b in {**contents,'RUN.json':dump(run)}.items():
  with (run_dir/name).open('xb') as f:f.write(b)
 for p in local:
  dst=run_dir/'source-snapshot'/p.name;dst.parent.mkdir(exist_ok=True)
  with dst.open('xb') as f:f.write(p.read_bytes())
 print(json.dumps({'run':str(run_dir.relative_to(ROOT)),'status':run['status'],'exit_code':result.returncode,'cache':str(cache)},ensure_ascii=False))
 print(result.stdout.decode());print(result.stderr.decode())
 return result.returncode
if __name__=='__main__':raise SystemExit(main())
