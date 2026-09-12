"""Replay reviewed source simulators verbatim and probe their actual behavior.
These are adversarial software diagnostics, NOT a HoTT kernel certification.
"""
from pathlib import Path
import json, hashlib, subprocess, sys, os, time, datetime, io, contextlib, runpy, ast
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'artifacts/r019'; SRC=ROOT/'scripts/recovered/HoTT2_json'
recorded={x['chunk']:x for x in json.loads((OUT/'RECORDED_EXECUTIONS.json').read_text())}
replays=[]
for chunk in [13,64,70]:
    f=SRC/f'executable_c{chunk:03}_00.py'
    tree=ast.parse(f.read_text())
    imports=[n.names[0].name for n in ast.walk(tree) if isinstance(n,ast.Import)]
    assert all(i=='time' for i in imports),imports
    cwd=OUT/'replay';cwd.mkdir(exist_ok=True)
    argv=[sys.executable,'-B',str(f)]
    start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
    r=subprocess.run(argv,cwd=cwd,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONHASHSEED':'0'},capture_output=True,text=True,timeout=10)
    row={'chunk':chunk,'argv':argv,'cwd':str(cwd),'source_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'started_at_utc':start,'duration_seconds':time.monotonic()-t,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'recorded_result_chunk':chunk+1,'stdout_identical':r.stdout==recorded[chunk+1]['output'],'scope':'Python stdout replay, not formal proof'}
    replays.append(row)
    (OUT/'replay'/f'c{chunk:03}.stdout.txt').write_text(r.stdout)
    (OUT/'replay'/f'c{chunk:03}.stderr.txt').write_text(r.stderr)
(OUT/'REPLAYS.json').write_text(json.dumps(replays,ensure_ascii=False,indent=2)+'\n')
mods={}
for chunk in [13,64,70]:
    with contextlib.redirect_stdout(io.StringIO()):
        mods[chunk]=runpy.run_path(str(SRC/f'executable_c{chunk:03}_00.py'),run_name=f'r019_probe_c{chunk}')
rows=[]
def check(name,fn,expected=True):
    try:
        value=fn();ok=value==expected
        rows.append({'id':name,'status':'PASS' if ok else 'FAIL','actual':value,'expected':expected})
    except Exception as e:
        rows.append({'id':name,'status':'FAIL','exception':repr(e),'expected':expected})
def rejects(fn):
    try:fn()
    except Exception:return True
    return False
v1=mods[13];v2=mods[64];v3=mods[70]
check('D01_old_python_output_reproduced',lambda:replays[0]['stdout_identical'])
check('D02_v2_python_output_reproduced',lambda:replays[1]['stdout_identical'])
check('D03_v3_python_output_reproduced',lambda:replays[2]['stdout_identical'])
check('D04_all_three_terminate_normally',lambda:all(r['exit_code']==0 for r in replays))
check('D05_old_has_no_type_checker',lambda:'type_check' not in v1 and 'hott_type_check' not in v1)
check('D06_old_trunc_extracts_arbitrary_bool',lambda:repr(v1['reduce_eval'](v1['Unquot'](v1['Trunc'](v1['Bool'](True)))))=='true' and repr(v1['reduce_eval'](v1['Unquot'](v1['Trunc'](v1['Bool'](False)))))=='false')
check('D07_v2_real_not',lambda:str(v2['evaluate'](v2['App'](v2['NotFunc'](),v2['TrueVal']())))=='false')
check('D08_v2_ua_transport_typed_bool',lambda:str(v2['type_check'](v2['Transport'](v2['UnivalenceAxiom'](v2['NotFunc']()),v2['TrueVal']())))=='Bool')
check('D09_v2_ua_transport_returns_ast',lambda:isinstance(v2['evaluate'](v2['Transport'](v2['UnivalenceAxiom'](v2['NotFunc']()),v2['TrueVal']())),v2['Transport']))
check('D10_v2_refl_is_rejected_by_type_checker',lambda:rejects(lambda:v2['type_check'](v2['Refl'](v2['BoolType']()))))
check('D11_v2_refl_transport_is_rejected_by_type_checker',lambda:rejects(lambda:v2['type_check'](v2['Transport'](v2['Refl'](v2['BoolType']()),v2['TrueVal']()))))
check('D12_v2_evaluator_nevertheless_handles_refl',lambda:str(v2['evaluate'](v2['Transport'](v2['Refl'](v2['BoolType']()),v2['TrueVal']())))=='true')
check('D13_v2_rejects_invalid_path_true',lambda:rejects(lambda:v2['type_check'](v2['Transport'](v2['TrueVal'](),v2['NotFunc']()))))
check('D14_v2_rejects_ua_true_without_equivalence',lambda:rejects(lambda:v2['type_check'](v2['UnivalenceAxiom'](v2['TrueVal']()))))
check('D15_v3_accepts_true_as_path_and_not_as_value',lambda:str(v3['hott_type_check'](v3['Transport'](v3['TrueVal'](),v3['NotFunc']())))=='Bool')
check('D16_v3_accepts_none_transport_arguments',lambda:str(v3['hott_type_check'](v3['Transport'](None,None)))=='Bool')
check('D17_v3_accepts_uniquechoice_false_as_nat',lambda:str(v3['hott_type_check'](v3['UniqueChoice'](v3['FalseVal']())))=='Nat')
check('D18_v3_accepts_uniquechoice_none_as_nat',lambda:str(v3['hott_type_check'](v3['UniqueChoice'](None)))=='Nat')
check('D19_v3_proof_leaf_itself_not_checked',lambda:rejects(lambda:v3['hott_type_check'](v3['TruncProof']('halting_step'))))
check('D20_v3_ua_leaf_itself_not_checked',lambda:rejects(lambda:v3['hott_type_check'](v3['UA'](v3['NotFunc']()))))
check('D21_v3_invalid_ua_hidden_under_transport_is_accepted',lambda:str(v3['hott_type_check'](v3['Transport'](v3['UA'](v3['TrueVal']()),v3['TrueVal']())))=='Bool')
check('D22_v3_choice_infers_no_predicate_or_uniqueness',lambda:str(v3['hott_type_check'](v3['UniqueChoice'](v3['TruncProof']('FALSE_0_equals_1'))))=='Nat')
check('D23_v3_choice_evaluator_returns_ast',lambda:isinstance(v3['hott_evaluate'](v3['UniqueChoice'](v3['TruncProof']('halting_step'))),v3['UniqueChoice']))
check('D24_v3_choice_calls_no_search',lambda: no_search()) if False else None
# Only record a test actually executed, not its planned status.
def no_search():
    fn=v3['hott_evaluate'];g=fn.__globals__
    old=g['reality_infinite_search']
    def forbidden():raise RuntimeError('search invoked')
    g['reality_infinite_search']=forbidden
    try: return isinstance(fn(v3['UniqueChoice'](v3['TruncProof']('x'))),v3['UniqueChoice'])
    finally:g['reality_infinite_search']=old
check('D24_v3_choice_calls_no_search',no_search)
check('D25_v3_transport_does_not_normalize_nested_app',lambda:isinstance(v3['hott_evaluate'](v3['Transport'](v3['UA'](v3['NotFunc']()),v3['App'](v3['NotFunc'](),v3['TrueVal']()))).val,v3['App']))
# Observe the exact finite loop without real waiting; source replay above retained sleeps.
log=io.StringIO()
with patch('time.sleep') as sleeper, contextlib.redirect_stdout(log):
    ret=v3['reality_infinite_search']()
check('D26_claimed_infinite_search_returns_literal',lambda:ret=='TIMEOUT_ERROR_NON_TERMINATING')
check('D27_claimed_infinite_search_only_three_sleeps',lambda:sleeper.call_count,3)
check('D28_claimed_infinite_search_prints_three_steps',lambda:log.getvalue().count('正在计算第'),3)
check('D29_v3_no_nat_value_constructor',lambda: not any(k in v3 for k in ('Zero','Succ','NatVal','Numeral','Sigma','IsProp','FirstHalt')))
# Exact finite truth countervaluation to the claimed implication rule.
check('D30_conjunction_denial_does_not_force_conclusion_false',lambda:((not(False and True)) or True) and (not False) and True)
check('D31_forgetting_coordinate_does_not_force_wrong_output',lambda: all((x,x)[0]==x for x in range(-3,4)))
# explicit check that executable form and narrative form are different
check('D32_no_actual_lean_run_in_recorded_code',lambda: all(e['language'].upper()=='PYTHON' for e in json.loads((OUT/'CODE_INDEX.json').read_text()) if e['origin']=='executableCode'))
(OUT/'DIAGNOSTIC_TESTS.json').write_text(json.dumps({'status':'PASS' if all(r['status']=='PASS' for r in rows) else 'FAIL','scope':'Adversarial diagnostics of extracted code, not a HoTT proof','count':len(rows),'passed':sum(r['status']=='PASS' for r in rows),'cases':rows,'patched_probe_note':'Only D26-D28 patched time.sleep for instrumentation; all three verbatim subprocess replays retained source sleeps.'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'replay_count':len(replays),'matching_outputs':sum(r['stdout_identical'] for r in replays),'exit_codes':[r['exit_code'] for r in replays],'diagnostic_count':len(rows),'passed':sum(r['status']=='PASS' for r in rows),'failures':[r for r in rows if r['status']!='PASS']},ensure_ascii=False,indent=2))
if not all(r['status']=='PASS' for r in rows):raise SystemExit(1)
