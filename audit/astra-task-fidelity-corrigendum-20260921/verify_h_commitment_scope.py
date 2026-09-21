#!/usr/bin/env python3
"""Mechanically verify hashes and stated source anchors for the bounded H audit.

This script checks only source identity and selected text anchors.  It does not
decide the semantic question whether an arbitrary source supplies H.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "SOURCE-MANIFEST.json"
OUT = HERE / "VERIFICATION.json"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> int:
    manifest = json.loads(MANIFEST.read_text())
    checks = []
    failures = []
    for entry in manifest["sources"]:
        path = ROOT / entry["path"]
        data = path.read_bytes()
        text = data.decode()
        hash_ok = sha(data) == entry["sha256"]
        fragments = {fragment: fragment in text for fragment in entry.get("required_fragments", [])}
        ok = hash_ok and all(fragments.values())
        checks.append(
            {
                "path": entry["path"],
                "sha256": sha(data),
                "hash_matches_manifest": hash_ok,
                "required_fragments": fragments,
                "status": "PASS" if ok else "FAIL",
            }
        )
        if not ok:
            failures.append(entry["path"])

    vocabulary = re.compile(manifest["negative_vocabulary_regex"], re.IGNORECASE)
    negative = {}
    for rel in manifest["negative_vocabulary_scope"]:
        matches = vocabulary.findall((ROOT / rel).read_text())
        negative[rel] = {"matches": matches, "match_count": len(matches)}
        if matches:
            failures.append(rel + ":negative_vocabulary")

    result = {
        "schema_version": "astra-task-fidelity-h-scope-verification/v1",
        "status": "PASS" if not failures else "FAIL",
        "manifest_sha256": sha(MANIFEST.read_bytes()),
        "checks": checks,
        "negative_vocabulary": negative,
        "failures": failures,
        "scope_limit": "Mechanical verification of a fixed source set; no global absence theorem and no semantic automatic decision.",
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
