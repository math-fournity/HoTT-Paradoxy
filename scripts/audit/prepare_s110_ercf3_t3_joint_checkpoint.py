#!/usr/bin/env python3
"""Prepare revision 110: register MP-ERCF3-T3-JOINT-001 (T3 shared-decision joint recursion)."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-110-ERCF3-T3-JOINT"
PREV = "S-RES-20260913-109-AUTONOMOUS-ROUND3"
PROOF_ID = "MP-ERCF3-T3-JOINT-001"
CLAIM_IDS = "C-157–C-159"
RESULT_ID = "A-ERCF3-T3-JOINT-001"
OUTCOME_ID = "OUT-TOP-ERCF3-T3-JOINT-RECURSION"
README = "HoTT/formal/ercf3-t3/README.md"
SOURCE = "HoTT/formal/ercf3-t3/JointRecursion.agda"
RUN_DIR = "HoTT/verification/runs/20260913-MP-ERCF3-T3-JOINT-001-02"
FAILED_RUN = "HoTT/verification/runs/20260913-MP-ERCF3-T3-JOINT-001-01"
TOOLCHAIN = "HoTT/formal/ercf3-t3/TOOLCHAIN.json"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
CLOSURE = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"

SPEC = importlib.util.spec_from_file_location("runtime_s110", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | `MP-ERCF3-T3-JOINT-001`（T3 第十四脉冲）：**共享判定联合递归**收口——"
    "（C-157）显式判定下码级修正替换与语法级替换一致；（C-158）**原始逐出现判定的项层恒等式**成立"
    "（N34 记录的剩余义务）；（C-159）修正后的公式层码替换与语法替换一致 | "
    "`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | "
    "当前工作包（用户目标「全部做完再停下」；第二线 T3） | `MACHINE_PROVED_LOCAL_UNCOMMITTED / "
    "ERCF3_T3_SHARED_DECISION_JOINT_RECURSION` | Agda 2.8.0-3d04bac + Cubical v0.9 库声明、仅 Agda builtins、"
    "exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；`-01` 为 `--safe` pragma 触发 `CoInfectiveImport` 的"
    "失败尝试（保留）；复现修正：`CodeStoreFixF` 的 `all` 影子分支曾双重编码（`codeF (all m φ)` 应为 `codeF φ`） | "
    "**不是** ERCF-3 本体（无证明谓词表示性/反射/对角不动点）；不使用 univalence/cubical Path/HIT/truncation；"
    "ERCF-3 保持 `GATED`；历史脉冲文件逐字节未改 | "
    f"`{README}`；`{MATRIX}`（追加节）；`{RUN_DIR}/RUN.json`；`{CLOSURE}`（later_packages） |\n"
)

AUDIT_FOCUS = {
    "KC-000021": ("ALIGNED", "按 F-011 走完源码→canonical run→索引→版本登记；实际 kernel exit 0、stderr 0。"),
    "KC-000028": ("DEEPENED", "自反线（自馈回环）所需的编码层义务被收口：替换与编码在哪一侧对齐已机器化。"),
    "KC-000030": ("ALIGNED", "理论经济/工具链代价如实记录（--safe pragma 传染、早期脉冲模块缺 pragma 导致 canonical 命令选择）。"),
    "KC-000036": ("ALIGNED", "Gödel/自馈仍归门 B；本包不升级为 HoTT 特有结论，只闭合编码层义务。"),
    "KC-000025": ("ALIGNED", "自指线要求真实连接；本包只交付编码层结果，不冒充自指实例。"),
    "KC-000017": ("ALIGNED", "以 kernel 与源码约束判断；发现的历史脉冲 bug 以新模块+README 登记，不重写历史。"),
    "KC-000005": ("ALIGNED", "先固定精确命题（三条）再交付，未追认更强归因。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是 T3 编码层义务的机器收口，不产生新的理论结论。",
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
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{README}`；{kid} | 数学开放项不变。 |"
        )
    aligned = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "ALIGNED")
    deepened = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "DEEPENED")
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: YES_IN_PLACE — 方向行原位记录 T3 编码层义务收口与 ERCF-3 仍 gated。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/006 ERCF-3 与 T3 脉冲 shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 第二线 T3 的编码/替换一致义务已闭合；下一义务为证明谓词表示性、反射与对角不动点（保持 gated，需消费者）。",
        "- cross_conflicts: 历史脉冲 `CodeStoreFixF` 的 `all` 影子分支双重编码被新模块修正；历史文件与会话证据逐字节保留，冲突以“修正记录”而非改写解决。",
        "- unresolved: P 表示性/反射/自应用未做；ERCF-3 仍 GATED；本包不构成 HoTT 悖论或内部不一致。",
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
    if state.get("revision") != 109 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_109_S109")

    run = json.loads((root / RUN_DIR / "RUN.json").read_text(encoding="utf-8"))
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
        raise SystemExit("RUN_NOT_READY")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "093"),
        ("PANORAMA", R.PANORAMA, "outcome", "093"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 109", "source_state_revision: 110"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-094",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/003 - LocalGPT 与 WebGPT 方向.md",
        "T3 保持 gated 并预测为 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，不把一般 Gödel 口号冒充 HoTT 实例 |",
        "T3 的**编码/替换一致义务已机器收口**（`MP-ERCF3-T3-JOINT-001` / C-157–C-159：共享判定联合递归 + "
        "原始逐出现判定的项层恒等式 + 修正后的公式层恒等式，run `-02` exit 0）；下一义务是证明谓词表示性、反射与"
        "对角不动点，ERCF-3 本体保持 `GATED`，仍预测为 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，不把一般 Gödel 口号冒充 HoTT 实例 |",
    )
    projection_edit.append_to_shard(
        projections["PANORAMA"],
        "全景视野/006 - ERCF-3 与 T3 脉冲及失败台账.md",
        OUTCOME_ROW,
    )

    memory = projection_edit.load(root, "MEMORY.md")
    projection_edit.replace_in_shard(
        memory,
        "MEMORY/001 - 当前执行队列.md",
        "3. 数学研究第二线：T3 共享判定联合递归。没有自然自验证 consumer 时保持 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，"
        "不冒充 HoTT 悖论。",
        "3. 数学研究第二线：T3 **共享判定联合递归已完成**（`MP-ERCF3-T3-JOINT-001`，C-157–C-159，run `-02` exit 0、"
        "`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）：显式共享判定一致 + 原始逐出现判定的**项层恒等式** + 修正后的公式层恒等式；"
        "下一义务是证明谓词表示性、反射与对角不动点。ERCF-3 本体保持 `GATED`；没有自然自验证 consumer 时保持 "
        "`GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，不冒充 HoTT 悖论。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S110 第二线 T3 编码层义务收口（用户目标「全部做完再停下」）：新增包 `MP-ERCF3-T3-JOINT-001`"
        "（C-157–C-159）——(C-157) 显式共享判定下码级修正替换与语法级替换一致 `substFixTd-agrees`；"
        "(C-158) **原始逐出现判定的项层恒等式** `substFixT k i t ≡ codeT (substT k i t)`（`fixT-agrees`，"
        "即 N34 记录的剩余义务）；(C-159) **修正后**的公式层码替换一致 `substFixFc k i φ ≡ codeF (substF k i φ)`"
        "（`fixF-agrees`）。canonical run `20260913-MP-ERCF3-T3-JOINT-001-02`：Agda 2.8.0-3d04bac、仅 Agda builtins、"
        "exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；`-01` 为 `--safe` 文件 pragma 触发 "
        "`CoInfectiveImport` 的失败尝试（保留）。发现并登记历史脉冲 `CodeStoreFixF` 的 `all` 影子分支双重编码错误"
        "（`codeF (all m φ)` 应为 `codeF φ`），历史文件与会话证据逐字节未改。`PROOF_VERSION_CLOSURE.json` 的 "
        "`later_packages` 追加第 2 条，later claims 8→11；`verify_proof_version_closure.py` PASS_WITH_SCOPE"
        "（17 冻结 + 2 追加）。**ERCF-3 仍 `GATED`**：无证明谓词表示性/反射/对角不动点，不构成 HoTT 悖论。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row58 = (
        "| 已闭合工作包 58 | 自主构造第三轮与搜索空间收口（S109） | "
        "`IDENTITY_CHANGE_AXIS_REDUCES_TO_INTERPRETATION_CONFLICT` / `EXPRESSIBILITY_AXIS_NO_HOTT_SPECIFIC_GAP` / "
        "`SEARCH_SPACE_REDUCES_TO_TWO_DOORS` | 身份轴三位置穷尽；表达轴三候选均无 HoTT 特有缺口；"
        "收口为门 A（不可形式化，先需规格）/ 门 B（同层自我担保，gated 缺消费者）；见 "
        "`audit/自主构造第三轮-表达与身份两轴-20260913.md` |"
    )
    frontier = replace_once(
        frontier,
        row58,
        row58 + "\n| 已闭合工作包 59 | ERCF-3 T3 共享判定联合递归（S110，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_SHARED_DECISION_JOINT_RECURSION` | "
        "C-157–C-159：显式共享判定一致 + 原始逐出现判定的项层恒等式 + 修正后的公式层恒等式；"
        f"run `{RUN_DIR}` exit 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；修正 `CodeStoreFixF` 的 all 影子分支双重编码"
        f"（新模块给出，不改历史）；见 `{README}` 与矩阵追加节 |",
    )
    frontier = replace_once(
        frontier,
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | blocked-on-natural-consumer-and-exact-calculus | "
        "只有资格提升桥梁成立才构造 diagonal |",
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | encoding-layer-obligation-closed; "
        "blocked-on-proof-predicate-representability-reflectance-and-consumer | "
        "T3 编码/替换一致义务已机器收口（C-157–C-159）；下一义务为 P 表示性、反射与对角不动点；"
        "ERCF-3 本体保持 gated，只有资格提升桥梁成立才构造 diagonal |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n89. T3 的“共享判定”教训：`--safe` 作为**文件 pragma** 会传染给未声明 `--safe` 的历史脉冲模块并触发 "
        "`CoInfectiveImport`，而**命令行 `--safe`** 不会——canonical run 必须与既存脉冲命令一致，失败尝试保留为 `-01`。"
        "另一条经验：**试图证明恒等式本身就是查错手段**——公式层证明失败时发现历史脉冲 `CodeStoreFixF` 的 `all` 影子分支"
        "把 `codeF φ` 写成了 `codeF (all m φ)`（双重编码）；正确做法是新模块给出修正函数并以新 claim 登记，"
        "历史文件与会话证据逐字节不改。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S110：第二线 T3 的编码层义务收口——`MP-ERCF3-T3-JOINT-001`（C-157–C-159）机器证明显式共享判定一致、"
        "**原始逐出现判定的项层恒等式**与修正后的公式层恒等式；run `-02` exit 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；"
        "`verify_proof_version_closure.py` PASS_WITH_SCOPE（17 冻结 + 2 追加包）。修正了历史脉冲 `CodeStoreFixF` 的 "
        "`all` 影子分支双重编码错误（新模块给出，不改历史）。**ERCF-3 仍 GATED**：下一义务是证明谓词表示性、反射与"
        "对角不动点，仍需消费者。第一工作包（两扇门）与门 A/门 B 状态不变。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目标「全部做完再停下」：执行 FRONTIER 第二线（T3 共享判定联合递归），完成 F-011 全链。
- 交付：`{README}`；`{SOURCE}`；canonical run `{RUN_DIR}`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）；失败尝试 `{FAILED_RUN}`（`--safe` pragma ⇒ `CoInfectiveImport`，保留）；
  矩阵追加节 `{MATRIX}`（`C-157`–`C-159`）；`{CLOSURE}` 的 `later_packages` 第 2 条（later claims 8→11）。
- 三条 claim：C-157 显式共享判定一致；C-158 原始逐出现判定的项层恒等式（N34 的剩余义务）；C-159 修正后的公式层恒等式
  （修正 `CodeStoreFixF` 的 `all` 影子分支双重编码）。
- 状态边界：不是 ERCF-3 本体（无 P 表示性/反射/对角不动点）；ERCF-3 保持 `GATED`；不使用 univalence/cubical Path/HIT/truncation；
  历史脉冲文件逐字节未改；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "proof_package": {
                "proof_id": PROOF_ID,
                "claim_ids": CLAIM_IDS,
                "source": SOURCE,
                "run": RUN_DIR,
                "toolchain": TOOLCHAIN,
                "status": "KERNEL_ACCEPTED_WITH_SCOPE",
                "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
                "failed_attempt": FAILED_RUN,
                "verdict": "ERCF3_T3_SHARED_DECISION_JOINT_RECURSION",
            },
            "closure_registry": {"later_packages": 2, "later_machine_proved_claims": 11},
            "new_math_claims": ["C-157", "C-158", "C-159"],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 110
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_ERCF3_T3_JOINT_RECURSION",
            "status": STATUS,
            "next_minimal_verification": (
                "Second line (T3) next obligation: proof-predicate representability, reflection and the diagonal fixed point "
                "over the now-closed encoding layer (C-157-C-159). ERCF-3 stays GATED; without a consumer the prediction "
                "remains GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC. First line (two doors) unchanged: door A needs a formalisable "
                "reality-quantity specification, door B needs a same-layer self-guarantee consumer."
            ),
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-094", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-094", "semantic_status": STATUS}
    )
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": README,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-ERCF3-T2-ENCODING-ROUTE-001", "A-ERCF3-PREREQUISITE-ASSESSMENT-001"],
        "full_sources": [README, SOURCE, f"{RUN_DIR}/RUN.json", MATRIX, CLOSURE, TOOLCHAIN],
        "source_hashes": {
            SOURCE: R.sha((root / SOURCE).read_bytes()),
            f"{RUN_DIR}/RUN.json": R.sha((root / RUN_DIR / "RUN.json").read_bytes()),
            MATRIX: R.sha((root / MATRIX).read_bytes()),
            CLOSURE: R.sha((root / CLOSURE).read_bytes()),
        },
        "scope": (
            "MP-ERCF3-T3-JOINT-001 (C-157-C-159): shared-decision joint recursion at the encoding layer. C-157 the corrected "
            "code-level substitution agrees with the explicit-decision syntax-level substitution; C-158 the original "
            "per-occurrence term-level identity substFixT ≡ codeT ∘ substT; C-159 the corrected formula-level identity with "
            "substFixFc, fixing the double-encoded `all` shadow branch of CodeStoreFixF. Native Agda 2.8.0 run, exit 0, "
            "indexed. ERCF-3 itself remains GATED: no proof-predicate representability, no reflection, no diagonal fixed point."
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
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, README, f"{RUN_DIR}/RUN.json"],
        "source_hashes": {},
        "scope": (
            "Registration of MP-ERCF3-T3-JOINT-001: canonical run, matrix append section, closure later_packages entry, "
            "projection/MEMORY/FRONTIER/LESSONS/RESUME updates. ERCF-3 remains gated."
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
            "Active goal 'finish everything before stopping'. The registered second research line (T3 shared-decision joint "
            "recursion) was self-contained and did not need external input, so it was executed end to end: new proof module, "
            "canonical pinned-toolchain run, matrix append section, closure registry entry, package README, and this state "
            "registration. ERCF-3 remains gated. No push."
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
                "revision": 110,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
