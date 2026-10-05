#!/usr/bin/env python3
"""Check the deliberately restricted GZ-005 cctt source-input profile.

This is not a parser or a termination prover for cctt.  It removes cctt
comments and string literals, rejects holes, ``undefined``, imports, and a
cycle in the top-level-definition reference graph, then reports the exact
reasons.  It is only the project-defined precondition of
``ClosedProofAccept_cctt``; the pinned upstream checker remains a separate
required component.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_']*")


def erase_comments_and_strings(source: str) -> str:
    """Preserve offsets/newlines while blanking comments and string literals."""
    out: list[str] = []
    i = 0
    nested_comment = 0
    in_string = False
    while i < len(source):
        if nested_comment:
            if source.startswith("{-", i):
                nested_comment += 1
                out.extend("  ")
                i += 2
            elif source.startswith("-}", i):
                nested_comment -= 1
                out.extend("  ")
                i += 2
            else:
                out.append("\n" if source[i] == "\n" else " ")
                i += 1
        elif in_string:
            if source[i] == "\\" and i + 1 < len(source):
                out.extend("  ")
                i += 2
            elif source[i] == '"':
                out.append(" ")
                in_string = False
                i += 1
            else:
                out.append("\n" if source[i] == "\n" else " ")
                i += 1
        elif source.startswith("--", i):
            end = source.find("\n", i)
            if end < 0:
                out.extend(" " * (len(source) - i))
                break
            out.extend(" " * (end - i))
            out.append("\n")
            i = end + 1
        elif source.startswith("{-", i):
            nested_comment = 1
            out.extend("  ")
            i += 2
        elif source[i] == '"':
            out.append(" ")
            in_string = True
            i += 1
        else:
            out.append(source[i])
            i += 1
    if nested_comment:
        raise ValueError("UNTERMINATED_BLOCK_COMMENT")
    if in_string:
        raise ValueError("UNTERMINATED_STRING")
    return "".join(out)


def top_level_chunks(source: str) -> list[str]:
    """Split declarations at semicolons that are outside (), [] and {}."""
    chunks: list[str] = []
    start = 0
    paren = bracket = brace = 0
    for index, char in enumerate(source):
        if char == "(":
            paren += 1
        elif char == ")":
            paren -= 1
        elif char == "[":
            bracket += 1
        elif char == "]":
            bracket -= 1
        elif char == "{":
            brace += 1
        elif char == "}":
            brace -= 1
        elif char == ";" and paren == bracket == brace == 0:
            chunks.append(source[start:index])
            start = index + 1
    residue = source[start:].strip()
    if residue:
        raise ValueError("TOP_LEVEL_DECLARATION_MISSING_SEMICOLON")
    if min(paren, bracket, brace) < 0 or any((paren, bracket, brace)):
        raise ValueError("UNBALANCED_DELIMITERS")
    return chunks


def definition_bodies(chunks: list[str]) -> dict[str, str]:
    definitions: dict[str, str] = {}
    for chunk in chunks:
        if not chunk.strip() or re.match(r"^\s*(higher\s+)?inductive\b", chunk):
            continue
        if ":=" not in chunk:
            continue
        left, body = chunk.split(":=", 1)
        match = IDENTIFIER.search(left)
        if not match:
            raise ValueError("TOP_LEVEL_DEFINITION_NAME_NOT_FOUND")
        name = match.group(0)
        if name in {"let", "case"}:
            raise ValueError("TOP_LEVEL_DEFINITION_NAME_AMBIGUOUS")
        if name in definitions:
            raise ValueError(f"DUPLICATE_TOP_LEVEL_DEFINITION:{name}")
        definitions[name] = body
    return definitions


def cyclic_definition_names(definitions: dict[str, str]) -> list[str]:
    names = set(definitions)
    graph = {
        name: {token for token in IDENTIFIER.findall(body) if token in names}
        for name, body in definitions.items()
    }
    visiting: set[str] = set()
    visited: set[str] = set()
    cycles: set[str] = set()

    def visit(name: str, stack: list[str]) -> None:
        if name in visiting:
            cycles.update(stack[stack.index(name):])
            return
        if name in visited:
            return
        visiting.add(name)
        for child in graph[name]:
            visit(child, [*stack, name])
        visiting.remove(name)
        visited.add(name)

    for name in graph:
        visit(name, [])
    return sorted(cycles)


def assess(path: Path) -> dict[str, object]:
    source = path.read_text(encoding="utf-8")
    errors: list[str] = []
    try:
        code = erase_comments_and_strings(source)
        chunks = top_level_chunks(code)
        definitions = definition_bodies(chunks)
    except ValueError as exc:
        return {"path": str(path), "accepted": False, "reasons": [str(exc)]}

    if "?" in code:
        errors.append("HOLE_TOKEN")
    for forbidden in ("undefined", "import"):
        if re.search(rf"\b{re.escape(forbidden)}\b", code):
            errors.append(f"FORBIDDEN_TOKEN:{forbidden}")
    cycles = cyclic_definition_names(definitions)
    if cycles:
        errors.append("TOP_LEVEL_RECURSION_CYCLE:" + ",".join(cycles))
    return {
        "path": str(path),
        "accepted": not errors,
        "reasons": errors,
        "definition_names": sorted(definitions),
        "top_level_definition_count": len(definitions),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    result = assess(args.source)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["accepted"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
