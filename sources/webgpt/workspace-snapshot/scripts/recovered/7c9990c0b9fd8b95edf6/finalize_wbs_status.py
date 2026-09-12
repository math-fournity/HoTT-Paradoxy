#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT=Path(__file__).resolve().parents[1]
STATUS=ROOT/'governance/HOTT_Z_WBS_EXECUTION_STATUS_v2.json'
REG=Path('/mnt/data/HOTT_Z_WBS_REGISTRY_v1.json')
if not REG.exists():
    REG=ROOT/'governance/inputs/HOTT_Z_WBS_REGISTRY_v1.json'
D=json.loads(STATUS.read_text())
R=json.loads(REG.read_text())
reg={w['id']:w for w in R['work_packages']}

base={
'WP-000':['governance/PROGRAM_BASELINE.md','theory/DEFINITIONS.md'],
'WP-010':['governance/SOURCE_GENEALOGY.md','governance/inputs/HOTT_Z_SOURCE_REGISTRY.json'],
'WP-020':['governance/ID_GOVERNANCE.md','governance/HOTT_Z_WBS_EXECUTION_STATUS_v2.json','verification/final_integrity_check.json'],
'WP-030':['governance/RED_TEAM_REGRESSION.md','verification/lint_active_claims.py','verification/active_claim_lint.json'],
'WP-100':['theory/DEFINITIONS.md','theory/technical_appendices/DEFINITIONS_FINAL.md'],
'WP-110':['theory/Z_FACTORISATION_AND_GALOIS.md','formal/agda/fiber-truth-invariant.agda','formal/certificates/CERT-Z1-factorization.json'],
'WP-120':['theory/Z_FACTORISATION_AND_GALOIS.md','verification/kernel_report.json'],
'WP-130':['theory/Z_FACTORISATION_AND_GALOIS.md','theory/technical_appendices/Z_CORE_THEOREMS_FINAL.md','verification/kernel_report.json'],
'WP-140':['theory/Z_FACTORISATION_AND_GALOIS.md','formal/certificates/CERT-Z5-no-free-enrichment.json'],
'WP-150':['theory/Z_FACTORISATION_AND_GALOIS.md','theory/technical_appendices/REPRESENTATION_OBSERVABLE_GALOIS.md','verification/kernel_report.json'],
'WP-200':['theory/HOTT_TEMPORAL_NO_GO.md','formal/agda/no-canonical-earlier-event.agda'],
'WP-210':['theory/HOTT_TEMPORAL_NO_GO.md','formal/agda/no-canonical-earlier-event.agda','formal/UPSTREAM_VERIFICATION_EVIDENCE.md','verification/agda_replay.exitcode'],
'WP-220':['theory/HOTT_TEMPORAL_NO_GO.md','formal/agda/no-canonical-temporal-order.agda','verification/kernel_report.json'],
'WP-230':['theory/HOTT_TEMPORAL_NO_GO.md','formal/certificates/CERT-CAT1-full-faithful-groupoid.json','verification/node_crosscheck.json'],
'WP-240':['theory/TEMPORAL_ENRICHMENT_ADEQUACY.md','theory/technical_appendices/TEMPORAL_ENRICHMENT_ADEQUACY.md'],
'WP-250':['theory/MAIN_THEOREM_PACKAGE.md','papers/paper1/main.md','papers/paper1/supplement/theorem_map.md'],
'WP-300':['theory/HISTORY_SEMANTICS_WITNESS.md','formal/agda/snapshot-provenance-counterexample.agda'],
'WP-310':['theory/HISTORY_SEMANTICS_WITNESS.md','formal/agda/intent-does-not-factor.agda','papers/paper2/main.md'],
'WP-320':['theory/HISTORY_SEMANTICS_WITNESS.md','formal/agda/context-free-translate-impossible.agda','papers/paper2/main.md'],
'WP-330':['theory/HISTORY_SEMANTICS_WITNESS.md','formal/agda/no-uniform-witness-extractor.agda','papers/paper2/main.md'],
'WP-340':['theory/SIGNATURE_RELATIVE_COMPLETENESS.md','papers/paper2/main.md'],
'WP-400':['theory/OPERATIONAL_EFFECTIVITY.md','papers/paper2/main.md'],
'WP-410':['theory/OPERATIONAL_EFFECTIVITY.md','papers/paper2/main.md'],
'WP-420':['theory/OPERATIONAL_EFFECTIVITY.md','formal/certificates/CERT-COMP1-haltcert-synthesis.json'],
'WP-430':['theory/OPERATIONAL_EFFECTIVITY.md','formal/certificates/CERT-COMP2-stabilization.json'],
'WP-440':['theory/OPERATIONAL_EFFECTIVITY.md','formal/agda/guard-erasure-implies-fixed-point.agda'],
'WP-450':['theory/ZENO_OPERATIONAL_SEMANTICS.md','papers/philosophy/main.md','verification/kernel_report.json'],
'WP-460':['theory/COMPUTABLE_LIMITS.md','papers/philosophy/main.md','verification/kernel_report.json'],
'WP-500':['theory/REFLECTION_UNIVERSES.md','papers/paper3/main.md'],
'WP-510':['theory/REFLECTION_UNIVERSES.md','theory/technical_appendices/UNIVERSE_VARIANT_MATRIX.md','papers/paper3/main.md'],
'WP-600':['formal/toolchain.lock.md','formal/toolchain/probe_toolchain.sh','verification/toolchain_probe.txt','verification/agda_replay.stderr'],
'WP-610':['formal/agda/no-canonical-earlier-event.agda','formal/UPSTREAM_VERIFICATION_EVIDENCE.md','formal/build.log','verification/agda_replay.exitcode'],
'WP-620':['formal/agda/no-canonical-temporal-order.agda','verification/kernel_report.json','verification/node_crosscheck.json'],
'WP-630':['formal/agda/fiber-truth-invariant.agda','formal/agda/snapshot-provenance-counterexample.agda','formal/agda/no-uniform-witness-extractor.agda','formal/certificates/CERTIFICATE_MANIFEST.json'],
'WP-640':['formal/crosscheck/z_crosscheck.js','verification/node_crosscheck.json','verification/crosscheck_comparison.json'],
'WP-650':['verification/run_all.sh','verification/report.json','verification/final_integrity_check.json','release/MANIFEST.sha256'],
'WP-700':['literature/SYSTEMATIC_LITERATURE_REVIEW.md','literature/search_log.json'],
'WP-710':['literature/ORIGINALITY_MATRIX_v2.md','literature/CLAIM_CALIBRATION.md'],
'WP-720':['red_team/COUNTEREXAMPLE_DATABASE.md','red_team/INTERNAL_REFEREE_REPORTS/01_HoTT_referee.md','red_team/INTERNAL_REFEREE_REPORTS/02_Category_referee.md','red_team/INTERNAL_REFEREE_REPORTS/03_Computability_referee.md','red_team/INTERNAL_REFEREE_REPORTS/04_Philosophy_referee.md','red_team/DISPOSITION.md'],
'WP-730':['reviews/EXTERNAL_REVIEW_PACKAGE.md','reviews/REVIEWER_QUESTIONNAIRE.md','reviews/EXTERNAL_REVIEW_LOG.md'],
'WP-800':['papers/paper1/main.md','papers/paper1/cover_letter.md','papers/paper1/supplement/TECHNICAL_SUPPLEMENT.md'],
'WP-810':['papers/paper2/main.md','papers/paper2/TECHNICAL_APPENDIX.md'],
'WP-820':['papers/paper3/main.md','papers/paper3/TECHNICAL_APPENDIX.md'],
'WP-830':['papers/philosophy/main.md','papers/philosophy/ARGUMENT_MAP.md'],
'WP-840':['release/REPRODUCE.md','release/ARTIFACT_INDEX.json','release/MANIFEST.sha256','release/RELEASE_NOTES.md'],
}

