#!/usr/bin/env python3
"""Freeze and verify the Coq Undecidability MM2 source snapshots used by R2."""
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
REPLAY_CACHE = Path("/Volumes/D/HoTT-toolchain-cache/coq-undecidability-c486697da8cfa4b9")
CURRENT_CACHE = Path("/Volumes/D/HoTT-toolchain-cache/coq-undecidability-c7257b736763d7b2")
FORMAL_ROOT = ROOT / "HoTT/formal/external-coq-mm2"
QUAL_ROOT = ROOT / "audit/literature/LIT-MECH-META-001/coq-library-undecidability"

SELECTED_COMMON = [
    "README.md",
    "opam",
    "theories/Synthetic/Definitions.v",
    "theories/Synthetic/Undecidability.v",
    "theories/Synthetic/ReducibilityFacts.v",
    "theories/TM/SBTM.v",
    "theories/MinskyMachines/MM2.v",
    "theories/MinskyMachines/MM2_undec.v",
    "theories/MinskyMachines/MMA2_undec.v",
    "theories/MinskyMachines/Reductions/MMA2_to_MM2.v",
    "theories/FRACTRAN/FRACTRAN_undec.v",
]


def selected_for(name: str) -> list[str]:
    license_path = "CeCILL_LICENSE.txt" if name == "replay" else "LICENSE"
    return [license_path, *SELECTED_COMMON]

VERSIONS = {
    "replay": {
        "branch": "coq-8.15",
        "commit": "c486697da8cfa4b9bb11b4c53eea7d57781c0deb",
        "git_tree": "6469b73eb0e8cd73d8ecd0cac5711a07912c54d2",
        "cache": REPLAY_CACHE,
        "archive_bytes": 1386841,
        "archive_sha256": "e88230dec71d1dfeb268aa7959268a5d6d8d9f4a356d594db7366e7cb76519a4",
        "etag": '"5a1f91fbecab96a20c082ac5a5d0df512ab15a9532ceafecab66b7cfb3c05ba7"',
        "destination": FORMAL_ROOT / "upstream-coq-8.15-c486697",
    },
    "current": {
        "branch": "rocq-9.2",
        "commit": "c7257b736763d7b2bc3bd25ac47d5fb7ce749c9c",
        "git_tree": "ae3d19c1245b74119327997898905d6364143511",
        "cache": CURRENT_CACHE,
        "archive_bytes": 1288501,
        "archive_sha256": "6bac7312d0de2e2246a18735262186a361134915b3abfd6e3243fb07eb009af3",
        "etag": '"eb36bf676362960051ff042aee2c07339ddd3ae3174f3728aabc22e9042e49e1"',
        "destination": QUAL_ROOT / "current-rocq-9.2-c7257b7",
    },
}


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
    return {
        "path": relative if relative is not None else str(path),
        "bytes": len(data),
        "sha256": sha(data),
    }


def tree_manifest(root: Path) -> dict[str, object]:
    if not root.is_dir() or root.is_symlink():
        raise ImportError(f"TREE_INVALID:{root}")
    rows: list[dict[str, object]] = []
    total = 0
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ImportError(f"TREE_SYMLINK_UNSUPPORTED:{path}")
        if path.is_file() and path.name != ".DS_Store":
            row = file_row(path, path.relative_to(root).as_posix())
            rows.append(row)
            total += int(row["bytes"])
    rows.sort(key=lambda row: str(row["path"]))
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {
        "schema_version": "external-source-tree-manifest/v1",
        "file_count": len(rows),
        "total_bytes": total,
        "tree_sha256": digest.hexdigest(),
        "files": rows,
    }


