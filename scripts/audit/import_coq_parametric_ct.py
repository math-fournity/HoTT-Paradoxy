#!/usr/bin/env python3
"""Qualify the pinned Parametric CT source and write deterministic replay manifests."""
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
CACHE = Path("/Volumes/D/HoTT-literature-cache/parametric-ct-b9523cb")
FORMAL_ROOT = ROOT / "HoTT/formal/external-coq-parametric-ct"
COMMIT = "b9523cb33180dc58b227432e60045cc38615b711"
GIT_TREE = "9cfc31a04f31e0a73cd9494a8d745a39ee639082"
ARCHIVE_BYTES = 203159
ARCHIVE_SHA256 = "c58a601b1bb8a1ff88e517b4f6a157a141565d6219761532db4d583e62ce7700"
ARCHIVE_ETAG = '"b80f69b349e0a8e618948c90a7be83564c467960bb5dc391c1cfab1a6cea7b76"'
TREE_FILE_COUNT = 109
TREE_TOTAL_BYTES = 814289
TREE_SHA256 = "093f04f2c16c465e1a42993f5acf6137f721fa39d4ed1d755564ced39cdb4670"
IMAGE_TAG = "hott-parametric-ct:coq-8.13.2-target-deps"
IMAGE_ID = "sha256:7e35dbfedcb7281c00420071437fce8316345ab006b1699cd0926f525a669df8"

# This is the complete local source closure observed while building
# Axioms/halting.vo in the pinned environment.  Optional L/MetaCoq/Smpl files
# are deliberately outside this target replay.
TARGET_SOURCE_FILES = [
    "Shared/Dec.v",
    "Synthetic/Definitions.v",
    "Shared/FilterFacts.v",
    "Shared/ListAutomation.v",
    "Shared/mu_nat.v",
    "Shared/equiv_on.v",
    "Shared/Pigeonhole.v",
    "Synthetic/FinitenessFacts.v",
    "Synthetic/DecidabilityFacts.v",
    "Shared/embed_nat.v",
    "Shared/partial.v",
    "Synthetic/EnumerabilityFacts.v",
    "Synthetic/SemiDecidabilityFacts.v",
    "Synthetic/ListEnumerabilityFacts.v",
    "Synthetic/MoreEnumerabilityFacts.v",
    "Synthetic/truthtables.v",
    "Synthetic/reductions.v",
    "Synthetic/ReducibilityFacts.v",
    "Axioms/bestaxioms.v",
    "Axioms/halting.v",
]


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
    return {
        "path": relative if relative is not None else str(path),
        "bytes": len(data),
        "sha256": sha(data),
    }


