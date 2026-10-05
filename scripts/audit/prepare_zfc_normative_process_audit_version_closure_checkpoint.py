#!/usr/bin/env python3
"""Prepare the corrective final-run checkpoint for the Q_norm proof package.

The previous Q_norm session faithfully preserved the then-primary `…-02` run.
This successor does not revise that immutable session.  It records why the
source-manifest became stale after documentation changed and promotes the
fresh, fully pinned `…-03` run as the only current primary receipt.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".codex" / "tools"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import cognition_runtime as R
import projection_edit
import prepare_zfc_normative_process_audit_checkpoint as P


SESSION_ID = "S-RES-20261005-ZFC-META-SUBTHEORY-QNORM-VERSION-CLOSURE-001"
PREVIOUS_SESSION = "S-RES-20261005-ZFC-META-SUBTHEORY-QNORM-001"
RUN_ID = "20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-03"
PROOF_ID = "MP-ZFC-NORMATIVE-PROCESS-AUDIT-001"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def text(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def update_direction(root: Path, texts: dict[str, str], revision: int) -> None:
    doc = projection_edit.load(root, "方向追踪.md")
    projection_edit.replace_in_index(doc, "source_state_revision: 307", f"source_state_revision: {revision}")
    projection_edit.replace_in_index(
        doc,
        "projection_generation: 20261005-zfc-normative-process-audit-307",
        f"projection_generation: 20261005-zfc-normative-process-audit-version-closure-{revision}",
    )
    texts["方向追踪.md"] = doc["index_text"]
    texts.update(doc["shards"])


def update_panorama(root: Path, texts: dict[str, str], revision: int) -> None:
    doc = projection_edit.load(root, "全景视野.md")
    projection_edit.replace_in_index(doc, "source_state_revision: 307", f"source_state_revision: {revision}")
    projection_edit.replace_in_index(
        doc,
        "projection_generation: 20261005-zfc-normative-process-audit-307",
        f"projection_generation: 20261005-zfc-normative-process-audit-version-closure-{revision}",
    )
    shard = "全景视野/003 - 当前机器证明包与原生重放.md"
    projection_edit.replace_in_shard(
        doc,
        shard,
        "HoTT/verification/runs/20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-02/",
        "HoTT/verification/runs/20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-03/",
    )
    texts["全景视野.md"] = doc["index_text"]
    texts.update(doc["shards"])


def update_memory(text_value: str) -> str:
    old = "primary run `…-02` 含 source、\nLean binary digest、冻结矩阵行和 exact replay；首次 `…-01` 仅因 capture manifest 缺\nbinary pin 而未能版本闭合，已保留并由新的 run 取代。"
    new = "最终 primary run `…-03` 含稳定的 source、Lean binary digest、冻结矩阵行和 exact replay；`…-01` 因 capture manifest 缺binary pin，`…-02` 因其所pin的文档后来补充package链接而source manifest失效；二者均被保留但不作为当前primary。"
    if old not in text_value:
        raise SystemExit("MEMORY_QNORM_RUN_TEXT_MISSING")
    return text_value.replace(old, new, 1)


def audit_text(root: Path) -> str:
    prior = text(root, f".codex/research/hott/sessions/{PREVIOUS_SESSION}/CORE_COGNITION_AUDIT.md")
    prior = prior.replace(PREVIOUS_SESSION, SESSION_ID)
    prior = prior.replace(
        "dedicated ZFC+Q_norm process-completion audit interface; source-to-spec binding, Lean-core theorem/run/index closure and capture-pipeline repair; no bare-ZFC C6 theorem.",
        "Q_norm primary-run source-manifest repair: `…-03` replaces `…-02` only as the current evidence pointer; prior receipts remain historical; no bare-ZFC C6 theorem.",
        1,
    )
    old_fields = "- core_change: NO — 本单元没有新的用户元数学原文，不修改 core generation。\n- direction_change: YES — F-053 的 extension lane 从“准入/重放控制”变成有独立 C-370–C-374 package 的 `Q_NORM_EXTENSION_MACHINE_PROVED_WITH_SCOPE`；核心下一动作仍为 C0-SUCCESSOR-RESELECTION-003。\n- panorama_change: YES — 新增 `OUT-U-ZFC-NORMATIVE-PROCESS-AUDIT-C370-C374`，但明确标为 extension，不是 C6 结果。\n- essay_change: NO — 未修改扩展认知。\n- update_decision: 写回专用 proof package、claim matrix、registry、run、capture-pipeline repair、F-053、closure、MEMORY、方向/全景投影、C6 admission和新 session。\n- cross_conflicts: Q_norm 是研究发起人规范；C5E/C0R3说明 application bridge 是真实可问的问题，但现有 bare-ZFC sources并未把该规范指定为其职责。规范可机器化，不等于 bare-ZFC 已实例化。\n- unresolved: actual same M/S/Q/P/Adequacy contract、physical bridge payment、SameQ_H0、qualified Mizar/Isabelle replay和C6 core verdict仍未支付。"
    new_fields = "- core_change: NO — 本单元没有新的用户元数学原文，不修改 core generation。\n- direction_change: NO — F-053 的方向、核心下一动作和C6状态都不变。\n- panorama_change: YES — 既有 `OUT-U-ZFC-NORMATIVE-PROCESS-AUDIT-C370-C374` 的primary run由`…-02`精确换为`…-03`，无新数学命题。\n- essay_change: NO — 未修改扩展认知。\n- update_decision: 写回`…-03` run、registry/matrix primary pointer、capture-pipeline lineage、MEMORY/方向/全景/STATE与新session。\n- cross_conflicts: 旧run的成功不等同于其来源清单在后来文档变化后仍有效；历史收据保留，当前claim必须指向source hashes仍相等的run。\n- unresolved: actual same M/S/Q/P/Adequacy contract、physical bridge payment、SameQ_H0、qualified Mizar/Isabelle replay和C6 core verdict仍未支付。"
    if old_fields not in prior:
        raise SystemExit("AUDIT_FIELDS_MISSING")
    return prior.replace(old_fields, new_fields, 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = ROOT.resolve()
    plan = R.plan(root, profile="research")
    if (root / f".codex/research/hott/sessions/{SESSION_ID}").exists():
        raise SystemExit("SESSION_ALREADY_EXISTS")

    texts = {rel: text(root, rel) for rel in P.mutable_with_shards(root)}
    state = json.loads(texts[R.STATE])
    revision = state["revision"] + 1
    update_direction(root, texts, revision)
    update_panorama(root, texts, revision)
    queue_path = "MEMORY/001 - 当前执行队列.md"
    texts[queue_path] = update_memory(texts[queue_path])
    log_path = "MEMORY/003 - 当前验证状态与顺序日志.md"
    texts[log_path] += (
        f"\n\n{SESSION_ID}：`{PROOF_ID}` 的最终primary run重定为`…-03`。"
        "`…-01`缺Lean binary pin，`…-02`在extension/package documentation补充后source manifest drift；两份历史receipt均保留但不修改。"
        "`…-03`重新固定11个source、Lean binary、matrix行与exact replay，成为当前version-closure候选；C6仍未释放。\n"
    )

    sources = [
        "sources/prompts/Codex-ZFC核心层最终机器证明与不停机Goal-用户原文-20261004.md",
        "sources/prompts/Codex-ZFC元理论子理论时间与完成桥-用户原文-20261003.md",
        "dev-docs/ZFC元理论子理论充分性最终闭环SOP.md",
        "认知闭包/ZFC-META-SUBTHEORY-ADEQUACY-001.md",
        "HoTT/formal/zfc-normative-process-audit/ProcessCompletionAudit.lean",
        "HoTT/formal/zfc-normative-process-audit/CLAIM.md",
        f"HoTT/verification/runs/{RUN_ID}/RUN.json",
        f"HoTT/verification/runs/{RUN_ID}/source-manifest.json",
        f"HoTT/verification/runs/{RUN_ID}/index-row-manifest.json",
        "HoTT/CLAIM_EVIDENCE_MATRIX.md",
        "HoTT/verification/PROOF_VERSION_CLOSURE.json",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-NORMATIVE-PROCESS-AUDIT-PACKAGE.md",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-NORMATIVE-PROCESS-AUDIT-EXTENSION-ADMISSION.md",
    ]
    state["revision"] = revision
    state["latest_session"] = SESSION_ID
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "Q_NORM_PRIMARY_RUN_SOURCE_MANIFEST_VERSION_CLOSED_PENDING_GIT / CORE_C6_NOT_RELEASED",
        "full_sources": sources,
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
        "path_mode": "document",
        "related_records": [PREVIOUS_SESSION],
        "scope": "Corrective proof-evidence session: rebinds C-370–C-374 to the stable-source-manifest primary run -03 without changing their Lean theorem or scope. Bare-ZFC C6 stays unreleased.",
        "source_hashes": {p: sha((root / p).read_bytes()) for p in sources},
        "status": "complete",
    }
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    base = f".codex/research/hott/sessions/{SESSION_ID}/"
    texts[base + "SESSION.md"] = f"""# {SESSION_ID}

