#!/usr/bin/env python3
"""Prepare a checkpoint rebinding C0R8 to its final proof receipts.

The source-to-spec Markdown inputs were cleaned before Git closure.  New primary
runs re-pinned their exact bytes; this checkpoint updates only the current C0R8
record's run locators and hashes.  It does not alter any theorem or research verdict.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / ".codex" / "tools"))
import cognition_runtime as R
import projection_edit


TARGET = "S-RES-20261005-ZFC-META-SUBTHEORY-C0R8-MSS-CONTROLS-001"
SESSION_ID = "S-GOV-20261005-ZFC-META-SUBTHEORY-C0R8-FINAL-RECEIPT-REBIND-001"
OLD_DOMAIN = "20261005-MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001-03"
NEW_DOMAIN = "20261005-MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001-04"
OLD_ORDER = "20261005-MP-ZFC-MSS-PHASE-ORDER-CONTROL-001"
NEW_ORDER = "20261005-MP-ZFC-MSS-PHASE-ORDER-CONTROL-002"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read(root: Path, rel: str) -> str:
    return (root / rel).read_text(encoding="utf-8")


def mutable_with_shards(root: Path) -> list[str]:
    paths: list[str] = []
    for rel in R.MUTABLE:
        if rel not in paths:
            paths.append(rel)
        index = R.parse_shard_index((root / rel).read_bytes(), rel)
        if index is not None:
            for row in index["shards"]:
                if row["path"] not in paths:
                    paths.append(row["path"])
    return paths


def prepend_once(text: str, marker: str, block: str) -> str:
    if marker in text:
        return text
    i = text.find("\n")
    return text[: i + 1] + block + text[i + 1 :]


def audit_text(root: Path) -> str:
    prior = read(root, f".codex/research/hott/sessions/{TARGET}/CORE_COGNITION_AUDIT.md")
    prior = prior.replace(f"# CORE COGNITION AUDIT — {TARGET}", f"# CORE COGNITION AUDIT — {SESSION_ID}", 1)
    old = "> **scope:** C0R8 MSS/domain/phase-order source and machine controls. The unit establishes representation-level positive and negative controls plus a real operational-consumer seed; it fixes no bare-ZFC core contract and no C6 verdict."
    new = "> **scope:** C0R8 final receipt rebinding. The proof inputs were byte-recaptured after documentation whitespace cleanup; this changes evidence locators/hashes only, not any source, theorem, or core verdict."
    if old not in prior:
        raise SystemExit("AUDIT_SCOPE_NOT_FOUND")
    prior = prior.replace(old, new, 1)
    replacements = {
        "- direction_change: YES — F-053 C0 frontier从C0R8 cited-source screen推进到C0R9 ZFC-specific temporal-operation contract screen。": "- direction_change: NO — C0R9 remains the current successor; this unit rebinds final proof receipts only。",
        "- panorama_change: YES — 新增C-375–C-378的两个Lean-core source-motivated representation controls。": "- panorama_change: NO — C-375–C-378 and their source-to-spec classifications are unchanged。",
        "- update_decision: 写回C0 manifest、taskcards、primary source snapshots、two proof packages/runs/matrix/registry、MEMORY/方向/全景/STATE与新session。": "- update_decision: 将C0R8 record从pre-cleanup runs重绑到final `…-04` / `…-002` primary receipts，并保存新的registry/matrix/index hashes。",
        "- cross_conflicts: source把time definability与domain recovery并置，同时把state description与prediction/operational caveat并置；这支持分层，不支持把任一层偷换为ZFC core verdict。": "- cross_conflicts: receipt rebinding occurs because exact source manifests are byte-sensitive; it is evidence hygiene, not an additional theoretical or philosophical argument。",
        "- unresolved: ZFC-specific M、fixed operational/process Q、actual P、FormalDone→OriginDone bridge、foundation adequacy role、SameQ_H0和C6仍未支付。": "- unresolved: ZFC-specific M、fixed operational/process Q、actual P、FormalDone→OriginDone bridge、foundation adequacy role、SameQ_H0和C6仍未支付；receipt rebinding does not alter any of them。",
    }
    for old_line, new_line in replacements.items():
        if old_line not in prior:
            raise SystemExit(f"AUDIT_LINE_NOT_FOUND:{old_line[:45]}")
        prior = prior.replace(old_line, new_line, 1)
    marker = "## 本单元 source-first 对照"
    repair = """## 本单元的最终收据重绑

