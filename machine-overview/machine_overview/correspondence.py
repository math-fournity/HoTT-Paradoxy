"""Rules-based correspondence review between the original task and the witness.

The mechanism description is derived from the witness structure (ops and
observed difference), not from the observation mode alone (audit F4).  Task
preservation is computed from explicit checks against the frozen grammar,
observation kinds and case/search binding; it is never asserted unconditionally.
"""
from __future__ import annotations

from pathlib import Path

from .search import within_grammar_witness, witness_ast_sha256
from .model import value_from_json
from .util import MachineOverviewError, git_state, read_json, sha256_file, utc_now, write_json


def _business_continuation(grammar: dict) -> dict | None:
    for continuation in grammar.get("bind_continuations", []):
        if continuation["id"] == "deliver_business":
            return continuation["map"]
    return None


def mechanism_facts(witness: dict, grammar: dict) -> dict:
    ops = witness["ops"]
    kinds = [op["kind"] for op in ops]
    has_deadline = "deadline" in kinds
    business = _business_continuation(grammar)
    has_business_bind = any(
        op["kind"] == "bind" and business is not None and op["continuation"] == business for op in ops
    )
    has_race = any(kind in ("race_left", "race_right") for kind in kinds)
    has_plain_bind = "bind" in kinds and not has_business_bind
    separation = witness["separation_kind"]
    context_summary = []
    for op in ops:
        if op["kind"] == "deadline":
            context_summary.append(f"deadline({op['k']}, □)")
        elif op["kind"] == "race_left":
            context_summary.append("race(□, partner)")
        elif op["kind"] == "race_right":
            context_summary.append("race(partner, □)")
        elif op["kind"] == "bind":
            context_summary.append("bind(□, continuation)" + ("[declared business]" if has_business_bind and op["continuation"] == business else ""))

    if separation == "deadline_observation":
        mechanism = (
            "The declared deadline consumer reads the round index n that the pinned constructor `ret n a` "
            "already carries. Result equivalence ≈ identifies `ret n a` with `ret m a`, so it cannot see "
            "the difference the deadline consumer reads."
        )
        compensation = {
            "class": "READS_DECLARED_REPRESENTATION",
            "detail": "The round index is part of the constructor already present in the frozen model; "
                      "this is not recovery of n from a result quotient, and no quotient-level recovery is claimed.",
        }
    elif separation == "completion_divergence" and has_business_bind:
        mechanism = (
            "The declared race context reads completion order, and the declared business continuation turns "
            "the losing branch into divergence; ≈ identifies the two inputs because they have the same result "
            "behaviour before composition."
        )
        compensation = {
            "class": "PRE_KEPT_BY_TASK_DECLARATION",
            "detail": "The business continuation is declared as part of the task input before the search; "
                      "it is not invented after seeing the candidate.",
        }
    elif separation == "completion_divergence":
        mechanism = (
            "The declared race context makes one side diverge while the other returns; ≈ cannot see completion "
            "order, so it identifies the two result-equivalent inputs."
        )
        compensation = {
            "class": "DECLARED_CONSUMER_READS_COMPLETION_ORDER",
            "detail": "No extra information is added: the race consumer reads completion order exposed by the "
                      "pinned operations.",
        }
    elif separation == "value_mismatch":
        mechanism = (
            "The declared context selects a different delivered Bool value on the two sides. Result equivalence "
            "≈ identifies the input computations (same value and same convergence behaviour), so it cannot see "
            "which branch the context delivers."
        )
        compensation = {
            "class": "DECLARED_CONSUMER_READS_COMPLETION_ORDER",
            "detail": "The value difference is produced solely by the declared race context; no extra input, "
                      "continuation or assumption is introduced.",
        }
    else:
        mechanism = f"Unclassified separation kind: {separation}"
        compensation = {"class": "UNRESOLVED", "detail": "The review cannot classify this witness."}
    return {
        "context_summary": context_summary,
        "has_deadline": has_deadline,
        "has_race": has_race,
        "has_business_bind": has_business_bind,
        "has_plain_bind": has_plain_bind,
        "mechanism": mechanism,
        "compensation": compensation,
    }


