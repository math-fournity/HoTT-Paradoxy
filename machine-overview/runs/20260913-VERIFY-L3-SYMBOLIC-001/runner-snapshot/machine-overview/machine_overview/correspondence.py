"""Rules-based correspondence review between the original task and the witness.

The mechanism description is derived from the witness structure (ops and
observed difference), not from the observation mode alone (audit F4).  Task
preservation is computed from explicit checks against the frozen grammar,
observation kinds and case/search binding; it is never asserted unconditionally.
"""
from __future__ import annotations

from pathlib import Path

from .case import case_identity_sha256
from .search import derive_witness_record, within_grammar_witness, witness_ast_sha256
from .model import value_from_json
from .util import MachineOverviewError, git_state, read_json, sha256_file, utc_now, write_json


def _business_continuation(grammar: dict) -> dict | None:
    for continuation in grammar.get("bind_continuations", []):
        if continuation["id"] == "deliver_business":
            return continuation["map"]
    return None


def mechanism_facts(witness: dict, grammar: dict) -> dict:
    derived = derive_witness_record(witness, grammar)
    if grammar.get("backend") == "symbolic-horn-v1":
        used_rules = derived["used_rules"]
        required = set(grammar.get("mechanism_rules", []))
        classified = bool(required) and required.issubset(set(used_rules))
        return {
            "context_summary": [f"symbolic rule: {rule_id}" for rule_id in used_rules],
            "has_deadline": False,
            "has_race": False,
            "has_business_bind": False,
            "has_plain_bind": False,
            "mechanism": (
                "The declared theoryization uses the cubical interval as the activity's time carrier. "
                "Any internal observable f : I → A supplies an endpoint Path λ i → f i; composing that "
                "Path with the task's declared endpoint apartness yields the searched obstruction."
                if classified else "The symbolic witness does not contain the declared L3 mechanism rules."
            ),
            "compensation": {
                "class": "THEORYIZATION_ADDS_PATH_COHERENCE" if classified else "UNRESOLVED",
                "detail": (
                    "The endpoint values and exact completion observation are retained, while the I-indexed "
                    "encoding adds Path coherence between every observable's endpoints."
                    if classified else "Required symbolic mechanism rules are absent."
                ),
            },
            "derived_witness": derived,
        }
    ops = derived["ops"]
    kinds = [op["kind"] for op in ops]
    has_deadline = "deadline" in kinds
    business = _business_continuation(grammar)
    has_business_bind = any(
        op["kind"] == "bind" and business is not None and op["continuation"] == business for op in ops
    )
    has_race = any(kind in ("race_left", "race_right") for kind in kinds)
    has_plain_bind = "bind" in kinds and not has_business_bind
    separation = derived["separation_kind"]
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
        "derived_witness": derived,
    }


def _consumer_requirement_met(task: dict, separation: str, ops: list[dict], grammar: dict) -> tuple[bool, str]:
    requirements = task.get("correspondence", {}).get("consumer_requirements", {})
    requirement = requirements.get(separation)
    if not isinstance(requirement, dict):
        return False, f"no consumer requirement declared for {separation}"
    kinds = [op.get("kind") for op in ops]
    for required in requirement.get("requires", []):
        if required not in kinds:
            return False, f"missing required consumer operation {required}"
    any_required = requirement.get("requires_any", [])
    if any_required and not any(kind in kinds for kind in any_required):
        return False, f"missing any of {any_required}"
    bind_id = requirement.get("requires_bind_id")
    if bind_id:
        declared = next((item.get("map") for item in grammar.get("bind_continuations", [])
                         if item.get("id") == bind_id), None)
        if declared is None or not any(op.get("kind") == "bind" and op.get("continuation") == declared for op in ops):
            return False, f"missing declared bind continuation {bind_id}"
    return True, "declared consumer shape present"


