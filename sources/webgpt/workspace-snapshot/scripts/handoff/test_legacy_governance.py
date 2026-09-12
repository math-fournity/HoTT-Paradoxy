#!/usr/bin/env python3
"""Run inherited mechanical governance tests via a scripts/ entrypoint; no math certification."""
from pathlib import Path
import importlib.util, sys, unittest
ROOT=Path(__file__).resolve().parents[2]
suite=unittest.TestSuite()
for n in ['test_cognition_runtime','test_full_closure_loading']:
 p=ROOT/'.codex/skills/hott-paradox-research/checks'/(n+'.py')
 spec=importlib.util.spec_from_file_location('handoff_'+n,p);m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
 suite.addTests(unittest.defaultTestLoader.loadTestsFromModule(m))
r=unittest.TextTestRunner(verbosity=2).run(suite)
raise SystemExit(0 if r.wasSuccessful() else 1)
