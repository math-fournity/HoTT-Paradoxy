#!/usr/bin/env python3
"""Build and query a verbatim, source-traceable HoTT discussion corpus.

Raw Markdown files remain authoritative.  Every generated excerpt is a contiguous byte
slice with source SHA-256 and 1-based line boundaries.  Semantic review may add labels in
future generations, but the manager never rewrites source text or treats an excerpt as a
mathematical proof.
"""

from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


SCHEMA_VERSION = "hott-discussion-corpus/v1"
MANAGER_VERSION = "1.2.0"
DEFAULT_SOURCE_ROOTS = (
    "aistudio-docs",
    "HoTT/sources/aistudio-docs",
)
DEFAULT_OUTPUT_ROOT = "HoTT/sources/aistudio-discussions"
SOURCE_STRUCTURES = {"qa_dialogue", "prompt_response", "headed_prose", "unheaded_prose"}
PROSE_STRUCTURES = {"headed_prose", "unheaded_prose"}
SUPPORTED_MARKDOWN_SUFFIXES = {".md", ".markdown"}

ANCHORS: tuple[tuple[str, str, str], ...] = (
    ("hott", "hott", r"\bHoTT\b"),
    ("homotopy_type_theory", "hott", r"homotopy\s+type\s+theory|同伦类型论"),
    ("univalence", "univalence", r"univalence|univalent\s+foundations?|单价公理|泛等公理|泛等价公理"),
    ("hott_identity_phrase", "identity", r"等价即(?:相等|同一)|相等即路径|类型即空间|同伦同一性"),
    ("identity_type", "identity", r"identity\s+types?|path\s+induction"),
    ("higher_inductive", "higher_inductive", r"higher\s+inductive\s+types?|高阶归纳类型"),
    ("infinity_groupoid", "groupoid", r"∞[- ]?groupoid|infinity[- ]groupoid|无穷群胚"),
    ("cubical_type_theory", "variant", r"cubical\s+type\s+theory|立方类型论"),
    ("guarded_type_theory", "variant", r"guarded\s+(?:cubical\s+)?type\s+theory"),
    ("two_level_type_theory", "variant", r"two[- ]level\s+type\s+theory|2LTT"),
    ("directed_type_theory", "variant", r"directed\s+(?:homotopy\s+)?type\s+theory"),
)

CONTEXT_TAGS: tuple[tuple[str, str], ...] = (
    ("time_process", r"时间|time|temporal|动态|过程|process|Becoming|生成|先后|clock|later|stage|trace|轨迹"),
    ("history_provenance", r"历史|history|provenance|原作|复制品|数字孪生|忒修斯|来源|语境|意图|用途"),
    ("identity_equivalence", r"identity|同一|相等|equality|equivalence|等价|path|路径|transport"),
    ("resource_cost", r"资源|resource|成本|cost|耗时|runtime|复杂度|linear|线性|消耗"),
    ("self_reference", r"自指|自我指涉|self[- ]reference|反射|reflection|元理论|meta[- ]theory|固定点|fixed point|循环"),
    ("limit_zeno", r"极限|limit|芝诺|Zeno|无穷|infinite|收敛|convergen|可达|reachable"),
    ("paradox_critique", r"悖论|paradox|矛盾|contradiction|缺陷|bug|批判|攻击|不完备"),
    ("computation_proof", r"计算|computation|归约|reduction|证明|proof|type check|类型检查|停机|halting"),
    ("universe", r"宇宙|universe|resizing|predicativ|层级|hierarchy"),
)

QA_QUESTION_RE = re.compile(r"^#\s*(\d+)\.\s*问\s*$")
PROMPT_RE = re.compile(r"^##\s*Prompt:?\s*$", re.IGNORECASE)
SECTION_RE = re.compile(r"^#{1,2}\s+\S")


class CorpusError(RuntimeError):
    pass


@dataclass(frozen=True)
class SourceInstance:
    path: str
    root_id: str
    sha256: str
    size: int
    lines: int


