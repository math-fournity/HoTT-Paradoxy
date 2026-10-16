#!/usr/bin/env python3
"""Prepare revision 105: absorb the independent C11 review and register the v2 revision."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-GOV-20260913-105-C11-REVIEW-ABSORPTION"
PREV = "S-RES-20260913-104-P2-P3-AND-COARSE-SCAN"
IMPORT_ID = "A-C11-REVIEW-IMPORT-001"
ABSORB_ID = "A-C11-REVIEW-ABSORPTION-001"
OUTCOME_ID = "OUT-TOP-C11-REVIEW-ABSORPTION"
IMPORT_ROOT = "audit/imports/c11-review-20260913"
IMPORT_FILE = f"{IMPORT_ROOT}/20260913-C11统观思路独立评审.md"
IMPORT_JSON = f"{IMPORT_ROOT}/IMPORT.json"
ABSORB_REPORT = "audit/c11评审吸收与独立核验-20260913.md"
C11 = "理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md"
P2P3_REPORT = "audit/p2-p3与粗域接口搜索-20260913.md"
LEDGER_RECORD = "A-THEORY-ECONOMY-LEDGER-001"
P2P3_RECORD = "A-P2-P3-CHECKLIST-001"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"

SPEC = importlib.util.spec_from_file_location("runtime_s105", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | 吸收另一 AI 对 C11 的独立评审：评审 5 条主主张 + 5 条细节全部 `ACCEPTED`"
    "（一条附范围限定），C11 原位修订为 **v2** | `DIR-TOP-THEORY-ECONOMY-LEDGER` | 用户转交外部评审"
    f"（字节保全 `{IMPORT_FILE}`，SHA-256 `e41f07b0…`） | `DOCUMENTED / ABSORPTION_AND_INDEPENDENT_VERIFICATION` | "
    "核验要点：`labeledChoice` 属“预先保留”而非恢复；`canon` 丢等待时间；`GuardErasure` 是等价刻画不是判定器；"
    "集合商消去到集合只需尊重关系 + 集合余域；v1 §5 结论句与“装置不存在”列口径冲突。v2 变化：接上 Theory Schema/C6、"
    "不变量降为非判据、六字段账本、补偿动作三分、四坐标分离、2×2 降为检查坐标、补时间结构与 B 方向、"
    "回溯结论降级为“归类一致性”。 | 不新增数学 claim；评审不因转交升格为事实；v1 由 Git 保存 | "
    f"`{ABSORB_REPORT}`；`{IMPORT_JSON}`；`{C11}` |\n"
)

AUDIT_FOCUS = {
    "KC-000005": ("DEEPENED", "评审明确反对“先完成整套排他归因才允许构造”，v2 删除了判别格的门槛化用法。"),
    "KC-000006": ("ALIGNED", "v2 增补“时间与运动结构”为独立检查坐标，不让“同阶段”替代时间问题。"),
    "KC-000010": ("ALIGNED", "吸收过程仍以现实相对非现实性为目标，不改判词。"),
    "KC-000013": ("DEEPENED", "“补偿操作”被拆成恢复/预先保留/新增三类，逐例核对理论经济代价。"),
    "KC-000014": ("ALIGNED", "v2 把 B 方向（未完成被当已取得）列为独立检查项，不再由两坐标覆盖。"),
    "KC-000015": ("ALIGNED", "“理论加入理想结构”与“遗忘现实因子”并列，忠实于原话的双向含义。"),
    "KC-000017": ("ALIGNED", "吸收外部评审但逐条独立核验，不因外部意见或共识消音/改写用户问题。"),
    "KC-000021": ("ALIGNED", "本轮未新增机器证明；核验只做源码与文本核对，未重放 run。"),
    "KC-000022": ("ALIGNED", "A/B 两类目标在 v2 中并列保留，B 方向获得独立位置。"),
    "KC-000023": ("ALIGNED", "v2 明确“同阶段/同层”不能替代时间与运动结构的定位要求。"),
    "KC-000025": ("ALIGNED", "P3 增加退化测试，避免用术语并列冒充新构造。"),
    "KC-000027": ("ALIGNED", "共享机制与专属性分开，评审与吸收都没有要求机制独有。"),
    "KC-000028": ("ALIGNED", "自指担保的四坐标分离（宇宙/元理论/扩展/阶段）避免“升层即出理论”的笼统说法。"),
    "KC-000030": ("DEEPENED", "行类型字段把原始规则、派生定理、表示选择、可选扩展、实现事实分开。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是外部评审的独立核验与 C11 v2 修订，不产生数学结论。",
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
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{ABSORB_REPORT}`；{kid} | 数学开放项不变。 |"
        )
    aligned = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "ALIGNED")
    deepened = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "DEEPENED")
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: YES_IN_PLACE — 方向行原位记录 C11 v2 与评审吸收；研究第一线补上“自主构造 + 退化测试”。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/004 owner shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 评审 5 主条 + 5 细节全部吸收（一条附范围限定）；C11 原位升为 v2；判别格由门槛降为检查坐标。",
        "- cross_conflicts: v1 §5 结论句与“装置不存在”列的口径冲突已按三类装置改写；评审“还不是有效验证”与本报告“归类一致性已完成”并存为诚实分层。",
        "- unresolved: 逐行复活条件生成、时间/运动结构落行、B 方向独立成行、退化测试实际执行均未完成；无新候选。",
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
    if state.get("revision") != 104 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_104_S104")

    c11_hash = R.sha((root / C11).read_bytes())
    p2p3_hash = R.sha((root / P2P3_REPORT).read_bytes())
    repinned = []
    for record_id, path, new_hash, why in (
        (LEDGER_RECORD, C11, c11_hash, "C11 was revised in place to v2 after the independent review was absorbed "
                                        "(six-field ledger, compensation-action trichotomy, four separate level "
                                        "coordinates, 2x2 grid demoted to a check coordinate, retrodiction claim "
                                        "downgraded to classification consistency)."),
        (P2P3_RECORD, P2P3_REPORT, p2p3_hash, "the P2/P3 report gained a v2 framing note: the grid is a check "
                                              "coordinate rather than a gate, and P3 must pass the degeneration test."),
    ):
        record = state["records"][record_id]
        hashes = record.get("source_hashes") or {}
        if hashes.get(path) == new_hash:
            continue
        hashes[path] = new_hash
        record["source_hashes"] = hashes
        record["revalidation"] = f"{path} re-hashed by {SESSION_ID}: {why} Claim and scope unchanged."
        repinned.append(record_id)
    if sorted(repinned) != sorted([LEDGER_RECORD, P2P3_RECORD]):
        raise SystemExit(f"EXPECTED_TWO_REPINNED:{sorted(repinned)}")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "088"),
        ("PANORAMA", R.PANORAMA, "outcome", "088"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 104", "source_state_revision: 105"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-089",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/002 - 治理与用户方向.md",
        "下一步：triage 批次 1（20 条）＋ P3 定向找“文档承诺 > 接口类型能力”的真实接口 |",
        "**C11 已按独立评审修订为 v2**（`" + ABSORB_REPORT + "`：5 主条 + 5 细节全部吸收；判别格由门槛降为检查坐标，"
        "补偿动作三分，补时间结构与 B 方向）；下一步并行两条：**自主构造**（独立任务 → 规则改动 → 合法推演 → 对应回原活动，"
        "组合候选必过退化测试）与 **triage 批次 1（20 条）** 找“文档承诺 > 接口类型能力”的真实接口 |",
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
        "下一轮：146 条 triage 队列取 20 条逐条读，并定向找“**文档承诺 > 接口类型能力**”的真实接口"
        "（类型层已由消去器的同余义务关闭）。",
        "C11 已吸收独立评审并修订为 **v2**：判别格**不再是准入门槛**，而是检查坐标之一；账本改为六字段"
        "（行类型/经济决策/被悬置或被加入的因子/补偿操作/复活条件/现有判词），补偿动作三分"
        "（恢复/预先保留/新增），并补入时间与运动结构、B 方向与退化测试。下一轮**两条并行**："
        "① 自主构造（独立任务 → 哪条规则/规则组合改变前提 → 合法推演 → 对应回原活动），"
        "② 146 条 triage 队列取 20 条，定向找“**文档承诺 > 接口类型能力**”的真实接口。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S105 吸收另一 AI 对 C11 的独立评审（用户转交 `20260913-C11统观思路独立评审.md`，"
        "字节保全导入 `audit/imports/c11-review-20260913/`，SHA-256 `e41f07b0…`；被评 v1 哈希 `8452e1a2…` 与评审自述一致）："
        "5 条主主张 + 5 条细节**全部逐项独立核验后接受**（一条附范围限定），无实质驳回。核验要点："
        "`NoCanonicalPoint.agda:108-114` 的 `labeledChoice` 是**预先保留**而非恢复；`QuotientMonad.agda:57-61` 的 `canon` "
        "丢掉等待时间；`GuardErasure.agda:36-58` 是**等价刻画 + 特定反例**而非判定器；集合商消去到集合只需“尊重关系 + "
        "集合余域”（canonical section 是另一件事）；v1 §5 结论句与“装置不存在”列口径冲突。**C11 原位修订为 v2**："
        "接上 `THEORY_SCHEMA.md`/C6；不变量降为**非判据**；六字段账本 + 行类型；补偿动作三分；四坐标分离"
        "（宇宙大小/对象-元理论/理论扩展/执行阶段）；2×2 降为检查坐标；补时间与运动结构、B 方向、退化测试；"
        "回溯结论降级为“归类一致性”。未新增数学 claim，未改判词；v1 由 Git 保存。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row53 = (
        "| 已闭合工作包 53 | P2/P3 判别格应用与粗域接口搜索（S104） | "
        "`P2_PREDICTION_HOLDS_NO_CONSUMER` / `P3_PREDICTION_HOLDS_NO_CONSUMER` / "
        "`COARSE_CONSUMER_SCAN_BOUNDED_NEGATIVE_WITH_TRIAGE_QUEUE` | P2 支付装置=层级上升（昂贵但存在）；"
        "P3 形式要件最齐（支付装置已由 C-142–C-148 证明不存在）；三语料 239 命中 / 93 带义务 / 146 triage，"
        "10 例实读全部无害；见 `audit/p2-p3与粗域接口搜索-20260913.md` 与 "
        "`audit/coarse-consumer-scan-20260913.json` |"
    )
    frontier = replace_once(
        frontier,
        row53,
        row53 + "\n| 已闭合工作包 54 | C11 独立评审吸收与 v2 修订（S105） | "
        "`ABSORPTION_AND_INDEPENDENT_VERIFICATION`（5 主条 + 5 细节全部 ACCEPTED，一条附范围限定） | "
        "C11 v1→v2：接上 Theory Schema/C6、不变量降为非判据、六字段账本、补偿动作三分、四坐标分离、"
        "2×2 降为检查坐标、补时间结构与 B 方向、回溯结论降级；v1 由 Git 保存；见 "
        f"`{ABSORB_REPORT}` |",
    )
    frontier = replace_once(
        frontier,
        "| 第一工作包 | triage 队列批次 1（146 条取 20）＋ P3 定向搜索“粗域接口 + 阶段交付承诺” | active | "
        "逐条读命中声明的上下文与文档段落，判义务是否由签名/余域承担；若出现“必须取回 + 同阶段/同层”全命中的"
        "真实接口，按 P1 报告 §6 的三条 claim 草案走 F-011；否则保持有界负结论 |",
        "| 第一工作包 | ① 自主构造（C11 v2 §6 路线）② triage 批次 1（146 取 20）＋ P3 定向 | active | "
        "自主构造：独立任务 → 理论如何表示 → 哪条规则/规则组合改变了什么 → 合法推演产生什么 → 对应回原活动；"
        "组合候选必过退化测试。triage：逐条读命中声明的上下文与文档段落，判义务由签名还是余域承担；"
        "命中“必须取回 + 同阶段/同层”的真实接口时按 P1 报告 §6 草案走 F-011 |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n84. 吸收外部评审时，先做**逐项独立核验**再决定判词：本轮 5 主条 + 5 细节全部成立，但核验本身产生了新事实——"
        "`labeledChoice` 是“预先保留”而非“恢复”、`canon` 丢弃等待时间、`GuardErasure` 是等价刻画不是判定器、"
        "集合商消去到集合只需尊重关系 + 集合余域。方法层的第二课：**不要把待检验的猜想变成准入 Gate**；"
        "判别坐标只能描述候选的处境，不能决定它是否有资格被研究；“补偿操作”必须逐例写成可检查的三类动作"
        "（恢复/预先保留/新增），否则“表示更细”会掩盖换了任务。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S105：另一 AI 对 C11 的独立评审已字节保全导入并逐项核验（5 主条 + 5 细节全部接受，一条附范围限定）；"
        "C11 原位修订为 **v2**（判别格降为检查坐标、六字段账本、补偿动作三分、四坐标分离、补时间结构与 B 方向、"
        "回溯结论降级为归类一致性、新增退化测试）。未新增数学 claim。下一步两条并行：自主构造（须过退化测试）"
        "与 triage 批次 1（146 取 20）。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户转交另一 AI 的独立评审 `20260913-C11统观思路独立评审.md`，要求评估。
- 处置：字节保全导入 `{IMPORT_ROOT}/`（`e41f07b0…`，与来源逐字节一致；被评 C11 v1 哈希 `8452e1a2…` 与评审自述一致）
  → 逐项独立核验（`{ABSORB_REPORT}`：5 主条 + 5 细节全部 `ACCEPTED`，一条附范围限定；无实质驳回）
  → C11 原位修订为 v2，并在 `{P2P3_REPORT}` 顶部加 v2 口径备注。
- v2 主要变化：接上 `THEORY_SCHEMA.md`/C6；总账不变量降为**非判据**；账本六字段 + 行类型；补偿动作三分
  （恢复/预先保留/新增）；四坐标分离（宇宙大小/对象-元理论/理论扩展/执行阶段）；2×2 降为检查坐标；
  补时间与运动结构、B 方向、退化测试；回溯结论降级为“归类一致性”；保留自主构造路线。
- 本 checkpoint 写 machine-managed 状态：`STATE.revision=105`、两个 revalidation（`{LEDGER_RECORD}` / `{P2P3_RECORD}`）、
  结果 `{ABSORB_ID}` 与导入 `{IMPORT_ID}`、方向行原位更新、全景新结果行、MEMORY/FRONTIER/LESSONS 84/RESUME。
- 状态边界：不新增数学 claim、不改判词、未重放任何 run、未访问网络；v1 由 Git 保存；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "imported_review": {
                "path": IMPORT_FILE,
                "sha256": "e41f07b095704fcff6f19ebf901ddd68b2badf71c9afed1bd8d10d5321fabd77",
                "reviewed_c11_v1_sha256": "8452e1a2a3137e057919694e401a99a1c52c3d2b9c4d009f0a26d9260c4d6a8b",
            },
            "verdicts": {"main_claims": 5, "details": 5, "accepted": 10, "rejected": 0, "accepted_with_scope": 1},
            "c11_v2_sha256": c11_hash,
            "repinned_records": repinned,
            "new_math_claims": [],
            "new_proof_package": None,
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 105
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_C11_REVIEW_ABSORPTION",
            "status": STATUS,
            "next_minimal_verification": (
                "Two parallel lines. (1) Autonomous construction per C11 v2 §6: pick an independent task, state how the "
                "theory represents it, which rule or rule combination changes the premise, what the legal derivation "
                "produces, and how it maps back to the original activity; combination candidates must pass the "
                "degeneration test. (2) Coarse-consumer triage batch 1 (20 of 146) looking for an interface whose "
                "documentation promises more than its type can deliver. Any hit goes to MATH_PROOF_BEFORE_DELIVERY_V1 "
                "per the P1 report §6 draft."
            ),
        }
    )
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-089", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-089", "semantic_status": STATUS}
    )
    state["records"][IMPORT_ID] = {
        "kind": "result",
        "path": IMPORT_JSON,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [SESSION_ID, ABSORB_ID],
        "full_sources": [IMPORT_FILE, IMPORT_JSON, ABSORB_REPORT],
        "source_hashes": {IMPORT_FILE: R.sha((root / IMPORT_FILE).read_bytes())},
        "scope": (
            "Byte-preserved import of another AI's independent review of C11 (DOCUMENT_REVIEW / METHOD_PROPOSAL, not a "
            "shared-repo owner). Carries no mathematical claim and does not promote the review's statements to facts."
        ),
    }
    state["records"][ABSORB_ID] = {
        "kind": "result",
        "path": ABSORB_REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [SESSION_ID, IMPORT_ID, LEDGER_RECORD, P2P3_RECORD],
        "full_sources": [ABSORB_REPORT, IMPORT_FILE, C11, P2P3_REPORT],
        "source_hashes": {ABSORB_REPORT: R.sha((root / ABSORB_REPORT).read_bytes())},
        "scope": (
            "Item-by-item independent verification of the C11 review: five main claims and five detail items, all "
            "accepted (one with a scope qualifier), no substantive rejection. Verification used source lines "
            "(NoCanonicalPoint.agda labeledChoice; QuotientMonad.agda canon; GuardErasure.agda equivalence plus "
            "counterexample; Cubical SetQuotients rec/elim). Resulted in the in-place C11 v2 revision: grid demoted "
            "from gate to check coordinate, six-field ledger, compensation-action trichotomy, four level coordinates, "
            "time-structure and B-direction coverage, degeneration test, retrodiction claim downgraded."
        ),
    }
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, IMPORT_ID, ABSORB_ID],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, ABSORB_REPORT, IMPORT_JSON],
        "source_hashes": {},
        "scope": (
            "Absorption of the external C11 review and registration of the C11 v2 revision: import, verification "
            "report, two record revalidations (ledger + P2/P3 report), projection/MEMORY/FRONTIER/LESSONS/RESUME "
            "updates. No mathematical change."
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
            "User asked to evaluate another AI's partial review of C11. The review was byte-preserved, verified item "
            "by item, and the accepted corrections were applied in place to C11 v2 (plus a framing note on the P2/P3 "
            "report). No new mathematical claim, no verdict change, no network access, no push."
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
                "revision": 105,
                "session_id": SESSION_ID,
                "files": len(texts),
                "c11_v2_sha256": c11_hash,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
