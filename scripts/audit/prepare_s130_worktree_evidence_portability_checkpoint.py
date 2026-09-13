#!/usr/bin/env python3
"""Prepare revision 130: route current evidence through tracked worktree inputs."""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-130-WORKTREE-EVIDENCE-PORTABILITY"
PREV = "S-GOV-20260913-129-DUAL-TRACK-COMMUNICATION-CONTRACT"
RESULT_ID = "A-WORKTREE-EVIDENCE-PORTABILITY-001"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_1_WORKTREE_PORTABILITY_PENDING_FRESH"
CONTRACT = "docs/quality/Git多Worktree证据可移植性合同.md"
IMPORT_RECEIPT = "audit/worktree-portability-source-import-20260913.json"
MERGE_MANIFEST = "audit/understanding-chapter-merge-manifest.json"
SOURCE_MANIFEST = "sources/SOURCE_MANIFEST.json"
IMPORT_MANAGER = "scripts/audit/import_worktree_portability_sources.py"
MERGE_BUILDER = "scripts/audit/build_understanding_merge_manifest.py"
MERGE_VERIFIER = "scripts/audit/verify_understanding_merge.py"
FRESH_VERIFIER = "scripts/audit/verify_fresh_three_way.py"
FEATURES = "feature-list.md"
RULINGS = "rulings.md"
PROJECT_AGENTS = "AGENTS.md"
LOCAL_SKILL = ".codex/skills/hott-local-session-governance/SKILL.md"
PROTOCOL = ".codex/cognition/PROTOCOL.md"
LOAD_SET = ".codex/cognition/LOAD_SET.json"
SOURCE_COMMIT = "80da06ead06f38bc87ec8ebe7c82f72865401308"
STATIC_COMMIT = "d58dbfdbb4dd1f71c192801f57f49cfacc288933"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s130", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_line(text: str, marker: str, replacement: str) -> str:
    lines = text.splitlines()
    matches = [index for index, line in enumerate(lines) if line.startswith(marker)]
    if len(matches) != 1:
        raise ValueError(f"LINE_MATCH_COUNT:{marker}:{len(matches)}")
    lines[matches[0]] = replacement
    return "\n".join(lines) + "\n"


def insert_before(text: str, marker: str, value: str) -> str:
    if text.count(marker) != 1:
        raise ValueError(f"INSERT_MARKER_COUNT:{marker}:{text.count(marker)}")
    return text.replace(marker, value.rstrip("\n") + "\n\n" + marker, 1)


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def append_revalidation(record: dict, note: str) -> None:
    old = str(record.get("revalidation", "")).strip()
    record["revalidation"] = (old + " " + note).strip()


def git_tracked() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "-z"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=True,
    )
    return {item for item in result.stdout.split("\0") if item}


