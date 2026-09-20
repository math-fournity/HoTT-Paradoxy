#!/usr/bin/env python3
"""Fetch a fixed public mathlib source archive onto D; not a theorem replay."""
import datetime as dt,hashlib,json,os,shutil,subprocess,tarfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
REV='5ed2965256430c3649e86755f9576b54eca72435'

def main():
    pre=json.loads((OUT/'download-preflight.json').read_text());mount=Path(pre['mount']);base=Path(pre['destination'])
    assert os.path.ismount(mount) and os.stat(base).st_dev==pre['device']
    archive=base/('mathlib4-'+REV+'.tar.gz');control=Path(str(archive)+'.aria2')
    if archive.exists() and not control.exists():raise SystemExit('EXISTING_FILE_REQUIRES_PRIOR_RECEIPT_CHECK')
    assert shutil.disk_usage(base).free>1024**3
    cmd=[pre['aria2c'],'--no-conf=true','--no-netrc=true','--max-concurrent-downloads=1','--split=1','--max-connection-per-server=1','--piece-length=1M','--min-split-size=1M','--continue=true','--auto-file-renaming=false','--allow-overwrite=false','--file-allocation=none','--auto-save-interval=10','--max-tries=5','--retry-wait=5','--connect-timeout=20','--timeout=60','--check-certificate=true','--header=Accept-Encoding: identity','--dir='+str(base),'--out='+archive.name,'--log='+str(base/'aria2.log')]
    etag=pre['range_probe'].get('etag')
    if etag and not etag.startswith('W/'):cmd+=['--header=If-Match: '+etag]
    cmd+=[pre['range_probe']['url']]
    (OUT/'download-command.json').write_text(json.dumps(cmd,ensure_ascii=False,indent=2)+'\n')
    env=os.environ.copy();env['TMPDIR']=str(base)
    started=dt.datetime.now(dt.timezone.utc).isoformat()
    with (base/'stdout.txt').open('wb') as so,(base/'stderr.txt').open('wb') as se:
        process=subprocess.Popen(cmd,cwd=base,env=env,stdout=so,stderr=se)
        (OUT/'DOWNLOAD-START.json').write_text(json.dumps({'pid':process.pid,'started':started,'command':cmd,'destination':str(base)},ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'state':'RUNNING','pid':process.pid,'destination':str(base)}),flush=True)
        rc=process.wait()
    for name in ('stdout.txt','stderr.txt','aria2.log'):
        if (base/name).exists():shutil.copy2(base/name,OUT/('download-'+name))
    assert rc==0,('ARIA2_EXIT',rc)
    assert os.path.ismount(mount) and os.stat(base).st_dev==pre['device']
    gzip=subprocess.run(['gzip','-t',str(archive)],capture_output=True);assert gzip.returncode==0,gzip.stderr
    source=base/('mathlib4-'+REV);assert not source.exists()
    with tarfile.open(archive) as tf:
        members=tf.getmembers();assert all(not Path(m.name).is_absolute() and '..' not in Path(m.name).parts and Path(m.name).parts[0]==source.name for m in members)
        expanded=sum(m.size for m in members if m.isfile());assert shutil.disk_usage(base).free>expanded+1024**3
        tf.extractall(base,filter='data')
    expected=json.loads((OUT/'SOURCE.json').read_text())['sources']
    parity=[]
    for row in expected:
        p=source/row['source_path'];actual=hashlib.sha256(p.read_bytes()).hexdigest();assert actual==row['sha256'];parity.append({'path':row['source_path'],'sha256':actual})
    result={'status':'SOURCE_ARCHIVE_DOWNLOADED_AND_EXTRACTED','started':started,'completed':dt.datetime.now(dt.timezone.utc).isoformat(),'exit_code':rc,'archive':str(archive),'archive_bytes':archive.stat().st_size,'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'source_root':str(source),'members':len(members),'expanded_file_bytes':expanded,'pinned_source_parity':parity,'transfer_slots':1,'range_response':pre['range_probe']['status'],'no_claim':'Archive integrity/source parity only. No mathlib dependency cache installed, no theorem replay, no HoTT translation.'}
    (OUT/'DOWNLOAD.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
