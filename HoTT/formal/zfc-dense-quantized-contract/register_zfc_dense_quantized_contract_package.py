#!/usr/bin/env python3
"""Register C-371 in the machine-managed proof-version closure registry."""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "HoTT/verification/PROOF_VERSION_CLOSURE.json"
sys.path.insert(0, str(ROOT / "scripts/audit"))
from proof_claim_ids import expand_claim_ids

PACKAGE = {
    "proof_id": "MP-ZFC-DENSE-QUANTIZED-CONTRACT-001",
    "claim_ids": "C-371",
    "source": "HoTT/formal/zfc-dense-quantized-contract/NormalizedCompletionContract.lean",
    "toolchain": "HoTT/formal/zfc-dense-quantized-contract/LEAN_CORE_TOOLCHAIN.json",
    "run": "HoTT/verification/runs/20261005-MP-ZFC-DENSE-QUANTIZED-CONTRACT-001-02",
    "kind": "lean_core_symbolic_dense_quantized_completion_contract_control",
    "verdict": "FORMAL_CHECKED_WITH_SCOPE: fixed normalized dense and quantized controls agree through stage three but their finite-stage completion predicates are not pointwise equivalent.",
    "notes": "Not a theorem about physical spacetime, ZFC, limit theory, IEP source facts, or a same-task bridge; C-361 and C-370 remain separate controls.",
}


def atomic_write(path: Path, data: bytes) -> None:
    fd, temp = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as out:
            out.write(data)
            out.flush()
            os.fsync(out.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--refresh-primary-run", action="store_true")
    args = parser.parse_args()
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    later, frozen = registry.get("later_packages"), registry.get("packages")
    if registry.get("schema_version") != "hott-proof-version-closure/v2" or not isinstance(later, list) or not isinstance(frozen, list):
        raise SystemExit("REGISTRY_SCHEMA_INVALID")
    rows = [*frozen, *later]
    existing = next((row for row in later if isinstance(row, dict) and row.get("proof_id") == PACKAGE["proof_id"]), None)
    if existing is not None and not args.refresh_primary_run:
        raise SystemExit("PACKAGE_ALREADY_REGISTERED")
    if existing is not None and any(existing.get(key) != PACKAGE[key] for key in ("proof_id", "claim_ids", "source", "toolchain")):
        raise SystemExit("REFRESH_IDENTITY_MISMATCH")
    claims = expand_claim_ids(PACKAGE["claim_ids"])
    occupied = {
        claim
        for row in rows
        if isinstance(row, dict)
        if row.get("proof_id") != PACKAGE["proof_id"]
        for claim in expand_claim_ids(row.get("claim_ids"))
    }
    if any(claim in occupied for claim in claims):
        raise SystemExit("CLAIM_ALREADY_REGISTERED")
    if not all((ROOT / PACKAGE[key]).is_file() for key in ("source", "toolchain")):
        raise SystemExit("PACKAGE_SOURCE_OR_TOOLCHAIN_MISSING")
    run_path = ROOT / PACKAGE["run"] / "RUN.json"
    if not run_path.is_file():
        raise SystemExit("PRIMARY_RUN_MISSING")
    run = json.loads(run_path.read_text(encoding="utf-8"))
    if run.get("proof_id") != PACKAGE["proof_id"] or run.get("claim_ids") != claims or run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE" or run.get("exit_code") != 0:
        raise SystemExit("PRIMARY_RUN_IDENTITY_INVALID")
    manifest = json.loads((run_path.parent / "source-manifest.json").read_text(encoding="utf-8"))
    if PACKAGE["source"] not in {row.get("path") for row in manifest.get("files", []) if isinstance(row, dict)}:
        raise SystemExit("PRIMARY_SOURCE_NOT_IN_MANIFEST")
    proposed = dict(registry)
    proposed["later_packages"] = [dict(PACKAGE) if isinstance(row, dict) and row.get("proof_id") == PACKAGE["proof_id"] else row for row in later]
    if existing is None:
        proposed["later_packages"].append(dict(PACKAGE))
    all_claims = {claim for row in proposed["later_packages"] for claim in expand_claim_ids(row.get("claim_ids"))}
    proposed["later_machine_proved_claim_count"] = len([claim for claim in all_claims if claim.startswith("C-") and claim[2:].isdigit()])
    if args.write:
        atomic_write(REGISTRY, (json.dumps(proposed, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8"))
    status = "REFRESHED" if args.refresh_primary_run and args.write else "WOULD_REFRESH" if args.refresh_primary_run else "REGISTERED" if args.write else "WOULD_REGISTER"
    print(json.dumps({"status": status, "proof_id": PACKAGE["proof_id"], "run": PACKAGE["run"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
