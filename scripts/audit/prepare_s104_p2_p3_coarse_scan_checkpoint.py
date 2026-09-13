#!/usr/bin/env python3
"""Prepare revision 104: register the P2/P3 checklist application and the coarse-consumer scan."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-104-P2-P3-AND-COARSE-SCAN"
PREV = "S-RES-20260913-103-P1-TIME-LINE-AUDIT"
REPORT_ID = "A-P2-P3-CHECKLIST-001"
SCAN_ID = "A-COARSE-CONSUMER-SCAN-001"
OUTCOME_ID = "OUT-TOP-COARSE-CONSUMER-SCAN"
REPORT = "audit/p2-p3与粗域接口搜索-20260913.md"
SCAN_RECEIPT = "audit/coarse-consumer-scan-20260913.json"
SCAN_SCRIPT = "scripts/audit/scan_coarse_consumers.py"
P1_REPORT = "audit/p1-时序线候选与支付装置审计-20260913.md"
C11 = "理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"

SPEC = importlib.util.spec_from_file_location("runtime_s104", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | P2/P3 判别格应用与“粗域接口”搜索：P2（同层不可用）判 `P2_PREDICTION_HOLDS_NO_CONSUMER`"
    "（支付装置 = 层级上升，存在但昂贵；缺 S053 P8 消费者）；P3（交叉线）判 `P3_PREDICTION_HOLDS_NO_CONSUMER`"
    "（支付装置已被 C-142–C-148 证明不存在，形式要件最齐，列为最优先） | `DIR-TOP-THEORY-ECONOMY-LEDGER` | "
    "用户 2026-09-13「继续」；当前工作包 | `DOCUMENTED / BOUNDED_NEGATIVE_WITH_TRIAGE_QUEUE` | "
    "三固定语料（Cubical v0.9 1091 文件 / agda-unimath 7b81411d 3056 文件 / 本 repo formal 34 文件）机械扫出 "
    "239 条“粗域 + 箭头”命中（93 条签名自带义务 token，146 条进入 triage 队列）；固定 10 例人工实读全部落入"
    "“余域截断 / 返回 Truncated-Type 记录 / 我们自己的不可能性定理”三类无害形态 | "
    "不新增数学 claim；词汇级扫描不证明库内不存在粗域消费者；负结论只覆盖本轮固定语料、规则与抽样 | "
    f"`{REPORT}`；`{SCAN_RECEIPT}` |\n"
)

AUDIT_FOCUS = {
    "KC-000005": ("ALIGNED", "P2/P3 同样先固定候选形状与缺环，不把归因提前。"),
    "KC-000010": ("ALIGNED", "目标仍定在“现实相对非现实性”，不是内部矛盾；三轮判词都是缺消费者。"),
    "KC-000011": ("ALIGNED", "P3 把“理论工作过程是否承担阶段”与“是否给出代表元”合并为一个任务形状。"),
    "KC-000012": ("ALIGNED", "ASK 的“凭什么此刻可以交付”落到 P3 的阶段判据。"),
    "KC-000013": ("ALIGNED", "P2 的支付装置（升层/信任基）正是理论经济性代价的直接体现。"),
    "KC-000015": ("ALIGNED", "粗域接口扫描是“理论为经济性悬置了什么”的可机械 triage 版本。"),
    "KC-000017": ("ALIGNED", "用固定语料与固定抽样约束判断，不靠印象或训练先验。"),
    "KC-000021": ("ALIGNED", "本轮不新增机器证明，也未把扫描当成证明；所有判词不改动既有 kernel 结果。"),
    "KC-000022": ("ALIGNED", "P2 属第二类（理论绕过 ASK 的自我担保版本）的候选形状；仍缺消费者。"),
    "KC-000023": ("DEEPENED", "把“应能直接定位 HoTT 的时间处理”推进为 P3 的接口判据（域粗化 + 阶段交付）。"),
    "KC-000025": ("ALIGNED", "自指线给出明确缺环（内部总自证消费者），而不是重复“自指难找”。"),
    "KC-000026": ("ALIGNED", "P2 把“自指不可越过”写成层级支付问题，与 ERCF-3 gated 一致。"),
    "KC-000027": ("ALIGNED", "共享机制不冒充 HoTT 独有：P2/P3 的支付装置多数来自一般计算/表示事实。"),
    "KC-000028": ("ALIGNED", "自馈回环被放到 P2“同层不可用”格子，并保持通用边界判词。"),
    "KC-000036": ("ALIGNED", "Gödel 内部化仍归 P2；没有真实消费者前不作 HoTT 特有结论。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是 P2/P3 判别格应用与粗域接口搜索，不产生数学结论。",
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
        f"- direction_change: YES_IN_PLACE — `DIR-TOP-THEORY-ECONOMY-LEDGER` 行原位补上 P2/P3 判词与 triage 计划。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/004 owner shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 三条预测路径全部闭合到“缺真实接口 / 缺消费者”；下一轮为 triage 队列批次 1（20 条）与 P3 定向搜索。",
        "- cross_conflicts: P2 的支付装置“可用但昂贵”与“同层不可用”的表述需并存——升层离开理论，等于任务失败；本轮明确保留该双层表述。",
        "- unresolved: 146 条 triage 队列未逐条读；10 例抽样只覆盖三层代表形态；未找到“文档承诺 > 类型能力”的真实接口。",
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
    if state.get("revision") != 103 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_103_S103")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "087"),
        ("PANORAMA", R.PANORAMA, "outcome", "087"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 103", "source_state_revision: 104"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-088",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/002 - 治理与用户方向.md",
        "下一步按同一 checklist 处理 P2 / P3，并把搜索目标定为“接口文档承诺 > 接口类型能力”的真实接口 |",
        "**P2 判 `P2_PREDICTION_HOLDS_NO_CONSUMER`、P3 判 `P3_PREDICTION_HOLDS_NO_CONSUMER`**（P3 的形式要件最齐："
        "支付装置已由 C-142–C-148 证明不存在）；三语料机械扫描 239 条命中 / 93 带义务 / 146 入 triage 队列，"
        "10 例人工抽样全为无害形态（`" + OUTCOME_ID + "`）。下一步：triage 批次 1（20 条）＋ P3 定向找“文档承诺 > 接口类型能力”的真实接口 |",
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
        "下一步按同一 checklist 处理 P2 自指线与 P3 交叉线，并把搜索目标定为"
        "“**接口文档承诺 > 接口类型能力**”的真实接口（类型层已由消去器的同余义务关闭）。",
        "P2 自指线判 `P2_PREDICTION_HOLDS_NO_CONSUMER`、P3 交叉线判 `P3_PREDICTION_HOLDS_NO_CONSUMER`"
        "（P3 支付装置已由 C-142–C-148 证明不存在，形式要件最齐，列为最优先）。"
        "下一轮：146 条 triage 队列取 20 条逐条读，并定向找“**文档承诺 > 接口类型能力**”的真实接口"
        "（类型层已由消去器的同余义务关闭）。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S104 P2/P3 判别格应用与粗域接口搜索（用户「继续」）：P2（同层不可用）判 `P2_PREDICTION_HOLDS_NO_CONSUMER`"
        "——支付装置是层级上升（2LTT/QIIT/内部模型），存在但昂贵，缺 S053 P8 消费者，ERCF-3 保持 gated；"
        "P3（交叉）判 `P3_PREDICTION_HOLDS_NO_CONSUMER`——它同时要求阶段交付与代表元/统一选点，"
        "而 `MP-NOCANONICAL-001`（C-142–C-148）已机器证明后者不存在，形式要件最齐，列为最优先。"
        "新增机械资产 `scripts/audit/scan_coarse_consumers.py` + 收据 `audit/coarse-consumer-scan-20260913.json`："
        "三固定语料（Cubical v0.9 1091 文件、agda-unimath@7b81411d 3056 literate 文件、本 repo formal 34 文件）"
        "扫出 239 条“粗域 + 箭头”命中，93 条签名自带义务 token，146 条入 triage 队列；固定 10 例人工实读"
        "全部为无害形态（余域截断 / 返回 Truncated-Type 记录 / 我们自己的不可能性定理）。未新增数学 claim。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row52 = (
        "| 已闭合工作包 52 | P1 时序线候选与支付装置审计（S103） | `P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE` | "
        "候选固定为“阶段 k 交付已落定结果”；D1–D6 支付装置全部可用（含消去器的同余义务）；checklist 重读 "
        "N1/N5/N10/T4 无命中；机械回溯 18 包 / 66 源文件重哈希见 `audit/ledger-retrodiction-check-20260913.json`；"
        "不建重复证明包 |"
    )
    frontier = replace_once(
        frontier,
        row52,
        row52 + "\n| 已闭合工作包 53 | P2/P3 判别格应用与粗域接口搜索（S104） | "
        "`P2_PREDICTION_HOLDS_NO_CONSUMER` / `P3_PREDICTION_HOLDS_NO_CONSUMER` / "
        "`COARSE_CONSUMER_SCAN_BOUNDED_NEGATIVE_WITH_TRIAGE_QUEUE` | P2 支付装置=层级上升（昂贵但存在）；"
        "P3 形式要件最齐（支付装置已由 C-142–C-148 证明不存在）；三语料 239 命中 / 93 带义务 / 146 triage，"
        f"10 例实读全部无害；见 `{REPORT}` 与 `{SCAN_RECEIPT}` |",
    )
    frontier = replace_once(
        frontier,
        "| 第一工作包 | P2 自指线 / P3 交叉线（同一 checklist）＋“承诺 > 类型”的粗域接口搜索 | active | "
        "对每个候选回答“粗域接口？必须取回？同阶段同层？”；类型层已由消去器的同余义务关闭，"
        "因此目标是找到**文档承诺超出接口类型能力**的真实接口，再按 F-011 草案机器化 |",
        "| 第一工作包 | triage 队列批次 1（146 条取 20）＋ P3 定向搜索“粗域接口 + 阶段交付承诺” | active | "
        "逐条读命中声明的上下文与文档段落，判义务是否由签名/余域承担；若出现“必须取回 + 同阶段/同层”全命中的"
        "真实接口，按 P1 报告 §6 的三条 claim 草案走 F-011；否则保持有界负结论 |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n83. “找粗域接口”要分两步：先用**词汇级 triage** 缩小到有界队列（本轮：三固定语料 239 条“粗域 + 箭头”，"
        "93 条签名自带义务 token，146 条入队列），再**人工实读**判定义务由谁承担。实测三类无害形态占满样本："
        "余域本身是截断/命题类型、返回 `Truncated-Type` 记录（义务随记录）、以及我们自己的不可能性定理。"
        "不要用像素级 grep 结果直接当候选，也不要把“没扫到”写成“不存在”；每轮只读有界批次并保留复算规则。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S104：P2/P3 判别格应用与粗域接口搜索完成——P2 判 `P2_PREDICTION_HOLDS_NO_CONSUMER`（支付装置=层级上升，缺 S053 P8 消费者），"
        "P3 判 `P3_PREDICTION_HOLDS_NO_CONSUMER`（形式要件最齐：C-142–C-148 已证无统一选点）；三固定语料机械扫描 239 命中 / "
        "93 带义务 / 146 triage，10 例人工实读全部无害。下一轮：triage 批次 1（20 条）＋ P3 定向找“文档承诺 > 类型能力”的真实接口。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户说「继续」，执行 FRONTIER 登记的第一工作包：P2/P3 判别格应用 ＋ “粗域接口”搜索。
- 交付：`{REPORT}`（P2 `P2_PREDICTION_HOLDS_NO_CONSUMER`、P3 `P3_PREDICTION_HOLDS_NO_CONSUMER`、
  扫描 `COARSE_CONSUMER_SCAN_BOUNDED_NEGATIVE_WITH_TRIAGE_QUEUE`）与机械资产
  `{SCAN_SCRIPT}` → `{SCAN_RECEIPT}`（三固定语料、239 命中、93 带义务、146 triage、10 例人工实读）。
- 关键结构结论：三条预测路径（P1/P2/P3）在数学侧都闭合到“缺真实接口/消费者”；P3 最优先，因为它的支付装置
  （统一选点）已被 `MP-NOCANONICAL-001` 证明不存在。
- 本 checkpoint 写 machine-managed 状态：`STATE.revision=104`、结果 `{REPORT_ID}` 与 `{SCAN_ID}`、
  方向行原位更新、全景新结果行、MEMORY/FRONTIER/LESSONS 83/RESUME。
- 状态边界：不新增数学 claim、不改判词、不做外部网络检索；负结论只覆盖本轮固定语料、规则与抽样；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "work_package": "P2/P3 checklist application + coarse-consumer scan",
            "verdicts": [
                "P2_PREDICTION_HOLDS_NO_CONSUMER",
                "P3_PREDICTION_HOLDS_NO_CONSUMER",
                "COARSE_CONSUMER_SCAN_BOUNDED_NEGATIVE_WITH_TRIAGE_QUEUE",
            ],
            "scan": {
                "corpora": 3,
                "files": 4181,
                "hits": 239,
                "hits_with_obligation_token": 93,
                "triage_queue": 146,
                "manual_sample_read": 10,
                "receipt": SCAN_RECEIPT,
            },
            "new_math_claims": [],
            "new_proof_package": None,
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 104
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_P2_P3_AND_COARSE_SCAN",
            "status": STATUS,
            "next_minimal_verification": (
                "Coarse-consumer triage batch 1: take 20 of the 146 queued declarations, read each declaration's "
                "context and documentation, and decide whether the obligation is carried by the signature or by the "
                "codomain. Target P3 specifically: an interface whose domain is stage-erased/quotiented (or truncated) "
                "AND whose documented promise requires delivering a representative or uniform choice at a stage. Only "
                "such an interface can upgrade to NATURAL_USAGE_MISMATCH, and it must then be machine-formalised per "
                "MATH_PROOF_BEFORE_DELIVERY_V1."
            ),
        }
    )
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-088", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-088", "semantic_status": STATUS}
    )
    state["records"][REPORT_ID] = {
        "kind": "result",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-P1-TIME-LINE-BOUNDED-NEGATIVE-001", SCAN_ID],
        "full_sources": [REPORT, C11, P1_REPORT, SCAN_RECEIPT],
        "source_hashes": {REPORT: R.sha((root / REPORT).read_bytes())},
        "scope": (
            "P2/P3 application of the C11 checklist: P2 (same-layer) payment device is a level increment — available "
            "but expensive, consumer missing (S053 P8); P3 (intersection) has the strongest formal prerequisites "
            "because MP-NOCANONICAL-001 (C-142-C-148) already proves no uniform choice exists, and MP-ONLINE-CAUSALITY-001 "
            "gives the stage boundary. Both verdicts are PREDICTION_HOLDS_NO_CONSUMER; no new mathematical claim."
        ),
    }
    state["records"][SCAN_ID] = {
        "kind": "result",
        "path": SCAN_RECEIPT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [SESSION_ID, REPORT_ID],
        "full_sources": [SCAN_RECEIPT, SCAN_SCRIPT],
        "source_hashes": {SCAN_SCRIPT: R.sha((root / SCAN_SCRIPT).read_bytes())},
        "scope": (
            "Coarse-domain consumer scan over three pinned local corpora (Cubical v0.9 1091 files, agda-unimath "
            "7b81411d 3056 literate files, repo HoTT/formal 34 files): 239 hits where a coarse constructor appears "
            "before the first arrow in a top-level signature and the codomain is not prop/truncated by the lexical "
            "rule; 93 carry an obligation token in the signature; 146 form the triage queue; a fixed 10-hit manual "
            "sample all fell into harmless classes. Lexical scan only: it does not prove absence of coarse consumers "
            "and creates no mathematical claim."
        ),
    }
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, REPORT_ID, SCAN_ID],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, REPORT, SCAN_RECEIPT],
        "source_hashes": {},
        "scope": (
            "Registration of the P2/P3 checklist application and the coarse-consumer scan: verdicts, triage queue, "
            "projection/MEMORY/FRONTIER/LESSONS/RESUME updates. No mathematical change."
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
            "User said '继续' (continue) for the registered first work package: apply the C11 checklist to P2 and P3 and "
            "search for coarse-domain interfaces, then register the outcome. No new mathematical claim, no duplicate "
            "proof package, no network access, no push."
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
                "revision": 104,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
