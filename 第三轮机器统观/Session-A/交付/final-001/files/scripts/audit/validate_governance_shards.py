#!/usr/bin/env python3
# PROJECT-PINNED COPY - do not hand-edit.
# source: /Users/aurolafly/codex-worktrees/long-doc-sharding-3.16.0/tools/validate_governance_shards.py
# source_commit: 2e4e4d2dbe13046470bc79e98e64735312ee9bd5
# source_sha256: fb756482e99cf7c7405fed11156fcaa042185103159221653e9891aa2cb96860
# spec: /Users/aurolafly/codex-worktrees/long-doc-sharding-3.16.0/docs/governance/长治理文档分片与索引规范.md
# rationale: the shared main repo /Users/aurolafly/codex still ships the v1/200-line validator;
#            re-sync this copy from the canonical main repo once governance-v3.16.0 is tagged there.
"""Validate v1/v2 indexed governance shards without enforcing a line-count cap."""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from pathlib import Path
import re
import sys


INDEX_STARTS = {
    "v1": "<!-- governance-shard-index:v1",
    "v2": "<!-- governance-shard-index:v2",
}
SHARD_STARTS = {
    "v1": "<!-- governance-shard:v1",
    "v2": "<!-- governance-shard:v2",
}
# Public aliases preserve imports used by older fixtures and callers.
INDEX_START = INDEX_STARTS["v1"]
SHARD_START = SHARD_STARTS["v1"]
TABLE_START = "<!-- governance-shard-table:start -->"
TABLE_END = "<!-- governance-shard-table:end -->"
ROW_RE = re.compile(
    r"^\|\s*`?([A-Za-z0-9._-]+)`?\s*\|\s*\[([^]]+)\]\(([^)]+)\)\s*\|"
)
V2_SHARD_NAME_RE = re.compile(r"^(?P<shard_id>[0-9]{3}) - (?P<title>.+)\.md$")
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
VALID_MODES = {"topical", "sequential"}
REQUIRED_INDEX_KEYS = {
    "logical_id",
    "mode",
    "shard_root",
    "last_shard",
    "append_target",
    "soft_line_target",
}
REQUIRED_SHARD_KEYS = {"logical_id", "shard_id", "index"}


@dataclass
class Result:
    errors: list[str] = field(default_factory=list)
    notices: list[str] = field(default_factory=list)

    def extend(self, other: "Result") -> None:
        self.errors.extend(other.errors)
        self.notices.extend(other.notices)


def _marker(text: str, start: str) -> dict[str, str] | None:
    lines = text.splitlines()
    try:
        begin = next(i for i, line in enumerate(lines) if line.strip() == start)
    except StopIteration:
        return None
    values: dict[str, str] = {}
    for line in lines[begin + 1 :]:
        stripped = line.strip()
        if stripped == "-->":
            return values
        if not stripped or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        values[key.strip()] = value.strip()
    return None


def _marker_any(
    text: str, starts: dict[str, str]
) -> tuple[str, dict[str, str]] | None:
    for version, start in starts.items():
        values = _marker(text, start)
        if values is not None:
            return version, values
    return None


def _table_rows(text: str) -> list[tuple[str, str, str]] | None:
    try:
        body = text.split(TABLE_START, 1)[1].split(TABLE_END, 1)[0]
    except IndexError:
        return None
    rows: list[tuple[str, str, str]] = []
    for line in body.splitlines():
        match = ROW_RE.match(line.strip())
        if match:
            title = match.group(2).strip()
            path = match.group(3).strip()
            if path.startswith("<") and path.endswith(">"):
                path = path[1:-1]
            rows.append((match.group(1), title, path))
    return rows


