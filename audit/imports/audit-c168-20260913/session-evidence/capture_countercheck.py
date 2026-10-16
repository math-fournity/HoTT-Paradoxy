"""Capture the audit countercheck without editing audited source modules."""
from pathlib import Path
import datetime, hashlib, json, os, platform, shutil, subprocess, tempfile
ROOT=Path(__file__).resolve().parents[6]
RUN=ROOT/'HoTT/verification/runs/20260913-AUD-C168-01A09B1E-01'
SOURCE=ROOT/'HoTT/formal/audit-c168-20260913/Countercheck.agda'
def sha(b): return hashlib.sha256(b).hexdigest()
def write(name,obj): (RUN/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
tc_path=ROOT/'HoTT/formal/ercf3-t3/TOOLCHAIN.json'
tc=json.loads(tc_path.read_text()); binary=Path(tc['agda']['local_binary']);cache=tc['runtime_cache']
assert sha(binary.read_bytes())==tc['agda']['binary_sha256']
env=os.environ.copy();env.update(XDG_DATA_HOME=cache['xdg_data_home'],XDG_CONFIG_HOME=cache['xdg_config_home'],TMPDIR=cache['tmpdir'])
deps=['ArithmeticTags','ObjectSyntax','DiagonalCore','CodingRepair','DecodingFence','DiagonalLemma']
files=[SOURCE,tc_path,Path(__file__)]+[ROOT/'HoTT/formal/ercf3-t3'/f'{m}.agda' for m in deps]
rows=[dict(path=str(p.relative_to(ROOT)),bytes=len(p.read_bytes()),sha256=sha(p.read_bytes())) for p in files]
RUN.mkdir(parents=True,exist_ok=False)
started=datetime.datetime.now(datetime.timezone.utc).isoformat()
with tempfile.TemporaryDirectory(prefix='c168-countercheck-') as temp:
    temp=Path(temp)
    for p in files:
        if p.suffix=='.agda':shutil.copy2(p,temp/p.name)
    argv=[str(binary),'--safe','--without-K','--no-libraries','--ignore-interfaces','-i',str(temp),str(temp/SOURCE.name)]
    p=subprocess.run(argv,cwd=temp,env=env,capture_output=True)
    cwd=str(temp)
completed=datetime.datetime.now(datetime.timezone.utc).isoformat()
version=subprocess.check_output([str(binary),'--version'],env=env,text=True)
(RUN/'stdout.txt').write_bytes(p.stdout);(RUN/'stderr.txt').write_bytes(p.stderr)
(RUN/'environment.txt').write_text(f'platform={platform.platform()}\n{version}\noptions=--safe --without-K --no-libraries --ignore-interfaces\ntheory=ordinary intensional Agda; builtins only; no new postulates\n')
write('source-manifest.json',dict(files=rows,agda_binary=dict(path=str(binary),sha256=sha(binary.read_bytes())),
    scope='Countercheck and full local transitive import closure, copied byte-identically to temporary build directory'))
for row in rows:assert sha((ROOT/row['path']).read_bytes())==row['sha256']
receipt=dict(schema_version='formal-proof-run/v1',run_id=RUN.name,proof_id='MP-AUD-C168-20260913',
    claim_ids=['AUD-C168-ONE-20260913','AUD-C168-SURJ-20260913'],command_argv=argv,cwd=cwd,
    started_at_utc=started,completed_at_utc=completed,exit_code=p.returncode,
    proof_assistant='Agda',proof_assistant_version=version.strip(),theory_variant='intensional Agda --safe --without-K; builtins only',
    scope='codeAtom (anum 0) = 1; every Nat has a codeAtom preimage. Exact imported codeAtom from revision 118.',
    non_goals=['No HoTT paradox or inconsistency','No claim about codeT-prime or codeF-prime surjectivity','No automatic correction of historical C-168'],
    status='KERNEL_ACCEPTED_WITH_SCOPE' if p.returncode==0 else 'KERNEL_REJECTED',
    index_status='PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE',git_status='LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED')
for key,name in [('stdout','stdout.txt'),('stderr','stderr.txt'),('environment','environment.txt'),('source_manifest','source-manifest.json')]:
    b=(RUN/name).read_bytes();receipt[key]=dict(path=name,bytes=len(b),sha256=sha(b))
write('RUN.json',receipt)
print(json.dumps(dict(run=str(RUN.relative_to(ROOT)),exit_code=p.returncode,stderr=p.stderr.decode()),ensure_ascii=False))
