

===== SOURCE scripts/recovered/14dfd1f5313ea9b792a6/hott_discussion_corpus.py | SHA256 14dfd1f5313ea9b792a6ae9335f3f38a840e61e8c45a2ec6a3b95d53e841e06f | LINES 1-848/848 =====
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

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/21f9dfe3db9017beb8f6/IntentRole.agda | SHA256 21f9dfe3db9017beb8f6e7e3c5aa5c586a4812aecc460d59624fbbf44503ea07 | LINES 1-31/31 =====
module IntentRole where

open import Agda.Builtin.Equality using (_≡_; refl)

data ⊥ : Set where
¬_ : Set → Set
¬ A = A → ⊥
_≢_ : {A : Set} → A → A → Set
x ≢ y = ¬ (x ≡ y)

data Bit : Set where b0 b1 : Bit
neq01 : b0 ≢ b1
neq01 ()

data Unit : Set where unit : Unit

sym : {A : Set} {x y : A} → x ≡ y → y ≡ x
sym refl = refl
trans : {A : Set} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl q = q


bareRepresentation : Bit → Unit
bareRepresentation _ = unit
role : Bit → Bit
role r = r

bareTypeCannotRecoverRole :
  (decode : Unit → Bit) → ¬ ((r : Bit) → decode (bareRepresentation r) ≡ role r)
bareTypeCannotRecoverRole decode exact =
  neq01 (trans (sym (exact b0)) (exact b1))

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/2268b955e7011f715d3b/preflight.sh | SHA256 2268b955e7011f715d3b5028da7cf3046d32e6562358a6a1cc5b7f917a63b9d3 | LINES 1-11/11 =====
#!/usr/bin/env bash
set +e
OUT="$(cd "$(dirname "$0")" && pwd)/build/preflight.log"
mkdir -p "$(dirname "$OUT")"
: > "$OUT"
for x in agda ghc cabal lean lake coqc rocq rzk git python3; do
  printf '%-10s ' "$x" | tee -a "$OUT"
  command -v "$x" 2>&1 | tee -a "$OUT"
done
printf 'timestamp_utc=' | tee -a "$OUT"; date -u +%Y-%m-%dT%H:%M:%SZ | tee -a "$OUT"
exit 0

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/272ac9514bfcbde7a1b7/WalkingArrowCore.agda | SHA256 272ac9514bfcbde7a1b7d40c6d809ca9c3dacbd4ce66d00fd0c188ed20aee58e | LINES 1-36/36 =====
module WalkingArrowCore where

open import Agda.Builtin.Equality using (_≡_; refl)

data ⊥ : Set where
¬_ : Set → Set
¬ A = A → ⊥
_≢_ : {A : Set} → A → A → Set
x ≢ y = ¬ (x ≡ y)

data Bit : Set where b0 b1 : Bit
neq01 : b0 ≢ b1
neq01 ()

data Unit : Set where unit : Unit

sym : {A : Set} {x y : A} → x ≡ y → y ≡ x
sym refl = refl
trans : {A : Set} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl q = q


data ProcessWorld : Set where forward backward : ProcessWorld

-- The invertible-arrow core forgets which nonidentity directed arrow exists.
core : ProcessWorld → Unit
core _ = unit

direction : ProcessWorld → Bit
direction forward = b0
direction backward = b1

coreCannotRecoverDirection :
  (decode : Unit → Bit) → ¬ ((w : ProcessWorld) → decode (core w) ≡ direction w)
coreCannotRecoverDirection decode exact =
  neq01 (trans (sym (exact forward)) (exact backward))

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/2799cbbbb0b3f1afd1b4/provenance_factorization_check.py | SHA256 2799cbbbb0b3f1afd1b4bff72e71ad132a4e180de4c82ad5be047837c99b15b3 | LINES 1-65/65 =====
#!/usr/bin/env python3
"""Finite sanity checks for the history/provenance Z-factorization theorem.

This script is not an unbounded formal proof. It exhaustively checks the smallest
finite model used in the paper:
  History = Snapshot × {original, replica}
and confirms that IsOriginal does not factor through the snapshot projection,
while it does factor through the enriched identity representation.
"""
from __future__ import annotations

from itertools import product
from typing import Dict, Hashable, Iterable, Tuple

History = Tuple[str, str]


def all_boolean_functions(domain: Iterable[Hashable]):
    domain = tuple(domain)
    for values in product((False, True), repeat=len(domain)):
        yield dict(zip(domain, values))


def main() -> None:
    snapshots = ("same-current-structure",)
    provenances = ("original", "replica")
    histories: Tuple[History, ...] = tuple(product(snapshots, provenances))

    coarse = {h: h[0] for h in histories}
    fine = {h: h for h in histories}
    is_original = {h: h[1] == "original" for h in histories}

    coarse_factorizations = []
    for predictor in all_boolean_functions(snapshots):
        if all(predictor[coarse[h]] == is_original[h] for h in histories):
            coarse_factorizations.append(predictor)

    # The enriched representation has the obvious predictor.
    fine_predictor: Dict[History, bool] = {h: is_original[h] for h in histories}
    fine_factors = all(fine_predictor[fine[h]] == is_original[h] for h in histories)

    # Exhaustively test whether the non-injective coarse map has a left inverse.
    # A candidate beta maps the single snapshot back to one of the two histories.
    left_inverses = []
    for chosen in histories:
        beta = {snapshots[0]: chosen}
        if all(beta[coarse[h]] == h for h in histories):
            left_inverses.append(beta)

    print("Finite provenance factorization sanity check")
    print("Histories:", histories)
    print("Coarse fibers:", {s: [h for h in histories if coarse[h] == s] for s in snapshots})
    print("IsOriginal values:", is_original)
    print("Coarse factorization count:", len(coarse_factorizations))
    print("Fine representation factors:", fine_factors)
    print("Exact left inverse count for coarse abstraction:", len(left_inverses))

    assert len(coarse_factorizations) == 0
    assert fine_factors
    assert len(left_inverses) == 0
    print("PASS: provenance is not recoverable from the coarse snapshot, but is recoverable after enrichment.")


if __name__ == "__main__":
    main()

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/2943a809821477f1197c/guard-erasure-implies-fixed-point.agda | SHA256 2943a809821477f1197c640fd39dcda12f1e0dbb084bd07cfda6d5bebb885da5 | LINES 1-15/15 =====
module guard-erasure-implies-fixed-point where

open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.universe-levels

-- A time-indexed orbit can collapse to one state while preserving its update
-- law only by supplying a fixed point of F.
Guard-Erasure : {l : Level} (X : UU l) (F : X → X) → UU l
Guard-Erasure X F = Σ X (λ c → c ＝ F c)

fixed-point-guard-erasure :
  {l : Level} {X : UU l} {F : X → X} →
  Guard-Erasure X F → Σ X (λ c → c ＝ F c)
fixed-point-guard-erasure e = e

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/30897b629eb87d98db20/round3_semantic_operational_model_check.py | SHA256 30897b629eb87d98db20133c6897d7a438f12c677683db9eacdb27e9583953b8 | LINES 1-88/88 =====
#!/usr/bin/env python3
"""Finite sanity checks for round-3 semantic-role, operational-cost, and fixed-point examples.

These checks validate only the displayed finite countermodels. They are not an
unbounded proof, a proof-assistant compilation, or a verification of the Rice-style theorem.
"""
from itertools import product
import json
from pathlib import Path

out = {}

# 1. One bare object, two forgotten roles. No recovery q: Bare -> Role can recover both.
bare = [0]
roles = ["Arith", "Index"]
enriched = [(0, r) for r in roles]
recoveries = [{0: r} for r in roles]
valid_role_recoveries = [
    q for q in recoveries
    if all(q[b] == r for b, r in enriched)
]
out["semantic_role_non_descent"] = {
    "bare_states": bare,
    "enriched_states": enriched,
    "candidate_recoveries": len(recoveries),
    "valid_exact_recoveries": len(valid_role_recoveries),
    "passed": len(valid_role_recoveries) == 0,
}

# 2. Two programs, same extensional denotation, different costs.
programs = {
    "fast_id": {"denotation": (0, 1), "cost": 1},
    "slow_id": {"denotation": (0, 1), "cost": 3},
}
denotations = sorted(set(v["denotation"] for v in programs.values()))
# A cost function on denotations chooses one natural number for the single denotation.
candidate_costs = [{denotations[0]: c} for c in range(5)]
valid_cost_recoveries = [
    q for q in candidate_costs
    if all(q[p["denotation"]] == p["cost"] for p in programs.values())
]
out["operational_cost_non_descent"] = {
    "programs": programs,
    "distinct_denotations": len(denotations),
    "candidate_cost_maps_checked": len(candidate_costs),
    "valid_exact_cost_maps": len(valid_cost_recoveries),
    "passed": len(valid_cost_recoveries) == 0,
}

# 3. Bool negation has no fixed point but has arbitrarily long finite prefixes of a trajectory.
def neg(b: bool) -> bool:
    return not b
fixed_points = [b for b in [False, True] if b == neg(b)]
trajectory = [False]
for _ in range(15):
    trajectory.append(neg(trajectory[-1]))
trajectory_ok = all(trajectory[n+1] == neg(trajectory[n]) for n in range(len(trajectory)-1))
out["static_fixed_point_vs_dynamic_trajectory"] = {
    "fixed_points": fixed_points,
    "trajectory_prefix": trajectory,
    "trajectory_equations_hold": trajectory_ok,
    "passed": len(fixed_points) == 0 and trajectory_ok,
}

# 4. Exact left inverse to the role-forgetting map cannot exist.
# Enumerate maps r: Bare -> Enriched and test r(pi(e)) = e for every e.
candidate_sections = [{0: e} for e in enriched]
exact_left_inverses = [
    r for r in candidate_sections
    if all(r[b] == (b, role) for b, role in enriched)
]
out["no_exact_reconstruction_left_inverse"] = {
    "candidate_maps": len(candidate_sections),
    "exact_left_inverses": len(exact_left_inverses),
    "passed": len(exact_left_inverses) == 0,
}

out["scope_warning"] = (
    "Finite enumeration only. It does not prove the general dependent-type/SIP theorem, "
    "the unbounded program-equivalence theorem, or any inconsistency of HoTT."
)
out["all_finite_checks_passed"] = all(
    v.get("passed", True) if isinstance(v, dict) else True for v in out.values()
)

