#!/usr/bin/env python3
"""Exercise layered loading (four-piece full set) in a fresh Python process and preserve a receipt.

This validates byte/EOF/order/profile/task behavior only.  No model is invoked,
so model ingestion, understanding and mathematical correctness remain NOT_RUN.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FULL_SET = ("核心认知.md", "方向追踪.md", "全景视野.md", "从抽象到悖论——HoTT研究的核心问题意识与思想展开.md")


def load_runtime(root: Path):
    path = root / ".codex/tools/cognition_runtime.py"
    spec = importlib.util.spec_from_file_location("cognition_runtime", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("RUNTIME_IMPORT_FAILED")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_plan(runtime, root: Path, plan: dict, profile: str, task_ids=()) -> tuple[list[dict], dict]:
    chunks: list[dict] = []
    for entry in plan["documents"]:
        cursor = 1
        while True:
            chunk = runtime.read_chunk(
                root, plan["snapshot"], entry["path"], cursor, 200000,
                profile=profile, task_ids=task_ids
            )
            chunks.append(chunk)
            if chunk["next_start_line"] is None:
                break
            cursor = int(chunk["next_start_line"])
    return chunks, runtime.check_coverage(plan, chunks)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=Path("audit/fresh-three-way-verification-20260912.json"))
    args = parser.parse_args()
    root = args.project_root.resolve()
    runtime = load_runtime(root)

    governance = runtime.plan(root, profile="governance")
    research = runtime.plan(root, profile="research")
    if tuple(governance["full_set_documents"]) != FULL_SET:
        raise SystemExit("FAIL governance full-set identity")
    # A trio member may itself be a v2 logical document: its index stays at the
    # canonical path and its shards are expanded right after it.  The invariant is
    # "the three indexes appear in fixed order and each expands to every shard",
    # not "the literal first three document rows are the trio paths".
    for label, plan in (("governance", governance), ("research", research)):
        positions = []
        for rel in FULL_SET:
            matches = [i for i, row in enumerate(plan["documents"]) if row["path"] == rel]
            if len(matches) != 1:
                raise SystemExit(f"FAIL {label} full-set row count: {rel}")
            entry = plan["documents"][matches[0]]
            positions.append(matches[0])
            if entry["logical_role"] == "index":
                expanded = [row["path"] for row in plan["documents"]
                            if row["logical_id"] == entry["logical_id"] and row["logical_role"] == "shard"]
                declared = next((doc for doc in plan["logical_documents"]
                                 if doc["logical_id"] == entry["logical_id"]), None)
                if declared is None or sorted(expanded) != sorted(declared["shards"]):
                    raise SystemExit(f"FAIL {label} full-set shards incomplete: {rel}")
        if positions != sorted(positions):
            raise SystemExit(f"FAIL {label} full-set order")
    governance_paths = {row["path"] for row in governance["documents"]}
    cold = set(governance["query_first_documents"] + governance["archive_verify_only_documents"])
    leaked_cold = sorted(governance_paths & cold)
    if leaked_cold:
        raise SystemExit(f"FAIL cold assets in boot plan: {leaked_cold}")
    if governance.get("automatically_included_historical_sessions") != []:
        raise SystemExit("FAIL historical sessions automatically included")

    governance_chunks, governance_coverage = read_plan(runtime, root, governance, "governance")
    research_chunks, research_coverage = read_plan(runtime, root, research, "research")
    full_set_receipt: list[dict[str, object]] = []
    for path in FULL_SET:
        pieces = [chunk for chunk in governance_chunks if chunk["path"] == path]
        assembled = "".join(chunk["text"] for chunk in pieces)
        expected = next(row for row in governance["documents"] if row["path"] == path)
        if sha(assembled) != expected["sha256"]:
            raise SystemExit(f"FAIL full-set hash: {path}")
        full_set_receipt.append({
            "path": path,
            "sha256": expected["sha256"],
            "bytes": expected["bytes"],
            "lines": expected["lines"],
            "ranges": [[chunk["start_line"], chunk["end_line"]] for chunk in pieces],
            "status": "FULL_EMITTED_BYTES_MATCH"
        })

    query = runtime.query_record(root, "A-AISTUDIO-COVERAGE-001")
    hydrated = runtime.plan(root, profile="research", task_ids=("A-AISTUDIO-COVERAGE-001",))
    if "A-AISTUDIO-COVERAGE-001" not in hydrated["hydrated_records"]:
        raise SystemExit("FAIL explicit task hydration")
    if hydrated["snapshot"] in {governance["snapshot"], research["snapshot"]}:
        raise SystemExit("FAIL task hydration snapshot identity")

    negatives: dict[str, str] = {}
    try:
        runtime.read_chunk(root, "STALE-SNAPSHOT", FULL_SET[0], 1, 1000)
    except Exception as exc:
        negatives["wrong_snapshot"] = str(exc)
    else:
        raise SystemExit("FAIL wrong snapshot accepted")
    try:
        runtime.check_coverage(governance, governance_chunks[:-1])
    except Exception as exc:
        negatives["incomplete_coverage"] = str(exc)
    else:
        raise SystemExit("FAIL incomplete coverage accepted")
    tampered = list(governance_chunks)
    tampered[0] = dict(tampered[0]); tampered[0]["chunk_sha256"] = "0" * 64
    try:
        runtime.check_coverage(governance, tampered)
    except Exception as exc:
        negatives["tampered_chunk"] = str(exc)
    else:
        raise SystemExit("FAIL tampered chunk accepted")
    try:
        runtime.read_chunk(root, research["snapshot"], FULL_SET[0], 1, 1000, profile="governance")
    except Exception as exc:
        negatives["profile_snapshot_mismatch"] = str(exc)
    else:
        raise SystemExit("FAIL profile snapshot mismatch accepted")

    child_code = f"""
