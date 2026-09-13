#!/usr/bin/env python3
"""Prepare revision 124: absorb the independent audit of the 统观 technical report."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"

SESSION_ID = "S-GOV-20260913-124-INDEPENDENT-AUDIT-ABSORPTION"
PREV = "S-GOV-20260913-123-PROJECTION-REVISION-REPAIR-3"
RESULT_ID = "A-INDEPENDENT-AUDIT-ABSORPTION-001"
REPORT = "audit/统观工作技术报告-20260913.md"
ABSORPTION = "audit/独立审计吸收与独立核验-20260913.md"
IMPORT_DIR = "audit/imports/audit-c168-20260913"
COUNTERCHECK_RUN = "HoTT/verification/runs/20260913-MP-ERCF3-T3-C168-COUNTERCHECK-001-01"
IMAGE_RUN = "HoTT/verification/runs/20260913-MP-ERCF3-T3-CODING-IMAGE-001-01"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s124", RUNTIME_PATH)
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


AUDIT_FOCUS = {
    "KC-000021": ("ALIGNED", "F1/F2/F6/F7 全部以机器证据复核并修复；F3/F4/F5 按降级/登记处理。"),
    "KC-000017": ("ALIGNED", "吸收过程：逐字节导入 → 逐项独立核验 → 原位修正 → 新事务重绑，全部留证。"),
    "KC-000005": ("ALIGNED", "撤回 C-168 的越界叙述并补上真正成立的依据（C-186/C-187），不保留未证叙述。"),
    "KC-000014": ("TENSION", "F4 指出 S109 的 KC-000014/000015 评估与原文范围不符；历史回评保留，当前以本轮记录为准。"),
    "KC-000015": ("TENSION", "同上：把 B 方向归入门 B 的范围过窄，已恢复 C11 v2 自列未落账轴的资格。"),
    "KC-000030": ("ALIGNED", "F3 后把「收口」降级为暂选路线，并在 MEMORY/方向/报告三处原位修正。"),
    "KC-000036": ("ALIGNED", "审计未改变 T3 的 GENERIC_BOUNDARY 定性；新 claim 仍属通用编码事实。"),
}


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；"
        "本单元是**独立审计吸收**（7 条发现 + 两条机器重放），不产生新的理论结论。",
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
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{ABSORPTION}`；{kid} | 数学开放项不变。 |"
        )
    aligned = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "ALIGNED")
    tension = sum(1 for v in AUDIT_FOCUS.values() if v[0] == "TENSION")
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户原文。",
        "- direction_change: YES_IN_PLACE — `方向追踪/005` 第 4 条改为 v2 语义并恢复未落账轴资格。",
        "- panorama_change: YES — 新增独立审计吸收的更正行（全景视野/006）。",
        "- essay_change: NO — 常驻第四件未改动。",
        "- update_decision: F1/F2 以新机器证据闭合；F3/F4/F5 降级并原位修正；F6/F7 登记为结构缺口由 verifier 机械执行。",
        "- cross_conflicts: S109 的 KC-000014/000015 评估与本轮修正冲突 ⇒ 标 TENSION，历史回评保留、当前以本轮为准。",
        "- unresolved: F3 的广义否定未证；C11 v2 自列未落账轴尚未开工；triage 队列开放；T3 剩余义务仍需门 B。",
        "",
        "## 汇总",
        "",
        f"`ALIGNED={aligned}`；`TENSION={tension}`；其余 `NOT_TOUCHED`；无 `DEVIATED`。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 123 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_123_S123")
    for rel in (ABSORPTION, f"{IMPORT_DIR}/IMPORT.json", f"{COUNTERCHECK_RUN}/RUN.json", f"{IMAGE_RUN}/RUN.json"):
        if not (root / rel).is_file():
            raise SystemExit(f"MISSING:{rel}")

    direction = projection_edit.load(root, R.DIRECTION)
    projection_edit.replace_in_shard(
        direction,
        "方向追踪/003 - LocalGPT 与 WebGPT 方向.md",
        "var/num 片段 Nat 值编码 `codeAtom`（`2n`/`2n+1`）单射、编码非满射故全解码器需缺省分支）",
        "var/num 片段 Nat 值编码 `codeAtom`（`2n`/`2n+1`）单射；**2026-09-13 独立审计 F1 更正**：C-168 的"
        "「`1` 无原像」引理谈的是 `double`，`codeAtom` 实际**满射**（C-184–C-185），修复后 `codeT'`/`codeF'` 的"
        "缺省分支由 C-186–C-187 依据）",
    )
    projection_edit.replace_in_shard(
        direction,
        "方向追踪/005 - 交叉审视、优先级与更新规则.md",
        "4. **当前第一工作包（S102 起由账本驱动）**：先按 `理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md` 的 2×2 判别格选择候选——P1 时序线（同阶段不可用）优先，其次 P2 自指线（同层不可用）与 P3 交叉线；",
        "4. **当前第一工作包（S102 起由账本驱动）**：按 `理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md`（**v2**）推进——判别格**不是**准入门槛而是**检查坐标**之一（任何一格都可进入机器化讨论，区别只在补偿操作写清）；已做 P1 时序线、P2 自指线与 P3 交叉线。C11 v2 §3.2 明列**尚未落进账本**的轴（时间/运动结构、量词与完成顺序、B 方向独立行）**保持研究资格**；2026-09-13 独立审计（F3/F4）判定「S109 用有界检查宣布其余形状关闭」**论证不足**，「两扇门」降级为**暂选路线**（不再含穷尽/唯一含义）；",
    )

    memory = projection_edit.load(root, "MEMORY.md")
    projection_edit.replace_in_shard(
        memory,
        "MEMORY/001 - 当前执行队列.md",
        "**搜索空间收口为两扇门**：",
        "**「搜索空间收口为两扇门」已于 2026-09-13 被独立审计 F3/F4 判定论证不足，降级为暂选路线**"
        "（不再含穷尽/唯一含义；C11 v2 §3.2 自列尚未落账的轴——时间/运动结构、量词与完成顺序、B 方向独立行——恢复研究资格）：",
    )
    projection_edit.replace_in_shard(
        memory,
        "MEMORY/001 - 当前执行队列.md",
        "**算术半第一片已完成**（`MP-ERCF3-T3-ARITH-TAGS-001`，C-166–C-168）",
        "**算术半第一片已完成**（`MP-ERCF3-T3-ARITH-TAGS-001`，C-166–C-168；**2026-09-13 审计 F1 更正**："
        "C-168 的「`1` 无原像」谈的是 `double`，`codeAtom` 实际**满射**（C-184–C-185）；修复后 `codeT'`/`codeF'` 的"
        "缺省分支由 C-186–C-187 依据）",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S124 独立审计吸收（`A-INDEPENDENT-AUDIT-ABSORPTION-001`，`audit/独立审计吸收与独立核验-20260913.md`；"
        "原文逐字节导入 `audit/imports/audit-c168-20260913/`）。7 条发现全部成立：**F1** C-168 对象错配"
        "（`one-has-no-preimage` 谈 `double`；`codeAtom` 满射）——撤回叙述并补机器依据（`C-184`–`C-187`，"
        "两个 run 均固定完整传递闭包）；**F2** closure verifier 缺证据核验——扩展为源哈希/收据四文件/冻结行/"
        "依赖缺口/计数重算五类检查，三例受控改写（矩阵行、源码、删 stdout）在临时 worktree 全部 fail closed；"
        "**F3** S108「不敏感 ⇒ 自动同余」论证不足、两扇门非穷尽收口——降级为暂选路线并恢复未落账轴资格；"
        "**F4** C11 v2 语义未在使用入口收敛——`方向追踪/005` 与 STATE ledger scope 原位修正；"
        "**F5** triage 停止理由过强（队列第 32/34 项是真实截断消费者）——改为收益停止、队列开放；"
        "**F6** 五个历史 run 缺传递依赖——登记 6 条 allowlist（不回填历史），新 run 固定完整闭包；"
        "**F7** later claim 计数漏计（34 实为 35）与复现命令不可执行——verifier 改为重算（现 39）、报告 §12 改正。"
        "未新增理论结论；ERCF-3 保持 `GATED`。\n",
    )

    panorama = projection_edit.load(root, R.PANORAMA)
    projection_edit.append_to_shard(
        panorama,
        "全景视野/006 - ERCF-3 与 T3 脉冲及失败台账.md",
        "| `OUT-TOP-INDEPENDENT-AUDIT-ABSORPTION` | 外部独立审计吸收（7 条发现）：**F1** C-168 对象错配已更正并以完整闭包重放反证"
        "（`C-184`–`C-185`）+ 补上修复后编码的缺省分支依据（`C-186`–`C-187`）；**F2** closure verifier 扩为五类证据检查"
        "（源哈希/收据四文件/冻结行/依赖缺口/计数重算），三例受控改写全部 fail closed；**F3/F4** 搜索空间「收口」降级为暂选路线、"
        "C11 v2 语义在使用入口原位修正；**F5** triage 改为收益停止（队列第 32/34 项是真实截断消费者）；"
        "**F6** 5 个历史 run 的依赖缺口登记 allowlist（6 条，不回填）；**F7** later claims 34→35 更正、现为 39，verifier 重算 | "
        "`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-L-SELF-REFLECTION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | "
        "当前工作包（独立审计回收） | `DOCUMENTED / AUDIT_INPUT_ABSORBED` | 审计原文与证据逐字节导入 "
        f"`{IMPORT_DIR}/`；吸收文档 `{ABSORPTION}`；两个新 run `{COUNTERCHECK_RUN}/`、`{IMAGE_RUN}/` | "
        "F3 的广义否定仍未证；未落账轴尚未开工；triage 队列开放；T3 剩余义务（表示性/反射/对角不动点）仍需门 B；"
        "未新增理论结论；ERCF-3 保持 `GATED` | "
        f"`{ABSORPTION}`；`{IMPORT_DIR}/IMPORT.json`；`HoTT/verification/PROOF_VERSION_CLOSURE.json`（11 追加包 / 39 claims） |",
    )

    essay = projection_edit.load(root, R.ESSAY)

    # Projection revision lines must move with STATE in the *same* checkpoint.
    projections = {"DIRECTION": direction, "PANORAMA": panorama}
    for key, gen, old_gen in (("DIRECTION", "direction", "105"), ("PANORAMA", "outcome", "105")):
        doc = projections[key]
        projection_edit.replace_in_index(doc, "source_state_revision: 123", "source_state_revision: 124")
        projection_edit.replace_in_index(
            doc,
            f"projection_generation: 20260913-{gen}-{old_gen}",
            f"projection_generation: 20260913-{gen}-106",
        )

    ledger = state["records"]["A-THEORY-ECONOMY-LEDGER-001"]
    ledger["scope"] = (
        "C11 theory-economy ledger (v2): eleven economy rows (truncation, set quotients, univalence/SIP, HIT, judgmental "
        "equality, reduction/normalisation, inductive elimination + in-language totality, explicit stage streams, proof "
        "irrelevance, universe/self-description, no global choice) with income / suspended reality factor / payment device / "
        "revival condition / existing verdict; the former 2x2 discrimination grid is retained only as a *check coordinate* "
        "(not a gate); predictions P1 (time), P2 (self-reference), P3 (intersection); retrodiction over 18 machine packages "
        "(17 with an available payment device, 1 -- MP-NOCANONICAL-001 -- without). PAPER_ONLY method ledger: no new "
        "mathematical claim, no verdict change. Audit F4 corrected the earlier scope text (nine rows / 2x2 gate / 'no "
        "unavailable cell') in place."
    )
    ledger["revalidation"] = (
        f"scope text corrected by {SESSION_ID} after independent audit finding F4 (the v2 document itself was already "
        "correct; this record's summary was stale). Content, hashes and evidence status unchanged."
    )

    tags = state["records"]["A-ERCF3-T3-ARITH-TAGS-001"]
    tags["revalidation"] = (
        f"narrative corrected by {SESSION_ID} after independent audit finding F1: `one-has-no-preimage` is about "
        "`double` (the avar-only fragment), not about `codeAtom`, which is surjective (C-184/C-185). The formal claims "
        "C-166-C-168, the run receipt and the frozen matrix rows are unchanged; the default-branch justification for the "
        "repaired coders is now carried by C-186/C-187."
    )

    report_record = state["records"]["A-AUDIT-REPORT-TONGGUAN-001"]
    report_record["source_hashes"] = {REPORT: R.sha((root / REPORT).read_bytes())}
    report_record["revalidation"] = (
        f"{REPORT} re-hashed by {SESSION_ID}: sections 5.1/5.2/6/8.3(d)/9.2/10/12 revised and section 14 (independent "
        "audit absorption) added. The report remains DOCUMENTED and makes no new mathematical claim."
    )

    state["records"][RESULT_ID] = {
        "kind": "result",
        "path": ABSORPTION,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "DOCUMENTED",
        "depends_on": [],
        "related_records": [SESSION_ID, "A-AUDIT-REPORT-TONGGUAN-001", "A-THEORY-ECONOMY-LEDGER-001",
                            "A-ERCF3-T3-ARITH-TAGS-001"],
        "full_sources": [ABSORPTION, f"{IMPORT_DIR}/IMPORT.json", REPORT],
        "source_hashes": {
            ABSORPTION: R.sha((root / ABSORPTION).read_bytes()),
            f"{IMPORT_DIR}/IMPORT.json": R.sha((root / f"{IMPORT_DIR}/IMPORT.json").read_bytes()),
        },
        "scope": (
            "Absorption of the independent audit of the panoramic-survey technical report. Seven findings, all verified "
            "and accepted: F1 (C-168 object mismatch; withdrawn and re-grounded by replayed counterchecks C-184/C-185 plus "
            "C-186/C-187), F2 (closure verifier evidence gap; fixed and mutation-tested), F3 (the search-space 'closure' is "
            "not proved; downgraded to a provisional route), F4 (C11 v2 semantics not propagated; corrected in place), "
            "F5 (triage stop reason; restated as a cost-benefit stop with the queue left open), F6 (dependency-closure gaps "
            "allowlisted), F7 (claim count and replay commands corrected; count now recomputed). No new theoretical claim; "
            "ERCF-3 remains gated."
        ),
    }
    state["records"]["A-ERCF3-T3-C168-COUNTERCHECK-001"] = {
        "kind": "result",
        "path": "HoTT/formal/ercf3-t3/C168Countercheck.agda",
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "depends_on": [],
        "related_records": ["A-ERCF3-T3-ARITH-TAGS-001", RESULT_ID],
        "full_sources": ["HoTT/formal/ercf3-t3/C168Countercheck.agda", f"{COUNTERCHECK_RUN}/RUN.json"],
        "source_hashes": {"HoTT/formal/ercf3-t3/C168Countercheck.agda": R.sha((root / "HoTT/formal/ercf3-t3/C168Countercheck.agda").read_bytes())},
        "scope": (
            "Replay of the independent audit's C-168 countercheck with the complete transitive closure pinned: "
            "C-184 codeAtom (anum zero) = 1; C-185 codeAtom is surjective."
        ),
    }
    state["records"]["A-ERCF3-T3-CODING-IMAGE-001"] = {
        "kind": "result",
        "path": "HoTT/formal/ercf3-t3/CodingImage.agda",
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "depends_on": [],
        "related_records": ["A-ERCF3-T3-C168-COUNTERCHECK-001", "A-ERCF3-T3-STREAMING-PARSER-001", RESULT_ID],
        "full_sources": ["HoTT/formal/ercf3-t3/CodingImage.agda", f"{IMAGE_RUN}/RUN.json"],
        "source_hashes": {"HoTT/formal/ercf3-t3/CodingImage.agda": R.sha((root / "HoTT/formal/ercf3-t3/CodingImage.agda").read_bytes())},
        "scope": (
            "Replacement justification for the repaired decoders' default branches: C-186 codeT' misses 1; C-187 codeF' "
            "misses 1. Both runs pin the complete transitive closure."
        ),
    }

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户输入：外部 AI 对本 repo 技术报告的独立审计（{IMPORT_DIR}/）。
- 处置：7 条发现全部核验成立——F1/F2 以新机器证据闭合（`C-184`–`C-187`、closure verifier 扩展 + 三例受控改写复测）；
  F3/F4/F5 降级并原位修正当前语义（`方向追踪/005`、`MEMORY/001`、STATE scope）；F6/F7 登记为结构缺口（依赖 allowlist、计数重算、报告 §12 命令更正）。
- 交付：`{ABSORPTION}`（逐项核验与变更清单）；`{REPORT}` 更新至 §14 并重绑哈希。
- 不变：任何既有 claim 行、run 收据、冻结矩阵行、版本闭环；ERCF-3 保持 `GATED`。
- 未闭合：F3 的广义否定未证；C11 v2 未落账轴未开工；triage 队列开放；T3 表示性/反射/对角不动点仍需门 B。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "runtime_version": R.VERSION,
            "audit_absorption": {
                "import_dir": IMPORT_DIR,
                "absorption_document": ABSORPTION,
                "findings": {
                    "F1": "accepted; C-184/C-185 replay + C-186/C-187 replacement justification; original rows untouched",
                    "F2": "accepted; verifier extended (source/receipt/index-row/dependency-gap/count) + 3 mutation tests fail closed",
                    "F3": "accepted; search-space closure downgraded to a provisional route",
                    "F4": "accepted; current-truth entries corrected in place (direction priority, STATE ledger scope)",
                    "F5": "accepted; triage restated as a cost-benefit stop with the queue left open",
                    "F6": "accepted; 6 dependency gaps allowlisted, new runs pin the full closure",
                    "F7": "accepted; counts recomputed by the verifier (39) and the replay commands fixed",
                },
            },
            "new_math_claims": ["C-184", "C-185", "C-186", "C-187"],
            "verdict_changes": [],
            "push": "NOT_AUTHORIZED",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"

    state["revision"] = 124
    state["latest_session"] = SESSION_ID
    state["execution_control"].update(
        {
            "last_checkpoint_session": SESSION_ID,
            "checkpoint_result": "CHECKPOINT_APPLIED_INDEPENDENT_AUDIT_ABSORPTION",
            "status": STATUS,
            "next_minimal_verification": (
                "The independent audit of the panoramic technical report has been absorbed (F1-F7). Binding state: the "
                "search-space 'closure' is only a provisional route (F3); the axes C11 v2 lists as not-yet-ledgered "
                "(time/motion, quantifier/completion order, an independent B-direction row) have their research eligibility "
                "restored; the triage queue stays open (at least two real truncation consumers); the T3 coding line's "
                "self-contained part is closed and the remaining obligations (object-level representability, proof-predicate "
                "representability, reflection, diagonal fixed point) still need the door-B consumer. ERCF-3 stays GATED."
            ),
        }
    )
    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [],
        "related_records": [PREV, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, ABSORPTION, f"{IMPORT_DIR}/IMPORT.json"],
        "source_hashes": {},
        "scope": "Registration of the independent-audit absorption: import, verification, fixes, records and re-pinning.",
    }

    texts: dict[str, str] = {rel: (root / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for doc in (projections["DIRECTION"], projections["PANORAMA"], memory, essay):
        texts[doc["index_path"]] = doc["index_text"]
        texts.update(doc["shards"])
    texts[session_path] = session
    texts[audit_path] = audit_text(root)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "User supplied an external independent audit of the 统观 technical report. Absorb it with the established "
            "procedure: byte-preserved import, item-by-item verification, in-place correction of current truth, new "
            "machine evidence where a claim was wrong, corrective re-pin and all six verifiers. No push."
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
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 124,
                      "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
