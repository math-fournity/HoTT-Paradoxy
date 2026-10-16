"""Preserve only final, user-visible test answers via the canonical trajectory reader."""
from pathlib import Path
import hashlib
import json
import subprocess
from verify_visible_reads import READER, ROOT, OUT, SOURCES


def main():
    receipt = {}
    for arm, source in SOURCES.items():
        private = ROOT / "private-audit/highest-directive-astra-20260923" / (arm + "-visible-answers.json")
        subprocess.run(["python3", READER, "context", "--host", "codex", "--source", source,
                        "--kind", "assistant_message", "--section", "assistant", "--format", "json",
                        "--no-truncate", "--output", str(private)], check=True, capture_output=True)
        events = json.loads(private.read_text())["events"]
        finals = [e for e in events if e.get("data", {}).get("phase") == "final_answer"]
        receipt[arm] = []
        for number, event in enumerate(finals, 1):
            name = f"{arm}-round-{number}.md"
            data = event["text"].encode()
            target = OUT / name
            if target.exists() and target.read_bytes() != data:
                raise SystemExit(f"Refusing to replace preserved answer: {name}")
            if not target.exists():
                target.write_bytes(data)
            receipt[arm].append({"file": name, "sha256": hashlib.sha256(data).hexdigest(),
                                 "locator": event["locator"], "turn": event["turn_id"],
                                 "timestamp": event["timestamp"], "bytes": len(data)})
    (OUT / "ANSWER-RECEIPTS.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({arm: len(items) for arm, items in receipt.items()}))


if __name__ == "__main__":
    main()