def _inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def validate_index(index_path: Path) -> Result:
    result = Result()
    index_path = index_path.resolve()
    try:
        text = index_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        result.errors.append(f"{index_path}: cannot read index: {exc}")
        return result

    marker = _marker_any(text, INDEX_STARTS)
    if marker is None:
        result.errors.append(
            f"{index_path}: missing or unterminated supported governance shard index marker"
        )
        return result
    index_version, meta = marker
    missing = sorted(REQUIRED_INDEX_KEYS - set(meta))
    if missing:
        result.errors.append(f"{index_path}: missing index keys: {', '.join(missing)}")
        return result

    mode = meta["mode"]
    if mode not in VALID_MODES:
        result.errors.append(f"{index_path}: invalid mode {mode!r}")

    try:
        soft_target = int(meta["soft_line_target"])
        if soft_target <= 0:
            raise ValueError
    except ValueError:
        result.errors.append(f"{index_path}: soft_line_target must be a positive integer")
        soft_target = 300 if index_version == "v2" else 200

    rows = _table_rows(text)
    if rows is None:
        result.errors.append(f"{index_path}: missing shard table markers")
        return result
    if not rows:
        result.errors.append(f"{index_path}: shard table has no indexed shards")
        return result

    ids = [item[0] for item in rows]
    rel_paths = [item[2] for item in rows]
    if len(ids) != len(set(ids)):
        result.errors.append(f"{index_path}: duplicate shard IDs")
    if len(rel_paths) != len(set(rel_paths)):
        result.errors.append(f"{index_path}: duplicate shard paths")
    if meta["last_shard"] != rel_paths[-1]:
        result.errors.append(
            f"{index_path}: last_shard={meta['last_shard']!r} does not match final table path={rel_paths[-1]!r}"
        )
    if mode == "sequential" and meta["append_target"] != meta["last_shard"]:
        result.errors.append(f"{index_path}: sequential append_target must equal last_shard")
    if mode == "topical" and meta["append_target"] != "-":
        result.errors.append(f"{index_path}: topical append_target must be '-'")

    base = index_path.parent
    root = (base / meta["shard_root"]).resolve()
    if index_version == "v2" and meta["shard_root"] != index_path.stem:
        result.errors.append(
            f"{index_path}: v2 shard_root must equal index stem {index_path.stem!r}"
        )
    if not _inside(root, base):
        result.errors.append(f"{index_path}: shard_root escapes index directory")
        return result
    if not root.is_dir():
        result.errors.append(f"{index_path}: shard_root is not a directory: {root}")
        return result

    indexed_paths: set[Path] = set()
    for shard_id, link_title, rel_path in rows:
        shard_path = (base / rel_path).resolve()
        indexed_paths.add(shard_path)
        if index_version == "v2":
            rel = Path(rel_path)
            if len(rel.parts) != 2 or rel.parts[0] != index_path.stem:
                result.errors.append(
                    f"{index_path}: v2 shard path must be directly inside {index_path.stem}/: {rel_path}"
                )
            name_match = V2_SHARD_NAME_RE.fullmatch(rel.name)
            if name_match is None:
                result.errors.append(
                    f"{index_path}: v2 shard filename must match 'NNN - topic.md': {rel_path}"
                )
            else:
                if name_match.group("shard_id") != shard_id:
                    result.errors.append(
                        f"{index_path}: v2 filename shard ID does not match table: {rel_path}"
                    )
                if name_match.group("title") != link_title:
                    result.errors.append(
                        f"{index_path}: v2 filename topic does not match link title: {rel_path}"
                    )
        if not _inside(shard_path, root):
            result.errors.append(f"{index_path}: shard path escapes shard_root: {rel_path}")
            continue
        if not shard_path.is_file():
            result.errors.append(f"{index_path}: missing shard: {rel_path}")
            continue
        try:
            shard_text = shard_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            result.errors.append(f"{shard_path}: cannot read shard: {exc}")
            continue
        shard_marker = _marker_any(shard_text, SHARD_STARTS)
        if shard_marker is None:
            result.errors.append(
                f"{shard_path}: missing or unterminated supported governance shard marker"
            )
            continue
        shard_version, shard_meta = shard_marker
        if shard_version != index_version:
            result.errors.append(
                f"{shard_path}: shard marker {shard_version} does not match index marker {index_version}"
            )
        shard_missing = sorted(REQUIRED_SHARD_KEYS - set(shard_meta))
        if shard_missing:
            result.errors.append(f"{shard_path}: missing shard keys: {', '.join(shard_missing)}")
            continue
        if shard_meta["logical_id"] != meta["logical_id"]:
            result.errors.append(f"{shard_path}: logical_id does not match index")
        if shard_meta["shard_id"] != shard_id:
            result.errors.append(f"{shard_path}: shard_id does not match table")
        linked_index = (shard_path.parent / shard_meta["index"]).resolve()
        if linked_index != index_path:
            result.errors.append(f"{shard_path}: index backlink does not resolve to {index_path}")
        if index_version == "v2":
            heading = H1_RE.search(shard_text)
            if heading is None:
                result.errors.append(f"{shard_path}: v2 shard is missing an H1 title")
            elif heading.group(1).strip() != link_title:
                result.errors.append(
                    f"{shard_path}: v2 H1 title does not match index link title {link_title!r}"
                )
        line_count = len(shard_text.splitlines())
        if line_count > soft_target:
            result.notices.append(
                f"{shard_path}: {line_count} lines exceed soft target {soft_target}; content remains valid"
            )

    actual_paths = {path.resolve() for path in root.rglob("*.md") if path.is_file()}
    for orphan in sorted(actual_paths - indexed_paths):
        result.errors.append(f"{index_path}: orphan shard not listed: {orphan.relative_to(base)}")
    for outside in sorted(indexed_paths - actual_paths):
        if outside.exists():
            result.errors.append(f"{index_path}: indexed file is outside shard Markdown set: {outside}")
    return result


def discover_indexes(root: Path) -> list[Path]:
    indexes: list[Path] = []
    for path in root.resolve().rglob("*.md"):
        if ".git" in path.parts or "templates" in path.parts:
            continue
        try:
            opening_lines = path.read_text(encoding="utf-8").splitlines()[:20]
            if any(
                line.strip() in INDEX_STARTS.values() for line in opening_lines
            ):
                indexes.append(path)
        except (OSError, UnicodeError):
            continue
    return sorted(indexes)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("indexes", nargs="*", type=Path, help="logical Markdown index files")
    parser.add_argument("--scan", type=Path, help="scan a repository/directory for shard indexes")
    args = parser.parse_args(argv)

    paths = list(args.indexes)
    if args.scan:
        paths.extend(discover_indexes(args.scan))
    unique_paths = sorted({path.resolve() for path in paths})
    if not unique_paths and not args.scan:
        parser.error("provide at least one index or --scan")

    combined = Result()
    for path in unique_paths:
        combined.extend(validate_index(path))
    for notice in combined.notices:
        print(f"NOTICE: {notice}")
    for error in combined.errors:
        print(f"FAIL: {error}", file=sys.stderr)
    if combined.errors:
        print(f"FAIL: governance shard validation has {len(combined.errors)} issue(s)", file=sys.stderr)
        return 1
    print(
        f"PASS: governance shard indexes={len(unique_paths)}; "
        f"soft-target notices={len(combined.notices)}; v1/v2 compatible; "
        "line targets are non-blocking"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
