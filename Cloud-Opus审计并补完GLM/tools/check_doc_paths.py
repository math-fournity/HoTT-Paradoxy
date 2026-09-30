#!/usr/bin/env python3
"""Check that the paths and links named in the community-audit documents exist.

What it checks (only existence; it does not judge content):
  1. every backticked token that starts with a known repo-relative prefix and
     looks like a file path (line/column suffixes such as `:52` are stripped);
  2. every relative Markdown link target `[text](target)` (external http(s)
     links and pure anchors are skipped; `%20`-style escapes and `<...>`
     wrappers are decoded; a `#fragment` is stripped).

A path that is not a file in the repository is reported as missing. Tokens that
contain a placeholder (`{`, `<`, `…`, `*`) are skipped because they name a
family of files, not one file.

Usage:
    python3 -B Cloud-Opus审计并补完GLM/tools/check_doc_paths.py [doc ...]

With no arguments it checks the two community-audit documents, their README,
and the entry documents that point to them. Exit status 0 when nothing is
missing, 1 otherwise.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]

DEFAULT_DOCS = [
    "docs/社区审计提交/README.md",
    "docs/社区审计提交/01-芝诺悖论的幽灵.md",
    "docs/社区审计提交/02-罗素悖论的幽灵.md",
    "README/001 - 当前入口与关键文件.md",
    "Cloud-Opus审计并补完GLM/README.md",
    "Cloud-Opus审计并补完GLM/15-入核与登记记录.md",
]

PREFIXES = (
    "HoTT/", "Cloud-Opus", "docs/", ".claude/", ".codex/", "sources/",
    "GLM-5.3-Flash/", "Terra对", "scripts/", "audit/", "核心认知", "扩展认知",
    "方向追踪", "全景视野", "README/", "第三轮机器统观/",
)
FILE_SUFFIXES = (
    ".md", ".json", ".agda", ".lean", ".py", ".sh", ".txt", ".log", ".yml",
    ".yaml", ".agda-lib", ".toml",
)

BACKTICK = re.compile(r"`([^`\n]+)`")
MDLINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")
LINESPEC = re.compile(r"[:：]\d[\d,–\-]*$")


def looks_like_path(token: str) -> bool:
    if not token.startswith(PREFIXES):
        return False
    if any(ch in token for ch in "{<…*"):
        return False
    return True


def candidate_from_backtick(token: str) -> str | None:
    token = token.strip()
    if not looks_like_path(token):
        return None
    # `path:52`, `path:52–64`, `path（说明）`, `path, other` -> take the first path
    token = token.split("（")[0].split("(")[0].strip()
    token = LINESPEC.sub("", token)
    token = re.split(r"[;；,，]\s", token)[0].strip()
    if " " in token and not token.endswith(FILE_SUFFIXES):
        return None
    if not (token.endswith(FILE_SUFFIXES) or token.endswith("/")):
        # bare names such as `核心认知.md` are files; bare directory-like
        # tokens without a suffix are not checked (they may be ids or tags)
        return None
    return token


def resolve_link(doc: Path, target: str) -> Path | None:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
        return None
    target = unquote(target.split("#", 1)[0])
    if not target:
        return None
    return (doc.parent / target).resolve()


def check(doc_rel: str) -> tuple[list[tuple[str, str]], int]:
    """Return (missing items, number of paths and links actually checked)."""
    doc = ROOT / doc_rel
    if not doc.exists():
        return [(doc_rel, "<the document itself is missing>")], 0
    text = doc.read_text(encoding="utf-8")
    missing: list[tuple[str, str]] = []
    checked = 0
    for m in BACKTICK.finditer(text):
        cand = candidate_from_backtick(m.group(1))
        if cand is None:
            continue
        checked += 1
        p = ROOT / cand
        if not p.exists():
            missing.append((doc_rel, f"`{m.group(1)}`"))
    for m in MDLINK.finditer(text):
        p = resolve_link(doc, m.group(1))
        if p is None:
            continue
        checked += 1
        if not p.exists():
            missing.append((doc_rel, f"link -> {m.group(1)}"))
    return missing, checked


def main(argv: list[str]) -> int:
    docs = argv or DEFAULT_DOCS
    total_missing: list[tuple[str, str]] = []
    total_checked = 0
    for d in docs:
        miss, n = check(d)
        status = "OK" if not miss else f"{len(miss)} missing"
        print(f"{d}: {status} ({n} paths and links checked)")
        total_missing.extend(miss)
        total_checked += n
    if total_missing:
        print()
        for d, tok in total_missing:
            print(f"MISSING  {d}  {tok}")
        return 1
    print(f"all {total_checked} named paths and relative links exist")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