path = Path('/mnt/data/verification/round3_semantic_operational_model_check.json')
path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(out, ensure_ascii=False, indent=2))

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/362b8b22c8ad19b6500a/round3_context_resource_checks.py | SHA256 362b8b22c8ad19b6500aa341a48a0aaced7b72fd49c3eefd51e5ac3d40132573 | LINES 1-120/120 =====
#!/usr/bin/env python3
"""Finite sanity checks for HOTT-Z round 3.

These checks illustrate minimal countermodels and registry invariants. They are not
proof-assistant verification and must not be described as unbounded formal proofs.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def role_erasure_check() -> dict[str, Any]:
    # One bare object has two enriched interpretations.
    bare = "successor-algebra"
    enriched = [(bare, "Arith"), (bare, "Index")]

    # Any deterministic predictor from the singleton bare domain chooses one role.
    predictors = [dict(value=v) for v in ("Arith", "Index")]
    failures = []
    for predictor in predictors:
        value = predictor["value"]
        bad = [e for e in enriched if e[1] != value]
        failures.append({"predictor": value, "misclassified": bad})

    return {
        "bare_images_equal": enriched[0][0] == enriched[1][0],
        "roles_different": enriched[0][1] != enriched[1][1],
        "predictor_count": len(predictors),
        "every_predictor_fails": all(item["misclassified"] for item in failures),
        "details": failures,
    }


def swap_equivariance_check() -> dict[str, Any]:
    # A two-element symmetric carrier; a canonical choice must be fixed by swap.
    carrier = (0, 1)
    swap = {0: 1, 1: 0}
    fixed = [x for x in carrier if swap[x] == x]
    return {
        "carrier": carrier,
        "swap": swap,
        "fixed_points": fixed,
        "equivariant_global_choice_exists": bool(fixed),
    }


def cartesian_structure_check() -> dict[str, Any]:
    # Finite-set illustration: every element is duplicated by the diagonal and
    # every element is discarded by the unique map to the singleton.
    A = ("token0", "token1")
    diagonal = {a: (a, a) for a in A}
    discard = {a: "*" for a in A}
    return {
        "object": A,
        "diagonal": diagonal,
        "discard": discard,
        "all_elements_duplicated": all(diagonal[a] == (a, a) for a in A),
        "all_elements_discarded": all(discard[a] == "*" for a in A),
        "interpretation": "Finite cartesian semantics automatically supplies copy/delete; a non-copyable resource needs extra structure or a different regime.",
    }


def registry_check() -> dict[str, Any]:
    reg = json.loads((ROOT / "HOTT_Z_SOURCE_REGISTRY.json").read_text(encoding="utf-8"))
    by_id = {s["id"]: s for s in reg["sources"]}
    duplicate_pairs = []
    all_match = True
    for source in reg["sources"]:
        dup = source.get("duplicate_of")
        if not dup:
            continue
        target = by_id[dup]
        same = source["sha256"] == target["sha256"]
        duplicate_pairs.append({"source": source["id"], "target": dup, "same_sha256": same})
        all_match = all_match and same
    return {
        "source_count": len(reg["sources"]),
        "duplicate_pairs": duplicate_pairs,
        "all_declared_byte_duplicates_match": all_match,
    }


def main() -> None:
    result = {
        "schema_version": "hott_z_round3_checks.v1",
        "scope_warning": "Finite sanity checks only; not proof-assistant verification or an unbounded proof.",
        "role_erasure": role_erasure_check(),
        "swap_equivariance": swap_equivariance_check(),
        "cartesian_copy_delete": cartesian_structure_check(),
        "source_registry": registry_check(),
    }
    out_json = ROOT / "verification" / "round3_context_resource_checks.json"
    out_txt = ROOT / "verification" / "round3_context_resource_checks.txt"
    out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "HOTT-Z round 3 finite sanity checks",
        "WARNING: finite checks only; not a proof-assistant verification or unbounded proof.",
        "",
        f"role erasure: every bare-only predictor fails = {result['role_erasure']['every_predictor_fails']}",
        f"two-point swap: equivariant choice exists = {result['swap_equivariance']['equivariant_global_choice_exists']}",
        f"cartesian copy/delete present = {result['cartesian_copy_delete']['all_elements_duplicated'] and result['cartesian_copy_delete']['all_elements_discarded']}",
        f"declared byte duplicates match = {result['source_registry']['all_declared_byte_duplicates_match']}",
    ]
    out_txt.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out_txt.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/394add51e4c8db753f3b/ContextFormalizer.agda | SHA256 394add51e4c8db753f3bc0f2f67cf905b76f43d4a2c855f5c52e5baa2320ed00 | LINES 1-31/31 =====
module ContextFormalizer where

open import Agda.Builtin.Equality using (_≡_; refl)

data ⊥ : Set where
¬_ : Set → Set
¬ A = A → ⊥
_≢_ : {A : Set} → A → A → Set
x ≢ y = ¬ (x ≡ y)

data Bit : Set where b0 b1 : Bit
neq01 : b0 ≢ b1
neq01 ()

data Unit : Set where unit : Unit

sym : {A : Set} {x y : A} → x ≡ y → y ≡ x
sym refl = refl
trans : {A : Set} {x y z : A} → x ≡ y → y ≡ z → x ≡ z
trans refl q = q


surfaceText : Unit
surfaceText = unit
correctSpec : Bit → Bit
correctSpec context = context

noContextFreePerfectFormalizer :
  (translate : Unit → Bit) → ¬ ((context : Bit) → translate surfaceText ≡ correctSpec context)
noContextFreePerfectFormalizer translate exact =
  neq01 (trans (sym (exact b0)) (exact b1))

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/3c2345d4fb803b1cd194/build_agda_unimath.sh | SHA256 3c2345d4fb803b1cd19432439ebbfd5c49cc77ffd0a1ceb476ccf90db8bf5910 | LINES 1-44/44 =====
#!/usr/bin/env bash
set -uo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PREFIX="${PREFIX:-$ROOT/.toolchain}"
AGDA="${AGDA:-$PREFIX/bin/agda}"
LIB="${AGDA_UNIMATH_ROOT:-$PREFIX/src/agda-unimath}"
OUT="$ROOT/build"
mkdir -p "$OUT"
LOG="$OUT/build.log"
: > "$LOG"
STATUS=0
if [[ ! -x "$AGDA" ]]; then
  echo "BLOCKED: Agda executable not found at $AGDA" | tee -a "$LOG"
  exit 77
fi
if [[ ! -d "$LIB/src" ]]; then
  echo "BLOCKED: agda-unimath source not found at $LIB" | tee -a "$LOG"
  exit 77
fi
"$AGDA" --version | tee -a "$LOG"
git -C "$LIB" rev-parse HEAD 2>&1 | tee -a "$LOG"
FLAGS=(--without-K --exact-split --no-import-sorts --auto-inline --no-require-unique-meta-solutions -WnoWithoutKFlagPrimEraseEquality --no-postfix-projections)
FILES=(
  "$ROOT/specs/FixedPointFreeMonodromy.agda"
  "$ROOT/specs/FiberTruthInvariant.agda"
  "$ROOT/specs/NoFreeEnrichment.agda"
  "$ROOT/specs/GuardErasure.agda"
  "$ROOT/specs/SnapshotProvenance.agda"
  "$ROOT/specs/IntentRole.agda"
  "$ROOT/specs/ContextFormalizer.agda"
  "$ROOT/specs/ExtensionalCost.agda"
  "$ROOT/specs/WalkingArrowCore.agda"
  "$ROOT/agda-unimath/hott-z/no-canonical-earlier-event.agda"
  "$ROOT/agda-unimath/hott-z/no-canonical-temporal-order.agda"
  "$ROOT/agda-unimath/hott-z/no-uniform-witness-extractor.agda"
)
for f in "${FILES[@]}"; do
  echo "=== $f ===" | tee -a "$LOG"
  "$AGDA" "${FLAGS[@]}" -i "$LIB/src" -i "$ROOT/agda-unimath" -i "$ROOT/specs" "$f" 2>&1 | tee -a "$LOG"
  rc=${PIPESTATUS[0]}
  echo "exit_code=$rc" | tee -a "$LOG"
  if [[ $rc -ne 0 ]]; then STATUS=$rc; fi
done
exit "$STATUS"

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/5871a660a963e6af8cef/_build_hierarchical_wbs_v2.py | SHA256 5871a660a963e6af8cef4492eb1761522ff48aa1f0dd41f8c56e272fe72259ad | LINES 1-1208/1208 =====
from __future__ import annotations

import json
import os
import re
import shutil
import hashlib
import zipfile
from collections import defaultdict, deque
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

BASE = Path('/mnt/data')
DATE = '2026-08-31'
STAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
BACKUP = BASE / '_research_backup_20260831_before_hierarchical_wbs_v2'
BACKUP.mkdir(parents=True, exist_ok=True)

FILES_TO_BACKUP = [
    'AGENTS.md', 'CURRENT_RESEARCH_INDEX.md', 'RESEARCH_LOG.md',
    'HOTT_Z_SOURCE_REGISTRY.json',
    'HOTT_Z_后续工作总方案与工作包分解_v1.md',
    'HOTT_Z_后续工作总体方案与工作包分解_第四轮.md',
    'HOTT_Z_后续工作总方案与WBS_v1.md',
    'HOTT_Z_WORK_PACKAGE_REGISTER.json',
    'HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json',
    'HOTT_Z_WBS_REGISTRY_v1.json',
    'HOTT_Z_执行看板.md',
    'HOTT_Z_阶段闸门与验收矩阵.md',
    'HOTT_Z_风险与红队登记表.md',
    'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md',
    'HOTT_Z_工作包—来源—主张追踪矩阵_v1_1.md',
    'HOTT_Z_后续工作执行摘要_规范版.md',
]
for name in FILES_TO_BACKUP:
    src = BASE / name
    if src.exists():
        shutil.copy2(src, BACKUP / name)


def load_json_path(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8'))

def load_json(name: str, fallback: str | None = None) -> dict[str, Any]:
    p = BASE / name
    if not p.exists() and fallback is not None:
        p = BASE / fallback
    return load_json_path(p)

wp_register = load_json(
    'HOTT_Z_WORK_PACKAGE_REGISTER.json',
    'archive/superseded_workplans_20260831/26_wp_plan_superseded/HOTT_Z_WORK_PACKAGE_REGISTER.json'
)
macro_register = load_json(
    'HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json',
    'archive/superseded_workplans_20260831/14_wp_round4_plan_superseded/HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json'
)
micro_register = load_json('HOTT_Z_WBS_REGISTRY_v1.json')
source_registry = load_json('HOTT_Z_SOURCE_REGISTRY.json')

# ---------------------------------------------------------------------------
# Canonical hierarchy
# ---------------------------------------------------------------------------
areas = [
    {'id': 'AREA-00', 'title': '治理、来源与单一事实源', 'objective': '固定源材料、活动台账、版本、编号和变更控制，使所有结论可追溯且不重复计证。'},
    {'id': 'AREA-01', 'title': '理论剖面与不完备性口径', 'objective': '逐定理固定 HoTT 变体、对象/元理论、宇宙、相等概念、目标语义与允许结论。'},
    {'id': 'AREA-02', 'title': 'Z 铁律数学核心', 'objective': '建立因子分解障碍、真值损失谱、表示精化和最小充分真值商。'},
    {'id': 'AREA-03', 'title': '单价时间定向与群胚方向障碍', 'objective': '证明裸单价对象和可逆 core 不能自然、免费、无损恢复一般时间方向。'},
    {'id': 'AREA-04', 'title': '时间轨道、极限与操作完成', 'objective': '区分固定点、轨道、极限、闭包、可达性、有限时间完成与 guarded 富化。'},
    {'id': 'AREA-05', 'title': '历史、语义角色与语境', 'objective': '研究 provenance、originality、intended role 与上下文规约在遗忘后的不可定义性。'},
    {'id': 'AREA-06', 'title': '资源制度与操作成本', 'objective': '以外延语义非因子化和 Cartesian–linear/quantitative 结构差异替代旧 transport 攻击。'},
    {'id': 'AREA-07', 'title': '断言、截断与具体见证', 'objective': '区分布尔标签、mere existence 与具体 path/equivalence witness，并研究无统一抽取。'},
    {'id': 'AREA-08', 'title': '有效求解与未来判定', 'objective': '在固定有效演算中研究稳定性、inhabitation、合成与 canonicalization 的不可总化边界。'},
    {'id': 'AREA-09', 'title': '反射、宇宙与对角化', 'objective': '在真实语法编码、评价与可证明性对象基础上独立研究 Lawvere/Gödel/宇宙开放性。'},
    {'id': 'AREA-10', 'title': '证明助理与可复现形式化', 'objective': '锁定工具链、完成核心定理机器检查、交叉验证和持续集成。'},
    {'id': 'AREA-11', 'title': '文献、原创性与红队', 'objective': '逐定理查清既有工作、最强反驳、变体边界和贡献等级。'},
    {'id': 'AREA-12', 'title': '论文组合与哲学分流', 'objective': '形成窄数学论文 A–D 与哲学伴随稿，防止支线污染主证明。'},
    {'id': 'AREA-13', 'title': '独立复核、复现与发布', 'objective': '完成独立核验、干净环境重建、清单、匿名包和公开包。'},
]

wp_area = {
    'WP-00': 'AREA-00', 'WP-02': 'AREA-00',
    'WP-01': 'AREA-01',
    'WP-10': 'AREA-02', 'WP-11': 'AREA-02',
    'WP-12': 'AREA-03', 'WP-13': 'AREA-03',
    'WP-14': 'AREA-04',
    'WP-15': 'AREA-05', 'WP-18': 'AREA-05',
    'WP-16': 'AREA-06',
    'WP-17': 'AREA-07',
    'WP-19': 'AREA-08',
    'WP-20': 'AREA-09',
    'WP-30': 'AREA-10', 'WP-31': 'AREA-10', 'WP-32': 'AREA-10', 'WP-33': 'AREA-10',
    'WP-03': 'AREA-11', 'WP-40': 'AREA-11',
    'WP-41': 'AREA-12', 'WP-42': 'AREA-12', 'WP-43': 'AREA-12', 'WP-44': 'AREA-12', 'WP-45': 'AREA-12',
    'WP-46': 'AREA-13',
}

# Map the 45 fine-grained legacy WPs to canonical work packages.
legacy_tm_parent = {
    'WP-000': 'WP-01', 'WP-010': 'WP-02', 'WP-020': 'WP-00', 'WP-030': 'WP-40',
    'WP-100': 'WP-01', 'WP-110': 'WP-10', 'WP-120': 'WP-11', 'WP-130': 'WP-11',
    'WP-140': 'WP-10', 'WP-150': 'WP-11',
    'WP-200': 'WP-12', 'WP-210': 'WP-12', 'WP-220': 'WP-12',
    'WP-230': 'WP-13', 'WP-240': 'WP-13', 'WP-250': 'WP-41',
    'WP-300': 'WP-15', 'WP-310': 'WP-15', 'WP-320': 'WP-18', 'WP-330': 'WP-17', 'WP-340': 'WP-15',
    'WP-400': 'WP-16', 'WP-410': 'WP-16', 'WP-420': 'WP-19', 'WP-430': 'WP-19',
    'WP-440': 'WP-14', 'WP-450': 'WP-14', 'WP-460': 'WP-14',
    'WP-500': 'WP-20', 'WP-510': 'WP-20',
    'WP-600': 'WP-30', 'WP-610': 'WP-31', 'WP-620': 'WP-31', 'WP-630': 'WP-32',
    'WP-640': 'WP-31', 'WP-650': 'WP-30',
    'WP-700': 'WP-03', 'WP-710': 'WP-03', 'WP-720': 'WP-40', 'WP-730': 'WP-46',
    'WP-800': 'WP-41', 'WP-810': 'WP-42', 'WP-820': 'WP-44', 'WP-830': 'WP-45', 'WP-840': 'WP-46',
}
legacy_tm_supports = {
    'WP-240': ['WP-14', 'WP-40'],
    'WP-250': ['WP-10', 'WP-12', 'WP-13', 'WP-15'],
    'WP-330': ['WP-32'],
    'WP-420': ['WP-43'],
    'WP-430': ['WP-43'],
    'WP-440': ['WP-32'],
    'WP-450': ['WP-45'],
    'WP-460': ['WP-43', 'WP-45'],
    'WP-630': ['WP-31', 'WP-33'],
    'WP-640': ['WP-40'],
    'WP-650': ['WP-46'],
    'WP-700': ['WP-41', 'WP-42', 'WP-43', 'WP-44'],
    'WP-710': ['WP-41', 'WP-42', 'WP-43', 'WP-44'],
    'WP-720': ['WP-41', 'WP-42', 'WP-43', 'WP-44'],
    'WP-730': ['WP-41'],
    'WP-840': ['WP-41'],
}

# Mechanisms used across the program.
mechanisms = [
    {'id': 'M1', 'name': '非因子化／不可定义', 'criterion': '同一抽象纤维中存在目标真值差异，故目标不能经遗忘映射下降。'},
    {'id': 'M2', 'name': '无截面／无自然选择', 'criterion': '自同构或 monodromy 对候选富化无固定点，故不存在自然全局选择。'},
    {'id': 'M3', 'name': '不可总判定／不可总合成', 'criterion': '假定总算法可归约出 halting、inhabitation 或程序语义等已知不可判定问题。'},
    {'id': 'M4', 'name': '反射与元理论开放性', 'criterion': '对象理论无法无条件内部化其全部真理、可证明性或一致性；必须明确语法和元理论。'},
    {'id': 'GOV', 'name': '治理与证据控制', 'criterion': '不产生数学定理，但保证来源、编号、版本、状态和证据等级可信。'},
    {'id': 'FORMAL', 'name': '机器化与复现', 'criterion': '把纸笔定理转成固定工具链上的可重复编译证据。'},
    {'id': 'PUB', 'name': '论文与发布', 'criterion': '将已过门结果组织为范围明确、可复核、可复现的稿件。'},
]

evidence_levels = [
    {'id': 'E0', 'name': '源材料直觉', 'definition': '来自对话、比喻、思想实验或待修复攻击；不能作定理证据。'},
    {'id': 'E1', 'name': '良构陈述', 'definition': '对象、量词、宇宙、相等和目标语义已明确，但证明未完成。'},
    {'id': 'E2', 'name': '纸笔证明', 'definition': '已有可审查证明或严格反例；尚无证明助理回执。'},
    {'id': 'E3', 'name': '有限程序核验', 'definition': '有限枚举、模型检查或索引检查通过；不得冒充无界证明。'},
    {'id': 'E4', 'name': '证明助理通过', 'definition': '固定版本工具链对核心源码 type-check/compile 成功，并保存回执。'},
    {'id': 'E5', 'name': '独立红队复核', 'definition': '独立证明、反例搜索或第二形式化栈复核通过。'},
    {'id': 'E6', 'name': '文献与原创性审计', 'definition': '逐定理完成 prior-art、归属、差异和不确定性审计。'},
    {'id': 'E7', 'name': '发布级复现', 'definition': '干净环境重建、论文/源码/日志/哈希一致并可公开复现。'},
]

status_vocabulary = [
    {'id': 'COMPLETE', 'meaning': '本工作包当前版本的验收条件已满足；后续变更需重新开门。'},
    {'id': 'ACTIVE', 'meaning': '正在执行且依赖已满足。'},
    {'id': 'READY', 'meaning': '定义和纸笔基础充分，可以开始。'},
    {'id': 'PAPER_PROVED_FORMALIZATION_BLOCKED', 'meaning': '纸笔证明存在，但机器化受工具链或依赖阻塞。'},
    {'id': 'BLOCKED_TOOLCHAIN_ABSENT', 'meaning': '当前环境缺少必要证明助理或库。'},
    {'id': 'BLOCKED_DEPENDENCY', 'meaning': '依赖工作包尚未通过。'},
    {'id': 'DEFERRED', 'meaning': '主动延后，防止分散主线。'},
    {'id': 'PARKED', 'meaning': '保留材料但不进入活动证明链。'},
]

# Convert fine-grained work packages to task modules.
def tm_id(old_id: str) -> str:
    assert old_id.startswith('WP-')
    return 'TM-' + old_id[3:]

modules: list[dict[str, Any]] = []
for old in micro_register['work_packages']:
    oid = old['id']
    if oid not in legacy_tm_parent:
        raise KeyError(f'Missing TM parent mapping for {oid}')
    m = deepcopy(old)
    m['id'] = tm_id(oid)
    m['legacy_id'] = oid
    m['parent_wp'] = legacy_tm_parent[oid]
    m['supports_wps'] = legacy_tm_supports.get(oid, [])
    m['dependencies'] = [tm_id(x) for x in old.get('dependencies', [])]
    m['legacy_stream'] = m.pop('stream', None)
    m['level'] = 'task_module'
    modules.append(m)

# Add a dedicated formalization module for canonical WP-33, which the old fine-grained plan only covered indirectly.
modules.append({
    'id': 'TM-635',
    'legacy_id': None,
    'parent_wp': 'WP-33',
    'supports_wps': ['WP-13', 'WP-16', 'WP-19'],
    'title': '形式化批次 C：范畴、资源与可计算性集成',
    'legacy_stream': 'S6 形式化验证',
    'mechanism': 'FORMAL/M1/M3',
    'priority': 'P2',
    'status': 'BLOCKED',
    'objective': '把 walking-arrow/core、cartesian–linear 结构障碍与固定演算归约组织为独立重型机器化批次。',
    'current_basis': '纸笔证明与最小有限模型存在；尚缺合适的范畴/可计算性形式化栈。',
    'source_refs': ['SRC-NARR-001', 'SRC-HEEL-001', 'SRC-SELF-001'],
    'claim_refs': ['Z-33', 'Z-34', 'Z-39', 'Z-136', 'Z-137', 'Z-138'],
    'proof_refs': ['PA-09', 'PA-11', 'PA-33', 'PA-63', 'PA-64', 'PA-72', 'PA-73'],
    'result_refs': ['R-08', 'R-10', 'R-30', 'R-59', 'R-60', 'R-70', 'R-71'],
    'dependencies': ['TM-230', 'TM-400', 'TM-410', 'TM-420', 'TM-430', 'TM-600'],
    'tasks': ['选择 Rzk/Agda Categories/Lean 等适配栈', '机器化 walking arrow 与 core', '机器化 strong monoidal comonoid transfer 或最小替代', '机器化至少一条 halting/inhabitation reduction', '保存失败最小复现'],
    'deliverables': ['formal/batch_c/', 'verification/batch_c_build.log', 'formal/batch_c/ASSUMPTIONS.md'],
    'acceptance_criteria': ['工具选择有书面理由', '至少一条核心对象/归约达到 E4', '不把有限搜索冒充无界证明', '失败依赖和 postulates 完整公开'],
    'failure_or_split_conditions': ['若单一工具栈无法覆盖三类结果，则拆分为 category/resource 与 computability 两个批次；不得因工具不匹配改变数学结论。'],
    'target_outputs': ['Paper A/B/C formal appendices'],
    'level': 'task_module',
})

# Add the publication module missing from the 45-package detailed plan.
modules.append({
    'id': 'TM-815',
    'legacy_id': None,
    'parent_wp': 'WP-43',
    'supports_wps': ['WP-19', 'WP-33', 'WP-40'],
    'title': '论文 C：有效求解与未来判定边界组装',
    'legacy_stream': 'S8 写作发布',
    'mechanism': 'PUB/M3',
    'priority': 'P2',
    'status': 'READY',
    'objective': '把 future stabilization、inhabitation synthesis 与 semantic canonicalization 的条件性不可计算结果组织为独立论文，避免绑架 Paper A。',
    'current_basis': 'WP-19 已有纸笔归约框架；尚缺固定演算、机器化和逐定理文献审计。',
    'source_refs': ['SRC-HEEL-001', 'SRC-SELF-001', 'SRC-Z-001'],
    'claim_refs': ['Z-46', 'Z-59', 'Z-137', 'Z-156'],
    'proof_refs': ['PA-15', 'PA-64', 'PA-65', 'PA-72'],
    'result_refs': ['R-14', 'R-25', 'R-31', 'R-32', 'R-70'],
    'dependencies': ['TM-420', 'TM-430', 'TM-700', 'TM-720'],
    'tasks': ['锁定统一计算模型与编码', '统一三类归约的假设模板', '写 positive escape routes：partial/interactive/heuristic solver', '完成论文范围、limitations 和复现附录'],
    'deliverables': ['paper_C/main.md或.tex', 'paper_C/reductions/', 'paper_C/assumption_matrix.json'],
    'acceptance_criteria': ['所有不可判定性结论给出明确归约', '至少一条归约达到 E4 或 E5', '标题不暗示 HoTT 独有', '不从自然语言模糊直接跳到 halting'],
    'failure_or_split_conditions': ['若固定 HoTT 演算的 inhabitation 元理论不足，则降为一般依赖类型论/证明合成论文；若三个归约缺乏共同结构，则拆为短文。'],
    'target_outputs': ['Paper C'],
    'level': 'task_module',
})

# Status overrides grounded in current environment/tool facts.
status_override = {
    'WP-30': ('BLOCKED_TOOLCHAIN_ABSENT', 'E1'),
    'WP-31': ('BLOCKED_TOOLCHAIN_ABSENT', 'E1'),
    'WP-32': ('BLOCKED_DEPENDENCY', 'E1'),
    'WP-33': ('BLOCKED_DEPENDENCY', 'E1'),
    'WP-12': ('PAPER_PROVED_FORMALIZATION_BLOCKED', 'E2'),
    'WP-17': ('PAPER_PROVED_FORMALIZATION_BLOCKED', 'E2'),
    'WP-46': ('BLOCKED_DEPENDENCY', 'E0'),
}

# Additional source basis when not captured by the detailed modules.
wp_source_extra: dict[str, list[str]] = {
    'WP-00': ['SRC-META-001'],
    'WP-01': ['SRC-Z-001', 'SRC-FINAL-001', 'SRC-NARR-001'],
    'WP-02': ['SRC-META-001'],
    'WP-03': [],
    'WP-10': ['SRC-Z-001', 'SRC-FINAL-001'],
    'WP-11': ['SRC-Z-001', 'SRC-LAST-001'],
    'WP-12': ['SRC-Z-001', 'SRC-ID-001'],
    'WP-13': ['SRC-NARR-001', 'SRC-Z-001'],
    'WP-14': ['SRC-Z-001', 'SRC-FINAL-EX-001', 'SRC-SELF-001'],
    'WP-15': ['SRC-SEM-001', 'SRC-ID-001'],
    'WP-16': ['SRC-HEEL-001', 'SRC-NARR-001'],
    'WP-17': ['SRC-PROB-001', 'SRC-PROB-EX-001'],
    'WP-18': ['SRC-HEEL-001', 'SRC-Z-001'],
    'WP-19': ['SRC-HEEL-001', 'SRC-SELF-001'],
    'WP-20': ['SRC-GODEL-001', 'SRC-CANTOR-001', 'SRC-MIRROR-001', 'SRC-MIRROR-EX-001', 'SRC-UNIV-001'],
    'WP-30': [], 'WP-31': [], 'WP-32': [], 'WP-33': [],
    'WP-40': ['SRC-EXP-001', 'SRC-OBSERVER-001', 'SRC-QUANTUM-001', 'SRC-HOMID-001', 'SRC-CANTOR-001', 'SRC-GODEL-001'],
    'WP-41': ['SRC-Z-001', 'SRC-ID-001', 'SRC-SEM-001'],
    'WP-42': ['SRC-SEM-001', 'SRC-HEEL-001', 'SRC-PROB-EX-001', 'SRC-ID-001'],
    'WP-43': ['SRC-HEEL-001', 'SRC-SELF-001', 'SRC-Z-001'],
    'WP-44': ['SRC-GODEL-001', 'SRC-CANTOR-001', 'SRC-MIRROR-001'],
    'WP-45': ['SRC-FINAL-001', 'SRC-NARR-001', 'SRC-FINAL-EX-001', 'SRC-Z-001'],
    'WP-46': ['SRC-META-001'],
}

modules_by_parent: dict[str, list[dict[str, Any]]] = defaultdict(list)
for m in modules:
    modules_by_parent[m['parent_wp']].append(m)

# Parse linked research IDs from the 26-WP plan and union with detailed modules.
def classify_ref(x: str) -> tuple[str, str] | None:
    x = x.strip()
    # ranges are retained as linked_research_ids but not used for existence checking.
    if re.fullmatch(r'Z-\d+', x): return ('claim', x)
    if re.fullmatch(r'PA-\d+', x): return ('proof', x)
    if re.fullmatch(r'R-\d+', x): return ('result', x)
    if re.fullmatch(r'LIT-\d+', x): return ('literature', x)
    return None

canonical_wps: list[dict[str, Any]] = []
for old in wp_register['work_packages']:
    w = deepcopy(old)
    wid = w['id']
    w['level'] = 'work_package'
    w['area_id'] = wp_area[wid]
    if wid in status_override:
        w['status'], w['current_evidence'] = status_override[wid]
    tms = sorted(modules_by_parent.get(wid, []), key=lambda x: x['id'])
    w['task_modules'] = [m['id'] for m in tms]
    source_refs = set(wp_source_extra.get(wid, []))
    claims, proofs, results, lits = set(), set(), set(), set()
    for m in tms:
        source_refs.update(m.get('source_refs', []))
        claims.update(m.get('claim_refs', []))
        proofs.update(m.get('proof_refs', []))
        results.update(m.get('result_refs', []))
    for ref in w.get('linked_research_ids', []):
        c = classify_ref(ref)
        if c:
            kind, val = c
            {'claim': claims, 'proof': proofs, 'result': results, 'literature': lits}[kind].add(val)
    w['source_refs'] = sorted(source_refs)
    w['claim_refs'] = sorted(claims, key=lambda s: int(s.split('-')[1]))
    w['proof_refs'] = sorted(proofs, key=lambda s: int(s.split('-')[1]))
    w['result_refs'] = sorted(results, key=lambda s: int(s.split('-')[1]))
    w['literature_refs'] = sorted(lits)
    w['failure_or_split_conditions'] = []
    for m in tms:
        for item in m.get('failure_or_split_conditions', []):
            if item not in w['failure_or_split_conditions']:
                w['failure_or_split_conditions'].append(item)
    if not w['failure_or_split_conditions']:
        w['failure_or_split_conditions'] = ['若验收条件无法满足，则收缩量词、分离 HoTT 特定与一般部分，或降级为限制/反例/哲学动机；不得以修辞替代证明。']
    canonical_wps.append(w)

# Areas get their work packages and intended outputs.
area_output_map = {
    'AREA-00': ['单一事实源', '来源与编号治理'],
    'AREA-01': ['TheoryProfile', 'Claim Scope Matrix'],
    'AREA-02': ['Z core', 'Loss spectrum', 'Minimal sufficient quotient'],
    'AREA-03': ['Paper A core theorems', 'orientation/core formalization'],
    'AREA-04': ['Paper A appendix', 'Paper III / philosophy companion'],
    'AREA-05': ['Paper B'],
    'AREA-06': ['Paper B'],
    'AREA-07': ['Paper B'],
    'AREA-08': ['Paper C'],
    'AREA-09': ['Paper D'],
    'AREA-10': ['formal/ source and receipts'],
    'AREA-11': ['originality matrix', 'red-team reports'],
    'AREA-12': ['Papers A–D', 'philosophy companion'],
    'AREA-13': ['reproducibility bundle'],
}
for a in areas:
    a['work_packages'] = [w['id'] for w in canonical_wps if w['area_id'] == a['id']]
    a['target_outputs'] = area_output_map[a['id']]

# Unified gates.
gates = [
    {
        'id': 'G-00', 'title': '单一事实源与治理基线',
        'requires': ['WP-00', 'WP-02'],
        'criteria': ['活动 Source/Claim/Proof/Result/Literature/WP/TM ID 唯一', '规范/候选/历史计划状态无冲突', '源文件重复与派生关系已登记'],
        'unlocks': ['WP-01', 'WP-03', 'WP-10', 'WP-30']
    },
    {
        'id': 'G-01', 'title': '理论剖面与数学核心冻结',
        'requires': ['WP-01', 'WP-10', 'WP-11'],
        'criteria': ['每个定理指定 HoTT 变体、对象/元理论、宇宙与相等概念', 'Z 因子化必要方向纸笔证明完整', '充分性仅在 image/quotient/满射等明确条件下陈述'],
        'unlocks': ['WP-12', 'WP-13', 'WP-14', 'WP-15', 'WP-16', 'WP-18', 'WP-19']
    },
    {
        'id': 'G-02', 'title': '可复现证明助理工具链',
        'requires': ['WP-30'],
        'criteria': ['固定编译器与库 commit', 'smoke test 退出码 0', '命令、stdout/stderr、源码哈希和环境锁文件齐全'],
        'unlocks': ['WP-31', 'WP-32', 'WP-33']
    },
    {
        'id': 'G-03', 'title': '首个 HoTT 特定机器定理',
        'requires': ['WP-12', 'WP-31'],
        'criteria': ['no-canonical-earlier-event 或同等核心定理达到 E4', '无等价于结论的新增 postulate', '纸笔定理、源码与主稿逐项对应'],
        'unlocks': ['WP-17', 'WP-41']
    },
    {
        'id': 'G-04', 'title': '核心定理套件与变体红队',
        'requires': ['WP-13', 'WP-17', 'WP-40'],
        'criteria': ['ordinary non-invertible functions 等最强反驳已处理', '裸层、富化层与具体遗忘映射严格区分', '至少一个 core/time-reversal 或 witness 定理达到 E4/E5'],
        'unlocks': ['WP-41', 'WP-42']
    },
    {
        'id': 'G-05', 'title': '文献、归属与原创性清算',
        'requires': ['WP-03', 'WP-40'],
        'criteria': ['逐定理 prior-art matrix 完成', '创建者/拥趸主张仅使用一手可核对材料', '无无证“首次/推翻/学界未发现”措辞'],
        'unlocks': ['WP-41', 'WP-42', 'WP-43', 'WP-44']
    },
    {
        'id': 'G-06', 'title': 'Paper A 投稿就绪',
        'requires': ['WP-41'],
        'criteria': ['中心定理至少一项 E4', '关键定理均有 E2、E5、E6', '摘要明确相对不完备而非 HoTT⊢⊥', '形式化附录和 claim crosswalk 完整'],
        'unlocks': ['WP-46']
    },
    {
        'id': 'G-07', 'title': '独立复现与项目发布',
        'requires': ['WP-46'],
        'criteria': ['从干净环境重建成功', '论文/源码/日志/清单哈希一致', '未解决异议与失败路线公开', '发布物明确区分主论文与支线'],
        'unlocks': ['公开发布', '后续论文 B/C/D 正式启动']
    },
]

critical_path = ['WP-00', 'WP-02', 'WP-01', 'WP-10', 'WP-30', 'WP-12', 'WP-31', 'WP-03', 'WP-13', 'WP-14', 'WP-40', 'WP-41', 'WP-46']

parallel_lanes = [
    {'id': 'LANE-A', 'name': 'Paper A 主线', 'sequence': ['WP-01', 'WP-10', 'WP-30', 'WP-12', 'WP-31', 'WP-13', 'WP-14', 'WP-40', 'WP-41', 'WP-46']},
    {'id': 'LANE-B', 'name': '签名/语义/资源', 'sequence': ['WP-10', 'WP-15', 'WP-16', 'WP-17', 'WP-18', 'WP-32', 'WP-42']},
    {'id': 'LANE-C', 'name': '有效求解', 'sequence': ['WP-01', 'WP-10', 'WP-19', 'WP-33', 'WP-43']},
    {'id': 'LANE-D', 'name': '反射与宇宙（隔离）', 'sequence': ['WP-01', 'WP-03', 'WP-20', 'WP-44']},
    {'id': 'LANE-PH', 'name': '哲学伴随', 'sequence': ['WP-10', 'WP-14', 'WP-40', 'WP-45']},
]

publication_portfolio = [
    {
        'id': 'PAPER-A',
        'working_title': 'No-Free Temporal and Historical Enrichment in Univalent Foundations',
        'scope': ['Z factorization', 'no canonical temporal orientation', 'groupoid core/time reversal', 'minimal historical enrichment', 'selected limit/operational corollary'],
        'must_exclude': ['HoTT⊢⊥', 'all HoTT arrows are reversible', 'HoTT cannot encode time', 'old transport paradox', 'Gödel-space shortcut'],
        'work_packages': ['WP-10', 'WP-12', 'WP-13', 'WP-14', 'WP-31', 'WP-40', 'WP-41', 'WP-46'],
    },
    {
        'id': 'PAPER-B',
        'working_title': 'Signature-Relative Incompleteness: Context, Intent, Evidence, and Resource Regimes in Univalent Foundations',
        'scope': ['provenance', 'intended role', 'contextual formalization', 'cost/resource regimes', 'truncation/witness'],
        'must_exclude': ['meaning is intrinsically non-mathematical', 'Nat≃Nat′ implies judgmental interchangeability', 'old once-only transport'],
        'work_packages': ['WP-15', 'WP-16', 'WP-17', 'WP-18', 'WP-32', 'WP-42'],
    },
    {
        'id': 'PAPER-C',
        'working_title': 'Effective Boundaries of Formalization, Proof Synthesis, and Future Stabilization',
        'scope': ['future stabilization', 'inhabitation synthesis', 'semantic canonicalization', 'partial/interactive positive results'],
        'must_exclude': ['halting claim without a reduction', 'natural-language ambiguity directly implies undecidability', 'HoTT-specific attribution without proof'],
        'work_packages': ['WP-19', 'WP-33', 'WP-43'],
    },
    {
        'id': 'PAPER-D',
        'working_title': 'Reflection and Diagonalization in Univalent Type-Theoretic Foundations',
        'scope': ['syntax coding', 'provability/evaluation', 'Lawvere fixed point', 'universe/resizing/predicativity'],
        'must_exclude': ['Map(1,G)=ΩG', 'a universe of all types at the same level', 'observer-dimension analogy as proof'],
        'work_packages': ['WP-20', 'WP-44'],
    },
    {
        'id': 'PAPER-PH',
        'working_title': 'Z Law, Zeno, Being and Becoming: The Ontological Limits of Formal Abstraction',
        'scope': ['original philosophical insight', 'photograph/film/projector', 'extensional vs operational completion', 'model/reality boundary'],
        'must_exclude': ['philosophical premise presented as formal theorem', 'limit theory is mathematically inconsistent'],
        'work_packages': ['WP-14', 'WP-45'],
    },
]

immediate_queue = [
    {'id': 'AQ-01', 'priority': 'P0', 'work_package': 'WP-00', 'action': '完成分层 WBS v2 合并、废止竞争计划、更新单一事实源。', 'output': '本方案、机器注册表、交叉索引和完整性回执。', 'status': 'COMPLETE'},
    {'id': 'AQ-02', 'priority': 'P0', 'work_package': 'WP-01', 'action': '建立 HOTT_Z_THEORY_PROFILE.md：逐定理固定 axiomatic/cubical/directed/guarded/linear profile。', 'output': 'TheoryProfile 与 Claim Scope Matrix。', 'status': 'NEXT'},
    {'id': 'AQ-03', 'priority': 'P0', 'work_package': 'WP-10', 'action': '冻结 Z factorization 的集合、hProp、image/quotient 三版陈述。', 'output': 'Z_FACTORISATION_CORE.md 与 formal lemma spec。', 'status': 'NEXT'},
    {'id': 'AQ-04', 'priority': 'P0', 'work_package': 'WP-30', 'action': '安装并锁定 Agda-unimath 主栈；若当前环境不可安装，生成可复现容器/脚本和明确阻塞回执。', 'output': 'toolchain.lock、smoke test、完整日志。', 'status': 'BLOCKED_TOOLCHAIN_ABSENT'},
    {'id': 'AQ-05', 'priority': 'P0', 'work_package': 'WP-31', 'action': '机器化 fixed-point-free monodromy 与 no-canonical-earlier-event。', 'output': '首个 E4 HoTT 特定定理。', 'status': 'BLOCKED_BY_AQ-04'},
    {'id': 'AQ-06', 'priority': 'P0', 'work_package': 'WP-03', 'action': '建立 Paper A 逐定理 prior-art matrix，重点检索 univalence/no-section/global choice/directed type theory。', 'output': 'HOTT_Z_ORIGINALITY_MATRIX.md。', 'status': 'PARALLEL_READY'},
    {'id': 'AQ-07', 'priority': 'P0', 'work_package': 'WP-13', 'action': '完成 walking-arrow/core/time-reversal 最小形式模型，并选择 Rzk/Agda Categories/Lean 路线。', 'output': '方向障碍定理稿与机器化设计。', 'status': 'READY'},
    {'id': 'AQ-08', 'priority': 'P1', 'work_package': 'WP-17', 'action': '复用 no-section/global-choice 结果建立 no-uniform-witness-extractor。', 'output': '证据截断定理和形式化文件。', 'status': 'DEPENDENT_ON_AQ-05'},
    {'id': 'AQ-09', 'priority': 'P0', 'work_package': 'WP-40', 'action': '对 Paper A 运行最强红队：ordinary functions、Step relations、directed/cubical/guarded enrichments。', 'output': '反驳矩阵与定理收缩记录。', 'status': 'ACTIVE'},
    {'id': 'AQ-10', 'priority': 'P0', 'work_package': 'WP-41', 'action': '只在 G-03/G-05 通过后冻结 Paper A 定理集并压缩 v4 候选。', 'output': '窄 Paper A 匿名稿。', 'status': 'BLOCKED_BY_GATES'},
]

# Risks unified from prior plans plus reconciliation risk.
risks = [
    {'id': 'RK-01', 'severity': 'CRITICAL', 'risk': '把相对表示不完备误写成 HoTT 内部不一致。', 'mitigation': 'WP-01 scope matrix；摘要和每条定理强制写目标语义、遗忘映射和富化政策。'},
    {'id': 'RK-02', 'severity': 'CRITICAL', 'risk': '把 ordinary function/Step 可表示非可逆过程这一反例忽略。', 'mitigation': 'WP-40 永久回归测试；结论限定 identity/core 或指定遗忘表示。'},
    {'id': 'RK-03', 'severity': 'CRITICAL', 'risk': 'no-section 机制和因子分解定理属于既有一般数学，原创性被否定。', 'mitigation': 'WP-03 逐定理 prior-art；贡献改为 HoTT 特定专门化、统一框架或新应用。'},
    {'id': 'RK-04', 'severity': 'HIGH', 'risk': '当前证明助理工具链不存在，形式化长期阻塞。', 'mitigation': 'WP-30 先建立容器/锁文件；允许换第二工具栈但必须保留可复现回执。'},
    {'id': 'RK-05', 'severity': 'HIGH', 'risk': '单价“无方向”定理只是任意对称对象无自然选择的改名。', 'mitigation': '明确一般引理与 HoTT/time 专门化的贡献层级；增加 strict order、core 和 enrichment 下界。'},
    {'id': 'RK-06', 'severity': 'HIGH', 'risk': '从数学极限越界到物理超任务或连续统本体结论。', 'mitigation': 'WP-14 每个物理结论附加模型公理；数学结论只谈 reachability/closure/factorization。'},
    {'id': 'RK-07', 'severity': 'HIGH', 'risk': '形式化翻译的不确定性被无归约地升级为停机不可判定。', 'mitigation': 'WP-18 先证明语境欠定；WP-19 只有固定编码后做 reduction。'},
    {'id': 'RK-08', 'severity': 'HIGH', 'risk': '旧 transport、Gödel space、universe equivalence、observer dimension 或 quantum successor 重新进入主证明。', 'mitigation': 'WP-40 负控制套件和隔离表；CI 检查禁用措辞/引用。'},
    {'id': 'RK-09', 'severity': 'MEDIUM', 'risk': '论文 A 范围过宽，被哲学、资源和反射支线淹没。', 'mitigation': 'Paper A 只保留 Z core、orientation、core/time-reversal 和必要历史富化。'},
    {'id': 'RK-10', 'severity': 'MEDIUM', 'risk': '源材料多为 AI 对话与派生摘录，被误作独立学术证据。', 'mitigation': 'WP-02 来源谱系；对话只作思想来源，数学证据来自证明/形式化/一手文献。'},
    {'id': 'RK-11', 'severity': 'MEDIUM', 'risk': '无截面证明隐藏选择、公理或 universe/truncation 问题。', 'mitigation': 'WP-10/WP-12 明确 constructive assumptions；源码审查 postulates。'},
    {'id': 'RK-12', 'severity': 'MEDIUM', 'risk': '不同 HoTT/cubical/directed/linear 变体被混称为同一理论。', 'mitigation': 'WP-01 TheoryProfile；每条定理附 profile card。'},
    {'id': 'RK-13', 'severity': 'MEDIUM', 'risk': '并行写入再次产生多个规范计划或重复编号。', 'mitigation': '本 v2 为唯一规范；旧计划标记 SUPERSEDED；AGENTS 和 JSON 固定变更流程。'},
    {'id': 'RK-14', 'severity': 'MEDIUM', 'risk': '有限 Python 枚举被误写为无界形式证明。', 'mitigation': 'E3/E4 分级；所有日志注明证据等级。'},
    {'id': 'RK-15', 'severity': 'LOW', 'risk': '哲学稿的强修辞被误引入数学摘要。', 'mitigation': 'Paper-PH 与 Paper A 分仓；claim lint 检查“粉碎/幻觉/非法”等词。'},
]

superseded_plans = [
    {'file': 'HOTT_Z_后续工作总方案与工作包分解_v1.md', 'role': '26-WP execution plan; canonical WP IDs retained in v2', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_WORK_PACKAGE_REGISTER.json', 'role': 'legacy 26-WP registry; absorbed verbatim/normalized into v2', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_后续工作总体方案与工作包分解_第四轮.md', 'role': '14-macro-area plan; concepts retained as AREA level', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json', 'role': 'legacy 14-WP macro registry; absorbed as program areas and gates', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_后续工作总方案与WBS_v1.md', 'role': '45-package fine-grained plan; IDs converted to TM task modules', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_WBS_REGISTRY_v1.json', 'role': 'legacy 45-package registry; converted to TM modules, plus TM-635 and TM-815 added', 'status': 'SUPERSEDED_NONCANONICAL'},
    {'file': 'HOTT_Z_工作包—来源—主张追踪矩阵_v1_1.md', 'role': 'v1.1 trace matrix; replaced by v2 registry and crosswalk', 'status': 'SUPERSEDED_NONCANONICAL'},
]

program = {
    'schema_version': 'hott_z_hierarchical_wbs.v2',
    'canonical': True,
    'program_id': 'HOTT-Z-RP-20260831',
    'version': '2.0',
    'date': DATE,
    'generated_at_utc': STAMP,
    'title': 'HoTT–Z 相对不完备性研究：后续工作总体方案与分层 WBS',
    'mission': '把 Z 铁律的哲学洞察重构为可证明、可形式化、可红队、可检索和可复现的 HoTT 相对不完备性结果。',
    'central_thesis': '当指定 HoTT/单价表示遗忘了目标相关的时间、历史、语境、资源或见证差异时，这些真值不能在无新增信息条件下由裸表示免费、自然、无损恢复。',
    'non_goals': [
        '不以当前项目证明 HoTT⊢⊥。',
        '不主张 HoTT 完全不能编码时间、非可逆函数、状态转移或资源结构。',
        '不把一般 Gödel/halting/no-choice 限制冒充 HoTT 独有漏洞。',
        '不把 AI 对话中的赞同、沉默或专家角色当作数学证据。',
        '不把有限枚举和索引脚本冒充证明助理验证。',
    ],
    'source_basis_note': '源材料提供问题发现、Being/Becoming、照片/电影/放映机、三大阿喀琉斯之踵和语义角色等思想；旧证明中的逻辑、类型和归约错误已转入红队负控制。',
    'hierarchy': {'areas': 14, 'work_packages': len(canonical_wps), 'task_modules': len(modules), 'gates': len(gates)},
    'mechanisms': mechanisms,
    'evidence_levels': evidence_levels,
    'status_vocabulary': status_vocabulary,
    'areas': areas,
    'work_packages': canonical_wps,
    'task_modules': sorted(modules, key=lambda x: x['id']),
    'gates': gates,
    'critical_path': critical_path,
    'parallel_lanes': parallel_lanes,
    'publication_portfolio': publication_portfolio,
    'immediate_queue': immediate_queue,
    'risks': risks,
    'current_toolchain_facts': {
        'checked_on': DATE,
        'executables': {'agda': False, 'lean': False, 'lake': False, 'coqc': False, 'rocq': False, 'rzk': False},
        'consequence': 'WP-30/WP-31 remain blocked until a reproducible stack is installed or supplied.'
    },
    'superseded_plans': superseded_plans,
    'canonical_pointer': {
        'file': 'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md',
        'status': 'ACTIVE_CANONICAL',
        'note': 'The earlier v1.1 pointer content was replaced in place; this path now points exclusively to hierarchical WBS v2 and is not a superseded artifact.',
    },
}

# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------
def unique_ids(items: Iterable[dict[str, Any]], key: str = 'id') -> tuple[bool, list[str]]:
    seen, dup = set(), []
    for x in items:
        val = x[key]
        if val in seen: dup.append(val)
        seen.add(val)
    return (not dup, dup)


def cycle_check(nodes: list[str], deps: dict[str, list[str]]) -> tuple[bool, list[str]]:
    indeg = {n: 0 for n in nodes}
    out = {n: [] for n in nodes}
    for n in nodes:
        for d in deps.get(n, []):
            if d in indeg:
                indeg[n] += 1
                out[d].append(n)
    q = deque([n for n, i in indeg.items() if i == 0])
    order = []
    while q:
        n = q.popleft(); order.append(n)
        for y in out[n]:
            indeg[y] -= 1
            if indeg[y] == 0: q.append(y)
    return len(order) == len(nodes), order


def extract_ids(path: Path, pattern: str) -> set[str]:
    if not path.exists(): return set()
    return set(re.findall(pattern, path.read_text(encoding='utf-8', errors='replace')))

area_ids = {a['id'] for a in areas}
wp_ids = {w['id'] for w in canonical_wps}
tm_ids = {m['id'] for m in modules}
source_ids = {s['id'] for s in source_registry['sources']}
claim_ids = extract_ids(BASE/'CLAIM_LEDGER.md', r'(?<![A-Za-z0-9])Z-\d+(?![A-Za-z0-9])')
proof_ids = extract_ids(BASE/'PROOF_ATTEMPTS.md', r'(?<![A-Za-z0-9])PA-\d+(?![A-Za-z0-9])')
result_ids = extract_ids(BASE/'RESULTS.md', r'(?<![A-Za-z0-9])R-\d+(?![A-Za-z0-9])')
lit_ids = extract_ids(BASE/'LITERATURE_MAP.md', r'(?<![A-Za-z0-9])LIT-\d+(?![A-Za-z0-9])')

validation: dict[str, Any] = {'schema_version': 'hott_z_hierarchical_wbs_validation.v2', 'checked_at_utc': STAMP}
validation['unique_area_ids'] = {'ok': unique_ids(areas)[0], 'duplicates': unique_ids(areas)[1]}
validation['unique_wp_ids'] = {'ok': unique_ids(canonical_wps)[0], 'duplicates': unique_ids(canonical_wps)[1]}
validation['unique_tm_ids'] = {'ok': unique_ids(modules)[0], 'duplicates': unique_ids(modules)[1]}
validation['wp_area_refs'] = {'ok': all(w['area_id'] in area_ids for w in canonical_wps), 'missing': sorted({w['area_id'] for w in canonical_wps if w['area_id'] not in area_ids})}
validation['wp_dependency_refs'] = {'ok': all(d in wp_ids for w in canonical_wps for d in w['dependencies']), 'missing': sorted({d for w in canonical_wps for d in w['dependencies'] if d not in wp_ids})}
validation['tm_parent_refs'] = {'ok': all(m['parent_wp'] in wp_ids for m in modules), 'missing': sorted({m['parent_wp'] for m in modules if m['parent_wp'] not in wp_ids})}
validation['tm_dependency_refs'] = {'ok': all(d in tm_ids for m in modules for d in m.get('dependencies', [])), 'missing': sorted({d for m in modules for d in m.get('dependencies', []) if d not in tm_ids})}
wp_acyclic, wp_topo = cycle_check(sorted(wp_ids), {w['id']: w['dependencies'] for w in canonical_wps})
tm_acyclic, tm_topo = cycle_check(sorted(tm_ids), {m['id']: m.get('dependencies', []) for m in modules})
validation['wp_acyclic'] = {'ok': wp_acyclic, 'topological_order': wp_topo}
validation['tm_acyclic'] = {'ok': tm_acyclic, 'topological_order': tm_topo}
validation['every_wp_has_module'] = {'ok': all(w['task_modules'] for w in canonical_wps), 'missing': [w['id'] for w in canonical_wps if not w['task_modules']]}
validation['source_refs'] = {
    'ok': all(s in source_ids for m in modules for s in m.get('source_refs', [])) and all(s in source_ids for w in canonical_wps for s in w.get('source_refs', [])),
    'missing': sorted(({s for m in modules for s in m.get('source_refs', [])} | {s for w in canonical_wps for s in w.get('source_refs', [])}) - source_ids),
}
validation['claim_refs'] = {'ok': all(x in claim_ids for m in modules for x in m.get('claim_refs', [])), 'missing': sorted({x for m in modules for x in m.get('claim_refs', []) if x not in claim_ids})}
validation['proof_refs'] = {'ok': all(x in proof_ids for m in modules for x in m.get('proof_refs', [])), 'missing': sorted({x for m in modules for x in m.get('proof_refs', []) if x not in proof_ids})}
validation['result_refs'] = {'ok': all(x in result_ids for m in modules for x in m.get('result_refs', [])), 'missing': sorted({x for m in modules for x in m.get('result_refs', []) if x not in result_ids})}
validation['critical_path_refs'] = {'ok': all(x in wp_ids for x in critical_path), 'missing': [x for x in critical_path if x not in wp_ids]}
validation['gate_refs'] = {'ok': all(x in wp_ids for g in gates for x in g['requires']), 'missing': sorted({x for g in gates for x in g['requires'] if x not in wp_ids})}
validation['counts'] = {'areas': len(areas), 'work_packages': len(canonical_wps), 'task_modules': len(modules), 'gates': len(gates), 'risks': len(risks), 'papers': len(publication_portfolio)}
validation['overall_ok'] = all(v.get('ok', True) for k, v in validation.items() if isinstance(v, dict) and 'ok' in v)
program['validation_summary'] = {'overall_ok': validation['overall_ok'], 'validation_file': 'verification/hierarchical_wbs_v2_integrity.json'}

# ---------------------------------------------------------------------------
# Update source registry with reverse links.
# ---------------------------------------------------------------------------
source_to_wps: dict[str, set[str]] = defaultdict(set)
source_to_tms: dict[str, set[str]] = defaultdict(set)
for w in canonical_wps:
    for s in w.get('source_refs', []): source_to_wps[s].add(w['id'])
for m in modules:
    for s in m.get('source_refs', []): source_to_tms[s].add(m['id'])
source_registry['workplan'] = {
    'canonical_plan': 'HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md',
    'canonical_registry': 'HOTT_Z_HIERARCHICAL_WBS_v2.json',
    'version': '2.0',
    'updated_at_utc': STAMP,
}
for s in source_registry['sources']:
    s['linked_work_packages'] = sorted(source_to_wps.get(s['id'], set()))
    s['linked_task_modules'] = sorted(source_to_tms.get(s['id'], set()))

# ---------------------------------------------------------------------------
# Markdown helpers
# ---------------------------------------------------------------------------
def md_list(items: list[str], indent: str = '') -> str:
    if not items: return indent + '- 无。'
    return '\n'.join(f'{indent}- {x}' for x in items)


def ref_list(items: list[str]) -> str:
    return '、'.join(items) if items else '—'

area_by_id = {a['id']: a for a in areas}
wp_by_id = {w['id']: w for w in canonical_wps}
tm_by_id = {m['id']: m for m in modules}

# Main plan markdown.
md: list[str] = []
md.append('# HoTT–Z 相对不完备性研究：后续工作总体方案与分层 WBS v2（规范版）')
md.append('')
md.append(f'**日期**：{DATE}  ')
md.append('**项目编号**：`HOTT-Z-RP-20260831`  ')
md.append('**状态**：`CANONICAL`  ')
md.append('**单一机器事实源**：`HOTT_Z_HIERARCHICAL_WBS_v2.json`')
md.append('')
md.append('> 本文件吸收并取代此前并行产生的 26-WP、14-WP 和 45-WP 三套计划。规范层级固定为：14 个 `AREA` → 26 个 `WP` → 47 个 `TM`。旧计划仅保留作历史记录，不再分配新状态或编号。')
md.append('')
md.append('## 1. 项目使命与严格边界')
md.append('')
md.append('### 1.1 项目使命')
md.append('')
md.append(program['mission'])
md.append('')
md.append('### 1.2 规范中心命题')
md.append('')
md.append('设现实/历史域为 `W`，数学表示域为 `M`，抽象或遗忘映射为 `α : W → M`，目标事实或完整命题—判定谱为 `J`。若同一 `α`-纤维内存在目标真值差异，则不存在只依赖 `M` 的恢复器在全部目标实例上无损恢复 `J`。')
md.append('')
md.append('应用于 HoTT/单价基础时，研究对象不是“不加限定的 HoTT”，而是指定的裸类型—identity/groupoid 表示、指定的遗忘函子或指定的等价自然性要求。')
md.append('')
md.append('### 1.3 明确不做的结论')
md.append('')
md.append(md_list(program['non_goals']))
md.append('')
md.append('## 2. 来源材料如何进入研究')
md.append('')
md.append('源材料承担四种角色：问题发现、思想谱系、反例启发和红队负控制。它们不因篇幅、重复次数或 AI 角色扮演中的“承认”而自动成为数学证据。')
md.append('')
md.append('- `SRC-Z-001` 与 `SRC-FINAL-001`：Z 铁律、Being/Becoming、照片/电影/放映机和极限类比的思想来源。')
md.append('- `SRC-HEEL-001`：资源、未知、表达三条旧攻击；其旧证明被废弃，分别重构为成本非因子化、无通用合成器和语境欠定。')
md.append('- `SRC-SEM-001` 与 `SRC-ID-001`：Nat/Nat′、provenance、角色和历史性；用于签名相对不完备与无免费富化。')
md.append('- `SRC-PROB-*`：断言、相似、mere existence 与具体 witness 的层级区分。')
md.append('- `SRC-SELF-001`：从静态循环转向 guarded/time-delayed dynamics。')
md.append('- `SRC-GODEL/CANTOR/UNIV/MIRROR-*`：只进入独立反射支线或负控制，不进入时间主证明。')
md.append('')
md.append('## 3. 研究架构')
md.append('')
md.append('### 3.1 三层 WBS')
md.append('')
md.append('| 层级 | 数量 | 作用 | 规范编号 |')
md.append('|---|---:|---|---|')
md.append(f'| Program Area | {len(areas)} | 学术领域和资源分流 | `AREA-00`–`AREA-13` |')
md.append(f'| Work Package | {len(canonical_wps)} | 可验收、可阻塞、可交付的主要工作 | `WP-00` 等 26 个稳定 ID |')
md.append(f'| Task Module | {len(modules)} | 定理、形式化、检索或写作的细粒度执行单元 | `TM-000` 等 47 个 ID |')
md.append('')
md.append('### 3.2 四种主要证明机制')
md.append('')
md.append('| ID | 名称 | 准入问题 |')
md.append('|---|---|---|')
for m in mechanisms[:4]:
    md.append(f"| {m['id']} | {m['name']} | {m['criterion']} |")
md.append('')
md.append('### 3.3 证据等级')
md.append('')
md.append('| 等级 | 名称 | 含义 |')
md.append('|---|---|---|')
for e in evidence_levels:
    md.append(f"| {e['id']} | {e['name']} | {e['definition']} |")
md.append('')
md.append('### 3.4 Program Areas')
md.append('')
md.append('| Area | 目标 | Work Packages | 主要产物 |')
md.append('|---|---|---|---|')
for a in areas:
    md.append(f"| {a['id']} {a['title']} | {a['objective']} | {ref_list(a['work_packages'])} | {ref_list(a['target_outputs'])} |")
md.append('')
md.append('## 4. 关键路径、并行轨道与当前阻塞')
md.append('')
md.append('### 4.1 唯一关键路径')
md.append('')
md.append('```text')
md.append(' → '.join(critical_path))
md.append('```')
md.append('')
md.append('此路径的中心不是扩写宏大判决，而是：先冻结理论口径与 Z 核心，再建立可复现工具链，获得 `no-canonical-earlier-event` 的真实机器回执，完成文献和红队审计，最后形成窄 Paper A。')
md.append('')
md.append('### 4.2 并行轨道')
md.append('')
for lane in parallel_lanes:
    md.append(f"- **{lane['id']} {lane['name']}**：`" + ' → '.join(lane['sequence']) + '`.')
md.append('')
md.append('### 4.3 当前工具链事实')
md.append('')
md.append('当前运行环境未发现 `agda`、`lean`、`lake`、`coqc`、`rocq` 或 `rzk`。因此 WP-30 与 WP-31 为真实阻塞状态；任何核心定理在获得编译回执前最多为 E2/E3。')
md.append('')
md.append('## 5. 工作包总览')
md.append('')
md.append('| WP | Area | 优先级 | 状态 | 当前证据 | 依赖 | 论文去向 |')
md.append('|---|---|---|---|---|---|---|')
for w in canonical_wps:
    md.append(f"| {w['id']} {w['title']} | {w['area_id']} | {w['priority']} | {w['status']} | {w['current_evidence']} | {ref_list(w['dependencies'])} | {w.get('paper_target') or '—'} |")
md.append('')
md.append('## 6. 工作包详细分解')
md.append('')
for w in canonical_wps:
    md.append(f"### {w['id']} — {w['title']}")
    md.append('')
    md.append(f"- **Program Area**：{w['area_id']} {area_by_id[w['area_id']]['title']}")
    md.append(f"- **优先级 / 状态 / 证据**：`{w['priority']}` / `{w['status']}` / `{w['current_evidence']}`")
    md.append(f"- **依赖**：{ref_list(w['dependencies'])}")
    md.append(f"- **论文去向**：{w.get('paper_target') or '无直接论文去向'}")
    md.append(f"- **源材料**：{ref_list(w.get('source_refs', []))}")
    md.append(f"- **研究索引**：Claims {ref_list(w.get('claim_refs', []))}；Proofs {ref_list(w.get('proof_refs', []))}；Results {ref_list(w.get('result_refs', []))}")
    md.append('')
    md.append('**目标**')
    md.append('')
    md.append(w['objective'])
    md.append('')
    md.append('**主要任务**')
    md.append('')
    md.append(md_list(w.get('tasks', [])))
    md.append('')
    md.append('**细粒度 Task Modules**')
    md.append('')
    for tid in w['task_modules']:
        t = tm_by_id[tid]
        md.append(f"- `{tid}` — {t['title']}（机制 `{t.get('mechanism','—')}`；状态 `{t.get('status','—')}`）")
    md.append('')
    md.append('**交付物**')
    md.append('')
    md.append(md_list(w.get('deliverables', [])))
    md.append('')
    md.append('**验收标准**')
    md.append('')
    md.append(md_list(w.get('acceptance_criteria', [])))
    md.append('')
    md.append('**失败、降级或拆分条件**')
    md.append('')
    md.append(md_list(w.get('failure_or_split_conditions', [])))
    if w.get('key_risks'):
        md.append('')
        md.append('**关键风险**')
        md.append('')
        md.append(md_list(w['key_risks']))
    md.append('')

md.append('## 7. Task Module 索引')
md.append('')
md.append('| TM | Parent WP | 旧 ID | 机制 | 优先级 | 状态 | 依赖 | 标题 |')
md.append('|---|---|---|---|---|---|---|---|')
for t in sorted(modules, key=lambda x: x['id']):
    md.append(f"| {t['id']} | {t['parent_wp']} | {t.get('legacy_id') or '新增'} | {t.get('mechanism','—')} | {t.get('priority','—')} | {t.get('status','—')} | {ref_list(t.get('dependencies', []))} | {t['title']} |")
md.append('')
md.append('## 8. 阶段门')
md.append('')
for g in gates:
    md.append(f"### {g['id']} — {g['title']}")
    md.append('')
    md.append(f"- **依赖工作包**：{ref_list(g['requires'])}")
    md.append('- **通过标准**：')
    md.append(md_list(g['criteria'], indent='  '))
    md.append(f"- **解锁**：{ref_list(g['unlocks'])}")
    md.append('')
md.append('## 9. 论文组合')
md.append('')
for p in publication_portfolio:
    md.append(f"### {p['id']} — {p['working_title']}")
    md.append('')
    md.append(f"- **工作包**：{ref_list(p['work_packages'])}")
    md.append(f"- **范围**：{ref_list(p['scope'])}")
    md.append(f"- **必须排除**：{ref_list(p['must_exclude'])}")
    md.append('')
md.append('## 10. 当前执行队列')
md.append('')
md.append('| Queue | WP | 优先级 | 状态 | 动作 | 验收产物 |')
md.append('|---|---|---|---|---|---|')
for q in immediate_queue:
    md.append(f"| {q['id']} | {q['work_package']} | {q['priority']} | {q['status']} | {q['action']} | {q['output']} |")
md.append('')
md.append('## 11. 风险登记')
md.append('')
md.append('| Risk | 严重度 | 风险 | 缓解措施 |')
md.append('|---|---|---|---|')
for r in risks:
    md.append(f"| {r['id']} | {r['severity']} | {r['risk']} | {r['mitigation']} |")
md.append('')
md.append('## 12. 变更控制与证据升级纪律')
md.append('')
md.append('1. 任何研究动作必须归属一个 `TM`，并通过其 parent `WP` 汇总。')
md.append('2. 数学真理状态变化必须同步更新 `CLAIM_LEDGER.md`、`PROOF_ATTEMPTS.md`、`RESULTS.md`。')
md.append('3. 文献或归属状态变化必须更新 `LITERATURE_MAP.md` 和 originality matrix。')
md.append('4. WP/TM 状态变化必须更新机器注册表、执行看板和 `RESEARCH_LOG.md`。')
md.append('5. E3 不能替代 E4；第二模型或有限枚举只能作错误探测。')
md.append('6. directed/guarded/linear/cost-aware 富化是合法逃逸路线；它们必须被记录为新增结构，不得被说成裸层免费恢复。')
md.append('7. 任何发现核心定理已知或错误的结果都属于成功的研究产出：定理必须降级、收缩或重新定位，不得隐藏。')
md.append('')
md.append('## 13. 废止与交叉索引')
md.append('')
md.append('以下计划已经被本 v2 吸收，不再是规范事实源：')
md.append('')
for s in superseded_plans:
    md.append(f"- `{s['file']}` — `{s['status']}`；{s['role']}。")
md.append('')
md.append('完整旧 ID → AREA/WP/TM 对照见 `HOTT_Z_WBS_CROSSWALK_v2.md`。')
md.append('')
md.append('## 14. 项目完成定义')
md.append('')
md.append('项目不能以“写完一篇宏大文本”为完成。至少满足：')
md.append('')
md.append('- Paper A 有清晰且窄的中心定理；至少一个 HoTT 特定核心达到 E4，全部关键结论达到 E5/E6。')
md.append('- 公开稿明确不证明 `HoTT ⊢ ⊥`，也不否认合法的时间/方向富化。')
md.append('- 源材料、数学证明、机器源码、一手文献和哲学解释分层可追溯。')
md.append('- 干净环境可复现，所有文件有哈希，所有未解决异议公开。')
md.append('- Paper B/C/D 只有在各自工作包通过后推进，不能反向拖累 Paper A。')
md.append('')

main_plan_path = BASE / 'HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md'
main_plan_path.write_text('\n'.join(md) + '\n', encoding='utf-8')

# Machine-readable registry.
registry_path = BASE / 'HOTT_Z_HIERARCHICAL_WBS_v2.json'
registry_path.write_text(json.dumps(program, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Crosswalk markdown.
cross: list[str] = []
cross.append('# HOTT–Z WBS v2 旧计划—规范层级对照表')
cross.append('')
cross.append(f'**日期**：{DATE}  ')
cross.append('**规范计划**：`HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md`')
cross.append('')
cross.append('## 1. 合并规则')
cross.append('')
cross.append('- 26-WP 计划的工作包 ID 被保留为规范 `WP`。')
cross.append('- 第四轮 14-WP 宏观计划被提升为 14 个 `AREA`，不再占用 `WP` 命名空间。')
cross.append('- 45-WP 细粒度计划全部重命名为 `TM`；另补 `TM-635` 与 `TM-815`，使 Paper C 具备明确写作模块。')
cross.append('')
cross.append('## 2. 26-WP 计划')
cross.append('')
cross.append('| 旧 ID | v2 ID | Area | 状态 |')
cross.append('|---|---|---|---|')
for w in canonical_wps:
    cross.append(f"| {w['id']} | {w['id']} | {w['area_id']} | 保留为规范 WP |")
cross.append('')
cross.append('## 3. 45-WP 细粒度计划')
cross.append('')
cross.append('| 旧 ID | v2 TM | Parent WP | Supporting WPs | 标题 |')
cross.append('|---|---|---|---|---|')
for t in sorted(modules, key=lambda x: x['id']):
    cross.append(f"| {t.get('legacy_id') or '新增'} | {t['id']} | {t['parent_wp']} | {ref_list(t.get('supports_wps', []))} | {t['title']} |")
cross.append('')
cross.append('## 4. 第四轮 14-WP 宏观计划')
cross.append('')
macro_to_area = {
    'WP-00': ['AREA-00'], 'WP-01': ['AREA-10'], 'WP-02': ['AREA-02'], 'WP-03': ['AREA-01', 'AREA-11'],
    'WP-04': ['AREA-03'], 'WP-05': ['AREA-03'], 'WP-06': ['AREA-05'], 'WP-07': ['AREA-06'],
    'WP-08': ['AREA-08'], 'WP-09': ['AREA-04'], 'WP-10': ['AREA-07'], 'WP-11': ['AREA-09'],
    'WP-12': ['AREA-11'], 'WP-13': ['AREA-12', 'AREA-13'],
}
cross.append('| 旧宏观 ID | v2 Program Area | 说明 |')
cross.append('|---|---|---|')
for old in macro_register['work_packages']:
    cross.append(f"| {old['id']} {old['title']} | {ref_list(macro_to_area[old['id']])} | 宏观内容被吸收，旧 ID 不再活动 |")
cross.append('')
cross.append('## 5. 不可再用的旧入口')
cross.append('')
for s in superseded_plans:
    cross.append(f"- `{s['file']}`：{s['role']}；仅作历史版本。")
(BASE / 'HOTT_Z_WBS_CROSSWALK_v2.md').write_text('\n'.join(cross) + '\n', encoding='utf-8')

# Mermaid graph.
graph: list[str] = ['flowchart LR']
for a in areas:
    graph.append(f"  subgraph {a['id'].replace('-','_')}[\"{a['id']} {a['title']}\"]")
    for wid in a['work_packages']:
        label = wp_by_id[wid]['title'].replace('"', "'")
        graph.append(f"    {wid.replace('-','_')}[\"{wid} {label}\"]")
    graph.append('  end')
for w in canonical_wps:
    for d in w['dependencies']:
        graph.append(f"  {d.replace('-','_')} --> {w['id'].replace('-','_')}")
for a, b in zip(critical_path, critical_path[1:]):
    graph.append(f"  {a.replace('-','_')} ==>|critical| {b.replace('-','_')}")
(BASE / 'HOTT_Z_HIERARCHICAL_WBS_v2.mmd').write_text('\n'.join(graph) + '\n', encoding='utf-8')

# Immediate queue file.
queue_md = ['# HOTT–Z 下一执行队列 v2', '', f'**日期**：{DATE}', '', '> 当前唯一不可分散 P0：建立工具链并使 `no-canonical-earlier-event` 获得真实 E4 回执。', '']
for q in immediate_queue:
    queue_md.append(f"## {q['id']} — {q['work_package']} — {q['status']}")
    queue_md.append('')
    queue_md.append(q['action'])
    queue_md.append('')
    queue_md.append(f"**产物**：{q['output']}")
    queue_md.append('')
queue_md.append('## 执行顺序')
queue_md.append('')
queue_md.append('```text')
queue_md.append('AQ-02 → AQ-03 → AQ-04 → AQ-05 → AQ-07 → AQ-09 → AQ-10')
queue_md.append('          ↘ AQ-06（并行文献）   ↘ AQ-08（首个无截面形式化后）')
queue_md.append('```')
queue_md.append('')
(BASE / 'HOTT_Z_下一执行队列_v2.md').write_text('\n'.join(queue_md), encoding='utf-8')

# Updated dashboard.
dash = ['# HOTT–Z 执行看板 v2', '', f'**更新时间**：{DATE}', '', '| WP | 标题 | 状态 | 证据 | 下一动作 |', '|---|---|---|---|---|']
next_action = {q['work_package']: q['action'] for q in immediate_queue}
for w in canonical_wps:
    dash.append(f"| {w['id']} | {w['title']} | {w['status']} | {w['current_evidence']} | {next_action.get(w['id'], '按依赖与验收标准推进')} |")
dash.append('')
dash.append('## 当前瓶颈')
dash.append('')
dash.append('`WP-30`：当前环境没有 Agda/Lean/Rocq/Rzk；因此 `WP-31` 尚不能达到 E4。')
dash.append('')
dash.append('## 当前唯一关键路径')
dash.append('')
dash.append('`' + ' → '.join(critical_path) + '`')
dash.append('')
(BASE / 'HOTT_Z_执行看板.md').write_text('\n'.join(dash), encoding='utf-8')

# Updated gates matrix.
gate_md = ['# HOTT–Z 阶段闸门与验收矩阵 v2', '', f'**日期**：{DATE}', '', '| Gate | 名称 | Requires | 核心验收 | Unlocks |', '|---|---|---|---|---|']
for g in gates:
    gate_md.append(f"| {g['id']} | {g['title']} | {ref_list(g['requires'])} | {'；'.join(g['criteria'])} | {ref_list(g['unlocks'])} |")
gate_md.append('')
gate_md.append('## 不可跨越规则')
gate_md.append('')
gate_md.append('- 未过 G-02，不得使用 `MACHINE_CHECKED`。')
gate_md.append('- 未过 G-03，不得把 Paper A 标成投稿就绪。')
gate_md.append('- 未过 G-05，不得使用“首次”“创建者认为”“学界未发现”等强归属。')
gate_md.append('- 未过 G-07，只能发布研究工作区快照，不能发布“最终证明包”。')
(BASE / 'HOTT_Z_阶段闸门与验收矩阵.md').write_text('\n'.join(gate_md) + '\n', encoding='utf-8')

# Updated risk table.
risk_md = ['# HOTT–Z 风险与红队登记表 v2', '', f'**日期**：{DATE}', '', '| ID | 严重度 | 风险 | 缓解措施 |', '|---|---|---|---|']
for r in risks:
    risk_md.append(f"| {r['id']} | {r['severity']} | {r['risk']} | {r['mitigation']} |")
risk_md.append('')
risk_md.append('## 永久负控制')
risk_md.append('')
risk_md.extend([
    '- ordinary `A→B` 可以非可逆；不得说 HoTT 所有箭头可逆。',
    '- 时间、方向、资源和成本可以通过显式结构富化；问题是是否可从裸层免费恢复。',
    '- `Map(1,G)` 不是环空间；环空间是带基点的自同一类型。',
    '- 宇宙“角色相似”不推出 universe equivalence。',
    '- 量子 successor、观察者维度和旧一次性 transport 不进入活动证明链。',
])
(BASE / 'HOTT_Z_风险与红队登记表.md').write_text('\n'.join(risk_md) + '\n', encoding='utf-8')

# Validation outputs.
verify_dir = BASE / 'verification'
verify_dir.mkdir(exist_ok=True)
(verify_dir / 'hierarchical_wbs_v2_integrity.json').write_text(json.dumps(validation, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
val_lines = [
    'HOTT-Z hierarchical WBS v2 integrity check',
    f'checked_at_utc: {STAMP}',
    f'overall_ok: {str(validation["overall_ok"]).lower()}',
    f'areas: {len(areas)}',
    f'work_packages: {len(canonical_wps)}',
    f'task_modules: {len(modules)}',
    f'gates: {len(gates)}',
    f'risks: {len(risks)}',
    f'papers: {len(publication_portfolio)}',
    f'wp_acyclic: {str(wp_acyclic).lower()}',
    f'tm_acyclic: {str(tm_acyclic).lower()}',
]
for key in ['unique_area_ids','unique_wp_ids','unique_tm_ids','wp_area_refs','wp_dependency_refs','tm_parent_refs','tm_dependency_refs','every_wp_has_module','source_refs','claim_refs','proof_refs','result_refs','critical_path_refs','gate_refs']:
    val_lines.append(f'{key}: {str(validation[key]["ok"]).lower()}')
    if validation[key].get('missing'): val_lines.append(f'  missing: {validation[key]["missing"]}')
    if validation[key].get('duplicates'): val_lines.append(f'  duplicates: {validation[key]["duplicates"]}')
(verify_dir / 'hierarchical_wbs_v2_integrity.txt').write_text('\n'.join(val_lines) + '\n', encoding='utf-8')

# Source registry update after validation.
(BASE / 'HOTT_Z_SOURCE_REGISTRY.json').write_text(json.dumps(source_registry, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Baseline lock with input/output hashes.
def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

baseline_inputs = [
    'archive/superseded_workplans_20260831/26_wp_plan_superseded/HOTT_Z_WORK_PACKAGE_REGISTER.json',
    'archive/superseded_workplans_20260831/14_wp_round4_plan_superseded/HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json',
    'HOTT_Z_WBS_REGISTRY_v1.json',
    'HOTT_Z_SOURCE_REGISTRY.json', 'CLAIM_LEDGER.md', 'PROOF_ATTEMPTS.md', 'RESULTS.md', 'LITERATURE_MAP.md',
    'HOTT_Z_后续研究可用性总索引_第三轮.md', 'HOTT_Z_内生时间不完备性_论文草案_v3.md',
    'HOTT_Z_内生时间不完备性_论文草案_v4_候选.md',
]
lock = {
    'schema_version': 'hott_z_program_baseline.v2', 'date': DATE, 'generated_at_utc': STAMP,
    'canonical_plan': main_plan_path.name, 'canonical_registry': registry_path.name,
    'input_files': [], 'toolchain_check': program['current_toolchain_facts'],
}
for name in baseline_inputs:
    p = BASE / name
    if p.exists():
        lock['input_files'].append({'file': name, 'bytes': p.stat().st_size, 'sha256': sha256(p)})
(BASE / 'HOTT_Z_PROGRAM_BASELINE_v2.json').write_text(json.dumps(lock, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Mark old markdown plans as superseded without deleting historical content.
supersede_note = (
    '> **SUPERSEDED_NONCANONICAL — 2026-08-31**  \n'
    '> 本文件已被 `HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md` 吸收。'
    '保留作历史版本；不得再作为活动编号、状态或执行顺序的事实源。\n\n'
)
for name in ['HOTT_Z_后续工作总方案与工作包分解_v1.md', 'HOTT_Z_后续工作总体方案与工作包分解_第四轮.md', 'HOTT_Z_后续工作总方案与WBS_v1.md', 'HOTT_Z_下一执行批次_P0P1.md', 'HOTT_Z_下一执行队列_第四轮.md', 'HOTT_Z_工作包—来源—主张追踪矩阵_v1_1.md', 'HOTT_Z_后续工作执行摘要_规范版.md']:
    p = BASE / name
    if p.exists():
        text = p.read_text(encoding='utf-8')
        if not text.startswith('> **SUPERSEDED_NONCANONICAL'):
            p.write_text(supersede_note + text, encoding='utf-8')

# Mark old JSON registries as noncanonical, preserving their data.
for name in ['HOTT_Z_WORK_PACKAGE_REGISTER.json', 'HOTT_Z_WORK_BREAKDOWN_STRUCTURE.json', 'HOTT_Z_WBS_REGISTRY_v1.json']:
    p = BASE / name
    if p.exists():
        d = json.loads(p.read_text(encoding='utf-8'))
        d['canonical'] = False
        d['status'] = 'SUPERSEDED_NONCANONICAL'
        d['superseded_by'] = 'HOTT_Z_HIERARCHICAL_WBS_v2.json'
        d['superseded_at'] = DATE
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Replace AGENTS plan section from first section 26 onward with one canonical section.
agents_path = BASE / 'AGENTS.md'
agents = agents_path.read_text(encoding='utf-8')
pos = agents.find('\n## 26.')
if pos == -1:
    pos = len(agents)
canonical_agents_section = f'''\n\n## 26. HOTT–Z 分层 WBS v2：唯一后续工作治理基线（{DATE}）\n\n### 26.1 唯一规范入口\n\n- 人类可读总方案：`HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md`；\n- 机器事实源：`HOTT_Z_HIERARCHICAL_WBS_v2.json`；\n- 旧计划对照：`HOTT_Z_WBS_CROSSWALK_v2.md`；\n- 依赖图：`HOTT_Z_HIERARCHICAL_WBS_v2.mmd`；\n- 当前执行队列：`HOTT_Z_下一执行队列_v2.md`；\n- 阶段门：`HOTT_Z_阶段闸门与验收矩阵.md`；\n- 风险与红队：`HOTT_Z_风险与红队登记表.md`；\n- 完整性回执：`verification/hierarchical_wbs_v2_integrity.*`。\n\n任何旧 26-WP、14-WP 或 45-WP 计划均为 `SUPERSEDED_NONCANONICAL`。发生冲突时，只能以本节和 v2 机器注册表为准。\n\n### 26.2 三层编号制度\n\n- `AREA-00`–`AREA-13`：14 个 Program Areas，只用于学术分流；\n- 26 个稳定 `WP`：可验收、可阻塞、可交付的工作包；\n- 46 个 `TM`：细粒度任务模块。旧 45-WP 细计划全部转换为 `TM`，另补 `TM-635` 与 `TM-815` 作为 Paper C 组装模块。\n\n新工作不得创造第四套 WP 编号。任何行动先进入一个 TM，再汇总到其 parent WP。\n\n### 26.3 唯一关键路径\n\n```text\n{' → '.join(critical_path)}\n```\n\n中央 P0 是：锁定理论口径与 Z 核心，建立可复现证明助理环境，使 `no-canonical-earlier-event` 获得真实 E4 回执，再完成文献、红队和 Paper A。\n\n### 26.4 证据等级与阶段门\n\n证据等级固定为 E0–E7。E3 有限程序核验不得替代 E4 证明助理通过。阶段门固定为 G-00–G-07；未过 G-03 不得把 Paper A 标记为投稿就绪，未过 G-05 不得宣称“首次”“推翻”或归属于 HoTT 创建者。\n\n### 26.5 当前工具链事实\n\n当前环境未发现 `agda`、`lean`、`lake`、`coqc`、`rocq` 或 `rzk`。因此 WP-30 与 WP-31 是真实阻塞；在安装、版本锁定和 smoke test 前不得声称机器化。\n\n### 26.6 论文分流\n\n- Paper A：Z 因子化、单价无规范时间定向、群胚 core/时间反演和必要历史富化；\n- Paper B：provenance、intended role、语境、资源、成本和 witness；\n- Paper C：future stabilization、inhabitation synthesis 和 canonicalization；\n- Paper D：Lawvere/Gödel、反射、宇宙、resizing/predicativity，保持隔离；\n- 哲学伴随稿：Being/Becoming、Zeno、照片/电影/放映机，不承担形式证明。\n\n### 26.7 状态更新纪律\n\n1. WP/TM 状态变化必须更新 `HOTT_Z_HIERARCHICAL_WBS_v2.json`、`HOTT_Z_执行看板.md` 和 `RESEARCH_LOG.md`。\n2. 数学真理变化同步更新 Claim/Proof/Result 台账；文献变化同步更新 `LITERATURE_MAP.md`。\n3. 旧失败攻击只作负控制，不得重新进入主证明。\n4. 任何定理若被发现已知、错误或依赖更强假设，必须立即降级、收缩或拆分；不得隐藏。\n'''
agents_path.write_text(agents[:pos].rstrip() + canonical_agents_section, encoding='utf-8')

# Rewrite current index as a clean single-source index.
idx: list[str] = []
idx.append('# HOTT–Z 当前研究总索引')
idx.append('')
idx.append(f'**更新时间**：{DATE}  ')
idx.append('**当前阶段**：分层 WBS v2 已建立；进入理论剖面、Z core、工具链和首个机器定理的关键路径。  ')
idx.append('**规范边界**：研究目标是相对于时间、历史、语境、资源、见证和有效求解的表示/自然性/判定不完备；当前没有证明 `HoTT ⊢ ⊥`，也没有证明 HoTT 完全不能编码动态结构。')
idx.append('')
idx.append('## 1. 唯一项目入口')
idx.append('')
idx.append('1. `HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md` — 完整项目章程和 WBS。')
idx.append('2. `HOTT_Z_HIERARCHICAL_WBS_v2.json` — AREA/WP/TM、依赖、状态、闸门、风险和论文的机器事实源。')
idx.append('3. `HOTT_Z_下一执行队列_v2.md` — 当前 P0/P1 执行队列。')
idx.append('4. `HOTT_Z_WBS_CROSSWALK_v2.md` — 三套旧计划到 v2 的对照。')
idx.append('5. `HOTT_Z_HIERARCHICAL_WBS_v2.mmd` — 依赖图。')
idx.append('6. `HOTT_Z_阶段闸门与验收矩阵.md`、`HOTT_Z_风险与红队登记表.md`、`HOTT_Z_执行看板.md`。')
idx.append('')
idx.append('## 2. 数学与来源入口')
idx.append('')
idx.append('- `HOTT_Z_后续研究可用性总索引_第三轮.md`：逐来源可用内核、失败路线和 M1–M4 分类。')
idx.append('- `HOTT_Z_SOURCE_REGISTRY.json`：来源谱系、哈希、重复关系和反向 WP/TM 链接。')
idx.append('- `HOTT_Z_内生时间不完备性_论文草案_v3.md`：当前规范数学主稿。')
idx.append('- `HOTT_Z_内生时间不完备性_论文草案_v4_候选.md`：候选整合稿，尚未替代 v3。')
idx.append('- `Z_LAW_CANONICAL_FORM.md`、`HOTT_Z_无免费富化与历史约化定理.md`、`HOTT_Z_结构同一原则下的语义角色与操作不完备性定理.md`。')
idx.append('- `CLAIM_LEDGER.md`、`PROOF_ATTEMPTS.md`、`RESULTS.md`、`LITERATURE_MAP.md`、`RESEARCH_LOG.md`。')
idx.append('')
idx.append('## 3. 当前最稳固结论')
idx.append('')
idx.extend([
    '1. 抽象纤维内若目标真值变化，目标事实不能经该抽象无损因子化。',
    '2. 裸二事件类型在等价自然性下不存在免费规范的“较早事件”选择。',
    '3. 时间反演的过程可具有相同可逆 core，却在方向命题上真值相反。',
    '4. provenance、originality、intended role、context 和 operation cost 若被遗忘，就不能仅由裸结构恢复。',
    '5. 布尔断言、命题截断存在与具体 witness 是不同证据层；统一抽取需要额外选择结构。',
    '6. 某些时间轨道压成单一静态值并保持更新律时必须产生固定点；无固定点过程不能如此无损静态化。',
    '7. 在固定有效演算和明确归约下，未来稳定性、inhabitation synthesis 与 canonicalization 可出现不可总判定边界。',
])
idx.append('')
idx.append('## 4. 四种证明机制')
idx.append('')
for m in mechanisms[:4]: idx.append(f"- **{m['id']} {m['name']}**：{m['criterion']}")
idx.append('')
idx.append('## 5. 当前工作结构')
idx.append('')
idx.append(f'- 14 个 Program Areas；26 个规范 Work Packages；47 个 Task Modules；8 个阶段门；15 项活动风险。')
idx.append('- 关键路径：`' + ' → '.join(critical_path) + '`。')
idx.append('- 当前工具链不存在，WP-30/WP-31 阻塞；Paper A 不得提前升级。')
idx.append('')
idx.append('## 6. 下一执行批次')
idx.append('')
for q in immediate_queue[1:]: idx.append(f"- `{q['id']}` / `{q['work_package']}` / `{q['status']}`：{q['action']}")
idx.append('')
idx.append('## 7. 永久红队边界')
idx.append('')
idx.extend([
    '- ordinary `A→B` 可非可逆；主定理必须限定 identity/core 或明确遗忘映射。',
    '- directed、guarded、linear、clocked、cost-aware 富化是合法方案；它们说明新增结构承担区分工作。',
    '- axiomatic HoTT 与 cubical/computational variants 必须区分。',
    '- 一次性 transport、`Map(1,G)=ΩG`、同层全包 universe、宇宙角色相似、观察者维度、量子 successor 永久隔离。',
    '- AI 对话是思想谱系，不是数学或历史归属证据。',
])
idx.append('')
idx.append('## 8. 历史计划状态')
idx.append('')
for s in superseded_plans: idx.append(f"- `{s['file']}`：`SUPERSEDED_NONCANONICAL`；{s['role']}。")
idx.append('')
idx.append('## 9. 完整性状态')
idx.append('')
idx.append(f"- 分层 WBS 校验：`overall_ok = {str(validation['overall_ok']).lower()}`。")
idx.append('- 回执：`verification/hierarchical_wbs_v2_integrity.json` 与 `.txt`。')
idx.append('- 旧计划内容未删除，已备份并保留交叉索引；活动事实源只有 v2。')
(BASE / 'CURRENT_RESEARCH_INDEX.md').write_text('\n'.join(idx) + '\n', encoding='utf-8')

# Append research log.
log_path = BASE / 'RESEARCH_LOG.md'
log = log_path.read_text(encoding='utf-8')
entry = f'''\n\n## {DATE} — 三套竞争工作计划合并为分层 WBS v2\n\n### 发现的问题\n\n工作区同时存在 26-WP、14-WP 和 45-WP 三套自称规范的计划，且 `AGENTS.md` 与 `CURRENT_RESEARCH_INDEX.md` 同时指向不同入口。若继续执行，会造成 WP 编号碰撞、状态漂移和两个“单一事实源”。\n\n### 合并决策\n\n1. 14-WP 宏观计划转换为 `AREA-00`–`AREA-13`；\n2. 26-WP 计划保留为稳定 `WP`；\n3. 45-WP 细计划全部转换为 `TM`，并新增 `TM-815` 补齐 Paper C；\n4. 建立 8 个统一阶段门、15 项风险和唯一关键路径；\n5. 旧计划均标记 `SUPERSEDED_NONCANONICAL`，不删除历史内容；\n6. `AGENTS.md` 第 26 节和 `CURRENT_RESEARCH_INDEX.md` 重写为单一入口。\n\n### 当前事实\n\n- 14 Areas / 26 WPs / 46 TMs；\n- WP/TM 依赖图均无环；\n- Source/Claim/Proof/Result 引用完整；\n- 当前环境未发现 Agda、Lean、Rocq/Coq 或 Rzk，WP-30/WP-31 仍受工具链阻塞；\n- 完整性检查：`overall_ok = {str(validation['overall_ok']).lower()}`。\n\n### 新建/更新\n\n- `HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md`；\n- `HOTT_Z_HIERARCHICAL_WBS_v2.json`；\n- `HOTT_Z_WBS_CROSSWALK_v2.md`；\n- `HOTT_Z_HIERARCHICAL_WBS_v2.mmd`；\n- `HOTT_Z_下一执行队列_v2.md`；\n- `HOTT_Z_PROGRAM_BASELINE_v2.json`；\n- `verification/hierarchical_wbs_v2_integrity.*`；\n- `AGENTS.md`、`CURRENT_RESEARCH_INDEX.md`、`HOTT_Z_SOURCE_REGISTRY.json`、执行看板、阶段门和风险表。\n'''
log_path.write_text(log.rstrip() + entry + '\n', encoding='utf-8')

# Rewrite the canonical pointer to v2.
pointer = [
    '# HOTT–Z 规范工作计划指针', '',
    '**当前唯一活动版本**：分层 WBS v2  ',
    f'**生效日期**：{DATE}  ', '',
    '## 规范入口', '',
    '1. `HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md`；',
    '2. `HOTT_Z_HIERARCHICAL_WBS_v2.json`；',
    '3. `HOTT_Z_WBS_CROSSWALK_v2.md`；',
    '4. `HOTT_Z_HIERARCHICAL_WBS_v2.mmd`；',
    '5. `HOTT_Z_下一执行队列_v2.md`；',
    '6. `HOTT_Z_执行看板.md`、`HOTT_Z_阶段闸门与验收矩阵.md`、`HOTT_Z_风险与红队登记表.md`。', '',
    '## 层级', '',
    '- 14 个 `AREA`；',
    '- 26 个规范 `WP`；',
    '- 47 个 `TM`。', '',
    '旧 26-WP、14-WP 与 45-WP/v1.1 计划均为历史版本，不得再作为活动状态或编号事实源。',
]
(BASE / 'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md').write_text('\n'.join(pointer) + '\n', encoding='utf-8')

# Final manifest and zip.
artifact_names = [
    'HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md',
    'HOTT_Z_HIERARCHICAL_WBS_v2.json',
    'HOTT_Z_WBS_CROSSWALK_v2.md',
    'HOTT_Z_HIERARCHICAL_WBS_v2.mmd',
    'HOTT_Z_下一执行队列_v2.md',
    'HOTT_Z_PROGRAM_BASELINE_v2.json',
    'HOTT_Z_执行看板.md',
    'HOTT_Z_阶段闸门与验收矩阵.md',
    'HOTT_Z_风险与红队登记表.md',
    'CURRENT_RESEARCH_INDEX.md',
    'AGENTS.md',
    'RESEARCH_LOG.md',
    'HOTT_Z_SOURCE_REGISTRY.json',
    'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md',
    'verification/hierarchical_wbs_v2_integrity.json',
    'verification/hierarchical_wbs_v2_integrity.txt',
    '_build_hierarchical_wbs_v2.py',
]
manifest_lines = []
for name in artifact_names:
    p = BASE / name
    manifest_lines.append(f'{sha256(p)}  {name}')
manifest_path = BASE / 'HOTT_Z_WORKPLAN_V2_MANIFEST.sha256'
manifest_path.write_text('\n'.join(manifest_lines) + '\n', encoding='utf-8')
artifact_names.append(manifest_path.name)

zip_path = BASE / 'HOTT_Z_workplan_hierarchical_v2_20260831.zip'
with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    for name in artifact_names:
        zf.write(BASE / name, arcname=name)

summary = {
    'overall_ok': validation['overall_ok'],
    'areas': len(areas), 'work_packages': len(canonical_wps), 'task_modules': len(modules),
    'gates': len(gates), 'risks': len(risks), 'papers': len(publication_portfolio),
    'zip': zip_path.name, 'zip_bytes': zip_path.stat().st_size, 'zip_sha256': sha256(zip_path),
    'main_plan_lines': len(main_plan_path.read_text(encoding='utf-8').splitlines()),
    'main_plan_bytes': main_plan_path.stat().st_size,
    'registry_bytes': registry_path.stat().st_size,
    'backup_dir': str(BACKUP),
}
print(json.dumps(summary, ensure_ascii=False, indent=2))
if not validation['overall_ok']:
    raise SystemExit(2)

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/5ac201e3a9146e2b3ca0/no-canonical-earlier-event.agda | SHA256 5ac201e3a9146e2b3ca0c7eecf5bc4fe30946b0150e8aeb22146f6fcffc0197f | LINES 1-13/13 =====
module hott-z.no-canonical-earlier-event where

open import foundation.negation
open import foundation.universe-levels
open import univalent-combinatorics.2-element-types

EarlierEvent : {l : Level} → 2-Element-Type l → UU l
EarlierEvent X = type-2-Element-Type X

-- This is an interpretive wrapper around the upstream theorem.
no-canonical-earlier-event :
  {l : Level} → ¬ ((X : 2-Element-Type l) → EarlierEvent X)
no-canonical-earlier-event = no-section-type-2-Element-Type

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/5c9a9706a846c29e9e14/validate_hierarchical_wbs_v2.py | SHA256 5c9a9706a846c29e9e142444c4133f43da01606614774a095850985b29d37706 | LINES 1-252/252 =====
from __future__ import annotations

from collections import Counter, defaultdict, deque
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import zipfile

BASE = Path('/mnt/data')
REGISTRY = BASE / 'HOTT_Z_HIERARCHICAL_WBS_v2.json'
SOURCE_REGISTRY = BASE / 'HOTT_Z_SOURCE_REGISTRY.json'
POINTER = BASE / 'HOTT_Z_WORKPLAN_CANONICAL_POINTER.md'


def duplicates(values: list[str]) -> list[str]:
    return sorted(k for k, v in Counter(values).items() if v > 1)


def topo(nodes: set[str], deps: dict[str, list[str]]) -> tuple[bool, list[str], list[str]]:
    incoming = {n: 0 for n in nodes}
    outgoing: dict[str, list[str]] = defaultdict(list)
    missing: list[str] = []
    for n in nodes:
        for d in deps.get(n, []):
            if d not in nodes:
                missing.append(f'{n}->{d}')
                continue
            incoming[n] += 1
            outgoing[d].append(n)
    q = deque(sorted(n for n, deg in incoming.items() if deg == 0))
    order: list[str] = []
    while q:
        n = q.popleft()
        order.append(n)
        for m in sorted(outgoing[n]):
            incoming[m] -= 1
            if incoming[m] == 0:
                q.append(m)
    cycle = sorted(n for n, deg in incoming.items() if deg > 0)
    return not missing and not cycle and len(order) == len(nodes), order, sorted(set(missing + cycle))


def ids_in_file(path: Path, pattern: str) -> set[str]:
    return set(re.findall(pattern, path.read_text(encoding='utf-8')))


def result(ok: bool, **details):
    return {'ok': bool(ok), **details}


def main() -> None:
    d = json.loads(REGISTRY.read_text(encoding='utf-8'))
    sreg = json.loads(SOURCE_REGISTRY.read_text(encoding='utf-8'))

    areas = d['areas']
    wps = d['work_packages']
    tms = d['task_modules']
    gates = d['gates']

    area_ids = [x['id'] for x in areas]
    wp_ids = [x['id'] for x in wps]
    tm_ids = [x['id'] for x in tms]
    gate_ids = [x['id'] for x in gates]
    area_set, wp_set, tm_set = set(area_ids), set(wp_ids), set(tm_ids)

    wp_by = {x['id']: x for x in wps}
    tm_by = {x['id']: x for x in tms}

    source_ids = {x['id'] for x in sreg.get('sources', [])}
    claim_ids = ids_in_file(BASE/'CLAIM_LEDGER.md', r'\bZ-\d+\b')
    proof_ids = ids_in_file(BASE/'PROOF_ATTEMPTS.md', r'\bPA-\d+\b')
    result_ids = ids_in_file(BASE/'RESULTS.md', r'\bR-\d+\b')
    literature_ids = ids_in_file(BASE/'LITERATURE_MAP.md', r'\bLIT-\d+\b')

    wp_dep = {x['id']: x.get('dependencies', []) for x in wps}
    tm_dep = {x['id']: x.get('dependencies', []) for x in tms}
    wp_acyclic, wp_order, wp_cycle_or_missing = topo(wp_set, wp_dep)
    tm_acyclic, tm_order, tm_cycle_or_missing = topo(tm_set, tm_dep)

    wp_area_missing = sorted(f"{x['id']}->{x.get('area_id')}" for x in wps if x.get('area_id') not in area_set)
    area_wp_missing = sorted(
        f"{a['id']}->{wid}" for a in areas for wid in a.get('work_packages', []) if wid not in wp_set
    )
    area_wp_mismatch = sorted(
        f"{a['id']}->{wid}" for a in areas for wid in a.get('work_packages', [])
        if wid in wp_by and wp_by[wid].get('area_id') != a['id']
    )

    tm_parent_missing = sorted(f"{x['id']}->{x.get('parent_wp')}" for x in tms if x.get('parent_wp') not in wp_set)
    wp_tm_missing = sorted(f"{w['id']}->{tid}" for w in wps for tid in w.get('task_modules', []) if tid not in tm_set)
    wp_tm_mismatch = sorted(
        f"{w['id']}->{tid}" for w in wps for tid in w.get('task_modules', [])
        if tid in tm_by and tm_by[tid].get('parent_wp') != w['id']
    )
    tm_not_listed_by_parent = sorted(
        f"{t['id']}->{t['parent_wp']}" for t in tms
        if t['id'] not in wp_by[t['parent_wp']].get('task_modules', [])
    )
    every_wp_has_module = sorted(w['id'] for w in wps if not w.get('task_modules'))

    source_ref_missing = []
    claim_ref_missing = []
    proof_ref_missing = []
    result_ref_missing = []
    literature_ref_missing = []
    for kind, items in [('WP', wps), ('TM', tms)]:
        for x in items:
            for ref in x.get('source_refs', []):
                if ref not in source_ids: source_ref_missing.append(f"{kind}:{x['id']}->{ref}")
            for ref in x.get('claim_refs', []):
                if ref not in claim_ids: claim_ref_missing.append(f"{kind}:{x['id']}->{ref}")
            for ref in x.get('proof_refs', []):
                if ref not in proof_ids: proof_ref_missing.append(f"{kind}:{x['id']}->{ref}")
            for ref in x.get('result_refs', []):
                if ref not in result_ids: result_ref_missing.append(f"{kind}:{x['id']}->{ref}")
            for ref in x.get('literature_refs', []):
                if ref not in literature_ids: literature_ref_missing.append(f"{kind}:{x['id']}->{ref}")

    reverse_source_missing = []
    for src in sreg.get('sources', []):
        for wid in src.get('linked_work_packages', []):
            if wid not in wp_set: reverse_source_missing.append(f"{src['id']}->WP:{wid}")
        for tid in src.get('linked_task_modules', []):
            if tid not in tm_set: reverse_source_missing.append(f"{src['id']}->TM:{tid}")

    gate_ref_missing = []
    for g in gates:
        for wid in g.get('requires', []):
            if wid not in wp_set: gate_ref_missing.append(f"{g['id']}:requires->{wid}")
        for target in g.get('unlocks', []):
            if target.startswith('WP-') and target not in wp_set:
                gate_ref_missing.append(f"{g['id']}:unlocks->{target}")

    critical_missing = sorted(x for x in d.get('critical_path', []) if x not in wp_set)

    pointer_name = POINTER.name
    superseded_files = {x.get('file') for x in d.get('superseded_plans', [])}
    pointer_text = POINTER.read_text(encoding='utf-8')
    pointer_json = d.get('canonical_pointer', {})
    pointer_ok = (
        pointer_name not in superseded_files
        and pointer_json.get('file') == pointer_name
        and pointer_json.get('status') == 'ACTIVE_CANONICAL'
        and '当前唯一活动版本' in pointer_text
        and '分层 WBS v2' in pointer_text
    )

    text_files = [
        BASE/'HOTT_Z_后续工作总体方案与分层WBS_v2_规范.md',
        BASE/'CURRENT_RESEARCH_INDEX.md',
        BASE/'HOTT_Z_WBS_CROSSWALK_v2.md',
    ]
    contradictory_pointer_lines = []
    for path in text_files:
        for i, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if pointer_name in line and ('SUPERSEDED_NONCANONICAL' in line or '仅作历史版本' in line):
                contradictory_pointer_lines.append(f'{path.name}:{i}:{line}')

    agents_text = (BASE/'AGENTS.md').read_text(encoding='utf-8')
    agents_section_count = len(re.findall(r'^## 26\b', agents_text, flags=re.M))
    agents_ok = agents_section_count == 1 and 'HOTT_Z_HIERARCHICAL_WBS_v2.json' in agents_text

    old_registry = BASE/'HOTT_Z_WBS_REGISTRY_v1.json'
    old_registry_ok = True
    old_registry_state = None
    if old_registry.exists():
        old = json.loads(old_registry.read_text(encoding='utf-8'))
        old_registry_state = {k: old.get(k) for k in ('canonical', 'status', 'superseded_by')}
        old_registry_ok = (
            old.get('canonical') is False
            and old.get('status') == 'SUPERSEDED_NONCANONICAL'
            and old.get('superseded_by') == REGISTRY.name
        )

    checks = {
        'unique_area_ids': result(not duplicates(area_ids), duplicates=duplicates(area_ids)),
        'unique_wp_ids': result(not duplicates(wp_ids), duplicates=duplicates(wp_ids)),
        'unique_tm_ids': result(not duplicates(tm_ids), duplicates=duplicates(tm_ids)),
        'unique_gate_ids': result(not duplicates(gate_ids), duplicates=duplicates(gate_ids)),
        'wp_area_refs': result(not (wp_area_missing or area_wp_missing or area_wp_mismatch), missing=wp_area_missing+area_wp_missing+area_wp_mismatch),
        'wp_dependency_refs_and_acyclicity': result(wp_acyclic, topological_order=wp_order, issues=wp_cycle_or_missing),
        'tm_parent_and_wp_crossrefs': result(not (tm_parent_missing or wp_tm_missing or wp_tm_mismatch or tm_not_listed_by_parent), missing=tm_parent_missing+wp_tm_missing+wp_tm_mismatch+tm_not_listed_by_parent),
        'tm_dependency_refs_and_acyclicity': result(tm_acyclic, topological_order=tm_order, issues=tm_cycle_or_missing),
        'every_wp_has_module': result(not every_wp_has_module, missing=every_wp_has_module),
        'source_refs': result(not source_ref_missing, missing=sorted(source_ref_missing)),
        'source_reverse_refs': result(not reverse_source_missing, missing=sorted(reverse_source_missing)),
        'claim_refs': result(not claim_ref_missing, missing=sorted(claim_ref_missing)),
        'proof_refs': result(not proof_ref_missing, missing=sorted(proof_ref_missing)),
        'result_refs': result(not result_ref_missing, missing=sorted(result_ref_missing)),
        'literature_refs': result(not literature_ref_missing, missing=sorted(literature_ref_missing)),
        'critical_path_refs': result(not critical_missing, missing=critical_missing),
        'gate_refs': result(not gate_ref_missing, missing=sorted(gate_ref_missing)),
        'canonical_pointer_invariant': result(pointer_ok, superseded=pointer_name in superseded_files, pointer_record=pointer_json),
        'human_text_pointer_consistency': result(not contradictory_pointer_lines, conflicts=contradictory_pointer_lines),
        'agents_single_canonical_section': result(agents_ok, section_26_count=agents_section_count),
        'old_v1_registry_is_noncanonical': result(old_registry_ok, state=old_registry_state),
    }

    counts = {
        'areas': len(areas),
        'work_packages': len(wps),
        'task_modules': len(tms),
        'gates': len(gates),
        'risks': len(d.get('risks', [])),
        'papers': len(d.get('publication_portfolio', [])),
        'sources': len(sreg.get('sources', [])),
    }
    expected_counts = {'areas':14,'work_packages':26,'task_modules':47,'gates':8,'risks':15,'papers':5}
    checks['expected_counts'] = result(all(counts[k] == v for k,v in expected_counts.items()), actual=counts, expected=expected_counts)

    overall = all(v['ok'] for v in checks.values())
    report = {
        'schema_version': 'hott_z_hierarchical_wbs_validation.v2.1',
        'checked_at_utc': datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'),
        'registry': REGISTRY.name,
        'checks': checks,
        'counts': counts,
        'overall_ok': overall,
    }

    out_json = BASE/'verification/hierarchical_wbs_v2_integrity.json'
    out_txt = BASE/'verification/hierarchical_wbs_v2_integrity.txt'
    final_json = BASE/'verification/hierarchical_wbs_v2_final_check.json'
    final_txt = BASE/'verification/hierarchical_wbs_v2_final_check.txt'
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    out_json.write_text(encoded, encoding='utf-8')
    final_json.write_text(encoded, encoding='utf-8')

    lines = [
        f"overall_ok: {str(overall).lower()}",
        *[f"{name}: {str(info['ok']).lower()}" for name, info in checks.items()],
        *[f"{k}: {v}" for k,v in counts.items()],
    ]
    if not overall:
        lines.append('FAILED_CHECK_DETAILS:')
        for name, info in checks.items():
            if not info['ok']:
                lines.append(f'- {name}: {json.dumps(info, ensure_ascii=False)}')
    text = '\n'.join(lines) + '\n'
    out_txt.write_text(text, encoding='utf-8')
    final_txt.write_text(text, encoding='utf-8')

    print(text, end='')
    if not overall:
        raise SystemExit(1)

if __name__ == '__main__':
    main()

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/61a764ef0830900c018c/no-canonical-temporal-order.agda | SHA256 61a764ef0830900c018c53de0e253cfac815bd92c1bb4369bfff9d08f73bafc4 | LINES 1-25/25 =====
module no-canonical-temporal-order where

open import foundation.negation
open import foundation.universe-levels
open import univalent-combinatorics.2-element-types

-- Any temporal structure from which an earliest event can be extracted would
-- induce the forbidden global section. This covers strict total orders on a
-- two-element carrier once their unique minimum operation is supplied.
module _
  {l1 l2 : Level}
  (Temporal-Structure : UU l1 → UU l2)
  (earliest : (A : UU l1) → Temporal-Structure A → A)
  where

  Canonical-Temporal-Structure : UU (lsuc l1 ⊔ l2)
  Canonical-Temporal-Structure =
    (X : 2-Element-Type l1) →
    Temporal-Structure (type-2-Element-Type X)

  no-canonical-temporal-structure :
    ¬ Canonical-Temporal-Structure
  no-canonical-temporal-structure F =
    no-section-type-2-Element-Type
      (λ X → earliest (type-2-Element-Type X) (F X))

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/62c80dd7f28427316e55/FixedPointFreeMonodromy.agda | SHA256 62c80dd7f28427316e55703db2a7207e764d8a7f2705abbd7d023a4e3d3c77bc | LINES 1-24/24 =====
module FixedPointFreeMonodromy where

open import Agda.Primitive using (Level)
open import Agda.Builtin.Equality using (_≡_; refl)

data ⊥ : Set where

¬_ : ∀ {ℓ} → Set ℓ → Set ℓ
¬ A = A → ⊥

transport : ∀ {ℓ ℓ'} {A : Set ℓ} (P : A → Set ℓ') {x y : A} → x ≡ y → P x → P y
transport P refl u = u

apd : ∀ {ℓ ℓ'} {A : Set ℓ} {P : A → Set ℓ'} (s : (x : A) → P x)
    {x y : A} (p : x ≡ y) → transport P p (s x) ≡ s y
apd s refl = refl

noSectionFromFixedPointFreeMonodromy :
  ∀ {ℓ ℓ'} {B : Set ℓ} (P : B → Set ℓ')
  (b : B) (loop : b ≡ b)
  → ((u : P b) → ¬ (transport P loop u ≡ u))
  → ¬ ((x : B) → P x)
noSectionFromFixedPointFreeMonodromy P b loop fixedPointFree s =
  fixedPointFree (s b) (apd s loop)

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/63f7b27a7a0177deca66/TwoEvent.lean | SHA256 63f7b27a7a0177deca66b7a8202ca7e86a63a28664705420e60a8c819682c256 | LINES 1-51/51 =====
/-!
Second-system specification for the finite automorphism obstruction.
This file is intentionally self-contained Lean 4 source.  It was not locally
compiled in the current runtime because no Lean executable was available.
-/

inductive Event where
  | left
  | right
  deriving DecidableEq

open Event

def swap : Event → Event
  | left  => right
  | right => left

theorem swap_no_fixed_point (x : Event) : swap x ≠ x := by
  cases x <;> simp [swap]

/-- A choice natural under every automorphism would in particular be fixed by swap. -/
theorem no_swap_invariant_choice : ¬ ∃ x : Event, swap x = x := by
  intro h
  rcases h with ⟨x, hx⟩
  exact swap_no_fixed_point x hx

inductive World where
  | forward
  | backward
  deriving DecidableEq

inductive Direction where
  | ab
  | ba
  deriving DecidableEq

/-- The reduct/core is the same unit value in both worlds. -/
def core : World → Unit := fun _ => ()

def direction : World → Direction
  | World.forward  => Direction.ab
  | World.backward => Direction.ba

theorem no_direction_decoder :
    ¬ ∃ decode : Unit → Direction, ∀ w, decode (core w) = direction w := by
  intro h
  rcases h with ⟨decode, exactness⟩
  have hf := exactness World.forward
  have hb := exactness World.backward
  have : Direction.ab = Direction.ba := hf.symm.trans hb
  cases this

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/642d42de1c0e9342f86a/probe_toolchain.sh | SHA256 642d42de1c0e9342f86aa8b16fd455e90e4399acf6447eee5fb150f907c9b18b | LINES 1-17/17 =====
#!/usr/bin/env bash
set -u
printf 'timestamp_utc=%s\n' "$(date -u +%FT%TZ)"
printf 'cwd=%s\n' "$PWD"
printf 'argv='; printf '%q ' "$0" "$@"; printf '\n'
printf 'uname=%s\n' "$(uname -a)"
printf 'python='; python --version 2>&1 || true
printf 'node='; node --version 2>&1 || true
for x in agda lean lake elan coqc rocq rzk ghc cabal stack nix; do
  if command -v "$x" >/dev/null 2>&1; then
    printf '%s_path=%s\n' "$x" "$(command -v "$x")"
    "$x" --version 2>&1 | head -n 3 | sed "s/^/${x}_version=/"
  else
    printf '%s_path=NOT_FOUND\n' "$x"
  fi
done
printf 'dns_github='; getent hosts github.com 2>&1 || true

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/65c80f5d759ca8f7c3af/round2_z_enrichment_model_check.py | SHA256 65c80f5d759ca8f7c3afcf0cfcb1d64203b0ee1f004ae9a1b8f96a8b578df23d | LINES 1-206/206 =====
#!/usr/bin/env python3
"""Finite sanity checks for the second-round HoTT–Z reconstruction.

