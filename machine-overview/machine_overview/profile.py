"""Profile qualification: pinned toolchain, pinned sources, declared symbols."""
from __future__ import annotations

from pathlib import Path

from .util import (
    MachineOverviewError,
    deterministic_tree,
    file_row,
    read_json,
    safe_relative,
    sha256_file,
)


def inspect_profile(repo_root: Path, profile_path: Path, *, fast: bool = False) -> dict:
    """Check that a profile's toolchain and sources still match their pins."""
    profile = read_json(profile_path)
    if profile.get("schema_version") != "machine-overview-profile/v1":
        raise MachineOverviewError("PROFILE_SCHEMA_INVALID")

    checks: list[dict] = []

    toolchain_rel = safe_relative(profile["toolchain_ref"])
    toolchain_path = repo_root / toolchain_rel
    toolchain = read_json(toolchain_path)
    if toolchain.get("schema_version") != "hott-cubical-agda-toolchain/v1":
        raise MachineOverviewError("TOOLCHAIN_SCHEMA_INVALID")
    checks.append({"check": "toolchain_file_present", "status": "PASS", "path": toolchain_rel.as_posix(),
                   "sha256": sha256_file(toolchain_path)})

    agda = toolchain["agda"]
    agda_binary = Path(agda["local_binary"])
    row = file_row(agda_binary)
    agda_ok = row["bytes"] == agda["binary_bytes"] and row["sha256"] == agda["binary_sha256"]
    checks.append({"check": "agda_binary_pin", "status": "PASS" if agda_ok else "FAIL",
                   "path": str(agda_binary), "sha256": row["sha256"],
                   "expected_sha256": agda["binary_sha256"], "bytes": row["bytes"]})

    cubical = toolchain["cubical_library"]
    library_file = Path(cubical["library_file"])
    library_row = file_row(library_file)
    library_ok = (
        library_row["bytes"] == cubical["library_file_bytes"]
        and library_row["sha256"] == cubical["library_file_sha256"]
    )
    checks.append({"check": "cubical_library_file_pin", "status": "PASS" if library_ok else "FAIL",
                   "path": str(library_file), "sha256": library_row["sha256"]})

    tree_status = "SKIPPED_FAST_MODE"
    tree_actual: dict[str, object] | None = None
    if not fast:
        tree_actual = deterministic_tree(Path(cubical["local_root"]))
        tree_ok = (
            tree_actual["file_count"] == cubical["tree_file_count"]
            and tree_actual["total_bytes"] == cubical["tree_total_bytes"]
            and tree_actual["tree_sha256"] == cubical["tree_sha256"]
        )
        tree_status = "PASS" if tree_ok else "FAIL"
    checks.append({"check": "cubical_source_tree_pin", "status": tree_status,
                   "expected_tree_sha256": cubical["tree_sha256"],
                   "actual": tree_actual})

    library_registry_rel = safe_relative(profile["library_registry"])
    registry_path = repo_root / library_registry_rel
    checks.append({"check": "library_registry_present", "status": "PASS" if registry_path.is_file() else "FAIL",
                   "path": library_registry_rel.as_posix(), "sha256": sha256_file(registry_path)})

    source_reports: list[dict] = []
    for source in profile.get("sources", []):
        relative = safe_relative(source["path"])
        path = repo_root / relative
        if not path.is_file() or path.is_symlink():
            source_reports.append({"path": relative.as_posix(), "status": "MISSING"})
            continue
        digest = sha256_file(path)
        pinned = source.get("sha256")
        report: dict = {
            "path": relative.as_posix(),
            "status": "PASS" if (pinned is None or pinned == digest) else "FAIL",
            "sha256": digest,
            "expected_sha256": pinned,
            "symbols": [],
        }
        lines = path.read_text(encoding="utf-8").splitlines()
        for symbol in source.get("symbols", []):
            start, end = symbol["lines"]
            window = "\n".join(lines[start - 1:end])
            found = symbol["name"] in window
            report["symbols"].append({"name": symbol["name"], "lines": [start, end], "kind": symbol.get("kind"),
                                      "status": "PASS" if found else "FAIL"})
        if any(item["status"] == "FAIL" for item in report["symbols"]):
            report["status"] = "FAIL"
        source_reports.append(report)

    hard_failures = [
        check["check"]
        for check in checks
        if check["status"] == "FAIL"
    ] + [
        report["path"] + ":" + symbol["name"]
        for report in source_reports
        for symbol in report.get("symbols", [])
        if symbol["status"] == "FAIL"
    ] + [
        report["path"] for report in source_reports if report["status"] == "MISSING"
    ]
    return {
        "profile_id": profile["profile_id"],
        "profile_path": str(profile_path),
        "schema_version": profile["schema_version"],
        "theory_variant": profile["theory_variant"],
        "toolchain_ref": toolchain_rel.as_posix(),
        "toolchain_sha256": sha256_file(toolchain_path),
        "library_registry": library_registry_rel.as_posix(),
        "checks": checks,
        "sources": source_reports,
        "supported_operations": profile.get("supported_operations", []),
        "unsupported": profile.get("unsupported", []),
        "status": "PROFILE_QUALIFIED" if not hard_failures else "PROFILE_NOT_QUALIFIED",
        "failures": hard_failures,
    }