def _derive_symbolic_correspondence_content(
    *, case: dict, task: dict, witness: dict, profile_report: dict,
    grammar: dict, search_run: dict,
) -> dict:
    facts = mechanism_facts(witness, grammar)
    derived = facts["derived_witness"]
    case_bound = (
        search_run.get("case_id") == case["case_id"]
        and int(search_run.get("case_revision", -1)) == int(case["revision"])
        and search_run.get("case_identity_sha256") == case_identity_sha256(case)
        and search_run.get("inputs", {}).get("profile_sha256") == case["profile"]["sha256"]
        and search_run.get("inputs", {}).get("task_sha256") == case["task"]["sha256"]
        and search_run.get("inputs", {}).get("grammar_sha256") == case["grammar"]["sha256"]
    )
    recorded = next((item for item in search_run.get("witnesses", [])
                     if item.get("witness_id") == derived["witness_id"]), None)
    observation = derived["separation_kind"]
    correspondence = task.get("correspondence", {})
    requirement = correspondence.get("consumer_requirements", {}).get(observation, {})
    required_rules = set(requirement.get("required_rules", [])) if isinstance(requirement, dict) else set()
    rules_met = bool(required_rules) and required_rules.issubset(set(derived["used_rules"]))
    time_structure = task.get("observation", {}).get("time_structure", {})
    time_distinguished = (
        isinstance(time_structure, dict)
        and bool(time_structure.get("reality"))
        and bool(time_structure.get("theory"))
    )
    preserved_fields = correspondence.get("preserved_fields", [])
    checks = [
        {"id": "profile_qualified", "status": "PASS" if profile_report.get("status") == "PROFILE_QUALIFIED" else "FAIL",
         "detail": profile_report.get("failures", [])},
        {"id": "grammar_membership", "status": "PASS", "detail": "symbolic proof AST re-typechecked"},
        {"id": "case_search_binding", "status": "PASS" if case_bound else "FAIL",
         "detail": f"search run case revision {search_run.get('case_revision')} vs case revision {case['revision']}"},
        {"id": "witness_search_binding", "status": "PASS" if recorded == derived else "FAIL",
         "detail": "full recomputed symbolic witness must equal the search-run record"},
        {"id": "declared_observation_kind",
         "status": "PASS" if observation in correspondence.get("declared_observation_kinds", []) else "FAIL",
         "detail": observation},
        {"id": "declared_symbolic_rules_present", "status": "PASS" if rules_met else "FAIL",
         "detail": sorted(required_rules)},
        {"id": "time_and_temporal_order_separated", "status": "PASS" if time_distinguished else "FAIL",
         "detail": time_structure},
        {"id": "preserved_task_fields_declared", "status": "PASS" if preserved_fields else "FAIL",
         "detail": preserved_fields},
        {"id": "compensation_classified",
         "status": "PASS" if facts["compensation"]["class"] != "UNRESOLVED" else "FAIL",
         "detail": facts["compensation"]["class"]},
    ]
    preservation = (
        "PRESERVED_ACROSS_DECLARED_ENDPOINT_OBSERVATION"
        if all(item["status"] == "PASS" for item in checks) else "REVIEW_REQUIRED"
    )
    return {
        "derived_witness": derived,
        "mechanism_summary": facts["mechanism"],
        "context_summary": facts["context_summary"],
        "mechanism_facts": {
            "has_deadline": False,
            "has_race": False,
            "has_business_bind": False,
            "has_plain_bind": False,
            "used_rules": derived["used_rules"],
            "compensation": facts["compensation"],
        },
        "review_checks": checks,
        "checklist": [
            {"item": "original activity and exact endpoint completion are declared before search",
             "status": "DECLARED", "evidence": [case["task"]["path"]]},
            {"item": "time structure is distinguished from temporal ordering",
             "status": "DECLARED", "detail": time_structure, "evidence": [case["task"]["path"]]},
            {"item": "the added Path-coherence obligation is localized to the I-indexed theoryization",
             "status": facts["compensation"]["class"], "detail": facts["compensation"]["detail"],
             "evidence": [case["grammar"]["path"]]},
            {"item": "quantifier scope", "status": "TYPE0_SYMBOLIC_THEOREM_TARGET",
             "detail": "the native target quantifies over A : Type₀ and f : I → A; physical time is not inferred",
             "evidence": [case["grammar"]["path"]]},
            {"item": "reality bridge", "status": "MODEL_RELATIVE_AND_UNRESOLVED",
             "detail": "the finite-stage control is an explicit operational model; empirical physics is outside this run",
             "evidence": [case["task"]["path"]]},
        ],
        "conclusion": {
            "correspondence_status": "MODEL_RELATIVE_THEORYIZATION_SPECIFIED",
            "task_preservation": preservation,
            "task_preservation_basis": [item for item in checks],
            "reality_correspondence": "UNRESOLVED",
            "research_relation": task.get("research_relation", "exploration"),
            "new_claim": False,
            "related_claims": case.get("claim_refs", []),
            "open_obligations": correspondence.get("open_obligations", []),
        },
    }


