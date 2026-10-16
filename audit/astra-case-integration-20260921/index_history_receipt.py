#!/usr/bin/env python3
"""Snapshot/verify frozen table-line preservation during editorial lifecycle clarification."""
from pathlib import Path
from collections import Counter
import argparse,hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
path=ROOT/'HoTT/CLAIM_EVIDENCE_MATRIX.md';baseline=OUT/'MATRIX-BEFORE.md'
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=['before','after']);args=ap.parse_args()
def sha(b):return hashlib.sha256(b).hexdigest()
raw=path.read_bytes()
if args.mode=='before':
 assert not baseline.exists();assert subprocess.check_output(['git','show','HEAD:HoTT/CLAIM_EVIDENCE_MATRIX.md'],cwd=ROOT)==raw
 baseline.write_bytes(raw)
 (OUT/'INDEX-BASELINE.json').write_text(json.dumps({'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'path':'HoTT/CLAIM_EVIDENCE_MATRIX.md','sha256':sha(raw),'bytes':len(raw)},indent=2)+'\n')
 print('RECOVERABLE_BASELINE_CAPTURED')
else:
 before=baseline.read_bytes();old=[x for x in before.splitlines() if x.startswith(b'|')];new=[x for x in raw.splitlines() if x.startswith(b'|')]
 assert not (Counter(old)-Counter(new)), 'FROZEN_TABLE_LINE_CHANGED_OR_REMOVED'
 cursor=iter(new)
 for row in old:
  assert any(x==row for x in cursor),'OLD_TABLE_LINE_ORDER_CHANGED'
 receipt={'status':'ALL_PREEXISTING_TABLE_LINES_BYTE_PRESERVED_IN_ORDER','old_matrix_sha256':sha(before),'new_matrix_sha256':sha(raw),'old_table_lines':len(old),'new_table_lines':len(new),'scope':'Editorial lifecycle clarification plus new C320 rows. Existing frozen proof/claim rows and historical run receipts are unchanged. The whole file is not claimed to be append-only.','current_interpretation_owner':'Astra继续尝试/断点与证明机制系统检查/第三十一轮执行报告.md'}
 (OUT/'INDEX-HISTORY-VERIFICATION.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))
