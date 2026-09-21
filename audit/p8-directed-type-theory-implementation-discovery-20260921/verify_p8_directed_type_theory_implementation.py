#!/usr/bin/env python3
"""Verify the bounded Rzk source freeze and P7 admission assessment."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-VERIFICATION.json'
FREEZE='audit/p8-directed-type-theory-implementation-discovery-20260921/P8-RZK-SOURCE-FREEZE.json'
REPORT='audit/p8-directed-type-theory-implementation-discovery-20260921/P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-REPORT.md'
SOURCES=[FREEZE,REPORT,'audit/p7-origin-directed-diagram-spec-20260921/P7-ORIGIN-DIRECTED-DIAGRAM-SPEC-REPORT.md','HoTT后续研究总体方案/003 - 分支顺序、准入与停止条件.md','HoTT后续研究总体方案/005 - 当前第一步与交接.md']
TOKENS=('NOT_A_CONSUMER','DEFENSE_PRESERVES_DIRECTIONAL_INPUT','P9-SHOTT-DIRUNIV-CORPUS-DENOMINATOR-001','K-input','K-output','K-claim','K-forgetting','K-version','NO_NEW_HOTT_DEFECT_CLAIM')
def digest(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()
def main()->int:
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
 missing=[x for x in SOURCES if not (ROOT/x).is_file()]
 report=(ROOT/REPORT).read_text(encoding='utf-8') if not missing else ''
 absent=[x for x in TOKENS if x not in report]
 freeze=json.loads((ROOT/FREEZE).read_text(encoding='utf-8')) if not missing else {}
 freeze_ok=(freeze.get('repository')=='https://github.com/rzk-lang/rzk' and freeze.get('commit')=='01b081e602a80156966b92de935b7d62a43fceac' and len(freeze.get('files',[]))==6 and freeze.get('lexical_negative_scope',{}).get('result')=='NO_MATCH_WITHIN_DECLARED_SIX_FILE_SCOPE')
 status='PASS_WITH_SCOPE' if not missing and not absent and freeze_ok else 'FAIL'
 out={'schema_version':'p8-directed-implementation-verification/v1','task_id':'P8-DIRECTED-TYPE-THEORY-IMPLEMENTATION-DISCOVERY-001','status':status,'verdict':'NOT_A_CONSUMER / DEFENSE_PRESERVES_DIRECTIONAL_INPUT / P9_SHOTT_DIRUNIV_CORPUS_DENOMINATOR_NEXT / NO_NEW_HOTT_DEFECT_CLAIM','scope':'Checks report/freeze identity and bounded five-condition audit. It does not build/run Rzk, audit its entire repository, prove its metatheory, or establish any HoTT defect.','sources':{x:digest(ROOT/x) for x in SOURCES if (ROOT/x).is_file()},'freeze_identity_ok':freeze_ok,'missing_sources':missing,'missing_tokens':absent,'public_sources_checked':['https://github.com/rzk-lang/rzk','https://arxiv.org/abs/2607.12207','https://arxiv.org/abs/1705.07442','https://arxiv.org/abs/2407.09146']}
 text=json.dumps(out,ensure_ascii=False,indent=2)+'\n'
 if a.write:OUT.write_text(text,encoding='utf-8')
 print(text,end='');return 0 if status=='PASS_WITH_SCOPE' else 1
if __name__=='__main__':raise SystemExit(main())
