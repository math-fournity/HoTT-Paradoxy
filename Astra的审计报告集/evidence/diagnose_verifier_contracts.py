"""Compare the actual canonical producer and verifier tree identities read-only."""
import importlib.util,json,pathlib,hashlib
ROOT=pathlib.Path('/Volumes/D/HoTT_AI_HANDOFF_20260911')
def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
V=load('formal_verifier_diag',ROOT/'scripts/audit/verify_formal_proof_run.py')
M=load('mm2_import_diag',ROOT/'scripts/audit/import_coq_undecidability_mm2.py')
run='20260914-MP-COQ-MM2-UNDECIDABILITY-REPLAY-001-01'
source=json.loads((ROOT/'HoTT/verification/runs'/run/'source-manifest.json').read_text())
expected=next(x for x in source['external_dependencies'] if x['label']=='coq-undecidability-extracted-tree')
path=pathlib.Path(expected['local_path']);producer=M.tree_manifest(path);checker=V.deterministic_tree(path)
recorded=json.loads((ROOT/'HoTT/formal/external-coq-mm2/SOURCE_TREE_MANIFEST.json').read_text())
ordered_paths=[p.relative_to(path).as_posix() for p in sorted(path.rglob('*')) if p.is_file() and p.name!='.DS_Store' and p.suffix!='.agdai']
string_paths=sorted(ordered_paths)
first=next((i for i,(a,b) in enumerate(zip(ordered_paths,string_paths)) if a!=b),None)
print(json.dumps({'expected':{k:expected[k] for k in ['file_count','total_bytes','tree_sha256']},'producer':{k:producer[k] for k in ['file_count','total_bytes','tree_sha256']},'generic_verifier':checker,'producer_matches_recorded_source_manifest':producer==recorded,'producer_matches_expected':all(producer[k]==expected[k] for k in ['file_count','total_bytes','tree_sha256']),'first_order_difference':None if first is None else {'index':first,'pathlib_order':ordered_paths[first],'string_order':string_paths[first]},'interpretation':'Same file content can hash differently under Path-component sorting and string sorting; producer receipt agrees with current tree here.'},ensure_ascii=False,indent=2))