def prepend_queue_item(text: str, item: str) -> str:
    heading = "## 当前执行队列（2026-09-13）\n"
    if text.count(heading) != 1:
        raise ValueError("CURRENT_QUEUE_HEADING")
    lines = text.splitlines()
    start = lines.index("## 当前执行队列（2026-09-13）") + 1
    end = next(
        (index for index in range(start, len(lines)) if lines[index].startswith("-") or lines[index].startswith("## ")),
        len(lines),
    )
    for index in range(start, end):
        match = re.match(r"^(\d+)\. (.*)$", lines[index])
        if match:
            lines[index] = f"{int(match.group(1)) + 1}. {match.group(2)}"
    insert_at = start
    while insert_at < len(lines) and not lines[insert_at].strip():
        insert_at += 1
    lines.insert(insert_at, f"1. {item}")
    return "\n".join(lines) + "\n"


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000001": ("ALIGNED", "把目标、来源岛、路由迁移和 fresh 验收分别写成可检查合同。"),
        "KC-000007": ("DEEPENED", "主 checkout 的 PASS 被 fresh linked worktree 反例纠正，判断回到 tracked bytes 与实际命令。"),
        "KC-000010": ("ALIGNED", "本轮是认知证据可恢复性修复，不产生 HoTT 内部矛盾或现实相对结论。"),
        "KC-000012": ("DEEPENED", "task hydration 的合法输入从路径存在提升为 tracked/pinned 且可在 fresh worktree 恢复。"),
        "KC-000017": ("ALIGNED", "不以旧主 checkout 经验覆盖新 worktree 的直接失败证据。"),
        "KC-000021": ("ALIGNED", "导入逐字节、manifest/hash、正负控制和 checkpoint/fresh 验收分层保存。"),
        "KC-000022": ("ALIGNED", "修复只恢复研究证据入口，不改变 A/B 两类悖论目标或现有判词。"),
        "KC-000029": ("DEEPENED", "防止治理框架以 checkout-local 隐含成本换取表面 PASS。"),
        "KC-000030": ("DEEPENED", "理论经济统观的证据供给被要求可版本恢复，避免当前账本依赖未提交历史源。"),
        "KC-000035": ("ALIGNED", "更可靠的证据加载支撑表达能力研究，但本轮不扩大 HoTT 可表达性结论。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮只修复 Git worktree 证据可移植性，不启动数学研究。",
        "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = focus.get(
            kid,
            ("NOT_TOUCHED", f"本轮没有重新研究或裁决“{label}”的数学、物理或哲学内容。"),
        )
        lines.append(
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{CONTRACT}`；{kid} | "
            "fresh linked-worktree 最终验收尚待 revision 130 commit 后执行。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 本轮用户指令是治理实施授权，不是新的悖论/元数学原文。",
        "- direction_change: YES_IN_PLACE — 新增 worktree evidence portability 方向并改 tracked source 路由。",
        "- panorama_change: YES_IN_PLACE — 登记 byte snapshot、manifest v2、8 条 record 路由和 pending fresh 验收。",
        "- essay_change: NO — 第四件不变。",
        "- update_decision: current 决定性证据必须 tracked/pinned；ignored working tree 只作 provenance/import source。",
        "- cross_conflicts: 主 checkout 6/6 与 linked worktree 4/6 的冲突已由 checkout-local input 解释。",
        "- unresolved: revision 130 commit 后仍须在一个全新 linked worktree 跑五个 task plans、六类 verifier 和负向控制。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = [
        CONTRACT,
        IMPORT_RECEIPT,
        MERGE_MANIFEST,
        SOURCE_MANIFEST,
        IMPORT_MANAGER,
        MERGE_BUILDER,
        MERGE_VERIFIER,
        FRESH_VERIFIER,
        FEATURES,
        RULINGS,
        PROJECT_AGENTS,
        LOCAL_SKILL,
        PROTOCOL,
        LOAD_SET,
    ]
    tracked = git_tracked()
    for rel in required:
        if not (ROOT / rel).is_file():
            raise SystemExit(f"MISSING:{rel}")
        if rel not in tracked:
            raise SystemExit(f"NOT_TRACKED:{rel}")
    if subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() != STATIC_COMMIT:
        raise SystemExit("STATIC_COMMIT_NOT_HEAD")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 129 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_129_S129")
    if RESULT_ID in state["records"] or SESSION_ID in state["records"]:
        raise SystemExit("S130_ID_ALREADY_EXISTS")

    old_prefix = "workspace/"
    new_prefix = "sources/webgpt/workspace-snapshot/"
    replaced_refs: list[tuple[str, str, str]] = []
    for record_id, record in state["records"].items():
        sources = record.get("full_sources", [])
        if not isinstance(sources, list):
            continue
        rewritten: list[str] = []
        for rel in sources:
            if isinstance(rel, str) and rel.startswith(old_prefix):
                new_rel = new_prefix + rel[len(old_prefix):]
                if not (ROOT / new_rel).is_file() or new_rel not in tracked:
                    raise SystemExit(f"WORKSPACE_TRACKED_REPLACEMENT_MISSING:{record_id}:{rel}:{new_rel}")
                if (Path("/Volumes/D/HoTT_AI_HANDOFF_20260911") / rel).read_bytes() != (ROOT / new_rel).read_bytes():
                    raise SystemExit(f"WORKSPACE_TRACKED_REPLACEMENT_DIFFERS:{record_id}:{rel}:{new_rel}")
                rewritten.append(new_rel)
                replaced_refs.append((record_id, rel, new_rel))
                record.setdefault("source_hashes", {})[new_rel] = R.sha((ROOT / new_rel).read_bytes())
                record["source_hashes"].pop(rel, None)
            else:
                rewritten.append(rel)
        record["full_sources"] = rewritten
    if len(replaced_refs) != 8 or len({old for _, old, _ in replaced_refs}) != 6:
        raise SystemExit(f"WORKSPACE_REFERENCE_COUNT:{len(replaced_refs)}:{len({old for _, old, _ in replaced_refs})}")
    for record_id in sorted({record_id for record_id, _, _ in replaced_refs}):
        count = sum(1 for candidate, _, _ in replaced_refs if candidate == record_id)
        append_revalidation(
            state["records"][record_id],
            f"{SESSION_ID} replaced {count} ignored workspace full-source path(s) with byte-identical top-level tracked workspace-snapshot paths; claim and evidence status are unchanged.",
        )

    aistudio = state["records"]["A-AISTUDIO-COVERAGE-001"]
    legacy_local = "sources/local-gpt/ALL-Markdown-root/HoTT_is_GONE_COMPLETE.md"
    tracked_local = "sources/local-gpt/HoTT_is_GONE_COMPLETE.md"
    if legacy_local not in aistudio["full_sources"] or tracked_local not in aistudio["full_sources"]:
        raise SystemExit("AISTUDIO_EXPECTED_DUAL_PATHS_MISSING")
    aistudio["full_sources"] = [path for path in aistudio["full_sources"] if path != legacy_local]
    aistudio.setdefault("source_hashes", {})[tracked_local] = R.sha((ROOT / tracked_local).read_bytes())
    append_revalidation(
        aistudio,
        f"{SESSION_ID} removed the ignored duplicate full-source route after byte identity was recorded in {IMPORT_RECEIPT}; coverage remains NOT_PROVEN.",
    )

    new_merge_hash = R.sha((ROOT / MERGE_MANIFEST).read_bytes())
    merge_repins = 0
    for record in state["records"].values():
        hashes = record.get("source_hashes", {})
        if MERGE_MANIFEST in hashes:
            hashes[MERGE_MANIFEST] = new_merge_hash
            append_revalidation(
                record,
                f"{SESSION_ID} re-pinned the v2 merge manifest after moving its historical side to the tracked 42-file transform snapshot; mathematical scope is unchanged.",
            )
            merge_repins += 1
    if merge_repins != 14:
        raise SystemExit(f"MERGE_REPIN_COUNT:{merge_repins}")

    for rel, expected_count, note in (
        ("理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md", 3, "tracked RP-B01/transition source locators"),
        ("理解章节/C9-W51命题化与RP-B01层映射-20260912.md", 2, "tracked RP-B01 source locators"),
        (PROJECT_AGENTS, 1, "project worktree-evidence portability rule"),
    ):
        new_hash = R.sha((ROOT / rel).read_bytes())
        count = 0
        for record in state["records"].values():
            hashes = record.get("source_hashes", {})
            if rel in hashes:
                hashes[rel] = new_hash
                append_revalidation(record, f"{SESSION_ID} re-pinned {rel} after updating {note}; claim scope is unchanged.")
                count += 1
        if count != expected_count:
            raise SystemExit(f"STATIC_REPIN_COUNT:{rel}:{count}:{expected_count}")

    understanding = state["records"]["A-UNDERSTANDING-RECONCILIATION-001"]
    for rel in (CONTRACT, IMPORT_RECEIPT, MERGE_BUILDER, MERGE_VERIFIER, SOURCE_MANIFEST):
        add_once(understanding["full_sources"], rel)
    understanding["source_hashes"] = {
        MERGE_MANIFEST: new_merge_hash,
        CONTRACT: R.sha((ROOT / CONTRACT).read_bytes()),
        IMPORT_RECEIPT: R.sha((ROOT / IMPORT_RECEIPT).read_bytes()),
        MERGE_BUILDER: R.sha((ROOT / MERGE_BUILDER).read_bytes()),
        MERGE_VERIFIER: R.sha((ROOT / MERGE_VERIFIER).read_bytes()),
        SOURCE_MANIFEST: R.sha((ROOT / SOURCE_MANIFEST).read_bytes()),
    }
    understanding["scope"] = (
        "File-level reconciliation is complete and non-destructive for the current 36/24 inventory "
        "(24 same-name pairs, 15 identical, 9 different, 12 top-only). The historical side is a "
        "top-level tracked 42-file transform snapshot; semantic equivalence and 2,396 historical claim review remain open."
    )
    append_revalidation(
        understanding,
        f"{SESSION_ID} migrated the historical directory from an ignored nested working tree to a tracked byte snapshot and upgraded the manifest/verifier to v2 path, tracked-file and source-tree checks.",
    )

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction_shard = "方向追踪/004 - 证据与覆盖方向及 STATE 覆盖表.md"
    direction["shards"][direction_shard] = replace_line(
        direction["shards"][direction_shard],
        "| `DIR-G-UNDERSTANDING-RECONCILIATION`",
        "| `DIR-G-UNDERSTANDING-RECONCILIATION` | 两个理解章节的逐文件语义融合和当前 canonical 路由 | 用户当前要求、顶层计划 | `SUPPORTING_DIRECTION` | `CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-UNDERSTANDING-MERGE`（设计） | 当前 36/24 inventory 已逐文件处置；历史侧改为 top-level tracked 42-file transform snapshot；继续按 2,396 条历史 claim 的用户选择范围做直接语义/数学复核 | `理解章节/`；`sources/understanding-transform/AI对话录/理解章节/`；`audit/understanding-chapter-merge-manifest.json` |",
    )
    new_direction_row = (
        "| `DIR-G-WORKTREE-EVIDENCE-PORTABILITY` | current hydration/verifier 的决定性证据在任意 linked worktree 由顶层 tracked snapshot/file 恢复 | 用户 ruling §22；本轮 4/6 worktree 反例 | `ACTIVE_IMPLEMENTATION_PENDING_FRESH_ACCEPTANCE` | `CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-G-WORKTREE-EVIDENCE-PORTABILITY` | revision 130 commit 后创建无 ignored islands 的 fresh linked worktree，跑 5 task plans、6 canonical verifiers 与 4 个负向控制 | `docs/quality/Git多Worktree证据可移植性合同.md`；`audit/worktree-portability-source-import-20260913.json` |"
    )
    direction["shards"][direction_shard] = insert_before(
        direction["shards"][direction_shard], "## 4. WebGPT `STATE` 全记录覆盖表", new_direction_row
    )
    direction["shards"]["方向追踪/003 - LocalGPT 与 WebGPT 方向.md"] = direction["shards"][
        "方向追踪/003 - LocalGPT 与 WebGPT 方向.md"
    ].replace("`workspace/", "`sources/webgpt/workspace-snapshot/")
    direction["shards"][direction_shard] = direction["shards"][direction_shard].replace(
        "`workspace/.codex/research/hott/STATE.json`", "`sources/webgpt/workspace-snapshot/.codex/research/hott/STATE.json`"
    )
    for old, new in (
        ("source_state_revision: 129", "source_state_revision: 130"),
        ("projection_generation: 20260913-direction-111", "projection_generation: 20260913-direction-112"),
        ("semantic_status: CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_COMMUNICATION_CONTRACT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_COMMUNICATION_CONTRACT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    panorama_governance = "全景视野/002 - 治理、门禁与骨架结果.md"
    projection_edit.append_to_shard(
        panorama,
        panorama_governance,
        f"| `OUT-G-WORKTREE-EVIDENCE-PORTABILITY` | ignored evidence island 迁移：42 文件 transform snapshot 纳入顶层 Git；8 个 workspace refs 与 LocalGPT artifact 改 tracked 路由；manifest/verifier 加 path/tracked/tree 检查 | `DIR-G-WORKTREE-EVIDENCE-PORTABILITY`、`DIR-G-UNDERSTANDING-RECONCILIATION` | 用户 ruling §22 + linked-worktree 4/6 反例 + 本轮 implementation commits | `IMPLEMENTED_LOCAL / FRESH_LINKED_WORKTREE_PENDING` | import 42/42、workspace 6/6（8 refs）、LocalGPT 同字节映射与 understanding 36/24 本 worktree PASS；pre-checkpoint fresh 精确拒绝旧路径 | 尚未证明候选 commit 在全新 linked worktree 6/6；不改变数学 claim、aistudio coverage 或双轨研究判词 | `docs/quality/Git多Worktree证据可移植性合同.md`；`audit/worktree-portability-source-import-20260913.json`；`{SESSION_REL}/` |",
    )
    history_shard = "全景视野/007 - 历史来源结果与关系.md"
    panorama["shards"][history_shard] = replace_line(
        panorama["shards"][history_shard],
        "| `OUT-UNDERSTANDING-MERGE`",
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录当前为 36/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C11 共 12 个独有文件（nonidentical union entries=21）；逐文件处置已生成 | `DIR-G-UNDERSTANDING-RECONCILIATION`、`DIR-G-WORKTREE-EVIDENCE-PORTABILITY` | 顶层只读审计 + tracked source migration | `VERIFIED_WITH_SCOPE / TRACKED_HISTORICAL_SOURCE` | 每个 union 文件有 hash、line diff、处置决定和 rollback；历史侧 24 文件来自 SOURCE_MANIFEST 固定并纳入顶层 Git 的 42-file transform snapshot | 不推出数学内容等价；2,396 条旧 claim 未全量裁决；fresh linked-worktree 全套验收仍待 revision 130 commit | `audit/understanding-chapter-merge-manifest.json`；`scripts/audit/verify_understanding_merge.py`；`理解章节/`；`sources/understanding-transform/AI对话录/理解章节/` |",
    )
    panorama["shards"][history_shard] = panorama["shards"][history_shard].replace(
        "`workspace/", "`sources/webgpt/workspace-snapshot/"
    )
    for old, new in (
        ("source_state_revision: 129", "source_state_revision: 130"),
        ("projection_generation: 20260913-outcome-111", "projection_generation: 20260913-outcome-112"),
        ("semantic_status: CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_COMMUNICATION_CONTRACT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_GOVERNANCE_V4_DUAL_TRACK_COMMUNICATION_CONTRACT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    memory_shard = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][memory_shard] = prepend_queue_item(
        memory["shards"][memory_shard],
        "用户已授权本分支实施 Git worktree 证据可移植性修复（F-016）：42-file transform snapshot 与 tracked 路由已落盘，revision 130 将改 STATE/投影；当前完成条件仍是从该 commit 新建无 ignored islands 的 linked worktree并通过 5 task plans、6 canonical verifiers 与负向控制。",
    )
    memory["shards"][memory_shard] = memory["shards"][memory_shard].replace(
        "runtime 3.6.0 / LOAD_SET v4 / PROTOCOL v2.6",
        "runtime 3.6.0 / LOAD_SET 4.1 / PROTOCOL v2.7 / local Skill 3.7",
        1,
    )
    memory["shards"][memory_shard] = memory["shards"][memory_shard].replace(
        "本 Codex task 启动 cwd 是 detached `eb7b` 审计 worktree（`fc79094a…`），但 S 轨 current 项目写入根是 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 的 `main`；所有 current 修改均以显式 workdir 执行原项目治理。",
        "本 Codex task 启动 cwd 是 detached `eb7b` 审计 worktree（`fc79094a…`）；用户现已授权在 `/Volumes/D/HoTT-semantic-overview` 的 `codex/semantic-overview` 分支完成 F-016 候选修复，canonical target `main` 仍未合并。",
        1,
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S130 worktree evidence portability（implementation checkpoint）：用户授权把 linked worktree 4/6 反例修成可恢复输入。source commit `80da06e…` 将 SOURCE_MANIFEST 固定的 42-file transform snapshot 按字节纳入顶层 Git；static commit `d58dbfd…` 加入 F-016/ruling §22、项目合同、AGENTS/Skill 3.7/PROTOCOL 2.7/LOAD_SET 4.1、understanding manifest v2 和 tracked-input/five-task fresh verifier。STATE 的 8 个 `workspace/**` refs 改为已有同字节 `sources/webgpt/workspace-snapshot/**`，A-AISTUDIO 删除 ignored 重复路径。当前本 worktree import 42/42、workspace 6/6 与 merge 36/24 PASS；revision 130 commit 后仍须 fresh linked-worktree 正负验收，故状态保持 PENDING_FRESH。无新数学 claim。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = frontier.replace(
        "# HoTT 研究前沿（S127 统观双轨）\n\n",
        "# HoTT 研究前沿（S130 worktree evidence portability）\n\nS130 只修复研究证据在 linked worktree 的可恢复性；S/B/M 研究分工、候选优先级、数学 claim 与 ERCF-3 `GATED` 均不变。revision 130 commit 后先完成 fresh-worktree 验收，再恢复 S 轨自然 consumer 主线。\n\n",
        1,
    )

    lessons_path = ".codex/research/hott/LESSONS.md"
    lessons = (ROOT / lessons_path).read_text(encoding="utf-8").rstrip("\n") + (
        "\n\n98. Git worktree 只复制顶层 tracked blobs；主 checkout 中 ignored nested repo/working bytes 的存在不能支持可移植 PASS。本轮 4/6 反例说明，stable-record 路径、manifest source directory 和 verifier 输入都要检查 tracked/pinned 身份。修复时先找已有同字节 tracked snapshot，只有真正缺失的 42-file transform 才做 byte import；历史 bytes 的 trailing whitespace 用 hash 验收，不能为了 `diff --check` 改写。\n"
    )

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = resume.replace(
        "## 当前停止点\n\n",
        "## 当前停止点\n\nS130：worktree evidence portability implementation checkpoint 已准备。42-file historical transform 已 tracked；8 个 workspace full-source refs 与 A-AISTUDIO ignored duplicate 已改路由；understanding manifest v2 和 fresh verifier 扩展已落账。当前状态 PENDING_FRESH：必须从 revision 130 commit 新建无 ignored islands 的 linked worktree，跑 5 task plans、6 canonical verifiers 与负向控制，之后才能关闭 F-016。数学研究状态不变。\n\n",
        1,
    )

    state["revision"] = 130
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_WORKTREE_PORTABILITY_PENDING_FRESH"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = (
        "Commit revision 130, create a new detached linked worktree without copying ignored source islands, "
        "run import verification, five portability task plans, six canonical verifiers and four negative controls; "
        "only then close F-016. Mathematical research queue is unchanged."
    )
    state["projection"]["status"] = STATUS
    direction_record = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_record["projection_generation"] = "20260913-direction-112"
    direction_record["semantic_status"] = STATUS
    for rel in (CONTRACT, IMPORT_RECEIPT):
        add_once(direction_record["full_sources"], rel)
    panorama_record = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_record["projection_generation"] = "20260913-outcome-112"
    panorama_record["semantic_status"] = STATUS
    for rel in (CONTRACT, IMPORT_RECEIPT, MERGE_MANIFEST):
        add_once(panorama_record["full_sources"], rel)

    state["records"][RESULT_ID] = {
        "classification": "WORKTREE_EVIDENCE_PORTABILITY_IMPLEMENTED_PENDING_FRESH",
        "depends_on": [],
        "evidence_status": "IMPLEMENTED_LOCAL_PENDING_FRESH_WORKTREE",
        "full_sources": [
            CONTRACT,
            IMPORT_RECEIPT,
            MERGE_MANIFEST,
            SOURCE_MANIFEST,
            IMPORT_MANAGER,
            MERGE_BUILDER,
            MERGE_VERIFIER,
            FRESH_VERIFIER,
            FEATURES,
            RULINGS,
            PROJECT_AGENTS,
            LOCAL_SKILL,
            PROTOCOL,
            LOAD_SET,
        ],
        "kind": "governance_portability_result",
        "lifecycle_status": "OPEN_ISSUE",
        "path": CONTRACT,
        "related_records": [SESSION_ID, "A-UNDERSTANDING-RECONCILIATION-001", "A-AISTUDIO-COVERAGE-001"],
        "scope": (
            "Project-local implementation that replaces checkout-local decisive evidence with tracked files/snapshots: "
            "42 imported transform files, 8 workspace reference rewrites over 6 unique files, one LocalGPT duplicate route removal, "
            "understanding manifest v2, tracked input checks and five-task fresh coverage. Local checks pass; exact-commit fresh linked-worktree acceptance remains pending."
        ),
        "source_hashes": {
            CONTRACT: R.sha((ROOT / CONTRACT).read_bytes()),
            IMPORT_RECEIPT: R.sha((ROOT / IMPORT_RECEIPT).read_bytes()),
            MERGE_MANIFEST: new_merge_hash,
            SOURCE_MANIFEST: R.sha((ROOT / SOURCE_MANIFEST).read_bytes()),
            IMPORT_MANAGER: R.sha((ROOT / IMPORT_MANAGER).read_bytes()),
            MERGE_BUILDER: R.sha((ROOT / MERGE_BUILDER).read_bytes()),
            MERGE_VERIFIER: R.sha((ROOT / MERGE_VERIFIER).read_bytes()),
            FRESH_VERIFIER: R.sha((ROOT / FRESH_VERIFIER).read_bytes()),
        },
        "status": "review_required",
    }
    add_once(state["review_due"], RESULT_ID)
    add_once(state["unresolved"], RESULT_ID)

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户授权：在看到 linked worktree 4/6 与三个 ignored evidence islands 后，用户明确要求“你把这事做了吧”（ruling §22）。
- 目标：让 current hydration 与 canonical verifier 的决定性输入由顶层 tracked file/snapshot 恢复；不依赖主 checkout ignored working tree。
- source baseline：`{SOURCE_COMMIT}`；42-file transform snapshot 按 SOURCE_MANIFEST hash 导入，旧 nested bytes 未改。
- static implementation：`{STATIC_COMMIT}`；合同、Feature/ruling、AGENTS/Skill/PROTOCOL/LOAD_SET、manifest v2 与 verifiers 已提交。
- 路由：8 个 `workspace/**` refs（6 unique）改到 `sources/webgpt/workspace-snapshot/**`；A-AISTUDIO 删除 ignored 同字节重复路径；understanding historical side 改 tracked transform snapshot。
- 当前证据：import 42/42 PASS；workspace 6/6 / 8 refs PASS；understanding 36/24 PASS；governance shards 与 three-way rev129 PASS；pre-checkpoint fresh 对旧 LocalGPT path fail closed。
- 完成边界：本 checkpoint 只登记 IMPLEMENTED_LOCAL_PENDING_FRESH；必须 commit 后从 exact OID 新建无 ignored islands 的 linked worktree做正负验收。
- 非目标：不修改原 nested repos，不恢复 aistudio-docs，不改变数学 claim/研究判词，不 merge main，不 push/tag，不修改 machine-overview worktree。

## C01–C10 固定影响闭包

- C01 `UPDATE`：ruling §22、F-016 与验收状态已新增。
- C02 `UPDATE_PROJECT_ONLY`：新增项目证据可移植性合同；共享 `/Users/aurolafly/codex` 当前有其它未提交治理工作，本修复不混入该 repo，shared contract 后续独立审查。
- C03 `UPDATE`：项目 PROTOCOL v2.7、local governance Skill 3.7、LOAD_SET 4.1 与 source/merge managers 已同步。
- C04 `UPDATE`：项目 AGENTS 新增 `WORKTREE_EVIDENCE_PORTABILITY_V1`；全局 AGENTS 不变。
- C05 `UPDATE`：README、docs/source maps、current understanding evidence locators 与 replacement routes 已更新。
- C06 `UPDATE`：understanding verifier 增加 path/tracked/tree checks；fresh verifier覆盖五个 portability tasks；正负/fresh验收已固定。
- C07 `NO_CHANGE`：Codex config、Rules/Hooks/plugins、权限和 secret 边界未改变。
- C08 `NOT_APPLICABLE`：没有产品专属 host adapter 或 OpenCode runtime 变化。
- C09 `UPDATE_CANDIDATE`：source/static commits 已固定；revision 130 待提交；contributor branch 不创建共享 tag、不 push。
- C10 `UPDATE`：旧 ignored 路径保留为 provenance，历史 checkpoint/receipt 不改；完整 1,209-file ALL-Markdown snapshot 与 shared-generic follow-up 保持显式边界。
- remainder：`0`。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "source_commit": SOURCE_COMMIT,
            "static_implementation_commit": STATIC_COMMIT,
            "pre_checkpoint": {
                "import_verify": {"status": "PASS", "copied_files": 42, "workspace_mappings": 6, "workspace_references": 8},
                "understanding_merge": {"status": "PASS", "union": 36, "nested": 24, "identical": 15, "different": 9},
                "governance_shards": "PASS",
                "three_way_revision_129": "PASS",
                "fresh_expected_negative": "MISSING_OR_UNREADABLE:sources/local-gpt/ALL-Markdown-root/HoTT_is_GONE_COMPLETE.md",
            },
            "workspace_reference_rewrites": len(replaced_refs),
            "workspace_unique_files": len({old for _, old, _ in replaced_refs}),
            "merge_manifest_repins": merge_repins,
            "fresh_linked_worktree": "PENDING_AFTER_COMMIT",
            "new_math_claims": [],
            "nested_repo_mutation": "NONE",
            "machine_worktree_mutation": "NONE",
            "main_merge": "NOT_PERFORMED",
            "push": "NOT_AUTHORIZED",
            "tag": "NOT_CREATED_CONTRIBUTOR_BRANCH",
        },
        ensure_ascii=False,
        sort_keys=True,
        indent=2,
    ) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "IMPLEMENTED_LOCAL_PENDING_FRESH_WORKTREE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, CONTRACT, IMPORT_RECEIPT, MERGE_MANIFEST],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV, RESULT_ID],
        "scope": "Revision 130 implementation checkpoint for tracked/pinned worktree evidence; final fresh linked-worktree acceptance remains pending; no mathematical change.",
        "source_hashes": {},
        "status": "complete",
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[frontier_path] = frontier
    texts[lessons_path] = lessons
    texts[resume_path] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text(ROOT)
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "Implement the user-requested project worktree-evidence portability repair on the candidate branch. "
            "Record implementation as pending exact-commit fresh linked-worktree acceptance; do not merge main, push, tag, or mutate ignored nested repos."
        ),
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None,
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
                "revision": 130,
                "session_id": SESSION_ID,
                "files": len(texts),
                "workspace_references": len(replaced_refs),
                "merge_repins": merge_repins,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
