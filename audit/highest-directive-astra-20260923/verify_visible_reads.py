"""Compare declared cat/sed ranges against visible results from the canonical reader.

Never reads raw rollout JSONL itself. The canonical reader owns host parsing.
Only complete literal range matches count; partial/unsupported results stay gaps.
"""
from pathlib import Path
import hashlib
import json
import re
import shlex
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
READER = "/Users/aurolafly/codex/tools/session_trajectory.py"
SOURCES = {
    "A": "/Users/aurolafly/.codex/sessions/2026/09/23/rollout-2026-09-23T11-25-08-01a0cede-e026-73d0-bc41-5ec5de7cd279.jsonl",
    "B": "/Users/aurolafly/.codex/sessions/2026/09/23/rollout-2026-09-23T11-25-34-01a0cedf-4803-7522-a78f-a09959ed7bed.jsonl",
}
for _arm, _source in tuple(SOURCES.items()):
    _active = Path(_source)
    _archived = Path("/Users/aurolafly/.codex/archived_sessions") / _active.name
    if not _active.exists() and _archived.exists():
        SOURCES[_arm] = str(_archived)


def run(*args):
    return subprocess.check_output(["python3", READER, *args], text=True)


def outputs(text):
    body = text.split("Output:\n", 1)[-1]
    decoded = []
    while body.strip():
        body = body.lstrip()
        try:
            obj, end = json.JSONDecoder().raw_decode(body)
        except json.JSONDecodeError:
            break
        if isinstance(obj, dict) and isinstance(obj.get("output"), str):
            decoded.append(obj["output"])
        body = body[end:]
    return decoded


def main():
    receipts = {}
    freeze = json.loads((OUT / "FREEZE.json").read_text())
    for arm, source in SOURCES.items():
        private = ROOT / "private-audit/highest-directive-astra-20260923" / (arm + "-visible-tools.json")
        run("context", "--host", "codex", "--source", source, "--kind", "tool_result",
            "--section", "all", "--format", "json", "--no-truncate", "--output", str(private))
        results = {e["data"]["call_id"]: e for e in json.loads(private.read_text())["events"]}
        summaries = run("scan", "--host", "codex", "--source", source, "--kind", "tool_call", "--limit", "1000", "--json")
        calls = [json.loads(line) for line in summaries.splitlines() if line.startswith("{")]
        evidence, commands = [], []
        for item in calls:
            if "locator" not in item:
                continue
            event = json.loads(run("inspect", "--host", "codex", "--source", source, item["locator"], "--no-truncate"))
            raw = event.get("data", {}).get("arguments", {}).get("raw", "")
            commands.append({"locator": event["locator"], "name": event["name"], "raw": raw})
            result = results.get(event["data"].get("call_id"))
            if not result or not isinstance(raw, str):
                continue
            visible = outputs(result["text"])
            for match in re.finditer(r'"?cmd"?\s*:\s*("(?:\\.|[^"\\])*")', raw):
                cmd = json.loads(match.group(1))
                parts = shlex.split(cmd)
                selections = []
                if parts and parts[0] == "cat":
                    selections = [(p, 1, None) for p in parts[1:] if not p.startswith("-")]
                elif len(parts) == 4 and parts[:2] == ["sed", "-n"]:
                    span = re.fullmatch(r"(\d+),(\d+|\$)p", parts[2])
                    if span:
                        selections = [(parts[3], int(span[1]), None if span[2] == "$" else int(span[2]))]
                for name, start, end in selections:
                    path = ROOT / name
                    if not path.is_file():
                        continue
                    lines = path.read_text().splitlines(keepends=True)
                    end = min(end or len(lines), len(lines))
                    expected = "".join(lines[start - 1:end])
                    exact = bool(expected) and any(expected in v for v in visible)
                    evidence.append({"path": name, "start": start, "end": end, "exact_visible_range": exact,
                                     "call": event["locator"], "result": result["locator"], "turn": event["turn_id"]})
        names = [n for n in freeze["source_inputs"] if not n.endswith("logic.tex")]
        names += ["audit/highest-directive-astra-20260923/directive-" + arm + ".md",
                  "audit/highest-directive-astra-20260923/book-logic-excerpts.tex"]
        coverage = []
        for name in names:
            lines = (ROOT / name).read_text().splitlines()
            covered = set()
            for e in evidence:
                if e["path"] == name and e["exact_visible_range"]:
                    covered.update(range(e["start"], e["end"] + 1))
            missing = sorted(set(range(1, len(lines) + 1)) - covered)
            coverage.append({"path": name, "lines": len(lines), "verified_lines": len(covered), "missing_lines": missing,
                             "status": "EXACT_RANGES_COVER_PHYSICAL_LINES" if not missing else "GAP"})
        directive_name = "audit/highest-directive-astra-20260923/directive-" + arm + ".md"
        directive_lines = len((ROOT / directive_name).read_text().splitlines())
        by_turn = []
        for turn in dict.fromkeys(e["turn"] for e in evidence):
            matched = [e for e in evidence if e["turn"] == turn and e["path"] == directive_name]
            covered = set()
            for e in matched:
                if e["exact_visible_range"]:
                    covered.update(range(e["start"], e["end"] + 1))
            by_turn.append({"turn": turn, "verified_lines": len(covered), "total_lines": directive_lines,
                            "complete": len(covered) == directive_lines,
                            "read_calls": [e["call"] for e in matched]})
        receipts[arm] = {"branch_source": source, "canonical_reader": READER,
                         "visible_results_sha256": hashlib.sha256(private.read_bytes()).hexdigest(),
                         "commands": commands, "range_evidence": evidence, "coverage": coverage,
                         "directive_reads_per_turn": by_turn,
                         "boundary": "literal ranges in paired model-visible results; not model understanding or raw request certification"}
    (OUT / "READ-VERIFICATION.json").write_text(json.dumps(receipts, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({arm: {"paths": len(v["coverage"]), "gaps": [x["path"] for x in v["coverage"] if x["missing_lines"]]} for arm, v in receipts.items()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
