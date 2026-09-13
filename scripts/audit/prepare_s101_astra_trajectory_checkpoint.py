#!/usr/bin/env python3
"""Prepare revision 101: register the Astra-1/Astra-2 trajectory audit in state.

The user asked to audit another AI's Codex sessions (`Astra-1`, `Astra-2`) with the
canonical trajectory tool and then to close the remaining registration gap
("补上").  The read-only audit bundle already exists in the repo
(`audit/astra-1-astra-2会话轨迹审计-20260913.md` and
`.codex/research/hott/sessions/S-AUD-20260913-101-ASTRA-TRAJECTORY/`); this
checkpoint adds the machine-managed registration: STATE revision 101, the
session-alias record, the projection markers/rows, MEMORY/LESSONS/RESUME entries
and the canonical session bundle for the registration itself.

Read-only with respect to the repository: it only writes the payload file.
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

SESSION_ID = "S-GOV-20260913-101-ASTRA-TRAJECTORY-STATE-REGISTRATION"
PREV = "S-GOV-20260913-100-FOUR-SET-UPGRADE"
AUDIT_SESSION = "S-AUD-20260913-101-ASTRA-TRAJECTORY"
RESULT_ID = "A-ASTRA-TRAJECTORY-AUDIT-001"
AUDIT_REPORT = "audit/astra-1-astra-2会话轨迹审计-20260913.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
AUDIT_SESSION_REL = f".codex/research/hott/sessions/{AUDIT_SESSION}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"

SPEC = importlib.util.spec_from_file_location("runtime_s101", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:70]}:{text.count(old)}")
    return text.replace(old, new, 1)


AUDIT_FOCUS = {
    "KC-000005": (
        "ALIGNED",
        "审计发现「先找到悖论、最终归因留后」在实际执行中被反转为「必须有 E6／真实错用链才允许升格」；"
        "该反转是把后置目标提前当成入口门槛，直接解释了为什么找不到目标。",
    ),
    "KC-000006": (
        "ALIGNED",
        "Astra-1 第 4 轮按用户澄清区分「时序（先后/依赖/可用性）」与「时间、时空与运动的结构前提」，"
        "修订已随长文进入 shard 002；审计复核了该修订的落点。",
    ),
    "KC-000007": (
        "TENSION",
        "Astra-2 自述：宽的问题意识被换成「熟悉、清楚、能够形式化的小问题」；"
        "即模式匹配能力被用在旧题型上，而不是在核心认知指引下重构问题。",
    ),
    "KC-000010": (
        "ALIGNED",
        "审计以「现实相对非现实性、而非内部矛盾」为标准判定本轮目标未达成，"
        "并保留 E6 仍 OPEN，不把负结果写成「HoTT 没有问题」。",
    ),
    "KC-000015": (
        "DEEPENED",
        "该 KC 只要求 HoTT 中的具体表现，而 `理解章节/C10-N11-A方向候选生成-20260912.md:20` 增设了"
        "「关键规则不可被普通类型论替代」的机制专属门槛；研究 Skill 第 64 行明确允许共享机制。"
        "审计把这一收窄固定为可引用的方法事实（是否改规则留待用户裁定）。",
    ),
    "KC-000017": (
        "TENSION",
        "长文正是为对抗训练先验而写的上下文工程；同一对话内 Astra-2 仍自述转向训练中熟悉的题型，"
        "说明「保存表达—传达理解—改变选题」三层里第三层尚未被验证。",
    ),
    "KC-000021": (
        "ALIGNED",
        "Astra-1 第 7 轮确实真跑了原生 Cubical Agda（exit 0、负向 exit 42、异目录重放），"
        "本 repo 又在 S098 独立重跑；但被证明的是自建有限模型，不是 HoTT 自身结论。",
    ),
    "KC-000023": (
        "TENSION",
        "该 KC 要求「应能直接定位 HoTT 对时间/时序的处理」；审计确认这一步始终没有做到，"
        "Astra-2 也已把它写成下一次编码前必须先写清的判据。",
    ),
    "KC-000027": (
        "ALIGNED",
        "「HoTT 对齐程序后继承程序界限」支持把共享机制作为 HoTT 实例来研究，"
        "与 C10 的机制专属门槛形成张力；审计保留了这一冲突而不是替任何一方裁决。",
    ),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是另一个 AI 的会话轨迹审计与状态注册，不改任何 KC 原文，不产生数学结论。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = AUDIT_FOCUS.get(
            kid,
            (
                "NOT_TOUCHED",
                f"本轮没有研究或重新裁决「{label}」的数学/哲学内容。",
            ),
        )
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | "
            f"`{AUDIT_REPORT}`；`{AUDIT_SESSION_REL}/SESSION.md`；{kid} | 数学开放项不变。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文；会话审计不进入 core。",
        "- direction_change: YES_IN_PLACE — `DIR-E-LOCAL-HISTORY-COVERAGE` 行原位补上该结果与新可发现性，不新增覆盖块。",
        "- panorama_change: YES — 新增 `OUT-TOP-ASTRA-TRAJECTORY-AUDIT` 结果行（写入 全景视野/002 owner shard）。",
        "- essay_change: NO — 常驻第四件（AI 阐释层）内容未改动；本单元只在全景/方向/记忆层登记审计结果。",
        "- update_decision: 会话别名闭合为 thread id；审计证据包与状态注册分开登记；不把 AI 自我诊断升格为数学结论；研究队列不变。",
        "- cross_conflicts: canonical 编号-Read 合同报 L2 FAIL，而运行期源快照 `35cace7` 的逐字节/逐行对账为完整——冲突按「合同不匹配 vs 内容缺失」分层保留，不互相覆盖。",
        "- unresolved: `Astra-2` 的独立 rollout 未做 L3/L1 复核；外部验证事件包仍只有项目内重放；fresh model behavior NOT_RUN；不 push。",
        "",
        "## 汇总",
        "",
        "`ALIGNED=5`（KC-000005/000006/000010/000021/000027）；`DEEPENED=1`（KC-000015）；"
        "`TENSION=3`（KC-000007/000017/000023）；`NOT_TOUCHED=27`；无 `DEVIATED`。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 100 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_100_S100")

    # --- projections -------------------------------------------------------
    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "084"),
        ("PANORAMA", R.PANORAMA, "outcome", "084"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 100", "source_state_revision: 101"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-085",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/004 - 证据与覆盖方向及 STATE 覆盖表.md",
        "| `OUT-TOP-LEDGERS` | 完成 response→tool→artifact/code→Git 的语义映射，保留 dirty/缺源边界 |",
        "| `OUT-TOP-LEDGERS`、`OUT-TOP-ASTRA-TRAJECTORY-AUDIT`（另一个 AI 的 `Astra-1`/`Astra-2` 会话按名称可解析） "
        "| 完成 response→tool→artifact/code→Git 的语义映射，保留 dirty/缺源边界 |",
    )
    projection_edit.append_to_shard(
        projections["PANORAMA"],
        "全景视野/002 - 治理、门禁与骨架结果.md",
        "| `OUT-TOP-ASTRA-TRAJECTORY-AUDIT` | 另一个 AI 的 Codex Session Name 复核：`Astra-1` = "
        "`01a099e9-66ee-7270-8bf9-04f7f1c81e62`（8 轮 / 104 tool call），`Astra-2` = "
        "`01a09a72-aeb6-7a50-81d6-d24f43c5e912`（1 轮，Astra-1 子线程）；三件套读取按运行期快照 `35cace7` "
        "逐字节/逐行复核为完整；判词 L5 目标未达成 | `DIR-E-LOCAL-HISTORY-COVERAGE` | 当前治理"
        "（用户要求理解另一 AI 的工作及失败原因） | `DOCUMENTED / L2_PASS_BY_RUN_SOURCE_COMPARE; L5_TARGET_NOT_MET` "
        "| 会话身份、逐轮工作、四类失败原因都有直接 locator；验证事件包（`C-149`–`C-156`）仍是该项目内唯一机器重放结果 "
        "| 不证明模型理解；不把自我诊断升格为「HoTT 必有 BUG」或「已充分搜索」；Astra-2 的回答不是数学主张 "
        f"| `{AUDIT_REPORT}`；`{AUDIT_SESSION_REL}/`；`~/.codex/sessions/2026/09/13/rollout-2026-09-13T04-36-45-01a099e9-*.jsonl` "
        "| \n",
    )

    # --- MEMORY -----------------------------------------------------------
    memory = projection_edit.load(root, "MEMORY.md")
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S101 Astra-1/Astra-2 轨迹审计与状态注册（用户先说「补上」）：用 canonical `session_trajectory.py` "
        "闭合会话别名——`Astra-1`=`01a099e9-66ee-7270-8bf9-04f7f1c81e62`（8 轮 / 104 tool call / `gpt-6-astra` ultra），"
        "`Astra-2`=`01a09a72-aeb6-7a50-81d6-d24f43c5e912`（1 轮，**Astra-1 的子线程**）。L2 以运行期源快照 `35cace7` "
        "逐字节/逐行复核三件套读取为完整；canonical 编号-Read 合同报 FAIL 属合同不匹配。未达目标的方法原因："
        "目标被收窄成可形式化小题型、C10:20 机制专属门槛与 C5:56 的 E6 唯一升格口比用户原意更窄、"
        "T3 十三个脉冲颗粒度过小、并行写者迫使工作移出 repo。会话别名与结果已登记为 STATE record "
        f"`{RESULT_ID}`（含两个 thread id）；研究队列（E6 consumer 第一线 / T3 第二线）与全部数学状态不变。\n",
    )

    # --- essay (unchanged, must ship in the payload) -----------------------
    essay = projection_edit.load(root, R.ESSAY)

    # --- FRONTIER / LESSONS / RESUME --------------------------------------
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row50 = (
        "| 已闭合工作包 50 | agda-unimath E6 源码/闭包扫描（S088 后复审） | `SOURCE_INSPECTED_BOUNDED_NEGATIVE` | "
        "`foundation.global-choice` 不在 C-05 run；20 postulate / 9 primitive / 22 union；run 闭包 7 声明文件；E6 仍开放 |"
    )
    frontier = replace_once(
        frontier,
        row50,
        row50 + "\n| 已闭合工作包 51 | Astra-1/Astra-2 会话轨迹审计与状态注册（S101） | "
        "`DOCUMENTED / L2_PASS_BY_RUN_SOURCE_COMPARE; L5_TARGET_NOT_MET` | 会话别名闭合为 thread id；"
        "Astra-1 8 轮 / 104 tool call，Astra-2 为其子线程；三件套读取按 `35cace7` 逐字节/逐行复核完整；"
        f"四类未达成原因与全部 locator 见 `{AUDIT_REPORT}`；研究队列不变 |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n80. 用户以 Session Name 指代另一个 AI 的会话时，repo 必须能解析该别名：把"
        "「名称 ↔ thread_id ↔ rollout 原件 ↔ 已吸收产物」写成一行可查记录，否则未来 AI 只能靠猜。"
        "另外，审计「有没有读到 EOF」不能只看 canonical 编号-Read 合同是否匹配——先看被审 Agent 实际用的是哪种读取工具，"
        "再用保存了该现场的 commit 做逐字节/逐行对账；否则会把合同不匹配误报成内容缺失（本轮实测：`coverage` 报 L2 FAIL，"
        "而运行期源快照对账为完整）。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S101：按用户要求审计了另一个 AI 的 `Astra-1`/`Astra-2` 会话并完成状态注册（别名→thread id、"
        "L2 逐字节复核、四类未达成原因、`OUT-TOP-ASTRA-TRAJECTORY-AUDIT`）。判词 L5 目标未达成，"
        "但研究队列**不变**：第一线仍是真实下游/派生开发的 E6 consumer，第二线仍是 T3 共享判定联合递归。\n\n",
    )

    # --- session bundle ----------------------------------------------------
    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户先要求用全局脚本与 Skill 审计另一个 AI 在当前 repo 的工作（Codex Session Name `Astra-1`/`Astra-2`），
  随后说「补上」，即补齐审计留下的状态注册缺口。
- 审计本身是只读的，证据包在 `{AUDIT_REPORT}` 与 `{AUDIT_SESSION_REL}/`（SESSION/RUNS/36-KC 回评，`DOCUMENTED`，无 canonical 收据）。
- 本 checkpoint 做的是 machine-managed 注册：STATE revision 101、会话别名 record、`{RESULT_ID}` 结果 record、
  方向/全景投影标记与行、MEMORY/FRONTIER/LESSONS/RESUME 条目，以及本 session 三个文件。
- 审计结论（不得升格）：`Astra-1` = `01a099e9-66ee-7270-8bf9-04f7f1c81e62`（8 轮 / 104 tool call），
  `Astra-2` = `01a09a72-aeb6-7a50-81d6-d24f43c5e912`（1 轮，Astra-1 子线程）；三件套读取在运行期快照 `35cace7` 上
  逐字节/逐行完整；本轮**没有**产出 HoTT 现实相对悖论或 E6 consumer。
- 不改 KC 原文，不改数学判词，不改研究队列；不 push；fresh model behavior NOT_RUN。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "audited_sessions": {
                "Astra-1": "01a099e9-66ee-7270-8bf9-04f7f1c81e62",
                "Astra-2": "01a09a72-aeb6-7a50-81d6-d24f43c5e912",
            },
            "audit_evidence": [AUDIT_REPORT, f"{AUDIT_SESSION_REL}/SESSION.md"],
            "coverage_verdicts": {
                "L1_context_injection": "NOT_TESTED",
                "L2_selected_read_coverage": "PASS_BY_RUN_SOURCE_COMPARE",
                "L3_model_recall": "NOT_TESTED",
                "L4_cognition_execution": "PARTIAL_MIXED",
                "L5_behavior_verdict": "TARGET_NOT_MET",
            },
            "mathematics": "NOT_CERTIFIED",
            "research_queue_changed": False,
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    # --- STATE -------------------------------------------------------------
    state["revision"] = 101
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_ASTRA_TRAJECTORY_STATE_REGISTRATION",
            "status": STATUS,
        }
    )
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-085", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-085", "semantic_status": STATUS}
    )
    state["records"][AUDIT_SESSION] = {
        "kind": "session",
        "path": f"{AUDIT_SESSION_REL}/SESSION.md",
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [SESSION_ID, RESULT_ID],
        "full_sources": [
            f"{AUDIT_SESSION_REL}/SESSION.md",
            f"{AUDIT_SESSION_REL}/CORE_COGNITION_AUDIT.md",
            f"{AUDIT_SESSION_REL}/RUNS.json",
            AUDIT_REPORT,
        ],
        "source_hashes": {},
        "scope": (
            "Read-only trajectory audit of the other AI's Codex sessions Astra-1/Astra-2 in this repo; "
            "authored before the canonical checkpoint below and deliberately without its own receipt."
        ),
    }
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": AUDIT_REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [SESSION_ID, AUDIT_SESSION],
        "full_sources": [AUDIT_REPORT, f"{AUDIT_SESSION_REL}/SESSION.md", f"{AUDIT_SESSION_REL}/CORE_COGNITION_AUDIT.md"],
        "source_hashes": {},
        "scope": (
            "Session-alias closure and workline audit for the other AI: Astra-1 = "
            "01a099e9-66ee-7270-8bf9-04f7f1c81e62 (8 turns, 104 tool calls, gpt-6-astra/ultra); Astra-2 = "
            "01a09a72-aeb6-7a50-81d6-d24f43c5e912 (1 turn, child of Astra-1). L2 read coverage passes by "
            "run-source comparison against commit 35cace7; L1/L3 NOT_TESTED; L5 target NOT_MET (no HoTT "
            "reality-relative paradox, no E6 consumer). Records why the goal was not reached: formalisable "
            "small-problem narrowing, C10:20 exclusivity threshold and C5:56 E6-only upgrade gate narrower "
            "than the user's own words, T3 micro-pulses, and concurrent-writer avoidance. Research queue unchanged."
        ),
    }
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, RESULT_ID, AUDIT_SESSION],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, AUDIT_REPORT],
        "source_hashes": {},
        "scope": (
            "Machine-managed registration of the Astra-1/Astra-2 trajectory audit: STATE revision 101, "
            "session-alias and result records, projection markers/rows, MEMORY/LESSONS/RESUME entries. "
            "No mathematical change; research queue unchanged."
        ),
    }

    # --- payload -----------------------------------------------------------
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
            "User asked (1) to audit the other AI's Codex sessions Astra-1/Astra-2 in this repo with the global "
            "scripts and Skills, and (2) after the audit reported that Astra-2 had no STATE record and that the "
            "alias was unresolvable in-repo, said '补上' — i.e. close that registration gap via the canonical "
            "checkpoint so future AIs can resolve the names and the verdict. No mathematical change, no research "
            "queue change, no push."
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
                "revision": 101,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
