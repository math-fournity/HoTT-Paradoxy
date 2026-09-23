#!/usr/bin/env python3
"""Bounded P44 primary-source reading and reuse manifest."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
BOOK=Path('HoTT/theory-schema/upstream/book-578b85cc')
ranges={'homotopy.tex':[[1,186],[405,548],[596,655],[938,994],[1175,1227],[1558,1604],[1620,1648],[1733,1767],[1879,1918],[2340,2541]],
 'hlevels.tex':[[1378,1449],[1665,1906]],
 'categories.tex':[[1,168],[539,675],[1073,1157],[1366,1425],[1444,1463],[1529,1584],[1655,1708]],
 'setmath.tex':[[683,759],[887,968],[1000,1065],[1158,1188],[1278,1337],[1445,1766]]}
paths=[BOOK/p for p in ranges]+[Path('HoTT理论充分检视/003 - P41同一性、等价与前提资格.md'),Path('HoTT/formal/sip-representation/SIPRepresentation.agda')]
out=dict(schema_version='bounded-theory-source-audit/v1',baseline='bd43d8468af68d775ea62814238cc6a266bf7f68',book_commit='578b85cc8d586b1677ec4335148adeb443057d24',read_ranges=ranges,
 source_hashes={str(p):hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
 existing_control_status='P41_SIP_SOURCE_REUSE_NOT_REPLAYED',new_math_claims=[],new_kernel_runs=[],
 external_sources=[dict(url='https://arxiv.org/pdf/1706.07526v6',read='intro, Definitions2.1/2.2, Theorem3.1 scope, 3.17-3.21 with universe discussion',status='SOURCE_REPORTED_NOT_REPLAYED'),dict(url='https://arxiv.org/pdf/1303.0584',read='Theorem8.4 scope,8.5/Remark8.6/Examples8.7-8.8, formalization scope',status='SOURCE_REPORTED_NOT_REPLAYED')],
 verdict='DERIVED_IDENTIFICATION_AND_UNIVERSALITY_KEEP_TARGET_AND_COHERENCE_CONDITIONS',
 coverage_boundary='Representative derived contracts and critical interactions, not all theorems or all models.')
(HERE/'EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'SOURCE_IDENTITIES_RECORDED','files':len(paths),'new_kernel_runs':0}))
