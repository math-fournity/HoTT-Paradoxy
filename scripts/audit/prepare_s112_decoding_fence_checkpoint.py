#!/usr/bin/env python3
"""Prepare revision 112: register MP-ERCF3-T3-DECODING-001 (decodability/injectivity fence)."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-112-ERCF3-T3-DECODING"
PREV = "S-GOV-20260913-111-PROOF-INDEX-REFRESH"
PROOF_ID = "MP-ERCF3-T3-DECODING-001"
RESULT_ID = "A-ERCF3-T3-DECODING-001"
OUTCOME_ID = "OUT-TOP-ERCF3-T3-DECODABILITY-FENCE"
SOURCE = "HoTT/formal/ercf3-t3/DecodingFence.agda"
DIR_README = "HoTT/formal/ercf3-t3/README.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
RUN_DIR = "HoTT/verification/runs/20260913-MP-ERCF3-T3-DECODING-001-01"
TOOLCHAIN = "HoTT/formal/ercf3-t3/TOOLCHAIN.json"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
CLOSURE = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
EXPECTED_REPIN = {"A-MATH-PROOF-DELIVERY-GATE-001", "S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"}

SPEC = importlib.util.spec_from_file_location("runtime_s112", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | `MP-ERCF3-T3-DECODING-001`（T3 第十五脉冲）：编码的**可解码性/单射性围栏**——"
    "`codeT (var 2) ≡ codeT (num 0)` 而两项不同，故不存在单射解码器（C-160）；同一碰撞提升到公式层（C-161）；"
    "数字片段单射为正控制（C-162） | `DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、"
    "`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前工作包（用户目标「全部做完再停下」；第二线 T3） | "
    "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_DECODABILITY_FENCE` | Agda 2.8.0-3d04bac、仅 Agda builtins、"
    "exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；结论：`ObjectSyntax` 记录的 decodability/injectivity 义务"
    "**不能由当前编码满足**，需标签不相交（`3n`/`3n+1`/配对）或列表编码的修复 | "
    "不给出修复方案或其单射性证明；不声称对角引理不可形式化；不涉及 P 表示性/反射/对角不动点；"
    "不改写 `DiagonalCore` 的 `⌜-injective` 命名或历史脉冲文件；ERCF-3 保持 `GATED` | "
    f"`{DIR_README}`；`{MATRIX}`（追加节）；`{RUN_DIR}/RUN.json`；`{CLOSURE}`（later_packages） |\n"
)

AUDIT_FOCUS = {
    "KC-000021": ("ALIGNED", "按 F-011 完成源码→canonical run→索引→版本登记；kernel exit 0、stderr 0。"),
    "KC-000028": ("DEEPENED", "自反线的前置 (a) 被推进：编码的可解码性缺口被机器化，替代了“隐式假设编码可用”。"),
    "KC-000030": ("ALIGNED", "发现当前编码不单射并登记修复要求，属理论工具性代价的诚实记账。"),
    "KC-000036": ("ALIGNED", "Gödel/自馈仍归门 B；本包不升级为 HoTT 特有结论。"),
    "KC-000025": ("ALIGNED", "自指线仍要求真实连接：本包只交付前置义务的下界，不冒充自指实例。"),
    "KC-000017": ("ALIGNED", "以 kernel 与源码为据；发现的历史命名误用（`⌜-injective`）不改写文件，只登记。"),
    "KC-000005": ("ALIGNED", "先固定精确命题（三条）再交付，负结论有界。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是 T3 前置条件 (a) 的编码可解码性围栏，不产生新的理论结论。",
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
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{DIR_README}`；{kid} | 数学开放项不变。 |"
        )
    aligned = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "ALIGNED")
    deepened = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "DEEPENED")
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: YES_IN_PLACE — 方向行原位记录可解码性围栏与新的下一义务（修复编码）。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/006 shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: T3 前置 (a) 的“编码可解码/单射”缺口被机器化为**围栏**；下一义务=给出标签不相交或列表编码并证明其单射性，之后才是 P 表示性/反射/对角不动点。",
        "- cross_conflicts: `DiagonalCore.⌜-injective` 的命名与其实质（同余）不一致——以“登记误用、不改历史文件”处理。",
        "- unresolved: 修复编码未给出；P 表示性与对角不动点未做；ERCF-3 仍 GATED。",
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
    if state.get("revision") != 111 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_111_S111")

    run = json.loads((root / RUN_DIR / "RUN.json").read_text(encoding="utf-8"))
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
        raise SystemExit("RUN_NOT_READY")

    formal_hash = R.sha((root / FORMAL_README).read_bytes())
    runs_hash = R.sha((root / RUNS_README).read_bytes())
    repinned = []
    for record_id, record in state["records"].items():
        hashes = record.get("source_hashes") or {}
        changed = []
        for path, new_hash in ((FORMAL_README, formal_hash), (RUNS_README, runs_hash)):
            if path in hashes and hashes[path] != new_hash:
                hashes[path] = new_hash
                changed.append(path)
        if changed:
            record["source_hashes"] = hashes
            record["revalidation"] = (
                f"{', '.join(changed)} re-hashed by {SESSION_ID}: the formal package index and the run index gained "
                "MP-ERCF3-T3-DECODING-001 (C-160-C-162) and its run. Record scope, claims and evidence status unchanged."
            )
            repinned.append(record_id)
    if set(repinned) != EXPECTED_REPIN:
        raise SystemExit(f"EXPECTED_TWO_REPIN:{sorted(repinned)}")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "095"),
        ("PANORAMA", R.PANORAMA, "outcome", "095"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 111", "source_state_revision: 112"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-096",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/003 - LocalGPT 与 WebGPT 方向.md",
        "T3 的**编码/替换一致义务已机器收口**（`MP-ERCF3-T3-JOINT-001` / C-157–C-159：共享判定联合递归 + "
        "原始逐出现判定的项层恒等式 + 修正后的公式层恒等式，run `-02` exit 0）；下一义务是证明谓词表示性、反射与"
        "对角不动点，ERCF-3 本体保持 `GATED`，仍预测为 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，不把一般 Gödel 口号冒充 HoTT 实例",
        "T3 的**编码/替换一致义务**（`MP-ERCF3-T3-JOINT-001` / C-157–C-159）与**可解码性围栏**"
        "（`MP-ERCF3-T3-DECODING-001` / C-160–C-162：当前编码非单射、需标签不相交或列表编码修复）均已机器收口；"
        "**下一义务是给出修复后的编码并证明其单射性**，之后才是证明谓词表示性、反射与对角不动点。ERCF-3 本体保持 `GATED`，"
        "仍预测为 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，不把一般 Gödel 口号冒充 HoTT 实例",
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
        "3. 数学研究第二线：T3 **共享判定联合递归已完成**（`MP-ERCF3-T3-JOINT-001`，C-157–C-159，run `-02` exit 0、"
        "`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）：显式共享判定一致 + 原始逐出现判定的**项层恒等式** + 修正后的公式层恒等式；"
        "下一义务是证明谓词表示性、反射与对角不动点。ERCF-3 本体保持 `GATED`；没有自然自验证 consumer 时保持 "
        "`GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，不冒充 HoTT 悖论。",
        "3. 数学研究第二线：T3 **编码/替换一致**（`MP-ERCF3-T3-JOINT-001`，C-157–C-159）与**可解码性围栏**"
        "（`MP-ERCF3-T3-DECODING-001`，C-160–C-162：`codeT`/`codeF` 非单射，`var 2` 与 `num 0` 碰撞，**"
        "需标签不相交或列表编码修复**）均已机器收口。下一义务=给出修复后的编码并证明其单射性，之后才是证明谓词表示性、"
        "反射与对角不动点。ERCF-3 本体保持 `GATED`；没有自然自验证 consumer 时保持 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，"
        "不冒充 HoTT 悖论。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S112 T3 第十五脉冲：编码可解码性/单射性围栏（`MP-ERCF3-T3-DECODING-001`，C-160–C-162）。"
        "`codeT (var 2) ≡ codeT (num 0)` 而两项不同 ⇒ 不存在单射解码器（`no-injective-codeT`）；同一碰撞提升到公式层"
        "（`no-injective-codeF`）；数字片段单射为正控制（`num-code-injective`）。run "
        "`20260913-MP-ERCF3-T3-DECODING-001-01`：Agda 2.8.0-3d04bac、仅 builtins、exit 0、stderr 0、"
        "`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；`index-row-manifest.json` 4 行冻结。`later_packages` 追加第 3 条，"
        "later claims 11→14；`verify_proof_version_closure.py` 需在提交后复跑（要求新文件已 tracked）。"
        "结论：`ObjectSyntax` 记录的 decodability/injectivity 义务**不能被当前编码满足**，修复要求（标签值域不相交或列表编码）"
        "已登记为下一有界脉冲；`DiagonalCore.⌜-injective` 的命名误用只登记不改写。ERCF-3 保持 `GATED`。## 未新增理论结论。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row60 = (
        "| 已闭合工作包 60 | 证明/运行索引刷新（S111，corrective hygiene） | `INDEX_REFRESH_ONLY` | "
        "`HoTT/formal/README.md` 补齐两个 later package 与“17 冻结 + 2 追加”表述；"
        "`HoTT/verification/runs/README.md` 的 run 索引补齐 5 组 later runs；`HoTT/README.md` 计数与下一义务同步；"
        "两条 owner record 按新哈希 revalidation 重绑；数学与队列不变 |"
    )
    frontier = replace_once(
        frontier,
        row60,
        row60 + "\n| 已闭合工作包 61 | T3 编码可解码性围栏（S112，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_DECODABILITY_FENCE` | C-160–C-162：`codeT`/`codeF` 非单射"
        "（`var 2` 与 `num 0` 碰撞）、无单射解码器、数字片段正控制；结论是当前编码不满足 `ObjectSyntax` 记录的 "
        "decodability/injectivity 义务，需标签不相交/列表编码修复（下一有界脉冲）；见 "
        "`HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |",
    )
    frontier = replace_once(
        frontier,
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | encoding-layer-obligation-closed; "
        "blocked-on-proof-predicate-representability-reflectance-and-consumer | "
        "T3 编码/替换一致义务已机器收口（C-157–C-159）；下一义务为 P 表示性、反射与对角不动点；"
        "ERCF-3 本体保持 gated，只有资格提升桥梁成立才构造 diagonal |",
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | decodability-fence-closed; "
        "next-obligation-is-a-repaired-injective-coding | "
        "T3 编码/替换一致（C-157–C-159）与可解码性围栏（C-160–C-162）已闭合；**下一义务=修复编码（标签不相交或列表编码）"
        "并证明其单射性**，其后才是 P 表示性、反射与对角不动点；ERCF-3 本体保持 gated，只有资格提升桥梁成立才构造 diagonal |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n91. 登记义务前先查**命名是否兑现了承诺**：`DiagonalCore.⌜-injective` 只做“沿码相等的替换同余”，"
        "不是单射性；而 `ObjectSyntax` 明文把 decodability/injectivity 列为未形式化义务。"
        "把这条义务的下界机器化（`codeT (var 2) ≡ codeT (num 0)` 而两项不同 ⇒ 无单射解码器）比继续在错误编码上"
        "做 P 表示性更省时间：**当前编码不可解码，必须先修编码**。命名误用只登记、不改历史文件。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S112：T3 编码可解码性围栏完成（`MP-ERCF3-T3-DECODING-001`，C-160–C-162）——当前 `codeT`/`codeF` **非单射**"
        "（`var 2` 与 `num 0` 碰撞），无单射解码器，数字片段有正控制；`later_packages` 追加第 3 条（later claims 11→14）。"
        "**下一义务=给出修复后的编码（标签值域不相交或列表编码）并证明其单射性**，之后才是证明谓词表示性、反射与对角不动点。"
        "ERCF-3 保持 `GATED`；门 A/门 B 状态不变。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目标「全部做完再停下」，第二线 T3 第十五脉冲：编码可解码性/单射性围栏。
- 交付：`{SOURCE}`；canonical run `{RUN_DIR}`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`；矩阵追加节（`C-160`–`C-162`）；
  `{CLOSURE}` 的 `later_packages` 第 3 条（later claims 11→14）；`{DIR_README}` 的包清单与专节；
  `{FORMAL_README}` / `{RUNS_README}` 索引同步（两条 owner record revalidation 重绑）。
- 三条 claim：C-160 编码非单射（`var 2`/`num 0` 碰撞，无单射解码器）；C-161 公式层同碰撞；C-162 数字片段正控制。
- 结论：`ObjectSyntax` 记录的 decodability/injectivity 义务**不能被当前编码满足**；修复（标签值域不相交或列表编码）是下一有界脉冲。
- 边界：不给修复方案；不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`；不改写历史脉冲文件与 `⌜-injective` 命名；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "proof_package": {
                "proof_id": PROOF_ID,
                "claim_ids": "C-160–C-162",
                "source": SOURCE,
                "run": RUN_DIR,
                "toolchain": TOOLCHAIN,
                "status": "KERNEL_ACCEPTED_WITH_SCOPE",
                "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
                "verdict": "ERCF3_T3_DECODABILITY_FENCE",
            },
            "closure_registry": {"later_packages": 3, "later_machine_proved_claims": 14},
            "repinned_records": sorted(repinned),
            "new_math_claims": ["C-160", "C-161", "C-162"],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 112
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_ERCF3_T3_DECODING_FENCE",
            "status": STATUS,
            "next_minimal_verification": (
                "Second line (T3), next bounded pulse: give a repaired coding with disjoint tag ranges (e.g. var n ↦ 3n, "
                "num n ↦ 3n+1, _+t_ ↦ 3*pair+2) or a list-based encoding, and prove its injectivity/decodability; only then "
                "resume proof-predicate representability, reflection and the diagonal fixed point. ERCF-3 stays GATED. "
                "First line (two doors) unchanged: door A needs a formalisable reality-quantity specification, door B needs "
                "a same-layer self-guarantee consumer."
            ),
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-096", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-096", "semantic_status": STATUS}
    )
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-ERCF3-T3-JOINT-001", "A-ERCF3-T2-ENCODING-ROUTE-001"],
        "full_sources": [SOURCE, DIR_README, f"{RUN_DIR}/RUN.json", MATRIX, CLOSURE, TOOLCHAIN],
        "source_hashes": {
            SOURCE: R.sha((root / SOURCE).read_bytes()),
            f"{RUN_DIR}/RUN.json": R.sha((root / RUN_DIR / "RUN.json").read_bytes()),
            MATRIX: R.sha((root / MATRIX).read_bytes()),
            CLOSURE: R.sha((root / CLOSURE).read_bytes()),
        },
        "scope": (
            "MP-ERCF3-T3-DECODING-001 (C-160-C-162): the decodability/injectivity fence for the concrete coding. The coding "
            "is not injective (codeT (var 2) = codeT (num 0) while the terms differ), so no injective decoder exists; the "
            "same collision lifts to formulas; the numeral fragment is injective as a positive control. Conclusion: the "
            "decodability/injectivity obligation recorded in ObjectSyntax cannot be met by the current coding, so a repaired "
            "coding (disjoint tag ranges or list-based) must come first. ERCF-3 remains gated."
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
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, SOURCE, f"{RUN_DIR}/RUN.json"],
        "source_hashes": {},
        "scope": (
            "Registration of MP-ERCF3-T3-DECODING-001: canonical run, matrix append section, closure later_packages entry, "
            "directory/formal/run index updates, two owner record revalidations. ERCF-3 remains gated."
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
            "Active goal 'finish everything before stopping'. Next self-contained obligation of the second line: the "
            "decodability/injectivity obligation that ObjectSyntax explicitly leaves open. The fence is machine-checked, "
            "indexed, registered and the repaired coding is named as the next bounded pulse. No new theoretical claim, no push."
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
                "revision": 112,
                "session_id": SESSION_ID,
                "files": len(texts),
                "repinned": sorted(repinned),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
