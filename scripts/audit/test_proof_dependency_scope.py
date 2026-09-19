"""Deterministic evidence-checker controls; no test asserts a mathematical theorem."""
from __future__ import annotations
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import proof_claim_ids as ids
import mark_proof_run_indexed as mark
import verify_formal_proof_run as formal
import verify_proof_version_closure as version
from test_proof_evidence_links import historical_fixture, temporary_root, write_copy, json_bytes

ROOT = Path(__file__).resolve().parents[2]

class ClaimIdentityTests(unittest.TestCase):
    def test_legacy_and_numeric_identifiers_share_one_parser(self):
        for value in ["C-05", "C-261–C-262", "CAND-F2-7-REAL-LAYER", "C-01, CAND-X-2"]:
            self.assertEqual(ids.expand_claim_ids(value), version.expand_claim_ids(value))
            self.assertEqual(ids.expand_claim_ids(value), mark.expand_claim_ids(value))

    def test_malformed_and_duplicate_identifiers_rejected(self):
        for bad in ["", "CAND-", "CAND-X/../../A", "C-4–C-2", "C-2, C-2", "CAND-X, CAND-X", "CAND-A–CAND-Z"]:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                ids.expand_claim_ids(bad)

    def test_duplicate_legacy_rows_remain_detectable(self):
        data=b"| CAND-X | a |\n| CAND-X | b |\n"
        with self.assertRaisesRegex(version.ClosureError,"MATRIX_IDENTITY_NOT_UNIQUE"):
            version.unique_matrix_line(version.matrix_identity_lines(data),"CAND-X")

class AgdaOptionTests(unittest.TestCase):
    def test_real_flags_and_primed_identifiers(self):
        text="{-# OPTIONS --safe --cubical #-}\nmodule A where\nx' = 1\n"
        self.assertEqual(formal.agda_options(text),["--safe","--cubical"])

    def test_strings_cannot_supply_flags(self):
        for text in ['x = "{-# OPTIONS --safe --cubical #-}"',
                     'x = "escaped \\" {-# OPTIONS --safe #-}"',
                     "{- nested {- {-# OPTIONS --safe #-} -} -}\n-- {-# OPTIONS --safe #-}\nx = \"--safe\""]:
            self.assertNotIn("--safe",formal.agda_options(text))

    def test_literal_then_real_pragma_and_characters(self):
        self.assertEqual(formal.agda_options('x = "fake"\n{-# OPTIONS --safe #-}'),["--safe"])
        self.assertEqual(formal.agda_options("x = '\"'\n{-# OPTIONS --safe #-}"),["--safe"])

    def test_actual_unsafe_control_has_no_safe_option(self):
        p=ROOT/"HoTT/formal/astra-breakpoint-check/StringPragmaControl.agda"
        self.assertNotIn("--safe",formal.agda_options(p.read_text()))

class DependencyCoverageTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix="hott-dependency-scope-")
        self.root=Path(self.temp.name);self.project=self.root/"project";self.tree=self.root/"library"
        self.project.mkdir();self.tree.mkdir()
        self.local="HoTT/formal/example/Main.agda"
        (self.project/self.local).parent.mkdir(parents=True);(self.project/self.local).write_text("module Main where\n")
        (self.tree/"Cubical").mkdir();self.module=self.tree/"Cubical/Base.agda";self.module.write_text("module Cubical.Base where\n")
        self.row={"label":"cubical-extracted-tree","local_path":str(self.tree),**formal.deterministic_tree(self.tree)}
        self.manifest={"external_dependencies":[self.row]}
        self.receipt={"proof_id":"MP-TEST","run_id":"R-TEST","cwd":str(self.project),"source_manifest":{"sha256":"manifest"},"stdout":{"sha256":"stdout"}}

    def tearDown(self):self.temp.cleanup()

    def call(self,stdout,manifest=None,paths=None,gaps=None):
        return version.observed_dependency_coverage(stdout,self.receipt,manifest if manifest is not None else self.manifest,paths if paths is not None else [self.local],gaps or {})

    def test_pinned_external_tree_and_exact_local_path(self):
        r=self.call(f"Checking Main ({self.project/self.local}).\n Checking Cubical.Base ({self.module}).\n")
        self.assertEqual((r["local_modules"],r["external_modules"],r["dependency_gaps"]),(1,1,0))

    def test_missing_local_module_same_basename_is_not_accepted(self):
        other=self.project/"HoTT/formal/other/Main.agda"
        with self.assertRaisesRegex(version.ClosureError,"LATER_DEPENDENCY_GAP_NOT_ALLOWLISTED"):
            self.call(f"Checking Main ({other}).")

    def test_changed_external_bytes_rejected(self):
        self.module.write_text("module Cubical.Base where\n-- changed\n")
        with self.assertRaisesRegex(version.ClosureError,"EXTERNAL_TREE_MISMATCH"):
            self.call(f"Checking Cubical.Base ({self.module}).")

    def test_unpinned_external_path_rejected(self):
        with self.assertRaisesRegex(version.ClosureError,"CHECKED_MODULE_NOT_PINNED"):
            self.call(f"Checking Foreign ({self.root/'unlisted.agda'}).")

    def test_symlink_and_path_traversal_rejected(self):
        link=self.tree/"Alias.agda";link.symlink_to(self.module)
        with self.assertRaisesRegex(version.ClosureError,"EXTERNAL_MODULE_SYMLINK"):
            self.call(f"Checking Alias ({link}).")
        with self.assertRaisesRegex(version.ClosureError,"CHECKED_MODULE_PATH_TRAVERSAL"):
            self.call(f"Checking Other ({self.project/'../library/Cubical/Base.agda'}).")

    def test_conflicting_paths_for_one_module_rejected(self):
        with self.assertRaisesRegex(version.ClosureError,"CHECKED_MODULE_PATH_CONFLICT"):
            self.call(f"Checking X ({self.module}).\nChecking X ({self.tree/'Other.agda'}).")

    def test_exact_historical_gap_cannot_transfer(self):
        rel="HoTT/formal/missing/Local.agda";key=("MP-TEST","R-TEST","Local")
        gap={key:{"missing_path":rel,"source_manifest_sha256":"manifest","stdout_sha256":"stdout"}}
        output=f"Checking Local ({self.project/rel})."
        self.assertEqual(self.call(output,gaps=gap)["dependency_gaps"],1)
        self.receipt["run_id"]="R-NEW"
        with self.assertRaisesRegex(version.ClosureError,"LATER_DEPENDENCY_GAP_NOT_ALLOWLISTED"):
            self.call(output,gaps=gap)

