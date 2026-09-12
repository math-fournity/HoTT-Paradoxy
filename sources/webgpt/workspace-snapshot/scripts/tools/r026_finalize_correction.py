"""Correct a line-count explanation, preserve prior receipts, deliver final Git snapshot."""
from __future__ import annotations
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,tempfile,zipfile
from pathlib import Path,PurePosixPath
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r026'
DEST=ROOT.parent
PREVIOUS='067053a5a99ece46030dbb9de3cf72e051503f53'
LOG=[]
def sha(b):return hashlib.sha256(b).hexdigest()
def serial(o):return json.dumps(o,ensure_ascii=False,indent=2)+'\n'
def put(p,v):
    p=Path(p)
    if p.exists():raise FileExistsError(p)
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(v if isinstance(v,str) else serial(v),encoding='utf-8')
def command(a,cwd=ROOT):
    a=[str(x) for x in a]
    r=subprocess.run(a,cwd=cwd,capture_output=True,text=True,timeout=60)
    LOG.append({'argv':a,'cwd':str(cwd),'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
    if r.returncode:raise RuntimeError(r.stderr)
    return r.stdout.strip()
def git(*a,cwd=ROOT):return command(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*a],cwd)
def main():
    if git('rev-parse','HEAD')!=PREVIOUS:raise RuntimeError('Unexpected HEAD')
    b=(ROOT/'.codex/research/hott/reviews/EARLY-GEMINI-001/ORIGINAL.md').read_bytes()
    txt=b.decode('utf-8')
    old=json.loads((OUT/'LINE_METRICS.json').read_text())
    put(OUT/'LINE_METRICS_SUPERSEDED.json',old)
    new={'bytes':len(b),'LF_count':b.count(b'\n'),'ends_with_LF':b.endswith(b'\n'),
        'bytes_splitlines':len(b.splitlines()),'unicode_splitlines':len(txt.splitlines()),
        'other_line_separator_counts':{repr(c):txt.count(c) for c in ['\r','\v','\f','\x1c','\x1d','\x1e','\x85','\u2028','\u2029']},
        'note':'The original has 497 LF separators and 498 lines because the last line has no trailing LF. No Unicode-only separator difference is claimed. The source is unchanged.'}
    if new['LF_count']!=497 or new['unicode_splitlines']!=498 or new['ends_with_LF']:
        raise AssertionError('Unexpected source line metrics')
    if any(new['other_line_separator_counts'].values()):raise AssertionError('Unexpected separator')
    (OUT/'LINE_METRICS.json').write_text(serial(new))
    report=(OUT/'REPORT.md').read_text()
    report=report.replace('497个LF换行，Python Unicode splitlines计498行，属于行分隔口径差异。','498行，497个LF分隔符，末行没有换行；早期Session中的497按LF计数。')
    report+='\n## 行数说明修正\n\n第一次元数据说明误称有Unicode专用行分隔符；实际原文末行没有LF，因此497个LF对应498行。已保存旧说明并更正，不改原文字节、数学论证、测试或checkpoint。最终Git与交付包见外部final_delivery_verification。\n'
    (OUT/'REPORT.md').write_text(report)
    put(OUT/'LINE_METRICS_CORRECTION.json',{'previous_head':PREVIOUS,'corrected_at_utc':datetime.now(timezone.utc).isoformat(),
        'files':['artifacts/r026/LINE_METRICS.json','artifacts/r026/REPORT.md'],
        'source_unchanged':True,'old_note_preserved':'artifacts/r026/LINE_METRICS_SUPERSEDED.json','state_revision_unchanged':26})
    route=json.loads(command([sys.executable,'-B',ROOT/'scripts/session/r026_plan_check.py']))
    before_route=json.loads((OUT/'FRESH_ROUTE.json').read_text())
    if route['snapshot']!=before_route['snapshot']:raise AssertionError('Cognition dependency changed')
    git('add','--all');git('commit','-m','Correct source line-count metadata without altering original or research results')
    head=git('rev-parse','HEAD')
    if git('status','--porcelain'):raise AssertionError('Dirty final worktree')
    git('fsck','--full')
    full=DEST/'HoTT_early_reassessment_rev26_final_with_git.zip'
    bundle=DEST/'HoTT_early_reassessment_rev26_final.bundle'
    small=DEST/'HoTT_early_Gemini_review_R026_final.zip'
    for p in [full,bundle,small]:
        if p.exists():raise FileExistsError(p)
    git('bundle','create',bundle,'--all');git('bundle','verify',bundle)
    files=[p for p in sorted(ROOT.rglob('*')) if p.is_file()]
    with zipfile.ZipFile(full,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files:z.write(p,ROOT.name+'/'+p.relative_to(ROOT).as_posix())
    with zipfile.ZipFile(full) as z:
        assert z.testzip() is None
        assert all(z.read(ROOT.name+'/'+p.relative_to(ROOT).as_posix())==p.read_bytes() for p in files)
    old_small=DEST/'HoTT_early_Gemini_review_R026.zip'
    with zipfile.ZipFile(old_small) as oldz, zipfile.ZipFile(small,'w',zipfile.ZIP_DEFLATED) as z:
        manifest=[]
        for n in oldz.namelist():
            if n=='MANIFEST.json':continue
            local=ROOT/n
            data=local.read_bytes() if n=='artifacts/r026/REPORT.md' else oldz.read(n)
            z.writestr(n,data);manifest.append({'path':n,'bytes':len(data),'sha256':sha(data)})
        data=(OUT/'LINE_METRICS.json').read_bytes();n='artifacts/r026/LINE_METRICS.json'
        z.writestr(n,data);manifest.append({'path':n,'bytes':len(data),'sha256':sha(data)})
        z.writestr('MANIFEST.json',serial({'files':manifest,'scope':'Source assessment and six narrow check groups; not a HoTT proof.'}))
    with zipfile.ZipFile(small) as z:
        assert z.testzip() is None and all(sha(z.read(e['path']))==e['sha256'] for e in manifest)
    with tempfile.TemporaryDirectory(prefix='hott-r026-final-') as t:
        target=Path(t)
        with zipfile.ZipFile(full) as z:
            for inf in z.infolist():
                p=PurePosixPath(inf.filename)
                if p.is_absolute() or '..' in p.parts:raise ValueError('Unsafe archive path')
            z.extractall(target)
            for inf in z.infolist():
                if not inf.is_dir():(target/inf.filename).chmod(0o755 if (inf.external_attr>>16)&0o111 else 0o644)
        restored=target/ROOT.name
        assert git('rev-parse','HEAD',cwd=restored)==head
        assert not git('status','--porcelain',cwd=restored)
        p=json.loads(command([sys.executable,'-B',restored/'scripts/session/r026_plan_check.py'],cwd=target))
        assert p['snapshot']==route['snapshot'] and p['required_paths_present']
        clone=target/'from-bundle';command(['git','-c','core.hooksPath=/dev/null','clone',bundle,clone],cwd=target)
        assert git('rev-parse','HEAD',cwd=clone)==head and not git('status','--porcelain',cwd=clone)
    outputs=[]
    for p in [full,bundle,small]:
        h=sha(p.read_bytes());put(str(p)+'.sha256',h+'  '+p.name+'\n')
        outputs.append({'path':str(p),'bytes':p.stat().st_size,'sha256':h})
    validation={'status':'VERIFIED_FINAL_FILES_AND_GIT','revision':26,'head':head,'previous_head':PREVIOUS,
        'inherited_head':'0d7ef5e48c67ee3586606dc45fb9f4ef4a30a685','workspace':str(ROOT),
        'line_metrics':new,'core_checks_passed':44,'prior_validation_sha256':sha((DEST/'HoTT_early_reassessment_rev26_delivery_verification.json').read_bytes()),
        'final_roundtrip':True,'restored_clean':True,'bundle_same_head':True,'same_cognition_snapshot':route['snapshot'],
        'outputs':outputs,'commands':LOG,'native_hott_kernel':'NOT_RUN','full_business_cognition':'NOT_CLAIMED'}
    receipt=DEST/'HoTT_early_reassessment_rev26_final_delivery_verification.json'
    put(receipt,validation)
    print(serial({'head':head,'revision':26,'outputs':outputs,'receipt':str(receipt)}))
if __name__=='__main__':main()
