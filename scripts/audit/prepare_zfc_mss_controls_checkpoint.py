#!/usr/bin/env python3
"""Prepare, but do not apply, the C0R8 MSS representation-controls checkpoint.

The checkpoint records two source-motivated Lean-core controls and the resulting
C0 successor.  It deliberately preserves the distinction between an actual
consumer seed and a bare-ZFC M/S/Q/P/Bridge/Adequacy contract.
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


SESSION_ID = "S-RES-20261005-ZFC-META-SUBTHEORY-C0R8-MSS-CONTROLS-001"
PREVIOUS_SESSION = "S-RES-20261005-ZFC-META-SUBTHEORY-QNORM-VERSION-CLOSURE-001"
DOMAIN_PROOF = "MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001"
DOMAIN_RUN = "20261005-MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001-03"
ORDER_PROOF = "MP-ZFC-MSS-PHASE-ORDER-CONTROL-001"
ORDER_RUN = "20261005-MP-ZFC-MSS-PHASE-ORDER-CONTROL-001"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def current_text(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def mutable_with_shards(root: Path) -> list[str]:
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


def prepend_once(text: str, marker: str, addition: str) -> str:
    if marker in text:
        return text
    first_newline = text.find("\n")
    return text[: first_newline + 1] + addition + text[first_newline + 1 :]


def replace_table_row(text: str, kc: str, replacement: str) -> str:
    prefix = f"| `{kc}` |"
    rows = text.splitlines()
    found = [index for index, row in enumerate(rows) if row.startswith(prefix)]
    if len(found) != 1:
        raise SystemExit(f"KC_ROW_COUNT:{kc}:{len(found)}")
    rows[found[0]] = replacement
    return "\n".join(rows) + "\n"


def audit_text(root: Path) -> str:
    prior = current_text(
        root,
        f".codex/research/hott/sessions/{PREVIOUS_SESSION}/CORE_COGNITION_AUDIT.md",
    )
    table_start = prior.index("| KC |")
    table = prior[table_start:]
    rows = {
        "KC-000003": "| `KC-000003` | 稠密性／合取前提保持为研究动机；本轮将时间相关表示拆为 domain carrier、parameter order 与 operation consumer，未把任一控制升级为物理反证。 | `ALIGNED` | C-375–C-378；C0R8 source cards。 | actual Q/bridge仍须来源支付。 |",
        "KC-000004": "| `KC-000004` | 反证式回溯保持开放；C0R8只得到表示控制和 source operational caveat，没有把它写成bare-ZFC矛盾。 | `ALIGNED` | C0R8 real consumer screen §4。 | 需同一M/S/Q/P/Adequacy contract。 |",
        "KC-000006": "| `KC-000006` | 时间机制不被收窄为稠密性：carrier/domain、parameter/order、practical operation三层被明确分开。 | `DEEPENED` | C-375/C-376；C-377/C-378；C0R8 cards。 | 不同层须各自有source/task payment。 |",
        "KC-000010": "| `KC-000010` | 现实相对非现实性不被混成内部矛盾；两个Lean包只证明固定表示控制。 | `ALIGNED` | 两个 package CLAIM.md。 | actual physics bridge仍开放。 |",
        "KC-000011": "| `KC-000011` | 时序不是仅有time variable：`C-377/C-378`给出 parameter order与state range的可检验差异。 | `DEEPENED` | phase-order source-to-spec control。 | actual phase-space semantics不可由有限control代替。 |",
        "KC-000012": "| `KC-000012` | ASK用于问一个形式重述是否仍能支付原操作/观察；source的not-operational caveat保留为候选，不强行当作Done。 | `ALIGNED` | da Costa--Sant'Anna thermodynamics screen。 | fixed task仍缺。 |",
        "KC-000013": "| `KC-000013` | 理论工具性与计算合法性张力保持：逻辑 eliminability、state description与operation consumer不可互相替代。 | `DEEPENED` | C0R8 real consumer screen。 | 未形成bare-ZFC实例。 |",
        "KC-000015": "| `KC-000015` | 抽象导致非现实性仍是研究立场；本轮用反控制防止把抽象重述本身误判为悖论。 | `ALIGNED` | C-375/C-377 positive controls。 | actual unsuitable abstraction仍需source/task证据。 |",
        "KC-000018": "| `KC-000018` | 不把ZFC写成无时间：source和C-375均显示可恢复time carrier；问题收紧为特定projection与consumer是否保真。 | `CORRECTED` | C-375；C0R8 source cards。 | 不得作语言缺失外推。 |",
        "KC-000019": "| `KC-000019` | 稠密空间仍是用户哲学背景；本轮没有把有限Bool controls说成连续时空结论。 | `ALIGNED` | two package non-goals。 | continuous task needs separate contract。 |",
        "KC-000044": "| `KC-000044` | 现实对齐落实为检查representation是否保留实际consumer的observation；not-operational source caveat被保留但未夸张。 | `DEEPENED` | real consumer screen §2–§4。 | operational task must be source-defined。 |",
        "KC-000045": "| `KC-000045` | 理论经济性可能舍弃何种数据，被具体分为primitive name、domain carrier、parameter order和operation contract。 | `DEEPENED` | C-375–C-378；C0R8 cards。 | 哪一层构成不合理仍需same-task proof。 |",
        "KC-000047": "| `KC-000047` | 合取前提与理论经济只作为候选归因；本轮正反表示控制限制归因过强。 | `ALIGNED` | C-375/C-376；C-377/C-378。 | actual M/S/Q/P missing。 |",
        "KC-000048": "| `KC-000048` | 针对性策略得到细化：必须先固定被遗忘的是carrier、order还是consumer contract，再设计敏感过程。 | `DEEPENED` | C0R8 taskcards 008/009。 | 不做无靶枚举。 |",
        "KC-000054": "| `KC-000054` | UR仍要求原本简单任务在理论中做不到；C0R8尚未得到source-fixed UR，只得到候选观察边界。 | `ALIGNED` | real consumer screen verdict。 | Q未固定时禁止声称UR。 |",
        "KC-000056": "| `KC-000056` | 目标仍是基础理论级问题；MSS/thermodynamics只作可能将基础和物理消费者接合的探针。 | `ALIGNED` | F-053 / C0 manifest。 | 不把单一控制当核心靶。 |",
        "KC-000058": "| `KC-000058` | 内在知识用于提出MSS位置，原始论文、PDF页、source card和Lean kernel共同裁决。 | `ALIGNED` | 2001/2014 snapshots；C-375–C-378。 | neural match不是证据。 |",
        "KC-000059": "| `KC-000059` | P的时间/计算张力获得两种结构化测试：carrier recovery与order erasure；存在性/自指仍未被假装支付。 | `DEEPENED` | C0R8 source-to-spec controls。 | 仍需actual P/Q source。 |",
        "KC-000060": "| `KC-000060` | 从明显承诺出发得到MSS domain/time与phase parameter位置；C0R9继续筛同源contract，避免漫游。 | `ALIGNED` | C0 manifest successor scan。 | no generic search conclusion。 |",
        "KC-000061": "| `KC-000061` | 新发现进入source snapshot、source card、formal package、run、matrix、registry、closure and checkpoint route。 | `ALIGNED` | current work-unit artifacts。 | future sessions reload. |",
        "KC-000062": "| `KC-000062` | 模式匹配产生MSS线索后，源码与machine controls决定其资格；one-pass heuristic不取代验证。 | `ALIGNED` | C0R8 cards / C-375–C-378。 | Q remains unlocated. |",
    }
    for kc, row in rows.items():
        table = replace_table_row(table, kc, row).rstrip("\n")
    header = f"""# CORE COGNITION AUDIT — {SESSION_ID}