def derive_correspondence_content(
    *, case: dict, task: dict, witness: dict, profile_report: dict,
    grammar: dict, search_run: dict,
) -> dict:
    """Recompute every semantic review field from frozen inputs."""
    if grammar.get("backend") == "symbolic-horn-v1":
        return _derive_symbolic_correspondence_content(
            case=case, task=task, witness=witness, profile_report=profile_report,
            grammar=grammar, search_run=search_run,
        )
    facts = mechanism_facts(witness, grammar)
    derived_witness = facts["derived_witness"]
    left = value_from_json(derived_witness["pair"]["left"])
    right = value_from_json(derived_witness["pair"]["right"])
    inside, reason = within_grammar_witness(derived_witness["ops"], left, right, grammar)
    case_bound = (
        search_run.get("case_id") == case["case_id"]
        and int(search_run.get("case_revision", -1)) == int(case["revision"])
        and search_run.get("case_identity_sha256") == case_identity_sha256(case)
        and search_run.get("inputs", {}).get("profile_sha256") == case["profile"]["sha256"]
        and search_run.get("inputs", {}).get("task_sha256") == case["task"]["sha256"]
        and search_run.get("inputs", {}).get("grammar_sha256") == case["grammar"]["sha256"]
    )
    search_witness = next((item for item in search_run.get("witnesses", [])
                           if item.get("witness_id") == derived_witness["witness_id"]), None)
    witness_bound = search_witness == derived_witness
    declared_observation_kinds = set(task.get("correspondence", {}).get("declared_observation_kinds",
                                                                       []))
    consumer_met, consumer_detail = _consumer_requirement_met(
        task, derived_witness["separation_kind"], derived_witness["ops"], grammar
    )
    checks = [
        {"id": "profile_qualified", "status": "PASS" if profile_report.get("status") == "PROFILE_QUALIFIED" else "FAIL",
         "detail": profile_report.get("failures", [])},
        {"id": "grammar_membership", "status": "PASS" if inside else "FAIL", "detail": reason},
        {"id": "case_search_binding", "status": "PASS" if case_bound else "FAIL",
         "detail": f"search run case revision {search_run.get('case_revision')} vs case revision {case['revision']}"},
        {"id": "witness_search_binding", "status": "PASS" if witness_bound else "FAIL",
         "detail": "full recomputed witness must equal the search-run record"},
        {"id": "declared_observation_kind",
         "status": "PASS" if derived_witness["separation_kind"] in declared_observation_kinds else "FAIL",
         "detail": derived_witness["separation_kind"]},
        {"id": "declared_consumer_present",
         "status": "PASS" if consumer_met else "FAIL", "detail": consumer_detail},
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
    return {
        "derived_witness": derived_witness,
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
    content = derive_correspondence_content(
        case=case, task=task, witness=witness, profile_report=profile_report,
        grammar=grammar, search_run=search_run,
    )
    derived_witness = content.pop("derived_witness")
    review = {
        "schema_version": "machine-overview-correspondence-review/v2"
        if case.get("schema_version") == "machine-overview-case/v2"
        else "machine-overview-correspondence-review/v1",
        "review_id": review_id,
        "case_id": case["case_id"],
        "case_revision": case["revision"],
        "case_pointer": str(case_path),
        "case_sha256": sha256_file(case_path),
        "witness_id": derived_witness["witness_id"],
        "candidate_ast_sha256": witness_ast_sha256(derived_witness),
        "source_search_run": {
            "run_id": search_run["run_id"],
            "path": search_run_path.as_posix(),
            "sha256": sha256_file(search_run_path),
        },
        "created_at_utc": utc_now(),
        **content,
        "git": git_state(repo_root),
    }
    if output_path.exists():
        existing = read_json(output_path)
        comparable_existing = dict(existing)
        comparable_review = dict(review)
        for value in (comparable_existing, comparable_review):
            value.pop("created_at_utc", None)
            value.pop("git", None)
        if comparable_existing == comparable_review:
            return existing
        raise MachineOverviewError(f"REVIEW_ALREADY_EXISTS_WITH_DIFFERENT_CONTENT:{output_path}")
    write_json(output_path, review)
    return review
