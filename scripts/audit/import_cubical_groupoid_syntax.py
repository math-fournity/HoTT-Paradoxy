#!/usr/bin/env python3
"""Qualify and freeze the CSL 2026 Cubical Agda groupoid-syntax source."""
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
CACHE = Path("/Volumes/D/HoTT-literature-cache/groupoid-syntax-cohtt-5babc385")
FORMAL_ROOT = ROOT / "HoTT/formal/external-cubical-groupoid-syntax"
COMMIT = "5babc385d01500c1777ff932dd8c79299a1d766a"
GIT_TREE = "13849af00ff393300c0ae6cdd47ba6ddfa0d1cd8"
ARCHIVE_BYTES = 777803
ARCHIVE_SHA256 = "f83f4b0fcbfc3748b51ffb0a48272551f8d15d282d5174b30fc13ea789c20efd"
FULL_FILE_COUNT = 91
FULL_TOTAL_BYTES = 1706237
FULL_TREE_SHA256 = "fa825bb99108697838933ac56977cfb43efaa6e0a072744c5751300e893b577e"
VERIFIER_FILE_COUNT = 90
VERIFIER_TOTAL_BYTES = 1700089
VERIFIER_TREE_SHA256 = "704d67511b165eedf3e5e2a6d904643878fb41ece882785bd0ebfcb6f97b9afa"


class QualificationError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def file_row(path: Path, relative: str | None = None) -> dict[str, object]:
    if not path.is_file() or path.is_symlink():
        raise QualificationError(f"FILE_INVALID:{path}")
    data = path.read_bytes()
    return {"path": relative if relative is not None else str(path), "bytes": len(data), "sha256": sha(data)}


def deterministic_tree(root: Path, exclude_ds_store: bool = False) -> dict[str, object]:
    if not root.is_dir() or root.is_symlink():
        raise QualificationError(f"TREE_INVALID:{root}")
    rows: list[dict[str, object]] = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise QualificationError(f"TREE_SYMLINK_UNSUPPORTED:{path}")
        if path.is_file() and not (exclude_ds_store and path.name == ".DS_Store"):
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


def archive_tree(archive: Path) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    with tarfile.open(archive, "r:gz") as bundle:
        for member in sorted(bundle.getmembers(), key=lambda item: item.name):
            if not member.isfile():
                continue
            parts = Path(member.name).parts
            if len(parts) < 2:
                raise QualificationError(f"ARCHIVE_MEMBER_PATH_INVALID:{member.name}")
            handle = bundle.extractfile(member)
            if handle is None:
                raise QualificationError(f"ARCHIVE_MEMBER_UNREADABLE:{member.name}")
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
        raise QualificationError(f"GIT_FAILED:{' '.join(args)}:{result.stderr.strip()}")
    return result.stdout.strip()


