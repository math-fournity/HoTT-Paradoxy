#!/usr/bin/env python3
"""Prepare a checkpoint repairing C0R8 binary-source hydration routing.

`full_sources` is a text-hydration field.  The C0R8 session initially listed
primary PDFs there, so `cognition_runtime plan --task` truthfully stopped at
`NOT_UTF8`.  This repair retains the PDFs in `binary_source_hashes` and in the
source snapshot README/cards, while leaving only text-readable entry points in
`full_sources`.
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


TARGET_SESSION = "S-RES-20261005-ZFC-META-SUBTHEORY-C0R8-MSS-CONTROLS-001"
SESSION_ID = "S-GOV-20261005-ZFC-META-SUBTHEORY-C0R8-BINARY-SOURCE-ROUTE-REPAIR-001"


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


def prepend_once(text: str, marker: str, addition: str) -> str:
    if marker in text:
        return text
    i = text.find("\n")
    return text[: i + 1] + addition + text[i + 1 :]


def audit_text(root: Path) -> str:
    prior = read(root, f".codex/research/hott/sessions/{TARGET_SESSION}/CORE_COGNITION_AUDIT.md")
    prior = prior.replace(f"# CORE COGNITION AUDIT — {TARGET_SESSION}", f"# CORE COGNITION AUDIT — {SESSION_ID}", 1)
    old_scope = "> **scope:** C0R8 MSS/domain/phase-order source and machine controls. The unit establishes representation-level positive and negative controls plus a real operational-consumer seed; it fixes no bare-ZFC core contract and no C6 verdict."
    new_scope = "> **scope:** C0R8 hydration-route repair. It changes only evidence routing: binary PDFs remain hash-pinned through text source-readmes/cards, while `full_sources` becomes UTF-8 readable. No mathematical claim, source assessment, C0 successor, or C6 status changes."
    if old_scope not in prior:
        raise SystemExit("AUDIT_SCOPE_NOT_FOUND")
    prior = prior.replace(old_scope, new_scope, 1)
    replacements = {
        "- core_change: NO — 本单元没有新的用户元数学原文，不修改 core generation。": "- core_change: NO — 本单元没有新的用户元数学原文，不修改 core generation。",
        "- direction_change: YES — F-053 C0 frontier从C0R8 cited-source screen推进到C0R9 ZFC-specific temporal-operation contract screen。": "- direction_change: NO — C0R9 与F-053方向不变；只修复未来session能读取C0R8 record的证据路由。",
        "- panorama_change: YES — 新增C-375–C-378的两个Lean-core source-motivated representation controls。": "- panorama_change: NO — C-375–C-378的证据与范围不变。",
        "- update_decision: 写回C0 manifest、taskcards、primary source snapshots、two proof packages/runs/matrix/registry、MEMORY/方向/全景/STATE与新session。": "- update_decision: 将C0R8 record的PDF从`full_sources`移入`binary_source_hashes`，保留text README/cards作为可水合入口；写回STATE/MEMORY/FRONTIER/RESUME与repair session。",
        "- cross_conflicts: source把time definability与domain recovery并置，同时把state description与prediction/operational caveat并置；这支持分层，不支持把任一层偷换为ZFC core verdict。": "- cross_conflicts: proof source manifest可以且必须pin binary PDF；cognition `full_sources`则是UTF-8 hydration contract。二者职责不同，不能为了文本加载删去原件，也不能把原件误当文本。",
        "- unresolved: ZFC-specific M、fixed operational/process Q、actual P、FormalDone→OriginDone bridge、foundation adequacy role、SameQ_H0和C6仍未支付。": "- unresolved: ZFC-specific M、fixed operational/process Q、actual P、FormalDone→OriginDone bridge、foundation adequacy role、SameQ_H0和C6仍未支付；C0R8 route repair不改变这些未知。",
    }
    for old, new in replacements.items():
        if old not in prior:
            raise SystemExit(f"AUDIT_TEXT_NOT_FOUND:{old[:40]}")
        prior = prior.replace(old, new, 1)
    heading = "## 本单元 source-first 对照"
    note = """## 本单元的证据路由修复

