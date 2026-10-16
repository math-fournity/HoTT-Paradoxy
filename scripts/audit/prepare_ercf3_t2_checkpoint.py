#!/usr/bin/env python3
"""Prepare revision 54: record the T2 encoding-route result and route A11.1.

S054 ran the bounded T2 experiment: route (a) (ordinary inductive encoding)
carries the object-level syntax, capture-free substitution and a Hilbert
proof-predicate interface in the SAME layer using only Agda builtins (no
cubical features, no library imports); both --safe and --safe --without-K
checks exit 0.  P2/P3's syntactic layer therefore needs no extra level; the
QIIT/2LTT pressure belongs to P6 (self-application).  The next work package is
the A11.1 W51xRP-B01 propositionalisation; T3/T4 and the ERCF-3 body stay
gated.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-054-ERCF3-T2-ENCODING-ROUTE"
PREV_SESSION = "S-RES-20260912-053-ERCF3-PREREQUISITE-AUDIT"
RESULT_ID = "A-ERCF3-T2-ENCODING-ROUTE-001"
C8 = "理解章节/C8-ERCF-3前置评估与最小代理任务-20260912.md"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
MERGE_MANIFEST = "audit/understanding-chapter-merge-manifest.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
SRC = f"{SESSION_REL}/evidence/agda/ObjectSyntax.agda"
EVIDENCE = [
    SRC,
    f"{SESSION_REL}/evidence/agda/ObjectSyntax.check.stdout.txt",
    f"{SESSION_REL}/evidence/agda/ObjectSyntax.check.stderr.txt",
    f"{SESSION_REL}/evidence/agda/ObjectSyntax.check-withoutK.stdout.txt",
    f"{SESSION_REL}/evidence/agda/ObjectSyntax.check-withoutK.stderr.txt",
]
NEW_STATUS = "ERCF3_T2_ROUTE_A_VERIFIED_A111_PROPOSITIONALISATION_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_ercf3_t2", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sub_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"SUB_COUNT:{count}:{old[:80]}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000010": ("ALIGNED", "T2 仍是可行性/边界工作，不升级为内部矛盾。"),
        "KC-000012": ("DEEPENED", "资格问题在 T2 中具体化为：对象语法层可由最弱载体承载，压力只在自应用层。"),
        "KC-000013": ("ALIGNED", "理论工具性经济在 T2 中体现为：语法/替换/证明谓词接口不需要任何 cubical 特征。"),
        "KC-000021": ("ALIGNED", "T2 探针实际运行：--safe 与 --safe --without-K 均 EXIT=0。"),
        "KC-000025": ("ALIGNED", "自指构造的进展在 T2 后更精确：前置条件逐项关闭，自应用层仍需 P6。"),
        "KC-000026": ("DEEPENED", "自身自指问题在 T2 后分层：对象语法可同层完成，压力在类型论自身内部化。"),
        "KC-000028": ("DEEPENED", "自反验证回环的机器化路径推进一层：P2/P3 语法层不需要新增层级。"),
        "KC-000029": ("ALIGNED", "理论经济：用最弱载体承载语法层，避免过早引入表示代价。"),
        "KC-000031": ("ALIGNED", "最小理想理论覆盖问题仍需要 P8 或 HoTT 特有性证据。"),
        "KC-000035": ("ALIGNED", "对象层语法与自应用层代价被 T2 分开记录。"),
        "KC-000036": ("DEEPENED", "T3 预测为 GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC；ERCF-3 本体保持 gated。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    aligned = deepened = 0
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = touched.get(
            unit["id"],
            ("NOT_TOUCHED", "本轮是 S054 T2 编码路线实验；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S054/SESSION.md；{C8} | T3/T4 与其它域仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — T2 完成（路线 (a) 可行）；第一工作包转 A11.1 命题化；ERCF-3 与 T3/T4 保持 gated；revision 54/generation 038。",
        "- panorama_change: `YES` — `OUT-TOP-ERCF3-PREREQUISITE-ASSESSMENT` 原位更新 T2 结果；inventory 仍 33/24。",
        "- update_decision: `T2 探针证据进入 session evidence；C8 原位更新；merge manifest 重建；不新增 claim matrix 行。`",
        "- cross_conflicts: `NONE_OBSERVED` — T2 与 C4 §10 在层次上相容（压力在 P6）。",
        "- unresolved: `A11.1、T3/T4、P8、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `ERCF3_T2_ROUTE_A_VERIFIED`（无新数学 claim）。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S053 路由的第一工作包 T2（编码路线实验，有界可行性）。",
        "- 产出：`evidence/agda/ObjectSyntax.agda`：对象语法（var/num/+t；=f/bot/=>f/all）、无捕获替换（闭数字项替换 + 绑定遮蔽）、7 条结构引理、Hilbert 证明谓词接口（axK/axS/mp、Prov、prov-interface）。",
        "- 关键身份：仅使用 Agda.Builtin.{Nat,Equality,Bool}；无 cubical 特征、无库导入；--safe 与 --safe --without-K 均 EXIT=0、零 warning、stderr 0 字节。",
        "- 判定：路线 (a) 可行；P2/P3 语法层不需要新增层级；QIIT/2LTT 压力属于 P6（自应用）。T2 停止条件未触发。",
        "- 边界：替换代数完整定律、Gödel 编码、可表示性与对角引理为 T3 义务；不新增 claim matrix 行；不主张新数学结果。",
        "- 治理联动：C8 原位更新；merge manifest 重建 33/24；stale hash 由 checkpoint 事务修复。",
        "- 三件套：direction/panorama revision 54/generation 038；core 不变。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_ERCF3_PREREQUISITE_ASSESSED_T2_ENCODING_ROUTE_NEXT`",
        "状态：`CORE_GENERATION_4_ERCF3_T2_ROUTE_A_VERIFIED_A111_PROPOSITIONALISATION_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 53", "source_state_revision: 54")
    direction = sub_once(direction, "projection_generation: 20260912-direction-037", "projection_generation: 20260912-direction-038")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_ERCF3_PREREQUISITE_ASSESSED_T2_ENCODING_ROUTE_NEXT",
        "semantic_status: CORE_GENERATION_4_ERCF3_T2_ROUTE_A_VERIFIED_A111_PROPOSITIONALISATION_NEXT",
    )
    direction = sub_once(
        direction,
        "S053 把 ERCF-3 的 8 个前置条件、5 个代理任务与停止条件固定，并完成对角核机器核查；ERCF-3 本体保持 gated，下一步做 T2 编码路线实验 |",
        "S053 把 ERCF-3 的 8 个前置条件、5 个代理任务与停止条件固定并完成对角核机器核查；S054 完成 T2：路线 (a) 在纯 Agda builtins 下给出语法 + 无捕获替换 + 证明谓词接口（P2/P3 语法层不需要新增层级）；ERCF-3 本体保持 gated，下一步做 A11.1 命题化 |",
    )
    direction = sub_once(
        direction,
        "Code/quote/substitution/evaluation/provability 的固定工作已按 S053 的 P1–P8 前置表推进（L0 已资格化；L1 路线由 T2 决定）；抽象对角核（Lawvere + 无精确自编码）已机器核查；继续按 T2/T3 停止条件检验总停机/健全/完备/内部可证四者不可兼得的精确条件，不把一般 Gödel 口号冒充 HoTT 实例 |",
        "Code/substitution/provability 的固定工作已按 S053 的 P1–P8 前置表推进：L0 已资格化，S054 的 T2 证明路线 (a) 在纯 Agda builtins 下即可承载语法 + 无捕获替换 + 证明谓词接口；抽象对角核（Lawvere + 无精确自编码）已机器核查；T3 保持 gated 并预测为 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，不把一般 Gödel 口号冒充 HoTT 实例 |",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：T2 编码路线实验——在 (a) 普通归纳编码 + 算术化、(b) QIIT、(c) 2LTT 三条路线中确定哪条能在固定工具链中给出“语法 + 替换 + 证明谓词接口”的最小可通过片段；只做可行性，不写 Gödel 句；若 (a) 无法在无新增层级下完成而 (b)/(c) 需要分层，则记录 `SAME_LAYER_INTERNALIZATION_REQUIRES_STRATIFICATION` 并停止在该结论；ERCF-3 本体与 T3/T4 保持 gated，备选为 A11.1 W51×RP-B01 命题化。",
        "4. **当前第一工作包**：A11.1 W51×RP-B01 命题化——把 W51 命题（“HoTT 作为逻辑+几何+程序的系统继承而非豁免程序的计算界限”）写成精确命题，与 RP-B01 的已证/未证层（含 `MP-ERCF-001` 骨架与 N2 提取接口审计）逐项对应，并固定第三层（自然 Think-in-HoTT 交付提升）的缺口与验收判据；若只是通用边界重述则保持 `PARKED`。备选（ERCF 线）：T4 第五层 consumer 审计。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_ERCF3_PREREQUISITE_ASSESSED_T2_ENCODING_ROUTE_NEXT`",
        "状态：`CORE_GENERATION_4_ERCF3_T2_ROUTE_A_VERIFIED_A111_PROPOSITIONALISATION_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 53", "source_state_revision: 54")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-037", "projection_generation: 20260912-outcome-038")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_ERCF3_PREREQUISITE_ASSESSED_T2_ENCODING_ROUTE_NEXT",
        "semantic_status: CORE_GENERATION_4_ERCF3_T2_ROUTE_A_VERIFIED_A111_PROPOSITIONALISATION_NEXT",
    )
    panorama = sub_once(
        panorama,
        "；ERCF-3 本体保持 `GATED` |",
        "；S054 完成 T2：路线 (a) 在纯 Agda builtins 下承载对象语法 + 无捕获替换 + Hilbert 证明谓词接口（`--safe` 与 `--safe --without-K` 均 EXIT=0），P2/P3 语法层不需要新增层级；ERCF-3 本体保持 `GATED` |",
    )
    panorama = sub_once(
        panorama,
        "S053 把 ERCF-3 拆成 P1–P8/T1–T5 并完成对角核机器核查，判定其本体保持 gated；R032 回放、",
        "S053 把 ERCF-3 拆成 P1–P8/T1–T5 并完成对角核机器核查，判定其本体保持 gated；S054 完成 T2 编码路线实验（路线 (a)，纯 Agda builtins，无新增层级）并转 A11.1 命题化；R032 回放、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "判定 ERCF-3 本体保持 gated、强读法在编码层被通用对角核反驳。所有新结论继续执行 F-011。",
        "判定 ERCF-3 本体保持 gated、强读法在编码层被通用对角核反驳；S054 完成 T2 编码路线实验（路线 (a)，纯 Agda builtins，无 cubical 特征），P2/P3 语法层不需要新增层级。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | T2 编码路线实验 | 有界可行性（语法 + 替换 + 证明谓词接口） | 三路线选一；若需分层则记录 `SAME_LAYER_INTERNALIZATION_REQUIRES_STRATIFICATION` 并停止；T3/T4 保持 gated；备选 A11.1 |",
        "| 已闭合工作包 12 | T2 编码路线实验（S054） | route (a) verified / probe | `ObjectSyntax.agda`：语法 + 无捕获替换 + Hilbert 证明谓词接口，纯 Agda builtins，`--safe`/`--safe --without-K` EXIT=0；停止条件未触发；P2/P3 语法层不需要新增层级 |\n"
        "| 第一工作包 | A11.1 W51×RP-B01 命题化 | paper + 证据映射 | W51 写成精确命题并与 RP-B01 已证/未证层逐项对应；固定第三层缺口与验收判据；无进展则保持 PARKED；备选 T4 |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 T2 编码路线实验：在 (a) 普通归纳编码 + 算术化、(b) QIIT、(c) 2LTT 中选一条，做出可通过 kernel 的最小片段（语法 + 替换 + 一个证明谓词接口）；只做可行性，不写 Gödel 句；若需分层则记录 `SAME_LAYER_INTERNALIZATION_REQUIRES_STRATIFICATION` 并停止；ERCF-3 本体与 T3/T4 保持 gated，备选 A11.1。",
        "2. 当前第一工作包转为 A11.1 W51×RP-B01 命题化：把 W51 命题写成精确命题，与 RP-B01 的已证/未证层逐项对应，并固定第三层（自然 Think-in-HoTT 交付提升）的缺口与验收判据；若只是通用边界重述则保持 `PARKED`。备选（ERCF 线）：T4 第五层 consumer 审计。",
    )
    memory = sub_once(
        memory,
        "- N10 工具链/应用层交付审计（S052）：",
        "- S054 完成 T2 编码路线实验：`ObjectSyntax.agda`（纯 Agda builtins，无 cubical 特征、无库导入）给出对象语法 + 无捕获替换（7 条结构引理）+ Hilbert 证明谓词接口；`--safe` 与 `--safe --without-K` 均 EXIT=0、零 warning。路线 (a) 可行，P2/P3 语法层不需要新增层级，分层压力属于 P6（自应用）；C8 原位更新，merge manifest 重建 33/24；下一工作包转 A11.1 命题化，T3/T4 保持 gated。\n"
        "- N10 工具链/应用层交付审计（S052）：",
    )
    memory = sub_once(
        memory,
        "`A-ERCF3-PREREQUISITE-ASSESSMENT-001`。",
        "`A-ERCF3-PREREQUISITE-ASSESSMENT-001`、`A-ERCF3-T2-ENCODING-ROUTE-001`。",
    )
    memory = sub_once(
        memory,
        "S053 完成 ERCF-3 前置评估（P1–P8/T1–T5 + 对角核机器核查）并把 ERCF-3 本体保持 gated，转 T2 编码路线实验，不直接跳 ERCF-3 构造。",
        "S053 完成 ERCF-3 前置评估（P1–P8/T1–T5 + 对角核机器核查）并把 ERCF-3 本体保持 gated；S054 完成 T2 编码路线实验（路线 (a) 可行，语法层不需要新增层级）并转 A11.1 命题化，不直接跳 ERCF-3 构造。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S054 完成 T2 编码路线实验：`ObjectSyntax.agda`（仅 Agda builtins，无 cubical 特征/库导入）机器核查对象语法、无捕获替换（7 条结构引理）与 Hilbert 证明谓词接口（axK/axS/mp、Prov、prov-interface）；`--safe` 与 `--safe --without-K` 均 EXIT=0、零 warning。判定：路线 (a) 可行，P2/P3 语法层不需要新增层级，QIIT/2LTT 压力属于 P6（自应用）；停止条件未触发。C8 原位更新；merge manifest 重建 33/24；下一工作包为 A11.1 命题化，T3/T4 与 ERCF-3 本体保持 gated。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "52. ERCF-3 一类“理论为自身认证器开总完备证明”的要求，",
        "53. 前置任务的“同层可行性”应先用最弱载体检验：ERCF-3 的 P2/P3 语法层（对象语法、无捕获替换、Hilbert 证明谓词接口）在纯 Agda builtins（无 cubical 特征、无库导入）下即可通过 kernel，因此“需要 QIIT/2LTT”的压力只属于自应用层（把类型论自身内部化），不属于对象语法层。把“需要新层级”的判断推迟到它真正出现的那一层，可以避免用表示代价掩盖问题本身的层次结构。技术提示：定义用 if_then_else_ + rewrite 引理比多层嵌套 with 更稳；替换代数的完整定律应与可表示性一起留给同一后续任务。\n"
        "52. ERCF-3 一类“理论为自身认证器开总完备证明”的要求，",
    )
    return {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 53 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_53_AND_S053")
    if not (root / C8).is_file():
        raise SystemExit(f"C8_MISSING:{C8}")
    for rel in EVIDENCE:
        if not (root / rel).is_file():
            raise SystemExit(f"EVIDENCE_MISSING:{rel}")

    new_hashes = {rel: sha(root / rel) for rel in EVIDENCE}
    new_hashes[C8] = sha(root / C8)
    new_hashes[MERGE_MANIFEST] = sha(root / MERGE_MANIFEST)

    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = sha(path) if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    unexpected = sorted({rel for _, rel in observed_stale} - {MATRIX, FORMAL_README, RUNS_README, MERGE_MANIFEST, C8})
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE_PATHS:{unexpected}")
    note = (
        "Revalidated after the S054 T2 encoding-route experiment: C8 was updated in place and the understanding-chapter merge manifest "
        "was rebuilt (33/24); no proof source, run or claim-matrix row changed."
    )
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes.get(rel, sha(root / rel))
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "formal_feasibility_probe",
        "path": SRC,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "ERCF3_T2_ROUTE_A_VERIFIED",
        "research_parent": "A-ERCF3-PREREQUISITE-ASSESSMENT-001",
        "depends_on": ["A-ERCF3-PREREQUISITE-ASSESSMENT-001", "A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [*EVIDENCE, C8, MERGE_MANIFEST,
                         "scripts/audit/prepare_ercf3_t2_checkpoint.py"],
        "source_hashes": {C8: new_hashes[C8], MERGE_MANIFEST: new_hashes[MERGE_MANIFEST],
                          **{rel: new_hashes[rel] for rel in EVIDENCE}},
        "resolution": {
            "reason": "Route (a) carries the object-level syntax, capture-free substitution and a Hilbert proof-predicate interface in the same layer using only Agda builtins; both --safe and --safe --without-K checks exit 0 with zero warnings. The T2 stop condition was not triggered.",
            "evidence": [SRC, EVIDENCE[1], EVIDENCE[3], C8],
        },
        "scope": "Bounded feasibility probe for the ERCF-3 syntactic prerequisites (P2/P3): object syntax, capture-free numeral substitution with structural lemmas, and a Hilbert-style proof predicate interface, formalized without cubical features or library imports. No new mathematical claim; Goedel coding, representability and the diagonal lemma remain T3 obligations.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, C8, *EVIDENCE,
                         MERGE_MANIFEST, "scripts/audit/prepare_ercf3_t2_checkpoint.py"],
        "source_hashes": {C8: new_hashes[C8], MERGE_MANIFEST: new_hashes[MERGE_MANIFEST],
                          **{rel: new_hashes[rel] for rel in EVIDENCE}},
        "mathematical_status": "NO_NEW_MATHEMATICAL_CLAIM_T2_FEASIBILITY_PROBE",
        "cognition_status": "ERCF3_T2_ROUTE_A_VERIFIED_AND_A111_ROUTED",
        "scope": "T2 encoding-route experiment (route (a) verified as sufficient for the syntactic layer) and routing of the A11.1 propositionalisation.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-038" if rid.startswith("I-DIRECTION") else "20260912-outcome-038"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (SRC, C8, MERGE_MANIFEST):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after the T2 encoding-route experiment: route (a) is verified as sufficient for P2/P3's syntactic layer; the first work package is the A11.1 propositionalisation."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the T2 encoding-route result (route (a), no extra level at the syntactic layer); the next strand is A11.1."
    )

    state["revision"] = 54
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "A11.1 propositionalisation: state the W51 proposition precisely (HoTT as a logic+geometry+program system inherits rather than exempts program-level limits), "
            "map it item by item onto the RP-B01 proved/unproved layers (including the MP-ERCF-001 skeleton and the N2 extraction-interface audit), and fix the third-layer gap "
            "(natural Think-in-HoTT delivery lift) with acceptance criteria. If the statement merely re-derives the generic boundary, keep it PARKED. "
            "ERCF-3 body, T3 and T4 stay gated; the ERCF-line alternative is the T4 fifth-layer consumer audit."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "probe_kind": "ercf3_t2_encoding_route",
        "mathematical_claim_added": False,
        "claim_matrix_unchanged": True,
        "t2_probe": {
            "path": SRC,
            "sha256": new_hashes[SRC],
            "checks": {
                "--safe": {"exit": 0, "warnings": 0, "stdout_sha256": new_hashes[EVIDENCE[1]], "stderr_bytes": 0},
                "--safe --without-K": {"exit": 0, "warnings": 0, "stdout_sha256": new_hashes[EVIDENCE[3]], "stderr_bytes": 0},
            },
            "imports": ["Agda.Builtin.Nat", "Agda.Builtin.Equality", "Agda.Builtin.Bool"],
            "contents": [
                "object syntax (var/num/+t; =f/bot/=>f/all)",
                "capture-free substitution of closed numerals with bound-variable shadowing",
                "structural lemmas (num case, var-self, bot, all-shadowing, absent-variable cases, numeral-comm)",
                "Hilbert proof-predicate interface (axK/axS/mp, Prov, prov-interface)",
            ],
            "not_a_claim_package": True,
            "stop_condition_triggered": False,
        },
        "verdict": "ERCF3_T2_ROUTE_A_VERIFIED",
        "understanding_merge": {"top_level_files": 33, "nested_files": 24, "union_files": 33,
                                "top_level_unique": 9, "nonidentical_union_entries": 18,
                                "unresolved_nontrivial": 0},
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"assessment": C8, "session_evidence": f"{SESSION_REL}/evidence/"},
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    edited = apply_projection_edits(root)
    texts = {
        **edited,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session_text(),
        audit_path: audit_text(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. "
            "This in-scope checkpoint records the T2 encoding-route experiment (route (a) verified for the syntactic layer with a bounded probe), "
            "updates C8 in place, rebuilds the understanding-chapter merge manifest, and routes the A11.1 propositionalisation. "
            "No new mathematical claim, no Git commit, tag or push."
        ),
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
                "text": value,
            }
            for rel, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PREPARED",
        "snapshot": plan["snapshot"],
        "revision": 54,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
