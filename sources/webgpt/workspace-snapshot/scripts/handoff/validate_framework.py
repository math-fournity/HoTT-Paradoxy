#!/usr/bin/env python3
from pathlib import Path
import hashlib, importlib.util, json, subprocess,sys, tempfile
from datetime import datetime,timezone
from govern import load
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'artifacts/r040';OUT.mkdir(exist_ok=True)
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def main():
 cmd=[sys.executable,'-B','scripts/handoff/test_legacy_governance.py'];start=datetime.now(timezone.utc).isoformat();p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True)
 dump(OUT/'LEGACY_TEST_EXECUTION.json',{'argv':cmd,'cwd':str(ROOT),'started_at_utc':start,'finished_at_utc':datetime.now(timezone.utc).isoformat(),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'scope':'Inherited mechanical governance tests, not mathematics or cognition'})
 if p.returncode:print(p.stderr);raise SystemExit(p.returncode)
 rt=load(ROOT);plan=rt.plan(ROOT);state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
 needs=[r for r in plan['review_required'] if state['records'][r]['status']!='review_required']
 with tempfile.TemporaryDirectory(prefix='hott-portable-entry-') as tmp:
  t=Path(tmp);paths=[ROOT/'governance/PATHS.json',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py']
  for src in paths:
   target=t/src.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(src.read_bytes())
  cmd2=[sys.executable,'-B',str(ROOT/'scripts/handoff/govern.py'),'--root',str(t),'install-entry','--directory','my_non_codex_rules']
  q=subprocess.run(cmd2,cwd='/',capture_output=True,text=True)
  if q.returncode:raise RuntimeError(q.stderr+q.stdout)
  stub=(t/'my_non_codex_rules/HOTT_ENTRYPOINT.md').read_text();assert 'governance/ENTRYPOINT.md' in stub
  q2=subprocess.run(cmd2,cwd='/',capture_output=True,text=True);assert q2.returncode!=0
 version_notes={'current_business_skill':'1.3.4 (SKILL.md actual metadata)','legacy_business_MANIFEST_version':json.loads((ROOT/'.codex/skills/hott-paradox-research/MANIFEST.json').read_text())['version'],'legacy_manifest_is_not_current_integrity_authority':True,'new_current_manifest':'governance/FRAMEWORK_MANIFEST.json'}
 dump(OUT/'FRAMEWORK_TESTS.json',{'status':'PASSED','legacy_test_stderr':p.stderr,'alternate_entry_directory_test':'my_non_codex_rules/HOTT_ENTRYPOINT.md','alternate_entry_exit':q.returncode,'existing_entry_refused':q2.returncode!=0,'new_dependency_reviews_required':needs,'version_notes':version_notes,'old_record_count':len(state['records']),'runtime_sha256':hashlib.sha256((ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py').read_bytes()).hexdigest()})
 print(json.dumps({'legacy_tests':p.stderr[-400:],'alternate_entry_passed':True,'needs_review':needs,'version_notes':version_notes},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
