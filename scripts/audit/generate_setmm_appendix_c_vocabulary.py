#!/usr/bin/env python3
"""Generate the source-bound vocabulary layer of an Appendix-C companion map.

This program deliberately does *not* claim to construct a ZF-internal
``mFS`` witness for the complete ``set.mm`` database.  Its narrower job is to
read one pinned raw database, extract the actual variable declarations and
their ``$f`` type assignments, and generate a Lean data declaration consumed
by the M-level vocabulary-extension proof.

The generated Lean file is a machine-managed derived artifact.  Its source
identity is the SHA-256 below; editing it by hand breaks the source contract.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


SCHEMA = "setmm-appendix-c-vocabulary/v1"
EXPECTED_SHA256 = "d8420798bcedcd04fcfe337736e2609b66914c76f8f2db967fa79673d5026b2a"
EXPECTED_VARIABLE_COUNT = 355
EXPECTED_CONSTANT_COUNT = 1474
EXPECTED_TYPE_COUNTS = {"wff": 61, "setvar": 139, "class": 155}
TYPE_CONSTRUCTORS = {"wff": "wff", "setvar": "setvar", "class": "class"}


def strip_comments(text: str) -> str:
    """Replace each non-nested Metamath ``$( ... $)`` comment by whitespace."""

    result: list[str] = []
    cursor = 0
    while True:
        start = text.find("$(", cursor)
        if start < 0:
            result.append(text[cursor:])
            return "".join(result)
        result.append(text[cursor:start])
        end = text.find("$)", start + 2)
        if end < 0:
            raise ValueError("UNTERMINATED_METAMATH_COMMENT")
        result.append(" ")
        cursor = end + 2


def parse_vocabulary(text: str) -> tuple[list[str], list[str], dict[str, str]]:
    """Return ordered variables, constants, and a variable-to-type mapping."""

    tokens = strip_comments(text).split()
    variables: list[str] = []
    constants: list[str] = []
    var_types: dict[str, str] = {}
    index = 0

    while index < len(tokens):
        marker = tokens[index]
        if marker not in {"$c", "$v", "$d", "$f", "$e", "$a", "$p"}:
            index += 1
            continue

        index += 1
        payload: list[str] = []
        while index < len(tokens) and tokens[index] != "$.":
            payload.append(tokens[index])
            index += 1
        if index == len(tokens):
            raise ValueError(f"UNTERMINATED_METAMATH_STATEMENT:{marker}")
        index += 1

        if marker == "$v":
            variables.extend(payload)
        elif marker == "$c":
            constants.extend(payload)
        elif marker == "$f":
            if len(payload) != 2:
                raise ValueError(f"MALFORMED_F_STATEMENT:{payload!r}")
            typecode, variable = payload
            previous = var_types.setdefault(variable, typecode)
            if previous != typecode:
                raise ValueError(
                    f"INCONSISTENT_VARIABLE_TYPE:{variable}:{previous}:{typecode}"
                )

    ordered_variables: list[str] = []
    seen: set[str] = set()
    for variable in variables:
        if variable not in seen:
            seen.add(variable)
            ordered_variables.append(variable)

    undeclared_type_assignments = set(var_types).difference(ordered_variables)
    if undeclared_type_assignments:
        raise ValueError(
            "TYPE_ASSIGNMENT_FOR_UNDECLARED_VARIABLE:"
            + ",".join(sorted(undeclared_type_assignments))
        )
    missing_assignments = set(ordered_variables).difference(var_types)
    if missing_assignments:
        raise ValueError(
            "DECLARED_VARIABLE_WITHOUT_F_ASSIGNMENT:"
            + ",".join(sorted(missing_assignments))
        )
    unsupported = set(var_types.values()).difference(TYPE_CONSTRUCTORS)
    if unsupported:
        raise ValueError("UNSUPPORTED_VARIABLE_TYPECODE:" + ",".join(sorted(unsupported)))

    return ordered_variables, constants, var_types


def lean_string(value: str) -> str:
    """JSON string syntax is also valid for the ASCII token strings emitted here."""

    return json.dumps(value, ensure_ascii=False)


def render_lean(
    source_sha256: str, variables: list[str], var_types: dict[str, str]
) -> str:
    constructors = [f"  | v{index:03d}" for index in range(len(variables))]
    type_equations = [
        f"  | .v{index:03d} => .{TYPE_CONSTRUCTORS[var_types[variable]]}"
        for index, variable in enumerate(variables)
    ]
    lexeme_equations = [
        f"  | .v{index:03d} => {lean_string(variable)}"
        for index, variable in enumerate(variables)
    ]
    return "\n".join(
        [
            "/-",
            "  MACHINE_MANAGED_CANONICAL",
            "  generator: scripts/audit/generate_setmm_appendix_c_vocabulary.py",
            f"  schema: {SCHEMA}",
            f"  source_sha256: {source_sha256}",
            "  This file encodes only the pinned raw database vocabulary and $f",
            "  assignments. It is not an internal mFS witness, a proof relation, or",
            "  an adequacy theorem for set.mm.",
            "-/",
            "",
            "namespace SetMMAppendixCGenerated",
            "",
            "inductive RawType where",
            "  | wff",
            "  | setvar",
            "  | class",
            "deriving DecidableEq, Repr",
            "",
            "inductive RawVar where",
            *constructors,
            "deriving DecidableEq, Repr",
            "",
            "def sourceSha256 : String := " + lean_string(source_sha256),
            f"def sourceVariableCount : Nat := {len(variables)}",
            "",
            "def rawVarType : RawVar → RawType",
            *type_equations,
            "",
            "def rawVarLexeme : RawVar → String",
            *lexeme_equations,
            "",
            "end SetMMAppendixCGenerated",
            "",
        ]
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    raw = args.input.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"SETMM_SHA256_MISMATCH:{digest}")

    variables, constants, var_types = parse_vocabulary(raw.decode("utf-8"))
    type_counts = Counter(var_types.values())
    if len(variables) != EXPECTED_VARIABLE_COUNT:
        raise SystemExit(f"UNEXPECTED_VARIABLE_COUNT:{len(variables)}")
    if len(set(constants)) != EXPECTED_CONSTANT_COUNT:
        raise SystemExit(f"UNEXPECTED_CONSTANT_COUNT:{len(set(constants))}")
    if dict(type_counts) != EXPECTED_TYPE_COUNTS:
        raise SystemExit(f"UNEXPECTED_TYPE_COUNTS:{dict(type_counts)}")

    output = render_lean(digest, variables, var_types)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    result = {
        "schema_version": SCHEMA,
        "input": str(args.input),
        "input_sha256": digest,
        "output": str(args.output),
        "output_sha256": hashlib.sha256(output.encode("utf-8")).hexdigest(),
        "unique_variable_count": len(variables),
        "unique_constant_count": len(set(constants)),
        "variable_type_counts": dict(sorted(type_counts.items())),
        "scope": (
            "Vocabulary extraction for an Appendix-C companion construction; "
            "does not establish a ZF-internal mFS witness, mPPSt/mThm adequacy, "
            "Prv, a diagonal sentence, or a completion bridge."
        ),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
