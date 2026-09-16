#!/usr/bin/env python3
"""Import and verify the CC-BY Agda sources accompanying LOPS 2018."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_ROOT = Path("/Volumes/D/HoTT-literature-cache/lops-internal-universes-2018/extracted/internal-universes/code")
ARCHIVE = Path("/Volumes/D/HoTT-literature-cache/lops-internal-universes-2018/internal-universes.zip")
DEST = ROOT / "HoTT/formal/external-agda-flat-internal-universes/upstream"
MANIFEST = ROOT / "HoTT/formal/external-agda-flat-internal-universes/SOURCE_TREE_MANIFEST.json"
ARCHIVE_BYTES = 126655
ARCHIVE_SHA256 = "56b18248ae275f4efc6cfd98287ba40651a9eea8d23e1ac5f360a3d4402b963a"
EXPECTED = {
    "README.agda": (909, "fb35f1e8ced48e5f47c3434c5430c74c599f4cc0ae95dcaf13877ecf3445c8c0"),
    "agda/cchm.agda": (649, "82921ee602aa7a6e52d9f8b2f1e13906b270083d8d0993d697ede8422f62669f"),
    "agda/cctt.agda": (712, "51be3df7831ae7534ab88126703d5f64e06afdf56f9d0a8d5ea0775ee20dedcf"),
    "agda/exp-path.agda": (733, "5ba2266a41c585feaecf09379bed25d3db1fbbd59015609a91308c6b304d0d89"),
    "agda/fibration.agda": (3481, "792c584d7ab242bbee8e1ba52cc58d9247d4e255a61a637640dcf09e12b85ae7"),
    "agda/postulates.agda": (602, "b27acce56fcedf7074dc555fea7aa9abd81cc2fee906492d6eaa4ede68928255"),
    "agda/prelude.agda": (4971, "60b933a3fa86fff12b79c69bfaf234f8494b38c713727bb2b4c25573a6eb96d8"),
    "agda-flat/prelude.agda": (828, "5a5844bd607aa1a052036fe7c2b6740c7bfabe315cda12da8679f913fa46175d"),
    "agda-flat/tiny.agda": (3939, "ac33bd842981e9599319840fc70ea4fc7301bf485daca1d8499e11bba4cb295b"),
    "proposition-6-2.agda": (6956, "a8b05827de5d8c0396a324a1d17bb5679bd4812e1814e10f731efdf871e7099a"),
    "theorem-3-1.agda": (3490, "be3000f1663a6221a22c1cf26df56eb9f47a7ae431adebc79338be8f03d080d7"),
    "theorem-5-2-relative.agda": (9044, "dcab8bc6b3156a1bda649b5cfa7a26ef95d8bce5e6046158c99e16796425027b"),
    "theorem-5-2.agda": (8060, "5bb7835114581329d77b54dedd166cf7c7fab46785685b1f6b84d088af7ccdbb"),
}


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def manifest_value() -> dict[str, object]:
    rows = [
        {"path": path, "bytes": size, "sha256": digest}
        for path, (size, digest) in sorted(EXPECTED.items())
    ]
    tree_digest = hashlib.sha256()
    for row in rows:
        tree_digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))
        tree_digest.update(b"\n")
    return {
        "schema_version": "lops-internal-universes-source-tree/v1",
        "title": "Internal Universes in Models of Homotopy Type Theory",
        "authors": ["Daniel R. Licata", "Ian Orton", "Andrew M. Pitts", "Bas Spitters"],
        "paper_doi": "10.4230/LIPIcs.FSCD.2018.22",
        "dataset_doi": "10.17863/CAM.22369",
        "dataset_item_uuid": "c9612c2f-f011-417b-96a0-6223f23e34fb",
        "license": "CC BY 4.0 (repository item metadata)",
        "archive": {
            "url": "https://api.repository.cam.ac.uk/server/api/core/bitstreams/85c6f492-6de1-4ce9-9c6f-08d40b09c120/content",
            "bytes": ARCHIVE_BYTES,
            "sha256": ARCHIVE_SHA256,
        },
        "source_root": "HoTT/formal/external-agda-flat-internal-universes/upstream",
        "file_count": len(rows),
        "total_bytes": sum(row["bytes"] for row in rows),
        "tree_sha256": tree_digest.hexdigest(),
        "files": rows,
        "exclusions": ["HTML renderings", ".DS_Store", "__MACOSX", "generated .agdai interfaces"],
    }


def exclusive_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    archive_data = ARCHIVE.read_bytes()
    if len(archive_data) != ARCHIVE_BYTES or sha(archive_data) != ARCHIVE_SHA256:
        raise SystemExit("LOPS_ARCHIVE_MISMATCH")
    actual_source = {p.relative_to(SOURCE_ROOT).as_posix() for p in SOURCE_ROOT.rglob("*.agda")}
    if actual_source != set(EXPECTED):
        raise SystemExit(f"LOPS_SOURCE_DENOMINATOR_MISMATCH:{sorted(actual_source ^ set(EXPECTED))}")
    for relative, (size, digest) in EXPECTED.items():
        data = (SOURCE_ROOT / relative).read_bytes()
        if len(data) != size or sha(data) != digest:
            raise SystemExit(f"LOPS_SOURCE_MISMATCH:{relative}")
        target = DEST / relative
        if args.write and not target.exists():
            exclusive_write(target, data)
        if not target.is_file() or target.is_symlink() or target.read_bytes() != data:
            raise SystemExit(f"LOPS_IMPORTED_SOURCE_MISMATCH:{relative}")

    imported = {p.relative_to(DEST).as_posix() for p in DEST.rglob("*.agda")} if DEST.exists() else set()
    if imported != set(EXPECTED):
        raise SystemExit(f"LOPS_IMPORTED_DENOMINATOR_MISMATCH:{sorted(imported ^ set(EXPECTED))}")
    value = manifest_value()
    data = (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    if args.write and not MANIFEST.exists():
        exclusive_write(MANIFEST, data)
    if not MANIFEST.is_file() or MANIFEST.is_symlink() or MANIFEST.read_bytes() != data:
        raise SystemExit("LOPS_MANIFEST_MISMATCH")
    print(json.dumps({
        "status": "VALID", "files": value["file_count"], "bytes": value["total_bytes"],
        "tree_sha256": value["tree_sha256"], "archive_sha256": ARCHIVE_SHA256,
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