class ExplicitScopeTests(unittest.TestCase):
    def run_cli(self,*args):
        return subprocess.run([sys.executable,str(ROOT/"scripts/audit/verify_proof_version_closure.py"),*args],cwd=ROOT,capture_output=True,text=True)

    def test_one_selected_package_is_not_global_or_version_pass(self):
        r=self.run_cli("--evidence-only","--proof-id","MP-ASTRA-RESTORE-CRITERION-001")
        self.assertEqual(r.returncode,0,r.stdout+r.stderr);d=json.loads(r.stdout)
        self.assertEqual(d["selected_claim_ids"],["C-261","C-262"])
        self.assertEqual(d["git_version_closure"],"NOT_CLAIMED")
        self.assertEqual(d["scope"],"EXPLICIT_PROOF_SELECTION")
        self.assertEqual(d["theory_option_qualification"],"SEPARATE_VERIFY_FORMAL_PROOF_RUN_REQUIRED")
        self.assertGreater(len(d["excluded_proof_ids"]),0)
        self.assertEqual(d["later_evidence"]["packages"],1)

    def test_unknown_or_duplicate_scope_rejected(self):
        for args,code in [(('--proof-id','MP-NO-SUCH-PROOF'),'PROOF_SELECTION_UNKNOWN'),
                          (('--proof-id','MP-ASTRA-PATH-001','--proof-id','MP-ASTRA-PATH-001'),'PROOF_SELECTION_DUPLICATE')]:
            r=self.run_cli('--evidence-only',*args)
            self.assertNotEqual(r.returncode,0);self.assertIn(code,r.stdout)

    def test_evidence_mode_cannot_claim_release_tag(self):
        r=self.run_cli('--evidence-only','--require-tag')
        self.assertNotEqual(r.returncode,0)

    def test_selected_source_drift_is_not_hidden_by_local_mode(self):
        with tempfile.TemporaryDirectory(prefix='hott-selected-drift-') as td:
            root=temporary_root(td)
            rel='HoTT/formal/astra-breakpoint-check/PointRestoration.agda'
            write_copy(root,rel,(ROOT/rel).read_bytes()+b'\n-- changed fixture\n')
            r=self.run_cli('--project-root',str(root),'--evidence-only','--proof-id','MP-ASTRA-RESTORE-CRITERION-001')
            self.assertNotEqual(r.returncode,0)
            self.assertIn('LATER_SOURCE_HASH_DRIFT',r.stdout)

    def test_version_mode_rejects_consistent_but_uncommitted_run_bytes(self):
        with tempfile.TemporaryDirectory(prefix='hott-version-drift-') as td:
            root=historical_fixture(td)
            registry=json.loads((root/'HoTT/verification/PROOF_VERSION_CLOSURE.json').read_text())
            package=next(x for x in registry['later_packages'] if x['proof_id']=='MP-ERCF3-T3-CODING-IMAGE-001')
            rel=package['run'];data=(root/rel/'stdout.txt').read_bytes()+b'\n'
            write_copy(root,rel+'/stdout.txt',data)
            receipt=json.loads((root/rel/'RUN.json').read_text())
            receipt['stdout']['bytes']=len(data);receipt['stdout']['sha256']=formal.sha(data)
            write_copy(root,rel+'/RUN.json',json_bytes(receipt))
            local=self.run_cli('--project-root',str(root),'--evidence-only','--proof-id',package['proof_id'])
            self.assertEqual(local.returncode,0,local.stdout+local.stderr)
            versioned=self.run_cli('--project-root',str(root),'--proof-id',package['proof_id'])
            self.assertNotEqual(versioned.returncode,0)
            self.assertIn('WORKING_FILE_NOT_VERSION_CLOSED',versioned.stdout)

if __name__=='__main__':unittest.main()
