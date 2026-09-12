#!/usr/bin/env python3
"""Build the immutable, chronological core-cognition ledger.

The three user-message extraction files named by the user are the primary
inputs.  The Codex parent and parallel extraction files are included as
explicit supplements so that the 38-turn local-GPT lineage is not silently
reduced to the HoTT-2 child file.  This script is deliberately deterministic:
it does not use an LLM, does not rewrite source text, and records every source
message in a disposition ledger whether or not it becomes a core unit.

The generated Markdown contains the exact selected source payloads.  The JSON
manifest is the machine-readable authority for IDs, hashes, timestamps,
locators, and dispositions.  Re-running the script is expected to change only
the build timestamp and therefore is suitable for reproducibility checks.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[2]
PRIMARY = [
    ("LocalGPT", "primary", Path("sources/prompts/Codex-HoTT-2-用户消息提取-20260911.md"), 0),
    ("WebGPT", "primary", Path("sources/prompts/ChatGPT-HoTT-Main-用户消息提取-20260911.md"), 1),
    ("Gemini", "primary", Path("sources/prompts/Gemini-AI对话录-用户消息提取-20260911.md"), 2),
]
SUPPLEMENTAL = [
    ("LocalGPT", "supplemental", Path("sources/prompts/Codex-HoTT父线程-01a059c1-用户消息提取-20260911.md"), 0),
    ("LocalGPT", "supplemental", Path("sources/prompts/Codex-并行会话-素数与归档-用户消息提取-20260911.md"), 0),
]
USER_REQUIREMENT_SUPPLEMENTAL = [
    (
        "User",
        "user_requirement_supplemental",
        Path("sources/prompts/治理三件套与历史融合要求-用户消息提取-20260912.md"),
        3,
    ),
]

THEME_PATTERNS: list[tuple[str, str]] = [
    ("HOTT_OBJECT", r"HoTT|HOTT|同伦类型|类型理论|类型构造|Theory Schema"),
    ("HOTT_PARADOX", r"HoTT.{0,30}(悖论|矛盾|问题)|悖论.{0,30}HoTT"),
    ("PARADOX_DISCOVERY", r"悖论|反证|矛盾|反例|不相容|非现实性"),
    ("ABSTRACTION_AND_NEGATION", r"抽象|理论化|否定现实|理想化|静态|工具性"),
    ("Z_LAW", r"Z铁律|理论抽象必然导致悖论"),
    ("TIME_AND_TEMPORALITY", r"时间|时序|时空|时间维度|先后|顺序|过程|阶段|历史"),
    ("BEING_AND_BECOMING", r"存在|形成|生成|可用|完成|成为|本体|静态"),
    ("RUSSELL", r"罗素|Russell|集合S|朴素集合"),
    ("ZENO", r"芝诺|Zeno|走一半"),
    ("CIRCLE_PARADOX", r"圆环|圆圈|拿掉一个点|还原"),
    ("BETTER_BEST", r"Better.?Best|最好|最优"),
    ("SHENCHENSH_MATRIX", r"深层|矩阵|Shen|九类|方向"),
    ("IDENTITY_UNIVALENCE_TRANSPORT", r"恒等|身份|相等|等价|路径|运输|transport|univalence|单值性"),
    ("TRUNCATION_QUOTIENT_REFLECTION", r"截断|商类型|quotient|reflection|反射|消去"),
    ("GUARDED_DIRECTED_VARIANTS", r"guard|guarded|有向|递归|不动点|固定点|自应用"),
    ("COMPUTATIONAL_LEGITIMACY", r"可计算|不可计算|不可停机|停机|计算合法|非法程序|算法|执行"),
    ("ASK", r"\bASK\b|合法的提问|有效输入|能否构造|能否完成"),
    ("THEORY_SCHEMA", r"Theory Schema|理论.*Schema|规则|公理|语义|演算"),
    ("EVIDENCE_DISCIPLINE", r"证据|核验|验证|机器证明|Lean|Agda|运行过|审计锚点|可审计"),
    ("RESEARCH_METHOD", r"怎么找|凭什么|研究方法|策略|线索|候选|探索|反驳"),
    ("SESSION_CONTINUITY", r"Session|跨会话|连续性|认知闭包|MEMORY|全文加载|压缩"),
    ("HANDOFF_GOVERNANCE", r"交接|治理|工作流|落盘|Skill|工作目录|Git|提交"),
]
BUSINESS_RE = re.compile("|".join(f"(?:{p})" for _, p in THEME_PATTERNS), re.I)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_utf8(path: Path) -> tuple[str, str]:
    data = path.read_bytes()
    return data.decode("utf-8"), sha256(data)


def parse_timestamp(header: str, platform: str) -> tuple[str, str, str]:
    """Return original timestamp, UTC ISO timestamp, and parse policy."""
    original = header
    original = re.split(r"\s*[（·]", original, maxsplit=1)[0].strip()
    if platform == "WebGPT":
        local = dt.datetime.strptime(original, "%m/%d/%Y, %I:%M:%S %p")
        local = local.replace(tzinfo=ZoneInfo("America/New_York"))
        return original, local.astimezone(dt.timezone.utc).isoformat(), "America/New_York"
    value = original.replace("Z", "+00:00")
    parsed = dt.datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return original, parsed.astimezone(dt.timezone.utc).isoformat(), "source-offset"


def parse_record_header(header: str, platform: str) -> tuple[str, str, dict[str, object]]:
    timestamp_original, timestamp_utc, timestamp_policy = parse_timestamp(header, platform)
    line_match = re.search(r"源文件第\s*([0-9]+)\s*行", header)
    meta: dict[str, object] = {
        "timestamp_parse_policy": timestamp_policy,
        "source_line": int(line_match.group(1)) if line_match else None,
    }
    if "driveDocument" in header or "附件" in header:
        meta["attachment_reference"] = True
    return timestamp_original, timestamp_utc, meta


def split_records(text: str) -> list[tuple[int, str, str]]:
    """Find extraction records without using horizontal rules as delimiters."""
    matches = list(re.finditer(r"(?m)^#{2,3}\s+\[(\d+)\]\s+(.+?)\s*$", text))
    records: list[tuple[int, str, str]] = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end]
        body = re.sub(r"\A\s*\n", "", body)
        body = re.sub(r"\n\s*\Z", "", body)
        records.append((int(match.group(1)), match.group(2), body))
    return records


def split_units(text: str) -> list[str]:
    """Split on blank lines outside fenced code, preserving each payload."""
    lines = text.splitlines(keepends=True)
    chunks: list[str] = []
    current: list[str] = []
    fence: str | None = None
    for line in lines:
        stripped = line.lstrip()
        fence_match = re.match(r"(`{3,}|~{3,})", stripped)
        if fence is None and fence_match:
            fence = fence_match.group(1)[0]
        elif fence is not None and fence_match and fence_match.group(1)[0] == fence:
            fence = None
        if not line.strip() and fence is None:
            if current:
                chunks.append("".join(current).strip("\r\n"))
                current = []
        else:
            current.append(line)
    if current:
        chunks.append("".join(current).strip("\r\n"))
    return [
        chunk
        for chunk in chunks
        if chunk.strip() and chunk.strip() not in {"---", "----", "-----"}
    ]


def segment_author_class(body: str) -> list[tuple[str, str]]:
    marker = re.search(r"(?m)^##\s+My request:\s*$", body)
    if not marker:
        return [("USER_OWNED", body)]
    before = body[: marker.start()].strip("\r\n")
    after = body[marker.end() :].strip("\r\n")
    parts: list[tuple[str, str]] = []
    if before.strip():
        parts.append(("USER_RELAYED_CONTEXT", before))
    if after.strip():
        parts.append(("USER_OWNED", after))
    return parts


def classify_lifecycle(text: str) -> str:
    if re.search(r"(?i)\b(必须|需要|请|立即|开始|执行|记录|落盘|提交|全文加载|每次)", text):
        if re.search(r"(?i)提交|执行|落盘|记录|加载|治理|工作流|Skill", text):
            return "HANDOFF_REQUIREMENT"
        return "EVIDENCE_REQUIREMENT"
    if re.search(r"(?i)\b(为什么|是否|能不能|如何|怎么|你认为|你是否|有没有)", text):
        return "QUESTION_OR_OPEN_PROBLEM"
    if re.search(r"(但是|不过|不完全|注意|其实|重要的是|换句话说|我认为|在我看来)", text):
        return "POSITION_OR_CORRECTION"
    return "RESEARCH_CONTEXT"


def themes_for(text: str) -> list[str]:
    return [name for name, pattern in THEME_PATTERNS if re.search(pattern, text, re.I)]


def max_tilde_run(text: str) -> int:
    runs = re.findall(r"~+", text)
    return max((len(run) for run in runs), default=0)


def fenced_payload(text: str) -> str:
    size = max(3, max_tilde_run(text) + 3)
    marker = "~" * size
    return f"{marker}text\n{text}\n{marker}"


def parse_sources(
    root: Path, include_user_requirements: bool = False
) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    messages: list[dict[str, object]] = []
    files: list[dict[str, object]] = []
    all_inputs = PRIMARY + SUPPLEMENTAL
    if include_user_requirements:
        all_inputs += USER_REQUIREMENT_SUPPLEMENTAL
    for platform, role, rel, rank in all_inputs:
        path = root / rel
        text, file_sha = read_utf8(path)
        file_row = {
            "path": rel.as_posix(),
            "platform": platform,
            "input_role": role,
            "sha256": file_sha,
            "bytes": path.stat().st_size,
            "message_count_declared": None,
        }
        records = split_records(text)
        file_row["message_count_parsed"] = len(records)
        files.append(file_row)
        for record_index, (ordinal, header, body) in enumerate(records, start=1):
            ts_original, ts_utc, header_meta = parse_record_header(header, platform)
            prefix = "P" if "父线程" in rel.name else "S" if "并行" in rel.name else "M"
            message_id = f"{platform.upper()}-{prefix}-{record_index:03d}"
            source_locator = f"{rel.as_posix()}#record-{record_index};message-{ordinal}"
            if header_meta.get("source_line") is not None:
                source_locator += f";source-line-{header_meta['source_line']}"
            # The parallel extraction is a prime-only branch.  It is kept in
            # the disposition ledger for lineage completeness, but the user
            # explicitly said that pure prime research must not enter the
            # HoTT/paradox core document.
            message_business = bool(BUSINESS_RE.search(body)) and "并行" not in rel.name
            segments = segment_author_class(body)
            unit_rows: list[dict[str, object]] = []
            for segment_class, segment in segments:
                for unit_ordinal, unit_text in enumerate(split_units(segment), start=1):
                    unit_themes = themes_for(unit_text)
                    if "并行" in rel.name or (not message_business and not unit_themes):
                        continue
                    unit_rows.append(
                        {
                            "text": unit_text,
                            "author_class": segment_class,
                            "unit_ordinal": unit_ordinal,
                            "themes": unit_themes,
                        }
                    )
            disposition = "INCLUDED" if unit_rows else "EXCLUDED_OUT_OF_SCOPE"
            if header_meta.get("attachment_reference"):
                disposition = "ATTACHMENT_REFERENCE_ONLY"
            messages.append(
                {
                    "source_message_id": message_id,
                    "platform": platform,
                    "input_role": role,
                    "source_file": rel.as_posix(),
                    "source_file_sha256": file_sha,
                    "source_message_ordinal": ordinal,
                    "timestamp_original": ts_original,
                    "timestamp_utc": ts_utc,
                    "timestamp_parse_policy": header_meta["timestamp_parse_policy"],
                    "source_locator": source_locator,
                    "source_line": header_meta.get("source_line"),
                    "attachment_reference": bool(header_meta.get("attachment_reference")),
                    "message_text_sha256": sha256(body.encode("utf-8")),
                    "message_text_bytes": len(body.encode("utf-8")),
                    "business_keyword_match": message_business,
                    "disposition": disposition,
                    "unit_count": len(unit_rows),
                    "unit_rows": unit_rows,
                }
            )
    return messages, files


def build(
    root: Path, generation: str = "core-cognition-generation-1", include_user_requirements: bool = False
) -> tuple[dict[str, object], str, str]:
    messages, files = parse_sources(root, include_user_requirements=include_user_requirements)
    included = [m for m in messages if m["disposition"] == "INCLUDED"]
    included.sort(
        key=lambda m: (
            m["timestamp_utc"],
            0 if m["platform"] == "LocalGPT" else 1 if m["platform"] == "WebGPT" else 2,
            int(m["source_message_ordinal"]),
            str(m["source_locator"]),
        )
    )
    units: list[dict[str, object]] = []
    unit_number = 1
    for message in included:
        for unit in message["unit_rows"]:
            text = str(unit["text"])
            unit_id = f"KC-{unit_number:06d}"
            relations: list[dict[str, str]] = []
            if units:
                previous = units[-1]
                if message["source_message_id"] == previous["source_message_id"]:
                    relations.append({"type": "same_source_message", "target": str(previous["id"])})
                if re.search(r"(但是|不过|不完全|注意|其实|补充|另外|换句话说)", text):
                    relations.append({"type": "possible_correction_or_refinement", "target": str(previous["id"])})
            units.append(
                {
                    "id": unit_id,
                    "source_message_id": message["source_message_id"],
                    "platform": message["platform"],
                    "input_role": message["input_role"],
                    "timestamp_original": message["timestamp_original"],
                    "timestamp_utc": message["timestamp_utc"],
                    "source_file": message["source_file"],
                    "source_locator": message["source_locator"] + f";unit-{unit['unit_ordinal']}",
                    "source_sha256": message["source_file_sha256"],
                    "source_message_sha256": message["message_text_sha256"],
                    "unit_sha256": sha256(text.encode("utf-8")),
                    "unit_bytes": len(text.encode("utf-8")),
                    "author_class": unit["author_class"],
                    "themes": unit["themes"],
                    "lifecycle": classify_lifecycle(text),
                    "relations": relations,
                    "unit_ordinal": unit["unit_ordinal"],
                    "text": text,
                }
            )
            unit_number += 1

    manifest: dict[str, object] = {
        "schema_version": "core-cognition/v1",
        "generation": generation,
        "build_policy": {
            "primary_inputs": [rel.as_posix() for _, _, rel, _ in PRIMARY],
            "supplemental_inputs": [rel.as_posix() for _, _, rel, _ in SUPPLEMENTAL],
            "user_requirement_inputs": [rel.as_posix() for _, _, rel, _ in USER_REQUIREMENT_SUPPLEMENTAL]
            if include_user_requirements
            else [],
            "unit_boundary": "paragraph outside fenced code; exact UTF-8 payload; metadata-only classification",
            "business_filter": "high-recall keyword themes; excluded messages remain in disposition",
            "timestamp_policy": "UTC sort; WebGPT naive export timestamp interpreted as America/New_York",
            "source_text_policy": "never paraphrase or normalize selected payloads",
        },
        "files": files,
        "message_disposition": [
            {k: v for k, v in row.items() if k != "unit_rows"}
            for row in messages
        ],
        "counts": {
            "primary_files": len(PRIMARY),
            "supplemental_files": len(SUPPLEMENTAL),
            "user_requirement_files": len(USER_REQUIREMENT_SUPPLEMENTAL) if include_user_requirements else 0,
            "messages_parsed": len(messages),
            "messages_included": sum(1 for row in messages if row["disposition"] == "INCLUDED"),
            "messages_excluded": sum(1 for row in messages if row["disposition"] != "INCLUDED"),
            "core_units": len(units),
        },
        "units": [{k: v for k, v in row.items() if k != "text"} for row in units],
    }

    lines = [
        "# 核心认知",
        "",
        f"> 机器生成的原文认知账本。Schema：`core-cognition/v1`；generation：`{generation}`。",
        "> 本文件的原文单元只从 `sources/prompts/` 中登记的用户消息提取文件复制；不要把这里的原文改写成 AI 摘要。",
        "> 每次工作开始必须从第 1 行读到 EOF；每次工作结束必须逐一回评所有 `KC-*` 编号。机器清单 `核心认知.manifest.json` 保存哈希、定位和处置记录。",
        "",
        "## 0. 读取与证据规则",
        "",
        "本账本不是 HoTT 的公理、数学定理或外部事实认证。它保存用户在历史对话中的原始研究方向、判断、问题、证据要求和交接要求。`USER_RELAYED_CONTEXT` 表示用户转发/批注的上下文，不冒充用户已经证明的结论；`USER_OWNED` 表示提取记录中用户自己的正文。主题、生命周期和关系字段是机器辅助索引，不能替代逐字原文与来源证据。",
        "",
        "排序使用 `timestamp_utc → platform → source_message_ordinal → source_locator → unit_ordinal`。同一时间戳只表示排序相同，不凭此制造因果关系。对悖论、非现实性、不可停机和 HoTT 的判断，必须再回到 `理解章节/`、`HoTT/`、来源快照、AI response ledger、代码、运行结果与 Git。",
        "",
        "## 1. 输入与计数",
        "",
        f"本次生成解析了 `{manifest['counts']['messages_parsed']}` 条消息，收录 `{manifest['counts']['core_units']}` 个核心单元；三份用户指定提取文件为 primary，Codex 父线程和并行会话是为完整处理 38-turn lineage 而登记的 supplemental；本代若存在用户治理补充，则按单独的 `user_requirement_supplemental` 身份登记。完整逐消息处置见 `核心认知.manifest.json`。",
        "",
        "## 2. 按时间顺序的核心认知原文",
        "",
    ]
    for row in units:
        metadata = {k: v for k, v in row.items() if k != "text"}
        lines.extend(
            [
                f"### {row['id']} · {row['platform']} · {row['timestamp_original']}",
                "",
                f"<!-- KC-METADATA {json.dumps(metadata, ensure_ascii=False, sort_keys=True)} -->",
                "",
                fenced_payload(str(row["text"])),
                "",
            ]
        )
    core_text = "\n".join(lines).rstrip() + "\n"
    manifest["core_document_sha256"] = sha256(core_text.encode("utf-8"))
    return manifest, core_text, json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--core", type=Path, default=Path("核心认知.md"))
    parser.add_argument("--manifest", type=Path, default=Path("核心认知.manifest.json"))
    parser.add_argument("--generation")
    parser.add_argument("--include-user-requirements", action="store_true")
    args = parser.parse_args()
    root = args.project_root.resolve()
    existing_generation = None
    existing_user_inputs = False
    if (root / args.manifest).is_file():
        try:
            existing_manifest = json.loads((root / args.manifest).read_text(encoding="utf-8"))
            existing_generation = existing_manifest.get("generation")
            existing_user_inputs = bool(existing_manifest.get("build_policy", {}).get("user_requirement_inputs"))
        except (OSError, ValueError, TypeError, AttributeError):
            existing_generation = None
    generation = args.generation or existing_generation or "core-cognition-generation-1"
    include_user_requirements = args.include_user_requirements or (args.generation is None and existing_user_inputs)
    manifest, core_text, manifest_text = build(
        root,
        generation=generation,
        include_user_requirements=include_user_requirements,
    )
    (root / args.core).write_text(core_text, encoding="utf-8")
    (root / args.manifest).write_text(manifest_text, encoding="utf-8")
    print(json.dumps({"status": "BUILT", "counts": manifest["counts"], "core_sha256": manifest["core_document_sha256"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
