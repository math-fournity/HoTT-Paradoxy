#!/usr/bin/env python3
"""Import the user-provided MinerU conversion of Rosser's 1936 article.

The user PDF and MinerU's normalized ``*_origin.pdf`` are both pinned.  Each
contains a JSTOR cover followed by the five journal pages 87--91; their bytes
differ because MinerU rewrote the PDF.  The receipt therefore keeps original
input identity, normalized-derivative identity, and source-content identity
as separate facts.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import uuid
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MINERU_ROOT = Path("/Users/aurolafly/MinerU")
MINERU_GLOB = "Extensions of Some Theorems of G*del and Church (Barkley Rosser)*"
INPUT = ROOT / "audit/literature/PDF-to-Markdown-20260914/Rosser-1936-Extensions.pdf"
USER_PDF = ROOT / "外部资料/Extensions of Some Theorems of Gödel and Church (Barkley Rosser) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
DEST = ROOT / "audit/literature/LIT-CLASSICS-001/mineru-rosser-primary"
MANIFEST = DEST / "IMPORT.json"
RECEIPT = DEST / "RECEIPT.json"
DISCOVERY_DATE = "2026-09-14"
EXPECTED_INPUT_BYTES = 538312
EXPECTED_INPUT_SHA256 = "72a53b2c765df55b921b1d08ea584c76021af60aa2034ac3210e6697005bbb2a"
EXPECTED_ORIGIN_BYTES = 539387
EXPECTED_ORIGIN_SHA256 = "a7d3020cc4ec9f84dce21776f6f6351539e6074b787870a72a823f6305c00e02"
EXPECTED_PDF_PAGES = 6
IMAGE_PATTERN = re.compile(r"images/[0-9a-f]{64}\.(?:jpg|jpeg|png)")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def one(root: Path, pattern: str, label: str) -> Path:
    rows = sorted(root.glob(pattern))
    if len(rows) != 1 or not rows[0].is_file() or rows[0].is_symlink():
        raise SystemExit(f"{label}_COUNT:{root}:{len(rows)}")
    return rows[0]


def resolve_mineru_root() -> Path:
    rows = sorted(path for path in MINERU_ROOT.glob(MINERU_GLOB) if path.is_dir() and not path.is_symlink())
    if len(rows) != 1:
        raise SystemExit(f"ROSSER_MINERU_ROOT_COUNT:{len(rows)}")
    return rows[0]


def essential_bundle(root: Path) -> dict[str, Any]:
    markdown = root / "full.md"
    origin = one(root, "*_origin.pdf", "ORIGIN_PDF")
    content = one(root, "*_content_list_v2.json", "CONTENT_LIST_V2")
    if not markdown.is_file() or markdown.is_symlink() or origin.read_bytes()[:5] != b"%PDF-":
        raise SystemExit("ROSSER_MINERU_PRIMARY_INVALID")
    markdown_text = markdown.read_text(encoding="utf-8")
    content_text = content.read_text(encoding="utf-8")
    value = json.loads(content_text)
    if not isinstance(value, list):
        raise SystemExit(f"MINERU_PAGE_STRUCTURE_INVALID:{root}")
    refs = sorted(set(IMAGE_PATTERN.findall(markdown_text)) | set(IMAGE_PATTERN.findall(content_text)))
    for rel in refs:
        path = root / rel
        if not path.is_file() or path.is_symlink():
            raise SystemExit(f"ROSSER_IMAGE_MISSING:{rel}")
    paths = [("full.md", markdown), ("origin.pdf", origin), ("content-list-v2.json", content)]
    paths.extend((rel, root / rel) for rel in refs)
    rows = [{"path": label, "bytes": path.stat().st_size, "sha256": sha(path)} for label, path in paths]
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {
        "root": root,
        "markdown": markdown,
        "markdown_text": markdown_text,
        "origin": origin,
        "content": content,
        "image_refs": refs,
        "essential_files": rows,
        "essential_tree_sha256": digest.hexdigest(),
        "page_count": len(value),
    }


def inspect_mineru(root: Path) -> dict[str, Any]:
    row = essential_bundle(root)
    for anchor in (
        "EXTENSIONS OF SOME THEOREMS OF GÖDEL AND CHURCH",
        "BARKLEY ROSSER",
        "The Journal of Symbolic Logic, Vol. 1, No. 3",
        "pp. 87-91",
        "THEOREM II",
        "THEOREM III",
        "THEOREM V",
        "HARVARD UNIVERSITY",
    ):
        if anchor.casefold() not in row["markdown_text"].casefold():
            raise SystemExit(f"ROSSER_TEXT_ANCHOR_MISSING:{anchor}")
    if row["page_count"] != EXPECTED_PDF_PAGES:
        raise SystemExit("ROSSER_PAGE_STRUCTURE_INVALID")
    return row


def current_discovery(target_fingerprint: str) -> dict[str, Any]:
    groups: dict[str, list[str]] = defaultdict(list)
    for root in sorted(path for path in MINERU_ROOT.iterdir() if path.is_dir() and path.name != "data"):
        if dt.datetime.fromtimestamp(root.stat().st_mtime).date().isoformat() != DISCOVERY_DATE:
            continue
        markdown = root / "full.md"
        origins = sorted(root.glob("*_origin.pdf"))
        contents = sorted(root.glob("*_content_list_v2.json"))
        if not markdown.is_file() or len(origins) != 1 or len(contents) != 1:
            continue
        row = essential_bundle(root)
        groups[row["essential_tree_sha256"]].append(root.name)
    members = groups.get(target_fingerprint, [])
    if len(members) != 1:
        raise SystemExit(f"ROSSER_CONTENT_GROUP_MEMBER_COUNT:{len(members)}")
    if len(groups) != 16 or sum(map(len, groups.values())) != 42:
        raise SystemExit(f"MINERU_DISCOVERY_DENOMINATOR_CHANGED:{len(groups)}:{sum(map(len, groups.values()))}")
    return {
        "selection_rule": "DIRECTORIES_WITH_LOCAL_MTIME_DATE_2026-09-14",
        "directory_count": 42,
        "unique_content_group_count": 16,
        "duplicate_directory_count": 26,
        "prior_imported_unique_groups": 15,
        "new_unique_groups": 1,
        "new_group_members": members,
        "new_group_essential_tree_sha256": target_fingerprint,
        "source_directories_preserved": True,
        "deletion_performed": False,
    }


def file_row(path: Path, root: Path) -> dict[str, Any]:
    return {"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "sha256": sha(path)}


def inspect_source() -> dict[str, Any]:
    source = inspect_mineru(resolve_mineru_root())
    for label, path in (("USER_PDF", USER_PDF), ("CANONICAL_INPUT", INPUT)):
        if not path.is_file() or path.is_symlink() or path.read_bytes()[:5] != b"%PDF-":
            raise SystemExit(f"ROSSER_{label}_INVALID")
        if path.stat().st_size != EXPECTED_INPUT_BYTES or sha(path) != EXPECTED_INPUT_SHA256:
            raise SystemExit(f"ROSSER_{label}_IDENTITY_MISMATCH")
    if sha(USER_PDF) != sha(INPUT):
        raise SystemExit("ROSSER_CANONICAL_COPY_NOT_BYTE_IDENTICAL")
    if source["origin"].stat().st_size != EXPECTED_ORIGIN_BYTES or sha(source["origin"]) != EXPECTED_ORIGIN_SHA256:
        raise SystemExit("ROSSER_MINERU_ORIGIN_IDENTITY_MISMATCH")
    return source


def build_manifest(temp: Path, source: dict[str, Any]) -> dict[str, Any]:
    target = temp / "Rosser-1936-Extensions"
    target.mkdir()
    shutil.copy2(source["markdown"], target / "full.md")
    shutil.copy2(source["origin"], target / "origin.pdf")
    shutil.copy2(source["content"], target / "content-list-v2.json")
    for rel in source["image_refs"]:
        destination = target / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source["root"] / rel, destination)
    files = [
        file_row(path, temp)
        for path in sorted(temp.rglob("*"))
        if path.is_file() and path.name not in {"IMPORT.json", "RECEIPT.json"}
    ]
    digest = hashlib.sha256()
    for row in files:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {
        "schema_version": "lit-classics-rosser-primary-import/v1",
        "status": "VALID",
        "import_date": DISCOVERY_DATE,
        "source_id": "ROSSER-1936",
        "title": "Extensions of Some Theorems of Gödel and Church",
        "author": "Barkley Rosser",
        "bibliographic_identity": {
            "journal": "The Journal of Symbolic Logic",
            "volume": "1",
            "issue": "3",
            "date": "September 1936",
            "printed_pages": "87-91",
            "doi": "10.2307/2269028",
            "stable_url": "https://www.jstor.org/stable/2269028",
        },
        "source_role": "PRIMARY_ORIGINAL_ARTICLE_SCAN",
        "content_identity_status": "PRIMARY_BODY_CONFIRMED_BY_TITLE_AUTHOR_JOURNAL_PAGES_AND_FULL_VISUAL_REVIEW",
        "byte_provenance_status": "PRECONVERSION_INPUT_AND_MINERU_NORMALIZED_ORIGIN_BOTH_PINNED",
        "instruction_boundary": "DOCUMENT_CONTENT_ONLY_NOT_AGENT_INSTRUCTIONS",
        "canonical_input": {
            "path": INPUT.relative_to(ROOT).as_posix(),
            "bytes": INPUT.stat().st_size,
            "sha256": sha(INPUT),
            "relation_to_user_pdf": "BYTE_IDENTICAL_COPY",
            "relation_to_mineru_origin": "MINERU_NORMALIZED_DERIVATIVE_NOT_BYTE_IDENTITY",
            "pdf_pages": 6,
            "page_structure": "PDF page 1 JSTOR cover; PDF pages 2-6 journal pages 87-91",
        },
        "user_pdf": {
            "path": USER_PDF.relative_to(ROOT).as_posix(),
            "bytes": USER_PDF.stat().st_size,
            "sha256": sha(USER_PDF),
        },
        "mineru_source_root": str(source["root"]),
        "mineru_essential_tree_sha256": source["essential_tree_sha256"],
        "mineru_origin": {
            "source_name": source["origin"].name,
            "bytes": source["origin"].stat().st_size,
            "sha256": sha(source["origin"]),
            "relation_to_input": "MINERU_NORMALIZED_DERIVATIVE_NOT_BYTE_IDENTITY",
        },
        "markdown": {
            "path": "Rosser-1936-Extensions/full.md",
            "bytes": source["markdown"].stat().st_size,
            "sha256": sha(source["markdown"]),
            "lines": source["markdown_text"].count("\n") + 1,
        },
        "content_list": {
            "path": "Rosser-1936-Extensions/content-list-v2.json",
            "bytes": source["content"].stat().st_size,
            "sha256": sha(source["content"]),
            "pdf_pages": 6,
        },
        "referenced_images": len(source["image_refs"]),
        "visual_review": {
            "status": "ALL_6_PDF_PAGES_REVIEWED",
            "artifact_role": "IDENTITY_AND_PAGE_COMPLETENESS_CHECK",
            "formula_warning": "MinerU OCR is searchable but exact symbolic formulas must be checked against the scan.",
        },
        "theorem_review_scope": ["Introduction", "Lemma I-II", "Theorem I-V"],
        "mathematics_status": "SOURCE_REPORTED_NOT_REPLAYED",
        "current_discovery": current_discovery(source["essential_tree_sha256"]),
        "files": files,
        "file_count": len(files),
        "total_bytes": sum(row["bytes"] for row in files),
        "tree_sha256": digest.hexdigest(),
        "scope": "Preserves the Rosser 1936 primary article conversion and content identity. It does not certify OCR formulas or replay Theorems I-V in the current project proof assistant.",
    }


def receipt_value(manifest: dict[str, Any], manifest_bytes: bytes) -> dict[str, Any]:
    return {
        "schema_version": "lit-classics-rosser-primary-receipt/v1",
        "status": "VALID",
        "source_id": manifest["source_id"],
        "source_role": manifest["source_role"],
        "content_identity_status": manifest["content_identity_status"],
        "byte_provenance_status": manifest["byte_provenance_status"],
        "mathematics_status": manifest["mathematics_status"],
        "import_manifest": "IMPORT.json",
        "import_manifest_bytes": len(manifest_bytes),
        "import_manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        "file_count": manifest["file_count"],
        "total_bytes": manifest["total_bytes"],
        "tree_sha256": manifest["tree_sha256"],
        "pdf_pages": manifest["canonical_input"]["pdf_pages"],
        "printed_pages": manifest["bibliographic_identity"]["printed_pages"],
        "current_unique_content_groups": manifest["current_discovery"]["unique_content_group_count"],
        "new_unique_groups": manifest["current_discovery"]["new_unique_groups"],
        "source_directories_preserved": manifest["current_discovery"]["source_directories_preserved"],
        "scope": "Small hydration receipt for the hash-pinned Rosser 1936 primary import. Source-reported theorems remain un-replayed in the current project.",
    }


def verify() -> dict[str, Any]:
    manifest_bytes = MANIFEST.read_bytes()
    manifest = json.loads(manifest_bytes)
    if manifest.get("schema_version") != "lit-classics-rosser-primary-import/v1":
        raise SystemExit("MANIFEST_SCHEMA_INVALID")
    expected = manifest.get("files")
    if not isinstance(expected, list):
        raise SystemExit("MANIFEST_FILES_INVALID")
    actual = sorted(
        path.relative_to(DEST).as_posix()
        for path in DEST.rglob("*")
        if path.is_file() and path.name not in {"IMPORT.json", "RECEIPT.json"}
    )
    if actual != sorted(row["path"] for row in expected):
        raise SystemExit("IMPORT_PATH_SET_MISMATCH")
    for row in expected:
        path = DEST / row["path"]
        if path.stat().st_size != row["bytes"] or sha(path) != row["sha256"]:
            raise SystemExit(f"IMPORT_FILE_MISMATCH:{row['path']}")
    digest = hashlib.sha256()
    for row in expected:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    if digest.hexdigest() != manifest.get("tree_sha256"):
        raise SystemExit("IMPORT_TREE_MISMATCH")
    source = inspect_source()
    if source["essential_tree_sha256"] != manifest.get("mineru_essential_tree_sha256"):
        raise SystemExit("MINERU_SOURCE_CHANGED")
    if current_discovery(source["essential_tree_sha256"]) != manifest.get("current_discovery"):
        raise SystemExit("DISCOVERY_CHANGED")
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    if receipt != receipt_value(manifest, manifest_bytes):
        raise SystemExit("RECEIPT_MISMATCH")
    return {
        "status": "VALID",
        "source_id": manifest["source_id"],
        "content_identity_status": manifest["content_identity_status"],
        "byte_provenance_status": manifest["byte_provenance_status"],
        "mathematics_status": manifest["mathematics_status"],
        "file_count": manifest["file_count"],
        "total_bytes": manifest["total_bytes"],
        "tree_sha256": manifest["tree_sha256"],
        "pdf_pages": manifest["canonical_input"]["pdf_pages"],
        "printed_pages": manifest["bibliographic_identity"]["printed_pages"],
        "current_unique_content_groups": manifest["current_discovery"]["unique_content_group_count"],
        "source_directories_preserved": manifest["current_discovery"]["source_directories_preserved"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    if args.verify_only:
        print(json.dumps(verify(), ensure_ascii=False, sort_keys=True))
        return 0
    if DEST.exists():
        raise SystemExit("IMPORT_DESTINATION_ALREADY_EXISTS")
    source = inspect_source()
    DEST.parent.mkdir(parents=True, exist_ok=True)
    temp = DEST.with_name(f".{DEST.name}.tmp-{uuid.uuid4().hex}")
    temp.mkdir(parents=False, exist_ok=False)
    try:
        manifest = build_manifest(temp, source)
        manifest_bytes = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
        (temp / "IMPORT.json").write_bytes(manifest_bytes)
        (temp / "RECEIPT.json").write_text(
            json.dumps(receipt_value(manifest, manifest_bytes), ensure_ascii=False, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
        )
        os.replace(temp, DEST)
    finally:
        if temp.exists():
            shutil.rmtree(temp)
    print(json.dumps(verify(), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