def archive_tree_manifest(archive: Path) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    total = 0
    with tarfile.open(archive, "r:gz") as bundle:
        for member in sorted(bundle.getmembers(), key=lambda item: item.name):
            if not member.isfile():
                continue
            parts = Path(member.name).parts
            if len(parts) < 2:
                raise ImportError(f"ARCHIVE_MEMBER_PATH_INVALID:{member.name}")
            relative = Path(*parts[1:]).as_posix()
            extracted = bundle.extractfile(member)
            if extracted is None:
                raise ImportError(f"ARCHIVE_MEMBER_UNREADABLE:{member.name}")
            data = extracted.read()
            row = {"path": relative, "bytes": len(data), "sha256": sha(data)}
            rows.append(row)
            total += len(data)
    rows.sort(key=lambda row: str(row["path"]))
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {
        "schema_version": "external-source-tree-manifest/v1",
        "file_count": len(rows),
        "total_bytes": total,
        "tree_sha256": digest.hexdigest(),
        "files": rows,
    }


def git_value(git_dir: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", f"--git-dir={git_dir}", *args],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise ImportError(f"GIT_FAILED:{' '.join(args)}:{result.stderr.strip()}")
    return result.stdout.strip()


def qualify_version(name: str, spec: dict[str, object]) -> tuple[dict[str, object], dict[str, object]]:
    cache = Path(spec["cache"])
    archive = cache / "source.tar.gz"
    git_tree = cache / "git-export"
    git_dir = cache / "objects.git"
    archive_row = file_row(archive)
    if archive_row["bytes"] != spec["archive_bytes"] or archive_row["sha256"] != spec["archive_sha256"]:
        raise ImportError(f"ARCHIVE_IDENTITY_MISMATCH:{name}")
    commit = str(spec["commit"])
    if git_value(git_dir, "rev-parse", "FETCH_HEAD") != commit:
        raise ImportError(f"FETCH_HEAD_MISMATCH:{name}")
    if git_value(git_dir, "rev-parse", "FETCH_HEAD^{tree}") != spec["git_tree"]:
        raise ImportError(f"GIT_TREE_ID_MISMATCH:{name}")
    codeload_manifest = archive_tree_manifest(archive)
    git_manifest = tree_manifest(git_tree)
    if codeload_manifest != git_manifest:
        raise ImportError(f"CODELOAD_GIT_TREE_CONTENT_MISMATCH:{name}")
    selected_rows = []
    for relative in selected_for(name):
        source = git_tree / relative
        if not source.is_file() or source.is_symlink():
            raise ImportError(f"SELECTED_SOURCE_MISSING:{name}:{relative}")
        selected_rows.append(file_row(source, relative))
    summary = {
        "role": name,
        "upstream": "https://github.com/uds-psl/coq-library-undecidability",
        "branch": spec["branch"],
        "commit": commit,
        "git_tree": spec["git_tree"],
        "archive": {
            "url": f"https://codeload.github.com/uds-psl/coq-library-undecidability/tar.gz/{commit}",
            "local_path": str(archive),
            "bytes": archive_row["bytes"],
            "sha256": archive_row["sha256"],
            "etag": spec["etag"],
            "range_probe": "SERVER_RETURNED_200_FOR_BYTES_0_0_SINGLE_CONNECTION_USED",
        },
        "git_fetch": {
            "local_git_dir": str(git_dir),
            "fetched_commit": commit,
            "tree": spec["git_tree"],
        },
        "content_comparison": "CODELOAD_ARCHIVE_CONTENT_MATCHES_GIT_ARCHIVE_OF_FETCHED_COMMIT",
        "tree": {key: git_manifest[key] for key in ("file_count", "total_bytes", "tree_sha256")},
        "selected_files": selected_rows,
    }
    return summary, git_manifest


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


def selected_documents(
    name: str, source_root: Path, destination: Path
) -> tuple[dict[Path, bytes], list[dict[str, object]]]:
    documents: dict[Path, bytes] = {}
    rows: list[dict[str, object]] = []
    for relative in selected_for(name):
        source = source_root / relative
        target = destination / relative
        data = source.read_bytes()
        documents[target] = data
        rows.append({
            "path": target.relative_to(ROOT).as_posix(),
            "bytes": len(data),
            "sha256": sha(data),
        })
    return documents, rows


def expected_documents() -> tuple[dict[Path, bytes], dict[str, object]]:
    replay, replay_manifest = qualify_version("replay", VERSIONS["replay"])
    current, current_manifest = qualify_version("current", VERSIONS["current"])
    replay_selected_docs, replay_selected = selected_documents(
        "replay",
        Path(VERSIONS["replay"]["cache"]) / "git-export",
        Path(VERSIONS["replay"]["destination"]),
    )
    current_selected_docs, current_selected = selected_documents(
        "current",
        Path(VERSIONS["current"]["cache"]) / "git-export",
        Path(VERSIONS["current"]["destination"]),
    )
    replay_source = {
        "schema_version": "coq-mm2-replay-source/v1",
        "upstream_identity": replay,
        "docker": {
            "image_tag": "hott-coq-synthetic-incompleteness:cd7d849",
            "image_id": "sha256:d4a84f07bbfe0bf3f2dce5b07e7fb43423ff64f990678a114ec6b080d131010b",
            "platform": "linux/amd64",
            "coq_version": "8.15.2",
            "ocaml_version": "4.07.1",
        },
        "primary_theorem": "MM2_HALTING_undec : undecidable MM2_HALTING",
        "definition_boundary": "undecidable P := decidable P -> enumerable (complement SBTM_HALT)",
        "selected_project_files": replay_selected,
        "full_tree_manifest": "HoTT/formal/external-coq-mm2/SOURCE_TREE_MANIFEST.json",
    }
    qualification = {
        "schema_version": "coq-undecidability-mm2-qualification/v1",
        "generated_for": "R2-UNIVERSALITY-001",
        "replay": replay,
        "current": current,
        "current_selected_project_files": current_selected,
        "comparison": {
            "mm2_instruction_and_step_core": "MANUAL_SEMANTIC_REVIEW_REQUIRED",
            "synthetic_undecidable_definition": "MANUAL_SEMANTIC_REVIEW_REQUIRED",
            "replay_theorem_to_current_theorem": "MANUAL_SEMANTIC_REVIEW_REQUIRED",
            "byte_identity_not_claimed": True,
        },
        "scope": "Source qualification and exact byte identity only; it does not prove semantic equivalence or the Agda compiler bridge.",
    }
    documents = {
        **replay_selected_docs,
        **current_selected_docs,
        FORMAL_ROOT / "REPLAY_SOURCE.json": json_bytes(replay_source),
        FORMAL_ROOT / "SOURCE_TREE_MANIFEST.json": json_bytes(replay_manifest),
        QUAL_ROOT / "QUALIFICATION.json": json_bytes(qualification),
        QUAL_ROOT / "CURRENT_TREE_MANIFEST.json": json_bytes(current_manifest),
    }
    meta = {
        "replay_files": replay_manifest["file_count"],
        "replay_bytes": replay_manifest["total_bytes"],
        "replay_tree_sha256": replay_manifest["tree_sha256"],
        "current_files": current_manifest["file_count"],
        "current_bytes": current_manifest["total_bytes"],
        "current_tree_sha256": current_manifest["tree_sha256"],
        "selected_per_version": len(SELECTED_COMMON) + 1,
    }
    return documents, meta


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        documents, meta = expected_documents()
        if args.write:
            for path, data in documents.items():
                atomic_write(path, data)
        else:
            for path, data in documents.items():
                if not path.is_file() or path.is_symlink() or path.read_bytes() != data:
                    raise ImportError(f"PROJECT_OUTPUT_MISMATCH:{path}")
        print(json.dumps({"status": "VALID", "writes": args.write, **meta}, ensure_ascii=False))
        return 0
    except (ImportError, OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "INVALID", "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
