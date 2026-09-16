#!/usr/bin/env python3
"""Prepare revision 150: close CE-MAP v1 and activate the R3/R4 Gödel return."""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SCRIPTS = ROOT / "scripts/audit"
SESSION_ID = "S-RES-20260915-150-CE-MAP-V1"
PREV = "S-RES-20260915-149-INTERNALISATION-CONSUMERS"
STATUS = "CORE_GENERATION_4_CE_MAP_V1_COMPLETE_R3_R4_GODEL_NEXT"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"

GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-002"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
COVERAGE_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
LIT_CLASSICS_ID = "A-LIT-CLASSICS-001"
LIT_HOTT_ID = "A-LIT-HOTT-COMPUTABILITY-001"
SYNTAX_ID = "A-G-HOTT-SYNTAX-001"
CE_ID = "A-CE-MAP-001"
R3_ID = "A-R3-R4-GODEL-RETURN-001"

CE_DOC = ".codex/research/hott/CE-MAP-001.md"
R3_DOC = ".codex/research/hott/R3-R4-GODEL-RETURN-001.md"
GOAL = "goal.md"
FEATURE = "feature-list.md"
PROGRAM_005 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/005 - 阶段路线、验收与当前缺口.md"
PROGRAM_006 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/006 - 计算合法性主线与学术谱系覆盖审计.md"
PROGRAM_TEST = "scripts/audit/test_hott_programmatic_exploration_completeness.py"
CE_MANAGER = "scripts/audit/build_ce_map.py"
CE_TEST = "scripts/audit/test_ce_map.py"
IMPORT_MANAGER = "scripts/audit/import_machine_overview_ce_map.py"
IMPORT_ROOT = "audit/imports/machine-overview-ce-map-20260915"
IMPORT_MANIFEST = f"{IMPORT_ROOT}/IMPORT.json"
IMPORT_CATALOG = f"{IMPORT_ROOT}/CATALOG.json"
CE_ROOT = "audit/ce-map"
CE_README = f"{CE_ROOT}/README.md"
CE_MAP = f"{CE_ROOT}/CE-MAP.json"
CE_UNCLASSIFIED = f"{CE_ROOT}/UNCLASSIFIED.json"
CE_REPORT = f"{CE_ROOT}/REPORT.md"
CE_RECEIPT = f"{CE_ROOT}/RECEIPT.json"
AUDIT = "audit/CE-MAP机器统观八轴映射与同型归约-20260915.md"
PREPARE = "scripts/audit/prepare_s150_ce_map_checkpoint.py"

LIT_CLASSICS_003 = ".codex/research/hott/LIT-CLASSICS-001/003 - Gödel、Rosser与Löb：算术化、独立句与自担保.md"
LIT_CLASSICS_005 = ".codex/research/hott/LIT-CLASSICS-001/005 - 现代机器化对照与R2-R4前提.md"
LIT_HOTT_004 = ".codex/research/hott/LIT-HOTT-COMPUTABILITY-001/004 - 2LTT、groupoid-syntax 与下一候选.md"
GROUP_SYNTAX_CLAIM = "HoTT/formal/external-cubical-groupoid-syntax/CLAIM-G-HOTT-SYNTAX.md"
GROUP_SYNTAX_RUN = "HoTT/verification/runs/20260914-MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001-01/RUN.json"
COQ_R3_ROOT = f"{IMPORT_ROOT}/source/evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001"
COQ_R3_REPORT = f"{COQ_R3_ROOT}/REPORT.md"
COQ_R3_BUILD = f"{COQ_R3_ROOT}/BUILD-RECEIPT.json"
COQ_R3_SOURCE = f"{COQ_R3_ROOT}/SOURCE-MANIFEST.json"

