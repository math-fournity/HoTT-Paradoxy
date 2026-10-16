#!/usr/bin/env python3
"""Deterministic keyword inventory for a frozen natural-consumer source set.

The inventory narrows a bounded human/AI source assessment; keyword hits never
decide the E1-E6 semantic criteria.  Remote artifacts live in the manifest's
external cache and are verified by byte size and SHA-256 before scanning.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

from machine_overview.util import (
    MachineOverviewError,
    json_bytes,
    read_json,
    sha256_bytes,
    sha256_file,
    deterministic_tree,
    utc_now,
    write_json,
)

MANIFEST_SCHEMA = "machine-overview-natural-consumer-retrieval/v1"
INVENTORY_SCHEMA = "machine-overview-natural-consumer-inventory/v1"
PATTERNS = {
    "arrival": r"\barriv(?:al|e|es|ed|ing)\b",
    "clock": r"\bclocks?\b",
    "completion": r"\bcomplet(?:e|es|ed|ing|ion|ions)\b",
    "concurrency": r"\bconcurr(?:ency|ent|ently)\b",
    "dimension": r"\bdimensions?\b",
    "event": r"\bevents?\b",
    "interval": r"\bintervals?\b",
    "later": r"\blater\b",
    "path": r"\bpaths?\b",
    "process": r"\bprocess(?:es)?\b",
    "step": r"\bsteps?\b",
    "temporal": r"\btemporal(?:ly)?\b",
    "tick": r"\bticks?\b",
    "time": r"\btimes?\b",
}
MAX_HITS_PER_PATTERN = 120
PAGE_MARKER = re.compile(r"^===== PDF_PAGE (\d+) =====$")


def repo_root() -> Path:
    current = Path.cwd().resolve()
    while current != current.parent:
        if (current / ".git").exists() and (current / "machine-overview").is_dir():
            return current
        current = current.parent
    raise MachineOverviewError("PROJECT_ROOT_NOT_FOUND")


def _under(path: Path, root: Path, label: str) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise MachineOverviewError(f"PATH_OUTSIDE_DECLARED_ROOT:{label}:{path}") from exc
    return resolved


def _verify_external_file(cache_root: Path, row: dict, label: str) -> Path:
    path = _under(Path(row.get("path", "")), cache_root, label)
    if not path.is_file() or path.is_symlink():
        raise MachineOverviewError(f"AUDIT_ARTIFACT_INVALID:{label}")
    if path.stat().st_size != row.get("bytes") or sha256_file(path) != row.get("sha256"):
        raise MachineOverviewError(f"AUDIT_ARTIFACT_CHANGED:{label}")
    return path


def _hits_from_lines(lines: list[str], source_path: str | None = None) -> dict:
    compiled = {key: re.compile(pattern, re.IGNORECASE) for key, pattern in PATTERNS.items()}
    counts = {key: 0 for key in PATTERNS}
    hits = {key: [] for key in PATTERNS}
    page = None
    for line_number, line in enumerate(lines, 1):
        marker = PAGE_MARKER.match(line.strip())
        if marker:
            page = int(marker.group(1))
            continue
        normalized = " ".join(line.split())
        if not normalized:
            continue
        for key, pattern in compiled.items():
            matches = list(pattern.finditer(normalized))
            if not matches:
                continue
            counts[key] += len(matches)
            if len(hits[key]) < MAX_HITS_PER_PATTERN:
                hit = {"line": line_number, "excerpt": normalized[:300]}
                if page is not None:
                    hit["pdf_page"] = page
                if source_path is not None:
                    hit["source_path"] = source_path
                hits[key].append(hit)
    return {
        "counts": counts,
        "captured_hits": {key: value for key, value in hits.items() if value},
        "capture_limit_per_pattern": MAX_HITS_PER_PATTERN,
    }


def _scan_text(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="strict")
    result = _hits_from_lines(text.splitlines())
    result.update({"scanned_files": 1, "scanned_bytes": len(text.encode("utf-8"))})
    return result


def _scan_tree(root: Path) -> dict:
    aggregate_counts = {key: 0 for key in PATTERNS}
    aggregate_hits = {key: [] for key in PATTERNS}
    scanned_files = 0
    scanned_bytes = 0
    skipped_non_utf8 = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink() or path.suffix == ".agdai" or path.name == ".DS_Store":
            continue
        data = path.read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            skipped_non_utf8.append(path.relative_to(root).as_posix())
            continue
        scanned_files += 1
        scanned_bytes += len(data)
        relative = path.relative_to(root).as_posix()
        result = _hits_from_lines(text.splitlines(), source_path=relative)
        for key in PATTERNS:
            aggregate_counts[key] += result["counts"][key]
            room = MAX_HITS_PER_PATTERN - len(aggregate_hits[key])
            if room > 0:
                aggregate_hits[key].extend(result["captured_hits"].get(key, [])[:room])
    return {
        "counts": aggregate_counts,
        "captured_hits": {key: value for key, value in aggregate_hits.items() if value},
        "capture_limit_per_pattern": MAX_HITS_PER_PATTERN,
        "scanned_files": scanned_files,
        "scanned_bytes": scanned_bytes,
        "skipped_non_utf8": skipped_non_utf8,
    }


def _scope_pin(root: Path, manifest: dict) -> tuple[dict, dict]:
    pin = manifest.get("scope")
    if not isinstance(pin, dict):
        raise MachineOverviewError("AUDIT_SCOPE_PIN_MISSING")
    path = root / pin.get("path", "")
    if not path.is_file() or path.stat().st_size != pin.get("bytes") or sha256_file(path) != pin.get("sha256"):
        raise MachineOverviewError("AUDIT_SCOPE_PIN_CHANGED")
    scope = read_json(path)
    return pin, scope


def compute_inventory(root: Path, manifest_path: Path) -> dict:
    manifest = read_json(manifest_path)
    if manifest.get("schema_version") != MANIFEST_SCHEMA:
        raise MachineOverviewError("AUDIT_RETRIEVAL_SCHEMA_INVALID")
    scope_pin, scope = _scope_pin(root, manifest)
    cache_root = Path(manifest.get("external_cache_root", ""))
    if not cache_root.is_dir() or cache_root.is_symlink():
        raise MachineOverviewError("AUDIT_EXTERNAL_CACHE_INVALID")
    source_ids = [row.get("source_id") for row in manifest.get("sources", [])]
    scope_ids = [row.get("source_id") for row in scope.get("sources", [])]
    if source_ids != scope_ids or len(source_ids) != len(set(source_ids)):
        raise MachineOverviewError("AUDIT_SOURCE_ROSTER_MISMATCH")

    inventories = []
    for row in manifest["sources"]:
        source_id = row["source_id"]
        kind = row.get("scan_kind")
        if kind == "pdf_text":
            artifact = _verify_external_file(cache_root, row["artifact"], f"{source_id}.artifact")
            text_path = _verify_external_file(cache_root, row["derived_text"], f"{source_id}.derived_text")
            scan = _scan_text(text_path)
            identity = {
                "artifact": row["artifact"],
                "derived_text": row["derived_text"],
                "page_count": row.get("page_count"),
                "artifact_file_type": row.get("artifact_file_type"),
            }
            del artifact
        elif kind == "text":
            text_path = _verify_external_file(cache_root, row["artifact"], f"{source_id}.artifact")
            scan = _scan_text(text_path)
            identity = {"artifact": row["artifact"]}
        elif kind == "tree":
            tree_root = Path(row.get("local_root", "")).resolve()
            actual = deterministic_tree(tree_root)
            if actual != row.get("tree_identity"):
                raise MachineOverviewError(f"AUDIT_TREE_CHANGED:{source_id}")
            scan = _scan_tree(tree_root)
            identity = {"local_root": str(tree_root), "tree_identity": actual}
        else:
            raise MachineOverviewError(f"AUDIT_SCAN_KIND_INVALID:{source_id}:{kind}")
        inventories.append({
            "source_id": source_id,
            "scan_kind": kind,
            "source_url": row.get("source_url"),
            "identity": identity,
            "scan": scan,
        })
    return {
        "audit_id": scope["audit_id"],
        "scope": scope_pin,
        "retrieval_manifest": {
            "path": manifest_path.relative_to(root).as_posix(),
            "bytes": manifest_path.stat().st_size,
            "sha256": sha256_file(manifest_path),
        },
        "patterns": PATTERNS,
        "source_count": len(inventories),
        "sources": inventories,
        "semantic_limit": (
            "Keyword inventory is retrieval evidence only. E1-E6 decisions require direct reading of "
            "the cited construction; absence of a keyword is not absence of a concept."
        ),
    }


def run_inventory(root: Path, manifest_path: Path, output_path: Path) -> dict:
    if output_path.exists():
        raise MachineOverviewError("AUDIT_INVENTORY_ALREADY_EXISTS")
    deterministic = compute_inventory(root, manifest_path)
    evaluator = Path(__file__).resolve()
    output = {
        "schema_version": INVENTORY_SCHEMA,
        "generated_at_utc": utc_now(),
        "evaluator": {
            "path": evaluator.relative_to(root).as_posix(),
            "bytes": evaluator.stat().st_size,
            "sha256": sha256_file(evaluator),
        },
        "deterministic": deterministic,
        "deterministic_sha256": sha256_bytes(json_bytes(deterministic)),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    write_json(output_path, output)
    return output


def verify_inventory(root: Path, inventory_path: Path) -> dict:
    inventory = read_json(inventory_path)
    if inventory.get("schema_version") != INVENTORY_SCHEMA:
        raise MachineOverviewError("AUDIT_INVENTORY_SCHEMA_INVALID")
    evaluator = inventory.get("evaluator", {})
    evaluator_path = root / evaluator.get("path", "")
    if (not evaluator_path.is_file() or evaluator_path.stat().st_size != evaluator.get("bytes")
            or sha256_file(evaluator_path) != evaluator.get("sha256")):
        raise MachineOverviewError("AUDIT_EVALUATOR_CHANGED")
    manifest_path = root / inventory["deterministic"]["retrieval_manifest"]["path"]
    deterministic = compute_inventory(root, manifest_path)
    digest = sha256_bytes(json_bytes(deterministic))
    if digest != inventory.get("deterministic_sha256") or deterministic != inventory.get("deterministic"):
        raise MachineOverviewError("AUDIT_INVENTORY_REPLAY_MISMATCH")
    return {
        "status": "NATURAL_CONSUMER_INVENTORY_VALID",
        "audit_id": deterministic["audit_id"],
        "source_count": deterministic["source_count"],
        "deterministic_sha256": digest,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("--manifest", required=True)
    run.add_argument("--out", required=True)
    verify = sub.add_parser("verify")
    verify.add_argument("--inventory", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = repo_root()
    try:
        if args.command == "run":
            output = run_inventory(root, root / args.manifest, root / args.out)
            print(json.dumps({
                "status": "NATURAL_CONSUMER_INVENTORY_WRITTEN",
                "path": args.out,
                "sources": output["deterministic"]["source_count"],
                "deterministic_sha256": output["deterministic_sha256"],
            }, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(
                verify_inventory(root, root / args.inventory), ensure_ascii=False, indent=2,
            ))
    except (MachineOverviewError, OSError, ValueError, KeyError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