- `MSSDomainTimeControl.lean` 与 `MSSPhaseOrderControl.lean` 都没有改变；
- 唯一变化是 source-to-spec Markdown 的尾随空格清理，因而旧source manifest按设计失效；
- 两个新 primary run重跑同一Lean命令，固定新字节哈希并通过exact replay；
- C0R8 state record现在只指向新的 primary receipts；之前的未提交中间run不进入Git证据链。

"""
    if repair not in prior:
        prior = prior.replace(marker, repair + marker, 1)
    return prior


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    root = ROOT.resolve()
    plan = R.plan(root, profile="research")
    if (root / f".codex/research/hott/sessions/{SESSION_ID}").exists():
        raise SystemExit("SESSION_ALREADY_EXISTS")
    texts = {rel: read(root, rel) for rel in mutable_with_shards(root)}
    state = json.loads(texts[R.STATE])
    revision = state["revision"] + 1
    record = state["records"].get(TARGET)
    if not isinstance(record, dict):
        raise SystemExit("TARGET_RECORD_MISSING")
    replacements = ((OLD_DOMAIN, NEW_DOMAIN), (OLD_ORDER, NEW_ORDER))
    record["full_sources"] = [
        next((path.replace(old, new) for old, new in replacements if old in path), path)
        for path in record["full_sources"]
    ]
    record["source_hashes"] = {path: sha((root / path).read_bytes()) for path in record["full_sources"]}
    record["revalidation"] = (
        "Final proof-receipt rebinding: documentation whitespace cleanup changed source-manifest bytes, so new primary Lean runs "
        f"{NEW_DOMAIN} and {NEW_ORDER} recaptured the unchanged theorems and fixed the final receipt hashes. "
        "C-375–C-378, source classification, C0R9 and C6 scope are unchanged."
    )
    state["revision"] = revision
    state["latest_session"] = SESSION_ID
    repair_sources = [
        ".codex/research/hott/STATE.json",
        f".codex/research/hott/sessions/{TARGET}/CORE_COGNITION_AUDIT.md",
        f"HoTT/verification/runs/{NEW_DOMAIN}/RUN.json",
        f"HoTT/verification/runs/{NEW_DOMAIN}/index-row-manifest.json",
        f"HoTT/verification/runs/{NEW_ORDER}/RUN.json",
        f"HoTT/verification/runs/{NEW_ORDER}/index-row-manifest.json",
        "HoTT/CLAIM_EVIDENCE_MATRIX.md",
        "HoTT/verification/PROOF_VERSION_CLOSURE.json",
    ]
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "C0R8_FINAL_PROOF_RECEIPTS_REBOUND / NO_MATHEMATICAL_STATUS_CHANGE",
        "full_sources": repair_sources,
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
        "path_mode": "document",
        "related_records": [TARGET],
        "scope": "Rebinds C0R8 to final primary proof receipts after Markdown byte cleanup. No formal proposition, source interpretation, current successor, or bare-ZFC conclusion changes.",
        "source_hashes": {path: sha((root / path).read_bytes()) for path in repair_sources},
        "status": "complete",
    }
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    for index_rel in ("方向追踪.md", "全景视野.md"):
        doc = projection_edit.load(root, index_rel)
        # The preceding route-repair checkpoint intentionally left the header's
        # source revision at 309 while moving its generation label to 310.
        # Update both fields on the same in-memory index document so one edit
        # cannot overwrite the other.
        projection_edit.replace_in_index(doc, "source_state_revision: 309", f"source_state_revision: {revision}")
        projection_edit.replace_in_index(doc, "projection_generation: 20261005-zfc-mss-route-repair-310", f"projection_generation: 20261005-zfc-mss-final-receipts-{revision}")
        texts[index_rel] = doc["index_text"]
        texts.update(doc["shards"])

    note = """### `C0R8` final receipt rebinding（2026-10-05）