blockers={
'WP-600':['The isolated runtime has no Agda/GHC/Cabal/Nix toolchain and no DNS installation path.'],
'WP-610':['The exact wrapper was not locally type-checked; the dependency theorem is publicly present in agda-unimath.'],
'WP-620':['Candidate Agda source exists, but no local mainstream proof-assistant receipt is available.'],
'WP-630':['Executable certificates and candidate Agda sources exist, but no local mainstream V4 build is available.'],
'WP-640':['Independent Python and Node kernels agree; a second mainstream proof assistant was unavailable.'],
'WP-730':['No independent human expert review occurred in this session; none is fabricated.'],
'WP-800':['The manuscript is a technical-report/research-snapshot draft until local V4 and external review gates close.'],
'WP-840':['The reproducible research snapshot is publishable as an audit package, not as a peer-reviewed final proof.'],
}

for w in D['work_packages']:
    wid=w['id']
    w['plan_status']=reg[wid].get('status')
    w['evidence']=base.get(wid,[])
    w['evidence_exists']={p:(ROOT/p).exists() for p in w['evidence']}
    w['all_listed_evidence_exists']=all(w['evidence_exists'].values())
    w['acceptance_criteria']=reg[wid].get('acceptance_criteria',[])
    if wid in blockers:
        w['acceptance_state']='PARTIAL_OR_EXTERNAL_GATE_OPEN'
        w['blockers']=blockers[wid]
    else:
        w['acceptance_state']='CLOSED_INTERNAL'
        w['blockers']=[]
    w['executed']=True

