#!/usr/bin/env python3
"""Launcher: ``python3 machine-overview/mo.py <command>`` from the repo root."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from machine_overview.cli import main  # noqa: E402

raise SystemExit(main())
