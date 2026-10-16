#!/usr/bin/env python3
"""N14(a): bounded repair for the claim-ledger drift issue.

The snapshot ledger `audit/claim-evidence-ledger.jsonl` records each claim's
owner document and line number but no owner-document hash, so claims drift
when the owner document is edited later.  This read-only tool:

1. pins the current owner-document hashes into a sidecar file so that future
   owner edits are detectable by hash comparison;
2. re-checks every claim's line anchor against the owner document's *current*
   content and classifies it (MATCH / PREFIX / CONTAINED / DRIFTED /
   LINE_OUT_OF_RANGE / MISSING_FILE);
3. writes a machine-readable drift report with per-owner aggregates.

It does not modify the ledger; re-extraction of drifted claims remains an
explicit follow-up decision.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER = "audit/claim-evidence-ledger.jsonl"
SIDECAR = "audit/claim-ledger-owner-hashes-20260912.json"
REPORT = "audit/claim-ledger-drift-check-20260912.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def norm(text: str) -> str:
    return " ".join((text or "").split())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.project_root.resolve()

    rows = [json.loads(line) for line in (root / LEDGER).read_text(encoding="utf-8").splitlines() if line.strip()]
    by_owner: dict[str, list[dict]] = {}
    for row in rows:
        by_owner.setdefault(row["claim_owner_document"], []).append(row)

    owner_hashes, results, drift_examples = {}, {}, []
    totals = {"MATCH": 0, "PREFIX": 0, "CONTAINED": 0, "DRIFTED": 0, "LINE_OUT_OF_RANGE": 0, "MISSING_FILE": 0}
    for owner, claims in sorted(by_owner.items()):
        path = root / owner
        if not path.is_file():
            status_counts = {"MISSING_FILE": len(claims)}
            owner_hashes[owner] = None
        else:
            raw = path.read_text(encoding="utf-8", errors="replace")
            lines = raw.splitlines()
            owner_hashes[owner] = {
                "sha256": sha(path),
                "bytes": path.stat().st_size,
                "lines": len(lines),
                "claim_count": len(claims),
            }
            status_counts = {k: 0 for k in totals}
            for claim in claims:
                ln = claim.get("claim_line")
                text = norm(claim.get("claim_text", ""))
                if not isinstance(ln, int) or ln < 1 or ln > len(lines):
                    status = "LINE_OUT_OF_RANGE"
                else:
                    current = norm(lines[ln - 1])
                    if current == text:
                        status = "MATCH"
                    elif text and current.startswith(text):
                        status = "PREFIX"
                    elif text and text in current:
                        status = "CONTAINED"
                    else:
                        status = "DRIFTED"
                status_counts[status] = status_counts.get(status, 0) + 1
                if status in ("DRIFTED", "LINE_OUT_OF_RANGE") and len(drift_examples) < 40:
                    drift_examples.append({
                        "claim_id": claim["claim_id"],
                        "owner": owner,
                        "line": ln,
                        "status": status,
                        "ledger_text": text[:160],
                        "current_text": (norm(lines[ln - 1])[:160] if isinstance(ln, int) and 1 <= ln <= len(lines) else None),
                    })
            for key in totals:
                totals[key] += status_counts.get(key, 0)
        results[owner] = {"claim_count": len(claims), "status_counts": status_counts}

    sidecar = {
        "schema_version": "claim-ledger-owner-hashes/v1",
        "generated_for_ledger": LEDGER,
        "ledger_sha256": sha(root / LEDGER),
        "owners": {o: h for o, h in owner_hashes.items()},
    }
    (root / SIDECAR).write_text(json.dumps(sidecar, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = {
        "schema_version": "claim-ledger-drift-check/v1",
        "ledger": LEDGER,
        "ledger_sha256": sidecar["ledger_sha256"],
        "totals": totals,
        "owners": results,
        "drift_examples": drift_examples,
        "sidecar": SIDECAR,
        "policy": "Read-only check. Citation of any claim line must re-check the owner document's current content until the drifted claims are re-extracted.",
    }
    (root / REPORT).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "CHECKED", "totals": totals, "owners": len(results),
                      "drift_examples": len(drift_examples), "sidecar": SIDECAR, "report": REPORT}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
