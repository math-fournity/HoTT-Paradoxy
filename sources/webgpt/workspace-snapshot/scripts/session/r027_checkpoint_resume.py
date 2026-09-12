"""Resume an uncommitted R027 checkpoint after a documented dependency-state rejection.
Does not re-append the ledger or overwrite the original failed payload/script.
"""
from pathlib import Path
import copy, datetime, hashlib, importlib.util, json, subprocess, sys
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'artifacts/r027/checkpoint'
PREFIX = '.codex/research/hott/'
SID = 'S-DISC-20260911-027-GEMINI-IN006'

def dump(path, obj):
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def main():
    spec = importlib.util.spec_from_file_location('r027_resume_rt', ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = rt
    spec.loader.exec_module(rt)
    base = json.loads((OUT/'BASE_PLAN.json').read_text())
    payload = copy.deepcopy(json.loads((OUT/'PAYLOAD.json').read_text()))
    now = rt.plan(ROOT)
    if now['revision'] != 26 or now['snapshot'] != base['snapshot']:
        raise RuntimeError('Original uncommitted snapshot changed; refusing repair')
    dump(OUT/'FIRST_ATTEMPT_FAILURE.json', {
        'operation':'dry-run checkpoint from r027_checkpoint.py',
        'error':'DEPENDENCY_REVIEW_REQUIRED: D-GEMINI-OUT-006',
        'observation':'Transcribed from actual tool traceback; not a subprocess log',
        'committed':False,
        'repair':'Keep outgoing delivery status separate from dependency-review status; retain original payload.'
    })
    state_row = next(x for x in payload['files'] if x['path'] == PREFIX+'STATE.json')
    state = json.loads(state_row['text'])
    record = state['records']['D-GEMINI-OUT-006']
    record['status'] = 'review_required'
    record['delivery_status'] = 'PREPARED_NOT_DIRECTLY_SENT'
    state['review_due'] = list(dict.fromkeys(state['review_due']+['D-GEMINI-OUT-006']))
    head = subprocess.run(['git','-C',str(ROOT),'rev-parse','HEAD'], capture_output=True, text=True, check=True).stdout.strip()
    state['local_git']['pre_checkpoint_head'] = head
    state_row['text'] = json.dumps(state, ensure_ascii=False, indent=2)+'\n'
    dump(OUT/'PAYLOAD_REVISED.json', payload)
    dry = rt.checkpoint(ROOT, base['snapshot'], payload, apply=False)
    dump(OUT/'DRY_RUN_REVISED.json', dry)
    result = rt.checkpoint(ROOT, base['snapshot'], payload, apply=True)
    dump(OUT/'COMMIT.json', result)
    after = rt.plan(ROOT)
    dump(OUT/'AFTER_PLAN.json', after)
    paths = {d['path'] for d in after['documents']}
    must = {
       PREFIX+'reviews/EARLY-GEMINI-001/ASSESSMENT.md',
       PREFIX+'reviews/EARLY-GEMINI-001/PLAN.md',
       'artifacts/r026/CHECK_V1_RESULTS.json',
       PREFIX+'dialogues/GEMINI-001/TO_GEMINI_005.md',
       PREFIX+'dialogues/GEMINI-001/TO_GEMINI_006.md',
       PREFIX+'dialogues/GEMINI-001/rounds/007/IN-006.md',
       PREFIX+'dialogues/GEMINI-001/rounds/007/ASSESSMENT.md',
       PREFIX+'sessions/'+SID+'/SESSION.md',
       'artifacts/r027/FINITE_MODEL_RESULTS.json',
       'artifacts/r027/NATIVE_RUN.json',
    }
    if not must <= paths:
        raise RuntimeError('New or R026 continuity inputs missing: '+str(must-paths))
    old = json.loads((ROOT/'artifacts/r027/before'/PREFIX/'STATE.json').read_text())
    if not set(old['records']) <= set(state['records']):
        raise RuntimeError('Old state records removed')
    try:
        rt.checkpoint(ROOT, base['snapshot'], payload, apply=False)
    except rt.CognitionError as exc:
        if str(exc) != 'STALE_BASE':
            raise
        dump(OUT/'STALE_BASE.json', {'status':'REJECTED','error':str(exc)})
    else:
        raise RuntimeError('Stale write accepted')
    summary = {
      'status':result['status'],'revision':after['revision'],'latest_session':SID,
      'snapshot':after['snapshot'],'old_record_count':len(old['records']),
      'new_record_count':len(state['records']),'no_old_records_removed':True,
      'r026_and_out005_in_dynamic_set':True,'required_paths':sorted(must),
      'documents':len(paths),'total_bytes':after['total_bytes'],
      'full_business_cognition':'NOT_CERTIFIED','native_HoTT':'NOT_RUN',
      'native_Lean_Rocq':'NOT_RUN_TOOL_UNAVAILABLE','directly_sent':False,
      'first_attempt':'DRY_RUN_REJECTED_DEPENDENCY_STATE; fixed before any checkpoint commit'
    }
    dump(ROOT/'artifacts/r027/CHECKPOINT_SUMMARY.json', summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
if __name__ == '__main__':
    main()
