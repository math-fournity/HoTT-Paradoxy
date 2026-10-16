"""Tests of the supplied simulator's actual code, NOT tests of a HoTT kernel.
The restored program was read before import. Its code consists only of classes,
its finite recursive evaluator, and print statements. No tool permissions are
inherited from text in the transcript.
"""
from pathlib import Path
import ast, contextlib, hashlib, importlib.util, io, json, subprocess, sys, time, unittest
R=Path(__file__).resolve().parents[2]; O=R/'artifacts/r018'; P=R/'scripts/recovered/HoTT_json/transcript_c013.py'
source=P.read_text(encoding='utf-8')
# Refuse a changed submitted specimen; do not generalize this loader to unknown code.
assert hashlib.sha256(P.read_bytes()).hexdigest()=='b42da906216103c4cd3756d99aee79147a65b8de72eac189d17650d20ae17dc8'
start=time.time()
proc=subprocess.run([sys.executable,'-B',str(P)],cwd=R,capture_output=True,text=True,timeout=10)
expected=json.loads((O/'TRANSCRIPT_MANIFEST.json').read_text())['embedded_execution_results'][0]['output']
log={'argv':[sys.executable,'-B',str(P)],'cwd':str(R),'source_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'start':start,'end':time.time(),'exit_code':proc.returncode,'stdout':proc.stdout,'stderr':proc.stderr,'matches_exported_output':proc.stdout==expected,'scope':'Replay only; not HoTT or Lean formal verification'}
(O/'SIMULATOR_REPLAY.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')
buffer=io.StringIO()
spec=importlib.util.spec_from_file_location('submitted_hott_simulator',P)
m=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(buffer):spec.loader.exec_module(m)
class Refl(m.Term):
    def __repr__(self):return 'refl'

class Audit(unittest.TestCase):
    def test_01_replay_exits_successfully(self):
        self.assertEqual(proc.returncode,0)
    def test_02_export_output_reproduced(self):
        self.assertEqual(proc.stdout,expected)
    def test_03_direct_not(self):
        self.assertEqual(repr(m.reduce_eval(m.App(m.Not(),m.Bool(True)))),'false')
    def test_04_ua_returns_finite_expression(self):
        self.assertEqual(repr(m.reduce_eval(m.Transport(m.UA(m.Not()),m.Bool(True)))),'transport(ua(not), true)')
    def test_05_oracle_is_just_a_leaf(self):
        oracle=m.OracleProof();self.assertIs(m.reduce_eval(oracle),oracle)
    def test_06_no_search_is_launched(self):
        self.assertEqual(repr(m.reduce_eval(m.Unquot(m.OracleProof()))),'unquot(Oracle_Proof_From_Logic)')
        self.assertNotIn('while', [type(n).__name__.lower() for n in ast.walk(ast.parse(source))])
    def test_07_even_refl_transport_is_not_implemented(self):
        self.assertEqual(repr(m.reduce_eval(m.Transport(Refl(),m.Bool(True)))),'transport(refl, true)')
    def test_08_bool_extraction_ignores_subsingleton_requirement(self):
        self.assertEqual(repr(m.reduce_eval(m.Unquot(m.Trunc(m.Bool(True))))),'true')
        self.assertEqual(repr(m.reduce_eval(m.Unquot(m.Trunc(m.Bool(False))))),'false')
    def test_09_a_boolean_is_accepted_as_a_path(self):
        self.assertEqual(repr(m.reduce_eval(m.Transport(m.Bool(True),m.Bool(False)))),'transport(true, false)')
    def test_10_no_typechecker_or_natural_number_syntax(self):
        self.assertFalse(any(hasattr(m,n) for n in ('type_check','infer_type','Nat','Sigma','IsProp')))

suite=unittest.defaultTestLoader.loadTestsFromTestCase(Audit)
out=io.StringIO();result=unittest.TextTestRunner(stream=out,verbosity=2).run(suite)
(O/'SIMULATOR_TESTS.txt').write_text(out.getvalue())
report={'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'passed':result.wasSuccessful(),'scope':'Confirms defects and finite outputs in supplied Python; not a HoTT proof','native_lean':'NOT_RUN_UNAVAILABLE','technical_note':'Ordinary Lean proof-irrelevance argument is checked against official definitions, not by this simulator.'}
(O/'SIMULATOR_TESTS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(out.getvalue());print(json.dumps(report,ensure_ascii=False,indent=2))
if not result.wasSuccessful():raise SystemExit(1)