@dataclass
class ContentGroup:
    sha256: str
    instances: list[SourceInstance]
    anchor_lines: dict[int, list[str]]
    anchor_topics: dict[str, str]
    line_count: int
    source_structure: str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_dump(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def compile_anchor_regex() -> re.Pattern[str]:
    parts = [f"(?P<{name}>{pattern})" for name, _topic, pattern in ANCHORS]
    return re.compile("|".join(parts), re.IGNORECASE)


ANCHOR_RE = compile_anchor_regex()
ANCHOR_TOPIC = {name: topic for name, topic, _pattern in ANCHORS}


def root_identity(repo_root: Path, path: Path, roots: Sequence[Path]) -> str:
    rel = path.relative_to(repo_root).as_posix()
    for root in roots:
        if path.is_relative_to(root):
            root_rel = root.relative_to(repo_root).as_posix()
            return "migrated_hott" if root_rel.startswith("HoTT/") else "aistudio_archive"
    raise CorpusError(f"source path is outside configured roots: {rel}")


def find_anchor_lines(text: str) -> tuple[dict[int, list[str]], dict[str, str]]:
    line_starts = [0]
    line_starts.extend(match.end() for match in re.finditer(r"\n", text))
    found: dict[int, set[str]] = defaultdict(set)
    for match in ANCHOR_RE.finditer(text):
        line = bisect.bisect_right(line_starts, match.start())
        if match.lastgroup:
            found[line].add(match.lastgroup)
    return ({line: sorted(names) for line, names in sorted(found.items())}, ANCHOR_TOPIC)


def classify_source_structure(lines: Sequence[str]) -> str:
    """Classify the source container without assuming every archive is a dialogue."""
    stripped = [line.rstrip("\r\n") for line in lines]
    if any(QA_QUESTION_RE.match(line) for line in stripped):
        return "qa_dialogue"
    if any(PROMPT_RE.match(line) for line in stripped):
        return "prompt_response"
    if any(SECTION_RE.match(line) for line in stripped):
        return "headed_prose"
    return "unheaded_prose"


def discover_sources(repo_root: Path, source_roots: Sequence[Path]) -> tuple[list[SourceInstance], dict[str, ContentGroup], int]:
    instances: list[SourceInstance] = []
    groups: dict[str, ContentGroup] = {}
    total_bytes = 0
    paths: list[Path] = []
    for root in source_roots:
        if not root.is_dir():
            raise CorpusError(f"missing source root: {root}")
        paths.extend(sorted(
            path for path in root.rglob("*")
            if path.is_file() and path.suffix.casefold() in SUPPORTED_MARKDOWN_SUFFIXES
        ))
    for path in sorted(set(paths), key=lambda item: item.relative_to(repo_root).as_posix()):
        data = path.read_bytes()
        digest = sha256_bytes(data)
        line_count = len(data.splitlines(keepends=True))
        rel = path.relative_to(repo_root).as_posix()
        instance = SourceInstance(
            path=rel,
            root_id=root_identity(repo_root, path, source_roots),
            sha256=digest,
            size=len(data),
            lines=line_count,
        )
        instances.append(instance)
        total_bytes += len(data)
        if digest not in groups:
            text = data.decode("utf-8", errors="replace")
            anchors, topics = find_anchor_lines(text)
            groups[digest] = ContentGroup(
                sha256=digest,
                instances=[],
                anchor_lines=anchors,
                anchor_topics=topics,
                line_count=line_count,
                source_structure=classify_source_structure(text.splitlines(keepends=True)),
            )
        groups[digest].instances.append(instance)
    return instances, groups, total_bytes


def canonical_instance(group: ContentGroup) -> SourceInstance:
    def rank(instance: SourceInstance) -> tuple[int, int, str]:
        preferred = 0 if instance.root_id == "migrated_hott" else 1
        return (preferred, len(instance.path), instance.path)
    return sorted(group.instances, key=rank)[0]


def merge_ranges(ranges: Iterable[tuple[int, int, str]], line_count: int) -> list[tuple[int, int, list[str]]]:
    normalized = sorted((max(1, start), min(line_count, end), mode) for start, end, mode in ranges if start <= end)
    merged: list[tuple[int, int, list[str]]] = []
    for start, end, mode in normalized:
        if not merged or start > merged[-1][1] + 1:
            merged.append((start, end, [mode]))
        else:
            old_start, old_end, modes = merged[-1]
            merged[-1] = (old_start, max(old_end, end), sorted(set(modes + [mode])))
    return merged


def range_contains(ranges: Sequence[tuple[int, int, Sequence[str]]], line: int) -> bool:
    return any(start <= line <= end for start, end, _mode in ranges)


def ranges_for_content(lines: Sequence[str], anchor_lines: Sequence[int], full_file_mode: str | None, adjacent_turns: int) -> list[tuple[int, int, list[str]]]:
    line_count = len(lines)
    if full_file_mode:
        return [(1, line_count, [full_file_mode])] if line_count else []
    ranges: list[tuple[int, int, str]] = []
    questions = [index + 1 for index, line in enumerate(lines) if QA_QUESTION_RE.match(line.rstrip("\r\n"))]
    if questions:
        turn_ranges = [(start, (questions[i + 1] - 1 if i + 1 < len(questions) else line_count)) for i, start in enumerate(questions)]
        selected: set[int] = set()
        for line in anchor_lines:
            idx = bisect.bisect_right(questions, line) - 1
            if idx >= 0:
                for offset in range(-adjacent_turns, adjacent_turns + 1):
                    candidate = idx + offset
                    if 0 <= candidate < len(turn_ranges):
                        selected.add(candidate)
        for idx in sorted(selected):
            ranges.append((*turn_ranges[idx], "qa_turn"))
    prompts = [index + 1 for index, line in enumerate(lines) if PROMPT_RE.match(line.rstrip("\r\n"))]
    if prompts and not questions:
        prompt_ranges = [(start, (prompts[i + 1] - 1 if i + 1 < len(prompts) else line_count)) for i, start in enumerate(prompts)]
        selected = set()
        for line in anchor_lines:
            idx = bisect.bisect_right(prompts, line) - 1
            if idx >= 0:
                for offset in range(-adjacent_turns, adjacent_turns + 1):
                    candidate = idx + offset
                    if 0 <= candidate < len(prompt_ranges):
                        selected.add(candidate)
        for idx in sorted(selected):
            ranges.append((*prompt_ranges[idx], "prompt_turn"))
    provisional = merge_ranges(ranges, line_count)
    uncovered = [line for line in anchor_lines if not range_contains(provisional, line)]
    if uncovered:
        headings = [index + 1 for index, line in enumerate(lines) if SECTION_RE.match(line.rstrip("\r\n"))]
        for line in uncovered:
            idx = bisect.bisect_right(headings, line) - 1
            if idx >= 0:
                start = headings[idx]
                end = headings[idx + 1] - 1 if idx + 1 < len(headings) else line_count
                ranges.append((start, end, "heading_section"))
            else:
                ranges.append((line - 40, line + 40, "context_window"))
    provisional = merge_ranges(ranges, line_count)
    uncovered = [line for line in anchor_lines if not range_contains(provisional, line)]
    for line in uncovered:
        ranges.append((line - 40, line + 40, "context_window"))
    return merge_ranges(ranges, line_count)


def context_tags(text: str) -> list[str]:
    return sorted(name for name, pattern in CONTEXT_TAGS if re.search(pattern, text, re.IGNORECASE))


def snapshot_id(instances: Sequence[SourceInstance], adjacent_turns: int) -> str:
    payload = {
        "schema": SCHEMA_VERSION,
        "manager": MANAGER_VERSION,
        "adjacent_turns": adjacent_turns,
        "sources": [(item.path, item.sha256, item.size) for item in sorted(instances, key=lambda row: row.path)],
    }
    return hashlib.sha256(json_dump(payload).encode("utf-8")).hexdigest()[:20]


def make_entry(repo_root: Path, group: ContentGroup, source: SourceInstance, lines_bytes: Sequence[bytes], lines_text: Sequence[str], start: int, end: int, modes: Sequence[str]) -> tuple[dict[str, object], bytes]:
    selected_anchor_lines = {
        str(line): names for line, names in group.anchor_lines.items() if start <= line <= end
    }
    counts: Counter[str] = Counter()
    for names in selected_anchor_lines.values():
        counts.update(names)
    topics = sorted({ANCHOR_TOPIC[name] for name in counts})
    verbatim = b"".join(lines_bytes[start - 1 : end])
    seed = f"{SCHEMA_VERSION}\0{group.sha256}\0{start}\0{end}".encode("utf-8")
    entry_id = "HOTT-DISC-" + hashlib.sha256(seed).hexdigest()[:16].upper()
    excerpt_path = f"excerpts/{entry_id}.md"
    entry: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "id": entry_id,
        "source_path": source.path,
        "source_instances": [item.path for item in sorted(group.instances, key=lambda row: row.path)],
        "source_root_id": source.root_id,
        "source_structure": group.source_structure,
        "source_sha256": group.sha256,
        "source_bytes": source.size,
        "source_lines": source.lines,
        "duplicate_source_count": len(group.instances),
        "line_start": start,
        "line_end": end,
        "captured_lines": end - start + 1,
        "extraction_modes": sorted(modes),
        "anchor_counts": dict(sorted(counts.items())),
        "anchor_match_lines": {key: value for key, value in selected_anchor_lines.items()},
        "topic_tags": topics,
        "context_tags": context_tags("".join(lines_text[start - 1 : end])),
        "review_status": "UNREVIEWED_RAW_CAPTURE",
        "excerpt_path": excerpt_path,
        "verbatim_bytes": len(verbatim),
        "verbatim_sha256": sha256_bytes(verbatim),
        "manager_version": MANAGER_VERSION,
    }
    header = (
        "<!--\n"
        "machine_managed: true\n"
        f"schema_version: {SCHEMA_VERSION}\n"
        f"id: {entry_id}\n"
        f"source_path: {source.path}\n"
        f"source_sha256: {group.sha256}\n"
        f"source_line_range: {start}-{end}\n"
        "review_status: UNREVIEWED_RAW_CAPTURE\n"
        "canonical_manager: HoTT/tools/hott_discussion_corpus.py\n"
        "-->\n\n"
        f"# HoTT discussion excerpt {entry_id}\n\n"
        f"- Source: `{source.path}`\n"
        f"- Source instances: {len(group.instances)}\n"
        f"- Source structure: `{group.source_structure}`\n"
        f"- Source lines: `{start}-{end}`\n"
        f"- Extraction modes: `{', '.join(sorted(modes))}`\n"
        f"- Anchor topics: `{', '.join(topics)}`\n"
        "- Status: `UNREVIEWED_RAW_CAPTURE`\n\n"
        "The following bytes are a contiguous source slice. They are evidence of what the source discussed, not proof that its claims are true.\n\n"
        "<!-- BEGIN VERBATIM -->\n"
    ).encode("utf-8")
    footer_prefix = b"" if verbatim.endswith(b"\n") or not verbatim else b"\n"
    excerpt = header + verbatim + footer_prefix + b"<!-- END VERBATIM -->\n"
    entry["excerpt_sha256"] = sha256_bytes(excerpt)
    return entry, excerpt


