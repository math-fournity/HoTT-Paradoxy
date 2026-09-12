"""Tests of the read-only closure reader. No model-behavior or math certification."""
from pathlib import Path
import hashlib
import runpy
import tempfile
import unittest

SKILL_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = SKILL_ROOT.parents[2]
READER = runpy.run_path(str(SKILL_ROOT / "scripts/read_cognitive_closure.py"),
                       run_name="hott_closure_reader")
read_chunk = READER["read_chunk"]
infer_root = READER["infer_project_root"]
ReadError = READER["ClosureReadError"]
REL = READER["CLOSURE_RELATIVE_PATH"]
ACTUAL = PROJECT_ROOT / REL

class FullClosureLoadingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="closure-loading-test-")
        self.root = Path(self.temp.name)
        self.path = self.root / REL
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.raw = ACTUAL.read_bytes()
        self.path.write_bytes(self.raw)

    def tearDown(self):
        self.temp.cleanup()

    def read_all(self):
        start, expected, pieces = 1, None, []
        while True:
            part = read_chunk(self.root, start_line=start, max_bytes=131072,
                              expected_sha256=expected)
            expected = part["file_sha256"]
            pieces.append(part)
            if part["file_eof"]:
                return part, b"".join(p["text"].encode("utf-8") for p in pieces)
            start = part["next_start_line"]

    def test_01_default_path_resolves_from_script(self):
        self.assertEqual(infer_root(), PROJECT_ROOT)
        self.assertEqual(Path(read_chunk()["path"]), ACTUAL)

    def test_02_all_chunks_preserve_every_byte(self):
        start, expected, body, ranges = 1, None, [], []
        while True:
            p = read_chunk(self.root, start_line=start, max_bytes=10000,
                           expected_sha256=expected)
            self.assertEqual(p["start_line"], start)
            expected = p["file_sha256"]
            body.append(p["text"])
            ranges.append((p["start_line"],p["end_line"]))
            if p["file_eof"]:
                self.assertIsNone(p["next_start_line"])
                break
            start = p["next_start_line"]
        self.assertEqual("".join(body).encode("utf-8"), self.raw)
        self.assertEqual(ranges[0][0],1)
        self.assertEqual(ranges[-1][1],len(self.raw.decode("utf-8").splitlines()))
        for a,b in zip(ranges,ranges[1:]):
            self.assertEqual(a[1]+1,b[0])

    def test_03_second_invocation_returns_text_again(self):
        a,b = read_chunk(self.root),read_chunk(self.root)
        self.assertEqual(a["text"],b["text"])
        self.assertEqual(b["start_line"],1)
        self.assertNotEqual(b["text"],"")
        self.assertNotIn("cached_pass",b)

    def test_04_new_invocation_reads_changed_file(self):
        first=read_chunk(self.root)
        self.path.write_bytes(self.raw+b"\nNEW CURRENT CONTENT\n")
        second=read_chunk(self.root)
        self.assertNotEqual(first["file_sha256"],second["file_sha256"])
        self.assertGreater(second["total_lines"],first["total_lines"])

    def test_05_changed_snapshot_rejects_continuation(self):
        first=read_chunk(self.root)
        self.path.write_bytes(self.raw+b"\nCHANGED\n")
        with self.assertRaises(ReadError):
            read_chunk(self.root,start_line=first["next_start_line"],
                       expected_sha256=first["file_sha256"])

    def test_06_continuation_needs_snapshot_identity(self):
        with self.assertRaises(ReadError):
            read_chunk(self.root,start_line=2)

    def test_07_missing_file_fails_closed(self):
        self.path.unlink()
        with self.assertRaisesRegex(ReadError,"BLOCKED_FULL_CLOSURE_LOAD"):
            read_chunk(self.root)

    def test_08_wrong_closure_id_is_rejected(self):
        self.path.write_text("# Not the selected closure\n",encoding="utf-8")
        with self.assertRaisesRegex(ReadError,"core generation ID"):
            read_chunk(self.root)

    def test_09_oversized_line_is_not_sliced(self):
        with self.assertRaisesRegex(ReadError,"will not be truncated"):
            read_chunk(self.root,max_bytes=1)

    def test_10_invalid_utf8_does_not_get_replaced(self):
        self.path.write_bytes(b"\xff"+self.raw)
        with self.assertRaisesRegex(ReadError,"UTF-8"):
            read_chunk(self.root)

    def test_11_eof_is_not_model_context_certificate(self):
        p, body=self.read_all()
        self.assertTrue(p["file_eof"])
        self.assertEqual(p["model_context_completeness"],"NOT_CERTIFIED_BY_READER")
        self.assertEqual(body,self.raw)

    def test_12_file_growth_uses_current_eof_not_historical_line_floor(self):
        original_lines=len(self.raw.decode("utf-8").splitlines())
        self.path.write_bytes(self.raw+b"\nAFTER THE OLD END\n")
        p, body=self.read_all()
        self.assertTrue(p["file_eof"])
        self.assertIn("AFTER THE OLD END",body.decode("utf-8"))
        self.assertGreater(p["end_line"],original_lines)

    def test_13_invalid_start_range_is_rejected(self):
        for n in (0,-1):
            with self.assertRaises(ReadError):
                read_chunk(self.root,start_line=n)
        with self.assertRaises(ReadError):
            read_chunk(self.root,start_line=99999,
                       expected_sha256=hashlib.sha256(self.raw).hexdigest())

    def test_14_symlink_is_rejected(self):
        copy=self.root/"alternate.md"
        copy.write_bytes(self.raw)
        self.path.unlink()
        self.path.symlink_to(copy)
        with self.assertRaisesRegex(ReadError,"symlink"):
            read_chunk(self.root)

    def test_15_unexpected_script_location_rejected(self):
        with self.assertRaises(ReadError):
            infer_root(self.root/"not-the-skill"/"reader.py")

    def test_16_main_gate_precedes_research(self):
        text=(SKILL_ROOT/"SKILL.md").read_text(encoding="utf-8")
        self.assertLess(text.index("## -1."),text.index("## 0."))
        for term in ("FULL_TRIO_PLUS_RESEARCH_PROFILE_AND_EXPLICIT_TASK_HYDRATION",REL,"上下文压缩",
                     "第1行","BLOCKED_FULL_TRIO_COGNITION","当前模型上下文"):
            self.assertIn(term,text)
        self.assertNotIn("再核最新第五闭包 §7/§14/§19",text)
        self.assertNotIn("已读且未变化的来源可复用可回查记录，不每轮重新阅读全文",text)

    def test_17_recovery_documents_have_no_skip_exemption(self):
        paths=[
            SKILL_ROOT/"references/execution-playbook.md",
            SKILL_ROOT/"references/project-context.md",
            SKILL_ROOT/"templates/resume.md",
            SKILL_ROOT/"templates/closure.md",
        ]
        for p in paths:
            text=p.read_text(encoding="utf-8")
            self.assertIn("全文",text)
            self.assertIn("每次",text)
            self.assertTrue("压缩" in text or "§-1" in text)

if __name__ == "__main__":
    unittest.main(verbosity=2)
