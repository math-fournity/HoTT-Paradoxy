from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


import capture_agda_proof_run as capture


def git(path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(path), *args],
        capture_output=True,
        text=True,
        check=True,
    )


class ProjectGitRootQualificationTest(unittest.TestCase):
    def test_primary_checkout_and_linked_worktree_are_both_exact_roots(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            primary = base / "primary"
            linked = base / "linked"
            primary.mkdir()
            git(primary, "init", "-q")
            git(primary, "config", "user.name", "Machine Overview Test")
            git(primary, "config", "user.email", "machine-overview@example.invalid")
            (primary / "tracked.txt").write_text("baseline\n", encoding="utf-8")
            git(primary, "add", "--", "tracked.txt")
            git(primary, "commit", "-q", "-m", "baseline")
            git(primary, "worktree", "add", "-q", "-b", "linked-test", str(linked))

            primary_identity = capture.qualify_project_git_root(primary)
            linked_identity = capture.qualify_project_git_root(linked)

            self.assertFalse(primary_identity["linked_worktree"])
            self.assertTrue(linked_identity["linked_worktree"])
            self.assertEqual(primary_identity["git_common_dir"], primary_identity["git_dir"])
            self.assertNotEqual(linked_identity["git_common_dir"], linked_identity["git_dir"])
            self.assertEqual(linked_identity["branch"], "linked-test")
            self.assertEqual(primary_identity["head"], linked_identity["head"])

    def test_subdirectory_and_non_repository_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            repo = base / "repo"
            child = repo / "child"
            repo.mkdir()
            child.mkdir()
            git(repo, "init", "-q")
            with self.assertRaisesRegex(capture.CaptureError, "PROJECT_GIT_ROOT_REQUIRED"):
                capture.qualify_project_git_root(child)
            with self.assertRaisesRegex(capture.CaptureError, "PROJECT_GIT_ROOT_REQUIRED"):
                capture.qualify_project_git_root(base)

    def test_include_directories_are_repository_relative_unique_and_existing(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source_parent = Path("formal/current")
            (root / source_parent).mkdir(parents=True)
            (root / "formal/dependency").mkdir(parents=True)
            result = capture.qualify_include_dirs(
                root,
                source_parent,
                ["formal/dependency", "formal/current", "formal/dependency"],
            )
            self.assertEqual(
                result,
                [Path("formal/current"), Path("formal/dependency")],
            )

    def test_include_directories_reject_missing_file_symlink_and_unsafe_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source_parent = Path("formal/current")
            (root / source_parent).mkdir(parents=True)
            (root / "formal/file").write_text("not a directory\n", encoding="utf-8")
            (root / "formal/link").symlink_to(root / source_parent, target_is_directory=True)
            for value in (
                "formal/missing",
                "formal/file",
                "formal/link",
            ):
                with self.subTest(value=value), self.assertRaisesRegex(
                    capture.CaptureError, "INCLUDE_DIR_MISSING_OR_SYMLINK"
                ):
                    capture.qualify_include_dirs(root, source_parent, [value])
            with self.assertRaisesRegex(capture.CaptureError, "UNSAFE_RELATIVE_PATH"):
                capture.qualify_include_dirs(root, source_parent, ["../outside"])


if __name__ == "__main__":
    unittest.main()