def build_entries(repo_root: Path, groups: dict[str, ContentGroup], adjacent_turns: int) -> tuple[list[dict[str, object]], dict[str, bytes], Counter[str]]:
    entries: list[dict[str, object]] = []
    excerpts: dict[str, bytes] = {}
    mode_counts: Counter[str] = Counter()
    for digest, group in sorted(groups.items()):
        if not group.anchor_lines:
            continue
        source = canonical_instance(group)
        data = (repo_root / source.path).read_bytes()
        lines_bytes = data.splitlines(keepends=True)
        lines_text = [line.decode("utf-8", errors="replace") for line in lines_bytes]
        if any(instance.root_id == "migrated_hott" for instance in group.instances):
            full_file_mode = "full_migrated_source"
        elif group.source_structure in {"headed_prose", "unheaded_prose"}:
            full_file_mode = "full_non_qa_source"
        else:
            full_file_mode = None
        ranges = ranges_for_content(lines_text, sorted(group.anchor_lines), full_file_mode, adjacent_turns)
        for start, end, modes in ranges:
            entry, excerpt = make_entry(repo_root, group, source, lines_bytes, lines_text, start, end, modes)
            entries.append(entry)
            excerpts[str(entry["excerpt_path"])] = excerpt
            mode_counts.update(modes)
    entries.sort(key=lambda row: (str(row["source_path"]), int(row["line_start"]), str(row["id"])))
    return entries, excerpts, mode_counts


