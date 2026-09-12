#!/usr/bin/env python3
"""Build and validate verbatim paradox extracts from the Matrix book MinerU source."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


SCHEMA_VERSION = "matrix-book-paradox-extract/v1"
MANAGER_VERSION = "1.0.0"
DEFAULT_SOURCE = (
    "/Users/aurolafly/MinerU/"
    "The Art of The Matrix 宇宙编程学 —— 世界与意识、悖论与时空（第三版）.doc-"
    "49840494-168f-45cd-997a-0b1e891c222f/"
    "MinerU_markdown_202609010456973_03d86f36.md"
)
DEFAULT_OUTPUT = "HoTT/sources/user-originals/matrix-book-paradoxes"
EXPECTED_SOURCE_SHA256 = "24530b89725d4043a7a5292a403ab50d48feed5417351c348790150726ae9409"
EXPECTED_SOURCE_BYTES = 297_569
EXPECTED_SOURCE_LOGICAL_LINES = 5_683
FULL_SOURCE_FILENAME = "宇宙编程学第三版-MinerU全文原文.md"

PARADOX_PATTERN = re.compile(
    r"悖论|paradox|罗素|说谎|芝诺|shenchensh|Better\s*Best|相交直线|平行线转动|"
    r"假集合|不可停机|停机",
    re.IGNORECASE,
)
IMAGE_PATTERN = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
MINERU_ANCHOR_PATTERN = re.compile(r'^<a id="__RefHeading___Toc\d+"></a>\s*$')


class ExtractError(RuntimeError):
    pass


@dataclass(frozen=True)
class ExtractSpec:
    id: str
    filename: str
    title: str
    line_start: int
    line_end: int
    role: str
    topics: tuple[str, ...]


EXTRACTS: tuple[ExtractSpec, ...] = (
    ExtractSpec(
        "MP-01",
        "01-悖论研究缘起与总体路线-原文.md",
        "悖论研究缘起与总体路线",
        176,
        358,
        "research_origin",
        ("zeno", "shenchensh", "density", "discrete_spacetime", "premise_negation"),
    ),
    ExtractSpec(
        "MP-02",
        "02-被推演世界中的离散时空前提-原文.md",
        "被推演世界中的离散时空前提",
        804,
        896,
        "supporting_world_model",
        ("discrete_spacetime", "density", "causal_points", "operative_time"),
    ),
    ExtractSpec(
        "MP-03",
        "03-罗素悖论与假集合-原文.md",
        "罗素悖论与假集合",
        3570,
        3626,
        "paradox_and_proposed_resolution",
        ("russell", "false_set", "constructibility", "existence"),
    ),
    ExtractSpec(
        "MP-04",
        "04-Better-Best-说谎者-计算合法性与芝诺-原文.md",
        "Better Best、说谎者、计算合法性与芝诺",
        3627,
        3939,
        "paradox_family_and_proposed_resolution",
        ("better_best", "liar", "russell", "causal_admissibility", "zeno", "limit"),
    ),
    ExtractSpec(
        "MP-05",
        "05-shenchensh平行线转动悖论-原始发难-原文.md",
        "shenchensh 平行线转动悖论：原始发难",
        3941,
        4001,
        "paradox_statement",
        ("shenchensh", "parallel_lines", "rotation", "infinity", "zeno"),
    ),
    ExtractSpec(
        "MP-06",
        "06-shenchensh悖论-圆型体与稠密空间方案-原文.md",
        "shenchensh 悖论：圆型体与稠密空间方案",
        4202,
        4872,
        "proposed_dense_closed_space_resolution",
        ("shenchensh", "dense_space", "closed_space", "projective_infinity", "geometry"),
    ),
    ExtractSpec(
        "MP-07",
        "07-shenchensh悖论-非稠密离散时空方案-原文.md",
        "shenchensh 悖论：非稠密离散时空方案",
        4873,
        5175,
        "proposed_discrete_spacetime_resolution",
        ("shenchensh", "non_dense_space", "discrete_rotation", "causal_points", "ray_closure"),
    ),
    ExtractSpec(
        "MP-08",
        "08-芝诺与shenchensh悖论-前提否定总结-原文.md",
        "芝诺与 shenchensh 悖论：前提否定总结",
        5176,
        5212,
        "premise_audit_summary",
        ("zeno", "shenchensh", "density", "flatness", "infinity", "premise_negation"),
    ),
    ExtractSpec(
        "MP-09",
        "09-理论抽象的工具性与悖论必然性-原文.md",
        "理论抽象的工具性与悖论必然性",
        5213,
        5369,
        "ultimate_user_hypothesis_source",
        ("abstraction", "tool_utility", "premise_negation", "reality_relative_paradox", "dialectic"),
    ),
    ExtractSpec(
        "MP-10",
        "10-悖论研究后记综合-原文.md",
        "悖论研究后记综合",
        5472,
        5544,
        "afterword_synthesis",
        ("zeno", "shenchensh", "discrete_spacetime", "causal_admissibility", "simulation"),
    ),
)

# Explicit lexical hits that are metadata/navigation/incidental references rather than substantive discussion.
EXCLUDED_HIT_RANGES: tuple[tuple[int, int, str], ...] = (
    (2, 172, "table of contents navigation only"),
    (485, 504, "book-title mention and acknowledgement only"),
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


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
            raise ExtractError(f"build lock exists: {self.path}") from exc
        os.write(self.fd, f"pid={os.getpid()}\n".encode())
        return self

    def __exit__(self, _exc_type: object, _exc: object, _tb: object) -> None:
        if self.fd is not None:
            os.close(self.fd)
        try:
            self.path.unlink()
        except FileNotFoundError:
            pass


def load_source(source: Path) -> tuple[bytes, list[bytes], list[str]]:
    if not source.is_file():
        raise ExtractError(f"missing source: {source}")
    data = source.read_bytes()
    if sha256_bytes(data) != EXPECTED_SOURCE_SHA256:
        raise ExtractError("source SHA-256 changed; inspect before creating a new extraction generation")
    if len(data) != EXPECTED_SOURCE_BYTES:
        raise ExtractError(f"source bytes changed: {len(data)}")
    line_bytes = data.splitlines(keepends=True)
    if len(line_bytes) != EXPECTED_SOURCE_LOGICAL_LINES:
        raise ExtractError(f"source logical line count changed: {len(line_bytes)}")
    line_text = [line.decode("utf-8", errors="strict") for line in line_bytes]
    return data, line_bytes, line_text


def line_in_ranges(line: int, ranges: Sequence[tuple[int, int]]) -> bool:
    return any(start <= line <= end for start, end in ranges)


def collect_images(source: Path, source_text: str) -> list[dict[str, object]]:
    source_root = source.parent
    refs = IMAGE_PATTERN.findall(source_text)
    unique_refs = sorted(set(refs))
    for ref in unique_refs:
        rel = Path(ref)
        if rel.is_absolute() or ".." in rel.parts or not ref.startswith("images/"):
            raise ExtractError(f"unsafe image reference: {ref}")
        if not (source_root / rel).is_file():
            raise ExtractError(f"missing referenced image: {ref}")
    image_root = source_root / "images"
    image_paths = sorted(path for path in image_root.iterdir() if path.is_file())
    image_inventory = {f"images/{path.name}" for path in image_paths}
    if not set(unique_refs) <= image_inventory:
        missing = set(unique_refs) - image_inventory
        raise ExtractError(f"referenced images missing from source image inventory: {sorted(missing)}")
    counts: dict[str, int] = {}
    for ref in refs:
        counts[ref] = counts.get(ref, 0) + 1
    records = []
    for path in image_paths:
        data = path.read_bytes()
        rel = f"images/{path.name}"
        records.append(
            {
                "path": rel,
                "bytes": len(data),
                "sha256": sha256_bytes(data),
                "reference_count_in_full_source": counts.get(rel, 0),
            }
        )
    return records


def lexical_coverage(line_text: Sequence[str]) -> dict[str, object]:
    hit_lines = [i for i, line in enumerate(line_text, 1) if PARADOX_PATTERN.search(line)]
    selected_ranges = [(item.line_start, item.line_end) for item in EXTRACTS]
    excluded_ranges = [(start, end) for start, end, _reason in EXCLUDED_HIT_RANGES]
    selected_hits = [line for line in hit_lines if line_in_ranges(line, selected_ranges)]
    excluded_hits = [line for line in hit_lines if line_in_ranges(line, excluded_ranges)]
    uncovered = [line for line in hit_lines if line not in selected_hits and line not in excluded_hits]
    return {
        "pattern": PARADOX_PATTERN.pattern,
        "hit_count": len(hit_lines),
        "hit_lines": hit_lines,
        "selected_hit_count": len(selected_hits),
        "selected_hit_lines": selected_hits,
        "excluded_hit_count": len(excluded_hits),
        "excluded_hit_lines": excluded_hits,
        "excluded_ranges": [
            {"line_start": start, "line_end": end, "reason": reason}
            for start, end, reason in EXCLUDED_HIT_RANGES
        ],
        "uncovered_hit_lines": uncovered,
    }


def normalized_book_slice(text: str) -> str:
    lines = ["" if MINERU_ANCHOR_PATTERN.match(line.strip()) else line for line in text.splitlines()]
    return "\n".join(lines).rstrip() + "\n"


def build_model(repo_root: Path, source: Path) -> tuple[dict[str, object], dict[str, bytes]]:
    source_data, line_bytes, line_text = load_source(source)
    source_text = source_data.decode("utf-8", errors="strict")
    images = collect_images(source, source_text)
    coverage = lexical_coverage(line_text)
    if coverage["uncovered_hit_lines"]:
        raise ExtractError(f"uncovered explicit paradox hits: {coverage['uncovered_hit_lines']}")

    previous_end = 0
    artifacts: dict[str, bytes] = {FULL_SOURCE_FILENAME: source_data}
    extracts: list[dict[str, object]] = []
    for spec in EXTRACTS:
        if spec.line_start <= previous_end:
            raise ExtractError(f"overlapping or unsorted extract range: {spec.id}")
        if not 1 <= spec.line_start <= spec.line_end <= len(line_bytes):
            raise ExtractError(f"invalid extract range: {spec.id}")
        previous_end = spec.line_end
        verbatim = b"".join(line_bytes[spec.line_start - 1 : spec.line_end])
        verbatim_sha = sha256_bytes(verbatim)
        refs = sorted(set(IMAGE_PATTERN.findall(verbatim.decode("utf-8", errors="strict"))))
        header = (
            "<!--\n"
            "machine_managed: true\n"
            f"schema_version: {SCHEMA_VERSION}\n"
            f"manager_version: {MANAGER_VERSION}\n"
            f"extract_id: {spec.id}\n"
            f"source_external_path: {source}\n"
            f"source_sha256: {EXPECTED_SOURCE_SHA256}\n"
            f"source_line_range: {spec.line_start}-{spec.line_end}\n"
            f"verbatim_sha256: {verbatim_sha}\n"
            "review_status: USER_SOURCE_UNREVIEWED_CLAIMS\n"
            "-->\n\n"
            f"# {spec.title}\n\n"
            f"- Extract ID: `{spec.id}`\n"
            f"- Source lines: `{spec.line_start}-{spec.line_end}`\n"
            f"- Source SHA-256: `{EXPECTED_SOURCE_SHA256}`\n"
            f"- Role: `{spec.role}`\n"
            f"- Topics: `{', '.join(spec.topics)}`\n"
            "- Status: `USER_SOURCE_UNREVIEWED_CLAIMS`\n\n"
            "下面是连续、逐字的 MinerU 源片段。它证明用户原作中这样讨论过，不自动证明其中的"
            "数学、物理或历史主张正确。\n\n"
            "<!-- BEGIN VERBATIM -->\n"
        ).encode("utf-8")
        footer_prefix = b"" if verbatim.endswith(b"\n") or not verbatim else b"\n"
        artifact = header + verbatim + footer_prefix + b"<!-- END VERBATIM -->\n"
        artifacts[spec.filename] = artifact
        extracts.append(
            {
                "id": spec.id,
                "filename": spec.filename,
                "title": spec.title,
                "line_start": spec.line_start,
                "line_end": spec.line_end,
                "captured_lines": spec.line_end - spec.line_start + 1,
                "role": spec.role,
                "topics": list(spec.topics),
                "verbatim_bytes": len(verbatim),
                "verbatim_sha256": verbatim_sha,
                "artifact_bytes": len(artifact),
                "artifact_sha256": sha256_bytes(artifact),
                "image_references": refs,
            }
        )

    existing_better = repo_root / "HoTT/sources/user-originals/Better-Best悖论-原文.md"
    existing_relation: dict[str, object]
    if existing_better.is_file():
        source_slice = b"".join(line_bytes[3627 - 1 : 3939]).decode("utf-8", errors="strict")
        existing_text = existing_better.read_text(encoding="utf-8")
        equivalent = normalized_book_slice(source_slice) == normalized_book_slice(existing_text)
        existing_relation = {
            "path": existing_better.relative_to(repo_root).as_posix(),
            "sha256": sha256_bytes(existing_better.read_bytes()),
            "source_line_start": 3627,
            "source_line_end": 3939,
            "equivalent_after_removing_mineru_anchors_and_trailing_blank": equivalent,
        }
        if not equivalent:
            raise ExtractError("existing Better Best source no longer matches the normalized book slice")
    else:
        existing_relation = {"path": None, "status": "missing"}

    generation_payload = {
        "schema_version": SCHEMA_VERSION,
        "manager_version": MANAGER_VERSION,
        "source_external_path": str(source),
        "source_sha256": EXPECTED_SOURCE_SHA256,
        "extracts": [
            (item.id, item.filename, item.line_start, item.line_end, item.role, item.topics)
            for item in EXTRACTS
        ],
        "excluded_hit_ranges": EXCLUDED_HIT_RANGES,
        "images": [(item["path"], item["sha256"], item["bytes"]) for item in images],
    }
    generation_id = sha256_bytes(
        json.dumps(generation_payload, ensure_ascii=False, sort_keys=True).encode("utf-8")
    )[:20]
    manifest: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "manager_version": MANAGER_VERSION,
        "generation_id": generation_id,
        "source": {
            "external_path": str(source),
            "sha256": EXPECTED_SOURCE_SHA256,
            "bytes": len(source_data),
            "logical_lines": len(line_bytes),
            "full_snapshot_file": FULL_SOURCE_FILENAME,
            "full_snapshot_sha256": sha256_bytes(source_data),
        },
        "extract_count": len(extracts),
        "extracts": extracts,
        "image_count": len(images),
        "images": images,
        "full_source_image_reference_count": len(IMAGE_PATTERN.findall(source_text)),
        "full_source_unique_image_reference_count": len(set(IMAGE_PATTERN.findall(source_text))),
        "coverage": coverage,
        "existing_related_asset": existing_relation,
        "review_status": "USER_SOURCE_UNREVIEWED_CLAIMS",
    }
    artifacts["MANIFEST.json"] = json_bytes(manifest)
    artifacts["INDEX.md"] = render_index(manifest)
    return manifest, artifacts


def render_index(manifest: dict[str, object]) -> bytes:
    source = dict(manifest["source"])
    coverage = dict(manifest["coverage"])
    related = dict(manifest["existing_related_asset"])
    lines = [
        "# 《宇宙编程学》第三版：悖论原文独立阅读索引",
        "",
        "<!-- MACHINE_MANAGED_DERIVED: edit via HoTT/tools/matrix_book_paradox_extract.py -->",
        "",
        f"- Schema: `{SCHEMA_VERSION}`",
        f"- Manager: `{MANAGER_VERSION}`",
        f"- Generation: `{manifest['generation_id']}`",
        f"- External source: `{source['external_path']}`",
        f"- Source SHA-256: `{source['sha256']}`",
        f"- Source bytes/logical lines: `{source['bytes']}` / `{source['logical_lines']}`",
        f"- Full source snapshot: [{FULL_SOURCE_FILENAME}]({FULL_SOURCE_FILENAME})",
        f"- Images: `{manifest['image_count']}`",
        f"- Standalone verbatim extracts: `{manifest['extract_count']}`",
        f"- Explicit paradox-family hits: `{coverage['hit_count']}`; selected: "
        f"`{coverage['selected_hit_count']}`; metadata/navigation/incidental: "
        f"`{coverage['excluded_hit_count']}`; uncovered: `{len(coverage['uncovered_hit_lines'])}`",
        "- Status: `USER_SOURCE_UNREVIEWED_CLAIMS`",
        "",
        "这些文件用于直接回读用户原作，不是 AI 摘要，也不自动证明其中关于集合、停机、连续时空、",
        "普朗克尺度、几何、相对论或宇宙的主张正确。当前技术裁决仍以认知闭包、Z owner 和主张矩阵为准。",
        "",
        "| ID | 独立文档 | 源行 | 角色 | 主题 |",
        "|---|---|---:|---|---|",
    ]
    for item in list(manifest["extracts"]):
        row = dict(item)
        lines.append(
            f"| `{row['id']}` | [{row['title']}]({row['filename']}) | "
            f"{row['line_start']}-{row['line_end']} | `{row['role']}` | "
            f"{', '.join(row['topics'])} |"
        )
    lines.extend(
        [
            "",
            "## 与已有 Better Best 原文的关系",
            "",
            f"- Existing path: `{related.get('path')}`",
            f"- Existing SHA-256: `{related.get('sha256')}`",
            "- Book source range: `3627-3939`",
            "- Equivalent after removing MinerU navigation anchors/trailing blank: "
            f"`{str(related.get('equivalent_after_removing_mineru_anchors_and_trailing_blank')).lower()}`",
            "",
            "两份来源身份不同：已有文件保存早期 attachment 原字节；MP-04 保存本书 MinerU 快照中的"
            "连续原文。不能以相似为由覆盖任一来源。",
            "",
            "## 显式命中覆盖边界",
            "",
            "以下命中未制作正文摘录，因为它们只属于书名、目录或致谢：",
            "",
        ]
    )
    for item in list(coverage["excluded_ranges"]):
        row = dict(item)
        lines.append(f"- `{row['line_start']}-{row['line_end']}`：{row['reason']}")
    lines.extend(
        [
            "",
            "`uncovered=0` 只证明当前显式悖论族词表和人工加入的完整解答链已覆盖，不证明书中所有"
            "隐喻性矛盾、两难或潜在悖论都被语义穷尽。",
            "",
        ]
    )
    return "\n".join(lines).encode("utf-8")


def scan(repo_root: Path, source: Path) -> dict[str, object]:
    manifest, _artifacts = build_model(repo_root, source)
    return {
        "schema_version": manifest["schema_version"],
        "manager_version": manifest["manager_version"],
        "generation_id": manifest["generation_id"],
        "source": manifest["source"],
        "extract_count": manifest["extract_count"],
        "image_count": manifest["image_count"],
        "coverage": manifest["coverage"],
        "existing_related_asset": manifest["existing_related_asset"],
        "review_status": manifest["review_status"],
    }


def build(repo_root: Path, source: Path, output_root: Path, dry_run: bool) -> dict[str, object]:
    manifest, artifacts = build_model(repo_root, source)
    if dry_run:
        print(json.dumps(scan(repo_root, source), ensure_ascii=False, indent=2, sort_keys=True))
        return manifest
    generation_id = str(manifest["generation_id"])
    generations = output_root / "generations"
    target = generations / generation_id
    with BuildLock(output_root):
        if not target.exists():
            generations.mkdir(parents=True, exist_ok=True)
            temp = Path(tempfile.mkdtemp(prefix=f".{generation_id}.", dir=generations))
            try:
                for rel, data in sorted(artifacts.items()):
                    destination = temp / rel
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(data)
                for image in list(manifest["images"]):
                    row = dict(image)
                    rel = Path(str(row["path"]))
                    destination = temp / rel
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(source.parent / rel, destination)
                os.replace(temp, target)
            except Exception:
                shutil.rmtree(temp, ignore_errors=True)
                raise
        atomic_write(output_root / "CURRENT", (generation_id + "\n").encode("utf-8"))
    print(json.dumps(scan(repo_root, source), ensure_ascii=False, indent=2, sort_keys=True))
    return manifest


def current_generation(output_root: Path) -> Path:
    current = output_root / "CURRENT"
    if not current.is_file():
        raise ExtractError(f"missing CURRENT: {current}")
    generation_id = current.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"[0-9a-f]{20}", generation_id):
        raise ExtractError(f"invalid CURRENT generation: {generation_id!r}")
    generation = output_root / "generations" / generation_id
    if not generation.is_dir():
        raise ExtractError(f"missing CURRENT generation directory: {generation}")
    return generation


def validate(repo_root: Path, source: Path, output_root: Path) -> dict[str, object]:
    expected_manifest, expected_artifacts = build_model(repo_root, source)
    generation = current_generation(output_root)
    if generation.name != expected_manifest["generation_id"]:
        raise ExtractError(
            f"CURRENT is stale: current={generation.name} expected={expected_manifest['generation_id']}"
        )
    manifest_path = generation / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest != expected_manifest:
        raise ExtractError("persisted MANIFEST differs from a fresh deterministic model")

    expected_files = set(expected_artifacts)
    expected_files.update(str(dict(image)["path"]) for image in list(manifest["images"]))
    actual_files = {
        path.relative_to(generation).as_posix()
        for path in generation.rglob("*")
        if path.is_file()
    }
    if expected_files != actual_files:
        raise ExtractError(
            f"generation file mismatch: missing={sorted(expected_files-actual_files)} "
            f"orphan={sorted(actual_files-expected_files)}"
        )

    for rel, expected in expected_artifacts.items():
        actual = (generation / rel).read_bytes()
        if actual != expected:
            raise ExtractError(f"artifact bytes differ from deterministic build: {rel}")

    source_data, line_bytes, _line_text = load_source(source)
    if (generation / FULL_SOURCE_FILENAME).read_bytes() != source_data:
        raise ExtractError("full source snapshot is not byte-identical")
    for image in list(manifest["images"]):
        row = dict(image)
        rel = Path(str(row["path"]))
        copied = (generation / rel).read_bytes()
        original = (source.parent / rel).read_bytes()
        if copied != original or sha256_bytes(copied) != row["sha256"]:
            raise ExtractError(f"image mismatch: {rel}")

    for item in list(manifest["extracts"]):
        row = dict(item)
        verbatim = b"".join(line_bytes[int(row["line_start"]) - 1 : int(row["line_end"])])
        artifact = (generation / str(row["filename"])).read_bytes()
        marker = b"<!-- BEGIN VERBATIM -->\n"
        offset = artifact.find(marker)
        if offset < 0:
            raise ExtractError(f"missing verbatim marker: {row['filename']}")
        captured = artifact[offset + len(marker) : offset + len(marker) + int(row["verbatim_bytes"])]
        if captured != verbatim or sha256_bytes(captured) != row["verbatim_sha256"]:
            raise ExtractError(f"verbatim source slice mismatch: {row['id']}")

    for markdown in [path for path in generation.glob("*.md") if path.is_file()]:
        for ref in IMAGE_PATTERN.findall(markdown.read_text(encoding="utf-8")):
            rel = Path(ref)
            if rel.is_absolute() or ".." in rel.parts or not (generation / rel).is_file():
                raise ExtractError(f"broken/unsafe local image link in {markdown.name}: {ref}")

    result = {
        "status": "PASS",
        "schema_version": SCHEMA_VERSION,
        "manager_version": MANAGER_VERSION,
        "generation_id": generation.name,
        "source_sha256": manifest["source"]["sha256"],
        "source_logical_lines": manifest["source"]["logical_lines"],
        "extract_count": manifest["extract_count"],
        "image_count": manifest["image_count"],
        "explicit_hit_count": manifest["coverage"]["hit_count"],
        "selected_hit_count": manifest["coverage"]["selected_hit_count"],
        "excluded_hit_count": manifest["coverage"]["excluded_hit_count"],
        "uncovered_hit_count": len(manifest["coverage"]["uncovered_hit_lines"]),
        "better_best_normalized_equivalent": manifest["existing_related_asset"].get(
            "equivalent_after_removing_mineru_anchors_and_trailing_blank"
        ),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return result


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=None)
    parser.add_argument("--source", default=DEFAULT_SOURCE)
    parser.add_argument("--output-root", default=DEFAULT_OUTPUT)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("scan", help="read-only source/extract/image/coverage statistics")
    build_parser = sub.add_parser("build", help="build immutable generation and update CURRENT")
    build_parser.add_argument("--dry-run", action="store_true")
    sub.add_parser("validate", help="validate CURRENT against source, images, ranges and coverage")
    sub.add_parser("stats", help="print CURRENT manifest summary")
    args = parser.parse_args(argv)
    repo_root = Path(args.repo_root).resolve() if args.repo_root else Path(__file__).resolve().parents[2]
    source = Path(args.source).resolve()
    output_root = (repo_root / args.output_root).resolve()
    try:
        if args.command == "scan":
            print(json.dumps(scan(repo_root, source), ensure_ascii=False, indent=2, sort_keys=True))
        elif args.command == "build":
            build(repo_root, source, output_root, args.dry_run)
        elif args.command == "validate":
            validate(repo_root, source, output_root)
        elif args.command == "stats":
            generation = current_generation(output_root)
            manifest = json.loads((generation / "MANIFEST.json").read_text(encoding="utf-8"))
            print(json.dumps(scan(repo_root, source), ensure_ascii=False, indent=2, sort_keys=True))
            if manifest["generation_id"] != generation.name:
                raise ExtractError("CURRENT manifest generation ID mismatch")
        else:
            parser.error(f"unknown command: {args.command}")
    except ExtractError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
