"""Bounded, logged probe; does not install packages or run untrusted project code."""
from pathlib import Path
import datetime, hashlib, json, shutil, subprocess, urllib.request
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r027'; OUT.mkdir(parents=True,exist_ok=True)
def main():
    records=[]
    for name in ['lean','lake','elan','agda','coqc','rocq','ocamlc','apt-cache','node']:
        path=shutil.which(name); row={'tool':name,'path':path}
        if path and name in ['lean','coqc','ocamlc','node']:
            p=subprocess.run([path,'--version'] if name!='ocamlc' else [path,'-version'],capture_output=True,text=True,timeout=10)
            row.update(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
        records.append(row)
    urls=['https://raw.githubusercontent.com/leanprover/lean4/v4.19.0/README.md','https://github.com/leanprover/lean4/releases/download/v4.19.0/lean-4.19.0-linux.tar.zst']
    net=[]
    for url in urls:
        row={'url':url,'at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
        try:
            req=urllib.request.Request(url,method='HEAD',headers={'User-Agent':'HoTT-R027-audit'})
            with urllib.request.urlopen(req,timeout=12) as r:
                row.update(status=r.status,headers=dict(r.headers),final_url=r.url)
        except Exception as e: row.update(error=type(e).__name__,message=str(e))
        net.append(row)
    result={'tools':records,'network_probes':net,'native_executed':False,'scope':'Local tools and two official URLs only; no installation'}
    (OUT/'TOOLCHAIN_PROBE.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
