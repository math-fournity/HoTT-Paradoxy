#!/usr/bin/env python3
"""Prepare revision 102: register the C11 theory-economy ledger as a method work package.

The user asked how to systematically survey HoTT so that its reality-relative
paradox can be located, and approved turning that method into
`理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md` plus registering it as
the next work package.  This checkpoint writes the MUTABLE state (projections,
MEMORY, FRONTIER, LESSONS, RESUME, STATE) and the canonical session bundle;
the C11 document, the 理解章节 index and the rebuilt merge manifest are ordinary
repo files written before this transaction and committed with it.

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

SESSION_ID = "S-RES-20260913-102-THEORY-ECONOMY-LEDGER"
PREV = "S-GOV-20260913-101-ASTRA-TRAJECTORY-STATE-REGISTRATION"
RESULT_ID = "A-THEORY-ECONOMY-LEDGER-001"
DIRECTION_ID = "DIR-TOP-THEORY-ECONOMY-LEDGER"
OUTCOME_ID = "OUT-TOP-THEORY-ECONOMY-LEDGER"
C11 = "理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
MANIFEST = "audit/understanding-chapter-merge-manifest.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"

SPEC = importlib.util.spec_from_file_location("runtime_s102", RUNTIME_PATH)
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


DIRECTION_ROW = (
    f"| `{DIRECTION_ID}` | HoTT 理论经济账本与悖论位置判别：先列规则级经济决策"
    "（收入 / 被悬置的现实因子 / 支付装置 / 复活条件），再做“同阶段 / 同层”可用性判别并预测候选 | "
    "用户 2026-09-13 指出 Astra-1/Astra-2 未做“统观”；C11 | `ACTIVE_USER_DIRECTION` | "
    "`THEORY_ECONOMY`, `PARADOX_DISCOVERY`, `TIME_AND_TEMPORALITY`, `SELF_REFERENCE` | "
    f"`{OUTCOME_ID}`（9 行账本 + 2×2 判别格 + P1–P3 预测 + 18 包回溯检验） | "
    "按判别格选 1–2 个“同阶段 / 同层不可用”的候选并执行 F-011 机器化；P1 时序线优先 | "
    f"`{C11}` |\n"
)

OUTCOME_ROW = (
    f"| `{OUTCOME_ID}` | C11 HoTT 理论经济账本与悖论位置判别：把“统观”做成可证伪的索引——"
    "9 行规则级经济账本（截断 / 商 / ua / funext / 判断相等 / 总性 / 命题无关 / 宇宙 / 无全局选择）"
    "+ “同阶段 / 同层”2×2 判别格 + P1–P3 预测，并用现有 18 个机器包做回溯检验 | "
    f"`{DIRECTION_ID}` | 用户 2026-09-13 要求系统化统观；当前 AI 综合 | "
    "`DOCUMENTED / PAPER_ONLY_METHOD_AND_LEDGER` | 账本能逐条解释现有 18 个机器包为何停在"
    " `DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY`：它们的支付装置都在“同阶段同层可用”格子内；"
    "唯一“支付装置不存在”的已证结果（C-142–C-148 无统一选点）缺少一个真实任务 | "
    "不新增数学 claim；账本本身不是定理；不证明悖论存在或不存在；“支付装置不可用”只说明缺真实任务 | "
    f"`{C11}`；`audit/astra-1-astra-2会话轨迹审计-20260913.md` |\n"
)

AUDIT_FOCUS = {
    "KC-000001": (
        "ALIGNED",
        "账本把“找什么 / 怎么找 / 凭什么”落成可执行顺序：先列理论端经济决策，再由判别格生成任务。",
    ),
    "KC-000005": (
        "ALIGNED",
        "账本坚持“先定位现象、归因留后”：P1–P3 只给出候选形状与缺环，不在缺环未补时宣布归因。",
    ),
    "KC-000007": (
        "DEEPENED",
        "针对“模式匹配被用在旧题型上”的失败形状，账本把搜索从题型驱动改为经济决策驱动。",
    ),
    "KC-000010": (
        "ALIGNED",
        "判别格的目标是现实相对非现实性（同任务完成性反差），不是内部矛盾。",
    ),
    "KC-000011": (
        "ALIGNED",
        "账本 #5/#6 行正对应“理论的工作过程是否承担时序、可用与部分性”。",
    ),
    "KC-000012": (
        "ALIGNED",
        "ASK 的“凭什么可以问/可以完成”被实现为支付装置与两条可用性判据。",
    ),
    "KC-000013": (
        "ALIGNED",
        "账本把“理论为了工具性悬置了什么”作为第一列收入的经济学表达。",
    ),
    "KC-000015": (
        "DEEPENED",
        "“否定现实前提”被具体化为：某现实因子在理论内不再起作用；并把“机制专属性”从入口门槛降为事后问题。",
    ),
    "KC-000017": (
        "ALIGNED",
        "账本是为抵抗训练先验而设计的检索顺序；它不要求先接受任何既有分类。",
    ),
    "KC-000018": (
        "ALIGNED",
        "理论经济（工具性收益与其代价）成为账本的收入/支付两列。",
    ),
    "KC-000021": (
        "NOT_TOUCHED",
        "本单元不产生机器证明；候选机器化仍须走 `MATH_PROOF_BEFORE_DELIVERY_V1`。",
    ),
    "KC-000022": (
        "ALIGNED",
        "P1 对应第一类（现实可完成、理论引入额外完成困难）；P2 对应第二类的自指版本。",
    ),
    "KC-000023": (
        "DEEPENED",
        "账本把“应当能直接定位 HoTT 对时间/时序的处理”变成可检查的 #5/#6 行与“同阶段”判据。",
    ),
    "KC-000025": (
        "ALIGNED",
        "P2 明确回答“自指型为什么难找”：需要真实内部担保消费者，而不是重复对角口号。",
    ),
    "KC-000026": (
        "ALIGNED",
        "账本 #8 行把“自指不可越过”写成层级支付问题，并与 ERCF-3 的 gated 状态一致。",
    ),
    "KC-000027": (
        "ALIGNED",
        "“共享机制可用、不冒充 HoTT 独有”被写进判词规则：账本不要求机制专属性即可立项。",
    ),
    "KC-000028": (
        "ALIGNED",
        "自馈回环被定位在 #8 行“同层不可用”格子，并给出可证伪的支付装置判据。",
    ),
    "KC-000030": (
        "ALIGNED",
        "C11 是对“HoTT 追求怎样的理论经济学”的正面回答尝试（收入/支付两列）。",
    ),
    "KC-000036": (
        "ALIGNED",
        "Gödel 内部化在账本中属 #8 行；未取得真实消费者前只保留通用边界。",
    ),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元把“理论经济账本与悖论位置判别”立为方法工作包，不产生数学结论。",
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
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{C11}`；{kid} | 数学开放项不变。 |"
        )
    aligned = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "ALIGNED")
    deepened = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "DEEPENED")
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文；方法账本不进入 core。",
        f"- direction_change: YES — 新增 `{DIRECTION_ID}` 方向行，并把第一工作包改为账本驱动的候选选择（原位修改，不加覆盖块）。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/004 owner shard）。",
        "- essay_change: NO — 常驻第四件（AI 阐释层）未改动；C11 是它的操作化索引，不替代它。",
        "- update_decision: 账本先立、候选后选；判别判据从“理论忘了什么”改为“支付装置能否在同阶段同层提供该因子”；回溯检验失败则修账本而非改判词。",
        "- cross_conflicts: C10 的“机制不可替代”门槛与 KC-000015/KC-000027 的共享机制许可冲突 → 账本把专属性降为事后问题，保留冲突文本不改写历史文件。",
        f"- unresolved: P1/P2/P3 均未取得真实任务或自然消费者；账本自身为 `PAPER_ONLY`；未新增机器证明；fresh model behavior NOT_RUN。",
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
    if state.get("revision") != 101 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_101_S101")
    manifest_hash = R.sha((root / MANIFEST).read_bytes())

    # --- projections -------------------------------------------------------
    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "085"),
        ("PANORAMA", R.PANORAMA, "outcome", "085"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 101", "source_state_revision: 102"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-086",
        )
        projections[key] = doc

    projection_edit.append_to_shard(
        projections["DIRECTION"],
        "方向追踪/002 - 治理与用户方向.md",
        DIRECTION_ROW,
    )
    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/005 - 交叉审视、优先级与更新规则.md",
        "4. **当前第一工作包**：从 N43 三选一收敛为真实下游 consumer 的 E6 定向审计。",
        "4. **当前第一工作包（S102 起由账本驱动）**：先按 `"
        + C11
        + "` 的 2×2 判别格选择候选——P1 时序线（同阶段不可用）优先，其次 P2 自指线（同层不可用）与 P3 交叉线；"
        "选定后仍固定具体应用/派生开发、版本、调用链与交付承诺，只在它把截断存在、商类、等价存在或 noncomputable "
        "分类提升成可执行数据时考虑 `NATURAL_USAGE_MISMATCH`。E6 定向审计仍是具体执行目标。",
    )
    projection_edit.append_to_shard(
        projections["PANORAMA"],
        "全景视野/004 - 距离综合与消费者审计.md",
        OUTCOME_ROW,
    )

    # --- MEMORY -----------------------------------------------------------
    memory = projection_edit.load(root, "MEMORY.md")
    projection_edit.replace_in_shard(
        memory,
        "MEMORY/001 - 当前执行队列.md",
        "2. 数学研究第一线：寻找**真实下游应用或派生开发中的 E6 consumer**。",
        "2. 数学研究第一线（S102 起由账本驱动）：先按 `理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md` "
        "的 2×2 判别格选候选（P1 时序线优先 / P2 自指线 / P3 交叉线），再落到"
        "**真实下游应用或派生开发中的 E6 consumer**。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S102 理论经济账本（C11）立为方法工作包：用户指出 Astra-1/Astra-2 未做“统观”，并要求把账本系统化。"
        "C11 给出 9 行规则级账本（截断 / 商 / ua / funext / 判断相等 / 总性 / 命题无关 / 宇宙 / 无全局选择，"
        "每行固定“收入 / 被悬置因子 / 支付装置 / 复活条件 / 现有判词”）、“同阶段 / 同层”2×2 判别格、"
        "P1–P3 三条预测路径，以及现有 18 个机器包的逐条回溯检验（全部落在“支付装置可用”格，"
        "与判词停在第二级一致）。新方向 `DIR-TOP-THEORY-ECONOMY-LEDGER` 与结果 `OUT-TOP-THEORY-ECONOMY-LEDGER` 已登记；"
        "merge manifest 重建为 36/24（top-level unique 12）。**不新增数学 claim**；P1/P2/P3 均缺真实任务或自然消费者。\n",
    )

    # --- essay (unchanged, must ship in the payload) -----------------------
    essay = projection_edit.load(root, R.ESSAY)

    # --- FRONTIER / LESSONS / RESUME --------------------------------------
    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = replace_once(
        frontier,
        "| 第一工作包 | 固定下游应用/派生开发的真实 E6 consumer | active | 固定版本、调用链、输入和交付承诺；只有真实资格越级才升格 |",
        "| 第一工作包 | C11 理论经济账本驱动的候选选择（P1 时序线优先 / P2 自指线 / P3 交叉线） | active | "
        "先用“同阶段 / 同层”判别格挑 1–2 个候选，再固定版本、调用链、输入与交付承诺并走 F-011；"
        "固定下游应用/派生开发的真实 E6 consumer 仍是具体执行目标 |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n81. 找“理论的非现实性”时，顺序应当是**先立账、再找题**：先列出理论为经济性悬置了哪些现实因子"
        "（收入 / 悬置因子 / 支付装置 / 复活条件），再由账本生成任务。否则会退化成在熟悉题型附近采样——"
        "这是 Astra-1/Astra-2 的实测失败形状。判别候选的关键不是“理论忘了什么”，而是“支付装置能否在任务所需的"
        "**同一阶段**与**同一层**把该因子带回来”：能带回来的一律停在表示边界（现有 18 个机器包全部如此），"
        "带不回来的才是悖论位置；而“支付装置不存在”还需要一个真实任务才构成候选。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S102：`理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md` 已立为方法工作包并要求回溯检验通过；"
        "研究第一线由此改为**账本驱动的候选选择**（P1 时序线优先、P2 自指线、P3 交叉线），"
        "E6 consumer 与 T3 共享判定联合递归分别保留为具体执行目标与第二线。未新增数学结论。\n\n",
    )

    # --- session bundle ----------------------------------------------------
    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户要求把“如何系统化地统观 HoTT、预测其现实相对悖论会出现的位置”落成文档，并在其确认后登记为下一工作包。
- 交付：`{C11}`——9 行规则级经济账本 + “同阶段 / 同层”2×2 判别格 + P1–P3 预测 + 现有 18 个机器包的回溯检验；
  同时原位更新 `理解章节/README.md` 的 C 系列表并重建 merge manifest（36/24，top-level unique 12）。
- 本 checkpoint 写 machine-managed 状态：`STATE.revision=102`、方向行 `{DIRECTION_ID}`、结果行 `{OUTCOME_ID}`、
  投影标记（`source_state_revision: 102`、`projection_generation: -086`）、MEMORY/FRONTIER/LESSONS/RESUME 条目，
  以及 14 条 pin 了 merge manifest 的 record 的重新哈希与 revalidation 说明。
- 状态边界：C11 是 `PAPER_ONLY` 方法账本，**不新增数学 claim**、不改判词、不升级任何候选；
  P1/P2/P3 均缺真实任务或自然消费者；不 push；fresh model behavior NOT_RUN。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "deliverable": C11,
            "ledger_rows": 9,
            "retrodiction_packages": 18,
            "predictions": ["P1_TIME_STAGE_UNAVAILABLE", "P2_SELF_LAYER_UNAVAILABLE", "P3_INTERSECTION"],
            "manifest_counts": {"union_files": 36, "top_level_unique": 12},
            "mathematics": "NOT_CERTIFIED",
            "new_math_claims": [],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    # --- STATE -------------------------------------------------------------
    repinned = []
    for key, record in state["records"].items():
        hashes = record.get("source_hashes") or {}
        if MANIFEST not in hashes:
            continue
        if hashes[MANIFEST] == manifest_hash:
            continue
        hashes[MANIFEST] = manifest_hash
        record["source_hashes"] = hashes
        record["revalidation"] = (
            f"{MANIFEST} re-hashed by {SESSION_ID} after C11 was added to 理解章节/ and the merge manifest was rebuilt "
            "(union 36 / nested 24; top-level unique 12). The record's claim, scope and evidence status are unchanged."
        )
        repinned.append(key)
    if len(repinned) != 14:
        raise SystemExit(f"EXPECTED_14_MANIFEST_PINS:{sorted(repinned)}")

    state["revision"] = 102
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_THEORY_ECONOMY_LEDGER",
            "status": STATUS,
            "next_minimal_verification": (
                "C11 ledger-driven candidate selection: pick 1–2 candidates whose payment device is unavailable in the "
                "same stage or the same layer (P1 time line first), then fix version/call chain/delivery promise and run "
                "MATH_PROOF_BEFORE_DELIVERY_V1. E6 consumer remains the concrete first-line target; T3 joint recursion "
                "remains the second line."
            ),
        }
    )
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-086", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-086", "semantic_status": STATUS}
    )
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": C11,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-C5-PARADOX-DISTANCE-001", "A-A-DIRECTION-CANDIDATES-001"],
        "full_sources": [C11, "HoTT/CLAIM_EVIDENCE_MATRIX.md", "audit/astra-1-astra-2会话轨迹审计-20260913.md"],
        "source_hashes": {C11: R.sha((root / C11).read_bytes())},
        "scope": (
            "C11 theory-economy ledger: nine rule-level economy rows (truncation, quotients/HIT, ua, funext, judgmental "
            "equality, totality, proof irrelevance, universe/self-description, no global choice) with income / suspended "
            "reality factor / payment device / revival condition / existing verdict; a same-stage vs same-layer 2x2 "
            "discrimination grid; predictions P1 (time), P2 (self-reference), P3 (intersection); and a retrodiction table "
            "mapping all 18 existing machine packages into the grid (none in the 'payment device unavailable' cell). "
            "PAPER_ONLY method ledger: no new mathematical claim, no verdict change."
        ),
    }
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, C11],
        "source_hashes": {},
        "scope": (
            "Registration of the C11 theory-economy ledger as the method work package: STATE revision 102, new direction "
            "and outcome rows, projection markers, MEMORY/FRONTIER/LESSONS/RESUME entries, merge-manifest rebuild with "
            "14 pinned records revalidated. No mathematical change."
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
            "User asked how to survey HoTT globally so that its reality-relative paradox can be located, then said "
            "'可以' to the concrete proposal: write 理解章节/C11 (rule-level theory-economy ledger + same-stage/same-layer "
            "discrimination grid + retrodiction criteria) and register it as the next work package in 方向追踪.md/STATE, "
            "ending with a canonical checkpoint. No mathematical claim, no research-queue replacement beyond the "
            "ledger-driven selection method, no push."
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
                "revision": 102,
                "session_id": SESSION_ID,
                "files": len(texts),
                "repinned_manifest_records": len(repinned),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
