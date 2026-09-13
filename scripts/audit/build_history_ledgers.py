#!/usr/bin/env python3
"""Build the four historical audit ledgers for the integrated handoff repo.

This is a provenance builder, not a semantic judge.  It uses the canonical
shared Codex trajectory reader for LocalGPT (catalog/tree/scan/inspect), parses
the user-supplied WebGPT export by its section headers, and parses the
user-supplied Gemini JSON structure without modifying any source.  Full visible
assistant answers are retained where the canonical reader can return them;
tool arguments/results are bounded in the public ledger and remain directly
inspectable through their raw locator in private-audit/.
"""
from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from logical_document import logical_text  # noqa: E402  (shared reader for v2 shard indexes)
CANONICAL_TRAJECTORY = Path("/Users/aurolafly/codex/tools/session_trajectory.py")
CORE_MANIFEST = Path("核心认知.manifest.json")
SOURCE_MANIFEST = Path("sources/SOURCE_MANIFEST.json")
WEB_EXPORT = Path("sources/webgpt/ChatGPT-HoTT - Main-20260911-1222.md")
GEMINI_EXPORT = Path("sources/gemini/Gemini - AI 对话录.json")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_text(value: str) -> str:
    return sha(value.encode("utf-8"))


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def dump_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def bound(value: Any, limit: int = 1800) -> tuple[str, bool, str]:
    text = value if isinstance(value, str) else dump_json(value)
    digest = sha_text(text)
    if len(text) <= limit:
        return text, False, digest
    return text[:limit], True, digest


def source_label(path: Path) -> str:
    name = path.name
    if "01a059c1" in name:
        return "codex-parent"
    if "_01a0869f" in name:
        return "codex-hott2-main"
    if "01a08699" in name:
        return "codex-hott2-root"
    if "01a05a10" in name:
        return "codex-prime-worktree"
    if "01a059dd" in name:
        return "codex-prime-line"
    return re.sub(r"[^A-Za-z0-9_-]+", "-", path.stem).strip("-")


def run_json_command(args: list[str]) -> tuple[list[dict[str, Any]], str, int]:
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=False)
    rows: list[dict[str, Any]] = []
    for line in result.stdout.splitlines():
        try:
            value = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            rows.append(value)
    return rows, result.stderr, result.returncode


def run_json_object(args: list[str]) -> tuple[dict[str, Any] | None, str, int]:
    result = subprocess.run(args, cwd=ROOT, capture_output=True, text=True, check=False)
    try:
        value = json.loads(result.stdout)
    except json.JSONDecodeError:
        value = None
    return value if isinstance(value, dict) else None, result.stderr, result.returncode


