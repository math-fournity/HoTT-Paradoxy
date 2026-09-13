#!/usr/bin/env python3
"""Prepare revision 103: register the P1 (time line) bounded negative and its receipt.

The user said "开始吧，全部做完" for the work package proposed after C11: fix the P1
candidate, audit its payment devices, and decide whether F-011 machine work is
warranted.  Deliverables written before this transaction:

- `audit/p1-时序线候选与支付装置审计-20260913.md` (verdict
  `P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE`, no new mathematical claim);
- `scripts/audit/verify_ledger_retrodiction.py` and its receipt
  `audit/ledger-retrodiction-check-20260913.json` (18 packages, 66 source files
  re-hashed, 17 available + 1 absent payment-device cell, `status: PASS`).

This checkpoint writes only the MUTABLE state and the canonical session bundle.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-103-P1-TIME-LINE-AUDIT"
PREV = "S-RES-20260913-102-THEORY-ECONOMY-LEDGER"
RESULT_ID = "A-P1-TIME-LINE-BOUNDED-NEGATIVE-001"
CHECK_ID = "A-LEDGER-RETRODICTION-CHECK-001"
OUTCOME_ID = "OUT-TOP-TIME-LINE-P1-BOUNDED-NEGATIVE"
REPORT = "audit/p1-时序线候选与支付装置审计-20260913.md"
CHECK_RECEIPT = "audit/ledger-retrodiction-check-20260913.json"
CHECK_SCRIPT = "scripts/audit/verify_ledger_retrodiction.py"
C11 = "理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"

SPEC = importlib.util.spec_from_file_location("runtime_s103", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:60]}:{text.count(old)}")
    return text.replace(old, new, 1)


OUTCOME_ROW = (
    f"| `{OUTCOME_ID}` | P1 时序线（C11 判别格第一次应用）：候选固定为“阶段 k 交付已落定结果”，"
    "支付装置 D1–D6 逐项审计（阶段索引 C-106–C-109、阶段擦除判据 C-92–C-95、partial/strict C-118–C-123、"
    "保留代表元 C-129–C-133/C-96–C-99/C-154–C-155、上下文族 C-71–C-91），"
    "D6 = 外部库 `SetQuotients.Properties.rec/elim` 把同余义务写进类型 | `DIR-TOP-THEORY-ECONOMY-LEDGER` | "
    "用户 2026-09-13「开始吧，全部做完」；当前工作包 | `DOCUMENTED / P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE` | "
    "P1 在类型层不可能失配（消去器强制同余）；用 checklist 重读 N1/N5/N10/T4 候选集合后，"
    "无候选同时满足“粗域接口 + 必须取回 + 同阶段同层”；机械回溯收据 18 包 / 66 源文件重哈希 / 17 可用 + 1 缺失 | "
    "不新增数学 claim；不证明 HoTT 无问题；负结论只覆盖本 repo 固定工具链与已审计接口集合 | "
    f"`{REPORT}`；`{CHECK_RECEIPT}`；`{C11}` |\n"
)

AUDIT_FOCUS = {
    "KC-000005": ("ALIGNED", "先固定候选与完成判据、把归因留后；P1 判负后不追认任何归因。"),
    "KC-000010": ("ALIGNED", "以现实相对非现实性（同任务完成性反差）为目标，而不是内部矛盾。"),
    "KC-000011": ("DEEPENED", "“理论工作过程是否承担时序”被落实为 D1–D5 支付装置与阶段交付判据。"),
    "KC-000012": ("ALIGNED", "ASK 的“此刻是否合法/可用”被写成 P1 的任务判据与 checklist 第 4 项。"),
    "KC-000013": ("ALIGNED", "理论为了工具性悬置阶段，再用索引/部分性/细化表示支付。"),
    "KC-000015": ("DEEPENED", "“否定现实前提”具体化为“阶段因子被商/截断/外延化悬置”，并用 D6 给出类型层边界。"),
    "KC-000017": ("ALIGNED", "用机械回溯与库级源码核对约束叙述，不依赖训练先验的结论。"),
    "KC-000021": ("ALIGNED", "本轮所有判词都回指已保存的 18 个 kernel run；未新增未运行的主张。"),
    "KC-000022": ("ALIGNED", "P1 是第一类形态（现实可完成、理论引入额外完成困难）的固定候选；结论为支付装置可用。"),
    "KC-000023": ("DEEPENED", "“应当能直接定位 HoTT 对时间/时序的处理”落实为：阶段擦除、partial/strict、在线因果三条机器边界。"),
    "KC-000025": ("NOT_TOUCHED", "自指线（P2）本轮未推进；留给下一步。"),
    "KC-000026": ("NOT_TOUCHED", "HoTT 自指未由本轮检验。"),
    "KC-000027": ("ALIGNED", "共享机制不冒充 HoTT 独有：P1 的装置多来自一般计算/表示事实，本文如实标注。"),
    "KC-000028": ("NOT_TOUCHED", "自馈回环未推进；ERCF-3 保持 gated。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是 P1 时序线的候选固定与支付装置审计，不产生数学结论。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = AUDIT_FOCUS.get(
            kid, ("NOT_TOUCHED", f"本轮没有研究或重新裁决「{label}」的数学/哲学内容。")
        )
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{REPORT}`；{kid} | 数学开放项不变。 |"
        )
    aligned = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "ALIGNED")
    deepened = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "DEEPENED")
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文。",
        f"- direction_change: YES_IN_PLACE — `DIR-TOP-THEORY-ECONOMY-LEDGER` 行原位补上 P1 判词与下一步（不加覆盖块）。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/004 owner shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: P1 判 `BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE`；不建重复证明包；搜索目标改为“接口文档承诺 > 接口类型能力”。",
        "- cross_conflicts: C5 的 E6 仍是升级口，但本轮证明类型层不可能给出 E6（消去器强制同余）→ E6 被限定为接口事实，保留冲突表述不改历史文件。",
        "- unresolved: P2/P3 未处理；未找到任何真实粗域接口；机械回溯只核对账目与文件事实，不验证语义。",
        "",
        "## 汇总",
        "",
        f"`ALIGNED={aligned}`；`DEEPENED={deepened}`；其余 `NOT_TOUCHED`；无 `DEVIATED`。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 102 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_102_S102")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "086"),
        ("PANORAMA", R.PANORAMA, "outcome", "086"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 102", "source_state_revision: 103"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-087",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/002 - 治理与用户方向.md",
        "`OUT-TOP-THEORY-ECONOMY-LEDGER`（9 行账本 + 2×2 判别格 + P1–P3 预测 + 18 包回溯检验） | "
        "按判别格选 1–2 个“同阶段 / 同层不可用”的候选并执行 F-011 机器化；P1 时序线优先 |",
        "`OUT-TOP-THEORY-ECONOMY-LEDGER`、`" + OUTCOME_ID + "`（9 行账本 + 2×2 判别格 + P1–P3 预测 + 18 包机械回溯） | "
        "**P1 已判 `P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE`**（D1–D6 支付装置全部可用；"
        "商/截断消去器把同余义务写进类型，故类型层不可能给出 E6）；下一步按同一 checklist 处理 P2 / P3，"
        "并把搜索目标定为“接口文档承诺 > 接口类型能力”的真实接口 |",
    )
    projection_edit.append_to_shard(
        projections["PANORAMA"],
        "全景视野/004 - 距离综合与消费者审计.md",
        OUTCOME_ROW,
    )

    memory = projection_edit.load(root, "MEMORY.md")
    projection_edit.replace_in_shard(
        memory,
        "MEMORY/001 - 当前执行队列.md",
        "2. 数学研究第一线（S102 起由账本驱动）：先按 `理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md` "
        "的 2×2 判别格选候选（P1 时序线优先 / P2 自指线 / P3 交叉线），再落到"
        "**真实下游应用或派生开发中的 E6 consumer**。",
        "2. 数学研究第一线（S103 起）：**P1 时序线已判 `P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE`**"
        "（支付装置 D1–D6 全部可用；见 `audit/p1-时序线候选与支付装置审计-20260913.md`）。"
        "下一步按同一 checklist 处理 P2 自指线与 P3 交叉线，并把搜索目标定为"
        "“**接口文档承诺 > 接口类型能力**”的真实接口（类型层已由消去器的同余义务关闭）。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S103 P1 时序线工作包完成（用户「开始吧，全部做完」）：候选固定为“阶段 k 交付已落定结果”，"
        "支付装置 D1–D6 逐项审计（C-106–C-109 / C-92–C-95 / C-118–C-123 / C-129–C-133 / C-96–C-99 / "
        "C-71–C-91；D6 = 外部库 `SetQuotients.Properties.rec/elim` 把同余义务写进类型），"
        "判 `P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE`；用 checklist 重读 N1/N5/N10/T4 候选集合，"
        "无候选同时满足“粗域接口 + 必须取回 + 同阶段同层”。**F-011 决策：不建重复证明包**"
        "（避免重证 C-59–C-66/C-73–C-76/C-106–C-109/C-118–C-123/C-154 的同一机制）。"
        "新增机械资产 `scripts/audit/verify_ledger_retrodiction.py` + 收据 "
        "`audit/ledger-retrodiction-check-20260913.json`：18 包、66 个源文件按 source-manifest 重哈希一致、"
        "17 个“支付装置可用” + 1 个“支付装置不存在”（`MP-NOCANONICAL-001`，无真实消费者）、"
        "verdict 无 `NATURAL_USAGE_MISMATCH`/`INTERNAL_INCONSISTENCY`、self-test 3/3。未新增数学 claim。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row51 = (
        "| 已闭合工作包 51 | Astra-1/Astra-2 会话轨迹审计与状态注册（S101） | "
        "`DOCUMENTED / L2_PASS_BY_RUN_SOURCE_COMPARE; L5_TARGET_NOT_MET` | 会话别名闭合为 thread id；"
        "Astra-1 8 轮 / 104 tool call，Astra-2 为其子线程；三件套读取按 `35cace7` 逐字节/逐行复核完整；"
        "四类未达成原因与全部 locator 见 `audit/astra-1-astra-2会话轨迹审计-20260913.md`；研究队列不变 |"
    )
    frontier = replace_once(
        frontier,
        row51,
        row51 + "\n| 已闭合工作包 52 | P1 时序线候选与支付装置审计（S103） | "
        "`P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE` | 候选固定为“阶段 k 交付已落定结果”；"
        "D1–D6 支付装置全部可用（含消去器的同余义务）；checklist 重读 N1/N5/N10/T4 无命中；"
        f"机械回溯 18 包 / 66 源文件重哈希见 `{CHECK_RECEIPT}`；不建重复证明包 |",
    )
    frontier = replace_once(
        frontier,
        "| 第一工作包 | C11 理论经济账本驱动的候选选择（P1 时序线优先 / P2 自指线 / P3 交叉线） | active | "
        "先用“同阶段 / 同层”判别格挑 1–2 个候选，再固定版本、调用链、输入与交付承诺并走 F-011；"
        "固定下游应用/派生开发的真实 E6 consumer 仍是具体执行目标 |",
        "| 第一工作包 | P2 自指线 / P3 交叉线（同一 checklist）＋“承诺 > 类型”的粗域接口搜索 | active | "
        "对每个候选回答“粗域接口？必须取回？同阶段同层？”；类型层已由消去器的同余义务关闭，"
        "因此目标是找到**文档承诺超出接口类型能力**的真实接口，再按 F-011 草案机器化 |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n82. 在商/截断上找“类型层越级”是徒劳的：Cubical 的 `SetQuotients.Properties.rec/elim` 把同余义务"
        "写进**类型参数**（`(a b : A) (r : R a b) → f a ≡ f b`），所以“从粗类型取回被悬置因子”在类型检查阶段就被拒。"
        "结论：E6 只能出现在“**接口文档承诺超出接口类型能力**”的地方（文档说能按期交付，类型却只给出商/截断）。"
        "相应的工作方法是先判“支付装置是否可用”，再去找文档与类型的落差；不要靠再证一遍同一有限模型来推进。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S103：P1 时序线工作包已完成并判 `P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE`（支付装置 D1–D6 全可用；"
        "类型层已由消去器的同余义务关闭）；未新增数学 claim、未建重复证明包。"
        "下一步按同一 checklist 处理 P2 自指线与 P3 交叉线，并把搜索目标定为“接口文档承诺 > 接口类型能力”的真实接口。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户对 C11 之后提出的工作包说「开始吧，全部做完」：用判别格固定 P1 时序线候选、审计支付装置、决定 F-011。
- 交付：`{REPORT}`（判词 `P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE`）与机械资产
  `{CHECK_SCRIPT}` → `{CHECK_RECEIPT}`（18 包 / 66 源文件重哈希 / 17 可用 + 1 缺失 / self-test 3 控制 / `status: PASS`）。
- 决策：**不为 P1 建新证明包**（避免重证 C-59–C-66、C-73–C-76、C-106–C-109、C-118–C-123、C-154 的同一机制）；
  给出若出现“文档承诺 > 类型能力”接口时的三条 claim 机器化草案。
- 本 checkpoint 写 machine-managed 状态：`STATE.revision=103`、结果 `{RESULT_ID}` 与检查 `{CHECK_ID}`、
  方向行原位更新、全景新结果行、MEMORY/FRONTIER/LESSONS 82/RESUME。
- 状态边界：不新增数学 claim、不改判词、不把 P1 写成已发现的悖论；负结论只覆盖本 repo 固定工具链与已审计接口集合；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "work_package": "P1 time line (C11 grid, first application)",
            "verdict": "P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE",
            "payment_devices": ["D1 stage index", "D2 guard-erasure criterion", "D3 partial/strict",
                                "D4 refined representation", "D5 context family", "D6 eliminator congruence obligation"],
            "retrodiction_receipt": CHECK_RECEIPT,
            "packages_checked": 18,
            "source_files_rehashed": 66,
            "device_available": 17,
            "device_absent": ["MP-NOCANONICAL-001"],
            "new_math_claims": [],
            "new_proof_package": None,
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 103
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_P1_TIME_LINE_BOUNDED_NEGATIVE",
            "status": STATUS,
            "next_minimal_verification": (
                "Apply the C11 checklist to P2 (same-layer unavailable) and P3 (intersection), and search for a real "
                "coarse-domain interface whose documentation promises more than its type can deliver (deadline/stage "
                "delivery from a quotient or truncated type). Type-level mismatch is closed by the eliminator's "
                "congruence obligation; only a documented-promise mismatch can upgrade to NATURAL_USAGE_MISMATCH, and it "
                "must then be machine-formalised per MATH_PROOF_BEFORE_DELIVERY_V1."
            ),
        }
    )
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-087", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-087", "semantic_status": STATUS}
    )
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-THEORY-ECONOMY-LEDGER-001", CHECK_ID],
        "full_sources": [REPORT, C11, "HoTT/CLAIM_EVIDENCE_MATRIX.md"],
        "source_hashes": {REPORT: R.sha((root / REPORT).read_bytes())},
        "scope": (
            "P1 time-line work package: candidate fixed as 'deliver the already-settled result at stage k'; payment "
            "devices D1-D6 audited (stage index, guard-erasure criterion, partial/strict classifiers, refined "
            "representation, context family, eliminator congruence obligation); checklist re-read of the N1/N5/N10/T4 "
            "candidate sets finds no candidate with (coarse-domain interface + must recover + same stage/layer). "
            "Verdict P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE; no new mathematical claim; no duplicate proof package."
        ),
    }
    state["records"][CHECK_ID] = {
        "kind": "result",
        "path": CHECK_RECEIPT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [SESSION_ID, RESULT_ID],
        "full_sources": [CHECK_RECEIPT, CHECK_SCRIPT, "HoTT/CLAIM_EVIDENCE_MATRIX.md"],
        "source_hashes": {CHECK_SCRIPT: R.sha((root / CHECK_SCRIPT).read_bytes())},
        "scope": (
            "Mechanical retrodiction check for the C11 grid: 18 packages verified for matrix package row + verdict "
            "token, per-claim matrix rows, final run receipt files with exit_code 0, and source-manifest file hashes "
            "(66 files re-hashed); verdicts contain no NATURAL_USAGE_MISMATCH / INTERNAL_INCONSISTENCY; distribution "
            "17 payment-device-available + 1 absent (MP-NOCANONICAL-001, no real consumer). Self-test has three "
            "controls. Scope: mechanical bookkeeping and file facts only; semantics of the ledger rows are not verified."
        ),
    }
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, RESULT_ID, CHECK_ID],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, REPORT, CHECK_RECEIPT],
        "source_hashes": {},
        "scope": (
            "Registration of the P1 time-line work package: verdict, payment-device audit, F-011 decision, mechanical "
            "retrodiction receipt, projection/MEMORY/FRONTIER/LESSONS/RESUME updates. No mathematical change."
        ),
    }

    texts: dict[str, str] = {}
    for doc in (projections["DIRECTION"], projections["PANORAMA"], memory, essay):
        texts[doc["index_path"]] = doc["index_text"]
        texts.update(doc["shards"])
    texts[f"{R.PREFIX}FRONTIER.md"] = frontier
    texts[f"{R.PREFIX}LESSONS.md"] = lessons
    texts[f"{R.PREFIX}RESUME.md"] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text(root)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "User said '开始吧，全部做完' for the work package proposed after C11: fix the P1 time-line candidate, audit "
            "its payment devices, and decide whether F-011 machine work is warranted, then register the outcome. "
            "No new mathematical claim, no duplicate proof package, no push."
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
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PREPARED",
                "snapshot": plan["snapshot"],
                "revision": 103,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