SPEC = importlib.util.spec_from_file_location("runtime_s150", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{text.count(old)}")
    return text.replace(old, new, 1)


def replace_line(text: str, marker: str, replacement: str) -> str:
    lines = text.splitlines()
    matches = [index for index, line in enumerate(lines) if line.startswith(marker)]
    if len(matches) != 1:
        raise ValueError(f"LINE_MATCH_COUNT:{marker}:{len(matches)}")
    lines[matches[0]] = replacement
    return "\n".join(lines) + "\n"


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def file_hashes(paths: list[str], future: dict[str, str] | None = None) -> dict[str, str]:
    future = future or {}
    return {
        path: R.sha(future[path].encode("utf-8") if path in future else (ROOT / path).read_bytes())
        for path in paths
    }


def command_pass(argv: list[str], required: str) -> None:
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, check=False)
    output = result.stdout + result.stderr
    if result.returncode != 0 or required not in output:
        raise SystemExit(f"PRECHECK_FAILED:{' '.join(argv)}\n{output}")


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000002": "CE-MAP 把 theory construct 与 abstraction change 分轴登记，避免把对象和删改操作混成一个名称。",
        "KC-000005": "478 个具名输入全部进入地图，69 个 unknown 原样保留；统观完整性不再由工作量或文件数量代替。",
        "KC-000007": "import→catalog→map→query→negative control 形成可执行机器发现链，下一 successor 由未覆盖 cell 选择。",
        "KC-000010": "CE_MAP_V1_COMPLETE_WITH_SCOPE 被限定为 revision-149 closed world，不提升为 HoTT 悖论或开放世界完备。",
        "KC-000011": "physical-time cell 仍保留 UNKNOWN Oracle；没有用 global/local 时序替代运动、时空和稠密连续性。",
        "KC-000012": "每个 item 的前提、framework、oracle 与 completion 分列；无法确定就写 UNKNOWN。",
        "KC-000013": "pattern class 明列 consumer/observation/completion/framework anti-preservation，防止能力层级混同。",
        "KC-000015": "C-228–C-240 的抽象变化归约为取消资格后的 external/pointwise→local/open/context-uniform promotion。",
        "KC-000021": "478 item、四输出 hash、169-file import、7/7 tests与负控制构成多样审计锚点。",
        "KC-000022": "方向 A/B、Gödel、Oracle、physical time 与 reality cells 没有被 internalisation class吞掉。",
        "KC-000027": "下一步要求 exact HoTT syntax/proof predicate，而不是把一般 Gödel theorem 写进 HoTT 宿主就称专属结果。",
        "KC-000029": "类归约计算重复机制的理论经济，同时保留不同 consumer 所支付的 crisp/transport/context 成本。",
        "KC-000031": "已有 internalisation family 被 defense解释后，机器主动转向 R3/R4 未覆盖轴，不继续累积同型 no-go。",
        "KC-000035": "machine-managed canonical + query 路由让 594KB 地图可跨 Session 使用而不强制全文预载。",
        "KC-000036": "R3/R4 TaskSpec 将 Gödel 线拆成有效语法、checker、representability、fixed point、independence、HoTT essentiality和现实桥梁。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；根 Goal 保持 active。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        identity = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "DEEPENED" if identity in focus else "NOT_TOUCHED"
        assessment = focus.get(identity, f"本轮没有重新裁决“{label}”的数学、现实或哲学内容。")
        lines.append(
            f"| `{identity}` | {label} | `{relation}` | {assessment} | `{AUDIT}`；{identity} | "
            "R3/R4、HoTT essentiality、现实同任务、Oracle、物理时间、ambient R2 与开放世界覆盖仍开放。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新用户悖论／元数学原文。",
        "- direction_change: YES_IN_PLACE — CE-MAP 闭合，第一 successor 转 R3/R4 Gödel。",
        "- panorama_change: YES_IN_PLACE — 新增 CE-MAP scoped outcome。",
        "- essay_change: NO。",
        "- update_decision: 具名分母 COMP-3 与 internalisation pattern COMP-4 scoped 完成；根 Goal 未完成。",
        "- cross_conflicts: pattern reduction 不保持完整 consumer/task，不升级为等价类证明。",
        "- unresolved: 69 unknown、holdout、R3/R4、HoTT essentiality、经验现实、Oracle、物理时间与全面文献。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = [
        CE_DOC,
        R3_DOC,
        GOAL,
        FEATURE,
        PROGRAM_005,
        PROGRAM_006,
        PROGRAM_TEST,
        CE_MANAGER,
        CE_TEST,
        IMPORT_MANAGER,
        IMPORT_MANIFEST,
        IMPORT_CATALOG,
        CE_README,
        CE_MAP,
        CE_UNCLASSIFIED,
        CE_REPORT,
        CE_RECEIPT,
        AUDIT,
        PREPARE,
        LIT_CLASSICS_003,
        LIT_CLASSICS_005,
        LIT_HOTT_004,
        GROUP_SYNTAX_CLAIM,
        GROUP_SYNTAX_RUN,
        COQ_R3_REPORT,
        COQ_R3_BUILD,
        COQ_R3_SOURCE,
    ]
    missing = [path for path in required if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"S150_EVIDENCE_MISSING:{missing}")
    command_pass(["python3", "-B", IMPORT_MANAGER, "validate"], '"status": "VALID"')
    command_pass(["python3", "-B", CE_MANAGER, "validate", "--require-current-sources"], '"status": "VALID"')
    command_pass(["python3", "-B", CE_TEST], "Ran 7 tests")
    command_pass(["python3", "-B", PROGRAM_TEST], "Ran 5 tests")
    command_pass(["python3", "-B", "scripts/audit/verify_governance_shards.py"], '"status": "PASS"')

    receipt = json.loads((ROOT / CE_RECEIPT).read_text(encoding="utf-8"))
    mapping = json.loads((ROOT / CE_MAP).read_text(encoding="utf-8"))
    if (
        receipt.get("status") != "CE_MAP_V1_COMPLETE_WITH_SCOPE"
        or receipt.get("input_count") != 478
        or receipt.get("output_item_count") != 478
        or receipt.get("input_remainder") != 0
        or receipt.get("axis_cell_remainder") != 0
        or receipt.get("duplicate_ids") != 0
        or receipt.get("unclassified_count") != 69
        or mapping.get("selected_successor", {}).get("task") != "R3_R4_GODEL_RETURN_001"
    ):
        raise SystemExit("S150_CE_MAP_RECEIPT_INVALID")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 149 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_149_S149")
    if R3_ID in state["records"] or SESSION_ID in state["records"]:
        raise SystemExit("S150_RECORD_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    d2 = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][d2] = replace_line(
        direction["shards"][d2],
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`",
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 与根 `goal.md` 为唯一工作面推进计算合法性／不可停机／Gödel 到 HoTT 现实相对悖论；CE-MAP v1 已坐标化 revision-149 的 478 个具名输入并保留 69 unknown | 用户当前 App Goal；`goal.md`；F-011/F-015/F-016；CE receipt | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY`, `THEORY_ECONOMY` | `OUT-TOP-INTERNALISATION-CONSUMER-DEFENSE`、`OUT-TOP-CE-MAP-V1` | 当前做 `R3-R4-GODEL-RETURN-001`：先 exact R3 source replay，再连接 HoTT syntax/proof predicate/representability；保持 Oracle、ambient R2、物理时间与 reality 返回口 | `goal.md`；`audit/ce-map/REPORT.md`；R3/R4 TaskSpec |",
    )
    for old, new in (
        ("source_state_revision: 149", "source_state_revision: 150"),
        ("projection_generation: 20260915-direction-131", "projection_generation: 20260915-direction-132"),
        ("状态：`CORE_GENERATION_4_C188_C243_INTERNALISATION_CLASS_DEFENSE_WORKS_CE_MAP_NEXT`", f"状态：`{STATUS}`"),
        ("semantic_status: CORE_GENERATION_4_C188_C243_INTERNALISATION_CLASS_DEFENSE_WORKS_CE_MAP_NEXT", f"semantic_status: {STATUS}"),
        ("runtime 3.3.0 强制全片覆盖", "runtime 3.6.1 强制全片覆盖与 canonical table 顺序"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    p2 = "全景视野/002 - 治理、门禁与骨架结果.md"
    projection_edit.append_to_shard(
        panorama,
        p2,
        "| `OUT-TOP-CE-MAP-V1` | revision-149 的 proof/package/claim、non-session STATE 与 machine-overview task/case/evaluation/run/review 八轴 canonical map | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-G-CHECKPOINT-HYDRATION-INTEGRITY` | 当前 main CE-MAP manager/import | `CE_MAP_V1_COMPLETE_WITH_SCOPE / 478 ITEMS / 69 EXPLICIT UNKNOWN` | input remainder=0、axis remainder=0、duplicate=0；internalisation + defense 两个 pattern class；7/7 tests、两次独立重建一致 | 只证明具名 closed-world registration；pattern 非完整 task-preserving reduction；不证明 HoTT 悖论、开放世界完备或 Goal 完成 | `audit/ce-map/REPORT.md`；`audit/ce-map/RECEIPT.json`；`audit/CE-MAP机器统观八轴映射与同型归约-20260915.md` |\n",
    )
    for old, new in (
        ("source_state_revision: 149", "source_state_revision: 150"),
        ("projection_generation: 20260915-outcome-131", "projection_generation: 20260915-outcome-132"),
        ("状态：`CORE_GENERATION_4_C188_C243_INTERNALISATION_CLASS_DEFENSE_WORKS_CE_MAP_NEXT`", f"状态：`{STATUS}`"),
        ("semantic_status: CORE_GENERATION_4_C188_C243_INTERNALISATION_CLASS_DEFENSE_WORKS_CE_MAP_NEXT", f"semantic_status: {STATUS}"),
        ("runtime 3.3.0 强制全片覆盖", "runtime 3.6.1 强制全片覆盖与 canonical table 顺序"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    m1 = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][m1] = replace_once(
        memory["shards"][m1],
        "当前 App Goal 为短指针，根 `goal.md` 是唯一完整 objective owner。C-188–C-243 已在 main 形成 R1/R2、exact syntax 与 internalisation 正负链：2LTT R→UIP、LOPS classifier/crisp、ITT regular/degenerate+transport 均 exact replay。natural consumer 存在但受限接口保住任务；最终 HoTT witness 未找到。",
        "当前 App Goal 为短指针，根 `goal.md` 是唯一完整 objective owner。C-188–C-243 已形成 R1/R2、exact syntax 与 internalisation 正负链；CE-MAP v1 又把 478 个具名输入全部映射到八轴，保留 69 unknown并归约 internalisation/defense patterns。最终 HoTT witness 未找到。",
    )
    memory["shards"][m1] = replace_once(
        memory["shards"][m1],
        "当前仍未得到 ambient HoTT 无条件 no-decider、R3 independent sentence、完整 R4 calculus/incompleteness、E6、现实桥梁、`NATURAL_USAGE_MISMATCH` 或 HoTT 内部矛盾。17 个冻结 + 24 个 later package 只支持各自范围；新资产仍 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。",
        "当前仍未得到 ambient HoTT 无条件 no-decider、机器重放的 exact R3 independent sentence、完整 R4 calculus/incompleteness、E6、现实桥梁、`NATURAL_USAGE_MISMATCH` 或 HoTT 内部矛盾。CE-MAP v1 只关闭具名坐标化；17 个冻结 + 24 个 later package 只支持各自范围；新资产仍 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。",
    )
    memory["shards"][m1] = replace_once(
        memory["shards"][m1],
        "Post/Parametric CT/Oracle/groupoid-syntax、2LTT replacement 与 natural-consumer/支付消融均有 scoped evidence。当前优先 `CE-MAP-001`；并行保留 Oracle、ambient R2、完整 R4/Gödel、物理时间与 reality。未获授权不 push、不 tag。",
        "Post/Parametric CT/Oracle/groupoid-syntax、2LTT replacement、natural-consumer/支付消融与 CE-MAP v1 均有 scoped evidence。当前优先 `R3-R4-GODEL-RETURN-001`；并行保留 Oracle、ambient R2、物理时间与 reality。未获授权不 push、不 tag。",
    )
    m2 = "MEMORY/002 - 当前证据上限与恢复入口.md"
    memory["shards"][m2] = replace_once(
        memory["shards"][m2],
        "可计算性主线已有 C-188–C-218 的 R1/R2 基础与 synthetic reduction，C-219–C-222 又给显式 `EPF_bool + SCT` 前提下 internal `~decidable`；它不是 ambient HoTT 无条件结论。C-223–C-243 形成 syntax/internalisation/consumer/支付链。完整 R4/Gödel、ambient HoTT no-decider、CE-MAP、经验现实桥梁与学术全面覆盖均开放。",
        "可计算性主线已有 C-188–C-218 的 R1/R2 基础与 synthetic reduction，C-219–C-222 又给显式 `EPF_bool + SCT` 前提下 internal `~decidable`；它不是 ambient HoTT 无条件结论。C-223–C-243 形成 syntax/internalisation/consumer/支付链。CE-MAP v1 已关闭 revision-149 具名坐标化；完整 R3/R4 Gödel、ambient HoTT no-decider、经验现实桥梁与学术全面覆盖仍开放。",
    )
    memory["shards"][m2] = replace_once(
        memory["shards"][m2],
        "优先读第 006 片、`.codex/research/hott/LIT-HOTT-COMPUTABILITY-001.md` 全部 shards 和 `audit/imports/machine-overview-computability-20260914/IMPORT.json`；不依赖外部 worktree 才能恢复当前判词。",
        "优先读第 006 片、`.codex/research/hott/LIT-HOTT-COMPUTABILITY-001.md` 全部 shards、`audit/ce-map/README.md`/`REPORT.md`/`RECEIPT.json` 与 `R3-R4-GODEL-RETURN-001.md`；具体 map item 用 manager query，不全文预载 594KB JSON；不依赖外部 worktree 才能恢复当前判词。",
    )
    m3 = "MEMORY/003 - 当前验证状态与顺序日志.md"
    if not memory["shards"][m3].endswith("\n"):
        memory["shards"][m3] += "\n"
    memory["shards"][m3] += (
        "- S150 CE-MAP v1：只读冻结 machine-overview 169 文件；41 proof packages +186 claims +143 non-session STATE +108 machine artifacts=478/478，69 explicit unknown；input/axis/duplicate remainder=0；internalisation/defense pattern classes保留 anti-preservation；7/7 tests与独立重建一致。下一 `R3-R4-GODEL-RETURN-001`；Goal active。\n"
    )

    essay = projection_edit.load(ROOT, R.ESSAY)
    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(
        frontier,
        "# HoTT 研究前沿（S149 internalisation consumer/支付消融完成）",
        "# HoTT 研究前沿（S150 CE-MAP v1 具名坐标化完成）",
    )
    frontier = replace_once(
        frontier,
        "C-188–C-243 已在 main 形成 R2、syntax 与 internalisation 正负链。LOPS/ITT exact replay确认 global→local、fiberwise→familywise会坍缩 interval/推出 False；fibration universe、HIT、model structure、Reedy natural consumers真实，但 crisp、DFib+Trans、pointwise-fibrant限制完成来源任务。当前判 `DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT`，第一 successor=`CE-MAP-001`；ambient R2、完整 R4/Gödel、物理时间、经验 reality 与全面覆盖均 OPEN。",
        "C-188–C-243 已形成 R2、syntax 与 internalisation 正负链。CE-MAP v1 进一步登记 478 个具名输入、保留 69 unknown，并把 unqualified internalisation 归为一个带 anti-preservation 的 pattern；qualified defenses完成来源任务。第一 successor=`R3-R4-GODEL-RETURN-001`；ambient R2、完整 R4/Gödel、物理时间、经验 reality 与全面覆盖均 OPEN。",
    )
    frontier = replace_line(
        frontier,
        "| 当前高判别候选 |",
        "| 当前高判别候选 | R3/R4 Gödel：exact independent sentence→HoTT syntax/proof predicate/representability | `TASKSPEC_FROZEN / IMPLEMENTATION_NOT_STARTED` | 先重放作者 R3 package；逐项核 H-SYNTAX/H-NAT/H-PROOF-CODE/H-REPRESENTABILITY/H-FIXPOINT/H-INDEPENDENCE；一般机制与 HoTT essentiality消融 |",
    )
    lessons_path = ".codex/research/hott/LESSONS.md"
    lessons = (ROOT / lessons_path).read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n113. closed-world completeness 必须同时保存 denominator、canonical typed ID、显式 UNKNOWN 和 source snapshot；478/478 只说明具名输入登记完成，不等于开放世界穷尽。\n"
        "\n114. 类归约必须把 anti-preservation 写进 class：internalisation 三论文共享 scope-widening pattern，但 consumer、observation、completion 与 framework 不同；只能减少搜索重复，不能传播定理。\n"
        "\n115. machine-managed 巨型 registry 应通过 query/list 消费，报告与 receipt 负责水合；全文预载 594KB JSON 会破坏最小充分认知而不增加语义判断。\n"
        "\n116. Gödel 返回线必须先机器重放 exact R3，再逐义务连接 exact HoTT calculus。宿主语言里实现普通不完备性、一次 proof search 不返回、或通用 theorem 的 HoTT 实例都不能单独证明 HoTT essentiality。\n"
    )
    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\nS150：CE-MAP v1 已以 478/478、69 explicit unknown 完成 revision-149 具名八轴登记；169-file machine import、两个 pattern classes、7/7 tests、删 input/axis 负控制及独立进程重建均闭合。active=`A-R3-R4-GODEL-RETURN-001`：先 exact R3 source replay，再做 HoTT calculus 义务桥；Goal保持 active。\n\n",
    )

    state["revision"] = 150
    state["latest_session"] = SESSION_ID
    state["active"] = ["I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912", GOAL_ID, R3_ID]
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_CE_MAP_V1"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = (
        "Execute R3-SOURCE-REPLAY-001: qualify and replay one exact author incompleteness package, freeze its theorem and assumptions, then populate the R3-to-R4 HoTT calculus obligation matrix without claiming HoTT essentiality."
    )
    state["projection"]["status"] = STATUS
    for key, generation in (
        ("I-DIRECTION-PORTFOLIO-20260912", "20260915-direction-132"),
        ("I-OUTCOME-PANORAMA-20260912", "20260915-outcome-132"),
    ):
        state["records"][key]["projection_generation"] = generation
        state["records"][key]["semantic_status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Current portfolio through CE-MAP v1: 478 named inputs registered, 69 unknown retained, R3/R4 Gödel active, Goal open."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Integrated outcomes through CE-MAP v1; no open-world completeness, exact HoTT incompleteness, empirical bridge or final paradox."
    )

    ce_sources = [
        CE_DOC,
        CE_README,
        CE_REPORT,
        CE_RECEIPT,
        CE_MANAGER,
        CE_TEST,
        IMPORT_MANAGER,
        IMPORT_MANIFEST,
        IMPORT_CATALOG,
        AUDIT,
    ]
    ce_record = state["records"][CE_ID]
    ce_record["lifecycle_status"] = "CLOSED"
    ce_record["status"] = "complete"
    ce_record["evidence_status"] = "CE_MAP_V1_COMPLETE_WITH_SCOPE / VERIFIED_WITH_NEGATIVE_CONTROLS"
    ce_record["full_sources"] = ce_sources
    ce_record["source_hashes"] = file_hashes(ce_sources)
    ce_record["resolution"] = {
        "evidence": [CE_MAP, CE_RECEIPT, CE_REPORT, CE_TEST, AUDIT],
        "reason": "478 named inputs have unique canonical items and eight explicit axis cells; 69 unknowns are preserved; order/rebuild and deletion controls pass.",
    }
    ce_record["scope"] = (
        "Revision-149 named-input registration only: 478 items, 69 explicit unknown, two mechanism/defense pattern classes. No open-world or mathematical completeness claim."
    )
    ce_record["revalidation"] = (
        f"{SESSION_ID}: implementation replaced TASKSPEC_ACTIVE with CE_MAP_V1_COMPLETE_WITH_SCOPE; source evolution after checkpoint is reported separately from frozen artifact integrity."
    )
    ce_record["machine_managed_canonical"] = CE_MAP
    ce_record["query_command"] = "python3 -B scripts/audit/build_ce_map.py query --id <id>"
    ce_record["artifact_hashes"] = file_hashes([CE_MAP, CE_UNCLASSIFIED, CE_REPORT, CE_RECEIPT])
    add_once(ce_record.setdefault("related_records", []), R3_ID)
    add_once(ce_record["related_records"], SESSION_ID)

    r3_sources = [
        R3_DOC,
        CE_REPORT,
        CE_RECEIPT,
        GOAL,
        LIT_CLASSICS_003,
        LIT_CLASSICS_005,
        LIT_HOTT_004,
        GROUP_SYNTAX_CLAIM,
        GROUP_SYNTAX_RUN,
        COQ_R3_REPORT,
        COQ_R3_BUILD,
        COQ_R3_SOURCE,
    ]
    state["records"][R3_ID] = {
        "classification": "EXACT_R3_INDEPENDENT_SENTENCE_TO_HOTT_R4_FAITHFULNESS_BRIDGE",
        "depends_on": [],
        "evidence_status": "TASKSPEC_FROZEN / IMPLEMENTATION_NOT_STARTED",
        "full_sources": r3_sources,
        "kind": "candidate_search_task",
        "lifecycle_status": "ACTIVE_WORK",
        "path": R3_DOC,
        "research_parent": GOAL_ID,
        "related_records": [CE_ID, SYNTAX_ID, PLAN_ID, COVERAGE_ID, LIT_CLASSICS_ID, LIT_HOTT_ID, SESSION_ID],
        "scope": (
            "Replay one exact R3 incompleteness package, then map its effectivity/proof-code/representability/fixed-point obligations to a named HoTT calculus; keep generic Gödel, HoTT essentiality and reality correspondence distinct."
        ),
        "source_hashes": file_hashes(r3_sources),
        "status": "active",
    }

    for record_id in (GOAL_ID, PLAN_ID, COVERAGE_ID, LIT_CLASSICS_ID, LIT_HOTT_ID, SYNTAX_ID):
        record = state["records"][record_id]
        for related in (CE_ID, R3_ID, SESSION_ID):
            add_once(record.setdefault("related_records", []), related)
    goal_record = state["records"][GOAL_ID]
    for path in (GOAL, FEATURE, CE_DOC, CE_REPORT, CE_RECEIPT, R3_DOC, AUDIT):
        add_once(goal_record.setdefault("full_sources", []), path)
    goal_record["source_hashes"] = file_hashes(goal_record["full_sources"])
    goal_record["revalidation"] = (
        f"{SESSION_ID}: CE-MAP v1 closes named registration only; 69 unknown and all final witness gates remain. Goal stays active and moves to {R3_ID}."
    )
    plan_record = state["records"][PLAN_ID]
    for path in (PROGRAM_005, PROGRAM_006, CE_DOC, CE_REPORT, CE_RECEIPT, R3_DOC, AUDIT):
        add_once(plan_record.setdefault("full_sources", []), path)
    plan_record["source_hashes"] = file_hashes(plan_record["full_sources"])
    plan_record["evidence_status"] = "DOCUMENTED / CE_MAP_V1_MECHANICALLY_VERIFIED_WITH_SCOPE"
    plan_record["revalidation"] = (
        f"{SESSION_ID}: COMP-3 named denominator complete; internalisation COMP-4 is pattern-only with anti-preservation; COMP-5/6 remain open."
    )
    syntax_record = state["records"][SYNTAX_ID]
    add_once(syntax_record.setdefault("full_sources", []), R3_DOC)
    syntax_record["source_hashes"] = file_hashes(syntax_record["full_sources"])
    syntax_record["evidence_status"] = "FIRST_EXACT_SYNTAX_SLICE / R3_R4_GODEL_BRIDGE_ACTIVE / FULL_CALCULUS_OPEN"
    syntax_record["scope"] = (
        "C-223-C-226 groupoid syntax is exact; R3/R4 task now requires Nat, general Path/identity, derivation checker/enumerator, arithmetic interpretation, representability and fixed point."
    )
    syntax_record["revalidation"] = (
        f"{SESSION_ID}: CE-MAP selected this uncovered frontier; no new syntax or incompleteness theorem is claimed yet."
    )
    coverage_record = state["records"][COVERAGE_ID]
    for path in (CE_REPORT, CE_RECEIPT, R3_DOC, AUDIT):
        add_once(coverage_record.setdefault("full_sources", []), path)
    coverage_record["source_hashes"] = file_hashes(coverage_record["full_sources"])
    coverage_record["revalidation"] = (
        f"{SESSION_ID}: CE-MAP closes the named artifact denominator, not literature/open-world coverage; R3/R4 primary-source replay is next."
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session_text = f"""# {SESSION_ID}

- 工作单元：CE-MAP v1 八轴具名分母与 internalisation 同型类归约。
- machine import：169 files；14 tasks / 13 cases / 15 evaluations / 48 runs / 18 reviews；dirty external worktree byte snapshot。
- map：41 packages + 186 claims + 143 non-session STATE + 108 machine artifacts = 478；69 explicit unknown；remainder/duplicate/axis gap 均 0。
- classes：unqualified internalisation pattern 与 qualified defense pattern；anti-preservation 显式，不宣称完整任务等价。
- verification：7/7 tests；删 C-234/删 axis 负控制；正序/逆序、同进程/独立进程重建一致。
- 下一：`{R3_ID}`，先 exact R3 source replay，再做 R3→R4 HoTT calculus obligation bridge。
- Goal：active；Git：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；未 push、未 tag。
"""
    runs_text = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "machine_import": {
                "snapshot_id": "6dafaaba2cfe49032b8219f9c24e42c01bbdb9d124ff9e2ef918803f26785e00",
                "documents": 169,
                "status": "VALID",
            },
            "ce_map": {
                "source_snapshot": receipt["source_snapshot"],
                "items": 478,
                "unclassified": 69,
                "classes": 2,
                "status": "CE_MAP_V1_COMPLETE_WITH_SCOPE",
                "receipt": CE_RECEIPT,
            },
            "verification": {
                "ce_tests": "7/7 PASS",
                "program_tests": "5/5 PASS",
                "negative_controls": ["deleted_known_input", "deleted_axis_cell"],
                "determinism": receipt["determinism"],
            },
            "verdict": "NAMED_REGISTRATION_COMPLETE_OPEN_WORLD_AND_ROOT_GOAL_OPEN",
            "next": [R3_ID, "CLASSIFIER-REALITY-BRIDGE-001", "ORACLE-MODALITY-REPLAY-001", "R2-AMBIENT-UNDEC-001", "PHYSICAL-TIME-REALITY-001"],
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "CE_MAP_V1_COMPLETE_WITH_SCOPE / VERIFIED_WITH_NEGATIVE_CONTROLS",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, CE_REPORT, CE_RECEIPT, AUDIT],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV, GOAL_ID, PLAN_ID, CE_ID, R3_ID, SYNTAX_ID],
        "scope": "Close revision-149 CE-MAP named registration and activate R3/R4 without claiming open-world completeness or a final paradox.",
        "source_hashes": {},
        "status": "complete",
    }

    texts: dict[str, str] = {path: (ROOT / path).read_text(encoding="utf-8") for path in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[frontier_path] = frontier
    texts[lessons_path] = lessons
    texts[resume_path] = resume
    texts[session_path] = session_text
    texts[audit_path] = audit_text()
    texts[runs_path] = runs_text

    changed = [
        GOAL,
        FEATURE,
        PROGRAM_005,
        PROGRAM_006,
        CE_DOC,
        R3_DOC,
        CE_REPORT,
        CE_RECEIPT,
        CE_MANAGER,
        CE_TEST,
        IMPORT_MANAGER,
        IMPORT_MANIFEST,
        IMPORT_CATALOG,
        AUDIT,
        *texts.keys(),
    ]
    for record in state["records"].values():
        source_hashes = record.get("source_hashes") if isinstance(record, dict) else None
        if not isinstance(source_hashes, dict):
            continue
        rebound = []
        for path in changed:
            if path not in source_hashes or path == R.STATE:
                continue
            data = texts[path].encode("utf-8") if path in texts else (ROOT / path).read_bytes()
            value = R.sha(data)
            if source_hashes[path] != value:
                source_hashes[path] = value
                rebound.append(path)
        if rebound and record not in (ce_record, state["records"][R3_ID]):
            note = (
                f"{SESSION_ID}: revalidated current owner evolution at {', '.join(rebound)}; prior mathematical scopes remain unchanged."
            )
            previous = record.get("revalidation")
            record["revalidation"] = f"{previous} {note}" if isinstance(previous, str) and previous else note

    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "Continue the active root goal.md autonomously and maintain project governance/evidence continuity across compaction boundaries."
        ),
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": path,
                "expected_sha256": R.sha((ROOT / path).read_bytes()) if (ROOT / path).exists() else None,
                "text": value,
            }
            for path, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PREPARED",
                "snapshot": plan["snapshot"],
                "revision": 150,
                "session_id": SESSION_ID,
                "files": len(texts),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
