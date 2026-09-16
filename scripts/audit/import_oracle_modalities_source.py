#!/usr/bin/env python3
"""Import the pinned MIT-licensed Oracle Modalities source into the project."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import tarfile
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CACHE = Path("/Volumes/D/HoTT-literature-cache/oracle-modality-e6e3f75")
DEST = ROOT / "audit/literature/LIT-HOTT-COMPUTABILITY-001/oracle-modalities/source-e6e3f75"
META = ROOT / "audit/literature/LIT-HOTT-COMPUTABILITY-001/oracle-modalities"
COMMIT = "e6e3f75e26da528731a5783c41f0b002336e9919"
GIT_TREE = "c68b0e0eb3fa7a1a936741eb0665f9e84eafacc4"
ARCHIVE_BYTES = 36674
ARCHIVE_SHA256 = "c1db2dfb60aaf9eecbd7f75e87242ca29d213e994ba43744702affabc23c12c5"
ARCHIVE_ETAG = '"fa78623aa9e583b094fba8a80765ea14722c5d01420ee6dea69784a3a7c9ae76"'
TREE_FILE_COUNT = 34
TREE_TOTAL_BYTES = 142253
TREE_SHA256 = "06bbc48b39a55594eaab6184face767e4856fcf572fd08416f50060c30d19ac7"


class ImportError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def file_row(path: Path, relative: str | None = None) -> dict[str, object]:
    if not path.is_file() or path.is_symlink():
        raise ImportError(f"FILE_INVALID:{path}")
    data = path.read_bytes()
    return {"path": relative if relative is not None else str(path), "bytes": len(data), "sha256": sha(data)}


def tree_manifest(root: Path) -> dict[str, object]:
    if not root.is_dir() or root.is_symlink():
        raise ImportError(f"TREE_INVALID:{root}")
    rows: list[dict[str, object]] = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ImportError(f"TREE_SYMLINK_UNSUPPORTED:{path}")
        if path.is_file() and path.name != ".DS_Store" and path.suffix != ".agdai":
            rows.append(file_row(path, path.relative_to(root).as_posix()))
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {
        "schema_version": "external-source-tree-manifest/v1",
        "file_count": len(rows),
        "total_bytes": sum(int(row["bytes"]) for row in rows),
        "tree_sha256": digest.hexdigest(),
        "files": rows,
    }


def archive_manifest(path: Path) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    with tarfile.open(path, "r:gz") as bundle:
        for member in sorted(bundle.getmembers(), key=lambda item: item.name):
            if not member.isfile():
                continue
            parts = Path(member.name).parts
            if len(parts) < 2:
                raise ImportError(f"ARCHIVE_MEMBER_PATH_INVALID:{member.name}")
            handle = bundle.extractfile(member)
            if handle is None:
                raise ImportError(f"ARCHIVE_MEMBER_UNREADABLE:{member.name}")
            data = handle.read()
            rows.append({"path": Path(*parts[1:]).as_posix(), "bytes": len(data), "sha256": sha(data)})
    rows.sort(key=lambda row: Path(str(row["path"])))
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {
        "schema_version": "external-source-tree-manifest/v1",
        "file_count": len(rows),
        "total_bytes": sum(int(row["bytes"]) for row in rows),
        "tree_sha256": digest.hexdigest(),
        "files": rows,
    }


def git_value(*args: str) -> str:
    result = subprocess.run(
        ["git", f"--git-dir={CACHE / 'objects.git'}", *args],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise ImportError(f"GIT_FAILED:{' '.join(args)}:{result.stderr.strip()}")
    return result.stdout.strip()


def expected_documents() -> tuple[dict[Path, bytes], dict[str, object]]:
    archive = CACHE / "source.tar.gz"
    source = CACHE / "git-export"
    archive_row = file_row(archive)
    if archive_row["bytes"] != ARCHIVE_BYTES or archive_row["sha256"] != ARCHIVE_SHA256:
        raise ImportError("ARCHIVE_IDENTITY_MISMATCH")
    if git_value("rev-parse", "FETCH_HEAD") != COMMIT or git_value("rev-parse", "FETCH_HEAD^{tree}") != GIT_TREE:
        raise ImportError("GIT_IDENTITY_MISMATCH")
    manifest = tree_manifest(source)
    if {
        "file_count": manifest["file_count"],
        "total_bytes": manifest["total_bytes"],
        "tree_sha256": manifest["tree_sha256"],
    } != {
        "file_count": TREE_FILE_COUNT,
        "total_bytes": TREE_TOTAL_BYTES,
        "tree_sha256": TREE_SHA256,
    }:
        raise ImportError("TREE_IDENTITY_MISMATCH")
    if archive_manifest(archive) != manifest or tree_manifest(CACHE / "source") != manifest:
        raise ImportError("ARCHIVE_GIT_EXTRACTED_TREE_MISMATCH")
    license_text = (source / "LICENSE").read_text(encoding="utf-8")
    if "Permission is hereby granted, free of charge" not in license_text:
        raise ImportError("EXPECTED_MIT_LICENSE_TEXT_MISSING")
    documents: dict[Path, bytes] = {}
    imported_rows: list[dict[str, object]] = []
    for row in manifest["files"]:
        relative = Path(str(row["path"]))
        data = (source / relative).read_bytes()
        target = DEST / relative
        documents[target] = data
        imported_rows.append({
            "path": target.relative_to(ROOT).as_posix(),
            "bytes": len(data),
            "sha256": sha(data),
        })
    source_manifest = {
        **manifest,
        "upstream_commit": COMMIT,
        "upstream_git_tree": GIT_TREE,
        "license": "MIT; source-e6e3f75/LICENSE copied verbatim",
    }
    import_receipt = {
        "schema_version": "oracle-modalities-source-import/v1",
        "upstream": "https://github.com/awswan/oraclemodality",
        "branch": "main",
        "commit": COMMIT,
        "git_tree": GIT_TREE,
        "archive": {
            "url": f"https://codeload.github.com/awswan/oraclemodality/tar.gz/{COMMIT}",
            "local_path": str(archive),
            "bytes": ARCHIVE_BYTES,
            "sha256": ARCHIVE_SHA256,
            "etag": ARCHIVE_ETAG,
            "range_probe": "SERVER_RETURNED_200_FOR_RANGE_REQUEST_SINGLE_CONNECTION_USED",
        },
        "content_comparison": "CODELOAD_ARCHIVE_CONTENT_MATCHES_INDEPENDENT_GIT_EXPORT",
        "tree": {key: manifest[key] for key in ("file_count", "total_bytes", "tree_sha256")},
        "imported_files": imported_rows,
        "declared_toolchain": "Agda 2.6.4.3 plus Cubical library v0.7",
        "replay_status": "NOT_REPLAYED_IN_CURRENT_PROJECT_TOOLCHAIN",
        "axiom_boundaries": {
            "negative_resizing": "Axioms/NegativeResizing.agda:24-31 postulates Ω¬¬ and its classifier/retraction operations",
            "markov_induction": "Axioms/MarkovInduction.agda:39-43 postulates markov-ind",
            "machine_and_choice": "Axioms/ComputableChoice.agda:38-40 postulates φ₀/haltsOnce and :67-72 postulates ComputableChoice",
            "derived": "ECT and CT are derived only after those explicit postulates",
        },
        "scope": "Full MIT-licensed source copy for source inspection and future version-matched replay; file presence and hashes do not prove the postulated axioms or paper theorems in ambient HoTT.",
    }
    documents[META / "SOURCE_TREE_MANIFEST.json"] = json_bytes(source_manifest)
    documents[META / "IMPORT.json"] = json_bytes(import_receipt)
    return documents, import_receipt


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.is_symlink() or not path.is_file() or path.read_bytes() != data:
            raise ImportError(f"EXISTING_OUTPUT_DIFFERS:{path}")
        return
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    finally:
        temp = Path(temp_name)
        if temp.exists():
            temp.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        documents, receipt = expected_documents()
        if args.write:
            for path, data in documents.items():
                atomic_write(path, data)
        for path, data in documents.items():
            if not path.is_file() or path.is_symlink() or path.read_bytes() != data:
                raise ImportError(f"PROJECT_DOCUMENT_MISMATCH:{path}")
        print(json.dumps({
            "status": "VALID",
            "mode": "write" if args.write else "verify",
            "commit": receipt["commit"],
            "git_tree": receipt["git_tree"],
            "file_count": receipt["tree"]["file_count"],
            "total_bytes": receipt["tree"]["total_bytes"],
            "tree_sha256": receipt["tree"]["tree_sha256"],
            "replay_status": receipt["replay_status"],
        }, ensure_ascii=False))
        return 0
    except (ImportError, OSError, UnicodeError, ValueError, tarfile.TarError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