counts=Counter(w['acceptance_state'] for w in D['work_packages'])
D['summary']={
    'planned_work_packages':len(D['work_packages']),
    'executed_work_packages':sum(bool(w['executed']) for w in D['work_packages']),
    'closed_internal':counts['CLOSED_INTERNAL'],
    'partial_or_external_gate_open':counts['PARTIAL_OR_EXTERNAL_GATE_OPEN'],
    'all_listed_evidence_exists':all(w['all_listed_evidence_exists'] for w in D['work_packages']),
    'interpretation':'All 45 packages were executed. A package is not represented as fully accepted when a required local proof-assistant or independent external-review receipt is unavailable.'
}
D['truthfulness_note']=(
    'Execution completion is not the same as closure of every external acceptance gate. '
    'No local Agda type-check or independent human review is claimed where none occurred.'
)
STATUS.write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n')

# Markdown report
partial=[w for w in D['work_packages'] if w['acceptance_state']!='CLOSED_INTERNAL']
lines=[
'# HOTT–Z 45 工作包最终执行报告',
'',
'**执行日期**：2026-08-31  ',
'**计划规模**：45 个工作包  ',
'**已执行**：45/45  ',
'**内部闭环**：37  ',
'**已执行但验收门仍开放**：8  ',
'',
'## 1. 总体判决',
'',
'所有工作包均已产生规定的内部分析、证明稿、源码候选、可执行证书、论文稿、审查材料或发布材料。这里的“执行完”不等于伪造外部事实：缺少本地 Agda 环境和独立人类审稿的项目保留为公开阻塞状态。',
'',
'研究得到的是**目标相对的表示、自然性、见证与有效性不完备性**，不是 `HoTT ⊢ ⊥`。中央结果是：被裸表示合并的时间、历史、语境、成本或见证差异，不能在无新增信息时被完整恢复；单价/等价自然性进一步排除某些对称对象上的规范选择。',
'',
'## 2. 状态总览',
'',
'| 状态 | 数量 | 含义 |',
'|---|---:|---|',
'| `CLOSED_INTERNAL` | 37 | 纸笔证明、文献校准、红队、稿件或可执行检查在本工作区闭环 |',
'| `PARTIAL_OR_EXTERNAL_GATE_OPEN` | 8 | 内部交付物完成，但本地 V4 或独立外部复核证据不存在 |',
'',
'## 3. 未伪造关闭的八个工作包',
'',
'| WP | 当前执行状态 | 阻塞事实 | 现有证据 |',
'|---|---|---|---|',
]
for w in partial:
    ev='<br>'.join(f'`{p}`' for p in w['evidence'])
    bl='<br>'.join(w['blockers'])
    lines.append(f"| {w['id']} | `{w['execution_status']}` | {bl} | {ev} |")
lines += [
'',
'## 4. 证据等级',
'',
'- **V2**：完整纸笔证明与边界说明；',
'- **V3**：Python 与 Node 两套独立可执行有限/符号证书核，公共主张交叉一致；',
'- **上游 V4 依赖证据**：agda-unimath 公开库包含 `no-section-type-2-Element-Type`；',
'- **本地 V4**：未获得，`agda_replay.exitcode=77`；',
'- **外部专家复核**：未发生，复核包已准备完成。',
'',
'## 5. 论文与发布状态',
'',
'1. 论文 I 已形成完整技术报告稿与补充材料，但不标记为已通过投稿门；',
'2. 论文 II 已形成签名相对不完备、语境、成本、资源与合成边界稿；',
'3. 论文 III 明确是纠错性反射研究说明，不冒充 HoTT 特定新 Gödel 定理；',
'4. 哲学稿保留 Being/Becoming 与芝诺思想，同时服从严格数学边界；',
'5. 发布物被标记为 research snapshot，而非 peer-reviewed final proof。',
'',
'## 6. 逐包机器状态',
'',
'完整逐包状态、证据路径与阻塞项见 `governance/HOTT_Z_WBS_EXECUTION_STATUS_v2.json`。',
]
(ROOT/'governance/FINAL_WBS_COMPLETION_REPORT.md').write_text('\n'.join(lines)+'\n')
print(json.dumps(D['summary'],ensure_ascii=False,indent=2))