This program checks only small finite witnesses used to catch mistakes in the
paper arguments.  It is NOT a proof-assistant formalization and does not replace
any unbounded mathematical proof.

Checked patterns:
1. provenance cannot factor through a current-snapshot projection;
2. a finer representation recovers every observable recoverable by a coarser one;
3. opposite event orders cannot factor through an unordered support;
4. duration cannot factor through an unparameterized trace;
5. endpoint reachability cannot factor through closure alone;
6. the target-truth signature is sufficient for exactly the chosen observables;
7. a non-injective abstraction has no exact reconstruction left inverse.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from itertools import product
import json
from pathlib import Path
from typing import Any, Callable, Dict, Hashable, Iterable, Mapping, Sequence, Tuple

ROOT = Path(__file__).resolve().parent
OUT_JSON = ROOT / "round2_z_enrichment_model_check.json"


def all_functions(domain: Sequence[Hashable], codomain: Sequence[Any]):
    """Enumerate all functions from a finite domain to a finite codomain."""
    for values in product(codomain, repeat=len(domain)):
        yield dict(zip(domain, values))


def factors_through(
    worlds: Sequence[Hashable],
    abstraction: Mapping[Hashable, Hashable],
    observable: Mapping[Hashable, Any],
) -> bool:
    """Finite fiber-constancy criterion for factorization."""
    seen: Dict[Hashable, Any] = {}
    for world in worlds:
        abstract = abstraction[world]
        value = observable[world]
        if abstract in seen and seen[abstract] != value:
            return False
        seen[abstract] = value
    return True


