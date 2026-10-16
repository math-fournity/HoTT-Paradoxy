#!/usr/bin/env python3
"""Prepare revision 92: project-local governance/proof Git version closure."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260913-092-GOVERNANCE-V3-2-VERSION-CLOSURE"
PREV = "S-GOV-20260913-091-GOVERNANCE-REPAIR-ALIGNMENT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
ASSET_COMMIT = "d3dfb0e1869f5f05527f23ef4cb05dc95352eb10"
RELEASE_REF = "governance-v3.2.0"
REGISTRY = "HoTT/verification/PROOF_VERSION_CLOSURE.json"
RELEASE_EVIDENCE = "audit/governance-v3.2.0-release-evidence-20260913.md"
VERSION_VERIFIER = "scripts/audit/verify_proof_version_closure.py"

SPEC = importlib.util.spec_from_file_location("runtime_s092", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1: raise ValueError(f"REPLACE_COUNT:{old[:100]}:{text.count(old)}")
    return text.replace(old, new, 1)


def replace_line_prefix(text: str, prefix: str, new: str) -> str:
    lines = text.splitlines(); hits = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(hits) != 1: raise ValueError(f"LINE_PREFIX_COUNT:{prefix}:{len(hits)}")
    lines[hits[0]] = new
    return "\n".join(lines) + "\n"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    aligned = {
        "KC-000001": "把研究证据从本地未提交推进到 exact commit/ref 可恢复，增强‘凭什么’的版本锚点。",
        "KC-000005": "Version closure 不宣布悖论；只封存已有窄结论与开放边界。",
        "KC-000017": "跨 Session 认知输入、治理和 proof 资产现在有可恢复 Git ref，可对抗压缩后的记忆漂移。",
        "KC-000021": "17 个 proof source/run/index 已固定到 exact commit；Git closure 与 kernel proof 仍明确分层。",
        "KC-000022": "两类现实相对悖论仍未建立，版本封存不改变研究判词。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮仅做 Git/version closure。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]; label = str(unit["semantic_label"]).replace("|", "\\|")
        if kid in aligned: relation = "ALIGNED"; assessment = aligned[kid]
        else: relation = "NOT_TOUCHED"; assessment = f"本轮没有研究或重新裁决“{label}”的数学/哲学内容。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{REGISTRY}`；`{RELEASE_EVIDENCE}`；{kid} | E6、现实桥梁、自馈不可停机与 HoTT 悖论仍未建立。 |")
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: NO — 无新用户原文，generation-4/36 保持不变。",
        "- direction_change: NO_SEMANTIC_CHANGE — 只更新 Git/version 状态；下游 E6 consumer 仍第一线。",
        "- panorama_change: YES_STATUS_ONLY — current proof/replay 从 local 状态映射到 exact-commit version closure；frozen matrix rows 不改。",
        "- update_decision: 17 package/90 claim + C-05 外部重放绑定到 d3dfb0e；S092 current owners 与 release ref 对齐。",
        "- cross_conflicts: frozen matrix 行必须保持 run-time 状态文本，与 current Git 状态分离；追加 registry 消解，不原位改行。",
        "- unresolved: fresh model behavior NOT_RUN；并行工作树有未提交资产；数学目标仍开放；不 push。",
        "", "## 汇总", "", "`ALIGNED=5`；`NOT_TOUCHED=31`；无 `DEVIATED`。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(); root = ROOT
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 91 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_91_S091")

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = replace_line_prefix(memory, "7. 接手现场已由 Git commit", "7. 版本闭合：接手现场 `35cace7`、proof/治理修复资产 `d3dfb0e…`、current metadata S092 与本地 annotated `governance-v3.2.0` 形成可恢复链；未 push。")
    memory = replace_line_prefix(memory, "- project-local governance 3.2", "- project-local governance 3.2 已由 S090/S091/S092 canonical checkpoints 与本地 annotated `governance-v3.2.0` 闭合；runtime 3.2 / PROTOCOL 2.3 / business Skill 1.8；不 push，fresh model behavior 仍 NOT_RUN。")
    memory = replace_line_prefix(memory, "- `MP-ERCF-001` 是 F-011 下首个真实数学 package", "- `MP-ERCF-001` 是 F-011 下首个真实数学 package：Lean 4.33.1 final run/index/hash/exact replay PASS；其与其余 16 个 current package 的 proof assets 已固定到 commit `d3dfb0e…`，当前 Git 维度为 version-closed；仍只证明各自精确范围。")
    memory = replace_once(memory, "## 当前已验证状态\n\n", "## 当前已验证状态\n\n- S092 版本闭合：17 个 current proof package（90 个 current-project claims）与 C-05 external replay 绑定 exact commit `d3dfb0e…`；frozen matrix rows 不改，追加 registry 表达 current Git 维度；release ref `governance-v3.2.0`。\n")
    memory = memory.replace("EXACT_INDEX_SNAPSHOT_MATCH", "ROW_STABLE_AFTER_INDEX_EVOLUTION")

    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = replace_once(direction, "source_state_revision: 91", "source_state_revision: 92")
    direction = replace_once(direction, "projection_generation: 20260913-direction-075", "projection_generation: 20260913-direction-076")
    direction = replace_once(direction, "状态：`GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING`", "状态：`GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST`")
    direction = replace_once(direction, "semantic_status: GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING", "semantic_status: GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST")
    direction = replace_line_prefix(direction, "| `DIR-G-CHECKPOINT-HYDRATION-INTEGRITY`", "| `DIR-G-CHECKPOINT-HYDRATION-INTEGRITY` | applied checkpoint 必须有 canonical transaction/result，Session evidence 与 36-KC audit 同事务；叙事关系不递归污染 task hydration | 用户 ruling §16 / F-012 | `ACTIVE_USER_DIRECTION` | `CORE_UNRELATED/GOVERNANCE_RULING` | `OUT-TOP-GOVERNANCE-CHECKPOINT-HYDRATION` | S090/S091/S092 receipts 与五个 task plan 已闭合；历史 S086–S089 缺口不伪造；继续观察 fresh model behavior | `docs/design/detailed/认知水合关系与检查点事务合同.md`；`audit/S090治理修复实施与验收证据-20260913.md`；`governance-v3.2.0` |")

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = replace_once(panorama, "source_state_revision: 91", "source_state_revision: 92")
    panorama = replace_once(panorama, "projection_generation: 20260913-outcome-075", "projection_generation: 20260913-outcome-076")
    panorama = replace_once(panorama, "状态：`GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING`", "状态：`GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST`")
    panorama = replace_once(panorama, "semantic_status: GOVERNANCE_REPAIR_VERIFIED_VERSION_CLOSE_PENDING", "semantic_status: GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST")
    local_row = "| `MACHINE_PROVED_LOCAL_UNCOMMITTED` | 精确 claim/source/kernel run/index 链已在当前工作树闭合，但尚未进入获准 Git commit，不能声称 version-closed |"
    panorama = replace_once(panorama, local_row, local_row + "\n| `MACHINE_PROVED_VERSION_CLOSED` | 精确 proof/source/run/index 已进入 registry 指定的可恢复 Git commit；不扩大命题或替代 kernel proof |")
    panorama = panorama.replace("MACHINE_PROVED_LOCAL_UNCOMMITTED", "MACHINE_PROVED_VERSION_CLOSED")
    # Restore the state-definition row: local-uncommitted remains a valid state even though current packages advanced.
    panorama = panorama.replace("| `MACHINE_PROVED_VERSION_CLOSED` | 精确 claim/source/kernel run/index 链已在当前工作树闭合，但尚未进入获准 Git commit，不能声称 version-closed |", local_row)
    panorama = panorama.replace("`REPLAYED_EXTERNAL_LIBRARY_WITH_SCOPE`", "`MACHINE_REPLAYED_EXTERNAL_LIBRARY_VERSION_CLOSED_WITH_SCOPE`")
    panorama = panorama.replace("version-close 仍待最终 tag", "17 个 current package 已由 exact commit/version registry 闭合；fresh behavior 仍 NOT_RUN")
    panorama = panorama.replace("EXACT_INDEX_SNAPSHOT_MATCH", "ROW_STABLE_AFTER_INDEX_EVOLUTION")

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = frontier.replace("machine-proved-local-uncommitted", "machine-proved-version-closed")
    frontier = frontier.replace("MACHINE_PROVED_LOCAL_UNCOMMITTED", "MACHINE_PROVED_VERSION_CLOSED")
    frontier = frontier.replace("`REPLAYED_EXTERNAL_LIBRARY_WITH_SCOPE`", "`MACHINE_REPLAYED_EXTERNAL_LIBRARY_VERSION_CLOSED_WITH_SCOPE`")
    frontier = frontier.replace("EXACT_INDEX_SNAPSHOT_MATCH", "ROW_STABLE_AFTER_INDEX_EVOLUTION")
    frontier = replace_once(frontier, "\n本轮 S090 不新增数学结论", "\nS092 只更新 Git 可恢复性：17 个 current package 已绑定 `d3dfb0e…`，frozen claim rows 保持不变；数学范围与第一研究线不变。\n\n本轮 S090 不新增数学结论")
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    if not lessons.endswith("\n"): lessons += "\n"
    lessons += "\n71. Proof run 的 frozen index row 与当前 Git closure 是正交维度：原位把 `LOCAL_UNCOMMITTED` 改成 `VERSION_CLOSED` 会破坏历史 row manifest。正确做法是保持旧行逐字不变，在矩阵末尾追加 exact commit registry，并由 current STATE/投影引用；Git closure 不重证数学。\n"
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(resume, "## 当前停止点\n", "## 当前停止点\nS092 version closure：17 个 current package/90 claims + C-05 external replay 绑定 `d3dfb0e…`；current Git 维度 version-closed，frozen matrix rows/RUN.json 不改；本地 release ref `governance-v3.2.0`，未 push。\n\n")
    resume = resume.replace("MACHINE_PROVED_LOCAL_UNCOMMITTED", "MACHINE_PROVED_VERSION_CLOSED")
    resume = resume.replace("EXACT_INDEX_SNAPSHOT_MATCH", "ROW_STABLE_AFTER_INDEX_EVOLUTION")

    records = state["records"]
    project_keys = [key for key, rec in records.items() if key.startswith("A-") and rec.get("evidence_status") == "MACHINE_PROVED_LOCAL_UNCOMMITTED"]
    if len(project_keys) != 18: raise SystemExit(f"EXPECTED_18_PROJECT_PROOF_RECORDS:{len(project_keys)}")
    external_key = "A-UNIMATH-NOSECTION-REPLAY-001"
    closure = {"status": "VERSION_CLOSED", "proof_asset_commit": ASSET_COMMIT, "release_ref": RELEASE_REF, "registry": REGISTRY, "scope_preserved": True}
    for key in project_keys:
        rec = records[key]; rec["evidence_status"] = "MACHINE_PROVED_VERSION_CLOSED"; rec["version_closure"] = dict(closure)
        if isinstance(rec.get("formal"), dict): rec["formal"]["index_validation"] = "ROW_STABLE_AFTER_INDEX_EVOLUTION"
        if isinstance(rec.get("resolution"), dict):
            reason = rec["resolution"]["reason"]
            reason = reason.replace(" Git version closure is not authorized, so status remains local-uncommitted.", "")
            reason = reason.replace(" Git version closure is not authorized.", "")
            rec["resolution"]["reason"] = reason + f" Proof/source/run/index assets are Git-version-closed at {ASSET_COMMIT}; current matrix evolution is append-only and does not alter the theorem scope."
    external = records[external_key]
    external["evidence_status"] = "MACHINE_REPLAYED_EXTERNAL_LIBRARY_VERSION_CLOSED_WITH_SCOPE"
    external["version_closure"] = dict(closure)
    external["formal"]["index_validation"] = "ROW_STABLE_AFTER_INDEX_EVOLUTION"
    external["resolution"]["reason"] += f" The replay assets are Git-version-closed at {ASSET_COMMIT}; this does not extend replay to foundation.global-choice."

    math_gate = records["A-MATH-PROOF-DELIVERY-GATE-001"]
    for rel in [REGISTRY, VERSION_VERIFIER, RELEASE_EVIDENCE]:
        if rel not in math_gate["full_sources"]: math_gate["full_sources"].append(rel)
    math_gate["scope"] = "Require machine proof source/run/index before delivery. Seventeen current packages (90 current-project claims) plus the scoped C-05 external replay are Git-version-closed at d3dfb0e; frozen rows remain unchanged. Fresh-model behavior remains NOT_RUN."
    records["A-PROOF-VERSION-CLOSURE-001"] = {
        "kind": "proof_version_closure", "path": REGISTRY, "status": "complete", "lifecycle_status": "CURRENT", "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "17_PACKAGES_90_CLAIMS_PLUS_C05_VERSION_CLOSED", "depends_on": [],
        "related_records": sorted(project_keys + [external_key, "A-MATH-PROOF-DELIVERY-GATE-001"]),
        "full_sources": [REGISTRY, "HoTT/CLAIM_EVIDENCE_MATRIX.md", VERSION_VERIFIER, RELEASE_EVIDENCE, RESULT_REL], "source_hashes": {},
        "resolution": {"reason": f"All listed proof source/run/index assets exist in exact commit {ASSET_COMMIT}; current matrix is an append-only successor preserving frozen rows.", "evidence": [REGISTRY, "HoTT/CLAIM_EVIDENCE_MATRIX.md", VERSION_VERIFIER, RELEASE_EVIDENCE]},
        "scope": "Git recoverability and current evidence status only; does not re-prove or expand mathematics.",
    }
    records["A-GOVERNANCE-V3-2-RELEASE-001"] = {
        "kind": "governance_release", "path": RELEASE_EVIDENCE, "status": "complete", "lifecycle_status": "CURRENT", "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "PROJECT_LOCAL_GOVERNANCE_V3_2_VERSION_CLOSED", "depends_on": [],
        "related_records": ["A-GOVERNANCE-REPAIR-S090-001", "A-PROOF-VERSION-CLOSURE-001"],
        "full_sources": [RELEASE_EVIDENCE, REGISTRY, VERSION_VERIFIER, RESULT_REL], "source_hashes": {},
        "resolution": {"reason": "Project-local governance 3.2 is closed by the S090-S092 canonical checkpoint chain, exact Git commits and the local annotated release ref; no push.", "evidence": [RELEASE_EVIDENCE, REGISTRY, VERSION_VERIFIER]},
        "scope": "Local Git release only; shared governance repositories and other hosts are unchanged.",
    }

    session_path = f"{SESSION_REL}/SESSION.md"; audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"; runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 目的：把 17 个 current proof package、90 个 current-project claims 与 C-05 scoped external replay 的 Git 维度绑定到 exact commit `{ASSET_COMMIT}`，并闭合 project-local governance 3.2。
- Frozen proof/claim rows 与历史 RUN.json 不改；当前矩阵只 append version registry。
- S090/S091 checkpoint、task hydration 与 evidence corrections 保持；数学范围不变，E6/悖论仍未建立。
- 本地 release ref：`{RELEASE_REF}`；本 checkpoint 成功后提交并创建 annotated tag；不 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "proof_asset_commit": ASSET_COMMIT, "registry": REGISTRY, "version_verifier": VERSION_VERIFIER,
        "package_count": 17, "machine_proved_claim_count": 90, "external_replayed_claim_count": 1,
        "checkpoint_result": RESULT_REL, "release_ref": RELEASE_REF,
        "mathematics": "NOT_REPROVED_OR_EXPANDED_BY_GIT_CLOSURE", "push": "NOT_AUTHORIZED",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    state["revision"] = 92; state["latest_session"] = SESSION_ID
    state["execution_control"].update({"last_checkpoint_session": SESSION_ID, "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT", "status": "GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"})
    state["projection"]["status"] = "CORE_GENERATION_4_GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"
    state["load_policy"]["manifest_version"] = "3.2.0"
    records["I-DIRECTION-PORTFOLIO-20260912"].update({"projection_generation": "20260913-direction-076", "semantic_status": "CORE_GENERATION_4_GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"})
    records["I-OUTCOME-PANORAMA-20260912"].update({"projection_generation": "20260913-outcome-076", "semantic_status": "CORE_GENERATION_4_GOVERNANCE_V3_2_VERSION_CLOSED_DOWNSTREAM_E6_CONSUMER_FIRST"})
    records[SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete", "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [], "related_records": [PREV, "A-PROOF-VERSION-CLOSURE-001", "A-GOVERNANCE-V3-2-RELEASE-001"],
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, REGISTRY, RELEASE_EVIDENCE, VERSION_VERIFIER], "source_hashes": {},
        "scope": "Git/version closure only; no new or expanded mathematical claim.",
    }
    texts = {
        "MEMORY.md": memory, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons, f"{R.PREFIX}RESUME.md": resume,
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    def proposed(rel: str) -> bytes:
        if rel in texts: return texts[rel].encode("utf-8")
        path = root / rel
        if not path.is_file(): raise ValueError(f"HASH_TARGET_MISSING:{rel}")
        return path.read_bytes()
    for key, rec in records.items():
        hashes = rec.get("source_hashes")
        if not isinstance(hashes, dict): continue
        changed = False
        for rel, old in list(hashes.items()):
            new = sha_bytes(proposed(rel))
            if new != old: hashes[rel] = new; changed = True
        if changed:
            rec["revalidation"] = f"S092 records Git version closure at {ASSET_COMMIT} and refreshes append-only matrix/registry/current-owner hashes; retained proof source and run bodies are unchanged."
    for key in ("A-PROOF-VERSION-CLOSURE-001", "A-GOVERNANCE-V3-2-RELEASE-001"):
        rec = records[key]
        for rel in rec["resolution"]["evidence"]: rec["source_hashes"][rel] = sha_bytes(proposed(rel))
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "User explicitly authorized the recommended exact local commit/tag. This checkpoint records Git version closure for already committed project assets and updates in-repo cognition owners only; no push, publication, source restoration or mathematical expansion.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value} for rel, value in texts.items()],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 92, "session_id": SESSION_ID, "project_proof_records": len(project_keys), "external_replay_records": 1}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
