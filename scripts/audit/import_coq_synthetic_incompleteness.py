#!/usr/bin/env python3
"""Freeze the exact CSL 2023 Coq source and replay inputs into main."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
import os
import subprocess
import tarfile
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
SOURCE = Path("/Volumes/D/HoTT-machine-overview-cache/community-frameworks/coq-synthetic-incompleteness")
PACKAGE = ROOT / "HoTT/formal/external-coq-synthetic-incompleteness"
IMPORTED = ROOT / "audit/imports/machine-overview-ce-map-20260915/source/evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001"
QUALIFICATION_SOURCE = Path("/Volumes/D/HoTT-machine-overview-cache/community-frameworks/coq-synthetic-incompleteness-qualification-cd7d849/QUALIFICATION.v")
DOCKERFILE_SOURCE = Path("/Volumes/D/HoTT-machine-overview-cache/community-frameworks/coq-synthetic-incompleteness-docker/Dockerfile")
COMMIT = "cd7d8490f8542bfe85658c465bcb26b2ed163f53"
BRANCH = "csl"
ARCHIVE_NAME = "upstream-cd7d849.tar.gz"
SCHEMA = "coq-synthetic-incompleteness-main-import/v1"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def manifest_hash(rows: list[dict[str, Any]]) -> str:
    payload = b"".join(
        (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode()
        for row in rows
    )
    return digest(payload)


def tracked_rows(source: Path) -> list[dict[str, Any]]:
    names = [
        value.decode()
        for value in subprocess.check_output(["git", "-C", str(source), "ls-files", "-z"]).split(b"\0")
        if value
    ]
    rows = []
    for name in sorted(names):
        data = (source / name).read_bytes()
        rows.append({"path": name, "bytes": len(data), "sha256": digest(data)})
    return rows


def qualify_source(source: Path) -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    if subprocess.check_output(["git", "-C", str(source), "rev-parse", "HEAD"], text=True).strip() != COMMIT:
        raise ValueError("SOURCE_COMMIT_MISMATCH")
    if subprocess.check_output(["git", "-C", str(source), "branch", "--show-current"], text=True).strip() != BRANCH:
        raise ValueError("SOURCE_BRANCH_MISMATCH")
    if subprocess.check_output(["git", "-C", str(source), "status", "--short"], text=True).strip():
        raise ValueError("SOURCE_DIRTY")
    rows = tracked_rows(source)
    imported_manifest = json.loads((IMPORTED / "SOURCE-MANIFEST.json").read_text(encoding="utf-8"))
    if imported_manifest.get("commit") != COMMIT or imported_manifest.get("files") != rows:
        raise ValueError("IMPORTED_SOURCE_MANIFEST_MISMATCH")
    build = json.loads((IMPORTED / "BUILD-RECEIPT.json").read_text(encoding="utf-8"))
    if build.get("source", {}).get("tracked_tree_sha256") != manifest_hash(rows):
        raise ValueError("BUILD_RECEIPT_SOURCE_TREE_MISMATCH")
    return rows, imported_manifest, build


def deterministic_archive(source: Path) -> tuple[bytes, bytes]:
    tar_bytes = subprocess.check_output(["git", "-C", str(source), "archive", "--format=tar", COMMIT])
    buffer = io.BytesIO()
    with gzip.GzipFile(filename="", fileobj=buffer, mode="wb", compresslevel=9, mtime=0) as handle:
        handle.write(tar_bytes)
    return tar_bytes, buffer.getvalue()


def archive_rows(data: bytes) -> list[dict[str, Any]]:
    rows = []
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
        for member in sorted(archive.getmembers(), key=lambda value: value.name):
            path = Path(member.name)
            if path.is_absolute() or ".." in path.parts:
                raise ValueError(f"ARCHIVE_PATH_INVALID:{member.name}")
            if member.isdir():
                continue
            if not member.isfile():
                raise ValueError(f"ARCHIVE_NONREGULAR_MEMBER:{member.name}:{member.type!r}")
            extracted = archive.extractfile(member)
            if extracted is None:
                raise ValueError(f"ARCHIVE_READ_FAILED:{member.name}")
            content = extracted.read()
            rows.append({"path": member.name, "bytes": len(content), "sha256": digest(content)})
    return rows


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except BaseException:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def build_outputs(source: Path) -> dict[str, bytes]:
    rows, imported_manifest, build = qualify_source(source)
    tar_bytes, archive_bytes = deterministic_archive(source)
    if archive_rows(archive_bytes) != rows:
        raise ValueError("ARCHIVE_TREE_MISMATCH")
    qualification = QUALIFICATION_SOURCE.read_bytes()
    dockerfile = DOCKERFILE_SOURCE.read_bytes()
    license_bytes = (source / "CeCILL_LICENSE.txt").read_bytes()
    source_manifest = canonical_json(imported_manifest)
    archive_identity = {
        "schema_version": "coq-synthetic-incompleteness-source-archive/v1",
        "repository": build["source"]["repository"],
        "branch": BRANCH,
        "commit": COMMIT,
        "archive": {"path": ARCHIVE_NAME, "bytes": len(archive_bytes), "sha256": digest(archive_bytes)},
        "uncompressed_tar": {"bytes": len(tar_bytes), "sha256": digest(tar_bytes)},
        "tracked": {"files": len(rows), "bytes": sum(row["bytes"] for row in rows), "tree_sha256": manifest_hash(rows)},
        "source_manifest": {"path": "SOURCE_TREE_MANIFEST.json", "bytes": len(source_manifest), "sha256": digest(source_manifest)},
        "license": {"path": "CeCILL_LICENSE.txt", "bytes": len(license_bytes), "sha256": digest(license_bytes)},
    }
    toolchain = {
        "schema_version": "coq-synthetic-incompleteness-toolchain/v1",
        "platform": build["container"]["platform"],
        "base_image": build["container"]["base_image"],
        "derived_image": build["container"]["derived_image"],
        "coq": "8.15.2",
        "ocaml": "4.07.1",
        "dependencies": {
            "coq-equations": "1.3+8.15",
            "coq-smpl": "8.15",
            "coq-metacoq-template": "dev+8.15@9493bb6",
        },
        "dockerfile": {"path": "Dockerfile", "bytes": len(dockerfile), "sha256": digest(dockerfile)},
        "qualification": {"path": "Qualification.v", "bytes": len(qualification), "sha256": digest(qualification)},
        "upstream_build_receipt": {
            "path": "audit/imports/machine-overview-ce-map-20260915/source/evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001/BUILD-RECEIPT.json",
            "bytes": (IMPORTED / "BUILD-RECEIPT.json").stat().st_size,
            "sha256": digest((IMPORTED / "BUILD-RECEIPT.json").read_bytes()),
        },
    }
    import_receipt = {
        "schema_version": SCHEMA,
        "status": "VALID",
        "source_archive_sha256": digest(archive_bytes),
        "source_tree_sha256": manifest_hash(rows),
        "source_files": len(rows),
        "source_bytes": sum(row["bytes"] for row in rows),
        "qualification_sha256": digest(qualification),
        "dockerfile_sha256": digest(dockerfile),
        "evidence_boundary": "REPO_CONTAINED_EXACT_SOURCE_ARCHIVE_AND_REPLAY_INPUTS_NOT_YET_A_KERNEL_RUN",
    }
    return {
        ARCHIVE_NAME: archive_bytes,
        "SOURCE_TREE_MANIFEST.json": source_manifest,
        "SOURCE_ARCHIVE.json": canonical_json(archive_identity),
        "TOOLCHAIN.json": canonical_json(toolchain),
        "Qualification.v": qualification,
        "Dockerfile": dockerfile,
        "CeCILL_LICENSE.txt": license_bytes,
        "IMPORT.json": canonical_json(import_receipt),
    }


def validate(package: Path) -> dict[str, Any]:
    archive_meta = json.loads((package / "SOURCE_ARCHIVE.json").read_text(encoding="utf-8"))
    toolchain = json.loads((package / "TOOLCHAIN.json").read_text(encoding="utf-8"))
    receipt = json.loads((package / "IMPORT.json").read_text(encoding="utf-8"))
    manifest = json.loads((package / "SOURCE_TREE_MANIFEST.json").read_text(encoding="utf-8"))
    if receipt.get("schema_version") != SCHEMA or receipt.get("status") != "VALID":
        raise ValueError("IMPORT_RECEIPT_INVALID")
    archive_data = (package / ARCHIVE_NAME).read_bytes()
    if len(archive_data) != archive_meta["archive"]["bytes"] or digest(archive_data) != archive_meta["archive"]["sha256"]:
        raise ValueError("SOURCE_ARCHIVE_DRIFT")
    rows = archive_rows(archive_data)
    if rows != manifest.get("files"):
        raise ValueError("ARCHIVE_MANIFEST_MISMATCH")
    if len(rows) != receipt["source_files"] or manifest_hash(rows) != receipt["source_tree_sha256"]:
        raise ValueError("SOURCE_SUMMARY_MISMATCH")
    for key in ("dockerfile", "qualification"):
        row = toolchain[key]
        data = (package / row["path"]).read_bytes()
        if len(data) != row["bytes"] or digest(data) != row["sha256"]:
            raise ValueError(f"REPLAY_INPUT_DRIFT:{key}")
    license_row = archive_meta["license"]
    license_data = (package / license_row["path"]).read_bytes()
    if len(license_data) != license_row["bytes"] or digest(license_data) != license_row["sha256"]:
        raise ValueError("LICENSE_DRIFT")
    return {
        "status": "VALID",
        "commit": archive_meta["commit"],
        "source_files": len(rows),
        "source_bytes": sum(row["bytes"] for row in rows),
        "source_tree_sha256": manifest_hash(rows),
        "archive_bytes": len(archive_data),
        "archive_sha256": digest(archive_data),
        "image": toolchain["derived_image"]["id"],
        "evidence_boundary": receipt["evidence_boundary"],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("build", "validate"))
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--package", type=Path, default=PACKAGE)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "build":
            outputs = build_outputs(args.source.resolve())
            if not args.write:
                result = {"status": "DRY_RUN", "writes": False, "files": len(outputs), "archive_sha256": digest(outputs[ARCHIVE_NAME])}
            else:
                for name, data in outputs.items():
                    atomic_write(args.package.resolve() / name, data)
                result = validate(args.package.resolve())
        else:
            result = validate(args.package.resolve())
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError, subprocess.CalledProcessError, tarfile.TarError) as exc:
        print(json.dumps({"status": "INVALID", "error": str(exc)}, ensure_ascii=False, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
