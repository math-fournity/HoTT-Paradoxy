"""Run saved source files; keep stdout/stderr/exit status and explicit native skips."""
from pathlib import Path
import datetime, hashlib, json, shutil, subprocess, sys, time
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'artifacts/r027'
def record(argv,timeout=30):
    t=time.perf_counter(); start=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        p=subprocess.run(argv,cwd=ROOT,capture_output=True,text=True,timeout=timeout)
        return {'argv':argv,'cwd':str(ROOT),'started_utc':start,'duration_seconds':time.perf_counter()-t,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'timeout':False}
    except subprocess.TimeoutExpired as e:
        return {'argv':argv,'cwd':str(ROOT),'started_utc':start,'duration_seconds':time.perf_counter()-t,'exit_code':None,'stdout':str(e.stdout or ''),'stderr':str(e.stderr or ''),'timeout':True,'mathematical_nontermination':'NOT_INFERRED'}
def main():
    call=record([sys.executable,'-B','scripts/research/r027_fixedpoint_lemma_audit.py'])
    (OUT/'FINITE_EXECUTION.json').write_text(json.dumps(call,ensure_ascii=False,indent=2)+'\n')
    if call['exit_code']!=0: raise RuntimeError('Finite audit failed; see receipt')
    native=[]
    lean=shutil.which('lean')
    if lean:
        native.append(record([lean,'--version']))
        for p in sorted((ROOT/'scripts/research/r027_lean').glob('*.lean')):
            r=record([lean,str(p)])
            r['source_sha256']=hashlib.sha256(p.read_bytes()).hexdigest(); native.append(r)
    else: native.append({'tool':'lean','status':'NOT_RUN_TOOL_UNAVAILABLE','not_replaced_by_python_simulator':True})
    coqc=shutil.which('coqc')
    if coqc:
        native.append(record([coqc,'--version']))
        native.append(record([coqc,'-q','scripts/research/r027_coq/OracleExtraction.v']))
    else: native.append({'tool':'coqc','status':'NOT_RUN_TOOL_UNAVAILABLE','not_replaced_by_python_simulator':True})
    (OUT/'NATIVE_RUN.json').write_text(json.dumps({'records':native,'native_HoTT':'NOT_RUN; ordinary Lean/Rocq only if installed','source_status':'Drafts, not certified when tool unavailable'},ensure_ascii=False,indent=2)+'\n')
    summary=json.loads((OUT/'FINITE_MODEL_RESULTS.json').read_text())
    print(json.dumps({'finite_groups':len(summary['groups']),'counts':summary['counts'],'native':native},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