def deterministic_tree(root: Path) -> dict[str, object]:
    if not root.is_dir() or root.is_symlink():
        raise QualificationError(f"TREE_INVALID:{root}")
    rows: list[dict[str, object]] = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise QualificationError(f"TREE_SYMLINK_UNSUPPORTED:{path}")
        if path.is_file() and path.name != ".DS_Store":
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
            rows.append({
                "path": Path(*parts[1:]).as_posix(),
                "bytes": len(data),
                "sha256": sha(data),
            })
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
    if git_value("rev-parse", "FETCH_HEAD") != COMMIT:
        raise QualificationError("FETCH_HEAD_MISMATCH")
    if git_value("rev-parse", "FETCH_HEAD^{tree}") != GIT_TREE:
        raise QualificationError("GIT_TREE_ID_MISMATCH")
    git_manifest = deterministic_tree(source)
    if {
        "file_count": git_manifest["file_count"],
        "total_bytes": git_manifest["total_bytes"],
        "tree_sha256": git_manifest["tree_sha256"],
    } != {
        "file_count": TREE_FILE_COUNT,
        "total_bytes": TREE_TOTAL_BYTES,
        "tree_sha256": TREE_SHA256,
    }:
        raise QualificationError("SOURCE_TREE_IDENTITY_MISMATCH")
    if archive_tree(archive) != git_manifest:
        raise QualificationError("CODELOAD_GIT_TREE_CONTENT_MISMATCH")
    working_tree = deterministic_tree(CACHE / "source")
    if working_tree != git_manifest:
        raise QualificationError("QUALIFIED_SOURCE_COPY_MISMATCH")
    selected = [file_row(source / relative, relative) for relative in TARGET_SOURCE_FILES]
    closure = {
        "schema_version": "coq-parametric-ct-target-closure/v1",
        "target": "Axioms/halting.vo",
        "probe": "CheckInternalUndec.v",
        "source_file_count": len(selected),
        "source_files": selected,
        "external_packages": [
            "coq-equations.1.2.3+8.13",
            "coq-stdpp.1.5.0",
        ],
        "excluded_optional_branches": [
            "L/Complexity/* requiring Smpl",
            "L/Tactics/* requiring MetaCoq",
        ],
    }
    replay = {
        "schema_version": "coq-parametric-ct-replay-source/v1",
        "upstream": "https://github.com/yforster/coq-synthetic-computability",
        "branch": "code",
        "commit": COMMIT,
        "git_tree": GIT_TREE,
        "archive": {
            "url": f"https://codeload.github.com/yforster/coq-synthetic-computability/tar.gz/{COMMIT}",
            "local_path": str(archive),
            "bytes": ARCHIVE_BYTES,
            "sha256": ARCHIVE_SHA256,
            "etag": ARCHIVE_ETAG,
            "range_probe": "SERVER_RETURNED_200_FOR_BYTES_0_0_SINGLE_CONNECTION_USED",
        },
        "git_fetch": {
            "local_git_dir": str(CACHE / "objects.git"),
            "fetched_commit": COMMIT,
            "tree": GIT_TREE,
        },
        "content_comparison": "CODELOAD_ARCHIVE_CONTENT_MATCHES_GIT_ARCHIVE_OF_FETCHED_COMMIT",
        "full_tree_manifest": "HoTT/formal/external-coq-parametric-ct/SOURCE_TREE_MANIFEST.json",
        "target_closure": "HoTT/formal/external-coq-parametric-ct/TARGET_CLOSURE.json",
        "primary_theorems": [
            "EPF_SCT_halting : EPF_bool + SCT -> exists K, semi_decidable K /\\ ~ semi_decidable (compl K) /\\ ~ decidable K /\\ ~ decidable (compl K)",
            "K_nat_bool_undec : EPF_bool + SCT -> ~ decidable (compl K_nat_bool)",
            "K_nat_undec : EPF_bool + SCT -> ~ decidable (fun f => forall n, f n = 0)",
        ],
        "assumption_boundary": "EPF_bool or SCT is an explicit theorem premise; Closed under the global context reports no additional global axiom for the proved implication.",
        "license_boundary": "NO_LICENSE_FILE_PRESENT_IN_PINNED_TREE; retained for local research replay; no redistribution permission is inferred.",
        "docker": {
            "image_tag": IMAGE_TAG,
            "image_id": IMAGE_ID,
            "platform": "linux/amd64",
            "coq_version": "8.13.2",
            "ocaml_version": "4.07.1",
            "equations_version": "1.2.3+8.13",
            "stdpp_version": "1.5.0",
        },
    }
    return replay, git_manifest, closure


def expected_documents() -> dict[Path, bytes]:
    replay, manifest, closure = qualified_payloads()
    return {
        FORMAL_ROOT / "REPLAY_SOURCE.json": json_bytes(replay),
        FORMAL_ROOT / "SOURCE_TREE_MANIFEST.json": json_bytes(manifest),
        FORMAL_ROOT / "TARGET_CLOSURE.json": json_bytes(closure),
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
        replay, manifest, closure = qualified_payloads()
        print(json.dumps({
            "status": "VALID",
            "mode": "write" if args.write else "verify",
            "commit": replay["commit"],
            "git_tree": replay["git_tree"],
            "file_count": manifest["file_count"],
            "total_bytes": manifest["total_bytes"],
            "tree_sha256": manifest["tree_sha256"],
            "target_source_files": closure["source_file_count"],
            "license_boundary": replay["license_boundary"],
        }, ensure_ascii=False))
        return 0
    except (QualificationError, OSError, UnicodeError, ValueError, tarfile.TarError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
