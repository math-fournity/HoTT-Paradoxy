#!/usr/bin/env python3
"""Build and validate the CE-MAP eight-axis machine overview.

CE-MAP v1 is a closed-world registry over named, frozen project inputs.  It
does not infer mathematical semantics from words in filenames.  Known slices
are assigned through explicit ID sets; every other cell remains UNKNOWN or
NOT_APPLICABLE and is retained in UNCLASSIFIED.json.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable, Iterator


ROOT = Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "audit/ce-map"
IMPORT_DIR = ROOT / "audit/imports/machine-overview-ce-map-20260915"

MAP_SCHEMA = "hott-candidate-evidence-map/v1"
UNCLASSIFIED_SCHEMA = "hott-ce-map-unclassified/v1"
RECEIPT_SCHEMA = "hott-ce-map-receipt/v1"

AXES = (
    "TheoryConstruct",
    "AbstractionChange",
    "RealityOrTask",
    "ConsumerOrContext",
    "ObservationLayer",
    "CompletionProperty",
    "Oracle",
    "FrameworkOrModel",
)
UNKNOWN = "UNKNOWN"
NOT_APPLICABLE = "NOT_APPLICABLE"


def template(
    theory: str,
    change: str,
    reality: str,
    consumer: str,
    observation: str,
    completion: str,
    oracle: str,
    framework: str,
) -> dict[str, str]:
    return dict(zip(AXES, (theory, change, reality, consumer, observation, completion, oracle, framework), strict=True))


UNKNOWN_TEMPLATE = {axis: UNKNOWN for axis in AXES}
NA_TEMPLATE = {axis: NOT_APPLICABLE for axis in AXES}

TEMPLATES: dict[str, dict[str, str]] = {
    "ABSTRACT_FACTORISATION": template(
        "ABSTRACT_FACTORISATION",
        "INFORMATION_FORGETTING",
        "OBSERVABLE_RELATIVE_FORMAL_TASK",
        "ABSTRACT_OBSERVER",
        "KERNEL_PROPOSITIONAL_THEOREM",
        "FACTORIZATION_OR_NONRECOVERY",
        "NONE",
        "MIXED_MACHINE_PROOF_FRAMEWORKS",
    ),
    "PARTIALITY_TEMPORAL": template(
        "PARTIALITY_OR_DELAY",
        "SCHEDULE_OR_WITNESS_ERASURE",
        "FORMAL_TASK_REALITY_BRIDGE_UNRESOLVED",
        "DEADLINE_CONTINUATION_OR_CAUSAL_OBSERVER",
        "BOUNDED_OPERATIONAL_AND_KERNEL_OBSERVATION",
        "PARTIAL_OR_BOUNDED_COMPLETION",
        "FINITE_OBSERVATION_BOUND",
        "CUBICAL_AGDA",
    ),
    "REPRESENTATION_RECOVERY": template(
        "TRUNCATION_QUOTIENT_OR_REPRESENTATION",
        "WITNESS_OR_LABEL_ERASURE",
        "FORMAL_TASK_REALITY_BRIDGE_UNRESOLVED",
        "RECOVERY_OR_REPRESENTATION_CONSUMER",
        "KERNEL_PROPOSITIONAL_THEOREM",
        "NO_CANONICAL_RECOVERY",
        "NONE",
        "MIXED_AGDA_FRAMEWORKS",
    ),
    "VERIFICATION_EVENT": template(
        "PROOF_VERIFICATION_EVENT",
        "SOURCE_TO_REPLAY_TRANSLATION",
        "FORMAL_SAME_CLAIM_WITH_SCOPED_REPLAY",
        "PROOF_KERNEL",
        "KERNEL_ACCEPTANCE_AND_NEGATIVE_CONTROL",
        "FINITE_VERIFICATION_COMPLETES",
        "KERNEL",
        "CUBICAL_AGDA",
    ),
    "GODEL_INFRASTRUCTURE": template(
        "FORMAL_SYNTAX_AND_PROOF_CODE",
        "SYNTAX_TO_NUMERIC_ENCODING",
        "FORMAL_OBJECT_THEORY_ONLY",
        "PROOF_CHECKER_OR_DIAGONAL_CONSUMER",
        "KERNEL_PROPOSITIONAL_THEOREM",
        "FINITE_COMPONENT_TOTALITY_FULL_INCOMPLETENESS_OPEN",
        "NONE",
        "CUBICAL_AGDA",
    ),
    "COMPUTABILITY": template(
        "PROGRAM_CODE_AND_HALTING",
        "BOUNDED_TO_UNBOUNDED_OR_SYNTHETIC_REDUCTION",
        "FORMAL_COMPUTABILITY_TASK_REALITY_BRIDGE_UNRESOLVED",
        "INTERPRETER_ENUMERATOR_OR_DECIDER",
        "BOUNDED_EXECUTION_AND_KERNEL_THEOREM",
        "FIXED_DIVERGENCE_SEMI_DECISION_OR_UNDECIDABILITY",
        "NONE_OR_EXPLICIT_CT_EPF_SCT",
        "MIXED_CUBICAL_AGDA_AND_COQ",
    ),
    "HOTT_SYNTAX": template(
        "INTERNAL_TYPE_THEORY_SYNTAX",
        "GROUPOID_TO_SET_SYNTAX_COMPARISON",
        "FORMAL_OBJECT_THEORY_ONLY",
        "HOTT_METATHEORY_AND_REPRESENTABILITY",
        "KERNEL_PROPOSITIONAL_THEOREM",
        "EXACT_SLICE_REPLAY_FULL_R4_OPEN",
        "NONE",
        "CUBICAL_AGDA",
    ),
    "INTERNALISATION_MIXED": template(
        "FIBRATION_CLASSIFIER_OR_REPLACEMENT",
        "UNQUALIFIED_EXTERNAL_TO_INTERNAL_PROMOTION",
        "FORMAL_TASK_SCOPE_MIXED_WITHIN_PACKAGE",
        "FIBRATION_UNIVERSE_HIT_OR_INTERNAL_METATHEORY",
        "KERNEL_CONTRADICTION_AND_POSITIVE_CONTROLS",
        "COLLAPSE_OR_QUALIFIED_RECOVERY_MIXED",
        "EXPLICIT_MODAL_OR_FIBRANCY_STRUCTURE",
        "MIXED_2LTT_AGDA_FLAT_AND_COQ_ITT",
    ),
    "TRUNCATED_LIMIT_TASK": template(
        "TRUNCATED_LIMIT_OR_COMPLETION",
        "FINITE_WITNESS_TO_MERE_EXISTENCE",
        "FORMAL_TASK_REALITY_BRIDGE_UNRESOLVED",
        "LIMIT_CONSUMER",
        "FINITE_PREFIX_AND_KERNEL_OBSERVATION",
        "TRUNCATED_COMPLETION",
        "FINITE_OBSERVATION_BOUND",
        "CUBICAL_AGDA",
    ),
    "EVENT_BOUNDARY_TASK": template(
        "EVENT_BOUNDARY",
        "PROCESS_TO_STATIC_BOUNDARY",
        "FORMAL_TASK_REALITY_BRIDGE_UNRESOLVED",
        "EVENT_OBSERVER",
        "BOUNDED_OPERATIONAL_OBSERVATION",
        "BOUNDARY_COMPLETION",
        "FINITE_OBSERVATION_BOUND",
        "CUBICAL_AGDA",
    ),
    "FINITE_TO_EXACT_TASK": template(
        "CAUCHY_LIMIT_OR_EXACT_VALUE",
        "FINITE_APPROXIMATION_TO_EXACT_COMPLETION",
        "FORMAL_TASK_REALITY_BRIDGE_UNRESOLVED",
        "EXACT_LIMIT_CONSUMER",
        "FINITE_PREFIX_OBSERVATION",
        "EXACT_COMPLETION_FROM_FINITE_DATA",
        "MODULUS_OR_FINITE_BOUND",
        "CUBICAL_AGDA",
    ),
    "PHYSICAL_TIME_TASK": template(
        "INTERVAL_TIME_AND_MOTION",
        "NONCONTINUOUS_PROCESS_TO_DENSE_CONTINUUM",
        "PHYSICAL_REALITY_BRIDGE_REQUIRED",
        "MOTION_OR_EVENT_CONSUMER",
        "PHYSICAL_AND_FORMAL_OBSERVATION_MUST_BE_RELATED",
        "INFINITE_DIVISIBILITY_OR_COMPLETION",
        "UNKNOWN",
        "HOTT_OR_CUBICAL_MODEL_UNFIXED",
    ),
    "HIGHER_PATH_TASK": template(
        "HIGHER_PATH_AND_COHERENCE",
        "STRUCTURE_TO_IDENTITY_OR_PATH",
        "FORMAL_TASK_REALITY_BRIDGE_UNRESOLVED",
        "PATH_COHERENCE_CONSUMER",
        "KERNEL_PATH_THEOREM",
        "COHERENCE_COMPLETION",
        "NONE",
        "CUBICAL_AGDA",
    ),
    "SIP_TASK": template(
        "STRUCTURE_IDENTITY_PRINCIPLE",
        "EQUIVALENCE_TO_IDENTITY",
        "FORMAL_TASK_REALITY_BRIDGE_UNRESOLVED",
        "REPRESENTATION_SENSITIVE_CONSUMER",
        "KERNEL_PATH_THEOREM",
        "IDENTITY_TRANSFER",
        "NONE",
        "CUBICAL_AGDA",
    ),
    "PROOF_SEARCH_TASK": template(
        "FORMAL_PROOF_SYSTEM",
        "BOUNDED_SEARCH_TO_GLOBAL_CLAIM",
        "FORMAL_OBJECT_THEORY_ONLY",
        "PROOF_CHECKER_SEARCHER_OR_TRUTH_DECIDER",
        "META_OPERATIONAL_AND_KERNEL_OBSERVATION",
        "BOUNDED_SEARCH_OR_TOTAL_CHECKING",
        "FINITE_SEARCH_BOUND",
        "MIXED_COQ_AND_CUBICAL_AGDA",
    ),
    "SELF_REFERENCE_TASK": template(
        "SELF_REFERENCE_AND_PROVABILITY",
        "THEORY_TO_INTERNAL_SELF_CERTIFICATION",
        "FORMAL_OBJECT_THEORY_ONLY",
        "LOB_GODEL_OR_SELF_GUARANTEE_CONSUMER",
        "KERNEL_AND_META_PROOF_OBSERVATION",
        "INCOMPLETENESS_OR_UNPROVABILITY",
        "PROVABILITY_ORACLE_UNRESOLVED",
        "HOTT_CALCULUS_UNFIXED",
    ),
    "THEORY_ENRICHMENT_TASK": template(
        "THEORY_COMPENSATION_OR_ENRICHMENT",
        "FORGOTTEN_INFORMATION_TO_ADDED_STRUCTURE",
        "SAME_TASK_PRESERVATION_REQUIRED",
        "ENRICHED_THEORY_CONSUMER",
        "KERNEL_AND_CORRESPONDENCE_OBSERVATION",
        "COHERENCE_OF_COMPENSATION",
        "ADDED_INFORMATION",
        "HOTT_OR_CUBICAL_MODEL_UNFIXED",
    ),
    "COVERAGE_META": dict(NA_TEMPLATE),
}


PROOF_GROUPS: dict[str, set[str]] = {
    "ABSTRACT_FACTORISATION": {"MP-ERCF-001", "MP-ERCF-TRUNC-001"},
    "PARTIALITY_TEMPORAL": {
        "MP-RACE-TIMEOUT-001",
        "MP-CONTEXTUAL-EQUIV-001",
        "MP-QUOTIENT-MONAD-001",
        "MP-CONTEXT-CHARACTERIZATION-001",
        "MP-GUARD-ERASURE-001",
        "MP-COST-FACTORIZATION-001",
        "MP-PATH-CERTIFICATE-001",
        "MP-ONLINE-CAUSALITY-001",
        "MP-TRANSITION-LIFT-001",
        "MP-PARTIAL-DECISION-001",
    },
    "REPRESENTATION_RECOVERY": {
        "MP-SIP-REPRESENTATION-001",
        "MP-CAUCHY-MODULUS-001",
        "MP-TRUNC-NORECOVERY-001",
        "MP-NOCANONICAL-001",
        "MP-UNIMATH-NOSECTION-REPLAY-001",
    },
    "VERIFICATION_EVENT": {"MP-VERIFICATION-EVENT-001"},
    "GODEL_INFRASTRUCTURE": {
        "MP-ERCF3-T3-JOINT-001",
        "MP-ERCF3-T3-DECODING-001",
        "MP-ERCF3-T3-REPAIR-SPEC-001",
        "MP-ERCF3-T3-ARITH-TAGS-001",
        "MP-ERCF3-T3-BIT-CODING-001",
        "MP-ERCF3-T3-STREAMING-PARSER-001",
        "MP-ERCF3-T3-FORMULA-CODING-001",
        "MP-ERCF3-T3-REPAIRED-SYNTAX-001",
        "MP-ERCF3-T3-C168-COUNTERCHECK-001",
        "MP-ERCF3-T3-CODING-IMAGE-001",
    },
    "COMPUTABILITY": {
        "MP-CUBICAL-MACHINE-HALTING-001",
        "MP-CUBICAL-PROGRAM-CODE-001",
        "MP-CUBICAL-NAT-PROGRAM-CODE-001",
        "MP-CUBICAL-FAIR-ENUMERATION-001",
        "MP-CUBICAL-SEMI-HALTING-001",
        "MP-COQ-MM2-UNDECIDABILITY-REPLAY-001",
        "MP-CUBICAL-MM2-BRIDGE-001",
        "MP-COQ-MM2-PROGRAMCODE-BRIDGE-001",
        "MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001",
    },
    "HOTT_SYNTAX": {"MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001"},
    "INTERNALISATION_MIXED": {
        "MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001",
        "MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001",
        "MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001",
    },
}


MACHINE_TASK_GROUPS: dict[str, set[str]] = {
    "PARTIALITY_TEMPORAL": {
        "MS-TASK-L1-RACE-COMPLETION-001",
        "MS-TASK-L1-RACE-COMPLETION-002",
    },
    "TRUNCATED_LIMIT_TASK": {"MS-TASK-L2-TRUNCATED-LIMIT-001"},
    "EVENT_BOUNDARY_TASK": {"MS-TASK-L3-EXPLICIT-EVENT-BOUNDARY-001"},
    "FINITE_TO_EXACT_TASK": {"MS-TASK-L3-FINITE-TO-EXACT-001"},
    "PHYSICAL_TIME_TASK": {"MS-TASK-L3-INTERVAL-COMPLETION-001"},
    "HIGHER_PATH_TASK": {"MS-TASK-L3-PATH-COHERENCE-POSITIVE-001"},
    "SIP_TASK": {"MS-TASK-L4-SIP-OBSERVATION-001"},
    "PROOF_SEARCH_TASK": {
        "MS-TASK-L5-BOUNDED-PROOF-SEARCH-001",
        "MS-TASK-L5-FINITE-TRUTH-DECISION-001",
        "MS-TASK-L5-GIVEN-PROOF-CHECK-001",
    },
    "SELF_REFERENCE_TASK": {
        "MS-TASK-L5-LOB-SELF-CERTIFICATION-001",
        "MS-TASK-L5-SELF-GUARANTEE-001",
    },
    "THEORY_ENRICHMENT_TASK": {"MS-TASK-L6-COMPENSATION-COHERENCE-001"},
}


EVALUATION_GROUPS: dict[str, set[str]] = {
    "PROOF_SEARCH_TASK": {"COQ-HOTT-REFLECTIVE-TYPECLASS-RECURSION-001"},
    "GODEL_INFRASTRUCTURE": {
        "COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001",
        "CUBICAL-GODEL-PROOF-CHECKER-001",
        "CUBICAL-SYNTHETIC-INCOMPLETENESS-001",
        "HOTT-QUOTATION-BRIDGE-001",
    },
    "COMPUTABILITY": {"CUBICAL-MACHINE-HALTING-001"},
    "PARTIALITY_TEMPORAL": {
        "REFLECTED-TICK-REDUCTION-OBSERVER-001",
        "TICK-IRRELEVANCE-OPERATIONAL-GAP-001",
    },
    "COVERAGE_META": {
        "CUBICAL-CANDIDATE-COVERAGE-001",
        "L3-ENGINE-FREEZE-001",
        "L3-NATURAL-CONSUMER-AUDIT-001",
        "L5-CONSUMER-QUALIFICATION-001",
        "M3-BREADTH-001",
        "M4-LITE-L3-001",
        "NONTERMINATION-OVERVIEW-COMPLETENESS-AUDIT-001",
    },
}


NON_MATHEMATICAL_STATE_KINDS = {
    "active_goal",
    "ai_communication_contract",
    "coordination_decision",
    "core_generation_migration",
    "cross_source_reconciliation",
    "derived_development_audit",
    "direction_review",
    "evidence_drift",
    "evidence_hygiene_and_sample",
    "evidence_queue_sample_review",
    "evidence_sample",
    "evidence_sample_and_caliber",
    "evidence_sample_and_library_read",
    "fresh_runtime_verification",
    "governance_gap",
    "governance_release",
    "governance_repair",
    "governance_requirement",
    "governance_runtime_repair",
    "governance_upgrade",
    "handoff_report",
    "historical_audit",
    "historical_claim_review",
    "historical_governance_evidence_gap",
    "integrated_direction_projection",
    "integrated_outcome_panorama",
    "proof_version_closure",
    "provenance_label_correction",
    "understanding_chapter_reconciliation",
    "machine_overview_coverage_task",
}


CLAIM_OVERRIDES: dict[str, tuple[str, dict[str, str]]] = {
    "C-227": ("strict outer loop canonicalisation", template("STRICT_OUTER_EQUALITY", "OUTER_STRICT_TO_INNER_IDENTITY_ENCODING", "FORMAL_CONDITIONAL_TASK", "FIBRANT_REPLACEMENT", "KERNEL_PROPOSITIONAL_EQUALITY", "UIP_COLLAPSE_PRECURSOR", "OUTER_UIP_ASSUMPTION", "CUBICAL_AGDA_2LTT_ENCODING")),
    "C-228": ("context-uniform replacement lifts a path-dependent strict witness", template("FIBRANT_REPLACEMENT", "EXTERNAL_POINTWISE_TO_CONTEXT_UNIFORM_INTERNAL", "TASK_SCOPE_WIDENED", "INTERNAL_HOTT_METATHEORY", "KERNEL_PROPOSITIONAL_THEOREM", "CONTEXT_UNIFORM_CAPABILITY", "OUTER_UIP_ASSUMPTION", "CUBICAL_AGDA_2LTT_ENCODING")),
    "C-229": ("the replacement fragment contracts inner identity proofs", template("INNER_IDENTITY_TYPE", "EXTERNAL_POINTWISE_TO_CONTEXT_UNIFORM_INTERNAL", "TASK_SCOPE_WIDENED", "INTERNAL_HOTT_METATHEORY", "KERNEL_PROPOSITIONAL_THEOREM", "UIP_COLLAPSE", "OUTER_UIP_ASSUMPTION", "CUBICAL_AGDA_2LTT_ENCODING")),
    "C-230": ("a nontrivial inner loop is incompatible with the fragment", template("NONTRIVIAL_INNER_LOOP", "EXTERNAL_POINTWISE_TO_CONTEXT_UNIFORM_INTERNAL", "TASK_SCOPE_WIDENED", "INTERNAL_HOTT_METATHEORY", "KERNEL_CONTRADICTION", "CONTRADICTION_FROM_ASSUMPTIONS", "OUTER_UIP_ASSUMPTION", "CUBICAL_AGDA_2LTT_ENCODING")),
    "C-231": ("native circle loop is a nontriviality control", template("CIRCLE_HIGHER_PATH", "NO_ABSTRACTION_CHANGE_CONTROL", "FORMAL_CONTROL", "NATIVE_HOTT_PATH_CONSUMER", "KERNEL_PATH_INEQUALITY", "NONTRIVIAL_LOOP_PRESERVED", "NONE", "CUBICAL_AGDA")),
    "C-232": ("removing the strict bridge admits identity replacement", template("NATIVE_IDENTITY_REPLACEMENT", "STRICT_BRIDGE_REMOVED", "QUALIFIED_TASK_COMPLETED", "NATIVE_HOTT_REPLACEMENT", "KERNEL_POSITIVE_CONTROL", "DEPENDENT_ELIMINATION_AVAILABLE", "NONE", "CUBICAL_AGDA")),
    "C-233": ("LOPS source and historical toolchain qualification", dict(NA_TEMPLATE)),
    "C-234": ("ordinary internal classifier promotes fiberwise to familywise fibrancy", template("INTERNAL_FIBRATION_CLASSIFIER", "FIBERWISE_TO_FAMILYWISE_AND_GLOBAL_TO_LOCAL", "TASK_SCOPE_WIDENED", "FIBRATION_UNIVERSE_CLASSIFIER", "KERNEL_CONTRADICTION", "INTERVAL_COLLAPSE", "UNQUALIFIED_LOCAL_SUBSTITUTION", "AGDA_FLAT_ORDINARY_INTERNAL_TT")),
    "C-235": ("CCHM and CTT classifier instances", template("INTERNAL_FIBRATION_CLASSIFIER", "FIBERWISE_TO_FAMILYWISE_AND_GLOBAL_TO_LOCAL", "TASK_SCOPE_WIDENED", "CCHM_AND_CARTESIAN_CUBICAL_UNIVERSES", "KERNEL_CONTRADICTION", "INTERVAL_COLLAPSE", "UNQUALIFIED_LOCAL_SUBSTITUTION", "AGDA_FLAT_ORDINARY_INTERNAL_TT")),
    "C-236": ("crisp classifier restricts inputs to global data", template("CRISP_FIBRATION_CLASSIFIER", "LOCAL_TO_CRISP_GLOBAL_RESTRICTION", "QUALIFIED_TASK_COMPLETED", "FIBRATION_UNIVERSE_CLASSIFIER", "KERNEL_CONSTRUCTION", "CLASSIFIER_CONSTRUCTED", "TINY_INTERVAL_RIGHT_ADJOINT", "AGDA_FLAT_CRISP_MODAL_TT")),
    "C-237": ("modal control rejects local classifier input", template("CRISP_MODAL_TYPING", "LOCAL_INPUT_REJECTED", "QUALIFICATION_ENFORCED", "FIBRATION_UNIVERSE_CLASSIFIER", "TYPECHECK_ACCEPT_REJECT_CONTROL", "LOCAL_SCOPE_PROMOTION_BLOCKED", "CRISP_GLOBAL_CONTEXT", "AGDA_FLAT_CRISP_MODAL_TT")),
    "C-238": ("relative universes and fibration-notion morphisms", template("RELATIVE_FIBRATION_UNIVERSE", "GLOBAL_QUALIFIED_INTERNALISATION", "QUALIFIED_TASK_COMPLETED", "RELATIVE_UNIVERSE_CONSUMER", "KERNEL_CONSTRUCTION", "UNIVERSE_MORPHISM_CONSTRUCTED", "CRISP_UNIVERSE_POSTULATES", "AGDA_FLAT_CRISP_MODAL_TT")),
    "C-239": ("interval type theory source and toolchain qualification", dict(NA_TEMPLATE)),
    "C-240": ("regular replacement for every open family derives contradiction", template("REGULAR_FIBRANT_REPLACEMENT", "POINTWISE_TO_OPEN_FAMILY_REGULARITY", "TASK_SCOPE_WIDENED", "HIT_AND_MODEL_STRUCTURE_CONSUMER", "KERNEL_CONTRADICTION", "CONTRADICTION_FROM_ASSUMPTIONS", "UNQUALIFIED_REGULAR_FIBRANCY", "COQ_INTERVAL_TYPE_THEORY")),
    "C-241": ("actual QIT replacement supplies degenerate fibrancy", template("DEGENERATE_FIBRANT_REPLACEMENT", "REGULAR_TO_DEGENERATE_RESTRICTION", "QUALIFIED_TASK_COMPLETED", "HIT_AND_MODEL_STRUCTURE_CONSUMER", "KERNEL_CONSTRUCTION", "DEGENERATE_COMPOSITION_CONSTRUCTED", "QIT_REDUCTION_ASSUMPTIONS", "COQ_INTERVAL_TYPE_THEORY")),
    "C-242": ("regular fibrancy decomposes into degenerate fibrancy plus transport", template("FIBRANCY_DECOMPOSITION", "REGULAR_TO_DEGENERATE_PLUS_TRANSPORT", "TASK_DECOMPOSED_WITH_EXPLICIT_PAYMENT", "HIT_AND_MODEL_STRUCTURE_CONSUMER", "KERNEL_EQUIVALENCE_COMPONENTS", "REGULARITY_RECOVERED_WITH_TRANSPORT", "TRANSPORT_STRUCTURE", "COQ_INTERVAL_TYPE_THEORY")),
    "C-243": ("replacement elimination keeps motive and context qualifications", template("REPLACEMENT_ELIMINATOR", "OPEN_TO_QUALIFIED_OR_EMPTY_CONTEXT", "QUALIFICATION_ENFORCED", "HIT_AND_MODEL_STRUCTURE_CONSUMER", "KERNEL_ASSUMPTION_AUDIT", "ELIMINATION_AVAILABLE_WITH_RESTRICTION", "EXTENSION_RULE_EMPTY_CONTEXT", "COQ_INTERVAL_TYPE_THEORY")),
}


STATE_MANUAL_TEMPLATES = {
    "A-NATURAL-CONSUMER-2LTT-REPLACEMENT-002": "INTERNALISATION_MIXED",
    "A-G-HOTT-SYNTAX-001": "HOTT_SYNTAX",
    "A-CAND-2LTT-FIBRANT-REPLACEMENT-UIP-001": "INTERNALISATION_MIXED",
    "A-NATURAL-CONSUMER-AUDIT-001": "COVERAGE_META",
    "A-HOTT-PROGRAMMATIC-COMPLETENESS-001": "COVERAGE_META",
    "A-LIT-DENOMINATOR-001": "COVERAGE_META",
    "A-LIT-CLASSICS-001": "COVERAGE_META",
    "A-LIT-HOTT-COMPUTABILITY-001": "COVERAGE_META",
    "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001": "COVERAGE_META",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def clone_axes(value: dict[str, str]) -> dict[str, str]:
    return {axis: value[axis] for axis in AXES}


def normalize_claim_id(number: int) -> str:
    return f"C-{number:02d}"


def expand_claims(value: str) -> list[str]:
    text = value.replace("–", "..").replace("—", "..")
    range_match = re.fullmatch(r"\s*C-(\d+)\s*\.\.\s*C-(\d+)\s*", text)
    if range_match:
        first, last = map(int, range_match.groups())
        if first > last:
            raise ValueError(f"REVERSED_CLAIM_RANGE:{value}")
        return [normalize_claim_id(number) for number in range(first, last + 1)]
    single = re.fullmatch(r"\s*C-(\d+)\s*", text)
    if single:
        return [normalize_claim_id(int(single.group(1)))]
    raise ValueError(f"UNKNOWN_CLAIM_RANGE:{value}")


def matrix_claim_rows(path: Path) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        match = re.match(r"^\|\s*(C-\d+)\s*\|", line)
        if not match:
            continue
        parts = [part.strip() for part in line.split("|")]
        if len(parts) < 6:
            raise ValueError(f"MALFORMED_MATRIX_ROW:{line_number}")
        claim_id = normalize_claim_id(int(match.group(1).split("-")[1]))
        row = {"claim": parts[2], "status": parts[3], "line": str(line_number)}
        if claim_id in rows and rows[claim_id] != row:
            raise ValueError(f"DUPLICATE_MATRIX_CLAIM:{claim_id}")
        rows[claim_id] = row
    return rows


def flatten_strings(value: Any) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, child in value.items():
            yield str(key)
            yield from flatten_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from flatten_strings(child)


def keyed_values(value: Any, keys: set[str]) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key in keys and isinstance(child, str):
                found.add(child)
            found.update(keyed_values(child, keys))
    elif isinstance(value, list):
        for child in value:
            found.update(keyed_values(child, keys))
    return found


def group_for(source_id: str, groups: dict[str, set[str]]) -> str | None:
    matches = [name for name, ids in groups.items() if source_id in ids]
    if len(matches) > 1:
        raise ValueError(f"MULTIPLE_CURATED_GROUPS:{source_id}:{matches}")
    return matches[0] if matches else None


def framework_for_package(package: dict[str, Any], axes: dict[str, str]) -> None:
    proof_id = package["proof_id"]
    source = str(package.get("source", ""))
    if proof_id == "MP-ERCF-001":
        axes["FrameworkOrModel"] = "LEAN4"
    elif proof_id == "MP-UNIMATH-NOSECTION-REPLAY-001":
        axes["FrameworkOrModel"] = "AGDA_UNIMATH"
    elif proof_id == "MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001":
        axes["FrameworkOrModel"] = "AGDA_FLAT_CRISP_AND_ORDINARY_TT"
    elif proof_id == "MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001":
        axes["FrameworkOrModel"] = "COQ_INTERVAL_TYPE_THEORY"
    elif source.endswith(".v"):
        axes["FrameworkOrModel"] = "COQ_CIC"
    elif source.endswith(".lean"):
        axes["FrameworkOrModel"] = "LEAN4"
    elif source.endswith(".agda"):
        axes["FrameworkOrModel"] = "CUBICAL_AGDA"


def make_item(
    namespace: str,
    source_id: str,
    paths: Iterable[str],
    axes: dict[str, str],
    assignment: str,
    **extra: Any,
) -> dict[str, Any]:
    if not source_id:
        raise ValueError(f"EMPTY_SOURCE_ID:{namespace}")
    if set(axes) != set(AXES) or any(not isinstance(axes[a], str) or not axes[a] for a in AXES):
        raise ValueError(f"INCOMPLETE_AXES:{namespace}:{source_id}")
    item = {
        "id": f"{namespace}:{source_id}",
        "namespace": namespace,
        "source_id": source_id,
        "source_paths": sorted(set(paths)),
        "axes": clone_axes(axes),
        "assignment": assignment,
        "unknown_axes": [axis for axis in AXES if axes[axis] == UNKNOWN],
        "class_ids": [],
        "related_ids": [],
    }
    item.update(extra)
    return item


def validate_import() -> tuple[dict[str, Any], dict[str, Any]]:
    manifest = json.loads((IMPORT_DIR / "IMPORT.json").read_text(encoding="utf-8"))
    catalog = json.loads((IMPORT_DIR / "CATALOG.json").read_text(encoding="utf-8"))
    if manifest.get("schema_version") != "machine-overview-ce-map-import/v1":
        raise ValueError("MACHINE_IMPORT_SCHEMA")
    errors: list[str] = []
    for row in manifest["documents"]:
        path = IMPORT_DIR / row["imported_path"]
        if not path.is_file():
            errors.append(f"missing:{row['imported_path']}")
            continue
        data = path.read_bytes()
        if len(data) != row["bytes"] or sha256(data) != row["sha256"]:
            errors.append(f"drift:{row['imported_path']}")
    if sha256(json_bytes(catalog)) != manifest["catalog_sha256"]:
        errors.append("catalog")
    if errors:
        raise ValueError("MACHINE_IMPORT_INVALID:" + ",".join(errors))
    return manifest, catalog


def logical_paths(index_rel: str) -> list[str]:
    index = ROOT / index_rel
    paths = [index_rel]
    shard_dir = index.with_suffix("")
    if shard_dir.is_dir():
        paths.extend(path.relative_to(ROOT).as_posix() for path in sorted(shard_dir.glob("*.md")))
    return paths


def source_set() -> list[dict[str, Any]]:
    paths = [
        "HoTT/verification/PROOF_VERSION_CLOSURE.json",
        "HoTT/CLAIM_EVIDENCE_MATRIX.md",
        ".codex/research/hott/STATE.json",
        ".codex/research/hott/CE-MAP-001.md",
        ".codex/research/hott/R3-R4-GODEL-RETURN-001.md",
        "goal.md",
        "scripts/audit/build_ce_map.py",
        "scripts/audit/test_ce_map.py",
        "audit/imports/machine-overview-ce-map-20260915/IMPORT.json",
        "audit/imports/machine-overview-ce-map-20260915/CATALOG.json",
    ]
    for logical in (
        ".codex/research/hott/LIT-DENOMINATOR-001.md",
        ".codex/research/hott/LIT-CLASSICS-001.md",
        ".codex/research/hott/LIT-HOTT-COMPUTABILITY-001.md",
        "全景视野.md",
    ):
        paths.extend(logical_paths(logical))
    rows = []
    for rel in sorted(set(paths)):
        path = ROOT / rel
        if not path.is_file():
            raise ValueError(f"SOURCE_MISSING:{rel}")
        data = path.read_bytes()
        rows.append({"path": rel, "bytes": len(data), "sha256": sha256(data)})
    return rows


def proof_items(reverse: bool = False) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    closure_path = ROOT / "HoTT/verification/PROOF_VERSION_CLOSURE.json"
    matrix_path = ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md"
    closure = json.loads(closure_path.read_text(encoding="utf-8"))
    packages = list(closure["packages"]) + list(closure["later_packages"])
    if reverse:
        packages.reverse()
    expected_ids = {package["proof_id"] for package in packages}
    assigned_ids = set().union(*PROOF_GROUPS.values())
    if expected_ids != assigned_ids:
        raise ValueError(
            "PROOF_GROUP_REMAINDER:missing="
            + repr(sorted(expected_ids - assigned_ids))
            + ":extra="
            + repr(sorted(assigned_ids - expected_ids))
        )
    matrix = matrix_claim_rows(matrix_path)
    items: list[dict[str, Any]] = []
    package_by_id: dict[str, dict[str, Any]] = {}
    claim_owner: dict[str, str] = {}
    for package in packages:
        proof_id = package["proof_id"]
        group = group_for(proof_id, PROOF_GROUPS)
        if group is None:
            raise ValueError(f"UNMAPPED_PROOF_PACKAGE:{proof_id}")
        axes = clone_axes(TEMPLATES[group])
        framework_for_package(package, axes)
        claims = expand_claims(package["claim_ids"])
        for claim_id in claims:
            if claim_id in claim_owner:
                raise ValueError(f"CLAIM_HAS_TWO_PACKAGES:{claim_id}")
            if claim_id not in matrix:
                raise ValueError(f"CLAIM_NOT_IN_MATRIX:{claim_id}")
            claim_owner[claim_id] = proof_id
        package_by_id[proof_id] = package
        items.append(
            make_item(
                "proof_package",
                proof_id,
                [package["source"], package["run"], "HoTT/verification/PROOF_VERSION_CLOSURE.json"],
                axes,
                f"CURATED_PROOF_GROUP:{group}",
                claim_ids=claims,
                evidence_status=package.get("verdict", package.get("kind", UNKNOWN)),
                lifecycle_status="FROZEN_PROOF_PACKAGE",
            )
        )
        for claim_id in claims:
            if claim_id in CLAIM_OVERRIDES:
                rationale, claim_axes = CLAIM_OVERRIDES[claim_id]
                assignment = "CURATED_CLAIM_OVERRIDE"
            else:
                rationale, claim_axes = f"inherits scoped package {proof_id}", axes
                assignment = f"INHERITED_FROM_PROOF_PACKAGE:{proof_id}"
            items.append(
                make_item(
                    "proof_claim",
                    claim_id,
                    ["HoTT/CLAIM_EVIDENCE_MATRIX.md", package["source"], package["run"]],
                    claim_axes,
                    assignment,
                    proof_id=proof_id,
                    rationale=rationale,
                    evidence_status=matrix[claim_id]["status"],
                    matrix_line=int(matrix[claim_id]["line"]),
                    lifecycle_status="FROZEN_CLAIM",
                )
            )
    return items, package_by_id


def linked_proof_id(record: dict[str, Any], packages: dict[str, dict[str, Any]]) -> str | None:
    declared = record.get("proof_id")
    if isinstance(declared, str) and declared in packages:
        return declared
    declared_claims = {
        normalize_claim_id(int(match.group(1)))
        for value in record.get("claim_ids", [])
        if isinstance(value, str)
        for match in [re.fullmatch(r"C-(\d+)", value)]
        if match
    }
    if declared_claims:
        claim_matches = {
            proof_id
            for proof_id, package in packages.items()
            if declared_claims <= set(expand_claims(package["claim_ids"]))
        }
        if len(claim_matches) == 1:
            return next(iter(claim_matches))
    strings = list(flatten_strings(record))
    matches: set[str] = set()
    for proof_id, package in packages.items():
        source_dir = str(Path(package["source"]).parent)
        run = str(package["run"])
        if any(proof_id in text or text.startswith(source_dir + "/") or text.startswith(run + "/") or text == run for text in strings):
            matches.add(proof_id)
    return next(iter(matches)) if len(matches) == 1 else None


def state_items(packages: dict[str, dict[str, Any]], proof_axis: dict[str, dict[str, str]], reverse: bool = False) -> list[dict[str, Any]]:
    path = ROOT / ".codex/research/hott/STATE.json"
    state = json.loads(path.read_text(encoding="utf-8"))
    if state.get("revision") != 149:
        raise ValueError(f"CE_MAP_V1_REQUIRES_STATE_REVISION_149:{state.get('revision')}")
    records = [(record_id, record) for record_id, record in state["records"].items() if record.get("kind") != "session"]
    if reverse:
        records.reverse()
    items = []
    for record_id, record in records:
        kind = record.get("kind", UNKNOWN)
        linked = linked_proof_id(record, packages)
        if linked:
            axes = proof_axis[linked]
            assignment = f"INHERITED_FROM_LINKED_PROOF_PACKAGE:{linked}"
        elif record_id in STATE_MANUAL_TEMPLATES:
            group = STATE_MANUAL_TEMPLATES[record_id]
            axes = TEMPLATES[group]
            assignment = f"CURATED_STATE_TEMPLATE:{group}"
        elif kind in NON_MATHEMATICAL_STATE_KINDS:
            axes = NA_TEMPLATE
            assignment = f"NOT_APPLICABLE_STATE_KIND:{kind}"
        else:
            axes = UNKNOWN_TEMPLATE
            assignment = f"EXPLICIT_UNKNOWN_STATE_KIND:{kind}"
        items.append(
            make_item(
                "state_record",
                record_id,
                [".codex/research/hott/STATE.json", record.get("path", "")],
                axes,
                assignment,
                record_kind=kind,
                lifecycle_status=record.get("lifecycle_status", record.get("status", UNKNOWN)),
                evidence_status=record.get("evidence_status", UNKNOWN),
                linked_proof_id=linked,
            )
        )
    return items


def load_imported_json(rel: str) -> Any:
    return json.loads((IMPORT_DIR / rel).read_text(encoding="utf-8"))


def machine_items(reverse: bool = False) -> list[dict[str, Any]]:
    _, catalog = validate_import()
    tasks = list(catalog["tasks"])
    cases = list(catalog["cases"])
    evaluations = list(catalog["evaluations"])
    runs = list(catalog["runs"])
    reviews = list(catalog["reviews"])
    if reverse:
        for values in (tasks, cases, evaluations, runs, reviews):
            values.reverse()
    expected_tasks = {row["source_id"] for row in tasks}
    assigned_tasks = set().union(*MACHINE_TASK_GROUPS.values())
    if expected_tasks != assigned_tasks:
        raise ValueError(f"MACHINE_TASK_GROUP_REMAINDER:{sorted(expected_tasks ^ assigned_tasks)}")
    expected_evals = {row["source_id"] for row in evaluations}
    assigned_evals = set().union(*EVALUATION_GROUPS.values())
    if expected_evals != assigned_evals:
        raise ValueError(f"EVALUATION_GROUP_REMAINDER:{sorted(expected_evals ^ assigned_evals)}")

    items: list[dict[str, Any]] = []
    task_axes: dict[str, dict[str, str]] = {}
    for row in tasks:
        source_id = row["source_id"]
        group = group_for(source_id, MACHINE_TASK_GROUPS)
        assert group is not None
        axes = TEMPLATES[group]
        task_axes[source_id] = axes
        data = load_imported_json(row["path"])
        items.append(
            make_item(
                "machine_task",
                source_id,
                [f"audit/imports/machine-overview-ce-map-20260915/{row['path']}"],
                axes,
                f"CURATED_MACHINE_TASK_GROUP:{group}",
                lifecycle_status="FROZEN_TASK_SPEC",
                evidence_status=data.get("schema_version", UNKNOWN),
                declared_observation=data.get("observation"),
                declared_completion=data.get("completion"),
            )
        )
    for row in cases:
        source_id = row["source_id"]
        axes = task_axes.get(source_id, UNKNOWN_TEMPLATE)
        items.append(
            make_item(
                "machine_case",
                source_id,
                [f"audit/imports/machine-overview-ce-map-20260915/{row['path']}"],
                axes,
                f"INHERITED_FROM_MACHINE_TASK:{source_id}" if source_id in task_axes else "EXPLICIT_UNKNOWN_PARENT_TASK",
                lifecycle_status="FROZEN_LATEST_CASE_REVISION",
                evidence_status=row.get("schema_version", UNKNOWN),
            )
        )

    eval_axes: dict[str, dict[str, str]] = {}
    for row in evaluations:
        source_id = row["source_id"]
        group = group_for(source_id, EVALUATION_GROUPS)
        assert group is not None
        axes = TEMPLATES[group]
        eval_axes[source_id] = axes
        items.append(
            make_item(
                "machine_evaluation",
                source_id,
                [f"audit/imports/machine-overview-ce-map-20260915/{p}" for p in row["paths"]],
                axes,
                f"CURATED_EVALUATION_GROUP:{group}",
                lifecycle_status="FROZEN_EVALUATION",
                evidence_status="SOURCE_MANIFESTS_AND_REPORT_FROZEN",
            )
        )

    known_task_ids = set(task_axes)
    known_eval_ids = set(eval_axes)
    for namespace, rows in (("machine_run", runs), ("machine_review", reviews)):
        for row in rows:
            data = load_imported_json(row["path"])
            refs = keyed_values(data, {"task_id", "case_id", "evaluation_id", "audit_id"})
            task_matches = sorted(refs & known_task_ids)
            eval_matches = sorted(refs & known_eval_ids)
            path_parts = Path(row["path"]).parts
            if len(path_parts) >= 3 and path_parts[1] == "evaluations" and path_parts[2] in known_eval_ids:
                eval_matches = sorted(set(eval_matches) | {path_parts[2]})
            parents = [("task", value, task_axes[value]) for value in task_matches] + [
                ("evaluation", value, eval_axes[value]) for value in eval_matches
            ]
            if len(parents) == 1:
                parent_kind, parent_id, axes = parents[0]
                assignment = f"INHERITED_FROM_MACHINE_{parent_kind.upper()}:{parent_id}"
            else:
                axes = UNKNOWN_TEMPLATE
                assignment = "EXPLICIT_UNKNOWN_NO_UNIQUE_STRUCTURED_PARENT"
            items.append(
                make_item(
                    namespace,
                    row["source_id"],
                    [f"audit/imports/machine-overview-ce-map-20260915/{row['path']}"],
                    axes,
                    assignment,
                    lifecycle_status="FROZEN_RUN_OR_REVIEW",
                    evidence_status=row.get("schema_version", UNKNOWN),
                    parent_refs=sorted(refs),
                )
            )
    return items


def class_definitions() -> list[dict[str, Any]]:
    return [
        {
            "id": "CE-CLASS-UNQUALIFIED-INTERNALISATION-001",
            "class_kind": "MECHANISM_PATTERN_CLASS",
            "representative": "proof_claim:C-234",
            "members": [
                "proof_claim:C-228",
                "proof_claim:C-229",
                "proof_claim:C-230",
                "proof_claim:C-234",
                "proof_claim:C-235",
                "proof_claim:C-240",
            ],
            "shared_pattern": "an external, pointwise, fiberwise, or otherwise qualified capability is promoted to local/open/context-uniform internal use without preserving its qualification",
            "reduction_status": "PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE",
            "preservation": {
                "abstraction_shape": "PRESERVED_AT_HIGH_LEVEL",
                "reality_or_task_scope_widening": "PRESERVED",
                "input_domain_qualification_loss": "PRESERVED",
            },
            "anti_preservation": {
                "consumer": "NOT_PRESERVED: internal metatheory, universe classification, and HIT/model structure differ",
                "observation": "NOT_PRESERVED: UIP, interval collapse, and False are different consequences",
                "completion": "NOT_PRESERVED",
                "framework": "NOT_PRESERVED",
            },
            "counting_rule": "Count one search mechanism family while retaining every theorem and consumer as a distinct evidence item.",
            "evidence_refs": [
                "HoTT/CLAIM_EVIDENCE_MATRIX.md#C-227-C-243",
                "audit/2LTT纤维替换自然消费者与crisp退化纤维性消融-20260915.md",
            ],
        },
        {
            "id": "CE-CLASS-QUALIFIED-INTERNALISATION-DEFENSE-001",
            "class_kind": "DEFENSE_PATTERN_CLASS",
            "representative": "proof_claim:C-237",
            "members": [
                "proof_claim:C-232",
                "proof_claim:C-236",
                "proof_claim:C-237",
                "proof_claim:C-241",
                "proof_claim:C-242",
                "proof_claim:C-243",
            ],
            "shared_pattern": "restore the intended construction by retaining a global/crisp/context boundary or decomposing regular capability into degenerate structure plus transport",
            "reduction_status": "RELATED_DEFENSES_NOT_A_SINGLE_EQUIVALENCE",
            "preservation": {"explicit_payment": "PRESERVED", "qualified_task_completion": "PRESERVED"},
            "anti_preservation": {
                "payment": "NOT_PRESERVED: strict bridge removal, modal crispness, transport, and empty-context extension differ",
                "consumer": "NOT_PRESERVED",
                "framework": "NOT_PRESERVED",
            },
            "counting_rule": "Treat defenses as one design family for coverage, but test each payment against its own consumer.",
            "evidence_refs": [
                "HoTT/CLAIM_EVIDENCE_MATRIX.md#C-232-C-243",
                "audit/2LTT纤维替换自然消费者与crisp退化纤维性消融-20260915.md",
            ],
        },
    ]


def apply_classes(items: list[dict[str, Any]], classes: list[dict[str, Any]]) -> None:
    by_id = {item["id"]: item for item in items}
    for cls in classes:
        if cls["representative"] not in cls["members"]:
            raise ValueError(f"CLASS_REPRESENTATIVE_NOT_MEMBER:{cls['id']}")
        for member in cls["members"]:
            if member not in by_id:
                raise ValueError(f"CLASS_MEMBER_MISSING:{cls['id']}:{member}")
            by_id[member]["class_ids"].append(cls["id"])
    relation_pairs = [
        ("proof_claim:C-228", "proof_claim:C-234"),
        ("proof_claim:C-234", "proof_claim:C-240"),
        ("proof_claim:C-232", "proof_claim:C-237"),
        ("proof_claim:C-237", "proof_claim:C-242"),
    ]
    for left, right in relation_pairs:
        by_id[left]["related_ids"].append(right)
        by_id[right]["related_ids"].append(left)
    for item in items:
        item["class_ids"].sort()
        item["related_ids"].sort()


def validate_items(items: list[dict[str, Any]]) -> dict[str, Any]:
    ids = [item["id"] for item in items]
    duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
    if duplicates:
        raise ValueError(f"DUPLICATE_CANONICAL_ITEMS:{duplicates}")
    bad_axes = []
    for item in items:
        if set(item["axes"]) != set(AXES):
            bad_axes.append(item["id"])
        elif any(not item["axes"][axis] for axis in AXES):
            bad_axes.append(item["id"])
    if bad_axes:
        raise ValueError(f"AXIS_CELL_REMAINDER:{bad_axes}")
    return {"duplicate_ids": 0, "axis_cell_remainder": 0, "canonical_items": len(items)}


def build_core(reverse: bool = False) -> tuple[dict[str, Any], dict[str, Any], str]:
    sources = source_set()
    proof, packages = proof_items(reverse=reverse)
    proof_axis = {item["source_id"]: item["axes"] for item in proof if item["namespace"] == "proof_package"}
    items = proof + state_items(packages, proof_axis, reverse=reverse) + machine_items(reverse=reverse)
    classes = class_definitions()
    apply_classes(items, classes)
    items.sort(key=lambda item: item["id"])
    checks = validate_items(items)
    namespace_counts = dict(sorted(Counter(item["namespace"] for item in items).items()))
    source_snapshot = sha256(json_bytes(sources))
    vocabulary = {
        axis: sorted({UNKNOWN, NOT_APPLICABLE} | {item["axes"][axis] for item in items})
        for axis in AXES
    }
    selected_successor = {
        "id": "state_record:A-G-HOTT-SYNTAX-001",
        "task": "R3_R4_GODEL_RETURN_001",
        "reason": (
            "The newly reduced internalisation family has published qualified defenses.  The exact HoTT "
            "syntax/representability route remains outside that class, is explicitly required by goal.md, "
            "and its CompletionProperty remains FULL_R4_OPEN for a new machine slice."
        ),
        "preserves_parallel_frontiers": [
            "state_record:A-ORACLE-MODALITIES-SOURCE-QUALIFICATION-001",
            "machine_task:MS-TASK-L3-INTERVAL-COMPLETION-001",
            "state_record:A-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001",
        ],
    }
    if selected_successor["id"] not in {item["id"] for item in items}:
        raise ValueError("SELECTED_SUCCESSOR_MISSING")
    ce_map = {
        "schema_version": MAP_SCHEMA,
        "status": "CE_MAP_V1_COMPLETE_WITH_SCOPE",
        "input_cutoff": {"state_revision": 149, "latest_claim": "C-243", "machine_import_snapshot": validate_import()[0]["snapshot_id"]},
        "scope": (
            "Closed-world registration of the named revision-149 STATE records (excluding sessions), frozen "
            "proof packages and their claims, and the imported machine-overview tasks/cases/evaluations/runs/reviews."
        ),
        "non_goals": [
            "No open-world exhaustiveness claim.",
            "No claim that UNKNOWN cells are mathematically equivalent.",
            "No proof that HoTT is inconsistent or that a reality-relative paradox has been completed.",
            "No novelty claim for published internalisation no-go results.",
        ],
        "axes": list(AXES),
        "axis_vocabulary": vocabulary,
        "source_snapshot": source_snapshot,
        "sources": sources,
        "input_denominator": {"total": len(items), "by_namespace": namespace_counts},
        "integrity": {**checks, "input_remainder": 0, "unmapped_input_ids": []},
        "classes": classes,
        "selected_successor": selected_successor,
        "items": items,
    }
    unclassified_rows = [
        {
            "id": item["id"],
            "source_id": item["source_id"],
            "namespace": item["namespace"],
            "unknown_axes": item["unknown_axes"],
            "assignment": item["assignment"],
            "source_paths": item["source_paths"],
        }
        for item in items
        if item["unknown_axes"]
    ]
    unclassified = {
        "schema_version": UNCLASSIFIED_SCHEMA,
        "source_snapshot": source_snapshot,
        "status": "PRESERVED_REMAINDER",
        "count": len(unclassified_rows),
        "entries": unclassified_rows,
    }
    report = render_report(ce_map, unclassified)
    return ce_map, unclassified, report


def render_report(ce_map: dict[str, Any], unclassified: dict[str, Any]) -> str:
    counts = ce_map["input_denominator"]["by_namespace"]
    rows = "\n".join(f"| `{key}` | {value} |" for key, value in counts.items())
    classes = "\n".join(
        f"| `{cls['id']}` | {len(cls['members'])} | `{cls['reduction_status']}` | {cls['representative']} |"
        for cls in ce_map["classes"]
    )
    unknown_by_axis = Counter(
        axis for entry in unclassified["entries"] for axis in entry["unknown_axes"]
    )
    unknown_rows = "\n".join(f"| `{axis}` | {unknown_by_axis.get(axis, 0)} |" for axis in AXES)
    preview = "\n".join(
        f"- `{entry['id']}`：{', '.join(entry['unknown_axes'])}"
        for entry in unclassified["entries"][:25]
    ) or "- 无"
    successor = ce_map["selected_successor"]
    return f"""# CE-MAP v1：HoTT 非现实性悖论机器统观八轴映射

