#!/usr/bin/env python3
"""Actual CLI safety checks; not a replacement for the project proof-index verifier."""
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FORMAL = "HoTT/formal/astra-breakpoint-check/"
BASE_RUN = ROOT / "HoTT/verification/runs/20260919-MP-ASTRA-PATH-01"

def digest(path):
    b = path.read_bytes()
    return {"path": str(path), "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}

def main():
    base = json.loads((BASE_RUN / "RUN.json").read_text())
    retry = sys.argv[1:] == ["--safe-retry"]
    cases = [("SAFE", "Qualification", 0)] if retry else ([("RESTORATION", "RestorationQualification", 0)] if sys.argv[1:] == ["--restoration"] else [("SAFE", "Qualification", 0), ("OPAQUE", "OpaquePath", 42), ("STRING", "StringPragmaControl", 42)])
    for label, module, expected in cases:
        dest = ROOT / "HoTT/verification/runs" / ("20260919-ASTRA-CLI-" + label + ("-02" if retry else "-01"))
        dest.mkdir(exist_ok=False)
        cmd = base["command_argv"][:-1] + ["--safe", "--cubical", "--guardedness", FORMAL + module + ".agda"]
        start = dt.datetime.now(dt.timezone.utc).isoformat()
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True)
        (dest / "stdout.txt").write_bytes(result.stdout)
        (dest / "stderr.txt").write_bytes(result.stderr)
        (dest / "environment.txt").write_bytes((BASE_RUN / "environment.txt").read_bytes())
        paths = sorted(set(re.findall(r"Checking [\w.]+ \(([^\n]+\.agda)\)", result.stdout.decode())))
        own = sorted((ROOT / FORMAL).glob("*.agda")) if module == "Qualification" else [ROOT / FORMAL / (module + ".agda")]
        declarations = []
        for p in paths:
            for n, line in enumerate(Path(p).read_text().splitlines(), 1):
                if re.match(r"\s*(postulate|primitive)\b", line):
                    declarations.append({"path": p, "line": n, "text": line, "classification": "LEXICAL_CANDIDATE_NOT_SEMANTIC_AXIOM_AUDIT"})
        manifest = {"files": [digest(p) for p in own], "observed_checked_paths": paths,
                    "observed_source_hashes": [digest(Path(p)) for p in paths],
                    "declaration_scan": declarations,
                    "scan_scope": "Actual stdout-listed Agda sources; line-leading declaration candidates. Builtins/primitive kernel remain trusted; CLI --safe is separately enforced.",
                    "external_dependency_pins": json.loads((BASE_RUN / "source-manifest.json").read_text())["external_dependencies"]}
        (dest / "source-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        receipt = {"schema": "astra-cli-qualification/v1", "command_argv": cmd, "cwd": str(ROOT),
                   "started_at_utc": start, "completed_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                   "exit_code": result.returncode, "expected_exit": expected,
                   "status": "OBSERVED_EXPECTED_EXIT" if result.returncode == expected else "UNEXPECTED_EXIT",
                   "scope": "CLI option qualification and explicitly imported modules; no whole-project release claim",
                   "artifacts": [digest(dest / n) for n in ("stdout.txt", "stderr.txt", "environment.txt", "source-manifest.json")]}
        (dest / "RUN.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"run": dest.name, "exit": result.returncode, "expected": expected, "checked_sources": len(paths)}), flush=True)

if __name__ == "__main__":
    main()
