"""Read-only audit of registered proof receipts using canonical validators."""
import concurrent.futures, importlib.util, json, pathlib, sys
ROOT=pathlib.Path('/Volumes/D/HoTT_AI_HANDOFF_20260911')
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path); obj=importlib.util.module_from_spec(spec); spec.loader.exec_module(obj); return obj
V=module('proof_run_audit',ROOT/'scripts/audit/verify_formal_proof_run.py')
C=module('closure_audit',ROOT/'scripts/audit/verify_proof_version_closure.py')
registry=C.load(ROOT/'HoTT/verification/PROOF_VERSION_CLOSURE.json')
packages=C.package_map(registry)
matrix=C.matrix_identity_lines((ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md').read_bytes())
gaps=C.load_gap_allowlist(registry)
def check(item):
    identity,row=item
    rel=pathlib.Path(row['run']); result={'proof_id':identity,'run':str(rel)}
    try: result['formal_receipt']=V.validate(ROOT,rel,False)
    except Exception as exc: result['formal_receipt']={'status':'FAIL','error':str(exc)}
    if row in registry['later_packages']:
        try: result['relation']=C.check_later_package(ROOT/rel,row,gaps,matrix)
        except Exception as exc: result['relation']={'status':'FAIL','error':str(exc)}
    else: result['relation']={'status':'FROZEN_PACKAGE_CHECKED_BY_VERSION_VERIFIER_BEFORE_LATER_GIT_FAILURE'}
    return result
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: rows=list(pool.map(check,packages.items()))
print(json.dumps({'role':'DERIVED_AUDIT_RESULT_NOT_PROJECT_CURRENT_TRUTH','packages':len(rows),'passed_formal_receipt':sum(x['formal_receipt'].get('status')=='PASS_WITH_SCOPE' for x in rows),'failed_formal_receipt':sum(x['formal_receipt'].get('status')=='FAIL' for x in rows),'rows':rows},ensure_ascii=False,indent=2,default=lambda x:sorted(x) if isinstance(x,set) else str(x)))
