"""Freeze exact document bytes and bounded source excerpts for a two-arm reading trial.

This is an evidence-copying utility, not a semantic judge or a persistent registry manager.
It refuses to overwrite a frozen trial. Run once before spawning test actors.
"""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BASE = "a98926f65d5c804261c7143084dd49050aa45ef0"


def identity(data):
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
            "lines": len(data.splitlines())}


def main():
    if (OUT / "FREEZE.json").exists():
        raise SystemExit("Already frozen; do not overwrite trial evidence")
    baseline = subprocess.check_output(["git", "-C", str(ROOT), "show", BASE + ":最高指示.md"])
    files = {"directive-A.md": baseline, "directive-B.md": (ROOT / "最高指示.md").read_bytes()}
    source = ROOT / "HoTT/theory-schema/upstream/book-578b85cc/logic.tex"
    lines = source.read_bytes().splitlines(keepends=True)
    files["book-logic-excerpts.tex"] = b"% Source ranges: 160-173; 701-850 (inclusive)\n" + b"".join(lines[159:173]) + b"\n% Original line 701 follows\n" + b"".join(lines[700:850])
    for name, data in files.items():
        with (OUT / name).open("xb") as handle:
            handle.write(data)
    inputs = ["核心认知.md", "扩展认知.md"] + [str(p.relative_to(ROOT)) for p in sorted((ROOT / "扩展认知").glob("*.md"))]
    inputs += ["HoTT/sources/user-originals/Z铁律-抽象-圆环-时间维度-用户原始论述-20260901.md",
               "HoTT/sources/user-originals/Better-Best悖论-原文.md", str(source.relative_to(ROOT))]
    receipt = {"scope": "old-v2 versus new-v3 diagnostic trial; not a no-document control",
               "base_commit": BASE, "requested_model": "gpt-6-astra", "requested_reasoning_effort": "ultra",
               "copies": {name: identity(data) for name, data in files.items()},
               "source_inputs": {name: identity((ROOT / name).read_bytes()) for name in inputs},
               "preregister": identity((OUT / "PREREG.md").read_bytes()),
               "limitations": ["two instances; no population effect estimate", "same model and author-judge bias",
                               "shared filesystem; read restrictions are instructed, not filesystem isolation",
                               "requested model identity is not independent backend attestation"]}
    (OUT / "FREEZE.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": "FROZEN", "root": str(OUT), "copies": receipt["copies"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