def inventory_rows(instances: Sequence[SourceInstance], groups: dict[str, ContentGroup]) -> list[dict[str, object]]:
    canonical_by_sha = {digest: canonical_instance(group).path for digest, group in groups.items()}
    return [
        {
            "schema_version": SCHEMA_VERSION,
            "path": item.path,
            "root_id": item.root_id,
            "source_structure": groups[item.sha256].source_structure,
            "sha256": item.sha256,
            "bytes": item.size,
            "lines": item.lines,
            "canonical_content_path": canonical_by_sha[item.sha256],
            "duplicate_source_count": len(groups[item.sha256].instances),
            "candidate": bool(groups[item.sha256].anchor_lines),
            "anchor_match_count": sum(len(names) for names in groups[item.sha256].anchor_lines.values()),
        }
        for item in sorted(instances, key=lambda row: row.path)
    ]


def percentile(sorted_values: Sequence[int], fraction: float) -> int:
    if not sorted_values:
        return 0
    index = round((len(sorted_values) - 1) * fraction)
    return sorted_values[index]


def statistics(instances: Sequence[SourceInstance], groups: dict[str, ContentGroup], entries: Sequence[dict[str, object]], total_bytes: int, generation: str, adjacent_turns: int, mode_counts: Counter[str]) -> dict[str, object]:
    candidate_groups = [group for group in groups.values() if group.anchor_lines]
    candidate_paths = sum(len(group.instances) for group in candidate_groups)
    captured_lines = sum(int(entry["captured_lines"]) for entry in entries)
    captured_bytes = sum(int(entry["verbatim_bytes"]) for entry in entries)
    unique_candidate_lines = sum(group.line_count for group in candidate_groups)
    unique_candidate_bytes = sum(canonical_instance(group).size for group in candidate_groups)
    all_structure_counts: Counter[str] = Counter()
    candidate_structure_counts: Counter[str] = Counter()
    candidate_unique_structure_counts: Counter[str] = Counter()
    for group in groups.values():
        all_structure_counts[group.source_structure] += len(group.instances)
        if group.anchor_lines:
            candidate_structure_counts[group.source_structure] += len(group.instances)
            candidate_unique_structure_counts[group.source_structure] += 1
    excerpt_structure_counts = Counter(str(entry["source_structure"]) for entry in entries)
    excerpt_sizes = sorted(int(entry["verbatim_bytes"]) for entry in entries)
    largest_entry = max(entries, key=lambda entry: int(entry["verbatim_bytes"]), default=None)
    anchor_counts: Counter[str] = Counter()
    topic_counts: Counter[str] = Counter()
    for entry in entries:
        anchor_counts.update({str(key): int(value) for key, value in dict(entry["anchor_counts"]).items()})
        topic_counts.update(str(value) for value in list(entry["topic_tags"]))
    return {
        "schema_version": SCHEMA_VERSION,
        "manager_version": MANAGER_VERSION,
        "generation_id": generation,
        "adjacent_turns": adjacent_turns,
        "source_files": len(instances),
        "source_bytes": total_bytes,
        "unique_source_contents": len(groups),
        "duplicate_content_groups": sum(1 for group in groups.values() if len(group.instances) > 1),
        "candidate_source_files": candidate_paths,
        "unique_candidate_contents": len(candidate_groups),
        "candidate_source_lines": unique_candidate_lines,
        "unique_candidate_source_bytes": unique_candidate_bytes,
        "excerpt_count": len(entries),
        "captured_source_lines": captured_lines,
        "captured_verbatim_bytes": captured_bytes,
        "captured_candidate_line_ratio": round(captured_lines / unique_candidate_lines, 6) if unique_candidate_lines else 0,
        "captured_candidate_byte_ratio": round(captured_bytes / unique_candidate_bytes, 6) if unique_candidate_bytes else 0,
        "all_source_structure_counts": dict(sorted(all_structure_counts.items())),
        "candidate_source_structure_counts": dict(sorted(candidate_structure_counts.items())),
        "candidate_unique_structure_counts": dict(sorted(candidate_unique_structure_counts.items())),
        "excerpt_source_structure_counts": dict(sorted(excerpt_structure_counts.items())),
        "non_qa_source_files": len(instances) - all_structure_counts["qa_dialogue"],
        "non_qa_candidate_source_files": candidate_paths - candidate_structure_counts["qa_dialogue"],
        "non_qa_excerpt_count": len(entries) - excerpt_structure_counts["qa_dialogue"],
        "excerpt_verbatim_bytes_distribution": {
            "min": excerpt_sizes[0] if excerpt_sizes else 0,
            "p50": percentile(excerpt_sizes, 0.50),
            "p90": percentile(excerpt_sizes, 0.90),
            "p99": percentile(excerpt_sizes, 0.99),
            "max": excerpt_sizes[-1] if excerpt_sizes else 0,
        },
        "largest_excerpt": ({
            "id": largest_entry["id"],
            "source_path": largest_entry["source_path"],
            "line_start": largest_entry["line_start"],
            "line_end": largest_entry["line_end"],
            "verbatim_bytes": largest_entry["verbatim_bytes"],
        } if largest_entry else None),
        "full_file_excerpt_count": sum(any(str(mode).startswith("full_") for mode in list(entry["extraction_modes"])) for entry in entries),
        "full_migrated_source_excerpt_count": sum("full_migrated_source" in list(entry["extraction_modes"]) for entry in entries),
        "full_non_qa_source_excerpt_count": sum("full_non_qa_source" in list(entry["extraction_modes"]) for entry in entries),
        "mode_counts": dict(sorted(mode_counts.items())),
        "anchor_counts": dict(sorted(anchor_counts.items())),
        "topic_counts": dict(sorted(topic_counts.items())),
        "review_status": "UNREVIEWED_RAW_CAPTURE",
    }