> **core identity:** `core-cognition-generation-13`；逐条回评 62 个 KC。
> **scope:** C0R8 MSS/domain/phase-order source and machine controls. The unit establishes representation-level positive and negative controls plus a real operational-consumer seed; it fixes no bare-ZFC core contract and no C6 verdict.

- core_change: NO — 本单元没有新的用户元数学原文，不修改 core generation。
- direction_change: YES — F-053 C0 frontier从C0R8 cited-source screen推进到C0R9 ZFC-specific temporal-operation contract screen。
- panorama_change: YES — 新增C-375–C-378的两个Lean-core source-motivated representation controls。
- essay_change: NO — 未修改扩展认知。
- update_decision: 写回C0 manifest、taskcards、primary source snapshots、two proof packages/runs/matrix/registry、MEMORY/方向/全景/STATE与新session。
- cross_conflicts: source把time definability与domain recovery并置，同时把state description与prediction/operational caveat并置；这支持分层，不支持把任一层偷换为ZFC core verdict。
- unresolved: ZFC-specific M、fixed operational/process Q、actual P、FormalDone→OriginDone bridge、foundation adequacy role、SameQ_H0和C6仍未支付。

## 本单元 source-first 对照

- C-375：ZFC-style graph/domain presentation可恢复固定endpoint membership；
- C-376：deliberately domainless function-only projection对同一endpoint observation非决定；
- C-377：parameterized two-stage trace决定固定start/end order；
- C-378：visited-state range在forward/reverse pair上不决定该order；
- 2001 thermodynamics source称 no-explicit-time formulation不很具操作性，却保留time domain component；它是consumer seed，不是fixed OriginDone。