def exact_left_inverse_exists(
    worlds: Sequence[Hashable],
    abstract_values: Sequence[Hashable],
    abstraction: Mapping[Hashable, Hashable],
) -> bool:
    """Exhaustively test for beta with beta(alpha(w)) = w for every world."""
    for candidate in all_functions(abstract_values, worlds):
        if all(candidate[abstraction[w]] == w for w in worlds):
            return True
    return False


@dataclass(frozen=True)
class Check:
    name: str
    passed: bool
    detail: str


def main() -> None:
    checks = []

    # 1. Snapshot/provenance.
    histories = (
        ("same-current-structure", "original"),
        ("same-current-structure", "replica"),
    )
    snapshot = {h: h[0] for h in histories}
    enriched = {h: h for h in histories}
    is_original = {h: h[1] == "original" for h in histories}

    coarse_provenance = factors_through(histories, snapshot, is_original)
    fine_provenance = factors_through(histories, enriched, is_original)
    checks.append(Check(
        "provenance_nonfactorization",
        (not coarse_provenance) and fine_provenance,
        "IsOriginal varies inside one snapshot fiber, but factors through the enriched history.",
    ))

    # 2. Refinement monotonicity on a finite observable family.
    current_structure = {h: h[0] == "same-current-structure" for h in histories}
    observables = {
        "current_structure": current_structure,
        "is_original": is_original,
    }
    coarse_recoverable = {
        name for name, obs in observables.items() if factors_through(histories, snapshot, obs)
    }
    fine_recoverable = {
        name for name, obs in observables.items() if factors_through(histories, enriched, obs)
    }
    checks.append(Check(
        "refinement_monotonicity",
        coarse_recoverable <= fine_recoverable and coarse_recoverable < fine_recoverable,
        f"coarse={sorted(coarse_recoverable)}, fine={sorted(fine_recoverable)}",
    ))

    # 3. Direction vs unordered event support.
    ordered_histories = ("a-before-b", "b-before-a")
    unordered_support = {h: frozenset(("a", "b")) for h in ordered_histories}
    a_before_b = {
        "a-before-b": True,
        "b-before-a": False,
    }
    checks.append(Check(
        "direction_nonfactorization",
        not factors_through(ordered_histories, unordered_support, a_before_b),
        "Opposite orders have the same unordered support but opposite truth values.",
    ))

    # 4. Duration vs unparameterized trace.
    timed_paths = ("unit-speed", "half-speed")
    geometric_trace = {h: "oriented-unit-interval-trace" for h in timed_paths}
    duration = {"unit-speed": 1, "half-speed": 2}
    checks.append(Check(
        "duration_nonfactorization",
        not factors_through(timed_paths, geometric_trace, duration),
        "The same unparameterized trace supports different durations.",
    ))

    # 5. Closure vs actual endpoint reachability.
    processes = ("closed-domain-reaches", "open-ended-asymptotic")
    closure = {p: "closed-unit-interval" for p in processes}
    reaches_endpoint = {
        "closed-domain-reaches": True,
        "open-ended-asymptotic": False,
    }
    checks.append(Check(
        "closure_reachability_nonfactorization",
        not factors_through(processes, closure, reaches_endpoint),
        "Equal image closures do not determine whether the endpoint is attained.",
    ))

    # 6. Minimal sufficient truth signature for selected observables.
    worlds = ("a-before-b", "b-before-a", "simultaneous")
    target_observables = {
        "a_before_b": {
            "a-before-b": True,
            "b-before-a": False,
            "simultaneous": False,
        },
        "b_before_a": {
            "a-before-b": False,
            "b-before-a": True,
            "simultaneous": False,
        },
    }
    truth_signature = {
        w: tuple(target_observables[name][w] for name in sorted(target_observables))
        for w in worlds
    }
    signature_sufficient = all(
        factors_through(worlds, truth_signature, obs)
        for obs in target_observables.values()
    )
    collapsed = {w: "one-state" for w in worlds}
    collapsed_sufficient = all(
        factors_through(worlds, collapsed, obs)
        for obs in target_observables.values()
    )
    checks.append(Check(
        "truth_signature_sufficiency",
        signature_sufficient and not collapsed_sufficient,
        f"signatures={truth_signature}",
    ))

    # 7. No exact left inverse for a non-injective abstraction.
    abstract_values = tuple(sorted(set(snapshot.values())))
    no_left_inverse = not exact_left_inverse_exists(histories, abstract_values, snapshot)
    checks.append(Check(
        "no_free_exact_reconstruction",
        no_left_inverse,
        "A non-injective snapshot projection has no beta with beta∘alpha=id.",
    ))

    payload = {
        "scope": "finite_sanity_check_only",
        "not_a_proof_assistant_formalization": True,
        "checks": [asdict(c) for c in checks],
        "all_passed": all(c.passed for c in checks),
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("Second-round HoTT–Z finite model sanity checks")
    print("NOTE: finite checks only; not an unbounded formal proof.\n")
    for c in checks:
        print(f"[{'PASS' if c.passed else 'FAIL'}] {c.name}: {c.detail}")
    print(f"\nall_passed={payload['all_passed']}")
    print(f"json={OUT_JSON}")

    if not payload["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

===== END SOURCE CHUNK | EOF=true =====


===== SOURCE scripts/recovered/6938542b37fdf9056e46/cognition_runtime.py | SHA256 6938542b37fdf9056e46252909ef266a457db75ce729ba69e05fe95633f4e99f | LINES 1-393/393 =====
#!/usr/bin/env python3
"""File-based full cognition loading and optimistic checkpointing.

Standard library only. plan/read/check are read-only. checkpoint defaults to a
no-write preview; --apply and current user authorization are required to write.
No network, subprocess, model invocation, or mathematical verification occurs.
A coverage result concerns emitted file ranges, never the model's understanding.
"""
from __future__ import annotations
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import sys
import uuid

VERSION = '1.2.0'
PREFIX = '.codex/research/hott/'
CONFIG = '.codex/cognition/LOAD_SET.json'
STATE = PREFIX + 'STATE.json'
HEAD = '.codex/cognition/HEAD.json'
LOCK = '.codex/cognition/WRITE_LOCK.json'
TXN = '.codex/cognition/TRANSACTION.json'
SKILL = '.codex/skills/hott-paradox-research/SKILL.md'
CLOSURE = '认知闭包/2026-09-01-Z铁律最终定性-时间否定与朴素集合论-HoTT怀疑-认知闭包.md'
QUESTIONS = 'HoTT/HoTT研究三问-找什么-怎么找-凭什么-20260909.md'
CLOSURE_ID = 'CC-20260901-z-law-final-temporal-negation-naive-set-hott'
MUTABLE = ('MEMORY.md', PREFIX+'FRONTIER.md', PREFIX+'LESSONS.md', PREFIX+'RESUME.md', STATE)
REQUIRED = (CLOSURE, QUESTIONS, 'AGENTS.md', SKILL, 'README.md', 'MEMORY.md', CONFIG, STATE,
            '.codex/cognition/PROTOCOL.md', PREFIX+'FRONTIER.md', PREFIX+'LESSONS.md', PREFIX+'RESUME.md')
ID = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_-]{0,100}$')

class CognitionError(RuntimeError):
    pass

def stamp() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()

def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def dump(obj) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, sort_keys=True, indent=2)+'\n').encode('utf-8')

