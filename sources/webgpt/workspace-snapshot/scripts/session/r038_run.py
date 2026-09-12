#!/usr/bin/env python3
"""Run saved files and retain exact command, source hashes, output, cwd, timestamps."""
from pathlib import Path
from datetime import datetime,timezone
import sys,subprocess,json,hashlib,argparse,os
ROOT=Path(__file__).resolve().parents[2]
def main():
 p=argparse.ArgumentParser();p.add_argument('label');p.add_argument('argv',nargs=argparse.REMAINDER);a=p.parse_args()
 argv=a.argv[1:] if a.argv and a.argv[0]=='--' else a.argv
 if not argv:raise ValueError('argv required')
 dest=ROOT/'artifacts/r038'/f'{a.label}.json'
 if dest.exists():raise FileExistsError(dest)
 def now():return datetime.now(timezone.utc).isoformat()
 before=now();env=os.environ.copy();env['PYTHONDONTWRITEBYTECODE']='1'
 try:
  r=subprocess.run(argv,cwd=ROOT,env=env,capture_output=True,text=True,timeout=120)
  data=dict(argv=argv,cwd=str(ROOT),started_utc=before,ended_utc=now(),exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr,timed_out=False)
 except subprocess.TimeoutExpired as e:
  data=dict(argv=argv,cwd=str(ROOT),started_utc=before,ended_utc=now(),exit_code=None,stdout=str(e.stdout),stderr=str(e.stderr),timed_out=True,result='UNKNOWN_NOT_NONTERMINATION_PROOF')
 data['source_hashes']={x:hashlib.sha256((ROOT/x).read_bytes()).hexdigest() for x in argv if (ROOT/x).is_file()}
 dest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n');print(json.dumps(data,ensure_ascii=False,indent=2))
 if data['exit_code']!=0:sys.exit(1)
if __name__=='__main__':main()
