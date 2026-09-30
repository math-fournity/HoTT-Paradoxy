#!/usr/bin/env python3
"""Read-only checks for the root README logical document (index + shards).

It checks declarations, not meaning:

  1. snapshot - the ``readme-snapshot:v1`` block in README.md matches the
                owners: STATE revision, core generation and KC count, and the
                projection generations of 方向追踪.md and 全景视野.md;
  2. ids      - every DIR-/OUT-/KC-/CN-/CG001-C-/run/session/STATE-record id
                named in the README exists in its owner;
  3. quotes   - every quote marked 【用户原话，KC-NNNNNN…】 is verbatim in that
                KC entry of 核心认知.md (fragments may be joined by "……"),
                and every quote marked 【用户判定…】 is verbatim in rulings.md;
  4. routes   - the route map shard (file name contains 路线地图) names every
                direction row of 方向追踪.md;
  5. paths    - backticked repository paths and relative Markdown links exist.

Exit status: 0 when everything passes; 1 on any hard failure (missing id,
quote mismatch, route gap, missing path, malformed or missing snapshot);
3 when the only problem is a stale snapshot (the README is older than its
owners: re-check chapters 004-006 and update the stamps).

The script never writes files and never uses the network.

Usage:
    python3 -B scripts/readme/verify_readme_snapshot.py [--readme PATH] [--root PATH] [--json]

``--readme`` points at a README index (default: <root>/README.md); links in a
copy placed elsewhere are resolved as if the copy were at the repository root,
which lets negative controls run on modified copies.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

DEFAULT_ROOT = Path(__file__).resolve().parents[2]

SHARD_ROW = re.compile(r"^\|\s*\d{3}\s*\|\s*\[[^\]]*\]\(<([^>]+)>\)")
SNAPSHOT = re.compile(r"<!--\s*readme-snapshot:v1\s*(.*?)-->", re.S)
SNAPSHOT_KEYS = (
    "snapshot_date", "state_revision", "core_generation", "core_kc_count",
    "direction_projection", "panorama_projection",
)

ID_PATTERNS = {
    "DIR": re.compile(r"(?<![A-Za-z0-9_-])(DIR-[A-Z0-9]+(?:-[A-Z0-9]+)*)(?![A-Za-z0-9_-])"),
    "OUT": re.compile(r"(?<![A-Za-z0-9_-])(OUT-[A-Z0-9]+(?:-[A-Z0-9]+)*)(?![A-Za-z0-9_-])"),
    "KC": re.compile(r"(?<![A-Za-z0-9_-])(KC-\d{6})(?![0-9])"),
    "CN": re.compile(r"(?<![A-Za-z0-9_-])(CN-\d{3})(?![0-9])"),
    "CG001": re.compile(r"(?<![A-Za-z0-9_-])(CG001-C-\d{2})(?![0-9])"),
    "RUN": re.compile(r"(?<![A-Za-z0-9_-])(\d{8}-[A-Z0-9]+(?:-[A-Z0-9]+)*-\d{2})(?![A-Za-z0-9_-])"),
    "SESSION": re.compile(r"(?<![A-Za-z0-9_-])(S-[A-Z0-9]+-\d{8}-[A-Z0-9-]*[A-Z0-9])(?![A-Za-z0-9_-])"),
    "STATE": re.compile(
        r"(?<![A-Za-z0-9_-])((?:A|G|I)-[A-Z0-9]+(?:-[A-Z0-9]+)+|MO3-[A-Z0-9]+(?:-[A-Z0-9]+)*|R4-[A-Z0-9]+(?:-[A-Z0-9]+)*)(?![A-Za-z0-9_-])"
    ),
}

QUOTE_MARK = re.compile(r"【用户原话，(KC-\d{6})[^】]*】")
VERDICT_MARK = re.compile(r"【用户判定[^】]*】")
CORNER = re.compile(r"「(.+?)」")
BACKTICK = re.compile(r"`([^`\n]+)`")
MDLINK = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")
LINESPEC = re.compile(r"[:：]\d[\d,–\-]*$")
WS = re.compile(r"\s+")


def norm(text: str) -> str:
    return WS.sub("", text)


def read_logical(index: Path) -> tuple[str, list[Path]]:
    """Return the concatenated text of an index and its shards, and the shards."""
    text = index.read_text(encoding="utf-8")
    shards = []
    for line in text.splitlines():
        m = SHARD_ROW.match(line)
        if m:
            shards.append(index.parent / m.group(1))
    parts = [text] + [s.read_text(encoding="utf-8") for s in shards]
    return "\n".join(parts), shards


def kc_texts(core: str) -> dict[str, str]:
    out: dict[str, str] = {}
    current = None
    buf: list[str] = []
    inside = False
    for line in core.splitlines():
        head = re.match(r"^### (KC-\d{6}) ", line)
        if head:
            current = head.group(1)
            continue
        if current and line.startswith("~~~text"):
            inside, buf = True, []
            continue
        if inside and line.startswith("~~~"):
            out[current] = "\n".join(buf)
            inside, current = False, None
            continue
        if inside:
            buf.append(line)
    return out


def projection_generation(text: str) -> str | None:
    m = re.search(r"^projection_generation:\s*(\S+)", text, re.M)
    return m.group(1) if m else None


def check_quotes(path: Path, text: str, kcs: dict[str, str], rulings: str) -> tuple[list[str], int]:
    problems = []
    checked = 0
    lines = text.splitlines()
    for i, line in enumerate(lines):
        marks = [(m.start(), m.group(1)) for m in QUOTE_MARK.finditer(line)]
        marks += [(m.start(), "VERDICT") for m in VERDICT_MARK.finditer(line)]
        marks.sort()
        if not marks:
            continue
        segments = [(m.start(), m.group(1)) for m in CORNER.finditer(line)]
        pieces: list[tuple[str, str]] = []
        if segments:
            for pos, seg in segments:
                owner = None
                for mpos, mid in marks:
                    if mpos < pos:
                        owner = mid
                if owner:
                    pieces.append((owner, seg))
        elif line.strip().endswith("】") and not line.lstrip().startswith("|"):
            # a marker that ends its line introduces a block quote on the following lines
            owner = marks[-1][1]
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            block = []
            while j < len(lines) and lines[j].startswith(">"):
                block.append(lines[j][1:].strip())
                j += 1
            if not block:
                problems.append(f"{path.name}:{i + 1}: marker without a quote")
            for q in block:
                if q:
                    pieces.append((owner, q))
        for owner, quote in pieces:
            source = rulings if owner == "VERDICT" else kcs.get(owner)
            if source is None:
                problems.append(f"{path.name}:{i + 1}: {owner} has no text in 核心认知.md")
                continue
            for frag in quote.split("……"):
                f = norm(frag)
                if f:
                    checked += 1
                if f and f not in norm(source):
                    label = "rulings.md" if owner == "VERDICT" else owner
                    problems.append(f"{path.name}:{i + 1}: not verbatim in {label}: {frag[:40]}")
    return problems, checked


def path_exists(root: Path, token: str) -> bool:
    """A path exists, or names one shard by its number (`方向追踪/005` for `方向追踪/005 - ….md`)."""
    target = root / token
    if target.exists():
        return True
    parent, last = target.parent, target.name
    if parent.is_dir() and re.fullmatch(r"\d{3}", last):
        return len([p for p in parent.iterdir() if p.name.startswith(last + " - ")]) == 1
    return False


def check_paths(files: list[tuple[Path, str, Path]], root: Path) -> list[str]:
    problems = []
    top = {p.name for p in root.iterdir()}
    for real, text, virtual_dir in files:
        in_fence = False
        for n, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for token in BACKTICK.findall(line):
                token = LINESPEC.sub("", token.strip())
                if any(ch in token for ch in "<>{}*…") or token.startswith("-"):
                    continue
                first = token.split("/")[0]
                if first not in top:
                    continue
                if not path_exists(root, token.rstrip("/")):
                    problems.append(f"{real.name}:{n}: missing path `{token}`")
            for target in MDLINK.findall(line):
                target = target.strip()
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                if re.match(r"[a-z]+://", target) or target.startswith("#"):
                    continue
                target = unquote(target.split("#", 1)[0])
                if target and not (virtual_dir / target).exists():
                    problems.append(f"{real.name}:{n}: missing link target {target}")
    return problems


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=str(DEFAULT_ROOT))
    ap.add_argument("--readme", default=None)
    ap.add_argument("--json", action="store_true", help="print a JSON summary")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    index = Path(args.readme).resolve() if args.readme else root / "README.md"
    readme_text, shards = read_logical(index)
    files = [(index, index.read_text(encoding="utf-8"), root)]
    for s in shards:
        rel = s.relative_to(index.parent)
        files.append((s, s.read_text(encoding="utf-8"), (root / rel).parent))

    state = json.loads((root / ".codex/research/hott/STATE.json").read_text(encoding="utf-8"))
    state_raw = (root / ".codex/research/hott/STATE.json").read_text(encoding="utf-8")
    core = (root / "核心认知.md").read_text(encoding="utf-8")
    direction, _ = read_logical(root / "方向追踪.md")
    panorama, _ = read_logical(root / "全景视野.md")
    rulings = (root / "rulings.md").read_text(encoding="utf-8")
    idx003 = (root / ".claude/总索引/003 - 工作单元与证据登记.md").read_text(encoding="utf-8")
    idx004 = (root / ".claude/总索引/004 - 思考与发现登记.md").read_text(encoding="utf-8")

    report: dict[str, object] = {"readme": str(index), "shards": [s.name for s in shards]}
    hard: list[str] = []
    stale: list[str] = []

    # 1. snapshot
    m = SNAPSHOT.search(files[0][1])
    snap: dict[str, str] = {}
    if not m:
        hard.append("snapshot: no readme-snapshot:v1 block in the index")
    else:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                snap[k.strip()] = v.strip()
        missing = [k for k in SNAPSHOT_KEYS if k not in snap]
        if missing:
            hard.append("snapshot: missing keys " + ", ".join(missing))
        expected = {
            "state_revision": str(state.get("revision")),
            "core_generation": state["current_core"]["generation"],
            "core_kc_count": str(state["current_core"]["kc_count"]),
            "direction_projection": projection_generation(direction),
            "panorama_projection": projection_generation(panorama),
        }
        for k, v in expected.items():
            if k in snap and snap[k] != v:
                stale.append(f"snapshot: {k} is {snap[k]}, owner says {v}")
    report["snapshot"] = snap

    # 2. ids
    owners = {
        "DIR": set(re.findall(r"^\|\s*`(DIR-[A-Z0-9-]+)`", direction, re.M)),
        "OUT": set(re.findall(r"^\|\s*`(OUT-[A-Z0-9-]+)`", panorama, re.M)),
        "KC": set(re.findall(r"^### (KC-\d{6}) ", core, re.M)),
        "CN": set(re.findall(r"^\|\s*(CN-\d{3})\s*\|", idx004, re.M)),
        "CG001": set(re.findall(r"`(CG001-C-\d{2})`", idx003)),
    }
    runs_root = root / "HoTT/verification/runs"
    sessions_root = root / ".codex/research/hott/sessions"
    counts: dict[str, int] = {}
    listed: dict[str, list[str]] = {}
    for kind, pat in ID_PATTERNS.items():
        found = set(pat.findall(readme_text))
        counts[kind] = len(found)
        listed[kind] = sorted(found)
        for ident in sorted(found):
            if kind in owners:
                ok = ident in owners[kind]
            elif kind == "RUN":
                ok = (runs_root / ident).is_dir()
            elif kind == "SESSION":
                ok = (sessions_root / ident).is_dir()
            else:  # STATE-like record ids
                ok = ident in state_raw or any((root / ".codex/research/hott").glob(ident + "*"))
            if not ok:
                hard.append(f"ids: {kind} {ident} not found in its owner")
    report["id_counts"] = counts
    report["ids"] = listed

    # 3. quotes
    kcs = kc_texts(core)
    quote_problems: list[str] = []
    fragments = 0
    for real, text, _ in files:
        probs, n = check_quotes(real, text, kcs, rulings)
        quote_problems += probs
        fragments += n
    report["quote_fragments_checked"] = fragments
    hard += ["quotes: " + p for p in quote_problems]
    report["quote_markers"] = sum(
        len(QUOTE_MARK.findall(t)) + len(VERDICT_MARK.findall(t)) for _, t, _ in files
    )

    # 4. routes
    route_files = [t for real, t, _ in files if "路线地图" in real.name]
    if not route_files:
        hard.append("routes: no shard whose file name contains 路线地图")
    else:
        named = set(ID_PATTERNS["DIR"].findall(route_files[0]))
        gap = sorted(owners["DIR"] - named)
        for g in gap:
            hard.append(f"routes: direction {g} is not on the route map")
        report["routes"] = {"owner_directions": len(owners["DIR"]), "on_map": len(owners["DIR"] & named)}

    # 5. paths and links
    hard += ["paths: " + p for p in check_paths(files, root)]

    report["hard_failures"] = hard
    report["stale"] = stale
    status = 1 if hard else (3 if stale else 0)
    report["status"] = {0: "PASS", 1: "FAIL", 3: "STALE"}[status]

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print(f"README: {index} ({len(shards)} shards)")
        print("snapshot:", ", ".join(f"{k}={snap.get(k)}" for k in SNAPSHOT_KEYS))
        print("ids checked:", ", ".join(f"{k}={v}" for k, v in counts.items()))
        print("quote markers:", report["quote_markers"], "| fragments checked:", report["quote_fragments_checked"])
        if "routes" in report:
            r = report["routes"]
            print(f"route map: {r['on_map']}/{r['owner_directions']} directions")
        for s in stale:
            print("STALE", s)
        for h in hard:
            print("FAIL", h)
        print("RESULT", report["status"])
    return status


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