def root_path(value=None) -> Path:
    if value is None:
        script = Path(__file__).resolve()
        if script.parts[-5:-1] != ('.codex','skills','hott-paradox-research','scripts'):
            raise CognitionError('ROOT_UNRESOLVED: use --project-root')
        value = script.parents[4]
    p=Path(value)
    if p.is_symlink(): raise CognitionError('ROOT_SYMLINK')
    return p.resolve()

def path_of(root: Path, rel: str) -> Path:
    if not isinstance(rel,str) or not rel or '\\' in rel or '\x00' in rel:
        raise CognitionError('UNSAFE_PATH')
    p=PurePosixPath(rel)
    if p.is_absolute() or any(x in ('','..','.') for x in rel.split('/')):
        raise CognitionError('UNSAFE_PATH: '+rel)
    cursor=root
    for part in p.parts:
        cursor=cursor/part
        if cursor.is_symlink(): raise CognitionError('SYMLINK_FORBIDDEN: '+rel)
    try: cursor.resolve().relative_to(root)
    except ValueError as e: raise CognitionError('PATH_ESCAPE: '+rel) from e
    return cursor

def read_bytes(root, rel):
    p=path_of(root,rel)
    try:
        before=p.stat();data=p.read_bytes();after=p.stat()
    except OSError as e: raise CognitionError('MISSING_OR_UNREADABLE: '+rel) from e
    if (before.st_ino,before.st_size,before.st_mtime_ns)!=(after.st_ino,after.st_size,after.st_mtime_ns):
        raise CognitionError('CHANGED_DURING_READ: '+rel)
    return data

