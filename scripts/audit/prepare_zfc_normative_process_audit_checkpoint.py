#!/usr/bin/env python3
"""Prepare, but do not apply, the Q_norm process-audit checkpoint.

This builder records a narrow but durable change in the active F-053 line:
the user-normative `ZFC+Q_norm` completion-audit interface now has a pinned
Lean-core proof package.  It deliberately keeps the bare-ZFC C6 question open.

Apply the emitted payload only through the canonical writer:

  python3 -B .codex/tools/cognition_runtime.py checkpoint \\
    --snapshot <printed-snapshot> --payload <output> --apply
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".codex" / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import cognition_runtime as R
import projection_edit


SESSION_ID = "S-RES-20261005-ZFC-META-SUBTHEORY-QNORM-001"
PREVIOUS_SESSION = "S-RES-20261005-ZFC-META-SUBTHEORY-C5D-F-C0R3-001"
RUN_ID = "20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-02"
PROOF_ID = "MP-ZFC-NORMATIVE-PROCESS-AUDIT-001"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def current_text(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def mutable_with_shards(root: Path) -> list[str]:
    """Return every canonical mutable document and its current owned shards."""
    ordered: list[str] = []
    for rel in R.MUTABLE:
        if rel not in ordered:
            ordered.append(rel)
        index = R.parse_shard_index((root / rel).read_bytes(), rel)
        if index is not None:
            for row in index["shards"]:
                if row["path"] not in ordered:
                    ordered.append(row["path"])
    return ordered


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"REPLACE_COUNT:{label}:{count}")
    return text.replace(old, new, 1)


def add_current_frontier(text: str) -> str:
    marker = "## ZFC 元理论—子理论充分性主线（2026-10-05）"
    if marker in text:
        return text
    addition = """\n## ZFC 元理论—子理论充分性主线（2026-10-05）

- 当前最高优先是 `F-053` / `ZFC-META-SUBTHEORY-ADEQUACY-SOP`。bare ZFC 的核心问题仍要求一个同一 actual `M/S/Q/P/Bridge/Adequacy` contract，C6 未释放。
- `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` / C-370–C-374 已在 Lean 4.34.1 core 中把用户外加的 `ZFC+Q_norm` 过程审计接口固定下来：paid bridge、explicit task switch、missing bridge 分别得到 original/revised/bridge-required verdict，后二者不能被静默升格为 original。
- 该结果是规范性 extension 的机器证明，不是 bare ZFC 的对象语言定理、共同体政策或 C6 verdict。下一核心行动保持 `C0-SUCCESSOR-RESELECTION-003`；不要重做已完成的 strict-task-switch、proof-checker、generic Gödel 或 Q_norm interface 控制。
\n"""
    first_newline = text.find("\n")
    return text[: first_newline + 1] + addition + text[first_newline + 1 :]


def add_current_resume(text: str) -> str:
    marker = "## 当前 ZFC 元理论—子理论恢复点（2026-10-05）"
    if marker in text:
        return text
    addition = """\n## 当前 ZFC 元理论—子理论恢复点（2026-10-05）

1. 先加载 `认知闭包/ZFC-META-SUBTHEORY-ADEQUACY-001.md` 与 `ZFC-META-SUBTHEORY-ADEQUACY-SOP` 的全部分片，确认 C6 仍未释放。
2. `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` / C-370–C-374 已 version-closed pending current Git commit：它是 `ZFC+Q_norm` 的规范审计接口，不能被用作 bare ZFC 或同一实际 Q 的替身。
3. 接续核心线时只做 `C0-SUCCESSOR-RESELECTION-003`：寻找能支付或明确界定 physical `FormalDone ↔ OriginDone` 的 version-fixed source contract；新来源、actual bridge payment、SameQ_H0或用户重定原任务是重开/转向条件。
\n"""
    needle = "## 历史停止点"
    if needle not in text:
        raise SystemExit("RESUME_HISTORY_HEADING_MISSING")
    return text.replace(needle, addition + needle, 1)


def add_current_memory_queue(text: str) -> str:
    marker = "### `Q_norm` 规范性 extension（2026-10-05）"
    if marker in text:
        return text
    addition = """\n### `Q_norm` 规范性 extension（2026-10-05）

`MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` / C-370–C-374 已把研究发起人外加的
`ZFC+Q_norm` 过程完成审计固定为 Lean core contract：paid bridge 才能判
`originalResolved`；明确改题与 bridge 缺失分别得到 `revisedResolved` 与
`bridgeRequired`，后二者不能静默成为原任务完成。primary run `…-02` 含 source、
Lean binary digest、冻结矩阵行和 exact replay；首次 `…-01` 仅因 capture manifest 缺
binary pin 而未能版本闭合，已保留并由新的 run 取代。该结果是 extension，**不**是 bare
ZFC 的语法/模型/共同体政策或 C6 instance。核心状态仍为 actual `M/S/Q/P/Adequacy`
contract 未支付、C6 未释放；下一动作不变：`C0-SUCCESSOR-RESELECTION-003`。
\n"""
    needle = "## 想法 T：理论精度、观察边界与哥德尔式自反（2026-10-04）"
    if needle not in text:
        raise SystemExit("MEMORY_T_HEADING_MISSING")
    return text.replace(needle, addition + needle, 1)


def audit_text(root: Path) -> str:
    prior = current_text(
        root,
        f".codex/research/hott/sessions/{PREVIOUS_SESSION}/CORE_COGNITION_AUDIT.md",
    )
    table_start = prior.index("| KC |")
    table = prior[table_start:]
    replacements = {
        "C5D–C5F, C0R2/C0R3 and normative-extension admission; process-observation positive control and physical-bridge source boundary; no core machine theorem.": "dedicated ZFC+Q_norm process-completion audit interface; source-to-spec binding, Lean-core theorem/run/index closure and capture-pipeline repair; no bare-ZFC C6 theorem.",
        "- core_change: NO — 本单元没有新的用户元数学原文，不修改 core generation。\n- direction_change: YES — C5D–C5F加入构造性／hybrid-Zeno正控制；F-A取得SEP physical-bridge requirement；下一选择变为C0-SUCCESSOR-RESELECTION-003。\n- panorama_change: NO — 本单元重放既有C-359/C-361/C-362/C-364控制，未新增数学claims matrix行。\n- essay_change: NO — 未修改扩展认知。\n- update_decision: 写回C5D/C5E/C5F、C0R2/C0R3、C6 admission、normative extension admission、source snapshots与当前owners。\n- cross_conflicts: SEP要求physical applicability，hybrid source将过程积累诊断为模型不完整，而当前set-theoretic foundation sources未把这项审计直接赋给bare ZFC；三层必须分开。\n- unresolved: actual same M/S/Q/P/Adequacy contract、physical bridge payment、SameQ_H0、qualified Mizar/Isabelle replay和C6 core verdict仍未支付。": "- core_change: NO — 本单元没有新的用户元数学原文，不修改 core generation。\n- direction_change: YES — F-053 的 extension lane 从“准入/重放控制”变成有独立 C-370–C-374 package 的 `Q_NORM_EXTENSION_MACHINE_PROVED_WITH_SCOPE`；核心下一动作仍为 C0-SUCCESSOR-RESELECTION-003。\n- panorama_change: YES — 新增 `OUT-U-ZFC-NORMATIVE-PROCESS-AUDIT-C370-C374`，但明确标为 extension，不是 C6 结果。\n- essay_change: NO — 未修改扩展认知。\n- update_decision: 写回专用 proof package、claim matrix、registry、run、capture-pipeline repair、F-053、closure、MEMORY、方向/全景投影、C6 admission和新 session。\n- cross_conflicts: Q_norm 是研究发起人规范；C5E/C0R3说明 application bridge 是真实可问的问题，但现有 bare-ZFC sources并未把该规范指定为其职责。规范可机器化，不等于 bare-ZFC 已实例化。\n- unresolved: actual same M/S/Q/P/Adequacy contract、physical bridge payment、SameQ_H0、qualified Mizar/Isabelle replay和C6 core verdict仍未支付。",
        "- C5D：constructive foundations把 construction/admissibility作为对象与证明准入的实际来源维度，但不等于有限物理时间。\n- C5E：Maddy/SEP给出 foundation proof/risk/representation 与 application target/accuracy 的责任分层。\n- C5F：Berkeley hybrid systems将有限时间无限离散跃迁当作抽象模型不完整性，并需要post-Zeno状态。\n- C0R3：SEP明确纯数学解答不足以回答physical Zeno question；bridge须由物理适用性另行支付。\n- C-359/C-361/C-362/C-364均已本轮 exact rerun；它们仍是条件性或source-bound controls，不是bare-ZFC core verdict。": "- `Q_norm`：`CompletionContract`把 formal/origin completion 与 bridge status 分开；paid / explicitTaskSwitch / missing 三分 verdict 被 Lean core 实际检查。\n- C-370–C-374：original verdict 的 soundness、task switch和missing bridge的反偷换、paid正控制与missing负控制均有冻结 run和exact replay。\n- capture repair：第一次 `…-01` 缺 Lean binary manifest pin，被proof-version verifier拒绝；新的 `…-02` 以修复后的 generic capture 重新捕获和冻结。\n- C5E/C5F/C0R3继续提供此规范的来源背景和正控制，但不把 Q_norm 转成 bare-ZFC source role。\n- C6仍未释放：没有 actual same M/S/Q/P/Adequacy contract。",
        "| `KC-000011` | 时序与程序可表示性不等于理论自动保留过程合同。 | `ALIGNED` | C1C positive infrastructure control。 | 保留 representation/control 区分。 |": "| `KC-000011` | `FormalDone`可表示或可判定，不等于可把它合法提升为`OriginDone`；新 audit把这一差别写成显式 bridge field。 | `ALIGNED` | C-370–C-374；Q_norm package audit。 | actual source仍须支付。 |",
        "| `KC-000012` | ASK 被用于检查 P 是否有同一任务资格。 | `ALIGNED` | C3A/C5C task-switch audit。 | bridge 未付时不升级。 |": "| `KC-000012` | ASK 被用于检查 promotion是否付出同一任务 bridge；新 audit明确把改题和缺 bridge分开。 | `ALIGNED` | C-371/C-372；C5C。 | actual bridge未付时不升级。 |",
        "| `KC-000014` | B 向“理论假装完成”被检查，但此来源公开 revised task。 | `ALIGNED` | C5C. | 新 source 才可能重开 failure route。 |": "| `KC-000014` | B 向“理论假装完成”在规范层获得精确防线：revised task 和 missing bridge均不能获得 original verdict。 | `ALIGNED` | C-371/C-372/C-374。 | 这不判当前bare-ZFC practice。 |",
        "| `KC-000021` | 机器证明要求被保留；本 leaf未伪造 C6 theorem。 | `ALIGNED` | no C6 claim; existing controls replayed。 | 仅 source-to-spec closure后运行kernel。 |": "| `KC-000021` | 机器证明门禁落实为专用source/run/index/freeze/exact-replay链；它严格不伪造C6 theorem。 | `ALIGNED` | C-370–C-374；RUN.json；proof registry。 | C6仍须source-to-spec closure。 |",
        "| `KC-000044` | 现实对齐作为解释任务，未被否认。 | `ALIGNED` | C5B model-target criterion。 | target contract must be explicit。 |": "| `KC-000044` | 现实对齐要求被翻译为`FormalDone → OriginDone` bridge审计；规范接口不自行宣布任何现实对应已付。 | `ALIGNED` | Q_norm package CLAIM；C5B/C0R3。 | target contract仍须actual source。 |",
        "| `KC-000045` | 现实诠释中定位舍弃前提的要求已由 bridge table落实。 | `ALIGNED` | C5A–C5C tables。 | preserve input/operation/observation/Done. |": "| `KC-000045` | 现实诠释中的完成替换被专用审计分类为 paid bridge、task switch或missing bridge。 | `ALIGNED` | C-370–C-374；package audit §2。 | 不能从分类反推实际source。 |",
        "| `KC-000059` | 时间、存在、自指模式P保持，但本轮不制造 P 结论。 | `ALIGNED` | C0/C5 source controls。 | direct P source needed. |": "| `KC-000059` | 时间化过程完成的追问被写成Q_norm audit，但不存在性/自指模式P没有被偷偷当成已证bare-ZFC实例。 | `ALIGNED` | Q_norm package scope；C6 admission。 | direct actual P/source仍需。 |",
        "| `KC-000061` | 工作意识已写回 closure/MEMORY/Feature。 | `ALIGNED` | current owner updates。 | future sessions reload. |": "| `KC-000061` | 工作意识已写回 closure/MEMORY/Feature/方向/全景/STATE；capture缺口也保留为可审计修复，而非静默覆盖。 | `ALIGNED` | package audit §5；current owners。 | future sessions reload exact package boundary. |",
    }
    head = prior[:table_start]
    for old, new in replacements.items():
        if old in head:
            head = replace_once(head, old, new, "audit-head")
        else:
            table = replace_once(table, old, new, "audit-row")
    head = head.replace(PREVIOUS_SESSION, SESSION_ID)
    return head + table


def update_direction(root: Path, texts: dict[str, str], revision: int) -> None:
    doc = projection_edit.load(root, "方向追踪.md")
    projection_edit.replace_in_index(doc, "版本：`integrated-direction-portfolio/v1.19`", "版本：`integrated-direction-portfolio/v1.20`")
    projection_edit.replace_in_index(doc, "日期：2026-10-02", "日期：2026-10-05")
    projection_edit.replace_in_index(doc, "状态：`MO3_C_PARENT_SCOPE_INCOMPLETE`", "状态：`F053_CORE_ADEQUACY_ACTIVE / C6_NOT_RELEASED`")
    projection_edit.replace_in_index(doc, "source_state_revision: 298", f"source_state_revision: {revision}")
    projection_edit.replace_in_index(doc, "projection_generation: 20261002-direction-onepass-298", f"projection_generation: 20261005-zfc-normative-process-audit-{revision}")
    projection_edit.replace_in_index(doc, "semantic_status: MO3_C_PARENT_SCOPE_INCOMPLETE", "semantic_status: F053_CORE_ADEQUACY_ACTIVE / C6_NOT_RELEASED")
    anchor = "| `DIR-U-BARE-ZFC-Q-PRECISION` | bare ZFC 的理论精度／观察力：检验一个 foundation-facing completion interface 是否原生要求区分 FormalDone／OriginDone、支付 bridge、拒绝未支付完成提升 | 研究发起人 2026-10-03/04 直接纠正；KC-000003、KC-000018、KC-000059；F-049 | `CLOSED_WITH_SCOPE / SOURCE_APPLICATION_INTERFACE_CONTROL_COMPLETE / BARE_SEMANTIC_INTERFACE_UNDERDETERMINED` | `ZENO`、`RUSSELL`、`COMPUTATIONAL_LEGITIMACY`、`THEORY_ECONOMY`、`EVIDENCE_DISCIPLINE` | `OUT-U-BARE-ZFC-Q-PRECISION-C364` | P0/P1/P3 固定：SEP 给语言与可编码性控制，IEP 给 application-level resolution owner，Norton 明示 task switch；C-364 只对固定 application view 证明 Q 精度边界。重开仅为实际来源将 bare-ZFC formal acceptance 直接抬升为原过程／物理完成而未给 bridge，或用户指定新的 OriginDone。 | `audit/20261004-BARE-ZFC-Q-PRECISION-P0-P3-来源接口与完成合同.md`；`HoTT/formal/bare-zfc-q-precision/CLAIM.md`；C-364 |"
    row = "| `DIR-U-ZFC-META-SUBTHEORY-ADEQUACY` | bare ZFC 或明确 ZFC-founded foundation context 对其连续统／极限子理论的 `FormalDone → OriginDone` 提升是否承担并实际履行 bridge 审查责任；并把用户提出的 `Q_norm` 与 bare-ZFC evidence line 严格分开 | 研究发起人 2026-10-04 的不停机Goal；F-053；KC-000003、KC-000018、KC-000059 | `ACTIVE_CORE_RESEARCH / C0_UNIVERSE_FROZEN / Q_NORM_EXTENSION_MACHINE_PROVED_WITH_SCOPE / SAME_ACTUAL_M_S_P_ADEQUACY_CONTRACT_UNPAID / C6_NOT_RELEASED` | `ZENO`、`RUSSELL`、`COMPUTATIONAL_LEGITIMACY`、`THEORY_ECONOMY`、`EVIDENCE_DISCIPLINE` | `OUT-U-ZFC-NORMATIVE-PROCESS-AUDIT-C370-C374`；C1/C5/C0R3 source cards | `Q_norm` 已作为 extension 写成C-370–C-374；核心下一步保持`C0-SUCCESSOR-RESELECTION-003`，只选择能改变 actual physical `FormalDone ↔ OriginDone` bridge的version-fixed source。C6只在同一M/S/Q/P/Bridge/Adequacy contract付清后释放。 | `dev-docs/ZFC元理论子理论充分性最终闭环SOP.md`；`认知闭包/ZFC-META-SUBTHEORY-ADEQUACY-001.md`；`audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-NORMATIVE-PROCESS-AUDIT-PACKAGE.md`；F-053 |"
    projection_edit.replace_in_shard(doc, "方向追踪/002 - 治理与用户方向.md", anchor, anchor + "\n" + row)
    texts["方向追踪.md"] = doc["index_text"]
    texts.update(doc["shards"])


def update_panorama(root: Path, texts: dict[str, str], revision: int) -> None:
    doc = projection_edit.load(root, "全景视野.md")
    projection_edit.replace_in_index(doc, "版本：`integrated-outcome-panorama/v1.20`", "版本：`integrated-outcome-panorama/v1.21`")
    projection_edit.replace_in_index(doc, "日期：2026-10-02", "日期：2026-10-05")
    projection_edit.replace_in_index(doc, "状态：`MO3_C_PARENT_SCOPE_INCOMPLETE`", "状态：`F053_CORE_ADEQUACY_ACTIVE / C6_NOT_RELEASED`")
    projection_edit.replace_in_index(doc, "source_state_revision: 298", f"source_state_revision: {revision}")
    projection_edit.replace_in_index(doc, "projection_generation: 20261002-outcome-onepass-298", f"projection_generation: 20261005-zfc-normative-process-audit-{revision}")
    projection_edit.replace_in_index(doc, "semantic_status: MO3_C_PARENT_SCOPE_INCOMPLETE", "semantic_status: F053_CORE_ADEQUACY_ACTIVE / C6_NOT_RELEASED")
    anchor = "| `OUT-U-BARE-ZFC-Q-PRECISION-C364` | `MP-BARE-ZFC-Q-PRECISION-001` / C-364：固定两 completion-contract worlds 共享同一个 coarse standard-resolution view，却有相反 OriginDone；该 view 不能决定 OriginDone 或支付 universal completion bridge，rich contract view 与 finite code view 是正控制 | `DIR-U-BARE-ZFC-Q-PRECISION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | SEP/IEP/Norton 来源卡 + Lean 4.34.1 core | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_BOUND_APPLICATION_VIEW / BARE_SEMANTIC_INTERFACE_UNDERDETERMINED` | 固定 ZFC-supported Standard Solution application control 需要额外 contract 信息才能忠实决定 OriginDone；主 run exit 0、stderr 0、十条定理无公理、精确重放一致，negative control拒绝 coarse decoder | 不形式化 bare ZFC 的语法／模型／一致性；不证明 ZFC 不能编码时间或过程，不证明所有标准解法遗漏 Q，也不证明与 HoTT Q 是同一个完整任务 | `HoTT/formal/bare-zfc-q-precision/CLAIM.md`；`HoTT/verification/runs/20261004-MP-BARE-ZFC-Q-PRECISION-001-03/`；`audit/20261004-BARE-ZFC-Q-PRECISION-P0-P3-来源接口与完成合同.md`；C-364 |"
    row = "| `OUT-U-ZFC-NORMATIVE-PROCESS-AUDIT-C370-C374` | `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001`：研究发起人显式 `ZFC+Q_norm` completion-audit interface；paid bridge才可输出 original resolution，explicit task switch和missing bridge分别输出 revised / bridge-required，后二者不能静默成为original | `DIR-U-ZFC-META-SUBTHEORY-ADEQUACY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | 用户Q_norm规范 + C5E/C5F/C0R3 source cards + Lean 4.34.1 core | `KERNEL_ACCEPTED_WITH_SCOPE / NORMATIVE_FORMAL_SPECIFICATION / VERSION_CLOSED_PENDING_CURRENT_GIT_COMMIT` | 12条 selected theorem无公理、primary run exit 0/stderr 0、source/Lean-binary digest/index rows均冻结、exact rerun通过；规范接口可区分支付、改题和缺失 | 不证明bare ZFC已拥有/违反Q_norm，不证明数学共同体政策、IEP/Norton历史文本、SameFullQ、物理完成或ZFC对象语言矛盾；不能代替C6 | `HoTT/formal/zfc-normative-process-audit/CLAIM.md`；`HoTT/verification/runs/20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-02/`；`audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-NORMATIVE-PROCESS-AUDIT-PACKAGE.md`；C-370–C-374 |"
    projection_edit.replace_in_shard(doc, "全景视野/003 - 当前机器证明包与原生重放.md", anchor, anchor + "\n" + row)
    texts["全景视野.md"] = doc["index_text"]
    texts.update(doc["shards"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT.resolve()
    plan = R.plan(root, profile="research")
    if (root / f".codex/research/hott/sessions/{SESSION_ID}").exists():
        raise SystemExit("SESSION_ALREADY_EXISTS")

    texts = {rel: current_text(root, rel) for rel in mutable_with_shards(root)}
    prior_state = json.loads(texts[R.STATE])
    revision = prior_state["revision"] + 1
    update_direction(root, texts, revision)
    update_panorama(root, texts, revision)
    texts["MEMORY/001 - 当前执行队列.md"] = add_current_memory_queue(texts["MEMORY/001 - 当前执行队列.md"])
    texts[".codex/research/hott/FRONTIER.md"] = add_current_frontier(texts[".codex/research/hott/FRONTIER.md"])
    texts[".codex/research/hott/RESUME.md"] = add_current_resume(texts[".codex/research/hott/RESUME.md"])

    log_path = "MEMORY/003 - 当前验证状态与顺序日志.md"
    log_entry = (
        f"\n\n{SESSION_ID}：`{PROOF_ID}` / C-370–C-374 将用户的 `ZFC+Q_norm` 过程完成审计固定为 Lean core contract。"
        "primary run `…-02` 的 source、Lean binary digest、matrix行与exact replay均通过；初次`…-01`因capture manifest缺binary pin被版本闭合检查拒绝，保留为pipeline receipt并以修复后的`…-02`取代。"
        "结果是规范性extension，C6 bare-ZFC core contract仍未释放；下一动作`C0-SUCCESSOR-RESELECTION-003`。"
    )
    if SESSION_ID not in texts[log_path]:
        texts[log_path] += log_entry + "\n"

    source_paths = [
        "sources/prompts/Codex-ZFC核心层最终机器证明与不停机Goal-用户原文-20261004.md",
        "sources/prompts/Codex-ZFC元理论子理论时间与完成桥-用户原文-20261003.md",
        "dev-docs/ZFC元理论子理论充分性最终闭环SOP.md",
        "认知闭包/ZFC-META-SUBTHEORY-ADEQUACY-001.md",
        "feature-list.md",
        "HoTT/formal/zfc-normative-process-audit/ProcessCompletionAudit.lean",
        "HoTT/formal/zfc-normative-process-audit/CLAIM.md",
        "HoTT/formal/zfc-normative-process-audit/LEAN_CORE_TOOLCHAIN.json",
        f"HoTT/verification/runs/{RUN_ID}/RUN.json",
        f"HoTT/verification/runs/{RUN_ID}/source-manifest.json",
        f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
        "HoTT/CLAIM_EVIDENCE_MATRIX.md",
        "HoTT/verification/PROOF_VERSION_CLOSURE.json",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-NORMATIVE-PROCESS-AUDIT-PACKAGE.md",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-NORMATIVE-PROCESS-AUDIT-EXTENSION-ADMISSION.md",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C6-ENTRY-ADMISSION-REVIEW.md",
    ]
    state = prior_state
    state["revision"] = revision
    state["latest_session"] = SESSION_ID
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "Q_NORM_EXTENSION_MACHINE_PROVED_WITH_SCOPE / CORE_C6_NOT_RELEASED",
        "full_sources": source_paths,
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
        "path_mode": "document",
        "related_records": [PREVIOUS_SESSION],
        "scope": "Dedicated Lean-core formalization of the user-normative ZFC+Q_norm process-completion audit. It kernel-checks paid bridge / explicit task switch / missing bridge verdicts and their controls; it does not supply an actual bare-ZFC M/S/Q/P/Adequacy contract or release C6.",
        "source_hashes": {path: sha((root / path).read_bytes()) for path in source_paths},
        "status": "complete",
    }
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    session_base = f".codex/research/hott/sessions/{SESSION_ID}/"
    texts[session_base + "SESSION.md"] = f"""# {SESSION_ID}