> **Role:** `RESEARCH_GENERATION`.
> **Tier:** `T3` — proof-evidence correction for C-370–C-374; no new mathematical theorem and no C6 core result.

## 研究对象

验证 `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` 的 current primary receipt 是否仍绑定其当前 source-to-spec材料和Lean binary。此前两个不可变历史run分别缺binary pin或在后续文档更新后发生source-manifest drift；本单元只修复证据绑定。

## 实际结果

- primary run `{RUN_ID}` 重新捕获11个稳定输入、`lean-core-binary` digest、proof/claim index rows，并通过 exact kernel replay。
- registry与claim matrix的primary pointer已转到`…-03`；`…-01`和`…-02`保留原状作为历史receipt。
- C-370–C-374 的Lean源码、命题和禁止外推不变；bare-ZFC C6的source-to-spec义务仍未支付。

## successor

继续 `C0-SUCCESSOR-RESELECTION-003`，而不是重做 Q_norm interface 或把它包装为 core verdict。
"""
    texts[base + "RUNS.json"] = json.dumps({
        "next": "C0-SUCCESSOR-RESELECTION-003: find an actual source contract; do not reopen the completed Q_norm interface absent a source/toolchain change.",
        "role": "RESEARCH_GENERATION",
        "schema_version": "hott-research-runs/v1",
        "session_id": SESSION_ID,
        "status": "PRIMARY_RUN_REBOUND_TO_STABLE_SOURCE_MANIFEST_C6_NOT_RELEASED",
        "tier": "T3",
        "verification": [
            {"command": f"python3 -B scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/{RUN_ID} --rerun", "scope": "exact proof run replay", "status": "PASS_WITH_SCOPE"},
            {"command": f"python3 -B scripts/audit/verify_proof_version_closure.py --proof-id {PROOF_ID} --evidence-only", "scope": "manifest/registry/index relation", "status": "LOCAL_EVIDENCE_PASS_NOT_VERSION_CLOSED"},
            {"command": "preserve -01/-02 receipts without mutation", "scope": "historical pipeline lineage", "status": "PASS"},
        ],
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    texts[base + "CORE_COGNITION_AUDIT.md"] = audit_text(root)

    files = []
    for rel in sorted(texts):
        target = root / rel
        files.append({"path": rel, "expected_sha256": sha(target.read_bytes()) if target.is_file() else None, "text": texts[rel]})
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User authorized continued execution, durable documentation, commit and push; this corrective checkpoint preserves exact proof evidence rather than silently replacing an old run.",
        "load_profile": "research",
        "task_ids": [],
        "files": files,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": revision, "session_id": SESSION_ID, "files": len(files)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
