"""One-audit derived receipts; never writes project owners or historical inputs.

This is an audit artifact writer, not a canonical project registry/manager.
Commands run without a shell. Each label is append-once and stores raw bytes.
"""
from __future__ import annotations
import argparse, datetime, hashlib, json, pathlib, subprocess, time

ROOT = pathlib.Path('/Volumes/D/HoTT_AI_HANDOFF_20260911')
OUT = pathlib.Path(__file__).resolve().parent

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write_json(path, value):
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n')

def capture(label, cwd, command, timeout=1200):
    dest=OUT/'commands'/label
    dest.mkdir(parents=True, exist_ok=False)
    started=now(); clock=time.monotonic()
    try:
        result=subprocess.run(command,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout)
        stdout,stderr,code,status=result.stdout,result.stderr,result.returncode,'COMPLETED'
    except subprocess.TimeoutExpired as exc:
        stdout,stderr,code,status=exc.stdout or b'',exc.stderr or b'',None,'OBSERVATION_TIMEOUT'
    (dest/'stdout.txt').write_bytes(stdout)
    (dest/'stderr.txt').write_bytes(stderr)
    receipt=dict(label=label,cwd=str(cwd),command=command,started_at=started,ended_at=now(),wall_seconds=time.monotonic()-clock,exit_code=code,status=status,stdout_sha256=sha(stdout),stderr_sha256=sha(stderr))
    write_json(dest/'RUN.json',receipt)
    return receipt

def snapshot(label):
    dest=OUT/'snapshots'/label
    dest.mkdir(parents=True,exist_ok=False)
    roots=[ROOT,pathlib.Path('/Volumes/D/HoTT-machine-overview'),pathlib.Path('/Volumes/D/HoTT-semantic-overview'),pathlib.Path('/Volumes/D/ALL-Markdown'),ROOT/'workspace',ROOT/'AI对话录',pathlib.Path('/Users/aurolafly/.codex/worktrees/eb7b/HoTT_AI_HANDOFF_20260911'),pathlib.Path('/Volumes/D/HoTT独立答复')]
    root_rows=[]
    for i,root in enumerate(roots):
        row={'root':str(root),'exists':root.exists()}
        if root.exists():
            for key,args in [('identity',['rev-parse','--show-toplevel','--git-common-dir','HEAD']),('branch',['branch','--show-current']),('status',['status','--porcelain=v1','-uall']),('index',['diff','--cached','--name-status']),('tags',['tag','--points-at','HEAD'])]:
                p=subprocess.run(['git','-C',str(root),*args],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                (dest/f'root-{i}-{key}.txt').write_bytes(p.stdout+p.stderr)
                row[key]={'exit':p.returncode,'sha256':sha(p.stdout),'bytes':len(p.stdout),'lines':len(p.stdout.splitlines())}
        root_rows.append(row)
    write_json(dest/'roots.json',{'observed_at':now(),'roots':root_rows})
    files=[]
    selected=['goal.md','AGENTS.md','README.md','MEMORY.md','feature-list.md','rulings.md','核心认知.md','核心认知.manifest.json','方向追踪.md','全景视野.md','从抽象到悖论——HoTT研究的核心问题意识与思想展开.md','GLM的回应','GPT的方案','GPT的回应','GLM的建议方案','GLM独立审计','dev-notes','方向追踪','全景视野','从抽象到悖论——HoTT研究的核心问题意识与思想展开','README','MEMORY','.codex/cognition/HEAD.json','.codex/cognition/LOAD_SET.json','.codex/cognition/PROTOCOL.md','.codex/research/hott/STATE.json','.codex/research/hott/R4-HOTT-NAT-EFFECTIVITY-001.md','.codex/research/hott/FRONTIER.md','.codex/research/hott/RESUME.md','.codex/research/hott/LESSONS.md','HoTT/verification/PROOF_VERSION_CLOSURE.json','HoTT/CLAIM_EVIDENCE_MATRIX.md']
    for name in selected:
        path=ROOT/name
        paths=sorted(path.rglob('*')) if path.is_dir() else [path]
        for p in paths:
            if p.is_file():
                data=p.read_bytes(); stat=p.stat()
                files.append({'path':str(p.relative_to(ROOT)),'bytes':len(data),'lines':len(data.splitlines()),'sha256':sha(data),'mtime_ns':stat.st_mtime_ns})
    write_json(dest/'files.json',{'observed_at':now(),'files':files,'count':len(files),'role':'DERIVED_AUDIT_INPUT_SNAPSHOT_NOT_PROJECT_CURRENT_TRUTH'})
    for p in ['goal.md','.codex/research/hott/R4-HOTT-NAT-EFFECTIVITY-001.md','.codex/research/hott/STATE.json']:
        d=dest/'input-copies'/p; d.parent.mkdir(parents=True,exist_ok=True); d.write_bytes((ROOT/p).read_bytes())
    return {'label':label,'files':len(files),'roots':len(root_rows)}

def main():
    parser=argparse.ArgumentParser(); sub=parser.add_subparsers(dest='op',required=True)
    snap=sub.add_parser('snapshot'); snap.add_argument('label')
    run=sub.add_parser('run'); run.add_argument('label'); run.add_argument('--cwd',default=str(ROOT)); run.add_argument('--timeout',type=int,default=1200); run.add_argument('command',nargs=argparse.REMAINDER)
    args=parser.parse_args()
    if args.op=='snapshot': result=snapshot(args.label)
    else:
        command=args.command
        if command and command[0]=='--': command=command[1:]
        result=capture(args.label,args.cwd,command,args.timeout)
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__': main()
