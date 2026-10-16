#!/usr/bin/env python3
"""Check the source citations in the community-audit documents against the sources.

The two community documents quote formal statements and cite them as
`path:line`. This tool checks, mechanically, the declaration layer of those
documents against the proof layer:

  1. LINE CITATIONS. Every `HoTT/...agda|lean:NN[, NN][–NN]` citation (and every
     short `File.agda:NN` citation that names a unique file under HoTT/formal)
     must point at a line that exists. The source line is printed so that a human
     can see what is actually there (the printed listing is the evidence; the
     automatic rule below only catches gross drift).
       - Automatic rule: within a table row, the cited line must contain at
         least one identifier that the row names in backticks. A citation that
         fails the rule is reported as WARN, not as a failure, because a row may
         legitimately cite a line by another identifier.
  2. VERBATIM QUOTES. In a table row that cites source files, every backticked
     fragment that looks like a formal statement (contains ` : `, `≡`, `≃`, `→`,
     `:=`, or starts with `theorem `/`def `/`record `) must occur in one of the
     cited files, after whitespace is collapsed. A fragment may use `…` to elide
     a stretch of the source; the pieces on either side of each `…` must then
     occur in order. A fragment that is not found is a FAIL.

It checks existence and quotation, not meaning: that a quoted statement says what
the prose says is a question for the reader (see 13-外部复核请求.md).

Usage:
    python3 -B Cloud-Opus审计并补完GLM/tools/check_doc_citations.py [--quiet] [doc ...]

With no documents it checks the two community-audit documents. Exit status is 0
when there is no FAIL, 1 otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_DOCS = [
    "docs/社区审计提交/01-芝诺悖论的幽灵.md",
    "docs/社区审计提交/02-罗素悖论的幽灵.md",
]

FULL = re.compile(r"(HoTT/[^\s`：:;；、（）()]+\.(?:agda|lean))[:：]\s*([0-9][0-9,，–\- ]*)")
FULLPATH = re.compile(r"(HoTT/[^\s`：:;；、（）()]+\.(?:agda|lean))")
SHORT = re.compile(r"`([A-Za-z0-9_]+\.(?:agda|lean))[:：]\s*([0-9][0-9,，–\- ]*)`")
SHORTNAME = re.compile(r"`([A-Za-z0-9_]+\.(?:agda|lean))")
TICK = re.compile(r"`([^`\n]+)`")
WORD = re.compile(r"[^\s()\[\]{}:=,，;；∙·|`]+")


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def looks_formal(fragment: str) -> bool:
    return (
        " : " in fragment or "≡" in fragment or ":=" in fragment or "→" in fragment
        or "≃" in fragment
        or fragment.startswith(("theorem ", "def ", "record ", "postulate "))
    )


def parse_ranges(spec: str) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for part in re.split(r"[,，]", spec):
        part = part.strip()
        if not part:
            continue
        m = re.match(r"(\d+)\s*[–\-]\s*(\d+)$", part)
        if m:
            out.append((int(m.group(1)), int(m.group(2))))
        elif part.isdigit():
            out.append((int(part), int(part)))
    return out


def in_order(pieces: list[str], text: str) -> bool:
    pos = 0
    for piece in pieces:
        piece = piece.strip()
        if not piece:
            continue
        found = text.find(piece, pos)
        if found < 0:
            return False
        pos = found + len(piece)
    return True


def main(argv: list[str]) -> int:
    quiet = "--quiet" in argv
    docs = [a for a in argv if not a.startswith("--")] or DEFAULT_DOCS

    sources: dict[Path, list[str]] = {}
    normalized: dict[Path, str] = {}
    by_name: dict[str, list[Path]] = {}
    for p in sorted((ROOT / "HoTT/formal").rglob("*")):
        if p.suffix in (".agda", ".lean"):
            lines = p.read_text(encoding="utf-8").splitlines()
            sources[p] = lines
            normalized[p] = norm("\n".join(lines))
            by_name.setdefault(p.name, []).append(p)

    fails = 0
    warns = 0
    citations = 0
    fragments = 0
    fragments_ok = 0
    seen: set[tuple[Path, int, int]] = set()

    for doc_rel in docs:
        doc = Path(doc_rel) if Path(doc_rel).is_absolute() else ROOT / doc_rel
        rows = doc.read_text(encoding="utf-8").splitlines()
        for lineno, row in enumerate(rows, 1):
            cited: list[tuple[Path, str]] = []
            for m in FULL.finditer(row):
                cited.append((ROOT / m.group(1), m.group(2)))
            for m in SHORT.finditer(row):
                cands = by_name.get(m.group(1), [])
                if len(cands) == 1:
                    cited.append((cands[0], m.group(2)))
                else:
                    print(f"FAIL  {doc_rel}:{lineno}  short citation `{m.group(1)}` names "
                          f"{len(cands)} files")
                    fails += 1

            row_words: set[str] = set()
            for t in TICK.finditer(row):
                frag = t.group(1)
                if frag.startswith("HoTT/") or frag.endswith((".agda", ".lean")):
                    continue
                for w in WORD.findall(frag):
                    if len(w) >= 3:
                        row_words.add(w)

            for path, spec in cited:
                if path not in sources:
                    print(f"FAIL  {doc_rel}:{lineno}  cited file does not exist: "
                          f"{path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}")
                    fails += 1
                    continue
                src = sources[path]
                for a, b in parse_ranges(spec):
                    if (path, a, b) in seen:
                        continue
                    seen.add((path, a, b))
                    citations += 1
                    if a > len(src) or b > len(src):
                        print(f"FAIL  {path.name}:{a}–{b} is beyond the end of the file "
                              f"({len(src)} lines)  [{doc_rel}:{lineno}]")
                        fails += 1
                        continue
                    shown = [src[a - 1]] if a == b else [src[a - 1], "...", src[b - 1]]
                    text = " | ".join(s.strip()[:110] for s in shown)
                    ends = [src[a - 1]] if a == b else [src[a - 1], src[b - 1]]
                    hit = any(w in line for line in ends for w in row_words)
                    if not hit:
                        warns += 1
                    if not quiet or not hit:
                        tag = "ok  " if hit else "WARN"
                        rng = f"{a}" if a == b else f"{a}–{b}"
                        print(f"{tag}  {path.name}:{rng}  ->  {text}")

            if cited:
                files = {p for p, _ in cited if p in normalized}
                for m in SHORTNAME.finditer(row):
                    files.update(by_name.get(m.group(1), []))
                for m in FULLPATH.finditer(row):
                    p = ROOT / m.group(1)
                    if p in normalized:
                        files.add(p)
                for t in TICK.finditer(row):
                    frag = t.group(1)
                    if frag.startswith("HoTT/") or frag.endswith((".agda", ".lean")):
                        continue
                    if not looks_formal(frag):
                        continue
                    fragments += 1
                    pieces = [norm(x) for x in frag.split("…")]
                    if any(in_order(pieces, normalized[p]) for p in files):
                        fragments_ok += 1
                    else:
                        fails += 1
                        print(f"FAIL  {doc_rel}:{lineno}  quoted statement is not verbatim in the "
                              f"cited file(s): {norm(frag)[:140]}")

    print()
    print(f"line citations checked: {citations}  (WARN: {warns})")
    print(f"formal-looking quotes checked: {fragments}  verbatim: {fragments_ok}")
    print("RESULT:", "PASS" if fails == 0 else f"FAIL ({fails})")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