def obj(data):
    try:
        out=json.loads(data)
    except (ValueError,UnicodeError) as e:raise CognitionError('INVALID_JSON') from e
    if not isinstance(out,dict):raise CognitionError('JSON_OBJECT_REQUIRED')
    return out

def text(data, name):
    try:t=data.decode('utf-8')
    except UnicodeError as e:raise CognitionError('NOT_UTF8: '+name) from e
    if not t.strip():raise CognitionError('EMPTY_REQUIRED_FILE: '+name)
    return t

def graph(config, state, get):
    if config.get('schema_version')!='cognition-load-set/v1':raise CognitionError('CONFIG_SCHEMA')
    fixed=config.get('fixed_full_text')
    if not isinstance(fixed,list) or any(not isinstance(x,str) for x in fixed) or len(set(fixed))!=len(fixed):raise CognitionError('FIXED_LIST_INVALID')
    if fixed[:2]!=[CLOSURE,QUESTIONS] or not set(REQUIRED)<=set(fixed):
        raise CognitionError('REQUIRED_COGNITION_REMOVED_OR_REORDERED')
    if config.get('dynamic_state')!=STATE:raise CognitionError('STATE_PATH_CHANGED')
    if state.get('schema_version')!='hott-working-state/v1' or type(state.get('revision')) is not int or state['revision']<1:
        raise CognitionError('STATE_SCHEMA')
    records=state.get('records')
    if not isinstance(records,dict):raise CognitionError('RECORDS_OBJECT_REQUIRED')
    seeds=[]
    latest=state.get('latest_session')
    if not isinstance(latest,str) or latest not in records or not isinstance(records[latest],dict) or records[latest].get('kind')!='session':
        raise CognitionError('LATEST_SESSION_MISSING')
    seeds.append(latest)
    for group in ('active','review_due','unresolved'):
        xs=state.get(group)
        if not isinstance(xs,list) or any(not isinstance(x,str) for x in xs) or len(set(xs))!=len(xs):raise CognitionError('SEED_LIST_INVALID: '+group)
        seeds.extend(xs)
    ordered=list(fixed);visited=set();visiting=set();selected=[];stale=set()
    def add(p):
        if not isinstance(p,str):raise CognitionError('PATH_STRING_REQUIRED')
        if p not in ordered:ordered.append(p)
    def visit(k):
        if k in visiting:raise CognitionError('DEPENDENCY_CYCLE: '+str(k))
        if k in visited:return
        if not isinstance(k,str) or not ID.fullmatch(k) or k not in records:
            raise CognitionError('MISSING_RECORD: '+str(k))
        record=records[k]
        if not isinstance(record,dict):raise CognitionError('INVALID_RECORD: '+k)
        visiting.add(k);add(record.get('path'))
        deps=record.get('depends_on',[]); sources=record.get('full_sources',[]); hashes=record.get('source_hashes',{})
        if not isinstance(deps,list) or not isinstance(sources,list) or not isinstance(hashes,dict):
            raise CognitionError('INVALID_DEPENDENCIES: '+k)
        for d in deps:visit(d)
        for p in sources:add(p)
        for p,h in hashes.items():
            add(p)
            if not isinstance(h,str) or not re.fullmatch('[0-9a-f]{64}',h):raise CognitionError('INVALID_SOURCE_HASH: '+k)
            if sha(get(p))!=h:stale.add(k)
        if any(d in stale for d in deps):stale.add(k)
        if record.get('status')=='review_required':stale.add(k)
        visiting.remove(k);visited.add(k);selected.append(k)
    for k in seeds:visit(k)
    # Directly declared dependencies are complete textual sources, not summaries.
    for p in ordered:text(get(p),p)
    if CLOSURE_ID not in '\n'.join(text(get(CLOSURE),CLOSURE).splitlines()[:12]):
        raise CognitionError('WRONG_CLOSURE_ID')
    return ordered,selected,sorted(stale)

