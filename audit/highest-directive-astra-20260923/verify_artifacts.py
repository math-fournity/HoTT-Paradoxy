"""Record bounded integrity checks for this completed document/behavior trial."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent


def main():
    freeze = json.loads((OUT / "FREEZE.json").read_text())
    current = (ROOT / "最高指示.md").read_text()
    baseline = (OUT / "directive-A.md").read_text()
    quote = lambda s: re.findall(r"~~~text\n(.*?)\n~~~", s, re.S)[:2]
    report = ROOT / "audit/最高指示Astra质量复审-20260923.md"
    rows = re.findall(r"^\|(000\d{3})\|", report.read_text(), re.M)
    paths = [ROOT / p for p in ["最高指示.md", "悖论靶前提与针对性过程演练-20260923.md",
             "feature-list.md", "rulings.md", "README/001 - 当前入口与关键文件.md"]] + [report]
    gaps = []
    for path in paths:
        for match in re.finditer(r"\]\((?:<([^>]+)>|([^\)]+))\)", path.read_text()):
            target = (match[1] or match[2]).split("#", 1)[0]
            if target and not re.match(r"[a-z]+://", target) and not (path.parent / target).exists():
                gaps.append([str(path.relative_to(ROOT)), target])
    diff = subprocess.run(["git", "diff", "--check", "--", *[str(p.relative_to(ROOT)) for p in paths]],
                          cwd=ROOT, capture_output=True, text=True)
    read = json.loads((OUT / "READ-VERIFICATION.json").read_text())
    answers = json.loads((OUT / "ANSWER-RECEIPTS.json").read_text())
    checks = {
        "original_two_blocks_byte_equivalent": quote(current) == quote(baseline) and len(quote(current)) == 2,
        "current_directive_equals_tested_B": (ROOT / "最高指示.md").read_bytes() == (OUT / "directive-B.md").read_bytes(),
        "no_directive_shard_directory": not (ROOT / "最高指示").exists(),
        "kc_48_once_in_order": rows == [f"{i:06}" for i in range(1, 49)],
        "source_pins_unchanged": all(hashlib.sha256((ROOT / n).read_bytes()).hexdigest() == v["sha256"] for n, v in freeze["source_inputs"].items()),
        "local_links_resolve": not gaps,
        "git_diff_check": diff.returncode == 0,
        "all_15_inputs_verified_each_arm": all(len(v["coverage"]) == 15 and not any(x["missing_lines"] for x in v["coverage"]) for v in read.values()),
        "both_turns_reread_directive": all(len(v["directive_reads_per_turn"]) == 2 and all(t["complete"] for t in v["directive_reads_per_turn"]) for v in read.values()),
        "four_visible_final_answers_preserved": set(answers) == {"A", "B"} and all(len(v) == 2 for v in answers.values()) and all(hashlib.sha256((OUT / e["file"]).read_bytes()).hexdigest() == e["sha256"] for v in answers.values() for e in v),
    }
    result = {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks,
              "link_gaps": gaps, "diff_check_stdout": diff.stdout, "diff_check_stderr": diff.stderr,
              "scope": "artifact integrity and visible read ranges; no mathematical proof or general model-effect claim",
              "base_head_unchanged": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() == freeze["base_commit"],
              "historical_shard_check": {"command": "python3 -B scripts/audit/verify_governance_shards.py", "observed_exit": 0, "observed_status": "PASS", "observation_time_utc": "2026-09-23T15:33:43.712218+00:00", "receipt_boundary": "summary of actual parent tool result; not a re-execution by this script"}}
    (OUT / "STATIC-VERIFICATION.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
