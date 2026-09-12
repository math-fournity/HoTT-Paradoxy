"""Reconcile current dialogue pointers without rewriting any prior letter or assessment.
The original ledger and the pre-reconciliation version are retained.
"""
from pathlib import Path
import copy, datetime, hashlib, importlib.util, json, sys
ROOT=Path(__file__).resolve().parents[2]
D='.codex/research/hott/dialogues/GEMINI-001/'
OUT=ROOT/'artifacts/r027'
def put(p,obj):
    if p.exists(): raise FileExistsError(p)
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def main():
    path=ROOT/D/'DEBATE_LEDGER.json'
    raw=path.read_bytes(); ledger=json.loads(raw)
    put(OUT/'LEDGER_BEFORE_METADATA_RECONCILIATION.json',ledger)
    if ledger['latest_incoming']!='IN-006': raise RuntimeError('Unexpected current letter')
    ledger.setdefault('question_history',[]).append({
      'questions':copy.deepcopy(ledger['next_questions']),
      'reply':'IN-006','assessment':D+'rounds/007/ASSESSMENT.md',
      'note':'Prior NOT_RECEIVED values preserved as history, not current state.'})
    ledger['next_questions']=[
      {'id':'M01','introduced_in':'OUT-006','peer_response':'NOT_RECEIVED',
       'required_to_continue_our_research':False},
      {'id':'M02','introduced_in':'OUT-006','peer_response':'NOT_RECEIVED',
       'required_to_continue_our_research':False}]
    for row in ledger['outgoing']:
        if row['id']=='OUT-005':
            row.update(reply_received=True,reply_id='IN-006',status='USER_RELAYED_REPLY_RECEIVED',
               delivery_evidence='Current user provided IN-006; no direct assistant sending action.')
    ledger['received_rounds']=len(ledger['incoming'])
    ledger['outgoing_count']=len(ledger['outgoing'])
    ledger['round']=6
    ledger.setdefault('workflow_history',[]).append(copy.deepcopy(ledger['workflow']))
    ledger['workflow'].update(status='IN006_REVIEWED_OUT006_READY',
       optional_next_peer_action='M01 actual proof/ReachTrap or counterexample; M02 versioned native logs.',
       next_action='Continue RP-B01 scope and R026 specification/environment fidelity; do not wait for peer.',
       awaiting_peer_to_start_research=False,
       direct_contact_this_round=False,simulated_peer_reply=False)
    ledger['limits']=[
       ('Historical R020 limit: a quoted parallel rev24 planning artifact was not supplied; not a claim that our present R024 is absent.'
        if x=='Quoted rev24 history not available in restored rev19' else x)
       for x in ledger['limits']]
    ledger['updated_at_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    if path.read_bytes()!=raw: raise RuntimeError('Concurrent ledger change')
    path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    spec=importlib.util.spec_from_file_location('r027_ledger_rt',ROOT/'.codex/skills/hott-paradox-research/scripts/cognition_runtime.py')
    rt=importlib.util.module_from_spec(spec);sys.modules[spec.name]=rt;spec.loader.exec_module(rt)
    plan=rt.plan(ROOT)
    state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    assert all(state['records'][i]['status']=='review_required' for i in plan['review_required'])
    put(OUT/'FINAL_PLAN.json',plan)
    put(OUT/'LEDGER_RECONCILIATION.json',{
       'status':'PASS','revision':plan['revision'],'latest_session':plan['latest_session'],
       'snapshot':plan['snapshot'],'ledger_sha256_before':hashlib.sha256(raw).hexdigest(),
       'ledger_sha256_after':hashlib.sha256(path.read_bytes()).hexdigest(),
       'counts':{'incoming':len(ledger['incoming']),'outgoing':len(ledger['outgoing'])},
       'checkpoint_state_modified':False,'current_pointers_consistent':True,
       'dependency_hashes_not_refreshed_to_hide_staleness':True,
       'note':'Dialogue metadata finalized after checkpoint; use FINAL_PLAN snapshot, not earlier receipt for a new read.'})
    print(json.dumps({'revision':plan['revision'],'snapshot':plan['snapshot'],
                     'incoming':len(ledger['incoming']),'outgoing':len(ledger['outgoing'])},indent=2))
if __name__=='__main__':main()
