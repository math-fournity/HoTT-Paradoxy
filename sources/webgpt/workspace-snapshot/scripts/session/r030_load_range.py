#!/usr/bin/env python3
"""Emit consecutive full-text pages via the saved reader; no summaries."""
from pathlib import Path
import argparse, subprocess, sys
ROOT=Path(__file__).resolve().parents[2]
a=argparse.ArgumentParser();a.add_argument('first',type=int);a.add_argument('last',type=int);x=a.parse_args()
for i in range(x.first,x.last+1):
 r=subprocess.run([sys.executable,'-B',str(ROOT/'scripts/session/r030_context.py'),'read','--page',str(i)],cwd=ROOT)
 if r.returncode:raise SystemExit(r.returncode)
