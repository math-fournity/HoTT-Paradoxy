#!/usr/bin/env python3
"""Run an explicitly chosen command and preserve actual stdout/stderr/exit/cwd/argv."""
from pathlib import Path
import argparse, datetime, hashlib, json, os, subprocess, sys, time

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--record',type=Path,required=True);ap.add_argument('--cwd',type=Path,required=True);ap.add_argument('--timeout',type=int,default=120);ap.add_argument('command',nargs=argparse.REMAINDER);a=ap.parse_args()
    cmd=a.command[1:] if a.command and a.command[0]=='--' else a.command
    if not cmd:ap.error('missing command')
    if a.record.exists():raise SystemExit('Refusing overwrite of execution receipt')
    started=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic();timedout=False
    try:
        p=subprocess.run(cmd,cwd=a.cwd,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),text=True,capture_output=True,timeout=a.timeout)
        out,err,code=p.stdout,p.stderr,p.returncode
    except subprocess.TimeoutExpired as e:
        out=e.stdout or '';err=e.stderr or '';out=out.decode(errors='replace') if isinstance(out,bytes) else out;err=err.decode(errors='replace') if isinstance(err,bytes) else err;code=None;timedout=True
    record={'argv':cmd,'cwd':str(a.cwd.resolve()),'started_utc':started,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'duration_seconds':time.monotonic()-t,'exit_code':code,'timeout':timedout,'stdout':out,'stderr':err}
    a.record.parent.mkdir(parents=True,exist_ok=True);a.record.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(out,end='');print(err,end='',file=sys.stderr)
    return code if code is not None else 124
if __name__=='__main__':raise SystemExit(main())
