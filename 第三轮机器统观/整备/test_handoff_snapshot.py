"""Bounded evidence handoff tests; fixtures do not certify research semantics."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import handoff_snapshot as h


class SnapshotTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / "源.md").write_text("真实fixture字节\n")
        self.paths = self.root / "paths.txt"
        self.paths.write_text("源.md\n")
        self.out = self.root / "out"
        self.identity = patch.object(h, "git_identity", return_value={"root": str(self.root), "head": "fixture", "branch": "fixture"})
        self.identity.start()
        self.addCleanup(self.identity.stop)

    def create(self):
        return h.seal(self.root, self.paths, self.out)

    def test_roundtrip_and_copy(self):
        import shutil
        receipt = self.create()
        self.assertEqual(h.verify(self.out, receipt["manifest_sha256"])["file_count"], 1)
        shutil.copytree(self.out, self.root / "audit-copy")
        self.assertEqual(h.verify(self.root / "audit-copy")["status"], "VERIFIED_BYTES_ONLY")

    def test_modified_member_rejected(self):
        self.create()
        (self.out / "files/源.md").write_text("篡改")
        with self.assertRaisesRegex(ValueError, "FILE_HASH_MISMATCH"):
            h.verify(self.out)

    def test_missing_and_extra_members_rejected(self):
        self.create()
        (self.out / "extra.txt").write_text("extra")
        with self.assertRaisesRegex(ValueError, "UNLISTED"):
            h.verify(self.out)
        (self.out / "extra.txt").unlink()
        (self.out / "files/源.md").unlink()
        with self.assertRaisesRegex(ValueError, "FILE_MISSING"):
            h.verify(self.out)

    def test_live_drift_does_not_change_frozen_subject(self):
        self.create()
        (self.root / "源.md").write_text("later")
        self.assertEqual(h.verify(self.out)["status"], "VERIFIED_BYTES_ONLY")
        with self.assertRaisesRegex(ValueError, "LIVE_SOURCE_DRIFT"):
            h.verify(self.out, live_root=self.root)

    def test_anchor_and_seal_required(self):
        self.create()
        with self.assertRaisesRegex(ValueError, "MANIFEST_HASH_MISMATCH"):
            h.verify(self.out, "0" * 64)
        (self.out / "SEAL.json").unlink()
        with self.assertRaisesRegex(ValueError, "FILE_MISSING"):
            h.verify(self.out)

    def test_path_and_symlink_rejection(self):
        for name in ["../x", "/tmp/x", "a/./b", ".git/config", "private-audit/x"]:
            with self.assertRaises(ValueError):
                h.safe_relative(name)
        (self.root / "alias").symlink_to(self.root / "源.md")
        self.paths.write_text("alias\n")
        with self.assertRaisesRegex(ValueError, "SYMLINK"):
            self.create()

    def test_no_overwrite_and_duplicates(self):
        self.create()
        with self.assertRaisesRegex(ValueError, "OUTPUT_ALREADY_EXISTS"):
            self.create()
        self.paths.write_text("源.md\n源.md\n")
        with self.assertRaisesRegex(ValueError, "DUPLICATE"):
            h.seal(self.root, self.paths, self.root / "other")

    def test_identity_change_aborts_publication(self):
        self.identity.stop()
        with patch.object(h, "git_identity", side_effect=[{"head": "a"}, {"head": "b"}]):
            with self.assertRaisesRegex(ValueError, "IDENTITY_CHANGED"):
                self.create()
        self.assertFalse(self.out.exists())


if __name__ == "__main__":
    unittest.main()