> **Role:** `RESEARCH_GENERATION`.
> **Tier:** `T3` — user-normative process-completion extension proof and source-to-spec/pipeline audit; no C6 core theorem.

## 研究对象

把研究发起人提出的 `Q_norm` 明确写成 `CompletionContract`：理论或应用在报告原任务完成前，必须给出 paid `FormalDone → OriginDone` bridge；若明示改题，则只报告 revised task；若bridge缺失，则保留 bridge-required obligation。

## 实际结果

- `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` / C-370–C-374 在 Lean 4.34.1 core 实际通过；12条 selected theorem的axiom report均为空。
- primary run `{RUN_ID}` 保存了源码、来源/规范卡、toolchain和Lean binary digest；freeze后的 exact rerun通过。
- 第一次 `…-01` capture缺少binary pin，proof-version verifier拒绝版本闭合；捕获器修复后以独立目录 `…-02` 重跑。该修复改变的是证据完整性，不改变数学命题。
- Q_norm是规范性extension；C6仍无同一 actual `M/S/Q/P/Bridge/Adequacy` contract，bare-ZFC核心判词仍未产生。

## successor

`C0-SUCCESSOR-RESELECTION-003`：只寻找能支付或明确界定physical `FormalDone ↔ OriginDone` bridge的版本固定实际source；不重做本 package、strict-task-switch、ZF infrastructure、proof checker或generic Gödel controls。
"""
    texts[session_base + "RUNS.json"] = json.dumps({
        "next": "C0-SUCCESSOR-RESELECTION-003: locate an actual version-fixed source contract that pays or explicitly delimits a physical FormalDone ↔ OriginDone bridge.",
        "role": "RESEARCH_GENERATION",
        "schema_version": "hott-research-runs/v1",
        "session_id": SESSION_ID,
        "status": "Q_NORM_EXTENSION_MACHINE_PROVED_WITH_SCOPE_NO_CORE_C6",
        "tier": "T3",
        "verification": [
            {
                "command": f"python3 -B scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/{RUN_ID} --rerun",
                "scope": "exact Lean command/source/output/index replay for C-370–C-374",
                "status": "PASS_WITH_SCOPE",
            },
            {
                "command": f"python3 -B scripts/audit/verify_proof_version_closure.py --proof-id {PROOF_ID} --evidence-only",
                "scope": "source manifest, pinned Lean binary, primary run/index-row relation and registry binding",
                "status": "LOCAL_EVIDENCE_PASS_NOT_VERSION_CLOSED",
            },
            {
                "command": "C6 admission re-read",
                "scope": "Q_norm extension cannot substitute for actual bare-ZFC M/S/Q/P/Bridge/Adequacy source contract",
                "status": "NOT_RELEASED",
            },
        ],
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    texts[session_base + "CORE_COGNITION_AUDIT.md"] = audit_text(root)

    rows = []
    for rel in sorted(texts):
        target = root / rel
        rows.append({
            "path": rel,
            "expected_sha256": sha(target.read_bytes()) if target.is_file() else None,
            "text": texts[rel],
        })
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User explicitly authorized continued ZFC meta/subtheory work, durable documentation, exact-path commits, and remote push; this checkpoint preserves the Q_norm extension result without closing the core Goal.",
        "load_profile": "research",
        "task_ids": [],
        "files": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PREPARED",
        "snapshot": plan["snapshot"],
        "revision": revision,
        "session_id": SESSION_ID,
        "files": len(rows),
        "proof_id": PROOF_ID,
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
