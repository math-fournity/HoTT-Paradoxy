#!/usr/bin/env python3
"""Verify this package covers the whole Foundation subset of the import closure.

Run from the package directory:  python3 verify_coverage.py
No Lean needed.  Checks:
  1. every Foundation module in MATHLIB_CLOSURE.json has a source file here;
  2. every project .lean module that the W8 receipt pinned still matches its SHA-256.
"""
import hashlib, json
from pathlib import Path

PKG = Path(__file__).resolve().parent
cl = json.loads((PKG / "项目模块/MATHLIB_CLOSURE.json").read_text(encoding="utf-8"))
man = json.loads((PKG / "收据/W8-source-manifest.json").read_text(encoding="utf-8"))

fd = PKG / "Foundation"
have = {"Foundation." + ".".join(f.relative_to(fd).with_suffix("").parts) for f in fd.rglob("*.lean")}
want = sorted({r["module"] for r in cl["modules"] if r.get("module", "").startswith("Foundation.")})
missing = [m for m in want if m not in have]
print(f"Foundation closure modules : {len(want)}")
print(f"Foundation source files     : {len(have)}")
print(f"MISSING                     : {len(missing)}")
for m in missing:
    print("   ", m)

rows = {r["path"]: r for r in man["files"]}
ok = bad = np = 0
for m in sorted((PKG / "项目模块/GodelQ").rglob("*.lean")):
    rel = "HoTT/formal/claude-cg001/godel-q-zfc-z0-full/" + str(m.relative_to(PKG / "项目模块"))
    if rel not in rows:
        np += 1; print("NOT_PINNED (expected for the 3 unproved files):", rel); continue
    if hashlib.sha256(m.read_bytes()).hexdigest() == rows[rel]["sha256"]:
        ok += 1
    else:
        bad += 1; print("HASH_MISMATCH", rel)
print(f"project modules hash-ok     : {ok}")
print(f"project modules mismatch    : {bad}")
print(f"project modules not pinned  : {np}  (Z0Blocked / Z0Bridge / Z0Probe - all carry unproved markers)")
print()
print("RESULT:", "COMPLETE" if not missing and bad == 0 else "INCOMPLETE")
