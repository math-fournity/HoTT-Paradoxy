#!/usr/bin/env python3
"""Write LEAN_TOOLCHAIN.json and MATHLIB_CLOSURE.json for the CG-006 package `godel-q-zfc-z0` (S6, Z0 conditional form).

Why this exists: the package compiles against FormalizedFormalLogic/Foundation@1fb01b72, built
locally (network-denied) into /Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0
by tools/ffl_build.py.  That build tree holds the Foundation modules it compiled plus a symlink
mirror of the project-owned Mathlib build (Astra cache, commit 5ed29652) and of the CG-005
computability overlay.  zfc_lean_check.py refuses to run unless every pinned input still matches.
This tool computes the pins once: the Lean binary and core library files, and the SHA-256
digests of every compiled module in the import closure of the package sources (found by walking
`import` lines through the Foundation, Mathlib and dependency sources; symlinks are followed).
Copied unchanged from make_zfc_pins.py except for the package path and this docstring (make_zfc_pins.py is frozen by the godel-q-zfc receipts).

Usage (cwd = repository root):
  python3 -B .claude/goals/CG-006-zfc-complete-formalization/tools/make_z0_pins.py
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "HoTT/formal/claude-cg001/godel-q-zfc-z0"
PREFIX = Path("/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0")
ASTRA = Path("/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435")
FSRC = Path("/Volumes/D/HoTT-toolchain-cache/foundation-src")
FBUILD = Path("/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0/lib/lean")
PACKAGES = ["batteries", "aesop", "Qq", "proofwidgets", "importGraph", "LeanSearchClient", "plausible", "Cli"]
TOP = {"Mathlib": "foundation-build", "Foundation": "foundation-build", "Batteries": "batteries",
       "Aesop": "aesop", "Qq": "Qq", "ProofWidgets": "proofwidgets", "ImportGraph": "importGraph",
       "LeanSearchClient": "LeanSearchClient", "Plausible": "plausible", "Cli": "Cli"}
CORE = ("Init", "Lean", "Std", "Lake")
IMPORT_RE = re.compile(r"^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([A-Za-z][\w\.]*)", re.MULTILINE)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def library_roots() -> dict[str, Path]:
    roots = {"foundation-build": FBUILD}
    for name in PACKAGES:
        roots[name] = ASTRA / ".lake/packages" / name / ".lake/build/lib/lean"
    return roots


def source_root(module: str) -> Path:
    top = module.split(".")[0]
    if top == "Foundation":
        return FSRC
    if top == "Mathlib":
        return ASTRA
    return ASTRA / ".lake/packages" / TOP[top]


def module_digest(lib_root: Path, module: str) -> str:
    base = lib_root.joinpath(*module.split("."))
    digest = hashlib.sha256()
    found = False
    for suffix in (".olean", ".olean.private", ".olean.server"):
        path = Path(str(base) + suffix)
        if path.exists():
            found = True
            digest.update(suffix.encode())
            digest.update(sha(path.read_bytes()).encode())
    if not found:
        raise SystemExit(f"MODULE_OLEAN_MISSING:{module}")
    return digest.hexdigest()


def imports_of(text: str) -> list[str]:
    body = re.sub(r"/-.*?-/", "", text, flags=re.DOTALL)
    return IMPORT_RE.findall(body)


def git_head(path: Path) -> str:
    out = subprocess.run(["git", "-C", str(path), "rev-parse", "HEAD"], capture_output=True, text=True)
    return out.stdout.strip()


def main() -> int:
    pinned = []
    for rel in ("bin/lean", "lib/lean/libleanshared.dylib", "lib/lean/libleanshared_1.dylib",
                "lib/lean/libleanshared_2.dylib", "lib/lean/libInit_shared.dylib",
                "lib/lean/libLake_shared.dylib", "lib/lean/Init.olean", "lib/lean/Init/Prelude.olean",
                "lib/lean/Lean.olean", "lib/lean/Std.olean"):
        data = (PREFIX / rel).read_bytes()
        pinned.append({"relative_path": rel, "bytes": len(data), "sha256": sha(data)})
    version = subprocess.run([str(PREFIX / "bin/lean"), "--version"], capture_output=True, text=True,
                             env={"PATH": f"{PREFIX}/bin:/usr/bin:/bin", "LEAN_SYSROOT": str(PREFIX)}).stdout.strip()
    toolchain = {
        "schema_version": "claude-cg006-lean-toolchain/v1",
        "tool": "lean",
        "version_line": version,
        "prefix": str(PREFIX),
        "pinned_files": pinned,
        "theory": "Lean 4 kernel with Mathlib and FormalizedFormalLogic/Foundation (classical: propext, Classical.choice, Quot.sound); first-order ZFC (Foundation's 𝗭𝗙𝗖 over ℒₛₑₜ, LK), arithmetic, computability and abstract proof theory; never HoTT paths",
        "provenance": "elan toolchain leanprover/lean4:v4.34.0, installed on this machine before 2026-09-25; not downloaded for CG-006",
        "isolation": "the driver calls bin/lean by absolute path inside /usr/bin/sandbox-exec with (deny network*); environment PATH=<prefix>/bin:/usr/bin:/bin, LEAN_SYSROOT=<prefix>, LEAN_PATH=<temporary build>:<pinned library roots>; the elan proxy is never invoked",
        "source_policy": "no sorry, admit, native_decide, axiom declarations, unsafe, implemented_by, extern, opaque or kernel-skipping options in sources; main theorems are followed by #print axioms",
    }

    lib = library_roots()
    start = []
    for path in sorted((PACKAGE / "GodelQ").rglob("*.lean")):
        start += imports_of(path.read_text(encoding="utf-8"))
    seen: set[str] = set()
    stack = [m for m in start if m.split(".")[0] in TOP]
    rows = []
    while stack:
        module = stack.pop()
        if module in seen:
            continue
        seen.add(module)
        top = module.split(".")[0]
        if top in CORE:
            continue
        if top not in TOP:
            raise SystemExit(f"UNKNOWN_TOP_LEVEL:{module}")
        source = source_root(module).joinpath(*module.split(".")).with_suffix(".lean")
        if not source.exists():
            raise SystemExit(f"MODULE_SOURCE_MISSING:{module}")
        for imp in imports_of(source.read_text(encoding="utf-8")):
            if imp.split(".")[0] in TOP and imp not in seen:
                stack.append(imp)
        rows.append({"module": module, "root": TOP[top], "digest": module_digest(lib[TOP[top]], module)})
    rows.sort(key=lambda r: r["module"])
    aggregate = hashlib.sha256("".join(f"{r['module']}:{r['digest']}\n" for r in rows).encode()).hexdigest()
    built = []
    for path in sorted(FBUILD.rglob("*")):
        if path.is_file() and not path.is_symlink():
            data = path.read_bytes()
            built.append({"path": path.relative_to(FBUILD).as_posix(), "bytes": len(data), "sha256": sha(data)})
    closure = {
        "schema_version": "claude-cg006-foundation-closure/v1",
        "mathlib_source": {"path": str(ASTRA), "commit": "5ed2965256430c3649e86755f9576b54eca72435",
                            "lean_toolchain": (ASTRA / "lean-toolchain").read_text().strip()},
        "foundation_source": {"path": str(FSRC), "commit": git_head(FSRC),
                               "lean_toolchain": (FSRC / "lean-toolchain").read_text().strip()},
        "foundation_build": {"path": str(FBUILD.parent.parent),
                              "note": "built by .claude/goals/CG-006-zfc-complete-formalization/tools/ffl_build.py with the pinned lean, network-denied; Mathlib entries are symlinks to the Astra build and the CG-005 overlay, except modules compiled for Foundation",
                              "locally_built_files": built},
        "library_roots": {k: str(v) for k, v in lib.items()},
        "lean_path": [str(lib["foundation-build"])] + [str(lib[name]) for name in PACKAGES],
        "lean_options": {"autoImplicit": "false"},
        "module_count": len(rows),
        "aggregate_sha256": aggregate,
        "modules": rows,
    }
    (PACKAGE / "LEAN_TOOLCHAIN.json").write_text(json.dumps(toolchain, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (PACKAGE / "MATHLIB_CLOSURE.json").write_text(json.dumps(closure, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"modules": len(rows), "aggregate_sha256": aggregate, "locally_built_files": len(built)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
