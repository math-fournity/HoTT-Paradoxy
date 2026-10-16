#!/usr/bin/env python3
"""Prepare revision 107: register triage round 1 (closed) and autonomous candidate #1 (failed)."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-107-TRIAGE-AND-OBLIGATION-ROUND1"
PREV = "S-GOV-20260913-106-C11-V2-REPIN"
ROUND_ID = "A-TRIAGE-AND-OBLIGATION-ROUND1-001"
OUTCOME_ID = "OUT-TOP-TRIAGE-AND-OBLIGATION-ROUND1"
REPORT = "audit/triage批次与自主构造第一轮-20260913.md"
SCAN_RECEIPT = "audit/coarse-consumer-scan-20260913.json"
SCAN_SCRIPT = "scripts/audit/scan_coarse_consumers.py"
SCAN_RECORD = "A-COARSE-CONSUMER-SCAN-001"
C11 = "理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"

SPEC = importlib.util.spec_from_file_location("runtime_s107", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | C11 v2 §6 两条并行线第一轮：线 A（粗域接口 triage）两批 40 条全为非候选 → "
    "判 `TRIAGE_LINE_CLOSED_PRECISION_LIMIT_REACHED`（词汇级对命名约定无分辨力，43 条队列转为附录）；"
    "线 B（自主构造候选 #1＝“加入义务”读法）逐步落在 C-142–C-148 → 判 `DEGENERATION_TEST_FAILED_KNOWN_PACKAGE` | "
    "`DIR-TOP-THEORY-ECONOMY-LEDGER` | 用户 2026-09-13「开始」；当前工作包 | "
    "`DOCUMENTED / BOUNDED_NEGATIVE_PLUS_FILTER_CRITERION` | 本轮唯一新产出是**候选筛选判据**：新增义务须可定位 + "
    "不可满足 + **现实侧程序在理论已识别的层面上仍然完成**；若现实侧解依赖被识别掉的呈现（本候选即是），那是解释冲突而非悖论 | "
    "不新增数学 claim；线 B 的数学全部来自 C-142–C-148，未重证；线 A 负结论只覆盖两批 40 条实读样本与固定规则 | "
    f"`{REPORT}`；`{SCAN_RECEIPT}` |\n"
)

AUDIT_FOCUS = {
    "KC-000005": ("ALIGNED", "两条线都先固定候选与判据，判负后不追认归因。"),
    "KC-000007": ("DEEPENED", "线 B 的“加入义务”读法直接把“理论要求了更多什么”定位到身份原则那一步。"),
    "KC-000010": ("ALIGNED", "仍以现实相对非现实性为目标；两轮都是有界负结论。"),
    "KC-000014": ("ALIGNED", "B 方向（现实可做/理论不可做）被具体化为候选 #1，并判为解释冲突而非悖论。"),
    "KC-000015": ("DEEPENED", "“否定”被补上“加入”的一面：身份原则加入相干义务，而不是仅仅遗忘。"),
    "KC-000017": ("ALIGNED", "用机器 claim 与源码定位约束判断，不靠印象；两批假阳性被如实登记。"),
    "KC-000021": ("ALIGNED", "本轮不新增机器证明；线 B 的机器证据全部引用既有 C-142–C-148。"),
    "KC-000022": ("ALIGNED", "第一类/第二类目标都保留了位置；候选 #1 属第二类形状但判负。"),
    "KC-000023": ("DEEPENED", "把“理论在哪一步改变了前提”推进为可定位的“识别步 + 相干义务”。"),
    "KC-000025": ("ALIGNED", "退化测试用于防止用术语并列冒充新构造。"),
    "KC-000027": ("ALIGNED", "共享机制不冒充 HoTT 独有；候选 #1 的机制来自身份原则而非 HoTT 独有。"),
    "KC-000030": ("ALIGNED", "“理论经济”继续以补偿操作/义务的形式被检查。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是两条并行线的第一轮（triage 关闭 + 自主候选 #1 判负），不产生数学结论。",
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
        "- direction_change: YES_IN_PLACE — 方向行原位记录线 A 关闭、线 B 第一轮判负与新筛选判据。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/004 owner shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 线 A 停止逐条读队列（精度极限）；线 B 采用新筛选判据（现实侧程序须对理论识别不敏感）。",
        "- cross_conflicts: 线 A 的机械结果与评审“不要把 grep 当候选”一致；线 B 的“现实可做/理论不可做”被判为解释冲突，与 B 方向的目标形状并存但不升级。",
        "- unresolved: 43 条队列未逐条语义裁决；候选 #1 的“识别不敏感任务”搜索未开始；无新机器证明。",
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
    if state.get("revision") != 106 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_106_S106")

    # the scanner script changed (operator-position rule); re-pin its record
    scan_record = state["records"][SCAN_RECORD]
    hashes = scan_record.get("source_hashes") or {}
    new_script_hash = R.sha((root / SCAN_SCRIPT).read_bytes())
    if hashes.get(SCAN_SCRIPT) != new_script_hash:
        hashes[SCAN_SCRIPT] = new_script_hash
        scan_record["source_hashes"] = hashes
        scan_record["revalidation"] = (
            f"{SCAN_SCRIPT} re-hashed by {SESSION_ID}: the coarse-token rule was narrowed to operator position after "
            "triage batch 1 showed 20/20 false positives from the record name `Truncated-Type`; the receipt was "
            "regenerated (queue 146 → 43). Scope and evidence status unchanged."
        )

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "090"),
        ("PANORAMA", R.PANORAMA, "outcome", "090"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 106", "source_state_revision: 107"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-091",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/002 - 治理与用户方向.md",
        "下一步并行两条：**自主构造**（独立任务 → 规则改动 → 合法推演 → 对应回原活动，组合候选必过退化测试）与 "
        "**triage 批次 1（20 条）** 找“文档承诺 > 接口类型能力”的真实接口 |",
        "**线 A（triage）已关闭**：两批 40 条实读全为非候选（记录名/谓词名），判 "
        "`TRIAGE_LINE_CLOSED_PRECISION_LIMIT_REACHED`，43 条队列转为可复算附录；**线 B（自主构造）第一轮判负**："
        "候选 #1（“加入义务”读法）逐步落在 C-142–C-148，判 `DEGENERATION_TEST_FAILED_KNOWN_PACKAGE`。"
        "新筛选判据：新增义务须可定位 + 不可满足 + **现实侧程序在理论已识别的层面上仍然完成**；"
        "下一轮搜索问题 = 找“**对理论识别不敏感、却在 HoTT 表达下不可完成**的任务” |",
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
        "下一轮**两条并行**：① 自主构造（独立任务 → 哪条规则/规则组合改变前提 → 合法推演 → 对应回原活动），"
        "② 146 条 triage 队列取 20 条，定向找“**文档承诺 > 接口类型能力**”的真实接口。",
        "第一轮结果（S107）：**线 A（triage）关闭**——两批 40 条实读全为非候选（词表对命名约定无分辨力），"
        "43 条队列转附录；**线 B（自主构造）候选 #1 判负**——“加入义务”读法逐步落在 C-142–C-148，"
        "退化测试判 `DEGENERATION_TEST_FAILED_KNOWN_PACKAGE`。下一轮唯一搜索问题：找“**对理论识别不敏感、"
        "却在 HoTT 表达下不可完成**的任务”（现实侧程序须对理论识别不敏感，否则只是解释冲突）。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S107 C11 v2 §6 两条并行线第一轮（用户「开始」）：**线 A** 粗域接口 triage——v1 规则批次 1 判 20/20 假阳性"
        "（`Truncated-Type`/`trunc-map` 等记录名），收紧为算子位置后批次 2 仍 20/20 假阳性（`mere-emb`/`mere-eq` 等谓词名）→ "
        "判 `TRIAGE_LINE_CLOSED_PRECISION_LIMIT_REACHED`，队列 146→43 条转可复算附录，不再逐条读；外部接口判断回到 "
        "N1/N5/N10/T4 语义审计集合。**线 B** 自主构造候选 #1（“理论为经济性**加入**了相干义务”）：现实从无标签二元素集合取值，"
        "HoTT 的身份原则把两种标签识别为一，统一选点须尊重族自身识别 → 逐条落到 C-147（识别步）、C-143（相干义务）、"
        "C-144/C-145（不可满足）、C-148（非平凡）、C-146（正控制）→ 退化测试判 `DEGENERATION_TEST_FAILED_KNOWN_PACKAGE`。"
        "本轮唯一新产出：**候选筛选判据**（新增义务可定位 + 不可满足 + 现实侧程序在理论已识别层面上仍完成）。未新增数学 claim。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row55 = (
        "| 已闭合工作包 55 | C11 v2 哈希再绑定（S106，corrective） | `HASH_REPIN_ONLY` | 补回 v2 误删的 "
        "univalence/SIP 行（#2b）；校验脚本行标签对齐 v2 行号；重建 merge manifest；重新绑定 16 条 record"
        "（C11 / 校验脚本 / 14 条 manifest pin）；五个 verifier 全 PASS；数学与队列不变 |"
    )
    frontier = replace_once(
        frontier,
        row55,
        row55 + "\n| 已闭合工作包 56 | triage 批次 1–2 与自主构造第一轮（S107） | "
        "`TRIAGE_LINE_CLOSED_PRECISION_LIMIT_REACHED` / `DEGENERATION_TEST_FAILED_KNOWN_PACKAGE` | "
        "线 A：两批 40 条实读全非候选（记录名/谓词名），队列 146→43 转附录；线 B：候选 #1（“加入义务”）"
        "逐步落在 C-142–C-148，退化测试判负；新筛选判据 = 新增义务可定位 + 不可满足 + 现实侧程序对理论识别不敏感；见 "
        f"`{REPORT}` |",
    )
    frontier = replace_once(
        frontier,
        "| 第一工作包 | ① 自主构造（C11 v2 §6 路线）② triage 批次 1（146 取 20）＋ P3 定向 | active | "
        "自主构造：独立任务 → 理论如何表示 → 哪条规则/规则组合改变了什么 → 合法推演产生什么 → 对应回原活动；"
        "组合候选必过退化测试。triage：逐条读命中声明的上下文与文档段落，判义务由签名还是余域承担；"
        "命中“必须取回 + 同阶段/同层”的真实接口时按 P1 报告 §6 草案走 F-011 |",
        "| 第一工作包 | 自主构造第二轮：找“对理论识别不敏感、却在 HoTT 表达下不可完成”的任务 | active | "
        "筛选判据（S107）：新增义务可定位 + 不可满足 + 现实侧程序在理论已识别层面上仍完成；"
        "先在同一族（C-142–C-148）上检查识别不变的观察量，再扩到商/截断/ua 替换族；"
        "线 A（词汇 triage）已关闭，仅在语义审计需要时重开 |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n86. 词汇级扫描的精度上限来自**命名约定**，不是词表长度：两批各 20 条实读 40/40 非候选（`Truncated-Type`/"
        "`trunc-map` 记录名、`mere-emb`/`mere-eq` 谓词名）。有信息量的部分（带义务 token 的命中）在第一轮就收完了，"
        "继续调词表是打地鼠——正确做法是把队列转成可复算附录并关闭该线。另一条经验：判断“加入义务”型候选时，"
        "**必须先问现实侧的完成程序在理论做的识别下是否不变**；若现实侧只是依赖被识别掉的呈现（如“看一眼拿一个”），"
        "那得到的是解释冲突，不是悖论。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S107：两条并行线第一轮完成——线 A（粗域接口词汇 triage）判 `TRIAGE_LINE_CLOSED_PRECISION_LIMIT_REACHED` 并关闭"
        "（两批 40 条全非候选；43 条队列转附录）；线 B 自主构造候选 #1（“加入义务”读法）判 "
        "`DEGENERATION_TEST_FAILED_KNOWN_PACKAGE`（逐步落在 C-142–C-148）。新筛选判据：新增义务可定位 + 不可满足 + "
        "**现实侧程序在理论已识别层面上仍完成**。下一轮唯一问题：找“对理论识别不敏感、却在 HoTT 表达下不可完成”的任务。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户说「开始」，执行 C11 v2 §6 登记的两条并行线第一轮。
- 线 A（粗域接口 triage）：v1 规则批次 1 20/20 假阳性（记录名）；收紧为算子位置后批次 2 仍 20/20 假阳性（谓词名）
  → 判 `TRIAGE_LINE_CLOSED_PRECISION_LIMIT_REACHED`；队列 146→43 转为可复算附录；外部接口判断回到 N1/N5/N10/T4。
- 线 B（自主构造候选 #1，“加入义务”读法）：现实取点 vs HoTT 身份原则加入相干义务；逐步落到 C-147（识别步）、
  C-143（相干义务）、C-144/C-145（不可满足）、C-148（非平凡）、C-146（正控制）→ 退化测试判
  `DEGENERATION_TEST_FAILED_KNOWN_PACKAGE`。
- 本轮唯一新产出：**候选筛选判据**（新增义务可定位 + 不可满足 + 现实侧程序在理论已识别层面上仍完成）。
- 交付：`{REPORT}`；扫描收据 `{SCAN_RECEIPT}`（规则收紧后重生成）。
- 状态边界：不新增数学 claim、不改判词、未重放 run；线 B 数学全部引用 C-142–C-148；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "round": "C11 v2 §6 parallel lines, round 1",
            "line_a": {
                "verdict": "TRIAGE_LINE_CLOSED_PRECISION_LIMIT_REACHED",
                "batches_read": 2,
                "items_read": 40,
                "candidates": 0,
                "queue_after_rule_v2": 43,
            },
            "line_b": {
                "candidate": "added-obligation reading of the unlabeled two-element choice family",
                "verdict": "DEGENERATION_TEST_FAILED_KNOWN_PACKAGE",
                "claims_used": ["C-143", "C-144", "C-145", "C-146", "C-147", "C-148"],
            },
            "new_criterion": (
                "A new autonomous candidate must (i) locate the added obligation at a rule/identification step, "
                "(ii) show it is unsatisfiable, and (iii) have a reality-side procedure that still completes after the "
                "theory's identification — i.e. insensitive to what the theory identified."
            ),
            "new_math_claims": [],
            "new_proof_package": None,
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 107
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_TRIAGE_AND_OBLIGATION_ROUND1",
            "status": STATUS,
            "next_minimal_verification": (
                "Autonomous round 2: find a task that is insensitive to the theory's own identification yet cannot be "
                "completed in HoTT. Check identification-invariant observables on the C-142-C-148 family first, then on "
                "quotient/truncation/ua-substitution families. Apply the S107 filter: located obligation + unsatisfiable "
                "+ reality-side procedure insensitive to the identification. Lexical triage stays closed."
            ),
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-091", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-091", "semantic_status": STATUS}
    )
    state["records"][ROUND_ID] = {
        "kind": "result",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [SESSION_ID, SCAN_RECORD, "A-P2-P3-CHECKLIST-001"],
        "full_sources": [REPORT, SCAN_RECEIPT, C11, "HoTT/CLAIM_EVIDENCE_MATRIX.md"],
        "source_hashes": {REPORT: R.sha((root / REPORT).read_bytes())},
        "scope": (
            "Round 1 of the two parallel lines: line A (coarse-domain lexical triage) closed with "
            "TRIAGE_LINE_CLOSED_PRECISION_LIMIT_REACHED after 40/40 false positives in two read batches; line B "
            "(autonomous candidate #1, the added-obligation reading of the unlabeled two-element choice family) mapped "
            "step by step onto C-142-C-148 and failed the degeneration test. New output: a candidate filter criterion "
            "(located obligation + unsatisfiable + reality-side procedure insensitive to the theory's identification). "
            "No new mathematical claim."
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
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, REPORT, SCAN_RECEIPT],
        "source_hashes": {},
        "scope": (
            "Registration of triage round 1 and autonomous candidate #1: verdicts, re-pinned scanner script, "
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
            "User said '开始' for the two registered parallel lines from C11 v2 §6. Round 1 executed both: the lexical "
            "coarse-consumer triage was closed as a bounded negative after 40/40 false positives, and the first "
            "autonomous candidate (added-obligation reading) failed the degeneration test as a known package. Both "
            "were registered with the derived filter criterion. No new mathematical claim, no push."
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
                "revision": 107,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
