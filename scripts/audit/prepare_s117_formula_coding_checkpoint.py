#!/usr/bin/env python3
"""Prepare revision 117: register MP-ERCF3-T3-FORMULA-CODING-001 (formula layer of the repair)."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-117-ERCF3-T3-FORMULA-CODING"
PREV = "S-RES-20260913-116-ERCF3-T3-STREAMING-PARSER"
RESULT_ID = "A-ERCF3-T3-FORMULA-CODING-001"
OUTCOME_ID = "OUT-TOP-ERCF3-T3-FORMULA-CODING"
SOURCE = "HoTT/formal/ercf3-t3/FormulaCoding.agda"
DIR_README = "HoTT/formal/ercf3-t3/README.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
RUN_DIR = "HoTT/verification/runs/20260913-MP-ERCF3-T3-FORMULA-CODING-001-01"
TOOLCHAIN = "HoTT/formal/ercf3-t3/TOOLCHAIN.json"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
CLOSURE = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
EXPECTED_REPIN = {"A-MATH-PROOF-DELIVERY-GATE-001", "S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"}

SPEC = importlib.util.spec_from_file_location("runtime_s117", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | `MP-ERCF3-T3-FORMULA-CODING-001`（T3 第二十脉冲）：**修复编码的公式层（复用项层解码器）**——"
    "公式符号层 `bitsF`/`STEPS` 与迭代数精确的流式 `run`（C-177）；`=f` 的 Tm 子项交给项层解析器，"
    "燃料取剩余位数（C-178）；长度对账 `STEPS φ ≤ LEN (bitsF φ)`（C-179）；`codeF' = codeBits ∘ bitsF` 带全解码器 "
    "`decF`、往返 `decF (codeF' φ) ≡ φ`，故单射（C-180）——**Tm 与 Fml 两级编码修复均已闭合** | "
    "`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | "
    "当前工作包（用户目标「全部做完再停下」；第二线 T3） | "
    "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_FORMULA_CODING` | Agda 2.8.0-3d04bac、仅 Agda builtins、"
    "exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；剩余：公式层与对象层替换对齐、`⌜·⌝` 算术化表示、"
    "P 表示性/反射/对角不动点（仍需门 B 消费者） | "
    "只覆盖 `Fml` 的编码/解码与单射性；不宣称公式层替换一致、不构造 P 或对角不动点；"
    "`BitCoding`/`StreamingParser` 与历史脉冲文件逐字节未改；ERCF-3 保持 `GATED` | "
    f"`{DIR_README}`；`{MATRIX}`（追加节）；`{RUN_DIR}/RUN.json`；`{CLOSURE}`（later_packages） |\n"
)

AUDIT_FOCUS = {
    "KC-000021": ("ALIGNED", "按 F-011 完成源码→canonical run→索引→版本登记；kernel exit 0、stderr 0。"),
    "KC-000028": ("DEEPENED", "自反线前置 (a) 的编码缺口在 Tm 与 Fml 两级闭合：对角化真正引用的公式层已有可解码编码。"),
    "KC-000030": ("ALIGNED", "按层推进（Tm → Fml）并把下一义务（替换对齐、⌜·⌝ 算术化）如实登记。"),
    "KC-000036": ("ALIGNED", "编码可解码 ≠ HoTT 自馈；Gödel/自馈仍归门 B，本包不升级为 HoTT 特有结论。"),
    "KC-000025": ("ALIGNED", "自指线仍要求真实连接：本包只交付前置编码层，不构造对角不动点。"),
    "KC-000017": ("ALIGNED", "以 kernel 与源码为据；四条命题都有源码标识与哈希固定的 run（含对既有模块哈希不变的交叉核对）。"),
    "KC-000005": ("ALIGNED", "先固定四条精确命题再交付；范围与禁止外推显式写明。"),
    "KC-000014": ("ALIGNED", "公式层编码闭合 ≠ 对角引理已形式化；禁止外推里逐项写明未做部分。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是修复编码的公式层（复用项层解码器），不产生新的理论结论。",
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
        "- direction_change: YES_IN_PLACE — 方向行原位记录两级编码修复闭合与新的剩余义务。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/006 shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 编码修复按层收口（Tm 由 C-176、Fml 由 C-180）；T3 编码层义务完成，剩余为替换对齐、⌜·⌝ 算术化与门 B 本体。",
        "- cross_conflicts: 无新增冲突；Fml 编码与旧 `codeF` 的边界在禁止外推里写明，且既有模块哈希经两次 run 交叉核对未变。",
        "- unresolved: 公式层与对象层替换（`substF`/`substFix` 系列）对齐、`⌜·⌝` 算术化表示、P 表示性/反射/对角不动点均未做。",
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
    if state.get("revision") != 116 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_116_S116")

    run = json.loads((root / RUN_DIR / "RUN.json").read_text(encoding="utf-8"))
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
        raise SystemExit("RUN_NOT_READY")
    if run.get("claim_ids") != ["C-177", "C-178", "C-179", "C-180"]:
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
                "MP-ERCF3-T3-FORMULA-CODING-001 (C-177-C-180) and its run. Record scope, claims and evidence status unchanged."
            )
            repinned.append(record_id)
    if set(repinned) != EXPECTED_REPIN:
        raise SystemExit(f"EXPECTED_TWO_REPIN:{sorted(repinned)}")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "100"),
        ("PANORAMA", R.PANORAMA, "outcome", "100"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 116", "source_state_revision: 117"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-101",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/003 - LocalGPT 与 WebGPT 方向.md",
        "**下一义务=公式层 `codeF` 的对应修复 + 把 `codeT'`/`dec` 与对象层替换（`substFix` 系列）对齐**；"
        "其后才是证明谓词表示性、反射与对角不动点（仍需门 B 消费者）。",
        "**第四片（修复编码的公式层）亦已机器收口**（`MP-ERCF3-T3-FORMULA-CODING-001` / C-177–C-180："
        "公式符号层与迭代数精确的流式 `run`、`=f` 的 Tm 子项复用项层解析器、长度界 `STEPS φ ≤ LEN (bitsF φ)`、"
        "`codeF'` 带全解码器 `decF` 与往返 ⇒ 单射——**Tm 与 Fml 两级编码修复均已闭合**）。"
        "**下一义务=公式层与对象层替换（`substF`/`substFix` 系列）的对齐 + `⌜·⌝` 的算术化表示**；"
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
        "**下一义务=公式层 `codeF` 的对应修复 + 与对象层替换（`substFix` 系列）对齐**，"
        "其后才是证明谓词表示性、反射与对角不动点。",
        "**第四片（修复编码的公式层）亦已完成**（`MP-ERCF3-T3-FORMULA-CODING-001`，C-177–C-180：公式符号层与"
        "迭代数精确的 `run`、`=f` 的 Tm 子项复用项层解析器、长度界、`codeF'` 带全解码器与往返 ⇒ 单射，"
        "**Tm 与 Fml 两级编码修复均已闭合**）；**下一义务=公式层与对象层替换（`substF`/`substFix` 系列）的对齐 + "
        "`⌜·⌝` 的算术化表示**，其后才是证明谓词表示性、反射与对角不动点。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S117 T3 第二十脉冲：修复编码的公式层（`MP-ERCF3-T3-FORMULA-CODING-001`，C-177–C-180）。"
        "C-177 公式符号层 `bitsF`/`STEPS` 与迭代数精确的流式 `run`（`parse-run`、`index-run`）；"
        "C-178 项层解析器复用 `tmFrom bs = SP.run (LEN bs) bs (SP.startSub SP.ε)` 满足 "
        "`tmFrom (bits t ++ rest) ≡ res t rest`（`tmFrom-run`、`eq-node`、`eqRight-step`）；"
        "C-179 长度对账 `STEPS φ ≤ LEN (bitsF φ)`（`STEPS≤LEN`）；"
        "C-180 `codeF' = codeBits ∘ bitsF` 带全解码器 `decF` 与往返 `decF (codeF' φ) ≡ φ`，故单射"
        "（`codeF'-roundtrip`、`codeF'-injective`）——Tm 与 Fml 两级编码修复闭合。"
        "run `20260913-MP-ERCF3-T3-FORMULA-CODING-001-01`：Agda 2.8.0-3d04bac、仅 builtins、exit 0、stderr 0、"
        "`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；`index-row-manifest.json` 5 行冻结；`later_packages` 第 8 条，"
        "later claims 27→31。剩余：公式层与对象层替换对齐、`⌜·⌝` 算术化、P 表示性/反射/对角不动点。"
        "ERCF-3 保持 `GATED`；`BitCoding`/`StreamingParser` 哈希经 run 交叉核对未变。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row65 = (
        "| 已闭合工作包 65 | T3 符号层 + 流式解析器 + 修复后的 Nat 值编码（S116，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_NAT_CODING` | C-173–C-176：一元索引自定界、"
        "燃料精确的流式 `run`、长度/界/多余燃料分解、`codeT'` 带全解码器与像上往返 ⇒ 单射；"
        "**编码层修复义务（C-163/C-164/C-165）已闭合**；剩余=公式层 `codeF` 修复 + 替换对齐 + P 表示性/反射/对角不动点；"
        "见 `HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |"
    )
    frontier = replace_once(
        frontier,
        row65,
        row65 + "\n| 已闭合工作包 66 | T3 修复编码的公式层（S117，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_FORMULA_CODING` | C-177–C-180：公式符号层与"
        "迭代数精确的 `run`、项层解析器复用、长度界、`codeF'` 带全解码器与往返 ⇒ 单射；"
        "**Tm 与 Fml 两级编码修复均已闭合**；剩余=替换对齐 + `⌜·⌝` 算术化 + P 表示性/反射/对角不动点；"
        "见 `HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |",
    )
    frontier = replace_once(
        frontier,
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | coding-repair-obligation-closed-at-the-coding-layer; "
        "next-obligation-is-the-formula-layer-and-substitution-alignment | "
        "T3 编码/替换一致（C-157–C-159）、可解码性围栏（C-160–C-162）、修复规格（C-163–C-165）与算术半三段"
        "（C-166–C-168、C-169–C-172、C-173–C-176）均已闭合，**编码层修复义务已闭合**；"
        "**下一义务=公式层 `codeF` 的对应修复 + 与对象层替换（`substFix` 系列）对齐**，其后才是 P 表示性、"
        "反射与对角不动点（仍需门 B 消费者）；ERCF-3 本体保持 gated |",
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | coding-repair-closed-at-both-Tm-and-Fml; "
        "next-obligation-is-substitution-alignment-and-quotation-arithmetisation | "
        "T3 编码/替换一致（C-157–C-159）、可解码性围栏（C-160–C-162）、修复规格（C-163–C-165）、算术半三段"
        "（C-166–C-168、C-169–C-172、C-173–C-176）与公式层修复（C-177–C-180）均已闭合；"
        "**下一义务=公式层与对象层替换（`substF`/`substFix` 系列）对齐 + `⌜·⌝` 的算术化表示**，其后才是 P 表示性、"
        "反射与对角不动点（仍需门 B 消费者）；ERCF-3 本体保持 gated |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n96. 换一个数据类型重做同一构造时，最容易卡住的不是数学而是**定义的可归约性**。两条实测教训："
        "（1）**模式参数放最前**：`run` 的第一个参数是 `Mode`（永远是构造子），若把位串放前面，`eqRight` 那一步的位串是"
        "卡住的 `bits u ++ rest`，Agda 就无法在不知道位串构造子的情况下选择子句——连「定义上相等」的等式也证不出来，"
        "把模式提到第一位即可。（2）**命题步骤要写成引理**：`tmFrom (bits t ++ rest) ≡ res t rest` 是命题而非定义上的等同，"
        "直接 `refl` 必然失败（`rewrite` 甚至找不到可改写位置，因为它不会自动展开目标里的 `run`）；把带 `tmFrom …` 的目标"
        "写成独立引理（`tmFrom-run`/`eq-node`/`eqRight-step`），再用 `SP.subst'` 显式搬运燃料与位串，才既可控又可读。"
        "另有两条小坑：`≤` 与 `+` 同默认 fixity，`n ≤ n + m` 会被解析成 `(n ≤ n) + m`，和式要加括号；"
        "登记义务时不要用 `Set` 占位符充数（`BitCoding` 已改用注释形式记录下一义务）。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S117：T3 修复编码的公式层完成（`MP-ERCF3-T3-FORMULA-CODING-001`，C-177–C-180）——公式符号层与迭代数精确的流式 "
        "`run`、`=f` 的 Tm 子项复用项层解析器（燃料取剩余位数）、长度界 `STEPS φ ≤ LEN (bitsF φ)`、"
        "`codeF'` 带全解码器 `decF` 与往返 ⇒ 单射；**Tm 与 Fml 两级编码修复均已闭合**；`later_packages` 第 8 条"
        "（later claims 27→31）。**下一义务=公式层与对象层替换（`substF`/`substFix` 系列）对齐 + `⌜·⌝` 的算术化表示**，"
        "其后才是 P 表示性/反射/对角不动点（仍需门 B 消费者）。ERCF-3 保持 `GATED`；门 A/门 B 状态不变。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目标「全部做完再停下」，第二线 T3 第二十脉冲：修复编码的公式层（复用项层解码器）。
- 交付：`{SOURCE}`；canonical run `{RUN_DIR}`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（5 行冻结）；矩阵追加节（`C-177`–`C-180`）；
  `{CLOSURE}` 的 `later_packages` 第 8 条（later claims 27→31）；`{DIR_README}` / `{FORMAL_README}` /
  `{RUNS_README}` 索引同步（两条 owner record revalidation 重绑）。
- 四条 claim：C-177 公式符号层与迭代数精确的流式 `run`；C-178 项层解析器复用（燃料=剩余位数）；
  C-179 长度对账 `STEPS φ ≤ LEN (bitsF φ)`；C-180 `codeF'` 带全解码器 `decF`、往返 ⇒ 单射。
- 交叉核对：`BitCoding.agda` 与 `StreamingParser.agda` 的哈希在各自注册 run 与本 run 的 `source-manifest.json` 中一致
  （逐字节未改）。
- 边界：只覆盖 `Fml` 的编码/解码与单射性；不做公式层替换对齐、`⌜·⌝` 算术化、P 表示性/反射/对角不动点；
  ERCF-3 保持 `GATED`；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "proof_package": {
                "proof_id": "MP-ERCF3-T3-FORMULA-CODING-001",
                "claim_ids": "C-177–C-180",
                "source": SOURCE,
                "run": RUN_DIR,
                "toolchain": TOOLCHAIN,
                "status": "KERNEL_ACCEPTED_WITH_SCOPE",
                "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
                "verdict": "ERCF3_T3_REPAIRED_FORMULA_CODING",
            },
            "closure_registry": {"later_packages": 8, "later_machine_proved_claims": 31},
            "repinned_records": sorted(repinned),
            "new_math_claims": ["C-177", "C-178", "C-179", "C-180"],
            "cross_checked_unchanged_modules": ["HoTT/formal/ercf3-t3/BitCoding.agda", "HoTT/formal/ercf3-t3/StreamingParser.agda"],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 117
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_ERCF3_T3_FORMULA_CODING",
            "status": STATUS,
            "next_minimal_verification": (
                "Second line (T3): the repaired coding now exists at both levels (Tm by C-176, Fml by C-180) with total "
                "decoders and round trips, hence injectivity. Next bounded obligation: align the formula layer with "
                "object-level substitution (the `substF`/`substFix` family) and arithmetise the quotation `⌜·⌝` over the "
                "repaired coding. After that: proof-predicate representability, reflection and the diagonal fixed point, "
                "which still need the door-B consumer. ERCF-3 stays GATED. First line (two doors) unchanged."
            ),
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-101", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-101", "semantic_status": STATUS}
    )
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-ERCF3-T3-STREAMING-PARSER-001", "A-ERCF3-T3-REPAIR-SPEC-001"],
        "full_sources": [SOURCE, DIR_README, f"{RUN_DIR}/RUN.json", MATRIX, CLOSURE, TOOLCHAIN],
        "source_hashes": {
            SOURCE: R.sha((root / SOURCE).read_bytes()),
            f"{RUN_DIR}/RUN.json": R.sha((root / RUN_DIR / "RUN.json").read_bytes()),
            MATRIX: R.sha((root / MATRIX).read_bytes()),
            CLOSURE: R.sha((root / CLOSURE).read_bytes()),
        },
        "scope": (
            "MP-ERCF3-T3-FORMULA-CODING-001 (C-177-C-180): the formula layer of the coding repair, reusing the term-level "
            "parser as a black box. The formula symbol layer with a streaming parser whose round trip is exact in the "
            "iteration count; the Tm children of `=f` parsed by the term-level parser with fuel = remaining bit length; the "
            "length bound STEPS <= LEN (bitsF); and codeF' = codeBits . bitsF with a total decoder decF and round trip "
            "decF (codeF' phi) = phi, hence injectivity. Formula-layer substitution alignment, quotation arithmetisation, "
            "proof-predicate representability, reflection and the diagonal fixed point remain open; ERCF-3 remains gated."
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
            "Registration of MP-ERCF3-T3-FORMULA-CODING-001: canonical run, matrix append section, closure later_packages "
            "entry, index updates, two owner record revalidations and the cross-check that BitCoding/StreamingParser are "
            "byte-identical to their own registration runs. ERCF-3 remains gated."
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
            "Active goal 'finish everything before stopping'. Next self-contained obligation: the formula layer of the "
            "coding repair (reusing the term-level parser), completing a decodable Nat coding for Fml. No new theoretical "
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
                "revision": 117,
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