"""
    return header + table + "\n"


def update_direction(root: Path, texts: dict[str, str], revision: int) -> None:
    doc = projection_edit.load(root, "方向追踪.md")
    projection_edit.replace_in_index(doc, "版本：`integrated-direction-portfolio/v1.20`", "版本：`integrated-direction-portfolio/v1.21`")
    projection_edit.replace_in_index(doc, "source_state_revision: 308", f"source_state_revision: {revision}")
    projection_edit.replace_in_index(
        doc,
        "projection_generation: 20261005-zfc-normative-process-audit-version-closure-308",
        f"projection_generation: 20261005-zfc-mss-controls-{revision}",
    )
    shard = "方向追踪/002 - 治理与用户方向.md"
    old = next(line for line in doc["shards"][shard].splitlines() if line.startswith("| `DIR-U-ZFC-META-SUBTHEORY-ADEQUACY` |"))
    new = "| `DIR-U-ZFC-META-SUBTHEORY-ADEQUACY` | bare ZFC 或明确 ZFC-founded foundation context 对其连续统／极限子理论的 `FormalDone → OriginDone` 提升是否承担并实际履行 bridge 审查责任；以MSS source中的domain carrier、parameter order与operational consumer作受限P calibration | 研究发起人 2026-10-04 的不停机Goal；F-053；KC-000003、KC-000018、KC-000059 | `ACTIVE_CORE_RESEARCH / C0R8_SOURCE_CONSUMER_SEED / C375_C378_MACHINE_CONTROLS / ZFC_SPECIFIC_OPERATION_CONTRACT_UNPAID / C6_NOT_RELEASED` | `ZENO`、`RUSSELL`、`COMPUTATIONAL_LEGITIMACY`、`THEORY_ECONOMY`、`EVIDENCE_DISCIPLINE` | `OUT-U-ZFC-NORMATIVE-PROCESS-AUDIT-C370-C374`；`OUT-U-ZFC-MSS-REPRESENTATION-C375-C378` | C0R8已分开primitive-name elimination、domain recovery、parameter order与operational caveat；核心下一步是`C0-SUCCESSOR-RESELECTION-009`，只选能付ZFC-specific M、fixed task和actual bridge的同源contract。C6只在M/S/Q/P/Bridge/Adequacy齐备后释放。 | `dev-docs/ZFC元理论子理论充分性最终闭环SOP.md`；`认知闭包/ZFC-META-SUBTHEORY-ADEQUACY-001.md`；C0R8 cards；C-375–C-378；F-053 |"
    projection_edit.replace_in_shard(doc, shard, old, new)
    texts["方向追踪.md"] = doc["index_text"]
    texts.update(doc["shards"])


def update_panorama(root: Path, texts: dict[str, str], revision: int) -> None:
    doc = projection_edit.load(root, "全景视野.md")
    projection_edit.replace_in_index(doc, "版本：`integrated-outcome-panorama/v1.21`", "版本：`integrated-outcome-panorama/v1.22`")
    projection_edit.replace_in_index(doc, "source_state_revision: 308", f"source_state_revision: {revision}")
    projection_edit.replace_in_index(
        doc,
        "projection_generation: 20261005-zfc-normative-process-audit-version-closure-308",
        f"projection_generation: 20261005-zfc-mss-controls-{revision}",
    )
    shard = "全景视野/003 - 当前机器证明包与原生重放.md"
    anchor = next(line for line in doc["shards"][shard].splitlines() if line.startswith("| `OUT-U-ZFC-NORMATIVE-PROCESS-AUDIT-C370-C374` |"))
    row = "| `OUT-U-ZFC-MSS-REPRESENTATION-C375-C378` | `MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001` / C-375,C-376与`MP-ZFC-MSS-PHASE-ORDER-CONTROL-001` / C-377,C-378：MSS source-motivated controls分开graph-domain recovery、domainless endpoint loss、parameterized order retention与visited-state range order loss | `DIR-U-ZFC-META-SUBTHEORY-ADEQUACY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | Sant'Anna--Bueno 2014；da Costa--Sant'Anna 2001；Lean 4.34.1 core | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_MOTIVATED_REPRESENTATION_CONTROLS / REAL_OPERATIONAL_CONSUMER_SEED_WITHOUT_FIXED_Q` | 两primary runs exit 0/stderr 0、selected theorem无公理、exact rerun；source确有domain recovery与operational caveat，machine controls表明具体representation可以保留或丢失固定observation | 不形式化MSS/ZFC/N、phase-space semantics、prediction、Zeno/圆环OriginDone、HoTT同Q或bare-ZFC adequacy；source的curve不自动等同finite range | `HoTT/formal/zfc-mss-domain-time-control/CLAIM.md`；`HoTT/formal/zfc-mss-phase-order-control/CLAIM.md`；C0R8 source cards；C-375–C-378 |"
    projection_edit.replace_in_shard(doc, shard, anchor, anchor + "\n" + row)
    texts["全景视野.md"] = doc["index_text"]
    texts.update(doc["shards"])


def append_memory(text: str) -> str:
    marker = "### `C0R8`：MSS 时间表示与实际 consumer seed（2026-10-05）"
    if marker in text:
        return text
    addition = f"""
