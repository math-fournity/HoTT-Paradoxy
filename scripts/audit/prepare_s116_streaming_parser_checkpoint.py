#!/usr/bin/env python3
"""Prepare revision 116: register MP-ERCF3-T3-STREAMING-PARSER-001 (coding repair closed)."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-116-ERCF3-T3-STREAMING-PARSER"
PREV = "S-RES-20260913-115-ERCF3-T3-BIT-CODING"
RESULT_ID = "A-ERCF3-T3-STREAMING-PARSER-001"
OUTCOME_ID = "OUT-TOP-ERCF3-T3-STREAMING-PARSER"
SOURCE = "HoTT/formal/ercf3-t3/StreamingParser.agda"
DIR_README = "HoTT/formal/ercf3-t3/README.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
RUN_DIR = "HoTT/verification/runs/20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01"
TOOLCHAIN = "HoTT/formal/ercf3-t3/TOOLCHAIN.json"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
CLOSURE = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
EXPECTED_REPIN = {"A-MATH-PROOF-DELIVERY-GATE-001", "S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"}

SPEC = importlib.util.spec_from_file_location("runtime_s116", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | `MP-ERCF3-T3-STREAMING-PARSER-001`（T3 第十九脉冲）：**符号层 + 流式解析器 + 修复后的 Nat 值编码**——"
    "自定界一元索引层（C-173）；符号层 `bits`/`BLEN` 与燃料精确的流式 `run`（显式框架栈解决顺序消费，C-174）；"
    "长度对账、界即和分解与 `unbits` 多余燃料分解（C-175）；`codeT' = codeBits ∘ bits` 带全解码器 `dec`、"
    "往返 `dec (codeT' t) ≡ t`，故由 C-164 单射（C-176）——**在编码层闭合 `CodingRepair` 的修复义务（C-163/C-164/C-165）** | "
    "`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | "
    "当前工作包（用户目标「全部做完再停下」；第二线 T3） | "
    "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_NAT_CODING` | Agda 2.8.0-3d04bac、仅 Agda builtins、"
    "exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；剩余：公式层 `codeF` 的对应修复、与对象层替换"
    "（`substFix` 系列）对齐、P 表示性/反射/对角不动点（仍需门 B 消费者） | "
    "只覆盖 **Tm** 的编码/解码与单射性；不修复 `codeF` 实现、不重做旧 `codeT`/`codeF` 的对象层替换一致义务；"
    "历史脉冲文件与 `DiagonalCore` 既有编码逐字节未改；ERCF-3 保持 `GATED` | "
    f"`{DIR_README}`；`{MATRIX}`（追加节）；`{RUN_DIR}/RUN.json`；`{CLOSURE}`（later_packages） |\n"
)

AUDIT_FOCUS = {
    "KC-000021": ("ALIGNED", "按 F-011 完成源码→canonical run→索引→版本登记；kernel exit 0、stderr 0。"),
    "KC-000028": ("DEEPENED", "自反线前置 (a) 的编码缺口在编码层闭合：存在可解码（故单射）的 Nat 值编码。"),
    "KC-000030": ("ALIGNED", "把算术半按三段推进后收口；剩余义务（公式层修复、替换对齐、P 表示性）如实登记。"),
    "KC-000036": ("ALIGNED", "编码层可解码 ≠ HoTT 自馈；Gödel/自馈仍归门 B，本包不升级为 HoTT 特有结论。"),
    "KC-000025": ("ALIGNED", "自指线仍要求真实连接：本包只交付前置编码层，不构造对角不动点。"),
    "KC-000017": ("ALIGNED", "以 kernel 与源码为据；四条命题都有源码标识与哈希固定的 run。"),
    "KC-000005": ("ALIGNED", "先固定四条精确命题再交付；范围与禁止外推显式写明。"),
    "KC-000014": ("ALIGNED", "编码层闭合 ≠ 对角引理已形式化；禁止外推里逐项写明未做部分。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是修复编码的算术半第三片（符号层 + 流式解析器 + Nat 值修复编码），不产生新的理论结论。",
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
        "- direction_change: YES_IN_PLACE — 方向行原位记录编码层修复义务闭合与新的剩余义务。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/006 shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 算术半三段（标签算术 → 位级底座 → 符号层/解析器/修复编码）全部闭合；T3 编码层义务收口，剩余为公式层修复、替换对齐与门 B 本体。",
        "- cross_conflicts: 无新增冲突；新编码与旧 `codeT`/`codeF` 的边界在禁止外推里写明。",
        "- unresolved: `codeF` 的对应修复、`codeT'`/`dec` 与对象层替换（`substFix` 系列）对齐、P 表示性/反射/对角不动点均未做。",
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
    if state.get("revision") != 115 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_115_S115")

    run = json.loads((root / RUN_DIR / "RUN.json").read_text(encoding="utf-8"))
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
        raise SystemExit("RUN_NOT_READY")
    if run.get("claim_ids") != ["C-173", "C-174", "C-175", "C-176"]:
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
                "MP-ERCF3-T3-STREAMING-PARSER-001 (C-173-C-176) and its run. Record scope, claims and evidence status unchanged."
            )
            repinned.append(record_id)
    if set(repinned) != EXPECTED_REPIN:
        raise SystemExit(f"EXPECTED_TWO_REPIN:{sorted(repinned)}")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "099"),
        ("PANORAMA", R.PANORAMA, "outcome", "099"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 115", "source_state_revision: 116"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-100",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/003 - LocalGPT 与 WebGPT 方向.md",
        "**下一义务=符号层（自定界索引位 + 构造子标签）+ 带缺省分支的解析器 + 像上往返**；"
        "其后才是证明谓词表示性、反射与对角不动点。",
        "**第三片（符号层 + 流式解析器 + 修复后的 Nat 值编码）亦已机器收口**（`MP-ERCF3-T3-STREAMING-PARSER-001` / "
        "C-173–C-176：一元索引自定界、燃料精确的流式 `run`（显式框架栈解决顺序消费）、`codeT' = codeBits ∘ bits` "
        "带全解码器 `dec`、往返 `dec (codeT' t) ≡ t` ⇒ 单射，**编码层修复义务已闭合**）。"
        "**下一义务=公式层 `codeF` 的对应修复 + 把 `codeT'`/`dec` 与对象层替换（`substFix` 系列）对齐**；"
        "其后才是证明谓词表示性、反射与对角不动点（仍需门 B 消费者）。",
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
        "**下一义务=符号层（自定界索引位 + 构造子标签）+ 带缺省分支的解析器 + 像上往返**，"
        "其后才是证明谓词表示性、反射与对角不动点。",
        "**第三片（符号层 + 流式解析器 + 修复后的 Nat 值编码）亦已完成**（`MP-ERCF3-T3-STREAMING-PARSER-001`，"
        "C-173–C-176：一元索引自定界、燃料精确的 `run`、`codeT' = codeBits ∘ bits` 带全解码器 `dec`、"
        "往返 `dec (codeT' t) ≡ t` ⇒ 单射，**编码层修复义务已闭合**）；**下一义务=公式层 `codeF` 的对应修复 + "
        "与对象层替换（`substFix` 系列）对齐**，其后才是证明谓词表示性、反射与对角不动点。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S116 T3 第十九脉冲：符号层 + 流式解析器 + 修复后的 Nat 值编码（`MP-ERCF3-T3-STREAMING-PARSER-001`，"
        "C-173–C-176）。C-173 自定界一元索引层（`unary-run`）；C-174 符号层 `bits`/`BLEN` 与**燃料精确**的流式解析器 "
        "`run`（显式框架栈 `Slot`/`Stack`/`close` 在同一个递减递归内解决顺序消费，`parse-run`/`parse-run-app`）；"
        "C-175 长度对账 `LEN (bits t) ≡ BLEN t`、界即和分解 `≤-split`、`unbits` 多余燃料分解 `unbits-split`；"
        "C-176 `codeT' = codeBits ∘ bits` 带全解码器 `dec`（含缺省分支）与往返 `dec (codeT' t) ≡ t`，"
        "由 C-164 得单射（`codeT'-injective`）——**在编码层闭合 `CodingRepair` 的修复义务（C-163/C-164/C-165）**。"
        "run `20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01`：Agda 2.8.0-3d04bac、仅 builtins、exit 0、stderr 0、"
        "`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；`index-row-manifest.json` 5 行冻结；`later_packages` 第 7 条，"
        "later claims 23→27。剩余：公式层 `codeF` 的对应修复、与对象层替换（`substFix` 系列）对齐、"
        "P 表示性/反射/对角不动点。ERCF-3 保持 `GATED`；未新增理论结论。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row64 = (
        "| 已闭合工作包 64 | T3 算术半第二片：位级底座与燃料界（S115，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_BIT_SUBSTRATE` | C-169–C-172：最低位/折半数字算术、"
        "`codeBits`/`unbits` 两侧引理与已知长度往返、码支配自身长度；**下一义务=符号层（自定界索引位 + 构造子标签）"
        "+ 带缺省分支的解析器 + 像上往返**；见 `HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |"
    )
    frontier = replace_once(
        frontier,
        row64,
        row64 + "\n| 已闭合工作包 65 | T3 符号层 + 流式解析器 + 修复后的 Nat 值编码（S116，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_NAT_CODING` | C-173–C-176：一元索引自定界、"
        "燃料精确的流式 `run`、长度/界/多余燃料分解、`codeT'` 带全解码器与像上往返 ⇒ 单射；"
        "**编码层修复义务（C-163/C-164/C-165）已闭合**；剩余=公式层 `codeF` 修复 + 替换对齐 + P 表示性/反射/对角不动点；"
        "见 `HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |",
    )
    frontier = replace_once(
        frontier,
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | arithmetic-half-bit-substrate-closed; "
        "next-obligation-is-the-symbol-layer-and-the-parser | "
        "T3 编码/替换一致（C-157–C-159）、可解码性围栏（C-160–C-162）、修复规格（C-163–C-165）、算术半第一片"
        "（C-166–C-168）与第二片位级底座（C-169–C-172）均已闭合；**下一义务=符号层（自定界索引位 + 构造子标签）"
        "+ 带缺省分支的解析器 + 像上往返**，其后才是 P 表示性、反射与对角不动点；ERCF-3 本体保持 gated |",
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | coding-repair-obligation-closed-at-the-coding-layer; "
        "next-obligation-is-the-formula-layer-and-substitution-alignment | "
        "T3 编码/替换一致（C-157–C-159）、可解码性围栏（C-160–C-162）、修复规格（C-163–C-165）与算术半三段"
        "（C-166–C-168、C-169–C-172、C-173–C-176）均已闭合，**编码层修复义务已闭合**；"
        "**下一义务=公式层 `codeF` 的对应修复 + 与对象层替换（`substFix` 系列）对齐**，其后才是 P 表示性、"
        "反射与对角不动点（仍需门 B 消费者）；ERCF-3 本体保持 gated |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n95. 解析器的难点不在文法而在**递归形状**：`(t +t u)` 的自然解析是「先解析 t、再解析 u」，"
        "第二次调用必须用第一次调用**返回**的燃料，这在 Agda 里既不是结构递归也不被终止检查接受。"
        "解法是把待解析的右子做成显式框架栈（`Slot`/`Stack`/`close`），让每步只做一次 `run f rest …`："
        "一次迭代恰好消费一位、消耗一个燃料单位，结构递归立即通过，而往返定理仍可写成**精确**形式"
        "（燃料 `BLEN t + k`，剩余恰为 `k`）。两条配套经验：把「多余燃料」下的 `unbits` 说成"
        "`unbits (i + j) c ≡ unbits i c ++ unbits j (halfs i c)`，再用 `n ≤ m → Σ k, m ≡ n + k`"
        "把 C-172 的界转成燃料形式，就完全避开了减法算术；以及 Agda 的 `rewrite` 在目标含"
        "同名子项时会同时改写不该动的位置（本轮 `junk` 内层被连带改写），改用 `subst'` 显式指定"
        "要改写的那个位置更稳。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S116：T3 编码层修复义务闭合（`MP-ERCF3-T3-STREAMING-PARSER-001`，C-173–C-176）——自定界一元索引、"
        "燃料精确的流式解析器、`codeT' = codeBits ∘ bits` 带全解码器 `dec` 与往返 ⇒ 单射；`later_packages` 第 7 条"
        "（later claims 23→27）。**下一义务=公式层 `codeF` 的对应修复 + 与对象层替换（`substFix` 系列）对齐**，"
        "其后才是 P 表示性/反射/对角不动点（仍需门 B 消费者）。ERCF-3 保持 `GATED`；门 A/门 B 状态不变。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目标「全部做完再停下」，第二线 T3 第十九脉冲：符号层 + 流式解析器 + 修复后的 Nat 值编码。
- 交付：`{SOURCE}`；canonical run `{RUN_DIR}`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（5 行冻结）；矩阵追加节（`C-173`–`C-176`）；
  `{CLOSURE}` 的 `later_packages` 第 7 条（later claims 23→27）；`{DIR_README}` / `{FORMAL_README}` /
  `{RUNS_README}` 索引同步（两条 owner record revalidation 重绑）。
- 四条 claim：C-173 自定界一元索引层；C-174 符号层与燃料精确的流式解析器；C-175 长度对账/界即和分解/
  多余燃料分解；C-176 `codeT'` 带全解码器 `dec`、往返 ⇒ 单射（**编码层修复义务闭合**）。
- 边界：只覆盖 Tm 的编码/解码与单射性；不修复 `codeF` 实现、不重做旧 `codeT`/`codeF` 的对象层替换一致义务；
  不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`；历史脉冲文件逐字节未改；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "proof_package": {
                "proof_id": "MP-ERCF3-T3-STREAMING-PARSER-001",
                "claim_ids": "C-173–C-176",
                "source": SOURCE,
                "run": RUN_DIR,
                "toolchain": TOOLCHAIN,
                "status": "KERNEL_ACCEPTED_WITH_SCOPE",
                "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
                "verdict": "ERCF3_T3_REPAIRED_NAT_CODING",
            },
            "closure_registry": {"later_packages": 7, "later_machine_proved_claims": 27},
            "repinned_records": sorted(repinned),
            "new_math_claims": ["C-173", "C-174", "C-175", "C-176"],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 116
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_ERCF3_T3_STREAMING_PARSER",
            "status": STATUS,
            "next_minimal_verification": (
                "Second line (T3): the coding-repair obligation of CodingRepair is closed at the coding layer (a Nat-valued "
                "coder with a total decoder, hence injective). Next bounded obligation: the formula layer (the corresponding "
                "repair of `codeF`) and the alignment of `codeT'`/`dec` with the object-level substitution of the "
                "`substFix` family. After that: proof-predicate representability, reflection and the diagonal fixed point, "
                "which still need the door-B consumer. ERCF-3 stays GATED. First line (two doors) unchanged."
            ),
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-100", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-100", "semantic_status": STATUS}
    )
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-ERCF3-T3-BIT-CODING-001", "A-ERCF3-T3-REPAIR-SPEC-001"],
        "full_sources": [SOURCE, DIR_README, f"{RUN_DIR}/RUN.json", MATRIX, CLOSURE, TOOLCHAIN],
        "source_hashes": {
            SOURCE: R.sha((root / SOURCE).read_bytes()),
            f"{RUN_DIR}/RUN.json": R.sha((root / RUN_DIR / "RUN.json").read_bytes()),
            MATRIX: R.sha((root / MATRIX).read_bytes()),
            CLOSURE: R.sha((root / CLOSURE).read_bytes()),
        },
        "scope": (
            "MP-ERCF3-T3-STREAMING-PARSER-001 (C-173-C-176): the symbol layer, a streaming parser whose round trip is "
            "fuel-exact, the length/bound/extra-fuel bookkeeping, and the repaired Nat-valued coder codeT' = codeBits . bits "
            "with a total decoder dec and the round trip dec (codeT' t) = t -- hence injectivity by C-164. This closes the "
            "coding-repair obligation recorded in CodingRepair (C-163/C-164/C-165) at the coding layer. Only Tm coding is "
            "covered: codeF, object-level substitution alignment, proof-predicate representability, reflection and the "
            "diagonal fixed point remain open; ERCF-3 remains gated."
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
            "Registration of MP-ERCF3-T3-STREAMING-PARSER-001: canonical run, matrix append section, closure "
            "later_packages entry, index updates and two owner record revalidations. ERCF-3 remains gated."
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
            "Active goal 'finish everything before stopping'. Next self-contained obligation: the symbol layer plus the "
            "streaming parser plus the repaired Nat-valued coding, closing the coding-repair obligation at the coding layer. "
            "No new theoretical claim, no push."
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
                "revision": 116,
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
