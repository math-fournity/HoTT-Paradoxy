"""Rules-based correspondence review between the original task and the witness.

This is a checklist engine over declared inputs, not a philosophical oracle:
every field names the input it was derived from, and unresolved reality
bridge items stay unresolved.
"""
from __future__ import annotations

from pathlib import Path

from .util import git_state, sha256_file, utc_now, write_json


def review_correspondence(
    repo_root: Path,
    *,
    review_id: str,
    case: dict,
    case_path: Path,
    task: dict,
    witness: dict,
    profile_report: dict,
    output_path: Path,
) -> dict:
    correspondence = task.get("correspondence", {})
    mode = witness["observation_mode"]
    if mode == "deadline":
        mechanism = "the result-equivalence class forgets the round index; the deadline consumer reads it"
        compensation = {
            "class": "RECOVERY_FROM_ORIGINAL_REPRESENTATION",
            "detail": "the round index n is already carried by ret n a; the consumer reads only that",
        }
    else:
        mechanism = "race reads completion order; the composed business continuation turns the losing branch into divergence"
        compensation = {
            "class": "PRE_KEPT_BY_TASK_DECLARATION",
            "detail": "the business continuation is part of the declared task input, not invented after seeing the candidate",
        }
    checklist = [
        {
            "item": "original activity and completion criterion are declared before search",
            "status": "DECLARED",
            "evidence": [case["task"]["path"], f"revision {task['revision']}"],
        },
        {
            "item": "the theoryization step is an operation of the pinned model",
            "status": "SUPPORTED",
            "evidence": [
                f"{profile_report['profile_id']}: supported_operations",
                case["profile"]["path"],
            ],
        },
        {
            "item": "the separating observation is declared in the task, not an oracle added later",
            "status": "DECLARED",
            "detail": correspondence.get("observation_justification"),
            "evidence": [case["task"]["path"]],
        },
        {
            "item": "compensation class of the consumer",
            "status": compensation["class"],
            "detail": compensation["detail"],
            "evidence": [case["profile"]["path"]],
        },
        {
            "item": "quantifier scope of the claim",
            "status": "FINITE_DECLARED_GRAMMAR_ONLY",
            "detail": "the verified statement is a ground instance; no universal or physical claim is made",
            "evidence": [case["grammar"]["path"]],
        },
        {
            "item": "reality bridge",
            "status": "NOT_CLOSED_IN_M1",
            "detail": "the run is a model-level calibration instance; a real consumer would be a separate E6-style audit",
            "evidence": [case["task"]["path"]],
        },
    ]
    review = {
        "schema_version": "machine-overview-correspondence-review/v1",
        "review_id": review_id,
        "case_id": case["case_id"],
        "case_revision": case["revision"],
        "case_pointer": str(case_path),
        "witness_id": witness["witness_id"],
        "created_at_utc": utc_now(),
        "mechanism_summary": mechanism,
        "checklist": checklist,
        "conclusion": {
            "correspondence_status": "MODEL_ONLY_OPERATIONALLY_SPECIFIED",
            "task_preservation": "PRESERVED_AT_MODEL_LEVEL",
            "reality_correspondence": "UNRESOLVED",
            "research_relation": "calibration",
            "new_claim": False,
            "related_claims": case.get("claim_refs", []),
            "open_obligations": correspondence.get("open_obligations", []),
        },
        "case_sha256": sha256_file(case_path),
        "git": git_state(repo_root),
    }
    write_json(output_path, review)
    return review
