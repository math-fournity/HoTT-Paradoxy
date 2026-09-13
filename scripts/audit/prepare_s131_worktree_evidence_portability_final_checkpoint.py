#!/usr/bin/env python3
"""Prepare revision 131: close the worktree portability result after fresh acceptance."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-131-WORKTREE-PORTABILITY-FRESH-ACCEPTANCE"
PREV = "S-GOV-20260913-130-WORKTREE-EVIDENCE-PORTABILITY"
RESULT_ID = "A-WORKTREE-EVIDENCE-PORTABILITY-001"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V4_1_WORKTREE_PORTABILITY_VERIFIED"
CONTRACT = "docs/quality/Git多Worktree证据可移植性合同.md"
IMPORT_RECEIPT = "audit/worktree-portability-source-import-20260913.json"
ACCEPTANCE_RECEIPT = "audit/worktree-portability-fresh-acceptance-20260913.json"
ACCEPTANCE_REPORT = "audit/Git-worktree证据可移植性修复与验收-20260913.md"
MERGE_MANIFEST = "audit/understanding-chapter-merge-manifest.json"
FEATURES = "feature-list.md"
ACCEPTANCE_COMMIT = "a8e948d119c60e88180ffd7f749535be85bed69f"
TESTED_COMMIT = "802e4f890f07adeb50d32f7d8a3e1866d8d8d597"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s131", RUNTIME_PATH)
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


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def append_revalidation(record: dict, note: str) -> None:
    old = str(record.get("revalidation", "")).strip()
    record["revalidation"] = (old + " " + note).strip()


def remove_once(values: list[str], item: str) -> None:
    while item in values:
        values.remove(item)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000001": ("ALIGNED", "fresh worktree 正向与四类负向结果把治理完成判据落实为可复核证据。"),
        "KC-000007": ("DEEPENED", "不再依赖 AI 声称已复制来源；exact commit、缺岛前置和 tracked plan 直接证明。"),
        "KC-000010": ("ALIGNED", "治理 PASS 只说明证据路径可恢复，不升级为 HoTT 内部或现实结论。"),
        "KC-000012": ("DEEPENED", "五个 task plan 均在 fresh process 中水合且 untracked_documents=0。"),
        "KC-000017": ("ALIGNED", "主 checkout 旧 PASS 被独立 worktree 反例修正，最终又由新 worktree 正向复核。"),
        "KC-000021": ("ALIGNED", "42-file hash、6/8 路由、六 verifier、四负控与 clean restore 均留收据。"),
        "KC-000022": ("ALIGNED", "修复完成后原 A/B 研究目标、自然 consumer 缺口与数学状态保持不变。"),
        "KC-000029": ("DEEPENED", "checkout-local 隐含支付已从 current 验证链中移除。"),
        "KC-000030": ("DEEPENED", "理论经济账本及其证据现在能由 Git worktree 独立恢复，减少虚假低成本 PASS。"),
        "KC-000035": ("ALIGNED", "本轮提升研究上下文可恢复性，不把它写成 HoTT 表达能力的新增结论。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}",
        "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮关闭 F-016 的项目内 fresh-worktree 验收，不启动数学研究。",
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
            f"| `{kid}` | {label} | `{relation}` | {assessment} | `{ACCEPTANCE_REPORT}`；{kid} | "
            "main 尚未集成；共享通用治理是否吸收该规则另行处理。 |"
        )
    lines += [
        "",
        "## 四件套交叉与更新归属",
        "",
        "- core_change: NO — 无新的用户悖论/元数学原文。",
        "- direction_change: YES_IN_PLACE — portability 方向从 pending 改为 verified current control。",
        "- panorama_change: YES_IN_PLACE — exact-commit fresh 6/6 与四负控进入结果行。",
        "- essay_change: NO — 第四件不变。",
        "- update_decision: F-016 在 candidate branch `VERIFIED_WITH_SCOPE`；main 仍 `NOT_INTEGRATED`。",
        "- cross_conflicts: 主 checkout 旧 6/6 与 linked 4/6 的冲突已修复并由无 ignored-island fresh 6/6 闭合。",
        "- unresolved: canonical main 集成、共享治理通用化、aistudio coverage 与数学研究开放项均不由本轮关闭。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    for rel in (CONTRACT, IMPORT_RECEIPT, ACCEPTANCE_RECEIPT, ACCEPTANCE_REPORT, MERGE_MANIFEST, FEATURES):
        if not (ROOT / rel).is_file():
            raise SystemExit(f"MISSING:{rel}")
    if R.sha((ROOT / ACCEPTANCE_RECEIPT).read_bytes()) != "e5ab194accf0d4f955f1ce1eb53d3dab2058b34a1d2529579ead23ff282aecb9":
        raise SystemExit("ACCEPTANCE_RECEIPT_HASH")
    if json.loads((ROOT / ACCEPTANCE_RECEIPT).read_text(encoding="utf-8")).get("status") != "PASS_WITH_SCOPE":
        raise SystemExit("ACCEPTANCE_RECEIPT_STATUS")
    if __import__("subprocess").check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() != ACCEPTANCE_COMMIT:
        raise SystemExit("ACCEPTANCE_COMMIT_NOT_HEAD")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 130 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_130_S130")
    if SESSION_ID in state["records"]:
        raise SystemExit("S131_ALREADY_EXISTS")

    contract_hash = R.sha((ROOT / CONTRACT).read_bytes())
    contract_repins = 0
    for record in state["records"].values():
        hashes = record.get("source_hashes", {})
        if CONTRACT in hashes:
            hashes[CONTRACT] = contract_hash
            append_revalidation(
                record,
                f"{SESSION_ID} re-pinned the portability contract after recording exact-commit fresh acceptance; underlying source/merge semantics are unchanged.",
            )
            contract_repins += 1
    if contract_repins != 2:
        raise SystemExit(f"CONTRACT_REPIN_COUNT:{contract_repins}")

    result = state["records"][RESULT_ID]
    for rel in (ACCEPTANCE_RECEIPT, ACCEPTANCE_REPORT):
        add_once(result["full_sources"], rel)
        result["source_hashes"][rel] = R.sha((ROOT / rel).read_bytes())
    result["classification"] = "WORKTREE_EVIDENCE_PORTABILITY_VERIFIED_WITH_SCOPE"
    result["evidence_status"] = "VERIFIED_WITH_SCOPE_FRESH_LINKED_WORKTREE"
    result["lifecycle_status"] = "CURRENT"
    result["scope"] = (
        f"Project-local tracked/pinned evidence repair verified from exact commit {TESTED_COMMIT}: "
        "a fresh detached worktree with no top-level workspace/dialogues repo or legacy LocalGPT ignored artifact "
        "passed 42-file import verification, five task hydrations with zero untracked documents and all six canonical verifiers; "
        "four controlled mutations failed closed and clean state was restored. Candidate is not integrated into main."
    )
    result["resolution"] = {
        "reason": (
            "Exact-commit fresh linked-worktree acceptance removed the original checkout-local preconditions: "
            "all five affected task plans used only tracked documents, all six canonical verifiers passed, "
            "four independent content/index/route/path mutations failed closed, and clean state was restored."
        ),
        "evidence": [
            ACCEPTANCE_RECEIPT,
            ACCEPTANCE_REPORT,
            IMPORT_RECEIPT,
            MERGE_MANIFEST,
            "scripts/audit/import_worktree_portability_sources.py",
            "scripts/audit/verify_understanding_merge.py",
            "scripts/audit/verify_fresh_three_way.py",
        ],
    }
    result["status"] = "complete"
    append_revalidation(
        result,
        f"{SESSION_ID} accepted {ACCEPTANCE_RECEIPT}: exact {TESTED_COMMIT}, fresh 6/6, five tracked task plans, four expected negative rejections, clean restoration and worktree removal.",
    )
    remove_once(state["review_due"], RESULT_ID)
    remove_once(state["unresolved"], RESULT_ID)

    understanding = state["records"]["A-UNDERSTANDING-RECONCILIATION-001"]
    for rel in (ACCEPTANCE_RECEIPT, ACCEPTANCE_REPORT):
        add_once(understanding["full_sources"], rel)
        understanding["source_hashes"][rel] = R.sha((ROOT / rel).read_bytes())
    append_revalidation(
        understanding,
        f"{SESSION_ID} verified the v2 36/24 merge against the tracked historical snapshot in a fresh linked worktree; semantic-equivalence review remains open.",
    )

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction_shard = "方向追踪/004 - 证据与覆盖方向及 STATE 覆盖表.md"
    direction["shards"][direction_shard] = replace_line(
        direction["shards"][direction_shard],
        "| `DIR-G-WORKTREE-EVIDENCE-PORTABILITY`",
        f"| `DIR-G-WORKTREE-EVIDENCE-PORTABILITY` | current hydration/verifier 的决定性证据在任意 linked worktree 由顶层 tracked snapshot/file 恢复 | 用户 ruling §22；linked-worktree 4/6 反例 | `VERIFIED_CURRENT_CONTROL / CANDIDATE_NOT_INTEGRATED` | `CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-G-WORKTREE-EVIDENCE-PORTABILITY` | source/STATE/verifier 路径变化时重跑 exact-commit fresh worktree；main 集成时重分配唯一 revision | `{ACCEPTANCE_REPORT}`；`{ACCEPTANCE_RECEIPT}` |",
    )
    for old, new in (
        ("source_state_revision: 130", "source_state_revision: 131"),
        ("projection_generation: 20260913-direction-112", "projection_generation: 20260913-direction-113"),
        ("semantic_status: CORE_GENERATION_4_GOVERNANCE_V4_1_WORKTREE_PORTABILITY_PENDING_FRESH", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_GOVERNANCE_V4_1_WORKTREE_PORTABILITY_PENDING_FRESH`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    panorama_shard = "全景视野/002 - 治理、门禁与骨架结果.md"
    panorama["shards"][panorama_shard] = replace_line(
        panorama["shards"][panorama_shard],
        "| `OUT-G-WORKTREE-EVIDENCE-PORTABILITY`",
        f"| `OUT-G-WORKTREE-EVIDENCE-PORTABILITY` | ignored evidence island 迁移：42-file transform tracked；8 workspace refs 与 LocalGPT artifact 改 tracked 路由；manifest/verifier 检查 path/tracked/tree | `DIR-G-WORKTREE-EVIDENCE-PORTABILITY`、`DIR-G-UNDERSTANDING-RECONCILIATION` | 用户 ruling §22 + exact-commit fresh acceptance | `VERIFIED_WITH_SCOPE_ON_FRESH_LINKED_WORKTREE / NOT_INTEGRATED` | `{TESTED_COMMIT}` 的 detached worktree 无三个 ignored inputs；5 task plans 均 untracked=0；6 canonical verifier PASS；byte/index/route/path 四负控均拒绝，恢复后 clean | 不证明模型理解或数学；不关闭 aistudio coverage；candidate 未进入 main，共享治理未同步 | `{ACCEPTANCE_REPORT}`；`{ACCEPTANCE_RECEIPT}`；`{SESSION_REL}/` |",
    )
    for old, new in (
        ("source_state_revision: 130", "source_state_revision: 131"),
        ("projection_generation: 20260913-outcome-112", "projection_generation: 20260913-outcome-113"),
        ("semantic_status: CORE_GENERATION_4_GOVERNANCE_V4_1_WORKTREE_PORTABILITY_PENDING_FRESH", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_GOVERNANCE_V4_1_WORKTREE_PORTABILITY_PENDING_FRESH`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    memory_shard = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][memory_shard] = replace_line(
        memory["shards"][memory_shard],
        "1. 用户已授权本分支实施 Git worktree 证据可移植性修复",
        f"1. Git worktree 证据可移植性 F-016 已在 exact `{TESTED_COMMIT[:8]}…` 的无 ignored-island detached worktree 达到 `VERIFIED_WITH_SCOPE`：42-file import、5 task plans、6 canonical verifiers、4 负控与 clean restore 全通过；candidate 尚未进入 main，集成时须按 target HEAD 重分配 revision。S 轨可以恢复人工语义/natural-consumer 主线。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        f"\n- S131 worktree portability fresh acceptance：从 exact `{TESTED_COMMIT}` 创建 detached `/Volumes/D/HoTT-portability-verify-802e4f8`，未复制 ignored inputs；确认顶层 workspace/dialogues 与 legacy LocalGPT path 均不存在。import 42/42、workspace 6/6（8 refs）、5 task plans（53/78/228/204/244 docs，全部 untracked=0）、六类 canonical verifier全 PASS。四负控分别触发 byte/tree/nested hash drift、index-untracked、旧 workspace path missing、manifest path identity mismatch；恢复后正向重跑 PASS、Git clean、worktree 删除。F-016 与 portability result 关闭为 `VERIFIED_WITH_SCOPE / CANDIDATE_NOT_INTEGRATED`。无新数学 claim。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = frontier.replace(
        "# HoTT 研究前沿（S130 worktree evidence portability）\n\nS130 只修复研究证据在 linked worktree 的可恢复性；S/B/M 研究分工、候选优先级、数学 claim 与 ERCF-3 `GATED` 均不变。revision 130 commit 后先完成 fresh-worktree 验收，再恢复 S 轨自然 consumer 主线。",
        "# HoTT 研究前沿（S131 portability verified）\n\nF-016 已在 exact-commit fresh linked worktree 验收；该治理支线关闭为 candidate verified，S/B/M 研究分工、候选优先级、数学 claim 与 ERCF-3 `GATED` 均不变。S 轨恢复人工语义/natural-consumer 主线。",
        1,
    )

    lessons_path = ".codex/research/hott/LESSONS.md"
    lessons = (ROOT / lessons_path).read_text(encoding="utf-8").rstrip("\n") + (
        "\n\n99. Worktree 可移植性的完成证据必须来自 exact commit 的新 worktree，而不是在原工作树把文件 stage 后重跑。正向还不够：byte tamper、index removal、旧路径复活和 manifest path drift 分别证明 content、tracked identity、no-fallback 与 path identity 四个 oracle；每次负控后恢复并重跑正向，才能排除测试污染。\n"
    )

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = resume.replace(
        "## 当前停止点\n\n",
        f"## 当前停止点\n\nS131：F-016/worktree evidence portability 已在 exact `{TESTED_COMMIT[:8]}…` fresh linked worktree通过 5 task plans、6 canonical verifiers 与 4 负控，状态 `VERIFIED_WITH_SCOPE / CANDIDATE_NOT_INTEGRATED`。三个 ignored islands 不再是 candidate current hydration/PASS 的必需输入。main 集成与 shared generic governance follow-up 未执行；数学研究状态不变，S 轨下一步恢复自然 consumer/明确交付承诺的人工语义审计。\n\n",
        1,
    )

    state["revision"] = 131
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_WORKTREE_PORTABILITY_VERIFIED"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = (
        "Project portability work is complete on the candidate branch. Before canonical integration, compare exact candidate and target OIDs, "
        "reallocate any occupied revision IDs on target, and rerun fresh portability acceptance. S-track research may resume with a fixed natural consumer and explicit delivery promise."
    )
    state["projection"]["status"] = STATUS
    direction_record = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    direction_record["projection_generation"] = "20260913-direction-113"
    direction_record["semantic_status"] = STATUS
    panorama_record = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    panorama_record["projection_generation"] = "20260913-outcome-113"
    panorama_record["semantic_status"] = STATUS
    for record in (direction_record, panorama_record):
        for rel in (ACCEPTANCE_RECEIPT, ACCEPTANCE_REPORT):
            add_once(record["full_sources"], rel)

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目标：依据 revision 130 exact-commit fresh evidence 关闭 F-016 的 pending 状态。
- tested commit：`{TESTED_COMMIT}`；fresh worktree 未包含顶层 workspace/dialogues 或 legacy LocalGPT ignored path。
- 正向：import 42/42；workspace 6/6/8 refs；五个 task plans 全部 untracked=0；六类 canonical verifier PASS。
- 负向：byte tamper、index removal、旧 workspace route、manifest path identity 四类全部按特定错误失败；逐项恢复后正向再 PASS，Git clean，worktree 已删除。
- evidence：`{ACCEPTANCE_RECEIPT}`（SHA-256 `e5ab194a…`）与 `{ACCEPTANCE_REPORT}`。
- 状态：`A-WORKTREE-EVIDENCE-PORTABILITY-001` → `VERIFIED_WITH_SCOPE_FRESH_LINKED_WORKTREE / complete`；从 review_due/unresolved 移除。
- 边界：candidate 未 merge main；共享治理 repo 当前有并行 dirty 工作，本轮不修改；不 push/tag；无数学 claim。

## C01–C10 最终影响

- C01–C06：项目 ruling/Feature、合同、Skill/PROTOCOL/LOAD_SET、AGENTS/README 与 fresh/negative evidence 均 `UPDATE_VERIFIED`。
- C07：`NO_CHANGE`（config/Rules/Hooks/plugins/secret/权限不变）。
- C08：`NOT_APPLICABLE`（无 host adapter 变化）。
- C09：`UPDATE_CANDIDATE`（revision 131 与 commits；无 shared tag/push/main merge）。
- C10：`UPDATE`（历史 paths/provenance 与 external 1,209-file snapshot 边界保留；shared generic follow-up 未冒充完成）。
- remainder：`0`。
"""
    runs = json.dumps(
        {
            "schema_version": "hott-session-runs/v2",
            "session_id": SESSION_ID,
            "checkpoint_result": RESULT_REL,
            "tested_commit": TESTED_COMMIT,
            "acceptance_commit": ACCEPTANCE_COMMIT,
            "acceptance_receipt": ACCEPTANCE_RECEIPT,
            "acceptance_receipt_sha256": R.sha((ROOT / ACCEPTANCE_RECEIPT).read_bytes()),
            "fresh_preconditions": {
                "ignored_top_workspace_absent": True,
                "ignored_top_dialogues_absent": True,
                "legacy_local_path_absent": True,
                "git_status_clean": True,
            },
            "positive": {
                "import": "PASS_42_FILES_6_MAPPINGS_8_REFS",
                "portable_task_plans": "PASS_5_ALL_UNTRACKED_ZERO",
                "canonical_verifiers": "PASS_6_OF_6",
                "post_negative_restore": "PASS_AND_CLEAN",
            },
            "negative_controls": {
                "byte_tamper": "EXPECTED_REJECTION",
                "index_removal": "EXPECTED_REJECTION",
                "ignored_path_revival": "EXPECTED_REJECTION",
                "manifest_path_drift": "EXPECTED_REJECTION",
            },
            "temporary_worktree_removed": True,
            "new_math_claims": [],
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
        "evidence_status": "VERIFIED_WITH_SCOPE_FRESH_LINKED_WORKTREE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, ACCEPTANCE_RECEIPT, ACCEPTANCE_REPORT],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV, RESULT_ID],
        "scope": "Revision 131 closes project-local worktree evidence portability after exact-commit fresh positive and negative acceptance; candidate not integrated; no mathematical change.",
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
            "Close the user-authorized project worktree-evidence portability result using exact-commit fresh positive and negative evidence. "
            "Keep main integration, shared governance changes, push and tags out of scope."
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
                "revision": 131,
                "session_id": SESSION_ID,
                "files": len(texts),
                "contract_repins": contract_repins,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