### `C0R8`：MSS 时间表示与实际 consumer seed（2026-10-05）

`Sant'Anna--Bueno 2014` 给出 ZFC MSS 的 time/domain recoverability 与 domainless N-MSS
non-equivalence；其 2001 cited primary sources把 prediction/future/time 与 phase-space state
description并列，并在 continuum thermodynamics中称 no-explicit-time form不很具操作性。
`{DOMAIN_PROOF}` / C-375–C-376 和 `{ORDER_PROOF}` / C-377–C-378 已分别在 Lean 4.34.1
core中机器检查 carrier/domain 与 parameter/order 的正反表示控制。它们是 source-motivated
controls和real operational-consumer seed，不是 MSS/ZFC formalization、fixed Zeno Q或C6。
当前下一动作变为 `C0-SUCCESSOR-RESELECTION-009`：只筛同源支付 ZFC-specific M、continuous
physical S、concrete operational/process Q、P与bridge/Adequacy的来源合同。

"""
    needle = "## 想法 T：理论精度、观察边界与哥德尔式自反（2026-10-04）"
    if needle not in text:
        raise SystemExit("MEMORY_INSERTION_POINT_MISSING")
    return text.replace(needle, addition + needle, 1)


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
    texts["MEMORY/001 - 当前执行队列.md"] = append_memory(texts["MEMORY/001 - 当前执行队列.md"])
    texts[R.PREFIX + "FRONTIER.md"] = prepend_once(
        texts[R.PREFIX + "FRONTIER.md"],
        "## C0R8：MSS 时间表示控制（2026-10-05）",
        f"""
## C0R8：MSS 时间表示控制（2026-10-05）

- `{DOMAIN_PROOF}` / C-375–C-376：domain-bearing graph view可恢复固定endpoint observation；domainless function-only view不决定它。
- `{ORDER_PROOF}` / C-377–C-378：parameterized trace保留固定start/end order；visited-state range不决定它。
- 2001 source给出real operational-consumer seed，却未固定ZFC-specific M、user Q、OriginDone或bridge。当前只执行`C0-SUCCESSOR-RESELECTION-009`。

""",
    )
    texts[R.PREFIX + "RESUME.md"] = prepend_once(
        texts[R.PREFIX + "RESUME.md"],
        "## C0R8 MSS controls recovery point（2026-10-05）",
        f"""
## C0R8 MSS controls recovery point（2026-10-05）

1. Read `认知闭包/ZFC-META-SUBTHEORY-ADEQUACY-001.md`, the four-shard core SOP,
   C0 manifest and C0 successor 009.
