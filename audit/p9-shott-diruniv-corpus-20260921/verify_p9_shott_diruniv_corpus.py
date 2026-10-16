#!/usr/bin/env python3
"""Verify P9's branch-pinned sHoTT diruniv source audit."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-VERIFICATION.json'
FREEZE='audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-SOURCE-FREEZE.json';REPORT='audit/p9-shott-diruniv-corpus-20260921/P9-SHOTT-DIRUNIV-CORPUS-REPORT.md'
SOURCES=[FREEZE,REPORT,'audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-REPORT.md','audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md','HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md']
TOKENS=('NOT_A_CONSUMER','DEFENSE_EXPLICIT_COVARIANT_MODAL_STRUCTURE','P10-SECOND-SUCCESSOR-DISCOVERY-001','K-input','K-output','K-claim','K-forgetting','K-version','is-a-cov','mor2fun','dirglue','NO_NEW_HOTT_DEFECT_CLAIM')
def dig(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 a=argparse.ArgumentParser();a.add_argument('--write',action='store_true');x=a.parse_args();missing=[p for p in SOURCES if not(ROOT/p).is_file()];report=(ROOT/REPORT).read_text() if not missing else '';absent=[t for t in TOKENS if t not in report];freeze=json.loads((ROOT/FREEZE).read_text()) if not missing else {};ok=freeze.get('repository')=='https://github.com/LIshy2/sHoTT' and freeze.get('branch')=='diruniv' and freeze.get('commit')=='e76c196293dc402de945d3bcf9873ce84635ff76' and len(freeze.get('files',[]))==7;status='PASS_WITH_SCOPE' if not missing and not absent and ok else 'FAIL';out={'schema_version':'p9-shott-diruniv-verification/v1','task_id':'P9-SHOTT-DIRUNIV-CORPUS-DENOMINATOR-001','status':status,'verdict':'NOT_A_CONSUMER / DEFENSE_EXPLICIT_COVARIANT_MODAL_STRUCTURE / P10_SECOND_SUCCESSOR_DISCOVERY_NEXT / NO_NEW_HOTT_DEFECT_CLAIM','scope':'Checks fixed branch identity and the bounded P7-admission report. It does not typecheck sHoTT, audit all branch files, certify assumptions/postulates, find K, or prove a HoTT defect.','sources':{p:dig(ROOT/p) for p in SOURCES if(ROOT/p).is_file()},'freeze_identity_ok':ok,'missing_sources':missing,'missing_tokens':absent,'public_sources_checked':['https://github.com/LIshy2/sHoTT/tree/diruniv','https://github.com/rzk-lang/rzk','https://arxiv.org/abs/2407.09146','https://arxiv.org/abs/1705.07442']};text=json.dumps(out,ensure_ascii=False,indent=2)+'\n';
 if x.write:OUT.write_text(text)
 print(text,end='');return 0 if status=='PASS_WITH_SCOPE' else 1
if __name__=='__main__':raise SystemExit(main())
