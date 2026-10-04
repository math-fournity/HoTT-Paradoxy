#!/usr/bin/env python3
"""Capture bare-Lean source-card classification run for MP-SEP-COMPLETION-PROMOTION-SOURCE-001."""
from __future__ import annotations
import datetime as dt, hashlib, json, platform, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "20261004-MP-SEP-COMPLETION-PROMOTION-SOURCE-001-"
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else PREFIX + "01"
SOURCE = Path("HoTT/formal/zfc-observation-boundary/SepCompletionPromotion.lean")
CLAIM = Path("HoTT/formal/zfc-observation-boundary/SepCompletionPromotion-CLAIM.md")
CARD = Path("audit/20261004-P-DAG-ZFC-QP-103-PROMPT.md")
LEAN = Path("/Users/aurolafly/.elan/bin/lean")

def sha(b: bytes) -> str: return hashlib.sha256(b).hexdigest()
def row(p: Path) -> dict[str, object]:
    b = p.read_bytes(); return {"path": str(p.relative_to(ROOT)), "bytes": len(b), "sha256": sha(b)}
def write_new(p: Path, b: bytes) -> None:
    if p.exists(): raise RuntimeError(f"REFUSE_OVERWRITE:{p}")
    p.write_bytes(b)

def main() -> None:
    if "/" in RUN_ID or not RUN_ID.startswith(PREFIX): raise SystemExit("RUN_ID_INVALID")
    source, claim, card = ROOT / SOURCE, ROOT / CLAIM, ROOT / CARD
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists(): raise SystemExit("RUN_ALREADY_EXISTS")
    if not all(p.is_file() for p in (source, claim, card, LEAN)): raise SystemExit("REQUIRED_INPUT_MISSING")
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run([str(LEAN), str(source)], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    completed = dt.datetime.now(dt.timezone.utc)
    accepted = result.returncode == 0 and b"sorryAx" not in result.stdout and b"declaration uses 'sorry'" not in result.stderr
    version = subprocess.check_output([str(LEAN), "--version"], text=True).strip()
    run.mkdir(parents=True)
    manifest = {"schema_version":"formal-proof-source-manifest/v1", "proof_id":"MP-SEP-COMPLETION-PROMOTION-SOURCE-001", "run_id":RUN_ID, "files":[row(source),row(claim),row(card),row(Path(__file__))], "external_dependencies":[], "policy":"Machine-checks source-card classification only, not SEP truth, ZFC, topology, or physical completion."}
    receipt = {"schema_version":"formal-proof-run/v1", "run_id":RUN_ID, "proof_id":"MP-SEP-COMPLETION-PROMOTION-SOURCE-001", "claim_ids":["SEP-P-SOURCE-001","SEP-P-SOURCE-002","SEP-P-SOURCE-003"], "proof_assistant":"Lean", "proof_assistant_version":version, "theory_variant":"Lean 4 core source-card classification; no formalization of SEP prose, ZFC, physical motion, or topology.", "command_argv":[str(LEAN),str(source)], "cwd":str(ROOT), "started_at_utc":started.isoformat(), "completed_at_utc":completed.isoformat(), "duration_seconds":(completed-started).total_seconds(), "exit_code":result.returncode, "status":"KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED", "scope":"Frozen SEP card states convergence, promotion to every-step Done, no supplied verified bridge, and excluded final-action completion.", "non_goals":["No proof SEP is true.","No actual ZFC conclusion.","No general limit theorem.","No P-to-HoTT-B provenance."], "index_status":"CONTRIBUTOR_CANDIDATE_PENDING_CANONICAL_CLAIM_MATRIX_REVIEW", "git_status":"LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED"}
    env = f"platform={platform.platform()}\nlean={version}\nimports=none\naxioms=printed-in-stdout\n".encode()
    for name, data in [("stdout.txt",result.stdout),("stderr.txt",result.stderr),("environment.txt",env),("source-manifest.json",(json.dumps(manifest,ensure_ascii=False,sort_keys=True,indent=2)+"\n").encode())]:
        write_new(run/name,data); receipt[name.removesuffix('.txt').replace('-','_')]={"path":name,"bytes":len(data),"sha256":sha(data)}
    write_new(run/"RUN.json",(json.dumps(receipt,ensure_ascii=False,sort_keys=True,indent=2)+"\n").encode())
    print(json.dumps({"status":receipt["status"],"run_id":RUN_ID,"exit":result.returncode,"duration_seconds":receipt["duration_seconds"]},ensure_ascii=False))
if __name__ == "__main__": main()
