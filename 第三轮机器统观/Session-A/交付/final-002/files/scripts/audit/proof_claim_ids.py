"""Shared exact claim identifiers for proof registration; IDs do not assign evidence levels."""
from __future__ import annotations
import re

CLAIM_ID = re.compile(r"(?:C-\d+|CAND-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)\Z")
PROOF_ID = re.compile(r"MP-[A-Za-z0-9-]+\Z")

def expand_claim_ids(value: object) -> list[str]:
    if not isinstance(value, str):
        raise ValueError("CLAIM_IDS_NOT_STRING")
    compact = value.strip()
    if CLAIM_ID.fullmatch(compact):
        return [compact]
    interval = re.fullmatch(r"C-(\d+)\s*(?:\.\.|–)\s*C-(\d+)", compact)
    if interval:
        left, right = interval.groups()
        start, stop = int(left), int(right)
        if stop < start:
            raise ValueError(f"CLAIM_IDS_REVERSED:{value}")
        width = max(len(left), len(right))
        return [f"C-{n:0{width}d}" for n in range(start, stop + 1)]
    parts = [p.strip() for p in compact.split(",")]
    if parts and all(CLAIM_ID.fullmatch(p) for p in parts):
        if len(parts) != len(set(parts)):
            raise ValueError(f"CLAIM_IDS_DUPLICATE:{value}")
        return parts
    raise ValueError(f"CLAIM_IDS_UNPARSEABLE:{value}")

def matrix_identity_lines(data: bytes) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    for line in data.decode("utf-8").splitlines():
        if not line.startswith("|"):
            continue
        identity = line.strip().strip("|").split("|", 1)[0].strip().strip("` ")
        if CLAIM_ID.fullmatch(identity) or PROOF_ID.fullmatch(identity):
            found.setdefault(identity, []).append(line)
    return found