def build_local_gpt() -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    response_rows: list[dict[str, Any]] = []
    tool_rows: list[dict[str, Any]] = []
    trajectory_summaries: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    raw_paths = sorted((ROOT / "private-audit/local-gpt").glob("*.jsonl"))
    kinds = ["assistant_message", "tool_call", "tool_result", "user_message"]
    for raw_path in raw_paths:
        label = source_label(raw_path)
        relative = raw_path.relative_to(ROOT).as_posix()
        raw_hash = sha(raw_path.read_bytes())
        tree_args = [
            sys.executable,
            str(CANONICAL_TRAJECTORY),
            "tree",
            "--host",
            "codex",
            "--source",
            str(raw_path),
            "--recursive",
            "--json",
        ]
        tree, tree_stderr, tree_code = run_json_object(tree_args)
        if tree is None or tree_code != 0:
            errors.append({"source": relative, "stage": "tree", "returncode": tree_code, "stderr": tree_stderr[-2000:]})
            tree = {"status": "CANONICAL_TREE_FAILED"}
        trajectory_summaries.append(
            {
                "source_id": label,
                "source_path": relative,
                "source_sha256": raw_hash,
                "reader": "CAP-TRAJ-MULTIHOST:/Users/aurolafly/codex/tools/session_trajectory.py",
                "tree": tree,
                "tree_status": "PASS" if tree_code == 0 else "FAIL",
            }
        )
        scan_args = [
            sys.executable,
            str(CANONICAL_TRAJECTORY),
            "scan",
            "--host",
            "codex",
            "--source",
            str(raw_path),
            "--recursive",
        ]
        for kind in kinds:
            scan_args.extend(["--kind", kind])
        scan_args.extend(["--limit", "100000", "--text-chars", "1800", "--json"])
        scanned, scan_stderr, scan_code = run_json_command(scan_args)
        if scan_code != 0:
            errors.append({"source": relative, "stage": "scan", "returncode": scan_code, "stderr": scan_stderr[-2000:]})
        event_ids: dict[tuple[str, str], str] = {}
        pending_tool_rows: list[dict[str, Any]] = []
        assistant_events: list[dict[str, Any]] = []
        for event in scanned:
            kind = event.get("kind")
            sequence = event.get("sequence")
            if kind not in kinds or not isinstance(sequence, int):
                continue
            event_id = f"TE-{label}-{sequence:06d}-{kind}"
            event_ids[(kind, str(sequence))] = event_id
            if kind == "assistant_message":
                assistant_events.append((event, event_id))
            elif kind in ("tool_call", "tool_result"):
                data = event.get("data") if isinstance(event.get("data"), dict) else {}
                call_id = data.get("call_id") or event.get("name") or ""
                if kind == "tool_call":
                    visible, truncated, full_hash = bound(data.get("arguments", ""))
                    row = {
                        "tool_event_id": event_id,
                        "event_kind": kind,
                        "session_id": event.get("session_id"),
                        "turn_id": event.get("turn_id"),
                        "sequence": sequence,
                        "raw_locator": event.get("locator"),
                        "source_path": relative,
                        "source_id": label,
                        "tool_name": event.get("name"),
                        "call_id": call_id,
                        "visible_arguments": visible,
                        "visible_arguments_truncated": truncated,
                        "visible_arguments_sha256": full_hash,
                        "matching_result_id": None,
                        "path_mentions": sorted(set(re.findall(r"(?:/Volumes|/Users|/tmp|/mnt|[A-Za-z0-9_.-]+/)(?:[^\s'\"`]+)", visible)))[:80],
                        "side_effect_class": "CAPABILITY_PRESENT; inspect raw command for exact effect",
                        "completeness": event.get("completeness"),
                        "timestamp": event.get("timestamp"),
                    }
                else:
                    result_head = data.get("text_head", "")
                    visible, truncated, visible_hash = bound(result_head)
                    row = {
                        "tool_event_id": event_id,
                        "event_kind": kind,
                        "session_id": event.get("session_id"),
                        "turn_id": event.get("turn_id"),
                        "sequence": sequence,
                        "raw_locator": event.get("locator"),
                        "source_path": relative,
                        "source_id": label,
                        "tool_name": event.get("name"),
                        "call_id": call_id,
                        "visible_result_head": visible,
                        "visible_result_truncated": truncated or (data.get("text_chars", 0) > len(visible)),
                        "visible_result_head_sha256": visible_hash,
                        "full_result_chars": data.get("text_chars"),
                        "full_result_available_in_scan": False,
                        "matching_call_id": None,
                        "result_status": data.get("exit_code") or data.get("status") or "visible_result_recorded",
                        "path_mentions": sorted(set(re.findall(r"(?:/Volumes|/Users|/tmp|/mnt|[A-Za-z0-9_.-]+/)(?:[^\s'\"`]+)", visible)))[:80],
                        "side_effect_class": "RESULT_ONLY; effect determined by paired call and raw result",
                        "completeness": event.get("completeness"),
                        "timestamp": event.get("timestamp"),
                    }
                pending_tool_rows.append(row)
        calls_by_id = {str(row.get("call_id")): row for row in pending_tool_rows if row["event_kind"] == "tool_call" and row.get("call_id")}
        results_by_id = {str(row.get("call_id")): row for row in pending_tool_rows if row["event_kind"] == "tool_result" and row.get("call_id")}
        for call_id, call_row in calls_by_id.items():
            result_row = results_by_id.get(call_id)
            if result_row:
                call_row["matching_result_id"] = result_row["tool_event_id"]
                result_row["matching_call_id"] = call_row["tool_event_id"]
        tool_rows.extend(pending_tool_rows)
        for event, event_id in assistant_events:
            locator = event.get("locator")
            inspect_args = [
                sys.executable,
                str(CANONICAL_TRAJECTORY),
                "inspect",
                "--host",
                "codex",
                "--source",
                str(raw_path),
                "--recursive",
                "--no-truncate",
                str(locator),
            ]
            inspected, inspect_stderr, inspect_code = run_json_object(inspect_args)
            if inspected is None or inspect_code != 0:
                errors.append({"source": relative, "stage": "inspect", "locator": locator, "returncode": inspect_code, "stderr": inspect_stderr[-1000:]})
                content = str((event.get("data") or {}).get("text_head", ""))
                full_available = False
            else:
                content = inspected.get("text") if isinstance(inspected.get("text"), str) else ""
                full_available = bool(isinstance(inspected.get("text"), str))
            response_id = f"LOCALGPT-{label}-{event.get('name') or event_id}"
            response_rows.append(
                {
                    "ai_id": "LocalGPT",
                    "response_id": response_id,
                    "platform": "LocalGPT",
                    "source_id": label,
                    "source_path": relative,
                    "raw_locator": locator,
                    "sequence": event.get("sequence"),
                    "session_id": event.get("session_id"),
                    "turn_id": event.get("turn_id"),
                    "phase": (event.get("data") or {}).get("phase"),
                    "timestamp": event.get("timestamp"),
                    "content": content,
                    "content_sha256": sha_text(content),
                    "content_chars": len(content),
                    "visibility": "assistant_visible",
                    "full_text_available": full_available,
                    "material_claim_ids": sorted(set(re.findall(r"\b(?:KC|R|C|P)-[A-Za-z0-9_-]+", content))),
                    "artifact_ids": sorted(set(re.findall(r"(?:artifacts?|sessions?)/[A-Za-z0-9_.，。/@一-龥-]+", content)))[:80],
                    "git_ids": sorted(set(re.findall(r"\b[0-9a-f]{7,40}\b", content)))[:80],
                    "error": None if inspect_code == 0 else "CANONICAL_INSPECT_FAILED",
                    "truncation": "NONE" if full_available else "BOUNDED_SCAN_OR_INSPECT_FAILURE",
                    "disposition": "VISIBLE_ANSWER_AUDIT_RECORD; mathematical claims require independent evidence",
                }
            )
    return response_rows, tool_rows, trajectory_summaries, errors


