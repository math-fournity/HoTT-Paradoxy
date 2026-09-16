#!/usr/bin/env python3
"""Import the second user-produced MinerU batch for LIT-CLASSICS-001.

The batch contains three new content groups: Kleene's 1938 primary article,
Peter Smith's later historical exposition, and Benjamin Peters's 2022
bachelor's thesis.  The latter two discuss Rosser 1936 but are not the
Rosser article itself.  The importer also records content-level deduplication
of every MinerU directory created on 2026-09-14 and never deletes a source.
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
INPUT = ROOT / "audit/literature/PDF-to-Markdown-20260914"
MINERU_ROOT = Path("/Users/aurolafly/MinerU")
EXISTING_IMPORT = ROOT / "audit/literature/LIT-CLASSICS-001/mineru/IMPORT.json"
DEST = ROOT / "audit/literature/LIT-CLASSICS-001/mineru-supplement"
MANIFEST = DEST / "IMPORT.json"
RECEIPT = DEST / "RECEIPT.json"
DISCOVERY_DATE = "2026-09-14"
IMAGE_PATTERN = re.compile(r"images/[0-9a-f]{64}\.(?:jpg|jpeg|png)")


SOURCES: list[dict[str, Any]] = [
    {
        "id": "KLEENE-1938",
        "title": "On Notation for Ordinal Numbers",
        "source_role": "PRIMARY_ORIGINAL_ARTICLE",
        "rosser_1936_primary_body": False,
        "official_url": "https://doi.org/10.2307/2267778",
        "user_pdf": ROOT / "外部资料/Kleene - Ordinals.pdf",
        "input_pdf": INPUT / "Kleene-1938-Ordinal-Notation.pdf",
        "pages": 7,
        "bytes": 238353,
        "sha256": "4f08a85898e5642b92eff3337174675f970d0a9bca0a8c1b701bd92d53601d45",
        "anchor": "ON NOTATION FOR ORDINAL NUMBERS",
        "mineru": MINERU_ROOT / "Kleene - Ordinals.pdf-c8bf794c-235c-40d3-9e93-3936627ead00",
        "dest_stem": "Kleene-1938-On-Notation-for-Ordinal-Numbers",
    },
    {
        "id": "SMITH-EXPOSITION2",
        "title": "Expounding the First Incompleteness Theorem",
        "source_role": "SECONDARY_HISTORICAL_EXPOSITION_FOR_ROSSER_1936",
        "rosser_1936_primary_body": False,
        "official_url": "https://www.logicmatters.net/resources/pdfs/Exposition2.pdf",
        "user_pdf": ROOT / "外部资料/Rosser-1936-Extensions/Exposition2.pdf",
        "input_pdf": INPUT / "Peter-Smith-Expounding-First-Incompleteness.pdf",
        "pages": 33,
        "bytes": 391792,
        "sha256": "4ce2eebc1a2280f1169b4c09747afb94e691d8915cdb77edee7a504c4299bd1a",
        "anchor": "EXPOUNDING THE FIRST INCOMPLETENESS THEOREM",
        "mineru": MINERU_ROOT / "Exposition2.pdf-a45e49ec-3790-4870-bd9f-c21ad6e2e2ba",
        "dest_stem": "Peter-Smith-Expounding-the-First-Incompleteness-Theorem",
    },
    {
        "id": "PETERS-2022-THESIS",
        "title": "Gödel's Theorem Without Tears: Essential Incompleteness in Synthetic Computability",
        "source_role": "PRIMARY_FOR_OWN_THESIS_AND_MECHANIZATION_SECONDARY_FOR_ROSSER_1936",
        "rosser_1936_primary_body": False,
        "official_url": "https://www.ps.uni-saarland.de/~peters/bachelor/resources/thesis.screen.pdf",
        "user_pdf": ROOT / "外部资料/Rosser-1936-Extensions/thesis.screen.edited.pdf",
        "input_pdf": INPUT / "Peters-2022-Godel-Without-Tears-Bachelors-Thesis.pdf",
        "pages": 48,
        "bytes": 710984,
        "sha256": "d186581905329d182d361dee3ab61ced9e1bc2b23778f43aab763dc7817dbeed",
        "anchor": "Essential Incompleteness in Synthetic Computability",
        "mineru": MINERU_ROOT / "thesis.screen.edited.pdf-64b37a1f-72a0-43bc-a233-69dbaa49da52",
        "dest_stem": "Peters-2022-Godel-Without-Tears-Bachelors-Thesis",
    },
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def one(root: Path, pattern: str, label: str) -> Path:
    rows = sorted(root.glob(pattern))
    if len(rows) != 1 or not rows[0].is_file() or rows[0].is_symlink():
        raise SystemExit(f"{label}_COUNT:{root}:{len(rows)}")
    return rows[0]


def file_row(path: Path, rel_root: Path) -> dict[str, Any]:
    return {
        "path": path.relative_to(rel_root).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha(path),
    }


def inspect_mineru(root: Path) -> dict[str, Any]:
    if not root.is_dir() or root.is_symlink():
        raise SystemExit(f"MINERU_ROOT_INVALID:{root}")
    markdown = root / "full.md"
    origin = one(root, "*_origin.pdf", "ORIGIN_PDF")
    content = one(root, "*_content_list_v2.json", "CONTENT_LIST_V2")
    if not markdown.is_file() or markdown.is_symlink():
        raise SystemExit(f"MINERU_MARKDOWN_INVALID:{root}")
    if origin.read_bytes()[:5] != b"%PDF-":
        raise SystemExit(f"MINERU_ORIGIN_NOT_PDF:{root}")
    markdown_text = markdown.read_text(encoding="utf-8")
    content_text = content.read_text(encoding="utf-8")
    refs = sorted(set(IMAGE_PATTERN.findall(markdown_text)) | set(IMAGE_PATTERN.findall(content_text)))
    for rel in refs:
        path = root / rel
        if not path.is_file() or path.is_symlink():
            raise SystemExit(f"MINERU_IMAGE_MISSING:{root}:{rel}")
    essential_files = [markdown, origin, content] + [root / rel for rel in refs]
    essential_rows = [
        {
            "path": (
                "full.md"
                if path == markdown
                else "origin.pdf"
                if path == origin
                else "content-list-v2.json"
                if path == content
                else path.relative_to(root).as_posix()
            ),
            "bytes": path.stat().st_size,
            "sha256": sha(path),
        }
        for path in essential_files
    ]
    digest = hashlib.sha256()
    for row in essential_rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {
        "root": root,
        "markdown": markdown,
        "origin": origin,
        "content": content,
        "markdown_text": markdown_text,
        "content_value": json.loads(content_text),
        "image_refs": refs,
        "essential_files": essential_rows,
        "essential_tree_sha256": digest.hexdigest(),
        "fingerprints": {
            "full_md_sha256": sha(markdown),
            "origin_pdf_sha256": sha(origin),
            "content_list_v2_sha256": sha(content),
            "referenced_image_count": len(refs),
        },
    }


def inspect_source(spec: dict[str, Any]) -> dict[str, Any]:
    for label in ("user_pdf", "input_pdf"):
        path = Path(spec[label])
        if not path.is_file() or path.is_symlink() or path.read_bytes()[:5] != b"%PDF-":
            raise SystemExit(f"{label.upper()}_INVALID:{path}")
        if path.stat().st_size != spec["bytes"] or sha(path) != spec["sha256"]:
            raise SystemExit(f"{label.upper()}_IDENTITY_MISMATCH:{path}")
    if sha(Path(spec["user_pdf"])) != sha(Path(spec["input_pdf"])):
        raise SystemExit(f"INPUT_COPY_NOT_BYTE_IDENTICAL:{spec['id']}")
    row = inspect_mineru(Path(spec["mineru"]))
    if str(spec["anchor"]).casefold() not in row["markdown_text"].casefold():
        raise SystemExit(f"TITLE_ANCHOR_MISSING:{spec['id']}")
    content_value = row["content_value"]
    if not isinstance(content_value, list) or len(content_value) != spec["pages"]:
        actual = len(content_value) if isinstance(content_value, list) else "NOT_LIST"
        raise SystemExit(f"PAGE_COUNT_MISMATCH:{spec['id']}:{actual}")
    row["spec"] = spec
    return row


def discovery_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not MINERU_ROOT.is_dir():
        raise SystemExit(f"MINERU_DISCOVERY_ROOT_MISSING:{MINERU_ROOT}")
    for root in sorted(path for path in MINERU_ROOT.iterdir() if path.is_dir() and path.name != "data"):
        local_date = dt.datetime.fromtimestamp(root.stat().st_mtime).date().isoformat()
        if local_date != DISCOVERY_DATE:
            continue
        row = inspect_mineru(root)
        rows.append(
            {
                "root": str(root),
                "name": root.name,
                "essential_tree_sha256": row["essential_tree_sha256"],
                "fingerprints": row["fingerprints"],
                "essential_files": row["essential_files"],
            }
        )
    return rows


def existing_group_map() -> dict[str, list[str]]:
    value = json.loads(EXISTING_IMPORT.read_text(encoding="utf-8"))
    if value.get("schema_version") != "lit-classics-mineru-import/v1":
        raise SystemExit("EXISTING_IMPORT_SCHEMA_INVALID")
    groups: dict[str, list[str]] = defaultdict(list)
    for row in value.get("rows", []):
        source_root = Path(str(row["mineru_source_root"]))
        fingerprint = inspect_mineru(source_root)["essential_tree_sha256"]
        groups[fingerprint].append(str(row["id"]))
    return dict(groups)


def build_discovery(inspected: list[dict[str, Any]]) -> dict[str, Any]:
    rows = discovery_rows()
    existing = existing_group_map()
    supplement = {row["essential_tree_sha256"]: str(row["spec"]["id"]) for row in inspected}
    if len(supplement) != len(inspected):
        raise SystemExit("SUPPLEMENT_SELECTED_CONTENT_COLLISION")
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        groups[row["essential_tree_sha256"]].append(row)
    output: list[dict[str, Any]] = []
    unclassified: list[str] = []
    for number, (fingerprint, members) in enumerate(
        sorted(groups.items(), key=lambda item: item[1][0]["name"]), start=1
    ):
        if fingerprint in existing:
            disposition = "ALREADY_IMPORTED_V1"
            owner_ids = sorted(existing[fingerprint])
        elif fingerprint in supplement:
            disposition = "IMPORTED_SUPPLEMENT"
            owner_ids = [supplement[fingerprint]]
        else:
            disposition = "UNCLASSIFIED_UNIQUE_GROUP"
            owner_ids = []
            unclassified.append(fingerprint)
        output.append(
            {
                "group_id": f"DG-{number:03d}",
                "essential_tree_sha256": fingerprint,
                "member_count": len(members),
                "members": members,
                "disposition": disposition,
                "owner_ids": owner_ids,
                "deletion_performed": False,
            }
        )
    if unclassified:
        raise SystemExit(f"MINERU_DISCOVERY_UNCLASSIFIED:{len(unclassified)}")
    imported = [row for row in output if row["disposition"] == "IMPORTED_SUPPLEMENT"]
    if len(imported) != len(inspected):
        raise SystemExit(f"SUPPLEMENT_DISCOVERY_COUNT:{len(imported)}")
    return {
        "selection_rule": "DIRECTORIES_WITH_LOCAL_MTIME_DATE_2026-09-14",
        "source_root": str(MINERU_ROOT),
        "directory_count": len(rows),
        "unique_content_group_count": len(output),
        "duplicate_directory_count": len(rows) - len(output),
        "already_imported_group_count": sum(row["disposition"] == "ALREADY_IMPORTED_V1" for row in output),
        "supplement_group_count": len(imported),
        "unclassified_group_count": 0,
        "deduplication_identity": "full.md + normalized origin.pdf + content-list-v2.json + every referenced image, all byte-hashed",
        "source_directories_preserved": True,
        "groups": output,
    }


def copy_source(row: dict[str, Any], dest_root: Path) -> dict[str, Any]:
    spec = row["spec"]
    target = dest_root / str(spec["dest_stem"])
    target.mkdir(parents=True, exist_ok=False)
    shutil.copy2(row["markdown"], target / "full.md")
    shutil.copy2(row["origin"], target / "origin.pdf")
    shutil.copy2(row["content"], target / "content-list-v2.json")
    for rel in row["image_refs"]:
        source = row["root"] / rel
        destination = target / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    user_pdf = Path(spec["user_pdf"])
    input_pdf = Path(spec["input_pdf"])
    return {
        "id": spec["id"],
        "title": spec["title"],
        "source_role": spec["source_role"],
        "rosser_1936_primary_body": spec["rosser_1936_primary_body"],
        "official_url": spec["official_url"],
        "user_pdf": {
            "path": user_pdf.relative_to(ROOT).as_posix(),
            "bytes": user_pdf.stat().st_size,
            "sha256": sha(user_pdf),
            "pages": spec["pages"],
        },
        "canonical_input_copy": {
            "path": input_pdf.relative_to(ROOT).as_posix(),
            "bytes": input_pdf.stat().st_size,
            "sha256": sha(input_pdf),
            "relation_to_user_pdf": "BYTE_IDENTICAL_COPY",
        },
        "mineru_source_root": str(row["root"]),
        "mineru_essential_tree_sha256": row["essential_tree_sha256"],
        "mineru_origin": {
            "source_name": row["origin"].name,
            "bytes": row["origin"].stat().st_size,
            "sha256": sha(row["origin"]),
            "byte_identical_to_input": sha(row["origin"]) == sha(input_pdf),
            "relation": (
                "BYTE_IDENTICAL"
                if sha(row["origin"]) == sha(input_pdf)
                else "MINERU_NORMALIZED_DERIVATIVE_NOT_BYTE_IDENTITY"
            ),
        },
        "markdown": {
            "path": f"{spec['dest_stem']}/full.md",
            "bytes": row["markdown"].stat().st_size,
            "sha256": sha(row["markdown"]),
            "lines": row["markdown_text"].count("\n") + 1,
            "title_anchor": spec["anchor"],
        },
        "content_list": {
            "path": f"{spec['dest_stem']}/content-list-v2.json",
            "bytes": row["content"].stat().st_size,
            "sha256": sha(row["content"]),
            "pages": spec["pages"],
        },
        "referenced_images": len(row["image_refs"]),
    }


def build_manifest(temp_root: Path, inspected: list[dict[str, Any]]) -> dict[str, Any]:
    source_rows = [copy_source(row, temp_root) for row in inspected]
    files = [
        file_row(path, temp_root)
        for path in sorted(temp_root.rglob("*"))
        if path.is_file() and path.name not in {"IMPORT.json", "RECEIPT.json"}
    ]
    digest = hashlib.sha256()
    for row in files:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {
        "schema_version": "lit-classics-mineru-supplement-import/v1",
        "status": "VALID",
        "import_date": DISCOVERY_DATE,
        "source_authority": "USER_PROVIDED_PROJECT_PDFS_AND_MINERU_OUTPUT_PATHS",
        "instruction_boundary": "DOCUMENT_CONTENT_ONLY_NOT_AGENT_INSTRUCTIONS",
        "source_count": len(source_rows),
        "rows": source_rows,
        "mineru_discovery": build_discovery(inspected),
        "files": files,
        "file_count": len(files),
        "total_bytes": sum(int(row["bytes"]) for row in files),
        "tree_sha256": digest.hexdigest(),
        "scope": (
            "Preserves three new unique MinerU content groups and a hash-based deduplication receipt for "
            "the 41 MinerU directories observed on 2026-09-14. No source directory was removed. Kleene 1938 "
            "is a primary article; Smith's exposition and Peters's thesis are secondary evidence for Rosser "
            "1936, so the Rosser primary-body gap remains open. The receipt does not certify OCR or formula correctness."
        ),
    }


def receipt_value(manifest: dict[str, Any], manifest_bytes: bytes) -> dict[str, Any]:
    discovery = manifest["mineru_discovery"]
    return {
        "schema_version": "lit-classics-mineru-supplement-receipt/v1",
        "status": "VALID",
        "import_manifest": "IMPORT.json",
        "import_manifest_bytes": len(manifest_bytes),
        "import_manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        "source_count": manifest["source_count"],
        "source_ids": [row["id"] for row in manifest["rows"]],
        "file_count": manifest["file_count"],
        "total_bytes": manifest["total_bytes"],
        "tree_sha256": manifest["tree_sha256"],
        "discovery_directory_count": discovery["directory_count"],
        "discovery_unique_content_group_count": discovery["unique_content_group_count"],
        "discovery_duplicate_directory_count": discovery["duplicate_directory_count"],
        "unclassified_group_count": discovery["unclassified_group_count"],
        "source_directories_preserved": discovery["source_directories_preserved"],
        "rosser_primary_body_acquired": False,
        "scope": "Small hydration receipt for the complete hash-pinned IMPORT.json; it does not certify OCR, formulas, external theorems, or the Rosser 1936 primary body.",
    }


def write_receipt_only() -> dict[str, Any]:
    if RECEIPT.exists():
        raise SystemExit("RECEIPT_ALREADY_EXISTS")
    manifest_bytes = MANIFEST.read_bytes()
    manifest = json.loads(manifest_bytes)
    if manifest.get("schema_version") != "lit-classics-mineru-supplement-import/v1":
        raise SystemExit("MANIFEST_SCHEMA_INVALID")
    value = receipt_value(manifest, manifest_bytes)
    temp = RECEIPT.with_name(f".{RECEIPT.name}.tmp-{uuid.uuid4().hex}")
    try:
        temp.write_text(
            json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
        )
        os.replace(temp, RECEIPT)
    finally:
        if temp.exists():
            temp.unlink()
    return verify()


def verify() -> dict[str, Any]:
    manifest_bytes = MANIFEST.read_bytes()
    manifest = json.loads(manifest_bytes)
    if manifest.get("schema_version") != "lit-classics-mineru-supplement-import/v1":
        raise SystemExit("MANIFEST_SCHEMA_INVALID")
    expected = manifest.get("files")
    if not isinstance(expected, list):
        raise SystemExit("MANIFEST_FILES_INVALID")
    actual_paths = sorted(
        path.relative_to(DEST).as_posix()
        for path in DEST.rglob("*")
        if path.is_file() and path.name not in {"IMPORT.json", "RECEIPT.json"}
    )
    expected_paths = sorted(str(row.get("path")) for row in expected if isinstance(row, dict))
    if actual_paths != expected_paths:
        raise SystemExit("IMPORT_PATH_SET_MISMATCH")
    for row in expected:
        path = DEST / str(row["path"])
        if path.stat().st_size != row["bytes"] or sha(path) != row["sha256"]:
            raise SystemExit(f"IMPORT_FILE_MISMATCH:{row['path']}")
    digest = hashlib.sha256()
    for row in expected:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    if digest.hexdigest() != manifest.get("tree_sha256"):
        raise SystemExit("IMPORT_TREE_MISMATCH")
    discovery = manifest.get("mineru_discovery")
    if not isinstance(discovery, dict) or discovery.get("unclassified_group_count") != 0:
        raise SystemExit("DISCOVERY_MANIFEST_INVALID")
    observed_members = 0
    for group in discovery.get("groups", []):
        members = group.get("members", [])
        observed_members += len(members)
        for member in members:
            current = inspect_mineru(Path(str(member["root"])))
            if current["essential_tree_sha256"] != group["essential_tree_sha256"]:
                raise SystemExit(f"DISCOVERY_SOURCE_CHANGED:{member['root']}")
        if group.get("deletion_performed") is not False:
            raise SystemExit(f"DISCOVERY_DELETION_FLAG_INVALID:{group.get('group_id')}")
    if observed_members != discovery.get("directory_count"):
        raise SystemExit("DISCOVERY_DIRECTORY_COUNT_MISMATCH")
    for spec in SOURCES:
        for label in ("user_pdf", "input_pdf"):
            path = Path(spec[label])
            if path.stat().st_size != spec["bytes"] or sha(path) != spec["sha256"]:
                raise SystemExit(f"{label.upper()}_CHANGED:{spec['id']}")
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    expected_receipt = receipt_value(manifest, manifest_bytes)
    if receipt != expected_receipt:
        raise SystemExit("RECEIPT_MISMATCH")
    return {
        "status": "VALID",
        "source_count": manifest["source_count"],
        "file_count": manifest["file_count"],
        "total_bytes": manifest["total_bytes"],
        "tree_sha256": manifest["tree_sha256"],
        "discovery_directory_count": discovery["directory_count"],
        "discovery_unique_content_group_count": discovery["unique_content_group_count"],
        "discovery_duplicate_directory_count": discovery["duplicate_directory_count"],
        "unclassified_group_count": discovery["unclassified_group_count"],
        "source_directories_preserved": discovery["source_directories_preserved"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--write-receipt", action="store_true")
    modes.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    if args.verify_only:
        print(json.dumps(verify(), ensure_ascii=False, sort_keys=True))
        return 0
    if args.write_receipt:
        print(json.dumps(write_receipt_only(), ensure_ascii=False, sort_keys=True))
        return 0
    if DEST.exists():
        raise SystemExit("IMPORT_DESTINATION_ALREADY_EXISTS")
    inspected = [inspect_source(spec) for spec in SOURCES]
    DEST.parent.mkdir(parents=True, exist_ok=True)
    temp = DEST.with_name(f".{DEST.name}.tmp-{uuid.uuid4().hex}")
    temp.mkdir(parents=False, exist_ok=False)
    try:
        manifest = build_manifest(temp, inspected)
        manifest_bytes = (
            json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
        ).encode("utf-8")
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