2. Treat C-375–C-378 as source-motivated representation controls only. The current
   unresolved question is a ZFC-specific temporal-operation contract, not whether time
   can be written or definitionally recovered.
3. Freeze M/S/Q/P/Bridge/Adequacy before any next formalization; a source with an
   operational caveat alone is a seed, not a core verdict.

""",
    )
    lesson_marker = "## C0R8 representation lesson（2026-10-05）"
    if lesson_marker not in texts[R.PREFIX + "LESSONS.md"]:
        texts[R.PREFIX + "LESSONS.md"] += f"""

{lesson_marker}

Before treating a time-elimination result as a P/Q clue, distinguish four separate
questions: (1) was only the primitive name removed; (2) is the carrier/domain
recoverable; (3) is parameter/order recoverable; (4) does a source-defined operational
consumer still receive its task-level bridge? C-375–C-378 give paired controls for the
middle two questions; they do not answer the fourth.
"""

    log_path = "MEMORY/003 - 当前验证状态与顺序日志.md"
    log_entry = (
        f"\n\n{SESSION_ID}：C0R8 MSS source screen created two Lean-core representation-control packages: "
        f"`{DOMAIN_PROOF}` / C-375–C-376 and `{ORDER_PROOF}` / C-377–C-378. "
        "Primary sources support domain recovery, parameter/state-description tension, and a practical operational caveat; no actual bare-ZFC M/S/Q/P/Bridge/Adequacy contract is paid. "
        "Next successor is C0-SUCCESSOR-RESELECTION-009."
    )
    if SESSION_ID not in texts[log_path]:
        texts[log_path] += log_entry + "\n"

    source_paths = [
        "sources/prompts/Codex-ZFC核心层最终机器证明与不停机Goal-用户原文-20261004.md",
        "dev-docs/ZFC元理论子理论充分性最终闭环SOP.md",
        "认知闭包/ZFC-META-SUBTHEORY-ADEQUACY-001.md",
        "audit/ZFC-META-SUBTHEORY-ADEQUACY-001-C0-CANDIDATE-MANIFEST.md",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-008-TASKCARD.md",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0-SUCCESSOR-RESELECTION-009-TASKCARD.md",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-SANTANNA-BUENO-ZFC-TIME-ELIMINATION-CANDIDATE.md",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-DOMAIN-ELIMINATION-SOURCE-TO-SPEC-CONTROL.md",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-DACOSTA-SANTANNA-REAL-CONSUMER-SCREEN.md",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-MSS-PHASE-ORDER-SOURCE-TO-SPEC-CONTROL.md",
        "sources/external/zfc-meta-subtheory-c0r8-santanna-bueno-2014-20261005/README.md",
        "sources/external/zfc-meta-subtheory-c0r8-santanna-bueno-2014-20261005/SantAnna-Bueno-2014-Sets-and-Functions-Theoretical-Physics.pdf",
        "sources/external/zfc-meta-subtheory-c0r8-dacosta-santanna-2001-20261005/README.md",
        "sources/external/zfc-meta-subtheory-c0r8-dacosta-santanna-2001-20261005/daCosta-SantAnna-2001-Mathematical-Role-Time-Spacetime.pdf",
        "sources/external/zfc-meta-subtheory-c0r8-dacosta-santanna-2001-20261005/daCosta-SantAnna-2001-Time-Dispensable-Thermodynamics.pdf",
        "HoTT/formal/zfc-mss-domain-time-control/MSSDomainTimeControl.lean",
        "HoTT/formal/zfc-mss-domain-time-control/CLAIM.md",
        f"HoTT/verification/runs/{DOMAIN_RUN}/RUN.json",
        f"HoTT/verification/runs/{DOMAIN_RUN}/source-manifest.json",
        f"HoTT/verification/runs/{DOMAIN_RUN}/index-row-manifest.json",
        "HoTT/formal/zfc-mss-phase-order-control/MSSPhaseOrderControl.lean",
        "HoTT/formal/zfc-mss-phase-order-control/CLAIM.md",
        f"HoTT/verification/runs/{ORDER_RUN}/RUN.json",
        f"HoTT/verification/runs/{ORDER_RUN}/source-manifest.json",
        f"HoTT/verification/runs/{ORDER_RUN}/index-row-manifest.json",
        "HoTT/CLAIM_EVIDENCE_MATRIX.md",
        "HoTT/verification/PROOF_VERSION_CLOSURE.json",
    ]
    state = prior_state
    state["revision"] = revision
    state["latest_session"] = SESSION_ID
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "C0R8_SOURCE_CONSUMER_SEED_AND_C375_C378_MACHINE_CONTROLS_WITH_SCOPE / CORE_C6_NOT_RELEASED",
        "full_sources": source_paths,
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
        "path_mode": "document",
        "related_records": [PREVIOUS_SESSION],
        "scope": "C0R8 source-first examination of ZFC MSS / domainless N distinction and its 2001 cited sources. It produces four Lean-core representation controls for domain/endpoint and parameter/order recovery/loss, and records a real operational-consumer seed. It does not establish a ZFC-specific M/S/Q/P/Bridge/Adequacy contract, a physical completion claim, SameQ_H0, or C6.",
        "source_hashes": {path: sha((root / path).read_bytes()) for path in source_paths},
        "status": "complete",
    }
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    session_base = f".codex/research/hott/sessions/{SESSION_ID}/"
    texts[session_base + "SESSION.md"] = f"""# {SESSION_ID}

