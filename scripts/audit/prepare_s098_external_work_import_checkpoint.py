#!/usr/bin/env python3
"""Prepare revision 98: absorb the external verification-event work into the repo."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-098-EXTERNAL-WORK-IMPORT"
PREV = "S-GOV-20260913-097-INDEX-READER-BANNER"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
EVIDENCE = "audit/verification-event吸收与独立核验-20260913.md"
STATUS = "CORE_GENERATION_4_GOVERNANCE_V3_5_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
STATUS_SHORT = "GOVERNANCE_V3_5_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
PREV_STATUS_SHORT = "GOVERNANCE_V3_4_1_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
RELEASE_REF = "governance-v3.5.0"
EXPECTED_REPINNED = {"HoTT/CLAIM_EVIDENCE_MATRIX.md",
                     "HoTT/verification/PROOF_VERSION_CLOSURE.json",
                     "scripts/audit/verify_proof_version_closure.py"}
IMPORT_ROOT = "audit/imports/verification-event-20260913-01a099e9"
PROJECT_RUN = "HoTT/verification/runs/20260913-MP-VERIFICATION-EVENT-001-01"
PACKAGE_SOURCE = "HoTT/formal/verification-event/VerificationEvent.agda"
EARLY_SESSIONS = {
    "S-AUD-20260913-KC15-01a099e9": "核对 KC-000015 的收录、来源与读取范围（只读核对）。",
    "S-REV-20260913-WORKLINE-01a099e9": "本地/Web/当前 repo 工作史的方法诊断；AI 复审意见，未自动改成规则。",
    "S-DOC-20260913-CORE-ESSAY-01a099e9": "综合文章初稿：36 段 core 原文逐字保全与主题性展开。",
    "S-DOC-20260913-TIME-ORDER-01a099e9": "用户关于时间/时序的澄清与文章修订；原文保全核验。",
}
PANORAMA_ROW = (
    "| `OUT-TOP-VERIFICATION-EVENT` | `MP-VERIFICATION-EVENT-001`：导入另一个 AI 的有限验证事件模型并在项目内重放——"
    "保留时标的历史核查可完成（C-152）、固定过去→当前改写不存在（C-153）、完全阶段擦除不保真（C-154）、保阶段正控制（C-155） | "
    "`DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-L-TIME-WORK-DIMENSION`、`DIR-U-B-EFFECTIVE-DELIVERY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | "
    "外部独立来源（会话 01a099e9，交接说明与原件见 `audit/imports/verification-event-20260913-01a099e9/`）+ 本项目原生重放 | "
    "`MACHINE_PROVED_VERSION_CLOSED / VERIFICATION_EVENT_STAGE_BOUNDARY_WITH_POSITIVE_CONTROL` | "
    "项目 canonical run exit 0、stderr 0、`EXACT_INDEX_SNAPSHOT_MATCH`、rerun `EXACT_EXIT_STDOUT_STDERR_MATCH`；"
    "负向校准 exit 42 于 `BadCast.agda:10` `afterP != initial`；外部 9 个 run 与异目录重放原件按字节保全 | "
    "不构成 HoTT 自身非现实性实例；不说明任意不同时标命题都不同；不证明所有抽象都会丢掉阶段信息；"
    "不证明 HoTT 全局健全性或完整 Fitch/Gödel 定理 | "
    "`HoTT/formal/verification-event/README.md`；`C-149`–`C-156`；`" + PROJECT_RUN + "/`；`audit/verification-event吸收与独立核验-20260913.md`；`" + IMPORT_ROOT + "/` |\n"
)

SPEC = importlib.util.spec_from_file_location("runtime_s098", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:70]}:{text.count(old)}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    aligned = {
        "KC-000007": "外部 AI 的结论被要求先做独立核验再登记，防止把“另一个模型的自信”当模式匹配真值。",
        "KC-000017": "导入区分了“用户原文/AI 阐释/机器结果”：文章与候选留在来源与 audit，不进入 core。",
        "KC-000021": "本包走完 MATH_PROOF_BEFORE_DELIVERY_V1：源码、项目 run、唯一索引和 rerun 全部留在 repo。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮为外部工作吸收与机器核验，不改 KC 原文。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]; label = str(unit["semantic_label"]).replace("|", "\\|")
        if kid in aligned:
            relation = "ALIGNED"; assessment = aligned[kid]
        else:
            relation = "NOT_TOUCHED"; assessment = f"本轮没有研究或重新裁决“{label}”的数学/哲学内容。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{EVIDENCE}`；{kid} | 数学开放项不变。 |")
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: NO — 无新用户原文；外部候选与 AI 阐释不入 core。",
        "- direction_change: YES_IN_PLACE — `DIR-L-TIME-WORK-DIMENSION` 原位补上新结果与新闭环判词（不新增覆盖块）。",
        "- panorama_change: YES — 新增 `OUT-TOP-VERIFICATION-EVENT` 结果行（写入全景视野/003 owner shard）。",
        "- update_decision: 原件保全 + 项目内重放 + 矩阵 C-149–C-156 + 追加式版本登记 + 四个历史 Session 只登记身份不倒填收据。",
        "- cross_conflicts: 外部 run schema 与项目 capture 不同 → 不冒充，分别登记；外部候选的“值得研究”与“已被检验否证”分开写。",
        "- unresolved: 候选文档的更一般证书规格未实现；异目录重放为同宿主；fresh model behavior NOT_RUN；不 push。",
        "", "## 汇总", "", "`ALIGNED=3`；`NOT_TOUCHED=33`；无 `DEVIATED`。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 97 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_97_S097")

    repinned: set[str] = set()
    for record in state["records"].values():
        for rel, old_hash in list((record.get("source_hashes") or {}).items()):
            target = root / rel
            if not target.exists():
                continue
            new_hash = R.sha(target.read_bytes())
            if new_hash != old_hash:
                repinned.add(rel)
                record["source_hashes"][rel] = new_hash
                record["revalidation"] = (
                    f"{rel} re-hashed by {SESSION_ID} after absorbing the external verification-event package "
                    "(matrix appended C-149–C-156; closure registry extended additively; verifier gained the "
                    "later_packages check). The record's claim and scope are unchanged."
                )
    if repinned != EXPECTED_REPINNED:
        raise SystemExit(f"UNEXPECTED_REPINNED_HASHES:{sorted(repinned)}")

    projections = {}
    for key, rel, gen in (("DIRECTION", R.DIRECTION, "direction"), ("PANORAMA", R.PANORAMA, "outcome")):
        doc = projection_edit.load(root, rel)
        projection_edit.replace_in_index(doc, "source_state_revision: 97", "source_state_revision: 98")
        projection_edit.replace_in_index(doc, f"projection_generation: 20260913-{gen}-081",
                                         f"projection_generation: 20260913-{gen}-082")
        projection_edit.replace_in_index(doc, f"状态：`{PREV_STATUS_SHORT}`", f"状态：`{STATUS_SHORT}`")
        projection_edit.replace_in_index(doc, f"semantic_status: {PREV_STATUS_SHORT}", f"semantic_status: {STATUS_SHORT}")
        projections[key] = doc
    projection_edit.append_to_shard(projections["PANORAMA"], "全景视野/003 - 当前机器证明包与原生重放.md", PANORAMA_ROW)
    projection_edit.replace_in_shard(
        projections["DIRECTION"], "方向追踪/003 - LocalGPT 与 WebGPT 方向.md",
        "`OUT-TOP-ONLINE-CAUSALITY`（C-106–C-109） |",
        "`OUT-TOP-ONLINE-CAUSALITY`（C-106–C-109）、`OUT-TOP-VERIFICATION-EVENT` |",
    )
    projection_edit.replace_in_shard(
        projections["DIRECTION"], "方向追踪/003 - LocalGPT 与 WebGPT 方向.md",
        "guarded/clocked 完整翻译与物理时间保留为未来细化 |",
        "guarded/clocked 完整翻译与物理时间保留为未来细化；2026-09-13 新增 `OUT-TOP-VERIFICATION-EVENT`"
        "（外部导入模型的阶段/时标边界，CLOSED_WITH_SCOPE；未构成 HoTT 自身 BUG，重开条件见该 result 行） |",
    )

    memory = projection_edit.load(root, "MEMORY.md")
    projection_edit.replace_in_shard(
        memory, "MEMORY/001 - 当前执行队列.md",
        "1. project-local governance 3.4.0：三件套分片完成",
        "1. 外部 AI 工作已吸收（S098）：`MP-VERIFICATION-EVENT-001` 原件保全 + 项目内重放 + `C-149`–`C-156` + 追加式版本登记；"
        "判词 `VERIFICATION_EVENT_STAGE_BOUNDARY_WITH_POSITIVE_CONTROL`，未构成 HoTT 自身 BUG。历史分片波次：project-local governance 3.4.0：三件套分片完成",
    )
    projection_edit.append_to_shard(
        memory, "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S098 外部工作吸收：另一个 AI（会话 01a099e9）的有限验证事件模型经独立核验后进入本 repo——"
        "原件 170 文件/整树 `56376a96…` 与异目录重放 `f05422f9…` 按字节保全；主源码成为唯一 owner；"
        "项目 canonical run `20260913-MP-VERIFICATION-EVENT-001-01`（exit 0、rerun 字节一致）；"
        "负向校准 exit 42 于 `afterP != initial`；矩阵新增 `C-149`–`C-156`；"
        "`PROOF_VERSION_CLOSURE.json` 追加式 `later_packages` 登记（历史 17 包冻结收据不改写）；"
        "四个早期文档 Session 只登记历史身份、不倒填 checkpoint 收据。判词：最小候选未构成 HoTT BUG。\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"):
        lessons += "\n"
    lessons += (
        "\n77. 吸收外部 AI 工作时：原件必须按字节保全并**独立复现**其只读核验脚本；外部 run 的 schema 与项目 capture 不同，"
        "只能分别登记，不能改名/补字段冒充；历史 packege 的冻结 registry（如 17 包 PROOF_VERSION_CLOSURE）不改写，"
        "新包走追加式 `later_packages` + 'tracked/INDEXED/exit 0' 机械检查。候选文档的'值得研究'与被检验后的'未构成目标'必须分开写。\n"
    )
    resume = replace_once(
        (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8"), "## 当前停止点\n",
        f"## 当前停止点\n{SESSION_ID}：外部 AI 的验证事件工作已吸收（唯一 owner 源码 + 项目 run + `C-149`–`C-156` + 追加式版本登记）；"
        f"判词 `VERIFICATION_EVENT_STAGE_BOUNDARY_WITH_POSITIVE_CONTROL`（未构成 HoTT 自身 BUG）。"
        f"下一项回到研究第一线（E6 consumer）或用户指定课题。\n\n",
    )

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 用户要求把另一个 AI 的工作完整吸收进 repo，并确保未来 AI 知道发生过什么；工单见 `{IMPORT_ROOT}/交接说明-交由另一AI整合-20260913-01a099e9.md`。
- 处置：原件保全（`original-package/` 170 文件整树 `56376a96…`、`relocated-replay/` `f05422f9…`）→ 独立复现交接说明 §9 只读核验 →
  主源码部署为唯一 owner → 项目 canonical capture + rerun → 矩阵 `C-149`–`C-156` → 追加式版本登记 → 三件套原位更新。
- 负向校准：`negative/BadCast.agda` 故意不通过；项目探针（exit 42、`[UnequalTerms]`、`afterP != initial`）与外部 `negative-002` 并存。
- 历史：四个早期文档 Session（KC15/WORKLINE/CORE-ESSAY/TIME-ORDER）只登记身份与 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`，不倒填收据。
- 不改任何 KC 原文；不 push；fresh model behavior NOT_RUN。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "runtime_version": R.VERSION,
        "release_ref": RELEASE_REF,
        "imported_package": "MP-VERIFICATION-EVENT-001",
        "project_run": PROJECT_RUN,
        "claims": "C-149-C-156",
        "mathematics": "MACHINE_REPLAYED_IN_PROJECT_WITH_SCOPE",
        "push": "NOT_AUTHORIZED",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    state["revision"] = 98
    state["latest_session"] = SESSION_ID
    state["load_policy"].update({"manifest_version": "3.5.0"})
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_EXTERNAL_WORK_IMPORT",
        "status": STATUS,
        "release_ref": RELEASE_REF,
    })
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"].update(
        {"projection_generation": "20260913-direction-082", "semantic_status": STATUS})
    state["records"]["I-OUTCOME-PANORAMA-20260912"].update(
        {"projection_generation": "20260913-outcome-082", "semantic_status": STATUS})
    for sid, scope in EARLY_SESSIONS.items():
        base = f".codex/research/hott/sessions/{sid}"
        state["records"][sid] = {
            "kind": "session", "path": f"{base}/SESSION.md", "status": "complete",
            "lifecycle_status": "HISTORICAL", "evidence_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
            "depends_on": [], "related_records": [SESSION_ID],
            "full_sources": [f"{base}/SESSION.md", f"{base}/CORE_COGNITION_AUDIT.md", f"{base}/RUNS.json"],
            "source_hashes": {},
            "scope": scope,
            "revalidation": ("Registered as historical evidence by " + SESSION_ID + ": these sessions were authored "
                             "before the sharding waves and have no canonical checkpoint receipt; nothing is back-dated."),
        }
    state["records"]["A-VERIFICATION-EVENT-IMPORT-001"] = {
        "kind": "result",
        "path": EVIDENCE,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "MACHINE_PROVED_LOCAL_UNCOMMITTED",
        "depends_on": [],
        "related_records": ["A-LOAD-GOVERNANCE-V3-001"],
        "full_sources": [EVIDENCE, PACKAGE_SOURCE, "HoTT/formal/verification-event/README.md",
                         f"{PROJECT_RUN}/RUN.json", f"{PROJECT_RUN}/index-row-manifest.json",
                         "HoTT/CLAIM_EVIDENCE_MATRIX.md",
                         f"{IMPORT_ROOT}/IMPORT.json",
                         f"{IMPORT_ROOT}/project-negative-probe/probe.json"],
        "source_hashes": {PACKAGE_SOURCE: R.sha((root / PACKAGE_SOURCE).read_bytes()),
                          "HoTT/formal/verification-event/TOOLCHAIN.json":
                              R.sha((root / "HoTT/formal/verification-event/TOOLCHAIN.json").read_bytes())},
        "scope": ("Imported independent-source finite verification-event model, replayed in-project: "
                  "stage-preserving historical verification is constructible, past-to-current rewriting does not exist, "
                  "and full stage erasure does not preserve the judgement. C-149–C-156; verdict "
                  "VERIFICATION_EVENT_STAGE_BOUNDARY_WITH_POSITIVE_CONTROL."),
    }
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [], "related_records": [PREV, "A-VERIFICATION-EVENT-IMPORT-001"] + sorted(EARLY_SESSIONS),
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, EVIDENCE,
                         f"{IMPORT_ROOT}/IMPORT.json", PACKAGE_SOURCE, f"{PROJECT_RUN}/RUN.json"],
        "source_hashes": {},
        "scope": "Absorption of the external verification-event package: byte-preserved originals, independent verification, in-project canonical replay, matrix rows, additive registry entry, trio update.",
    }
    texts = {
        R.DIRECTION: projections["DIRECTION"]["index_text"],
        R.PANORAMA: projections["PANORAMA"]["index_text"],
        "MEMORY.md": memory["index_text"],
        f"{R.PREFIX}FRONTIER.md": (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8"),
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    texts.update(projections["DIRECTION"]["shards"])
    texts.update(projections["PANORAMA"]["shards"])
    texts.update(memory["shards"])
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": ("User asked to absorb the other AI's work from the named handoff file into this repo so future "
                          "AIs know what happened: preserve originals byte-exactly, verify independently, deploy the source "
                          "owner, run the project canonical capture, index the claims, register additively, update the trio, "
                          "and commit locally. No push."),
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
             "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 98,
                      "session_id": SESSION_ID, "repinned": sorted(repinned), "files": len(texts)},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
