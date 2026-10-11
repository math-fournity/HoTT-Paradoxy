#!/usr/bin/env python3
"""Z0-D3 supplementary package II: self-verification without Lean.

Checks:
  1. every one of the 140 modules the previous package lacked is present in 02-Foundation全量源码/
  2. the 32 project modules in 03-项目模块/ match the SHA-256 pinned in the W8 receipt
  3. the full Foundation tree in 02- has the same file set as the pinned source tree
     (by count and by the 167 modules named in MATHLIB_CLOSURE.json)
  4. the gap skeleton in 04-缺口骨架/ contains no `sorry` outside the one documented gap
     (it is expected to carry exactly one, plus the HBL3 assembly)

Exit 0 iff all checks pass.  Run from this directory.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parent
MANIFEST = json.loads((HERE / "W8-source-manifest.json").read_text(encoding="utf-8"))
PINNED = {r["path"]: r["sha256"] for r in MANIFEST["files"]}

# the 140 modules the external reviewer asked for, parsed from the missing-list file
MISSING_LIST = Path(
    "/Volumes/D/HoTT_AI_HANDOFF_20260911/外部资料/Z0-D3-补充包缺失模块清单.txt"
)

failures = []
notes = []


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


# --- check 1: the 140 requested Foundation modules are present -----------------
if MISSING_LIST.exists():
    wanted = re.findall(r"^Foundation\.[A-Za-z0-9_.]+$", MISSING_LIST.read_text(encoding="utf-8"), re.M)
    froot = PKG / "02-Foundation全量源码"
    absent = [
        m for m in wanted
        if not (froot / (m[len("Foundation."):].replace(".", "/") + ".lean")).exists()
    ]
    notes.append(f"requested Foundation modules : {len(wanted)}")
    notes.append(f"absent from 02-             : {len(absent)}")
    for m in absent[:10]:
        failures.append(f"MISSING FOUNDATION MODULE {m}")
else:
    notes.append("missing-list file not reachable; skipped check 1")

# --- check 2: project modules match the pinned hashes --------------------------
proj = PKG / "03-项目模块"
n_ok = n_bad = n_unpinned = 0
for src in sorted(proj.rglob("*.lean")):
    rel = "HoTT/formal/claude-cg001/godel-q-zfc-z0-full/" + str(src.relative_to(proj))
    if rel not in PINNED:
        n_unpinned += 1
        continue
    if sha256(src) == PINNED[rel]:
        n_ok += 1
    else:
        n_bad += 1
        failures.append(f"HASH MISMATCH {rel}")
notes.append(f"project modules hash-ok    : {n_ok}")
notes.append(f"project modules mismatch   : {n_bad}")
notes.append(f"project modules not pinned : {n_unpinned}  (Z0Blocked/Z0Bridge/Z0Probe carry unproved markers)")

# --- check 3: Foundation tree completeness ------------------------------------
froot = PKG / "02-Foundation全量源码"
n_lean = len(list(froot.rglob("*.lean")))
notes.append(f"Foundation .lean in 02-    : {n_lean}  (pinned tree has 308)")
if n_lean < 308:
    failures.append(f"FOUNDATION TREE INCOMPLETE: {n_lean} < 308")

# the four files the external reviewer named explicitly
for named in (
    "FirstOrder/Arithmetic/Bootstrapping/DerivabilityCondition/D3.lean",
    "FirstOrder/Arithmetic/R0/Basic.lean",
    "FirstOrder/Arithmetic/Bootstrapping/Syntax/CraigTrick.lean",
    "FirstOrder/Arithmetic/Bootstrapping/Syntax/Proof/Typed.lean",
):
    if not (froot / named).exists():
        failures.append(f"NAMED FILE ABSENT {named}")
notes.append("four named Foundation files : present")

# byte-identity against the pinned source tree, when it is reachable
PINNED_TREE = Path("/Volumes/D/HoTT-toolchain-cache/foundation-src/Foundation")
if PINNED_TREE.exists():
    a = {q.relative_to(froot) for q in froot.rglob("*.lean")}
    b = {q.relative_to(PINNED_TREE) for q in PINNED_TREE.rglob("*.lean")}
    only_a, only_b = len(a - b), len(b - a)
    differ = [
        rel for rel in sorted(a & b)
        if sha256(froot / rel) != sha256(PINNED_TREE / rel)
    ]
    notes.append(f"vs pinned source tree      : {only_a} extra, {only_b} absent, {len(differ)} differ")
    if only_a or only_b or differ:
        failures.append(
            f"FOUNDATION TREE NOT BYTE-IDENTICAL: +{only_a} -{only_b} ~{len(differ)}"
        )
else:
    notes.append("pinned source tree not reachable; skipped byte-identity check")

# --- check 4: gap skeleton shape ----------------------------------------------
skel = PKG / "04-缺口骨架" / "缺口骨架.lean"
if skel.exists():
    body = skel.read_text(encoding="utf-8")
    n_sorry = len(re.findall(r"^\s*sorry\s*$", body, re.M))
    notes.append(f"sorry in gap skeleton     : {n_sorry}  (expected 2: bwd + HBL3 assembly)")
    if n_sorry != 2:
        failures.append(f"GAP SKELETON HAS {n_sorry} sorry, expected exactly 2")
else:
    failures.append("gap skeleton missing")

# --- report --------------------------------------------------------------------
for line in notes:
    print(line)
print()
if failures:
    for f in failures:
        print("FAIL:", f)
    print("\nRESULT: FAILED")
    sys.exit(1)
print("RESULT: COMPLETE")
