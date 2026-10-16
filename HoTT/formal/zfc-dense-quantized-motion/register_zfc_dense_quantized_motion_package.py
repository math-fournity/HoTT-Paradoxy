#!/usr/bin/env python3
"""Register C-370's fixed Lean package in the machine-managed proof registry."""
from __future__ import annotations
import argparse, json, os, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "HoTT/verification/PROOF_VERSION_CLOSURE.json"
sys.path.insert(0, str(ROOT / "scripts/audit"))
from proof_claim_ids import expand_claim_ids
PACKAGE = {
    "proof_id": "MP-ZFC-DENSE-QUANTIZED-MOTION-001",
    "claim_ids": "C-370",
    "source": "HoTT/formal/zfc-dense-quantized-motion/QuantizedHalfControl.lean",
    "toolchain": "HoTT/formal/zfc-dense-quantized-motion/LEAN_CORE_TOOLCHAIN.json",
    "run": "HoTT/verification/runs/20261005-MP-ZFC-DENSE-QUANTIZED-MOTION-001-02",
    "kind": "lean_core_finite_quantized_half_step_motion_control",
    "verdict": "FORMAL_CHECKED_WITH_SCOPE: fixed eight-unit quantized half-step process reaches zero at stage four and not stage three; it is a finite control for the user-specified dense-versus-quantized contrast.",
    "notes": "Not a theorem about physical spacetime, Planck scale, ZFC, or limit theory; C-361 is a separately verified dense counterpart.",
}
def atomic_write(path: Path, data: bytes) -> None:
    fd, temp = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as out:
            out.write(data); out.flush(); os.fsync(out.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp): os.unlink(temp)
def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--refresh-primary-run", action="store_true")
    args = parser.parse_args()
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    later, frozen = registry.get("later_packages"), registry.get("packages")
    if registry.get("schema_version") != "hott-proof-version-closure/v2" or not isinstance(later,list) or not isinstance(frozen,list): raise SystemExit("REGISTRY_SCHEMA_INVALID")
    rows=[*frozen,*later]
    existing=next((r for r in later if isinstance(r,dict) and r.get("proof_id")==PACKAGE["proof_id"]),None)
    if existing is not None and not args.refresh_primary_run: raise SystemExit("PACKAGE_ALREADY_REGISTERED")
    if existing is not None and any(existing.get(k)!=PACKAGE[k] for k in ("proof_id","claim_ids","source","toolchain")): raise SystemExit("REFRESH_IDENTITY_MISMATCH")
    claims=expand_claim_ids(PACKAGE["claim_ids"])
    occupied={c for r in rows if isinstance(r,dict) and r.get("proof_id")!=PACKAGE["proof_id"] for c in expand_claim_ids(r.get("claim_ids"))}
    if any(c in occupied for c in claims): raise SystemExit("CLAIM_ALREADY_REGISTERED")
    if not all((ROOT/PACKAGE[k]).is_file() for k in ("source","toolchain")): raise SystemExit("PACKAGE_SOURCE_OR_TOOLCHAIN_MISSING")
    rp=ROOT/PACKAGE["run"]/'RUN.json'
    if not rp.is_file(): raise SystemExit("PRIMARY_RUN_MISSING")
    run=json.loads(rp.read_text())
    if run.get("proof_id")!=PACKAGE["proof_id"] or run.get("claim_ids")!=claims or run.get("status")!="KERNEL_ACCEPTED_WITH_SCOPE" or run.get("exit_code")!=0: raise SystemExit("PRIMARY_RUN_IDENTITY_INVALID")
    manifest=json.loads((rp.parent/'source-manifest.json').read_text())
    if PACKAGE["source"] not in {r.get("path") for r in manifest.get("files",[]) if isinstance(r,dict)}: raise SystemExit("PRIMARY_SOURCE_NOT_IN_MANIFEST")
    proposed=dict(registry); proposed["later_packages"]=[dict(PACKAGE) if isinstance(r,dict) and r.get("proof_id")==PACKAGE["proof_id"] else r for r in later]
    if existing is None: proposed["later_packages"].append(dict(PACKAGE))
    all_claims={c for r in proposed["later_packages"] for c in expand_claim_ids(r.get("claim_ids"))}
    proposed["later_machine_proved_claim_count"]=len([c for c in all_claims if c.startswith("C-") and c[2:].isdigit()])
    if args.write: atomic_write(REGISTRY,(json.dumps(proposed,ensure_ascii=False,sort_keys=True,indent=2)+"\n").encode())
    print(json.dumps({"status":"REFRESHED" if args.refresh_primary_run and args.write else "WOULD_REFRESH" if args.refresh_primary_run else "REGISTERED" if args.write else "WOULD_REGISTER","proof_id":PACKAGE["proof_id"],"run":PACKAGE["run"]},ensure_ascii=False))
    return 0
if __name__ == "__main__": raise SystemExit(main())
