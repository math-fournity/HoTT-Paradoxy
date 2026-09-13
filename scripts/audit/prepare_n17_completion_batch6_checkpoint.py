#!/usr/bin/env python3
"""Prepare revision 62: record MP-TRUNC-NORECOVERY-001 (C-134–C-138) and batch-5.

S062 adds the machine-checked set-valued truncation no-recovery family
(Agda 2.8.0 + Cubical v0.9, exit 0, exact replay, matrix rows C-134–C-138 with
a frozen index-row manifest) and the fifth evidence-queue sample (40 claims;
SUPPORTED 29 / PENDING 11 / no UNSUPPORTED / no E6; cumulative 202/2,396).
Next work package: N17 (queue continuation) with the standing E6 gate.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260913-063-N17-COMPLETION-FORMS-AND-BATCH6"
PREV_SESSION = "S-RES-20260913-062-N16-TRUNC-NORECOVERY-AND-BATCH5"
RESULT_ID = "A-TRUNC-COMPLETION-FORMS-001"
REPORT = "audit/truncation-completion-and-batch6-20260913.md"
SRC = "HoTT/formal/truncation-no-recovery/TruncationNoRecovery.agda"
README = "HoTT/formal/truncation-no-recovery/README.md"
TOOLCHAIN = "HoTT/formal/truncation-no-recovery/TOOLCHAIN.json"
LIBREG = "HoTT/formal/truncation-no-recovery/AGDA_LIBRARIES"
RUN_DIR = "HoTT/verification/runs/20260913-MP-TRUNC-NORECOVERY-001-02"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
SAMPLE_SCRIPT = "scripts/audit/sample_understanding_claims_batch6.py"
FILL_SCRIPT = "scripts/audit/fill_understanding_claim_sample_batch6.py"
SAMPLE_JSON = "audit/understanding-claim-sample-batch6-20260912.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EVIDENCE = [
    REPORT, SRC, README, TOOLCHAIN, LIBREG, MATRIX,
    f"{RUN_DIR}/RUN.json", f"{RUN_DIR}/index-row-manifest.json",
    SAMPLE_SCRIPT, FILL_SCRIPT, SAMPLE_JSON,
]
NEW_STATUS = "N17_COMPLETION_FORMS_AND_BATCH6_REVIEWED_QUEUE_CONTINUES"

SPEC = importlib.util.spec_from_file_location("runtime_n16", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sub_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"SUB_COUNT:{count}:{old[:80]}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000010": ("ALIGNED", "‘不可计算/不可停机’特征：本轮把截断拒绝逐点恢复做成族群化机器边界。"),
        "KC-000013": ("ALIGNED", "理论工具性异化：集合值消费者下身份不可恢复，资格分离被机器化。"),
        "KC-000022": ("ALIGNED", "B 方向（理论假装已完成）在截断接口处被拒；未见绕越。"),
        "KC-000029": ("DEEPENED", "理论经济拿掉多余现实因素：C-134–C-138 证明被遗忘的是 witness 身份。"),
        "KC-000036": ("ALIGNED", "E6 五批未出现；gated 状态不变。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    aligned = deepened = 0
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = touched.get(
            unit["id"],
            ("NOT_TOUCHED", "本轮是 S062 机器包与第五批抽样；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S062/SESSION.md；{REPORT}；{RUN_DIR}/RUN.json | E6 与队列余量仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — 新增 `MP-TRUNC-NORECOVERY-001`（C-134–C-138，判词 `SET_VALUED_TRUNCATION_NO_RECOVERY_FAMILY`）；N16 第五批 40 条完成（五批累计 202/2,396）；第一工作包转 N17；revision 62/generation 046。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-TRUNC-NORECOVERY` 与 `OUT-TOP-EVIDENCE-QUEUE-BATCH5`；理解章节 inventory 不变。",
        "- update_decision: `新增 HoTT/formal 与 run 证据、claim matrix 五行与冻结 manifest；抽样工件进入 audit/；不重写冻结账本。`",
        "- cross_conflicts: `NONE_OBSERVED` — 新包与 C-67–C-70 同向且更一般；五批抽样连续无 UNSUPPORTED、无 E6。",
        "- unresolved: `证据队列余量（冻结分母 2,396 的 ~91.6%）、E6、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `MACHINE_PROVED_TRUNC_NORECOVERY_FAMILY_PLUS_BATCH5`（新增 5 条机器 claim；无悖论升级）。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S061 路由的 N16（证据队列继续）+ 用户主方向的截断资格边界。",
        "- 机器包 `MP-TRUNC-NORECOVERY-001`（C-134–C-138）：Agda 2.8.0-3d04bac + Cubical v0.9，`--safe --cubical --guardedness`，exit 0、stderr 0、零 warning；`pointConstructorsForceEquality`（集合值读出在 point constructor 上强制相等）、`noPointRecovery`（应用形式）、Bool 与 ℕ 两个实例、`propositionValuedTestExists` 正控制。",
        "- final run `20260913-MP-TRUNC-NORECOVERY-001-01`：`KERNEL_ACCEPTED_WITH_SCOPE`、`EXACT_INDEX_SNAPSHOT_MATCH`、独立 `--rerun` 为 `EXACT_EXIT_STDOUT_STDERR_MATCH`；matrix 新增 proof 行 + C-134–C-138，冻结 6 行 index manifest。",
        "- 第五批抽样：按前 1–4 批抽样比升序分配 40 条（每 owner≤5），覆盖 README/B2/全量精读/B4/A6/B1/B0/A11；判词 `SUPPORTED=29`、`PENDING=11`、0 `UNSUPPORTED`、0 `SUPERSEDED`；五批累计 202/2,396（8.4%）：122/12/0/68；E6 五批一致未出现。",
        "- 边界：不证明 HoTT 内部矛盾；非集合（高阶）目标不外推；不把 `DEFENSE_WORKS` 升级为 `NATURAL_USAGE_MISMATCH`；本轮新数学 claim 已按 F-011 打包，抽样未触发 F-011。",
        "- 三件套：direction/panorama revision 62/generation 046；core 不变；无 理解章节 变更。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_N16_TRUNC_NORECOVERY_AND_BATCH5_REVIEWED_QUEUE_CONTINUES`",
        "状态：`CORE_GENERATION_4_N17_COMPLETION_FORMS_AND_BATCH6_REVIEWED_QUEUE_CONTINUES`",
    )
    direction = sub_once(direction, "source_state_revision: 62", "source_state_revision: 63")
    direction = sub_once(direction, "projection_generation: 20260913-direction-046", "projection_generation: 20260913-direction-047")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_N16_TRUNC_NORECOVERY_AND_BATCH5_REVIEWED_QUEUE_CONTINUES",
        "semantic_status: CORE_GENERATION_4_N17_COMPLETION_FORMS_AND_BATCH6_REVIEWED_QUEUE_CONTINUES",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N17 证据队列按比例继续（第 6 批，可选）——沿用同一抽样规则覆盖下一档 owner（`A5`、`升级方案-v2`、`A10`、`A2` 等），四值判词与前五批去重；若发现 E6 立即转 F-011。N16 已完成：`MP-TRUNC-NORECOVERY-001`（C-134–C-138，集合值截断不可恢复族，机器闭合）+ 第五批 40 条（29/0/0/11）；五批累计 202/2,396。备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。",
        "4. **当前第一工作包**：N18 证据队列按比例继续（第 7 批，可选）——沿用同一抽样规则覆盖下一档 owner（`A3`、`A9`、`A0`、`A2` 等），四值判词与前六批去重；若发现 E6 立即转 F-011。N17 已完成：`MP-TRUNC-NORECOVERY-001` 扩展（C-139/C-140 完成不可行性的内部否定形式，机器闭合，run `-02`）+ 第六批 40 条（27/0/0/13）；六批累计 242/2,396。备选：ERCF-3 T3（Gödel 句，仍按 C8 停止条件 gated）。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_N16_TRUNC_NORECOVERY_AND_BATCH5_REVIEWED_QUEUE_CONTINUES`",
        "状态：`CORE_GENERATION_4_N17_COMPLETION_FORMS_AND_BATCH6_REVIEWED_QUEUE_CONTINUES`",
    )
    panorama = sub_once(panorama, "source_state_revision: 62", "source_state_revision: 63")
    panorama = sub_once(panorama, "projection_generation: 20260913-outcome-046", "projection_generation: 20260913-outcome-047")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_N16_TRUNC_NORECOVERY_AND_BATCH5_REVIEWED_QUEUE_CONTINUES",
        "semantic_status: CORE_GENERATION_4_N17_COMPLETION_FORMS_AND_BATCH6_REVIEWED_QUEUE_CONTINUES",
    )
    row = (
        "| `OUT-TOP-TRUNC-NORECOVERY` | `MP-TRUNC-NORECOVERY-001`：集合值截断不可恢复族——`C-134` 集合值读出在 point constructor 上强制相等；`C-135` 加分离见证后读出与一致性证明不可共存；`C-136`/`C-137` 为 Bool 与 ℕ 实例（分离对 0/1）；`C-138` 为 mere-proposition 目标正控制 |"
        " `DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前原生 Cubical Agda 形式化 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SET_VALUED_TRUNCATION_NO_RECOVERY_FAMILY` |"
        " Agda 2.8.0 + Cubical v0.9、`--safe --cubical --guardedness`、exit 0（stderr 0、零 warning）、`EXACT_INDEX_SNAPSHOT_MATCH`、独立重放 `EXACT_EXIT_STDOUT_STDERR_MATCH` |"
        " 不证明 HoTT 内部矛盾、非集合（高阶）目标的同类结论或所有 `∥ A ∥₁ → A` 不存在；E6 仍开放 |"
        " `HoTT/formal/truncation-no-recovery/`；final run `20260913-MP-TRUNC-NORECOVERY-001-01`；claim matrix C-134–C-138；`audit/truncation-no-recovery-and-batch5-20260913.md` |\n"
        "| `OUT-TOP-EVIDENCE-QUEUE-BATCH5` | S062 第五批按比例抽样 40 条（README/B2/全量精读/B4/A6/B1/B0/A11 各 5）：`SUPPORTED=29`/`PENDING=11`/0 `UNSUPPORTED`/0 `SUPERSEDED`；五批累计 202/2,396（8.4%）：122/12/0/68；E6 未出现 |"
        " `DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前人工抽样复核 + 确定性脚本 | `DOCUMENTED / BOUNDED_SAMPLE_BATCH5` |"
        " 五批抽样无 UNSUPPORTED、无 E6；本轮新数学 claim 与抽样打包相互独立 |"
        " 冻结 2,396 分母不变；PENDING 不当作支持或否证 |"
        " `audit/understanding-claim-sample-batch5-20260912.json`；`scripts/audit/sample_understanding_claims_batch5.py` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "S061 完成 N15（a 口径对照表；b 第四批 40 条 28/0/0/12，四批累计 162/2,396，仍无 `UNSUPPORTED`、无 E6），并修正两项口径表述；R032 回放、",
        "S061 完成 N15（a 口径对照表；b 第四批 40 条 28/0/0/12，四批累计 162/2,396，仍无 `UNSUPPORTED`、无 E6），并修正两项口径表述；S062 新增 `MP-TRUNC-NORECOVERY-001`（C-134–C-138：集合值截断不可恢复族，exit 0、exact replay）并完成第五批抽样（40 条 29/0/0/11，五批累计 202/2,396，仍无 `UNSUPPORTED`、无 E6）；R032 回放、",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "S061 完成 N15 口径对照（2369 句/171 单元、125/119 记录、2,396 冻结行、22/24 owner 计数复现、当前面 4,547 行）与第四批按比例抽样（40 条 28/0/0/12，四批累计 162/2,396，无 UNSUPPORTED、无 E6；专项核验 14/14）。所有新结论继续执行 F-011。",
        "S061 完成 N15 口径对照（2369 句/171 单元、125/119 记录、2,396 冻结行、22/24 owner 计数复现、当前面 4,547 行）与第四批按比例抽样（40 条 28/0/0/12，四批累计 162/2,396，无 UNSUPPORTED、无 E6；专项核验 14/14）；S062 新增 `MP-TRUNC-NORECOVERY-001`（C-134–C-138：集合值消费者下截断不可逐点恢复族，Bool/ℕ 双实例 + 命题值正控制，exit 0、零 warning、exact replay）与第五批抽样（40 条 29/0/0/11，五批累计 202/2,396，仍无 UNSUPPORTED、无 E6）。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N16 证据队列按比例继续（可选第 5 批） | proportion sampling | 下一档 owner（A11/B5/A7 等）沿用同一规则并与前四批去重；发现 E6 即转 F-011；备选 ERCF-3 T3（gated） |",
        "| 已闭合工作包 20 | 集合值截断不可恢复族（S062，C-134–C-138） | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SET_VALUED_TRUNCATION_NO_RECOVERY_FAMILY` | 集合值读出强制相等；Bool/ℕ 实例；命题值正控制；非集合目标围栏 |\n"
        "| 已闭合工作包 21 | 第五批抽样（S062） | `BOUNDED_SAMPLE_BATCH5` | 40 条 29/0/0/11；五批累计 202/2,396；无 UNSUPPORTED、无 E6 |\n"
        "| 第一工作包 | N17 证据队列按比例继续（第 6 批） | proportion sampling | 下一档 owner（A5/升级方案-v2/A10/A2 等）沿用同一规则并与前五批去重；发现 E6 即转 F-011；备选 ERCF-3 T3（gated） |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N16 证据队列按比例继续（可选第 5 批）：沿用同一抽样规则覆盖下一档 owner（`A11` 5.2%、`B5` 5.2%、`A7` 6.5% 等）并与前四批去重；若发现 E6 立即转 F-011。N15 已完成（a 口径对照表；b 第四批 40 条 28/0/0/12；四批累计 162/2,396）。备选：ERCF-3 T3（gated）。",
        "2. 当前第一工作包转为 N18 证据队列按比例继续（第 7 批，可选）：沿用同一抽样规则覆盖下一档 owner（`A3`、`A9`、`A0`、`A2` 等）并与前六批去重；若发现 E6 立即转 F-011。N17 已完成：`MP-TRUNC-NORECOVERY-001` 扩展（C-139/C-140）+ 第六批 40 条（27/0/0/13；六批累计 242/2,396）。备选：ERCF-3 T3（gated）。",
    )
    memory = sub_once(
        memory,
        "- S061 完成 N15：",
        "- S063 完成 N17：(a) `MP-TRUNC-NORECOVERY-001` 扩展（C-139/C-140）：完成不可行性的内部否定形式，run `-02`、exit 0、exact replay、冻结 8 行 manifest；(b) 第六批抽样 40 条（27/0/0/13），六批累计 242/2,396；下一工作包 N18。\n- S062 完成 N16：(a) `MP-TRUNC-NORECOVERY-001`（C-134–C-138）集合值截断不可恢复族机器闭合；第五批抽样 40 条（29/0/0/11），五批累计 202/2,396；下一工作包 N17（队列按比例继续）。\n- S061 完成 N15：",
    )
    memory = sub_once(
        memory,
        "S061 完成 N15（口径机器对照 + 第四批 40 条，四批累计 162/2,396，仍无 UNSUPPORTED、无 E6），转 N16（队列按比例继续），不直接跳 ERCF-3 构造。",
        "S061 完成 N15（口径机器对照 + 第四批 40 条，四批累计 162/2,396，仍无 UNSUPPORTED、无 E6）；S062 完成 N16（`MP-TRUNC-NORECOVERY-001` C-134–C-138 机器闭合 + 第五批 40 条，五批累计 202/2,396，仍无 UNSUPPORTED、无 E6）；S063 完成 N17（C-139/C-140 完成不可行性内部否定形式 + 第六批 40 条，六批累计 242/2,396，仍无 UNSUPPORTED、无 E6），转 N18（队列按比例继续），不直接跳 ERCF-3 构造。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S062 完成 N16：(a) `MP-TRUNC-NORECOVERY-001`（C-134–C-138）在 Agda 2.8.0-3d04bac + Cubical v0.9 下原生机器化「集合值消费者下命题截断不可逐点恢复」族——`pointConstructorsForceEquality`（集合值读出与实现一致 ⇒ 任意两点值相等）、`noPointRecovery`（加分离见证后不可共存）、Bool 与 ℕ 实例（分离对 0/1）、`propositionValuedTestExists`（mere-proposition 正控制）；final run `20260913-MP-TRUNC-NORECOVERY-001-01`：exit 0、stderr 0、零 warning、`EXACT_INDEX_SNAPSHOT_MATCH`、独立 `--rerun` exact match；matrix 新增 proof 行 + C-134–C-138 并冻结 6 行 manifest。(b) 第五批按比例抽样 40 条（README/B2/全量精读/B4/A6/B1/B0/A11 各 5）：`SUPPORTED=29`、`PENDING=11`、0 `UNSUPPORTED`、0 `SUPERSEDED`；五批累计 202/2,396（8.4%）：122/12/0/68；E6 五批一致未出现。报告 `audit/truncation-no-recovery-and-batch5-20260913.md`；下一工作包 N17（队列第 6 批），备选 ERCF-3 T3（gated）。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "60. 报告口径必须先各带单位再比较：",
        "61. 截断“不可恢复”可以族群化而不失围栏：把 C-70 的 Bool 实例升级为「任意集合值读出 + 任意分离见证」的一般形式（C-134–C-138），代价只是把 motive 换成路径类型、并用库定理 `isOfHLevelPath'` 说明「集合中路径类型是命题」。族群化的价值是把用户「理论经济保留存在、遗忘身份」的命题从单例观察变成带正控制（mere proposition 目标仍可消费）和适用域围栏（非集合高阶目标不外推）的机器边界；它仍是 `DEFENSE_WORKS`，不是悖论。工程侧教训：Cubical Agda 2.8 中 `isOfHLevelPath'` 必须按位置传参（`isOfHLevelPath' 1 Sset x y`），把类型写成 `{A = ...}` 会被当作额外隐式参数而失败；边界计算（`squash₁` 端点）也不能依赖 λ 的直接展开，用 `cong`/`sym`/`∙` 组合更稳。\n"
        "60. 报告口径必须先各带单位再比较：",
    )
    return {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 62 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_62_AND_S062")
    for rel in EVIDENCE:
        if not (root / rel).is_file():
            raise SystemExit(f"EVIDENCE_MISSING:{rel}")

    new_hashes = {rel: sha(root / rel) for rel in EVIDENCE}

    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = sha(path) if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    allowed = {MATRIX, SRC, f"{RUN_DIR}/index-row-manifest.json", f"{RUN_DIR}/RUN.json", "HoTT/formal/README.md", "HoTT/verification/runs/README.md", "HoTT/README.md", "HoTT/verification/VERIFICATION_REPORT.md"}
    unexpected = sorted({rel for _, rel in observed_stale} - allowed)
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE_PATHS:{unexpected}")
    note = (
        "Revalidated after S062 (MP-TRUNC-NORECOVERY-001 C-134-C-138 and batch-5 sample); "
        "no existing proof source, run body or understanding-chapter file changed."
    )
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes.get(rel, sha(root / rel))
        state["records"][rid]["revalidation"] = note

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "formal_proof_package_and_sample",
        "path": SRC,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "classification": "SET_VALUED_TRUNCATION_NO_RECOVERY_FAMILY",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-EVIDENCE-HYGIENE-BATCH3-001", "A-ERCF-TRUNCATION-DEFENSE-001"],
        "full_sources": EVIDENCE,
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "formal": {
            "proof_id": "MP-TRUNC-NORECOVERY-001",
            "claim_ids": ["C-134", "C-135", "C-136", "C-137", "C-138", "C-139", "C-140"],
            "run_id": "20260913-MP-TRUNC-NORECOVERY-001-01",
            "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
            "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
            "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "resolution": {
            "reason": "The set-valued no-recovery family is machine-checked on the pinned toolchain (exit 0, zero warnings): constancy of set-valued reads on point constructors, the applied no-go, Bool and Nat instances, and the proposition-valued positive control. The batch-5 proportional sample adds 40 verdicts (29/0/0/11); cumulative 202/2396 with no UNSUPPORTED and no E6.",
            "evidence": EVIDENCE,
        },
        "scope": "Bounded family theorem for set-valued consumers of native propositional truncation plus the fifth evidence-queue sample. No HoTT inconsistency; higher-dimensional targets and all untruncations are outside scope; E6 remains open.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, *EVIDENCE],
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "mathematical_status": "MACHINE_PROVED_SET_VALUED_TRUNCATION_NO_RECOVERY_FAMILY",
        "cognition_status": "N16_TRUNC_NORECOVERY_AND_BATCH5_REVIEWED",
        "scope": "Truncation no-recovery family package, batch-5 sample, and routing of N17.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260913-direction-047" if rid.startswith("I-DIRECTION") else "20260913-outcome-047"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (REPORT, f"{RUN_DIR}/RUN.json", SAMPLE_JSON, MATRIX):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)

    state["revision"] = 63
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N17: continue the evidence queue by the same proportional rule over the next owner tier "
            "(A5, 升级方案-v2, A10, A2, ...), deduplicated against batches 1-5; keep the frozen 2,396 "
            "denominator and the current-document recount separate. If a natural-use chain (E6) appears, "
            "switch immediately to F-011 packaging. Fallback: ERCF-3 T3 (gated by the C8 stop conditions)."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "work_kind": "formal_package_and_batch5",
        "mathematical_claim_added": True,
        "claim_matrix_updated": {"proof_row": "MP-TRUNC-NORECOVERY-001", "claims": ["C-134", "C-135", "C-136", "C-137", "C-138", "C-139", "C-140"]},
        "formal_run": {
            "run_id": "20260913-MP-TRUNC-NORECOVERY-001-01",
            "proof_id": "MP-TRUNC-NORECOVERY-001",
            "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
            "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
            "exit_code": 0,
            "stderr_bytes": 0,
            "warnings": 0,
        },
        "batch5": {
            "rule": "owners by prior sampling ratio ascending, budget 40, max 5 per owner, equidistant, batches 1-4 excluded",
            "sample_size": 40,
            "verdicts": {"SUPPORTED": 27, "SUPERSEDED_BY_MACHINE_RESULT": 0, "UNSUPPORTED": 0, "PENDING": 13},
            "cumulative": {"sampled": 242, "coverage": "10.1%", "SUPPORTED": 149, "SUPERSEDED": 12, "UNSUPPORTED": 0, "PENDING": 81},
            "e6_found": False,
        },
        "stale_source_hash_repair": {"observed": len(observed_stale), "unexpected_remainder": 0},
        "evidence": {"report": REPORT, "sample": SAMPLE_JSON},
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    edited = apply_projection_edits(root)
    texts = {
        **edited,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session_text(),
        audit_path: audit_text(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate "
            "the next package. This in-scope checkpoint records MP-TRUNC-NORECOVERY-001 (C-134-C-138, machine-proved "
            "on the pinned Cubical Agda toolchain with exact replay) and the batch-5 sample (40 claims; 29/0/0/11; "
            "cumulative 202/2396, no UNSUPPORTED, no E6). It routes N17. No Git commit, tag or push."
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
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PREPARED",
        "snapshot": plan["snapshot"],
        "revision": 63,
        "session_id": SESSION_ID,
        "stale_repaired": len(observed_stale),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