SECTION_HEADER = re.compile(r"(?m)^## (Prompt|Response):\s*$")


def parse_web_sections() -> list[dict[str, Any]]:
    path = ROOT / WEB_EXPORT
    text = path.read_text(encoding="utf-8")
    matches = list(SECTION_HEADER.finditer(text))
    prompt_number = 0
    response_number = 0
    previous_prompt: str | None = None
    sections: list[dict[str, Any]] = []
    for index, match in enumerate(matches, start=1):
        end = matches[index].start() if index < len(matches) else len(text)
        body = text[match.end() : end].strip("\r\n")
        body_lines = body.splitlines()
        timestamp = body_lines[0].strip() if body_lines else ""
        content = "\n".join(body_lines[1:]).strip("\r\n") if body_lines else ""
        kind = match.group(1).lower()
        if kind == "prompt":
            prompt_number += 1
            section_id = f"WEBGPT-P-{prompt_number:03d}"
            previous_prompt = section_id
        else:
            response_number += 1
            section_id = f"WEBGPT-R-{response_number:03d}"
        line = text.count("\n", 0, match.start()) + 1
        sections.append(
            {
                "section_id": section_id,
                "section_index": index,
                "section_type": kind,
                "section_ordinal": prompt_number if kind == "prompt" else response_number,
                "timestamp_original": timestamp,
                "source_file": WEB_EXPORT.as_posix(),
                "raw_locator": f"{WEB_EXPORT.as_posix()}:section-{index}:line-{line}",
                "content": content,
                "content_sha256": sha_text(content),
                "content_chars": len(content),
                "full_text_available": True,
                "paired_prompt_id": previous_prompt if kind == "response" else None,
            }
        )
    return sections


