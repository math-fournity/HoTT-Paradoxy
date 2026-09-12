#!/usr/bin/env python3
"""Build the current core cognition from an explicit human curation.

Generation 3 returns to the user's original contract: only exact user-authored
paradox/metamathematical text from the three named primary extracts enters the
current core. The command is read-only by default. ``--write`` takes an
exclusive lock, uses atomic replacement, and rolls back Python-level failures.
A crash remains fail-closed through the residual lock/hash validator and the
pre-migration Git tag provides durable rollback.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
import uuid
from collections import Counter
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CURATION = Path("scripts/audit/core-cognition-curation-v3.json")
DEFAULT_CORE = Path("核心认知.md")
DEFAULT_MANIFEST = Path("核心认知.manifest.json")
DEFAULT_TRANSITION = Path("audit/core-cognition-generation-3-transition-20260912.json")
LOCK = Path(".codex/cognition/CORE_COGNITION_BUILD.lock")
HEADER_RE = re.compile(r"^##\s+\[(\d+)\]\s+(.+?)\s*$")
GENERATION_RE = re.compile(r"^core-cognition-generation-[0-9]+$")
MESSAGE_ID_RE = re.compile(r"^(LOCALGPT|WEBGPT|GEMINI)-M-[0-9]{3}$")
KC_RE = re.compile(r"^KC-[0-9]{6}$")

THEME_PATTERNS: list[tuple[str, str]] = [
    ("HOTT_OBJECT", r"HoTT|HOTT|同伦类型|类型理论|Theory Schema"),
    ("HOTT_PARADOX", r"HoTT.{0,30}(悖论|矛盾|问题)|悖论.{0,30}HoTT"),
    ("PARADOX_DISCOVERY", r"悖论|反证|矛盾|反例|不相容|非现实性"),
    ("ABSTRACTION_AND_NEGATION", r"抽象|理论化|否定现实|异化|静态|工具性"),
    ("Z_LAW", r"Z铁律|理论抽象必然导致悖论"),
    ("TIME_AND_TEMPORALITY", r"时间|时序|时空|先后|顺序|过程|阶段|运动"),
    ("BEING_AND_BECOMING", r"存在|形成|生成|可用|完成|构造"),
    ("RUSSELL", r"罗素|Russell|集合S"),
    ("ZENO", r"芝诺|Zeno|走一半"),
    ("CIRCLE_PARADOX", r"圆环|圆圈|拿掉一个点|还原"),
    ("BETTER_BEST", r"Better.?Best|最好|最优"),
    ("COMPUTATIONAL_LEGITIMACY", r"可计算|不可计算|不可停机|停机|计算合法|非法程序|算法|执行"),
    ("ASK", r"\bASK\b|合法的提问|有效输入|能否构造|能否完成"),
    ("THEORY_SCHEMA", r"Theory Schema|理论.*Schema|规则|公理|语义|演算"),
    ("EVIDENCE_DISCIPLINE", r"证据|核验|验证|机器证明|Lean|Agda|运行过"),
    ("RESEARCH_METHOD", r"怎么找|凭什么|研究方法|策略|线索|模式匹配|探索"),
    ("SELF_REFERENCE", r"自指|自身|哥德尔|反射"),
    ("ANTI_TRAINING_PRIOR", r"训练数据|训练语料|认知惯性|路径依赖|math philosophy"),
]


class CoreBuildError(RuntimeError):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def read_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CoreBuildError(f"INVALID_JSON:{path}") from exc
    if not isinstance(value, dict):
        raise CoreBuildError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def parse_timestamp(header: str, platform: str) -> tuple[str, str, str]:
    original = re.split(r"\s*[（·]", header, maxsplit=1)[0].strip()
    try:
        if platform == "WebGPT":
            local = dt.datetime.strptime(original, "%m/%d/%Y, %I:%M:%S %p")
            local = local.replace(tzinfo=ZoneInfo("America/New_York"))
            return original, local.astimezone(dt.timezone.utc).isoformat(), "America/New_York"
        parsed = dt.datetime.fromisoformat(original.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=dt.timezone.utc)
        return original, parsed.astimezone(dt.timezone.utc).isoformat(), "source-offset"
    except ValueError as exc:
        raise CoreBuildError(f"TIMESTAMP_PARSE_FAILED:{platform}:{header}") from exc


def parse_source(root: Path, source: dict[str, object]) -> tuple[dict[str, object], list[dict[str, object]], list[str]]:
    platform, rel, expected_sha = source.get("platform"), source.get("path"), source.get("sha256")
    if platform not in {"LocalGPT", "WebGPT", "Gemini"} or not isinstance(rel, str):
        raise CoreBuildError("CURATION_SOURCE_IDENTITY_INVALID")
    path = root / rel
    data = path.read_bytes()
    actual_sha = sha256(data)
    if actual_sha != expected_sha:
        raise CoreBuildError(f"CURATION_SOURCE_HASH_MISMATCH:{rel}:{actual_sha}")
    try:
        body = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CoreBuildError(f"SOURCE_NOT_UTF8:{rel}") from exc
    lines = body.splitlines(keepends=True)
    headers: list[tuple[int, int, str]] = []
    for line_index, line in enumerate(lines):
        match = HEADER_RE.match(line.rstrip("\r\n"))
        if match:
            headers.append((line_index, int(match.group(1)), match.group(2)))
    records: list[dict[str, object]] = []
    for record_index, (header_index, ordinal, header) in enumerate(headers, start=1):
        next_index = headers[record_index][0] if record_index < len(headers) else len(lines)
        timestamp_original, timestamp_utc, timestamp_policy = parse_timestamp(header, str(platform))
        raw_message = "".join(lines[header_index + 1 : next_index])
        raw_message = re.sub(r"\A\s*\n", "", raw_message)
        raw_message = re.sub(r"\n\s*\Z", "", raw_message)
        records.append({
            "source_message_id": f"{str(platform).upper()}-M-{record_index:03d}",
            "platform": platform,
            "source_file": rel,
            "source_file_sha256": actual_sha,
            "source_message_ordinal": ordinal,
            "record_index": record_index,
            "header_line": header_index + 1,
            "body_line_start": header_index + 2,
            "body_line_end": next_index,
            "timestamp_original": timestamp_original,
            "timestamp_utc": timestamp_utc,
            "timestamp_parse_policy": timestamp_policy,
            "message_text_sha256": sha256(raw_message.encode("utf-8")),
            "message_text_bytes": len(raw_message.encode("utf-8")),
        })
    return ({
        "path": rel,
        "platform": platform,
        "input_role": "primary",
        "sha256": actual_sha,
        "bytes": len(data),
        "lines": len(lines),
        "message_count_parsed": len(records),
    }, records, lines)


def unique_marker(text: str, marker: str, label: str) -> int:
    count = text.count(marker)
    if count != 1:
        raise CoreBuildError(f"SELECTOR_MARKER_{label}_COUNT:{count}:{marker[:80]}")
    return text.index(marker)


def select_payload(lines: list[str], record: dict[str, object], spec: dict[str, object]) -> tuple[str, dict[str, object]]:
    source_lines = spec.get("source_lines")
    if not isinstance(source_lines, list) or len(source_lines) != 2 or any(type(v) is not int for v in source_lines):
        raise CoreBuildError(f"SOURCE_LINES_INVALID:{record['source_message_id']}")
    start_line, end_line = source_lines
    if not (int(record["body_line_start"]) <= start_line <= end_line <= int(record["body_line_end"])):
        raise CoreBuildError(f"SOURCE_LINES_OUTSIDE_MESSAGE:{record['source_message_id']}:{source_lines}")
    selected = "".join(lines[start_line - 1 : end_line])
    if selected.endswith("\n"):
        selected = selected[:-1]
    if selected.endswith("\r"):
        selected = selected[:-1]
    operations: dict[str, str] = {}
    for key in ("start_at", "start_after", "end_before", "end_after"):
        value = spec.get(key)
        if value is not None:
            if not isinstance(value, str) or not value:
                raise CoreBuildError(f"SELECTOR_VALUE_INVALID:{record['source_message_id']}:{key}")
            operations[key] = value
    if {"start_at", "start_after"} <= operations.keys() or {"end_before", "end_after"} <= operations.keys():
        raise CoreBuildError(f"MULTIPLE_SELECTORS:{record['source_message_id']}")
    if "start_at" in operations:
        selected = selected[unique_marker(selected, operations["start_at"], "START") :]
    elif "start_after" in operations:
        marker = operations["start_after"]
        selected = selected[unique_marker(selected, marker, "START") + len(marker) :]
    if "end_before" in operations:
        selected = selected[: unique_marker(selected, operations["end_before"], "END")]
    elif "end_after" in operations:
        marker = operations["end_after"]
        selected = selected[: unique_marker(selected, marker, "END") + len(marker)]
    selected = selected.strip("\r\n")
    if not selected.strip():
        raise CoreBuildError(f"EMPTY_CURATED_PAYLOAD:{record['source_message_id']}")
    for token in ("# Response annotations:", "<response-annotations>", "AI回答：", "Gemini:\n"):
        if token in selected:
            raise CoreBuildError(f"RELAYED_CONTEXT_IN_CURATED_PAYLOAD:{record['source_message_id']}:{token}")
    receipt: dict[str, object] = {"source_line_start": start_line, "source_line_end": end_line}
    receipt.update(operations)
    return selected, receipt


def themes_for(text: str) -> list[str]:
    return [name for name, pattern in THEME_PATTERNS if re.search(pattern, text, re.I)]


def classify_lifecycle(text: str) -> str:
    if re.search(r"机器证明|Lean|Agda|运行过|证明", text, re.I):
        return "RESEARCH_EVIDENCE_REQUIREMENT"
    if re.search(r"为什么|是否|能不能|如何|怎么找|凭什么|我不相信", text, re.I):
        return "QUESTION_OR_OPEN_PROBLEM"
    if re.search(r"我认为|我觉得|我怀疑|在我看来|其实|也就是说|所以", text, re.I):
        return "POSITION_OR_REFINEMENT"
    return "RESEARCH_CONTEXT"


def fenced_payload(text: str) -> str:
    marker = "~" * max(3, max((len(run) for run in re.findall(r"~+", text)), default=0) + 3)
    return f"{marker}text\n{text}\n{marker}"


def load_curation(root: Path, rel: Path) -> tuple[dict[str, object], bytes]:
    path = root / rel
    data = path.read_bytes()
    value = read_json(path)
    if value.get("schema_version") != "core-cognition-curation/v1":
        raise CoreBuildError("CURATION_SCHEMA_INVALID")
    generation = value.get("generation")
    if not isinstance(generation, str) or not GENERATION_RE.fullmatch(generation):
        raise CoreBuildError("CURATION_GENERATION_INVALID")
    if value.get("asset_class") != "HUMAN_EDITED_CURATION_AUTHORITY":
        raise CoreBuildError("CURATION_ASSET_CLASS_INVALID")
    return value, data


def build(root: Path, curation_rel: Path = DEFAULT_CURATION) -> tuple[dict[str, object], str, bytes, list[dict[str, object]]]:
    curation, curation_bytes = load_curation(root, curation_rel)
    source_specs = curation.get("sources")
    if not isinstance(source_specs, list) or len(source_specs) != 3:
        raise CoreBuildError("EXACTLY_THREE_PRIMARY_SOURCES_REQUIRED")
    file_rows: list[dict[str, object]] = []
    records: list[dict[str, object]] = []
    lines_by_file: dict[str, list[str]] = {}
    for source in source_specs:
        if not isinstance(source, dict):
            raise CoreBuildError("CURATION_SOURCE_ROW_INVALID")
        file_row, parsed, lines = parse_source(root, source)
        file_rows.append(file_row)
        records.extend(parsed)
        lines_by_file[str(file_row["path"])] = lines
    records_by_id = {str(row["source_message_id"]): row for row in records}
    if len(records_by_id) != len(records):
        raise CoreBuildError("DUPLICATE_PARSED_MESSAGE_ID")

    decision_rows = curation.get("message_decisions")
    if not isinstance(decision_rows, list):
        raise CoreBuildError("MESSAGE_DECISIONS_REQUIRED")
    decisions: dict[str, dict[str, object]] = {}
    for row in decision_rows:
        if not isinstance(row, dict):
            raise CoreBuildError("MESSAGE_DECISION_ROW_INVALID")
        message_id, disposition, reason = row.get("source_message_id"), row.get("disposition"), row.get("reason")
        if not isinstance(message_id, str) or not MESSAGE_ID_RE.fullmatch(message_id):
            raise CoreBuildError(f"MESSAGE_DECISION_ID_INVALID:{message_id}")
        if message_id in decisions:
            raise CoreBuildError(f"DUPLICATE_MESSAGE_DECISION:{message_id}")
        if not isinstance(disposition, str) or not disposition or not isinstance(reason, str) or not reason.strip():
            raise CoreBuildError(f"MESSAGE_DECISION_INVALID:{message_id}")
        decisions[message_id] = row
    parsed_ids, decision_ids = set(records_by_id), set(decisions)
    if parsed_ids != decision_ids:
        raise CoreBuildError(
            f"MESSAGE_DECISION_DENOMINATOR_MISMATCH:missing={sorted(parsed_ids-decision_ids)}:extra={sorted(decision_ids-parsed_ids)}"
        )

    unit_specs = curation.get("units")
    if not isinstance(unit_specs, list) or not unit_specs:
        raise CoreBuildError("CURATED_UNITS_REQUIRED")
    provisional: list[dict[str, object]] = []
    unit_counts: Counter[str] = Counter()
    for order, spec in enumerate(unit_specs, start=1):
        if not isinstance(spec, dict):
            raise CoreBuildError("CURATED_UNIT_ROW_INVALID")
        message_id, label = spec.get("source_message_id"), spec.get("semantic_label")
        if not isinstance(message_id, str) or message_id not in records_by_id:
            raise CoreBuildError(f"CURATED_UNIT_MESSAGE_UNKNOWN:{message_id}")
        if decisions[message_id]["disposition"] != "INCLUDED":
            raise CoreBuildError(f"CURATED_UNIT_REFERENCES_EXCLUDED_MESSAGE:{message_id}")
        if not isinstance(label, str) or not label.strip():
            raise CoreBuildError(f"SEMANTIC_LABEL_REQUIRED:{message_id}")
        record = records_by_id[message_id]
        payload, selector = select_payload(lines_by_file[str(record["source_file"])], record, spec)
        provisional.append({
            "source_message_id": message_id,
            "platform": record["platform"],
            "timestamp_original": record["timestamp_original"],
            "timestamp_utc": record["timestamp_utc"],
            "timestamp_parse_policy": record["timestamp_parse_policy"],
            "source_file": record["source_file"],
            "source_sha256": record["source_file_sha256"],
            "source_message_ordinal": record["source_message_ordinal"],
            "source_message_sha256": record["message_text_sha256"],
            "selector": selector,
            "semantic_label": label,
            "selection_reason": decisions[message_id]["reason"],
            "author_class": "USER_OWNED_DIRECT",
            "themes": themes_for(payload),
            "lifecycle": classify_lifecycle(payload),
            "unit_sha256": sha256(payload.encode("utf-8")),
            "unit_bytes": len(payload.encode("utf-8")),
            "curation_order": order,
            "text": payload,
        })
        unit_counts[message_id] += 1
    for message_id, decision in decisions.items():
        if (decision["disposition"] == "INCLUDED") != (unit_counts[message_id] > 0):
            raise CoreBuildError(f"MESSAGE_UNIT_DISPOSITION_MISMATCH:{message_id}")

    platform_rank = {"LocalGPT": 0, "WebGPT": 1, "Gemini": 2}
    provisional.sort(key=lambda row: (
        row["timestamp_utc"], platform_rank[str(row["platform"])],
        int(row["source_message_ordinal"]), int(row["curation_order"])
    ))
    units: list[dict[str, object]] = []
    for index, row in enumerate(provisional, start=1):
        current = dict(row)
        current["id"] = f"KC-{index:06d}"
        selector = current["selector"]
        current["source_locator"] = (
            f"{current['source_file']}#L{selector['source_line_start']}-L{selector['source_line_end']}"
        )
        current["relations"] = ([{"type": "same_source_message", "target": str(units[-1]["id"])}]
                                if units and units[-1]["source_message_id"] == current["source_message_id"] else [])
        units.append(current)

    dispositions: list[dict[str, object]] = []
    for record in records:
        message_id = str(record["source_message_id"])
        decision = decisions[message_id]
        dispositions.append({
            "source_message_id": message_id,
            "platform": record["platform"],
            "input_role": "primary",
            "source_file": record["source_file"],
            "source_file_sha256": record["source_file_sha256"],
            "source_message_ordinal": record["source_message_ordinal"],
            "source_record_index": record["record_index"],
            "source_header_line": record["header_line"],
            "timestamp_original": record["timestamp_original"],
            "timestamp_utc": record["timestamp_utc"],
            "timestamp_parse_policy": record["timestamp_parse_policy"],
            "message_text_sha256": record["message_text_sha256"],
            "message_text_bytes": record["message_text_bytes"],
            "disposition": decision["disposition"],
            "disposition_reason": decision["reason"],
            "unit_count": unit_counts[message_id],
        })

    public_units = [{k: v for k, v in row.items() if k not in {"text", "curation_order"}} for row in units]
    disposition_counts = Counter(str(row["disposition"]) for row in dispositions)
    manifest: dict[str, object] = {
        "schema_version": "core-cognition/v2",
        "asset_class": "MACHINE_MANAGED_CANONICAL",
        "canonical_manager": "scripts/audit/build_core_cognition.py",
        "curation_authority": curation_rel.as_posix(),
        "curation_sha256": sha256(curation_bytes),
        "generation": curation["generation"],
        "previous_generation_ref": curation.get("previous_generation_ref"),
        "build_policy": {
            "primary_inputs_only": [row["path"] for row in file_rows],
            "primary_denominator": len(records),
            "semantic_boundary": "human-curated exact source ranges; one KC per coherent user idea",
            "source_text_policy": "exact UTF-8 substring copy; no paraphrase or normalization",
            "relayed_ai_policy": "retained in source/disposition, excluded from USER_OWNED_DIRECT current core",
            "duplicate_policy": "retain evolution; omit exact/redundant cross-platform repetition with per-message reason",
            "timestamp_policy": "UTC sort; WebGPT naive export timestamp interpreted as America/New_York",
            "inline_metadata_policy": "compact human locator only; full provenance remains in manifest",
        },
        "files": file_rows,
        "message_disposition": dispositions,
        "counts": {
            "primary_files": len(file_rows),
            "messages_parsed": len(records),
            "messages_included": sum(1 for row in dispositions if row["disposition"] == "INCLUDED"),
            "messages_excluded": sum(1 for row in dispositions if row["disposition"] != "INCLUDED"),
            "core_units": len(units),
            "dispositions": dict(sorted(disposition_counts.items())),
            "units_by_platform": dict(sorted(Counter(str(row["platform"]) for row in units).items())),
        },
        "units": public_units,
    }

    lines = [
        "# 核心认知", "",
        f"> 当前逻辑文档：`{curation['generation']}`；Schema：`core-cognition/v2`；共 `{len(units)}` 个按时间编号的用户原文语义单元。",
        "> 本文只保留三份用户指定 primary 提取中，用户本人关于悖论、HoTT 悖论挖掘、元数学及其直接研究方法的原文；不含 AI 回信、附件正文、一般治理操作或重复的继续指令。",
        "> 每个新 Session 与每次上下文压缩恢复后，都必须从第 1 行连续读到 EOF。`核心认知.manifest.json` 只负责来源、处置和哈希审计，不能替代本文正文。",
        "", "## 0. 解释与证据边界", "",
        "这些文字是用户为突破模型训练先验、认知惯性和路径依赖而设计的上下文输入；它们决定研究问题意识，但不会因进入本文就自动成为已经证明的数学定理或物理事实。研究仍须分别核对 HoTT 规则、合法推演、计算/证明工具、现实解释和证据范围。",
        "",
        "本代从 `governance-v2.1.0` 所保存的 generation-2 重建，而不是在 913 个机械分段上继续追加。旧 core、supplemental、转发 AI 内容及逐 KC 审计完整保留在 Git、来源和 generation transition receipt 中；退出当前全文输入不等于删除历史。",
        "", "## 1. 按时间顺序的用户核心认知原文", "",
    ]
    for row in units:
        selector = row["selector"]
        lines.extend([
            f"### {row['id']} · {row['platform']} · {row['timestamp_original']} · {row['semantic_label']}", "",
            f"> 来源锚点：`{row['source_file']}#L{selector['source_line_start']}-L{selector['source_line_end']}`；消息：`{row['source_message_id']}`。", "",
            fenced_payload(str(row["text"])), "",
        ])
    core_text = "\n".join(lines).rstrip() + "\n"
    manifest["core_document_sha256"] = sha256(core_text.encode("utf-8"))
    return manifest, core_text, json_bytes(manifest), units


def parse_core_payloads(text: str) -> dict[str, str]:
    lines = text.splitlines(keepends=True)
    payloads: dict[str, str] = {}
    index = 0
    while index < len(lines):
        match = re.match(r"^### (KC-[0-9]{6}) · ", lines[index])
        if not match:
            index += 1
            continue
        unit_id = match.group(1)
        index += 1
        while index < len(lines):
            fence = re.fullmatch(r"(~{3,})text", lines[index].rstrip("\r\n"))
            if fence:
                break
            if re.match(r"^### KC-[0-9]{6} · ", lines[index]):
                raise CoreBuildError(f"OLD_CORE_PAYLOAD_MISSING:{unit_id}")
            index += 1
        if index >= len(lines):
            raise CoreBuildError(f"OLD_CORE_FENCE_MISSING:{unit_id}")
        marker = fence.group(1)
        index += 1
        body: list[str] = []
        while index < len(lines) and lines[index].rstrip("\r\n") != marker:
            body.append(lines[index]); index += 1
        if index >= len(lines):
            raise CoreBuildError(f"OLD_CORE_FENCE_UNCLOSED:{unit_id}")
        payload = "".join(body)
        if payload.endswith("\n"):
            payload = payload[:-1]
        if payload.endswith("\r"):
            payload = payload[:-1]
        payloads[unit_id] = payload
        index += 1
    return payloads


def git_blob(root: Path, ref: str, rel: str) -> bytes:
    result = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=root, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, check=False)
    if result.returncode != 0:
        error = result.stderr.decode("utf-8", "replace").strip()
        raise CoreBuildError(f"PREVIOUS_GENERATION_GIT_BLOB_FAILED:{ref}:{rel}:{error}")
    return result.stdout


def build_transition(root: Path, previous_ref: str, new_manifest: dict[str, object],
                     new_units: list[dict[str, object]]) -> dict[str, object]:
    old_core_bytes = git_blob(root, previous_ref, DEFAULT_CORE.as_posix())
    old_manifest_bytes = git_blob(root, previous_ref, DEFAULT_MANIFEST.as_posix())
    old_manifest = json.loads(old_manifest_bytes.decode("utf-8"))
    old_payloads = parse_core_payloads(old_core_bytes.decode("utf-8"))
    old_units = old_manifest.get("units")
    if not isinstance(old_units, list) or len(old_units) != len(old_payloads):
        raise CoreBuildError("PREVIOUS_GENERATION_UNIT_COUNT_MISMATCH")
    decisions = {str(row["source_message_id"]): row for row in new_manifest["message_disposition"]}
    new_by_message: dict[str, list[dict[str, object]]] = {}
    for row in new_units:
        new_by_message.setdefault(str(row["source_message_id"]), []).append(row)
    mappings: list[dict[str, object]] = []
    relation_counts: Counter[str] = Counter()
    for old in old_units:
        old_id = str(old.get("id"))
        if not KC_RE.fullmatch(old_id) or old_id not in old_payloads:
            raise CoreBuildError(f"PREVIOUS_GENERATION_ID_INVALID:{old_id}")
        payload, message_id = old_payloads[old_id], str(old.get("source_message_id"))
        targets: list[str] = []
        if old.get("input_role") != "primary" or message_id not in decisions:
            relation = "EXCLUDED_NON_PRIMARY_INPUT"
            reason = "Generation 3 uses only the three user-named primary extracts; supplemental/governance inputs remain historical."
        elif old.get("author_class") == "USER_RELAYED_CONTEXT":
            relation = "EXCLUDED_RELAYED_AI_CONTEXT"
            reason = "Relayed AI/annotation text remains in source history but is not direct user cognition."
        elif decisions[message_id]["disposition"] != "INCLUDED":
            relation = "EXCLUDED_BY_CURRENT_SCOPE"
            reason = f"{decisions[message_id]['disposition']}: {decisions[message_id]['disposition_reason']}"
        else:
            candidates = new_by_message.get(message_id, [])
            exact = [row for row in candidates if str(row["text"]) == payload]
            containing = [row for row in candidates if payload and payload in str(row["text"])]
            contained = [row for row in candidates if str(row["text"]) and str(row["text"]) in payload]
            chosen = exact or containing or contained
            targets = [str(row["id"]) for row in chosen]
            if exact:
                relation, reason = "PRESERVED_EXACT", "Previous and current payloads are byte-identical."
            elif containing:
                relation, reason = "MERGED_EXACT_INTO_SEMANTIC_UNIT", "The old mechanical fragment is an exact substring of a coherent current unit."
            elif contained:
                relation, reason = "CURATED_EXACT_SUBRANGE", "The current direct-user unit is an exact subrange of an old mixed/over-broad fragment."
            else:
                relation, reason = "EXCLUDED_NON_CORE_WITHIN_INCLUDED_MESSAGE", "The message remains represented, but this old fragment is outside the curated direct-user ranges."
        relation_counts[relation] += 1
        mappings.append({
            "old_id": old_id,
            "old_source_message_id": message_id,
            "old_source_file": old.get("source_file"),
            "old_author_class": old.get("author_class"),
            "old_unit_sha256": old.get("unit_sha256"),
            "relation": relation,
            "target_ids": targets,
            "reason": reason,
        })
    return {
        "schema_version": "core-cognition-transition/v2",
        "status": "COMPLETE_WITH_EXPLICIT_SCOPE_REDUCTION",
        "previous": {
            "ref": previous_ref, "generation": old_manifest.get("generation"),
            "schema_version": old_manifest.get("schema_version"),
            "core_sha256": sha256(old_core_bytes), "manifest_sha256": sha256(old_manifest_bytes),
            "unit_count": len(old_units),
        },
        "current": {
            "generation": new_manifest.get("generation"), "schema_version": new_manifest.get("schema_version"),
            "core_sha256": new_manifest.get("core_document_sha256"),
            "curation_sha256": new_manifest.get("curation_sha256"), "unit_count": len(new_units),
        },
        "policy": "Every previous KC is mapped, merged, narrowed, or explicitly excluded; current-core exclusion never deletes source/Git history.",
        "relation_counts": dict(sorted(relation_counts.items())),
        "mapping_count": len(mappings), "mapping_remainder": len(old_units) - len(mappings),
        "mappings": mappings,
    }


def atomic_replace(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(f".{path.name}.tmp-{uuid.uuid4().hex}")
    try:
        with temp.open("xb") as handle:
            handle.write(data); handle.flush(); os.fsync(handle.fileno())
        os.replace(temp, path)
        try:
            descriptor = os.open(path.parent, os.O_RDONLY); os.fsync(descriptor); os.close(descriptor)
        except OSError:
            pass
    finally:
        if temp.exists():
            temp.unlink()


def write_outputs(root: Path, outputs: list[tuple[Path, bytes]]) -> None:
    lock_path = root / LOCK
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise CoreBuildError(f"CORE_BUILD_LOCKED:{LOCK}") from exc
    before: dict[Path, bytes | None] = {}
    completed: list[Path] = []
    try:
        os.write(descriptor, json_bytes({"pid": os.getpid(), "outputs": [p.as_posix() for p, _ in outputs]}))
        os.fsync(descriptor); os.close(descriptor)
        for rel, data in outputs:
            path = root / rel
            before[path] = path.read_bytes() if path.exists() else None
            atomic_replace(path, data); completed.append(path)
    except BaseException:
        for path in reversed(completed):
            previous = before[path]
            if previous is None:
                path.unlink(missing_ok=True)
            else:
                atomic_replace(path, previous)
        raise
    finally:
        lock_path.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--curation", type=Path, default=DEFAULT_CURATION)
    parser.add_argument("--core", type=Path, default=DEFAULT_CORE)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--transition-output", type=Path, default=DEFAULT_TRANSITION)
    parser.add_argument("--transition-from-ref")
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.project_root.resolve()
    try:
        manifest, core_text, manifest_bytes, units = build(root, args.curation)
        transition = None
        outputs = [(args.core, core_text.encode("utf-8")), (args.manifest, manifest_bytes)]
        if args.transition_from_ref:
            transition = build_transition(root, args.transition_from_ref, manifest, units)
            outputs.append((args.transition_output, json_bytes(transition)))
        if args.write:
            write_outputs(root, outputs); status = "BUILT"
        else:
            mismatches = [rel.as_posix() for rel, expected in outputs
                          if not (root / rel).is_file() or (root / rel).read_bytes() != expected]
            if mismatches:
                print(json.dumps({"status": "OUT_OF_DATE", "mismatches": mismatches}, ensure_ascii=False))
                return 1
            status = "PASS"
        print(json.dumps({
            "status": status, "generation": manifest["generation"], "counts": manifest["counts"],
            "core_sha256": manifest["core_document_sha256"],
            "transition_mapping_count": transition["mapping_count"] if transition else None,
        }, ensure_ascii=False))
        return 0
    except (CoreBuildError, OSError, ValueError, TypeError, KeyError, subprocess.SubprocessError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