- 被修复的不是论文、PDF、Lean proof 或 source-to-spec解释；
- 失败模式是 `cognition_runtime plan --task C0R8` 对 PDF 产生 `NOT_UTF8`；
- 处理方式是 text README/card 保留在 `full_sources`，三个PDF的路径和SHA-256保留在
  `binary_source_hashes` 与 source snapshot README；
- 成功标准是同一C0R8 session record再次水合时不读取二进制内容。

"""
    if note not in prior:
        prior = prior.replace(heading, note + heading, 1)
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
    prior = json.loads(texts[R.STATE])
    revision = prior["revision"] + 1
    target = state["records"].get(TARGET_SESSION)
    if not isinstance(target, dict):
        raise SystemExit("TARGET_SESSION_MISSING")
    all_sources = list(target.get("full_sources", []))
    binary = [path for path in all_sources if path.endswith(".pdf")]
    text_sources = [path for path in all_sources if not path.endswith(".pdf")]
    if len(binary) != 3:
        raise SystemExit(f"EXPECTED_THREE_BINARY_SOURCES:{len(binary)}")
    target["full_sources"] = text_sources
    target["binary_source_hashes"] = {path: sha((root / path).read_bytes()) for path in binary}
    target["source_hashes"] = {path: sha((root / path).read_bytes()) for path in text_sources}
    target["revalidation"] = (
        "Cognition hydration repair: the original C0R8 full_sources list contained three PDF binaries, "
        "so plan --task stopped with NOT_UTF8. PDFs remain hash-pinned in binary_source_hashes and source snapshot README/cards; "
        "full_sources now contains only text-readable routing/evidence entries. Mathematical claims C-375–C-378, source assessments, "
        "C0R9 and C6 scope are unchanged."
    )
    state["revision"] = revision
    state["latest_session"] = SESSION_ID
    repair_sources = [
        ".codex/research/hott/STATE.json",
        f".codex/research/hott/sessions/{TARGET_SESSION}/CORE_COGNITION_AUDIT.md",
        "sources/external/zfc-meta-subtheory-c0r8-santanna-bueno-2014-20261005/README.md",
        "sources/external/zfc-meta-subtheory-c0r8-dacosta-santanna-2001-20261005/README.md",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-DOMAIN-ELIMINATION-SOURCE-TO-SPEC-CONTROL.md",
        "audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-MSS-PHASE-ORDER-SOURCE-TO-SPEC-CONTROL.md",
    ]
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "COGNITION_ROUTE_REPAIRED_FOR_C0R8_TEXT_HYDRATION / NO_MATHEMATICAL_STATUS_CHANGE",
        "full_sources": repair_sources,
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": f".codex/research/hott/sessions/{SESSION_ID}/SESSION.md",
        "path_mode": "document",
        "related_records": [TARGET_SESSION],
        "scope": "Repairs C0R8 state hydration so binary source PDFs are retained as hash-pinned evidence but not read as UTF-8 full_sources. It changes no source conclusion, Lean theorem, proof receipt, C0 successor, or bare-ZFC verdict.",
        "source_hashes": {path: sha((root / path).read_bytes()) for path in repair_sources},
        "status": "complete",
    }
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    for index_rel, old, new in (
        ("方向追踪.md", "source_state_revision: 309", f"source_state_revision: {revision}"),
        ("全景视野.md", "source_state_revision: 309", f"source_state_revision: {revision}"),
        ("方向追踪.md", "projection_generation: 20261005-zfc-mss-controls-309", f"projection_generation: 20261005-zfc-mss-route-repair-{revision}"),
        ("全景视野.md", "projection_generation: 20261005-zfc-mss-controls-309", f"projection_generation: 20261005-zfc-mss-route-repair-{revision}"),
    ):
        doc = projection_edit.load(root, index_rel)
        projection_edit.replace_in_index(doc, old, new)
        texts[index_rel] = doc["index_text"]
        texts.update(doc["shards"])

    marker = "### `C0R8` binary source hydration repair（2026-10-05）"
    note = """
