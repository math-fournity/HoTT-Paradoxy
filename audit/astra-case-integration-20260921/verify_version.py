#!/usr/bin/env python3
"""Requalify C320 against exact committed source/run/index evidence."""
from pathlib import Path
import subprocess
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
p=subprocess.run(['python3','-B','scripts/audit/verify_proof_version_closure.py','--proof-id','MP-ASTRA-NATIVE-TASK-INTEGRATION-001'],cwd=ROOT,capture_output=True)
(OUT/'selected-version.stdout.json').write_bytes(p.stdout);(OUT/'selected-version.stderr.txt').write_bytes(p.stderr)
print(p.stdout.decode());print(p.stderr.decode());raise SystemExit(p.returncode)
