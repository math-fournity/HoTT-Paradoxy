# usage: python3 gui_qa_digest.py <outdir>   (reads audit/GUI-SYNTH-REDO/qa; writes <branch>.digest.md)
"""Verbatim subset of QA docs: per turn, the User block, the LAST Codex block, and changed-file paths.
No rewriting: text is copied byte-for-byte from the QA docs (which are machine exports of the rollouts)."""
import json, os, re, sys
QA = "/Volumes/D/HoTT_AI_HANDOFF_20260911/audit/GUI-SYNTH-REDO/qa"
OUT = sys.argv[1]
ranges = {  # branch -> (first_doc, last_doc) ; trunk dev-08 only from 76 (after first child fork at 75)
    "dev-08": (76, 127),
}
def split_blocks(text):
    body = text.split("\n---\n", 1)[1] if text.startswith("---") else text
    parts = re.split(r"(?m)^(## User|## Codex|### Files changed in this reply)\s*$", body)
    blocks, cur = [], None
    for p in parts:
        if p in ("## User", "## Codex", "### Files changed in this reply"):
            cur = [p, ""]; blocks.append(cur)
        elif cur is not None:
            cur[1] += p
    return blocks
stats = {}
for br in sorted(os.listdir(QA)):
    d = os.path.join(QA, br)
    if not os.path.isdir(d) or br.startswith("_"):
        continue
    docs = sorted(f for f in os.listdir(d) if re.fullmatch(r"\d{4}\.md", f))
    lo, hi = ranges.get(br, (1, 10**6))
    out = [f"# {br} — verbatim digest (User + last Codex + changed files), docs {lo}..{min(hi, len(docs))}\n"]
    s = dict(docs=0, total=0, user=0, final=0, mid=0, mid_blocks=0)
    for f in docs:
        n = int(f[:4])
        if not (lo <= n <= hi):
            continue
        t = open(os.path.join(d, f), encoding="utf-8").read()
        s["docs"] += 1; s["total"] += len(t.encode())
        bl = split_blocks(t)
        users = [b[1].strip() for b in bl if b[0] == "## User"]
        codex = [b[1].strip() for b in bl if b[0] == "## Codex"]
        files = [b[1] for b in bl if b[0].startswith("### Files")]
        u = "\n\n".join(re.sub(r"<environment_context>.*?</environment_context>", "[env]", x, flags=re.S) for x in users)
        fin = codex[-1] if codex else ""
        s["user"] += len(u.encode()); s["final"] += len(fin.encode())
        s["mid"] += sum(len(x.encode()) for x in codex[:-1]); s["mid_blocks"] += max(0, len(codex) - 1)
        paths = sorted(set(re.sub(r"^/Users/aurolafly/\.codex/worktrees/", "WT/", m) for m in re.findall(r"`(/[^`]+)`", "".join(files))))
        out.append(f"\n\n========== {br}/{f}  (codex blocks: {len(codex)}, changed files: {len(paths)}) ==========\n")
        out.append("### USER\n" + (u or "(none)") + "\n")
        out.append("### FINAL\n" + (fin or "(none)") + "\n")
        if paths:
            out.append("### FILES\n" + "\n".join(paths[:60]) + ("\n…(+%d more)" % (len(paths) - 60) if len(paths) > 60 else "") + "\n")
    open(os.path.join(OUT, f"{br}.digest.md"), "w", encoding="utf-8").write("".join(out))
    stats[br] = s
print(json.dumps(stats, indent=1))