def plan(project_root=None, *, _allow_busy=False):
    root=root_path(project_root)
    if not _allow_busy and (path_of(root,LOCK).exists() or path_of(root,TXN).exists()):
        raise CognitionError('CHECKPOINT_INCOMPLETE_OR_WRITER_ACTIVE')
    head_bytes=read_bytes(root,HEAD);head=obj(head_bytes)
    if head.get('schema_version')!='cognition-head/v1':raise CognitionError('HEAD_SCHEMA')
    cache={}
    def get(rel):
        if rel not in cache:cache[rel]=read_bytes(root,rel)
        return cache[rel]
    state=obj(get(STATE));config=obj(get(CONFIG))
    if head.get('revision')!=state.get('revision') or head.get('latest_session')!=state.get('latest_session'):
        raise CognitionError('HEAD_STATE_MISMATCH')
    tracked=head.get('tracked')
    if not isinstance(tracked,dict) or not set(MUTABLE)<=set(tracked):raise CognitionError('HEAD_TRACKING_INCOMPLETE')
    for rel,h in tracked.items():
        if sha(get(rel))!=h:raise CognitionError('UNCOMMITTED_STATE: '+rel)
    paths,records,stale=graph(config,state,get)
    entries=[]
    for rel in paths:
        b=get(rel);t=text(b,rel)
        entries.append({'path':rel,'sha256':sha(b),'bytes':len(b),'lines':len(t.splitlines(keepends=True))})
    for rel,b in cache.items():
        if read_bytes(root,rel)!=b:raise CognitionError('SNAPSHOT_CHANGED: '+rel)
    if read_bytes(root,HEAD)!=head_bytes:raise CognitionError('HEAD_CHANGED')
    if not _allow_busy and (path_of(root,LOCK).exists() or path_of(root,TXN).exists()):raise CognitionError('WRITER_STARTED')
    signature=sha(dump({'head_sha256':sha(head_bytes),'files':entries}))
    return {'schema_version':'cognition-plan/v1','snapshot':signature,'revision':head['revision'],
            'latest_session':state['latest_session'],'documents':entries,'dynamic_records':records,
            'review_required':stale,'total_bytes':sum(x['bytes'] for x in entries),
            'total_lines':sum(x['lines'] for x in entries),'model_context':'NOT_CERTIFIED_BY_TOOL',
            'policy':'NEW_FULL_READ_EVERY_INVOCATION_AND_AFTER_COMPACTION'}

