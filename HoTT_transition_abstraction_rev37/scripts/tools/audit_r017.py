#!/usr/bin/env python3
"""Read-only R017 verification against the inherited Git tree, with a new report.
Does not execute recovered programs or certify mathematics/complete cognition.
"""
from pathlib import Path
import argparse
import ast
import hashlib
import io
import json
import re
import subprocess
import tarfile

ROOT=Path(__file__).resolve().parents[2]
BASE='b07ac7ecc084a58be814995931b9706f955e4d95'
SID='S-ANS-20260910-017-LOCAL-EXECUTION'
S='.codex/research/hott/sessions/'+SID+'/'
ALLOWED={'AGENTS.md','MEMORY.md','scripts/README.md','DELIVERY_README.md',
         '.codex/cognition/HEAD.json','.codex/research/hott/STATE.json',
         '.codex/research/hott/FRONTIER.md','.codex/research/hott/LESSONS.md',
         '.codex/research/hott/RESUME.md'}
CODE_SUFFIXES={'.py','.sh','.js','.ts','.mjs','.cjs','.lean','.agda','.v','.hs','.ml','.rs','.c','.cpp','.rb','.jl'}

def sha(b):return hashlib.sha256(b).hexdigest()
def git(*args):
    return subprocess.run(['git','-c','core.hooksPath=/dev/null','-c','core.fsmonitor=false',*args],
                          cwd=ROOT,check=True,capture_output=True).stdout

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise SystemExit('Output exists; refuse overwrite')
    data=git('archive','--format=tar',BASE)
    old={}
    with tarfile.open(fileobj=io.BytesIO(data),mode='r:') as archive:
        for ent in archive.getmembers():
            if not ent.isfile():continue
            old[ent.name]=archive.extractfile(ent).read()
    changed=[name for name,b in old.items() if not (ROOT/name).is_file() or (ROOT/name).read_bytes()!=b]
    unexpected=[name for name in changed if name not in ALLOWED]
    assert not unexpected,unexpected
    actual={p.relative_to(ROOT).as_posix():p for p in ROOT.rglob('*')
            if p.is_file() and '.git' not in p.relative_to(ROOT).parts}
    new_names=sorted(set(actual)-set(old))
    outside_code=[name for name in new_names if Path(name).suffix in CODE_SUFFIXES and not name.startswith('scripts/')]
    assert not outside_code,outside_code
    syntax=[]
    for name,p in sorted(actual.items()):
        if name.startswith('scripts/') and name.endswith('.py') and '/recovered/' not in name:
            ast.parse(p.read_text(),filename=name)
            syntax.append(name)
    recovery=json.loads((ROOT/'scripts/RECOVERY_MANIFEST.json').read_text())
    for row in recovery['unique_payloads']:
        b=(ROOT/row['path']).read_bytes()
        assert len(b)==row['bytes'] and sha(b)==row['sha256'],row['path']
    outputs=json.loads((ROOT/'artifacts/r017/RESULTS.json').read_text())
    counts=outputs['counts']
    assert counts['wrapper_runs']==9216 and counts['base_programs']==256
    assert counts['local_zero_certificates']==1024
    assert counts['local_zero_certificates']+counts['halted_positive']+counts['reachable_spins']==counts['wrapper_runs']
    main_path=ROOT/'scripts/research/r017_local_execution.py'
    assert sha(main_path.read_bytes())==outputs['source_sha256']
    assert outputs==json.loads((ROOT/(S+'FINITE_RESULTS.json')).read_text())
    test=json.loads((ROOT/'artifacts/r017/execution/01-tests.json').read_text())
    assert test['exit_code']==0 and re.search(r'Ran 42 tests',test['stderr']) and test['stderr'].rstrip().endswith('OK')
    logs=[]
    receipts=list((ROOT/'artifacts/r017/execution').glob('*.json'))+[ROOT/'artifacts/r017/policy-execution.json']
    for p in receipts:
        obj=json.loads(p.read_text())
        argv=obj['argv']
        assert not any(token in ('-c','-e','-') for token in argv),p
        if Path(argv[0]).name.startswith('python'):
            program=next(arg for arg in argv[1:] if not arg.startswith('-'))
            target=(Path(obj['cwd'])/program).resolve()
            rel=target.relative_to(ROOT).as_posix()
            assert rel.startswith('scripts/') and target.is_file(),(p,argv)
        assert obj['exit_code']==0,(p,obj['exit_code'])
        logs.append({'path':p.relative_to(ROOT).as_posix(),'argv':argv,'exit_code':obj['exit_code']})
    state=json.loads((ROOT/'.codex/research/hott/STATE.json').read_text())
    base_state=json.loads(old['.codex/research/hott/STATE.json'])
    assert state['revision']==17 and state['latest_session']==SID
    for rid,record in base_state['records'].items():
        assert state['records'][rid]==record,rid
    stale=json.loads((ROOT/'artifacts/r017/checkpoint/STALE_BASE_TEST.json').read_text())
    assert stale['actual_error']=='STALE_BASE' and not stale['writes']
    fresh=json.loads((ROOT/'artifacts/r017/checkpoint/FRESH_PLAN.json').read_text())
    required={S+'PROOF_NOTE.md',S+'FINITE_RESULTS.json',S+'LOADING_EVIDENCE.json',
              'scripts/research/r017_local_execution.py','scripts/tests/test_r017_local_execution.py'}
    assert required <= {e['path'] for e in fresh['documents']}
    load=json.loads((ROOT/(S+'LOADING_EVIDENCE.json')).read_text())
    assert load['full_cognition_gate']=='NOT_PASSED' and load['post_draft_compaction_observed']
    assert load['pages_emitted']==list(range(1,13))
    policy=(ROOT/'AGENTS.md').read_text()
    assert '禁止 inline 代码' in policy and '不再允许“临时先执行、之后再补存”的例外' in policy
    assert '临时探索随后实际采用时' not in policy
    assert not git('remote').strip()
    # Only concrete high-confidence credential signals, not a general security proof.
    patterns={'private_key_header':re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'),
              'github_pat':re.compile(rb'\bgh[pousr]_[A-Za-z0-9]{36,255}\b'),
              'aws_access_key':re.compile(rb'\bAKIA[A-Z0-9]{16}\b')}
    hits=[]
    for name,p in actual.items():
        contents=p.read_bytes()
        for label,pat in patterns.items():
            if pat.search(contents):hits.append({'path':name,'pattern':label})
    assert not hits,hits
    original_zip=Path('/mnt/data/HoTT_workspace_rev16_with_git.zip')
    expected='1f9502a5eb2280dd702891670b557cdfa98d652e2052233df4913033912be4f6'
    assert sha(original_zip.read_bytes())==expected
    report={'schema_version':'hott-r017-workspace-audit/v1','status':'PASS_DEFINED_SCOPE',
        'baseline_git':BASE,'inherited_files_checked':len(old),'changed_inherited_paths':changed,
        'protected_unchanged_inherited_count':len(old)-len(changed),'unexpected_inherited_changes':unexpected,
        'new_code_outside_scripts':outside_code,'new_files_count':len(new_names),
        'python_ast_parsed_count':len(syntax),'python_ast_paths':syntax,
        'retained_recovered_payloads':len(recovery['unique_payloads']),
        'retained_source_occurrences':len(recovery['source_occurrences']),
        'recorded_script_invocations_checked':logs,
        'tests_passed':42,'finite_counts':counts,'result_sha_matches_source':True,
        'checkpoint_revision':17,'old_state_records_unmodified':True,'stale_base_rejected':True,
        'fresh_plan_documents':len(fresh['documents']),'fresh_plan_includes_r017_proof_and_scripts':True,
        'full_cognition_gate':'NOT_PASSED','proof_assistant':'NOT_RUN','independent_review':'NOT_RUN',
        'credential_signal_hits':hits,'credential_scan_scope':'Only listed strong regexes; no general secret guarantee',
        'source_archive_unchanged':True,'source_archive_sha256':expected,
        'code_policy_scope':'Checks saved new script paths and recorded argv, not hidden interpreter history',
        'scripts_executed_by_audit':'None; AST and byte reading only; local git read commands used'}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ('python_ast_paths','recorded_script_invocations_checked')},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
