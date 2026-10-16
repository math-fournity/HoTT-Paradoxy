#!/usr/bin/env python3
"""Read-only verification, usable from a relocated complete archive."""
from pathlib import Path
import argparse,hashlib,importlib.util,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[2]
P='.codex/research/hott/'
R=P+'reviews/SELF-REFERENCE-004/'
SID='S-RES-20260911-032-RESTRICTED-REFLECTION'
RID='P-RESTRICTED-REFLECTION-032'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--fresh',action='store_true');a=ap.parse_args()
    restore=json.loads((ROOT/'artifacts/r032/RESTORE.json').read_text())
    changed=[];missing=[];same=[]
    for rel,digest in restore['files'].items():
        p=ROOT/rel
        if not p.is_file():missing.append(rel)
        elif sha(p)!=digest:changed.append(rel)
        else:same.append(rel)
    expected={'.codex/cognition/HEAD.json','MEMORY.md',P+'STATE.json',P+'FRONTIER.md',P+'LESSONS.md',P+'RESUME.md',
              'HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md','scripts/README.md'}
    assert not missing,missing
    assert set(changed)==expected,changed
    old=json.loads((ROOT/'artifacts/r032/before'/P/'STATE.json').read_text())
    state=json.loads((ROOT/P/'STATE.json').read_text())
    assert state['revision']==32 and state['latest_session']==SID
    head=json.loads((ROOT/'.codex/cognition/HEAD.json').read_text())
    assert head['revision']==32 and head['latest_session']==SID
    for rel,digest in head['tracked'].items():assert sha(ROOT/rel)==digest,rel
    assert set(old['records'])<=set(state['records'])
    # Current round made no change to the old records, not merely their IDs.
    assert all(v==state['records'][k] for k,v in old['records'].items())
    for rel in ['HoTT/SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md','scripts/README.md',P+'LESSONS.md']:
        prior=(ROOT/'artifacts/r032/before'/rel).read_bytes()
        assert (ROOT/rel).read_bytes().startswith(prior),rel
    for record in (state['records'][RID],state['records'][SID]):
        for rel,digest in record['source_hashes'].items(): assert sha(ROOT/rel)==digest,rel
    result=json.loads((ROOT/'artifacts/r032/RESULTS_V1.json').read_text())
    assert result['source_sha256']==sha(ROOT/'scripts/research/r032_restricted_reflection.py')
    tests=json.loads((ROOT/'artifacts/r032/TEST_V1_EXECUTION.json').read_text())
    assert tests['exit_code']==0 and not tests['timeout']
    assert 'Ran 33 tests' in tests['stderr'] and tests['stderr'].rstrip().endswith('OK')
    spec=importlib.util.spec_from_file_location('r032_verify_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    plan=rt.plan(ROOT)
    assert plan['revision']==32
    allpaths={d['path'] for d in plan['documents']}
    required=[R+'PROOF_NOTE.md',R+'PLAN.md',P+'sessions/'+SID+'/SESSION.md',
              P+'reviews/SELF-REFERENCE-003/PROOF_NOTE.md',P+'reviews/SELF-REFERENCE-002/PROOF_NOTE.md',
              P+'reviews/EARLY-GEMINI-001/ASSESSMENT.md','MEMORY.md']
    assert set(required)<=allpaths
    pages=json.loads((ROOT/'artifacts/r032/CORE_PAGES.json').read_text())
    parts={}
    for i,p in enumerate(pages,1):
        receipt=json.loads((ROOT/'artifacts/r032/read_receipts'/f'{i:03}.json').read_text())
        assert receipt['sha256']==hashlib.sha256(p['text'].encode()).hexdigest()
        parts.setdefault(p['path'],[]).append(p['text'])
    assert len(pages)==12
    for rel,texts in parts.items():assert ''.join(texts).encode()==(ROOT/rel).read_bytes()
    native=json.loads((ROOT/'artifacts/r032/NATIVE_STATUS.json').read_text())
    assert native['native_check']=='NOT_RUN'
    stale=json.loads((ROOT/'artifacts/r032/checkpoint/STALE.json').read_text())
    assert stale['error']=='STALE_BASE'
    git=subprocess.run(['git','merge-base','--is-ancestor',restore['head'],'HEAD'],cwd=ROOT,capture_output=True,text=True)
    assert git.returncode==0
    answer={'status':'VERIFIED_FILES_AND_ROUTING_NOT_MATHEMATICAL_CERTIFICATION',
        'revision':32,'snapshot':plan['snapshot'],'prior_files':len(restore['files']),
        'old_files_unchanged':len(same),'old_files_changed':changed,'old_files_missing':missing,
        'previous_records':len(old['records']),'current_records':len(state['records']),
        'all_old_record_values_preserved':True,'dynamic_documents':len(plan['documents']),
        'new_and_selected_old_research_in_plan':required,'tests':33,'native_kernel':'NOT_RUN',
        'core_pages_emitted_before_actual_compaction':len(pages),'full_business_cognition':'INCOMPLETE'}
    if not a.fresh:
        dest=ROOT/'artifacts/r032/VERIFY.json'
        if dest.exists():raise FileExistsError(dest)
        dest.write_text(json.dumps(answer,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(answer,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