def read_chunk(project_root, snapshot, path, start_line=1, max_bytes=10000):
    root=root_path(project_root);p=plan(root)
    if snapshot!=p['snapshot']:raise CognitionError('STALE_SNAPSHOT_RESTART_ALL')
    entry=next((x for x in p['documents'] if x['path']==path),None)
    if entry is None:raise CognitionError('PATH_NOT_IN_CURRENT_LOAD_SET')
    if type(start_line) is not int or start_line<1 or type(max_bytes) is not int or max_bytes<1 or max_bytes>262144:
        raise CognitionError('INVALID_RANGE_OR_BUDGET')
    b=read_bytes(root,path)
    if sha(b)!=entry['sha256']:raise CognitionError('FILE_CHANGED')
    ls=text(b,path).splitlines(keepends=True)
    if start_line>len(ls):raise CognitionError('START_PAST_EOF')
    i=start_line-1;used=0;out=[]
    while i<len(ls):
        size=len(ls[i].encode('utf-8'))
        if used+size>max_bytes:
            if not out:raise CognitionError('LINE_TOO_LARGE_INCREASE_BUDGET')
            break
        out.append(ls[i]);used+=size;i+=1
    if plan(root)['snapshot']!=snapshot:raise CognitionError('SNAPSHOT_CHANGED_RESTART_ALL')
    body=''.join(out)
    return {'snapshot':snapshot,'path':path,'file_sha256':entry['sha256'],'start_line':start_line,
            'end_line':i,'total_lines':len(ls),'next_start_line':None if i==len(ls) else i+1,
            'chunk_sha256':sha(body.encode()),'text':body,'model_context':'NOT_CERTIFIED_BY_TOOL'}

def check_coverage(p, chunks):
    """Check supplied emitted ranges only; cannot certify the model read them."""
    by={x['path']:[] for x in p['documents']}
    for c in chunks:
        if c.get('snapshot')!=p['snapshot'] or c.get('path') not in by:raise CognitionError('COVERAGE_SNAPSHOT_OR_PATH')
        by[c['path']].append(c)
    for f in p['documents']:
        cursor=1;acc=[]
        for c in by[f['path']]:
            if c.get('file_sha256')!=f['sha256'] or c.get('start_line')!=cursor or c.get('end_line',0)<cursor:
                raise CognitionError('COVERAGE_GAP_OR_ORDER: '+f['path'])
            body=c.get('text','')
            if not isinstance(body,str) or len(body.splitlines(keepends=True))!=c['end_line']-cursor+1 or sha(body.encode())!=c.get('chunk_sha256'):
                raise CognitionError('COVERAGE_BODY_MISMATCH')
            acc.append(body);cursor=c['end_line']+1
        if cursor!=f['lines']+1 or sha(''.join(acc).encode())!=f['sha256']:
            raise CognitionError('COVERAGE_INCOMPLETE: '+f['path'])
    return {'status':'FULL_EMITTED_BYTES_MATCH','documents':len(by),'model_context':'NOT_CERTIFIED_BY_TOOL'}

def atomic(path: Path, data: bytes):
    path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name('.'+path.name+'.tmp-'+uuid.uuid4().hex)
    try:
        with temp.open('xb') as f:f.write(data);f.flush();os.fsync(f.fileno())
        os.replace(temp,path)
        try:
            fd=os.open(path.parent,os.O_RDONLY);os.fsync(fd);os.close(fd)
        except OSError:pass
    finally:
        if temp.exists():temp.unlink()

def allowed_write(rel,sid):
    if rel in MUTABLE:return True
    if re.fullmatch(re.escape(PREFIX)+r'candidates/[A-Za-z0-9_-]+/[A-Za-z0-9_.-]+',rel):return True
    if re.fullmatch(re.escape(PREFIX)+'sessions/'+re.escape(sid)+r'/[A-Za-z0-9_.-]+',rel):return True
    return False

def prepare(root, snapshot, payload, *, busy=False):
    p=plan(root,_allow_busy=busy)
    if snapshot!=p['snapshot']:raise CognitionError('STALE_BASE')
    if payload.get('schema_version')!='cognition-checkpoint/v1':raise CognitionError('PAYLOAD_SCHEMA')
    sid=payload.get('session_id')
    if not isinstance(sid,str) or not ID.fullmatch(sid):raise CognitionError('INVALID_SESSION_ID')
    if not isinstance(payload.get('authorization'),str) or not payload['authorization'].strip():raise CognitionError('AUTHORIZATION_STATEMENT_REQUIRED')
    if not isinstance(payload.get('files'),list):raise CognitionError('FILES_LIST_REQUIRED')
    changes={};old={}
    for row in payload['files']:
        if not isinstance(row,dict) or 'expected_sha256' not in row:raise CognitionError('EXPECTED_FILE_BASE_REQUIRED')
        rel=row.get('path');target=path_of(root,rel)
        if not allowed_write(rel,sid):raise CognitionError('WRITE_OUTSIDE_AUTHORIZED_STATE: '+str(rel))
        if rel in changes:raise CognitionError('DUPLICATE_WRITE')
        if not isinstance(row.get('text'),str):raise CognitionError('UTF8_TEXT_REQUIRED')
        before=read_bytes(root,rel) if target.exists() else None
        if (sha(before) if before is not None else None)!=row.get('expected_sha256'):raise CognitionError('FILE_BASE_MISMATCH: '+rel)
        if rel.startswith(PREFIX+'sessions/') and before is not None:raise CognitionError('SESSION_IMMUTABLE')
        changes[rel]=row['text'].encode();old[rel]=before
    if not set(MUTABLE)<=set(changes):raise CognitionError('INCOMPLETE_CHECKPOINT_STATE')
    session_path=PREFIX+'sessions/'+sid+'/SESSION.md'
    if session_path not in changes:raise CognitionError('SESSION_RECORD_REQUIRED')
    get=lambda rel: changes[rel] if rel in changes else read_bytes(root,rel)
    state=obj(get(STATE)); prior=obj(read_bytes(root,STATE))
    if state.get('revision')!=prior['revision']+1 or state.get('latest_session')!=sid:
        raise CognitionError('REVISION_OR_LATEST_SESSION_INVALID')
    if state.get('records',{}).get(sid,{}).get('path')!=session_path:raise CognitionError('SESSION_ROUTE_INVALID')
    _,_,stale=graph(obj(get(CONFIG)),state,get)
    for k in stale:
        if state['records'][k].get('status')!='review_required':raise CognitionError('DEPENDENCY_REVIEW_REQUIRED: '+k)
    # Removing old records would silently delete historical routing.
    if not set(prior['records'])<=set(state['records']):raise CognitionError('OLD_RECORD_ROUTING_REMOVED')
    for k,rec in prior['records'].items():
        new=state['records'][k]
        if not isinstance(new,dict) or new.get('path')!=rec.get('path') or new.get('kind')!=rec.get('kind'):
            raise CognitionError('RECORD_IDENTITY_CHANGED: '+k)
        if rec.get('source_hashes')!=new.get('source_hashes') and not str(new.get('revalidation','')).strip():
            raise CognitionError('REVALIDATION_EXPLANATION_REQUIRED: '+k)
    head={'schema_version':'cognition-head/v1','revision':state['revision'],'latest_session':sid,
          'updated_at_utc':stamp(),'tracked':{x:sha(changes[x]) for x in MUTABLE}}
    changes[HEAD]=dump(head);old[HEAD]=read_bytes(root,HEAD)
    return p,sid,changes,old

def checkpoint(project_root,snapshot,payload,*,apply=False,_fail_after=None):
    root=root_path(project_root)
    p,sid,changes,old=prepare(root,snapshot,payload)
    if not apply:return {'status':'DRY_RUN','revision':p['revision']+1,'paths':list(changes),'writes':False}
    lock=path_of(root,LOCK)
    try:
        with lock.open('xb') as f:f.write(dump({'session_id':sid,'created_at_utc':stamp(),'pid':os.getpid()}));f.flush();os.fsync(f.fileno())
    except FileExistsError as e:raise CognitionError('WRITER_LOCKED') from e
    published=False
    try:
        p,sid,changes,old=prepare(root,snapshot,payload,busy=True)
        if path_of(root,TXN).exists():raise CognitionError('TRANSACTION_EXISTS')
        transaction_root='.codex/cognition/checkpoints/'+sid
        if path_of(root,transaction_root).exists():raise CognitionError('CHECKPOINT_ID_EXISTS')
        rows=[]
        for rel,b in changes.items():
            after=transaction_root+'/after/'+rel;atomic(path_of(root,after),b)
            before=transaction_root+'/before/'+rel if old[rel] is not None else None
            if before:atomic(path_of(root,before),old[rel])
            rows.append({'path':rel,'old_sha256':sha(old[rel]) if old[rel] is not None else None,'new_sha256':sha(b),
                         'before_copy':before,'after_copy':after})
        journal={'schema_version':'cognition-transaction/v1','session_id':sid,'base_snapshot':snapshot,
                 'rows':rows,'created_at_utc':stamp(),'authorization':payload['authorization']}
        atomic(path_of(root,transaction_root+'/transaction.json'),dump(journal))
        atomic(path_of(root,TXN),dump(journal));published=True
        for n,row in enumerate(rows,1):
            atomic(path_of(root,row['path']),changes[row['path']])
            if _fail_after==n:raise CognitionError('INJECTED_INTERRUPTION')
        for row in rows:
            if sha(read_bytes(root,row['path']))!=row['new_sha256']:raise CognitionError('POSTWRITE_MISMATCH')
        result={'status':'CHECKPOINT_COMMITTED','session_id':sid,'revision':p['revision']+1,'paths':list(changes),
                'model_understanding':'NOT_CERTIFIED','mathematics':'NOT_CERTIFIED','completed_at_utc':stamp()}
        atomic(path_of(root,transaction_root+'/result.json'),dump(result))
        path_of(root,TXN).unlink();published=False
        return result
    finally:
        if not published and lock.exists():
            if obj(lock.read_bytes()).get('session_id')==sid:lock.unlink()

def recover(project_root,action,*,confirm_owner_stopped=False):
    root=root_path(project_root)
    if not confirm_owner_stopped:raise CognitionError('EXPLICIT_OWNER_STOP_CONFIRMATION_REQUIRED')
    if action not in ('finish','rollback'):raise CognitionError('INVALID_RECOVERY_ACTION')
    journal=obj(read_bytes(root,TXN));sid=journal.get('session_id')
    lock=obj(read_bytes(root,LOCK))
    if journal.get('schema_version')!='cognition-transaction/v1' or not isinstance(sid,str) or not ID.fullmatch(sid):
        raise CognitionError('INVALID_RECOVERY_JOURNAL')
    if lock.get('session_id')!=sid:raise CognitionError('LOCK_OWNER_MISMATCH')
    rows=journal.get('rows',[])
    if not isinstance(rows,list) or not rows:raise CognitionError('TRANSACTION_EMPTY')
    base='.codex/cognition/checkpoints/'+sid
    if read_bytes(root,TXN)!=read_bytes(root,base+'/transaction.json'):
        raise CognitionError('RECOVERY_JOURNAL_MISMATCH')
    seen=set()
    for row in rows:
        if not isinstance(row,dict):raise CognitionError('RECOVERY_ROW_INVALID')
        rel=row.get('path')
        if not isinstance(rel,str) or rel in seen or (rel!=HEAD and not allowed_write(rel,sid)):
            raise CognitionError('RECOVERY_PATH_REJECTED')
        path_of(root,rel);seen.add(rel)
        old=row.get('old_sha256');new=row.get('new_sha256')
        if not isinstance(new,str) or not re.fullmatch('[0-9a-f]{64}',new) or (old is not None and (not isinstance(old,str) or not re.fullmatch('[0-9a-f]{64}',old))):
            raise CognitionError('RECOVERY_HASH_INVALID')
        expected_before=base+'/before/'+rel if old is not None else None
        if row.get('before_copy')!=expected_before or row.get('after_copy')!=base+'/after/'+rel:
            raise CognitionError('RECOVERY_BACKUP_PATH_INVALID')
    if not set(MUTABLE)<=seen or HEAD not in seen or rows[-1]['path']!=HEAD:
        raise CognitionError('RECOVERY_STATE_INCOMPLETE_OR_HEAD_NOT_LAST')
    # Refuse if anyone has written content not part of this transaction.
    for row in rows:
        p=path_of(root,row['path']);now=sha(read_bytes(root,row['path'])) if p.exists() else None
        if now not in (row['old_sha256'],row['new_sha256']):raise CognitionError('THIRD_PARTY_WRITE_RECOVERY_REFUSED')
        for key,hkey in [('before_copy','old_sha256'),('after_copy','new_sha256')]:
            if row[key] and sha(read_bytes(root,row[key]))!=row[hkey]:raise CognitionError('RECOVERY_BACKUP_CORRUPT')
    sequence=rows if action=='finish' else list(reversed(rows))
    for row in sequence:
        source=row['after_copy'] if action=='finish' else row['before_copy'];target=path_of(root,row['path'])
        if source:atomic(target,read_bytes(root,source))
        elif target.exists():target.unlink()
    res={'status':'RECOVERED_'+action.upper(),'session_id':sid,'timestamp':stamp(),'model_understanding':'NOT_CERTIFIED'}
    atomic(path_of(root,'.codex/cognition/checkpoints/'+sid+'/recovery.json'),dump(res))
    plan(root,_allow_busy=True)
    path_of(root,TXN).unlink();path_of(root,LOCK).unlink()
    plan(root)
    return res

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--project-root',type=Path)
    sub=ap.add_subparsers(dest='command',required=True)
    sub.add_parser('plan')
    p=sub.add_parser('read');p.add_argument('--snapshot',required=True);p.add_argument('--path',required=True);p.add_argument('--start-line',type=int,default=1);p.add_argument('--max-bytes',type=int,default=10000)
    p=sub.add_parser('check');p.add_argument('--snapshot',required=True)
    p=sub.add_parser('checkpoint');p.add_argument('--snapshot',required=True);p.add_argument('--payload',type=Path,required=True);p.add_argument('--apply',action='store_true')
    p=sub.add_parser('recover');p.add_argument('--action',choices=['finish','rollback'],required=True);p.add_argument('--confirm-owner-stopped',action='store_true')
    a=ap.parse_args()
    try:
        if a.command=='plan':r=plan(a.project_root);r['invocation_nonce']=uuid.uuid4().hex
        elif a.command=='read':
            r=read_chunk(a.project_root,a.snapshot,a.path,a.start_line,a.max_bytes);body=r.pop('text')
            print('BEGIN_COGNITION_CHUNK');print(json.dumps(r,ensure_ascii=False));print('BEGIN_FULL_TEXT');sys.stdout.write(body)
            if not body.endswith('\n'):print()
            print('END_FULL_TEXT\nEND_COGNITION_CHUNK');return 0
        elif a.command=='check':
            r=plan(a.project_root)
            if r['snapshot']!=a.snapshot:raise CognitionError('STALE_SNAPSHOT_RESTART_ALL')
            r={'status':'SNAPSHOT_UNCHANGED','model_context':'NOT_CERTIFIED_BY_TOOL','snapshot':a.snapshot}
        elif a.command=='checkpoint':r=checkpoint(a.project_root,a.snapshot,obj(a.payload.read_bytes()),apply=a.apply)
        else:r=recover(a.project_root,a.action,confirm_owner_stopped=a.confirm_owner_stopped)
        print(json.dumps(r,ensure_ascii=False,indent=2));return 0
    except (CognitionError,OSError,ValueError,TypeError,KeyError) as e:
        print(json.dumps({'status':'BLOCKED','error':str(e)},ensure_ascii=False),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())

===== END SOURCE CHUNK | EOF=true =====