状态：`{ce_map['status']}`  
输入快照：`{ce_map['source_snapshot']}`  
冻结截止：STATE revision 149 / C-243 / machine import `{ce_map['input_cutoff']['machine_import_snapshot']}`

## 这份完成状态表示什么

本次把 {ce_map['input_denominator']['total']} 个具名输入逐一登记到八轴张量。每个轴都有受控值，无法从当前证据确定的值明确写成 `UNKNOWN`，与数学对象无关的记录明确写成 `NOT_APPLICABLE`。输入 remainder 为 0；`UNCLASSIFIED.json` 保留 {unclassified['count']} 个仍含未知轴的 item。

`CE_MAP_V1_COMPLETE_WITH_SCOPE` 只表示 revision 149 的具名分母已被完整登记。它不表示开放世界已经穷尽，也不表示 HoTT 中已经找到新的矛盾或最终现实相对悖论。

## 输入分母

| 命名空间 | 数量 |
|---|---:|
{rows}

## internalisation 归约结果

| class | 成员数 | 归约强度 | 代表 |
|---|---:|---|---|
{classes}

`CE-CLASS-UNQUALIFIED-INTERNALISATION-001` 把 C-228–C-240 中“取消输入资格后把能力提升到 local/open/context-uniform 使用”的共同机制只计作一个搜索家族。它没有把三个论文结果说成同一个定理：consumer、观察结果、完成性质和 framework 没有保持，因此其状态是 pattern reduction，而不是完整任务保真的双向归约。