import importlib.util, json, pathlib
p = pathlib.Path({str(root / '.codex/tools/cognition_runtime.py')!r})
s = importlib.util.spec_from_file_location('r', p)
m = importlib.util.module_from_spec(s)
s.loader.exec_module(m)
root = pathlib.Path({str(root)!r})
g = m.plan(root, profile='governance')
r = m.plan(root, profile='research')
trio = []
for rel in {list(FULL_SET)!r}:
    i = next(idx for idx, x in enumerate(g['documents']) if x['path'] == rel)
    entry = g['documents'][i]
    shards = 0
    if entry.get('logical_id'):
        shards = sum(1 for x in g['documents']
                     if x.get('logical_id') == entry['logical_id'] and x.get('logical_role') == 'shard')
    trio.append([rel, i, shards, entry.get('logical_role')])
print(json.dumps({{
    'g': {{'snapshot': g['snapshot'], 'documents': len(g['documents']), 'bytes': g['total_bytes']}},
    'r': {{'snapshot': r['snapshot'], 'documents': len(r['documents']), 'bytes': r['total_bytes']}},
    'trio': trio,
    'historical': g['automatically_included_historical_sessions'],
    'model_context': g['model_context'],
}}))
"""
    child = subprocess.run([sys.executable, "-B", "-c", child_code], cwd=root, text=True,
                           capture_output=True, check=False, env={"PYTHONDONTWRITEBYTECODE": "1"})
    if child.returncode != 0:
        raise SystemExit(f"FAIL fresh child: {child.stderr.strip()}")
    fresh_child = json.loads(child.stdout)
    positions = [row[1] for row in fresh_child["trio"]]
    if positions != sorted(positions) or fresh_child["historical"] != []:
        raise SystemExit("FAIL fresh child layered policy")

    receipt = {
        "schema_version": "fresh-three-way-verification/v2",
        "status": "PASS_WITH_SCOPE",
        "revision": governance["revision"],
        "full_set_order": list(FULL_SET),
        "full_set_input_fidelity": full_set_receipt,
        "profiles": {
            "governance": {"snapshot": governance["snapshot"], "documents": len(governance["documents"]),
                           "bytes": governance["total_bytes"], "lines": governance["total_lines"],
                           "coverage": governance_coverage},
            "research": {"snapshot": research["snapshot"], "documents": len(research["documents"]),
                         "bytes": research["total_bytes"], "lines": research["total_lines"],
                         "coverage": research_coverage}
        },
        "explicit_task_hydration": {
            "record": query["record_id"], "snapshot": hydrated["snapshot"],
            "documents": len(hydrated["documents"]), "hydrated_records": hydrated["hydrated_records"]
        },
        "cold_assets_absent_from_default": sorted(cold),
        "historical_sessions_auto_loaded": [],
        "negative_cases": negatives,
        "fresh_process_child": fresh_child,
        "model_context": "NOT_CERTIFIED_BY_TOOL",
        "model_behavior": "NOT_RUN_NO_FRESH_MODEL_INVOCATION_AUTHORIZED",
        "mathematics": "NOT_CERTIFIED",
        "interpretation": "Fresh Python processes verified exact trio bytes, layered plans, explicit hydration and fail-closed negatives. No model ingestion/comprehension claim is made."
    }
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": receipt["status"], "revision": receipt["revision"],
        "governance_documents": receipt["profiles"]["governance"]["documents"],
        "research_documents": receipt["profiles"]["research"]["documents"],
        "negative_cases": list(negatives), "model_behavior": receipt["model_behavior"]
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
