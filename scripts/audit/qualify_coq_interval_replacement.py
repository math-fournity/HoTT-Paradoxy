#!/usr/bin/env python3
"""Qualify the non-vendored Boulier--Tabareau InternalCubical-Coq subtree."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import tarfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = Path("/Volumes/D/HoTT-literature-cache/boulier-tabareau-internalcubical-28a2568.tar.gz")
MANIFEST = ROOT / "HoTT/formal/external-coq-interval-replacement/SOURCE_TREE_MANIFEST.json"
ARCHIVE_BYTES = 41455
ARCHIVE_SHA256 = "1f78d84fd3d8f01bbf89eab85ac632f38e59eb7ff4e0445e7bf94a76f652c955"
COMMIT = "28a256848a134d9111a2f332083b3d3ff35a58d3"
REPO_TREE = "dc98a8fb06f54f473318353750bdccd708d1e48b"
SUBTREE = "51ec7ae99395e8db73d2b48c6c4658df32dfd36e"
EXPECTED_FILES = 20
EXPECTED_BYTES = 177150
EXPECTED_TREE_SHA256 = "43557c5cd096c58dd606253956f8734cccc7e6fe2ca84438359ee294702ef188"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rows_from_archive() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with tarfile.open(ARCHIVE, "r:gz") as archive:
        members = [m for m in archive.getmembers() if m.isfile()]
        for member in sorted(members, key=lambda m: m.name):
            prefix = "InternalCubical-Coq/"
            if not member.name.startswith(prefix):
                raise SystemExit(f"COQ_INTERVAL_ARCHIVE_PATH_INVALID:{member.name}")
            relative = member.name[len(prefix):]
            if not relative or ".." in Path(relative).parts:
                raise SystemExit(f"COQ_INTERVAL_ARCHIVE_PATH_INVALID:{member.name}")
            handle = archive.extractfile(member)
            if handle is None:
                raise SystemExit(f"COQ_INTERVAL_ARCHIVE_MEMBER_UNREADABLE:{member.name}")
            data = handle.read()
            rows.append({"path": relative, "bytes": len(data), "sha256": sha(data)})
    return rows


def manifest_value() -> dict[str, object]:
    rows = rows_from_archive()
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))
        digest.update(b"\n")
    if len(rows) != EXPECTED_FILES or sum(int(r["bytes"]) for r in rows) != EXPECTED_BYTES or digest.hexdigest() != EXPECTED_TREE_SHA256:
        raise SystemExit("COQ_INTERVAL_SOURCE_TREE_MISMATCH")
    return {
        "schema_version": "coq-interval-replacement-source-tree/v1",
        "repository": "https://gitlab.inria.fr/sboulier/thesis-formalizations.git",
        "branch": "emptyctx",
        "commit": COMMIT,
        "repository_git_tree": REPO_TREE,
        "subtree": "InternalCubical-Coq",
        "subtree_git_tree": SUBTREE,
        "archive": {"path": str(ARCHIVE), "bytes": ARCHIVE_BYTES, "sha256": ARCHIVE_SHA256},
        "file_count": len(rows),
        "total_bytes": sum(int(r["bytes"]) for r in rows),
        "tree_sha256": digest.hexdigest(),
        "license_boundary": "No license file was found in the InternalCubical-Coq subtree; source is not vendored in this project.",
        "files": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    data = ARCHIVE.read_bytes()
    if len(data) != ARCHIVE_BYTES or sha(data) != ARCHIVE_SHA256:
        raise SystemExit("COQ_INTERVAL_ARCHIVE_MISMATCH")
    value = manifest_value()
    encoded = (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    if args.write and not MANIFEST.exists():
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        with MANIFEST.open("xb") as handle:
            handle.write(encoded); handle.flush(); os.fsync(handle.fileno())
    if not MANIFEST.is_file() or MANIFEST.is_symlink() or MANIFEST.read_bytes() != encoded:
        raise SystemExit("COQ_INTERVAL_MANIFEST_MISMATCH")
    print(json.dumps({
        "status": "VALID", "commit": COMMIT, "subtree": SUBTREE,
        "files": value["file_count"], "bytes": value["total_bytes"], "tree_sha256": value["tree_sha256"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