Markdown source-to-spec cards were whitespace-cleaned before the commit; their byte changes correctly
required recapturing the two primary Lean receipts. `…DOMAIN…-04` and `…PHASE…-002` now own C-375–C-378.
The previous uncommitted run folders are not evidence pointers. No mathematical or C0 status changed.

"""
    marker = "### `C0R8` final receipt rebinding（2026-10-05）"
    if marker not in texts["MEMORY/001 - 当前执行队列.md"]:
        needle = "## 想法 T：理论精度、观察边界与哥德尔式自反（2026-10-04）"
        texts["MEMORY/001 - 当前执行队列.md"] = texts["MEMORY/001 - 当前执行队列.md"].replace(needle, note + needle, 1)
    texts[R.PREFIX + "FRONTIER.md"] = prepend_once(texts[R.PREFIX + "FRONTIER.md"], marker, note)
    texts[R.PREFIX + "RESUME.md"] = prepend_once(
        texts[R.PREFIX + "RESUME.md"],
        "## C0R8 final proof receipts（2026-10-05）",
        f"""## C0R8 final proof receipts（2026-10-05）

Use `{NEW_DOMAIN}` for C-375/C-376 and `{NEW_ORDER}` for C-377/C-378. These are final
primary receipts after source-manifest byte rebinding; all earlier uncommitted local receipts are
non-authoritative.

""",
    )
    log = "MEMORY/003 - 当前验证状态与顺序日志.md"
    if SESSION_ID not in texts[log]:
        texts[log] += f"\n\n{SESSION_ID}：C0R8 final receipt rebinding: C-375/C-376 → `{NEW_DOMAIN}`，C-377/C-378 → `{NEW_ORDER}`。原因是source-to-spec Markdown whitespace cleanup造成manifest byte drift；数学范围不变。\n"

    base = f".codex/research/hott/sessions/{SESSION_ID}/"
    texts[base + "SESSION.md"] = f"""# {SESSION_ID}

> **Role:** `GOVERNANCE_ALIGNMENT`.
> **Tier:** `T3` — final proof-receipt binding; no mathematical claim changed.

## Result

The exact source-manifest inputs of C0R8 documentation changed only by whitespace cleanup. Two new
primary Lean core runs rechecked the unchanged proof sources and now own C-375–C-378:

- `{NEW_DOMAIN}` for domain/endpoint control;
- `{NEW_ORDER}` for phase/order control.

The C0R8 STATE record, matrix and registry now point to those receipts. C0R9 remains next.
"""
    texts[base + "RUNS.json"] = json.dumps({
        "next": "Continue C0-SUCCESSOR-RESELECTION-009; receipt rebinding is complete.",
        "role": "GOVERNANCE_ALIGNMENT",
        "schema_version": "hott-research-runs/v1",
        "session_id": SESSION_ID,
        "status": "C0R8_FINAL_RECEIPTS_REBOUND_NO_MATHEMATICAL_STATUS_CHANGE",
        "tier": "T3",
        "verification": [
            {"command": f"verify_formal_proof_run.py --run-dir HoTT/verification/runs/{NEW_DOMAIN} --rerun", "scope": "C-375/C-376 exact replay", "status": "PASS_WITH_SCOPE"},
            {"command": f"verify_formal_proof_run.py --run-dir HoTT/verification/runs/{NEW_ORDER} --rerun", "scope": "C-377/C-378 exact replay", "status": "PASS_WITH_SCOPE"},
        ],
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    texts[base + "CORE_COGNITION_AUDIT.md"] = audit_text(root)

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User authorized durable ZFC research, proof evidence repair, exact-path commit, and remote push. This checkpoint only rebinds final receipts.",
        "load_profile": "research",
        "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": sha((root / rel).read_bytes()) if (root / rel).is_file() else None, "text": texts[rel]}
            for rel in sorted(texts)
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": revision, "session_id": SESSION_ID, "files": len(payload["files"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
