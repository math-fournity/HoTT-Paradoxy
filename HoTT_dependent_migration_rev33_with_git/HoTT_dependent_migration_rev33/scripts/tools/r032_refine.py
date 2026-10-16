#!/usr/bin/env python3
"""Preserve v0, avoid an unnecessary inconsistent source env, add JSON replay."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'scripts/research/r032_restricted_reflection.py'
old=p.read_text()
backup=ROOT/'artifacts/r032/v0'
backup.mkdir(parents=True,exist_ok=False)
(backup/'r032_restricted_reflection.py').write_text(old)
for name in ['TEST_EXECUTION.json','CONSTRUCTION_EXECUTION.json','RESULTS.json']:
    (backup/name).write_bytes((ROOT/'artifacts/r032'/name).read_bytes())
text=old.replace("old = {'permit':p, 'unused':BOT}","old = {'permit':p, 'unused':q}")
needle='def main() -> None:\n'
addition='''def formula_from_json(a: Any) -> Formula:
    if type(a) is not list or not a: raise Rejected('invalid serialized formula')
    if a[0] == 'atom' and len(a) == 2: return atom(a[1])
    if a == ['bot']: return BOT
    if a[0] == 'imp' and len(a) == 3:
        return imp(formula_from_json(a[1]),formula_from_json(a[2]))
    raise Rejected('invalid serialized formula')

def proof_from_json(p: Any) -> dict:
    if type(p) is not dict: raise Rejected('invalid serialized proof')
    q = copy.deepcopy(p)
    r = q.get('rule')
    if r == 'lam':
        q['domain'] = formula_from_json(q['domain'])
        q['body'] = proof_from_json(q['body'])
    elif r == 'app':
        q['function'] = proof_from_json(q['function'])
        q['argument'] = proof_from_json(q['argument'])
    elif r == 'absurd':
        q['target'] = formula_from_json(q['target'])
        q['proof'] = proof_from_json(q['proof'])
    return q

def package_from_json(p: Any) -> dict:
    if type(p) is not dict: raise Rejected('invalid serialized package')
    q=copy.deepcopy(p)
    q['environment']={name:formula_from_json(a) for name,a in q['environment'].items()}
    q['goal']=formula_from_json(q['goal'])
    q['proof']=proof_from_json(q['proof'])
    check_package(q)
    return q

'''
assert needle in text
text=text.replace(needle,addition+needle)
p.write_text(text)
t=ROOT/'scripts/tests/test_r032_restricted_reflection.py'
s=t.read_text();s=s.replace('import sys\n','import sys\nimport json\n')
needle="if __name__=='__main__': unittest.main(verbosity=2)"
addition='''    def test_31_json_roundtrip_checked(self):
        pkg=r.quote({'p':P},r.ax('p'))
        restored=r.package_from_json(json.loads(r.encode_data(pkg)))
        self.assertEqual(restored,pkg)
    def test_32_serialized_false_index_rejected(self):
        self.reject(lambda:r.formula_from_json(['atom',True]))
    def test_33_sample_counterexample_source_consistent(self):
        # Both snapshots have Boolean models; the rejection is not based on
        # inserting an inconsistent axiom into the source theory.
        result=r.migration_claims()['changed_axiom']
        self.assertTrue(all(r.truth(a,{0:True,1:True}) for a in result['source'].values()))
        self.assertTrue(all(r.truth(a,{0:False,1:True}) for a in result['target'].values()))

'''
assert needle in s
t.write_text(s.replace(needle,addition+needle))
(ROOT/'artifacts/r032/REFINEMENT.json').write_text(json.dumps({
 'reason':'Use satisfiable source and target environments in the main counterexample; unused false axiom was not needed. Add archival JSON replay.',
 'prior_run':'All 30 prior tests passed; v0 preserved, not a hidden failed run.',
 'semantics_changed':'Only displayed counterexample unused axiom replaced; inference/migration rules unchanged.'},ensure_ascii=False,indent=2)+'\n')
