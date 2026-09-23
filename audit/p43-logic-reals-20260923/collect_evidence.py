#!/usr/bin/env python3
"""P43 source identity; paper/source review is not a kernel replay."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
BOOK=Path('HoTT/theory-schema/upstream/book-578b85cc')
ranges={'logic.tex':[[159,255],[353,558],[701,801]],'reals.tex':[[1,222],[264,357],[469,944],[1010,1143],[1724,1968],[2115,2185],[2200,2465],[2466,2548]],'setmath.tex':[[468,648]]}
paths=[BOOK/p for p in ranges]+[Path(p) for p in [
 'HoTT/theory-schema/DERIVED_STRUCTURES.md','HoTT/formal/dedekind-omega-missile/CutRealLayer.agda','HoTT/formal/dedekind-omega-missile/MissileFourNecessityLEM.agda','HoTT/formal/cauchy-modulus/CauchyModulus.agda',
 '.codex/research/hott/PREMISE-001/008 - SUPPLY-010 F2 缺口层两问与两枚导弹（Dedekind-Ω 簇）.md',
 'audit/p17-cubical-hott-cauchy-reals-corpus-20260921/P17-CUBICAL-HOTT-CAUCHY-REALS-CORPUS-REPORT.md',
 'audit/p17-cubical-hott-cauchy-reals-corpus-20260921/P17-CUBICAL-HOTT-CAUCHY-REALS-SOURCE-FREEZE.json',
 'Astra继续尝试/断点与证明机制系统检查/第三十五轮执行报告/001 - 原四弹逐项对账.md']]
out=dict(schema_version='bounded-theory-source-audit/v1',baseline='95886878d0352492b8ed63e372208f66d97d3310',book_commit='578b85cc8d586b1677ec4335148adeb443057d24',read_ranges=ranges,
    source_hashes={str(p):hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
    partial_read_boundaries={'MissileFourNecessityLEM.agda':'1-35,114-123','PREMISE-001/008':'102-121; exact Omega dependency occurrences','P35 report':'exact SingleOmega paragraph reused; not a new full historical audit'},
    existing_control_status='SOURCE_INSPECTED_NOT_REPLAYED_THIS_WAVE',new_math_claims=[],new_kernel_runs=[],
    external_sources=[
      dict(url='https://martinescardo.github.io/TypeTopology/UF.Size.html',read='definition of smallness/PR and Omega+/Omega resizing near lines57-108,267-339',status='SOURCE_REPORTED_NOT_REPLAYED'),
      dict(url='https://arxiv.org/html/2604.24782v1',read='intro, 3.4 and 5; local P17 reuse',status='KNOWN_SOURCE_PARTIAL_REUSE_NOT_NEW_K',repository_commit_previously_frozen='9fcc142b86d0c1e2bd6d06f86f7617200ad74857'),
      dict(url='https://arxiv.org/abs/1610.05072',read='identity/abstract only',status='LOCATOR_ONLY_NOT_SUBSTANTIVE_REVIEW')
    ],network_limit='GitHub API HEAD query returned HTTP403 rate limit; no new code identity/clone/replay claimed',
    current_map_correction='DERIVED_STRUCTURES D06/D11 inductive-recursive -> higher inductive-inductive; source reals.tex727-735',
    verdict='OPTIONAL_LOGIC_SIZE_CONSTRUCTION_AND_EFFECTIVE_REAL_TASKS_SEPARATED')
(HERE/'EVIDENCE.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':'SOURCE_IDENTITIES_RECORDED','files':len(paths),'new_kernel_runs':0}))
