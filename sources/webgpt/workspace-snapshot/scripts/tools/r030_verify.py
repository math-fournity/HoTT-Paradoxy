#!/usr/bin/env python3
"""Verify R030 persistence and scopes; this is not a mathematical kernel."""
from pathlib import Path
import argparse, hashlib, importlib.util, json, subprocess, sys, zipfile
ROOT=Path(__file__).resolve().parents[2]
def js(x):return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--fresh',action='store_true');a=ap.parse_args()
 s=importlib.util.spec_from_file_location('verify30_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py');rt=importlib.util.module_from_spec(s);sys.modules[s.name]=rt;s.loader.exec_module(rt)
 plan=rt.plan(ROOT);assert plan['revision']==30
 paths={d['path'] for d in plan['documents']}
 required={'.codex/research/hott/reviews/SELF-REFERENCE-001/PROOF_NOTE.md','.codex/research/hott/reviews/SELF-REFERENCE-002/PROOF_NOTE.md','.codex/research/hott/reviews/EARLY-GEMINI-001/ASSESSMENT.md','artifacts/r030/RESULTS_FIXED.json','MEMORY.md'}
 assert required<=paths
 if a.fresh:
  print(js({'status':'PASS_FRESH_PLAN','revision':30,'required':sorted(required),'model_cognition':'NOT_CERTIFIED','root':str(ROOT)}));return
 archive=Path('/mnt/data/HoTT_self_reference_rev29_with_git.zip');prefix='HoTT_self_reference_rev29/'
 same=[];changed=[];missing=[]
 with zipfile.ZipFile(archive) as z:
  oldstate=json.loads(z.read(prefix+'.codex/research/hott/STATE.json'))
  for ent in z.infolist():
   if ent.is_dir():continue
   assert ent.filename.startswith(prefix)
   rel=ent.filename[len(prefix):]
   if rel.startswith('.git/'):continue
   p=ROOT/rel
   if not p.is_file():missing.append(rel);continue
   if p.read_bytes()==z.read(ent):same.append(rel)
   else:changed.append(rel)
 assert not missing,missing
 allowed={'HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md','scripts/README.md','MEMORY.md','.codex/research/hott/STATE.json','.codex/research/hott/FRONTIER.md','.codex/research/hott/LESSONS.md','.codex/research/hott/RESUME.md','.codex/cognition/HEAD.json'}
 assert set(changed)<=allowed,changed
 current=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text());assert set(oldstate['records'])<=set(current['records'])
 res=json.loads((ROOT/'artifacts/r030/RESULTS_FIXED.json').read_text());assert res['status']=='PASS_FINITE_SCOPE' and res['tests_run']==13
 for field,path in [('source_sha256','scripts/research/r030_staged_reflection.py'),('test_sha256','scripts/tests/test_r030_staged_reflection.py')]:assert res[field]==hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
 assert json.loads((ROOT/'artifacts/r030/RESULTS.json').read_text())['status']=='FAIL'
 assert json.loads((ROOT/'artifacts/r030/EXECUTION_FIXED.json').read_text())['exit_code']==0
 assert json.loads((ROOT/'artifacts/r030/EXECUTION.json').read_text())['exit_code']==1
 assert json.loads((ROOT/'artifacts/r030/checkpoint/STALE.json').read_text())['error']=='STALE_BASE'
 assert 'NOT_RUN'==json.loads((ROOT/'artifacts/r030/NATIVE_STATUS.json').read_text())['status']
 assert not subprocess.check_output(['git','remote'],cwd=ROOT,text=True).strip()
 subprocess.run(['git','diff','--check'],cwd=ROOT,check=True)
 fresh=subprocess.run([sys.executable,'-B',str(Path(__file__).resolve()),'--fresh'],cwd='/mnt/data',text=True,capture_output=True,check=True)
 result={'status':'PASS_FILES_AND_ROUTING_ONLY','source_archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'unchanged_existing_files':len(same),'changed_existing_files':sorted(changed),'missing':missing,'prior_record_count':len(oldstate['records']),'current_record_count':len(current['records']),'old_record_ids_preserved':True,'fresh_process':json.loads(fresh.stdout),'native_status':'NOT_RUN','initial_test_failure_preserved':True,'full_cognition':'INCOMPLETE','mathematical_validation':'PAPER_PLUS_FINITE_SANITY_NOT_KERNEL'}
 out=ROOT/'artifacts/r030/VERIFICATION.json'
 if out.exists():raise FileExistsError(out)
 out.write_text(js(result));print(js(result))
if __name__=='__main__':main()