def render_index(stats: dict[str, object], entries: Sequence[dict[str, object]]) -> str:
    lines = [
        "# HoTT discussion corpus — current generation",
        "",
        "<!-- MACHINE_MANAGED_DERIVED: edit via HoTT/tools/hott_discussion_corpus.py -->",
        "",
        f"- Schema: `{SCHEMA_VERSION}`",
        f"- Manager: `{MANAGER_VERSION}`",
        f"- Generation: `{stats['generation_id']}`",
        f"- Source files scanned: `{stats['source_files']}`",
        f"- Candidate source files: `{stats['candidate_source_files']}`",
        f"- Unique candidate contents: `{stats['unique_candidate_contents']}`",
        f"- Candidate Q/A sources: `{dict(stats['candidate_source_structure_counts']).get('qa_dialogue', 0)}`",
        f"- Candidate non-Q/A sources: `{stats['non_qa_candidate_source_files']}`",
        f"- Verbatim excerpts: `{stats['excerpt_count']}`",
        f"- Non-Q/A-source excerpts: `{stats['non_qa_excerpt_count']}`",
        f"- Captured source lines: `{stats['captured_source_lines']}`",
        f"- Captured verbatim bytes: `{stats['captured_verbatim_bytes']}`",
        "- Review status: `UNREVIEWED_RAW_CAPTURE`",
        "",
        "This index is a high-recall verbatim view. Inclusion proves only that an anchor matched; semantic labels must never delete raw captures.",
        "",
        "| ID | Source | Structure | Lines | Modes | Topics | Excerpt |",
        "|---|---|---|---:|---|---|---|",
    ]
    for entry in entries:
        source = str(entry["source_path"]).replace("|", "\\|")
        modes = ", ".join(str(x) for x in list(entry["extraction_modes"]))
        topics = ", ".join(str(x) for x in list(entry["topic_tags"]))
        lines.append(
            f"| `{entry['id']}` | `{source}` | {entry['source_structure']} | {entry['line_start']}-{entry['line_end']} | {modes} | {topics} | [open]({entry['excerpt_path']}) |"
        )
    lines.append("")
    return "\n".join(lines)


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


