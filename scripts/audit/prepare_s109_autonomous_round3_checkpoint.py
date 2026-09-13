#!/usr/bin/env python3
"""Prepare revision 109: register autonomous round 3 (expressibility/identity axes, search-space closure)."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-109-AUTONOMOUS-ROUND3"
PREV = "S-RES-20260913-108-AUTONOMOUS-ROUND2"
ROUND_ID = "A-AUTONOMOUS-ROUND3-001"
OUTCOME_ID = "OUT-TOP-SEARCH-SPACE-TWO-DOORS"
REPORT = "audit/自主构造第三轮-表达与身份两轴-20260913.md"
ROUND1 = "audit/triage批次与自主构造第一轮-20260913.md"
ROUND2 = "audit/自主构造第二轮-识别不敏感与相干义务-20260913.md"
C11 = "理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md"
C8 = "理解章节/C8-ERCF-3前置评估与最小代理任务-20260912.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"

SPEC = importlib.util.spec_from_file_location("runtime_s109", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | 自主构造第三轮与搜索空间收口：身份轴判 `IDENTITY_CHANGE_AXIS_REDUCES_TO_INTERPRETATION_CONFLICT`"
    "（任务对识别掉的差异的三种使用位置穷尽：答案里→解释冲突；不出现→消去器自动接受；假设/分支→仍要求区分呈现）；"
    "表达轴判 `EXPRESSIBILITY_AXIS_NO_HOTT_SPECIFIC_GAP`（自指真谓词=层级问题；用户悖论理论对象化=规格问题；"
    "芝诺形状=可表达）。收口命题：**可形式化的候选会被正确拒绝或被细化表示修复，故现实相对悖论只剩两扇门**——"
    "门 A 理论上不可形式化（需先给出可对象化规格）、门 B 同一层自我担保（ERCF-3/W51-3，gated 缺消费者） | "
    "`DIR-TOP-THEORY-ECONOMY-LEDGER` | 目标「全部做完再停下」；当前工作包 | "
    "`DOCUMENTED / SEARCH_SPACE_REDUCES_TO_TWO_DOORS` | 解释了 18 个机器包为何一致停在 "
    "`DEFENSE_WORKS`/`REPRESENTATION_BOUNDARY`；两条门的下一步都需要**新的真实输入**（规格或消费者），不再由现有材料自动产生 | "
    "不新增数学 claim；三轴判定均为 `PAPER_ONLY` 结构论证；未重跑 run；不声称 HoTT 没有问题 | "
    f"`{REPORT}`；`{ROUND1}`；`{ROUND2}` |\n"
)

AUDIT_FOCUS = {
    "KC-000005": ("ALIGNED", "两轴检查先固定问题与判据，判负后不追认更强归因。"),
    "KC-000010": ("ALIGNED", "目标仍是现实相对非现实性；本轮收口的是搜索空间，不是目标。"),
    "KC-000014": ("ALIGNED", "B 方向（理论承诺多于现实可交付）被归入门 B（自我担保）而非表达轴。"),
    "KC-000015": ("DEEPENED", "“加入的结构”最终收敛为两种：不可形式化与层级担保。"),
    "KC-000017": ("ALIGNED", "以消去器语义与自有 claim 约束判断；未用“HoTT 无问题”收尾。"),
    "KC-000021": ("ALIGNED", "本轮不新增机器证明；收口命题明确标为 PAPER_ONLY 且可反驳。"),
    "KC-000023": ("ALIGNED", "时间/运动结构未由本轮关闭，仍属“需先对象化规格”的门 A 输入。"),
    "KC-000025": ("ALIGNED", "自指线仍要求实际连接（门 B 缺消费者），不以术语并列替代构造。"),
    "KC-000026": ("ALIGNED", "HoTT 自身自指不可越过的怀疑保留为门 B，未从边界正例推全局豁免。"),
    "KC-000031": ("DEEPENED", "最小理想理论覆盖问题被定位为“规格 vs 能力”的判别问题，并列出门 A。"),
    "KC-000035": ("DEEPENED", "“HoTT 能否完整表达本套理论”被明确为需先把“现实量”对象化。"),
    "KC-000036": ("ALIGNED", "Gödel/自馈仍归门 B；无真实消费者前不作 HoTT 特有结论。"),
    "KC-000030": ("ALIGNED", "理论经济继续以“义务/表达/层级”三种形式被检查。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是自主构造第三轮与搜索空间收口，不产生数学结论。",
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
        "- direction_change: YES_IN_PLACE — 方向行原位记录两轴判负与“两扇门”收口。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/004 owner shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 关闭身份轴与表达轴的同型枚举；第一工作包改为“门 A 需先对象化规格 / 门 B 需自我担保消费者”。",
        "- cross_conflicts: 收口命题与 C11 v2 “不把猜想当门槛”的约束一致——它被标为可反驳的 PAPER_ONLY 命题，不用于拒绝候选。",
        "- unresolved: 门 A 的“现实量规格”未给出；门 B 的消费者未构造；coverage no-go 仍 NOT_PROVEN；无新机器证明。",
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
    if state.get("revision") != 108 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_108_S108")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "092"),
        ("PANORAMA", R.PANORAMA, "outcome", "092"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 108", "source_state_revision: 109"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-093",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/002 - 治理与用户方向.md",
        "下一轮只在两轴上做有界检查：(a) 表达/覆盖缺口（KC-000031/000035）；"
        "(b) 识别改变对象身份且区别不可被携带呈现吸收 |",
        "**两轴均已判负**：身份轴 → `IDENTITY_CHANGE_AXIS_REDUCES_TO_INTERPRETATION_CONFLICT`；"
        "表达轴 → `EXPRESSIBILITY_AXIS_NO_HOTT_SPECIFIC_GAP`（自指真谓词=层级问题、悖论理论对象化=规格问题、芝诺形状可表达）。"
        "**搜索空间收口**：可形式化的候选会被正确拒绝或被细化修复，现实相对悖论只剩两扇门——"
        "**门 A** 理论上不可形式化（需先给出可对象化的现实量规格）、**门 B** 同一层自我担保（ERCF-3/W51-3，gated 缺消费者）。"
        "两条门都需要新的真实输入 |",
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
        "下一轮只在两轴上做有界检查：**(a) 表达/覆盖缺口**（KC-000031/000035）；"
        "**(b) 识别改变对象身份、且区别不可被“多带呈现”吸收**。",
        "第三轮（S109）已把两轴做完并判负：身份轴 → 解释冲突；表达轴 → 无 HoTT 特有缺口。"
        "**搜索空间收口为两扇门**：**门 A** 任务在 HoTT 中不可形式化（须先给出可对象化的现实量规格）；"
        "**门 B** 同一层自我担保（ERCF-3 / W51-3，`GATED`，缺自我担保消费者）。"
        "两条门都**需要新的真实输入**（规格或消费者），不再由现有材料自动产生；同型枚举停止。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S109 自主构造第三轮与搜索空间收口（目标「全部做完再停下」当前登记工作包）：身份轴检查——任务对识别掉的"
        "差异的三种使用位置（答案/不出现/假设分支）穷尽，分别落回解释冲突、消去器自动接受、解释冲突 → "
        "判 `IDENTITY_CHANGE_AXIS_REDUCES_TO_INTERPRETATION_CONFLICT`；表达轴检查——自指真谓词（层级问题）、"
        "用户悖论理论对象化（规格问题）、芝诺形状（可表达）→ 判 `EXPRESSIBILITY_AXIS_NO_HOTT_SPECIFIC_GAP`。"
        "**收口命题**（`PAPER_ONLY`，可反驳）：在商/截断/ua/消去器语义下，可形式化的“合理+合法+不可完成”候选"
        "必然依赖被识别或悬置的因子，而消去器义务正是该依赖良定义的判据 → 故现实相对悖论只剩**门 A（不可形式化）**"
        "与**门 B（同层自我担保）**。这解释了 18 个机器包为何一致停在 `DEFENSE_WORKS`/`REPRESENTATION_BOUNDARY`。"
        "未新增数学 claim、未重跑 run。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row57 = (
        "| 已闭合工作包 57 | 自主构造第二轮：识别不敏感任务搜索（S108） | "
        "`INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION` | `UnlabeledTwoElement` 族 6 个观察量：命题值全部可完成，"
        "唯一不可完成的“统一选点”不是不敏感的；结构论证：不敏感 ⇒ 同余 ⇒ 消去器接受，故“不敏感 + 义务”为空集；见 "
        "`audit/自主构造第二轮-识别不敏感与相干义务-20260913.md` |"
    )
    frontier = replace_once(
        frontier,
        row57,
        row57 + "\n| 已闭合工作包 58 | 自主构造第三轮与搜索空间收口（S109） | "
        "`IDENTITY_CHANGE_AXIS_REDUCES_TO_INTERPRETATION_CONFLICT` / `EXPRESSIBILITY_AXIS_NO_HOTT_SPECIFIC_GAP` / "
        "`SEARCH_SPACE_REDUCES_TO_TWO_DOORS` | 身份轴三位置穷尽；表达轴三候选均无 HoTT 特有缺口；"
        f"收口为门 A（不可形式化，先需规格）/ 门 B（同层自我担保，gated 缺消费者）；见 `{REPORT}` |",
    )
    frontier = replace_once(
        frontier,
        "| 第一工作包 | 自主构造第三轮：只在两轴上做有界检查 | active | (a) **表达/覆盖缺口**：任务的输出规格是否要求"
        "在理论里不存在/不可表达的对象（KC-000031/000035，现状 NOT_PROVEN，不启动新工作直到重新排队）；"
        "(b) **识别改变对象身份**：理论把两个现实上不同的对象识别为一，而任务的对象身份依赖该区别，"
        "且该区别**不可被“多带呈现”吸收**（否则只是解释冲突）。每轮一个有界检查并留失败位置 |",
        "| 第一工作包 | 两扇门各一等价输入：门 A 需可对象化的现实量规格；门 B 需自我担保消费者 | awaiting-external-input | "
        "门 A：先写出一个**可严格书写的现实量规格**（阶段可用性+截止期已可对象化，不能再作候选），再问 HoTT 能否形成该对象；"
        "门 B：构造或找到一个**要求理论在同一层担保自身判断**的消费者，按 C8 的 P1–P8 检查（W51-3 = E6 的自指版本）。"
        "同型枚举已停止；两条门在没有新输入前不启动新的机器证明 |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n88. 当一条自主搜索线连续关闭多个形状（支付装置可用 / 昂贵 / 不存在；词汇 triage；不敏感+义务；身份轴；表达轴）后，"
        "应当写一次**搜索空间收口**：把“还剩什么可能”写成门，并明确每条门需要的**新输入类型**。"
        "本轮收口结论：可形式化的候选会被消去器的良定义性义务正确拒绝或被细化表示修复，因此现实相对悖论只剩"
        "“不可形式化（先需规格）”与“同层自我担保（需消费者）”两扇门。收口命题必须标 `PAPER_ONLY` 且可反驳，"
        "不得当成新的准入 Gate。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S109：自主构造第三轮完成，身份轴与表达轴均判负，**搜索空间收口为两扇门**——门 A（任务在 HoTT 中不可形式化，"
        "须先给出可对象化的现实量规格）、门 B（同一层自我担保，ERCF-3/W51-3，`GATED` 缺消费者）。"
        "两条门都需要**新的真实输入**；同型枚举停止。未新增数学 claim、未重跑 run。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目标「全部做完再停下」的当前登记工作包：自主构造第三轮（两轴有界检查）＋ 搜索空间收口。
- 交付：`{REPORT}`。
- 判词：身份轴 `IDENTITY_CHANGE_AXIS_REDUCES_TO_INTERPRETATION_CONFLICT`；表达轴 `EXPRESSIBILITY_AXIS_NO_HOTT_SPECIFIC_GAP`；
  收口 `SEARCH_SPACE_REDUCES_TO_TWO_DOORS`。
- 收口内容：可形式化的候选会被消去器的良定义性义务正确拒绝或被细化表示修复 → 只剩门 A（不可形式化，先需规格）
  与门 B（同层自我担保，需消费者）；这解释了 18 个机器包为何一致停在 `DEFENSE_WORKS`/`REPRESENTATION_BOUNDARY`。
- 状态边界：§1–§3 为 `PAPER_ONLY` 结构论证；不新增数学 claim、不改判词、未重跑 run；收口命题不是新的准入 Gate；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "round": "autonomous round 3 (expressibility + identity axes) and search-space closure",
            "verdicts": [
                "IDENTITY_CHANGE_AXIS_REDUCES_TO_INTERPRETATION_CONFLICT",
                "EXPRESSIBILITY_AXIS_NO_HOTT_SPECIFIC_GAP",
                "SEARCH_SPACE_REDUCES_TO_TWO_DOORS",
            ],
            "doors": {
                "A": "task not formalisable in HoTT (requires a formalisable specification of a reality quantity first)",
                "B": "same-layer self-guarantee (ERCF-3 / W51-3, gated, needs a consumer)",
            },
            "new_math_claims": [],
            "new_proof_package": None,
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 109
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_AUTONOMOUS_ROUND3",
            "status": STATUS,
            "next_minimal_verification": (
                "Two doors, each awaiting a new external input. Door A: write a strictly formalisable specification of "
                "a reality quantity that is not yet objectified (stage availability + deadline is already objectified and "
                "therefore cannot serve), then test whether HoTT can form the object; classify the result as a "
                "specification gap or a HoTT capability gap. Door B: construct or find a consumer requiring the theory to "
                "guarantee its own judgement in the same layer; run C8's P1-P8 checklist (W51-3 = the self-referential E6). "
                "Homogeneous enumeration is stopped; no new machine proof starts before such an input exists."
            ),
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-093", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-093", "semantic_status": STATUS}
    )
    state["records"][ROUND_ID] = {
        "kind": "result",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-AUTONOMOUS-ROUND2-001", "A-TRIAGE-AND-OBLIGATION-ROUND1-001",
                            "A-THEORY-ECONOMY-LEDGER-001"],
        "full_sources": [REPORT, ROUND1, ROUND2, C11, C8],
        "source_hashes": {REPORT: R.sha((root / REPORT).read_bytes())},
        "scope": (
            "Autonomous round 3: identity axis closed (three positions of the erased distinction all reduce to "
            "interpretation conflict or automatic acceptance), expressibility axis closed for HoTT-specific gaps "
            "(self-referential truth predicate = level issue; objectifying the user's paradox theory = specification "
            "issue; Zeno shape = expressible). Search-space closure: only two doors remain - A not formalisable, "
            "B same-layer self-guarantee. Explains why all 18 packages stop at DEFENSE_WORKS/REPRESENTATION_BOUNDARY. "
            "No new mathematical claim; paper-only structural argument."
        ),
    }
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, ROUND_ID],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, REPORT],
        "source_hashes": {},
        "scope": (
            "Registration of autonomous round 3 and the search-space closure: verdicts, two doors, projection/MEMORY/"
            "FRONTIER/LESSONS/RESUME updates. No mathematical change."
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
            "Active goal 'finish everything before stopping'. The registered first work package was autonomous round 3: "
            "two bounded checks (expressibility/coverage axis and identity axis) plus, when both close, a search-space "
            "consolidation. This transaction registers those verdicts and the two remaining doors. No new mathematical "
            "claim, no push."
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
                "revision": 109,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
