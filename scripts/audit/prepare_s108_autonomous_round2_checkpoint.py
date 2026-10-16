#!/usr/bin/env python3
"""Prepare revision 108: register autonomous round 2 (invariant-obstruction search closed)."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-108-AUTONOMOUS-ROUND2"
PREV = "S-RES-20260913-107-TRIAGE-AND-OBLIGATION-ROUND1"
ROUND_ID = "A-AUTONOMOUS-ROUND2-001"
OUTCOME_ID = "OUT-TOP-AUTONOMOUS-ROUND2-INVARIANT-CLOSURE"
REPORT = "audit/自主构造第二轮-识别不敏感与相干义务-20260913.md"
ROUND1 = "audit/triage批次与自主构造第一轮-20260913.md"
C11 = "理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"

SPEC = importlib.util.spec_from_file_location("runtime_s108", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | 自主构造第二轮：把 S107 判据套到自有 `UnlabeledTwoElement` 族——6 个观察量逐项检查，"
    "命题值观察量（双射存在/基数 2/存在非平凡自同构/是集合/非空）**全部可完成**；唯一不可完成的是“统一选出一个点”，"
    "而它**不是**识别不敏感的。结构结论（`PAPER_ONLY`）：**不敏感 ⇒ 对族关系同余 ⇒ 消去器接受**，"
    "故“身份原则给不敏感任务强加不可满足义务”是空集 | `DIR-TOP-THEORY-ECONOMY-LEDGER` | "
    "用户 2026-09-13「继续」；当前工作包 | `DOCUMENTED / INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION` | "
    "该形状关闭；搜索转移到“**加入的结构改变了任务对象的同一性**”：(a) 表达/覆盖缺口（KC-000031/000035），"
    "(b) 识别改变对象身份且区别不可被“多带呈现”吸收。C-142–C-148 不受影响（它的任务本就不不敏感） | "
    "不新增数学 claim；§3 为纸笔结构论证；未重跑 run；负结论只覆盖“不敏感 + 义务”这一形状 | "
    f"`{REPORT}`；`{ROUND1}` |\n"
)

AUDIT_FOCUS = {
    "KC-000005": ("ALIGNED", "先固定判据与观察量表，再判负；不追认更强归因。"),
    "KC-000006": ("ALIGNED", "时间/运动结构仍未被本轮触及；未用“同阶段”替代。"),
    "KC-000010": ("ALIGNED", "仍以现实相对非现实性为目标；本轮只关闭一种形状。"),
    "KC-000014": ("ALIGNED", "B 方向候选（现实可做/理论不可做）在第一轮判负后，本轮关闭了其“义务”变体。"),
    "KC-000015": ("DEEPENED", "“加入的结构”从“义务”推进到“改变对象同一性/表达范围”，忠实于原话的加入面。"),
    "KC-000017": ("ALIGNED", "以消去器规则与同余语义约束判断，不靠印象。"),
    "KC-000021": ("ALIGNED", "本轮不新增机器证明，也未把纸笔结构论证写成定理；所有引用都可回源。"),
    "KC-000023": ("ALIGNED", "定位要求继续：义务发生在身份原则那一步已由 C-147/C-143 固定。"),
    "KC-000031": ("ALIGNED", "覆盖缺口被列为下一轮方向 (a)，但不启动新工作（现状 NOT_PROVEN）。"),
    "KC-000035": ("ALIGNED", "“HoTT 能否完整表达本套理论”被保留为表达层问题，而不是义务层问题。"),
    "KC-000027": ("ALIGNED", "共享机制与 HoTT 专属性分开；消去器义务是一般商结构的结果。"),
    "KC-000030": ("ALIGNED", "理论经济继续以“结构加入/义务/表达范围”三种形式被检查。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是自主构造第二轮（识别不敏感任务搜索的关闭），不产生数学结论。",
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
        "- direction_change: YES_IN_PLACE — 方向行原位记录“义务形状关闭、转向同一性/表达轴”。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/004 owner shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 关闭“不敏感任务 + 身份原则义务”形状；下一轮只在“同一性/表达”两轴上做有界检查。",
        "- cross_conflicts: 本条与评审 V2/V3 同向——把“不变量”与“义务”分开；C-142–C-148 的解释不受影响。",
        "- unresolved: (a)(b) 两轴均未做具体检查；coverage no-go 仍 NOT_PROVEN；无新机器证明。",
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
    if state.get("revision") != 107 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_107_S107")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "091"),
        ("PANORAMA", R.PANORAMA, "outcome", "091"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 107", "source_state_revision: 108"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-092",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/002 - 治理与用户方向.md",
        "下一轮搜索问题 = 找“**对理论识别不敏感、却在 HoTT 表达下不可完成**的任务” |",
        "**第二轮已关闭该搜索问题**：`UnlabeledTwoElement` 族的 6 个观察量里，命题值观察量全部可完成，"
        "唯一不可完成的“统一选点”**不是**识别不敏感的；结构论证（`PAPER_ONLY`）表明**不敏感 ⇒ 同余 ⇒ 消去器接受**，"
        "故“不敏感 + 义务”是空集（`INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION`）。"
        "下一轮只在两轴上做有界检查：(a) 表达/覆盖缺口（KC-000031/000035）；(b) 识别改变对象身份且区别不可被携带呈现吸收 |",
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
        "下一轮唯一搜索问题：找“**对理论识别不敏感、却在 HoTT 表达下不可完成**的任务”"
        "（现实侧程序须对理论识别不敏感，否则只是解释冲突）。",
        "第二轮已关闭上一轮的搜索问题：`UnlabeledTwoElement` 族上命题值观察量全部可完成，"
        "唯一不可完成的“统一选点”**不是**识别不敏感的；**不敏感 ⇒ 同余 ⇒ 消去器接受**，"
        "故“不敏感 + 身份原则义务”是空集（`INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION`）。"
        "下一轮只在两轴上做有界检查：**(a) 表达/覆盖缺口**（KC-000031/000035）；"
        "**(b) 识别改变对象身份、且区别不可被“多带呈现”吸收**。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S108 自主构造第二轮（用户「继续」）：把 S107 判据套到自有 `UnlabeledTwoElement`（`Σ A × ∥A ≃ Bool∥₁`）族——"
        "6 个观察量：双射存在/基数 2/存在非平凡自同构/是集合/非空 **全部可完成**（都是命题值或不变量），"
        "唯一不可完成的是“统一选出一个点”，而它**不是识别不敏感的**（C-143/C-144/C-145）。"
        "结构结论（`PAPER_ONLY`）：消去器的相干义务 = “对关系同余” = “不敏感”，因此**不敏感任务自动可定义**，"
        "“不敏感 + 不可满足义务”是空集 → 判 `INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION`，该形状关闭。"
        "自主构造线转向两轴：**(a) 表达/覆盖缺口**（KC-000031/000035，现状 NOT_PROVEN）；"
        "**(b) 识别改变对象身份且区别不可被携带呈现吸收**。未新增数学 claim；未重跑 run。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row56 = (
        "| 已闭合工作包 56 | triage 批次 1–2 与自主构造第一轮（S107） | "
        "`TRIAGE_LINE_CLOSED_PRECISION_LIMIT_REACHED` / `DEGENERATION_TEST_FAILED_KNOWN_PACKAGE` | "
        "线 A：两批 40 条实读全非候选（记录名/谓词名），队列 146→43 转附录；线 B：候选 #1（“加入义务”）"
        "逐步落在 C-142–C-148，退化测试判负；新筛选判据 = 新增义务可定位 + 不可满足 + 现实侧程序对理论识别不敏感；见 "
        "`audit/triage批次与自主构造第一轮-20260913.md` |"
    )
    frontier = replace_once(
        frontier,
        row56,
        row56 + "\n| 已闭合工作包 57 | 自主构造第二轮：识别不敏感任务搜索（S108） | "
        "`INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION` | `UnlabeledTwoElement` 族 6 个观察量：命题值全部可完成，"
        "唯一不可完成的“统一选点”不是不敏感的；结构论证：不敏感 ⇒ 同余 ⇒ 消去器接受，故“不敏感 + 义务”为空集；"
        f"见 `{REPORT}` |",
    )
    frontier = replace_once(
        frontier,
        "| 第一工作包 | 自主构造第二轮：找“对理论识别不敏感、却在 HoTT 表达下不可完成”的任务 | active | "
        "筛选判据（S107）：新增义务可定位 + 不可满足 + 现实侧程序在理论已识别层面上仍完成；"
        "先在同一族（C-142–C-148）上检查识别不变的观察量，再扩到商/截断/ua 替换族；"
        "线 A（词汇 triage）已关闭，仅在语义审计需要时重开 |",
        "| 第一工作包 | 自主构造第三轮：只在两轴上做有界检查 | active | (a) **表达/覆盖缺口**：任务的输出规格是否要求"
        "在理论里不存在/不可表达的对象（KC-000031/000035，现状 NOT_PROVEN，不启动新工作直到重新排队）；"
        "(b) **识别改变对象身份**：理论把两个现实上不同的对象识别为一，而任务的对象身份依赖该区别，"
        "且该区别**不可被“多带呈现”吸收**（否则只是解释冲突）。每轮一个有界检查并留失败位置 |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n87. “识别不敏感任务被身份原则强加不可满足义务”这一形状是**空集**：商/截断消去器的相干义务本身就等于"
        "“对关系同余”＝“对识别不敏感”，所以不敏感的任务自动可定义（在输出规格可形式化的前提下）。"
        "C-142–C-148 之所以成立，是因为“统一选点”**不是**不敏感的。教训：设计自主候选时先问"
        "“我的任务在理论做的识别下是否良定义”；若良定义，就不要再期待那里出现义务型悖论，"
        "而要去查表达/覆盖或对象同一性轴。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S108：自主构造第二轮完成并判 `INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION`——"
        "`UnlabeledTwoElement` 族上命题值观察量全部可完成，唯一不可完成的“统一选点”不是识别不敏感的；"
        "结构论证表明“不敏感 + 不可满足义务”是空集。自主构造线下一轮只在两轴做有界检查："
        "(a) 表达/覆盖缺口（KC-000031/000035）；(b) 识别改变对象身份且区别不可被携带呈现吸收。"
        "未新增数学 claim、未重跑 run。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户「继续」，执行 S107 登记的搜索问题（识别不敏感 + 理论不可完成）并在本轮关闭该形状。
- 交付：`{REPORT}`。
- 关键内容：`UnlabeledTwoElement` 族（`Σ A × ∥A ≃ Bool∥₁`）的 6 个观察量检查——双射存在/基数 2/存在非平凡自同构/
  是集合/非空全部可完成；唯一不可完成的是“统一选出一个点”，而它**不是**识别不敏感的（C-143/C-144/C-145）。
  结构论证（`PAPER_ONLY`）：消去器的相干义务 = “对关系同余” = “不敏感”，故“不敏感 + 不可满足义务”为空集
  → 判 `INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION`。
- 方向更新：自主构造线转向 (a) 表达/覆盖缺口、(b) 识别改变对象身份（区别不可被携带呈现吸收）。
- 状态边界：不新增数学 claim、不改判词、未重跑任何 run；§3 是纸笔结构论证；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "round": "autonomous round 2 (invariant-obstruction search)",
            "verdict": "INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION",
            "observables_checked": 6,
            "invariant_and_completable": 5,
            "non_invariant_and_obstructed": 1,
            "paper_argument": (
                "eliminator congruence obligation = insensitivity to the relation; hence an insensitive output spec "
                "automatically discharges the obligation and is definable (provided the spec is expressible)."
            ),
            "claims_used": ["C-142", "C-143", "C-144", "C-145", "C-146", "C-147", "C-148"],
            "new_math_claims": [],
            "new_proof_package": None,
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 108
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_AUTONOMOUS_ROUND2",
            "status": STATUS,
            "next_minimal_verification": (
                "Autonomous round 3, bounded to two axes: (a) expressibility/coverage gap — does the task's output "
                "spec require an object that does not exist or cannot be expressed in the theory (KC-000031/KC-000035; "
                "coverage no-go still NOT_PROVEN)? (b) identification changes object identity — the theory identifies "
                "two reality-distinct objects and the task's object identity depends on that distinction, which must "
                "NOT be absorbable by carrying presentations (otherwise it is only an interpretation conflict). "
                "The 'invariant task + obligation' shape is closed."
            ),
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-092", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-092", "semantic_status": STATUS}
    )
    state["records"][ROUND_ID] = {
        "kind": "result",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-TRIAGE-AND-OBLIGATION-ROUND1-001", "A-THEORY-ECONOMY-LEDGER-001"],
        "full_sources": [REPORT, ROUND1, C11, "HoTT/CLAIM_EVIDENCE_MATRIX.md"],
        "source_hashes": {REPORT: R.sha((root / REPORT).read_bytes())},
        "scope": (
            "Autonomous round 2: the S107 search question (identification-insensitive task that HoTT cannot complete) "
            "is closed. On the owned UnlabeledTwoElement family, five proposition-valued observables are completable "
            "and the only obstructed task (uniform choice) is not identification-insensitive. Paper-level structural "
            "argument: the eliminator's congruence obligation IS insensitivity, so 'insensitive + unsatisfiable "
            "obligation' is empty. Verdict INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION; no new mathematical claim."
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
            "Registration of autonomous round 2: verdict, observable table, paper-level structural argument, "
            "direction shift to the expressibility/identity axes, projection/MEMORY/FRONTIER/LESSONS/RESUME updates. "
            "No mathematical change."
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
            "User said '继续' after the previous turn was aborted. The previous turn's work (S107) was already applied and "
            "committed; this turn executes the registered next step: autonomous round 2, i.e. test whether an "
            "identification-insensitive task can be obstructed in HoTT. It closes that shape as empty by construction. "
            "No new mathematical claim, no push."
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
                "revision": 108,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
