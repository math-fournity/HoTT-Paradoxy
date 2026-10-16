#!/usr/bin/env python3
"""Build repeatable source/claim/scope evidence for the current R016 draft."""
from pathlib import Path
import hashlib, json, shutil
ROOT=Path(__file__).resolve().parents[2]
DRAFT=ROOT/'artifacts/r016/draft'

def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj):
    p=DRAFT/name
    if p.exists():raise SystemExit('Refusing overwrite: '+str(p))
    p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n' if not isinstance(obj,str) else obj)

def main():
    sources=[('HoTT/theory-schema/upstream/book-578b85cc/formal.tex',[(984,1009),(1135,1195)]),
             ('HoTT/theory-schema/upstream/book-578b85cc/basics.tex',[(1740,1788)])]
    rows=[];parts=['# R016 实际原始来源摘录\n\n固定项目Book版本，不是2026领域现状调查。\n']
    for rel,ranges in sources:
        p=ROOT/rel;lines=p.read_text().splitlines()
        rows.append({'path':rel,'sha256':h(p),'line_count':len(lines),'ranges':ranges,'scope':'targeted original rules, not full new proof audit'})
        for a,b in ranges:
            parts.append(f'\n## {rel}:{a}—{b}\n\n```text\n')
            parts.append('\n'.join(f'{i+1}: {lines[i]}' for i in range(a-1,b)))
            parts.append('\n```\n')
    write('SOURCE_EXCERPTS.md',''.join(parts));write('SOURCES.json',{'sources':rows,'external_search':False})
    results=json.loads((ROOT/'artifacts/r016/RESULTS.json').read_text())
    tests=json.loads((ROOT/'artifacts/execution/05-r016-tests.json').read_text())
    assert tests['exit_code']==0 and 'Ran 36 tests' in tests['stderr']
    assert results['family_inputs']==254
    write('CLAIMS.json',{'schema_version':'hott-r016-claims/v1','status':'REVIEW_REQUIRED',
        'known_result_attribution':'Fixed-source axiomatic computation distinction, not original discovery',
        'claims':[
        {'id':'T1','statement':'Book propositional ua computation does not add judgemental computation by itself','evidence':'source clauses','scope':'pinned presentation'},
        {'id':'T2','statement':'Opaque ua coercions in the declared fragment are closed noncanonical normal forms','evidence':'syntax paper argument plus explicit interpreter','scope':'not full Book elaboration'},
        {'id':'T3','statement':'Finite known-Bool-equivalence chains admit certificate-guided value recovery','evidence':'structural induction in PROOF_NOTE section6; 254 finite samples','scope':'not arbitrary axiomatic terms'},
        {'id':'T4','statement':'Stuck normalization proves general nontermination or uncomputability','status':'REJECTED','evidence':'zero-step normal form; finite positive alternatives'}],
        'tests':{'unit_tests':36,'family_inputs':254,'basic_noncanonical':252,'proof_guided_values':254,'prior_r015_groups_replayed':7},
        'hott_kernel':'NOT_RUN','external_independent_review':'NOT_RUN','full_cognition_gate':'NOT_PASSED',
        'main_paradox_manifestation':'OPEN_NOT_ESTABLISHED'})
    for src,name in [('artifacts/r016/RESULTS.json','FINITE_RESULTS.json'),('artifacts/r016/R015_REPLAY.json','R015_REPLAY.json')]:
        dst=DRAFT/name
        if dst.exists():raise SystemExit('Destination exists')
        shutil.copyfile(ROOT/src,dst)
    emitted=[]
    for p in sorted((ROOT/'artifacts/cognition/emitted').glob('*.json')):emitted.append(json.loads(p.read_text()))
    write('LOADING_EVIDENCE.json',{'state':'NOT_PASSED','required_snapshot':json.loads((ROOT/'artifacts/cognition/PLAN.json').read_text())['snapshot'],
       'required_document_count':110,'required_bytes':1476341,'fifth_closure_printed_complete_before_compaction':True,
       'questions_contiguous_print_ranges_before_and_after_compaction':'1-220,221-489,490-619',
       'actual_compaction_occurred':True,'initial_large_page_truncated':True,
       'complete_dynamic_set_received':False,'file_emit_logs':emitted,
       'qualification':'Emitter logs certify output attempts and versions only; not continued retention or independent understanding. No gate rules changed.'})
    tools={}
    for name in ['lean','agda','coqc','git']:
        tools[name]=shutil.which(name)
    write('ENVIRONMENT.json',{'available_executables':tools,'kernel_commands_executed':False,'external_installation':False})
    print(json.dumps({'source_files':len(rows),'tests_confirmed':36,'draft_files':sorted(p.name for p in DRAFT.iterdir())},ensure_ascii=False))
if __name__=='__main__':main()
