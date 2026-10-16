#!/usr/bin/env python3
"""Save experiment provenance, exact source excerpts, and the scripts index."""
from pathlib import Path
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 out=ROOT/'artifacts/r038';p=out/'RESEARCH_MANIFEST.json'
 if p.exists():raise FileExistsError(p)
 files=['scripts/research/r036_transition_abstraction.py','scripts/research/r038_current_lift.py','scripts/tests/test_r038_current_lift.py','scripts/session/r038_run.py','artifacts/r038/TEST_EXECUTION.json','artifacts/r038/MODEL_EXECUTION.json','artifacts/r038/RESULTS.json']
 p.write_text(json.dumps({'files':{s:sha(ROOT/s) for s in files},'scope':'28 unit tests; finite current-lift tables and all-successor certificates; no native kernel', 'runner_receipt_note':'source_hashes in r038_run are hashes of argv paths at completion, so MODEL_EXECUTION additionally contains the output RESULTS hash; this manifest explicitly records imported R036 source too.', 'native_tools':'All lean/agda/coqc/rocq entries null in START.json; no download/install/compile performed this round.'},ensure_ascii=False,indent=2)+'\n')
 pieces=['# R038 exact local source excerpts\n\nSource bytes are pinned by the manifest; quotations do not certify our new proofs.\n']
 for file,lo,hi in [('hits.tex',1210,1234),('logic.tex',801,838)]:
  path=ROOT/'HoTT/theory-schema/upstream/book-578b85cc'/file
  lines=path.read_text().splitlines()
  pieces.append(f'\n## {file} L{lo}–{hi}, sha256={sha(path)}\n\n```tex\n'+ '\n'.join(lines[lo-1:hi])+'\n```\n')
 (out/'SOURCE_EXCERPTS.md').write_text(''.join(pieces))
 (out/'COGNITION_STATUS.json').write_text(json.dumps({'status':'NOT_CERTIFIED_FULL_COGNITION','declared_scope':'Authorized bounded local continuation; not full business-skill acceptance','baseline_documents':418,'baseline_bytes':3159303,'actual_compaction':True,'core_order':'Fifth closure emitted pages 1–12 before actual compaction; three-question file emitted pages 13–16 after compaction','emitted_pages':sorted(int(x.stem) for x in (out/'reads').glob('*.json')),'policy_changed':False,'read_receipts_are_understanding':False},ensure_ascii=False,indent=2)+'\n')
 index=ROOT/'scripts/README.md'
 index.write_text(index.read_text()+'''\n## R038 — 当前态提升与终止证据\n\n- `research/r038_current_lift.py`：复用原R036模型；检验精确后继下降、逐当前态提升、有限Acc证书迁移与倒计时前缀。\n- `tests/test_r038_current_lift.py`：28项正反测试。\n- `session/r038_restore.py`、`r038_context.py`、`r038_run.py`、`r038_prepare.py`、`r038_checkpoint.py`、`r038_verify.py`、`r038_deliver.py`：先存后调用的恢复/读取/运行/保存/核验/打包程序。\n- 一般HoTT终止迁移及逆极限反例在纸笔文档，不声称Python充当HoTT内核。\n''')
 print('Saved research manifest, exact source excerpts, cognition scope and scripts index.')
if __name__=='__main__':main()
