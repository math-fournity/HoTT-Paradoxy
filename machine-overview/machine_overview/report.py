"""Human-readable report assembled from the receipts (never from memory)."""
from __future__ import annotations

from pathlib import Path

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
    lines = [
        f"# Machine-overview calibration report: {case['case_id']}",
        "",
        f"- generated_at_utc: {utc_now()}",
        f"- case: `{case_path}` (sha256 `{sha256_file(case_path)}`)",
        f"- search run: `{search_run_path}` (run `{search_run['run_id']}`, {search_run['exit_reason']})",
        f"- coordinator: `{search_run['coordinator_version']}` / registry `{search_run['registry_id']}`",
        f"- profile: `{search_run['profile']['profile_id']}` ({search_run['profile']['profile_status']})",
        "",
        "## What was searched",
        "",
        f"- declared grammar: `{case['grammar']['path']}` (sha256 `{case['grammar']['sha256']}`)",
        f"- delay atoms: {search_run['statistics']['delay_atoms']}; contexts: {search_run['statistics']['contexts']}; "
        f"pair-context checks: {search_run['statistics']['pair_context_checks']}",
        f"- separations seen in the declared space: {search_run['statistics']['separations_seen']}; "
        f"reduced distinct witnesses: {len(search_run['witnesses'])}",
        f"- search answer-independence: order permutation set-equal = "
        f"`{search_run['order_independence_check']['order_independent_set_equal']}`; "
        f"grammar mutation removes deadline kind = "
        f"`{search_run['grammar_sensitivity_check']['mutated_contains_deadline_kind']}`",
        f"- known calibration benchmark present in the discovered set: "
        f"`{search_run['calibration_match'].get('status')}` ({search_run['calibration_match'].get('claim_refs')})",
        "",
        "## Candidates (reduced, in discovery order)",
        "",
        "| witness | pair | context | separated observation | kind |",
        "|---|---|---|---|---|",
    ]
    for witness in search_run["witnesses"][:12]:
        pair = witness["pair"]
        lines.append(
            f"| {witness['witness_id']} | ({_value_text(pair['left'])}, {_value_text(pair['right'])}) | "
            f"{_ops_text(witness['ops'])} | {_value_text(witness['left_observation'])} ≠ "
            f"{_value_text(witness['right_observation'])} | {witness['separation_kind']} |"
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
        "## Native kernel verification",
        "",
    ]
    if not verify_runs:
        lines.append("- no verify run yet")
    for verify, verify_path in verify_runs:
        witness = witness_by_id.get(verify["witness_id"], {})
        lines += [
            f"### `{verify['run_id']}` (witness {verify['witness_id']})",
            "",
            f"- proof origin: `{verify['proof_origin']}`; status: `{verify['status']}`",
            f"- statement: ({_value_text(verify['statement']['pair']['left'])}, "
            f"{_value_text(verify['statement']['pair']['right'])}) under "
            f"{_ops_text(verify['statement']['ops'])}",
            f"- target sha256: `{verify['target_text_hash']}`",
        ]
        for kernel in verify["kernel_runs"]:
            lines.append(
                f"- kernel `{kernel['label']}`: exit {kernel['exit_code']}, status `{kernel['status']}`, "
                f"expectation met `{kernel['expectation_met']}`"
                + (f", replay match `{kernel.get('replay_match')}`" if "replay_match" in kernel else "")
            )
        lines += [
            f"- related existing claims: {verify['claim_relation']['related_claims']}",
            f"- registers new claim: `{verify['claim_relation']['registers_new_claim']}`",
            "",
        ]
    for review, review_path in reviews:
        lines += [
            f"## Correspondence review `{review['review_id']}` (witness {review['witness_id']})",
            "",
            f"- review: `{review_path}`",
            f"- mechanism: {review['mechanism_summary']}",
            f"- conclusion: `{review['conclusion']['correspondence_status']}`; "
            f"task preservation `{review['conclusion']['task_preservation']}`; "
            f"reality correspondence `{review['conclusion']['reality_correspondence']}`",
            "",
        ]
        for item in review["checklist"]:
            lines.append(f"- {item['item']}: `{item['status']}`")
        lines.append("")
    lines += [
        "## Evidence boundaries",
        "",
        "- This is a calibration instance of a mechanism already machine-proved in the pinned package "
        f"({case.get('claim_refs', [])}); it is not registered as a new mathematical claim.",
        "- The verified statement is a ground instance inside the declared grammar; nothing here quantifies "
        "over all HoTT models, implementations, or physical time.",
        "- Exploration receipts live under `machine-overview/runs/`; the formal-evidence contract "
        "(`HoTT/formal`, `HoTT/verification/runs`, `HoTT/CLAIM_EVIDENCE_MATRIX.md`) is untouched.",
        "",
    ]
    write_text(output_path, "\n".join(lines))
    return output_path