crisp/global 限制、identity-R 消融、degenerate fibrancy + transport 与 empty-context extension 被登记为一个 defense pattern。它们都通过显式支付保住来源中的真实任务，但支付内容不同，仍须逐 consumer 检查。

## 未决轴

| 轴 | 含 `UNKNOWN` 的 item 数 |
|---|---:|
{unknown_rows}

前 25 项如下；全量见 `UNCLASSIFIED.json`：

{preview}

## 下一机器切片

选择 `{successor['task']}`，对应 `{successor['id']}`。{successor['reason']}

Oracle、physical time/时空连续性、ambient R2 与现实桥梁仍保留为并行返回口，不被 internalisation class 吞掉。

## 复核入口

```bash
python3 -B scripts/audit/build_ce_map.py validate
python3 -B scripts/audit/build_ce_map.py query --id proof_claim:C-234
python3 -B scripts/audit/build_ce_map.py list-unclassified
python3 -B scripts/audit/test_ce_map.py
```
"""


def bundle_bytes() -> dict[str, bytes]:
    forward = build_core(reverse=False)
    reversed_build = build_core(reverse=True)
    forward_bytes = (json_bytes(forward[0]), json_bytes(forward[1]), forward[2].encode())
    reverse_bytes = (json_bytes(reversed_build[0]), json_bytes(reversed_build[1]), reversed_build[2].encode())
    if forward_bytes != reverse_bytes:
        raise ValueError("ORDER_INVARIANCE_FAILED")
    repeated = build_core(reverse=False)
    repeat_bytes = (json_bytes(repeated[0]), json_bytes(repeated[1]), repeated[2].encode())
    if forward_bytes != repeat_bytes:
        raise ValueError("REPEATED_BUILD_NOT_IDENTICAL")
    names = ("CE-MAP.json", "UNCLASSIFIED.json", "REPORT.md")
    result = dict(zip(names, forward_bytes, strict=True))
    ce_map, unclassified, _ = forward
    receipt = {
        "schema_version": RECEIPT_SCHEMA,
        "status": "CE_MAP_V1_COMPLETE_WITH_SCOPE",
        "source_snapshot": ce_map["source_snapshot"],
        "input_count": ce_map["input_denominator"]["total"],
        "output_item_count": len(ce_map["items"]),
        "input_remainder": ce_map["integrity"]["input_remainder"],
        "axis_cell_remainder": ce_map["integrity"]["axis_cell_remainder"],
        "duplicate_ids": ce_map["integrity"]["duplicate_ids"],
        "unclassified_count": unclassified["count"],
        "determinism": {
            "forward_vs_reverse_input_order_byte_identical": True,
            "same_process_repeat_byte_identical": True,
            "separate_process_rebuild_byte_identical": True,
            "canonical_json_sort_keys": True,
        },
        "negative_controls": {
            "deleted_known_input": "scripts/audit/test_ce_map.py::test_deleting_one_known_input_fails_validation",
            "deleted_axis_cell": "scripts/audit/test_ce_map.py::test_removing_one_axis_fails_validation",
        },
        "outputs": {name: {"bytes": len(data), "sha256": sha256(data)} for name, data in result.items()},
        "scope": "Named revision-149 input registration only; open-world and mathematical completeness are not claimed.",
    }
    result["RECEIPT.json"] = json_bytes(receipt)
    return result


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_name, path)
    except BaseException:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def write_bundle(output_dir: Path) -> dict[str, Any]:
    expected = bundle_bytes()
    for name in ("CE-MAP.json", "UNCLASSIFIED.json", "REPORT.md", "RECEIPT.json"):
        atomic_write(output_dir / name, expected[name])
    return validate_bundle(output_dir)


def validate_bundle(
    output_dir: Path,
    ce_map_override: Path | None = None,
    require_current_sources: bool = False,
) -> dict[str, Any]:
    names = ("CE-MAP.json", "UNCLASSIFIED.json", "REPORT.md", "RECEIPT.json")
    paths = {name: output_dir / name for name in names}
    if ce_map_override is not None:
        paths["CE-MAP.json"] = ce_map_override
    for name, path in paths.items():
        if not path.is_file():
            raise ValueError(f"OUTPUT_MISSING:{name}:{path}")
    actual = {name: path.read_bytes() for name, path in paths.items()}
    ce_map = json.loads(actual["CE-MAP.json"])
    if ce_map.get("schema_version") != MAP_SCHEMA:
        raise ValueError("CE_MAP_SCHEMA_MISMATCH")
    ids = [item["id"] for item in ce_map.get("items", [])]
    duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
    if duplicates:
        raise ValueError(f"INPUT_DENOMINATOR_DUPLICATES:{duplicates}")
    denominator = ce_map.get("input_denominator", {})
    if denominator.get("total") != len(ids):
        raise ValueError(f"INPUT_DENOMINATOR_COUNT:{denominator.get('total')}:{len(ids)}")
    actual_namespace_counts = dict(sorted(Counter(item.get("namespace") for item in ce_map["items"]).items()))
    if denominator.get("by_namespace") != actual_namespace_counts:
        raise ValueError("INPUT_NAMESPACE_COUNTS")
    integrity = ce_map.get("integrity", {})
    if integrity.get("input_remainder") != 0 or integrity.get("canonical_items") != len(ids):
        raise ValueError("INPUT_REMAINDER_OR_CANONICAL_COUNT")
    for item in ce_map["items"]:
        if set(item.get("axes", {})) != set(AXES) or any(not item["axes"].get(axis) for axis in AXES):
            raise ValueError(f"AXIS_CELL_MISSING:{item.get('id')}")
        expected_unknown = [axis for axis in AXES if item["axes"][axis] == UNKNOWN]
        if item.get("unknown_axes") != expected_unknown:
            raise ValueError(f"UNKNOWN_AXIS_PROJECTION:{item.get('id')}")
    if sha256(json_bytes(ce_map.get("sources", []))) != ce_map.get("source_snapshot"):
        raise ValueError("EMBEDDED_SOURCE_SNAPSHOT_HASH")
    by_id = {item["id"]: item for item in ce_map["items"]}
    for cls in ce_map.get("classes", []):
        if cls.get("representative") not in cls.get("members", []):
            raise ValueError(f"CLASS_REPRESENTATIVE:{cls.get('id')}")
        for member in cls.get("members", []):
            if member not in by_id or cls["id"] not in by_id[member].get("class_ids", []):
                raise ValueError(f"CLASS_MEMBERSHIP:{cls.get('id')}:{member}")
    unclassified = json.loads(actual["UNCLASSIFIED.json"])
    if unclassified.get("schema_version") != UNCLASSIFIED_SCHEMA:
        raise ValueError("UNCLASSIFIED_SCHEMA_MISMATCH")
    expected_unclassified_ids = [item["id"] for item in ce_map["items"] if item["unknown_axes"]]
    actual_unclassified_ids = [entry["id"] for entry in unclassified.get("entries", [])]
    if unclassified.get("count") != len(actual_unclassified_ids) or actual_unclassified_ids != expected_unclassified_ids:
        raise ValueError("UNCLASSIFIED_PROJECTION_MISMATCH")
    receipt = json.loads(actual["RECEIPT.json"])
    if receipt.get("schema_version") != RECEIPT_SCHEMA:
        raise ValueError("RECEIPT_SCHEMA_MISMATCH")
    if receipt.get("input_count") != len(ids) or receipt.get("output_item_count") != len(ids):
        raise ValueError("RECEIPT_INPUT_COUNT_MISMATCH")
    if receipt.get("unclassified_count") != unclassified["count"]:
        raise ValueError("RECEIPT_UNCLASSIFIED_COUNT_MISMATCH")
    for name in ("CE-MAP.json", "UNCLASSIFIED.json", "REPORT.md"):
        output_identity = receipt["outputs"][name]
        if output_identity["sha256"] != sha256(actual[name]) or output_identity["bytes"] != len(actual[name]):
            raise ValueError(f"RECEIPT_HASH_MISMATCH:{name}")

    source_drift = []
    for row in ce_map["sources"]:
        path = ROOT / row["path"]
        if not path.is_file():
            source_drift.append({"path": row["path"], "reason": "MISSING"})
            continue
        data = path.read_bytes()
        if len(data) != row["bytes"] or sha256(data) != row["sha256"]:
            source_drift.append({"path": row["path"], "reason": "CHANGED"})
    if require_current_sources and source_drift:
        raise ValueError(f"SOURCE_EVOLUTION:{source_drift}")
    exact_rebuild = False
    if not source_drift:
        expected = bundle_bytes()
        mismatches = [name for name in names if actual[name] != expected[name]]
        if mismatches:
            raise ValueError(f"NONCANONICAL_OUTPUT:{mismatches}")
        exact_rebuild = True
    return {
        "status": "VALID" if not source_drift else "VALID_WITH_SOURCE_EVOLUTION",
        "ce_map_status": ce_map["status"],
        "source_snapshot": ce_map["source_snapshot"],
        "items": len(ids),
        "unclassified": unclassified["count"],
        "classes": len(ce_map["classes"]),
        "selected_successor": ce_map["selected_successor"]["task"],
        "determinism": receipt["determinism"],
        "exact_rebuild": exact_rebuild,
        "source_drift": source_drift,
    }


def load_validated(output_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    validate_bundle(output_dir)
    return (
        json.loads((output_dir / "CE-MAP.json").read_text(encoding="utf-8")),
        json.loads((output_dir / "UNCLASSIFIED.json").read_text(encoding="utf-8")),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    build = sub.add_parser("build")
    build.add_argument("--write", action="store_true")
    build.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    validate = sub.add_parser("validate")
    validate.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    validate.add_argument("--ce-map", type=Path)
    validate.add_argument("--require-current-sources", action="store_true")
    query = sub.add_parser("query")
    query.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    query.add_argument("--id", required=True)
    unclassified = sub.add_parser("list-unclassified")
    unclassified.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "build":
            if args.write:
                result = write_bundle(args.output_dir.resolve())
            else:
                data = bundle_bytes()
                ce_map = json.loads(data["CE-MAP.json"])
                result = {
                    "status": "DRY_RUN",
                    "writes": False,
                    "items": len(ce_map["items"]),
                    "source_snapshot": ce_map["source_snapshot"],
                }
        elif args.command == "validate":
            result = validate_bundle(
                args.output_dir.resolve(),
                args.ce_map.resolve() if args.ce_map else None,
                args.require_current_sources,
            )
        elif args.command == "query":
            ce_map, _ = load_validated(args.output_dir.resolve())
            matches = [
                item for item in ce_map["items"] if item["id"] == args.id or item["source_id"] == args.id
            ]
            result = {"status": "FOUND" if matches else "NOT_FOUND", "count": len(matches), "items": matches}
            if not matches:
                print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
                return 1
        else:
            _, unclassified = load_validated(args.output_dir.resolve())
            result = unclassified
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "INVALID", "error": str(exc)}, ensure_ascii=False, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