class BuildLock:
    def __init__(self, output_root: Path) -> None:
        self.path = output_root / ".build.lock"
        self.fd: int | None = None

    def __enter__(self) -> "BuildLock":
        self.path.parent.mkdir(parents=True, exist_ok=True)
        try:
            self.fd = os.open(self.path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
        except FileExistsError as exc:
            raise CorpusError(f"build lock exists: {self.path}") from exc
        os.write(self.fd, f"pid={os.getpid()}\n".encode())
        return self

    def __exit__(self, _exc_type: object, _exc: object, _tb: object) -> None:
        if self.fd is not None:
            os.close(self.fd)
        try:
            self.path.unlink()
        except FileNotFoundError:
            pass


def scan(repo_root: Path, source_roots: Sequence[Path], adjacent_turns: int) -> tuple[list[SourceInstance], dict[str, ContentGroup], list[dict[str, object]], dict[str, bytes], dict[str, object], list[dict[str, object]]]:
    instances, groups, total_bytes = discover_sources(repo_root, source_roots)
    generation = snapshot_id(instances, adjacent_turns)
    entries, excerpts, mode_counts = build_entries(repo_root, groups, adjacent_turns)
    stats = statistics(instances, groups, entries, total_bytes, generation, adjacent_turns, mode_counts)
    inventory = inventory_rows(instances, groups)
    return instances, groups, entries, excerpts, stats, inventory


def write_jsonl(path: Path, rows: Sequence[dict[str, object]]) -> None:
    body = "".join(json_dump(row) + "\n" for row in rows).encode("utf-8")
    atomic_write(path, body)


def build(repo_root: Path, source_roots: Sequence[Path], output_root: Path, adjacent_turns: int, dry_run: bool) -> dict[str, object]:
    _instances, _groups, entries, excerpts, stats, inventory = scan(repo_root, source_roots, adjacent_turns)
    if dry_run:
        print(json.dumps(stats, ensure_ascii=False, indent=2, sort_keys=True))
        return stats
    generation = str(stats["generation_id"])
    generations_root = output_root / "generations"
    target = generations_root / generation
    with BuildLock(output_root):
        if not target.exists():
            generations_root.mkdir(parents=True, exist_ok=True)
            temp = Path(tempfile.mkdtemp(prefix=f".{generation}.", dir=generations_root))
            try:
                (temp / "excerpts").mkdir(parents=True)
                for rel, data in sorted(excerpts.items()):
                    path = temp / rel
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(data)
                write_jsonl(temp / "manifest.jsonl", entries)
                write_jsonl(temp / "source_inventory.jsonl", inventory)
                atomic_write(temp / "STATS.json", (json.dumps(stats, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8"))
                atomic_write(temp / "INDEX.md", render_index(stats, entries).encode("utf-8"))
                os.replace(temp, target)
            except Exception:
                shutil.rmtree(temp, ignore_errors=True)
                raise
        atomic_write(output_root / "CURRENT", (generation + "\n").encode("utf-8"))
    print(json.dumps(stats, ensure_ascii=False, indent=2, sort_keys=True))
    return stats


def current_generation(output_root: Path) -> Path:
    current = output_root / "CURRENT"
    if not current.is_file():
        raise CorpusError(f"missing CURRENT pointer: {current}")
    generation = current.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[0-9a-f]{20}", generation):
        raise CorpusError(f"invalid CURRENT generation id: {generation!r}")
    path = output_root / "generations" / generation
    if not path.is_dir():
        raise CorpusError(f"CURRENT generation is missing: {path}")
    return path


def load_jsonl(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open(encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise CorpusError(f"invalid JSONL at {path}:{number}: {exc}") from exc
            if not isinstance(row, dict):
                raise CorpusError(f"non-object JSONL row at {path}:{number}")
            rows.append(row)
    return rows


def validate(repo_root: Path, source_roots: Sequence[Path], output_root: Path, fast: bool) -> dict[str, object]:
    generation = current_generation(output_root)
    manifest = load_jsonl(generation / "manifest.jsonl")
    inventory = load_jsonl(generation / "source_inventory.jsonl")
    stats = json.loads((generation / "STATS.json").read_text(encoding="utf-8"))
    required_manifest_fields = {
        "schema_version", "id", "source_path", "source_instances", "source_root_id",
        "source_structure", "source_sha256", "source_bytes", "source_lines",
        "duplicate_source_count", "line_start", "line_end", "captured_lines",
        "extraction_modes", "anchor_counts", "anchor_match_lines", "topic_tags",
        "context_tags", "review_status", "excerpt_path", "verbatim_bytes",
        "verbatim_sha256", "excerpt_sha256", "manager_version",
    }
    if stats.get("schema_version") != SCHEMA_VERSION or stats.get("generation_id") != generation.name:
        raise CorpusError("STATS schema or generation mismatch")
    inventory_paths = [str(row.get("path")) for row in inventory]
    if inventory_paths != sorted(inventory_paths) or len(inventory_paths) != len(set(inventory_paths)):
        raise CorpusError("source inventory is not uniquely and deterministically sorted")
    all_structure_counts = Counter(str(row.get("source_structure")) for row in inventory)
    candidate_inventory = [row for row in inventory if bool(row.get("candidate"))]
    candidate_structure_counts = Counter(str(row.get("source_structure")) for row in candidate_inventory)
    if any(structure not in SOURCE_STRUCTURES for structure in all_structure_counts):
        raise CorpusError("unknown source structure in inventory")
    if dict(sorted(all_structure_counts.items())) != stats.get("all_source_structure_counts"):
        raise CorpusError("all-source structure statistics mismatch")
    if dict(sorted(candidate_structure_counts.items())) != stats.get("candidate_source_structure_counts"):
        raise CorpusError("candidate-source structure statistics mismatch")
    if len(inventory) - all_structure_counts["qa_dialogue"] != int(stats.get("non_qa_source_files", -1)):
        raise CorpusError("non-Q/A source count mismatch")
    if len(candidate_inventory) - candidate_structure_counts["qa_dialogue"] != int(stats.get("non_qa_candidate_source_files", -1)):
        raise CorpusError("non-Q/A candidate source count mismatch")
    ids = [str(row.get("id")) for row in manifest]
    if len(ids) != len(set(ids)):
        raise CorpusError("duplicate excerpt IDs")
    if ids != [str(row["id"]) for row in sorted(manifest, key=lambda row: (str(row["source_path"]), int(row["line_start"]), str(row["id"])))]:
        raise CorpusError("manifest is not deterministically sorted")
    expected_excerpt_paths = {str(row["excerpt_path"]) for row in manifest}
    actual_excerpt_paths = {path.relative_to(generation).as_posix() for path in (generation / "excerpts").glob("*.md")}
    if expected_excerpt_paths != actual_excerpt_paths:
        raise CorpusError(f"excerpt path mismatch: missing={sorted(expected_excerpt_paths-actual_excerpt_paths)[:10]} orphan={sorted(actual_excerpt_paths-expected_excerpt_paths)[:10]}")
    by_source: dict[str, list[tuple[int, int]]] = defaultdict(list)
    cached_source_path: Path | None = None
    cached_data = b""
    cached_lines: list[bytes] = []
    cached_digest = ""
    last_end_by_sha: dict[str, int] = {}
    for row in manifest:
        missing_fields = required_manifest_fields - set(row)
        if missing_fields:
            raise CorpusError(f"manifest row missing fields {sorted(missing_fields)}: {row.get('id')}")
        if row["schema_version"] != SCHEMA_VERSION or row["review_status"] != "UNREVIEWED_RAW_CAPTURE":
            raise CorpusError(f"invalid schema/review status: {row['id']}")
        if str(row["source_structure"]) not in SOURCE_STRUCTURES:
            raise CorpusError(f"invalid source structure: {row['id']}")
        source_rel = Path(str(row["source_path"]))
        source_path = (repo_root / source_rel).resolve()
        if source_rel.is_absolute() or not source_path.is_relative_to(repo_root) or not any(source_path.is_relative_to(root) for root in source_roots):
            raise CorpusError(f"source path escapes configured roots: {row['source_path']}")
        if not source_path.is_file():
            raise CorpusError(f"missing source: {source_path}")
        if cached_source_path != source_path:
            cached_source_path = source_path
            cached_data = source_path.read_bytes()
            cached_lines = cached_data.splitlines(keepends=True)
            cached_digest = sha256_bytes(cached_data)
            if cached_digest != row["source_sha256"]:
                raise CorpusError(f"source SHA changed: {source_path}")
        elif cached_digest != row["source_sha256"]:
            raise CorpusError(f"inconsistent source SHA in manifest: {source_path}")
        start, end = int(row["line_start"]), int(row["line_end"])
        if start < 1 or end < start or end > len(cached_lines) or int(row["captured_lines"]) != end - start + 1:
            raise CorpusError(f"invalid source line range: {row['id']}")
        expected_full_mode = None
        if row["source_root_id"] == "migrated_hott":
            expected_full_mode = "full_migrated_source"
        elif str(row["source_structure"]) in PROSE_STRUCTURES:
            expected_full_mode = "full_non_qa_source"
        if expected_full_mode and (
            list(row["extraction_modes"]) != [expected_full_mode]
            or start != 1
            or end != int(row["source_lines"])
            or int(row["verbatim_bytes"]) != int(row["source_bytes"])
        ):
            raise CorpusError(f"required full-source capture is incomplete: {row['id']}")
        source_digest = str(row["source_sha256"])
        if start <= last_end_by_sha.get(source_digest, 0):
            raise CorpusError(f"overlapping source ranges: {row['id']}")
        last_end_by_sha[source_digest] = end
        expected_id = "HOTT-DISC-" + hashlib.sha256(f"{SCHEMA_VERSION}\0{source_digest}\0{start}\0{end}".encode("utf-8")).hexdigest()[:16].upper()
        if row["id"] != expected_id or row["excerpt_path"] != f"excerpts/{expected_id}.md":
            raise CorpusError(f"non-deterministic excerpt identity: {row['id']}")
        verbatim = b"".join(cached_lines[start - 1 : end])
        if sha256_bytes(verbatim) != row["verbatim_sha256"] or len(verbatim) != int(row["verbatim_bytes"]):
            raise CorpusError(f"verbatim source slice mismatch: {row['id']}")
        excerpt_path = generation / str(row["excerpt_path"])
        excerpt = excerpt_path.read_bytes()
        if sha256_bytes(excerpt) != row["excerpt_sha256"]:
            raise CorpusError(f"excerpt SHA mismatch: {excerpt_path}")
        marker = b"<!-- BEGIN VERBATIM -->\n"
        offset = excerpt.find(marker)
        if offset < 0:
            raise CorpusError(f"missing verbatim marker: {excerpt_path}")
        captured = excerpt[offset + len(marker) : offset + len(marker) + int(row["verbatim_bytes"])]
        if captured != verbatim:
            raise CorpusError(f"excerpt is not exact source bytes: {excerpt_path}")
        by_source[source_digest].append((start, end))
    excerpt_structure_counts = Counter(str(row["source_structure"]) for row in manifest)
    persisted_mode_counts = Counter(str(mode) for row in manifest for mode in list(row["extraction_modes"]))
    if dict(sorted(excerpt_structure_counts.items())) != stats.get("excerpt_source_structure_counts"):
        raise CorpusError("excerpt source-structure statistics mismatch")
    if len(manifest) - excerpt_structure_counts["qa_dialogue"] != int(stats.get("non_qa_excerpt_count", -1)):
        raise CorpusError("non-Q/A excerpt count mismatch")
    if dict(sorted(persisted_mode_counts.items())) != stats.get("mode_counts"):
        raise CorpusError("extraction-mode statistics mismatch")
    if persisted_mode_counts["full_migrated_source"] != int(stats.get("full_migrated_source_excerpt_count", -1)):
        raise CorpusError("migrated full-source count mismatch")
    if persisted_mode_counts["full_non_qa_source"] != int(stats.get("full_non_qa_source_excerpt_count", -1)):
        raise CorpusError("non-Q/A full-source count mismatch")
    if len(manifest) != int(stats.get("excerpt_count", -1)):
        raise CorpusError("excerpt count mismatch")
    if sum(int(row["captured_lines"]) for row in manifest) != int(stats.get("captured_source_lines", -1)):
        raise CorpusError("captured line statistics mismatch")
    if sum(int(row["verbatim_bytes"]) for row in manifest) != int(stats.get("captured_verbatim_bytes", -1)):
        raise CorpusError("captured byte statistics mismatch")
    if len(inventory) != int(stats.get("source_files", -1)) or len(candidate_inventory) != int(stats.get("candidate_source_files", -1)):
        raise CorpusError("source inventory statistics mismatch")
    if sum(int(row["bytes"]) for row in inventory) != int(stats.get("source_bytes", -1)):
        raise CorpusError("source byte statistics mismatch")
    if not fast:
        current_instances, current_groups, _total = discover_sources(repo_root, source_roots)
        if inventory != inventory_rows(current_instances, current_groups):
            raise CorpusError("source inventory drifted; rebuild required")
        for digest, group in current_groups.items():
            if not group.anchor_lines:
                continue
            ranges = by_source.get(digest, [])
            uncovered = [line for line in group.anchor_lines if not any(start <= line <= end for start, end in ranges)]
            if uncovered:
                raise CorpusError(f"uncovered anchor lines for {canonical_instance(group).path}: {uncovered[:20]}")
    result = {
        "status": "PASS",
        "schema_version": SCHEMA_VERSION,
        "generation_id": generation.name,
        "manifest_rows": len(manifest),
        "inventory_rows": len(inventory),
        "fast": fast,
        "source_files": stats.get("source_files"),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return result


def query(output_root: Path, args: argparse.Namespace) -> None:
    generation = current_generation(output_root)
    rows = load_jsonl(generation / "manifest.jsonl")
    selected: list[dict[str, object]] = []
    for row in rows:
        if args.id and str(row["id"]) != args.id:
            continue
        if args.source and args.source.casefold() not in str(row["source_path"]).casefold():
            continue
        if args.structure and str(row["source_structure"]) != args.structure:
            continue
        if args.topic and args.topic not in list(row["topic_tags"]) and args.topic not in list(row["context_tags"]):
            continue
        if args.anchor and args.anchor not in dict(row["anchor_counts"]):
            continue
        selected.append(row)
        if len(selected) >= args.limit:
            break
    if args.json:
        print(json.dumps(selected, ensure_ascii=False, indent=2, sort_keys=True))
        return
    for row in selected:
        print(f"{row['id']}\t{row['source_structure']}\t{row['source_path']}:{row['line_start']}-{row['line_end']}\t{','.join(row['topic_tags'])}\t{generation / str(row['excerpt_path'])}")


def show_stats(output_root: Path) -> None:
    generation = current_generation(output_root)
    print((generation / "STATS.json").read_text(encoding="utf-8"), end="")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=None, help="repository root; defaults to script/../..")
    parser.add_argument("--source-root", action="append", default=[], help="project-relative source root; repeatable")
    parser.add_argument("--output-root", default=DEFAULT_OUTPUT_ROOT, help="project-relative derived corpus root")
    parser.add_argument("--adjacent-turns", type=int, default=1, help="whole Q/A turns retained before/after a matching turn")
    sub = parser.add_subparsers(dest="command", required=True)
    scan_cmd = sub.add_parser("scan", help="read-only high-recall scan and expected corpus statistics")
    scan_cmd.add_argument("--json", action="store_true", help="reserved; scan output is JSON")
    build_cmd = sub.add_parser("build", help="build an immutable generation and update CURRENT")
    build_cmd.add_argument("--dry-run", action="store_true", help="compute statistics without writing")
    validate_cmd = sub.add_parser("validate", help="validate CURRENT against sources and exact verbatim bytes")
    validate_cmd.add_argument("--fast", action="store_true", help="skip full source inventory and anchor coverage rescan")
    sub.add_parser("stats", help="print CURRENT STATS.json")
    query_cmd = sub.add_parser("query", help="query CURRENT manifest")
    query_cmd.add_argument("--id")
    query_cmd.add_argument("--source")
    query_cmd.add_argument("--structure", choices=sorted(SOURCE_STRUCTURES))
    query_cmd.add_argument("--topic")
    query_cmd.add_argument("--anchor")
    query_cmd.add_argument("--limit", type=int, default=50)
    query_cmd.add_argument("--json", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    script_root = Path(__file__).resolve().parents[2]
    repo_root = Path(args.repo_root).resolve() if args.repo_root else script_root
    source_root_values = args.source_root or list(DEFAULT_SOURCE_ROOTS)
    source_roots = [(repo_root / value).resolve() for value in source_root_values]
    output_root = (repo_root / args.output_root).resolve()
    if args.adjacent_turns < 0:
        parser.error("--adjacent-turns must be nonnegative")
    try:
        if args.command == "scan":
            _instances, _groups, _entries, _excerpts, stats, _inventory = scan(repo_root, source_roots, args.adjacent_turns)
            print(json.dumps(stats, ensure_ascii=False, indent=2, sort_keys=True))
        elif args.command == "build":
            build(repo_root, source_roots, output_root, args.adjacent_turns, args.dry_run)
        elif args.command == "validate":
            validate(repo_root, source_roots, output_root, args.fast)
        elif args.command == "stats":
            show_stats(output_root)
        elif args.command == "query":
            query(output_root, args)
        else:
            parser.error(f"unknown command: {args.command}")
    except CorpusError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
