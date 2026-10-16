#!/usr/bin/env python3
"""Write LEAN_TOOLCHAIN.json and MATHLIB_CLOSURE.json for the CG-005 Gödel-Q package.

Why this exists: the Gödel-Q package compiles against a project-owned Mathlib build
(the Astra cache, Lean v4.34.0) plus an overlay directory holding eight computability
modules that this goal compiled locally (network-denied).  The driver
godelq_lean_check.py refuses to run unless every pinned input still matches.  This
tool computes those pins once: the Lean binary and core library files, and the
SHA-256 digests of every compiled module in the import closure of the package
sources (found by walking `import` lines through the Mathlib and dependency sources).

Usage (cwd = repository root):
  python3 -B .claude/goals/CG-005-godel-q-synthesis/tools/make_godelq_pins.py
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
PACKAGE = ROOT / "HoTT/formal/claude-cg001/godel-q"
PREFIX = Path("/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0")
ASTRA = Path("/Volumes/D/HoTT-toolchain-cache/astra-real-geometry-v4.34.0/mathlib4-5ed2965256430c3649e86755f9576b54eca72435")
OVERLAY = Path("/Volumes/D/HoTT-toolchain-cache/godel-q-mathlib-ext-v4.34.0/lib/lean")
PACKAGES = ["batteries", "aesop", "Qq", "proofwidgets", "importGraph", "LeanSearchClient", "plausible", "Cli"]
TOP = {"Mathlib": "mathlib-overlay", "Batteries": "batteries", "Aesop": "aesop", "Qq": "Qq",
       "ProofWidgets": "proofwidgets", "ImportGraph": "importGraph",
       "LeanSearchClient": "LeanSearchClient", "Plausible": "plausible", "Cli": "Cli"}
CORE = ("Init", "Lean", "Std", "Lake")
IMPORT_RE = re.compile(r"^\s*(?:public\s+)?(?:meta\s+)?import\s+(?:all\s+)?([A-Za-z][\w\.]*)", re.MULTILINE)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def library_roots() -> dict[str, Path]:
    roots = {"mathlib-overlay": OVERLAY}
    for name in PACKAGES:
        roots[name] = ASTRA / ".lake/packages" / name / ".lake/build/lib/lean"
    return roots


def source_roots() -> dict[str, Path]:
    roots = {"mathlib-overlay": ASTRA}
    for name in PACKAGES:
        roots[name] = ASTRA / ".lake/packages" / name
    return roots


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
        "schema_version": "claude-cg005-lean-toolchain/v1",
        "tool": "lean",
        "version_line": version,
        "prefix": str(PREFIX),
        "pinned_files": pinned,
        "theory": "Lean 4 kernel with Mathlib (classical: propext, Classical.choice, Quot.sound); used for computability, real analysis and abstract proof-theory statements; never for HoTT paths",
        "provenance": "elan toolchain leanprover/lean4:v4.34.0, installed on this machine before 2026-09-25; not downloaded for CG-005",
        "isolation": "the driver calls bin/lean by absolute path inside /usr/bin/sandbox-exec with (deny network*); environment PATH=<prefix>/bin:/usr/bin:/bin, LEAN_SYSROOT=<prefix>, LEAN_PATH=<temporary build>:<pinned library roots>; the elan proxy is never invoked",
        "source_policy": "no sorry, admit, native_decide, axiom declarations, unsafe, implemented_by, extern, opaque or kernel-skipping options in sources; every main theorem is followed by #print axioms",
    }

    lib = library_roots()
    src = source_roots()
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
        label = TOP[top]
        source = src[label].joinpath(*module.split(".")).with_suffix(".lean")
        if not source.exists():
            raise SystemExit(f"MODULE_SOURCE_MISSING:{module}")
        for imp in imports_of(source.read_text(encoding="utf-8")):
            if imp.split(".")[0] in TOP and imp not in seen:
                stack.append(imp)
        rows.append({"module": module, "root": label, "digest": module_digest(lib[label], module)})
    rows.sort(key=lambda r: r["module"])
    aggregate = hashlib.sha256("".join(f"{r['module']}:{r['digest']}\n" for r in rows).encode()).hexdigest()
    overlay_built = []
    for path in sorted(OVERLAY.rglob("*")):
        if path.is_file() and not path.is_symlink():
            data = path.read_bytes()
            overlay_built.append({"path": path.relative_to(OVERLAY).as_posix(), "bytes": len(data), "sha256": sha(data)})
    closure = {
        "schema_version": "claude-cg005-mathlib-closure/v1",
        "mathlib_source": {"path": str(ASTRA), "commit": "5ed2965256430c3649e86755f9576b54eca72435",
                            "lean_toolchain": (ASTRA / "lean-toolchain").read_text().strip()},
        "overlay": {"path": str(OVERLAY.parent), "note": "symlink mirror of the Astra Mathlib build plus eight modules compiled for CG-005 with the pinned lean, network-denied, options autoImplicit=false maxSynthPendingDepth=3 pp.unicode.fun=true", "locally_built_files": overlay_built},
        "library_roots": {k: str(v) for k, v in lib.items()},
        "lean_path": [str(lib["mathlib-overlay"])] + [str(lib[name]) for name in PACKAGES],
        "lean_options": {"autoImplicit": "false"},
        "module_count": len(rows),
        "aggregate_sha256": aggregate,
        "modules": rows,
    }
    (PACKAGE / "LEAN_TOOLCHAIN.json").write_text(json.dumps(toolchain, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (PACKAGE / "MATHLIB_CLOSURE.json").write_text(json.dumps(closure, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"modules": len(rows), "aggregate_sha256": aggregate, "overlay_built_files": len(overlay_built)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
