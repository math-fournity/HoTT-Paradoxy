#!/usr/bin/env python3
"""Run the four declared changes and independent restoration after baseline acceptance."""
from pathlib import Path
import json, subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BASELINE = ROOT / 'HoTT/verification/runs/20260920-MP-ASTRA-S1-CONSUMER-001-01/RUN.json'
assert json.loads(BASELINE.read_text())['exit_code'] == 0
rows = []
for case in ['SC01', 'SC02', 'SC03', 'SC04', 'SC05']:
    subprocess.run(['python3', '-B', str(OUT / 'generate_cases.py'), '--case', case], cwd=ROOT, check=True)
    subprocess.run(['python3', '-B', str(OUT / 'capture.py'), '--case', case], cwd=ROOT, check=True)
    run = 'HoTT/verification/runs/20260920-MP-ASTRA-S1-' + case + '-CONTROL-01'
    receipt = json.loads((ROOT / run / 'RUN.json').read_text())
    rows.append({'case': case, 'run': run, 'exit': receipt['exit_code'],
                 'seconds': receipt['duration_seconds'], 'diagnostic_review': 'PENDING_DIRECT_REVIEW'})
    (OUT / 'CONTROL-RUNS.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