def qualified_payloads() -> tuple[dict[str, object], dict[str, object], dict[str, object]]:
    archive = CACHE / "source.tar.gz"
    source = CACHE / "git-export"
    archive_row = file_row(archive)
    if archive_row["bytes"] != ARCHIVE_BYTES or archive_row["sha256"] != ARCHIVE_SHA256:
        raise QualificationError("ARCHIVE_IDENTITY_MISMATCH")
    if git_value("rev-parse", "HEAD") != COMMIT or git_value("rev-parse", "HEAD^{tree}") != GIT_TREE:
        raise QualificationError("GIT_IDENTITY_MISMATCH")
    full = deterministic_tree(source)
    if {
        "file_count": full["file_count"],
        "total_bytes": full["total_bytes"],
        "tree_sha256": full["tree_sha256"],
    } != {
        "file_count": FULL_FILE_COUNT,
        "total_bytes": FULL_TOTAL_BYTES,
        "tree_sha256": FULL_TREE_SHA256,
    }:
        raise QualificationError("FULL_TREE_IDENTITY_MISMATCH")
    if archive_tree(archive) != full or deterministic_tree(CACHE / "source") != full:
        raise QualificationError("ARCHIVE_GIT_EXTRACTED_TREE_MISMATCH")
    verifier_tree = deterministic_tree(source, exclude_ds_store=True)
    if {
        "file_count": verifier_tree["file_count"],
        "total_bytes": verifier_tree["total_bytes"],
        "tree_sha256": verifier_tree["tree_sha256"],
    } != {
        "file_count": VERIFIER_FILE_COUNT,
        "total_bytes": VERIFIER_TOTAL_BYTES,
        "tree_sha256": VERIFIER_TREE_SHA256,
    }:
        raise QualificationError("VERIFIER_TREE_IDENTITY_MISMATCH")
    target_paths = [
        "readme.md",
        "cohtt.agda-lib",
        *sorted(path.relative_to(source).as_posix() for path in (source / "TT").rglob("*.agda")),
    ]
    target_rows = [file_row(source / relative, relative) for relative in target_paths]
    raw_lib = (source / "cohtt.agda-lib").read_text(encoding="utf-8")
    if raw_lib.startswith("name:") or "name:" in raw_lib.splitlines():
        raise QualificationError("UNEXPECTED_UPSTREAM_LIBRARY_NAME_PRESENT")
    target = {
        "schema_version": "cubical-groupoid-syntax-target/v1",
        "entrypoint": "TT/README.agda",
        "source_file_count": len(target_rows),
        "source_files": target_rows,
        "declared_toolchain": "Agda 2.8.0 and Cubical library v0.9",
        "declared_flags": [
            "--safe", "--cubical", "--guardedness", "--no-import-sorts",
            "--hidden-argument-puns", "-WnoUnsupportedIndexedMatch",
        ],
        "replay_wrapper": "The pinned cohtt.agda-lib has no name field. Replay adds only 'name: cohtt-replay' in a derived scratch manifest so Agda can select the library; all upstream flags and include/depend fields are preserved.",
        "two_phase_replay": "First compile from source with safe/cubical/guardedness and fresh interfaces; then delete only cohtt interfaces and recheck all 20 TT modules with the upstream library flags while using the freshly compiled pinned Cubical v0.9 interfaces.",
    }
    replay = {
        "schema_version": "cubical-groupoid-syntax-replay-source/v1",
        "paper": "The Groupoid-Syntax of Type Theory Is a Set",
        "paper_doi": "10.4230/LIPIcs.CSL.2026.40",
        "upstream": "https://bitbucket.org/akaposi/cohtt",
        "branch": "master",
        "commit": COMMIT,
        "git_tree": GIT_TREE,
        "archive": {
            "url": f"https://bitbucket.org/akaposi/cohtt/get/{COMMIT}.tar.gz",
            "local_path": str(archive),
            "bytes": ARCHIVE_BYTES,
            "sha256": ARCHIVE_SHA256,
            "range_probe": "SERVER_RETURNED_200_FOR_RANGE_REQUEST_SINGLE_CONNECTION_USED",
        },
        "full_tree": {key: full[key] for key in ("file_count", "total_bytes", "tree_sha256")},
        "verifier_tree_excluding_ds_store": {
            key: verifier_tree[key] for key in ("file_count", "total_bytes", "tree_sha256")
        },
        "content_comparison": "BITBUCKET_ARCHIVE_CONTENT_MATCHES_INDEPENDENT_GIT_EXPORT",
        "full_tree_manifest": "HoTT/formal/external-cubical-groupoid-syntax/SOURCE_TREE_MANIFEST.json",
        "target_manifest": "HoTT/formal/external-cubical-groupoid-syntax/TARGET_SOURCE_MANIFEST.json",
        "toolchain": "HoTT/formal/partiality-race-timeout/TOOLCHAIN.json",
        "license_boundary": "Repository contains CC-BY paper assets but no root/source-code license file; local source replay does not infer code redistribution permission.",
    }
    return replay, full, target


def expected_documents() -> dict[Path, bytes]:
    replay, manifest, target = qualified_payloads()
    return {
        FORMAL_ROOT / "REPLAY_SOURCE.json": json_bytes(replay),
        FORMAL_ROOT / "SOURCE_TREE_MANIFEST.json": json_bytes(manifest),
        FORMAL_ROOT / "TARGET_SOURCE_MANIFEST.json": json_bytes(target),
    }


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.is_symlink() or not path.is_file() or path.read_bytes() != data:
            raise QualificationError(f"EXISTING_OUTPUT_DIFFERS:{path}")
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
        documents = expected_documents()
        if args.write:
            for path, data in documents.items():
                atomic_write(path, data)
        for path, data in documents.items():
            if not path.is_file() or path.is_symlink() or path.read_bytes() != data:
                raise QualificationError(f"PROJECT_DOCUMENT_MISMATCH:{path}")
        replay, manifest, target = qualified_payloads()
        print(json.dumps({
            "status": "VALID",
            "mode": "write" if args.write else "verify",
            "commit": replay["commit"],
            "git_tree": replay["git_tree"],
            "full_files": manifest["file_count"],
            "full_bytes": manifest["total_bytes"],
            "full_tree_sha256": manifest["tree_sha256"],
            "target_source_files": target["source_file_count"],
            "license_boundary": replay["license_boundary"],
        }, ensure_ascii=False))
        return 0
    except (QualificationError, OSError, UnicodeError, ValueError, tarfile.TarError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
