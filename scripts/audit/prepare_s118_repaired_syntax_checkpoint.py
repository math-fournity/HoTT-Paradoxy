#!/usr/bin/env python3
"""Prepare revision 118: register MP-ERCF3-T3-REPAIRED-SYNTAX-001 (substitution + quotation)."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-118-ERCF3-T3-REPAIRED-SYNTAX"
PREV = "S-RES-20260913-117-ERCF3-T3-FORMULA-CODING"
RESULT_ID = "A-ERCF3-T3-REPAIRED-SYNTAX-001"
OUTCOME_ID = "OUT-TOP-ERCF3-T3-REPAIRED-SYNTAX"
SOURCE = "HoTT/formal/ercf3-t3/RepairedSyntax.agda"
DIR_README = "HoTT/formal/ercf3-t3/README.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
RUN_DIR = "HoTT/verification/runs/20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01"
TOOLCHAIN = "HoTT/formal/ercf3-t3/TOOLCHAIN.json"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
CLOSURE = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
EXPECTED_REPIN = {"A-MATH-PROOF-DELIVERY-GATE-001", "S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"}

SPEC = importlib.util.spec_from_file_location("runtime_s118", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | `MP-ERCF3-T3-REPAIRED-SYNTAX-001`（T3 第二十一脉冲）：**修复编码之上的替换一致与引用**——"
    "码级替换定义为「解码—替换—编码」，于是「码级替换 ≡ 语法级替换」在 `Tm`（C-181）与 `Fml`（C-182）两层都成为**推论**"
    "（旧编码需要 C-157–C-159 的联合递归工程）；引用 `⌜φ⌝' = num (codeF' φ)` 单射、对角实例 "
    "`diagonalize' φ = substF (codeF' φ) 0 φ` 是替换实例、其码可由码级替换算出（C-183） | "
    "`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | "
    "当前工作包（用户目标「全部做完再停下」；第二线 T3） | "
    "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_SUBSTITUTION_AND_QUOTATION` | Agda 2.8.0-3d04bac、"
    "仅 Agda builtins、exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；剩余：对象层可表示性、P 表示性、"
    "反射与对角不动点（门 B 消费者） | "
    "**诚实边界**：`substCodeT`/`substCodeF` 经解码器定义，本包不主张对象理论可表示它们；不构造 P、不证表示性/反射/对角不动点；"
    "历史脉冲文件与 `BitCoding`/`StreamingParser`/`FormulaCoding` 逐字节未改（三次 run 的 `source-manifest.json` 可交叉核对）；"
    "ERCF-3 保持 `GATED` | "
    f"`{DIR_README}`；`{MATRIX}`（追加节）；`{RUN_DIR}/RUN.json`；`{CLOSURE}`（later_packages） |\n"
)

AUDIT_FOCUS = {
    "KC-000021": ("ALIGNED", "按 F-011 完成源码→canonical run→索引→版本登记；kernel exit 0、stderr 0。"),
    "KC-000028": ("DEEPENED", "自反线前置 (a) 的形状已齐：修复编码 + 码级替换一致 + 引用单射 + 对角实例。"),
    "KC-000030": ("ALIGNED", "把「替换对齐」按修复编码收口，并把剩余义务（对象层可表示性）明确划到门 B。"),
    "KC-000036": ("ALIGNED", "引用/替换形状 ≠ HoTT 自馈；Gödel/自馈仍归门 B，本包不升级为 HoTT 特有结论。"),
    "KC-000025": ("ALIGNED", "自指线仍要求真实连接：本包只交付前置形状，不构造对角不动点。"),
    "KC-000017": ("ALIGNED", "以 kernel 与源码为据；三条命题都有源码标识与哈希固定的 run（含对既有模块哈希不变的交叉核对）。"),
    "KC-000005": ("ALIGNED", "先固定三条精确命题再交付；诚实边界（经解码器定义 vs 对象层可表示）显式写明。"),
    "KC-000014": ("ALIGNED", "替换一致与引用单射 ≠ 表示性；禁止外推里逐项写明未做部分。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是修复编码之上的替换一致与引用，不产生新的理论结论。",
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
        "- direction_change: YES_IN_PLACE — 方向行原位记录替换/引用形状闭合与门 B 剩余义务。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/006 shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: T3 编码线自足部分到此收口（编码 → 解析 → 替换 → 引用）；其余转入表示性/门 B。",
        "- cross_conflicts: 无新增冲突；「经解码器定义」与「对象层可表示」的区别在诚实边界与禁止外推里写明。",
        "- unresolved: 对象层可表示性、证明谓词 P 的表示性、反射与对角不动点均未做（需门 B 消费者）。",
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
    if state.get("revision") != 117 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_117_S117")

    run = json.loads((root / RUN_DIR / "RUN.json").read_text(encoding="utf-8"))
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
        raise SystemExit("RUN_NOT_READY")
    if run.get("claim_ids") != ["C-181", "C-182", "C-183"]:
        raise SystemExit("RUN_CLAIM_IDS_UNEXPECTED")

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
                "MP-ERCF3-T3-REPAIRED-SYNTAX-001 (C-181-C-183) and its run. Record scope, claims and evidence status unchanged."
            )
            repinned.append(record_id)
    if set(repinned) != EXPECTED_REPIN:
        raise SystemExit(f"EXPECTED_TWO_REPIN:{sorted(repinned)}")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "101"),
        ("PANORAMA", R.PANORAMA, "outcome", "101"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 117", "source_state_revision: 118"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-102",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/003 - LocalGPT 与 WebGPT 方向.md",
        "**下一义务=公式层与对象层替换（`substF`/`substFix` 系列）的对齐 + `⌜·⌝` 的算术化表示**；"
        "其后才是证明谓词表示性、反射与对角不动点（仍需门 B 消费者）。",
        "**第五片（修复编码之上的替换一致与引用）亦已机器收口**（`MP-ERCF3-T3-REPAIRED-SYNTAX-001` / C-181–C-183："
        "码级替换定义为「解码—替换—编码」，于是码级替换 ≡ 语法级替换在 `Tm`/`Fml` 两层都成为推论；引用 `⌜φ⌝'` 单射、"
        "对角实例是替换实例且其码可由码级替换算出）。**T3 的编码线自足部分到此收口**：剩余义务=对象层可表示性、"
        "证明谓词 `P` 的表示性、反射与对角不动点（仍需门 B 消费者）；",
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
        "**下一义务=公式层与对象层替换（`substF`/`substFix` 系列）的对齐 + `⌜·⌝` 的算术化表示**，"
        "其后才是证明谓词表示性、反射与对角不动点。",
        "**第五片（修复编码之上的替换一致与引用）亦已完成**（`MP-ERCF3-T3-REPAIRED-SYNTAX-001`，C-181–C-183："
        "码级替换=解码—替换—编码，`Tm`/`Fml` 两层一致都是推论；引用单射；对角实例及其码）。"
        "**T3 编码线自足部分收口**——剩余义务=对象层可表示性、证明谓词 `P` 的表示性、反射与对角不动点"
        "（需门 B 消费者）。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S118 T3 第二十一脉冲：修复编码之上的替换一致与引用（`MP-ERCF3-T3-REPAIRED-SYNTAX-001`，C-181–C-183）。"
        "C-181 `substCodeT k n c = codeT′ (substT k n (dec c))` 满足 `substCodeT k n (codeT′ t) ≡ codeT′ (substT k n t)`；"
        "C-182 公式层同型 `substCodeF k n (codeF′ φ) ≡ codeF′ (substF k n φ)`；C-183 引用 `⌜φ⌝′` 单射、"
        "对角实例 `diagonalize′ φ = substF (codeF′ φ) 0 φ` 是替换实例且 `codeF′ (diagonalize′ φ) ≡ "
        "substCodeF (codeF′ φ) 0 (codeF′ φ)`。诚实边界：两个码级函数经解码器定义，本包不主张对象理论可表示它们。"
        "run `20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01`：Agda 2.8.0-3d04bac、仅 builtins、exit 0、stderr 0、"
        "`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；`index-row-manifest.json` 4 行冻结；`later_packages` 第 9 条，"
        "later claims 31→34。剩余：对象层可表示性、P 表示性/反射/对角不动点。ERCF-3 保持 `GATED`；"
        "`BitCoding`/`StreamingParser`/`FormulaCoding` 哈希经 run 交叉核对未变。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row66 = (
        "| 已闭合工作包 66 | T3 修复编码的公式层（S117，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_FORMULA_CODING` | C-177–C-180：公式符号层与"
        "迭代数精确的 `run`、项层解析器复用、长度界、`codeF'` 带全解码器与往返 ⇒ 单射；"
        "**Tm 与 Fml 两级编码修复均已闭合**；剩余=替换对齐 + `⌜·⌝` 算术化 + P 表示性/反射/对角不动点；"
        "见 `HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |"
    )
    frontier = replace_once(
        frontier,
        row66,
        row66 + "\n| 已闭合工作包 67 | T3 修复编码之上的替换一致与引用（S118，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_SUBSTITUTION_AND_QUOTATION` | C-181–C-183："
        "码级替换=解码—替换—编码（`Tm`/`Fml` 两层一致为推论）、引用 `⌜φ⌝'` 单射、对角实例及其码；"
        "**T3 编码线自足部分收口**；剩余=对象层可表示性 + P 表示性/反射/对角不动点（门 B）；"
        "见 `HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |",
    )
    frontier = replace_once(
        frontier,
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | coding-repair-closed-at-both-Tm-and-Fml; "
        "next-obligation-is-substitution-alignment-and-quotation-arithmetisation | "
        "T3 编码/替换一致（C-157–C-159）、可解码性围栏（C-160–C-162）、修复规格（C-163–C-165）、算术半三段"
        "（C-166–C-168、C-169–C-172、C-173–C-176）与公式层修复（C-177–C-180）均已闭合；"
        "**下一义务=公式层与对象层替换（`substF`/`substFix` 系列）对齐 + `⌜·⌝` 的算术化表示**，其后才是 P 表示性、"
        "反射与对角不动点（仍需门 B 消费者）；ERCF-3 本体保持 gated |",
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | coding-and-substitution-shapes-closed; "
        "remaining-obligation-is-object-level-representability (door B) | "
        "T3 编码线自足部分收口：编码/替换一致（C-157–C-159）、可解码性围栏（C-160–C-162）、修复规格"
        "（C-163–C-165）、算术半三段（C-166–C-168、C-169–C-172、C-173–C-176）、公式层修复（C-177–C-180）与"
        "替换/引用形状（C-181–C-183）；**下一义务=对象层可表示性（算术/表示层）**，其后才是 P 表示性、反射与"
        "对角不动点（仍需门 B 消费者）；ERCF-3 本体保持 gated |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n97. 有了解码器之后，「码级替换与语法级替换一致」从工程变成**推论**：把码级替换定义为"
        "「解码—替换—编码」`substCode k n c = code' (subst k n (dec c))`，一致性就只是 `dec (code' t) ≡ t` 的一次改写"
        "（旧编码需要 C-157–C-159 的联合递归）。代价必须同时写清：这样的函数是**元层**的，"
        "「存在一个算得出来的函数」不等于「对象理论能表示它」——后者才是表示性义务。"
        "本轮据此把 T3 编码线自足部分收口，并把剩余义务明确归到门 B，避免用「看起来已完成」的推论冒充研究结论。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S118：T3 编码线自足部分收口（`MP-ERCF3-T3-REPAIRED-SYNTAX-001`，C-181–C-183）——码级替换=解码—替换—编码，"
        "`Tm`/`Fml` 两层替换一致成为推论；引用 `⌜φ⌝'` 单射；对角实例及其码。**诚实边界**：码级函数经解码器定义，"
        "不主张对象理论可表示；`later_packages` 第 9 条（later claims 31→34）。**下一义务=对象层可表示性（算术/表示层）**，"
        "其后才是 P 表示性/反射/对角不动点（仍需门 B 消费者）。ERCF-3 保持 `GATED`；门 A/门 B 状态不变。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目标「全部做完再停下」，第二线 T3 第二十一脉冲：修复编码之上的替换一致与引用。
- 交付：`{SOURCE}`；canonical run `{RUN_DIR}`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（4 行冻结）；矩阵追加节（`C-181`–`C-183`）；
  `{CLOSURE}` 的 `later_packages` 第 9 条（later claims 31→34）；`{DIR_README}` / `{FORMAL_README}` /
  `{RUNS_README}` 索引同步（两条 owner record revalidation 重绑）。
- 三条 claim：C-181 项层码级替换一致；C-182 公式层同型；C-183 引用单射 + 对角实例 + 其码。
- 诚实边界：码级替换经解码器定义（解码—替换—编码），不主张对象理论可表示该替换/引用。
- 交叉核对：`BitCoding`/`StreamingParser`/`FormulaCoding` 的哈希在各自注册 run、S117 run 与本 run 的
  `source-manifest.json` 中一致（逐字节未改）。
- 边界：不构造 P、不证表示性/反射/对角不动点（门 B）；ERCF-3 保持 `GATED`；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "proof_package": {
                "proof_id": "MP-ERCF3-T3-REPAIRED-SYNTAX-001",
                "claim_ids": "C-181–C-183",
                "source": SOURCE,
                "run": RUN_DIR,
                "toolchain": TOOLCHAIN,
                "status": "KERNEL_ACCEPTED_WITH_SCOPE",
                "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
                "verdict": "ERCF3_T3_REPAIRED_SUBSTITUTION_AND_QUOTATION",
            },
            "closure_registry": {"later_packages": 9, "later_machine_proved_claims": 34},
            "repinned_records": sorted(repinned),
            "new_math_claims": ["C-181", "C-182", "C-183"],
            "cross_checked_unchanged_modules": [
                "HoTT/formal/ercf3-t3/BitCoding.agda",
                "HoTT/formal/ercf3-t3/StreamingParser.agda",
                "HoTT/formal/ercf3-t3/FormulaCoding.agda",
            ],
            "honest_boundary": "substCodeT/substCodeF are defined through the decoders; object-level representability is NOT claimed",
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 118
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_ERCF3_T3_REPAIRED_SYNTAX",
            "status": STATUS,
            "next_minimal_verification": (
                "Second line (T3): the self-contained coding line is closed -- codings at both levels with total decoders "
                "(C-176, C-180), and substitution/quotation shapes over the repaired coding (C-181-C-183), with the honest "
                "boundary that the code-level substitution is defined through the decoders. The remaining obligation is the "
                "object-level representability layer (arithmetic/representation), after which come proof-predicate "
                "representability, reflection and the diagonal fixed point; all of these still need the door-B consumer. "
                "ERCF-3 stays GATED. First line (two doors) unchanged."
            ),
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-102", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-102", "semantic_status": STATUS}
    )
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-ERCF3-T3-FORMULA-CODING-001", "A-ERCF3-T3-STREAMING-PARSER-001"],
        "full_sources": [SOURCE, DIR_README, f"{RUN_DIR}/RUN.json", MATRIX, CLOSURE, TOOLCHAIN],
        "source_hashes": {
            SOURCE: R.sha((root / SOURCE).read_bytes()),
            f"{RUN_DIR}/RUN.json": R.sha((root / RUN_DIR / "RUN.json").read_bytes()),
            MATRIX: R.sha((root / MATRIX).read_bytes()),
            CLOSURE: R.sha((root / CLOSURE).read_bytes()),
        },
        "scope": (
            "MP-ERCF3-T3-REPAIRED-SYNTAX-001 (C-181-C-183): substitution and quotation over the repaired coding. "
            "Code-level substitution is defined as decode-substitute-encode, so the agreement with syntax-level "
            "substitution is a corollary at both levels (C-181/C-182); quotation is injective and the diagonal instance is a "
            "substitution instance whose code is reached by the code-level substitution (C-183). Honest boundary: these "
            "functions are defined through the decoders, so object-level representability, the proof predicate, reflection "
            "and the diagonal fixed point remain open (door B); ERCF-3 remains gated."
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
            "Registration of MP-ERCF3-T3-REPAIRED-SYNTAX-001: canonical run, matrix append section, closure later_packages "
            "entry, index updates, two owner record revalidations and the cross-check that BitCoding/StreamingParser/"
            "FormulaCoding are byte-identical to their registration runs. ERCF-3 remains gated."
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
            "Active goal 'finish everything before stopping'. Final self-contained obligation of the T3 coding line: "
            "substitution and quotation over the repaired coding, with the honest boundary that these code-level functions "
            "are defined through the decoders. No new theoretical claim, no push."
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
                "revision": 118,
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
