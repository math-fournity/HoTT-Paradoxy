#!/usr/bin/env python3
"""Extract and verify Post's 1944 article from the archived BAMS issue."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path

from pypdf import PdfReader, PdfWriter, __version__ as pypdf_version


ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path("/Volumes/D/HoTT-literature-cache/Post-1944-IA-issue/Bulletin-AMS-1944-50-5.pdf")
OUTPUT = ROOT / "外部资料/Post-1944-Recursively-Enumerable-Sets.pdf"
IMPORT_ROOT = ROOT / "audit/literature/LIT-CLASSICS-001/post-1944-primary"
TEXT_OUTPUT = IMPORT_ROOT / "full.txt"
PAGE_MAP = IMPORT_ROOT / "PAGE_MAP.json"
IMPORT = IMPORT_ROOT / "IMPORT.json"
PAGE_INDICES = list(range(1, 34))
SOURCE_BYTES = 13900730
SOURCE_SHA1 = "9d14c7c102ed115b14606ab7a3d691c1ed5b637e"
SOURCE_SHA256 = "1a3a03de9488ea9c339775b456adc6264e0e15b11d832ad37da7775fcf5ecbcb"
SOURCE_MD5 = "82372cb16def8b3ac44fccba55f75fb5"


class ImportError(RuntimeError):
    pass


def digest(data: bytes, algorithm: str = "sha256") -> str:
    return hashlib.new(algorithm, data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def file_row(path: Path, relative: bool = True) -> dict[str, object]:
    if not path.is_file() or path.is_symlink():
        raise ImportError(f"FILE_INVALID:{path}")
    data = path.read_bytes()
    return {
        "path": path.relative_to(ROOT).as_posix() if relative else str(path),
        "bytes": len(data),
        "sha256": digest(data),
    }


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temp = Path(temporary)
        if temp.exists():
            temp.unlink()


def verify_source() -> PdfReader:
    row = file_row(SOURCE, relative=False)
    data = SOURCE.read_bytes()
    if row["bytes"] != SOURCE_BYTES or row["sha256"] != SOURCE_SHA256:
        raise ImportError("SOURCE_SHA256_OR_SIZE_MISMATCH")
    if digest(data, "sha1") != SOURCE_SHA1 or digest(data, "md5") != SOURCE_MD5:
        raise ImportError("SOURCE_PUBLISHER_DIGEST_MISMATCH")
    reader = PdfReader(SOURCE)
    if len(reader.pages) != 69 or reader.is_encrypted:
        raise ImportError("SOURCE_PDF_STRUCTURE_INVALID")
    return reader


def page_texts(reader: PdfReader) -> list[str]:
    texts = [(reader.pages[index].extract_text() or "").strip() for index in PAGE_INDICES]
    if "RECURSIVELY ENUMERABLE SETS OF POSITIVE" not in texts[0] or "EMIL L. POST" not in texts[0]:
        raise ImportError("FIRST_ARTICLE_PAGE_ANCHOR_MISSING")
    if not texts[0].endswith("284"):
        raise ImportError("FIRST_PRINTED_PAGE_NUMBER_MISMATCH")
    if not texts[-1].startswith("316 E. L. POST") or "Tue City" not in texts[-1]:
        raise ImportError("LAST_ARTICLE_PAGE_ANCHOR_MISSING")
    outside = (reader.pages[34].extract_text() or "")
    if "THE FEBRUARY MEETING IN NEW YORK" not in outside:
        raise ImportError("ARTICLE_END_BOUNDARY_NOT_CONFIRMED")
    return texts


def create_pdf(reader: PdfReader) -> None:
    if OUTPUT.exists():
        raise ImportError("OUTPUT_ALREADY_EXISTS")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()
    for index in PAGE_INDICES:
        writer.add_page(reader.pages[index])
    writer.add_metadata({
        "/Title": "Recursively Enumerable Sets of Positive Integers and Their Decision Problems",
        "/Author": "Emil L. Post",
        "/Subject": "Bulletin of the American Mathematical Society 50 (1944), 284-316",
        "/Source": "Internet Archive issue sim_american-mathematical-society-bulletin_1944-05_50_5",
    })
    fd, temporary = tempfile.mkstemp(prefix=f".{OUTPUT.name}.", dir=OUTPUT.parent)
    os.close(fd)
    try:
        with open(temporary, "wb") as handle:
            writer.write(handle)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, OUTPUT)
    finally:
        temp = Path(temporary)
        if temp.exists():
            temp.unlink()


def compute_documents() -> dict[Path, bytes]:
    reader = verify_source()
    texts = page_texts(reader)
    if not OUTPUT.is_file() or OUTPUT.is_symlink():
        raise ImportError("EXTRACTED_ARTICLE_PDF_MISSING")
    article = PdfReader(OUTPUT)
    if len(article.pages) != 33 or article.is_encrypted:
        raise ImportError("EXTRACTED_ARTICLE_PDF_STRUCTURE_INVALID")
    extracted_texts = [(page.extract_text() or "").strip() for page in article.pages]
    if extracted_texts != texts:
        raise ImportError("EXTRACTED_ARTICLE_TEXT_DIFFERS_FROM_SOURCE_PAGES")
    full_text = "\n\n".join(
        f"===== PDF PAGE {position + 1} / PRINTED PAGE {284 + position} =====\n{text}"
        for position, text in enumerate(texts)
    ) + "\n"
    page_map = {
        "schema_version": "post-1944-page-map/v1",
        "source_pdf_pages_zero_based": PAGE_INDICES,
        "article_pdf_pages_one_based": list(range(1, 34)),
        "printed_pages": list(range(284, 317)),
        "pages": [
            {
                "source_index": source_index,
                "article_page": position + 1,
                "printed_page": 284 + position,
                "text_bytes": len(text.encode("utf-8")),
                "text_sha256": digest(text.encode("utf-8")),
                "first_line": text.splitlines()[0] if text.splitlines() else "",
            }
            for position, (source_index, text) in enumerate(zip(PAGE_INDICES, texts, strict=True))
        ],
        "next_source_page_anchor": "THE FEBRUARY MEETING IN NEW YORK / printed page 317",
    }
    documents = {
        TEXT_OUTPUT: full_text.encode("utf-8"),
        PAGE_MAP: json_bytes(page_map),
    }
    output_row = file_row(OUTPUT)
    text_row = {
        "path": TEXT_OUTPUT.relative_to(ROOT).as_posix(),
        "bytes": len(documents[TEXT_OUTPUT]),
        "sha256": digest(documents[TEXT_OUTPUT]),
    }
    page_map_row = {
        "path": PAGE_MAP.relative_to(ROOT).as_posix(),
        "bytes": len(documents[PAGE_MAP]),
        "sha256": digest(documents[PAGE_MAP]),
    }
    manifest = {
        "schema_version": "post-1944-primary-import/v1",
        "source": {
            "archive_item": "sim_american-mathematical-society-bulletin_1944-05_50_5",
            "archive_metadata_url": "https://archive.org/metadata/sim_american-mathematical-society-bulletin_1944-05_50_5",
            "download_url": "https://archive.org/download/sim_american-mathematical-society-bulletin_1944-05_50_5/sim_american-mathematical-society-bulletin_1944-05_50_5.pdf",
            "resolved_mirror": "https://ia800802.us.archive.org/19/items/sim_american-mathematical-society-bulletin_1944-05_50_5/sim_american-mathematical-society-bulletin_1944-05_50_5.pdf",
            "local_path": str(SOURCE),
            "bytes": SOURCE_BYTES,
            "sha1": SOURCE_SHA1,
            "sha256": SOURCE_SHA256,
            "md5": SOURCE_MD5,
            "etag": "65dba883-d41bba",
            "range_probe": "206 bytes 0-0/13900730",
            "download": "aria2c 1.37.0; 8 connections; 1MiB logical pieces; SHA-1 verified",
            "issue": "Bulletin of the American Mathematical Society 50(5), May 1944",
            "pages": 69,
        },
        "article": {
            "title": "Recursively Enumerable Sets of Positive Integers and Their Decision Problems",
            "author": "Emil L. Post",
            "doi": "10.1090/S0002-9904-1944-08111-1",
            "printed_pages": "284-316",
            "source_pdf_indices_zero_based": "1-33",
            "extracted_pages": 33,
        },
        "outputs": [output_row, text_row, page_map_row],
        "generator": {"path": "scripts/audit/import_post_1944_primary.py", "pypdf_version": pypdf_version},
        "preserved_invalid_response": {
            "path": "tmp/pdfs/LIT-CLASSICS-001/Post-1944-RE-Sets.pdf",
            "bytes": 5908,
            "sha256": "b2ff2e9802bc602fc5dff310b4c00f46acbcf040f4b3a60706d127906d3b3158",
            "identity": "HTML_ACCESS_VALIDATION_PAGE_NOT_PDF"
        },
        "evidence_boundary": "PRIMARY_ISSUE_SCAN_EXTRACTED_AND_TEXT_BOUNDARIES_VERIFIED; MATHEMATICAL_THEOREMS_SOURCE_REPORTED_NOT_REPLAYED"
    }
    documents[IMPORT] = json_bytes(manifest)
    return documents


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        reader = verify_source()
        page_texts(reader)
        if args.write and not OUTPUT.exists():
            create_pdf(reader)
        documents = compute_documents()
        if args.write:
            for path, data in documents.items():
                atomic_write(path, data)
        else:
            for path, data in documents.items():
                if not path.is_file() or path.is_symlink() or path.read_bytes() != data:
                    raise ImportError(f"OUTPUT_MISMATCH:{path}")
        manifest = json.loads(documents[IMPORT].decode("utf-8"))
        print(json.dumps({
            "status": "VALID", "writes": args.write,
            "article_pages": manifest["article"]["extracted_pages"],
            "source_sha1": manifest["source"]["sha1"],
            "output_pdf_sha256": manifest["outputs"][0]["sha256"],
            "text_bytes": manifest["outputs"][1]["bytes"],
        }, ensure_ascii=False))
        return 0
    except (ImportError, OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "INVALID", "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
