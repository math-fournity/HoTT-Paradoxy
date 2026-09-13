#!/usr/bin/env python3
"""Mechanical tests for layered loading and atomic checkpoint/recovery.

All mutations and fault injection occur in temporary repositories.  These
tests certify no model comprehension and no mathematical claim.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/cognition_runtime.py"
SPEC = importlib.util.spec_from_file_location("cognition_under_test", SCRIPT)
assert SPEC and SPEC.loader
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)


class RuntimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="hott-cognition-v3-")
        self.root = Path(self.temp.name)
        self.query_first = ["核心认知.manifest.json", "sources/SOURCE_MANIFEST.json"]
        self.task_expand = ["理解章节/README.md", "HoTT/CLAIM_EVIDENCE_MATRIX.md"]
        self.archive = ["audit/old-receipt.json", ".codex/tools/cognition_runtime.py"]
        paths = set(C.THREE_WAY) | set(C.REQUIRED_BOOT) | set(C.REQUIRED_RESEARCH)
        paths |= set(self.query_first) | set(self.task_expand) | set(self.archive)
        for rel in paths:
            self.put(rel, "TEST FIXTURE ONLY\n" + rel + "\n")
        self.put(C.SKILL, "---\nname: hott-paradox-research\n---\nBusiness fixture.\n")
        self.put(C.GOVERNANCE_SKILL, "---\nname: hott-local-session-governance\n---\nGovernance fixture.\n")
        self.put(C.ROLES, C.dump({
            "schema_version": "hott-skill-roles/v2",
            "roles": {
                "business": {"name": "hott-paradox-research", "path": C.SKILL},
                "governance": {"name": "hott-local-session-governance", "path": C.GOVERNANCE_SKILL}
            }
        }))
        self.put(C.CLOSURE, "# TEST FIXTURE ONLY\ncore-cognition-generation-3\n甲\n乙\n")
        self.put(C.DIRECTION, "<!-- integrated-direction-portfolio:v1\nsource_state_revision: 1\n-->\n")
        self.put(C.PANORAMA, "<!-- integrated-outcome-panorama:v1\nsource_state_revision: 1\n-->\n")
        self.config = {
            "schema_version": "cognition-load-set/v3",
            "always_full_three_way": list(C.THREE_WAY),
            "always_full_boot": list(C.REQUIRED_BOOT),
            "research_full": list(C.REQUIRED_RESEARCH),
            "query_first": self.query_first,
            "task_expand": self.task_expand,
            "archive_verify_only": self.archive,
            "dynamic_state": C.STATE,
            "three_way_order": list(C.THREE_WAY)
        }
        self.put(C.CONFIG, C.dump(self.config))
        state = {
            "schema_version": "hott-working-state/v2",
            "revision": 1,
            "current_core": {"generation": "core-cognition-generation-3", "kc_count": 2},
            "latest_session": "S0",
            "active": [],
            "review_due": [],
            "unresolved": [],
            "records": {
                "S0": {
                    "kind": "session",
                    "path": C.PREFIX + "sessions/S0/SESSION.md",
                    "status": "complete",
                    "lifecycle_status": "HISTORICAL",
                    "evidence_status": "VERIFIED_WITH_SCOPE",
                    "depends_on": [],
                    "full_sources": [],
                    "source_hashes": {}
                }
            }
        }
        self.put(C.PREFIX + "sessions/S0/SESSION.md", "# Test S0\nHistorical fixture.\n")
        self.set_state(state)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def put(self, rel: str, data: bytes | str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data if isinstance(data, bytes) else data.encode("utf-8"))

    def state(self) -> dict:
        return C.obj((self.root / C.STATE).read_bytes())

    def set_state(self, state: dict) -> None:
        self.put(C.STATE, C.dump(state))
        self.refresh_head()

    def refresh_head(self) -> None:
        state = self.state()
        self.put(C.HEAD, C.dump({
            "schema_version": "cognition-head/v1",
            "revision": state["revision"],
            "latest_session": state["latest_session"],
            "tracked": {rel: C.sha((self.root / rel).read_bytes()) for rel in C.MUTABLE}
        }))

    def plan(self, profile: str = "governance", task_ids=()):
        return C.plan(self.root, profile=profile, task_ids=task_ids)

    def all_hashes(self) -> dict[str, str]:
        return {p.relative_to(self.root).as_posix(): C.sha(p.read_bytes()) for p in self.root.rglob("*") if p.is_file()}

    def add_record(self, key="QX", *, lifecycle="OPEN_ISSUE", evidence="REVIEW_REQUIRED", status="review_required",
                   full_sources=None, depends_on=None) -> str:
        state = self.state()
        path = C.PREFIX + f"candidates/{key}/record.md"
        self.put(path, f"# Record {key}\nDirect fixture evidence.\n")
        state["records"][key] = {
            "kind": "candidate",
            "path": path,
            "status": status,
            "lifecycle_status": lifecycle,
            "evidence_status": evidence,
            "depends_on": list(depends_on or []),
            "full_sources": list(full_sources or []),
            "source_hashes": {}
        }
        self.set_state(state)
        return path

    def payload(self, sid="S1", *, add_candidate=False, profile="governance", task_ids=None) -> dict:
        state = self.state()
        state["revision"] += 1
        state["latest_session"] = sid
        session = C.PREFIX + f"sessions/{sid}/SESSION.md"
        state["records"][sid] = {
            "kind": "session",
            "path": session,
            "status": "complete",
            "lifecycle_status": "HISTORICAL",
            "evidence_status": "VERIFIED_WITH_SCOPE",
            "depends_on": [],
            "full_sources": [],
            "source_hashes": {}
        }
        audit = C.PREFIX + f"sessions/{sid}/CORE_COGNITION_AUDIT.md"
        runs = C.PREFIX + f"sessions/{sid}/RUNS.json"
        audit_rows = [
            f"| `KC-{n:06d}` | fixture | `NOT_TOUCHED` | Fixture assessment. | {session} | none |"
            for n in range(1, 3)
        ]
        audit_text = (
            f"# Core audit {sid}\n\n"
            "generation: core-cognition-generation-3\n\n"
            "| KC | label | relation | assessment | evidence | unresolved |\n"
            "|---|---|---|---|---|---|\n" + "\n".join(audit_rows) + "\n\n"
            "- core_change: NO\n- direction_change: NO\n- panorama_change: NO\n"
            "- update_decision: fixture\n- cross_conflicts: none\n- unresolved: none\n"
        )
        extra = {
            session: f"# Test {sid}\nEvidence and next action.\n",
            audit: audit_text,
            runs: C.dump({"schema_version": "hott-session-runs/v2", "session_id": sid}).decode("utf-8"),
        }
        if add_candidate:
            candidate = C.PREFIX + "candidates/C1/candidate.md"
            extra[candidate] = "# Candidate C1\nNew evidence.\n"
            state["records"]["C1"] = {
                "kind": "candidate", "path": candidate, "status": "open",
                "lifecycle_status": "OPEN_ISSUE", "evidence_status": "UNREVIEWED",
                "depends_on": [], "full_sources": [], "source_hashes": {}
            }
            state["active"] = ["C1"]
        texts = {rel: (self.root / rel).read_text(encoding="utf-8") for rel in C.MUTABLE}
        texts["MEMORY.md"] += f"# New state {sid}\n"
        texts[C.STATE] = C.dump(state).decode("utf-8")
        texts.update(extra)
        return {
            "schema_version": "cognition-checkpoint/v1",
            "session_id": sid,
            "authorization": "Authorized temporary fixture writes only",
            "load_profile": profile,
            "task_ids": list(task_ids or []),
            "files": [
                {
                    "path": rel,
                    "expected_sha256": C.sha((self.root / rel).read_bytes()) if (self.root / rel).exists() else None,
                    "text": value
                }
                for rel, value in texts.items()
            ]
        }

    def payload_state(self, payload: dict) -> dict:
        row = next(item for item in payload["files"] if item["path"] == C.STATE)
        return C.obj(row["text"].encode("utf-8"))

    def replace_payload_state(self, payload: dict, state: dict) -> None:
        next(item for item in payload["files"] if item["path"] == C.STATE)["text"] = C.dump(state).decode("utf-8")

    def fault(self, sid="S1", after=2) -> None:
        current = self.plan()
        with self.assertRaisesRegex(C.CognitionError, "INJECTED_INTERRUPTION"):
            C.checkpoint(self.root, current["snapshot"], self.payload(sid), apply=True, _fail_after=after)

    def test_governance_plan_has_trio_first_and_no_cold_assets(self) -> None:
        plan = self.plan()
        paths = [row["path"] for row in plan["documents"]]
        self.assertEqual(paths[:3], list(C.THREE_WAY))
        self.assertTrue(set(C.REQUIRED_BOOT) <= set(paths))
        self.assertFalse(set(C.REQUIRED_RESEARCH) & set(paths))
        self.assertFalse(set(self.query_first + self.archive) & set(paths))
        self.assertEqual(plan["automatically_included_historical_sessions"], [])
        self.assertEqual(plan["model_context"], "NOT_CERTIFIED_BY_TOOL")

    def test_research_profile_adds_only_research_layer(self) -> None:
        governance = self.plan()
        research = self.plan("research")
        g = {row["path"] for row in governance["documents"]}
        r = {row["path"] for row in research["documents"]}
        self.assertEqual(r - g, set(C.REQUIRED_RESEARCH))
        self.assertNotEqual(governance["snapshot"], research["snapshot"])

    def test_complete_chunk_coverage(self) -> None:
        plan = self.plan()
        chunks = []
        for row in plan["documents"]:
            line = 1
            while line:
                chunk = C.read_chunk(self.root, plan["snapshot"], row["path"], line, 1000)
                chunks.append(chunk)
                line = chunk["next_start_line"]
        self.assertEqual(C.check_coverage(plan, chunks)["status"], "FULL_EMITTED_BYTES_MATCH")

    def test_partial_and_out_of_order_coverage_rejected(self) -> None:
        plan = self.plan()
        one = C.read_chunk(self.root, plan["snapshot"], C.CLOSURE, 1, 1000)
        with self.assertRaisesRegex(C.CognitionError, "COVERAGE_INCOMPLETE"):
            C.check_coverage(plan, [one])
        two = C.read_chunk(self.root, plan["snapshot"], C.CLOSURE, 2, 1000)
        with self.assertRaisesRegex(C.CognitionError, "COVERAGE_GAP"):
            C.check_coverage(plan, [two])

    def test_long_line_is_not_truncated(self) -> None:
        self.put(C.CLOSURE, "core-cognition-generation-3\n" + "中" * 2000 + "\n")
        plan = self.plan()
        with self.assertRaisesRegex(C.CognitionError, "LINE_TOO_LARGE"):
            C.read_chunk(self.root, plan["snapshot"], C.CLOSURE, 2, 100)

    def read_all_chunks(self, plan: dict) -> list:
        chunks = []
        for row in plan["documents"]:
            line = 1
            while line:
                chunk = C.read_chunk(self.root, plan["snapshot"], row["path"], line, 1000)
                chunks.append(chunk)
                line = chunk["next_start_line"]
        return chunks

    def make_sharded(self, rel: str, shards, *, mode: str = "topical", logical_id: str = "LD",
                     last_shard=None, append_target=None, marker: str = "<!-- governance-shard-index:v2",
                     title_override=None) -> list:
        """Write a v2 shard index plus its shards; return the ordered shard paths."""
        stem = C.PurePosixPath(rel).stem
        rows = []
        for shard_id, title in shards:
            path = f"{stem}/{shard_id} - {title}.md"
            heading = title if title_override is None else title_override
            self.put(
                path,
                f"<!-- governance-shard:v2\nlogical_id: {logical_id}\nshard_id: {shard_id}\n"
                f"index: ../{stem}.md\n-->\n\n# {heading}\n\nbody {shard_id}\n",
            )
            rows.append((shard_id, title, path))
        table = "\n".join(
            f"| {shard_id} | [{title}](<{path}>) | scope | current |" for shard_id, title, path in rows
        )
        meta_last = last_shard if last_shard is not None else rows[-1][2]
        meta_append = append_target if append_target is not None else ("-" if mode == "topical" else meta_last)
        self.put(
            rel,
            f"{marker}\nlogical_id: {logical_id}\nmode: {mode}\nshard_root: {stem}\n"
            f"last_shard: {meta_last}\nappend_target: {meta_append}\nsoft_line_target: 300\n-->\n\n"
            "# fixture index\n\n<!-- governance-shard-table:start -->\n"
            "| Shard | 文件 | 语义范围 | 状态 |\n|---|---|---|---|\n"
            f"{table}\n<!-- governance-shard-table:end -->\n",
        )
        return [path for _, _, path in rows]

    def test_shard_index_expands_to_ordered_shards(self) -> None:
        index = "README.md"
        shards = self.make_sharded(
            index, [("001", "第一片"), ("002", "第二片")], logical_id="README"
        )
        plan = self.plan()
        paths = [row["path"] for row in plan["documents"]]
        start = paths.index(index)
        self.assertEqual(paths[start:start + 3], [index] + shards)
        rows = {row["path"]: row for row in plan["documents"]}
        self.assertEqual(rows[index]["logical_role"], "index")
        self.assertEqual(rows[shards[0]]["logical_role"], "shard")
        self.assertTrue(rows[shards[1]]["full_load"])
        self.assertEqual(plan["logical_documents"][0]["logical_id"], "README")
        self.assertEqual(plan["logical_documents"][0]["shard_count"], 2)
        self.assertTrue(plan["logical_documents"][0]["full_load_required"])

    def test_sharded_document_requires_every_shard(self) -> None:
        shards = self.make_sharded(
            "README.md", [("001", "第一片"), ("002", "第二片")], logical_id="README"
        )
        plan = self.plan()
        chunks = [chunk for chunk in self.read_all_chunks(plan) if chunk["path"] != shards[1]]
        with self.assertRaisesRegex(C.CognitionError, "COVERAGE_INCOMPLETE"):
            C.check_coverage(plan, chunks)
        self.assertEqual(C.check_coverage(plan, self.read_all_chunks(plan))["status"], "FULL_EMITTED_BYTES_MATCH")

    def test_shard_index_structural_failures_are_fail_closed(self) -> None:
        index = "README.md"
        shards = self.make_sharded(index, [("001", "第一片")], logical_id="A")
        self.put(f"{C.PurePosixPath(index).stem}/002 - 未登记片.md", "# 未登记片\n\norphan\n")
        with self.assertRaisesRegex(C.CognitionError, "UNLISTED_SHARD"):
            self.plan()
        (self.root / f"{C.PurePosixPath(index).stem}/002 - 未登记片.md").unlink()
        self.make_sharded(index, [("001", "第一片")], logical_id="A", last_shard="A/999 - 不存在.md")
        with self.assertRaisesRegex(C.CognitionError, "LAST_SHARD_MISMATCH"):
            self.plan()
        self.make_sharded(index, [("001", "第一片")], logical_id="A", mode="sequential",
                          append_target="README/000 - 不存在.md")
        with self.assertRaisesRegex(C.CognitionError, "APPEND_TARGET_MISMATCH"):
            self.plan()
        self.make_sharded(index, [("001", "第一片")], logical_id="A", mode="sequential")
        self.assertEqual(self.plan()["logical_documents"][0]["mode"], "sequential")
        self.make_sharded(index, [("001", "第一片")], logical_id="A", title_override="标题不一致")
        with self.assertRaisesRegex(C.CognitionError, "SHARD_TITLE_MISMATCH"):
            self.plan()
        self.make_sharded(index, [("001", "第一片")], logical_id="A")
        (self.root / shards[0]).unlink()
        with self.assertRaisesRegex(C.CognitionError, "MISSING_OR_UNREADABLE"):
            self.plan()

    def test_mutable_sharded_document_is_head_tracked(self) -> None:
        shards = self.make_sharded(
            "MEMORY.md", [("001", "当前执行队列"), ("002", "顺序日志")],
            mode="sequential", logical_id="MEMORY",
        )
        self.refresh_head()
        plan = self.plan()
        payload = self.payload("S2")
        texts = {row["path"]: row["text"] for row in payload["files"]}
        texts[shards[1]] = (self.root / shards[1]).read_text(encoding="utf-8") + "appended session record\n"
        for shard in shards:
            payload["files"].append({
                "path": shard,
                "expected_sha256": C.sha((self.root / shard).read_bytes()),
                "text": texts.get(shard, (self.root / shard).read_text(encoding="utf-8")),
            })
        _, _, changes, _ = C.prepare(self.root, plan["snapshot"], payload)
        head = C.obj(changes[C.HEAD])
        self.assertTrue(set(shards) <= set(head["tracked"]))
        self.assertTrue(set(C.MUTABLE) <= set(head["tracked"]))

    def test_mutable_shard_must_be_in_checkpoint(self) -> None:
        self.make_sharded(
            "MEMORY.md", [("001", "当前执行队列"), ("002", "顺序日志")],
            mode="sequential", logical_id="MEMORY",
        )
        self.refresh_head()
        plan = self.plan()
        with self.assertRaisesRegex(C.CognitionError, "SHARD_NOT_IN_CHECKPOINT"):
            C.prepare(self.root, plan["snapshot"], self.payload("S2"))

    def test_quoted_marker_in_documentation_is_not_an_index(self) -> None:
        """A contract document that *quotes* the marker must stay a plain document."""
        body = ["# 合同示例\n"] + [f"filler {n}\n" for n in range(30)]
        body += [
            "```markdown\n",
            "<!-- governance-shard-index:v2\n",
            "logical_id: MEMORY\nmode: sequential\nshard_root: MEMORY\n",
            "last_shard: MEMORY/002 - 顺序日志.md\nappend_target: MEMORY/002 - 顺序日志.md\n",
            "soft_line_target: 300\n-->\n",
            "| 001 | [示例](<MEMORY/001 - 示例.md>) | 示例 | current |\n",
            "```\n",
        ]
        self.put("README.md", "".join(body))
        plan = self.plan()
        rows = {row["path"]: row for row in plan["documents"]}
        self.assertIsNone(rows["README.md"]["logical_role"])
        self.assertEqual(plan["logical_documents"], [])

    def test_source_growth_changes_snapshot(self) -> None:
        old = self.plan()
        self.put(C.CLOSURE, (self.root / C.CLOSURE).read_text() + "new tail\n")
        new = self.plan()
        self.assertNotEqual(old["snapshot"], new["snapshot"])
        with self.assertRaisesRegex(C.CognitionError, "STALE_SNAPSHOT"):
            C.read_chunk(self.root, old["snapshot"], C.CLOSURE)

    def test_missing_boot_and_wrong_core_fail_closed(self) -> None:
        (self.root / "README.md").unlink()
        with self.assertRaisesRegex(C.CognitionError, "MISSING"):
            self.plan()
        self.put("README.md", "restored\n")
        self.put(C.CLOSURE, "wrong generation\n")
        with self.assertRaisesRegex(C.CognitionError, "WRONG_CLOSURE"):
            self.plan()

    def test_hash_pinned_core_transition_is_narrowly_accepted(self) -> None:
        body = "# TEST FIXTURE ONLY\ncore-cognition-generation-4\nnew core\n"
        self.put(C.CLOSURE, body)
        self.put("核心认知.manifest.json", C.dump({
            "generation": "core-cognition-generation-4",
            "core_document_sha256": C.sha(body.encode("utf-8")),
        }))
        self.put("transition.json", C.dump({
            "previous": {"generation": "core-cognition-generation-3", "unit_count": 1},
            "current": {"generation": "core-cognition-generation-4", "core_sha256": C.sha(body.encode("utf-8"))},
            "mapping_count": 1,
            "mapping_remainder": 0,
        }))
        transition = {
            "from_generation": "core-cognition-generation-3",
            "to_generation": "core-cognition-generation-4",
            "manifest": "核心认知.manifest.json",
            "transition": "transition.json",
        }
        with self.assertRaisesRegex(C.CognitionError, "WRONG_CLOSURE"):
            self.plan()
        self.assertEqual(
            C.plan(self.root, _allow_core_transition=transition)["revision"],
            1,
        )
        tampered = dict(transition)
        tampered["to_generation"] = "core-cognition-generation-5"
        with self.assertRaisesRegex(C.CognitionError, "CORE_TRANSITION_GENERATION_MISMATCH"):
            C.plan(self.root, _allow_core_transition=tampered)

    def test_trio_reorder_or_removal_rejected(self) -> None:
        altered = copy.deepcopy(self.config)
        altered["always_full_three_way"] = [C.DIRECTION, C.CLOSURE, C.PANORAMA]
        self.put(C.CONFIG, C.dump(altered))
        with self.assertRaisesRegex(C.CognitionError, "THREE_WAY_ORDER"):
            self.plan()

    def test_required_boot_and_research_cannot_be_removed(self) -> None:
        altered = copy.deepcopy(self.config)
        altered["always_full_boot"].remove("MEMORY.md")
        self.put(C.CONFIG, C.dump(altered))
        with self.assertRaisesRegex(C.CognitionError, "REQUIRED_BOOT"):
            self.plan()
        altered = copy.deepcopy(self.config)
        altered["research_full"].remove(C.QUESTIONS)
        self.put(C.CONFIG, C.dump(altered))
        with self.assertRaisesRegex(C.CognitionError, "REQUIRED_RESEARCH"):
            self.plan()

    def test_layer_overlap_rejected(self) -> None:
        altered = copy.deepcopy(self.config)
        altered["query_first"].append(C.CLOSURE)
        self.put(C.CONFIG, C.dump(altered))
        with self.assertRaisesRegex(C.CognitionError, "LOAD_LAYER_OVERLAP"):
            self.plan()

    def test_open_issue_is_visible_but_not_auto_hydrated(self) -> None:
        path = self.add_record()
        plan = self.plan()
        self.assertIn("QX", {row["id"] for row in plan["available_records"]})
        self.assertNotIn(path, [row["path"] for row in plan["documents"]])
        self.assertEqual(plan["hydrated_records"], [])

    def test_evidence_review_does_not_revive_historical_session(self) -> None:
        path = self.add_record("SOLD", lifecycle="HISTORICAL", evidence="REVIEW_REQUIRED")
        plan = self.plan()
        self.assertNotIn(path, [row["path"] for row in plan["documents"]])
        self.assertEqual(plan["automatically_included_historical_sessions"], [])

    def test_explicit_task_hydrates_dependencies_and_full_sources(self) -> None:
        source = "sources/lemma.md"
        self.put(source, "source truth\n")
        parent_path = self.add_record("PARENT", lifecycle="CURRENT", evidence="VERIFIED_WITH_SCOPE")
        child_path = self.add_record("CHILD", lifecycle="OPEN_ISSUE", evidence="REVIEW_REQUIRED",
                                     full_sources=[source], depends_on=["PARENT"])
        plan = self.plan("research", ("CHILD",))
        paths = [row["path"] for row in plan["documents"]]
        self.assertTrue({source, parent_path, child_path} <= set(paths))
        self.assertEqual(set(plan["hydrated_records"]), {"PARENT", "CHILD"})

    def test_related_record_is_visible_but_not_hydrated(self) -> None:
        parent_path = self.add_record("PARENT", lifecycle="CURRENT", evidence="VERIFIED_WITH_SCOPE")
        child_path = self.add_record("CHILD", lifecycle="CURRENT", evidence="VERIFIED_WITH_SCOPE")
        state = self.state()
        state["records"]["CHILD"]["related_records"] = ["PARENT"]
        self.set_state(state)
        plan = self.plan("research", ("CHILD",))
        paths = [row["path"] for row in plan["documents"]]
        self.assertIn(child_path, paths)
        self.assertNotIn(parent_path, paths)
        self.assertEqual(plan["hydrated_records"], ["CHILD"])

    def test_scope_locator_directory_uses_evidence_without_reading_directory(self) -> None:
        evidence = "audit/scope.md"
        self.put(evidence, "scope evidence\n")
        self.add_record("SCOPE", lifecycle="OPEN_ISSUE", evidence="REVIEW_REQUIRED", full_sources=[evidence])
        state = self.state()
        state["records"]["SCOPE"]["path"] = C.PREFIX + "sessions"
        state["records"]["SCOPE"]["path_mode"] = "scope_locator"
        self.set_state(state)
        plan = self.plan("research", ("SCOPE",))
        self.assertIn(evidence, [row["path"] for row in plan["documents"]])
        self.assertNotIn(C.PREFIX + "sessions", [row["path"] for row in plan["documents"]])

    def test_historical_record_can_only_be_loaded_explicitly(self) -> None:
        path = self.add_record("OLD", lifecycle="HISTORICAL", evidence="VERIFIED_WITH_SCOPE", status="complete")
        self.assertNotIn(path, [row["path"] for row in self.plan()["documents"]])
        self.assertIn(path, [row["path"] for row in self.plan(task_ids=("OLD",))["documents"]])

    def test_dependency_cycle_and_stale_hash_rejected_or_reported(self) -> None:
        self.add_record("A", lifecycle="CURRENT", evidence="VERIFIED_WITH_SCOPE")
        self.add_record("B", depends_on=["A"])
        state = self.state()
        state["records"]["A"]["depends_on"] = ["B"]
        self.set_state(state)
        with self.assertRaisesRegex(C.CognitionError, "DEPENDENCY_CYCLE"):
            self.plan(task_ids=("B",))
        state["records"]["A"]["depends_on"] = []
        self.put("sources/hash.md", "old\n")
        state["records"]["A"]["source_hashes"] = {"sources/hash.md": C.sha(b"old\n")}
        self.set_state(state)
        self.put("sources/hash.md", "new\n")
        self.assertEqual(self.plan(task_ids=("A",))["review_required"], ["A"])

    def test_query_returns_metadata_not_file_body(self) -> None:
        path = self.add_record()
        result = C.query_record(self.root, "QX")
        self.assertEqual(result["record"]["path"], path)
        self.assertEqual(result["hydrate_with"]["task_ids"], ["QX"])
        self.assertNotIn("Direct fixture evidence", json.dumps(result))

    def test_invalid_task_and_symlink_and_non_utf8_rejected(self) -> None:
        with self.assertRaisesRegex(C.CognitionError, "TASK_RECORD"):
            self.plan(task_ids=("missing",))
        (self.root / C.CLOSURE).unlink()
        (self.root / C.CLOSURE).symlink_to(self.root / "MEMORY.md")
        with self.assertRaisesRegex(C.CognitionError, "SYMLINK"):
            self.plan()
        (self.root / C.CLOSURE).unlink()
        self.put(C.CLOSURE, b"\xff")
        with self.assertRaisesRegex(C.CognitionError, "NOT_UTF8"):
            self.plan()

    def test_uncommitted_mutable_state_rejected(self) -> None:
        self.put("MEMORY.md", "uncommitted\n")
        with self.assertRaisesRegex(C.CognitionError, "UNCOMMITTED_STATE"):
            self.plan()

    def test_dry_run_zero_writes(self) -> None:
        plan = self.plan(); before = self.all_hashes()
        result = C.checkpoint(self.root, plan["snapshot"], self.payload())
        self.assertEqual(result["status"], "DRY_RUN")
        self.assertEqual(before, self.all_hashes())

    def test_checkpoint_and_new_process_observe_new_session(self) -> None:
        plan = self.plan()
        result = C.checkpoint(self.root, plan["snapshot"], self.payload(), apply=True)
        self.assertEqual(result["status"], "CHECKPOINT_COMMITTED")
        self.assertEqual(self.plan()["latest_session"], "S1")
        child = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--project-root", str(self.root), "plan", "--profile", "research"],
            capture_output=True, text=True, check=True, env={"PYTHONDONTWRITEBYTECODE": "1"}
        )
        self.assertEqual(json.loads(child.stdout)["latest_session"], "S1")

    def test_new_active_candidate_loads_primary_path_not_full_sources(self) -> None:
        plan = self.plan()
        C.checkpoint(self.root, plan["snapshot"], self.payload(add_candidate=True), apply=True)
        new = self.plan()
        paths = [row["path"] for row in new["documents"]]
        self.assertIn(C.PREFIX + "candidates/C1/candidate.md", paths)

    def test_stale_writer_session_immutability_and_old_record_identity(self) -> None:
        plan = self.plan(); first = self.payload("S1"); second = self.payload("S2")
        C.checkpoint(self.root, plan["snapshot"], first, apply=True)
        with self.assertRaisesRegex(C.CognitionError, "STALE_BASE"):
            C.checkpoint(self.root, plan["snapshot"], second, apply=True)
        current = self.plan()
        with self.assertRaisesRegex(C.CognitionError, "SESSION_IMMUTABLE"):
            C.checkpoint(self.root, current["snapshot"], self.payload("S1"))
        payload = self.payload("S2"); state = self.payload_state(payload)
        state["records"]["S0"]["path"] = "elsewhere.md"
        self.replace_payload_state(payload, state)
        with self.assertRaisesRegex(C.CognitionError, "RECORD_IDENTITY_CHANGED"):
            C.checkpoint(self.root, current["snapshot"], payload)

    def test_open_issue_closure_requires_resolution(self) -> None:
        self.add_record()
        plan = self.plan(); payload = self.payload(); state = self.payload_state(payload)
        state["records"]["QX"]["lifecycle_status"] = "CLOSED"
        state["records"]["QX"]["status"] = "closed"
        self.replace_payload_state(payload, state)
        with self.assertRaisesRegex(C.CognitionError, "RESOLUTION_REQUIRED"):
            C.checkpoint(self.root, plan["snapshot"], payload)

    def test_checkpoint_requires_all_state_files_and_blocks_core_write(self) -> None:
        plan = self.plan(); payload = self.payload()
        payload["files"] = [row for row in payload["files"] if row["path"] != "MEMORY.md"]
        with self.assertRaisesRegex(C.CognitionError, "INCOMPLETE_CHECKPOINT_STATE"):
            C.checkpoint(self.root, plan["snapshot"], payload)
        payload = self.payload()
        payload["files"].append({
            "path": C.CLOSURE,
            "text": "changed",
            "expected_sha256": C.sha((self.root / C.CLOSURE).read_bytes())
        })
        with self.assertRaisesRegex(C.CognitionError, "WRITE_OUTSIDE_AUTHORIZED"):
            C.checkpoint(self.root, plan["snapshot"], payload)

    def test_checkpoint_requires_runs_and_full_ordered_kc_audit(self) -> None:
        plan = self.plan(); payload = self.payload()
        payload["files"] = [row for row in payload["files"] if not row["path"].endswith("/RUNS.json")]
        with self.assertRaisesRegex(C.CognitionError, "SESSION_EVIDENCE_REQUIRED: RUNS.json"):
            C.checkpoint(self.root, plan["snapshot"], payload)
        payload = self.payload()
        audit = next(row for row in payload["files"] if row["path"].endswith("/CORE_COGNITION_AUDIT.md"))
        audit["text"] = audit["text"].replace("| `KC-000002`", "| `KC-000001`")
        with self.assertRaisesRegex(C.CognitionError, "KC_AUDIT_COVERAGE_OR_ORDER_INVALID"):
            C.checkpoint(self.root, plan["snapshot"], payload)

    def test_changed_verification_dependency_requires_declared_semantics(self) -> None:
        self.add_record("A", lifecycle="CURRENT", evidence="VERIFIED_WITH_SCOPE")
        self.add_record("B", lifecycle="CURRENT", evidence="VERIFIED_WITH_SCOPE")
        plan = self.plan(); payload = self.payload(); state = self.payload_state(payload)
        state["records"]["B"]["depends_on"] = ["A"]
        self.replace_payload_state(payload, state)
        with self.assertRaisesRegex(C.CognitionError, "DEPENDENCY_SEMANTICS_REQUIRED"):
            C.checkpoint(self.root, plan["snapshot"], payload)
        state["records"]["B"]["dependency_semantics"] = "verification_staleness"
        self.replace_payload_state(payload, state)
        self.assertEqual(C.checkpoint(self.root, plan["snapshot"], payload)["status"], "DRY_RUN")

    def test_interruption_finish_and_rollback(self) -> None:
        self.fault("S1", 2)
        with self.assertRaisesRegex(C.CognitionError, "CHECKPOINT_INCOMPLETE"):
            self.plan()
        self.assertEqual(C.recover(self.root, "finish", confirm_owner_stopped=True)["status"], "RECOVERED_FINISH")
        before = {rel: (self.root / rel).read_bytes() for rel in C.MUTABLE + (C.HEAD,)}
        self.fault("S2", 4)
        self.assertEqual(C.recover(self.root, "rollback", confirm_owner_stopped=True)["status"], "RECOVERED_ROLLBACK")
        for rel, data in before.items():
            self.assertEqual((self.root / rel).read_bytes(), data)

    def test_recovery_requires_confirmation_and_rejects_third_party_write(self) -> None:
        self.fault()
        with self.assertRaisesRegex(C.CognitionError, "EXPLICIT_OWNER_STOP"):
            C.recover(self.root, "finish")
        self.put("MEMORY.md", "third party\n")
        with self.assertRaisesRegex(C.CognitionError, "THIRD_PARTY_WRITE"):
            C.recover(self.root, "finish", confirm_owner_stopped=True)

    def test_state_v1_to_v2_requires_migration_receipt(self) -> None:
        old = self.state()
        old["schema_version"] = "hott-working-state/v1"
        for record in old["records"].values():
            record.pop("lifecycle_status", None); record.pop("evidence_status", None)
        self.set_state(old)
        plan = self.plan(); payload = self.payload(); state = self.payload_state(payload)
        state["schema_version"] = "hott-working-state/v2"
        for key, record in state["records"].items():
            record.setdefault("lifecycle_status", "HISTORICAL" if record["kind"] == "session" else "OPEN_ISSUE")
            record.setdefault("evidence_status", "VERIFIED_WITH_SCOPE")
        self.replace_payload_state(payload, state)
        with self.assertRaisesRegex(C.CognitionError, "MIGRATION_RECEIPT"):
            C.checkpoint(self.root, plan["snapshot"], payload)
        receipt = "audit/state-migration.md"; self.put(receipt, "# migration receipt\n")
        state["schema_migration"] = {
            "from": "hott-working-state/v1", "to": "hott-working-state/v2",
            "rollback_ref": "fixture-tag", "receipt": receipt
        }
        self.replace_payload_state(payload, state)
        self.assertEqual(C.checkpoint(self.root, plan["snapshot"], payload)["status"], "DRY_RUN")


if __name__ == "__main__":
    unittest.main(verbosity=2)
