#!/usr/bin/env python3
"""S7-c: extract C-NNN claim rows (N in a range) from HoTT/CLAIM_EVIDENCE_MATRIX.md and
formal-package CLAIM*.md files on many git refs; report collisions (same ID, different text)."""
import subprocess, re, sys, json, hashlib, collections
REPO = "/Volumes/D/HoTT_AI_HANDOFF_20260911"
LO, HI = 357, 420
def git(*a):
    return subprocess.run(["git", "-C", REPO, *a], capture_output=True, text=True).stdout
refs = sys.argv[1:]
rowre = re.compile(r"^\|\s*`?C-(\d{3})`?\s*\|\s*(.+?)\s*\|")
proofre = re.compile(r"^\|\s*`(MP-[A-Z0-9-]+)`\s*\|\s*`?(C-[\d–\-C, ]+)`?")
out = {}
for ref in refs:
    tip = git("rev-parse", "--short", ref).strip()
    mat = git("show", f"{ref}:HoTT/CLAIM_EVIDENCE_MATRIX.md")
    claims = {}
    for line in mat.splitlines():
        m = rowre.match(line)
        if m and LO <= int(m.group(1)) <= HI:
            claims.setdefault(int(m.group(1)), m.group(2)[:150])
    proofs = collections.defaultdict(list)
    for line in mat.splitlines():
        m = proofre.match(line)
        if m:
            for n in re.findall(r"C-(\d{3})", m.group(2)):
                if LO <= int(n) <= HI: proofs[int(n)].append(m.group(1))
    # package CLAIM files mentioning ids
    files = [f for f in git("ls-tree", "-r", "--name-only", ref, "HoTT/formal").splitlines() if re.search(r"CLAIM[^/]*\.md$", f)]
    pk = collections.defaultdict(set)
    for f in files:
        txt = git("show", f"{ref}:{f}")
        for n in set(re.findall(r"\bC-(\d{3})\b", txt)):
            if LO <= int(n) <= HI: pk[int(n)].add(f.split("/")[2] if f.count("/")>=3 else f)
    out[ref] = {"tip": tip, "claims": claims, "proofs": {k: sorted(set(v)) for k,v in proofs.items()}, "pkgs": {k: sorted(v) for k,v in pk.items()}}
json.dump(out, open(sys.stdout.fileno(), "w", closefd=False), ensure_ascii=False, indent=0)