> **Role:** `RESEARCH_GENERATION`.
> **Tier:** `T3` — C0R8 source-to-spec research plus two Lean-core representation controls; no bare-ZFC C6 theorem.

## 研究对象

检验 ZFC-MSS 中 time primitive 的可消去性到底删除了什么：仅是独立名字，还是 domain
carrier、parameter order或一个 source-defined operational consumer 所需要的观察。进一步检查
da Costa--Sant'Anna 2001 是否使此位置成为 actual core contract。

## 实际结果

- `{DOMAIN_PROOF}` / C-375–C-376：graph-domain recovery与deliberately domainless function-only
  endpoint non-determinacy均由Lean 4.34.1 core检查，selected axiom report为空。
- `{ORDER_PROOF}` / C-377–C-378：parameterized trace保留固定start/end order，而visited-state
  range在forward/reverse pair上不决定此order；同样为无额外公理的core check。
- 2014/2001 source确实提供 time/domain、prediction/state-description和practical-operation的
  文本连接；但其保留或可恢复的时间结构、generic set-theoretic M以及未固定的Done使它仅为
  consumer seed，而非actual bare-ZFC core contract。

## successor

`C0-SUCCESSOR-RESELECTION-009`：寻找同源付清 ZFC-specific M、continuous physical S、concrete
operational/process Q、P与Bridge/Adequacy的来源；不得把本控制包或operation caveat重复包装为Q。
"""
    texts[session_base + "RUNS.json"] = json.dumps({
        "next": "C0-SUCCESSOR-RESELECTION-009: find a ZFC-specific temporal-operation contract; do not turn C-375–C-378 or the operational caveat into an actual core Q.",
        "role": "RESEARCH_GENERATION",
        "schema_version": "hott-research-runs/v1",
        "session_id": SESSION_ID,
        "status": "C0R8_SOURCE_CONSUMER_SEED_WITH_REPRESENTATION_CONTROLS_C6_NOT_RELEASED",
        "tier": "T3",
        "verification": [
            {
                "command": f"python3 -B scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/{DOMAIN_RUN} --rerun",
                "scope": "C-375/C-376 exact Lean core replay",
                "status": "PASS_WITH_SCOPE",
            },
            {
                "command": f"python3 -B scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/{ORDER_RUN} --rerun",
                "scope": "C-377/C-378 exact Lean core replay",
                "status": "PASS_WITH_SCOPE",
            },
            {
                "command": f"python3 -B scripts/audit/verify_proof_version_closure.py --proof-id {DOMAIN_PROOF} --proof-id {ORDER_PROOF} --evidence-only",
                "scope": "source manifest, primary run/index-row relation and registry binding",
                "status": "LOCAL_EVIDENCE_PASS_NOT_VERSION_CLOSED",
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
        "authorization": "User authorized continued ZFC core research, source acquisition, formalization, machine verification, durable documentation, exact-path Git commits, and remote push. This checkpoint preserves C0R8 controls without closing the core Goal.",
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
        "proof_ids": [DOMAIN_PROOF, ORDER_PROOF],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