def review_correspondence(
    repo_root: Path,
    *,
    review_id: str,
    case: dict,
    case_path: Path,
    task: dict,
    witness: dict,
    profile_report: dict,
    grammar: dict,
    search_run: dict,
    search_run_path: Path,
    output_path: Path,
) -> dict:
    facts = mechanism_facts(witness, grammar)
    left = value_from_json(witness["pair"]["left"])
    right = value_from_json(witness["pair"]["right"])
    inside, reason = within_grammar_witness(witness["ops"], left, right, grammar)
    case_bound = (
        search_run.get("case_id") == case["case_id"]
        and int(search_run.get("case_revision", -1)) == int(case["revision"])
    )
    declared_observation_kinds = set(task.get("correspondence", {}).get("declared_observation_kinds",
                                                                       ["deadline_observation", "value_mismatch", "completion_divergence"]))
    checks = [
        {"id": "grammar_membership", "status": "PASS" if inside else "FAIL", "detail": reason},
        {"id": "case_search_binding", "status": "PASS" if case_bound else "FAIL",
         "detail": f"search run case revision {search_run.get('case_revision')} vs case revision {case['revision']}"},
        {"id": "declared_observation_kind",
         "status": "PASS" if witness["separation_kind"] in declared_observation_kinds else "FAIL",
         "detail": witness["separation_kind"]},
        {"id": "declared_consumer_present",
         "status": "PASS" if (facts["has_deadline"] or facts["has_race"]) else "FAIL",
         "detail": "the witness must apply at least one declared consumer (deadline or race)"},
        {"id": "compensation_classified",
         "status": "PASS" if facts["compensation"]["class"] != "UNRESOLVED" else "FAIL",
         "detail": facts["compensation"]["class"]},
    ]
    preservation = "PRESERVED_AT_MODEL_LEVEL" if all(item["status"] == "PASS" for item in checks) else "REVIEW_REQUIRED"

    checklist = [
        {"item": "original activity and completion criterion are declared before search",
         "status": "DECLARED", "evidence": [case["task"]["path"], f"revision {task['revision']}"]},
        {"item": "the theoryization step is an operation of the pinned model",
         "status": "SUPPORTED", "evidence": [f"{profile_report['profile_id']}: supported_operations", case["profile"]["path"]]},
        {"item": "the separating observation is declared in the task, not an oracle added later",
         "status": "DECLARED", "detail": task.get("correspondence", {}).get("observation_justification"),
         "evidence": [case["task"]["path"]]},
        {"item": "compensation class of the consumer", "status": facts["compensation"]["class"],
         "detail": facts["compensation"]["detail"], "evidence": [case["profile"]["path"]]},
        {"item": "quantifier scope of the claim", "status": "FINITE_DECLARED_GRAMMAR_ONLY",
         "detail": "the verified statement is a ground instance; no universal or physical claim is made",
         "evidence": [case["grammar"]["path"]]},
        {"item": "reality bridge", "status": "NOT_CLOSED_IN_M1",
         "detail": "the run is a model-level calibration instance; a real consumer would be a separate E6-style audit",
         "evidence": [case["task"]["path"]]},
    ]
    review = {
        "schema_version": "machine-overview-correspondence-review/v1",
        "review_id": review_id,
        "case_id": case["case_id"],
        "case_revision": case["revision"],
        "case_pointer": str(case_path),
        "case_sha256": sha256_file(case_path),
        "witness_id": witness["witness_id"],
        "candidate_ast_sha256": witness_ast_sha256(witness),
        "source_search_run": {
            "run_id": search_run["run_id"],
            "path": search_run_path.as_posix(),
            "sha256": sha256_file(search_run_path),
        },
        "created_at_utc": utc_now(),
        "mechanism_summary": facts["mechanism"],
        "context_summary": facts["context_summary"],
        "mechanism_facts": {
            "has_deadline": facts["has_deadline"],
            "has_race": facts["has_race"],
            "has_business_bind": facts["has_business_bind"],
            "has_plain_bind": facts["has_plain_bind"],
            "compensation": facts["compensation"],
        },
        "review_checks": checks,
        "checklist": checklist,
        "conclusion": {
            "correspondence_status": "MODEL_ONLY_OPERATIONALLY_SPECIFIED",
            "task_preservation": preservation,
            "task_preservation_basis": [item for item in checks],
            "reality_correspondence": "UNRESOLVED",
            "research_relation": "calibration",
            "new_claim": False,
            "related_claims": case.get("claim_refs", []),
            "open_obligations": task.get("correspondence", {}).get("open_obligations", []),
        },
        "git": git_state(repo_root),
    }
    if output_path.exists():
        existing = read_json(output_path)
        if existing == review:
            return existing
        raise MachineOverviewError(f"REVIEW_ALREADY_EXISTS_WITH_DIFFERENT_CONTENT:{output_path}")
    write_json(output_path, review)
    return review
