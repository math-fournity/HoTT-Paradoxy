#!/usr/bin/env python3
"""Prepare revision 64 (S064, N18): C-141 library-interface instance + batch 7.

Applies anchor-based edits to the seven current-state owners, then emits a
cognition-checkpoint payload covering those files plus STATE, session evidence
and HEAD. Anchors are exact substrings of the current documents; every
substitution asserts a unique match so a drifted document fails closed.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260913-064-N18-LIBRARY-INTERFACE-AND-BATCH7"
PREV_SESSION = "S-RES-20260913-063-N17-COMPLETION-FORMS-AND-BATCH6"
RESULT_ID = "A-LIBRARY-INTERFACE-NO-RECOVERY-001"
REPORT = "audit/library-interface-no-recovery-and-batch7-20260913.md"
SRC = "HoTT/formal/truncation-no-recovery/TruncationNoRecovery.agda"
README = "HoTT/formal/truncation-no-recovery/README.md"
TOOLCHAIN = "HoTT/formal/truncation-no-recovery/TOOLCHAIN.json"
LIBREG = "HoTT/formal/truncation-no-recovery/AGDA_LIBRARIES"
RUN_DIR = "HoTT/verification/runs/20260913-MP-TRUNC-NORECOVERY-001-03"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
SAMPLE_SCRIPT = "scripts/audit/sample_understanding_claims_batch7.py"
FILL_SCRIPT = "scripts/audit/fill_understanding_claim_sample_batch7.py"
SAMPLE_JSON = "audit/understanding-claim-sample-batch7-20260912.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
EVIDENCE = [
    REPORT, SRC, README, TOOLCHAIN, LIBREG, MATRIX,
    f"{RUN_DIR}/RUN.json", f"{RUN_DIR}/index-row-manifest.json",
    SAMPLE_SCRIPT, FILL_SCRIPT, SAMPLE_JSON,
]
NEW_STATUS = "N18_LIBRARY_INTERFACE_AND_BATCH7_REVIEWED_QUEUE_CONTINUES"
OLD_STATUS = "CORE_GENERATION_4_N17_COMPLETION_FORMS_AND_BATCH6_REVIEWED_QUEUE_CONTINUES"


def sub_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise SystemExit(f"ANCHOR_NOT_UNIQUE:{label}:{text.count(old)}")
    return text.replace(old, new, 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()

    spec = importlib.util.spec_from_file_location("runtime_n18", RUNTIME_PATH)
    assert spec and spec.loader
    R = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(R)

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") not in (63, 64):
        raise SystemExit("EXPECTED_REVISION_63_OR_64")
    for rel in EVIDENCE:
        if not (root / rel).is_file():
            raise SystemExit(f"EVIDENCE_MISSING:{rel}")

    # ---- projection edits (anchor-based) ----
    APPLY_EDITS = (state.get("revision") == 63)
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    if APPLY_EDITS:
        direction = sub_once(direction, f"状态：`{OLD_STATUS}`",
                             f"状态：`{NEW_STATUS}`", "dir-status")
    direction = sub_once(direction, "source_state_revision: 63", "source_state_revision: 64", "dir-rev")
    direction = sub_once(direction, "projection_generation: 20260913-direction-047",
                         "projection_generation: 20260913-direction-048", "dir-gen")
    direction = sub_once(direction, f"semantic_status: {OLD_STATUS}",
                         f"semantic_status: {NEW_STATUS}", "dir-sem")
    old_work = [l for l in direction.splitlines() if l.startswith("4. **当前第一工作包**")]
    assert len(old_work) == 1
    new_work = ("4. **当前第一工作包**：N19 证据队列按比例继续（第 8 批，可选）——沿用同一抽样规则覆盖下一档 owner"
                "（`B5`、`A7`、`A1` 等），四值判词与前七批去重；若发现 E6 立即转 F-011。N18 已完成："
                "`MP-TRUNC-NORECOVERY-001` 扩展（C-141：`isFinSet` 形状接口的统一枚举读出不存在，run `-03`）"
                "+ 第七批 40 条（27/0/0/13）；七批累计 282/2,396。备选：ERCF-3 T3（仍按 C8 停止条件 gated）。")
    direction = sub_once(direction, old_work[0], new_work, "dir-work")
    (root / R.DIRECTION).write_text(direction, encoding="utf-8")

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(panorama, f"状态：`{OLD_STATUS}`", f"状态：`{NEW_STATUS}`", "pan-status")
    panorama = sub_once(panorama, "source_state_revision: 63", "source_state_revision: 64", "pan-rev")
    panorama = sub_once(panorama, "projection_generation: 20260913-outcome-047",
                        "projection_generation: 20260913-outcome-048", "pan-gen")
    panorama = sub_once(panorama, f"semantic_status: {OLD_STATUS}", f"semantic_status: {NEW_STATUS}", "pan-sem")
    rows = (
        "| `OUT-TOP-LIBRARY-INTERFACE-NO-RECOVERY` | C-141：`isFinSet` 形状接口（`Σ n × ∥ A ≃ Fin n ∥₁`）的统一枚举读出不存在——任何逐点保持的 `pick : ∥ E ∥₁ → E` 迫使被读出枚举相等（run `-03`） | "
        "`DIR-U-THEORY-ECONOMY-SELF-VALIDATION`、`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前原生 Cubical Agda 形式化 + 固定库接口读取 | "
        "`MACHINE_PROVED_LOCAL_UNCOMMITTED` | Agda 2.8.0 + Cubical v0.9、exit 0（stderr 0、零 warning）、`EXACT_INDEX_SNAPSHOT_MATCH`、独立重放 exact match；matrix 覆盖 C-134–C-141 | "
        "不证明任何具体库误用该接口；E6 未因此成立；非集合目标不外推 | `HoTT/verification/runs/20260913-MP-TRUNC-NORECOVERY-001-03/`；`audit/library-interface-no-recovery-and-batch7-20260913.md` |\n"
        "| `OUT-TOP-EVIDENCE-QUEUE-BATCH7` | S064 第七批按比例抽样 40 条（B3/A3/A9/A0/B1/A2/B2/A8 各 5）：`SUPPORTED=27`/`PENDING=13`/0 `UNSUPPORTED`/0 `SUPERSEDED`；七批累计 282/2,396（11.8%）：176/12/0/94；E6 未出现 | "
        "`DIR-E-LOCAL-HISTORY-COVERAGE`、`DIR-G-UNDERSTANDING-RECONCILIATION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前人工抽样复核 + 确定性脚本 | `DOCUMENTED / BOUNDED_SAMPLE_BATCH7` | 七批抽样无 UNSUPPORTED、无 E6 | 冻结 2,396 分母不变 | "
        "`audit/understanding-claim-sample-batch7-20260912.json`；`scripts/audit/sample_understanding_claims_batch7.py` |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", rows + "| `OUT-TOP-CORE-FOUNDATION` |", "pan-rows")
    tail_old = "S063 完成 C-139/C-140（完成不可行性的内部否定形式，run `-02`，exit 0、exact replay）与第六批抽样（40 条 27/0/0/13，六批累计 242/2,396，仍无 `UNSUPPORTED`、无 E6）；R032 回放、"
    tail_new = "S063 完成 C-139/C-140（完成不可行性的内部否定形式，run `-02`，exit 0、exact replay）与第六批抽样（40 条 27/0/0/13，六批累计 242/2,396，仍无 `UNSUPPORTED`、无 E6）；S064 完成 C-141（`isFinSet` 形状接口的统一枚举读出不存在，run `-03`，exit 0、exact replay）与第七批抽样（40 条 27/0/0/13，七批累计 282/2,396，仍无 `UNSUPPORTED`、无 E6）；R032 回放、"
    panorama = sub_once(panorama, tail_old, tail_new, "pan-tail")
    (root / R.PANORAMA).write_text(panorama, encoding="utf-8")

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    f_old = "S063 扩展同一包（C-139/C-140：理论内部的完成不可行否定形式，run `-02`，exit 0、零 warning、exact replay）并完成第六批抽样（40 条 27/0/0/13，六批累计 242/2,396，仍无 UNSUPPORTED、无 E6）。所有新结论继续执行 F-011。"
    f_new = f_old[:-len("所有新结论继续执行 F-011。")] + "；S064 新增 C-141（`isFinSet` 形状接口的统一枚举读出不存在，run `-03`）与第七批抽样（40 条 27/0/0/13，七批累计 282/2,396，仍无 UNSUPPORTED、无 E6）。所有新结论继续执行 F-011。"
    frontier = sub_once(frontier, f_old, f_new, "frontier-text")
    flines = frontier.split("\n")
    idx = next(i for i, l in enumerate(flines) if l.startswith("| 第一工作包 | N18 证据队列按比例继续"))
    flines[idx] = ("| 已闭合工作包 24 | 库接口形状的不可恢复实例（S064，C-141，run `-03`） | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `isFinSet` 形状的统一枚举读出不存在；接口形状边界，非误用实例 |\n"
                   "| 已闭合工作包 25 | 第七批抽样（S064） | `BOUNDED_SAMPLE_BATCH7` | 40 条 27/0/0/13；七批累计 282/2,396；无 UNSUPPORTED、无 E6 |\n"
                   "| 第一工作包 | N19 证据队列按比例继续（第 8 批） | proportion sampling | 下一档 owner（B5/A7/A1 等）沿用同一规则并与前七批去重；发现 E6 即转 F-011；备选 ERCF-3 T3（gated） |")
    (root / f"{R.PREFIX}FRONTIER.md").write_text("\n".join(flines), encoding="utf-8")

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    mlines = memory.split("\n")
    idx = next(i for i, l in enumerate(mlines) if l.startswith("2. 当前第一工作包转为 N18"))
    mlines[idx] = ("2. 当前第一工作包转为 N19 证据队列按比例继续（第 8 批，可选）：沿用同一抽样规则覆盖下一档 owner（`B5`、`A7`、`A1` 等）并与前七批去重；若发现 E6 立即转 F-011。"
                   "N18 已完成：`MP-TRUNC-NORECOVERY-001` 扩展（C-141）+ 第七批 40 条（27/0/0/13；七批累计 282/2,396）。备选：ERCF-3 T3（gated）。")
    memory = "\n".join(mlines)
    hist = ("- S064 完成 N18：(a) `MP-TRUNC-NORECOVERY-001` 扩展 C-141（`isFinSet` 形状接口的统一枚举读出不存在），run `20260913-MP-TRUNC-NORECOVERY-001-03`，"
            "exit 0、零 warning、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay；matrix 覆盖 C-134–C-141，冻结 9 行 manifest；(b) 第七批抽样 40 条（27/0/0/13），七批累计 282/2,396，E6 未出现；"
            "下一工作包 N19，备选 ERCF-3 T3（gated）。\n")
    memory = sub_once(memory, "- S063 完成 N17：", hist + "- S063 完成 N17：", "mem-hist")
    (root / "MEMORY.md").write_text(memory, encoding="utf-8")

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    para = ("S064 完成 N18：(a) `MP-TRUNC-NORECOVERY-001` 扩展 C-141：对 Cubical 的 `isFinSet` 形状接口（`Σ n × ∥ A ≃ Fin n ∥₁`，枚举组件是命题），不存在统一读出具体枚举的 pick 函数；"
            "run `20260913-MP-TRUNC-NORECOVERY-001-03`：exit 0、stderr 0、零 warning、`EXACT_INDEX_SNAPSHOT_MATCH`、独立 `--rerun` exact match；matrix 覆盖 C-134–C-141，冻结 9 行 manifest。"
            "(b) 第七批抽样 40 条（B3/A3/A9/A0/B1/A2/B2/A8 各 5）：`SUPPORTED=27`、`PENDING=13`、0 `UNSUPPORTED`、0 `SUPERSEDED`；七批累计 282/2,396（11.8%）：176/12/0/94；E6 七批一致未出现。"
            "报告 `audit/library-interface-no-recovery-and-batch7-20260913.md`；下一工作包 N19（队列第 8 批），备选 ERCF-3 T3（gated）。\n\n")
    resume = sub_once(resume, "S063 完成 N17：(a)", para + "S063 完成 N17：(a)", "resume-head")
    (root / f"{R.PREFIX}RESUME.md").write_text(resume, encoding="utf-8")

    # ---- state / session payload ----
    new_hashes = {rel: hashlib.sha256((root / rel).read_bytes()).hexdigest() for rel in EVIDENCE}
    # refresh any stored hashes for the documents we just edited
    for rid, rec in state["records"].items():
        for rel in list(rec.get("source_hashes", {})):
            path = root / rel
            if path.is_file():
                rec["source_hashes"][rel] = hashlib.sha256(path.read_bytes()).hexdigest()

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))

    state["records"][RESULT_ID] = {
        "kind": "formal_proof_extension_and_sample",
        "path": REPORT,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "classification": "LIBRARY_INTERFACE_SHAPE_NO_UNIFORM_ENUMERATION",
        "research_parent": "A-HOTT-SELF-VALIDATION-ECONOMY-001",
        "depends_on": ["A-TRUNC-COMPLETION-FORMS-001"],
        "full_sources": EVIDENCE,
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "formal": {
            "proof_id": "MP-TRUNC-NORECOVERY-001",
            "claim_ids": ["C-141"],
            "run_id": "20260913-MP-TRUNC-NORECOVERY-001-03",
            "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
            "index_status": "INDEXED_IN_CLAIM_EVIDENCE_MATRIX",
            "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
            "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
        },
        "resolution": {
            "reason": "C-141 instantiates the no-recovery fence on the pinned library's isFinSet interface shape: the enumeration component is a proposition, so no uniform pick of a specific enumeration exists. Run -03 re-checks the package (exit 0, zero warnings, exact replay); the batch-7 sample adds 40 verdicts (27/0/0/13); cumulative 282/2396 with no UNSUPPORTED and no E6.",
            "evidence": EVIDENCE,
        },
        "scope": "Library-interface-shape boundary plus the seventh sample. No concrete misuse is claimed; E6 remains open.",
    }
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, *EVIDENCE],
        "source_hashes": {rel: new_hashes[rel] for rel in EVIDENCE},
        "mathematical_status": "MACHINE_PROVED_LIBRARY_INTERFACE_NO_RECOVERY",
        "cognition_status": "N18_LIBRARY_INTERFACE_AND_BATCH7_REVIEWED",
        "scope": "C-141 library-interface instance, batch-7 sample, routing of N19.",
    }
    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260913-direction-048" if rid.startswith("I-DIRECTION") else "20260913-outcome-048"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (REPORT, f"{RUN_DIR}/RUN.json", SAMPLE_JSON, MATRIX, SRC):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["revision"] = 64
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N19: continue the evidence queue by the same proportional rule over the next owner tier "
            "(B5, A7, A1, ...), deduplicated against batches 1-7. If a natural-use chain (E6) appears, "
            "switch immediately to F-011 packaging. Fallback: ERCF-3 T3 (gated by the C8 stop conditions)."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    session_text = "\n".join([
        f"# {SESSION_ID}", "",
        "- 触发：S063 路由的 N18（队列第 7 批）+ 库接口 E6 扫描。",
        "- 机器扩展 `MP-TRUNC-NORECOVERY-001`（C-141）：`isFinSet` 形状（`Σ n × ∥ A ≃ Fin n ∥₁`，枚举组件是命题）不存在统一读出具体枚举的函数；run `20260913-MP-TRUNC-NORECOVERY-001-03`，exit 0、stderr 0、零 warning、`EXACT_INDEX_SNAPSHOT_MATCH`、exact replay；matrix 覆盖 C-134–C-141，冻结 9 行 manifest。",
        "- 第七批抽样 40 条（B3/A3/A9/A0/B1/A2/B2/A8 各 5）：`SUPPORTED=27`、`PENDING=13`、0 `UNSUPPORTED`、0 `SUPERSEDED`；七批累计 282/2,396（11.8%）：176/12/0/94；E6 七批一致未出现。",
        "- 库内 E6 扫描（固定 Cubical v0.9 库）：未发现把该接口弱资格当强资格使用的真实消费者；库自身在 `isFinSet` 形状上保持资格分离。",
        "- 边界：C-141 是接口形状边界而非误用实例；不证明 HoTT 内部矛盾；未 commit/tag/push。",
        "- 三件套：direction/panorama revision 64/generation 048；core 不变。", "",
    ])
    touched = {
        "KC-000010": ("ALIGNED", "完成困难的结构：C-141 把统一枚举读出的不存在落到固定库接口形状。"),
        "KC-000013": ("ALIGNED", "理论工具性：接口保留存在、不保留具体表示，资格分离被执行。"),
        "KC-000029": ("DEEPENED", "理论经济：有限集接口只保留‘有限’而不保留‘是哪一个枚举’。"),
        "KC-000036": ("ALIGNED", "E6 七批未出现；gated 状态不变。"),
    }
    lines = [f"# 核心认知逐编号回评：{SESSION_ID}", "",
             f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
             "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|"]
    aligned = deepened = 0
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = touched.get(unit["id"], ("NOT_TOUCHED", "本轮是 S064 库接口实例与第七批抽样；未研究、改写或重新裁决该条用户原文。"))
        aligned += relation == "ALIGNED"; deepened += relation == "DEEPENED"
        lines.append(f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S064/SESSION.md；{REPORT}；{RUN_DIR}/RUN.json | E6 与队列余量仍开放。 |")
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend(["", "## 三件套交叉与更新归属", "",
                  "- core_change: `NO` — generation-4/36 KC 不变。",
                  "- direction_change: `YES` — C-141 完成；第七批 40 条完成（七批累计 282/2,396）；第一工作包转 N19；revision 64/generation 048。",
                  "- panorama_change: `YES` — 新增 `OUT-TOP-LIBRARY-INTERFACE-NO-RECOVERY` 与 `OUT-TOP-EVIDENCE-QUEUE-BATCH7`；理解章节 inventory 不变。",
                  "- update_decision: `新增 run -03 证据、claim matrix 一行与冻结 9 行 manifest；抽样工件进入 audit/。`",
                  "- cross_conflicts: `NONE_OBSERVED` — C-141 与 C-139 同族；七批抽样连续无 UNSUPPORTED、无 E6。",
                  "- unresolved: `E6、队列余量、fresh model behavior 与 Git version-close 仍开放。`",
                  "", "## 汇总", "",
                  f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮判定为 `MACHINE_PROVED_LIBRARY_INTERFACE_INSTANCE_PLUS_BATCH7`。", ""])
    audit_text = "\n".join(lines)
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "work_kind": "formal_extension_and_batch7",
        "mathematical_claim_added": True,
        "claim_matrix_updated": {"proof_row": "MP-TRUNC-NORECOVERY-001", "claims": ["C-141"]},
        "formal_run": {"run_id": "20260913-MP-TRUNC-NORECOVERY-001-03",
                       "kernel_status": "KERNEL_ACCEPTED_WITH_SCOPE",
                       "index_validation": "EXACT_INDEX_SNAPSHOT_MATCH",
                       "replay": "EXACT_EXIT_STDOUT_STDERR_MATCH",
                       "exit_code": 0, "stderr_bytes": 0, "warnings": 0, "index_rows": 9},
        "batch7": {"sample_size": 40,
                   "verdicts": {"SUPPORTED": 27, "SUPERSEDED_BY_MACHINE_RESULT": 0, "UNSUPPORTED": 0, "PENDING": 13},
                   "cumulative": {"sampled": 282, "coverage": "11.8%", "SUPPORTED": 176, "SUPERSEDED": 12, "UNSUPPORTED": 0, "PENDING": 94},
                   "e6_found": False},
        "evidence": {"report": REPORT, "sample": SAMPLE_JSON},
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    # sessions dir
    (root / SESSION_REL).mkdir(parents=True, exist_ok=True)
    (root / session_path).write_text(session_text, encoding="utf-8")
    (root / audit_path).write_text(audit_text, encoding="utf-8")
    (root / runs_path).write_text(runs, encoding="utf-8")
    (root / R.STATE).write_text(json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    # update HEAD tracked hashes for the seven edited documents
    head_path = root / ".codex/cognition/HEAD.json"
    head = json.loads(head_path.read_text(encoding="utf-8"))
    for rel in head.get("tracked", {}):
        path = root / rel
        if path.is_file():
            head["tracked"][rel] = hashlib.sha256(path.read_bytes()).hexdigest()
    head_path.write_text(json.dumps(head, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next "
            "package. This in-scope checkpoint records C-141 (isFinSet-shaped interface has no uniform enumeration read; "
            "run -03, exit 0, exact replay, 9-row frozen manifest) and the batch-7 sample (40 claims; 27/0/0/13; cumulative "
            "282/2396 with no UNSUPPORTED and no E6). It routes N19. No Git commit, tag or push."
        ),
        "load_profile": "governance",
        "task_ids": [],
        "files": [],
    }
    for rel in [R.STATE, session_path, audit_path, runs_path, R.DIRECTION, R.PANORAMA, "MEMORY.md",
                f"{R.PREFIX}FRONTIER.md", f"{R.PREFIX}LESSONS.md", f"{R.PREFIX}RESUME.md"]:
        path = root / rel
        text = path.read_text(encoding="utf-8")
        payload["files"].append({"path": rel, "expected_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "text": text})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 64, "session_id": SESSION_ID}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
