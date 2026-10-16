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
        observation = grammar.get("observation_kind")
        if observation != "continuous_phase_obstruction":
            mechanisms = {
                "path_coherence_positive": {
                    "mechanism": (
                        "The task asks for endpoint Path coherence from an internal f : I → A. "
                        "The witness uses the declared interval-abstraction rule, so the generated Path "
                        "is the requested output rather than an added completion obligation."
                    ),
                    "class": "PATH_COHERENCE_MATCHES_DECLARED_TASK",
                    "detail": (
                        "The task and the representation both request a Path between the two endpoints; "
                        "no discrete event predicate is inferred from that Path."
                    ),
                },
                "explicit_event_boundary": {
                    "mechanism": (
                        "The witness combines separately declared start, finish and apartness facts over "
                        "an ordinary Stage carrier.  Exact completion remains an event-boundary observation "
                        "and does not require treating Stage as the cubical dimension."
                    ),
                    "class": "EXPLICIT_EVENT_STRUCTURE_PRESERVES_BOUNDARY",
                    "detail": (
                        "The event structure is part of the frozen task input and supplies exactly the "
                        "boundary distinctions consumed by the task."
                    ),
                },
                "finite_to_exact_candidate": {
                    "mechanism": (
                        "The symbolic witness applies the declared speculative finite-to-exact rule to "
                        "finite approximation evidence.  Symbolic typing alone does not establish that the "
                        "rule has a native Cubical inhabitant."
                    ),
                    "class": "SPECULATIVE_FINITE_TO_EXACT_RULE_REQUIRES_NATIVE_CHECK",
                    "detail": (
                        "Finite approximation is pre-kept by the task, while exact arrival requires an "
                        "additional rule whose validity is deliberately left to the native negative task."
                    ),
                },
                "local_to_global_completion_boundary": {
                    "mechanism": (
                        "The witness starts from the declared stagewise truncated limit, applies the "
                        "hypothetical recovery to obtain one compatible exact limit, and eliminates that "
                        "result with the pinned exact-limit emptiness proof."
                    ),
                    "class": "LOCAL_EXISTENCE_DOES_NOT_SUPPLY_COMPATIBLE_GLOBAL",
                    "detail": (
                        "Each stage retains mere local existence, while the requested global object adds one "
                        "cross-stage compatibility obligation that is not supplied by those local witnesses."
                    ),
                },
                "identity_observation_boundary": {
                    "mechanism": (
                        "The witness maps the pinned SIP/ua identification through a proposed Bool observer "
                        "and combines it with the observer's two endpoint specifications, forcing true ≡ false."
                    ),
                    "class": "SIP_IDENTIFICATION_BLOCKS_OUTSIDE_SIGNATURE_OBSERVATION",
                    "detail": (
                        "The structure identity preserves the declared signature.  Recovering the external "
                        "Bool observation requires enriching that signature, as shown by the positive control."
                    ),
                },
                "self_guarantee_diagonal_boundary": {
                    "mechanism": (
                        "The witness instantiates the proposed exact self-coding section at its diagonal "
                        "predicate, evaluates the resulting function path at the decoded self, and obtains a "
                        "Boolean fixed point of negation."
                    ),
                    "class": "EXACT_SELF_CODING_FORCES_BOOLEAN_FIXED_POINT",
                    "detail": (
                        "Checking one supplied proof remains available; the rejected strengthening is a total "
                        "section for every Boolean predicate over the same domain."
                    ),
                },
                "given_proof_check_capability": {
                    "mechanism": (
                        "The witness starts with one supplied derivation in the fixed ERCF-3 object syntax "
                        "and passes that same derivation through the declared checker.  It performs no proof "
                        "search, truth decision or self-reliability step."
                    ),
                    "class": "SUPPLIED_PROOF_CHECKED_WITHOUT_SEARCH",
                    "detail": (
                        "The proof object is already present before the checker runs; acceptance is not "
                        "evidence that an unknown proof can be found or that all true formulas are decidable."
                    ),
                },
                "bounded_proof_search_capability": {
                    "mechanism": (
                        "The witness executes the declared one-fuel search, checks its successful Boolean "
                        "result, and packages the result with a derivation of the fixed K-formula."
                    ),
                    "class": "FUEL_BOUND_SEARCH_WITH_SOUND_FOUND_RESULT",
                    "detail": (
                        "Fuel is an explicit input and zero fuel is a negative control.  The result makes no "
                        "claim about unbounded proof search or completeness for the object theory."
                    ),
                },
                "finite_truth_decision_capability": {
                    "mechanism": (
                        "The witness evaluates one closed formula in the explicitly finite Boolean fragment "
                        "and supplies the resulting equality certificate."
                    ),
                    "class": "FINITE_FRAGMENT_TRUTH_DECIDED",
                    "detail": (
                        "The evaluator is total only for the declared BFml fragment.  It is not a truth "
                        "predicate or theoremhood decider for ERCF-3, HoTT or the host proof assistant."
                    ),
                },
                "lob_self_certification_boundary": {
                    "mechanism": (
                        "The witness instantiates the internally certified reflection principle at bottom, "
                        "uses the declared Löb rule to obtain boxed bottom, and applies reflection."
                    ),
                    "class": "LOB_PLUS_REFLECTION_PLUS_INTERNAL_CERTIFICATION_COLLAPSES",
                    "detail": (
                        "All three assumptions must belong to one qualified consumer with the stated scope. "
                        "The source audit currently finds no HoTT consumer supplying that joint interface."
                    ),
                },
                "compensation_coherence_conflict": {
                    "mechanism": (
                        "The witness applies the declared endpoint-apartness compensation to the declared Path "
                        "compensation for the same endpoints.  Their individual outputs have incompatible joint "
                        "coherence requirements."
                    ),
                    "class": "COMPENSATIONS_REQUIRE_INCOMPATIBLE_COHERENCE",
                    "detail": (
                        "A Path repair and an exact-apartness repair can be exhibited separately in the controls, "
                        "but the same endpoints cannot carry both without contradiction."
                    ),
                },
            }
            selected = mechanisms.get(observation)
            if selected is None:
                classified = False
                selected = {
                    "mechanism": "The symbolic witness has no registered mechanism classification.",
                    "class": "UNRESOLVED",
                    "detail": "The observation kind is not registered by the correspondence derivation.",
                }
            return {
                "context_summary": [f"symbolic rule: {rule_id}" for rule_id in used_rules],
                "has_deadline": False,
                "has_race": False,
                "has_business_bind": False,
                "has_plain_bind": False,
                "mechanism": selected["mechanism"] if classified else "Required symbolic mechanism rules are absent.",
                "compensation": {
                    "class": selected["class"] if classified else "UNRESOLVED",
                    "detail": selected["detail"] if classified else "Required symbolic mechanism rules are absent.",
                },
                "derived_witness": derived,
            }
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
    preservation_label = correspondence.get(
        "preservation_label", "PRESERVED_ACROSS_DECLARED_ENDPOINT_OBSERVATION"
    )
    preservation = preservation_label if all(item["status"] == "PASS" for item in checks) else "REVIEW_REQUIRED"
    if observation == "continuous_phase_obstruction":
        checklist = [
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
        ]
        correspondence_status = "MODEL_RELATIVE_THEORYIZATION_SPECIFIED"
        reality_correspondence = "UNRESOLVED"
    else:
        native_contract = grammar.get("native_contract", {})
        checklist = [
            {"item": "original task and observation are declared before search",
             "status": "DECLARED", "evidence": [case["task"]["path"]]},
            {"item": "time structure is distinguished from temporal ordering",
             "status": "DECLARED", "detail": time_structure, "evidence": [case["task"]["path"]]},
            {"item": "the searched mechanism is localized to the declared symbolic rules",
             "status": facts["compensation"]["class"], "detail": facts["compensation"]["detail"],
             "evidence": [case["grammar"]["path"]]},
            {"item": "native target scope", "status": "DECLARED_NATIVE_TARGET",
             "detail": native_contract.get("target_scope"), "evidence": [case["grammar"]["path"]]},
            {"item": "reality bridge", "status": correspondence.get(
                "reality_bridge_status", "MODEL_RELATIVE_AND_UNRESOLVED"),
             "detail": correspondence.get(
                 "reality_bridge_detail", "the run checks a declared model; empirical reality is outside the kernel"),
             "evidence": [case["task"]["path"]]},
        ]
        correspondence_status = correspondence.get("correspondence_status", "MODEL_RELATIVE_TASK_SPECIFIED")
        reality_correspondence = correspondence.get("reality_correspondence", "UNRESOLVED")
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
        "checklist": checklist,
        "conclusion": {
            "correspondence_status": correspondence_status,
            "task_preservation": preservation,
            "task_preservation_basis": [item for item in checks],
            "reality_correspondence": reality_correspondence,
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
