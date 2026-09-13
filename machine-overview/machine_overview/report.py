"""Human-readable report assembled from the receipts (never from memory)."""
from __future__ import annotations

from pathlib import Path

from .model import value_from_json
from .util import read_json, sha256_file, utc_now, write_text


def _value_text(row: dict) -> str:
    kind = row["kind"]
    if kind == "omega":
        return "ω"
    if kind == "ret":
        return f"ret {row['n']} {str(row['value']).lower()}"
    if kind == "none":
        return "none"
    if kind == "some":
        return f"some {str(row['value']).lower()}"
    return str(row)


def _ops_text(ops: list[dict]) -> str:
    parts = []
    for op in ops:
        if op["kind"] == "race_left":
            parts.append(f"race(□, {_value_text(op['partner'])})")
        elif op["kind"] == "race_right":
            parts.append(f"race({_value_text(op['partner'])}, □)")
        elif op["kind"] == "bind":
            left = _value_text(op["continuation"]["true"])
            right = _value_text(op["continuation"]["false"])
            parts.append(f"bind(□, λ{{true↦{left}; false↦{right}}})")
        elif op["kind"] == "deadline":
            parts.append(f"deadline({op['k']}, □)")
    return " → ".join(parts) if parts else "□"


def explain_case(
    repo_root: Path,
    *,
    case: dict,
    case_path: Path,
    search_run: dict,
    search_run_path: Path,
    verify_runs: list[tuple[dict, Path]],
    reviews: list[tuple[dict, Path]],
    output_path: Path,
) -> Path:
    witness_by_id = {item["witness_id"]: item for item in search_run["witnesses"]}
    statistics = search_run["statistics"]
    accepted = [item for item in verify_runs if item[0]["status"] == "NATIVE_CHECKED_CALIBRATION_INSTANCE"]
    odd_runs = [item for item in verify_runs if item[0]["status"] != "NATIVE_CHECKED_CALIBRATION_INSTANCE"]
    lines = [
        f"# Machine-overview calibration report: {case['case_id']}",
        "",
        f"- generated_at_utc: {utc_now()}",
        f"- case: `{case_path}` (revision {case['revision']}, sha256 `{sha256_file(case_path)}`)",
        f"- search run: `{search_run_path}` (run `{search_run['run_id']}`, {search_run['exit_reason']})",
        f"- coordinator: `{search_run['coordinator_version']}` / registry `{search_run['registry_id']}`",
        f"- profile: `{search_run['profile']['profile_id']}` ({search_run['profile']['profile_status']})",
        "",
        "## What was searched",
        "",
        f"- declared grammar: `{case['grammar']['path']}` (sha256 `{case['grammar']['sha256']}`)",
        f"- delay atoms: {statistics['delay_atoms']}; contexts planned: {statistics['contexts']}; "
        f"contexts examined: {statistics.get('contexts_examined')}",
        f"- pair-context checks: {statistics['pair_context_checks']} executed of "
        f"{statistics.get('checks_planned')} planned",
        f"- separations seen: {statistics['separations_seen']}; reduced distinct witnesses: "
        f"{len(search_run['witnesses'])}",
        f"- complete-within-declared-grammar: `{statistics['complete_within_declared_grammar']}`; "
        f"truncated: `{statistics['truncated']}` (checks budget `{statistics.get('checks_budget_exhausted')}`, "
        f"context budget `{statistics.get('context_budget_exhausted')}`, witness capture "
        f"`{statistics.get('witness_capture_truncated')}`)",
        f"- search answer-independence: order permutation set-equal = "
        f"`{search_run['order_independence_check']['order_independent_set_equal']}`; "
        f"grammar mutation removes deadline kind = "
        f"`{search_run['grammar_sensitivity_check']['mutated_contains_deadline_kind']}`",
        f"- known calibration benchmark present in the discovered set: "
        f"`{search_run['calibration_match'].get('status')}` ({search_run['calibration_match'].get('claim_refs')})",
        "",
        "## Candidates (reduced, in discovery order)",
        "",
        "| witness | pair | context | separated observation | kind | ast sha256 |",
        "|---|---|---|---|---|---|",
    ]
    for witness in search_run["witnesses"][:12]:
        pair = witness["pair"]
        lines.append(
            f"| {witness['witness_id']} | ({_value_text(pair['left'])}, {_value_text(pair['right'])}) | "
            f"{_ops_text(witness['ops'])} | {_value_text(witness['left_observation'])} ≠ "
            f"{_value_text(witness['right_observation'])} | {witness['separation_kind']} | "
            f"`{witness.get('ast_sha256', 'n/a')[:12]}…` |"
        )
    lines += [
        "",
        "## Controls",
        "",
        f"- positive control (`{search_run['controls']['positive']['control']}`, claim ref "
        f"{search_run['controls']['positive']['claim_ref']}): preserved = "
        f"`{search_run['controls']['positive']['preserved']}`",
        f"- negative control (`{search_run['controls']['negative']['control']}`): separated = "
        f"`{search_run['controls']['negative']['separated']}`, expectation met = "
        f"`{search_run['controls']['negative']['expectation_met']}`",
        "",
        "## Native kernel verification (accepted runs)",
        "",
    ]
    if not accepted:
        lines.append("- no accepted verify run yet")
    for verify, verify_path in accepted:
        binding = verify.get("source_search_run") or {}
        lines += [
            f"### `{verify['run_id']}` (witness {verify['witness_id']})",
            "",
            f"- proof origin: `{verify['proof_origin']}`; status: `{verify['status']}`; attempt: "
            f"`{verify.get('attempt', {}).get('attempt')}`",
            f"- source search run: `{binding.get('run_id')}` (sha256 `{binding.get('sha256')}`)",
            f"- candidate AST sha256: `{verify.get('candidate_ast_sha256')}`; target freeze: "
            f"`{(verify.get('target_freeze') or {}).get('status')}`",
            f"- statement: ({_value_text(verify['statement']['pair']['left'])}, "
            f"{_value_text(verify['statement']['pair']['right'])}) under "
            f"{_ops_text(verify['statement']['ops'])}",
            f"- target sha256: `{verify['target_text_hash']}`",
            f"- replay: `{(verify.get('replay') or {}).get('classification')}`",
        ]
        for kernel in verify["kernel_runs"]:
            lines.append(
                f"- kernel `{kernel['label']}`: exit {kernel['exit_code']}, status `{kernel['status']}`, "
                f"expectation met `{kernel['expectation_met']}`, diagnostic `{kernel.get('diagnostic')}`"
            )
        lines += [
            f"- related existing claims: {verify['claim_relation']['related_claims']}",
            f"- registers new claim: `{verify['claim_relation']['registers_new_claim']}`",
            "",
        ]
    if odd_runs:
        lines += ["## Other verify attempts (kept as evidence)", ""]
        for verify, verify_path in odd_runs:
            lines += [
                f"- `{verify['run_id']}` (witness {verify.get('witness_id')}): status `{verify['status']}`; "
                f"kernels: " + ", ".join(
                    f"{kernel['label']}={kernel['status']}({kernel['exit_code']})" for kernel in verify["kernel_runs"]
                ),
            ]
        lines.append("")
    for review, review_path in reviews:
        lines += [
            f"## Correspondence review `{review['review_id']}` (witness {review['witness_id']})",
            "",
            f"- review: `{review_path}`",
            f"- mechanism: {review['mechanism_summary']}",
            f"- conclusion: `{review['conclusion']['correspondence_status']}`; "
            f"task preservation `{review['conclusion']['task_preservation']}`; "
            f"reality correspondence `{review['conclusion']['reality_correspondence']}`",
            "- review checks: " + ", ".join(
                f"{item['id']}={item['status']}" for item in review.get("review_checks", [])
            ),
            "",
        ]
    lines += [
        "## Evidence boundaries",
        "",
        "- This is a calibration instance of a mechanism already machine-proved in the pinned package "
        f"({case.get('claim_refs', [])}); it is not registered as a new mathematical claim.",
        "- The verified statement is a ground instance inside the declared grammar; nothing here quantifies "
        "over all HoTT models, implementations, or physical time.",
        "- Every verify run is bound to (case revision, search run hash, witness AST hash, frozen target hash); "
        "exploration receipts live under `machine-overview/runs/` and the formal-evidence contract "
        "(`HoTT/formal`, `HoTT/verification/runs`, `HoTT/CLAIM_EVIDENCE_MATRIX.md`) is untouched.",
        "",
    ]
    write_text(output_path, "\n".join(lines))
    return output_path
