#!/usr/bin/env python3
"""Archive explicitly selected primary sources; preserve failed downloads honestly."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,urllib.request
ROOT=Path(__file__).resolve().parents[2];D=ROOT/'artifacts/r039/sources'
SOURCES=[
 ('leroy_partiality.html','https://xavierleroy.org/cdf-mech-sem/CDF.Partiality.html'),
 ('partiality_revisited_abstract.html','https://arxiv.org/abs/1610.09254'),
 ('explicit_divergence_abstract.html','https://arxiv.org/abs/0812.3068'),
]
def main():
 D.mkdir(parents=True,exist_ok=True);records=[]
 for name,url in SOURCES:
  p=D/name
  if p.exists():raise FileExistsError(p)
  r=dict(name=name,url=url,attempted_utc=datetime.now(timezone.utc).isoformat())
  try:
   with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'HoTT-research-source-audit/1.0'}),timeout=12) as f:data=f.read();r.update(final_url=f.geturl(),http_status=f.status)
   p.write_bytes(data);r.update(status='DOWNLOADED',bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  except Exception as e:r.update(status='FAILED',error=repr(e))
  records.append(r)
 out=D/'FETCH_RECEIPT.json'
 if out.exists():raise FileExistsError(out)
 out.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n');print(out.read_text())
if __name__=='__main__':main()
