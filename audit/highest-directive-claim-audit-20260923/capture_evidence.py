"""Capture public test answers and exact visible read ranges via the canonical reader.

Reuse the previous trial's tool-output decoder; do not parse native rollout JSONL.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import shlex
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
READER = "/Users/aurolafly/codex/tools/session_trajectory.py"
BASENAME = "rollout-2026-09-23T12-05-22-01a0cf03-b997-78f2-8480-8684e64f348b.jsonl"
SOURCE = Path("/Users/aurolafly/.codex/sessions/2026/09/23") / BASENAME
if not SOURCE.exists():
    SOURCE = Path("/Users/aurolafly/.codex/archived_sessions") / BASENAME
spec = importlib.util.spec_from_file_location("prior_read_verification", ROOT / "audit/highest-directive-astra-20260923/verify_visible_reads.py")
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)


def reader(*args):
    return subprocess.check_output(["python3", READER, *args, "--host", "codex", "--source", str(SOURCE)], text=True)


def context(kind, filename):
    private = ROOT / "private-audit/highest-directive-claim-audit-20260923" / filename
    reader("context", "--kind", kind, "--section", "all", "--format", "json", "--no-truncate", "--output", str(private))
    return json.loads(private.read_text())["events"]


def main():
    results = {e["data"]["call_id"]: e for e in context("tool_result", "visible-tools.json")}
    summaries = reader("scan", "--kind", "tool_call", "--limit", "1000", "--json")
    locators = [json.loads(line)["locator"] for line in summaries.splitlines() if line.startswith("{") and "locator" in json.loads(line)]
    calls, reads = [], []
    targets = {str(p.relative_to(ROOT)): p for p in [OUT / n for n in ["directive-C.md", "directive-D.md", "ROUND-1.md", "ROUND-2.md"]]}
    for locator in locators:
        e = json.loads(reader("inspect", locator, "--no-truncate"))
        raw = e.get("data", {}).get("arguments", {}).get("raw", "")
        calls.append({"locator": locator, "name": e["name"], "raw": raw})
        result = results.get(e["data"].get("call_id"))
        if not result or not isinstance(raw, str):
            continue
        visible = prior.outputs(result["text"])
        for match in re.finditer(r'"?cmd"?\s*:\s*("(?:\\.|[^"\\])*")', raw):
            parts = shlex.split(json.loads(match[1]))
            selections = []
            if parts and parts[0] == "cat":
                selections = [(p, 1, None) for p in parts[1:]]
            elif len(parts) == 4 and parts[:2] == ["sed", "-n"]:
                span = re.fullmatch(r"(\d+),(\d+|\$)p", parts[2])
                if span:
                    selections = [(parts[3], int(span[1]), None if span[2] == "$" else int(span[2]))]
            for name, start, end in selections:
                if name not in targets:
                    continue
                lines = targets[name].read_text().splitlines(keepends=True)
                end = min(end or len(lines), len(lines))
                expected = "".join(lines[start - 1:end])
                reads.append({"file": name, "start": start, "end": end, "exact": bool(expected) and any(expected in v for v in visible),
                              "turn": e["turn_id"], "call": locator, "result": result["locator"]})
    turns = list(dict.fromkeys(e["turn"] for e in reads))
    coverage = []
    for turn in turns:
        for name, path in targets.items():
            selected = [e for e in reads if e["turn"] == turn and e["file"] == name]
            if not selected:
                continue
            lines = set()
            for e in selected:
                if e["exact"]:
                    lines.update(range(e["start"], e["end"] + 1))
            total = len(path.read_text().splitlines())
            coverage.append({"turn": turn, "file": name, "covered": len(lines), "total": total, "complete": len(lines) == total})
    answers = []
    for e in context("assistant_message", "visible-answers.json"):
        if e.get("data", {}).get("phase") != "final_answer":
            continue
        name = f"answer-{len(answers) + 1}.md"
        data = e["text"].encode()
        target = OUT / name
        if target.exists() and target.read_bytes() != data:
            raise SystemExit("Refusing to overwrite preserved final")
        if not target.exists():
            target.write_bytes(data)
        answers.append({"file": name, "locator": e["locator"], "turn": e["turn_id"], "sha256": hashlib.sha256(data).hexdigest()})
    receipt = {"source": str(SOURCE), "canonical_reader": READER, "tool_calls": calls, "range_evidence": reads,
               "coverage": coverage, "answers": answers, "boundary": "Only public final answers and tool evidence; no private reasoning; source range matches do not certify comprehension"}
    (OUT / "EVIDENCE.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"answers": len(answers), "coverage": coverage}, ensure_ascii=False))


if __name__ == "__main__":
    main()