def build_webgpt(response_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    sections = parse_web_sections()
    for section in sections:
        if section["section_type"] != "response":
            continue
        response_rows.append(
            {
                "ai_id": "WebGPT",
                "response_id": section["section_id"],
                "platform": "WebGPT",
                "source_id": "webgpt-main-export",
                "source_path": WEB_EXPORT.as_posix(),
                "raw_locator": section["raw_locator"],
                "sequence": section["section_index"],
                "session_id": "ChatGPT-HoTT-Main",
                "turn_id": section.get("paired_prompt_id"),
                "phase": "visible_response",
                "timestamp": section["timestamp_original"],
                "content": section["content"],
                "content_sha256": section["content_sha256"],
                "content_chars": section["content_chars"],
                "visibility": "assistant_visible",
                "full_text_available": True,
                "material_claim_ids": sorted(set(re.findall(r"\b(?:KC|R|C|P)-[A-Za-z0-9_-]+", section["content"]))),
                "artifact_ids": sorted(set(re.findall(r"(?:artifacts?|sessions?)/[A-Za-z0-9_.，。/@一-龥-]+", section["content"])))[:80],
                "git_ids": sorted(set(re.findall(r"\b[0-9a-f]{7,40}\b", section["content"])))[:80],
                "error": None,
                "truncation": "NONE",
                "disposition": "VISIBLE_EXPORT_ANSWER; workspace/Git verification required",
            }
        )
    return sections


def text_parts(chunk: dict[str, Any]) -> str:
    if isinstance(chunk.get("text"), str):
        return chunk["text"]
    parts = chunk.get("parts") if isinstance(chunk.get("parts"), list) else []
    return "".join(part.get("text", "") for part in parts if isinstance(part, dict) and isinstance(part.get("text"), str))


def inline_file(chunk: dict[str, Any]) -> dict[str, Any] | None:
    if isinstance(chunk.get("inlineFile"), dict):
        return chunk["inlineFile"]
    parts = chunk.get("parts") if isinstance(chunk.get("parts"), list) else []
    for part in parts:
        if isinstance(part, dict) and isinstance(part.get("inlineFile"), dict):
            return part["inlineFile"]
    return None


def build_gemini(response_rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    source_path = ROOT / GEMINI_EXPORT
    payload = json.loads(source_path.read_text(encoding="utf-8"))
    chunks = payload.get("chunkedPrompt", {}).get("chunks", [])
    thoughts: list[dict[str, Any]] = []
    execution: list[dict[str, Any]] = []
    user_ordinal = 0
    ordinary_ordinal = 0
    thought_ordinal = 0
    execution_ordinal = 0
    for index, chunk in enumerate(chunks):
        if not isinstance(chunk, dict):
            continue
        role = chunk.get("role")
        if role == "user":
            user_ordinal += 1
            continue
        if role != "model":
            continue
        locator = f"{GEMINI_EXPORT.as_posix()}#chunk-{index}"
        timestamp = chunk.get("createTime")
        common = {
            "platform": "Gemini",
            "source_file": GEMINI_EXPORT.as_posix(),
            "raw_locator": locator,
            "chunk_index": index,
            "timestamp": timestamp,
            "nearest_user_ordinal": user_ordinal,
            "token_count": chunk.get("tokenCount"),
        }
        file_payload = inline_file(chunk)
        if file_payload is not None:
            execution_ordinal += 1
            encoded = file_payload.get("data", "")
            try:
                decoded = base64.b64decode(encoded, validate=True)
                content = decoded.decode("utf-8")
                decode_status = "DECODED_UTF8"
            except Exception as exc:  # malformed source is recorded, not hidden
                content = ""
                decode_status = f"DECODE_FAILED:{type(exc).__name__}"
            execution.append(
                {
                    **common,
                    "execution_id": f"GEMINI-INLINE-{execution_ordinal:03d}",
                    "record_type": "inlineFile",
                    "mime_type": file_payload.get("mimeType"),
                    "content": content,
                    "content_sha256": sha_text(content),
                    "content_chars": len(content),
                    "decode_status": decode_status,
                    "disposition": "INLINE_FILE_CODE_PAYLOAD; not empty; source-backed",
                }
            )
            continue
        if isinstance(chunk.get("executableCode"), dict):
            execution_ordinal += 1
            value = chunk["executableCode"]
            content = value.get("code", "") if isinstance(value.get("code"), str) else dump_json(value)
            execution.append(
                {
                    **common,
                    "execution_id": f"GEMINI-EXEC-{execution_ordinal:03d}",
                    "record_type": "executableCode",
                    "language": value.get("language"),
                    "content": content,
                    "content_sha256": sha_text(content),
                    "content_chars": len(content),
                    "outcome": None,
                    "disposition": "CODE_PAYLOAD; execution result paired by adjacent chronology where available",
                }
            )
            continue
        if isinstance(chunk.get("codeExecutionResult"), dict):
            execution_ordinal += 1
            value = chunk["codeExecutionResult"]
            content = value.get("output", "") if isinstance(value.get("output"), str) else dump_json(value)
            execution.append(
                {
                    **common,
                    "execution_id": f"GEMINI-EXEC-{execution_ordinal:03d}",
                    "record_type": "codeExecutionResult",
                    "language": None,
                    "content": content,
                    "content_sha256": sha_text(content),
                    "content_chars": len(content),
                    "outcome": value.get("outcome"),
                    "disposition": "EXECUTION_RESULT; finite sandbox output only",
                }
            )
            continue
        content = text_parts(chunk)
        if chunk.get("isThought"):
            thought_ordinal += 1
            thoughts.append(
                {
                    **common,
                    "thought_id": f"GEMINI-THOUGHT-{thought_ordinal:03d}",
                    "visibility": "exported_model_thought_record",
                    "content": content,
                    "content_sha256": sha_text(content),
                    "content_chars": len(content),
                    "full_text_available": True,
                    "disposition": "SOURCE_EXPORTED_THOUGHT; not treated as public answer or proof",
                }
            )
        else:
            ordinary_ordinal += 1
            response_rows.append(
                {
                    **common,
                    "ai_id": "Gemini",
                    "response_id": f"GEMINI-R-{ordinary_ordinal:03d}",
                    "platform": "Gemini",
                    "source_id": "gemini-export",
                    "sequence": index,
                    "session_id": "Gemini-AI对话录",
                    "turn_id": f"user-{user_ordinal:03d}",
                    "phase": "ordinary_visible_text",
                    "content": content,
                    "content_sha256": sha_text(content),
                    "content_chars": len(content),
                    "visibility": "ordinary_model_text",
                    "full_text_available": True,
                    "material_claim_ids": sorted(set(re.findall(r"\b(?:KC|R|C|P)-[A-Za-z0-9_-]+", content))),
                    "artifact_ids": sorted(set(re.findall(r"(?:artifacts?|scripts?|sessions?)/[A-Za-z0-9_.，。/@一-龥-]+", content)))[:80],
                    "git_ids": sorted(set(re.findall(r"\b[0-9a-f]{7,40}\b", content)))[:80],
                    "error": None,
                    "truncation": "NONE",
                    "disposition": "VISIBLE_MODEL_TEXT; project/file/Git claims require direct evidence",
                }
            )
    return thoughts, execution


def build_user_disposition() -> list[dict[str, Any]]:
    manifest = json.loads((ROOT / CORE_MANIFEST).read_text(encoding="utf-8"))
    unit_ids = defaultdict(list)
    for unit in manifest.get("units", []):
        unit_ids[unit.get("source_message_id")].append(unit.get("id"))
    rows: list[dict[str, Any]] = []
    for message in manifest.get("message_disposition", []):
        row = dict(message)
        row["selected_core_unit_ids"] = unit_ids.get(message.get("source_message_id"), [])
        row["coverage_claim"] = "CORE_UNIT_INCLUDED" if row["selected_core_unit_ids"] else "DISPOSITION_ONLY"
        rows.append(row)
    return rows


def build_work_products(response_rows: list[dict[str, Any]], trajectory_summaries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    source_manifest = json.loads((ROOT / SOURCE_MANIFEST).read_text(encoding="utf-8"))
    rows: list[dict[str, Any]] = []
    top_head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=False).stdout.strip()
    for snapshot in source_manifest.get("snapshot_roots", []):
        root_rel = snapshot.get("root")
        rows.append(
            {
                "artifact_id": f"SNAPSHOT-ROOT-{re.sub(r'[^A-Za-z0-9]+', '-', str(root_rel)).strip('-').upper()}",
                "path": root_rel,
                "source_ai": "LocalGPT" if root_rel in ("HoTT", "sources/local-gpt/ALL-Markdown-root") else "WebGPT/handoff",
                "origin_response_ids": [],
                "origin_tool_event_ids": [],
                "repo": "top-level-integrated-repo",
                "head_or_snapshot": snapshot.get("tree_sha256"),
                "file_sha256": snapshot.get("tree_sha256"),
                "file_count": snapshot.get("file_count"),
                "status": "HISTORICAL_ONLY",
                "evidence": "sources/SOURCE_MANIFEST.json tree_manifest",
            }
        )
        for item in snapshot.get("files", []):
            rel = f"{root_rel}/{item.get('path')}"
            path = ROOT / rel
            rows.append(
                {
                    "artifact_id": "FILE-" + sha_text(rel)[:16],
                    "path": rel,
                    "source_ai": "LocalGPT" if root_rel == "HoTT" or root_rel == "sources/local-gpt/ALL-Markdown-root" else "WebGPT",
                    "origin_response_ids": [],
                    "origin_tool_event_ids": [],
                    "repo": "top-level-integrated-repo",
                    "head_or_snapshot": top_head,
                    "file_sha256": item.get("sha256"),
                    "bytes": item.get("bytes"),
                    "exists_in_snapshot": path.is_file(),
                    "status": "HISTORICAL_ONLY",
                    "evidence": "sources/SOURCE_MANIFEST.json explicit tree member",
                }
            )
    for explicit in source_manifest.get("explicit_files", []):
        rows.append(
            {
                "artifact_id": "EXPLICIT-" + sha_text(str(explicit.get("path")))[:16],
                "path": explicit.get("path"),
                "source_ai": explicit.get("source_role"),
                "origin_response_ids": [],
                "origin_tool_event_ids": [],
                "repo": "top-level-integrated-repo",
                "head_or_snapshot": top_head,
                "file_sha256": explicit.get("sha256"),
                "bytes": explicit.get("bytes"),
                "status": "DOCUMENTED" if explicit.get("exists") else "MISSING",
                "evidence": "sources/SOURCE_MANIFEST.json explicit file row",
            }
        )
    current_paths = [
        "核心认知.md",
        "核心认知.manifest.json",
        "实施方案-三AI历史整合与核心认知治理.md",
        "AGENTS.md",
        "MEMORY.md",
        "feature-list.md",
        "rulings.md",
        ".codex/cognition/PROTOCOL.md",
        ".codex/cognition/LOAD_SET.json",
        ".codex/cognition/CORE_COGNITION.schema.json",
        ".codex/skills/SKILL_ROLES.json",
        ".codex/skills/hott-local-session-governance/SKILL.md",
        ".codex/skills/hott-paradox-research/SKILL.md",
        ".codex/tools/cognition_runtime.py",
        "scripts/audit/build_core_cognition.py",
        "scripts/audit/verify_core_cognition.py",
        "scripts/audit/build_history_ledgers.py",
    ]
    for rel in current_paths:
        path = ROOT / rel
        rows.append(
            {
                "artifact_id": "CURRENT-" + sha_text(rel)[:16],
                "path": rel,
                "source_ai": "integration-session",
                "origin_response_ids": [],
                "origin_tool_event_ids": [],
                "repo": "top-level-integrated-repo",
                "head_or_snapshot": top_head,
                "file_sha256": sha(path.read_bytes()) if path.is_file() else None,
                "bytes": path.stat().st_size if path.is_file() else None,
                "status": "VERIFIED_WITH_SCOPE" if rel in ("核心认知.md", "核心认知.manifest.json") else "UNVERSIONED_BASELINE",
                "evidence": "current integration session; top-level Git commit pending for this wave",
            }
        )
    for rel_root, source_ai in (("理解章节", "historical-transform"), ("HoTT", "LocalGPT")):
        for path in sorted((ROOT / rel_root).rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT).as_posix()
            rows.append(
                {
                    "artifact_id": "RESEARCH-FILE-" + sha_text(rel)[:16],
                    "path": rel,
                    "source_ai": source_ai,
                    "origin_response_ids": [],
                    "origin_tool_event_ids": [],
                    "repo": "top-level-integrated-repo",
                    "head_or_snapshot": top_head,
                    "file_sha256": sha(path.read_bytes()),
                    "bytes": path.stat().st_size,
                    "status": "HISTORICAL_ONLY" if rel_root == "HoTT" else "DIRTY_NOT_VERSION_CLOSED",
                    "evidence": "top-level imported snapshot; detailed origin mapping remains in history ledger",
                }
            )
    # Session records and checkpoint receipts are durable work products in
    # their own right.  They must not disappear merely because they live
    # under .codex rather than under the research document tree.
    for rel_root, source_ai, status in (
        (".codex/research/hott/sessions", "integration-session", "DOCUMENTED"),
        (".codex/cognition/checkpoints", "cognition-runtime", "RUNTIME_OBSERVED"),
    ):
        base = ROOT / rel_root
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT).as_posix()
            rows.append(
                {
                    "artifact_id": "DURABLE-" + sha_text(rel)[:16],
                    "path": rel,
                    "source_ai": source_ai,
                    "origin_response_ids": [],
                    "origin_tool_event_ids": [],
                    "repo": "top-level-integrated-repo",
                    "head_or_snapshot": top_head,
                    "file_sha256": sha(path.read_bytes()),
                    "bytes": path.stat().st_size,
                    "status": status,
                    "evidence": "durable session/checkpoint tree",
                }
            )
    for path in sorted((ROOT / "audit").glob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        rows.append(
            {
                "artifact_id": "AUDIT-" + sha_text(rel)[:16],
                "path": rel,
                "source_ai": "integration-session",
                "origin_response_ids": [],
                "origin_tool_event_ids": [],
                "repo": "top-level-integrated-repo",
                "head_or_snapshot": top_head,
                "file_sha256": sha(path.read_bytes()),
                "bytes": path.stat().st_size,
                "status": "VERIFIED_WITH_SCOPE" if rel.endswith("verification-report.json") else "DOCUMENTED",
                "evidence": "audit ledger output",
            }
        )
    return rows


def split_claims(line: str) -> list[str]:
    pieces = re.split(r"(?<=[。！？!?；;])\s*", line)
    return [piece.strip() for piece in pieces if piece.strip()]


def build_claims() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    number = 1
    for path in sorted((ROOT / "理解章节").glob("*.md")):
        rel = path.relative_to(ROOT).as_posix()
        body_text = logical_text(ROOT, rel)
        if body_text is None:
            body_text = path.read_text(encoding="utf-8")
        in_fence = False
        for line_number, line in enumerate(body_text.splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_fence = not in_fence
                continue
            if in_fence or not stripped or stripped.startswith("<!--") or stripped in {"---", "***"}:
                continue
            if stripped.startswith("#") or re.fullmatch(r"\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?", stripped):
                continue
            for fragment in split_claims(line):
                if len(fragment.strip(" |-")) < 8:
                    continue
                claim_id = f"CL-{number:06d}"
                text = fragment.strip()
                kc_refs = sorted(set(re.findall(r"KC-[0-9]{6}", text)))
                commit_refs = sorted(set(re.findall(r"\b[0-9a-f]{7,40}\b", text)))
                conflict = "冲突" in text or "矛盾" in text or "不一致" in text
                rows.append(
                    {
                        "claim_id": claim_id,
                        "claim_text": text,
                        "claim_owner_document": path.relative_to(ROOT).as_posix(),
                        "claim_line": line_number,
                        "claim_type": "HISTORICAL_OR_CURRENT_TEXT_REQUIRES_SCOPE_REVIEW",
                        "source_locators": [f"核心认知.md#{ref}" for ref in kc_refs],
                        "artifact_locators": sorted(set(re.findall(r"(?:理解章节|HoTT|sources|\.codex|audit|artifacts?)/[^`，。；;\s]+", text)))[:40],
                        "git_locators": commit_refs,
                        "verification_run_ids": [],
                        "scope": "line/sentence extracted from understanding chapter; semantic mapping is pending",
                        "conflicts": ["CONFLICT_WORD_PRESENT; inspect surrounding source"] if conflict else [],
                        "unknowns": ["DIRECT_SOURCE_MAPPING_PENDING", "AI_CLAIM_STATUS_NOT_AUTOMATICALLY_CERTIFIED"],
                        "verdict": "AUDIT_PENDING",
                    }
                )
                number += 1
    return rows


def main() -> int:
    global ROOT
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.project_root.resolve()
    ROOT = root
    response_rows, tool_rows, trajectory_summaries, errors = build_local_gpt()
    web_sections = build_webgpt(response_rows)
    gemini_thoughts, gemini_execution = build_gemini(response_rows)
    user_disposition = build_user_disposition()
    work_products = build_work_products(response_rows, trajectory_summaries)
    claims = build_claims()
    generated_at = now()
    out = root / "audit"
    write_jsonl(out / "user-message-disposition.jsonl", user_disposition)
    write_jsonl(out / "ai-response-ledger.jsonl", response_rows)
    write_jsonl(out / "tool-event-ledger.jsonl", tool_rows)
    write_jsonl(out / "webgpt-section-ledger.jsonl", web_sections)
    write_jsonl(out / "gemini-thought-ledger.jsonl", gemini_thoughts)
    write_jsonl(out / "gemini-execution-ledger.jsonl", gemini_execution)
    write_jsonl(out / "work-product-ledger.jsonl", work_products)
    write_jsonl(out / "claim-evidence-ledger.jsonl", claims)
    summary = {
        "schema_version": "historical-ledgers/v1",
        "generated_at_utc": generated_at,
        "canonical_trajectory_reader": str(CANONICAL_TRAJECTORY),
        "source_manifest": SOURCE_MANIFEST.as_posix(),
        "counts": {
            "user_message_disposition": len(user_disposition),
            "ai_response_ledger": len(response_rows),
            "local_gpt_assistant_responses_total": sum(1 for row in response_rows if row.get("platform") == "LocalGPT"),
            "local_gpt_primary_lineage_assistant_responses": sum(1 for row in response_rows if row.get("source_id") in ("codex-parent", "codex-hott2-main")),
            "local_gpt_auxiliary_lineage_assistant_responses": sum(1 for row in response_rows if row.get("platform") == "LocalGPT" and row.get("source_id") not in ("codex-parent", "codex-hott2-main")),
            "webgpt_responses": sum(1 for row in response_rows if row.get("platform") == "WebGPT"),
            "gemini_ordinary_text_responses": sum(1 for row in response_rows if row.get("platform") == "Gemini"),
            "tool_event_ledger": len(tool_rows),
            "webgpt_sections": len(web_sections),
            "gemini_thought_records": len(gemini_thoughts),
            "gemini_execution_records": len(gemini_execution),
            "gemini_executable_code": sum(1 for row in gemini_execution if row.get("record_type") == "executableCode"),
            "gemini_code_execution_results": sum(1 for row in gemini_execution if row.get("record_type") == "codeExecutionResult"),
            "gemini_inline_files": sum(1 for row in gemini_execution if row.get("record_type") == "inlineFile"),
            "work_products": len(work_products),
            "claim_evidence_rows": len(claims),
        },
        "trajectory_sources": trajectory_summaries,
        "errors": errors,
        "coverage_status": "STRUCTURALLY_BUILT; SEMANTIC_CLAIM_MAPPING_AND_MANUAL_REVIEW_PENDING",
        "visibility_policy": {
            "local_gpt_assistant": "full visible text requested through canonical inspect; raw tool output remains locator-backed and bounded",
            "local_gpt_reasoning": "not included; hidden reasoning is not inferred",
            "webgpt": "exported visible Prompt/Response sections retained",
            "gemini_thought": "exported thought field retained as source-visible record, not public answer/proof",
            "gemini_inline_file": "base64 decoded to UTF-8 where possible; not classified empty",
            "gemini_drive_document": "body unavailable remains in user-message disposition",
        },
    }
    (out / "ledger-summary.json").write_text(json.dumps(summary, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    coverage_path = out / "coverage-summary.json"
    if coverage_path.exists():
        coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
        coverage["status"] = "LEDGERS_BUILT_SEMANTIC_REVIEW_PENDING"
        coverage["ledger_built_at_utc"] = generated_at
        coverage["ledger_counts"] = summary["counts"]
        coverage["trajectory_reader_errors"] = len(errors)
        coverage_path.write_text(json.dumps(coverage, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "BUILT", "counts": summary["counts"], "trajectory_errors": len(errors)}, ensure_ascii=False))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
