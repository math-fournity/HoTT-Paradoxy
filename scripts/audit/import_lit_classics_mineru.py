#!/usr/bin/env python3
"""Import the user-produced MinerU corpus for LIT-CLASSICS-001.

The MinerU ``*_origin.pdf`` files are normalized derivatives and are not
assumed byte-identical to the project input PDFs.  The import records both
identities and preserves Markdown, page-structured content, the normalized
origin, and every referenced image in an immutable destination tree.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "audit/literature/PDF-to-Markdown-20260914"
DEST = ROOT / "audit/literature/LIT-CLASSICS-001/mineru"
MANIFEST = DEST / "IMPORT.json"
IMAGE_PATTERN = re.compile(r"images/[0-9a-f]{64}\.(?:jpg|jpeg|png)")


SOURCES = [
    {
        "id": "LAWVERE-1969",
        "pdf": "Lawvere-1969-Diagonal.pdf",
        "pages": 14,
        "bytes": 134978,
        "sha256": "65ae0958cb0f6350da05499f9d772732111338315c794fcb8aae37052b5f3897",
        "anchor": "DIAGONAL ARGUMENTS AND CARTESIAN CLOSED CATEGORIES",
        "mineru": "/Users/aurolafly/MinerU/Lawvere-1969-Diagonal.pdf-180baeed-beec-49cc-b5a4-02ae06577e4d",
    },
    {
        "id": "KIRST-HERMES-2021",
        "pdf": "Kirst-Hermes-2021-Synthetic-Undecidability.pdf",
        "pages": 20,
        "bytes": 801450,
        "sha256": "b5738da6699457c88a9040baf022ad4b750260bbbc8def2e6c3df4422e302d8a",
        "anchor": "Synthetic Undecidability and Incompleteness of First-Order Axiom Systems in Coq",
        "mineru": "/Users/aurolafly/MinerU/Kirst-Hermes-2021-Synthetic-Undecidability.pdf-cfeb0de2-9737-47d4-b414-5d0dfe7bfaed",
    },
    {
        "id": "2LTT-2017",
        "pdf": "Annenkov-Capriotti-Kraus-Sattler-2017-2LTT.pdf",
        "pages": 58,
        "bytes": 1100607,
        "sha256": "ac2a753e2e2e923d1aad19d324032299591b7d41504cfc289db65369a9fa958a",
        "anchor": "TWO-LEVEL TYPE THEORY AND APPLICATIONS",
        "mineru": "/Users/aurolafly/MinerU/Annenkov-Capriotti-Kraus-Sattler-2017-2LTT.pdf-69854ef4-cfff-49d9-a5a8-0fdac75cbc76",
    },
    {
        "id": "TURING-1936",
        "pdf": "Turing-1936-On-Computable-Numbers.pdf",
        "pages": 38,
        "bytes": 339421,
        "sha256": "b88da293ad7965c53c2726c19cf3fe68c549a1202cfd6d1a79224890f11b627d",
        "anchor": "ON COMPUTABLE NUMBERS, WITH AN APPLICATION TO THE ENTSCHEIDUNGSPROBLEM",
        "mineru": "/Users/aurolafly/MinerU/Turing-1936-On-Computable-Numbers.pdf-6a9e1c15-3cc7-448d-a5ad-8fc93cc2cd26",
    },
    {
        "id": "RICE-1953",
        "pdf": "Rice-1953-RE-Classes.pdf",
        "pages": 9,
        "bytes": 799682,
        "sha256": "9ac76ec7e30cd84512acea6b00f32cc9c46e1e25506323e6329eede22af43f34",
        "anchor": "CLASSES OF RECURSIVELY ENUMERABLE SETS AND THEIR DECISION PROBLEMS",
        "mineru": "/Users/aurolafly/MinerU/Rice-1953-RE-Classes.pdf-c88dfa8a-7fef-4641-8d61-14a2a73e06a1",
    },
    {
        "id": "GODEL-1931",
        "pdf": "Godel-1931-Unentscheidbare-Saetze.pdf",
        "pages": 26,
        "bytes": 1431327,
        "sha256": "49e3116e2fea8026c7744976e5d4abb8fb08c381229c5f6164da5d73668d9b05",
        "anchor": "Über formal unentscheidbare Sätze der Principia Mathematica",
        "mineru": "/Users/aurolafly/MinerU/Godel-1931-Unentscheidbare-Saetze.pdf-18b7fb9e-0b3c-4af2-8f60-9580593f8488",
    },
    {
        "id": "OCONNOR-2005-PAPER",
        "pdf": "OConnor-2005-Essential-Incompleteness-paper.pdf",
        "pages": 17,
        "bytes": 188561,
        "sha256": "d5acae99fa9a5a55e041c99af50829225498083b134cdf2a10ca68fd367d9610",
        "anchor": "Essential Incompleteness of Arithmetic Verified by Coq",
        "mineru": "/Users/aurolafly/MinerU/OConnor-2005-Essential-Incompleteness-paper.pdf-b1e74a5d-4ed7-485b-9e6e-1b6ff31d4863",
    },
    {
        "id": "CHURCH-1936",
        "pdf": "Church-1936-Unsolvable-Problem.pdf",
        "pages": 20,
        "bytes": 920839,
        "sha256": "d5c7e12252d07bb07f1e5ceee1786008fc9cb0849778d6a585f092da35199323",
        "anchor": "AN UNSOLVABLE PROBLEM OF ELEMENTARY NUMBER THEORY",
        "mineru": "/Users/aurolafly/MinerU/Church-1936-Unsolvable-Problem.pdf-b0131bb1-24e4-4e7f-a7d3-e8ac984b95f5",
    },
    {
        "id": "OCONNOR-2005-SLIDES",
        "pdf": "OConnor-2005-Essential-Incompleteness-slides.pdf",
        "pages": 28,
        "bytes": 932441,
        "sha256": "af5a5ccdbf83aa0030e9c2c77dacbcb0b3949d506207f9dc7d4559b4ef52a79f",
        "anchor": "Essential Incompleteness of Arithmetic Verified by Coq",
        "mineru": "/Users/aurolafly/MinerU/OConnor-2005-Essential-Incompleteness-slides.pdf-d908224c-c627-457f-9d14-7866a11ad5a5",
    },
    {
        "id": "KIRST-PETERS-2023",
        "pdf": "Kirst-Peters-2023-Godel-Without-Tears.pdf",
        "pages": 18,
        "bytes": 749481,
        "sha256": "422aa3f3aa6ee7d6721c029560d156fe86e34e96144ced5a68e495feea7231bf",
        "anchor": "Gödel’s Theorem Without Tears",
        "mineru": "/Users/aurolafly/MinerU/Kirst-Peters-2023-Godel-Without-Tears.pdf-5e95a924-0247-4010-a60c-b6b34c583f0e",
    },
    {
        "id": "SWAN-UEMURA-2019",
        "pdf": "Swan-Uemura-2019-Church-Thesis-Cubical-Assemblies.pdf",
        "pages": 23,
        "bytes": 291460,
        "sha256": "417e713e4a4a2e9353d892551e52453c3e603f3b6b3e9340ca52cec41750fff0",
        "anchor": "On Church’s Thesis in Cubical Assemblies",
        "mineru": "/Users/aurolafly/MinerU/Swan-Uemura-2019-Church-Thesis-Cubical-Assemblies.pdf-9cd6dcaf-ea62-47a0-b15f-b54fba0f15a6",
    },
    {
        "id": "LOB-1955",
        "pdf": "Lob-1955-Henkin.pdf",
        "pages": 5,
        "bytes": 303294,
        "sha256": "5f7b69331c8e83d56fc88c19e925e040701795ef4486e218cc38255a670b3c86",
        "anchor": "SOLUTION OF A PROBLEM OF LEON HENKIN",
        "mineru": "/Users/aurolafly/MinerU/Lob-1955-Henkin.pdf-1a81fec4-3929-4898-b24a-707316410c79",
    },
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def file_row(path: Path, rel_root: Path) -> dict[str, object]:
    return {
        "path": path.relative_to(rel_root).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha(path),
    }


def one(root: Path, pattern: str, label: str) -> Path:
    rows = sorted(root.glob(pattern))
    if len(rows) != 1 or not rows[0].is_file() or rows[0].is_symlink():
        raise SystemExit(f"{label}_COUNT:{root}:{len(rows)}")
    return rows[0]


def inspect_source(spec: dict[str, object]) -> dict[str, object]:
    source_root = Path(str(spec["mineru"]))
    if not source_root.is_dir() or source_root.is_symlink():
        raise SystemExit(f"MINERU_ROOT_INVALID:{source_root}")
    input_pdf = INPUT / str(spec["pdf"])
    if not input_pdf.is_file() or input_pdf.read_bytes()[:5] != b"%PDF-":
        raise SystemExit(f"INPUT_PDF_INVALID:{input_pdf}")
    if input_pdf.stat().st_size != spec["bytes"] or sha(input_pdf) != spec["sha256"]:
        raise SystemExit(f"INPUT_PDF_IDENTITY_MISMATCH:{input_pdf}")

    markdown = source_root / "full.md"
    origin = one(source_root, "*_origin.pdf", "ORIGIN_PDF")
    content = one(source_root, "*_content_list_v2.json", "CONTENT_LIST_V2")
    if not markdown.is_file() or markdown.is_symlink() or origin.read_bytes()[:5] != b"%PDF-":
        raise SystemExit(f"MINERU_PRIMARY_INVALID:{source_root}")
    markdown_text = markdown.read_text(encoding="utf-8")
    if str(spec["anchor"]).casefold() not in markdown_text.casefold():
        raise SystemExit(f"TITLE_ANCHOR_MISSING:{spec['id']}")
    content_value = json.loads(content.read_text(encoding="utf-8"))
    if not isinstance(content_value, list) or len(content_value) != spec["pages"]:
        raise SystemExit(f"PAGE_COUNT_MISMATCH:{spec['id']}:{len(content_value) if isinstance(content_value, list) else 'NOT_LIST'}")
    refs = set(IMAGE_PATTERN.findall(markdown_text))
    refs.update(IMAGE_PATTERN.findall(content.read_text(encoding="utf-8")))
    for rel in refs:
        path = source_root / rel
        if not path.is_file() or path.is_symlink():
            raise SystemExit(f"MINERU_IMAGE_MISSING:{spec['id']}:{rel}")
    return {
        "spec": spec,
        "source_root": source_root,
        "input_pdf": input_pdf,
        "markdown": markdown,
        "origin": origin,
        "content": content,
        "image_refs": sorted(refs),
    }


def copy_source(row: dict[str, object], dest_root: Path) -> dict[str, object]:
    spec = row["spec"]
    stem = Path(str(spec["pdf"])).stem
    target = dest_root / stem
    target.mkdir(parents=True, exist_ok=False)
    shutil.copy2(row["markdown"], target / "full.md")
    shutil.copy2(row["origin"], target / "origin.pdf")
    shutil.copy2(row["content"], target / "content-list-v2.json")
    for rel in row["image_refs"]:
        source = row["source_root"] / rel
        destination = target / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    return {
        "id": spec["id"],
        "input_pdf": {
            "path": row["input_pdf"].relative_to(ROOT).as_posix(),
            "bytes": row["input_pdf"].stat().st_size,
            "sha256": sha(row["input_pdf"]),
            "pages": spec["pages"],
        },
        "mineru_source_root": str(row["source_root"]),
        "mineru_origin": {
            "source_name": row["origin"].name,
            "bytes": row["origin"].stat().st_size,
            "sha256": sha(row["origin"]),
            "byte_identical_to_input": sha(row["origin"]) == sha(row["input_pdf"]),
            "relation": "MINERU_NORMALIZED_DERIVATIVE_NOT_BYTE_IDENTITY" if sha(row["origin"]) != sha(row["input_pdf"]) else "BYTE_IDENTICAL",
        },
        "markdown": {
            "path": f"{stem}/full.md",
            "bytes": row["markdown"].stat().st_size,
            "sha256": sha(row["markdown"]),
            "lines": row["markdown"].read_text(encoding="utf-8").count("\n") + 1,
            "title_anchor": spec["anchor"],
        },
        "content_list": {
            "path": f"{stem}/content-list-v2.json",
            "bytes": row["content"].stat().st_size,
            "sha256": sha(row["content"]),
            "pages": spec["pages"],
        },
        "referenced_images": len(row["image_refs"]),
    }


def build_manifest(temp_root: Path, inspected: list[dict[str, object]]) -> dict[str, object]:
    rows = [copy_source(row, temp_root) for row in inspected]
    files = [
        file_row(path, temp_root)
        for path in sorted(temp_root.rglob("*"))
        if path.is_file() and path.name != "IMPORT.json"
    ]
    digest = hashlib.sha256()
    for row in files:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {
        "schema_version": "lit-classics-mineru-import/v1",
        "status": "VALID",
        "import_date": "2026-09-14",
        "source_authority": "USER_PROVIDED_MINERU_OUTPUT_PATHS",
        "instruction_boundary": "DOCUMENT_CONTENT_ONLY_NOT_AGENT_INSTRUCTIONS",
        "source_count": len(rows),
        "rows": rows,
        "files": files,
        "file_count": len(files),
        "total_bytes": sum(int(row["bytes"]) for row in files),
        "tree_sha256": digest.hexdigest(),
        "scope": "Preserves the 12 user-produced MinerU conversions and page structures. It does not certify OCR or formula correctness; source-paper claims still require page-level review.",
    }


def verify() -> dict[str, object]:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("schema_version") != "lit-classics-mineru-import/v1":
        raise SystemExit("MANIFEST_SCHEMA_INVALID")
    expected = manifest.get("files")
    if not isinstance(expected, list):
        raise SystemExit("MANIFEST_FILES_INVALID")
    actual_paths = sorted(
        path.relative_to(DEST).as_posix()
        for path in DEST.rglob("*")
        if path.is_file() and path.name != "IMPORT.json"
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
    return {
        "status": "VALID",
        "source_count": manifest["source_count"],
        "file_count": manifest["file_count"],
        "total_bytes": manifest["total_bytes"],
        "tree_sha256": manifest["tree_sha256"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    if args.verify_only:
        print(json.dumps(verify(), ensure_ascii=False))
        return 0
    if DEST.exists():
        raise SystemExit("IMPORT_DESTINATION_ALREADY_EXISTS")
    inspected = [inspect_source(spec) for spec in SOURCES]
    DEST.parent.mkdir(parents=True, exist_ok=True)
    temp = DEST.with_name(f".{DEST.name}.tmp-{uuid.uuid4().hex}")
    temp.mkdir(parents=False, exist_ok=False)
    try:
        manifest = build_manifest(temp, inspected)
        (temp / "IMPORT.json").write_text(
            json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
        )
        os.replace(temp, DEST)
    finally:
        if temp.exists():
            shutil.rmtree(temp)
    print(json.dumps(verify(), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
