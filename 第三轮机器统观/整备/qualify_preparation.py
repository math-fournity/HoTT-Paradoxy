#!/usr/bin/env python3
"""One-shot local preparation evidence; not MO3 research or an AI-behavior test."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def save_json(path: Path, data: object):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


def run(argv: list[str], cwd: Path, out: Path, timeout=180):
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    try:
        completed = subprocess.run(argv, cwd=cwd, capture_output=True, timeout=timeout)
        code, stdout, stderr = completed.returncode, completed.stdout, completed.stderr
    except subprocess.TimeoutExpired as exc:
        code, stdout, stderr = "TIMEOUT", exc.stdout or b"", exc.stderr or b""
    (out / "stdout.txt").write_bytes(stdout)
    (out / "stderr.txt").write_bytes(stderr)
    receipt = {"argv": argv, "cwd": str(cwd), "exit": code, "observation_seconds": time.monotonic() - started,
               "timeout_seconds": timeout, "stdout_sha256": sha(stdout), "stderr_sha256": sha(stderr)}
    save_json(out / "RUN.json", receipt)
    return receipt, stdout, stderr


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    result = {"scope": "PREPARATION_INTERFACES_ONLY", "checks": {}}
    tests, _, _ = run([sys.executable, "-B", "-m", "unittest", "discover", "-s", str(HERE), "-p", "test_handoff_snapshot.py", "-v"], ROOT, out / "handoff-tests")
    result["checks"]["handoff_tests"] = tests["exit"] == 0
    load, body, _ = run([sys.executable, "-B", ".codex/tools/cognition_runtime.py", "plan", "--profile", "research"], ROOT, out / "loader-plan")
    if load["exit"] != 0:
        raise SystemExit("LOADER_PLAN_FAILED")
    plan = json.loads(body)
    save_json(out / "loader-summary.json", {k: plan.get(k) for k in ["snapshot", "revision", "latest_session", "full_set_documents", "hydration_diagnostics", "review_required"]} | {"documents": len(plan["documents"]), "bytes": sum(d["bytes"] for d in plan["documents"]), "lines": sum(d["lines"] for d in plan["documents"])})
    result["checks"]["research_plan"] = True
    counts = {}
    for name in ["Session-A-goal提示词.txt", "Session-B-goal提示词.txt"]:
        text = (HERE / name).read_text()
        counts[name] = {"unicode_codepoints_including_whitespace": len(text), "utf8_bytes": len(text.encode()), "sha256": sha(text.encode())}
    save_json(out / "prompt-counts.json", counts)
    result["checks"]["prompts_le_4000"] = all(v["unicode_codepoints_including_whitespace"] <= 4000 for v in counts.values())
    toolchain = json.loads((ROOT / "HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json").read_text())
    binary = Path(toolchain["agda"]["local_binary"])
    result["checks"]["native_binary_hash"] = sha(binary.read_bytes()) == toolchain["agda"]["binary_sha256"]
    sources = {
        "Positive.agda": "{-# OPTIONS --safe --cubical --guardedness #-}\nmodule Positive where\nopen import Cubical.Foundations.Prelude\nopen import Cubical.Data.Bool.Base using (Bool; true; false)\ncheck : true ≡ true\ncheck = refl\n",
        "Negative.agda": "{-# OPTIONS --safe --cubical --guardedness #-}\nmodule Negative where\nopen import Cubical.Foundations.Prelude\nopen import Cubical.Data.Bool.Base using (Bool; true; false)\ncheck : true ≡ false\ncheck = refl\n"}
    for name, content in sources.items():
        (out / name).write_text(content)
    # All interface/cache writes go to disposable copies; the pinned library is read only.
    with tempfile.TemporaryDirectory(prefix="mo3-native-", dir="/Volumes/D/HoTT-toolchain-cache") as temporary:
        work = Path(temporary).resolve()
        library = work / "cubical"
        original = Path(toolchain["cubical_library"]["local_root"])
        shutil.copytree(original, library, ignore=shutil.ignore_patterns("*.agdai", ".DS_Store", ".git"))
        registry = work / "libraries"
        registry.write_text(str(library / "cubical.agda-lib") + "\n")
        cache = toolchain["runtime_cache"]
        # A copied XDG data tree supplies builtins without modifying the original cache.
        xdg = work / "xdg-data"
        if Path(cache["xdg_data_home"]).exists():
            shutil.copytree(cache["xdg_data_home"], xdg, ignore=shutil.ignore_patterns("*.agdai"))
        else:
            xdg.mkdir()
        (work / "xdg-config").mkdir()
        (work / "tmp").mkdir()
        prefix = ["env", f"XDG_DATA_HOME={xdg}", f"XDG_CONFIG_HOME={work / 'xdg-config'}", f"TMPDIR={work / 'tmp'}", str(binary)]
        cases = [("native-positive", "Positive.agda"), ("native-negative", "Negative.agda"), ("auditor-copy-positive", "Positive.agda")]
        native = []
        for case, source in cases:
            case_root = work / case
            case_root.mkdir()
            shutil.copy2(out / source, case_root / source)
            argv = prefix + ["--ignore-interfaces", f"--library-file={registry}", "-l", "cubical-0.9", "-i", str(case_root), str(case_root / source)]
            receipt, stdout, stderr = run(argv, case_root, out / case)
            receipt["source_sha256"] = sha((case_root / source).read_bytes())
            receipt["library_identity_source"] = "HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json"
            native.append(receipt)
        result["checks"]["native_positive"] = native[0]["exit"] == 0
        negative_text = (out / "native-negative/stdout.txt").read_text() + (out / "native-negative/stderr.txt").read_text()
        result["checks"]["native_negative"] = native[1]["exit"] not in [0, "TIMEOUT"] and "true" in negative_text and "false" in negative_text
        result["checks"]["auditor_copy_replay"] = native[2]["exit"] == 0 and native[0]["source_sha256"] == native[2]["source_sha256"]
        save_json(out / "native-summary.json", native)
    result["status"] = "PASS_WITH_SCOPE" if all(result["checks"].values()) else "FAIL"
    save_json(out / "RESULT.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS_WITH_SCOPE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
