#!/usr/bin/env python3
"""Prepare revision 115: register MP-ERCF3-T3-BIT-CODING-001 (arithmetic half, second piece)."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-115-ERCF3-T3-BIT-CODING"
PREV = "S-RES-20260913-114-ERCF3-T3-ARITH-TAGS"
RESULT_ID = "A-ERCF3-T3-BIT-CODING-001"
OUTCOME_ID = "OUT-TOP-ERCF3-T3-BIT-CODING"
SOURCE = "HoTT/formal/ercf3-t3/BitCoding.agda"
DIR_README = "HoTT/formal/ercf3-t3/README.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
RUN_DIR = "HoTT/verification/runs/20260913-MP-ERCF3-T3-BIT-CODING-001-01"
TOOLCHAIN = "HoTT/formal/ercf3-t3/TOOLCHAIN.json"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
CLOSURE = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
EXPECTED_REPIN = {"A-MATH-PROOF-DELIVERY-GATE-001", "S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"}

SPEC = importlib.util.spec_from_file_location("runtime_s115", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | `MP-ERCF3-T3-BIT-CODING-001`（T3 第十八脉冲）：修复编码的**算术半第二片（位级底座）**——"
    "最低位/折半数字算术（`parity`/`half`/`twice`，C-169）；捆绑编码 `codeBits` 与抽取 `unbits` 的两侧引理（C-170）"
    "与**已知长度**的往返 `unbits (LEN bs) (codeBits bs) ≡ bs`（C-171）；码支配自身长度 "
    "`suc (LEN bs) ≤ codeBits bs`，故解析器燃料可取自码本身（C-172） | "
    "`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | "
    "当前工作包（用户目标「全部做完再停下」；第二线 T3） | "
    "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_BIT_SUBSTRATE` | Agda 2.8.0-3d04bac、仅 Agda builtins、"
    "exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；剩余：符号层（自定界索引位 + 构造子标签）+ 解析器 + 像上往返 | "
    "只覆盖位列表编解码与长度界；不给出符号层/解析器/全解码器；往返只在已知长度上成立；"
    "不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED` | "
    f"`{DIR_README}`；`{MATRIX}`（追加节）；`{RUN_DIR}/RUN.json`；`{CLOSURE}`（later_packages） |\n"
)

AUDIT_FOCUS = {
    "KC-000021": ("ALIGNED", "按 F-011 完成源码→canonical run→索引→版本登记；kernel exit 0、stderr 0。"),
    "KC-000028": ("DEEPENED", "自反线前置 (a) 的算术半继续落地：位级底座与燃料界已机器化，解析器可只凭码工作。"),
    "KC-000030": ("ALIGNED", "把算术半继续拆成有界义务（位级底座 → 符号层/解析器），如实登记未完成部分。"),
    "KC-000036": ("ALIGNED", "Gödel/自馈仍归门 B；本包不升级为 HoTT 特有结论。"),
    "KC-000025": ("ALIGNED", "自指线仍要求真实连接：本包只交付前置算术片。"),
    "KC-000017": ("ALIGNED", "以 kernel 与源码为据；每条命题都有源码标识与哈希固定的 run。"),
    "KC-000005": ("ALIGNED", "先固定四条精确命题再交付；范围与禁止外推显式写明。"),
    "KC-000014": ("ALIGNED", "位级底座完成 ≠ 算术半完成；义务边界在包与方向行里显式保留。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是修复编码的算术半第二片（位级底座与燃料界），不产生新的理论结论。",
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
        "- direction_change: YES_IN_PLACE — 方向行原位记录位级底座完成与剩余义务（符号层/解析器）。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/006 shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 算术半按“位级底座（含燃料界）→ 符号层/解析器 → 像上往返”推进；本包完成第一段。",
        "- cross_conflicts: 无新增冲突；位级结果与完整 Tm 编码的差距在禁止外推里写明。",
        "- unresolved: 符号层（自定界索引位与构造子标签）、带缺省分支的解析器、像上往返均未做；P 表示性/反射/对角不动点未做。",
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
    if state.get("revision") != 114 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_114_S114")

    run = json.loads((root / RUN_DIR / "RUN.json").read_text(encoding="utf-8"))
    if run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX":
        raise SystemExit("RUN_NOT_READY")
    if run.get("claim_ids") != ["C-169", "C-170", "C-171", "C-172"]:
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
                "MP-ERCF3-T3-BIT-CODING-001 (C-169-C-172) and its run. Record scope, claims and evidence status unchanged."
            )
            repinned.append(record_id)
    if set(repinned) != EXPECTED_REPIN:
        raise SystemExit(f"EXPECTED_TWO_REPIN:{sorted(repinned)}")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "098"),
        ("PANORAMA", R.PANORAMA, "outcome", "098"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 114", "source_state_revision: 115"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-099",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/003 - LocalGPT 与 WebGPT 方向.md",
        "**算术半第一片已机器收口**（`MP-ERCF3-T3-ARITH-TAGS-001` / C-166–C-168：`double` 单射、"
        "`double n ≢ odd m`、var/num 片段 Nat 值编码 `codeAtom`（`2n`/`2n+1`）单射、编码非满射故全解码器需缺省分支）。"
        "**下一义务=应用结点配对 + 带缺省分支的全解码器 + 像上往返**；",
        "**算术半第一片已机器收口**（`MP-ERCF3-T3-ARITH-TAGS-001` / C-166–C-168：`double` 单射、"
        "`double n ≢ odd m`、var/num 片段 Nat 值编码 `codeAtom`（`2n`/`2n+1`）单射、编码非满射故全解码器需缺省分支），"
        "**第二片（位级底座与燃料界）亦已机器收口**（`MP-ERCF3-T3-BIT-CODING-001` / C-169–C-172：最低位/折半数字算术、"
        "`codeBits`/`unbits` 两侧引理与已知长度往返、码支配自身长度 `suc (LEN bs) ≤ codeBits bs`）。"
        "**下一义务=符号层（自定界索引位 + 构造子标签）+ 带缺省分支的解析器 + 像上往返**；",
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
        "**算术半第一片已完成**（`MP-ERCF3-T3-ARITH-TAGS-001`，C-166–C-168：偶/奇标签算术、"
        "var/num 片段 Nat 值单射编码、非满射控制）；**下一义务=应用结点配对 + 带缺省分支的全解码器 + 像上往返**，",
        "**算术半第一片已完成**（`MP-ERCF3-T3-ARITH-TAGS-001`，C-166–C-168），**第二片（位级底座与燃料界）亦已完成**"
        "（`MP-ERCF3-T3-BIT-CODING-001`，C-169–C-172：最低位/折半数字算术、`codeBits`/`unbits` 两侧引理与已知长度往返、"
        "码支配自身长度 `suc (LEN bs) ≤ codeBits bs`）；**下一义务=符号层（自定界索引位 + 构造子标签）+ 带缺省分支的解析器 + 像上往返**，",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S115 T3 第十八脉冲：修复编码的算术半第二片（`MP-ERCF3-T3-BIT-CODING-001`，C-169–C-172）。"
        "C-169 数字算术：`parity (twice n) ≡ false`、`parity (suc (twice n)) ≡ true`、`half (twice n) ≡ n`、"
        "`half (suc (twice n)) ≡ n`；C-170 捆绑/抽取两侧引理 `parity (pack b c) ≡ b`、`half (pack b c) ≡ c`，"
        "`codeBits [] ≡ 1`、`codeBits (b ∷ bs) ≡ pack b (codeBits bs)`；C-171 **已知长度**往返 "
        "`unbits (LEN bs) (codeBits bs) ≡ bs`；C-172 码支配自身长度 `suc (LEN bs) ≤ codeBits bs`（解析器燃料可取自码本身）。"
        "run `20260913-MP-ERCF3-T3-BIT-CODING-001-01`：Agda 2.8.0-3d04bac、仅 builtins、exit 0、stderr 0、"
        "`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；`index-row-manifest.json` 5 行冻结；`later_packages` 第 6 条，"
        "later claims 20→23。剩余：符号层（自定界索引位与构造子标签）+ 带缺省分支的解析器 + 像上往返。"
        "ERCF-3 保持 `GATED`；未新增理论结论。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row63 = (
        "| 已闭合工作包 63 | T3 算术半第一片（S114，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_ARITHMETIC_TAGS_FRAGMENT` | C-166–C-168：偶/奇标签算术、"
        "var/num 片段 Nat 值编码（`2n`/`2n+1`）单射、非满射控制；**下一义务=应用结点配对 + 全解码器 + 像上往返**；"
        "见 `HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |"
    )
    frontier = replace_once(
        frontier,
        row63,
        row63 + "\n| 已闭合工作包 64 | T3 算术半第二片：位级底座与燃料界（S115，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_BIT_SUBSTRATE` | C-169–C-172：最低位/折半数字算术、"
        "`codeBits`/`unbits` 两侧引理与已知长度往返、码支配自身长度；**下一义务=符号层（自定界索引位 + 构造子标签）"
        "+ 带缺省分支的解析器 + 像上往返**；见 `HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |",
    )
    frontier = replace_once(
        frontier,
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | arithmetic-half-first-piece-closed; "
        "next-obligation-is-the-application-node-and-total-decoder | "
        "T3 编码/替换一致（C-157–C-159）、可解码性围栏（C-160–C-162）、修复规格（C-163–C-165）与算术半第一片"
        "（C-166–C-168）均已闭合；**下一义务=应用结点配对 + 带缺省分支的全解码器 + 像上往返**，其后才是 P 表示性、"
        "反射与对角不动点；ERCF-3 本体保持 gated |",
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | arithmetic-half-bit-substrate-closed; "
        "next-obligation-is-the-symbol-layer-and-the-parser | "
        "T3 编码/替换一致（C-157–C-159）、可解码性围栏（C-160–C-162）、修复规格（C-163–C-165）、算术半第一片"
        "（C-166–C-168）与第二片位级底座（C-169–C-172）均已闭合；**下一义务=符号层（自定界索引位 + 构造子标签）"
        "+ 带缺省分支的解析器 + 像上往返**，其后才是 P 表示性、反射与对角不动点；ERCF-3 本体保持 gated |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n94. 位级底座要按“数字算术 → 打包/抽取互逆 → 燃料界”一次做完整，别把界留成口号：本轮只做最低位/折半"
        "（`parity`/`half`/`twice`）就同时拿到了 C-170 的两侧引理，但**已知长度的往返**（C-171）仍不足以让解析器"
        "只凭码工作——真正让“燃料取自码本身”落地的是 C-172 的 `suc (LEN bs) ≤ codeBits bs`。"
        "两条经验：`double` 的单射/偶奇互斥这类引理用构造子冲突即可，不必引入模算术；而界证明的每一步"
        "（`≤-trans`、`n≤twice`、`suc≤pack`）都必须显式写出来，空缺处用 `Set` 占位符充数只会把义务藏起来。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S115：T3 算术半第二片完成（`MP-ERCF3-T3-BIT-CODING-001`，C-169–C-172）——最低位/折半数字算术、"
        "`codeBits`/`unbits` 两侧引理与已知长度往返、码支配自身长度（燃料可取自码本身）；`later_packages` 第 6 条"
        "（later claims 20→23）。**下一义务=符号层（自定界索引位 + 构造子标签）+ 带缺省分支的解析器 + 像上往返**。"
        "ERCF-3 保持 `GATED`；门 A/门 B 状态不变。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目标「全部做完再停下」，第二线 T3 第十八脉冲：修复编码的算术半第二片（位级底座与燃料界）。
- 交付：`{SOURCE}`；canonical run `{RUN_DIR}`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（5 行冻结）；矩阵追加节（`C-169`–`C-172`）；
  `{CLOSURE}` 的 `later_packages` 第 6 条（later claims 20→23）；`{DIR_README}` / `{FORMAL_README}` /
  `{RUNS_README}` 索引同步（两条 owner record revalidation 重绑）。
- 四条 claim：C-169 数字算术（`parity`/`half`/`twice`）；C-170 `codeBits`/`unbits` 两侧引理；
  C-171 已知长度往返 `unbits (LEN bs) (codeBits bs) ≡ bs`；C-172 码支配自身长度 `suc (LEN bs) ≤ codeBits bs`。
- 边界：只覆盖位列表编解码与长度界；符号层、解析器与全解码器未做；往返只在已知长度上成立；
  不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`；不改写历史脉冲文件；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "proof_package": {
                "proof_id": "MP-ERCF3-T3-BIT-CODING-001",
                "claim_ids": "C-169–C-172",
                "source": SOURCE,
                "run": RUN_DIR,
                "toolchain": TOOLCHAIN,
                "status": "KERNEL_ACCEPTED_WITH_SCOPE",
                "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
                "verdict": "ERCF3_T3_BIT_SUBSTRATE",
            },
            "closure_registry": {"later_packages": 6, "later_machine_proved_claims": 23},
            "repinned_records": sorted(repinned),
            "new_math_claims": ["C-169", "C-170", "C-171", "C-172"],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 115
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_ERCF3_T3_BIT_CODING",
            "status": STATUS,
            "next_minimal_verification": (
                "Second line (T3), next bounded pulse: the symbol layer (self-delimiting var/num index bits plus the "
                "constructor tags) and the parser with its default branch (C-168), then the round-trip on the image -- which "
                "by C-164 yields injectivity of the full Nat-valued coder `t |-> codeBits (bits t)`. Then resume "
                "proof-predicate representability, reflection and the diagonal fixed point. ERCF-3 stays GATED. First line "
                "(two doors) unchanged."
            ),
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-099", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-099", "semantic_status": STATUS}
    )
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-ERCF3-T3-ARITH-TAGS-001", "A-ERCF3-T3-REPAIR-SPEC-001"],
        "full_sources": [SOURCE, DIR_README, f"{RUN_DIR}/RUN.json", MATRIX, CLOSURE, TOOLCHAIN],
        "source_hashes": {
            SOURCE: R.sha((root / SOURCE).read_bytes()),
            f"{RUN_DIR}/RUN.json": R.sha((root / RUN_DIR / "RUN.json").read_bytes()),
            MATRIX: R.sha((root / MATRIX).read_bytes()),
            CLOSURE: R.sha((root / CLOSURE).read_bytes()),
        },
        "scope": (
            "MP-ERCF3-T3-BIT-CODING-001 (C-169-C-172): the bit-level substrate of the arithmetic half of the coding repair. "
            "C-169 digit arithmetic (parity/half/twice); C-170 the bundling/extraction lemma pair for codeBits/unbits; C-171 "
            "the round-trip on a bit list whose length is supplied; C-172 the code dominates its own length, so a future "
            "parser can take its fuel from the code itself. Remaining: the symbol layer (self-delimiting index bits and "
            "constructor tags), the parser with its default branch, and the round-trip on the image. ERCF-3 remains gated."
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
            "Registration of MP-ERCF3-T3-BIT-CODING-001: canonical run, matrix append section, closure later_packages "
            "entry, index updates and two owner record revalidations. ERCF-3 remains gated."
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
            "Active goal 'finish everything before stopping'. Next self-contained obligation: the arithmetic half of the "
            "coding repair, second piece -- the bit-level substrate and the fuel bound. No new theoretical claim, no push."
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
                "revision": 115,
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
