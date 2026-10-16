#!/usr/bin/env python3
"""Prepare revision 113: register MP-ERCF3-T3-REPAIR-SPEC-001 (coding repair specification)."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-RES-20260913-113-ERCF3-T3-REPAIR-SPEC"
PREV = "S-RES-20260913-112-ERCF3-T3-DECODING"
RESULT_ID = "A-ERCF3-T3-REPAIR-SPEC-001"
OUTCOME_ID = "OUT-TOP-ERCF3-T3-REPAIR-SPECIFICATION"
SOURCE = "HoTT/formal/ercf3-t3/CodingRepair.agda"
DIR_README = "HoTT/formal/ercf3-t3/README.md"
FORMAL_README = "HoTT/formal/README.md"
RUNS_README = "HoTT/verification/runs/README.md"
RUN_DIR = "HoTT/verification/runs/20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01"
TOOLCHAIN = "HoTT/formal/ercf3-t3/TOOLCHAIN.json"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
CLOSURE = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
EXPECTED_REPIN = {"A-MATH-PROOF-DELIVERY-GATE-001", "S-GOV-20260912-032-ERCF-TRUNCATION-FINAL-ALIGNMENT"}

SPEC = importlib.util.spec_from_file_location("runtime_s113", RUNTIME_PATH)
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
    f"| `{OUTCOME_ID}` | `MP-ERCF3-T3-REPAIR-SPEC-001`（T3 第十六脉冲）：把“修复编码”固定为规格——"
    "通用引理“有往返解码器 ⇒ 编码单射”（C-164）；结构化树编码 `encT/decT` 往返成立故单射（C-163，正控制）；"
    "当前 `codeT` **不存在解码器**（C-165） | `DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、"
    "`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前工作包（用户目标「全部做完再停下」；第二线 T3） | "
    "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIR_SPECIFICATION` | Agda 2.8.0-3d04bac、仅 Agda builtins、"
    "exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；修复义务=“Nat 值编码 + 解码器 + 往返证明”，"
    "结构半已完成、**算术半（标签不相交或列表编码）待下一个有界脉冲** | "
    "不给 Nat 值修复编码本身；不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`；历史脉冲文件不改写 | "
    f"`{DIR_README}`；`{MATRIX}`（追加节）；`{RUN_DIR}/RUN.json`；`{CLOSURE}`（later_packages） |\n"
)

AUDIT_FOCUS = {
    "KC-000021": ("ALIGNED", "按 F-011 完成源码→canonical run→索引→版本登记；kernel exit 0、stderr 0。"),
    "KC-000028": ("DEEPENED", "自反线前置 (a) 的“编码可解码”义务被写成可机器检查规格，并给出精确剩余义务。"),
    "KC-000030": ("ALIGNED", "把“修复编码”的成本（需要 Nat 算术/配对或列表编码）如实登记，不假装已完成。"),
    "KC-000036": ("ALIGNED", "Gödel/自馈仍归门 B；本包不升级为 HoTT 特有结论。"),
    "KC-000025": ("ALIGNED", "自指线仍要求真实连接：本包只交付前置规格与正控制。"),
    "KC-000017": ("ALIGNED", "以 kernel 与源码为据；规格引理与正控制都机器检查。"),
    "KC-000005": ("ALIGNED", "先固定精确命题（三条）再交付；否证有界、正控制明确。"),
    "KC-000014": ("ALIGNED", "“未完成 vs 已取得”的区分在编码层被严格执行：结构半完成不等于修复完成。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是 T3 编码修复规格（含精确剩余义务），不产生新的理论结论。",
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
        "- direction_change: YES_IN_PLACE — 方向行原位记录“修复规格已定、算术半待做”。",
        f"- panorama_change: YES — 新增 `{OUTCOME_ID}` 结果行（写入 全景视野/006 shard）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: 修复义务固定为“Nat 值编码 + 解码器 + 往返证明”；结构半完成（C-163），算术半进入下一有界脉冲。",
        "- cross_conflicts: 无新增冲突；`GATED` 状态与“前置义务推进”分层清楚。",
        "- unresolved: Nat 值修复编码（含配对/列表编码与算术引理）未做；P 表示性/反射/对角不动点未做。",
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
    if state.get("revision") != 112 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_112_S112")

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
                "MP-ERCF3-T3-REPAIR-SPEC-001 (C-163-C-165) and its run. Record scope, claims and evidence status unchanged."
            )
            repinned.append(record_id)
    if set(repinned) != EXPECTED_REPIN:
        raise SystemExit(f"EXPECTED_TWO_REPIN:{sorted(repinned)}")

    projections = {}
    for key, rel, gen, old_gen in (
        ("DIRECTION", R.DIRECTION, "direction", "096"),
        ("PANORAMA", R.PANORAMA, "outcome", "096"),
    ):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(
            doc, "source_state_revision: 112", "source_state_revision: 113"
        )
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-097",
        )
        projections[key] = doc

    projection_edit.replace_in_shard(
        projections["DIRECTION"],
        "方向追踪/003 - LocalGPT 与 WebGPT 方向.md",
        "T3 的**编码/替换一致义务**（`MP-ERCF3-T3-JOINT-001` / C-157–C-159）与**可解码性围栏**"
        "（`MP-ERCF3-T3-DECODING-001` / C-160–C-162：当前编码非单射、需标签不相交或列表编码修复）均已机器收口；"
        "**下一义务是给出修复后的编码并证明其单射性**，之后才是证明谓词表示性、反射与对角不动点。ERCF-3 本体保持 `GATED`，"
        "仍预测为 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，不把一般 Gödel 口号冒充 HoTT 实例",
        "T3 的**编码/替换一致**（C-157–C-159）、**可解码性围栏**（C-160–C-162）与**修复规格**"
        "（`MP-ERCF3-T3-REPAIR-SPEC-001` / C-163–C-165：往返 ⇒ 单射的通用引理；树编码正控制；当前 `codeT` 无解码器）"
        "均已机器收口；**下一义务=算术半**：给出 Nat 值编码 `codeT'` 与解码 `dec'` 并证明往返（需配对/列表编码与算术引理）。"
        "其后才是证明谓词表示性、反射与对角不动点。ERCF-3 本体保持 `GATED`，仍预测为 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，"
        "不把一般 Gödel 口号冒充 HoTT 实例",
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
        "下一义务=给出修复后的编码并证明其单射性，之后才是证明谓词表示性、"
        "反射与对角不动点。ERCF-3 本体保持 `GATED`；没有自然自验证 consumer 时保持 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，"
        "不冒充 HoTT 悖论。",
        "修复规格已定（`MP-ERCF3-T3-REPAIR-SPEC-001`，C-163–C-165：往返 ⇒ 单射的通用引理、树编码正控制、"
        "当前 `codeT` 无解码器）；**下一义务=算术半**——给出 Nat 值编码 `codeT'` 与解码 `dec'` 并证明往返"
        "（需配对/列表编码与算术引理），其后才是证明谓词表示性、反射与对角不动点。ERCF-3 本体保持 `GATED`；"
        "没有自然自验证 consumer 时保持 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，不冒充 HoTT 悖论。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S113 T3 第十六脉冲：编码修复规格（`MP-ERCF3-T3-REPAIR-SPEC-001`，C-163–C-165）。"
        "C-164 通用引理：任意目标类型上有往返解码器 ⇒ 编码单射（`roundtrip-implies-injective`）；C-163 正控制："
        "结构化树编码 `encT/decT` 往返成立故单射（`encT-roundtrip`/`encT-injective`）；C-165 精确否证：当前 `codeT` "
        "不存在解码器（`no-decoder-for-codeT`，由 C-164 与 `DecodingFence.no-injective-codeT` 合取）。run "
        "`20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01`：Agda 2.8.0-3d04bac、仅 builtins、exit 0、stderr 0、"
        "`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；`index-row-manifest.json` 4 行冻结；`later_packages` 第 4 条，"
        "later claims 14→17。修复义务被固定为“Nat 值编码 + 解码器 + 往返证明”：**结构半完成**，"
        "**算术半（标签不相交或列表编码 + 算术引理）是下一有界脉冲**。ERCF-3 保持 `GATED`；未新增理论结论。\n",
    )

    essay = projection_edit.load(root, R.ESSAY)

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    row61 = (
        "| 已闭合工作包 61 | T3 编码可解码性围栏（S112，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_DECODABILITY_FENCE` | C-160–C-162：`codeT`/`codeF` 非单射"
        "（`var 2` 与 `num 0` 碰撞）、无单射解码器、数字片段正控制；结论是当前编码不满足 `ObjectSyntax` 记录的 "
        "decodability/injectivity 义务，需标签不相交/列表编码修复（下一有界脉冲）；见 "
        "`HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |"
    )
    frontier = replace_once(
        frontier,
        row61,
        row61 + "\n| 已闭合工作包 62 | T3 编码修复规格（S113，第二线） | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIR_SPECIFICATION` | C-163–C-165：往返 ⇒ 单射的通用引理、"
        "结构化树编码正控制、当前 `codeT` 无解码器的精确否证；修复义务固定为“Nat 值编码 + 解码器 + 往返证明”，"
        "**算术半（配对/列表编码 + 算术引理）为下一有界脉冲**；见 `HoTT/formal/ercf3-t3/README.md` 与矩阵追加节 |",
    )
    frontier = replace_once(
        frontier,
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | decodability-fence-closed; "
        "next-obligation-is-a-repaired-injective-coding | "
        "T3 编码/替换一致（C-157–C-159）与可解码性围栏（C-160–C-162）已闭合；**下一义务=修复编码（标签不相交或列表编码）"
        "并证明其单射性**，其后才是 P 表示性、反射与对角不动点；ERCF-3 本体保持 gated，只有资格提升桥梁成立才构造 diagonal |",
        "| 战略自反深化 | ERCF-3 × W51/RP-B01 | repair-specification-closed; "
        "next-obligation-is-the-arithmetic-half-of-the-repaired-coding | "
        "T3 编码/替换一致（C-157–C-159）、可解码性围栏（C-160–C-162）与修复规格（C-163–C-165）均已闭合；"
        "**下一义务=算术半：Nat 值编码 + 解码器 + 往返证明（配对/列表编码与算术引理）**，其后才是 P 表示性、"
        "反射与对角不动点；ERCF-3 本体保持 gated |",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n92. 说“要修编码”之前，先把修复写成**可检查的规格**：`(c : Tm → A) (dec : A → Tm) → (∀ t → dec (c t) ≡ t) "
        "→ c 单射`。这条通用引理把“修复”与“单射性”绑在一起（C-164），于是“当前编码没有解码器”（C-165）就等于"
        "“当前编码不能作为修复”，而结构化树编码的往返（C-163）给出正控制。剩下的是明确的算术半：Nat 值编码需要"
        "标签不相交或列表/配对编码加算术引理——按义务边界分批，而不是一句“需要修编码”就换题。\n"
    )

    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"),
        "## 当前停止点\n",
        "## 当前停止点\n"
        "S113：T3 编码修复规格完成（`MP-ERCF3-T3-REPAIR-SPEC-001`，C-163–C-165）——往返 ⇒ 单射的通用引理、"
        "结构化树编码正控制、当前 `codeT` 无解码器的精确否证；`later_packages` 第 4 条（later claims 14→17）。"
        "**下一义务=算术半**：给出 Nat 值编码与解码器并证明往返（配对/列表编码 + 算术引理）。ERCF-3 保持 `GATED`；"
        "门 A/门 B 状态不变。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目标「全部做完再停下」，第二线 T3 第十六脉冲：编码修复规格。
- 交付：`{SOURCE}`；canonical run `{RUN_DIR}`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
  `INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`；矩阵追加节（`C-163`–`C-165`）；
  `{CLOSURE}` 的 `later_packages` 第 4 条（later claims 14→17）；`{DIR_README}` / `{FORMAL_README}` /
  `{RUNS_README}` 索引同步（两条 owner record revalidation 重绑）。
- 三条 claim：C-163 结构化树编码往返 ⇒ 单射（正控制）；C-164 往返 ⇒ 单射的通用规格引理；C-165 当前 `codeT` 无解码器。
- 结论：修复义务固定为“Nat 值编码 + 解码器 + 往返证明”；**结构半完成、算术半待做**（配对/列表编码 + 算术引理）。
- 边界：不给 Nat 值修复编码本身；不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`；不改写历史脉冲文件；不 push。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "proof_package": {
                "proof_id": "MP-ERCF3-T3-REPAIR-SPEC-001",
                "claim_ids": "C-163–C-165",
                "source": SOURCE,
                "run": RUN_DIR,
                "toolchain": TOOLCHAIN,
                "status": "KERNEL_ACCEPTED_WITH_SCOPE",
                "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
                "verdict": "ERCF3_T3_REPAIR_SPECIFICATION",
            },
            "closure_registry": {"later_packages": 4, "later_machine_proved_claims": 17},
            "repinned_records": sorted(repinned),
            "new_math_claims": ["C-163", "C-164", "C-165"],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 113
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_ERCF3_T3_REPAIR_SPEC",
            "status": STATUS,
            "next_minimal_verification": (
                "Second line (T3), next bounded pulse: the arithmetic half of the repaired coding — provide a Nat-valued "
                "coder codeT' with a decoder dec' and a round-trip proof (e.g. disjoint tag ranges 3n / 3n+1 / 3*pair+2 with a "
                "pairing function, or a list-based encoding), which by C-164 is automatically injective; then resume "
                "proof-predicate representability, reflection and the diagonal fixed point. ERCF-3 stays GATED. First line "
                "(two doors) unchanged."
            ),
        }
    )
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-097", "semantic_status": STATUS}
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-097", "semantic_status": STATUS}
    )
    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": SOURCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-ERCF3-T3-DECODING-001", "A-ERCF3-T3-JOINT-001"],
        "full_sources": [SOURCE, DIR_README, f"{RUN_DIR}/RUN.json", MATRIX, CLOSURE, TOOLCHAIN],
        "source_hashes": {
            SOURCE: R.sha((root / SOURCE).read_bytes()),
            f"{RUN_DIR}/RUN.json": R.sha((root / RUN_DIR / "RUN.json").read_bytes()),
            MATRIX: R.sha((root / MATRIX).read_bytes()),
            CLOSURE: R.sha((root / CLOSURE).read_bytes()),
        },
        "scope": (
            "MP-ERCF3-T3-REPAIR-SPEC-001 (C-163-C-165): the coding-repair specification. C-164 any coder with a round-trip "
            "decoder is injective; C-163 the structured tree coding encT/decT has a round-trip and is therefore injective "
            "(positive control); C-165 the current Nat coding admits no decoder. The repair obligation is therefore fixed as "
            "'Nat-valued coder + decoder + round-trip proof': the structural half is done, the arithmetic half (disjoint tag "
            "ranges or list encoding plus arithmetic lemmas) is the next bounded pulse. ERCF-3 remains gated."
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
            "Registration of MP-ERCF3-T3-REPAIR-SPEC-001: canonical run, matrix append section, closure later_packages "
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
            "Active goal 'finish everything before stopping'. Next self-contained obligation: turn 'repair the coding' into a "
            "machine-checked specification (round-trip ⇒ injectivity), with the structured coding as positive control and the "
            "precise no-decoder statement for the current coding. No new theoretical claim, no push."
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
                "revision": 113,
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
