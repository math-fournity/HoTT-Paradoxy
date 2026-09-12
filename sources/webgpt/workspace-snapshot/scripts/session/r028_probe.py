"""One bounded native-tool check; record facts, never synthesize expected diagnostics."""
from pathlib import Path
import hashlib, json, shutil, subprocess, urllib.request, datetime
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r028'
def main():
    tools={x:shutil.which(x) for x in ['lean','lake','elan','coqc','rocq','agda','ocamlc']}
    extra=[Path('/opt/lean/bin/lean'),Path('/root/.elan/bin/lean'),Path('/home/oai/.elan/bin/lean')]
    existing=[str(p) for p in extra if p.is_file()]
    versions={}
    for k,p in tools.items():
        if p:
            try:
                r=subprocess.run([p,'--version'],capture_output=True,text=True,timeout=8)
                versions[k]={'argv':[p,'--version'],'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
            except Exception as e: versions[k]={'error':repr(e)}
    network={}
    url='https://releases.lean-lang.org/lean4/v4.19.0/lean-4.19.0-linux.tar.zst'
    if not tools['lean'] and not existing:
        try:
            req=urllib.request.Request(url,method='HEAD')
            with urllib.request.urlopen(req,timeout=8) as r:
                network={'url':url,'status':r.status,'resolved_url':r.url,'content_length':r.headers.get('Content-Length')}
        except Exception as e: network={'url':url,'error':repr(e),'downloaded':False}
    result={'time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tools':tools,'additional_standard_paths_found':existing,
            'versions':versions,'one_official_release_probe':network,
            'scope':'PATH and listed standard paths; not an exhaustive filesystem search; prior NOT_RUN records retained',
            'native_execution_status':'AVAILABLE' if tools['lean'] or existing or tools['coqc'] or tools['rocq'] else 'NOT_RUN_NO_TOOLCHAIN',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    p=OUT/'NATIVE_AVAILABILITY.json'
    if p.exists(): raise FileExistsError(p)
    p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
