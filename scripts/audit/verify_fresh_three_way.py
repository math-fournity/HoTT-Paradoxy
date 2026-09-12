#!/usr/bin/env python3
"""Run a fresh-process full-read and fail-closed three-way rehearsal.

This validator exercises the local runtime, not the model's hidden context.
It emits a durable receipt for exact EOF/hash coverage and negative cases.
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
THREE_WAY = ("核心认知.md", "方向追踪.md", "全景视野.md")


def load_runtime(root: Path):
    spec = importlib.util.spec_from_file_location("cognition_runtime", root / ".codex/tools/cognition_runtime.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=Path("audit/fresh-three-way-verification-20260912.json"))
    args = parser.parse_args()
    root = args.project_root.resolve()
    runtime = load_runtime(root)
    plan = runtime.plan(root)
    assert tuple(plan["three_way_documents"]) == THREE_WAY
    full_read: list[dict[str, object]] = []
    all_chunks: list[dict[str, object]] = []
    for path in THREE_WAY:
        cursor = 1
        pieces: list[str] = []
        ranges: list[list[int]] = []
        while True:
            chunk = runtime.read_chunk(root, plan["snapshot"], path, cursor, 200000)
            body = chunk["text"]
            pieces.append(body)
            ranges.append([chunk["start_line"], chunk["end_line"]])
            all_chunks.append(chunk)
            if chunk["next_start_line"] is None:
                break
            cursor = int(chunk["next_start_line"])
        assembled = "".join(pieces)
        expected = next(row for row in plan["documents"] if row["path"] == path)
        if sha(assembled) != expected["sha256"]:
            raise SystemExit(f"FAIL full read hash: {path}")
        if len(assembled.splitlines(keepends=True)) != expected["lines"]:
            raise SystemExit(f"FAIL full read line count: {path}")
        full_read.append({
            "path": path,
            "sha256": sha(assembled),
            "bytes": len(assembled.encode("utf-8")),
            "lines": len(assembled.splitlines(keepends=True)),
            "ranges": ranges,
            "status": "FULL_EMITTED_BYTES_MATCH",
        })

    # check_coverage is intentionally defined for the complete current load
    # graph, not only the three-way prefix.  Read the remaining fixed and
    # dynamically expanded documents in this same fresh process so the
    # positive receipt covers the actual closure selected by STATE.
    already_read = set(THREE_WAY)
    for entry in plan["documents"]:
        path = str(entry["path"])
        if path in already_read:
            continue
        cursor = 1
        while True:
            chunk = runtime.read_chunk(root, plan["snapshot"], path, cursor, 200000)
            all_chunks.append(chunk)
            if chunk["next_start_line"] is None:
                break
            cursor = int(chunk["next_start_line"])
        already_read.add(path)
    positive = runtime.check_coverage(plan, all_chunks)
    negatives: dict[str, str] = {}
    try:
        runtime.read_chunk(root, "STALE-SNAPSHOT", THREE_WAY[0], 1, 1000)
    except Exception as exc:  # runtime has a stable typed error, but keep validator host-agnostic
        negatives["wrong_snapshot"] = str(exc)
    else:
        raise SystemExit("FAIL negative wrong snapshot accepted")
    try:
        runtime.check_coverage(plan, all_chunks[:-1])
    except Exception as exc:
        negatives["incomplete_coverage"] = str(exc)
    else:
        raise SystemExit("FAIL negative incomplete coverage accepted")
    bad = list(all_chunks)
    bad[0] = dict(bad[0])
    bad[0]["chunk_sha256"] = "0" * 64
    try:
        runtime.check_coverage(plan, bad)
    except Exception as exc:
        negatives["tampered_chunk"] = str(exc)
    else:
        raise SystemExit("FAIL negative tampered chunk accepted")
    fresh_code = (
        "import importlib.util, json; "
        "p='" + str(root / ".codex/tools/cognition_runtime.py").replace("'", "\\'") + "'; "
        "s=importlib.util.spec_from_file_location('rt',p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); "
        "x=m.plan('" + str(root).replace("'", "\\'") + "'); "
        "print(json.dumps({'revision':x['revision'],'first_three':x['three_way_documents'],'model_context':x['model_context']}))"
    )
    child = subprocess.run([sys.executable, "-c", fresh_code], cwd=root, text=True, capture_output=True, check=False)
    if child.returncode != 0:
        raise SystemExit(f"FAIL fresh subprocess: {child.stderr.strip()}")
    fresh_child = json.loads(child.stdout.strip())
    if fresh_child.get("first_three") != list(THREE_WAY):
        raise SystemExit("FAIL fresh subprocess order")
    if fresh_child.get("model_context") != "NOT_CERTIFIED_BY_TOOL":
        raise SystemExit("FAIL model context boundary")
    receipt = {
        "schema_version": "fresh-three-way-verification/v1",
        "status": "PASS_WITH_SCOPE",
        "runtime_plan_snapshot": plan["snapshot"],
        "revision": plan["revision"],
        "fresh_process_child": fresh_child,
        "three_way_order": list(THREE_WAY),
        "full_read": full_read,
        "coverage_check": positive,
        "negative_cases": negatives,
        "model_context": "NOT_CERTIFIED_BY_TOOL",
        "mathematics": "NOT_CERTIFIED",
        "interpretation": "Fresh runtime/EOF/hash and fail-closed negative behavior were exercised; no claim about hidden model retention or understanding is made.",
    }
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": receipt["status"], "revision": plan["revision"], "documents": len(full_read), "negative_cases": list(negatives)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
