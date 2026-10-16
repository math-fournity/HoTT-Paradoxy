#!/usr/bin/env python3
"""Round-trip a synthetic delta on the ACTUAL handoff Git baseline in temporary clones.
No research claim, no checkpoint bypass in the real workspace, no network, no source mutation.
"""
from pathlib import Path
import argparse, hashlib, json, os, subprocess, tempfile, time
from delta_tool import init_round, export_delta, verify_delta, stage_delta, git, commit, clean, snapshot
ROOT=Path(__file__).resolve().parents[2]
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,default=ROOT);ap.add_argument('--report',type=Path,required=True);a=ap.parse_args();root=a.root.resolve()
 clean(root);before=commit(root,'HEAD');before_tree=snapshot(root,before);t=time.time()
 with tempfile.TemporaryDirectory(prefix='hott-real-baseline-delta-') as tmp:
  tmp=Path(tmp);work=tmp/'sender'
  git(root,'clone','--no-hardlinks','--',str(root),str(work));git(work,'remote','remove','origin')
  git(work,'config','user.name','Handoff isolation test');git(work,'config','user.email','hott-handoff-test@local.invalid')
  req=tmp/'request.md';req.write_text('仅为实际基线增量传输的隔离合成验收，不是新研究、审计批准或用户追加任务。\n',encoding='utf-8')
  rid='HANDOFF-TRANSPORT-ROUNDTRIP';created=init_round(work,rid,req,before)
  (work/'exchange/rounds'/rid/'RESEARCH_DELTA.md').write_text('# 合成传输探针\n\n无数学成果；只在临时克隆中修改，用于校验真实基线能增量打包。\n',encoding='utf-8')
  (work/'exchange/rounds'/rid/'RUNS.json').write_text(json.dumps({'schema':'hott.run-ledger.v1','runs':[],'status':'SYNTHETIC_TRANSPORT_ONLY'},ensure_ascii=False)+'\n')
  (work/'exchange/rounds'/rid/'AUDIT_REQUEST.md').write_text('# 传输检查\n\n不是数学审计或采纳请求。验证新增文件、SHA、Git ancestry和隔离恢复。\n')
  git(work,'add','--all');git(work,'commit','-m','TEST ONLY: actual baseline incremental roundtrip')
  after=commit(work,'HEAD');z=tmp/'delta.zip';ex=export_delta(work,rid,before,after,z);vr=verify_delta(z,root)
  dest=tmp/'receiver';sr=stage_delta(z,root,dest)
  assert commit(dest,'HEAD')==after and snapshot(dest,after)==snapshot(work,after)
  assert snapshot(root,before)==before_tree and commit(root,'HEAD')==before
  clean(root)
  r={'status':'REAL_HANDOFF_BASELINE_DELTA_ROUNDTRIP_PASSED','synthetic_only':True,'real_research_or_acceptance':False,'base_commit':before,'synthetic_head':after,'unchanged_base_files':len(before_tree),'export':ex,'verify':vr,'stage':sr,'sender_initialization':created,'zip_bytes':z.stat().st_size,'zip_sha256':h(z),'temporary_clones_removed':True,'source_unchanged':True,'elapsed_seconds':round(time.time()-t,3)}
 if a.report.exists():raise FileExistsError(a.report)
 a.report.parent.mkdir(parents=True,exist_ok=True);a.report.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({k:r[k] for k in ['status','base_commit','unchanged_base_files','zip_bytes','source_unchanged']},ensure_ascii=False))
if __name__=='__main__':main()
