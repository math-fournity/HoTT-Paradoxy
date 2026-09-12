#!/usr/bin/env python3
"""Mechanical tests of new governance tools on synthetic temporary projects.

These are NOT mathematics, model-comprehension, or independent-AI tests.
All mutable fixtures and fault injection are isolated from the actual project.
"""
from __future__ import annotations
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT=Path(__file__).resolve().parents[1]/'scripts/cognition_runtime.py'
spec=importlib.util.spec_from_file_location('cognition_under_test',SCRIPT)
c=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)

class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(prefix='hott-cognition-test-')
        self.root=Path(self.tmp.name)
        fixed=[c.CLOSURE,c.QUESTIONS]+[x for x in c.REQUIRED if x not in (c.CLOSURE,c.QUESTIONS)]
        for rel in fixed:self.put(rel,'TEST FIXTURE ONLY\n'+rel+'\n')
        self.put(c.SKILL,'---\nname: hott-paradox-research\n---\nBusiness test fixture.\n')
        self.put(c.GOVERNANCE_SKILL,'---\nname: hott-session-governance\n---\nGovernance test fixture.\n')
        self.put(c.ROLES,c.dump({'schema_version':'hott-skill-roles/v1','roles':{'business':{'name':'hott-paradox-research','path':c.SKILL},'governance':{'name':'hott-session-governance','path':c.GOVERNANCE_SKILL}}}))
        self.put(c.CLOSURE,'# TEST FIXTURE ONLY\n'+c.CLOSURE_ID+'\n甲\n乙\n丙\n')
        config={'schema_version':'cognition-load-set/v1','fixed_full_text':fixed,'dynamic_state':c.STATE}
        self.put(c.CONFIG,c.dump(config))
        state={'schema_version':'hott-working-state/v1','revision':1,'latest_session':'S0',
               'active':[],'review_due':[],'unresolved':[],
               'records':{'S0':{'kind':'session','path':c.PREFIX+'sessions/S0/SESSION.md',
                                'status':'complete','depends_on':[],'full_sources':[],'source_hashes':{}}}}
        self.put(c.PREFIX+'sessions/S0/SESSION.md','# Test S0\nNot an AI session.\n')
        self.set_state(state)
    def tearDown(self):self.tmp.cleanup()
    def put(self,p,data):
        f=self.root/p;f.parent.mkdir(parents=True,exist_ok=True)
        f.write_bytes(data if isinstance(data,bytes) else data.encode('utf-8'))
    def state(self):return c.obj((self.root/c.STATE).read_bytes())
    def set_state(self,state):
        self.put(c.STATE,c.dump(state));self.refresh_head()
    def refresh_head(self):
        state=self.state()
        self.put(c.HEAD,c.dump({'schema_version':'cognition-head/v1','revision':state['revision'],
          'latest_session':state['latest_session'],
          'tracked':{p:c.sha((self.root/p).read_bytes()) for p in c.MUTABLE}}))
    def plan(self):return c.plan(self.root)
    def all_hashes(self):
        return {p.relative_to(self.root).as_posix():c.sha(p.read_bytes()) for p in self.root.rglob('*') if p.is_file()}
    def payload(self,sid='S1',candidate=False):
        state=self.state();state['revision']+=1;state['latest_session']=sid
        session=c.PREFIX+'sessions/'+sid+'/SESSION.md'
        state['records'][sid]={'kind':'session','path':session,'status':'complete',
                              'depends_on':[],'full_sources':[],'source_hashes':{}}
        extra={session:'# Test '+sid+'\nEvidence, failures, and next action.\n'}
        if candidate:
            path=c.PREFIX+'candidates/C1/candidate.md'
            extra[path]='# Test candidate C1\nNew evidence.\n'
            state['records']['C1']={'kind':'candidate','path':path,'status':'open',
                                   'depends_on':[],'full_sources':[],'source_hashes':{}}
            state['active']=['C1'];state['records'][sid]['depends_on']=['C1']
        texts={p:(self.root/p).read_text() for p in c.MUTABLE}
        texts['MEMORY.md']+='# New actual-state fixture '+sid+'\n'
        texts[c.STATE]=c.dump(state).decode();texts.update(extra)
        return {'schema_version':'cognition-checkpoint/v1','session_id':sid,
                'authorization':'Authorized test fixture writes only',
                'files':[{'path':p,'expected_sha256':c.sha((self.root/p).read_bytes()) if (self.root/p).exists() else None,
                          'text':t} for p,t in texts.items()]}
    def payload_state(self,payload):
        return c.obj(next(x['text'].encode() for x in payload['files'] if x['path']==c.STATE))
    def replace_payload_state(self,payload,state):
        next(x for x in payload['files'] if x['path']==c.STATE)['text']=c.dump(state).decode()
    def fault(self,sid='S1',after=2):
        p=self.plan()
        with self.assertRaisesRegex(c.CognitionError,'INJECTED_INTERRUPTION'):
            c.checkpoint(self.root,p['snapshot'],self.payload(sid),apply=True,_fail_after=after)
    def add_dependencies(self):
        state=self.state();self.put('sources/lemma.md','old source\n')
        for key,deps in [('A',[]),('B',['A'])]:
            path=c.PREFIX+'candidates/'+key+'/candidate.md';self.put(path,'Test '+key+'\n')
            state['records'][key]={'kind':'candidate','path':path,'status':'confirmed','depends_on':deps,
                'full_sources':[],'source_hashes':{'sources/lemma.md':c.sha((self.root/'sources/lemma.md').read_bytes())} if key=='A' else {}}
        state['active']=['B'];self.set_state(state)
    def test_initial_plan_and_order(self):
        p=self.plan();self.assertEqual([x['path'] for x in p['documents'][:2]],[c.CLOSURE,c.QUESTIONS])
        self.assertIn('S0',p['dynamic_records']);self.assertEqual(p['model_context'],'NOT_CERTIFIED_BY_TOOL')
    def test_complete_chunk_coverage(self):
        p=self.plan();chunks=[]
        for f in p['documents']:
            line=1
            while line:
                out=c.read_chunk(self.root,p['snapshot'],f['path'],line,1000);chunks.append(out);line=out['next_start_line']
        self.assertEqual(c.check_coverage(p,chunks)['status'],'FULL_EMITTED_BYTES_MATCH')
    def test_partial_coverage_rejected(self):
        p=self.plan();chunks=[c.read_chunk(self.root,p['snapshot'],c.CLOSURE,1,1000)]
        with self.assertRaisesRegex(c.CognitionError,'COVERAGE_INCOMPLETE'):c.check_coverage(p,chunks)
    def test_out_of_order_coverage_rejected(self):
        p=self.plan();out=c.read_chunk(self.root,p['snapshot'],c.CLOSURE,2,1000)
        with self.assertRaisesRegex(c.CognitionError,'COVERAGE_GAP'):c.check_coverage(p,[out])
    def test_long_line_fails_not_truncated(self):
        self.put(c.QUESTIONS,'中'*2000+'\n');p=self.plan()
        with self.assertRaisesRegex(c.CognitionError,'LINE_TOO_LARGE'):c.read_chunk(self.root,p['snapshot'],c.QUESTIONS,1,100)
    def test_source_growth_changes_snapshot(self):
        old=self.plan();self.put(c.QUESTIONS,(self.root/c.QUESTIONS).read_text()+'new tail\n')
        new=self.plan();self.assertNotEqual(old['snapshot'],new['snapshot'])
        with self.assertRaisesRegex(c.CognitionError,'STALE_SNAPSHOT'):c.read_chunk(self.root,old['snapshot'],c.CLOSURE)
    def test_missing_required_file(self):
        (self.root/c.QUESTIONS).unlink()
        with self.assertRaisesRegex(c.CognitionError,'MISSING'):self.plan()
    def test_wrong_closure(self):
        self.put(c.CLOSURE,'other closure\n')
        with self.assertRaisesRegex(c.CognitionError,'WRONG_CLOSURE'):self.plan()
    def test_required_config_cannot_be_removed(self):
        config=c.obj((self.root/c.CONFIG).read_bytes());config['fixed_full_text'].remove('MEMORY.md');self.put(c.CONFIG,c.dump(config))
        with self.assertRaisesRegex(c.CognitionError,'REQUIRED_COGNITION'):self.plan()
    def test_uncommitted_memory_rejected(self):
        self.put('MEMORY.md','uncommitted\n')
        with self.assertRaisesRegex(c.CognitionError,'UNCOMMITTED_STATE'):self.plan()
    def test_missing_dynamic_record_rejected(self):
        s=self.state();s['active']=['missing'];self.set_state(s)
        with self.assertRaisesRegex(c.CognitionError,'MISSING_RECORD'):self.plan()
    def test_recursive_sources_loaded(self):
        self.add_dependencies();p=self.plan();paths=[x['path'] for x in p['documents']]
        self.assertIn('sources/lemma.md',paths);self.assertTrue({'A','B'}<=set(p['dynamic_records']))
    def test_dependency_cycle_rejected(self):
        self.add_dependencies();s=self.state();s['records']['A']['depends_on']=['B'];self.set_state(s)
        with self.assertRaisesRegex(c.CognitionError,'DEPENDENCY_CYCLE'):self.plan()
    def test_transitive_review_propagation(self):
        self.add_dependencies();self.put('sources/lemma.md','changed\n')
        self.assertEqual(self.plan()['review_required'],['A','B'])
    def test_stale_dependencies_must_be_flagged(self):
        self.add_dependencies();self.put('sources/lemma.md','changed\n');p=self.plan()
        with self.assertRaisesRegex(c.CognitionError,'DEPENDENCY_REVIEW_REQUIRED'):
            c.checkpoint(self.root,p['snapshot'],self.payload(),apply=True)
    def test_review_required_checkpoint_allowed(self):
        self.add_dependencies();self.put('sources/lemma.md','changed\n');p=self.plan();payload=self.payload();s=self.payload_state(payload)
        for k in ('A','B'):s['records'][k]['status']='review_required'
        s['review_due']=['A','B'];self.replace_payload_state(payload,s)
        self.assertEqual(c.checkpoint(self.root,p['snapshot'],payload,apply=True)['status'],'CHECKPOINT_COMMITTED')
        self.assertEqual(self.plan()['review_required'],['A','B'])
    def test_rehash_not_revalidation(self):
        self.add_dependencies();self.put('sources/lemma.md','changed\n');p=self.plan();payload=self.payload();s=self.payload_state(payload)
        s['records']['A']['source_hashes']['sources/lemma.md']=c.sha((self.root/'sources/lemma.md').read_bytes());self.replace_payload_state(payload,s)
        with self.assertRaisesRegex(c.CognitionError,'REVALIDATION_EXPLANATION_REQUIRED'):c.checkpoint(self.root,p['snapshot'],payload)
    def test_dry_run_zero_writes(self):
        p=self.plan();before=self.all_hashes();out=c.checkpoint(self.root,p['snapshot'],self.payload())
        self.assertEqual(out['status'],'DRY_RUN');self.assertEqual(before,self.all_hashes())
    def test_new_candidate_is_next_load_content(self):
        p=self.plan();c.checkpoint(self.root,p['snapshot'],self.payload(candidate=True),apply=True)
        new=self.plan();self.assertEqual(new['latest_session'],'S1');self.assertIn('C1',new['dynamic_records'])
        self.assertIn(c.PREFIX+'candidates/C1/candidate.md',[x['path'] for x in new['documents']])
    def test_stale_second_writer_rejected(self):
        p=self.plan();first=self.payload('S1');second=self.payload('S2')
        c.checkpoint(self.root,p['snapshot'],first,apply=True);before=self.all_hashes()
        with self.assertRaisesRegex(c.CognitionError,'STALE_BASE'):c.checkpoint(self.root,p['snapshot'],second,apply=True)
        self.assertEqual(before,self.all_hashes())
    def test_new_process_observes_new_session(self):
        env={'PYTHONDONTWRITEBYTECODE':'1'}
        a=subprocess.run([sys.executable,'-B',str(SCRIPT),'--project-root',str(self.root),'plan'],capture_output=True,text=True,check=True,env=env)
        old=json.loads(a.stdout);c.checkpoint(self.root,old['snapshot'],self.payload('S1'),apply=True)
        b=subprocess.run([sys.executable,'-B',str(SCRIPT),'--project-root',str(self.root),'plan'],capture_output=True,text=True,check=True,env=env)
        new=json.loads(b.stdout);self.assertEqual(new['latest_session'],'S1');self.assertNotEqual(old['invocation_nonce'],new['invocation_nonce'])
    def test_session_append_only(self):
        p=self.plan();c.checkpoint(self.root,p['snapshot'],self.payload('S1'),apply=True);p=self.plan()
        with self.assertRaisesRegex(c.CognitionError,'SESSION_IMMUTABLE'):c.checkpoint(self.root,p['snapshot'],self.payload('S1'))
    def test_old_record_cannot_disappear(self):
        p=self.plan();payload=self.payload();s=self.payload_state(payload);del s['records']['S0'];self.replace_payload_state(payload,s)
        with self.assertRaisesRegex(c.CognitionError,'OLD_RECORD_ROUTING_REMOVED'):c.checkpoint(self.root,p['snapshot'],payload)
    def test_record_identity_immutable(self):
        p=self.plan();payload=self.payload();s=self.payload_state(payload);s['records']['S0']['path']='elsewhere.md';self.replace_payload_state(payload,s)
        with self.assertRaisesRegex(c.CognitionError,'RECORD_IDENTITY_CHANGED'):c.checkpoint(self.root,p['snapshot'],payload)
    def test_readers_reject_active_lock(self):
        self.put(c.LOCK,c.dump({'session_id':'other'}))
        with self.assertRaisesRegex(c.CognitionError,'CHECKPOINT_INCOMPLETE'):self.plan()
    def test_recovery_requires_confirmation(self):
        self.fault()
        with self.assertRaisesRegex(c.CognitionError,'EXPLICIT_OWNER_STOP'):c.recover(self.root,'finish')
    def test_interruption_finish(self):
        self.fault()
        with self.assertRaisesRegex(c.CognitionError,'CHECKPOINT_INCOMPLETE'):self.plan()
        self.assertEqual(c.recover(self.root,'finish',confirm_owner_stopped=True)['status'],'RECOVERED_FINISH')
        self.assertEqual(self.plan()['latest_session'],'S1')
    def test_interruption_rollback(self):
        before={p:(self.root/p).read_bytes() for p in c.MUTABLE+(c.HEAD,)};self.fault(after=6)
        c.recover(self.root,'rollback',confirm_owner_stopped=True)
        for p,b in before.items():self.assertEqual((self.root/p).read_bytes(),b)
        self.assertFalse((self.root/(c.PREFIX+'sessions/S1/SESSION.md')).exists())
    def test_every_write_boundary_can_finish(self):
        for stage in range(1,8):
            with self.subTest(stage=stage):
                sid='S'+str(stage);self.fault(sid,stage);c.recover(self.root,'finish',confirm_owner_stopped=True)
                self.assertEqual(self.plan()['latest_session'],sid)
    def test_third_party_write_blocks_recovery(self):
        self.fault();self.put('MEMORY.md','third party\n')
        with self.assertRaisesRegex(c.CognitionError,'THIRD_PARTY_WRITE'):c.recover(self.root,'finish',confirm_owner_stopped=True)
    def test_corrupt_backup_blocks_recovery(self):
        self.fault();j=c.obj((self.root/c.TXN).read_bytes());self.put(j['rows'][0]['after_copy'],'corrupt\n')
        with self.assertRaisesRegex(c.CognitionError,'RECOVERY_BACKUP_CORRUPT'):c.recover(self.root,'finish',confirm_owner_stopped=True)
    def test_mutated_journal_blocks_recovery(self):
        self.fault();j=c.obj((self.root/c.TXN).read_bytes());j['rows'][0]['path']=c.CLOSURE;self.put(c.TXN,c.dump(j))
        with self.assertRaisesRegex(c.CognitionError,'RECOVERY_JOURNAL_MISMATCH'):c.recover(self.root,'finish',confirm_owner_stopped=True)
    def test_recovery_cannot_target_closure(self):
        self.fault();j=c.obj((self.root/c.TXN).read_bytes());j['rows'][0]['path']=c.CLOSURE;data=c.dump(j)
        self.put(c.TXN,data);self.put('.codex/cognition/checkpoints/S1/transaction.json',data)
        with self.assertRaisesRegex(c.CognitionError,'RECOVERY_PATH_REJECTED'):c.recover(self.root,'finish',confirm_owner_stopped=True)
    def test_required_checkpoint_file_missing(self):
        p=self.plan();payload=self.payload();payload['files']=[x for x in payload['files'] if x['path']!='MEMORY.md']
        with self.assertRaisesRegex(c.CognitionError,'INCOMPLETE_CHECKPOINT_STATE'):c.checkpoint(self.root,p['snapshot'],payload)
    def test_explicit_expected_hash_required(self):
        p=self.plan();payload=self.payload();del payload['files'][-1]['expected_sha256']
        with self.assertRaisesRegex(c.CognitionError,'EXPECTED_FILE_BASE_REQUIRED'):c.checkpoint(self.root,p['snapshot'],payload)
    def test_closure_write_disallowed(self):
        p=self.plan();payload=self.payload();payload['files'].append({'path':c.CLOSURE,'text':'changed','expected_sha256':c.sha((self.root/c.CLOSURE).read_bytes())})
        with self.assertRaisesRegex(c.CognitionError,'WRITE_OUTSIDE_AUTHORIZED'):c.checkpoint(self.root,p['snapshot'],payload)
    def test_traversal_rejected(self):
        with self.assertRaisesRegex(c.CognitionError,'UNSAFE_PATH'):c.path_of(self.root,'../outside')
    def test_symlink_rejected(self):
        (self.root/c.QUESTIONS).unlink();(self.root/c.QUESTIONS).symlink_to(self.root/'MEMORY.md')
        with self.assertRaisesRegex(c.CognitionError,'SYMLINK_FORBIDDEN'):self.plan()
    def test_non_utf8_rejected(self):
        self.put(c.QUESTIONS,b'\xff')
        with self.assertRaisesRegex(c.CognitionError,'NOT_UTF8'):self.plan()
    def test_unchanged_plan_is_not_read_receipt(self):
        a=self.plan();b=self.plan();self.assertEqual(a['snapshot'],b['snapshot'])
        self.assertEqual(b['model_context'],'NOT_CERTIFIED_BY_TOOL')
        with self.assertRaisesRegex(c.CognitionError,'COVERAGE_INCOMPLETE'):c.check_coverage(b,[])


    # v1.3: named roles, automatic open records, and evidence-backed closure.
    def add_unqueued_open(self,key='QX',status='open'):
        s=self.state();path=c.PREFIX+'candidates/'+key+'/record.md'
        self.put(path,'# Open record '+key+'\nFull unresolved evidence.\n')
        s['records'][key]={'kind':'source_gap','path':path,'status':status,'depends_on':[], 'full_sources':[], 'source_hashes':{}}
        self.set_state(s);return path
    def test_named_roles_both_full_loaded(self):
        p=self.plan();paths=[x['path'] for x in p['documents']]
        self.assertIn(c.GOVERNANCE_SKILL,paths);self.assertIn(c.SKILL,paths);self.assertIn(c.ROLES,paths)
    def test_wrong_governance_registry_name_rejected(self):
        d=c.obj((self.root/c.ROLES).read_bytes());d['roles']['governance']['name']='wrong'
        self.put(c.ROLES,c.dump(d))
        with self.assertRaises(c.CognitionError):self.plan()
    def test_governance_frontmatter_mismatch_rejected(self):
        self.put(c.GOVERNANCE_SKILL,'---\nname: wrong\n---\nWrong fixture.\n')
        with self.assertRaises(c.CognitionError):self.plan()
    def test_governance_cannot_be_removed_from_fixed(self):
        d=c.obj((self.root/c.CONFIG).read_bytes());d['fixed_full_text'].remove(c.GOVERNANCE_SKILL)
        self.put(c.CONFIG,c.dump(d))
        with self.assertRaises(c.CognitionError):self.plan()
    def test_unqueued_open_record_is_loaded(self):
        path=self.add_unqueued_open();p=self.plan()
        self.assertIn('QX',p['dynamic_records']);self.assertIn(path,[x['path'] for x in p['documents']])
    def test_all_six_open_statuses_casefold_loaded(self):
        keys=[]
        for n,status in enumerate(sorted(c.OPEN_STATUSES)):
            key='Q'+str(n);keys.append(key);self.add_unqueued_open(key,status.upper())
        self.assertTrue(set(keys)<=set(self.plan()['dynamic_records']))
    def test_unqueued_open_dependency_body_loaded(self):
        self.add_unqueued_open();s=self.state();source='sources/full-proof.md';self.put(source,'Complete actual fixture proof.\n')
        s['records']['QX']['full_sources']=[source];self.set_state(s)
        self.assertIn(source,[x['path'] for x in self.plan()['documents']])
    def test_manual_queue_removal_cannot_hide_open_record(self):
        self.add_unqueued_open();s=self.state();s['unresolved']=['QX'];self.set_state(s)
        p=self.plan();payload=self.payload();s=self.payload_state(payload);s['unresolved']=[];self.replace_payload_state(payload,s)
        c.checkpoint(self.root,p['snapshot'],payload,apply=True)
        self.assertIn('QX',self.plan()['dynamic_records'])
    def test_missing_open_full_source_blocks(self):
        self.add_unqueued_open();s=self.state();s['records']['QX']['full_sources']=['sources/missing.md'];self.set_state(s)
        with self.assertRaises(c.CognitionError):self.plan()
    def test_close_open_without_resolution_rejected(self):
        self.add_unqueued_open();p=self.plan();payload=self.payload();s=self.payload_state(payload);s['records']['QX']['status']='closed';self.replace_payload_state(payload,s)
        with self.assertRaises(c.CognitionError):c.checkpoint(self.root,p['snapshot'],payload)
    def test_close_open_blank_reason_rejected(self):
        self.add_unqueued_open();p=self.plan();payload=self.payload();s=self.payload_state(payload)
        s['records']['QX'].update(status='closed',resolution={'reason':'  ','evidence':[s['records']['QX']['path']]});self.replace_payload_state(payload,s)
        with self.assertRaises(c.CognitionError):c.checkpoint(self.root,p['snapshot'],payload)
    def test_close_open_empty_evidence_rejected(self):
        self.add_unqueued_open();p=self.plan();payload=self.payload();s=self.payload_state(payload)
        s['records']['QX'].update(status='closed',resolution={'reason':'A reason','evidence':[]});self.replace_payload_state(payload,s)
        with self.assertRaises(c.CognitionError):c.checkpoint(self.root,p['snapshot'],payload)
    def test_close_with_actual_evidence_retained_and_loaded(self):
        path=self.add_unqueued_open();e='sources/closure-proof.md';self.put(e,'Actual fixture evidence, not a math proof.\n')
        p=self.plan();payload=self.payload();s=self.payload_state(payload)
        s['records']['QX'].update(status='closed',resolution={'reason':'Fixture resolved with supplied evidence','evidence':[e]})
        s['records']['S1']['depends_on']=['QX'];self.replace_payload_state(payload,s)
        c.checkpoint(self.root,p['snapshot'],payload,apply=True)
        self.assertIn('QX',self.state()['records']);self.assertIn(e,[x['path'] for x in self.plan()['documents']])
    def test_close_with_missing_evidence_rejected(self):
        self.add_unqueued_open();p=self.plan();payload=self.payload();s=self.payload_state(payload)
        s['records']['QX'].update(status='closed',resolution={'reason':'Claims resolved','evidence':['sources/missing-proof.md']});self.replace_payload_state(payload,s)
        with self.assertRaises(c.CognitionError):c.checkpoint(self.root,p['snapshot'],payload)
    def test_unrelated_closed_record_is_retained_not_forced_into_load(self):
        path=self.add_unqueued_open(status='closed');p=self.plan()
        self.assertIn('QX',self.state()['records']);self.assertNotIn('QX',p['dynamic_records']);self.assertNotIn(path,[x['path'] for x in p['documents']])
    def test_new_unqueued_open_visible_to_fresh_process(self):
        p=self.plan();payload=self.payload(candidate=True);s=self.payload_state(payload)
        s['active']=[];s['records']['S1']['depends_on']=[];self.replace_payload_state(payload,s)
        c.checkpoint(self.root,p['snapshot'],payload,apply=True)
        call=subprocess.run([sys.executable,'-B',str(SCRIPT),'--project-root',str(self.root),'plan'],capture_output=True,text=True,timeout=15)
        self.assertEqual(call.returncode,0,call.stderr);fresh=json.loads(call.stdout)
        self.assertIn('C1',fresh['dynamic_records'])

if __name__=='__main__':unittest.main(verbosity=2)
