#!/usr/bin/env python3
"""Show an exact full-line source segment, logging emission rather than claiming understanding."""
from pathlib import Path
import argparse,hashlib,json
root=Path(__file__).resolve().parents[2]
a=argparse.ArgumentParser();a.add_argument('path');a.add_argument('--start',type=int,default=1);a.add_argument('--chars',type=int,default=6500);x=a.parse_args()
p=(root/x.path).resolve();p.relative_to(root)
ls=p.read_text().splitlines(keepends=True);out=[];end=x.start-1
for i in range(x.start-1,len(ls)):
 if out and sum(map(len,out))+len(ls[i])>x.chars:break
 out.append(ls[i]);end=i+1
body=''.join(out)
print(f'SOURCE {x.path} L{x.start}-{end}/{len(ls)}\n'+body+f'\nNEXT_LINE {end+1 if end<len(ls) else "EOF"}')
d=root/'artifacts/cognition/emitted';d.mkdir(parents=True,exist_ok=True)
id=hashlib.sha256(x.path.encode()).hexdigest()[:12]
(d/f'{id}-{x.start}-{end}.json').write_text(json.dumps({'path':x.path,'start':x.start,'end':end,'total_lines':len(ls),'file_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'emitted_sha256':hashlib.sha256(body.encode()).hexdigest(),'model_reception':'NOT_CERTIFIED'},ensure_ascii=False,indent=2)+'\n')