### `C0R8` binary source hydration repair（2026-10-05）

`full_sources` 是 runtime 的 UTF-8 hydration 列表，不是所有证据文件的目录。C0R8 曾把三份PDF
直接列入该字段，导致按 session task plan 时得到 `NOT_UTF8`。修复后，PDF仍由 source snapshot
README、source cards与`STATE.records[…].binary_source_hashes`固定；`full_sources`只保留可读的
README/card/proof/run入口。C-375–C-378、C0R9和core status均未改变。

"""
    if marker not in texts["MEMORY/001 - 当前执行队列.md"]:
        needle = "## 想法 T：理论精度、观察边界与哥德尔式自反（2026-10-04）"
        texts["MEMORY/001 - 当前执行队列.md"] = texts["MEMORY/001 - 当前执行队列.md"].replace(needle, note + needle, 1)
    texts[R.PREFIX + "FRONTIER.md"] = prepend_once(texts[R.PREFIX + "FRONTIER.md"], marker, note)
    texts[R.PREFIX + "RESUME.md"] = prepend_once(
        texts[R.PREFIX + "RESUME.md"],
        "## C0R8 text hydration repair（2026-10-05）",
        """## C0R8 text hydration repair（2026-10-05）

When loading C0R8 through STATE, use its text `full_sources` (source README/cards and proof/run
receipts). Original PDFs are intentionally reached through those text entries and hash-pinned as
binary evidence; do not put a binary PDF into a runtime text hydration list.

""",
    )
    log_path = "MEMORY/003 - 当前验证状态与顺序日志.md"
    if SESSION_ID not in texts[log_path]:
        texts[log_path] += f"\n\n{SESSION_ID}：修复C0R8 state hydration。PDF原件从`full_sources`移到`binary_source_hashes`，以source README/card作为文本入口；plan `NOT_UTF8` route error不影响C-375–C-378、C0R9或C6状态。\n"

    base = f".codex/research/hott/sessions/{SESSION_ID}/"
    texts[base + "SESSION.md"] = f"""# {SESSION_ID}

> **Role:** `GOVERNANCE_ALIGNMENT`.
> **Tier:** `T3` — C0R8 evidence-route repair; no mathematical result changed.

## Problem

The C0R8 STATE record listed three PDFs in `full_sources`. `cognition_runtime` legitimately treats
that field as UTF-8 text hydration and stopped at `NOT_UTF8`.

## Repair

- retained each PDF SHA-256 in `binary_source_hashes` and the source snapshot README;
- retained text README/cards/proof/run assets in `full_sources`;
- revalidated the C0R8 state record with an explicit explanation;
- preserved C-375–C-378, C0R9 and all source-to-spec boundaries unchanged.
"""
    texts[base + "RUNS.json"] = json.dumps({
        "next": "Re-run text-only hydration for the C0R8 session, then continue C0-SUCCESSOR-RESELECTION-009.",
        "role": "GOVERNANCE_ALIGNMENT",
        "schema_version": "hott-research-runs/v1",
        "session_id": SESSION_ID,
        "status": "C0R8_BINARY_SOURCE_ROUTE_REPAIRED_NO_MATH_STATUS_CHANGE",
        "tier": "T3",
        "verification": [
            {"command": "cognition_runtime.py plan --profile research --task S-RES-20261005-ZFC-META-SUBTHEORY-C0R8-MSS-CONTROLS-001", "scope": "text-only record hydration", "status": "PENDING_AFTER_CHECKPOINT"},
        ],
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    texts[base + "CORE_COGNITION_AUDIT.md"] = audit_text(root)

    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User authorized continued ZFC research, durable cognitive writeback, formal proof evidence, exact-path commit, and remote push. This repair restores text hydration without changing mathematical claims.",
        "load_profile": "research",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": sha((root / rel).read_bytes()) if (root / rel).is_file() else None,
                "text": texts[rel],
            }
            for rel in sorted(texts)
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": revision, "session_id": SESSION_ID, "files": len(payload["files"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
